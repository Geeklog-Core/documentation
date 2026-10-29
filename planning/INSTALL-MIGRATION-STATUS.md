# Installation migration checklist

Source: `Geeklog-Core/geeklog` master `public_html/docs/english/install.html`, blob `eae47434247b4fc0e54706ee9b116618cc40f83e` (checked 2026-10-29).

This branch was created directly from the documentation repository's `main` so it can be reviewed independently from the foundation PR #1.

- [x] Identify nine legacy named HTML anchors and record them in `docs/installation/README.md`.
- [x] Write a limited installation/upgrade/migration introduction with explicit release-specific caveats.
- [ ] Compare install procedures with the current release and installer source.
- [ ] Review PHP/database version requirements for each supported release; do not treat historical minimums as current recommendations.
- [x] Extend the source-derived installation, upgrade, migration and troubleshooting draft with safer diagnostic recommendations.
- [ ] Verify all legacy troubleshooting examples and version-specific procedures before treating the draft as comprehensive.
- [x] Add standalone Markdown-to-HTML preview and test of all nine legacy `id` / `name` anchors on this branch; [CI succeeded](https://github.com/hostellerie/documentation/actions/runs/40865064684).
- [x] Inventory original HTML local assets/navigation and historical external references in `INSTALL-RESOURCE-AUDIT.md`.
- [x] Add standalone checks for local relative paths and fragment links, with a real table of contents linking to preserved historical anchors; [CI successful](https://github.com/hostellerie/documentation/actions/runs/40866083596).
- [x] Generate an independent **preview-only** offline bundle: `build/english/install.html`, `index.html`, `support.html`, `build/docstyle.css`, `build/images/logo.svg`; verify relative references in install page and upload complete bundle in CI ([successful run](https://github.com/hostellerie/documentation/actions/runs/40866357612)).
- [ ] Integrate with eventual shared build and validate original assets, all bundled docs, external references, release packaging and a real Geeklog installation. The SVG is a text-only preview mark, **not** the official logo.
- [ ] Verify documentation against a packaged installation and obtain maintainer review.

**Non-goal:** replacing or deleting existing shipped installation HTML in this branch.
