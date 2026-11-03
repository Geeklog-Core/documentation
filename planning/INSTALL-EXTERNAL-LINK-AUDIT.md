# External-link audit — installation draft

Reviewed: 2026-11-01. Scope: Markdown installation guide links only, **not all inherited Core HTML pages**.

| URL | Role | Check | Follow-up |
| --- | --- | --- | --- |
| https://github.com/Geeklog-Core/geeklog | Official source | Public project page accessible | Keep |
| https://github.com/Geeklog-Core/geeklog/blob/master/public_html/docs/english/install.html | Historical installation source | Path verified directly in GitHub connector; browser fetch was inconclusive | Keep as source citation |
| https://www.geeklog.net/ | Project website | Public site accessible | Keep |
| https://github.com/hostellerie/documentation/blob/docs/installation-migration/planning/INSTALL-REQUIREMENTS-SOURCE-AUDIT.md | Contributor's source audit | File exists in this branch | Replace branch-specific reference with stable published documentation before release |

The text also contains `https://example.com/` and `https://YOUR-SITE/admin/install/index.php` in code/examples. They are **illustrative**, not endpoints for automated availability checks.

This report is a point-in-time manual verification; it is not a guarantee that external URLs remain reachable. GitHub Actions should avoid live external HTTP dependencies in mandatory installation preview checks.

## Approval gates

- **Technical:** review actual installation/upgrade/migrate workflow on isolated Geeklog staging before declaring user documentation authoritative.
- **Editorial:** Tom should approve target version, historic link corrections and documentation architecture before merging, publishing or replacing Core HTML.
- **Optional author approval:** whether to keep a link to the contributor branch in the public guide. Prefer a stable official reference after the new documentation repository architecture is approved.

No PR should be opened before Tom's response on foundation PR #1.
