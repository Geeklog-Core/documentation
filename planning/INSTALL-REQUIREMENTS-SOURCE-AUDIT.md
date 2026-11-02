# Installer requirements: source cross-check

Reviewed 2026-10-29 against `Geeklog-Core/geeklog` `master`. **This is a source audit, not an executed installation or a declaration of release support.**

## Confirmed in current checked source

- `public_html/admin/install/classes/Common.php` declares `GL_VERSION = '2.2.2'`.
- That same file declares installer constants `SUPPORTED_PHP_VER = '5.6.4'`, `SUPPORTED_MYSQL_VER = '4.1.3'`, `SUPPORTED_PGSQL_VER = '9.1.7'`.
- `public_html/admin/install/classes/installer.class.php` calls `checkPhpVersion()` and compares the running `PHP_VERSION` with `SUPPORTED_PHP_VER`.
- `public_html/admin/install/index.php` loads `Install.php`, `Upgrade.php`, `Migrate.php` and the installer implementation. Its location corresponds to the URL described in the historical instructions.
- The existing `public_html/docs/english/install.html` lists Apache or IIS, PHP extensions such as mbstring, bzip2, database drivers, OpenSSL, JSON and fileinfo; it describes MySQL, MariaDB and PostgreSQL options.

## Interpretation and caveats

These constants represent **historical checks in the 2.2.2 source**, not secure deployment baselines. PHP 5.6 and early MySQL/PostgreSQL versions are obsolete and must not be recommended for newly exposed sites. A declared minimum also does **not** demonstrate compatibility with newer PHP versions; test against the supported release matrix.

**Geeklog 2.2.3:** the checked `master` source still identifies itself as 2.2.2. Do not claim confirmed 2.2.3 installer requirements until the release branch/tag and compatibility testing are available.

## Follow-up gates

- [ ] Verify supported runtime/database versions against the maintained release compatibility policy, CI and packaged release.
- [ ] Compare the install, upgrade and migrate workflows to current installer behavior through a staging installation.
- [ ] Check requirement completeness and fail-fast behavior for extensions and database drivers.
- [ ] Confirm the 2.2.3 release/tag requirements when published.
- [ ] Verify security guidance for removal/disabling of the installer and safe file placement.
