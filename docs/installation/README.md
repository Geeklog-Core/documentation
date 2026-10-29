# Installing, upgrading, and moving Geeklog

> **Work in progress — not release installation instructions.** This page is a reviewed migration outline, not a substitute for the `install.html` shipped with your selected Geeklog release. Do not use it alone to install or upgrade a production site.

## Choose your installation path

- **New installation:** prepare your server and database, obtain a release package, follow its installation instructions and verify the administrator account and access controls.
- **Upgrade:** make verified backups of the database and site files, review release notes, and use the upgrade procedure for your starting and target versions.
- **Move between hosts:** back up files and the database, review server paths, credentials and site URLs, then test links, uploads, permissions and scheduled tasks.

## Check requirements for your release

Confirm the required PHP version, database engines, extensions and hosting setup against the documentation distributed with the **actual target release**. The legacy HTML installation document includes historical minimum version numbers; they must not be reproduced here as current security recommendations without independent verification.

## Important terms

- **Document root / public_html:** the web-accessible directory; the name varies by host.
- **Path:** filesystem location, for example `/var/www/`.
- **URL:** web address, for example `https://example.com/`.

## Migration status

The following sections exist in the historical HTML but have **not** yet been fully checked or migrated: installation requirements; prerequisites; new installation; upgrades; migration; troubleshooting; database collation guidance; web-server-specific steps.

Source: [Geeklog Core install.html](https://github.com/Geeklog-Core/geeklog/blob/master/public_html/docs/english/install.html).

### URL/anchor compatibility contract

The eventual generated `public_html/docs/english/install.html` must preserve these historical targets:

```
#glossary
#public_html
#installation_requirements
#preinstall
#things_you_should_know
#install
#upgrade
#migrate
#installprob
```

These IDs are an inventory, **not** evidence of a completed conversion. Do not replace the existing HTML until all sections are complete and all nine targets have been tested.
