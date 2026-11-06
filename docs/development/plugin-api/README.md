# Geeklog plugin API — developer guide

> **Version scope: Geeklog 2.2.2.** This guide introduces the Core plugin dispatchers and links them to tagged source code. It is a practical reference, not a complete API contract: verify callback signatures and parameters in the installed release before implementation. Historical Wiki topics are noted for provenance but their wording and code have not been republished.

## How plugins integrate

Geeklog exposes core-level `PLG_*` dispatch functions. A plugin commonly implements optional callbacks named `plugin_<event>_<pluginname>` to participate in an operation. **Do not assume a one-to-one mapping**: a core dispatcher can choose more than one callback, and some events do not propagate to every plugin.

Start with [Geeklog's source](https://github.com/Geeklog-Core/geeklog). Examine the source for your **specific release**; this page is an overview, not a substitute for release-specific signatures.

## Plugin lifecycle

Historically documented callback families include:

| Area | Example callback | What to inspect |
| --- | --- | --- |
| Installation and upgrades | `plugin_autoinstall_<name>` | Required metadata and installation steps for the selected release |
| Upgrade | `plugin_upgrade_<name>` | Upgrade/version comparison and database migrations |
| Uninstallation | `plugin_uninstall_<name>` or `plugin_autouninstall_<name>` | Data cleanup semantics and administrator confirmation |
| Plugin search | `plugin_dopluginsearch_<name>` | Current search interface and access filtering |
| Moderation | `plugin_submissioncount_<name>`, `plugin_moderationapprove_<name>` | Submission queue and permissions |
| Comments | `plugin_displaycomment_<name>` | Current comment lifecycle |
| Statistics | `plugin_showstats_<name>` | Which statistics are exposed |

This table identifies **documented historical callbacks**, not confirmation that every one remains supported unchanged in Geeklog 2.2.2.

## Verification against Geeklog 2.2.2

The following **dispatcher-to-callback mappings were checked directly in the tagged Geeklog 2.2.2 source**, `system/lib-plugins.php` at [`v2.2.2`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/lib-plugins.php):

| Core dispatcher or installation mechanism | Callback referenced by Core |
| --- | --- |
| `PLG_install()` — **deprecated** | `plugin_install_<name>` (legacy callback; deprecated dispatcher) |
| `PLG_getParams()` — auto-install metadata lookup | `plugin_autoinstall_<name>` loaded from `plugins/<name>/autoinstall.php` when present |
| `PLG_upgrade()` | `plugin_upgrade_<name>` |
| `PLG_uninstall()` | `plugin_autouninstall_<name>` (auto path) or `plugin_uninstall_<name>` (legacy path) |
| `PLG_doSearch()` | `plugin_dopluginsearch_<name>` |
| `PLG_getSubmissionCount()` | `plugin_submissioncount_<name>` |
| `PLG_approveSubmission()` | `plugin_moderationapprove_<name>` |
| `PLG_displayComment()` | `plugin_displaycomment_<name>` |
| `PLG_getPluginStats()` | `plugin_showstats_<name>` when applicable |

**Important 2.2.2 distinction:** `PLG_install()` is marked deprecated since Geeklog 1.6.0 in the tagged source and calls `plugin_install_<name>`, not `plugin_autoinstall_<name>`. The `plugin_autoinstall_<name>` callback is accessed through `PLG_getParams()` when `autoinstall.php` exists. These are separate pathways and must not be conflated.

This confirms that **Core references these callback names** in 2.2.2. It does **not** establish every callback's full parameter contract, required implementation, availability in later Geeklog versions, or safety of older Wiki examples. Those remain release-validation tasks.

## Files and organization

Historically, plugin files reside under `plugins/<pluginname>/`, including `functions.inc`. The auto-install integration described in the old Wiki uses `autoinstall.php` in the same plugin directory. Review the plugin skeleton actually distributed with your Geeklog release before creating files.

## Installation metadata and permissions

The recovered `Plugin_Autoinstall` article describes installation metadata for plugin name, version, compatible Geeklog version and homepage, alongside optional groups, features, mappings and table registrations. If you are implementing this interface:

1. Review an actively maintained core plugin at the same release version.
2. Choose a stable internal plugin name and version.
3. Use the framework's supported setup and upgrade hooks instead of running untrusted SQL directly.
4. Declare only required permissions and groups.
5. Test installation, upgrades, enable/disable and uninstallation in a disposable environment.
6. Document whether removal preserves or deletes plugin-specific data.

**Security:** Never copy historical code samples directly into production without reviewing database permissions, input validation, output escaping, CSRF protection and access checks.

## Moderation, comments, search and templates

The Wiki describes callback families for submitted content, comments, search, and statistics. Implement only callbacks used by your chosen release. Check that each operation enforces permissions at the server, not only through hidden interface elements.

See the future dedicated guides for plugin installation, moderation and comment integration. They should reuse this page rather than duplicating API lists.

## Plan a plugin change before implementing callbacks

A reliable extension starts with a narrow feature contract, not with copying a historical example. For each intended operation, record the user action, owning plugin, required permissions, data touched, expected Core dispatcher and test scenario.

| Work item | Questions to answer before coding |
| --- | --- |
| Installation | Which files and database objects are created? How can a partially completed install be detected safely? |
| Upgrade | What is the supported source version? Is a backup required? Can an upgrade be repeated after interruption without duplicating data? |
| Uninstallation | What is deleted, retained or exported? Is the action visible and explicitly confirmed by the administrator? |
| User-facing output | Are permissions checked in the request handler and is untrusted content escaped for the output context? |
| Search integration | Do search results respect each item's visibility and publication status? |
| Moderation/comments | Can unauthorized submissions or approvals be rejected server-side? Are state transitions recorded? |
| Configuration | Which options are versioned, and how are upgrades from older plugin settings handled? |

A callback's name alone is not its API contract. Read the actual dispatcher implementation in [`system/lib-plugins.php` for Geeklog 2.2.2](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/lib-plugins.php) and a maintained plugin's implementation for the same release. Record parameters, return values and error-handling expectations only after verifying them.

## Practical staging acceptance matrix

Run these checks on an isolated Geeklog site with **disposable data** before releasing an extension.

| Stage | Successful outcome to verify | Failure path to exercise |
| --- | --- | --- |
| Fresh install | Plugin activates with expected metadata and rights | Missing prerequisite or failed installation step is reported without leaving an unsafe partial state |
| Upgrade | Existing configuration and data remain usable | Interrupted/unsupported upgrade leaves a recoverable backup and a clear error |
| Administrator UI | Authorized user can perform the intended action | Direct request without the required permission is rejected |
| Public view | Intended anonymous and registered audiences see only permitted content | Private or unpublished content does not appear in direct links or search |
| Submission or comment | Valid action follows the configured moderation workflow | Unauthorized or invalid submission is rejected |
| Disable/uninstall | Site remains operational and documented retention policy is respected | Re-enable or restoration path is understood before deleting data |

**Do not** treat the presence of a plugin's HTML help page, a visible administrator menu or a successful PHP syntax check as proof that these runtime paths have been tested.

## Document the plugin alongside its source

For a maintainable plugin, keep an English README or documentation section that describes its compatibility target, installation/upgrade procedure, configuration, permissions, user workflows, known limitations and recovery method. Refer to the [security and permissions guide](https://geeklog-core.github.io/documentation/modern/development/security-and-permissions/index.html) and the [configuration API guide](https://geeklog-core.github.io/documentation/modern/development/configuration-api/index.html) rather than duplicating unverified PHP examples.

When Geeklog 2.2.3 becomes the integration target, repeat callback and plugin-version checks against the actual tagged release. The 2.2.2 mappings in this page should remain labelled historical until that verification is complete.

## Compatibility checklist

- [x] Dispatcher mapping for `PLG_install()`, `PLG_getParams()` and `PLG_upgrade()` rechecked against the Geeklog v2.2.2 tagged source
- [ ] Complete callback parameter contracts checked against the target Geeklog release
- [ ] Installation and upgrade rehearsed in staging
- [ ] All code examples tested with the target PHP/runtime
- [ ] Permission/CSRF checks reviewed
- [ ] Legacy Wiki links mapped to final anchors
- [ ] Attribution and reuse license approved

**Source provenance:** new release-scoped synthesis informed by topic titles from the recovered 2024-11-02 Geeklog Wiki backup (titles above) and the tagged Geeklog v2.2.2 source. Original Wiki text, page contributors and reuse license still require verification before any verbatim republication. See `planning/EDITORIAL-PROVENANCE-REVIEW-222.md` in the source repository.
