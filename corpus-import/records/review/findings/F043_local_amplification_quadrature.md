# F043 — The operative tilt amplification is a finite, cutoff-stable LOCAL constant (consistent with TOS+J's exp(Σ J)); the load-bearing far-source decay is beyond the single-link diagnostic (June 13, 2026)

**Unit:** #64 (own-initiative continuation of F042, Alex "take it on"). **Verdict:** built and validated a deterministic S³ cap-intersection vMF quadrature, then used it (plus the exact cap solver) to resolve F042's MC-unresolved residual against the reduction's *actual* target. The reduction's bound is **(TOS+J)** `E_{μ^{S,s}}X_p ≤ C·q·exp(Σ_r J(p,r))`, `J(p,r) ≤ C_J e^{-m_J d(p,r)}` — so the amplification is *expected* to be a bounded factor `exp(Σ_incident J)`, and the load-bearing content is the **exponential decay of `J` with lattice distance** (far sources). Findings: (1) the full-conditioning (s→∞) limit on all 5 incident caps carries **negligible measure** (`ν(C_B)` below the resolvable floor; on S³ at most ~2 incident caps reliably co-occur), so it is not the operative object; (2) the **operative worst case — amplification conditioning on the maximal reliably-occurring incident subset (|A|≤2) — is median 1.0, with a thin tail to ~140–190, and is CUTOFF-STABLE** (L=4→8: max 187→140, log≤5.2 ⟹ per-incident-pair `J = O(1)`). This is a finite, cutoff-independent constant fully consistent with (TOS+J)'s local `J`-factor; it does **not** free `X_p`. (3) **What the single-link cap geometry cannot test — and the genuine Z.B content — is the exponential decay of `J(p,r)` over distance.** That delimits the entire cap-geometry diagnostic family (F037–F043).

## 1. The validated tool: deterministic S³ cap-intersection quadrature

`ENGINE_OP1_za_feasible_f043.py` / `ENGINE_OP1_za_lfull_f043b.py` build `ν(∩ caps)` under vMF(m,κ) on S³ exactly, via the m-frame factorization `u = w·m + √(1−w²)·ω`, `w ~ e^{κw}(1−w²)^{1/2}` on [−1,1], `ω` uniform on S² (Fibonacci grid): a cap `u·n_r ≤ a` becomes `c_r w + √(1−w²)(ω·ñ_r) ≤ a`. Gates: **G-Q1** single-cap quadrature vs the independent 1-D `nu_cap_quad` (≤ 4.7×10⁻³ at M=8000); **G-Q3** grid-refinement convergence (≤ 3.5×10⁻³, M and Nw doubled); **G-Q2** (in `_f043b`) `Lfull` quad vs MC on well-sampled records (Δlog = 0.000); **G-DT1** 0. Reusable for any cap-geometry probability on S³.

## 2. The s→∞ limit is not the operative object

The s→∞ tilt concentrates on `C_B = ∩(all 5 incident caps)`. The exact solver + quadrature show `ν(C_B)` is **below the resolvable floor** (`< 10⁻³`) for every record: on S³ (a 3-manifold) at most ~3 cap *boundaries* can be simultaneously active, and with reliable measure the **maximum feasible incident subset size is 2** (G-FS1, L=4 and L=8). So conditioning on all incident caps is conditioning on a negligible-measure event; the admissible tilt `s ≤ ρ/q` never gives it appreciable weight. (An earlier `_f043b` pass mis-reported a large "Lfull~26" — that was a quadrature 0/0 artifact on the empty/negligible `C_B`, and a `cmax` rank-deficiency for ≥4 active constraints; both are noted as edge-cases and superseded by the feasible-subset treatment here.)

## 3. The operative worst case: feasible-subset amplification (deterministic)

For each record with resolvable `ν(C_p) ≥ 10⁻³`, the worst amplification over reliably-occurring incident subsets, `max_{feasible A, ν(C_A)≥10⁻³} ν(C_p|C_A)/ν(C_p)`:

