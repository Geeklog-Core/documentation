# Configuration reference migration — Geeklog 2.2.2

## Why this is the priority

The bundled `public_html/docs/english/config.html` from Geeklog 2.2.2 is about 175 KB and contains **387 distinct context-sensitive help anchors** beginning with `desc_` (initial source inventory performed 2026-11-04). These fragments are consumed by administration/configuration help. A new documentation website that does not include this reference cannot be called complete.

The current online Markdown configuration overview includes 32 site and mail settings, including `desc_site_url` and `desc_site_name`, which represents **42 / 387** help anchors (~0.52%). It is intentionally labeled a partial preview; the shipped `english/config.html` is preserved unchanged.

## Control gate added

`tools/check_configuration_coverage.py`:
- takes the pinned Core docs path from `GEEKLOG_CORE_DOCS`
- confirms the embedded `config.html` is byte-for-byte unchanged
- parses exact `desc_*` anchors from the source HTML and generated online configuration page
- requires the 32 already migrated anchors not to disappear
- reports coverage and missing anchors as JSON at `dist/configuration-coverage.json`
- fails if source looks incomplete, if an anchor is fabricated, or if a preserved anchor is lost

This is a **structural** inventory, not proof of the validity of migrated prose.

## Migration order

1. Inventory anchors with labels/descriptions and record the existing HTML section/subgroup for each configuration setting.
2. Extract the content of each setting into a reviewable Markdown section, preserving **all original anchors**. Verify correct defaults and applicability in the pinned Geeklog 2.2.2 configuration definitions and the installed administration UI.
3. Improve the online page in batches. Keep each `desc_*` identifier stable and test links and fragments. The online site is one documentation, not a public Wiki archive.
4. Once **all 387** are migrated, test real help clicks, review licensing/attribution and generate `docs/english/config.html` from the same Markdown instead of preserving the old HTML.
5. Update `check_dual_archive.py` to permit the intentional config overlay **only when** the original anchor set and all legacy local references are preserved and a staging installation test passes.

Other Core/plugin help docs must go through the same process rather than silently pointing to obsolete Wiki URLs.

## Status

The configuration reference is **not yet modernized**. Coverage is 42/387, with the original 2.2.2 embedded file protected. This document records the evidence and mechanical migration acceptance tests; it does not claim that remaining settings are ready.

## First verified migration batch — site and mail settings

- **30** newly authored version-scoped site and mail configuration entries in `docs/configuration/README.md`, in addition to the two preexisting site settings.
- **32 of 387** `desc_*` anchors now authored and matched by exact name against the official Geeklog v2.2.2 `config.html`. No duplicate or invented names in this batch; **345** remain.
- `tools/check_configuration_coverage.py` now enforces a baseline of these exact **32** anchors. Source-HTML descriptions were condensed and still need editorial review; the embedded `english/config.html` remains byte-identical to pinned Core.
- GitHub Actions confirmation of the new report should be checked for final commit `feb27e4`. Do not mark complete solely from names.

## Second configuration batch — Syndication and comment feeds

- Added **10** release-scoped syndication and comment-feed parameters in `docs/configuration/README.md`: `backend`, `rdf_file`, `rdf_limit`, `rdf_storytext`, `rdf_language`, `syndication_max_headlines` and four `comment_feeds_*` settings.
- Current structural coverage: **42 of 387** official `desc_*` configuration-help anchors (**10.85%**); **345** remain. All 42 are unique and appear in the exact tagged v2.2.2 reference.
- `tools/check_configuration_coverage.py` now locks all 42 stable anchor identifiers. The original embedded `config.html` remains unchanged.
- The current workflow run must pass before declaring CI verification; exact descriptions and edge-case behavior remain to be tested in Geeklog 2.2.2.
