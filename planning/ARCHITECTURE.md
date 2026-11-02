# Proposed documentation architecture

Status: proposal for maintainer review; no site generator or CI selected.

## Principles

1. One authoritative, English-language Markdown source maintained in `Geeklog-Core/documentation`.
2. Forks and pull requests with review before merging; no competing GitHub Wiki editing workflow.
3. Documentation versions tied to Geeklog release tags or maintenance branches.
4. Preserve existing help links and offline bundled HTML during the transition.
5. Use a selective, attributed recovery of historical wiki pages, not a full republish.

## Suggested future tree

```text
README.md
CONTRIBUTING.md
planning/
docs/
  getting-started/
  administration/
  plugins/
  themes/
  development/
  troubleshooting/
  reference/
  history/
assets/
```

This is a proposed layout, not a populated content tree. Start with a few reviewed pages before choosing a site builder.

## Build outputs (later phase)

- Static searchable documentation site, publication URL and hosting to be agreed with maintainers.
- Version-specific HTML bundle preserving legacy `public_html/docs/english/*.html` names and anchors where used by Geeklog.
- GitHub Actions should generate artifacts, validate links and anchors, and optionally propose a PR to Geeklog Core; never write directly to upstream master.
- Keep generated offline HTML self-contained with relative images/CSS; no required live GitHub/network calls.

## Editorial and release policy to decide

- Whether documents describe development `main` versus a tagged release.
- Migration procedure for existing Japanese documentation.
- Licensing of new documentation and reuse conditions for old MediaWiki materials.
- Ownership of DNS, website publishing and redirects.
- No changes to Geeklog 2.2.3 release scope without maintainer decision.
