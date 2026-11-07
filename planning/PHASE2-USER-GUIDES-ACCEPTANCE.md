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
