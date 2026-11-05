# Configuration reference migration — Geeklog 2.2.2

## Why this is the priority

The bundled `public_html/docs/english/config.html` from Geeklog 2.2.2 is about 175 KB and contains **387 distinct context-sensitive help anchors** beginning with `desc_` (initial source inventory performed 2026-11-04). These fragments are consumed by administration/configuration help. A new documentation website that does not include this reference cannot be called complete.

The current online Markdown configuration overview includes 32 site and mail settings, including `desc_site_url` and `desc_site_name`, which represents **76 / 387** help anchors (~0.52%). It is intentionally labeled a partial preview; the shipped `english/config.html` is preserved unchanged.

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

The configuration reference is **not yet modernized**. Coverage is 76/387, with the original 2.2.2 embedded file protected. This document records the evidence and mechanical migration acceptance tests; it does not claim that remaining settings are ready.

## First verified migration batch — site and mail settings

- **30** newly authored version-scoped site and mail configuration entries in `docs/configuration/README.md`, in addition to the two preexisting site settings.
- **32 of 387** `desc_*` anchors now authored and matched by exact name against the official Geeklog v2.2.2 `config.html`. No duplicate or invented names in this batch; **311** remain.
- `tools/check_configuration_coverage.py` now enforces a baseline of these exact **32** anchors. Source-HTML descriptions were condensed and still need editorial review; the embedded `english/config.html` remains byte-identical to pinned Core.
- GitHub Actions confirmation of the new report should be checked for final commit `feb27e4`. Do not mark complete solely from names.

## Second configuration batch — Syndication and comment feeds

- Added **10** release-scoped syndication and comment-feed parameters in `docs/configuration/README.md`: `backend`, `rdf_file`, `rdf_limit`, `rdf_storytext`, `rdf_language`, `syndication_max_headlines` and four `comment_feeds_*` settings.
- Current structural coverage: **42 of 387** official `desc_*` configuration-help anchors (**10.85%**); **311** remain. All 42 are unique and appear in the exact tagged v2.2.2 reference.
- `tools/check_configuration_coverage.py` now locks all 42 stable anchor identifiers. The original embedded `config.html` remains unchanged.
- The current workflow run must pass before declaring CI verification; exact descriptions and edge-case behavior remain to be tested in Geeklog 2.2.2.

## Third migration batch — Article and login settings

- Added **34** more release-scoped Markdown configuration descriptions: **16** for article presentation/publishing and **18** for login/access/account protection.
- The existing documentation page now contains **76 of 387** unique `desc_*` anchors (**19.64% structural coverage, 311 remaining**). All 76 identifiers were checked against the exact bundled Geeklog v2.2.2 HTML reference. No IDs were fabricated or duplicated.
- The `tools/check_configuration_coverage.py` locked regression baseline was extended to all **76** identifiers.
- The legacy `pass_alg` setting is explicitly flagged as **historical**, not present-day security guidance. Actual login/security behavior remains to be tested in a disposable Geeklog installation.
- The embedded `docs/english/config.html` remains unchanged pending complete migration and compatibility tests.
- CI for this latest branch state must be confirmed separately; queued GitHub Actions workflows are not evidence of success.

## Fourth configuration batch — themes, submissions and comments

- Migrated **33** additional Geeklog 2.2.2 settings to Markdown: seven theme/template settings, three account-submission rules, nine content submission settings and fourteen comment/moderation settings.
- **109 / 387** source-matched unique `desc_*` anchors now appear in the online reference (**28.17% structural coverage, 278 outstanding**). All new names were checked against the pinned Core `config.html`, with no duplicates or invented identifiers.
- `tools/check_configuration_coverage.py` now locks all 109 migrated identifiers as regression requirements. The original embedded `english/config.html` remains byte-identical and is not replaced.
- Remaining substantive checks: verify the prose and defaults against actual installer configuration, live plugin/theme behavior, link fragment behavior, security and attribution. Do not treat structural coverage as editorial validation.

## Fifth migration batch — blocks and language/locale settings

- Added **37** version-scoped configurations: **19** for admin/topic/online/What's New blocks and **18** for site language, multilingual content, date/time and number formats.
- **146 of 387** official help anchors now structurally appear in the Markdown online configuration reference (**37.73%** coverage, **241** remain).
- Compared all 146 `desc_*` IDs with the exact Geeklog v2.2.2 bundled config HTML: all unique and present, and all required in `tools/check_configuration_coverage.py`.
- Embedded `english/config.html` is still preserved byte-for-byte; version-specific descriptions and runtime behavior need further editorial and staging validation.
- The corresponding GitHub Actions build has not yet completed; structural ID validation was performed separately and should not be confused with CI success.

## Sixth migration batch — image processing and avatars

- Migrated **22** more version-scoped configuration descriptions from the pinned Geeklog v2.2.2 source: 3 image libraries, 4 upload/scaling settings, 3 article image limits, 3 topic icon limits, 6 user photo/avatar settings and 3 Gravatar settings.
- The current online Markdown reference has **168 of 387** source-matched unique `desc_*` anchors (**43.41%** structurally present, **219 remaining**). All 168 are in the regression baseline in `tools/check_configuration_coverage.py`.
- The original embedded `english/config.html` is still preserved byte-for-byte. Statements about third-party image libraries and Gravatar must be tested on the installed environment; presence of an older setting is not evidence of external-service current functionality.
- Latest confirmed successful dual-preview run before this batch was **41867103306**, for `be2fb23` (146/387). The new image batch's CI outcome must be checked against the new commit before it can be called passed.

## Seventh batch — system paths, database backup and search configuration

