# Phase 2 — User documentation: source review and staging acceptance

**Date:** 2026-11-07  
**Baseline:** Geeklog **v2.2.2** tagged Core; not a certification of v2.2.3  
**Scope:** Documentation content improvements only; visual audit of the public documentation website intentionally deferred.

## Scope delivered

Five existing P0 guides have been expanded, without replacing the newly published six-section/25-guide architecture:

| Guide | New source-backed detail | Manual acceptance still needed |
| --- | --- | --- |
| Using Geeklog | Task routing: submission, privileged article edit, topics, blocks, moderation and plugins | Test ordinary reader/contributor/editor navigation in the actual theme |
| Articles, Topics and Publishing | Differentiate `submit.php`, `admin/article.php`, `admin/topic.php` and moderation queues; rights `story.edit`, `topic.edit`, `story.moderate` | Create a real draft, publish an allowed story, reject a restricted edit |
| Blocks, Menus and Navigation | Handler `admin/block.php`, `block.edit`, `block.delete`, CSRF checks; distinguish theme menus from blocks | Create, reorder, enable, hide and delete a disposable block in staging |
| Comments and Moderation | Separate conditional article/draft/comment queues and `comment.moderate`; CSRF | Moderate test comments, check anonymous visibility and denied requests |
| Plugin Installation and Management | Core plugin manager rights `plugin.edit`, `plugin.install`, `plugin.upload`, `PLG_upgrade` flow | Exercise read-only inspection, install/upgrade and rollback with test plugins |

## Source references checked in tagged Geeklog 2.2.2

