# M2 Results — Exact Pair-Level Certificates (June 12, 2026)

Milestone M2 of `01_PROOFS/synthesis/PLAN_OP1_unif_closure.md`, executed June 12, 2026. Everything here is exact finite linear algebra plus Monte-Carlo sampling; no claims beyond the printed numbers.

## What was built

`ENGINE_OP1_m2_pair_certificates.py` — by translation invariance, G_P((s,μ),(s',μ')) = T[μ][link((s'−s) mod L, μ')], so **4 projected solves per (L, β) determine the entire kernel**. Per-configuration certificates are then exact lookups:

    cert(D) = v₀ √( Σ_{b,b'∈D} G_P(b,b')² ) ≥ ‖K‖_HS ≥ ‖K‖_op = θ   (equality in HS step: this IS tr K²)

**Hard gates, all passing:** GATE-TR (lookup vs direct solve at random source links: max err ≤ 3×10⁻¹⁷); GATE-NSTAR (T_full reproduced against `CERT_OP1_kernel_consts.json`, independent computation, rtol 10⁻⁶); GATE-VALID (cert ≥ measured θ on every one of the 90 config/δ cases processed).

## Certification results

**Stored final states** (8 states × available δ, `m2_certs_L{4,6}.json`): pair-level certification extends beyond the count-only threshold N\* — e.g. L=4 β=6.0 δ=0.9: |D|=49 > N\*=30 yet cert = 0.81 **certified**; L=4 β=7.2 δ=0.7: |D|=74 > N\*=36, cert = 0.87 **certified**. Reason: real defect sets are spatially spread, and the kernel falls ~30× by site-distance² = 3 (shell table in `CERT_OP1_m2_l8_shells.json`).

**Fresh ensembles** (chain continuation from stored states; defect sets STORED per config in `m2_ensemble/`, removing the old final-state-only limitation):

| L | δ | pair-certified | count-only (N\*) | notes |
|---|-----|------|------|------|
| 4 | 1.1 | **50/50 (100%)** | 41/50 (82%) | gate target ≥80%: **met** |
| 4 | 0.9 | 34/50 (68%) | 25/50 (50%) | certifies all β ≥ 6.4 (30/30) |
| 6 | 1.1 | 12/18 (67%) | 12/18 (67%) | β=5.6 fails (|D| ≤ 136 vs N\*=42) |
| 6 | 0.9 | 6/18 (33%) | 6/18 (33%) | β=7.2 fully certified (6/6) |

Combined δ=1.1: **62/68 = 91% certified** (dossier gate ≥80%: met).

## L = 8 kernel constants (third volume point, `CERT_OP1_m2_l8_shells.json`)

| β | g_diag | T_full | c = √T_full | N\* |
|-----|--------|---------|-------|----|
| 5.6 | 0.11061 | 0.022062 | 0.149 | 45 |
| 6.4 | 0.09802 | 0.017738 | 0.133 | 56 |
| 7.2 | 0.08802 | 0.014633 | 0.121 | 68 |

T_full decreases monotonically in both β and L across L = 4, 6, 8 — the favorable trend now has three volume points.

## The structural lesson (honest limits of the HS route)

At fixed (β, δ), |D| grows ∝ L⁴ while N\* grows slowly — so **HS-based certificates cannot survive L → ∞ at fixed parameters**; the L=6 β=5.6 failures (cert ≈ 1.35 at θ ≈ 0.19) are this, not a deficiency of the engine. Certification at growing volume requires the defect *density* to fall (δ or β growing with the trajectory) — i.e. exactly the scaling form of sparsity that the open lemma (S) must deliver, consistent with how OP-1 frames the problem. Separately, the cert/θ ratio (~3–7) is the interference slack: dense-but-harmless regimes (θ ≈ 0.2 at |D| = 140) are beyond *any* HS argument and would need op-norm structure if ever required — but (S) targeting the sparse regime makes that unnecessary.

## Reproduction

    python3 ENGINE_OP1_m2_pair_certificates.py L β...    # tensors + stored-state certs (gates hard-fail)
    python3 ENGINE_OP1_m2_l8_shells.py all β...      # L=8 constants + W(r) shell tables
    python3 ENGINE_OP1_m2_ensemble.py T L n β...         # fresh certified ensemble, T-second chunk

Requires `ENGINE_OP1_op12_runner.py` and the `op12_state/` files one directory up; tensors cached in `m2_kernel/` (deposited — certificates reproducible without any solve). Same comparator conventions as the OP-12 scan (m₀² = 0.5, v₀ = 1, α_W = β/6); chain-continuation ensembles inherit the scan's thermalization caveat.
