# Isolated Geeklog installation validation protocol

Status as of **2026-11-03**: **isolated Geeklog 2.2.2 fresh-install and embedded-documentation overlay tested successfully**, with the limitations below. Earlier sections are chronological records of plans and preliminary results; statements such as “not yet executed” below describe the state **at that earlier checkpoint**. Upgrade, migration and rollback remain untested. No production website is in scope.

## Preconditions

- Select a disposable VM or container environment with no connection to production databases, domains, credentials, or user data.
- Pin the Geeklog release/tag, PHP version, database type and image/package digest. Keep each test result with those identifiers.
- Use a fresh throwaway database and temporary credentials.
- Keep inbound access private/local; do not expose an unfinished installer to the Internet.

## Test matrix

| Scenario | Input | Pass criteria |
| --- | --- | --- |
| New installation | Clean database; documented file layout | Installer completes, post-install access works, installer removed/disabled |
| Upgrade | Disposable copy of test site from documented supported previous release | Upgrader finishes; content/config preserved; no new errors |
| Migration | Disposable sample database, changed site URL / filesystem path | Migration updates expected paths/URLs; sample links and media work |
| Offline documentation | Generated docs overlay in a Geeklog distribution copy | `docs/english/install.html` loads, all nine historical anchors work, CSS/logo/index/support resolve |
| Rollback | Test-only backup | Restore to previous working test state |
| Security | Anonymous user | Installer no longer accessible; no secrets exposed |

For each scenario record exact commands, logs (redacted), screenshots where helpful, warnings, and whether any steps in Markdown differed from the installer.

## No-go conditions

Do not proceed if an environment is connected to production services, the release compatibility baseline is unknown, backups are absent for upgrades, or external access to the installer cannot be restricted.

## Approval required before execution

User approves a specific disposable environment, selected release and database engine. Tom/core maintainers validate architecture and publication strategy separately. No external site or server is accessed by this plan.

## Current evidence

- The user tested the generated `docs/english/install.html` page in a local **Geeklog 2.2.2 Docker** instance on PHP 8.1. The installation page rendered correctly after correcting escaped newlines; representative `#installation_requirements` and `#upgrade` fragments worked.
- The original Core `config.html#desc_site_url` help example, **all seven plugin documentation pages**, and representative context-sensitive help from the administration panel were manually reported working.
- Core and reCAPTCHA documents were backed up before the install-page overlay. Normalized line ending comparisons confirmed identical contents for three sampled unchanged HTML documents; automated CI additionally compares full pinned source inventories.
- **Not yet tested:** fresh install, upgrade, migration, rollback, security post-install checks or exact downloadable release-package equivalence. Browser access to documentation is not a substitute for testing those installer workflows.
- Current GitHub Actions covers Markdown rendering, nine installation anchors, historical resource paths, inherited link defect baseline and byte-identical preservation of non-install Core documentation. **It does not install, upgrade, or migrate Geeklog.**

## Docker preflight protocol — 2026-11-03

The user already operates two local Docker Geeklog installations: `geeklog211-web` and `geeklog222-web`, with separate database containers `geeklog211-db` and `geeklog222-db`. The Geeklog 2.2.2 web container uses port **8081** and PHP **8.1.33**. These are reference installations, **not disposable targets**.

### A. Inspect without modifying anything

Run the bundled read-only tool on the user's Docker host:

```bash
python3 tools/inspect_docker_staging.py
```

The tool reports each container's image name, running state, port mappings and mount **types/destinations only**. It deliberately suppresses environment variables, mount source paths, database passwords, network configuration and complete `docker inspect` output. Review output for volumes/mounts that could accidentally be shared between source and test environments.

If the helper is not yet in the official repository, use the corresponding file from the working branch. The tool requires only Python and Docker CLI.

### B. Staging preparation protocol (subsequently executed in isolated project)

Before running any installer wizard, prepare a **new project name** (e.g. `geeklog-docs-staging`), containers, networks, volumes and disposable MariaDB databases. All must be physically separate from `geeklog211-*` and `geeklog222-*`; do **not** bind-mount their live config, databases, backup directories or data volumes into the staging environment.

