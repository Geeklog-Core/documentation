# Online documentation — cross-guide audit

**Audit initiated:** 2026-11-06  
**Scope:** current `docs/online-troubleshooting-guide` branch, based on the published upstream documentation.  
**Priority:** online documentation first (P0); version-specific embedded help for Geeklog 2.2.3 remains separate (P1).

## Executive findings

The online build currently indexes **13 maintained Markdown guides** and emits **15 HTML pages** (four root pages, one modern landing page, ten modern guides). The embedded modern subset emits **11 HTML pages**; the original 2.2.2 Core/plugin help remains preserved by the existing release gates.

**Confirmed defect corrected:** eleven guide-to-guide links were hardcoded to `https://geeklog-core.github.io/documentation/modern/...`. In contributor previews and the embedded modern HTML, these links would open the public website and could lead to older content instead of the corresponding local guide. Eleven references in six Markdown guides now use `../../<category>/<guide>/index.html`, the path that works from the corresponding modern guide directory in **both** outputs. The first conversion used incorrect `../../../` depth, and CI correctly rejected it. The corrected links pass CI.

**Successful static CI evidence:** [GitHub Actions #42224111072](https://github.com/hostellerie/documentation/actions/runs/42224111072). The new `tools/audit_online_guides.py` verifies:

| Check | Result |
| --- | ---: |
| Unique indexed guide destinations and maintained sources | 13 |
| Online HTML pages examined | 15 |
| Local online references followed | 233 |
| Local online fragments checked | 41 |
| Embedded modern HTML pages examined | 11 |
| Local embedded modern references followed | 154 |
| Local embedded fragments checked | 0 |

These are **automated file/link observations**, not visual browser acceptance, external link validation, security/behavior testing or full editorial approval. The audit writes its machine-readable result to `dist/online-guide-audit.json`.

## Coverage matrix — maintained guides

**Status terminology:** `STRUCTURE CHECKED` means the source is indexed and generated destinations/local links pass CI. `EDITORIAL PENDING` means accuracy, examples, attribution and feature parity are not yet independently signed off. Every row below remains **EDITORIAL PENDING** unless separately reviewed.

| Maintained guide | Primary audience | Structural result | Next content work |
| --- | --- | --- | --- |
| Installation and migration | Site operators | STRUCTURE CHECKED | Verify release-specific upgrade/migration routes and PHP/database support; test migrations |
| Configuration reference | Administrators/developers | STRUCTURE CHECKED | Finish 321 outstanding source-semantic reviews; external links and historical explanation parity |
| Administration overview | Administrators | STRUCTURE CHECKED | Review reader journey, correct terminology and strengthen task-based links |
| Plugin API | Plugin developers | STRUCTURE CHECKED | Complete callback signatures/returns and check working plugin examples in staging |
| Themes and templates | Theme authors | STRUCTURE CHECKED | Validate actual theme/template path precedence and release-compatible sample edits |
| Static Pages | Editors/admins | STRUCTURE CHECKED | Test page creation, visibility, autotags and plugin permissions in real UI |
| Webservices | Integrators | STRUCTURE CHECKED | Confirm actual routes, supported operations, authentication and response contracts |
| Configuration API | Plugin/Core developers | STRUCTURE CHECKED | Confirm fresh install vs upgrade lifecycle and code examples |
| Users and groups | Administrators | STRUCTURE CHECKED | Exercise least-privileged role/denial scenarios in isolated Geeklog |
| Security and permissions | Developers | STRUCTURE CHECKED | Validate token/rights behavior and plugin-specific rules against target release |
| Backup and recovery | Administrators | STRUCTURE CHECKED | Perform and document a complete isolated database/files restoration |
| Maintenance and upgrades | Administrators | STRUCTURE CHECKED | Verify selected upgrade paths and plugin impact in staging |
| Troubleshooting | Administrators/support | STRUCTURE CHECKED | Test representative failure scenarios and redact source logs/screenshots |

## Eight audit axes and findings

| Axis | Verified today | Follow-up / priority |
| --- | --- | --- |
| 1. Navigation structure | 13 index entries match maintained Markdown source files | P1: review user journeys and legacy compatibility pages; legacy `docs/index.md`, `docs/install.md`, `docs/config.md` still contain outdated prototype wording but are not primary published sources |
| 2. Technical consistency | All reviewed guides distinguish Geeklog 2.2.2 or historical material; built-in Core source checks remain in CI | P1: validate higher-risk API, permissions, authentication and version claims against actual code/runtime |
| 3. Internal links and anchors | 233 online local links, 41 fragments, 154 embedded modern links checked; 11 cross-guide URLs fixed | P1: audit **external** destinations, redirects, archived Wiki and contributor references separately |
| 4. Editorial consistency | Guides have a generated H1 and consistent online/embedded modern HTML byte output | P1: harmonize 'draft', 'source checked' and 'historical' labels; remove outdated prototype wording only where content is sufficiently reviewed |
| 5. Coverage | Installation, configuration, admin, developers, themes, plugins represented by 13 guides | P1: missing task-level depth in callbacks, webservice operations, theme mechanics and exact installation upgrades |
| 6. Usability and search | Search index contains 13 unique destinations; homepage and static HTTP checks already run in CI | P1: **manual** keyboard, mobile, search relevance and real-page visual checks; not claimed passed |
| 7. Procedures and examples | Existing guides contain documented checklists and staging acceptance matrices | P1: real restore, permission, API and troubleshooting acceptance tests; do not convert checklists into claims of execution |
| 8. Build and release | CI checks online site, embedded modern guide file identity and historical 2.2.2 preservation | P1: re-run after each content batch and compare PR against upstream `main`; 2.2.3 embedded release needs its own version-specific gate |

## Automated audit contract

`tools/audit_online_guides.py` runs after online generation, search-index creation, static HTTP checks and the existing historical compatibility tests. It fails when any of these occur:

- Search-index guide URLs are missing, duplicated or not in the maintained 13-guide registry.
- A maintained Markdown source or its generated online page is absent.
- A modern guide in the embedded output is missing or differs from its corresponding online output.
- A generated local link escapes the site, points to a missing file or uses a missing HTML fragment.
- An HTML page lacks a single clear `h1`.
- A modern Markdown guide hardcodes a link to another modern guide on the official site rather than using offline-safe relative navigation.

This is not a live external-link checker, accessibility audit, PHP functionality test or editorial license verifier.

## Next substantial contribution criteria (no PR yet)

1. Expand cross-guide task navigation where useful, without duplicating entire articles.
2. Confirm source references, external link health and historical Wiki reuse rules.
3. Correct outdated prototype labels that confuse published-source pages with old pilot compatibility files.
4. Review code-heavy examples for API and permission correctness, explicitly separating source reading from staging execution.
5. Obtain clean CI and a reviewer-ready diff before opening one substantive online-only PR.

**Publication boundary:** edits on `hostellerie/documentation:docs/online-troubleshooting-guide` are not published to `Geeklog-Core/documentation:main` until reviewed and merged, followed by the maintainer-controlled Pages deployment.
