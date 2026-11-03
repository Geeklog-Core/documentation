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