Confirm distinct local-only ports and no shared Docker volume IDs. Do not connect to a production domain or any real users/data. Do not reuse actual site secrets. Record image tags/digests and the target Geeklog release.

### C. Execute only after the isolated environment is verified

1. Fresh install: use the **exact official 2.2.2 release archive** with new temporary database/credentials, confirm the described wizard URL `/admin/install/index.php`, complete the flow, then remove/disable installer access as directed and test anonymous access denial.
2. Upgrade: create a **disposable copy** of a test 2.1.1 installation with fake data, take an independently restorable backup and upgrade only the copy to 2.2.2. Record configuration, charset and plugin compatibility warnings.
3. Migrate: prepare independent test database/files and move to another private staging hostname/path; verify that URLs, media, paths and content update as claimed by the guide.
4. Rollback: restore the disposable pre-upgrade snapshot and verify data, configuration and request handling.
5. Cross-check each observed wizard step against `docs/installation/README.md`, with screenshots/redacted logs and exact PHP/database image versions.

### D. Safety stop conditions

- Any staging mount, named volume or database points at the running `geeklog211` or `geeklog222` instances.
- The installer would be exposed outside loopback or a trusted private test network.
- No tested restoration path exists before upgrade/migration.
- A test attempts to alter an active site, its credentials or its data.

**Status at this earlier preflight checkpoint:** the official 2.2.2 archive's installer entrypoint and `Common.php` requirement constants were inspected read-only and the validation helper was added. **Later on November 3, the clean installation was executed and the site/admin/documentation overlay validated; see sections K–N below.** Upgrade, migrate and rollback remain pending. These steps require the user's local Docker environment and an independent staging configuration, not just a source audit.

### E. Ready-to-run dedicated 2.2.2 installation laboratory — 2026-11-03

The user confirmed for the existing `222-web` image: `WorkDir=/var/www/html`, `Cmd=["apache2-foreground"]`, Apache `DocumentRoot=/var/www/html/public_html`, PHP 8.1.33 and `mysqli`, `mbstring`, `gd`, `curl`, `zip`, `openssl`, `fileinfo` present; `pdo_mysql` absent. No running Docker container publishes 8083. The image and its PHP configuration still need to be verified in the isolated runtime.

Dedicated project scaffolding is stored in `staging/geeklog-2.2.2/`:

- `compose.yaml`: distinct named MariaDB 10.11 volume/network, application name `geeklog-docs-stage` supplied via CLI, no host DB port, Web exposed on **127.0.0.1:8083**, separate `./site` bind.
- `prepare_local_staging.py`: **does not start Docker**; checks user-supplied official tarball against published size/MD5 and the independently computed SHA-256, rejects unsafe tar entries, extracts only into a fresh `site` folder and creates random throwaway DB secrets in local `.env` (0600). Refuses to overwrite either site or secrets.
- `README.md`: Chromebook preparation, safe Compose validation, optional start, and stop guidance.

The user-uploaded verified tarball is available to ChatGPT but **not** automatically on the user's Chromebook. The user must save it to `~/geeklog-docs-validation/geeklog-2.2.2.tar.gz` using the file link in chat, before preparation. Stage `site`, `.env` and Compose services have **not** yet been created or run on the user's host. Obtain the sanitized Compose preflight results before opening installer wizard.

### F. Actual installer page observed — permissions and install method (2026-11-03)

The user reached `http://localhost:8083/admin/install/index.php` inside the **isolated** `geeklog-docs-stage` project.

The wizard displayed **Step 1 — Set File Permissions**, followed by **Step 2 — Choose an Installation Method** offering New Install, Upgrade, and Migrate. It reported 25 paths needing Web-server write access (e.g. `db-config.php`, `backups/`, `data/` caches, 404/access/error/spamx logs, `public_html/siteconfig.php`, RSS, File Manager config and image storage). The paths were mode 0644 (files) or 0755 (directories), reflecting the extraction helper's safe defaults and UID 1000 ownership, not an archive defect.

