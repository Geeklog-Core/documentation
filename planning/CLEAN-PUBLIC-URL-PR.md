# PR handoff — clean public routes and documentation navigation

## Proposed pull request

**Title:** `docs: publish clean URLs and improve six-section navigation`

**Create PR:** https://github.com/Geeklog-Core/documentation/compare/main...hostellerie:documentation:docs/clean-public-urls?expand=1

**Base:** `Geeklog-Core/documentation:main`  
**Head:** `hostellerie/documentation:docs/clean-public-urls`  
**CI:** https://github.com/hostellerie/documentation/actions/runs/42374403729 (passed)

## Summary

- Change 3 flat website pages to directory routes (`/installation/`, `/configuration/`, `/administration/`).
- Remove `/modern/` from **public URLs**. The initial public User Guide becomes `/user-guide/`.
- Reclassify the stable Plugin API, Configuration API and Webservices API routes under `/reference/`.
- Merge troubleshooting and FAQ into one **public** guide while preserving the historical source and embedded FAQ output.
- Rename Reference & Archive to Technical Reference, grouping 4 references.
- Add a homepage beginner pathway: install → configure → publish → manage users → back up.
- Use compact six-section links, breadcrumbs, on-page contents and previous/next guide navigation.
- Link administrator users/groups to developer security/permissions rather than duplicate content.
- Adjust unified website search, generated HTML, static audits, HTTP checks and documentation summaries.
- Public output: **24 searchable guides and 25 HTML pages**, with no redirect or compatibility page.
- Embedded Geeklog 2.2.2 layout and historical Core/plugin help paths **unchanged**. The embedded `/english/modern/` subtree is intentionally retained.

## Publication boundaries

**No redirects or public compatibility pages**, per project decision. Existing public URLs such as `/modern/user-guide/overview/index.html` and `/installation.html` will no longer resolve after official deployment. Update external links manually if needed.

Merge does not deploy the official Pages website automatically: the upstream maintainer must run the existing manual GitHub Pages publishing workflow.

The CI verifies structure, links, rendered documents, static HTTP requests and archive preservation. It does not certify browser visual QA or actual Geeklog administration and plugin workflows. The separate 30-case staging suite remains pending.

## Permission note

The connected GitHub integration could push the contributor branch and run CI but returned **HTTP 403** when attempting to create an upstream pull request. Open it using the compare link above.
