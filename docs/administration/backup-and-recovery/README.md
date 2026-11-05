# Back up and recover a Geeklog site

> **Geeklog 2.2.2 reference.** These procedures distinguish the built-in database export from a complete site backup. Rehearse restoration with your actual database, hosting environment and plugins before using the procedure in production.

## What must be backed up

A usable Geeklog backup normally needs **both** the database and the relevant site files, not just one SQL export. Include the Geeklog application configuration, site-specific modifications, uploaded media and plugin data. The exact file locations depend on how Geeklog was installed.

Store backups outside the publicly accessible web directory and protect them against unauthorized downloads. Database exports can contain private user data and credential-derived material.

## Built-in database backup facility

Geeklog 2.2.2 includes [`public_html/admin/database.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/database.php) and [`system/classes/dbbackup.class.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/classes/dbbackup.class.php).

The source confirms two important constraints:

- The database administration page requires the **`Root` group** (checked with `SEC_inGroup('Root')`).
- Its built-in database backup facility is restricted to installations whose `$_DB_dbms` is **`mysql`**. Do not assume the same facility works for PostgreSQL.

The backup file location is controlled by the configuration setting **`backup_path`**, documented by the bundled [configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html).

## Before relying on the administrator backup screen

The [Geeklog 2.2.2 database administration handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/database.php) checks `SEC_inGroup('Root')` and refuses unsupported database engines when `$_DB_dbms` is not `mysql`. It also checks whether `$_CONF['backup_path']` is writable before presenting or creating database backups.

A practical administrator preflight:

1. Confirm that you are using a separately authorized `Root` administrator account. Do not grant `Root` merely to make backups convenient.
2. Confirm the configured database engine. For a different engine, use that engine's supported backup tools rather than assuming the Geeklog page supports it.
3. Inspect the configured `backup_path` **outside the public document root**. The PHP worker needs only the necessary directory access; do not grant broad permissions to the whole site.
4. Verify available disk space and a protected destination for copying the resulting backup away from the web server.
5. Confirm that the exported file can be identified by date, checked for size and securely transferred. A readable SQL dump alone does not capture uploaded images or custom theme/plugin files.

A failed or empty export is not a recovery point. Resolve any directory-permission warning before an upgrade, without using `chmod -R 777`.

## Backup inventory to preserve

| Component | Why it matters | Verification |
| --- | --- | --- |
| Database export | Articles, users, settings and plugin-managed records stored in SQL | Check file size, export completion and successful import in staging |
| Core and private configuration files | Environment-specific paths and database connection settings | Store securely; never put credentials in public tickets |
| Uploaded media and files | Attachments and images often live outside the SQL dump | Compare file inventory and open representative media after restore |
| Installed plugins and themes | Custom code and templates must match the restored data | Record exact versions and compare plugin directories |
| Site-specific changes | Deployment settings, customizations and local assets | Record a manifest or protected file hashes |

## Making a backup

1. Decide whether this is a routine backup or the mandatory pre-upgrade backup. For an upgrade, arrange a maintenance window if necessary.
2. Use the installation's supported database backup feature or an administrator-approved database backup method appropriate for the active database engine.
3. Include the complete Geeklog file tree and custom assets, without exposing private configuration files to the public.
4. Keep enough backup history to recover from errors that are discovered only later.
5. Record the Geeklog, PHP and database versions alongside the backup date.
6. Verify that the SQL dump is complete and the files can be read; keep a second copy in a separate protected location.

Do not rely solely on a backup-success message. A backup is useful only when it can be restored.

## Restoring a site

**Perform a trial restoration in an isolated environment before recovering production.**

1. Choose a known-good backup and determine its matching software versions.
2. Prepare a separate database and safe, non-public file paths.
3. Restore the database using a method supported by the actual database engine, then restore the associated Geeklog files and uploaded assets.
4. Review database connection settings, URLs, permissions and any environment-specific secrets without copying secrets into logs.
5. Validate sign-in, posts, plugins, media, permissions and page links.
6. Only after the trial succeeds, plan a controlled production recovery with rollback options.

This guide does **not** claim that the 2.2.2 administration screen offers a complete one-click site restore. Database export and full-site recovery are distinct tasks.

## Verification status

- [x] Database backup page and class confirmed in the Geeklog 2.2.2 source.
- [x] `Root` restriction and `mysql` limitation confirmed in `admin/database.php`.
- [x] `backup_path` configuration key located in the bundled reference.
- [x] `SEC_inGroup('Root')`, `$_DB_dbms` and `backup_path` checks rechecked directly in tagged `public_html/admin/database.php`.
- [ ] A complete backup-and-restore drill performed against an isolated 2.2.2 installation.
- [ ] Database-engine-specific recovery steps tested.
- [ ] Historical Wiki reuse and attribution checked.
