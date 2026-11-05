# Geeklog 2.2.2 — editorial and provenance release audit

Audit initiated: 2026-11-05. Scope: Markdown guides in `prototype/wiki-unified-222` destined for the official online documentation and the 2.2.2 embedded HTML preview. **This file is a release gate, not license clearance.**

## Evidence and licensing policy

- **Primary technical source:** the immutable [Geeklog 2.2.2 tag](https://github.com/Geeklog-Core/geeklog/tree/v2.2.2), original `public_html/docs/english/` and tagged plugin sources. A documented function's **existence** does not establish the safety or correctness of a usage example. Record exact source symbol and version for API claims.
- **Historical reference:** the contributor-reviewed Geeklog Wiki SQL backup dated 2024-11-02 and the 14-page pilot. 351 recovered pages were counted, but **only the initial 14 were classified**. The original author/revision histories and the Wiki's applicable site-specific reuse license are **not yet established**.
- **Software code versus Wiki text:** Geeklog software is distributed under the GPL, but **do not infer** that every contributor-authored Wiki article, screenshot or third-party illustration is licensed on the same terms. A MediaWiki installation does not establish any particular content license by itself.
- **Policy before official publication:** do not paste historical Wiki article bodies or code samples, unattributed passages, images or screenshots from the archive. Newly written factual summaries may describe observed behaviors with source links; any expressive reproduction or adapted text requires a contributor/license check and appropriate attribution. Keep source file names and original Wiki titles in this register as traceability, not as proof of reuse permission.
- **Existing bundled HTML in 2.2.2:** preserved byte-identical as compatibility assets. Assess licensing and redistribution requirements with the upstream maintainer for the official package. This audit does not grant rights to republish unrelated third-party works.
- **Editorial safety:** a draft must not use undocumented legacy PHP or SQL operations as modern best practice; old version minimums are historical information, not modern deployment recommendations.

## Publication matrix

| Published Markdown source | Primary basis | Historic Wiki basis | Editorial status / release action |
| --- | --- | --- | --- |
| `docs/installation/README.md` | v2.2.2 install HTML, installer source; isolated 2.2.2 staging report | No direct Wiki body | Installation walkthrough tested; upgrade/migrate/restore not validated; retain draft qualification |
| `docs/configuration/README.md` | v2.2.2 Core `config.html` and settings definitions | Configuration topics may overlap | 387 help and 449 unique historical anchors present, **content parity incomplete**; never use it to replace embedded legacy `config.html` |
| `docs/administration/README.md` | Newly written guide directory linking versioned topics | None reproduced | Navigation reviewed; not an exhaustive administrator manual |
| `docs/administration/users-and-groups/README.md` | v2.2.2 `admin/user.php`, `admin/group.php`, `lib-security.php` | Wiki topics not directly reprinted | Selected rights and CSRF checks source-linked; runtime permissions UI tests pending |
| `docs/administration/backup-and-recovery/README.md` | v2.2.2 `admin/database.php`, `dbbackup.class.php` | None reprinted | Source-backed Root/MySQL backup restrictions; full restore drill outstanding |
| `docs/administration/maintenance/README.md` | v2.2.2 install HTML, admin/database sources | None reprinted | Upgrade path not yet tested end to end |
| `docs/administration/troubleshooting/README.md` | v2.2.2 install/config HTML, database handler | Old error references only | Examples are diagnostic guidance, not verified fixes for all hosting platforms |
| `docs/development/plugin-api/README.md` | v2.2.2 `system/lib-plugins.php` | `Plugin_API`, `Functions.inc_-_Listing_of_the_Plugin_Functions`, `Plugin_Autoinstall`, `Adding_Moderation_Capability`, `Integrating_the_Comment_Engine` | **Corrected:** deprecated `PLG_install` invokes `plugin_install_*`; `PLG_getParams` retrieves `plugin_autoinstall_*` metadata. Callback parameter contracts and historical authors/license remain open |
| `docs/development/templates/README.md` | Release-scoped overview, with unverified specifics clearly qualified | `Caching_Template_Library`, `Theme_Developers_Guide` | Theme paths, caching behavior and API signatures need source/runtime validation |
| `docs/development/webservices/README.md` | v2.2.2 `system/lib-plugins.php`, Atom entry points | `Webservices_API` (Geeklog 1.5) | Dispatcher existence source-backed; supported routes/authentication behavior still untested |
| `docs/development/configuration-api/README.md` | v2.2.2 `system/classes/config.class.php` and install definitions | `AddToConfiguration` (Geeklog 1.7.x) | Method signature/source supported; code/upgrade example and Wiki attribution pending |
| `docs/development/security-and-permissions/README.md` | v2.2.2 `system/lib-security.php`, admin handlers | Older Wiki security practices not imported | Signatures verified, plugin-level authorization tests outstanding |
| `docs/plugins/static-pages/README.md` | New operational overview; no unreviewed PHP examples | `Static_Pages_Plugin` | Exact version 2.2.2 options and source attribution need verification; PHP execution remains explicitly discouraged |

## Confirmed code-review finding — 2026-11-05

Review of the tagged `system/lib-plugins.php` established that the earlier plugin guide mistakenly mapped `PLG_install()` to `plugin_autoinstall_<name>`. The source explicitly marks `PLG_install()` deprecated since 1.6.0 and calls `plugin_install_<name>`; `PLG_getParams()` consults `plugins/<name>/autoinstall.php` and invokes `plugin_autoinstall_<name>` if present. Corrected in the unified branch. Independently rechecked signatures of `SEC_hasRights`, `SEC_inGroup`, `SEC_createToken`, `SEC_checkToken`, `Configuration::add` and `PLG_invokeService` against tag v2.2.2.

## Attribution and release decision

**Current decision: not yet cleared for unqualified official publication.**

Before the final upstream PR is marked ready:

1. Locate the original Geeklog Wiki licensing notice from a verified snapshot or maintainer records, and the authors/edit histories for any article whose wording or code is to be reused. Do not guess a Creative Commons or GPL license. Where clearance cannot be demonstrated, **replace any copied expression with newly authored source-based explanation**, and do not reuse graphics.
2. Record actual credits/license notices for any material adapted from a specific historical contributor. Seek upstream maintainer approval on how to credit the bundled documentation and Markdown editorial contributions.
3. Verify high-impact developer API claims and version-specific administration operations against the v2.2.2 tag and reproducible staging tests; mark unverified claims as examples or scope-limited drafts.
4. Confirm every guide links to correct versioned resources and that the generated online and embedded HTML build passes all link and archive gates.
5. Confirm the new ZIP overlay in an isolated real Geeklog 2.2.2 admin session, including plugin help and rollback. The automated temporary-filesystem overlay check is *not* this integration test.
6. Keep the repository's `README.md` and site banners honest: legacy Core and plugin configuration references are preserved and the historical Wiki has not been fully migrated.

**Do not block a useful 2.2.2 delivery on an exhaustive 351-page Wiki rewrite.** Deliver a clearly version-scoped first edition with only reviewed claims and source-based new prose; track the remaining Wiki migrations as editorial backlog rather than silently importing them.
