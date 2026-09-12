# Task Record: 2026-09-11-planar-grading

## Identity
- **Task ID:** `2026-09-11-planar-grading`
- **Date:** `2026-09-11`
- **Agent / Model:** Claude Code, Claude Opus 5 (`claude-opus-5`)
- **Checkout:** `C:\WORKHOUSE\REPO` (the canonical checkout, which was clean apart from an untracked `graph-tasks/2026-09-11-unified-master-critical-review.md` belonging to another agent; that file was not staged or modified)
- **Branch / Revision:** `claude/planar-grading-20260911`, branched from `294c224` (main, PR #159 merged)

## Target
- **Graph IDs:** `G16` (rank-uniform control in τ = β/N³), with `G14` and `G9` read for scope.
- **Objective:** the user asked for a new theory built on the theory graph's last two days of work. The two ADRs of 2026-09-11 — 0046 (even orders: the `N^-(4k-1)` law, conjectured beyond k = 2, mechanism unnamed, per-channel label rule refuted) and 0047 (odd orders: the centre-parity theorem, proved) — describe the same N-grading from two sides. Test the even-order law past k = 2 and find the mechanism.
- **Regime:** strong-coupling series of the one-plaquette sector, fixed even order, over the field ℚ(N) where only balanced Haar families exist. No statement about convergence, about cluster cumulants, or about the G16 overlap theorem.

## Start Snapshot
- **Not taken.** `workhouse brief --startup` was **not** run before the work, contrary to the working agreement; the target was selected by reading `FRONTIER.md`, the two ADRs and `ledger/gaps.yaml` directly. Recorded as a process deviation rather than reconstructed after the fact. The end snapshot below is genuine.

## Established Inputs
- ADR 0046 and `runs/planar_band_2026-09-11`: the `N^-(4k-1)` conjecture, verified at k = 1, 2 on the fourth-order cluster cumulants; the 1,772 channel forms; the refuted label rule (47 failures); the planar limits with denominator 576.
- ADR 0047, `RESULT:ODD_ORDER_CENTRE_PARITY` and `src/workhouse/invariants/odd_order.py`: the centre-parity theorem, the determinant-family window `N <= m + 2`, and the one-plaquette character engine (`towers`, `character_series`, `casimir`, `_w`, `_add_box`, `_add_column`) that made this run cheap.
- `src/workhouse/sixth_order_characters.py` (`bloch_series`) and the G9 suite `src/workhouse/invariants/sixth_order_cluster.py`: the rank-generic ℚ(N) engine this work is built on, and the one-face k = 3 result it had already established.

## Obligation
- **Investigated Statement:** the rank dependence of the one-plaquette C-parity splitting `S_m(N) = odd_m - even_m` at even orders m = 2..10, and the channel decomposition responsible for its suppression.
- **Downstream Consequence:** the one-face exponent law is carried to k = 4 and k = 5 (the G9 suite had k = 3), the `τ`-normalisation in which every even order carries one power of N is made exact, and the cancellation gets a named mechanism with a falsifier the existing ADR 0046 channel record can decide.

## Ownership
- **Owned Files:** new `src/workhouse/invariants/planar_grading.py`, `tests/test_planar_grading.py`, `runs/planar_grading_2026-09-11/*`, `docs/decisions/0048-*.md`, `paper/research_notes/PLANAR_GRADING_SINGLE_FACE_20260911.md`, this record; anchored edits to `src/workhouse/invariants/__init__.py` (one module name), `runs/index.yaml` (one entry), `ledger/gaps.yaml` (G16 detail, one appended paragraph), `ledger/documents.yaml` (one alias), `ledger/results.yaml` (one RESULT), `paper/SHA256SUMS` (one pin), `docs/current_research.md` (one appended section); regenerated `index/*.jsonl`, `FRONTIER.md`, `CERTIFIED.md`.
- **Shared Processes:** all Python ran with this checkout's `.venv`. No Lean, `theory/`, `corpus-import/` or `ledger/derivation_statements.yaml` change. `make` is unavailable on this workstation; the `regen` chain was run as its three underlying commands in the Makefile's order (`index -w`, `frontier --write`, `certified --write`).

## Work and Checks

- **A claim was made and retracted mid-task; the retraction is the first entry here.** The first
  version of this work used the integer-rank engine of ADR 0047 with Richardson extrapolation and
  claimed `k = 3` as new, that ADR 0046's named test had not been reached, and that `c_6 = -1748/3`
  was a recognition of a numerical limit. All three were wrong. The **G9 suite** ("G9 direct sixth
  order on one face and the shared-link pairs, any rank", `runs/g9_direct_h6_pair_2026-09-11`, PR
  #149) had already settled the one-face `k = 3` case exactly over ℚ(N), including the `N^-11`
  order-six splitting, and had bounded the seven word-formula pieces of (F6) at `O(N^-5)`. The error
  surfaced because the repository's own full test run printed that check's name. The work was
  rebuilt on the ℚ(N) engine (`sixth_order_characters.bloch_series`), which is both exact and
  faster; the retraction is recorded in ADR 0048, the note, the run README and the G16 detail.
- **Result 1 (new).** Orders **eight and ten** (`k = 4, 5`), exactly over ℚ(N): for the C-parity
  splitting of the one-plaquette diagonal `S_m = odd_m - even_m = -2 K_m[0][1]`,
  `S_m = c_m N^-(2m-1)(1 + O(N^-2))`. Nothing in the corpus had gone past order six on this object.
  `k = 5` confirms a prediction the retracted draft made before it could test it.
- **Result 2 (new).** `c_2 = -4`, `c_4 = -32`, `c_6 = -1748/3`, `c_8 = -123332/9`,
  `c_10 = -49593808/135`. Since `u = N^2 τ/2`, the order-m term is `(c_m/2^m) N τ^m`: every even
  order carries the same single power of N, so the single-face band per unit N is a function of τ
  alone, with `b_2 = -1`, `b_4 = -2`, `b_6 = -437/48`, `b_8 = -30833/576`, `b_10 = -3099613/8640`.
- **Result 3 (new, the mechanism).** An exact decomposition of `S_m` by the intermediate state —
  asserted equal to `S_m` over ℚ(N) — gives **exactly four** channels at every even m ≥ 4: the
  singlet `((), ())`, the adjoint `((1,), (1,))`, and the two-box states `((2,), ())` and
  `((1,1), ())`, **each of order `N^-(m-1)`**, with leading coefficients `(-4, +2, +1, +1) ×
  2^(m/2-2)` summing to zero. The cancellation is between channels of *equal* order, carried by
  their relative coefficients. That explains ADR 0046's negative: no per-channel label rule can
  reproduce it. It is a different decomposition from the word-formula pieces of (F6).
- **Run:** `runs/planar_grading_2026-09-11/derive.py`, about four minutes (the order-10 Bloch series
  is a minute of it).
- **Suite:** "the single-face planar grading law through tenth order (G16)" — **three T1** checks
  (the law and coefficients at m = 2..8, the τ-normalisation, and the channel decomposition, all
  re-derived live over ℚ(N)) and **one T2** (the independent integer-rank cross-check, a tolerance
  on an extrapolated value). About 33 s. Order 10 is pinned from the certificate.
- **Independent confirmation:** the ADR 0047 integer-rank engine, which shares no primitive with the
  rank-generic Bloch series, reproduces `c_2, c_4, c_6, c_8` by extrapolation to within 1.4e-5.
- **Tests:** `tests/test_planar_grading.py`, 5 tests. `ruff check` and `ruff format` clean.
- **Scope kept explicit everywhere:** the object is the one-plaquette diagonal, **not** the cluster
  cumulant `β_N`. ADR 0046's cluster conjecture is **not** discharged; the shared-link pair route
  carries the multi-face statement; the G16 overlap theorem is untouched. Each order is an exact
  computation at that order, so the general-m law remains a conjecture, verified at `k = 1..5` here.
- **Falsifier for the mechanism** (registered in the G16 detail, ADR 0048 and the note): regrouping
  ADR 0046's 1,772 fourth-order channel forms by intermediate-irrep content should make their orders
  uniform at `N^-3` and their leading coefficients sum to zero.
- **Order 12 computed but deliberately not certified.** The order-12 series finished (14 minutes)
  and gives the exponent `-23` with `c_12 = -21582705596/2025`, `b_12 = -5395676399/2073600` — the
  law at `k = 6`. It is recorded in the note, ADR 0048 and here as an observed value with its
  provenance, and is **not** in `certificate.json`, the suite or the `RESULT:`, because folding it in
  would mean rebuilding the run and rerunning the entire regeneration and verification chain on an
  already-green state. It should be certified the next time this run is touched.
- **Not done:** no `DERIV:` statement group in `ledger/derivation_statements.yaml`; no Lean.

## End Snapshot
- To be completed from `workhouse brief G16 G14 G9 --json --live` after the regeneration chain and full verification, and from the pull request's CI.
