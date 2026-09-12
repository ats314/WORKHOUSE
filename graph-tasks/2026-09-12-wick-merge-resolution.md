# Task Record: 2026-09-12-wick-merge-resolution

## Identity
- **Task ID:** `2026-09-12-wick-merge-resolution`
- **Date:** `2026-09-12`
- **Agent / Model:** Claude Code (remote session), configured `claude-opus-5`
- **Checkout:** `/home/user/WORKHOUSE` with a linked worktree at `/tmp/claude-0/wick157`
  (remote clone; the workstation checkout is `C:\WORKHOUSE\REPO`)
- **Branch / Revision:** merge commit `c3ccb59` on `claude/theory-graph-review-8bpt0t`,
  carrying `codex/local-class-wick-20260911` @ `6feae90` merged with `origin/main` @ `a9373a9`

## Target
- **Graph IDs:** none selected for mathematical work. This is a landing task for
  the local-class-Wick integration authored in PR #157.
- **Objective:** resolve that branch's conflicts against current `main` without
  discarding either side, re-establish its verification at the merged head, and
  land it. No claim, status, evidence level, tier or route state is changed by
  the resolution.
- **Regime:** unchanged from the authored work (formal rank-uniform expansion).

## Start Snapshot
- The start observation for this session is
  `.graph-state/2026-09-12-theory-graph-review/start.json`, fingerprint
  `36a8ece58ab40a49c9944f7a32bb06ba8e8c056c7de3ef1bfe4ea2be26e8efdf`,
  freshness `unknown` (no local index-generation record in a fresh clone),
  retained with `graph-tasks/2026-09-12-theory-graph-review.md`.

## Established Inputs
- **Reviewed Sources:** the conflicted hunks themselves; `.gitattributes` pins
  on both sides; `src/workhouse/invariants/local_class_wick.py` and its
  registration in `src/workhouse/invariants/__init__.py`; PR #157's own body.
- **Dependencies:** none created. The merge asserts no new relationship.

## Obligation
- **Investigated Statement:** none. Landing work.
- **Downstream Consequence:** the five local-class-Wick T1 checks and their
  source-located records reach `main` instead of sitting in a conflicted branch.

## Ownership
- **Owned Files:** the merge resolution only — `.gitattributes` (hand-resolved
  as a union of both sides) and the four generated files `CERTIFIED.md`,
  `FRONTIER.md`, `docs/derivation_formalization.md`, `index/claims.jsonl`
  (regenerated, with `index/graph.jsonl` and `index/symbols.jsonl`), plus this
  record. No authored scientific content was edited.
- **Shared Processes:** PR #157 is Codex's. Its branch is **not** pushed to and
  its history is not rewritten; the resolution is carried on this branch and
  #157 should be closed as superseded once this lands.

## Work and Checks
- **Commands Executed** (all in the worktree, with `PYTHONPATH` pinned to that
  checkout's `src`):
  - `git merge --no-commit --no-ff origin/main`
  - `scripts/render_derivation_coverage.py`, then `workhouse index -w`,
    `workhouse frontier -w`, `workhouse certified --write` — the prescribed order
  - `workhouse verify`, `pytest -q`, `ruff check .`, `ruff format --check .`,
    `scripts/check_docs.py`, `workhouse status`
- **Outcomes:**
  - `workhouse verify` — **682/682** checks passed: `main`'s 677 plus this
    branch's five, which the regenerated frontier now carries as the suite row
    `local class Wick spectrum over all ranks | 5/5`.
  - `pytest -q` — exit 0 over 2126 collected tests, no failures.
  - `ruff check` clean; `ruff format --check` 638 files already formatted.
  - `check_docs.py` — 42 maintained files, 601 local links, 0 errors, 0 warnings.
  - `workhouse status` — *Ledgers structurally sound*; no open contradiction.
  - `workhouse index -w` wrote claims 19818, symbols 28, graph 32448.
- **Failure observed and corrected, worth recording:** the first regeneration
  pass used the repository's editable install, which resolved `workhouse` to the
  *other* checkout's `src` rather than the worktree's. It produced views reading
  `677/677` with no Wick suite row — generated files that would have read as
  current while describing a different tree. Those outputs were discarded and
  every regeneration and verification step was re-run with `PYTHONPATH` pinned
  to the worktree. Anyone regenerating scientific views from a linked worktree
  needs that pin, or the editable install silently wins.
- **Evidence Paths:** `.graph-state/2026-09-12-wick-merge/end.json` (local only;
  `.graph-state/` is gitignored).

## End Snapshot
- **Snapshot Path:** `.graph-state/2026-09-12-wick-merge/end.json`
- **Command:** `workhouse brief G19 --json --out .graph-state/2026-09-12-wick-merge/end.json`
- **Fingerprint:** `10ca4a83067527493a5347f119e8f2af801bb479c5b5d2b14e4997aa88036a19`
- **Freshness:** `matched` — *input and saved graph bytes match a successful
  index-generation record*, with 682 recorded checks. The start snapshot's
  `unknown` was the absence of a local generation record in a fresh clone, not a
  drifted view; the rebuild above supplies one for this tree.

## Handoff
- **Established Result:** none newly proved here. The authored analytic content
  keeps its recorded scope: the arbitrary-order construction remains a formal
  theorem, and no G19 route or Lean coverage is promoted by this merge.
- **Failed Attempts / Obstructions:** the contaminated-import regeneration
  above, retained rather than quietly repeated. Pushing the resolution to
  `codex/local-class-wick-20260911` was refused by this session's own
  permission layer, which is why the merge is carried on this branch.
- **Successor Obligation:** close PR #157 as superseded after this lands. The
  open mathematical obligations are unchanged and recorded in
  `graph-tasks/2026-09-12-theory-graph-review.md`: the M10 tube moments first.
