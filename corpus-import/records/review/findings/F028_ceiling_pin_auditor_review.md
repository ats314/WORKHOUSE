# F028 — Review of `NB_OP1_m5_tier_2_ceiling_pin_auditor.ipynb` (uploaded June 12, late)

**Unit:** #49. **Verdict: reduction algebra EXACT and adopted; data reproduction exact; the theorem's universal quantifier is over-broad (fails at x ≈ 9819, measured here) — repaired two ways, both deposited; the recommended analytic target is sharpened to a single inequality with uniform ×2.10 headroom.**
**Secured verbatim** → `numerics/op12_theta/m4_scaling/NB_OP1_m5_tier_2_ceiling_pin_auditor.ipynb` (md5 `7740d39b…`). Verification engine: `ENGINE_OP1_m4_ceiling_pin_audit.py` → `.json` (gates P1–P5, all pass). Naming note: despite the "M5" in the filename this is **M4 hardening** (the closure plan's M5 is the Lean milestone) — filed accordingly.

## 1. What it is

Single self-contained cell (stored outputs present; authoring-session artifact, same lineage as the F027 trio). It reduces the Tier-2 ceiling pins to one scalar inequality: with Y_L = α_W²T_C and A = 3/32π², if **Y_L ≤ A·ln s + B with B ≤ BCRIT = 57/1210** on the diagonal, then T̄ ≤ 1/8 ⇒ **T_C ≤ 1/8, N\*_C ≥ 8, T_full < 9/64, N\* ≥ 7** — turning the remaining work into "a scalar heat-kernel/theta-tail upper bound, not another lattice solve."

## 2. Verified [all machine-checked]

1. **Threshold algebra exact.** T̄(B) = 9(A/γ)/(β₀ − γB/A) = (27/44)/(28/5 − (44/3)B); T̄ = 1/8 at B = 57/1210 — confirmed **in rational arithmetic** (gate P1; uses A/γ = 3/44 exactly). The reduction logic (pointwise majorant ⇒ sup bound, T_H = 1/64 exact) is sound; floors follow.
2. **Cold run reproduces the stored outputs exactly** (whitespace-only diff). Its 17-row diagonal (which includes s = 10, 20 — new spot-checks) matches the F027-verified closed form; its B-summary (max B_L = 0.018355 at s = 64, min margin 0.02875) is correct for the computed range.
3. **Its ceiling values reconcile with F027**: T̄(0.018355) = 0.11511 = the trio's pinned-A variant; the safe-B ladder is arithmetically right.

## 3. The flaw, measured precisely [new computation, gates P2–P3]

Under the ∞-volume law (exact for s ≳ 100), **D(x) := Y − A·x − (A/2)ln α(x) is constant to machine precision: D∞ = 0.021301939, spread 3.8e-14 over x ∈ [40, 2×10⁴]**. Hence B(x) = D∞ + (A/2)ln α(x) grows without bound (doubly-logarithmically in s) and **crosses BCRIT between x = 9818 and 9820**. The notebook's hypothesis "for every integer L ≥ 4" is therefore **asymptotically false** — unprovable as stated. (Harmlessly far past the s ≈ 3×10¹⁵ ridge, and T_C itself is long-decaying there; the flaw is in the quantifier, not the conclusion.) Two minor display items: the critical-row printout "floor(1/Tbar)=7" at exactly BCRIT is float roundoff at the boundary (T̄ = 1/8 exactly ⇒ floor 8; the strict form B < BCRIT avoids the boundary anyway); stored Tbar line prints 0.125000000000 for the same reason.

## 4. Repairs [deposited, gates P4–P5]

**A (window + tail).** Tier-1 (PROVED, F027) gives T_C < 1/8 unconditionally for x ≥ x₁ = 2633 (takeover bracket gate-checked). So the B-window hypothesis is needed only on the **finite window x ∈ [0, 2633]**, where the true B(x) reaches at most 0.040909 — **margin 13% at the splice**, growing to 61% at the data end. x₁ ≪ x_cross ✓.

**B (three-parameter majorant — the recommended target).** Prove instead
**Y(x) ≤ A·x + (A/2)·ln α(x) + D for all x ≥ 0, with D ≤ D_crit = 0.044751725** (bisected, T̄₃(D_crit) = 1/8 ± 1e-9). Measured: D∞ = 0.021301939 (∞-volume, constant), and the finite-L diagonal sits lower still (D ≤ 0.018356 at every computed point). **Uniform headroom ×2.10, no window, no splice.** This majorant has exactly the shape the heat-kernel/theta-tail analysis produces (the (A/2)ln α term is the subleading structure the two-parameter form was missing), so it is the natural form for the bounded-effort Euler–Maclaurin/theta upgrade the trio flagged as pin (i).

## 5. Status after this review

The Tier-2 pins now stand as: **one inequality, two equivalent sufficient forms, thresholds exact (57/1210 rational; D_crit bisected), margins measured (13% windowed / ×2.10 uniform), and the D-constancy discovery** (the ∞-volume law Y = Ax + (A/2)ln α + D∞ is machine-exact for x ≥ 40 — D∞'s explicit Bessel-integral expression is in the audit engine; closed form for D∞ is an optional follow-up). What remains analytic: a two-sided bound on the heat-kernel integrand tails delivering form B with D ≤ 0.0448 — a scalar-analysis lemma with 2× room, no lattice content. Grounds: P1 exact-rational; P2–P5 machine-verified; the "repairs make it airtight" claim is conditional on proving the (now precisely specified) scalar inequality — nothing is claimed proven beyond Tier-1.
