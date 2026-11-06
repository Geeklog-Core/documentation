# Geeklog 2.2.2 configuration reference — content parity audit

Audit date: 2026-11-05. This audit compares `docs/configuration/README.md` on the current `docs/published-site-labels` working branch with the tagged Geeklog Core v2.2.2 `public_html/docs/english/config.html`. It supplements (does not supersede) `planning/CONFIGURATION-MIGRATION-222.md`.

## Incremental migration progress — 2026-11-05

The configuration landing page now identifies itself as the **Geeklog 2.2.2 configuration reference**, rather than an unpublished prototype. Its warning remains explicit: it is not yet the complete replacement for bundled `config.html`.

A first audited Markdown table restores seven historical default values, extracted from the [v2.2.2 tagged Core HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html):

| Anchor / setting | Historical default |
| --- | --- |
| `desc_site_url` | `http://www.example.com` |
| `desc_site_admin_url` | `http://www.example.com/admin` |
| `desc_site_name` | `Geeklog Site` |
| `desc_site_slogan` | `Another Nifty Geeklog Site` |
| `desc_mail_settings_port` | `25` |
| `desc_mail_settings_auth` | `0` |
| `desc_ip_anonymization` | `-1` |

`tools/check_configuration_coverage.py` now checks these values in generated online HTML and continues requiring the **embedded config.html to be byte-identical** to the original v2.2.2 source. These are documented *historical defaults* rather than universal recommended live settings, and this work does not certify the remaining 380 setting descriptions, 49 source tables or their embedded replacement.

## Reproducible defaults inventory — 2026-11-05

The workflow now runs `tools/audit_config_defaults.py` against the **pinned Geeklog 2.2.2** `public_html/docs/english/config.html`. The audit parses **387** `desc_*` table rows, extracts each row's displayed default into `dist/config-defaults-audit.json`, and explicitly marks only the **seven** individually source-checked entries as reviewed. This JSON file is a CI artifact for review and **is not published as official configuration guidance**.

The inventory checks for missing or duplicate help IDs and rejects changes to the seven validated default values. All remaining **380** entries require human editorial comparison, including contextual table notes, examples, markup, nontrivial defaults, and actual installer values. No automatic transformation of the old `config.html` into the embedded package is authorized by this progress.

## Full defaults transcription and compatibility candidate — 2026-11-05

**New migration work beyond the original 449-anchor structural coverage:**

- All **387 of 387 historical default values** from the tagged 2.2.2 reference are now written beside the existing Markdown setting descriptions, using the same setting identifiers. The previous seven-value summary table was removed to avoid duplicating entries. The transcription is checked against the original values on every CI build by `tools/audit_config_defaults.py`. **Only seven values have had separate human-style source review so far**; mechanically matching text is not full editorial verification.
- `tools/audit_config_defaults.py` records the complete **historical description text** next to the **maintained Markdown description** for each of the 387 settings in `dist/config-defaults-audit.json`. This creates a reviewable comparison for detecting missing explanations, rather than pretending that an anchor or default match proves content parity.
- A separate, **non-deployable** Markdown-generated `public_html/docs/english/config.html` candidate is built by `tools/build_config_candidate.py`. CI requires **all 449 unique historical anchors**, no unexpected/duplicate IDs, and 387 defaults, and checks its existing relative resources and internal links against the tagged 2.2.2 documentation tree.
- The candidate is uploaded as `geeklog-2.2.2-config-candidate-review` for review. It is **not** used in the standard 2.2.2 documentation ZIP or in the public site until maintainer approval and remaining parity gates.
- The candidate report now inventories original versus generated HTML tables, code blocks and local links. Those gaps still block replacing the embedded legacy reference.

**Remaining blocking work:** review 387 full descriptions against their source text, reconstruct the original section-specific tables, preformatted examples and internal cross-links, check applicable attribution/licensing, and test a complete candidate in the isolated Geeklog 2.2.2 administrator interface. The existing legacy `config.html` stays byte-identical.

