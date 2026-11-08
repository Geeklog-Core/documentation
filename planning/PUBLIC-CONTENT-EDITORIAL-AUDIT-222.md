# Public documentation editorial and completeness audit — Geeklog 2.2.2

**Audit date:** 2026-11-08  
**Working branch:** `hostellerie/documentation:docs/public-editorial-cleanup`  
**Public delivery:** 24 guide URLs / six groups. The embedded 2.2.2 HTML also builds from these Markdown files; its legacy paths remain unchanged.

## Publication policy

Public documentation explains **how to use Geeklog**, and carries warnings only when they affect an operator's choice (permissions, data loss, outdated security behavior, supported versions). It must not expose the documentation team's review gates, unexecuted test statuses, Wiki copyright deliberations, approval queues or release packaging notes.

Internal testing status must remain **truthful and private to the project workflow**: removing a disclaimer does not turn an untested action into a verified feature, an incomplete explanation into a complete API contract or a historical example into safe advice. Do not add unverified claims to fill a visible gap.

## Inventory of reader-facing status messages

| Type | Examples previously visible | Editorial disposition |
| --- | --- | --- |
| Migration/release banner | `editorial review ongoing`, `coverage notice`, `preview overlay`, `remaining gates` | Remove from reader pages; track in this audit and release checklists |
| Source provenance / Wiki migration | `historical Wiki leads`, `license and contributor attribution pending` | Record in `planning/EDITORIAL-PROVENANCE-REVIEW-222.md`; keep relevant linked code sources and safety facts |
| Validation not performed | `UI verification pending`, `not yet exercised`, `tests remain pending` | Keep test evidence and NOT_RUN states in `planning/PHASE2-STAGING-SCENARIOS.csv`; describe only actual user actions publicly |
| Documentation work queue | `What this guide still needs`, `Still to verify`, `Further verification`, `Remaining research`, `Still missing` | Remove author to-do lists from pages; record substantive gaps below |
| Checklist confusion | `- [ ]` acceptance boxes used as internal test state | Use ordinary readable steps / operational checks in guides; retain execution status only in internal scenario CSV |
| Generator-homepage boilerplate | `original embedded config remains authoritative` / migration status | Replace with plain language about finding configuration and other docs; keep backward-compatibility policy in project plans |
| Deprecated historical behavior | Historical password hashing / OpenID, old SQL and insecure PHP | Retain concise warnings when they materially protect visitors; do not erase real constraints |

## Public guide coverage and remaining verified work

