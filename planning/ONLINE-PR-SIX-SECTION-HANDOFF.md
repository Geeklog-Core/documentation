# Online documentation PR — six sections and 25 guides

**Scope:** Public online documentation first (P0). Version-specific embedded help for Geeklog 2.2.3 remains an independent future release task.

## What this PR delivers

- Restructure the homepage into **six task-oriented sections**, retaining every previously indexed guide exactly once.
- Expand from **13 to 25 searchable Markdown-based guides**, adding twelve original first-edition guides on using Geeklog, articles/topics, blocks/menus, comments/moderation, plugin management, plugin/theme development, RSS/autotags, bundled plugins, database model, FAQ and contribution.
- Preserve the historical Geeklog **2.2.2** configuration help and other original embedded plugin documentation unchanged in the experimental dual-output package.
- Improve responsive homepage layout, including appropriate spacing between the search label and input.
- Add two related-reading links to each of the **22** modern guides, with offline-safe relative URLs.
- Improve operational troubleshooting, backups, editor/permission guidance and developer lifecycle checklists.
- Add structural tests for grouped navigation, search index, source-guide parity, local links/fragments and non-regressing search fallback behavior.
- Provide a documented information architecture, coverage matrix, historical Wiki disposition and editorial follow-up inventory.

## Verification and boundaries

Branch CI checks source-generated online HTML and experimental offline ZIP compatibility, local HTTP reachability, MIME types, searchable destinations, local hyperlinks/anchors and the unchanged historical configuration help.

The new pages are **first-edition orientation guides**, not full runtime-validated specifications: administrator UI paths, upgrade/restore operations, template internals, plugin contracts and database schema details still require source and live-staging verification. The old Wiki had 351 recovered pages and only 14 were classified individually; the remaining pages were not bulk imported. Historical Wiki attribution/licensing remains unresolved, and no unverified text, screenshots or SQL were reprinted.

**This PR is not a certified embedded documentation release for Geeklog 2.2.3.** It keeps the original 2.2.2 admin help intact.

## Maintainer deployment checklist

1. Confirm the CI result on the PR's final head.
2. Review the six-section home and representative P0 guide content, especially the explicit release-scope caveats.
3. Check keyboard/mobile layout and search behavior manually.
4. Merge to `Geeklog-Core/documentation:main` if approved.
5. Run `Publish Geeklog documentation (maintainer opt-in)` on official `main`, and inspect the live 25-guide homepage.
6. Track deeper editorial acceptance and future Geeklog 2.2.3 embedded packaging as separate work.

## Supporting records

- `planning/ONLINE-SIX-SECTION-COVERAGE.md`
- `planning/ONLINE-DOCUMENTATION-AUDIT.md`
- `planning/WIKI-PILOT-14-AUDIT.md`
- `planning/EDITORIAL-PROVENANCE-REVIEW-222.md`
