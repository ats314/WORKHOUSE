# Task Record: 2026-09-11-m10-conditional-score

## Identity
- **Task ID:** `2026-09-11-m10-conditional-score`
- **Date:** `2026-09-11`
- **Agent / Model:** Antigravity / Gemini 3.8 Flash (High)
- **Checkout:** `C:\WORKHOUSE\worktrees\m10-score-domination-20260911`
- **Branch / Revision:** `antigravity/m10-score-domination-20260911 @ 7cf8a646521259a34a772d65c8740ef7597f0265`

## Target
- **Graph IDs:** `G19`, `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10`, `ROUTE:G19:prove-the-actual-conditional-score-domin-cd4cf7`
- **Objective:** Establish and verify the exact mathematical bounds for the conditional-score domination $K_g(w) \le C_0 + C_1 g^{-2} \mathbb{E}_{\mu_g}(V \mid w)$ under the synchronized $S_{13}$ radial transport, evaluating the tube variance, the complement outside deviation, and the antipodal degeneration.
- **Regime:** Discrete four-face compact $SU(2)^4$ Wilson block, finite-dimensional spectral and Agmon geometry, small coupling $0 < g < g_*$, rare coarse fibers $w \to \pm 1$.

## Start Snapshot
- **Snapshot Path:** `.graph-state/2026-09-11-m10-domination/start.json`
- **Command:** `workhouse brief DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10 --json --out .graph-state/2026-09-11-m10-domination/start.json`
- **Fingerprint:** `44175e0fe8150e4520deaa4914000811b0c6756d5e7436f9595fcf7dcd39429e`
- **Freshness:** `unknown` (isolated worktree without prior local index cache)

## Established Inputs
- **Reviewed Sources:**
  - `docs/derivations/w6-conditional-score-tail-control.md`
  - `docs/derivations/w6-conditional-transport-obstruction.md`
  - `docs/derivations/w6-antipodal-magnetic-geometry.md`
  - `scripts/check_m10_transport.py`
  - `scripts/check_w6_antipodal.py`
- **Dependencies:**
  - `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:ACTUAL_SOURCE_MOMENT`
  - `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:INTERVAL_OBSTRUCTION_REPAIR`
  - `RESULT:W6_CONDITIONAL_SCORE_CONTINUITY`
  - `RESULT:W6_SYNCHRONIZED_CONDITIONAL_DILATION`
  - `RESULT:W6_SYNCHRONIZED_SCORE_CRITERION`
  - `RESULT:W6_ANTIPODAL_HESSIAN_SPECTRUM`
  - `RESULT:W6_ANTIPODAL_GAUGE_NORMAL_COERCIVITY`
  - `RESULT:W6_ANTIPODAL_ANGULAR_REDUCTION`
  - `RESULT:W6_ANTIPODAL_GAUGE_SCORE_INVARIANCE`

## Obligation
- **Investigated Statement:** The sufficiency and uniform bounds of the synchronized $S_{13}$ transport field for conditional score domination M10, explicitly evaluating:
  1. Exact cancellation of the linear phase drift along the conditional minimizer curve $m(q)$.
  2. Bounding the tube variance $\mathbb{E}_{\text{tube}} |\sigma_g - \beta_g|^2$ by $C_0 + C_1 g^{-2} \mathbb{E}(V \mid Q)$.
  3. The behavior of the differentiated amplitude $a_g$ and the outside deviation.
  4. The antipodal degeneration $\theta \to \pi$ where the minimizer forms a gauge orbit 2-sphere $\mathcal{M}$.
- **Downstream Consequence:** Establishing M10 makes the uniform source moment bound M11-M15 applicable to the synchronized transport, controlling the W6 Wilson block transfer margin without requiring separate exponential marginal matching.

## Ownership
- **Owned Files:**
  - `worktrees/m10-score-domination-20260911/**`
  - `navigation/tasks/2026-09-11-m10-conditional-score.md`
- **Shared Processes:**
  Isolated from `C:/WORKHOUSE/REPO` to ensure zero collision with the agent landing Option 1.

## Work and Checks

### Created Files
| File | Purpose |
|------|---------|
| `scripts/verify_m10_tube_variance.py` | Exact symbolic verification: tangency cancellation, Euler cancellation, quadratic potential floor |
| `scripts/check_antipodal_score_bound.py` | Numerical+symbolic verification: antipodal Hessian spectrum, potential floor, gauge score invariance |
| `src/workhouse/invariants/w6_synchronized_m10.py` | 5-check T1 invariant suite for `workhouse verify` catalogue |
| `tests/test_m10_synchronized_score.py` | 7-test pytest suite covering all algebraic controls |
| `docs/derivations/w6-synchronized-m10-domination.md` | Full derivation document (4 sections + open hypotheses) |

### Modified Files
| File | Change |
|------|--------|
| `src/workhouse/invariants/__init__.py` | Added `"w6_synchronized_m10"` to `_MODULES` |
| `ledger/documents.yaml` | Added `W6_SYNCHRONIZED_M10_DOMINATION` document alias |
| `ledger/derivation_statements.yaml` | Added 3 derivation statements under `CITE:W6_SYNCHRONIZED_M10_DOMINATION` |
| `CERTIFIED.md` | Regenerated (532 → 537 checks) |
| `FRONTIER.md` | Regenerated (592/592 → 597/597 checks) |
| `index/claims.jsonl`, `index/symbols.jsonl`, `index/graph.jsonl` | Regenerated |

### Test Results
- `pytest tests/test_m10_synchronized_score.py` — **7/7 PASS**
- `pytest tests/test_graph.py` — **31/31 PASS**
- `pytest` (full suite) — **ALL PASS** (4 skips, 0 failures)

### Mathematical Status
| Step | Status | Evidence |
|------|--------|----------|
| S13 tangency drift cancellation | **Proven (T1)** | Exact algebraic zero `[0,0,0]` |
| Euler cancellation at q=0 | **Proven (T1)** | `F=0, Hess(F)=0` |
| Quadratic potential floor v_*(θ) ≥ 2θ²/π² | **Proven (T1)** | Symbolic bound on [0,π] |
| Antipodal Hessian spectrum (7 normals ≥ 4(√2−1)) | **Proven (T1)** | Exact eigenvalue computation |
| Gauge score invariance on T_M | **Proven (T1)** | Antipodal sphere check |
| Differentiated amplitude |∇_η a_g| ≤ c_a/g | **Conditional (T3)** | Requires Helffer–Sjöstrand input |
| Outside complement deviation bound | **Conditional (T3)** | Same dependency |

**M10 (`DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10`) remains open.**
The 5 proven algebraic controls are necessary ingredients; the full bound requires
the two conditional hypotheses above.

## End Snapshot
- **Snapshot Path:** `.graph-state/2026-09-11-m10-domination/end.json`
- **Command:** `workhouse brief DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10 --json --live --out .graph-state/2026-09-11-m10-domination/end.json`