- Migrated **22** original Geeklog v2.2.2 settings to `docs/configuration/README.md`: 7 site/filesystem paths, 4 database-backup options and 11 search controls.
- Direct comparison with the tagged 2.2.2 Core config reference confirms **190 distinct source-matched `desc_*` anchors of 387** (**49.10% structural coverage, 197 remaining**) and no duplicates or invented anchors.
- `tools/check_configuration_coverage.py` now requires all **190** anchors. The historical embedded `english/config.html` remains unmodified and must stay protected until full migration and compatibility tests.
- Do not interpret a structural anchor check as review of defaults, security, functionality, copyright attribution or live link behavior.

## Eighth configuration batch — advanced themes, cookies, misc and digest

- Migrated **32** further Geeklog 2.2.2 settings into the Markdown source: 3 advanced theme features, 13 cookie/session options, 13 general/diagnostic options and 3 daily digest options.
- **222 / 387** distinct original `desc_*` help anchors now structurally present (**57.36%**, with **165 outstanding**). All 222 are source-backed and unique and locked by the required anchor regression list.
- Security-sensitive historic defaults (such as session cookies, `rootdebug`, `frame_options`) are discussed as version-scoped behavior, not modern production recommendations.
- Embedded `english/config.html` remains byte-for-byte the original; full editorial review, runtime testing and legal attribution must precede any replacement.

## Ninth batch — filtering, webservices, Filemanager and permissions

- Added **81** release-scoped configuration descriptions: 5 HTML filtering, 3 content censoring, 1 IP lookup, 3 webservices, 5 topic breadcrumbs, 20 Filemanager and **44 default content/autotag permissions**.
- The Markdown online reference now includes **303/387** original `desc_*` configuration help anchors (**78.29% structural coverage, 84 remaining**).
- All 303 identifiers were directly compared against tagged Geeklog 2.2.2 bundled config HTML: unique, all present; explicit `tools/check_configuration_coverage.py` regression set requires all 303.
- Permissions and file-management descriptions are version-scoped, not endorsements of the historical security defaults. Review effective access on a staged site.
- The embedded legacy `english/config.html` remains byte-for-byte unchanged until all source anchors and page contents are verified, with a separate full-link/compatibility test and provenance/licensing check.

## Tenth batch — full structural configuration help coverage

- Converted the **last 84** `desc_*` help anchors from tagged Geeklog 2.2.2 `config.html`: 10 structured data/related article, 9 trackback/pingback, 16 core registration/identity/Spam-X, 21 historical third-party OAuth, 23 Likes, and 5 `siteconfig.php` bootstrap settings.
- Markdown now contains **all 387 / 387** official help identifiers, each exactly once. This was directly checked by comparing the complete `desc_*` ID sets from the Markdown and pinned source.
- `tools/check_configuration_coverage.py` now requires **exact equality** of source vs generated online help-ID sets, rather than only reporting partially migrated IDs. The 387 identifier regression baseline is pinned.
- **100% structural coverage is not 100% text or link compatibility.** The Markdown descriptions are often condensed; not all historical subtopics, tables, examples and cross-references have been migrated. The original embedded `config.html` has **not** been replaced.
- Next acceptance gates before making the Markdown the single source for the *embedded* config help: (a) extract ALL historical HTML ids/named anchors, not only `desc_*`, (b) audit local links/embedded assets and external references, (c) compare substantive sections and defaults for information loss, (d) review licensing/source attribution, (e) test in real Geeklog 2.2.2 configuration administration and install/staging flows, (f) only then generate `english/config.html` from a single Markdown source with compatible HTML paths and anchors.

## Historical navigation audit after 387/387 help anchors

An independent inventory of the original Geeklog 2.2.2 HTML config reference found:
- **449 unique** original named/ID anchors (450 occurrences; `users_comments` is repeated).
- **387 `desc_*`** context-help anchors: all represented in Markdown.
- **62 non-`desc_*`** anchors for historical headings, section navigation and auxiliary documentation: not yet present in the generated online Markdown configuration page.
- **34 unique** same-page fragment destinations in source links, all of which resolve against the original HTML source.

The configuration coverage script now reports the missing 62 non-help anchors and checks that the original source's same-page references still resolve. Missing headings are **reported rather than failed** in the transitional online preview; the legacy embedded HTML remains unchanged. Before replacing `english/config.html`, migrate these 62 section anchors or provide verified compatibility aliases, and test all help navigation and substantive paragraphs.

**Caution:** source uses a duplicate named anchor `users_comments`; preserve all source *unique identifiers* but resolve ambiguous duplicate heading naming during the final editorial pass without breaking historic references.

## Eleventh batch — all historical navigation anchors restored

- Added exact same-page compatibility anchors for all **62** non-`desc_*` historical section IDs to the Markdown configuration page, including headings for site, stories, users, images, locale, file manager and all original appendix entries. The source's repeated `users_comments` name is represented once (unique historical anchors preserved).
- Online Markdown now contains **449 / 449 distinct** historical anchor names, of which **387** are individual help settings and **62** are navigation/reference fragments. Verified direct ID-set comparison before commit (no unknown, missing or duplicate IDs).
- Added short migration-preview explanations at 8 original appendix destinations (`db-config.php`, `url-rewrite`, `url-routing`, `Localization`, `date_formats`, `url-cron`, `cron_daily_digest`, `cron_emailed_database_backup`). These **do not yet contain all the original long tables and examples**.
- The coverage script now **fails on any mismatch in the entire 449-anchor set** and if the 34 original same-page fragment destinations are absent from the generated online page. Original embedded `english/config.html` is still byte-identical.
- This closes the **structural anchor compatibility** gap but not remaining content, legacy relative link or installed admin functional parity. Do not ship a replacement embedded `config.html` before those gates and rights attribution review.
