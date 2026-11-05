# Isolated Geeklog 2.2.2 new-install staging

**Disposable lab only.** This uses the existing local Docker image `222-web` with PHP 8.1 and MariaDB 10.11, but **does not** use the existing `geeklog222-*` or `geeklog211-*` containers, data, mounts, project names, passwords, networks or database volumes.

## Before starting

Place the independently verified `geeklog-2.2.2.tar.gz` (SHA-256 `d12991f78225289d2bac297bff1a7e9be55f04a9e0aa097bb379e41d7fb138a8`) in `~/geeklog-docs-validation/`. The installer will use **a new copy** of this release, not the modified files from the prior documentation test.

On Chromebook/Crostini:

```bash
cd ~/geeklog-docs-validation
mkdir -p staging-222
cd staging-222
curl -fL https://raw.githubusercontent.com/hostellerie/documentation/docs/installation-release-audit-222/staging/geeklog-2.2.2/compose.yaml -o compose.yaml
curl -fL https://raw.githubusercontent.com/hostellerie/documentation/docs/installation-release-audit-222/staging/geeklog-2.2.2/prepare_local_staging.py -o prepare_local_staging.py
python3 prepare_local_staging.py
docker compose -p geeklog-docs-stage config --quiet
```

**Do not proceed** if the archive hash check, staging preparation or Compose validation fails. The helper intentionally refuses to overwrite existing staging files. `site/` and `.env` must be new and absent beforehand.

Only when the outputs are validated, explicitly start new containers:

```bash
docker compose -p geeklog-docs-stage up -d
docker compose -p geeklog-docs-stage ps
```

The new website is bound to **127.0.0.1:8083**. Database port 3306 is not published. The MariaDB root and application passwords are randomized and stored only in `staging-222/.env` with mode 0600. Do **not** paste its contents into issues or chat. The local DB parameters for the Geeklog wizard are: host `db`, database `geeklog_stage`, username `geeklog_stage`, password read locally from `.env`.

If the site is displayed but the installer asks for file writes, inspect the exact file/dir first. Do not broadly `chmod -R 777` or change files in existing test environments.

## Post-start preflight

```bash
docker compose -p geeklog-docs-stage ps
docker port "$(docker compose -p geeklog-docs-stage ps -q web)"
```

Confirm only port 8083 is published on the loopback host and the project is named `geeklog-docs-stage`. Before filling in the wizard, confirm no mounted source or volume overlaps the existing containers.

## Stopping / cleanup

To stop only this project without deleting its database:

```bash
docker compose -p geeklog-docs-stage stop
```

**Do not run** `docker compose down -v` until you have confirmed the project identity and completed all desired test/rollback evidence. Never run cleanup commands from the existing 211 or 222 Compose directories.

## Scope

This lab is for testing **new Geeklog 2.2.2 installation** against the Markdown installation guide. Upgrade/migrate scenarios need separate disposable copies and backups, not this database reused. The official documentation repo and production deployments are unaffected.
