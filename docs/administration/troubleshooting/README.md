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

## First-response decision path

Use the **first reproducible symptom**, not several speculative fixes at once:

1. **Only one page fails?** Record its full route *without sensitive query values*, HTTP status, and the action immediately before failure. Compare a second, known-good page to determine whether the problem affects all requests.
2. **HTTP 500 or blank content?** Read the earliest relevant PHP and web server error entry. Check the installed version and required PHP extensions before changing permissions or files. A blank page alone does not prove that a plugin is responsible.
3. **Site loads but admin/login fails?** Check the configured site and administration URLs, browser cookie behavior, and actual account/group permissions. Test in a private staging browser session; do not disable authentication to diagnose it.
4. **Database error?** Confirm the configured database engine, hostname and driver in a protected environment. Test connectivity using approved hosting tools; avoid printing connection secrets, and do not rerun the installer on an existing database.
5. **Failure began after a plugin/theme change?** Compare the before/after versions and inspect the first application error. Reproduce in an isolated copy before attempting rollback or disabling plugins on production.
6. **Failure began after upgrading?** Stop further upgrade attempts, preserve the current state, and follow the [maintenance and upgrade guide](../../../administration/maintenance/index.html). Validate a complete database-and-files backup before recovery.

If the first error is inconclusive, collect more evidence. Do not change multiple settings simultaneously: otherwise it becomes difficult to identify the actual cause.

## Safe diagnostics by HTTP symptom

| Observation | What it suggests (not proof) | Next useful evidence |
| --- | --- | --- |
| HTTP 404 | Missing file, incorrect route, rewrite rule or application URL | Exact route, server rewrite settings, whether an existing static asset works |
| HTTP 403 | Access control or hosting security rule | Path, account/role, timestamp and sanitized web server/security logs |
| HTTP 500 | Server-side exception or configuration failure | First PHP/web-server error and the affected operation |
| HTTP 200, page looks broken | Missing CSS/JS/assets or rendering error | Browser network requests, asset URLs and response content types |
| Redirect loop | Site URL, HTTPS/proxy or cookie configuration mismatch | Sanitized redirect sequence and effective canonical URL |
| Intermittent failure | Cache, resource pressure or external dependency | Timestamps, request pattern, server resource/error evidence |

Treat status codes as diagnostic starting points. Some hosting security layers return a generic error page, and an HTTP 200 response does not prove that an administrator action succeeded.

## Identify the failing layer without exposing credentials

On a disposable staging installation, compare these independent checks:

- **Static asset:** request a known stylesheet or image that normally loads. If static files work while PHP pages fail, investigate the PHP/application path rather than changing global file permissions.
- **Public application page:** check a known public article or homepage. If only administration fails, inspect URL, session and role-specific issues.
- **Documentation:** open a valid `/docs/english/config.html#desc_site_url` URL. The fragment is resolved by the browser: the server receives the document URL, not the fragment. Also click a real help link within an authorized administration session.
- **Plugin page:** compare a working Core route with the failing plugin route. A reachable plugin help HTML file does not establish that the plugin has installed or initialized successfully.

For diagnostics in production, prefer read-only observations. Do not enable verbose error display for public visitors, expose `phpinfo()` publicly, edit private configuration in a support ticket, or disable site-wide security controls as a default workaround.

## Redacted incident report template

When requesting help, provide enough details for reproduction without posting secrets:

```text
Geeklog version:
PHP / database engine and versions:
Web server / hosting type:
Affected route or feature (remove tokens/private IDs):
Observed HTTP status and first sanitized error:
First occurrence and recent change:
Does the issue reproduce in a clean staging installation?
What was checked (read-only) and the result:
Available backup and restoration test status:
```

Link to the relevant [configuration reference](https://geeklog-core.github.io/documentation/configuration.html), [users and groups guide](../../../administration/users-and-groups/index.html), or [backup and recovery guide](../../../administration/backup-and-recovery/index.html) when the symptom falls in those areas. These are online guides and do not replace context-sensitive help shipped with the installed Geeklog release.

## Installation and upgrade checks

The bundled [Geeklog 2.2.2 installation instructions](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/install.html) document the installer location `admin/install/index.php`, and require removing `admin/install` after successful installation or upgrade.

Do not repeatedly execute a failed upgrade against the same production database without first understanding the failure and verifying recovery options.

## Installer redirects to an error page after saving settings

In the isolated Geeklog 2.2.2 staging tests, entering a **filesystem directory** in a form field that stores `site_admin_url` caused an incorrect administration URL to be saved. The UI label may suggest an admin directory path, but the configuration value is an **HTTP URL**, not a path on disk.

For example, on a local staging installation served at `http://localhost:8083`:

| Setting or location | Example | Meaning |
| --- | --- | --- |
| `site_url` | `http://localhost:8083` | Browser-accessible site URL |
| `site_admin_url` | `http://localhost:8083/admin` | Browser-accessible administration URL |
| Admin directory on disk | `/var/www/html/public_html/admin` | Filesystem path; **not** a value for `site_admin_url` |

Do not paste these sample URLs into a live site: use its actual configured hostname and paths.

If installation fails after writing configuration, **do not rerun the installer blindly**. Inspect the existing staging configuration and database version first; an installation can be partially complete even when a later page fails. Back up the current state before any remediation. Never share the database password or full configuration dump when asking for help.

### XMLSitemap cannot create sitemap.xml

The bundled XMLSitemap plugin for Geeklog 2.2.2 may attempt to create `public_html/sitemap.xml` during post-install setup. On a staging system lacking write permission, the PHP error log can show a `touch(): Unable to create file` warning for this path.

Inspect the actual path and the web worker's permissions. Correct **only** the necessary file ownership/permissions in a disposable environment. Avoid `chmod -R 777` or granting write access to the entire public web tree. A successfully served XMLSitemap documentation page does **not** mean the plugin was installed or enabled successfully.

These examples are based on the documented 2.2.2 installation staging observations in [the repository's test report](https://github.com/Geeklog-Core/documentation/blob/main/planning/INSTALL-STAGING-VALIDATION.md), not on an assertion that the same problem affects every host.

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
