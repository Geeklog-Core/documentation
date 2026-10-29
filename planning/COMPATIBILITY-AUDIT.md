# Core and plugin help-link compatibility audit

Status: required gate **before** any replacement of bundled HTML. No compatibility tests have been run.

Tom confirmed that Geeklog Configuration tooltips and plugin configuration refer to bundled documentation. The current [English config.html](https://github.com/Geeklog-Core/geeklog/blob/master/public_html/docs/english/config.html) contains named anchors such as `desc_site_url` and `desc_site_name` as well as links to subsections. A generic Markdown-to-HTML converter can change or lose these identifiers.

## Manifest and test design

- [ ] Search Core configuration code for help URL and fragment construction; distinguish text tooltips from deep links.
- [ ] Inventory bundled plugin configuration help and extension patterns used by external plugins.
- [ ] Extract actual HTML file paths and all `id` / `name` anchors; map incoming links to targets.
- [ ] Track `legacy path#fragment -> proposed generated path#fragment` in a machine-readable manifest.
- [ ] Prefer maintaining identical relative URLs and legacy anchors in the first release.
- [ ] Check anchor uniqueness, internal hyperlinks, image/CSS paths, URL encoding, case sensitivity and offline operation.
- [ ] Run regression checks against Core and representative plugin configuration pages and an installed release package.
- [ ] Require reviewer approval and a rollback path before changing any help-link target or bundled docs path.

Examples to preserve pending verification:

```text
public_html/docs/english/config.html#desc_site_url
public_html/docs/english/config.html#desc_site_name
```

The above are observed document fragments, **not** yet verified as referenced by any particular runtime link. More anchors and paths may exist.

No Core files are modified by this branch.