| L | resolvable records | max feasible \|A\| | worst-amp median / q90 / q99 / max | log(worst amp)=Σ_incident J max |
|---|---|---|---|---|
| 4 | 81 | 2 | 1.00 / 34.1 / 187.5 / 187.5 | 5.23 |
| 8 | 78 | 2 | 1.00 / 26.1 / 140.6 / 140.6 | 4.95 |

**Reading:** most records have worst-amp **exactly 1** (no feasible incident overlap raises the target cap probability); a thin tail reaches ~10² when one incident cap pair strongly overlaps `C_p`. The magnitude is **cutoff-stable** (187 → 140 from L=4→8, not growing) — a finite O(1)-in-cutoff constant. Per (TOS+J) the allowed local factor is `exp(Σ_{incident} J(p,r))`; the measured `log(worst amp) ≤ 5.2` over ≤2 incident caps gives per-incident-pair `J = O(1)` — consistent. The bound `E X_p ≤ C·q·exp(Σ J)` therefore stays **proportional to `q`** with a finite constant: `X_p` does not go free.

This reconciles cleanly with F041/F042: F041's finite-`s` amplification (median ≈ 1, q90 ≈ 1+s) and this worst feasible-subset amplification (median 1, tail ~10²) are the same phenomenon — the bulk is unaffected, a thin tail is the strong single-pair-overlap records.

## 4. What remains open (the genuine Z.B content)

The single-link cap geometry probes only the **local** factor — sources `r` incident to the link `e`, all at lattice distance `O(1)` from `p`. The load-bearing claim in (TOS+J) is the **exponential decay** `J(p,r) ≤ C_J e^{-m_J d(p,r)}` over distance, which controls the **rooted sum over far sources** (= Z.B / Bałaban far-source stability). That requires a multi-plaquette spatial setup (sources at varying lattice distance) and is **beyond what any single-link cap-geometry diagnostic (F037–F043) can establish.** This is the precise hand-off to Alex's analytic far-source program: the local `J`-constant is finite and cutoff-stable (this pass); the decay-in-distance is the open input.

## 5. Scope / grounds (honest)

- **Grounds:** validated deterministic quadrature (G-Q1/Q2/Q3) + exact cap solver (G-DT1, G-FS1). The worst-amp **median (=1)** and the **max-feasible-|A|=2** facts are robust; the worst-amp **tail (~10²)** rests on ≈4 records per L (the |A|=2 stratum) and on the `ν(C_A) ≥ 10⁻³` reliability floor — it is the least-pinned number and should be read as "a finite cutoff-stable O(10²) constant," not to three digits.
- **Edge-cases surfaced (rule 6):** `cmax` is rank-deficient for ≥4 active constraints (irrelevant once we use feasibility + the |A|≤2 fact); quadrature ratios are unreliable when `ν(C_A)` is below the floor (handled by the floor); the first `_f043b` "Lfull~26" line is a 0/0 artifact, superseded here.
- **Setting:** SU(2) one-link heat-bath, β=3.5, κ≈18, a≈−0.0054 (F039–F042 geometry). Single-link conditional, not SU(3), not the assembled far-source rooted sum.
- No proved status changes. F037/F038/F040/F041/F042 stand; (D) closed.

## 6. Deposits

`za_cap_geometry/`: `ENGINE_OP1_za_feasible_f043.py` (md5 4e610158) + `ENGINE_OP1_za_lfull_f043b.py` (f8fdbac3, superseded-but-retained) + `feasible_L{4,8}.json` + `DATA_OP1_feasible_amp.png`. Updated: STATE.md, ZA_CAP_GEOMETRY note §10, REVIEW_LEDGER #64, SESSION_LOG. Ledger count → 45/57 closed (42 DONE + 3 SKIP), F001–F043.