**Source-audited behavior:** `public_html/admin/install/classes/installer.class.php`, method `checkPermissions()`, calls `is_writable($file)`. When it fails, the UI reports “Change to 666/777” and renders a blanket `chmod -R 777` shell command. These advertised octal modes are **not programmatic requirements**. The documented staging remediation is to change ownership of **only identified writable files/directories** to the Apache/PHP worker (`www-data`) while retaining their 0644/0755 baseline modes. Avoid broad recursive world-writable permissions. The local-only fix includes `backups`, `data`, log files, `siteconfig.php`, `db-config.php`, RSS and File Manager config, and the listed image storage directories; ownership changes recurse only under these intentionally writable staging directories.

**Security implication for documentation:** add a prominent warning in the final installation guide: do **not** copy the installer's `chmod -R 777` example to production. Use controlled ownership/group ACLs and minimal writable paths. After install, protect configuration, ensure installer cannot be accessed, and review Web-server-writable directories.

**Status at this earlier intermediate checkpoint:** the user had not yet confirmed completion. **Subsequent results in sections K–N supersede this status.** No runtime installation success claim should be made.

### G. Step 3 rendering failure after actual form submission — 2026-11-03

The user submitted the isolated fresh-install form and was redirected to `/admin/install/index.php?mode=install&step=3&...`, which returned **“Unfortunately, an error has occurred rendering this page. Please try again later.”** The prior form's `site_admin_url` query parameter contained the filesystem path `/var/www/html/public_html/admin`, because an earlier assistant instruction mistakenly supplied that for the form field labelled “Admin Directory Path.”

**Correct value:** `http://localhost:8083/admin` (no trailing slash), **not** `/var/www/html/public_html/admin`. Source proof: installer `layout/step1.thtml` names the input `site_admin_url`; `classes/Common.php::getSiteAdminUrl()` derives it from the HTTP request protocol/host/path; `classes/Install.php::step3()` saves it as the `site_admin_url` configuration key. The filesystem location remains useful for other purposes, but is **not** the value for this form field.

**Causality not yet proven:** this incorrect value is a real installer configuration defect, but the generic rendering failure might have an additional cause. Because the user reached step 3, the installer may already have modified `db-config.php`, `siteconfig.php`, created one or more database tables, or stored partial configuration. **Do not resubmit/reinitialize yet.** First perform nonmutating checks of current DB host/name/user (never print password), count table names via `information_schema` using the Compose database application account, and inspect narrowly scoped error logs with credentials/query strings redacted. If the stage DB contains partial installer data, any reset must be strictly scoped to the **disposable stage** and preceded by explicit confirmation of its Docker Compose project/volume identity.

**Documentation finding:** “Admin Directory Path” is potentially misleading in English UI. The replacement installation guide should clearly distinguish *admin URL* (`http://localhost:8083/admin`) from *admin filesystem path* (`/var/www/html/public_html/admin`), and never suggest the latter as the form value. At this earlier checkpoint, successful completion had not yet been established; later evidence confirms functional site and authenticated admin access.

### H. Partial installation evidenced by 43 database tables — 2026-11-03

The user executed a read-only `information_schema.tables` count in isolated `geeklog_stage` after the step-3 generic rendering failure. Result: **43 tables**. This confirms successful MariaDB connectivity and at least partial schema creation, **not** completed installation. Filtered last 100 Docker Web log lines yielded no error/warning/fatal matches; Docker stdout/stderr is not a substitute for Geeklog's own `/var/www/html/logs/error.log`.

**Do not repeat installer step 3 or wipe the database.** Next nonmutating checks: inspect narrowly scoped Geeklog error log with secrets redacted; enumerate table names and inspect `gl_vars` schema/version only if the table exists; inspect `db-config.php` host/name/user with password suppressed. Compare any failure to known partial-upgrade caution in Geeklog Memorandum, while respecting that the present run is a **fresh install**, not a 2.1.1→2.2.2 upgrade. Preserve current disposable staging state for reproducibility.

### I. Installer progressed through Core and seven plugins; XMLSitemap post-install write failure — 2026-11-03

Fresh-install stage evidence from user-supplied diagnostics:

