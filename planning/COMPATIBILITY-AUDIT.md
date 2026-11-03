# Core and plugin help-link compatibility audit

Status: source-code references and a complete named-anchor inventory have been captured; **full compatibility tests remain pending**.

Tom confirmed that Geeklog Configuration tooltips and plugin configuration refer to bundled documentation. The current [English config.html](https://github.com/Geeklog-Core/geeklog/blob/master/public_html/docs/english/config.html) contains named anchors such as `desc_site_url` and `desc_site_name` as well as links to subsections. A generic Markdown-to-HTML converter can change or lose these identifiers.

## Manifest and test design

- [x] Identify Core documentation URL construction: `system/classes/config.class.php` (`_set_ConfigHelp`) selects `COM_getDocumentUrl('docs', 'config.html')` for Core and `PLG_getDocumentationUrl($group, 'config')` for plugins, appending `#desc_<option>` unless a fragment is already present. `PLG_getConfigTooltip` can instead supply tooltip text.
- [x] Identify separate `public_html/admin/install/configinfo.php` links targeting `docs/english/config.html#desc_<option>`.
- [ ] Audit additional hard-coded links and the plugin-specific help URLs across bundled and externally maintained plugins.
- [ ] Inventory bundled plugin configuration help and extension patterns used by external plugins.
- [x] Capture all **450 occurrences** of `<a name="...">` (449 unique names) in the current `config.html`, source blob SHA stored in [legacy-config-anchors.json](legacy-config-anchors.json). One duplicate named anchor: `users_comments`; resolve during migration, not by deleting a legacy target without review.
- [ ] Extract `id` and `name` anchors across **all** docs pages and map incoming references; the existing JSON is only `config.html` named anchors.
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

These anchor patterns are confirmed by Core source code, but actual runtime behavior and individual options have not been exercised. The prototype currently tests only two config anchors; it is not a full compatibility replacement.

No Core files are modified by this branch.
