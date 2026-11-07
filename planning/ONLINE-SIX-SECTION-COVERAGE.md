# Geeklog online documentation — six-section coverage and Wiki extraction backlog

**Updated:** 2026-11-07  
**Source branch:** `hostellerie/documentation:docs/online-troubleshooting-guide`  
**Release baseline:** Geeklog **2.2.2** only. **Embedded documentation for 2.2.3 is a separate milestone.**

## Current canonical public information architecture (2026-11-07)

The new public output contains **24 searchable guides and 25 HTML pages** (one homepage plus the guides). The existing **22 embedded modern guides and index** remain under `public_html/docs/english/modern/`. The public version publishes **no `modern/` directory, no root-level legacy `.html` routes and no redirect/compatibility pages**.

| Homepage section | Current public guides | Notes |
| --- | ---: | --- |
| Getting Started | 2 | Installation and configuration |
| User Guide | 5 | Beginner orientation, content, blocks, comments and feeds |
| Administration | 5 | Administration, users, backup, maintenance, **one merged Troubleshooting + FAQ guide** |
| Plugins | 3 | Plugin management, bundled extensions and Static Pages |
| Development & Theming | 5 | Plugin development, permissions, templates, theme development and contributing |
| Technical Reference | 4 | Database schema plus Plugin, Configuration and Webservices APIs |
| **Total** | **24** | Each public guide appears once in catalogue and search |

New URL examples: `/installation/`, `/configuration/`, `/user-guide/`, `/administration/troubleshooting/`, `/reference/plugin-api/`, `/reference/configuration-api/` and `/reference/webservices/`.

New navigation: **six compact section links**, page breadcrumbs, on-page contents, previous/next links in catalogue order and a visible five-step beginner learning path (install → configure → publish → manage users → back up).

The existing source `docs/administration/troubleshooting-faq/README.md` is retained for the historical embedded output; its editorial content was merged into the public `docs/administration/troubleshooting/README.md`. No historic embedded help URL was renamed.

**No redirects were requested or implemented.** Previously shared public URLs such as `/modern/...` and `/installation.html` will stop working after the updated upstream Pages deployment. Update links in external sites separately if needed.

Automated checks: `tools/check_public_routes.py`, existing generated-link/fragment checks, local HTTP preview and embedded ZIP preservation. They cannot replace a visual audit of the deployed site.

## Earlier site information architecture (historical snapshot, before public URL cleanup)

The counts and category labels in the section below describe the *previous* 25-guide/27-page output and are retained as project history, not as the current published target.

## Site information architecture

All **25** searchable guides are generated from Markdown and grouped into six sections on the public-site homepage. The three top-level content pages (installation, configuration and administration) plus 22 modern guides produce **27 HTML pages** in the online output (including home and the modern guide index). The same 22 modern guides are also included in the **23-page modern HTML subset** of the experimental, legacy-preserving 2.2.2 package.

| Top-level section | Guides | Editorial purpose |
| --- | ---: | --- |
| Getting Started | 2 | Install, upgrade, configure |
| User Guide | 5 | Content creation, publishing, navigation, discussion and syndication |
| Administration | 6 | Operations, accounts, backup, maintenance, diagnostics and FAQ |
| Plugins | 3 | Extension management, bundled plugins and Static Pages |
| Development & Theming | 8 | APIs, tutorials, templates, security and contributions |
| Reference & Archive | 1 | Data-model research and historical compatibility boundaries |
| **Total** | **25** | Each guide appears once in homepage catalogue and search |

## Twelve new guides created

**Important status convention:** `INITIAL ONLINE GUIDE` means new, original, task-oriented prose with explicit Geeklog 2.2.2 scope and listed verification needs. It does **not** mean feature-complete, live-tested or approved for 2.2.3.

