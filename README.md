# Geeklog Documentation

Documentation for [Geeklog CMS](https://github.com/Geeklog-Core/geeklog), maintained in English using Markdown.

## Published documentation

- [Official documentation website](https://geeklog-core.github.io/documentation/)
- [Official source repository](https://github.com/Geeklog-Core/documentation)
- [Contributor fork](https://github.com/hostellerie/documentation)

The official documentation website is published from the upstream repository. Contributor changes appear there only after merging and running the maintainer-controlled Pages deployment.

## Delivery priorities (2026-11-06)

**P0 — Official online documentation.** Publish practical, version-labelled English guides on the [official documentation website](https://geeklog-core.github.io/documentation/) as soon as they pass website and editorial review. Source and build validation are already available; the remaining full embedded configuration-help migration does **not** block publication of suitably qualified online content. See [online-first roadmap](planning/ONLINE-FIRST-ROADMAP.md).

**P1 — Embedded documentation for Geeklog 2.2.3.** Produce and validate version-specific offline HTML and contextual administration help against a 2.2.3 baseline before integrating it into a Geeklog release. The existing 2.2.2 preservation ZIP and isolated config candidate are historical/test artifacts, **not** an approved 2.2.3 package. Their acceptance criteria remain separate.

The public website is deployed only from upstream `Geeklog-Core/documentation:main` following review, merge and the maintainer's manual GitHub Pages workflow.

## Two outputs from maintained Markdown

1. A searchable public HTML website with **25 guide routes across six sections** (26 HTML pages including home). Canonical directory URLs include `/installation/`, `/configuration/`, `/user-guide/` and `/reference/plugin-api/` — there is **no public `/modern/` subtree**, old flat public `.html` page, redirect or compatibility page.
2. A Geeklog **2.2.2 documentation overlay ZIP**, with **23 modern guides and their index** still under `public_html/docs/english/modern/`, and historically required Core/plugin help at its original paths. The public troubleshooting page includes the FAQ; the embedded guide layout is left intact.

The [Caching Template Library reference](docs/development/caching-template-library/README.md) documents source-checked Geeklog 2.2.2 template APIs and syntax. The [proposed release documentation workflow](planning/RELEASE-DOCUMENTATION-WORKFLOW.md) defines review and validation gates for future versioned online and embedded documentation.

The online homepage provides a five-step beginner journey. Individual guides include compact six-section navigation, breadcrumbs, an on-page outline and previous/next links. Technical API references are grouped under **Technical Reference**.

The embedded `public_html/docs/english/config.html` and bundled plugin help are still the **unmodified legacy 2.2.2 documents**. The online Geeklog 2.2.2 configuration reference preserves 387 help identifiers and 449 unique historical anchors and transcribes all 387 historical documented default values. It includes source-checked selected tables, examples and 66 targeted semantic reviews; full editorial parity of the other explanations, tables and links is still incomplete. This online reference may be published with version-scoped warnings, but must not replace the historical embedded `config.html`.

## Build and validation

See [the 2.2.2 release-candidate delivery checklist](planning/DELIVERY-222.md) and [staging test results](planning/INSTALL-STAGING-VALIDATION.md). The Actions workflow `.github/workflows/dual-preview.yml` builds both artifacts and checks provenance, anchors, expected archive paths, local resources and website search/navigation.

The Pages workflow is manually triggered after maintainer review and merge. The 2.2.2 overlay ZIP has been tested in an isolated Geeklog 2.2.2 installation, including browser/help navigation and rollback. This does not make it an official CMS release package.

## Migration scope

- Consolidate and technically review existing English Core documentation.
- Selectively recover useful information from the historic MediaWiki, preserving attribution and identifying obsolete APIs.
- Preserve offline help links, plugin-specific paths, Japanese legacy material, and release-specific references until replacement is verified.
- Use one active contributor branch for the next set of reviewed Markdown changes; do not maintain a parallel Wiki.

These are progressive goals. **Neither the historic Wiki nor all legacy configuration content has been completely migrated.**

## Contributing

Contribute Markdown improvements with version-scoped claims and source references. Verify API signatures, security advice, and installation procedures against the relevant Geeklog release. Use pull requests and request maintainer review before publishing official documentation.
