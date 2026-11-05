# Geeklog Documentation

Documentation for [Geeklog CMS](https://github.com/Geeklog-Core/geeklog), maintained in English using Markdown.

## Published documentation

- [Official documentation website](https://geeklog-core.github.io/documentation/)
- [Official source repository](https://github.com/Geeklog-Core/documentation)
- [Contributor fork](https://github.com/hostellerie/documentation)

The official website exists, but the additional guides in this contributor branch are **not published upstream until reviewed and merged**.

## Two outputs from maintained Markdown

1. A searchable public HTML website: 3 general guides and 10 modernized supplementary guides, with 13 pages in the search index.
2. A Geeklog **2.2.2 documentation overlay ZIP**, containing a generated installation guide, 10 additional modernized guides, and the historically required Core/plugin help at its original paths.

The embedded `public_html/docs/english/config.html` and bundled plugin help are still the **unmodified legacy 2.2.2 documents**. The condensed online configuration overview preserves 387 help anchors and 449 unique historical anchors but does not yet reproduce every default, table, or example. Do not replace the embedded historical configuration reference with this overview.

## Build and validation

See [the 2.2.2 release-candidate delivery checklist](planning/DELIVERY-222.md) and [staging test results](planning/INSTALL-STAGING-VALIDATION.md). The Actions workflow `.github/workflows/dual-preview.yml` builds both artifacts and checks provenance, anchors, expected archive paths, local resources and website search/navigation.

The Pages workflow is manually triggered after maintainer review and merge. The preview ZIP must be validated in an isolated Geeklog 2.2.2 installation before it can be described as a production-ready replacement.

## Migration scope

- Consolidate and technically review existing English Core documentation.
- Selectively recover useful information from the historic MediaWiki, preserving attribution and identifying obsolete APIs.
- Preserve offline help links, plugin-specific paths, Japanese legacy material, and release-specific references until replacement is verified.
- Develop in a consolidated contributor branch and submit reviewed changes to the official repository; do not maintain a parallel Wiki.

These are progressive goals. **Neither the historic Wiki nor all legacy configuration content has been completely migrated.**

## Contributing

Contribute Markdown improvements with version-scoped claims and source references. Verify API signatures, security advice, and installation procedures against the relevant Geeklog release. Use pull requests and request maintainer review before publishing official documentation.
