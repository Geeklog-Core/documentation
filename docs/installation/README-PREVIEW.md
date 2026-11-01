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
