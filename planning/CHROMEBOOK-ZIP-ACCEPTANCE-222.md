# Chromebook acceptance test — Geeklog 2.2.2 documentation ZIP

Scope: the generated documentation ZIP, **not** the 2024 historical Geeklog Wiki archive. This is the final manual runtime gate before claiming a verified Geeklog 2.2.2 embedded release candidate.

## Do not confuse archives

The contributor's `~/geeklog-wiki-migration/Geeklog_wiki-hG5d78A6hD.zip` is the archived Wiki data used for historical content recovery. Do **not** deploy it into Geeklog. The relevant artifact is `geeklog-2.2.2-embedded-docs-preview` from the latest passing GitHub Actions `Dual documentation prototype (unofficial)` run on `prototype/wiki-unified-222`. The downloaded Actions artifact contains `geeklog-2.2.2-docs-preview.zip`, which has a `public_html/` overlay layout.

## 1. Verify the existing isolated stage (read-only)

On Chromebook Crostini:

```bash
printf 'Existing isolated 2.2.2 lab:\\n'
ls -ld ~/geeklog-docs-validation/staging-222/site ~/geeklog-docs-validation/staging-222/compose.yaml
cd ~/geeklog-docs-validation/staging-222
docker compose -p geeklog-docs-stage ps
```

Stop immediately if the isolated site or Compose file is absent, if it is a symlink, or if the project/mounts have changed. **Never** use `geeklog222-web`, `geeklog211-web`, production documents or their shared volumes as this test target.

## 2. Download the latest **successful** ZIP

Find the latest successful dual-documentation workflow run for the head commit in the [contributor fork's Actions](https://github.com/hostellerie/documentation/actions/workflows/dual-preview.yml). The GitHub CLI command below uses `RUN_ID` from that verified run:

```bash
mkdir -p ~/geeklog-docs-validation/zip-acceptance
cd ~/geeklog-docs-validation/zip-acceptance
gh run download RUN_ID -R hostellerie/documentation -n geeklog-2.2.2-embedded-docs-preview -D .
sha256sum geeklog-2.2.2-docs-preview.zip
unzip -l geeklog-2.2.2-docs-preview.zip | head -n 20
```

If `gh` is not installed or authenticated, download the artifact via the workflow run's browser interface, copy it into the Chromebook's Linux files, and extract the **outer Actions artifact ZIP** to obtain `geeklog-2.2.2-docs-preview.zip`. Never invent a locally available artifact path or assume that the historical Wiki ZIP is a substitute.

## 3. Apply with independent backups (isolated stage only)

Obtain `tools/test_chromebook_overlay.py` from this same branch and examine the script before using it:

```bash
curl -fLsS https://raw.githubusercontent.com/hostellerie/documentation/prototype/wiki-unified-222/tools/test_chromebook_overlay.py -o test_chromebook_overlay.py
python3 test_chromebook_overlay.py --apply geeklog-2.2.2-docs-preview.zip
```

The helper rejects target paths other than `~/geeklog-docs-validation/staging-222/site`, validates ZIP layout, compares preexisting historical files while tolerating CRLF/LF-only differences, **preserves the original historical files byte-for-byte**, and creates a timestamped backup in `staging-222/`. It does **not** access the database or start/restart any containers. If permissions prevent writing, stop and inspect ownership; **do not** run recursive `chmod 777` or point it at another installation.

## 4. Browser and administrator acceptance

With the existing isolated stack running on `127.0.0.1:8083`, inspect:

- `http://localhost:8083/docs/english/install.html#installation_requirements`
- `http://localhost:8083/docs/english/config.html#desc_site_url`
- `http://localhost:8083/docs/english/modern/index.html`
- `http://localhost:8083/docs/english/modern/development/plugin-api/index.html`
- `http://localhost:8083/docs/english/calendar.html`, plus the Links, Polls, Spam-X, Static Pages and XMLSitemap HTML pages
- `http://localhost:8083/admin/plugins/recaptcha/docs/english/config.html`

Check the page layout, CSS, navigation, modern guide search, historical help anchors and an actual **administration configuration help link**. Record observed HTTP failures and visual issues. If XMLSitemap remains disabled in this staging installation, verify its preserved help page URL without pretending that plugin runtime is functioning.

## 5. Restore (or preserve the validated candidate)

The helper prints the backup path. To restore the original documentation, **from the same directory**:

```bash
python3 test_chromebook_overlay.py --rollback --backup /exact/path/printed/by/helper
```

The helper verifies original file digests. Do not replace the backup with an assumed path. Do not run `docker compose down -v`.

## Acceptance evidence for the single upstream PR

Record: exact GitHub Actions run/commit, SHA-256 of the ZIP, isolated Docker project identity, observed PHP/Geeklog version, successful URLs, an actual Core help-button click, plugin documentation links, result of restoration (if performed), and failures/warnings. Do not include passwords or private log content.

**Go/no-go:** do not mark runtime integration as passed until the Chromebook test output and manual admin browser results have been reviewed. CI and a static HTTP server are only the preliminary gate.
