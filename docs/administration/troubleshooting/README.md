# Troubleshooting Geeklog installations

> **Geeklog 2.2.2 — diagnostic guide.** Start with the earliest error and preserve evidence. The historical Wiki and bundled instructions contain examples from older PHP/database releases, so their original commands may be obsolete.

## Collect a useful diagnosis

Before changing a live site, record:

- Exact Geeklog release and active plugins.
- PHP and database versions, web server and hosting environment.
- First error message and the operation that triggered it.
- Relevant entries in PHP, web server and Geeklog logs, with private data removed.
- Recent configuration changes, plugin updates or file migrations.

**Never post** database passwords, private configuration files, authentication tokens or full user records to public support forums.

## Common problems

| Symptom | Checks to perform |
| --- | --- |
| Blank page or HTTP 500 | Read PHP and server logs; verify runtime compatibility and file integrity |
| Database connection failure | Check database host, credentials, name, engine and required PHP driver without exposing passwords |
| Missing CSS or images | Check deployment paths, URLs, filesystem permissions and rewrite settings |
| Login or administrator access fails | Check session/cookie settings, site URL, group rights and server logs |
| Broken configuration-help links | Confirm `docs/english/config.html` and the linked `#desc_...` anchor exist |
| Plugin pages fail | Disable or isolate the suspect plugin only by a supported procedure, then check compatibility |
| Upgrade wizard fails | Verify complete file deployment, database backup, permissions and the first reported error |
| Cannot write backup | Inspect `backup_path`, filesystem ownership and availability of the built-in MySQL-only backup facility |

## Installation and upgrade checks

The bundled [Geeklog 2.2.2 installation instructions](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/install.html) document the installer location `admin/install/index.php`, and require removing `admin/install` after successful installation or upgrade.

Do not repeatedly execute a failed upgrade against the same production database without first understanding the failure and verifying recovery options.

## Configuration documentation

The bundled [configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html) remains the authoritative source for release-specific setting names until those settings have been fully migrated to Markdown. Older Core/plugin help fragments are preserved in the generated embedded documentation.

## Escalation

Provide maintainers with a minimal reproduction, precise software versions, the first redacted error and whether it occurs in a clean staging installation. Refer to [Geeklog's official project](https://www.geeklog.net/) or [its GitHub repository](https://github.com/Geeklog-Core/geeklog).

## Verification status

- [x] Installer path and required installer-directory cleanup checked in bundled Geeklog 2.2.2 documentation.
- [x] Configuration help path confirmed in the 2.2.2 distribution.
- [x] Database backup restrictions checked against `admin/database.php`.
- [ ] Exact error signatures and fixes tested on a disposable installation.
- [ ] Linked legacy Wiki troubleshooting articles reviewed and attributed.