- [`public_html/submit.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/submit.php) — story submission and submission/preview workflows.
- [`public_html/admin/article.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/article.php) — checks `story.edit`.
- [`public_html/admin/topic.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/topic.php) — checks `topic.edit`, uses token validation on state-changing actions.
- [`public_html/admin/block.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/block.php) — checks `block.edit`, with separate delete rights and protected changes.
- [`public_html/admin/moderation.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/moderation.php) — differentiates story/comment moderation, draft-list configuration, plugin queues and token-checked actions.
- [`public_html/admin/plugins.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/plugins.php) — checks plugin editing, installation/upload rights, token checks and upgrade dispatcher.
- [`system/lib-security.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/lib-security.php) — feature-right checks and token routines.

The guide additions are **original explanations**, not copied historical Wiki prose. Their examples are learning exercises, not claims of completed PHP/runtime tests. Individual plugin install/upgrade behavior depends on that plugin and its version.

## Staging test protocol (pending, not completed)

1. Use a **disposable** Geeklog 2.2.2 installation and a restored test database that contains no personal production data.
2. Prepare at least four roles: anonymous visitor; ordinary member/contributor; topic/story editor; appropriately authorized moderator/plugin administrator.
3. Exercise each guide's checklist, recording exact account rights, configured moderation options, theme, plugin versions, results and any differing UI labels.
4. Perform at least one **denied direct request** to each tested administration route as an unauthorized account, plus one allowed state-changing operation.
5. Exercise a complete backup/restore before plugin upgrade tests. Never use the real production database for destructive tests.
6. Redact screenshots and diagnostic logs before attaching them to PR review.
7. If the UI or behavior differs from the source-based model, correct the guide; only then remove any remaining unverified label.

## Exit criteria for phase 2

- [x] All five P0 guides include concrete tasks, source links and clear role boundaries.
- [x] Code references point to an immutable Geeklog v2.2.2 tag rather than a changing branch.
- [x] The published 25-guide structure remains unchanged.
- [ ] CI must succeed for the new branch's generated online/embedded output.
- [ ] Actual staging results and screenshots must be documented before claiming UI acceptance.
- [ ] Geeklog v2.2.3 acceptance is a distinct release-scoped task.

**Explicitly deferred:** visual audit of the public docs site, complete historical Wiki classification and 2.2.3 embedded-help integration.

## Second source-review pass — date controls, block variants and plugin lifecycle

Further work on Geeklog v2.2.2 tagged code and its documented edit handlers expands three P0 pages without claiming completion of any UI session:

- **Articles and topics:** `public_html/admin/article.php` defines publication and expiration date controls and the four audience permissions (owner/group/members/anonymous); `public_html/admin/topic.php` defines a parent topic and inheritance option. A staging exercise now records actual scheduled publication and resulting visitor visibility rather than guessing how timing is implemented.
- **Blocks and navigation:** `public_html/admin/block.php` recognizes `normal`, `portal`, `phpblock`, `gldefault` and obtains supported additional locations through `PLG_getBlockLocations()`. Documentation describes the type distinction and limits executable PHP blocks to developer-reviewed use.
- **Plugin installation and management:** `public_html/admin/plugins.php` distinguishes code version, installed version, dependencies, enable/disable, upgrade and uninstall; the text explains why uninstall and file replacement are not automatically a safe rollback.
- **Repeatable documentation regression:** `tools/check_p0_user_guides.py` is run by `.github/workflows/dual-preview.yml` after the generated-site audit. It checks that all five existing P0 Markdown and HTML guides retain their version-pinned sources, key rights, procedural headings and unchecked staging items. This is **static documentation acceptance only**, not proof that PHP operations or role-based behavior passed a real installation test.

**Outstanding hands-on checks:** scheduling/expiration, parent-topic inheritance and effective access, permitted block positions in different themes, PHP/portal block security controls, plugin upgrade dependencies and restore/rollback scenarios. Audit of the live public documentation website remains deferred.

## Third source-review pass — P0 workflow distinctions

The following behavior was cross-checked directly in **Geeklog v2.2.2** PHP source, not through an executed administration session:

- The public `submit.php` route redirects users with `story.edit` toward the privileged editor for the normal story route. Submission validation also includes login-required options, topic selection, spam checks and a submission speed limit. `STORY_SAVED` and `STORY_SAVED_SUBMISSION` follow different redirect paths; the displayed result is not definitive proof of anonymous visibility.
- Topic saves in `admin/topic.php` validate the parent topic, reserved/duplicate identifiers, archive restrictions and rights on both target and parent; `TOPIC_ROOT` is a Core constant and should not be treated as a normal editable topic.
- Block saves in `admin/block.php` distinguish enabled state, audience permissions, device, theme/plugin placement, autotag settings and content type; the four named block types do not imply that arbitrary PHP code is an acceptable editor input.
- The moderation dashboard `admin/moderation.php` is protected by `SEC_hasModerationAccess()` and composes different story, draft, comment and plugin queues. Absence of a queue is not evidence of lost data.
- The plugin manager `admin/plugins.php` distinguishes read-only information actions (`info_installed`, `info_uninstalled`) from installation, upload, upgrade and load-order actions with differing rights and CSRF checks. Exact plugin migration outcomes remain plugin-specific.

**CI enhancement:** `tools/check_p0_user_guides.py` now guards these five workflow distinctions in Markdown and generated online HTML. This catches accidental removal of the corresponding explanations, not behavioral changes in PHP.

**Next action:** reproduce the P0 scenarios on a disposable Geeklog 2.2.2 site using specific test roles and record screenshots only after redacting private data. The user-requested live-site visual audit remains postponed. No PR has been opened for the phase 2 branch.

## Reproducible staging test matrix

The machine-readable [PHASE2-STAGING-SCENARIOS.csv](PHASE2-STAGING-SCENARIOS.csv) contains **22** case IDs covering anonymous visitors, contributors, editors, topic/block administrators, moderators and plugin administrators across all five P0 guides.

Each case captures a role, precondition, user action, expected behavior, tagged Core source path, execution status and evidence reference. All cases start as `NOT_RUN`. On execution, replace the status with `PASS`, `FAIL` or `BLOCKED` and add a sanitized evidence reference; do not mark any case as passed merely because its PHP handler exists.

The `tools/check_p0_user_guides.py` regression check now validates the CSV schema, unique IDs, role and guide coverage, allowed statuses and the requirement to provide evidence for any result other than `NOT_RUN`. This does not run the application or execute the scenarios; it makes future manual test results more auditable.

### Recommended execution sequence

1. Provision a disposable 2.2.2 site with isolated database and test users, then record configuration and theme.
2. Run safe read-only and anonymous checks first, followed by authorized edits in disposable content.
3. Run denied access / invalid-token cases **only in isolation** and avoid public endpoints or live user data.
4. Take a backup before destructive plugin cases and verify restoration.
5. Record the result and exact evidence for each case, plus any divergence requiring guide correction.
6. Keep the online public-site visual audit deferred until this workstream is complete.

## Practical tutorials completed in draft (2026-11-07)

Seven existing Markdown guides now contain structured, **step-by-step worked exercises**, original sample content, prerequisites, observable outcomes, troubleshooting and links to tagged Geeklog 2.2.2 Core source:

| Guide | Practical lessons |
| --- | --- |
| Using Geeklog | Four-part beginner course: discover roles, publish a story, add a block and standalone page, moderate and maintain |
| Articles and topics | Draft a story, submit as a contributor, approve with editorial rights, create parent/child topics, troubleshoot missing stories |
| Blocks and navigation | Create a normal information block, add a useful link, diagnose missing blocks |
| Comments and moderation | Submit a comment, approve a moderated comment, review a contributed story |
| Syndication, RSS and autotags | Create a Core RSS feed, safely insert a verified autotag, subscribe to existing public feeds |
| Plugin installation and management | Inspect a plugin, install a verified plugin on staging, test upgrades and recovery |
| Static Pages | Publish an About page, verify anonymous visibility, clone a disposable page safely |

**New tagged source reviewed:** `public_html/admin/syndication.php` for `syndication.edit`, title/description/file/format inputs, RSS 2.0 defaults and token-checked actions; `system/lib-plugins.php` for autotag parsing and installed-plugin dependent tags; `public_html/admin/plugins/staticpages/index.php` for `staticpages.edit`, `staticpages.delete`, `staticpages.PHP` and editor/clone operations. Earlier source review remains applicable to article, topic, block, moderation and plugin manager handlers.

**New CI test:** `tools/check_practical_tutorials.py` checks the seven Markdown/HTML pages for the added walkthroughs, source anchors, substantive numbered steps, permission hints and explicit staging caveats. It is invoked in `dual-preview.yml`. The original `tools/check_p0_user_guides.py` and 22 `NOT_RUN` staging scenarios remain intact.

**Editorial status:** first complete drafts of practical tutorials, **not live UI tested**. Interface labels, plugin behavior, themes, feed paths and publishing settings still require execution against a disposable Geeklog 2.2.2 installation. The user explicitly deferred the visual audit of the public documentation website. No phase-two PR is opened yet.

## Finalized seven-guide staging coverage

The acceptance matrix now has **30** test cases: the original 22 scenarios across five initial P0 guides plus **8** for syndicated RSS/autotags and Static Pages. New roles include `feed_admin` and `staticpages_editor`; tagged `system/` paths can be used as source references alongside `public_html/`.

New cases cover RSS feed creation and restricted administration, autotag rendering without access leakage, anonymous feed consumption, Static Page publication, denied editor access, cloning and the `staticpages.PHP` privilege boundary.

Every case remains `NOT_RUN` until execution with sanitized evidence; static CI validates the matrix structure and documented tutorials but **does not imply a successful manual test**.

## Proposed PR review boundaries

- This is a **content-focused documentation PR**: seven enriched tutorials, references to tagged Geeklog v2.2.2 sources, two documentation validation scripts and staging checklists.
- No changes to Geeklog Core PHP, the published 25-guide information architecture or the original embedded 2.2.2 configuration help.
- Do not claim final compatibility with Geeklog 2.2.3, complete historical Wiki migration, or browser/administrative staging certification.
- The public site's visual audit remains postponed by explicit project decision.
