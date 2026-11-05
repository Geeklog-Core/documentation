# Upstream pull request handoff — Geeklog 2.2.2 documentation

> GitHub connector cannot open pull requests in `Geeklog-Core/documentation`: `403 Resource not accessible by integration` (2026-11-05). This file is the prepared **single official PR**, to be opened by contributor `hostellerie` using the GitHub website or their local `gh` authentication. No upstream PR was created by the connector.

**Target:** `Geeklog-Core/documentation:main`

**Head:** `hostellerie/documentation:prototype/wiki-unified-222`

**Title:** Docs: consolidate Geeklog 2.2.2 online and embedded documentation

**Create:** https://github.com/Geeklog-Core/documentation/compare/main...hostellerie:documentation:prototype/wiki-unified-222?expand=1

## PR description — copy below

### Purpose

This PR proposes the **first maintainable Geeklog 2.2.2 documentation edition** with a searchable online output and an offline-compatible embedded documentation ZIP produced from maintained Markdown, while preserving historical Core/plugin context-sensitive help. It is a version-scoped delivery milestone, **not** a full migration of the 351-page historic Wiki.

### Included

- 13 searchable public guides (15 HTML pages) covering installation/configuration and 10 modern supplementary topics.
- Generated `public_html/` overlay ZIP with Markdown-generated installation help, additional modern guides, and unchanged legacy configuration/plugin docs at their original paths.
- Automated checks for historical anchors and compatibility, generated links, CSS/JS/search, ZIP extraction and restoration, and HTTP-served output.
- Reproducible, guarded Chromebook 2.2.2 staging deploy/rollback script and documentation.
- Editorial/provenance and content-parity audits; 14 historical Wiki pages classified for a selective pilot.

### Tested

- GitHub Actions build/validation: [fork workflows](https://github.com/hostellerie/documentation/actions).
- [Built ZIP artifact from run #41964801825](https://github.com/hostellerie/documentation/actions/runs/41964801825): `geeklog-2.2.2-docs-preview.zip`, 60 entries, SHA-256 `d4bc5bd80229e3d503d174dbd30d1bf02ae27bb0e1ff5f1dcd535bbb0915d69d`.
- **Real Chromebook Docker staging:** `geeklog-docs-stage`, Geeklog 2.2.2, PHP 8.1, MariaDB 10.11, Web bound to `127.0.0.1:8083`.
- Operator confirmed ZIP extraction and safe install, **12/12 HTTP 200**, visual design/navigation/search, Plugin API guide, actual admin help link and a successful **rollback** from the backup `docs-qa-backup-20261105-112828`.
- Evidence: [staging validation](planning/INSTALL-STAGING-VALIDATION.md) sections O–P. Browser and rollback results were **operator-reported**.

### Important limits / approvals

- Online `configuration.html` has 387 preserved help IDs and 449 unique historical identifiers, but does **not** yet reproduce the full `config.html` tables/defaults/examples. The embedded original `config.html` is intentionally preserved unchanged.
- Only 14/351 historical Wiki pages have been classified. Do not portray this as full Wiki migration.
- Historical Wiki page-specific contributor credits and reuse license are **unverified**. Avoid importing unlicensed Wiki prose or images; maintainers should confirm policy and editorial acceptance before publishing officially. See [editorial provenance register](planning/EDITORIAL-PROVENANCE-REVIEW-222.md).
- XMLSitemap help URL tested, but XMLSitemap itself was disabled in this disposable stage due to an independent filesystem permission issue.
- No Geeklog upgrade/migration drill or production hardening claims.

### Maintainer checklist

- [ ] Confirm architecture, generated outputs and backward compatibility for 2.2.2.
- [ ] Confirm attribution and Wiki-content license policy.
- [ ] Review technical wording and outstanding configuration parity work.
- [ ] Ensure latest branch CI is green.
- [ ] After merge, run the maintainer opt-in GitHub Pages publication workflow on upstream `main` and inspect the live site.
- [ ] Decide how and when the tested embedded ZIP is distributed with Geeklog releases.

See [release checklist](planning/DELIVERY-222.md). This PR is ready for **maintainer review**, not automatic publication.
