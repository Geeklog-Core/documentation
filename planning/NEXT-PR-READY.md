# Next documentation PR — reviewer handoff

**Target:** `Geeklog-Core/documentation:main`

**Head:** `hostellerie/documentation:docs/published-site-labels`

**Scope:** post-launch wording, nonrepeating homepage navigation/search, source-verified Geeklog 2.2.2 administration and Static Pages documentation, and maintenance/branch cleanup helpers.

## Proposed title

Docs: simplify published site and expand Geeklog 2.2.2 admin guides

## Proposed description

### Summary

Improve the published Geeklog documentation website and add practical, source-checked administration and plugin guidance without changing the release's historical context-sensitive help URLs or replacing the original embedded configuration reference.

### Website cleanup

- Remove obsolete prototype, preview and unpublished wording from generated public pages.
- Keep a **single catalogue** of 13 guides on the home page. Search results replace the visible catalogue while querying; when JavaScript is disabled the catalogue remains accessible.
- Remove duplicated introductory links and avoid repeating the home navigation.
- Add CI checks for the generated homepage and old labels.

### Documentation improvements

- Expand backup/recovery procedures to distinguish database exports from a complete recoverable Geeklog site.
- Add least-privilege user/group testing guidance, including `user.edit`, `group.assign`, `group.edit`.
- Document observed 2.2.2 admin URL and XMLSitemap installation pitfalls.
- Add post-update contextual-help tests for site administrators.
- Verify Static Pages plugin **1.7.3** feature rights using Geeklog `v2.2.2` source: `staticpages.edit`, `staticpages.delete`, and the separately protected `staticpages.PHP`.

### Compatibility and validation

- Retain the bundled `config.html` and plugin help unchanged. This PR does **not** claim full content parity with legacy configuration docs or full migration of historical Wiki articles.
- Verify the generated HTML, search links, ZIP overlay layout, legacy anchors, extraction/rollback simulation and static HTTP responses in GitHub Actions.
- Source-based checks are described separately from manual runtime claims: the new permission matrices have **not** been exercised against every plugin/user role.

### Repository maintenance

- Re-target CI to the active contributor branch and rename the old preview workflow.
- Close the obsolete fork draft PR #1 (done).
- Provide a **dry-run-first archival script** for old branches. Historical branches have **not** been deleted; archive tags must be confirmed by the repository owner before removal.

### After merge

The official Pages workflow is **manual**. Run **Publish Geeklog documentation (maintainer opt-in)** from upstream `main` and inspect the newly published home page and search, plus `configuration.html#desc_site_url`. Without this, the public site will still show the previous rendering.

### Remaining work outside this PR

- Full detailed Markdown replacement for historical `config.html` and plugin help.
- Historical Wiki provenance/license/attribution for any material proposed for republication.
- Additional runtime permission and full database restore tests.

## Reviewer checklist

- [ ] The latest `docs/published-site-labels` GitHub Actions run is green.
- [ ] Search and browse are visually mutually exclusive and keyboard accessible.
- [ ] 13 guide links are visible without JavaScript and each appears once.
- [ ] Legacy embedded configuration and plugin help remain byte-identical to their pinned sources.
- [ ] GitHub Pages publish workflow is run **after** merge, and live rendering confirmed.

**Submit after the latest branch build has passed.** No further archival-Wiki work is required for this targeted PR.
