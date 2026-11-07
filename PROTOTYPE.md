# Geeklog unified documentation — Geeklog 2.2.2 preview

**Status: work in progress, not an official release.** The goal is to deliver an updated official online site and a compatible embedded HTML documentation ZIP promptly, without waiting for every historical Wiki page or the complete modernization of `config.html`.

## Deliverables

- `dist/online/`: **24 searchable guides** across six homepage sections (**25 HTML pages**). Public paths are clean directories such as `/installation/`, `/user-guide/` and `/reference/plugin-api/`; no `/modern/`, redirects or flat legacy `.html` compatibility pages are published.
- `dist/geeklog-2.2.2-docs-preview.zip`: Geeklog 2.2.2 documentation overlay with paths relative to the Geeklog installation root (`public_html/...`).
- Inside the overlay, `public_html/docs/english/install.html` is generated from Markdown and the new guides are available under `public_html/docs/english/modern/`. The historical Core `config.html` and plugin documentation are preserved unchanged as compatibility assets.
- Both online and embedded guides derive from the maintained Markdown. Their **HTML presentation and navigation differ intentionally**: online paths and six-section navigation are optimized for the website, while the 22 embedded guides and their historical `/english/modern/` layout stay unchanged. The FAQ is consolidated into the public Troubleshooting guide, while its embedded page remains present.

## Build and deployment

See [Geeklog 2.2.2 delivery checklist](planning/DELIVERY-222.md). The workflow `.github/workflows/dual-preview.yml` builds and uploads preview artifacts with checks. The manually triggered `.github/workflows/publish-fork-pages.yml` now builds the unified site search and an embedded ZIP with integrity checks before publishing GitHub Pages. It checks out the current repository/ref instead of hardcoding an older fork branch.

The maintainer should merge one reviewed PR into the official `Geeklog-Core/documentation:main` before running the publishing workflow there. Fork deployment is only a preview.

## Remaining checks

- Inspect the real official Pages deployment (site, search, links, CSS).
- Test the ZIP overlay in a disposable Geeklog 2.2.2 installation, including real configuration and plugin help clicks.
- Complete the historical `config.html` defaults/tables/examples audit before **ever** replacing the embedded configuration reference with Markdown-generated HTML.
- Maintain release version labeling, source attribution and rollback documentation.

Do not treat structural anchor coverage as content or runtime compatibility.

## Verified official archive and isolated installer observations

The [official Geeklog 2.2.2 archive validation](planning/OFFICIAL-ARCHIVE-VALIDATION.md) checked the downloaded distribution's documentation against the pinned source: 46 documented files, eight byte-identical, 37 differing only by line-ending normalization, and one intended updated installation HTML file. These checks are distinct from an officially approved release.

The [isolated Docker installation report](planning/INSTALL-STAGING-VALIDATION.md) records a fresh installation from the official 2.2.2 archive using PHP 8.1.33 / MariaDB 10.11, working authenticated administration and a documentation overlay. XMLSitemap was disabled following a post-install permissions warning; this is not proof its installation is repaired. Upgrade, migration, tested rollback, and the final post-install security checklist are not yet accepted.
