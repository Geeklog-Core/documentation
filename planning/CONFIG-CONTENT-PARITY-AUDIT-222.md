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

## Decision

**BLOCK replacement of embedded `docs/english/config.html`.** Structural anchor coverage (387 help anchors and 62 historical navigation anchors) is necessary but not sufficient. The current embedded file must stay byte-for-byte the tagged original.

## Baseline evidence

| Check | Tagged Core 2.2.2 HTML | Migrated Markdown | Result |
| --- | ---: | ---: | --- |
| Unique historical anchors | 449 | 449 preserved by existing coverage check | Structural gate only |
| Individual help anchors | 387 | 387 preserved | Structural gate only |
| HTML tables | 49 | One new 7-setting default table; previous setting descriptions are prose | **Content/format gap remains** |
| HTML table rows | 462 | Seven historical defaults now in a table; complete table parity unverified | **Content/format gap remains** |
| HTML code/preformatted blocks | 9 `<pre>` elements | 0 fenced code blocks | **Example-format gap** |
| HTML list items | 76 `<li>` elements | Must compare manually/semantically | Review required |
| Historical HTML characters | 174,651 | 110,804 Markdown characters | Not a valid proof of missing text alone |

Counts are indicators, not claims that each HTML row needs a one-to-one Markdown table. The historic reference has **49 tables**, including configuration defaults and explanations. The Markdown reference already has all 387 setting descriptions and 449 anchors, and now includes one seven-setting default table; the remaining original default-value columns, examples and explanatory details have not been checked for content parity.

## Confirmed content loss / incomplete topics

1. **Setting defaults:** The source's `Variable | Default Value | Description` tables have not been fully transcribed. Examples from the tagged HTML: `site_url` defaults to `http://www.example.com`; `site_name` defaults to `Geeklog Site`; `mail_settings_port` defaults to `25` in the source table. The Markdown entry for the latter instead advises matching the port to the server, without preserving the documented v2.2.2 default.
2. **URL rewriting and routing:** Markdown itself says the historical URL mapping and route priority tables still need migration. Restore their complete legacy examples and test representative paths.
3. **Locale/date formatting:** Markdown retains some format tokens but explicitly says the full formatting table is missing.
4. **Cron scripts and schedules:** Markdown provides concise summaries rather than the full invocation examples and operational instructions.
5. **Syndication/comment formats:** Historical literal templates, placeholders, and formatted examples (including the `sprintf` argument order) require exact preservation, not just paraphrases.
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
