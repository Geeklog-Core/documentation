# Installation HTML preview

This branch generates a **non-authoritative, offline-readable preview**, not release documentation.

Run `python -m pip install -r requirements-docs.txt`, then `python tools/check_install_anchors.py`.

The build creates:
- `build/english/install.html`: Markdown installation draft, legacy nine anchors, local navigation.
- `build/english/index.html`: minimal preview landing page.
- `build/english/support.html`: support placeholder linking back to the installation guide.
- `build/docstyle.css`: local stylesheet.
- `build/images/logo.gif`: a transparent **1×1 placeholder GIF** retained at the historical path. It is **not** Geeklog branding artwork.

The packaging test now validates the exact four legacy local references (`../docstyle.css`, `../images/logo.gif`, `index.html`, `support.html`) as well as the nine historical anchors. External destinations are not fetched. The package does **not** replicate the original Geeklog Core distribution, and must not be shipped in place of it.

## Pinned Core-asset integration mode

In GitHub Actions, a separate checkout of `Geeklog-Core/geeklog` at commit `dd44c01368afad32e16467fd5357af3299c11d3a` supplies the **actual** `public_html/docs/docstyle.css` and `public_html/docs/images/logo.gif`. The `GEEKLOG_CORE_DOCS` environment variable points the generator to that source directory. For a local checkout without this variable, the generated output deliberately uses the earlier preview-only stylesheet and 1×1 placeholder GIF.

Only CSS and logo are imported. `index.html` and `support.html` remain prototype placeholders to avoid claiming support for the complete legacy documentation dependency tree. This is a partial integration test, not proof of full release packaging.
