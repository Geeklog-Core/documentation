# Original installation HTML resource audit

Source: `Geeklog-Core/geeklog/public_html/docs/english/install.html` (Geeklog 2.2.2-era document), reviewed 2026-10-29.

## Local resources required when reproducing legacy packaging

| Reference in source HTML | Purpose | Migration requirement |
| --- | --- | --- |
| `../docstyle.css` | Original documentation stylesheet | Include in packaged HTML or replace with verified local CSS |
| `../images/logo.gif` | Original Geeklog logo | Preserve a working local asset path or intentionally update it |
| `index.html` | Link back to documentation index | Preserve relative navigation |
| `support.html` | Link to bundled support page | Preserve link or verified redirect |
| Nine `#fragment` identifiers | Section links | All nine preserved in generated HTML; covered by CI |

The branch's standalone preview currently generates only `install.html`. It is **not** a distributable set and does not contain the original stylesheet, images, index or support page.

## External references requiring review

The old document references Geeklog.net, software vendors, third-party archive tools, historical mailing lists, Gitter and a MediaWiki URL. Do not assume historical discussion platforms remain active; review before publishing an updated guide.

## Next packaging tests

- [ ] Confirm local resources resolve in the full Geeklog docs distribution.
- [ ] Check relative links to `index.html` and `support.html`.
- [ ] Perform HTTP link checks on relevant external URLs.
- [ ] Verify accessibility and offline operation without external CSS/scripts.
- [ ] Test against an actual Geeklog installation and release archive.
