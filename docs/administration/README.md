# Geeklog 2.2.2 administration

> **Geeklog 2.2.2 reference.** This page brings together the available administration guides. The bundled configuration and plugin help files remain the reference for historical settings and their context-sensitive help links until their complete migration has been reviewed.

## Start here

Geeklog administration features depend on your account permissions and enabled plugins. Sign in with an authorized account and verify the installed Geeklog release before changing configuration or running upgrades.

| Topic | Guide | What it covers |
| --- | --- | --- |
| Users and groups | [Manage users and groups](modern/administration/users-and-groups/index.html) | Account access, roles, feature rights and account maintenance |
| Backup and recovery | [Back up and recover a site](modern/administration/backup-and-recovery/index.html) | File/database backups and safe recovery preparation |
| Maintenance and upgrades | [Maintain or upgrade Geeklog](modern/administration/maintenance/index.html) | Release review, prerequisites and upgrade checks |
| Troubleshooting | [Diagnose common problems](modern/administration/troubleshooting/index.html) | Logging, permissions, configuration and error investigation |
| Configuration reference | [Geeklog configuration](configuration.html) | Release-scoped setting descriptions and historical anchor links |
| Installation and migration | [Install, upgrade or move a site](installation.html) | Installation wizard, upgrades and migration guidance |
| Static Pages | [Static Pages plugin](modern/plugins/static-pages/index.html) | Managing standalone pages and plugin-specific permissions |

All linked guides are generated from the maintained Markdown tree. Release-specific configuration details should be checked against the installed version.

## Configuration and help links

In Geeklog 2.2.2, configuration fields can point to anchors such as `docs/english/config.html#desc_site_url`. **Keep those embedded links and historical anchors available.** The online Markdown configuration reference has structural anchor coverage but does not yet reproduce all original tables, examples and defaults. Do not treat it as a complete replacement for the bundled `config.html`.

Plugin configuration may use a plugin-specific help path; in particular, reCAPTCHA documentation is stored under `public_html/admin/plugins/recaptcha/docs/`, not alongside all the other Core plugin HTML pages.

## Before making administrative changes

1. Confirm the exact Geeklog, PHP, database and plugin versions.
2. Use an appropriately authorized account; never assume that hiding a menu item enforces permissions.
3. Back up both site files and the database before upgrades or consequential configuration changes, and verify the backup can be restored.
4. Perform upgrades, migrations and risky plugin experiments in an isolated environment before touching a production installation.
5. After a change, verify the public site and administrative pages, including the context-sensitive documentation links.
6. Do not expose installer directories, passwords, API tokens or database credentials in public help requests.

## Documentation status

This is a practical directory to the currently available Geeklog 2.2.2 guides, **not a claim that every historical Wiki page or Core/plugin reference has already been migrated**. Historic embedded documents remain available while their equivalents are reviewed. Where a modern guide is marked as a draft, verify code snippets and behavior against the [tagged Geeklog 2.2.2 source](https://github.com/Geeklog-Core/geeklog/tree/v2.2.2).