**Earlier notes in this audit that refer to only seven migrated defaults or no available default values are historical snapshots, superseded by this section.** The old configuration reference is still authoritative for unreviewed wording and examples.

## Detailed appendix migration — 2026-11-05

The tagged 2.2.2 configuration HTML includes two substantial URL reference tables and a locale date-format list. The existing Markdown page previously mentioned these appendices without reproducing their detailed values.

- Migrated **10 URL rewriting examples** into the existing `url-rewrite` section, preserving legacy query-string and rewritten URL patterns.
- Migrated **10 URL routing rules and numeric priorities** into the existing `url-routing` section.
- Restored all **33 locale date-format directives** in source order with newly written, concise explanations. This retains the legacy syntax for reference; support in modern runtime environments still needs checking.
- `tools/build_config_candidate.py` now compares every rewriting/routing table cell against the tagged source and checks every date-format token. The latest CI [run #41980025419](https://github.com/hostellerie/documentation/actions/runs/41980025419) passed.
- Candidate output remains isolated from the official embedded `english/config.html` and has not undergone a live Geeklog admin-help integration test.

**Still outstanding:** detailed examples outside these appendices, the other historical tables and links, semantic review of the full 387 descriptions, compatible representation of obsolete links, and final real administrator tests. Do not infer that passing the two specific table checks proves full content parity.

## Cron appendices and source verification — 2026-11-05

- Expanded the existing `url-cron`, `cron_daily_digest`, and `cron_emailed_database_backup` Markdown sections rather than creating separate or duplicate guides.
- Restored the historic daily-digest cron example `30 2 * * * /path/to/geeklog/cron-emailgeeklogdailydigest` as a fenced, preformatted example, explicitly marked as a non-deployable example path.
- Cross-checked the two actual Geeklog `v2.2.2` root scripts. Both load `lib-common.php` from a configurable installation path; the digest script calls `COM_emailUserTopics()`; the emailed database backup uses `dbBackup` and is limited to MySQL in the tagged implementation. The historic `db_backup_sendto` and `lastemailedstories` behaviors are documented with backup/staging precautions.
- The isolated candidate checker now requires the cron command, script names, key configuration identifiers and a rendered `<pre>` block. [GitHub Actions #41980462276](https://github.com/hostellerie/documentation/actions/runs/41980462276) passed.
- This remains a **documentation/source-code verification**. No cron script was executed, no outgoing mail was sent, and no production database was modified. The standard Geeklog embedded `config.html` remains the original.

**Remaining release blockers:** reconcile the other historical explanatory tables and formatted examples, review the 387 descriptions semantically, resolve/categorize old link destinations, and run context-sensitive help tests with the candidate in a disposable Geeklog 2.2.2 installation.

## Comment templates and server examples — 2026-11-05

The maintained Markdown now contains the three historical comment-feed template shapes (article reference, article author and comment author), including the `%s` placeholder counts and escaped HTML template syntax. These are shown as **literal code examples**, not executable or trusted HTML.

The URL routing appendix also includes the historical **Apache `mod_rewrite` rule example**, its three rule/path variants, and an **IIS `web.config` front-controller example** with the two file/directory bypass conditions. All are explicitly described as historical examples requiring per-host security/configuration review, not deployment-ready configs.

Together with the previously migrated cron sample, the generated review candidate now contains **nine preformatted examples**, matching the number of legacy `<pre>` blocks. The candidate checker enforces that count and the expected example topics. [GitHub Actions #41994067764](https://github.com/hostellerie/documentation/actions/runs/41994067764) succeeded.

**Important limitation:** matching nine rendered example blocks does not prove literal equivalence of every legacy snippet. The IIS sample has a newly written rule label and the examples contain editorial explanation. A separate review of semantics and deployed routing behavior is still required. The original embedded Geeklog 2.2.2 `config.html` is unchanged.

## Historical link inventory and release gate — 2026-11-05

A distinct, repeatable `tools/audit_config_links.py` job now parses actual link elements in the **tagged Geeklog 2.2.2 HTML**, so escaped `href="%s"` examples are not mistaken for navigation. It produces `dist/config-link-audit.json` as part of the existing **isolated candidate-review artifact**, without changing the official embedded configuration document.

GitHub Actions [#41998134534](https://github.com/hostellerie/documentation/actions/runs/41998134534) succeeded and identified **34 distinct historical same-page fragment destinations**, **3 local document/stylesheet paths**, and **48 external URLs**. All 34 fragments resolve within the historical reference and all three relative targets exist in the pinned installation archive. These are **original reference links**, not proof that all navigation has been reproduced in the Markdown candidate.

The 48 external URLs are classified separately; Wiki references receive a provenance/replacement-review flag. CI deliberately **does not follow external links** or claim their availability. The candidate's current references are validated separately by `tools/build_config_candidate.py`. The remaining publication requirement is an editorial decision for each external link: keep as useful, replace with authoritative maintained documentation, retain clearly as a historical reference, or remove with a documented reason. Do not blindly reproduce deprecated or insecure destinations.

## Legacy internal cross-references restored in candidate — 2026-11-05

The original 2.2.2 `config.html` contains **34 distinct same-page `href="#..."` destinations**. All 449 targets were already migrated as identifiers, but the links themselves were not necessarily present in the generated HTML.

Added a clearly labeled **Historical configuration cross-references** section to `docs/configuration/README.md` that restores each of the 34 original same-page destinations as a usable Markdown link, grouped by core section, reference appendix and setting. These links are generated by the existing Markdown-to-HTML pipeline, not inserted into the bundled original.

`tools/build_config_candidate.py` now **fails** if any of the 34 original `href="#..."` references is absent from the generated candidate, or if a target anchor is missing. The regression passed in [GitHub Actions #42000100296](https://github.com/hostellerie/documentation/actions/runs/42000100296).

**Limitation:** this restores the source's set of navigation links, **not their original in-paragraph positions**. The 3 historical relative file links remain a separate online/embedded path decision; the 48 external URLs still need editorial relevance, licensing and link-target review. Do not declare complete link-content parity based on this navigation index.

## First source-backed semantic review batch — 2026-11-05

The 387 configuration help anchors and their historical defaults were previously migrated. This batch improves **actual descriptions**, focusing on five configuration options with compatibility or security implications: `mail_settings_backend`, `pass_alg`, `ip_anonymization`, `url_routing`, and `filemanager_disabled`.

The changes restore specific tagged 2.2.2 information: the `smtps` transport's OpenSSL requirement; the full five historical password hash algorithm identifiers with a modern-security caveat; the dependence of delayed database IP anonymization on `cron_schedule_interval` and its exclusion of log files; URL routing's rewrite prerequisite and the historic appendix; and the exact `filemanager_disabled=true` behavior, including the `Root` exception.

A small `tools/check_config_semantic_gates.py` guard now checks those critical option tokens against both the tagged source and maintained Markdown. This is a **targeted editorial regression check for five options**, not an automated approval of the remaining **382** descriptions. It does not claim that an installed Geeklog 2.2.2 administration UI has been tested.

## Second semantic review batch — mail and account protection (2026-11-06)

Reviewed **seven additional** descriptions against tagged Geeklog `v2.2.2` documentation: `noreply_mail`, `mail_settings_port`, `mail_settings_auth`, `invalidloginattempts`, `invalidloginmaxtime`, `enable_twofactorauth`, and `pass_stretch`. This is a substantive correction batch rather than an additional structural inventory.

The Markdown now clarifies the original mail sender/reply behavior, historic SMTP port examples `25` and `587` without recommending them for current providers, authentication's `1`/`0`/empty distinction, the `0` switches that disable invalid-login notifications, the interaction between warning and login speed limits, per-user two-factor enrollment, and the historical password stretch requirement (greater than zero). Historical behavior must not be confused with current security best practices.

`tools/check_config_semantic_gates.py` now validates key source-backed details for **12 settings** (the prior five plus this batch). [CI #42139862435](https://github.com/hostellerie/documentation/actions/runs/42139862435) succeeded.

**Review accounting:** 12/387 descriptions have received these targeted source-checked improvements; **375 descriptions** remain outside these focused checks. This does not establish content parity for those 375 settings or validate running configuration behavior. The embedded `config.html` remains byte-identical to the v2.2.2 reference.

## Third source-backed semantic review — account and moderation settings (2026-11-06)

Reviewed **10 additional** configuration descriptions against the tagged 2.2.2 reference: `allow_account_delete`, `allow_username_change`, `custom_registration`, `usersubmission`, `disable_new_user_registration`, `allow_domains`, `disallow_domains`, `storysubmission`, `commentsubmission`, and `trackback_enabled`.

Restored the exact enabled/disabled meaning of account and submission controls, the retention of anonymized article/comment attribution after account deletion, byline changes after a username change, the `lib-custom.php` registration hook, queued-account handling when approval is disabled, distinctions between allowlist bypass and denylist enforcement, and separate article/comment moderation queues. The source's contradictory `trackback_enabled` boolean wording is flagged rather than copied as reliable operational advice.

The targeted `tools/check_config_semantic_gates.py` now checks **22 setting descriptions** against original source content and the current Markdown, with HTML whitespace normalization. [GitHub Actions #42140701426](https://github.com/hostellerie/documentation/actions/runs/42140701426) succeeded. Earlier runs in this batch exposed a missing queue wording detail and a whitespace comparison defect; both were corrected.

**Review accounting:** 22/387 targeted setting descriptions checked, leaving **365 without this specific review**. This does **not** prove complete prose parity, current security suitability, plugin functionality, or installed admin behavior. Historical `english/config.html` remains unchanged and no deployable candidate is approved.

## Permissions matrix verified against original 2.2.2 values — 2026-11-06

Inspected all 12 historical default-permission setting descriptions for new articles, topics and blocks (`default_permissions_{story,topic,block}_{0..3}`). They already contained the original values and short explanations in Markdown, so they were **not rewritten or counted as newly semantically reviewed settings**.

Added a clearly labeled role matrix to the existing permission section. The 2.2.2 defaults are **Read-Write for the owner** and **Read-Only for group, logged-in users and anonymous visitors** for each of the three content types. This table describes initial defaults for **new items**, not permissions granted on existing content or recommended current settings. The accompanying guidance distinguishes content editing from autotag `Use` rights and explicitly warns about anonymous access and non-retroactive changes.

Added `tools/check_config_permission_matrix.py`, which parses the tagged 2.2.2 HTML and the Markdown-generated table and checks **every one of its 12 cells**. Wired the gate into `.github/workflows/dual-preview.yml`; [GitHub Actions #42144608822](https://github.com/hostellerie/documentation/actions/runs/42144608822) passed.

**Review accounting remains unchanged:** 22 descriptions in targeted semantic review; the 12 permission defaults had already been transcribed and are now additionally covered by a **matrix-specific parity test**, not a new claim of broad prose review. Live authorization tests and full editorial parity are still outstanding; the original embedded `config.html` remains unchanged.

## Decision

**BLOCK replacement of embedded `docs/english/config.html`.** Structural anchor coverage (387 help anchors and 62 historical navigation anchors) is necessary but not sufficient. The current embedded file must stay byte-for-byte the tagged original.

## Baseline evidence

| Check | Tagged Core 2.2.2 HTML | Migrated Markdown | Result |
| --- | ---: | ---: | --- |
| Unique historical anchors | 449 | 449 preserved by existing coverage check | Structural gate only |
| Individual help anchors | 387 | 387 preserved | Structural gate only |
| HTML tables | 49 | Two restored URL mapping tables plus one date-format directive table | **Other table content still requires review** |
| HTML table rows | 462 | 20 URL mapping rows and 33 date-format directives now tabulated; defaults appear in each setting's section | **Full table parity remains unverified** |
| HTML code/preformatted blocks | 9 `<pre>` elements | 9 preformatted examples in candidate | **Structural count checked; snippet semantics still under review** |
| HTML list items | 76 `<li>` elements | Must compare manually/semantically | Review required |
| Historical HTML characters | 174,651 | 110,804 Markdown characters | Not a valid proof of missing text alone |

Counts are indicators, not claims that each HTML row needs a one-to-one Markdown table. The historic reference has **49 tables**, including configuration defaults and explanations. The Markdown reference has all 387 setting descriptions, 449 anchors and each original documented default, plus the URL mapping/routing and date-format tables. This does not certify parity for the remaining original table layouts, examples and explanations.

## Confirmed content loss / incomplete topics

1. **Setting defaults:** The source's `Variable | Default Value | Description` tables have not been fully transcribed. Examples from the tagged HTML: `site_url` defaults to `http://www.example.com`; `site_name` defaults to `Geeklog Site`; `mail_settings_port` defaults to `25` in the source table. The Markdown entry for the latter instead advises matching the port to the server, without preserving the documented v2.2.2 default.
2. **URL rewriting and routing:** Markdown itself says the historical URL mapping and route priority tables still need migration. Restore their complete legacy examples and test representative paths.
3. **Locale/date formatting:** Markdown retains some format tokens but explicitly says the full formatting table is missing.
4. **Cron scripts and schedules:** Markdown provides concise summaries rather than the full invocation examples and operational instructions.
5. **Syndication/comment formats:** Three historical template forms are now displayed as code with placeholder explanations. Exact runtime formatting and escaping behavior still require source-level and staging verification.
6. **Other deep explanations:** Review all 387 setting descriptions against the HTML source and actual tagged 2.2.2 config definitions, including permissions, mail, authentication, file manager, OAuth and IP anonymization.
7. **Relative references and assets:** Tagged HTML refers to `../docstyle.css`, `../images/logo.gif`, `index.html`, `spamx.html` and various internal fragment links. A generated embedded file must resolve the relative assets and links from `public_html/docs/english/config.html`, not the online preview base URL.
8. **Historical outgoing links:** External references include obsolete Wiki and third-party destinations. Record and classify each (valid, replacement, archived, historical-only), rather than silently deleting it.

## Required next implementation

- Extract an auditable source manifest keyed by legacy section and `desc_*` ID, retaining the original **default value, full explanatory content, code snippets, tables, internal/external links and asset references**.
- Generate Markdown or a structured source sidecar (e.g. YAML/JSON) from that inventory. If a sidecar is used, keep the Markdown + sidecar as **one maintained source**, with both online and embedded outputs derived from it.
- Build a repeatable diff with hard failures for missing IDs, unreviewed rows/defaults, missing code examples, missing local-link targets and untracked assets. Semantic/editorial comparison should be a separate signed-off gate, not inferred from matching character counts.
- Rebuild the candidate `english/config.html` only in a **separate staging directory**. Check 449 anchors, relative references, accessibility of configuration help fragments and all expected assets at the old paths.
- On a disposable Geeklog 2.2.2 installation, open real help buttons for representative settings in each group, including `config.html#desc_site_url`, `#desc_mail_settings_port`, `#desc_ip_anonymization`, and `#desc_filemanager_disabled`. Verify rendered tables, code blocks and navigation with browser testing.
- Review source attribution and applicable licensing before publishing the transformed reference.
- Only after all checks pass, modify the embedded bundler to replace historical `english/config.html`; retain a byte-identical 2.2.2 archival baseline and a rollback path.

## Scope and status

This is a **static repository audit**; no 2.2.2 staging administration session was operated, and the source content has **not yet been fully transformed**. No embedded files have been replaced. Exact tag verified at `https://raw.githubusercontent.com/Geeklog-Core/geeklog/v2.2.2/public_html/docs/english/config.html`.
