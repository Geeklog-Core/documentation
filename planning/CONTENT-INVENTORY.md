# Existing documentation inventory

Status: initial filename-level inventory, 2026-10-29. Content verification and dependency audit are pending.

## Current Geeklog Core documentation

Source: https://github.com/Geeklog-Core/geeklog/tree/master/public_html/docs

| Source | Files | Initial handling |
| --- | --- | --- |
| `english/` | `index.html`, `install.html`, `config.html`, `support.html`, `changes.html` | Prioritize for content review; maintain existing link targets |
| `english/` | `theme.html`, `themevars.html` | Compare with current theme/template implementation |
| `english/` | `calendar.html`, `links.html`, `polls.html`, `spamx.html`, `staticpages.html`, `xmlsitemap.html` | Assess each bundled plugin's current status and docs contract |
| `english/` | `trackback.html` | Verify current functionality, safety and relevance |
| `japanese/` | 15 HTML files plus `docstyle.css` | Preserve as historical source; translation retirement needs maintainer decision |
| `images/`, `docstyle.css` | Assets/style | Preserve where referenced by generated offline HTML |
| Root | `history`, `changed-files`, `removed-files`, `license` | Retain existing release/packaging management until independently assessed |

All counts are file listings, not a claim that pages have been checked for correctness. English: 14 HTML files. Japanese: 15 HTML files (plus a CSS file).

## Historical wiki

Candidate reference: https://web.archive.org/web/20210917094332/http://wiki.geeklog.net/Special:AllPages

Do not blindly import the old MediaWiki. Classify pages as current/update/archive/omit. Prioritize installer/configuration, plugin APIs, themes, development, troubleshooting. Collect provenance and licensing before republication. A complete export from Dan would aid preservation but is not a dependency for a pilot.

## Audit checklist

- [ ] Confirm current contents, age and scope of each English document against Geeklog Core and bundled plugins.
- [ ] Identify duplicated, obsolete, missing and externally linked content.
- [ ] Identify source ownership/licensing and image provenance.
- [ ] Record URL, anchors and asset references before conversion.
- [ ] Compare current configuration options with the separate configuration audit.
- [ ] Classify old wiki pages and capture available public archive URLs.
- [ ] Decide how release history and Japanese legacy documents remain accessible.
