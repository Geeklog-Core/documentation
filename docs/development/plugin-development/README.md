# Plugin development — step by step

> **Geeklog 2.2.2 developer workflow — no executable example certified yet.** Start with the tagged Core dispatcher and a maintained plugin of the same release. Historic Wiki callback examples may have changed or been deprecated.

## 1. Define a small feature contract

Describe one feature with the data it reads or writes, public route, administrator action, required role, configuration and upgrade behavior. Record how failures should be reported and how the plugin could be disabled or rolled back.

## 2. Study a release-matched plugin

Inspect the plugin tree, `functions.inc`, installation metadata, version and migration routines in a bundled or actively maintained plugin appropriate to your target release. Map the required Core dispatchers in [Plugin API](../plugin-api/index.html). Do not assume all callbacks are mandatory.

## 3. Implement with permissions first

Apply authorization on the server for every state-changing action and content read. Treat input as untrusted, escape output for its context, and use the release's supported database and CSRF token APIs. See [Security and permissions](../security-and-permissions/index.html).

## 4. Plan installation and upgrades

Document which configuration defaults, rights, database objects and templates the plugin adds. Test *fresh install* and *upgrade* independently; a setting registered for a clean installation may not automatically be created on existing sites. See [Configuration API](../configuration-api/index.html).

## 5. Test the plugin's lifecycle

| Scenario | Acceptance criterion |
| --- | --- |
| Fresh install | Expected settings/rights and no unexpected warnings |
| Supported upgrade | Data preserved, version recorded and recoverable failure path |
| Admin task | Authorized action succeeds; unauthorized direct request fails |
| Public view | No hidden or unpublished content leaks |
| Disable/uninstall | Site remains usable; documented retention policy respected |
| Compatibility | Relevant PHP version, theme and other plugins exercised in staging |

## 6. Document and release

Include an English README, installation and upgrade notes, compatibility target, permissions matrix, configuration options, troubleshooting, license and provenance, and recovery steps. Review source references before submitting a PR.
