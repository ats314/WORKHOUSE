# F034 — Ē₁ measured ≈ 1: the chessboard single-class Tier-S route does NOT reach the anchor (June 12, 2026, late night)

**Unit:** #55 (own-initiative computation, option (c) of the F031 hand-off). **Verdict: a sharp NEGATIVE result — recorded, not buried (CLAUDE.md rule 6).** The chessboard route's Tier-S target quantity **Ē₁(β) = E_{Z′}φ_p, measured directly, is ≈ 1**: Ē₁(5.6) = **1.0034 ± 0.0018**, Ē₁(7.2) = **0.9606 ± 0.0050** (L = 4 SU(3), binned MC errors). The route note (`NOTE_FLUX_s_chessboard_route_2026-06-12.md` §6) hoped for Ē₁ ≲ 0.49; the true value is ≈ 1. **Consequence: the single-class Tier-S upgrade buys essentially nothing for sparse animals (k_x = 1), so the chessboard route as written cannot reach the anchor (5.6, 1.1).** The deterministic side closed this session (F033); this finding sharpens where the *stochastic* side's difficulty actually lives. Engine: `numerics/op12_theta/s_chessboard/ENGINE_OP1_z_prime_mc.py` → `CERT_OP1_z_prime_mc.json`, gate **G-Z1 (calibration) PASS**, G-Z2 (acceptance/unitarity) PASS, G-Z3 result reported (md5 cfddd121).

## 1. What was computed and why it is the right object

Z′ is the SU(3) Wilson measure with **one orientation class (μ,ν) = (0,1) removed from the action entirely** (those plaquettes carry no Gibbs weight), and Ē₁ = ⟨φ_p⟩ on the removed class, φ_p = 1 − (1/3)Re tr U_p. This is exactly the object the chessboard bound produces: a reflection-positivity/chessboard estimate factorizes the constrained partition function into a **product measure over reflected copies in which whole orientation classes are dropped** — global class removal *is* the chessboard Z′, not an approximation of it (this is the defining feature of chessboard estimates, and resolves the route note's "Z′" ambiguity in favor of the faithful reading). The Jensen step the route note flags (E_{Z′}φ_p ≤ 1) is sharp precisely to the extent Ē₁ is below 1; the measurement tests how much room that step has. It has almost none.

## 2. The measurement (MC evidence, sampler gate-calibrated)

New Metropolis sampler (checkerboard-x batched, symmetric X/X† proposal pool, ε-tuned to 0.33–0.50 acceptance, unitarity drift ≤ 7·10⁻¹⁵). **G-Z1 hard gate:** the *full*-Wilson run through the identical code path reproduces the deposited ⟨φ⟩(L=4) — 0.4561 vs 0.4463 at β = 5.6, 0.3193 vs 0.3086 at 7.2 (within 0.012, the gate threshold; the small positive bias is the short L=4 run's finite-statistics, same sign both β) — so the sampler is validated against stored data before any Z′ number is trusted. Then Z′:

| β | full ⟨φ⟩ (self-coupled) | **Ē₁ = ⟨φ⟩_{Z′} (class removed)** |
|---|---|---|
| 5.6 | 0.456 | **1.003 ± 0.002** |
| 7.2 | 0.319 | **0.961 ± 0.005** |

**Interpretation.** Removing the class's self-coupling decouples those plaquettes almost completely: each (0,1) plaquette is a product of four links that, shorn of their own class's ordering field and seeing only the moderately-disordered kept plaquettes (⟨φ⟩_kept = 0.46–0.32, i.e. Re tr/3 ≈ 0.55–0.68), disorders to **near-free-Haar**, where ⟨φ⟩ = 1 exactly (⟨tr U⟩_Haar = 0). The residual ordering grows with β (1.00 → 0.96 as the kept links stiffen), a physically correct monotone trend. The route note's own structural caveat (§6: "Ē_k → 1 as k → 6, free Haar") had the limit right but mislocated it — the approach to 1 is already essentially complete at **k = 1**, not reserved for k = 6.

## 3. Why this blocks the route at the anchor

The route note's profile-weighted program (§6) trades per-cell entropy against per-cell rate β(δ − Ē_{k_x})·k_x. With **Ē₁ ≈ 1**, the k_x = 1 channel contributes rate β(δ − 1) — *identical to Tier-R*, no improvement. But k_x = 1 (one class removed, sparse/tree-like animals) is exactly the **binding open case**: it carries the maximal per-plaquette entropy up to log μ̄ = 3.9957 (F029), while Tier-R supplies only β(δ−1) = 0.56 at the anchor. So sparse animals miss the rooted-summability threshold by a wide margin, and the single-class expectation — the proposed tool — cannot close it. (The dense-animal end, k_x → 6, was already fine: low entropy, and there Ē → 1 harmlessly because the entropy is starved. The route works where it wasn't needed and fails where it was.)

## 4. What survives, and the redirect

This does **not** retract anything proved: Tier-R (the conditional Peierls display, F029) stands, the animal constant stays proved, the deterministic side stays closed (F033). What is refuted is one *opinion* — route note §6 (6)/§8 (6), my own prior pass's "highest-value (S) target" call. Honest redirect, three options now ranked by what the data supports:

1. **δ-window (cheapest, data-supported).** Ē₁ ≈ 1 makes Tier-R the only lever, and Tier-R covers β ≥ β_c(δ): at δ = 1.45, β_c = 8.9 (route §5). If gap-protection tolerates δ = 1.3–1.45 (open question vs `NOTE_OP1_unif_gap_protection_factorization.md`), Tier-R alone covers the **trajectory tail** ln s ≳ 24, and only a bounded-β window near the anchor needs (S) by other means. This is now the highest-value (S)-side question — and it is Alex's gap-protection call, not a chessboard estimate.
2. **Star-conditioning (route §6 option 2), NOT global removal.** Condition on the *star* of p (keep the neighboring plaquettes' weights, remove only p's own) — this retains the coupling that global class removal threw away, and should give Ē < 1. It is a different, more local object than the chessboard Z′, so it would need its own (non-chessboard) summability argument — more work, uncertain. A follow-up MC on this conditional law is the natural next probe; I did not run it this pass.
3. **Z.A/Z.B covariance form (M3a).** Untouched by this; targets the anchor's covariance structure directly, where the chessboard route is now known not to reach. Reinforces M3a as the bottleneck.

## 5. Status changes

(1) Route note §6/§8 optimism about Ē₁ — **refuted by direct measurement**; the note stays deposited verbatim, this finding is its erratum/redirect layer. (2) The (S) "highest-value target" is reassigned from "prove Ē₁ < 1" to **"settle the δ-window against gap-protection"** (Alex) — a cheaper, structurally cleaner lever. (3) OP-1's open content is unchanged in *kind* ((S) + v₀) but the (S) sub-strategy map is sharpened: the chessboard single-class route is now a recorded dead-end for the sparse channel, joining the four prior retired (S) routes (route note §0.5 / PMBSF pass-19). (4) No proved status anywhere changes. Grounds: G-Z1 gate-calibrated MC; the interpretation is physics (labeled); the redirect is opinion (labeled). MC is evidence, not proof — but the qualitative conclusion (Ē₁ ≈ 1, not ≲ 0.5) is far outside the error bars and robust to the finite-volume caveat (the decoupling only strengthens at larger L).