| Priority | Guide | Markdown source | Section | Status / source gaps |
| --- | --- | --- | --- | --- |
| P0 | Using Geeklog: User Guide | `docs/user-guide/README.md` | User Guide | INITIAL ONLINE GUIDE; UI screenshots and role-specific workflows pending |
| P0 | Articles, Topics and Publishing | `docs/user-guide/articles-and-topics/README.md` | User Guide | INITIAL ONLINE GUIDE; real editor, scheduling and permission acceptance pending |
| P0 | Blocks, Menus and Navigation | `docs/user-guide/blocks-and-navigation/README.md` | User Guide | INITIAL ONLINE GUIDE; exact block/menu controls and theme variants pending |
| P0 | Comments and Moderation | `docs/user-guide/comments-and-moderation/README.md` | User Guide | INITIAL ONLINE GUIDE; moderator/admin workflows pending |
| P0 | Plugin Installation and Management | `docs/plugins/plugin-installation-management/README.md` | Plugins | INITIAL ONLINE GUIDE; release-specific admin UI and safe upgrade tests pending |
| P1 | Plugin Development: Step by Step | `docs/development/plugin-development/README.md` | Development & Theming | INITIAL ONLINE GUIDE; complete runnable sample plugin pending |
| P1 | Theme Development: Step by Step | `docs/development/theme-development/README.md` | Development & Theming | INITIAL ONLINE GUIDE; tagged-theme example and rendering acceptance pending |
| P1 | Syndication, RSS and Autotags | `docs/user-guide/syndication-rss-autotags/README.md` | User Guide | INITIAL ONLINE GUIDE; feed endpoints/autotag registry and permission behavior pending |
| P1 | Bundled Plugins Reference | `docs/plugins/bundled-plugins/README.md` | Plugins | INITIAL ONLINE GUIDE; detailed individual Calendar/Links/Polls/Spam-X/XMLSitemap/reCAPTCHA guides pending |
| P1 | Database Schema and Data Model | `docs/reference/database-schema/README.md` | Reference & Archive | INITIAL ONLINE GUIDE; **not** a verified current schema; must generate from tagged installer and plugin sources |
| P2 | Troubleshooting and FAQ | `docs/administration/troubleshooting-faq/README.md` | Administration | INITIAL ONLINE GUIDE; questions based on existing checked symptoms, with broader FAQ audit pending |
| P2 | Contributing to Geeklog | `docs/development/contributing/README.md` | Development & Theming | INITIAL ONLINE GUIDE; current repository maintainers must approve coding/review policy |

## Wiki source handling

The historical Geeklog Wiki snapshot reportedly contains **351 nonredirect article pages** (360 catalog rows counting redirects). **Only fourteen pilot articles were individually classified** in `planning/WIKI-PILOT-14-AUDIT.md`; the remaining 337 **have not** undergone editorial classification. This PR does not claim to have re-reviewed all 351.

| Checked historical title | Proposed location | Disposition |
| --- | --- | --- |
| `Plugin_API`; `Functions.inc_-_Listing_of_the_Plugin_Functions` | Plugin API and Plugin Development | Synthesize using tagged Core code, not wholesale copy |
| `Plugin_Autoinstall` | Plugin Installation and Management / Plugin Development | Recheck metadata and upgrade paths against 2.2.2 |
| `Adding_Moderation_Capability`; `Integrating_the_Comment_Engine` | Comments and Moderation / Plugin API | Recheck historical callbacks and permissions; do not reuse old examples without review |
| `Caching_Template_Library`; `Theme_Developers_Guide` | Theme Development and Templates | Recheck template paths and rendering APIs |
| `Static_Pages_Plugin` | Existing Static Pages guide | Continue source-checked modernization |
| `AddToConfiguration` | Configuration API | Old 1.7-era instructions require confirmation |
| `Webservices_API` | Webservices API | Historical Atom assumptions require source and runtime checks |
| `DatabaseSchema` | Database Schema and Data Model | Historical 1.4.1 SQL is **not** an authoritative 2.2.2 schema |
| `Coding_Guidelines` | Contributing to Geeklog | Historical conventions are not current maintainer policy |
| `Plugin_APIG2`; `Multi-Site_Setup` | Reference & Archive (historical only) | Do not publish as supported current API or configuration |

No unreviewed Wiki text, screenshots or SQL were copied into the new Markdown guides. Contributor attribution and the Wiki's reuse license remain unverified, as recorded in `planning/EDITORIAL-PROVENANCE-REVIEW-222.md`.

## Generation and validation

- `tools/build_modern_pilot.py` now generates **22** modern guides and an index (23 modern HTML pages) from source, including two contextual next-step links per guide (**44** links).
- `tools/build_site_search.py` indexes **25** sources and enforces exact-once membership across **six** homepage categories.
- `tools/build_dual_preview.py` produces **27** online HTML pages and preserves the existing legacy 2.2.2 Core help pages in the experimental overlay.
- `tools/check_delivery_readiness.py`, `tools/check_http_preview.py` and `tools/audit_online_guides.py` use the expanded 25/22/27-guide/page inventory.
- [Successful branch CI #42321389316](https://github.com/hostellerie/documentation/actions/runs/42321389316): **751 online local links**, **41 online fragments**, **660 embedded modern local links**, **44 contextual links** and **79 external reference occurrences inventoried**.

The automated checks validate generated HTML, local navigation and packaging **not** browser usability, historical Wiki licenses, live external websites or plugin/administrator runtime behavior.

## Acceptance work before publication

1. Visual QA of the six-category homepage and nested 25-guide navigation (mobile, keyboard, focus, search).
2. Content review of each new P0 guide against the pinned Geeklog release and real administration workflows; remove uncertainty only after verifying.
3. Confirm remaining Core feature and API details, historic Wiki rights and any migrated code examples.
4. Decide whether the top-level `docs/index.md`, `docs/install.md`, `docs/config.md` compatibility prototypes need a clearer archive/deprecation label; they do not generate the six-section homepage.
5. Review a single substantive online PR only when the contribution is ready; have the upstream maintainer merge and manually trigger official Pages deployment.
6. Maintain Geeklog 2.2.3 embedded documentation as independent P1 release integration with version-specific help-anchor acceptance.
