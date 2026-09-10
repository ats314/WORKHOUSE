# Documentation and agent workflow refresh — September 9, 2026

This is a navigation and workflow audit, not a new mathematical certificate.
Its baseline is the [PR #113 merge](https://github.com/ats314/WORKHOUSE/commit/742033a604484bf2caf00611bc0d4f0973fe12c4).

## Scope and preservation

- Updated the root README and task index, agent instructions, contribution
  guide, research routing, workspace/corpus guidance, Lean workflow, and
  affected literature and notes entry points.
- Reviewed the less visible entry points: subtree instructions, Make help,
  session-start fallback, issue forms and PR template.
- Preserved 51 original instruction/navigation files with exact-byte SHA-256
  records in the maintainer workspace at
  `navigation/preserved/2026-09-09-github-docs-refresh/`. This local navigation
  backup is separate from scientific evidence manifests. The baseline Git
  revision also retains the previous versioned guides.
- Retained earlier research narratives as explicitly dated history or linked
  their immutable Git revision. Received library indexes retain their original
  local-layout links and provenance; mutable parent guides explain that scope.
- Changed no derivation sources, Lean proofs, scientific ledgers, kernel
  exports, generated theory graph, frontier, certified view, or proof map.
  Verified all 20 source hashes in the derivation statement inventory. No
  files were deleted or relocated.

## Corrections that affect future work

The canonical maintainer checkout is `C:\WORKHOUSE\REPO`; another contributor
uses their own clone root. Current source status must be checked before an
agent restarts an older route. Mathematical status and machine coverage remain
separate, including the established SC17 source results and their unfinished
complete Lean realization.

The formalization guide describes whole-statement versus scoped proof links,
kernel-extracted dependencies, strict builds, source hashes and the generator
order. `make regen` covers the catalogue, frontier and certified view; the
Lean export, proof map and atlas have separate commands. Documentation-only
changes do not require regenerating scientific evidence.

Notes scanning writes inventories while preserving archive inputs. PDF
extraction requires the complete matching local reading-copy collection and
preservation of existing outputs; it is not ordinary fresh-clone setup.
Publication is complete only after the tested change reaches GitHub main and
the remote files are verified.

## Repeatable documentation checks

The [maintenance guide](../documentation_maintenance.md) and
[manifest](../documentation_manifest.json) define the maintained scope. The
read-only checker runs in the Python CI entry point and has focused tests for
links, filename case, anchors, path escape and Markdown masking, including
interactions between comments and code fences.

```text
uv run --no-sync python scripts/check_docs.py --json
uv run --no-sync pytest tests/test_docs.py
```

The allowlist contains 27 maintained documents. This is not a crawl of every
historical Markdown file. External URL reachability, complex renderer-specific
Markdown, and non-Markdown fragments remain outside the parser's scope; its
JSON output lists those limitations. A Windows host can skip the symlink
fixture when it lacks permission to create symlinks.

The local audit also validates all three issue forms, parses the static
fallback JSON, checks shell syntax and preservation digests, and checks that
the generated proof map still matches its unchanged source inputs. See this
change's PR and exact CI revision for the full regression and strict Lean
results; a prior run on the baseline is not a run on the new commit.
