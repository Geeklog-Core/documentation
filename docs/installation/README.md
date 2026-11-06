# Installing, upgrading and migrating Geeklog

> **Migration draft — not yet authoritative.** Adapted from the Geeklog Core `install.html` bundled with the source tree (which describes Geeklog 2.2.2). Check your own release package, current installation wizard and release notes before following these instructions in production. A new-install walkthrough was exercised on isolated Geeklog 2.2.2 (PHP 8.1.33, MariaDB 10.11); the site and authenticated administration work, but final plugin and post-install security acceptance remain pending.

<a id="glossary" name="glossary"></a>

## Sections

[Requirements](#installation_requirements) · [New installation](#install) · [Upgrading](#upgrade) · [Moving a site](#migrate) · [Troubleshooting](#installprob)

## Glossary

- **Directory:** a filesystem folder.
- **Path:** a location on the server, such as `/var/www/`.
- **URL:** a web address, such as `https://example.com/`.

<a id="public_html" name="public_html"></a>

**Web root (`public_html`):** the directory whose files can be served publicly by the web server. Hosting providers may instead call it `htdocs` or `www`.

<a id="installation_requirements" name="installation_requirements"></a>

## Installation requirements

<a id="preinstall" name="preinstall"></a>

### Required software

You need a web server, a compatible PHP version with the necessary extensions, and a supported database engine (MySQL/MariaDB or PostgreSQL). The [Geeklog 2.2.2 release notes](https://github.com/Geeklog-Core/geeklog/releases/tag/v2.2.2) state historical minimums of PHP 5.6.4, MySQL 4.1.2 and PostgreSQL 9.1.7, and explicitly mention PHP 8.1 support. **The tagged installer source instead declares MySQL 4.1.3**; this discrepancy has not been resolved. These old versions are **not secure deployment recommendations**. Use a supported runtime and database combination validated for your particular Geeklog release; do not infer compatibility with newer versions from a minimum-version check. See the [requirements source audit](https://github.com/Geeklog-Core/documentation/blob/main/planning/INSTALL-REQUIREMENTS-SOURCE-AUDIT.md) for the differing sources.

The legacy instructions mention PHP extensions including `mbstring`, `bzip2`, MySQL or PostgreSQL drivers, OpenSSL, JSON and `fileinfo`. Confirm the precise list against the selected release and its packaging.

For a new database, choose an appropriate character set/collation before adding content. The old document recommends UTF-8 (`utf8mb4` for MySQL); compatibility with your database version and locale should be confirmed.

<a id="things_you_should_know" name="things_you_should_know"></a>

### Things to know before starting

- Arrange for a database and credentials with the permissions needed by the installer.
- Make sure the public web root and Geeklog's **non-public system files** are placed safely: system files should ideally live outside the web root.
- Know where the web server's document root points and which filesystem permissions it uses.
- Use a private/staging installation to rehearse upgrades and migrations.

<a id="install" name="install"></a>

## New installation

The following summarizes the process described in the source HTML; version-specific steps must still be reviewed.

1. Obtain the intended Geeklog release archive from the official project and verify its provenance.
2. Extract the distribution archive with a reliable archive tool.
3. Create an empty supported database and an account with the required privileges.
4. Copy the archive's `public_html/` contents to your server's public web root.
5. Copy the **remaining Geeklog files** outside the public web root, ideally to its parent directory or another non-public directory. If the installer cannot find these files, it may ask for their location.
6. Open `https://YOUR-SITE/admin/install/index.php` (adjust the URL to your installation) and follow the installer.
7. When installation is complete, follow the release's post-install security instructions. The source document explicitly instructs administrators to **delete the `admin/install` directory** and change the administrator's default password.

### Configuration fields that are easy to confuse

- **Site URL** is a web address, for example `http://localhost:8083` in a private staging environment.
- **Admin Directory Path** is a misleading label in the Geeklog 2.2.2 wizard: the submitted field is `site_admin_url`, which must be a **web URL**, such as `http://localhost:8083/admin` (no trailing slash). **Do not enter** a filesystem path such as `/var/www/html/public_html/admin`.
- The actual filesystem admin directory in this example is `/var/www/html/public_html/admin/` and is distinct from the administrator URL.
- **Database Hostname** must resolve from the Web server. In Docker Compose a service named `db` uses `db` rather than `localhost` (which could make MySQLi attempt a nonexistent local socket).
- For MySQL/MariaDB with InnoDB, select the supported MySQL/InnoDB choice and use fresh database credentials. Never paste credentials into support logs.

### Writable paths and plugin post-installation

Geeklog 2.2.2's installer may recommend `chmod -R 777` for its preflight list. **Do not run it.** The actual PHP check is whether the Web-server account can write the selected paths (`is_writable()`). Give that account narrowly scoped ownership or group/ACL access, with standard restrictive modes (for example 0644 for writable files owned by the PHP worker, 0755 for writable directories owned by it) where appropriate to the deployment. Verify permissions as the **actual PHP worker**, not only as root. A Docker `exec` script receiving input from a heredoc needs `docker exec -i` if piping commands into the container.

The **XMLSitemap** plugin can attempt to create `public_html/sitemap.xml` in its post-install hook. This file may lie outside the installer's initial writable-path list; insufficient permission can cause a separate post-install warning even when Core tables and other plugins were successfully created. A secure deployment should arrange appropriate **file-specific** sitemap writing permissions (or deliberately omit/disable the optional plugin when appropriate), rather than make the entire public directory world-writable. Disabling a plugin after a partial installation does not mean its failed post-installation has been repaired.

### Interrupted installs: preserve state before retrying

An installation can populate tables and install plugins before a subsequent warning or rendering error appears. Do **not** blindly repeat the installer, remove tables, or edit the stored `database_version`. First check the real DB schema/version, plugin statuses, the Geeklog application log and the saved `site_url` / `site_admin_url` configuration. The 2.2.2 stage test yielded 43 tables and `database_version=2.2.2`, while administrative access failed because `site_admin_url` contained a filesystem path. Correcting that specific serialized configuration value restored the admin page without reinstalling. This is a **staging observation**, not a universally safe manual recovery procedure.


**Security note:** the source mentions a legacy fallback involving a protected subdirectory inside the web root. This draft does *not* recommend that approach without a separate security review of web-server access controls.

## Preflight checklist before installation or migration

This checklist complements the release-specific instructions above. Complete it before using an installer or changing a live site.

| Check | New installation | Upgrade or move |
| --- | --- | --- |
| Release and runtime | Confirm target Geeklog, PHP extensions and database compatibility | Record both source and target versions, enabled plugins and theme versions |
| Site and administrator URLs | Check web-address values separately from filesystem paths | Record existing URLs and identify any domain/path changes |
| Database | Prepare an empty database and installer-specific access | Verify a protected backup and a tested restore into a separate database |
| Files | Ensure the public and non-public Geeklog directories are placed correctly | Inventory custom code, uploads, private configuration and plugin assets |
| Permissions | Permit writes only where needed by the PHP worker | Review old ownership and ensure the installer cannot remain publicly available |
| Recovery | Keep a clean copy of the release files | Maintain a documented rollback path for files **and** database state |

**Go/no-go rule:** do not begin a production upgrade or migration if you cannot identify the matching backup, restore it safely in staging, or confirm the target release's compatibility. Passing the installer preflight is not a substitute for those checks.

## Post-install acceptance checklist

After the installer completes, check the site as a visitor and with an authorized staging administrator:

1. Confirm that the homepage, a representative article and a plugin page render without PHP errors.
2. Check `site_url` and `site_admin_url` are browser URLs and that administration links resolve to the correct location.
3. Confirm public CSS/images and representative uploaded media load from their intended paths.
4. Test sign-in and sign-out, then a permitted administrative action through the normal interface.
5. Follow an actual context-sensitive help link, including `docs/english/config.html#desc_site_url`, and verify it points to the correct setting.
6. Check active plugin statuses and error logs separately; a successfully rendered plugin help page does not establish plugin health.
7. Confirm the installer directory has been removed or secured as required by the release instructions, and that the installation's default credentials have been replaced.
8. Record the exact versions, checks performed and outstanding warnings. If any critical check fails, stop and investigate rather than deploying more changes.

The [troubleshooting guide](https://geeklog-core.github.io/documentation/modern/administration/troubleshooting/index.html) explains how to collect useful error evidence. The [backup and recovery guide](https://geeklog-core.github.io/documentation/modern/administration/backup-and-recovery/index.html) covers testing restoration of both files and database.

<a id="upgrade" name="upgrade"></a>

## Upgrading

1. Back up the complete database and site files before any upgrade, including modified themes, images, static pages and custom code (notably `lib-custom.php`). Test that your backup is restorable.
2. Read the target version's upgrade notes and check its compatibility with PHP, databases and plugins.
3. Extract the target Geeklog release and carefully preserve site-specific modifications and configuration.
4. Follow the version-appropriate migration of configuration files. The legacy guide distinguishes upgrades from **1.4.1 or earlier**, which use old `config.php` files, and **1.5.0 or later**, which use `db-config.php` and `siteconfig.php`. These are historical paths, not an assertion that those old releases are currently supported upgrade sources.
5. Run the installer/upgrade wizard at `admin/install/index.php`, inspect the results and verify the site.
6. Follow post-upgrade cleanup: the legacy documentation explicitly requires removing `admin/install`.

Do not overwrite a production site without a rollback plan and a backup.

<a id="migrate" name="migrate"></a>

## Moving a Geeklog site

The existing installer describes a **Migrate** option for changing servers or domains, including updating configuration and URLs stored in content.

1. Back up the existing files and database and restore them in a safe destination.
2. Prepare destination database credentials and the required file paths.
3. Review the target release's migration wizard before using it to import an uploaded backup, a server-side backup or a previously imported database.
4. Check upload limits if transferring a backup through the browser.
5. After migration, verify links, media, authentication, file permissions and configuration. Restrict/remove installer access as directed by the release.

<a id="installprob" name="installprob"></a>

## Troubleshooting

Start by checking the filesystem paths in `siteconfig.php` and reading the **first** reported error; secondary errors may be consequences of an incorrect path. Also check PHP extensions, database connectivity, filesystem permissions and your web-server logs.

This remains a summary. The original [installation reference](https://github.com/Geeklog-Core/geeklog/blob/master/public_html/docs/english/install.html) contains additional database collation tables, requirements and specific troubleshooting examples which still need technical/editorial review.


### Historical errors and modern diagnostic approach

The original installer guide includes examples from older PHP and MySQL versions. Their exact messages and recommended fixes are **historical**, and should not be copied into modern production instructions without review.

| Symptom | What to investigate |
| --- | --- |
| PHP parse error in `siteconfig.php` | Look for malformed quotes, missing punctuation and an accidental edit near the indicated line; use PHP syntax checks in a safe environment |
| Missing required PHP file | Check whether the installation archive was extracted completely and whether filesystem paths are correct |
| Database table already exists | Determine whether this is a previously initialized or partially upgraded database; **do not drop a production database** to retry |
| Parse errors in `lib-common.php` | Verify file integrity against the release archive, encoding and whether deployment tools unintentionally modified the PHP code |
| Database access denied | Check connection details, host, user and permissions; use database-version-appropriate account management, not obsolete SQL commands |
| Unable to write a log file | Check parent directories, ownership and the web server's effective user; avoid world-writable permissions such as `777` |
| "Headers already sent" | Check for unexpected output, whitespace and encoding changes in PHP files; use logs to locate the first output |

**Security corrections relative to the historical instructions:** Never publish database credentials in a support request. Do not grant unrestricted access or use `chmod 777` as a generic fix. Preserve backups before investigating partially completed database upgrades.

### Support information to collect

Record the exact Geeklog release, PHP/database version, web server, first error message, relevant log entries, and the stage where the failure occurred. Redact passwords, tokens, secrets and private user data before sharing diagnostic output.

The legacy guide also links to mailing lists and a wiki that may no longer operate. These links must be checked and replaced during editorial review; the current [Geeklog project repository](https://github.com/Geeklog-Core/geeklog) and [Geeklog website](https://www.geeklog.net/) are suitable starting points.

## Migration compatibility

The nine legacy anchors `glossary`, `public_html`, `installation_requirements`, `preinstall`, `things_you_should_know`, `install`, `upgrade`, `migrate` and `installprob` are explicitly retained above as HTML anchors in the Markdown source.

**Remaining gates:** review licensing/provenance, complete broader runtime links and upgrade/migration/rollback tests, and obtain maintainer approval before distributing generated `install.html` as an official release. The preview overlay has been tested on an isolated 2.2.2 installation.
