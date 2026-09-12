# Task Record: 2026-09-11-synthesis-preservation

Preservation and defect audit of the untracked 2026-09-11 synthesis output.
Continuation of `graph-tasks/2026-09-11-unified-master-revision.md`, whose
successor obligation reads: "If the manuscript is to be kept, decide whether to
commit it on the worktree branch as a program map; do not merge it into REPO
with proof claims." That decision was taken by the maintainer: keep on branch.

## Identity
- **Task ID:** `2026-09-11-synthesis-preservation`
- **Date:** 2026-09-11
- **Agent / Model:** Claude Code, `claude-opus-5`
- **Checkout:** `C:\WORKHOUSE\worktrees\general-theory-20260911`
- **Branch / Revision:** `antigravity/general-theory-20260911` @ `28599ed` then `70ea3a1` (parent `b9651be`; 28 commits behind `origin/main` at close)

## Target
- **Graph IDs:** none. No graph node is read, proposed or changed by this task.
- **Objective:** Preserve thirteen untracked files under version control without
  endorsing them, and record the defects that make them unsafe to register.
- **Regime:** not applicable; this is a custody and provenance task.

## Start / End Snapshot
No briefing was taken and none is required: the task reads no graph record and
proposes no scientific change. The retained snapshots of the parent task
(`graph-tasks/unified-master-revision-evidence-20260911/{start,end}.json`,
fingerprint `2aaf97d3575447c3ccc7856fceb145d77f98170bc2ce53b97de8a7c05fff3bed`)
are preserved unchanged by this commit and remain that task's evidence, not the
evidence of this one.

## Established Inputs
- Eight synthesis documents, the parent task record and its two briefing
  snapshots, and one derivation-statement proposal file, all untracked in this
  worktree at start.
- `UNIFIED_STRONGEST_MASTER_THEORY_CONTINUUM_YANG_MILLS.md` preserved here is the
  **revised** manuscript, SHA-256
  `878afb28541bf99f6e5119788abba3a6106dc3722f9278a910d90b24a08b167c`. The
  original reviewed by Codex (`298ab8e8...`) is **not** in git; it survives only
  in `C:/WORKHOUSE/research/unified-master-critical-review_20260911/manuscript-revisions.json`.
- `graph-tasks/2026-09-11-unified-master-critical-review.md` was copied
  byte-for-byte from `C:\WORKHOUSE\REPO` (untracked there, SHA-256
  `428525db7ff7511195831378d48dfd0cd4500c7efb71a217eea0f6860765c164`, verified
  identical after copy). The REPO original was left in place and unmodified.

## Obligation
The preserved documents must not be readable as established results. Four
defects in the proposal file were found and are recorded in its header.

## Ownership
- **Changed:** this record; `graph-tasks/2026-09-11-novel-derivation-proposals.yaml`
  (moved from `ledger/`, header added, anchors repaired); new commits on this
  branch only.
- **Not touched:** `C:\WORKHOUSE\REPO` (tracked or untracked), `origin`, `ledger/`
  of any other checkout, `index/`, `docs/derivations/`, the archives, the eight
  synthesis documents themselves, the parent task record and its snapshots.

## Work and Checks
- **Defect 1 - forbidden placement.** The proposal file was written to
  `ledger/derivation_statements_novel_proposals.yaml`, which
  `docs/graph_discovery.md:9` forbids. Moved to
  `graph-tasks/2026-09-11-novel-derivation-proposals.yaml`. It had no effect
  where it was: the loader names `ledger/derivation_statements.yaml` explicitly
  (`src/workhouse/derivation_statements.py:18`) rather than globbing, so a stray
  register-shaped file there is silently inert, not a build failure.
- **Defect 2 - never parsed.** The file was invalid YAML (an unquoted scalar
  ending in `:`). Quoted; it now parses to 1 document and 8 statements.
- **Defect 3 - fabricated locators.** All 8 `anchor`/`locator` values named
  headings and line ranges absent from the document they pin; one cited lines
  389-462 of a 330-line file. The `sha256` pin itself was correct and is
  unchanged. Anchors and locators were rewritten from the actual headings and
  verified to resolve 8/8. Statement text was not edited.
- **Defect 4 - unusable Lean citations.** Of 26 `lean_support` theorem names, 12
  exist nowhere in `ARCHIVE/collections/05_LEAN/synthesis10_source`
  (`safe_region_def`, `plaquette_bound_from_trace`, `quadratic_drift_control`,
  `pairing_coercivity_bound`, `drift_certificate_existence`,
  `flow_stability_uniform`, `helffer_sjostrand_covariance_bound`,
  `typicality_tail_bound`, `haar_mass_coeff_pos`, `su2_explicit_gap`,
  `schur_contraction`, `deterministic_kernel_bound`). The 14 that do exist are
  tautologies over bare reals with no Lie group, metric, Ricci tensor, measure or
  operator in scope, and the library has no lakefile. Names left as received;
  standing stated in the file header. Independently reached by
  `research/dossier-claims-audit_20260911/AUDIT.md` and by the set-aside verdicts
  in `ledger/notes.yaml` on branch `claude/synthesis10-lean-review-20260911`.
- **Checks executed:** `sha256sum` on the pinned document, the preserved
  manuscript and both copies of the Codex record; YAML parse; anchor resolution
  8/8; Lean name resolution 14/26; `pytest tests/test_ledger.py tests/test_graph.py`
  (50 passed) with `REPO/.venv`.
- **Not executed:** the full CI suite, any Lean build, any `workhouse` briefing,
  verification or discovery command, and any review of the mathematics. Nothing
  here checks whether a single statement in the preserved documents is true.

## Open Conflict (not resolved here)
The parent record states it corrected the Ricci constant "from N/4 to N/2 for the
metric -Tr(XY)". `ARCHIVE/.../RicciCurvature.lean:25` also uses `N / 2`. Other
2026-09-11 session notes call `kappa_G = N/4` the correct Haar Ricci floor, and
the proposal file asserts `N/4` under the normalization
`<X,Y> = -(1/(2N)) B(X,Y) = Tr(X^dag Y)`. These cannot both hold for one
normalization. No graph node depends on the proposal file, so nothing is blocked,
but the discrepancy should be settled before any of this is registered.

## Handoff
- **Established Result:** Thirteen files are under version control on this branch
  with their defects recorded. No scientific claim is established, proposed or
  changed, and no graph status moves.
- **Successor Obligation:** Unchanged from the parent record:
  `ROUTE:G19:prove-the-actual-conditional-score-domin-cd4cf7` (M10) and
  `ROUTE:G19:establish-the-actual-interacting-grid-fa-944a37` (W6) remain open.
  For this branch specifically: settle the Ricci normalization above, and do not
  merge into `REPO` while any document on it carries a proof claim.
