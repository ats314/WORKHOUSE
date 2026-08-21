# s_chessboard — (S) chessboard/large-deviation route engine (F029, June 12, 2026)

Quantitative engine for `programs/op1_defect_sparsity/NOTE_FLUX_s_chessboard_route_2026-06-12.md`
(the (S)/M3a chessboard route note — operative 19:19 edition, the one with per-cell
dissemination; review: `records/review/findings/F029_s_chessboard_route_review.md`).

| File | md5 | Provenance |
|---|---|---|
| ENGINE_OP1_s_chessboard_rate.py | 1fb2b7dd875559406093aaa674ed5465 | Alex upload June 12 19:19 (parallel session), verbatim |
| CERT_OP1_s_chessboard_rate.json | 39a01c11239038366177d67385751b04 | Alex upload, verbatim (authoring-session output) |

Superseded same-day draft of the route note (19:12 edition, per-element dissemination —
author-corrected before deposit): md5 c6071dd7db162bd5a845cedc3bffe8c2, not deposited (rule 8).

**Gates (all hard asserts):** G-S1 Haar normalization, G-S2 Haar moments (E Re tr U,
E|tr U|²−1 at machine zero), G-S3 Tier-R single-plaquette inequality vs all 8 stored
ensembles (8/8), G-S4 exact animal counts a1..a4 = 1, 20, 458, 11132 vs the proved
bound e·(20e)^(n−1).

**Cold-run record (June 12, this session):** ALL GATES PASS in 0.48 s; output json
reproduces the stored one — every substantive value ≤ 1e-12 relative; the single diff
is `weyl/gate_EReTr` (a machine-noise diagnostic, true value 0): 6.5e-17 here vs
8.3e-17 stored (summation-order/BLAS difference; both pass the 1e-9 gate).

**Environment relics (F024/F027 species):** the engine reads ensembles from
`/mnt/project/results_L{n}_b{a}_{b}.json` (UNDERSCORE decimal) and writes
`/home/claude/CERT_OP1_s_chessboard_rate.json`. Our stores name them `CERT_OP1_results_l4_b5.6.json`
(DOT) under `../results/`. Cold-run recipe: copy the 8 results files to a stand-in
dir under underscore names, patch the two path constants on a scratch copy, run
`python3 s_chessboard_rate_run.py`. Dependencies: numpy.

**Resolution-stability check (this session, recorded in F029):** the Weyl tail
quantities integrate an indicator on an N×N midpoint grid (N = 1200); doubling and
tripling N moves r1(β, δ) by ≤ 4e-5 (e.g. r1(5.6, 1.1): 3.132412 → 3.132474) and
⟨φ⟩ by < 1e-8 — the Vandermonde weight vanishes quadratically at coincident angles,
so the indicator boundary is benign. Quoted 3-digit r1 values are safe.

**F034 (June 12, late night) — ENGINE_OP1_z_prime_mc.py: Ē₁ measured ≈ 1 (chessboard route NEGATIVE for the sparse channel).** New SU(3) L=4 Metropolis sampler measuring Ē₁ = E_{Z′}φ_p with one orientation class removed from the action (= the faithful chessboard product measure). Gates: G-Z1 (calibration — full-Wilson ⟨φ⟩ reproduces the deposited 0.446/0.309 within 0.012) PASS, G-Z2 (acceptance/unitarity) PASS, G-Z3 (result reported). **Result: Ē₁ = 1.0034±0.0018 @ β=5.6, 0.9606±0.0050 @ 7.2** — near-free-Haar, NOT the hoped ≲0.49 ⟹ single-class Tier-S buys nothing for sparse animals ⟹ chessboard route cannot reach the anchor. Redirect to the δ-window question. State: CERT_OP1_z_prime_mc.json (+ per-run .npy snapshots, regenerable). Finding: `records/review/findings/F034_ebar1_chessboard_negative.md`. md5 cfddd121.

**F035 (June 12) — ENGINE_OP1_op12_delta_window.py: the δ-window is one-sided on the (D) side.** Re-evaluates the deterministic firewall θ at the EXTENDED δ grid {1.10,1.20,1.30,1.40,1.45} by continuing the deposited thermalized MC states (`../op12_state/state_*.npz`) with the identical gated θ machinery (op12_runner's). Gates **G-DW1..G-DW6 PASS**: G-DW1 d₁d₀=0, G-DW2 P²=P, G-DW3 [M,P]=0, G-DW4 CG, **G-DW5 δ=1.10 reproduces the deposited June-11 scan** (anchor 0.202 vs 0.207, all 8 within MC band), **G-DW6 θ monotone non-increasing in δ**. **Result: θ_max falls monotonically as δ grows** — anchor 0.31→0.18→0.16 across δ=1.1→1.2→1.3 — so (D) imposes no upper θ-ceiling; δ∈[1.1,1.3] is safe AND tested (factor ≳6 below θ=1). Above δ≈1.35 defects of that depth don't occur on L≤6 (untested, not safe-by-margin). The real upper edge is comparator-validity (analytic, Alex), not a measured-θ failure. Adopting δ=1.3 cuts the (S) Tier-R clearance ln s 247→55 (4.5×), deterministically free. Files: ENGINE_OP1_op12_delta_window.py (md5 25614ea1), CERT_OP1_delta_window_summary.json (4d5502ba), DATA_OP1_delta_window.png (78b0cb3e), dw_state/ (8 jobs × 3 files, resumable). Finding: `records/review/findings/F035_delta_window_deterministic.md`. **(Partially retracted by F036 — see below; the in-model θ-fall stands, the "adopt δ=1.3" recommendation does not.)**

**F036 (June 12) — ENGINE_OP1_delta_max_curvature.py: the δ-window's UPPER edge δ_max ≤ 1 (comparator faithfulness).** Completes F035's flagged comparator-validity question. M = m₀²I + α_W d₁*d₁ is a **positive operator**, so it cannot lower-bound a plaquette whose per-plaquette link Hessian block H_ab = (1/6)Re tr({T_a,T_b}U_p) is net-negative. Computed exact: **tr H = (4/3)(1−s_p)** (sign change s_p=1), strict negative-eigendirection **onset s_p\* = 2/3** (at U_p=diag(1,i,−i)); gates **G-DM0 (Casimir ΣT_a²=(4/3)I), G-DM1 (trace law 4.4e-16), G-DM2 (finite-diff cross-check 4.0e-9), G-DM3 (s_p>1 ⟹ indefinite), G-DM4 (onset ≤1) ALL PASS**. ⟹ **hard, calibration-independent ceiling δ_max ≤ 1**; faithful range [2/3,1]. Tier-R needs δ>1 ⟹ **DISJOINT** from the faithful window (2nd structural obstruction to the route, complementing F034). Retracts F035's δ=1.3. Files: ENGINE_OP1_delta_max_curvature.py (canonical, host-correct, md5 b28c064c), RUN_OP1_dmax.py (fresh-path run copy, 4418005d — VM mount served a stale truncated view of the canonical file; gated run executed from the byte-equivalent copy, host verified by Read), CERT_OP1_delta_max_curvature.json (cb640f9e). Finding: `records/review/findings/F036_delta_max_comparator_faithfulness.md`.
