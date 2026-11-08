# Caching Template Library — Geeklog 2.2.2 reference

Geeklog's Caching Template Library (CTL) provides the `Template` class used by Core code, themes, and plugins to generate HTML from template files or in-memory views. This reference describes the features confirmed in the [Geeklog 2.2.2 template class](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/classes/template.class.php), with practical source-level examples. Test changes in an isolated site before deployment.

## What CTL does

CTL separates the data prepared by PHP from the markup in `.thtml` files. Depending on configuration, it compiles template source into PHP, stores compiled output in a cache directory, and recompiles when the underlying file changes. A view is a template supplied as a string through `set_view()`, rather than read from a file.

Template conditions control presentation only. **They do not replace server-side authorization, HTML escaping, or input validation.** Never let untrusted users supply arbitrary executable template code.

## Finding and overriding template files

`set_root($root)` accepts a directory or an ordered array of directories. It normalizes the input to an array, skips missing directories, and preserves the order of existing directories. The first matching file is selected by the file-lookup routine. This allows an override directory to precede a fallback directory.

For existing Geeklog code, prefer the Core's template helper routines and conventions for locating theme-specific plugin templates. Check the installed release and active theme before assuming any hard-coded layout path.

**Source-level example — choose an override before the fallback:**

```php
$root = array(
    $themeOverrideDirectory,
    $pluginDefaultTemplateDirectory
);
$template = new Template($root);
$template->set_file('panel', 'panel.thtml');
$template->set_var('heading', htmlspecialchars($heading, ENT_QUOTES, 'UTF-8'));
$html = $template->parse('rendered_panel', 'panel');
```

Both directory variables must be valid paths supplied by trusted application code. The named template must exist in at least one directory. This example illustrates the public method sequence and requires testing in the consuming plugin.

## Public template methods

The signatures below are present in `system/classes/template.class.php` at tag `v2.2.2`.

| Method | Purpose |
| --- | --- |
| `__construct($root = array('.'), $unknowns = 'remove')` | Create a template; set root directories and unknown-variable policy |
| `set_root($root)` | Set one or more lookup roots |
| `set_file($varName, $filename = '')` | Register a template file |
| `set_view($varName, $view = '')` | Register template source provided as a string |
| `set_block($parent, $varName, $name = '')` | Register a named block from a parent |
| `set_var($varName, $value = '', $append = false, $nocache = false)` | Assign or append replacement variables; optionally exclude them from instance caching |
| `get_var($varName)`, `get_vars()` | Read one or several assigned values |
| `clear_var($varName)`, `unset_var($varName)` | Empty a variable or remove it |
| `parse($target, $varName, $append = false)` | Parse a template and assign the rendered result to a variable |
| `pparse($target, $varName, $append = false)` | Parse, finish and print the result |
| `finish($str)` | Apply configured final processing |

The method signatures are **source-checked**. A PHP method's existence alone does not prove that every historical calling pattern is safe or supported by a particular plugin.

## Template variables and escaping

A replacement variable is written as `{heading}`. The 2.2.2 parser accepts letters, digits, underscores, periods, dashes and square brackets within variable names.

```html
<h2>{heading:s}</h2>
<a href="{destination:u}">Open the page</a>
<p>{summary:t120}</p>
```

The tagged implementation recognizes these modifiers (which may be combined in the parser):

| Modifier | Tagged-source behavior | Usage caution |
| --- | --- | --- |
| `:u` | `urlencode()` | Encodes a value; it does not validate a URL scheme or destination |
| `:s` | `htmlspecialchars()` | Escapes HTML-sensitive characters, subject to PHP's current defaults |
| `:h` | `strip_tags()` | Removes markup, **not** a complete XSS or HTML-sanitization policy |
| `:tN` | `substr(..., 0, N)` | Truncates bytes, potentially cutting multibyte characters |

In PHP, escape according to the **destination context** (HTML text, attribute, URL, JavaScript). Do not apply HTML escaping blindly to an entire completed markup fragment. Use application-side escaping and URL validation for sensitive output.

### Unknown variable behavior

The constructor and `set_unknowns()` support an unknown-variable policy. Common configured behaviors are `remove` (default), `comment`, and `keep`. The global `$TEMPLATE_OPTIONS['force_unknowns']` can override the requested setting. Do not use `keep` as a workaround for missing application variables.

## Conditions and loops

The `replace_extended()` method in Geeklog 2.2.2 recognizes simple variable conditions:

```html
{!if show_panel}
<section>{heading:s}</section>
{!else}
<p>The panel is hidden.</p>
{!endif}
```

