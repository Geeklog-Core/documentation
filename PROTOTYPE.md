# Independent dual-output documentation prototype

This branch is a **demonstration**, not an official Geeklog documentation release.
It does not modify the foundation pull request #1.

## Outputs

- `dist/online/`: four responsive static HTML pages, generated from Markdown; `index.html`, `installation.html`, `configuration.html`, and `administration.html`.
- `dist/geeklog-2.2.2/public_html/docs/`: pinned Core HTML documentation tree with **only** `english/install.html` replaced by the generated installation guide.
- `dist/geeklog-2.2.2-docs-preview.zip`: archive with paths relative to the Geeklog installation root.

**Note:** The pinned Core commit is `dd44c01368afad32e16467fd5357af3299c11d3a`. Validate this against the exact 2.2.2 release archive before claiming packaged-release equivalence. The original configuration and plugin HTML remain unchanged.

## Generating locally

```bash
python -m pip install -r requirements-docs.txt
export GEEKLOG_CORE_DOCS=/path/to/pinned/geeklog/public_html/docs
python tools/check_install_anchors.py
python tools/check_install_bundle.py
python tools/check_install_legacy.py
python tools/check_install_overlay.py
python tools/build_dual_preview.py
```

GitHub Actions workflow: `.github/workflows/dual-preview.yml`. Download both workflow artifacts from its successful run.

## Contributing

Edit the Markdown under `docs/installation/`, `docs/configuration/`, or `docs/administration/`; review factual changes against Geeklog source before publishing. Submit changes on an independent fork branch.

## Limitations and launch gates

This site does not yet have a public GitHub Pages deployment. Publishing via GitHub Pages from the fork requires configuration and a deployment workflow. Do not enable official Pages without owner approval.

Historical `config.html`, other Core HTML pages and plugin documentation are retained, not migrated. Existing `changes.html` link defects are tracked as a frozen baseline. Runtime staging installation and release-package comparison remain pending.
