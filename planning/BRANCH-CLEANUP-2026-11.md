# Geeklog documentation — branch cleanup and historical work inventory

Reviewed on 2026-11-05, after upstream PR #5 was merged. **Keep one active feature branch** (`docs/published-site-labels`) and the default `main` branch. The publication workflow remains controlled by the official upstream repository.

## Branches whose commits are fully contained in the active branch

The GitHub comparison against `docs/published-site-labels` returned `ahead_by=0` for the following branches. They can be deleted **after checking there are no open PRs pointing to them**:

- `docs/installation-migration`
- `docs/post-launch-cleanup`
- `prototype/dual-output-222`
- `prototype/wiki-unified-222`
- `release/unified-docs-preview`

Note: the published upstream `main` already includes the consolidated documentation PR #5. This does **not** mean the fork's local `main` ref is synchronized.

## Divergent historical branches — archive before deletion

These branches have commits not contained in the active branch. Avoid merging stale Markdown, workflow, installation guidance or audits blindly over newer verified documents.

| Branch | Unique historical value | Recommended treatment |
| --- | --- | --- |
| `docs/configuration-reference` | `planning/CONFIG-MIGRATION-STATUS.md` not yet in active tree; earlier configuration draft | Archive branch by Git tag, review status document against current configuration audit |
| `docs/installation-release-audit-222` | 40 divergent commits but core installation/staging documents and tools are present in later form in the active tree | Archive reference by Git tag; do not replay its earlier changes |
| `audit/config-content-parity-222` | One divergent commit; current parity audit exists in active tree | Archive as historical snapshot only |
| `docs/wiki-recovery-inventory-2024` | Historical recovery scripts (`wiki_catalog_review.py`, `wiki_navigation.py`, `wiki_review_pack.py`) and `planning/WIKI-RECOVERY-2024.md` not in active tree | **Preserve by tag** before deleting; review scripts for safe reuse in later Wiki migration |
| `feature/initial-documentation` | Original pilot workflow and documentation baseline | Historical tag sufficient; not a competing working branch |

A Git tag is a durable repository reference to the complete commit snapshot. Do not delete any divergent branch unless its tag is verified on GitHub first.

## Local cleanup command — requires contributor credentials

The connected GitHub integration available during this review **does not expose branch deletion**. The maintainer can use `gh` on the Chromebook. Commands below delete only branches known to be fully contained in the active branch; no forced deletion:

```bash
REPO=hostellerie/documentation
for branch in \
  docs/installation-migration docs/post-launch-cleanup \
  prototype/dual-output-222 prototype/wiki-unified-222 \
  release/unified-docs-preview
do
  gh api -X DELETE "repos/$REPO/git/refs/heads/$branch"
done
```

For historical divergent branches, **first create one archive tag per branch**, then confirm tags were pushed before choosing to delete branches. Example:

```bash
git clone https://github.com/hostellerie/documentation.git
cd documentation
git fetch origin --prune
for branch in \
  docs/configuration-reference docs/installation-release-audit-222 \
  audit/config-content-parity-222 docs/wiki-recovery-inventory-2024 \
  feature/initial-documentation
do
  tag="archive/2026-11-05/$(echo "$branch" | tr / -)"
  git tag "$tag" "origin/$branch"
  git push origin "$tag"
done
git ls-remote --tags origin 'refs/tags/archive/2026-11-05/*'
```

Only after confirming all expected tags exist on remote, delete the corresponding historical branches through `gh api -X DELETE`. Keep the main and active branches untouched.

## What remains active

- `Geeklog-Core/documentation:main`: official published source.
- `hostellerie/documentation:main`: fork default branch, to be kept in sync with upstream (fast-forward after verifying its history).
- `hostellerie/documentation:docs/published-site-labels`: **only** current working branch for wording cleanup, improvements and complementary docs.
- Archived Git tags: historical references only, not parallel development lines.
