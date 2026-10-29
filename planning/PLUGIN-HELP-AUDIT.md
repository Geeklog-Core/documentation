# Bundled plugin configuration help links

Source review: Geeklog Core `master`, 2026-10-29. This is a source-level inventory, **not** a functional test of installed Geeklog.

All seven bundled plugins implement `plugin_getdocumentationurl_<plugin>($file)` in `plugins/<plugin>/functions.inc`.

| Plugin | Expected English help document | Resolution |
| --- | --- | --- |
| calendar | `docs/english/calendar.html` | Shared `COM_getDocumentUrl` |
| links | `docs/english/links.html` | Shared `COM_getDocumentUrl` |
| polls | `docs/english/polls.html` | Shared `COM_getDocumentUrl` |
| recaptcha | `admin/plugins/recaptcha/docs/english/config.html` | Plugin-local URL, language fallback |
| spamx | `docs/english/spamx.html` | Shared `COM_getDocumentUrl` |
| staticpages | `docs/english/staticpages.html` | Shared `COM_getDocumentUrl` |
| xmlsitemap | `docs/english/xmlsitemap.html` | Shared `COM_getDocumentUrl` |

## Important exception: reCAPTCHA

`recaptcha` constructs a URL using `site_admin_url` and a language-specific directory under `admin/plugins/recaptcha/docs/`; it falls back to `english` if the selected language file does not exist. A generator targeting only `public_html/docs/english` **cannot** replace this document without additional deployment/packaging rules.

## Compatibility rules

- Preserve all seven plugin help document paths before replacing shipped HTML.
- For `config` help, `system/classes/config.class.php` appends `#desc_<option>` if a returned URL has no fragment.
- Keep `PLG_getConfigTooltip` overrides distinct from the links; some plugin options use tooltip text instead.
- Inventory per-page fragment identifiers and active option names, not just file existence.
- Validate both standalone Core HTML and the separate reCAPTCHA docs under the installed release package.
- Consult extension authors before making a global assumption about external plugins' URLs.
- Confirm any changed option/anchor behavior using integration tests; do not alter the Core in this planning branch.

Machine-readable reference: [bundled-plugin-doc-links.json](bundled-plugin-doc-links.json).