- `information_schema`: **43 tables** in disposable `geeklog_stage`; `gl_vars.database_version = 2.2.2`.
- `gl_plugins` reported approximately **7 rows** (the reported `information_schema.TABLE_ROWS` value is an estimate, not a `COUNT(*)` query); the Geeklog log explicitly reports successfully installed Links, Polls, reCAPTCHA, SpamX and Static Pages, then starts XMLSitemap installation.
- The latest visible Geeklog application error at Tue Nov 3 03:05:17 2026 is: `E_WARNING(2) - touch(): Unable to create file /var/www/html/public_html/sitemap.xml because Permission denied @ /var/www/html/plugins/xmlsitemap/xmlsitemap.class.php line 441`.
- In official Geeklog 2.2.2 `plugins/xmlsitemap/autoinstall.php` lines 130–137, `plugin_postinstall_xmlsitemap()` calls `XMLSMAP_update()`, which calls the sitemap writer. `plugins/xmlsitemap/xmlsitemap.class.php` line 441 uses `touch($filename)`, logs and returns false on failure.
- The earlier install-stage writable-path preflight did **not** cover `public_html/sitemap.xml` or allow the Web process to create it. Therefore this is a **reproducible post-install filesystem permission gap**, not the previously described Polls/SpamX *upgrade* SQL failure.
- The generic `Unfortunately, an error has occurred rendering this page` message is **not yet conclusively attributed** to the sitemap warning; a separate invalid `site_admin_url` was previously observed and may still be stored. Do not assert that every installation stage finished correctly or restart the installer blindly.
- Next: read-only test whether `public_html/sitemap.xml` exists and whether `www-data` can write it; inspect only the last redacted Geeklog log lines and public HTTP status; check the actual persisted admin URL and *exact* plugin count. If remediation is needed in this disposable stack, create only the sitemap file owned by `www-data` with mode 0644, rather than making the whole public Web directory writable or applying `chmod 777`. Then assess site/plugin health without replaying the full new-install process.

### J. User-selected XMLSitemap disablement for disposable installation — 2026-11-03

The user explicitly recalled that the problematic plugin should be disabled for the staged installer test. The current **fresh install** error pertains to XMLSitemap post-install's inability to create `public_html/sitemap.xml`; it is distinct from the Memorandum's historical **SpamX upgrade** SQL 1091 failure.

Recommended a **staging-only** check of `gl_plugins(pi_name, pi_version, pi_enabled)` followed by a narrowly scoped `UPDATE gl_plugins SET pi_enabled=0 WHERE pi_name='xmlsitemap'` and read-only verification. This is non-destructive to plugin tables and files but may not repair a partially completed installer. If XMLSitemap is absent from `gl_plugins`, the UPDATE changes nothing; do not claim a disabled plugin. Do not automatically resubmit the installer or assume the generic render failure is completely solved. The existing 43-table schema and `database_version=2.2.2` must be preserved for subsequent forensic review.

**Status at this earlier checkpoint:** the instructions were unverified; later `gl_plugins` query (section L) confirms XMLSitemap disabled.

### K. Staging fresh-install site and administration accessible — 2026-11-03

User confirms the disposable Geeklog 2.2.2 site is online and **the admin dashboard is accessible with an authenticated session** after correcting the misconfigured serialized `Core.site_admin_url` in `gl_conf_values` from filesystem path `/var/www/html/public_html/admin` to HTTP URL `http://localhost:8083/admin`. `Core.site_url` was already `http://localhost:8083` and `Core.path_html` was already `/var/www/html/public_html/`. This confirms that the earlier admin URL field confusion affected administration routing, and that correcting only that record restored admin access, without reinstalling the 43-table database. The generic step-3 render error still cannot definitively be ascribed solely to the wrong admin URL; XMLSitemap also logged its independent post-install write failure.

