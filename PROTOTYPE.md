# Documentation generation and embedded HTML compatibility prototype

This repository hosts the official Geeklog documentation website at https://geeklog-core.github.io/documentation/.
The **embedded Geeklog 2.2.2 HTML ZIP remains a compatibility prototype**, not an official Geeklog software/documentation release. The existing legacy HTML is still retained until each page has been migrated and verified.

## Outputs

- `dist/online/`: four responsive static HTML pages, generated from Markdown; `index.html`, `installation.html`, `configuration.html`, and `administration.html`.
- `dist/geeklog-2.2.2/public_html/docs/`: pinned Core HTML documentation tree with **only** `english/install.html` replaced by the generated installation guide.
- `dist/geeklog-2.2.2-docs-preview.zip`: archive with paths relative to the Geeklog installation root.

**Package provenance:** The pinned Core commit is `dd44c01368afad32e16467fd5357af3299c11d3a`. The project's separate official v2.2.2 archive audit (see `planning/OFFICIAL-ARCHIVE-VALIDATION.md`) verified the downloaded archive and all 46 document files: 8 byte-identical, 37 line-ending-only differences and exactly one intended changed HTML page. This **does not make the prototype an official release package**. The original configuration and plugin HTML remain unchanged.

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

The official GitHub Pages website is published. Deployment is an explicit, manually triggered GitHub Actions workflow after a reviewed change is merged to `main`. This workflow does not automatically modify any Geeklog Core release package.

Historical `config.html`, other Core HTML pages and plugin documentation are retained, not migrated. Existing `changes.html` link defects are tracked as a frozen baseline. **On 2026-11-03, a new installation from the official 2.2.2 tarball and a real embedded-doc overlay were validated** in an isolated Docker environment; the user confirmed site and authenticated admin access plus sampled Core and reCAPTCHA documentation pages and historical configuration anchor. XMLSitemap was deliberately disabled after a sitemap-file permission warning. Post-install default-password/config-permission review, actual restore/rollback, broader link checks, upgrade and migration flows remain pending. See `planning/INSTALL-STAGING-VALIDATION.md`.