| Public section | Guide or page | Editorial cleanup | Technical/content gap tracked internally |
| --- | --- | --- | --- |
| Getting Started | Installation and upgrades | Removed editorial introduction and publisher release gates | Run full upgrade, migration and rollback scenarios; reconcile release-notes vs installer MySQL minimum discrepancy |
| Getting Started | Configuration | Removed migration banners and repeated source-attribution boilerplate | Complete comparison of all defaults, descriptions, tables, examples and external links with pinned 2.2.2 HTML; preserve 387 help identifiers; test help behavior |
| User Guide | Using Geeklog | Removed UI-acceptance disclaimers and draft workload | Real UI/screenshots and role-specific guided flows still need confirmation |
| User Guide | Articles, Topics and Publishing | Converted internal staging status list into reader checks | Scheduling, draft/publication and role distinctions require real admin walkthrough |
| User Guide | Blocks, Menus and Navigation | Removed future-work prompts | Verify theme-specific placement/menu behavior and block permissions in UI |
| User Guide | Comments and Moderation | Removed historical Wiki and unrun-test notes | Verify moderation queues, permissions and CSRF with test accounts |
| User Guide | Syndication, RSS and Autotags | Removed research backlog | Verify feed destinations, update scheduling and enabled autotag catalogue from installed release |
| Administration | Overview | Removed migration status and incomplete-Wiki notice | Verify all navigation targets and operational links after deployment |
| Administration | Users and Groups | Removed internal verification checklist | Role/permission scenarios, interface labels and least-privilege access in real UI |
| Administration | Backup and Recovery | Removed internal verification status | Rehearse database+files restore with representative plugin/theme content |
| Administration | Maintenance and Upgrades | Removed internal test result notes | Upgrade and recovery behavior remains a separate staging test |
| Administration | Troubleshooting and FAQ | Removed Wiki/editorial status | Review symptom coverage and real diagnostic paths in staging |
| Plugins | Plugin Installation and Management | Removed implementation/approval gates, turned test status into operational checklist | Verify installed plugin manager actions with real clean and upgrade installations |
| Plugins | Bundled Plugins | Replaced research-only inventory with practical overview and task paths | Detailed version-specific UI guides still needed for Calendar, Links, Polls, Spam-X, XMLSitemap and reCAPTCHA |
| Plugins | Static Pages | Removed source migration provenance while retaining PHP execution restrictions | Verify UI and permission scenarios in isolated test site |
| Development & Theming | Plugin Development | Removed historic Wiki backlog | A fully runnable, tested reference plugin remains to be developed |
| Development & Theming | Security and Permissions | Removed editor-only checkboxes | Test exact permissions and session/CSRF interactions across roles |
| Development & Theming | Themes and Templates | Removed Wiki licensing commentary | Verify precise theme file/rendering sequences in tagged release |
| Development & Theming | Theme Development | Removed unexecuted-runtime banner | Source-checked end-to-end theme modification, screenshots and build checks |
| Development & Theming | Contributing | Removed historic coding-policy notes | Maintainers must confirm contribution policy before presenting it as official |
| Technical Reference | Database Schema and Data Model | Replaced an incomplete research checklist with 30 MySQL / 31 PostgreSQL tagged Core table inventory plus plugin table overview | Expand field-level relationships, PG differences and upgrade diffs through generated schema snapshots |
| Technical Reference | Plugin API | Removed Wiki/provenance status and unchecked compatibility boxes | Document tested callback parameters, supported lifecycle and a runnable reference plugin |
| Technical Reference | Configuration API | Removed technical editorial to-do section | Verify plugin configuration lifecycle and upgraded settings with a live site |
| Technical Reference | Webservices API | Removed Wiki and incomplete test declarations | Verify actual endpoints, request formats, authentication and permitted operations; do not advertise unsupported routes |

**Embedded-only source:** `docs/administration/troubleshooting-faq/README.md` remains for the existing offline ZIP, but its historical Wiki editorial backlog has also been removed.

## Source verification used for new schema content

- `Geeklog-Core/geeklog:v2.2.2/sql/mysql_tableanddata.php`: 30 `CREATE TABLE {$_TABLES[...]} ` definitions.
- `Geeklog-Core/geeklog:v2.2.2/sql/pgsql_tableanddata.php`: 31, including `topic_assignments`.
- `plugins/calendar/sql/mysql_install.php`: 3 plugin tables.
- `plugins/links/sql/mysql_install.php`: 3 plugin tables.
- `plugins/polls/sql/mysql_install.php`: 4 plugin tables.
- `plugins/spamx/sql/mysql_install.php`: 1 plugin table.

These counts describe tagged install scripts only, not actual tables in a running or upgraded site. The XMLSitemap schema should not be inferred from missing `CREATE TABLE` matches.

## Outstanding nonpublic acceptance and publication gates

1. **P0:** Run all 30 manually documented scenarios, retain dated evidence and statuses in `planning/PHASE2-STAGING-SCENARIOS.csv`.
2. **P0:** Finish semantic review for configuration and installation, especially potentially harmful upgrade/migration/security claims.
3. **P1:** Expand the six bundled-plugin workflows into tested, version-scoped individual guides.
4. **P1:** Complete the database field/relationship inventory from tagged MySQL and PostgreSQL schema, plus plugin schema and supported upgrade deltas.
5. **P1:** Verify callable Core/plugin API signatures and supported webservice endpoints; never promote guessed examples.
6. **P1:** Perform mobile/browser search, navigation and accessibility review on the public Pages deployment after merge.
7. **P1:** Preserve embedded help anchor, path and ZIP parity and verify the 2.2.3 baseline separately.
8. **P2:** Reuse only technically and legally reviewed historical Wiki material; retain editorial/provenance audit in this planning area.

## Review rule

Before each future documentation PR, run `tools/check_public_editorial.py` in CI to prevent reintroduction of internal editorial banners, unexecuted-test states, work-queue sections and migration approval language into public pages. This is a **structural lint**, not a substitute for technical content review or real runtime testing.
