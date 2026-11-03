# Isolated Geeklog installation validation protocol

Status: **documentation browser checks completed; installer workflows not executed**. This is a manual/staging test plan only and does not authorize access to any production website.

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

### B. Stage clones with unique resources (not yet executed)

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

**Current status:** the official 2.2.2 archive's installer entrypoint and `Common.php` requirement constants were inspected read-only, and the validation helper was added, but **no fresh install, upgrade, migrate or rollback was executed**. These steps require the user's local Docker environment and an independent staging configuration, not just a source audit.
