# Geeklog unified documentation — Geeklog 2.2.2 preview

**Status: work in progress, not an official release.** The goal is to deliver an updated official online site and a compatible embedded HTML documentation ZIP promptly, without waiting for every historical Wiki page or the complete modernization of `config.html`.

## Deliverables

- `dist/online/`: online pages generated from maintained Markdown, including installation, configuration and administration guides, 10 additional modern guides, and unified search across 13 guides.
- `dist/geeklog-2.2.2-docs-preview.zip`: Geeklog 2.2.2 documentation overlay with paths relative to the Geeklog installation root (`public_html/...`).
- Inside the overlay, `public_html/docs/english/install.html` is generated from Markdown and the new guides are available under `public_html/docs/english/modern/`. The historical Core `config.html` and plugin documentation are preserved unchanged as compatibility assets.
- Both online and embedded modern guides come from the same Markdown files.

## Build and deployment

See [Geeklog 2.2.2 delivery checklist](planning/DELIVERY-222.md). The workflow `.github/workflows/dual-preview.yml` builds and uploads preview artifacts with checks. The manually triggered `.github/workflows/publish-fork-pages.yml` now builds the unified site search and an embedded ZIP with integrity checks before publishing GitHub Pages. It checks out the current repository/ref instead of hardcoding an older fork branch.

The maintainer should merge one reviewed PR into the official `Geeklog-Core/documentation:main` before running the publishing workflow there. Fork deployment is only a preview.

## Remaining checks

- Inspect the real official Pages deployment (site, search, links, CSS).
- Test the ZIP overlay in a disposable Geeklog 2.2.2 installation, including real configuration and plugin help clicks.
- Complete the historical `config.html` defaults/tables/examples audit before **ever** replacing the embedded configuration reference with Markdown-generated HTML.
- Maintain release version labeling, source attribution and rollback documentation.

Do not treat structural anchor coverage as content or runtime compatibility.
