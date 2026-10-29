# Installation HTML preview

This branch generates a **non-authoritative, offline-readable preview**, not release documentation.

Run `python -m pip install -r requirements-docs.txt`, then `python tools/check_install_anchors.py`.

The build creates:
- `build/english/install.html`: Markdown installation draft, legacy nine anchors, local navigation.
- `build/english/index.html`: minimal preview landing page.
- `build/english/support.html`: support placeholder linking back to the installation guide.
- `build/docstyle.css`: local stylesheet.
- `build/images/logo.svg`: original-free *text-only project mark* used for preview, **not** the official Geeklog logo.

The packaging test validates local references and anchors. External destinations are not fetched. The package does **not** replicate the original Geeklog Core distribution, and must not be shipped in place of it.
