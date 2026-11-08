# Caching Template Library (CTL) — developer reference

Geeklog uses the `Template` class to separate presentation from application code. CTL can render template files and, in supported releases, template views. This reference focuses on the **Geeklog 2.2.2 source baseline** and preserves the historical Wiki's technical topics without treating every old example as tested in a modern installation.

**Source of truth:** [Geeklog v2.2.2 `system/classes/template.class.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/classes/template.class.php). Compare with the exact installed version before deploying theme or plugin changes.

## Core PHP API

The following public methods are present in the tagged Geeklog 2.2.2 template class:

| Method | Purpose | Notes |
| --- | --- | --- |
| `__construct($root = array('.'), $unknowns = 'remove')` | Create a template instance | Root may be an array; options and unknown-variable behavior are release-sensitive |
| `set_root($root)` | Configure template lookup directories | Verify lookup precedence and paths used by your theme |
| `set_file($varName, $filename = '')` | Register one or more template files | File resolution depends on active roots |
| `set_view($varName, $view = '')` | Register a string-based view | Verify rendering and permissions in the consuming application |
| `set_block($parent, $varName, $name = '')` | Register a block in a parent template | Verify block nesting and rendering behavior before reuse |
| `set_var($varName, $value = '', $append = false, $nocache = false)` | Supply template replacement variables | Variables containing untrusted content require appropriate output escaping |
| `get_var($varName)` / `get_vars()` | Read variable values | Do not expose internal values publicly |
| `clear_var($varName)` | Clear assigned variables | Inspect the implementation for the installed release |
| `parse($target, $varName, $append = false)` | Parse registered templates | Check output behavior and escaping at the actual call site |

This table verifies **method presence and signatures**, not successful runtime execution of every usage pattern.

## Basic rendering outline

A common integration sequence is to create a `Template` instance, register the template with `set_file`, assign data with `set_var`, and render via `parse`. The exact output and surrounding lifecycle depend on the caller. Consult existing Core and plugin usages in the tagged release before adapting this outline.

Do not copy historical PHP snippets straight into production themes. Always distinguish trusted static presentation values from data supplied by visitors, and enforce authorization in server-side code rather than template conditions.

## Templates, views, and source paths

The historic **Caching Template Library** page explains template compilation and caching, multiple source directories, reusable blocks, and string-based views. The 2.2.2 class contains `set_root`, `set_file`, `set_view`, and `set_block`, supporting the existence of these API entry points. **Specific lookup order, compilation/cache invalidation, and nested-block behavior still require targeted code and runtime review.**

A practical theme workflow:

1. Record the Geeklog version and enabled theme/plugins.
2. Copy the theme into an isolated installation.
3. Identify the actual rendered template and its candidate override directories.
4. Make one reversible change and test public, authenticated, and administrative views.
5. Check cached versus uncached output and restore the original if results differ.

## Historical CTL syntax — validation pending

The recovered Wiki documented advanced syntax beyond ordinary replacement variables:

- Conditional presentation: `{!if ...}`, `{!else}`, `{!elseif ...}`, `{!endif}`.
- Looping and control flow: `{!loop ...}`, `{!while ...}`, `{!break}`, `{!continue}`.
- Advanced actions: `{!!if ... !!}`, `{!!set ... !!}`, `{!!echo ... !!}`.
- Variable modifiers, automatic language variables, and template blocks.

**These are a historical feature inventory, not a promise that every spelling or behavior works in Geeklog 2.2.2 or 2.2.3.** Test each construct against the matching parser implementation and then in an isolated runtime before publishing executable examples. Do not enable arbitrary template PHP or advanced expressions with untrusted authors.

## Troubleshooting

| Symptom | First check |
| --- | --- |
| Replacement variable visible as raw markup | Variable name, value assignment, parsing path |
| Edited file does not appear | Active theme, root lookup order, cache/compilation |
| Blocks missing or repeated | `set_block` registration and parent mapping |
| Differences between users | Application permissions, variable population, and output caching |
| Upgrade changes output | Compare installed template class and release-specific files |

## Provenance and next verification steps

This guide is an independently rewritten, source-scoped reference inspired by the historic *Caching Template Library — GeeklogWiki* page provided by a Geeklog maintainer. It does **not** republish the historic article verbatim. Attribution and reuse of historical examples require a provenance/licensing review before incorporation.

Pending: verify CTL parser grammar and modifiers against v2.2.2, execute safe examples in an isolated Geeklog 2.2.2 instance, compare with the exact 2.2.3 release source when available, and check plugin/theme integration flows. Track evidence in the project's staging checklist.

See also [Themes and templates](../templates/), [Theme development](../theme-development/), and the [release documentation workflow](../../../planning/RELEASE-DOCUMENTATION-WORKFLOW.md).
