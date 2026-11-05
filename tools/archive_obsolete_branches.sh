#!/usr/bin/env bash
# Archive obsolete Geeklog documentation branches as immutable Git tags, then delete refs.
# DRY RUN by default: pass --apply to perform any mutation.
set -euo pipefail

REPO="hostellerie/documentation"
DATE="2026-11-05"
BRANCHES=(
  audit/config-content-parity-222
  docs/configuration-reference
  docs/installation-migration
  docs/installation-release-audit-222
  docs/post-launch-cleanup
  docs/wiki-recovery-inventory-2024
  feature/initial-documentation
  prototype/dual-output-222
  prototype/wiki-unified-222
  release/unified-docs-preview
)

if [[ ${1:-} != "--apply" ]]; then
  echo "DRY RUN only. Use --apply to archive and remove obsolete branch refs."
  echo "This never deletes main or docs/published-site-labels."
  printf '  %s\n' "${BRANCHES[@]}"
  exit 0
fi

gh auth status
# Prevent deletion of any head still used by a live pull request.
for repo in "hostellerie/documentation" "Geeklog-Core/documentation"; do
  open_heads=$(gh api "repos/$repo/pulls?state=open&per_page=100" --jq '.[].head.ref')
  for branch in "${BRANCHES[@]}"; do
    if grep -Fxq "$branch" <<<"$open_heads"; then
      echo "STOP: $repo has an open PR using $branch" >&2
      exit 1
    fi
  done
done

echo "Archiving all historical branches BEFORE deleting any branch..."
for branch in "${BRANCHES[@]}"; do
  sha=$(gh api "repos/$REPO/git/ref/heads/$branch" --jq '.object.sha')
  tag="archive/$DATE/${branch//\//-}"
  if current=$(gh api "repos/$REPO/git/ref/tags/$tag" --jq '.object.sha' 2>/dev/null); then
    if [[ "$current" != "$sha" ]]; then
      echo "STOP: existing tag points to a different commit: $tag" >&2
      exit 1
    fi
    echo "Tag exists and matches: $tag"
  else
    gh api -X POST "repos/$REPO/git/refs" -f "ref=refs/tags/$tag" -f "sha=$sha" --silent
    echo "Archived: $branch -> $tag"
  fi
done

echo "Verifying every remote tag before deleting branch refs..."
for branch in "${BRANCHES[@]}"; do
  sha=$(gh api "repos/$REPO/git/ref/heads/$branch" --jq '.object.sha')
  tag="archive/$DATE/${branch//\//-}"
  saved=$(gh api "repos/$REPO/git/ref/tags/$tag" --jq '.object.sha')
  [[ "$sha" == "$saved" ]] || { echo "STOP: tag mismatch $branch"; exit 1; }
done

for branch in "${BRANCHES[@]}"; do
  gh api -X DELETE "repos/$REPO/git/refs/heads/$branch" --silent
  echo "Removed obsolete branch: $branch (archive tag retained)"
done

echo "SUCCESS: branch refs archived and deleted; main and docs/published-site-labels untouched."
