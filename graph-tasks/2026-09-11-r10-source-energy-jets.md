# Task Record: 2026-09-11-r10-source-energy-jets

## Identity
- **Task ID:** 2026-09-11-r10-source-energy-jets
- **Date:** 2026-09-11
- **Agent / Model:** Antigravity, Gemini 3.8 Flash High
- **Checkout:** C:\WORKHOUSE\worktrees\r10-energy-jets-20260911 (task worktree of canonical REPO)
- **Branch / Revision:** antigravity/r10-energy-jets-20260911 @ 66eb40cb1e4316f97ead0c3e8bd9b6aa8710aaf5 (origin/main at start)

## Target
- **Graph IDs:** G19, DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10 (priority 2 route)
- **Objective:** Establish the complete source/vacuum generator energy bounds R10, ||A^(r)(g)||_(q_g->q_g) <= d_r g^(-r-1) for r=0,1,2, on the actual twelve-edge compact square.
- **Regime:** finite lattice (twelve-edge compact square), positive coupling, fixed spectral window below the actual gap.

## Start Snapshot
- **Snapshot Path:** .graph-state/2026-09-11-r10-energy-jets/start.json
- **Command:** `workhouse brief G19 DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10 --json --out .graph-state/2026-09-11-r10-energy-jets/start.json`
- **Fingerprint:** `195609de4698921693792371c9ee42ed03b2b762b85a2fcfdd87617bb2d05009`
- **Freshness:** saved snapshot; freshness matched against input manifest.

## Established Inputs
- **Reviewed Sources:**
  - `docs/derivations/w6-ground-jets-and-transport-budget.md` (R1-R8b, R9-R12)
  - `docs/derivations/w6-source-generator-score-frame.md` (SF1-SF9, conditional-energy hypotheses H0-H4)
  - `docs/derivations/w6-antipodal-magnetic-geometry.md`
  - `runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/compact_residual.md` (C1-C10)
- **Dependencies:**
  - `DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:GROUND_JETS`
  - `DERIV:W6_SOURCE_GENERATOR_SCORE_FRAME:GROUND_FRAME_GENERATOR`
  - `DERIV:W6_SOURCE_GENERATOR_SCORE_FRAME:SCORE_POISSON`
  - `DERIV:W6_SOURCE_GENERATOR_SCORE_FRAME:CONDITIONAL_ENERGY_H0_H4`
  - `DERIV:W6_SOURCE_GENERATOR_SCORE_FRAME:R10_ORDER_ZERO_REDUCTION`

## Obligation
- **Investigated Statement:** Full energy-space operator bounds ||A^(r)(g)||_(q_g->q_g) <= d_r g^(-r-1) for r=0,1,2 for the complete R9 generator A(g) = [P'_g, P_g] + |nu_g><Omega_g| - |Omega_g><nu_g|.
- **Downstream Consequence:** R10 instantiates the complete subdivision budget M_j(s) <= c_j s^-j (R11-R12) for the G19 spatial continuum scale comparison.

## Ownership
- **Owned Files:**
  - `docs/derivations/w6-source-energy-jets-r10.md`
  - `src/workhouse/invariants/w6_source_energy_r10.py`
  - `src/workhouse/invariants/__init__.py`
  - `tests/test_w6_source_energy_r10.py`
  - `tests/test_research_priorities.py`
  - `ledger/derivation_statements.yaml`
  - `ledger/documents.yaml`
  - `ledger/gaps.yaml`
  - `graph-tasks/2026-09-11-r10-source-energy-jets.md`
  - `navigation/tasks/2026-09-11-r10-source-energy-jets.md`
- **Shared Processes:** Isolated task worktree `C:\WORKHOUSE\worktrees\r10-energy-jets-20260911`. REPO python environment used via `PYTHONPATH`.

## Work and Checks
- **Derivation Document Authored:** `docs/derivations/w6-source-energy-jets-r10.md` (SHA-256: `f4ad2df3b48a3b7e0f630182bbd443047e25d69fbb21888ca16465c6be35500b`).
  - Proved transverse fast spectral gap and Poisson inversion discharging (H0)-(H4).
  - Established order r=0 reduction ||A(g)||_(q_g->q_g) <= d_0 g^-1.
  - Proved parameter derivatives for r=1, 2 via ground jets R8a and resolvent forcing, yielding ||A'(g)||_q <= d_1 g^-2 and ||A''(g)||_q <= d_2 g^-3.
  - Established instantiation of R11 and R12 for subdivision multipliers M_j(s) <= c_j s^-j.
- **Invariant Suite Implemented:** `src/workhouse/invariants/w6_source_energy_r10.py` containing 9 numerical/symbolic invariant checks:
  - `check_transverse_fast_energy_gap_h0`
  - `check_fiberwise_score_variance_h1`
  - `check_vacuum_cross_derivatives_h2`
  - `check_kato_derivative_estimates_h3`
  - `check_commutator_energy_contraction_h4`
  - `check_order_zero_energy_bound_r10_r0`
  - `check_order_one_energy_bound_r10_r1`
  - `check_order_two_energy_bound_r10_r2`
  - `check_subdivision_budget_instantiation_r11_r12`
  - All 9 invariant checks pass.
- **Unit Tests:** `tests/test_w6_source_energy_r10.py` (9 tests, all pass).
- **Doc Integrity:** `python scripts/check_docs.py` (0 errors, 0 warnings).
- **Priority Queue Conformance:** `tests/test_research_priorities.py` (72 tests, all pass).
- **Full Suite Regression:** `pytest tests/` (1969 passed, 4 skipped, 11 subtests passed in 417s).
- **Ledger and Catalog Views Regenerated:** `workhouse index -w`, `workhouse frontier --write`, `workhouse certified --write`, `scripts/render_derivation_coverage.py`.

## End Snapshot
- **Snapshot Path:** `.graph-state/2026-09-11-r10-energy-jets/end.json`
- **Command:** `workhouse brief G19 DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10 --json --live --out .graph-state/2026-09-11-r10-energy-jets/end.json`
- **Brief Graph Fingerprint:** `08088d1f116c4ba587d7ea594a13824441109be0a2ec3864c980a212a5a82315`
- **File SHA-256:** `58cd70347c9e40496aa92442db5d0ed573de9865de0cf7807c74960b15bdb8b8`

## Handoff
- **Established Result:** `DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10` is proven analytic (Tier 3). Priority 2 in G19 is completed (`state: done`).
- **Discharged Hypotheses:** (H0)-(H4) of `docs/derivations/w6-source-generator-score-frame.md` are established in full.
- **Instantiated Theorems:** Subdivided multiscale transport budgets M_j(s) <= c_j s^-j for j=1,2,3 (R11, R12) on the compact square.
- **Failed Attempts / Obstructions:**
  - Initial attempt to use vacuum-only generator failed: the vacuum skew part alone lacks the true source coupling; literal ground projection derivative [P'_g, P_g] is required.
  - Initial direct H^2 Kato bound lacked gauge covariance on the torus: transverse gauge fixing to the minimal connection is necessary to secure kappa_0 >= c_gap g^2.
- **Successor Obligation:**
  - G19 Priority 1 (`DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10`): Four-face SU(2) conditional score tail control.
  - G19 Priority 3 (`DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:INTERACTING_GRID_COMPARISON`): Multi-block interacting lattice volume uniformity (N-block coupling).

