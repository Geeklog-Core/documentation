# Plugin installation and management

> **Geeklog 2.2.2 administration guide — release-specific procedures to verify.** This is a safe planning and acceptance checklist, not a substitute for a plugin's own installation or upgrade instructions.

## Before installing

A plugin can change database tables, permissions, templates, configuration and public routes. Record the **exact plugin version**, supported Geeklog versions and required PHP/database features before installing it.

1. Read the plugin's release notes and supported upgrade path.
2. Identify which files, database tables, features and groups it introduces.
3. Back up application files and the database; verify the backup in an isolated restore rehearsal.
4. Install and exercise the plugin in a separate staging Geeklog instance.
5. Grant only the rights actually required by its administrators and editors.
6. Confirm the plugin's public pages, administration pages and any context-sensitive help links.
7. Record whether uninstall removes data and how rollback works before touching production.

## Upgrade acceptance matrix

| Stage | Expected evidence |
| --- | --- |
| Fresh install | Plugin shows the expected version and configured features |
| Upgrade | Existing plugin data, custom settings and compatible templates remain usable |
| Permissions | Authorized actions work; direct unauthorized requests are rejected |
| Help and navigation | Plugin documentation, public routes and admin links resolve |
| Disable/uninstall | Data retention and rollback behavior match the documented policy |

The Core [Plugin API](../../development/plugin-api/index.html) describes selected callback pathways. Those are for developers; they do not prove the installation procedure of a specific downloaded plugin.

## Locate the Geeklog 2.2.2 plugin manager

The [tagged plugin administration handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/plugins.php) lives at `public_html/admin/plugins.php`. It requires `plugin.edit` to enter. Additional operations use dedicated rights rather than granting every plugin administrator permission to install arbitrary code.

| Operation | Source-backed detail |
| --- | --- |
| Enter the Plugin Administration interface | Requires `plugin.edit` |
| Upload a plugin through Core administration | The upload form requires **both** `plugin.install` and `plugin.upload` |
| Install available plugin code | Installation is separately gated by `plugin.install` |
| Upgrade installed plugin code | Core invokes `PLG_upgrade()`; confirm dependencies and compatibility first |
| Enable, disable and uninstall | The Core handler exposes state transitions and uninstall paths; data retention depends on plugin implementation |
| Submit state-changing actions | Multiple actions use `SEC_checkToken()` as a CSRF check |

**Security note:** uploading a plugin grants a path to executing server-side PHP. Keep `plugin.upload` tightly restricted, review the source and provenance, and never assume the plugin package is safe because the administration interface accepted it.

### Example: inspect an installed plugin

1. Sign in with a dedicated authorized administrator and open Plugin Administration.
2. Record the plugin name, reported installed version, available code version and declared dependencies from the plugin interface where shown.
3. Check the release notes and the package metadata against the target Geeklog release.
4. Locate the plugin's configuration and contextual help. For the bundled plugins, use [Bundled Plugins Reference](../bundled-plugins/index.html).
5. Inspect the public/plugin administration functions with a low-privilege test user; do not use your privileged session as the only check.
6. Before updating, prepare a separate backup and a documented recovery path.

### Example: test an upgrade without risking production

1. Copy the site to an isolated environment, preserving the application's expected directories and database **without exposing production secrets**.
2. Record plugin/Core versions and install/upgrade requirements.
3. Apply the plugin's documented version-specific upgrade process through the supported administration workflow.
4. Verify its new version, configuration defaults, database migration effects, rights, routes and help pages.
5. Reproduce a permission-denied case and check that existing content remains intact.
6. Restore the staging snapshot to verify rollback rather than assuming that uninstall reverses every schema change.

**Source references:** [plugin administration](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/plugins.php), [plugin Core dispatcher](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/lib-plugins.php).

## Upgrade states and dependencies

The tagged [plugin manager](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/plugins.php) distinguishes upgrade, enable/disable and uninstall operations, invokes `PLG_upgrade()` for upgrade paths, and consults `PLG_resolveDependencies()` when processing plugin state. Treat an **installed plugin's recorded version**, its **available code version**, and its **dependencies** as separate facts.

For a routine maintenance review, record all three before changing the plugin:

| Question | Why it matters |
| --- | --- |
| Does the available code match the expected release? | A copied package may be newer than the installed database state |
| Are the dependencies satisfied? | Another plugin or Core capability may need to be present or enabled |
| Does this change upgrade data or settings? | A successful file copy does not prove database migrations succeeded |
| Is the plugin disabled or uninstalled? | Disabling may be reversible; uninstall behavior is plugin-specific |
| Can the previous state be restored? | Upgrade failure recovery must not depend on assumptions about uninstall |

**Do not edit the plugin database version field to force an upgrade.** Follow a plugin's documented migration pathway and validate with a disposable installation first.

## Plugin manager actions: reading is not upgrading

The tagged plugin manager exposes different operation branches:

| Administrator action | Handler / safety condition |
| --- | --- |
| Inspect installed plugin | `info_installed` returns plugin details |
| Inspect available plugin | `info_uninstalled` returns installation information |
| Install from available code | `autoinstall` path checks `plugin.install` and the CSRF token |
| Upload a package | File upload path checks `plugin.install`, `plugin.upload` and the CSRF token |
| Upgrade installed plugin | `updatethisplugin` route invokes the upgrade handler after token validation |
| Change load order | `change_load_order` route validates a token |

Always review the installed plugin's own migration logic and permissions before attempting these actions. The presence of a Core menu option does not establish that every third-party plugin works with that option.

**Important:** do not paste `mode` parameters or CSRF tokens into support messages. Use the normal administration interface, not constructed state-changing URLs.

**Source:** [plugin manager dispatch](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/plugins.php).

## Permission and lifecycle acceptance

- [ ] Plugin editor without upload/install permissions cannot reach package upload.
- [ ] Plugin install and upload operations are denied to roles lacking the respective rights.
- [ ] The allowed administrator can see the installed and code versions and declared dependencies where available.
- [ ] Fresh install and supported upgrade both preserve required site functionality.
- [ ] Disabling a plugin is distinguished from uninstalling it and deleting data.
- [ ] Backup restoration has been exercised before deploying the change to production.

These are planned manual acceptance cases. The existence of an API call is not proof a particular third-party extension's upgrade is safe.

## Troubleshooting safely

If an upgrade fails partway through, preserve logs and database state before retrying. Do not rerun destructive SQL, clear plugin records or change the Core database version blindly. Follow [Backup and recovery](../../administration/backup-and-recovery/index.html) and [Troubleshooting](../../administration/troubleshooting/index.html).

## Remaining verification

Document the exact bundled Geeklog 2.2.2 plugin administration screens and version-specific installation workflow against the release archive. A third-party extension requires its own source provenance, licensing and compatibility checks.
