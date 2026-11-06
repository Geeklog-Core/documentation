# Geeklog 2.2.2 — configuration candidate acceptance (NOT approved)

Status: **PREPARED / runtime test pending**. This is a manual-only procedure for the **isolated, disposable** Geeklog 2.2.2 staging site. The existing official-style documentation overlay has already had separate acceptance testing; that **does not** validate this new Markdown-generated configuration candidate.

## Separate the two archives

- `geeklog-2.2.2-embedded-docs-preview` is the standard overlay with the **original** `docs/english/config.html`.
- `geeklog-2.2.2-config-candidate-review` is an **isolated artifact** that contains `config-candidate-review.zip` with **one file**, `public_html/docs/english/config.html`. It is **not** a distributable update and must **never** be passed to `test_chromebook_overlay.py`.
- The candidate must not replace Core documentation, the public site or the user's existing production/older test installations.

## Gate A — repository and artifact

Use the exact successful workflow run on `docs/published-site-labels`, record its commit SHA, download only `geeklog-2.2.2-config-candidate-review`, and inspect the inner ZIP before use. GitHub Actions runs `tools/check_config_candidate_review.py` to enforce one entry, source-archive integrity, the exact 449-anchor set, ten representative contextual-help anchors and same-page links.

The extracted candidate HTML must **not** be presented as live-validated content solely because CI passed. Maintain distinct evidence for: (a) static/structural parity and (b) browser behavior in Geeklog.

## Gate B — disposable installation (manual operator approval required)

Before any file replacement, check the existing **isolated** staging site identity: `~/geeklog-docs-validation/staging-222/site` and its `compose.yaml`, separate Docker project `geeklog-docs-stage`, and local-only HTTP binding. Do **not** touch `geeklog222-web`, `geeklog211-web`, production directories or shared database volumes.

1. Record the exact artifact run and SHA-256, and confirm the ZIP contains **only** `public_html/docs/english/config.html`. Inspect `config-candidate-report.json` for the explicit `INCOMPLETE` content-parity status.
2. Save an independent, access-restricted copy of the site's current `public_html/docs/english/config.html`; record its SHA-256. Refuse if target or ancestor is a symlink, if the site identity differs, or if a backup cannot be verified.
3. **Only with the local operator's deliberate approval**, place the candidate at the equivalent path in that isolated site's web root (this is intentionally **not automated by CI**). Never overwrite the source file in GitHub or any packaged Core release.
4. After the test, restore the exact pre-test file from the recorded backup and verify its SHA-256 matches. Do not remove Docker volumes or change DB settings. If restoring fails, stop and report a blocker.

## Gate C — browser and administrator help

From the isolated site on `http://localhost:8083`, verify the layout, local CSS, fragment scrolling and expected explanations for these URLs:

| Category | Expected fragment |
| --- | --- |
| Site configuration | `docs/english/config.html#desc_site_url` |
| Mail | `#desc_mail_settings_port` |
| Privacy | `#desc_ip_anonymization` |
| Filemanager | `#desc_filemanager_disabled` |
| Anonymous article permission | `#desc_default_permissions_story_3` |
| Structured-data autotag | `#desc_autotag_permissions_structureddata_1` |
| Article placement | `#desc_frontpage` |
| Comment moderation | `#desc_commentsubmission` |
| Multilingual mapping | `#desc_language_files`, `#desc_languages` |

Also open **actual help links from the Geeklog administrative Configuration interface**, for representative Core options, using an authorized staging admin session. Confirm that the application builds the expected URL, anchors scroll to the correct setting, group subsections remain understandable, there is no blank/404 screen, and the help does not redirect to the published online preview. Inspect responsive rendering and keyboard navigation where feasible.

A successful direct URL **does not** prove an administrator help button works. Authentication/role-specific runtime checks should be performed with separate least-privileged staging accounts; do not infer that matrix defaults guarantee authorization.

## Gate D — editorial and release decision

Record pass/fail and date for each observed test, exact Geeklog/PHP versions, site environment, candidate ZIP hash, backup hash and restoration hash. **Exclude credentials and private site data**. Record missing explanations, outdated third-party links, inconsistent HTML tables and accessibility problems as blockers with references to the original tagged source.

Do **not** mark `config.html` ready to replace until real administrator links, complete prose/table/example/link parity, contributor attribution/licensing and maintainer approval pass. An isolated successful runtime experiment is necessary, **not sufficient**, for upstream PR acceptance.

Current status: no manual application of this candidate and no configuration-help runtime acceptance have been performed by this document or CI.

## Gate E — reproducible evidence form (complete only after actual testing)

Keep one copy per tested candidate commit and staging installation. **Never mark a row PASS based only on CI or direct URL checks.**

| Test / observation | Result (PASS / FAIL / NOT RUN) | Evidence / observation |
| --- | --- | --- |
| Staging site and separate Docker volume identity checked | NOT RUN | |
| Candidate ZIP run ID, commit and SHA-256 verified | NOT RUN | |
| One-file ZIP and source report checked | NOT RUN | |
| Original `config.html` backed up and SHA-256 recorded | NOT RUN | |
| Direct URLs and fragment navigation (10 sample targets) | NOT RUN | |
| Real configuration help clicks (site, mail, privacy, permissions) | NOT RUN | |
| CSS and HTML tables render correctly | NOT RUN | |
| Keyboard navigation and narrow viewport | NOT RUN | |
| Non-administrator or anonymous access checks | NOT RUN | |
| Original help restored and digest compared | NOT RUN | |
| Remaining wording, link, license review completed | NOT RUN | |

Metadata to fill: `date_utc`, `candidate_commit`, `github_actions_run`, `candidate_zip_sha256`, `geeklog_version`, `php_version`, `docker_project`, `backup_sha256`, `restored_sha256`, `operator`. Use non-sensitive identifiers; exclude usernames, tokens, cookies and server secrets.

A test is **FAIL** when the observed browser/administrator behavior differs from the expected target. A test is **NOT RUN** when evidence has not been collected. Keep blockers open and attach sanitized screenshots or notes only if authorized.
