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

## Troubleshooting safely

If an upgrade fails partway through, preserve logs and database state before retrying. Do not rerun destructive SQL, clear plugin records or change the Core database version blindly. Follow [Backup and recovery](../../administration/backup-and-recovery/index.html) and [Troubleshooting](../../administration/troubleshooting/index.html).

## Remaining verification

Document the exact bundled Geeklog 2.2.2 plugin administration screens and version-specific installation workflow against the release archive. A third-party extension requires its own source provenance, licensing and compatibility checks.
