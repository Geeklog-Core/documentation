# Installer requirements: source cross-check

Originally reviewed 2026-10-29 against `Geeklog-Core/geeklog` `master`; cross-checked 2026-11-03 against the pinned **`v2.2.2` tag** and its official release notes. **This is a source/release-notes audit, not an executed installation or a declaration of current runtime support.**

## Confirmed in current checked source

- `public_html/admin/install/classes/Common.php` declares `GL_VERSION = '2.2.2'`.
- That same file declares installer constants `SUPPORTED_PHP_VER = '5.6.4'`, `SUPPORTED_MYSQL_VER = '4.1.3'`, `SUPPORTED_PGSQL_VER = '9.1.7'`.
- `public_html/admin/install/classes/installer.class.php` calls `checkPhpVersion()` and compares the running `PHP_VERSION` with `SUPPORTED_PHP_VER`.
- `public_html/admin/install/index.php` loads `Install.php`, `Upgrade.php`, `Migrate.php` and the installer implementation. Its location corresponds to the URL described in the historical instructions.
- The existing `public_html/docs/english/install.html` lists Apache or IIS, PHP extensions such as mbstring, bzip2, database drivers, OpenSSL, JSON and fileinfo; it describes MySQL, MariaDB and PostgreSQL options.

## Release-notes discrepancy (confirmed 2026-11-03)

- [Official Geeklog v2.2.2 release notes](https://github.com/Geeklog-Core/geeklog/releases/tag/v2.2.2) explicitly list **PHP 5.6.4+**, **MySQL 4.1.2+** (MySQL 5 recommended), and **PostgreSQL 9.1.7+**; they state **PHP 8.1 support**.
- In contrast, [`public_html/admin/install/classes/Common.php` at tag `v2.2.2`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/install/classes/Common.php) defines `SUPPORTED_MYSQL_VER = '4.1.3'`. The same tagged installer declares PHP 5.6.4 and PostgreSQL 9.1.7.
- **Do not silently normalize MySQL 4.1.2 and 4.1.3.** The inconsistency belongs to the historical release description versus actual installer source. Neither number should be proposed as a safe modern deployment baseline. Prefer testing a maintained MySQL/MariaDB version compatible with the selected Geeklog release.

## Interpretation and caveats

These constants represent **historical checks in the 2.2.2 source**, not secure deployment baselines. PHP 5.6 and early MySQL/PostgreSQL versions are obsolete and must not be recommended for newly exposed sites. A declared minimum also does **not** demonstrate compatibility with newer PHP versions; test against the supported release matrix.

**Geeklog 2.2.3:** the checked `master` source still identifies itself as 2.2.2. Do not claim confirmed 2.2.3 installer requirements until the release branch/tag and compatibility testing are available.

## Follow-up gates

- [x] Cross-check historical `v2.2.2` source constants and release-notes requirements; document the 4.1.2 vs 4.1.3 MySQL discrepancy.
- [ ] Verify modern supported runtime/database versions against the maintained release compatibility policy, CI and the exact downloadable release package.
- [ ] Compare the install, upgrade and migrate workflows to current installer behavior through a staging installation.
- [ ] Check requirement completeness and fail-fast behavior for extensions and database drivers.
- [ ] Confirm the 2.2.3 release/tag requirements when published.
- [ ] Verify security guidance for removal/disabling of the installer and safe file placement.