It converts `{!if variable}` into a PHP check using `var_notempty()`. This evaluates an assigned variable's nonempty state; it is **not** a general authorization check.

The same parser recognizes `{!elseif variable}`, `{!while variable}`, and matching `{!endwhile}`. For numeric iteration it supports `{!loop variable}` and `{!endloop}`, backed by a counter managed through `loop()`. The source also handles `{!inc variable}`, `{!dec variable}`, optional `+echo`, `{!break}`, `{!continue}`, and `{!unset variable}`.

These constructs are source-supported, but their nesting, generated PHP, and behavior in a particular theme should be verified on a staging installation. In particular, do not assume that `{!for ...}` is implemented merely because an `endfor` pattern appears in the parser—the source comment explicitly marks `for` as future work.

## Advanced expressions and trusted template authors

The source also recognizes advanced expression forms including `{!!if ... !!}`, `{!!elseif ... !!}`, `{!!while ... !!}`, `{!!echo ... !!}`, `{!!set name ... !!}`, `{!!global ... !!}`, and `{!!autotag ... !!}`.

These expressions are converted into executable PHP. Restrict their use to trusted template files and reviewed application code. They must never be presented as a safe scripting interface for general site visitors, unrestricted editors or a hosted template builder.

The historical Wiki discusses embedding PHP in templates. This is a security-sensitive capability, not a recommendation to mix business logic into presentational code.

## Language strings and default variables

`replace_lang()` supports language references such as `{$LANG01[1]}` and `{$LANG01['1']}`, with behavior affected by `cache_by_language`. Language identifiers and indices must exist in the active language arrays.

The constructor's fallback configuration includes template variables such as `site_url`, `site_admin_url`, `layout_url`, `anonymous_user`, `device_mobile`, `language_code`, `front_page` and `current_url`. **Values may be updated by the application**; do not infer that their constructor-time defaults are the final values on a rendered page.

## Template blocks and views

A classic block is delimited by matching markers within a parent template:

```html
<ul>
<!-- BEGIN item -->
<li>{item_label:s}</li>
<!-- END item -->
</ul>
```

Application code registers it with `set_block($parent, $varName, $name)` and provides values before parsing. Check how your caller accumulates or replaces block content rather than assuming a particular rendering loop.

A view created with `set_view()` can include variables and certain blocks. The 2.2.2 source explicitly notes that **nested blocks in views are not supported by its existing handling**. Keep view structures simple and test their output.

## Cache behavior and options

In 2.2.2, the fallback `$TEMPLATE_OPTIONS` defined inside the template constructor includes:

| Option | Source behavior |
| --- | --- |
| `path_cache` | Compiled template storage, normally under data `layout_cache/` |
| `path_prefixes` | Ordered prefixes removed when deriving cache names |
| `incl_phpself_header` | Guard added to generated PHP to prevent direct execution outside Geeklog |
| `cache_by_language` | Separate cache paths for configured language |
| `cache_for_mobile` | Separate mobile cache paths where enabled |
| `default_vars` | Values initially assigned to template instances |
| `hook` | Callbacks for supported template operations |

These defaults are used only when a suitable global `$TEMPLATE_OPTIONS` has not already been provided by application initialization. Inspect the effective runtime configuration before changing cache behavior.

The tagged `check_cache()` method compares template and cached-file modification times. Stale output may therefore involve a wrong active template path, filesystem timestamps, cache permissions, language/mobile separation, or application-level cache layers. Do not disable caching permanently to hide a lookup error.

## Comments and debugging

The source handles `{# ... #}` template comments. The `template_comments` configuration controls whether they are removed or rendered as HTML comments. Do not put secrets in either form.

When debugging a custom theme, verify in order:

1. The exact Geeklog release, active theme, installed plugin and selected template directory.
2. The `set_root()` order and the actual file used by `set_file()`.
3. Variable assignment before the parse call, and the correct output context.
4. Block registration or view source when content repeats or disappears.
5. Cache directory, language/mobile partition and file timestamps.
6. Anonymous and administrative results, then theme/plugin behavior after upgrades.

## Compatibility and further reading

This reference is based on Geeklog **2.2.2** source behavior. Re-check syntax, APIs and generated output when targeting another version, including 2.2.3. The historical Wiki page *Caching Template Library* served as a topic inventory; its code examples have not been reproduced verbatim.

Related guides: [Themes and templates](../templates/) and [Theme development](../theme-development/). For the implementation, consult the [tagged template class](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/classes/template.class.php).
