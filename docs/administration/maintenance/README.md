# Maintaining and upgrading Geeklog

> **Geeklog 2.2.2 — administrator checklist.** This guide complements [the versioned Geeklog installation instructions](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/install.html); it is not a claim of compatibility with every modern PHP, database or plugin release.

## Before making changes

- Record the installed Geeklog release, database engine, PHP version and active plugins.
- Back up the database **and** application files; rehearse a restore in staging.
- Check each plugin's compatibility and update procedure.
- Review relevant application and server logs for existing faults.
- Arrange a maintenance window when a change could affect visitors or data.

## Upgrade procedure

The versioned [Geeklog 2.2.2 installation instructions](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/install.html) describe using the installation wizard at `admin/install/index.php` for upgrades.

1. Read the upgrade instructions for the specific source and destination releases.
2. Prepare a complete and tested backup.
3. Rehearse the upgrade on an isolated copy of the site, including its plugins and themes.
4. Deploy the appropriate release files while preserving site-specific configuration and modifications.
5. Run the version-appropriate installer or upgrade wizard.
6. Check the database version, authentication, homepage, articles, media and plugins.
7. **Remove the `admin/install` directory when the wizard is no longer needed**, as explicitly required by the bundled Geeklog 2.2.2 guide.
8. Monitor error logs and core functions after reopening the site.

**Do not use a historic minimum PHP version as a modern security recommendation.** Check current runtime and extension support for the particular Geeklog release you are deploying.

## Regular maintenance

A practical maintenance cycle includes checking backups and restoration readiness, reviewing new administrator accounts, ensuring permissions follow least privilege, testing broken links and uploaded media, and monitoring error logs. For a public site, keep themes, plugins, the runtime and the server software patched.

The 2.2.2 database administration page at `admin/database.php` is **restricted to `Root` and `mysql`**. Its optimization and backup interfaces are not a substitute for a tested recovery strategy.

## Troubleshooting after an update

If a site fails after an upgrade, collect the **first meaningful error**, the actual software versions and relevant server logs. Verify the file layout, database connectivity, configuration paths and plugin compatibility before attempting additional upgrades.

Avoid deleting production tables or granting broad filesystem permissions as generic fixes.

## Verification status

- [x] Versioned Geeklog 2.2.2 wizard URL and post-install cleanup confirmed in bundled instructions.
- [x] Database admin limitations confirmed in `admin/database.php`.
- [ ] Full upgrade path tested against selected source releases.
- [ ] Recommended monitoring and recovery procedures tested in staging.