**Status:** **functional** new Geeklog 2.2.2 installation under PHP 8.1.33, MariaDB 10.11, isolated Docker Compose `geeklog-docs-stage`, Web bound to `127.0.0.1:8083`. Site and authenticated administration confirmed by user. **Remaining checks:** actual `gl_plugins` registration/enabled status (especially `xmlsitemap`), exact user-facing warnings, plugin admin/help pages, site HTTP responses, correct locked-down installer access and post-install configuration permissions. Do not claim all core plugins or hardened deployment fully validated yet.

**Editorial correction required:** clarify Geeklog installer “Admin Directory Path” form widget behavior. Though label suggests a filesystem path, it stores `site_admin_url` as an HTTP URL. Document explicit examples side by side, avoid installer `chmod -R 777` advice, and separately cover optional plugin sitemap file writability when XMLSitemap is installed. Do not encourage blanket 0777 or root-dir write access.

### L. Core plugin registration and XMLSitemap disabled — 2026-11-03

User ran an **actual** `SELECT pi_name, pi_version, pi_enabled FROM gl_plugins ORDER BY pi_name` against disposable `geeklog_stage`. Exact results:

| Plugin | Version | Enabled |
| --- | --- | --- |
| calendar | 1.1.9 | 1 |
| links | 2.1.8 | 1 |
| polls | 2.2.1 | 1 |
| recaptcha | 1.2.4 | 1 |
| spamx | 1.3.6 | 1 |
| staticpages | 1.7.3 | 1 |
| xmlsitemap | 2.0.3 | **0** |

**Seven registered, six enabled, XMLSitemap explicitly disabled.** Its write failure has not been fixed; installing the plugin afresh or re-enabling it requires a separate writable-sitemap-file test. The site and authenticated admin were already confirmed accessible.

The working Markdown install guide `docs/installation/README.md` now documents the observed distinction between HTTP `site_admin_url` and the filesystem admin directory, limited file ownership vs unsafe `chmod -R 777`, optional XMLSitemap sitemap path, and safe diagnosis of partial installs.

**Next acceptance gate:** disable public installer reachability, verify configuration secrets and ownership after install, and test public/admin and representative plugin pages. Avoid broad world-writable permissions. New-install staging is functional with XMLSitemap disabled; do not call it full all-plugins acceptance.

### M. Installer disabled (HTTP 404) — 2026-11-03

After the recommended **staging-only** move of `public_html/admin/install` outside the Web root, the user reports **HTTP 404** from `http://localhost:8083/admin/install/index.php`. This confirms the installer entrypoint is no longer served at that URL. The relocated copy remains under `/var/www/html/install-disabled-staging`, outside Apache's `/var/www/html/public_html` document root.

**Still to check before full security acceptance:** site and authenticated administrator page remain functional *after* the move; administrator default credentials have been replaced; `db-config.php` and `siteconfig.php` are no longer unnecessarily writable by the Web worker; confirm any other installer entrypoints are not publicly accessible. The XMLSitemap plugin remains disabled, not repaired. This validation is staging-only, not production deployment approval.

### N. Embedded 2.2.2 documentation overlay installed and browser-tested — 2026-11-03

**User-reported success:** downloaded latest successful `dual-preview.yml` artifact from `hostellerie/documentation` branch `docs/installation-release-audit-222` via authenticated `gh` CLI on Chromebook and verified ZIP entries:

- `public_html/docs/english/install.html` (15,405 bytes)
- `public_html/docs/english/config.html` (174,651 bytes)
- `public_html/docs/english/index.html` (6,620 bytes)
- `public_html/admin/plugins/recaptcha/docs/english/config.html` (11,441 bytes)
- `public_html/admin/plugins/recaptcha/docs/english/install.html` (6,532 bytes)

The user then followed staging-only backup/overlay instructions on `~/geeklog-docs-validation/staging-222/site/public_html` (port 8083) and confirms **all documentation checks work**, including installation HTML, `config.html#desc_site_url` contextual anchor, index and reCAPTCHA plugin help. These are user-confirmed manual results, not independently observed browser responses. The entire published ZIP preserves legacy compatibility files; **only the embedded installation page is regenerated from Markdown** at present. Original docs and reCAPTCHA help were backed up under timestamped `~/geeklog-docs-validation/docs-backup-*` before overlay; backup path and rollback functionality not separately tested.

