# Back up and recover a Geeklog site

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

## Define recovery objectives before choosing a backup process

A backup procedure is only useful if it matches the site's recovery needs. Decide what would be lost if the most recent backup were unavailable and how long the site could reasonably remain offline. Record these as operational objectives; the Geeklog 2.2.2 built-in export does not enforce them automatically.

For each backup set, store a protected manifest containing:

| Field | Record |
| --- | --- |
| Application and data versions | Geeklog release, plugin versions, PHP and database engine |
| Backup scope | Database, private configuration, uploads, themes, plugins and other customized files |
| Export location | Protected location outside the publicly served web tree |
| Integrity evidence | Timestamp, file inventory and checksums for the artifacts created |
| Recovery dependency | Required database engine, extensions, permissions and relevant encryption keys |
| Restoration evidence | Date and result of the latest **isolated** restore drill, including what was not tested |

A checksum confirms that an artifact matches a recorded byte sequence; **it does not prove that the data is complete or restorable**. Protect the manifest if it contains sensitive paths or infrastructure details.

## Isolated restore rehearsal and acceptance

Conduct this test with separate infrastructure and sanitized data whenever possible. Do not overwrite a live database, change the production site's URLs, or point a staging application at production services.

1. Verify the archive inventory and record the backup source release and database engine.
2. Restore into a **new, isolated database**, with independent credentials and no unexpected network access to production.
3. Restore matching application files, uploaded assets and configuration into a separate site directory.
4. Adjust only the staging-specific URL, connection, secrets and filesystem ownership settings using approved procedures; preserve a record of these changes outside the public tree.
5. Verify public and authenticated page loads, a representative article and media upload, plugin pages, and the configuration help links.
6. Verify that the intended administrator can access an allowed action while a lower-privilege staging account is denied a prohibited action.
7. Record errors, missing assets and elapsed recovery steps, plus any manual intervention needed.
8. Mark the backup set **restore-tested** only if these acceptance checks pass; otherwise record a failure and correct the backup process before relying on it for an upgrade.

The initial restore is not a substitute for auditing application-specific integrations, scheduled jobs, mail delivery or third-party services. Document those as separate checks where applicable.

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
