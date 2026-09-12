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
- `graph-tasks/2026-09-11-unified-master-critical-review.md` was copied from
  `C:\WORKHOUSE\REPO` (untracked there, SHA-256
  `428525db7ff7511195831378d48dfd0cd4500c7efb71a217eea0f6860765c164`). The source
  carries CRLF, so the first commit of it (`aed3716`) stored a normalized blob
  hashing to `42cd82b8de51fca1777196b5a3bfb6875d228702703decd37b692b82c62db5f5`
  instead - the exact failure the `-text` section of `.gitattributes` was written
  to prevent. A `-text` rule was added for this path and the file re-added; the
  stored blob now hashes to `428525db...`, verified with
  `git cat-file -p :<path> | sha256sum`. The REPO original was left in place and
  unmodified.
- The retained snapshots `unified-master-revision-evidence-20260911/{start,end}.json`
  were checked the same way: both are LF, both blobs hash to
  `ef2f61ac31e623100ca1c20f5d360da9ff91aa23967550a30f525f20ef1aa503`, matching the
  pin in the parent record, so nothing was rewritten. They are byte-identical to
  each other, consistent with that record reporting an unchanged fingerprint. A
  protective `-text` rule was added for them as well.

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
- **Defect 5 - a pin recorded against the wrong bytes (this task's own).** The
  first commit of the Codex record normalized its CRLF, so the sha256 written
  into this record described the working file and not the stored blob. Corrected
  as described under Established Inputs. The lesson generalizes: verify a pin
  with `git cat-file -p :<path> | sha256sum`, not `sha256sum <path>`, or the
  digest passes in the tree it was written in and fails in a fresh clone.
- **Checks executed:** `sha256sum` on the pinned document, the preserved
  manuscript and both copies of the Codex record; `git cat-file` blob-hash
  verification on the Codex record and both snapshots; YAML parse; anchor
  resolution 8/8; Lean name resolution 14/26;
  `pytest tests/test_ledger.py tests/test_graph.py` (50 passed) with `REPO/.venv`.
- **Not executed:** the full CI suite, any Lean build, any `workhouse` briefing,
  verification or discovery command, and any review of the mathematics. Nothing
  here checks whether a single statement in the preserved documents is true.

## Resolved Conflict: the Haar Ricci constant
Both `N/2` and `N/4` are correct, for different metrics. The defect is that the
proposal file pairs the value `N/4` with the normalization that yields `N/2`.

For a bi-invariant metric on a compact group, `Ric = -(1/4) B` as bilinear forms,
independently of which bi-invariant metric is chosen; the metric enters only when
`Ric` is written as `kappa * g`. On `su(N)` in the fundamental,
`B(X,Y) = 2N tr(XY)`. Therefore:

| metric `g(X,Y)` | relation to `B` | `kappa` with `Ric = kappa g` |
| --- | --- | --- |
| `Tr(X^dag Y) = -tr(XY)` | `g = -(1/(2N)) B` | `N/2` |
| `2 Tr(X^dag Y) = -2 tr(XY)` | `g = -(1/N) B` | `N/4` |

The second row is the common gauge-theory convention in which generators
normalized by `tr(T^a T^b) = delta^{ab}/2` are orthonormal, which is why `N/4`
circulates in the sources.

The proposal file states its normalization explicitly as
`<X,Y> = -(1/(2N)) B(X,Y) = Tr(X^dag Y)` (row 1) and then asserts
`kappa_G = N/4` (row 2), at
`graph-tasks/2026-09-11-novel-derivation-proposals.yaml` lines 59-60, 72, 139 and
154. Under its own stated metric the value is `N/2`. The parent record's
correction was therefore right, and `RicciCurvature.lean:25` (`N / 2`) agrees by
coincidence only: that file states no metric at all, so it is not evidence either
way, and its surrounding comment writes both `-(1/4) Tr(ad_X^2)` and `(1/4)
B(X,X)` for the same quantity, which differ in sign.

**Check:** `graph-tasks/synthesis-preservation-evidence-20260911/ricci_normalization_check.py`
builds `su(N)` for `N = 2..6`, Gram-Schmidts an orthonormal basis for
`Tr(X^dag Y)`, and computes `B(X,X) = tr(ad_X^2)` and
`Ric(X,X) = (1/4) sum_a |[X,e_a]|^2` independently. Output retained at
`ricci_normalization_check.out`: `B(X,X)/tr(XX) = 2N` exactly, `Ric = -(1/4)B`
holds to `1e-8`, and `kappa = N/2` for every `N` tested. Independent cross-check
at `N = 2`: `Tr(X^dag Y)` makes `SU(2)` the round 3-sphere of radius `sqrt(2)`,
where `Ric = (2/r^2) g = g`, and `N/2 = 1`.

**Consequence and its limit.** `kappa_G` is convention-dependent, so a floor
stated as `rho_* >= kappa_G` carries no information until the metric, and with it
the Laplacian normalization, is fixed; the gap rescales with the same factor, so
no physical statement changes. This settles a normalization, nothing more. It
does not make the curvature argument of
`DERIV:HAAR_RICCI_BAKRY_EMERY_MASS_FLOOR` a proof of a volume-uniform gap: the
reduction from the lattice manifold to the group factor is the open part, and it
is untouched here.

## Handoff
- **Established Result:** Thirteen files are under version control on this branch
  with their defects recorded. No scientific claim is established, proposed or
  changed, and no graph status moves.
- **Successor Obligation:** Unchanged from the parent record:
  `ROUTE:G19:prove-the-actual-conditional-score-domin-cd4cf7` (M10) and
  `ROUTE:G19:establish-the-actual-interacting-grid-fa-944a37` (W6) remain open.
  For this branch specifically: settle the Ricci normalization above, and do not
  merge into `REPO` while any document on it carries a proof claim.