**Validated scope:** a real fresh Geeklog 2.2.2 staging site under PHP 8.1.33 / MariaDB 10.11 (site and authenticated admin accessible), six active bundled plugins with XMLSitemap disabled, installer entrypoint HTTP 404, generated documentation overlay and sampled contextual help. **Not yet validated:** every historic help link, actual restore/rollback, all-plugin success (XMLSitemap issue remains), administrator password change, config permissions after install, upgrade/migrate scenarios.

**Next:** review remaining gates, update contradictory old status claims in this document and the README/PROTOTYPE, run branch workflow after latest edits, then prepare **one grouped PR** for the installation-documentation workstream. Do not present the generated ZIP as an official release package.


### O. Latest consolidated ZIP — Chromebook acceptance, 2026-11-05

The contributor manually downloaded the **GitHub Actions dual-preview artifact from run #41964801825** (branch `prototype/wiki-unified-222`, commit `b57d742`). The outer artifact ZIP was verified with `unzip -tq`, contained `geeklog-2.2.2-docs-preview.zip`, and the inner ZIP passed `unzip -tq`.

- **Exact inner ZIP SHA-256:** `d4bc5bd80229e3d503d174dbd30d1bf02ae27bb0e1ff5f1dcd535bbb0915d69d`.
- **Archive entries:** 60, rooted under `public_html/docs/` and `public_html/admin/plugins/recaptcha/docs/`.
- **Staging container:** `geeklog-docs-stage-web-1` (image `222-web`, `127.0.0.1:8083->80`), independent MariaDB `geeklog-docs-stage-db-1` (`mariadb:10.11`, no published database port). No production installation used.
- **Apply:** `python3 tools/test_chromebook_overlay.py --apply geeklog-2.2.2-docs-preview.zip` returned `PASS: overlay applied in isolated staging only; original legacy files preserved` and `Files in ZIP: 60`.
- **Backup reported by local helper:** `/home/hostellerie/geeklog-docs-validation/staging-222/docs-qa-backup-20261105-112828`.
- **Static web requests:** the user ran the 12-URL HTTP check against `http://localhost:8083` and reports **HTTP 200 for all 12**, including install/config, modern index/plugin API/backup guide, six bundled Core plugin help pages and plugin-local reCAPTCHA config help.
- **Browser confirmation for this latest ZIP (user-reported, 2026-11-05):** the modern documentation home, CSS/navigation/search, Plugin API guide, and an actual configuration help link opened from the Geeklog administration interface all worked. This is **manual user evidence**, not a remote automated browser test. **Testing rollback** from the recorded backup remains outstanding.
- **Special case:** XMLSitemap documentation is reachable (HTTP 200), but its plugin was previously recorded disabled in this isolated installation. Do not describe that as a runtime plugin test.
- **Status:** latest consolidated ZIP **installed, 12/12 HTTP accepted and browser/admin help validated on the Chromebook**. Rollback remains **pending**, not failed. This supplements the older November 3 overlay test, which used a different archive.

### P. Rollback confirmed on Chromebook — 2026-11-05

After passing the 60-file overlay deployment, 12/12 HTTP checks, visual navigation/search and administrator help-link test, the user reports **“Restore OK”** for the isolated-stage restore. The backup used in this acceptance sequence was `staging-222/docs-qa-backup-20261105-112828`, created by `tools/test_chromebook_overlay.py`. The helper's rollback path restores the original Core and reCAPTCHA help trees and checks saved SHA-256 digests for three sentinel files.

**Evidence boundary:** success was reported by the Chromebook operator; the exact rollback terminal output and a post-rollback HTTP screenshot were not provided. Accordingly, record **manual rollback accepted (user-confirmed)**, not an independently reproduced container test or production backup/restore certification. No database rollback or Geeklog upgrade/migration is implied.

**Embedded documentation acceptance decision:** PASS for first-edition **2.2.2 documentation overlay in isolated staging** (ZIP integrity, original help preservation, HTTP/browser/help, and user-confirmed rollback). Historical Wiki contributor rights and editorial source verification remain separate approval matters for official publication.
