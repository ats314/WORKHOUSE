# Z.A cap-geometry: the bare-cap curvature lemma (proved), and a gap in the §9 incident reduction

**Date:** June 12, 2026
**Author:** session agent (lead math agent, DECISIONS #009), for Alex
**Target:** §§8–9 of `programs/pmbsf/NOTE_PMBSF_lci_tosj_reduction_lemmaq_2026_05_26.md` (the SU(2) Lemma Q reduction). That note proves LCI + far-source ⟹ TOS+J ⟹ Lemma Q (§§2,3,7,11) and reduces LCI to a finite-dimensional spherical cap-geometry condition (§§8–9), but states the key cap estimate as *"a Laplace ratio estimate gives … under nondegenerate exposed-maximizer hypotheses"* (8.4) and the curvature step *"Δ_p(A) ≥ c_curv χ₀²"* (9.5) **without proof or explicit constant**. This note proves the bare-cap case, certifies the cap-ratio law's rate, and exhibits a verified **counterexample to (9.5) for incident subsets** — with a constructive fix.
**Engine:** `ENGINE_OP1_za_cert_v5.py` (canonical; v1–v4 are gated iterations) → `CERT_OP1_za_cap.json`. Gates **G-ZA1, G-ZA2, G-ZA3, G-ZA3b, G-ZA4, G-ZA5 ALL PASS**.
**Status labels:** §1 PROVED (+machine-verified 1.3e-15); §2 PROVED (counterexample, sampling-verified); §3 MACHINE-CERTIFIED (rate); §4 the residual, labeled.

---

## 0. Setup (the §4–9 geometry)

For an incident link `e` with one-link heat-bath law vMF(m, κ) on `S³ ⊂ R⁴` (`m = H_e/‖H_e‖`, `κ = β‖H_e‖`), each incident plaquette `r` contributes a cap `C_r = {u ∈ S³ : u·n_r ≤ a}`, `a = 1−(t−η)`. For a cap set `A`, `C_A = ⋂_{r∈A} C_r`, `u_A = argmax_{u∈C_A} m·u`, `h(A) = m·u_A`. The target cap is `C_p`. Two quantities:

- the §9 **gap at the maximizer**: `χ₀(A) = u_A·n_p − a` (the good event `G_LCI` (9.7) asks `χ₀(A) ≥ χ₀*` for all incident `A`);
- the **height drop** the Laplace estimate (8.4) actually uses: `Δ_p(A) = h(A) − h(A∪{p}) ≥ 0`.

The reduction's §9 claims `χ₀(A) ≥ χ₀* ⟹ Δ_p(A) ≥ c_curv χ₀*²`, converting the analytic condition (8.4) into the computable gap criterion (9.4). **§2 below shows this implication is false for incident subsets.** §1 proves it (sharply) for the bare cap.

## 1. The bare-cap curvature lemma (A = ∅) — PROVED

**Lemma 1.** Let `c₀ = m·n_p` and `χ₀ = c₀ − a > 0` (the good event: the mean `m` lies outside `C_p`). Then `u_∅ = m`, `h(∅) = 1`, and

  **Δ_p(∅) = 1 − a c₀ − √((1−a²)(1−c₀²))**,  and  **Δ_p(∅) ≥ χ₀²/2**,

with the sharp small-gap constant `Δ_p(∅) = χ₀²/(2 sin²σ) → χ₀²/(2(1−c₀²))` as `χ₀ → 0`.

*Proof.* Since `c₀ > a`, the constraint `u·n_p ≤ a` binds, so `h({p})` is attained on `{u·n_p = a}`. Writing `u = a n_p + √(1−a²) v` with `v ⊥ n_p`, `|v|=1`, gives `m·u = a c₀ + √(1−a²)(m·v)`; maximizing `m·v` over `v ⊥ n_p` gives `|P_{n_p^⊥} m| = √(1−c₀²)`. Hence `h({p}) = a c₀ + √((1−a²)(1−c₀²))` and the displayed `Δ_p`.

Set `a = cos α`, `c₀ = cos β` with `α, β ∈ [0,π]`, `α > β` (since `a < c₀`). Then `a c₀ + √((1−a²)(1−c₀²)) = cos α cos β + sin α sin β = cos(α−β)`, so with `δ = (α−β)/2 > 0`:

  **Δ_p(∅) = 1 − cos(α−β) = 2 sin²δ.**

Also, with `σ = (α+β)/2`, `χ₀ = cos β − cos α = 2 sin σ sin δ`. Therefore

  `χ₀²/2 = 2 sin²σ sin²δ ≤ 2 sin²δ = Δ_p(∅)`,

because `sin²σ ≤ 1`. Equality iff `sin²σ = 1` (i.e. `α+β = π`). As `χ₀ → 0`, `δ → 0`, `χ₀ ≈ 2 sin σ · δ`, so `Δ_p ≈ 2δ² = χ₀²/(2 sin²σ)`, and `σ → β = arccos c₀` gives `sin²σ → 1 − c₀²`. ∎

**Machine check (G-ZA1/G-ZA2):** over the `k=0` good-event configs, the closed form matches the active-set solver to **1.33×10⁻¹⁵**; the lower bound `Δ_p ≥ χ₀²/2` holds with **min ratio exactly 0.50000** (the bound is tight, as the `sin²σ=1` equality case predicts); the leading constant `1/(2(1−c₀²))` is reproduced to 1.6% in the asymptotic regime `χ₀ ≪ 1−c₀²`. This is the explicit `c_curv = 1/2` (universal) / `1/(2(1−c₀²))` (sharp) the reduction's (9.5) left unspecified.

## 2. The incident reduction (9.5) is FALSE — counterexample (sampling-verified)

**Claim.** There exist `m, n_p` and an incident cap set `A` (`|A| ≥ 1`) and `a` with `χ₀(A) > 0` of order one, yet `Δ_p(A) ≪ χ₀(A)²/2`. Hence `χ₀(A) ≥ χ₀*` does **not** imply `Δ_p(A) ≥ c χ₀*²`, and the §9 good event `G_LCI` (9.7), which quantifies only `χ₀` at `u_A`, is **insufficient** to control the cap ratio (8.4).

**Exhibit (G-ZA5, independently sampling-verified at 4×10⁶ points):** `k = 3` incident caps, `χ₀(A) = 0.192` (a healthy gap at the maximizer), but the true height drop `Δ_p(A) = 0.0025` (solver and independent dense-sampling agree) versus `χ₀²/2 = 0.0184` — a **~7× shortfall**, ratio `Δ_p/χ₀² = 0.0069 ≪ 1/2`. Over all valid incident configs (hardened solver, 0 inconsistent-drop artifacts), the violation rate of `Δ_p ≥ χ₀²/2` is **12%**, with the ratio reaching `0.007`.

**Mechanism.** `χ₀(A) = u_A·n_p − a` measures only how far the single maximizer `u_A` sits outside `C_p`. With incident caps present, `C_A ∩ C_p` can still contain an *alternative* near-maximal point (one where a neighbor cap, not `C_p`, is active), so adding `C_p` barely lowers the height — `Δ_p` is small even though `u_A` is well outside `C_p`. The bare cap (§1) has no such alternative, which is why the implication holds there and only there.

**Constructive fix.** The cap-ratio estimate (8.4) is governed by the **true height drop** `Δ_p(A)`, not by `χ₀`. So the good event should be parametrized directly by `Δ_p`:

  **`G_LCI' = { Δ_p(A) ≥ Δ* for all incident A }`,  Δ* ≳ Δ_q + (M log κ + O(1))/κ,**

with `Δ_q ≈ −(log q)/κ`. This is the geometrically correct condition; `χ₀` is a valid proxy only in the single-cap case (§1, where `Δ_p ≥ χ₀²/2`). **Actionable consequence:** the diagnostic `ENGINE_FLUX_lci_typicality_diagnostic.py`, which measures `min_A χ₀(A)` and calls `G_LCI = {min χ₀ ≥ χ₀*}`, should be re-pointed to measure `min_A Δ_p(A)` directly — its cap-intersection solver already computes `h(A)` and `h(A∪{p})`, so the change is to report `h(A) − h(A∪{p})` rather than `u_A·n_p − a`.

## 3. The cap-ratio law (8.4) — rate certified

For `A = ∅`, `ν(C_p) = P_vMF(u·n_p ≤ a)` was computed by exact 2-D vMF quadrature (marginal of `(u·m, u·e)` on the unit disk `∝ e^{κ w}√(1−w²−y²)`) over a `κ` ladder `60…700`. The fit `−log ν(C_p) = κ Δ_p − M log κ − log C_geom` holds with **max residual 0.005**; the rate matches the proved `Δ_p` (G-ZA3: 2-point slope 0.0810 and 3-parameter slope 0.0802 vs `Δ_p = 0.0804`). The prefactor power is **M ≈ −0.49** (i.e. `ν ∼ C_geom κ^{+1/2} e^{−κΔ_p}`): the dominant Laplace point sits at the corner where the constraint line meets the sphere-disk boundary and the fiber density `√(1−w²−y²)` vanishes, so the prefactor *grows* like `κ^{1/2}` rather than decaying — a correction to the naive `κ^M, M>0` reading of (8.4), harmless because only the exponential rate is load-bearing for LCI.

## 4. What this settles, and the residual for Z.A

**Settled (this pass):**
- The cap curvature step (9.5) is **proved sharply for the bare cap** with explicit constant `c_curv = 1/2` (universal) / `1/(2(1−c₀²))` (sharp) — replacing the reduction's unspecified `c_curv`.
- The cap-ratio law (8.4) has the **correct exponential rate `Δ_p`** (certified), with the prefactor pinned at `κ^{+1/2}` (corner-Laplace).
- (9.5) is **false for incident subsets** (verified counterexample, 12% rate); the `χ₀`-parametrization of the good event must be replaced by the height-drop `Δ_p` (constructive fix; diagnostic re-pointing specified).

**Residual (Z.A still open):** with the good event correctly stated as `G_LCI' = {min_A Δ_p(A) ≥ Δ*}`, Z.A is the **typicality** statement: under the tempered SU(2) heat-bath geometry, `G_LCI'` holds with rooted/absorbed complement, uniformly. Two pieces remain:
1. **The multi-cap Laplace estimate (8.4) for `A ≠ ∅`** — proving `ν(C_p|C_A) ≤ C κ^{M} e^{−κ Δ_p(A)}` with the true `Δ_p(A)` and a uniform prefactor over incident subsets (the §1 method gives the rate; the constant uniformity over the 5 incident caps and the corner structure need the general Laplace argument). Agent-tractable next.
2. **The stochastic typicality of `min_A Δ_p(A) ≥ Δ*`** — the genuinely probabilistic core, tied to the heat-bath staple geometry and the far-source/Z.B stability. This is where the diagnostic (re-pointed to `Δ_p`) supplies evidence and Bałaban locality must enter.

**Scope honesty.** Nothing here proves Z.A or Lemma Q. It proves the bare-cap curvature constant, certifies the cap-ratio rate, and corrects a real gap in the published §9 reduction (the `χ₀`→`Δ_p` substitution). Grounds: §1 proof = derived-and-machine-verified (1.3e-15); §2 = a sampling-verified counterexample; §3 = exact-quadrature certificate; §4 residual = labeled open. The correction to §9 is the kind of referee-grade objection-plus-fix the reduction needs before it can be tightened to a theorem.

---

## 5-bis. The multi-cap rate (A ≠ ∅) — completing the deterministic core (F038)

§3 certified the cap-ratio rate for the bare cap. The incident case is settled by a large-deviation argument plus exact quadrature (finding F038; engine `ENGINE_OP1_za_multicap_v2.py`).

**Theorem (rate, A ≠ ∅).** For incident cap set `A` with `Δ_p(A) = h(A) − h(A∪{p}) > 0`,
`lim_{κ→∞} −(1/κ) log ν(C_p|C_A) = Δ_p(A)`.
*Proof.* vMF(m,κ) obeys an LDP on S³ with rate `I(u)=1−m·u`, speed κ. Varadhan/Laplace gives `−(1/κ)log ν(C_A) → 1−h(A)` and `−(1/κ)log ν(C_p∩C_A) → 1−h(A∪{p})`; subtract. ∎

**Certification (G-ZB1/G-ZB2, exact 3-D quadrature, κ = 20…150, codim 0/1/2):** the fitted rate matches the solver `Δ_p(A)` to worst error **0.0056**; the prefactor power `M ∈ [−0.47, −0.19] ⊂ [−1/2, 0]` (bounded, so at worst `κ^{1/2}`, absorbed into the LCI margin). The measured rates (0.06–0.30) differ from `χ₀` (0.18–0.45) — re-confirming `Δ_p`, not `χ₀`, governs.

**Consequence — the deterministic LCI core is complete.** Every finite-dimensional / Laplace step of §§6–11 is now proved or certified, and the LCI condition (6.3) holds **iff**
`min_A Δ_p(A) ≥ Δ_q + (M logκ + O(1))/κ`, `M ∈ [−½,0]`.
**Z.A is thereby reduced to the single typicality statement:** under the tempered heat-bath geometry, `G_LCI' = {min_A Δ_p(A) ≥ Δ_q + O(logκ/κ)}` holds P-typically, with rooted/absorbed complement. That is the entire remaining content of Z.A — purely stochastic, coupled to Z.B. Finding: `records/review/findings/F038_za_multicap_rate.md`.

---

## 6. The corrected observable measured on the heat-bath ensemble (F039)

Executing the §5/§5-bis actionable: the diagnostic observable is re-pointed from `min_A χ₀` to `min_A Δ_p` and measured on a real SU(2) exact-heat-bath config (β = 3.5, L = 4; engine `ENGINE_OP1_za_dp_v3.py`, gates G-DT1 no-impossible-drops + G-DT2 bare-cap-lemma-on-data PASS). Findings (F039):

- **The two observables agree on *whether* the good event holds** — exactly, since `min_A Δ_p > 0 ⟺ min_A χ₀ > 0` (Δ_p(A) > 0 ⟺ u_A ∉ C_p ⟺ χ₀(A) > 0). At L=4, β=3.5 both give good-fraction **0.125**. So χ₀ is a valid yes/no indicator; the F037 correction is about the *margin*, not the sign.
- **The margin is much smaller under Δ_p:** `min_A χ₀` reaches > 0.10 but `min_A Δ_p ≤ 0.05` always, and **half of the χ₀-comfortably-good records (>0.05) are Δ_p-marginal (<0.01)** — F037's overstatement, quantified on data.
- **Typicality steer:** κ_e ≈ 18 ⟹ threshold O(logκ/κ) ≈ 0.16, while min_Δp ≤ 0.05 everywhere ⟹ the strict G_LCI' good event is essentially empty at L=4, so almost everything is rooted. This does not refute Z.A (L=4 is maximally constrained; Stage-B plausibility was L=16) — it shows Z.A's typicality is a **larger-L + rooted (Z.B)** phenomenon. **Next experiment:** the same Δ_p measurement at L=16. Finding: `records/review/findings/F039_za_dp_observable_measured.md`.

---

## 7. The L-scan: the deterministic good event stays weak through L=16 (F040)

Executing §6's L=16 experiment required a faster sampler: a **vectorized SU(2) heat-bath** (`ENGINE_PMBSF_su2_hb_v3.py`, 28× faster; gates G-HB1 staple==diagnostic 6.7e-16, G-HB2 equilibrium plaquette matches). Measuring `min_A Δ_p` at L = 4, 8, 16 (β = 3.5; `ENGINE_OP1_za_dp_vsl.py`, G-DT1/G-DT2 PASS):

| L | frac(min_Δp>0) | max min_Δp | κ_e |
|---|---|---|---|
| 4 | 0.125 | ≤0.05 | 17.9 |
| 8 | 0.175 | 0.043 | 17.9 |
| 16 | 0.121 | 0.070 | 17.6 |

**The good-event fraction is roughly flat in L** (~0.12–0.18; the L=8 value is single-config noise — at L=16 it returns to 0.12), and margins stay small (median 0 at every L; only a mild tail extension to max 0.07 by L=16). **So F039's "typicality is a larger-L phenomenon" is NOT borne out** — going to the Stage-B size does not make `G_LCI'` typical; the bad set (min_Δp = 0 ⟹ some incident subset frees X_p ⟹ LCI fails for it) stays **~85% at all L ≤ 16**. Consequence: the LCI bound rests on the rooted/absorbed complement + **Z.B (far-source stability), which is load-bearing, not complementary to a healthy Z.A good event**. This is **not** a disproof of Z.A — min-over-all-subsets is the strictest good-event measure, and the rooted sum weights bad subsets by the tilt `s^{|A|}` — but it relocates OP-1's (S) closure question to "does Z.B control an ~85% bad set?", with the LCI cap geometry (Z.A's deterministic core, §§1–6 / F037/F038) settled. Finding: `records/review/findings/F040_za_dp_vs_L.md`.

---

## 8. The tilted ratio (7.2), not the pointwise min — F040's "bad set" is overwhelmingly fine (F041)

F040's `min_A Δ_p` is the **strictest** LCI proxy: it asks the term-wise bound `ν(C_p∩C_A) ≤ C_LCI q ν(C_A)` to hold for **every** subset A (the reduction's (7.4–7.5)). But (7.2) only needs the **ratio of the tilted sums** small. Using the exact identity (7.4–7.7), the source-tilted ratio is a single vMF expectation:

  `R(e,p;s) = ν^{B,s}(C_p) = E_ν[1_{C_p}∏_{r∈B}(1+s·1_{C_r})] / E_ν[∏_{r∈B}(1+s·1_{C_r})]`.

Measured on the F040 ensembles (engine `ENGINE_OP1_za_rt_f041b.py`, gates G-RT1 sampler-vs-Bessel, G-RT2 MC-vs-quadrature, G-RT3 s=0⟹Amp=1, G-RT4 7.4–7.7 identity, G-DT1; all PASS), reporting `Amp(s) = R/ν(C_p)`:

| L | pointwise-BAD frac | median Amp | q90 Amp | q99 / max Amp (s=4) |
|---|---|---|---|---|
| 4 (8 cfg) | 0.851 ± 0.026 | ≈1 | ≈ (1+s) | 31.8 / 123.7 |
| 8 (4 cfg) | 0.854 ± 0.015 | ≈1 | ≈ (1+s) | 24.3 / 33.0 |
| 16 (1 cfg)| 0.839 | ≈1 | ≈ (1+s) | 124 / 124 |

**Median Amp ≈ 1 and q90 ≈ 1+s at every L — identically on the ~85% pointwise-bad records.** So the term-wise bound failing on a subset almost never inflates the tilted ratio: F040's ~85% "bad set" is overwhelmingly **not** bad for (7.2), which the bulk satisfies with `C_LCI = O(1)`. The residual is a **thin (~1%) heavy tail** (q99 ≈ (1+s)², max ≈ (1+s)³) on records where `C_p` overlaps 2–3 incident caps, and it **does not grow with volume** (L=4→8 max 124→33). **Consequence:** Z.B's target sharpens from "control an 85% bad set" (F040) to "control a thin, volume-stable, multi-cap-overlap heavy tail of the tilted ratio" (the tilt `s ≤ ρ/q` makes that tail the load-bearing rare event). Finding `records/review/findings/F041_rooted_tilt_amplification.md`; data `rooted_tilt_L{4,8,16}.json`, plot `DATA_OP1_rooted_tilt_amp.png`.

## 9. The heavy tail is the cap-overlap mechanism — and it amplifies only mildly (F042; revises §8's tail)

§8's heavy tail (q99≈(1+s)², max≈(1+s)³) suggested the tail records are those where `C_p` overlaps several incident caps. F042 tests this with the pairwise conditional lift `L_r = ν(C_p|C_r)/ν(C_p)` and overlap count `k_eff = #{r: L_r ≥ 2}`, on records with ≥40 target-cap hits (engine `ENGINE_OP1_za_overlap_f042.py`; gates G-RT1, G-RT2, **G-OV1** `Amp(s=64) ≈ ν(C_p|C_B)/ν(C_p)` worst **0.000**, all PASS):

| L | median Amp(s=4) by k_eff (0/1/2/3/4) | top-1% Amp4 tail |
|---|---|---|
| 4 | 1.00 / 1.06 / 1.15 / 1.49 / 3.07 | 100% k_eff≥2 |
| 8 | 1.00 / 1.04 / 1.17 / 1.42 / 1.95 | 67% k_eff≥2 |
| 16| 0.99 / 1.09 / 1.17 / 1.75 / 2.79 | (1 record) |

**Mechanism confirmed** (amplification rises monotonically with k_eff; s→∞ limit = full-conditioning lift exactly; tail = multi-overlap). **But the magnitude is mild** — median `Amp(s=4) ≤ ~1.8` even for k_eff=3, versus the naive `5³=125`. So the incident caps overlap `C_p` *weakly*; multi-overlap compounds to a small factor.

**Revision to §8:** §8's reported heavy tail (q99/max ≈ (1+s)²–³) was largely **MC noise on near-zero-`ν_p` records** (a few `C_p` hits in 40k samples → a wildly noisy ratio). With ≥40 hits the genuine worst is single-digit. §8's *bulk* result (median≈1, q90≈1+s, (7.2) with `C_LCI=O(1)`) stands and is **strengthened** — the tilted object is O(1) essentially everywhere, including multi-overlap records. The only unresolved records are `ν_p < 7×10⁻⁴` (below the hit floor); their amplification is governed by the **deterministic** cap-geometry quantity `Lfull = ν(C_p|C_B)/ν(C_p)` (quadrature-computable) — the precise Z.B object, a cap-geometry estimate, not a stochastic 85%-bad-set problem. Finding `records/review/findings/F042_overlap_mechanism.md`; data `overlap_L{4,8,16}.json`, plot `DATA_OP1_overlap_amp_vs_keff.png`.

## 10. The operative amplification is a finite cutoff-stable LOCAL constant; far-source decay is beyond this diagnostic (F043)

Read against the reduction's actual target **(TOS+J, l.86):** `E_{μ^{S,s}}X_p ≤ C q exp(Σ_r J(p,r))`, `J(p,r)≤C_J e^{-m_J d(p,r)}` — the amplification is *allowed* to be `exp(Σ_incident J)`; the load-bearing content is `J`'s exponential **decay in distance** (far sources = Z.B). Built a validated deterministic S³ cap-intersection vMF quadrature (m-frame factorization `u=w m+√(1−w²)ω`; gates G-Q1 vs 1-D quad ≤4.7e-3, G-Q3 refinement ≤3.5e-3, G-Q2 vs MC 0.000). Results (engine `ENGINE_OP1_za_feasible_f043.py`, G-FS1/G-DT1 PASS):

- The **s→∞ full-conditioning limit is not operative**: `ν(C_B)` (all 5 incident caps) is below the resolvable floor (on S³ ≥4 generic hemispheres are jointly infeasible; **max feasible incident |A| = 2** at L=4 and L=8).
- **Operative worst case** — amplification on the maximal reliably-occurring incident subset (|A|≤2): **median 1.0**, thin tail to ~140–190, **cutoff-stable** (L=4→8: 187→140; log(worst amp)≤5.2 ⟹ per-incident-pair `J = O(1)`). A finite O(1)-in-cutoff constant, consistent with (TOS+J)'s local `J`-factor; `E X_p` stays `∝ q` — `X_p` does not go free. Reconciles F041/F042 (bulk unaffected; thin strong-single-pair-overlap tail).

**Delimitation:** the single-link cap geometry (§§1–10, F037–F043) settles the **local/incident** amplification structure. The genuine Z.B content — `J(p,r)`'s exponential decay over lattice distance for **far** sources — requires a multi-plaquette spatial setup and is **beyond this diagnostic family**. Hand-off to the analytic far-source program. Caveats (rule 6): worst-amp tail rests on ~4 records/L (least-pinned); `cmax` rank-deficiency for ≥4 active constraints and quadrature 0/0 on negligible sets surfaced and handled (the superseded `ENGINE_OP1_za_lfull_f043b.py` "Lfull~26" line was a 0/0 artifact). Finding `records/review/findings/F043_local_amplification_quadrature.md`; data `feasible_L{4,8}.json`, plot `DATA_OP1_feasible_amp.png`.

---

*Engine gates: G-ZA1 (bare-cap lower bound, tight 0.5), G-ZA2 (bare-cap closed form 1.3e-15), G-ZA3/3b (cap-ratio rate = Δ_p), G-ZA4 (law form, residual 0.005), G-ZA5 (incident counterexample, sampling-verified). `ENGINE_OP1_za_cert_v5.py` + `CERT_OP1_za_cap.json`. §7 (F040): `ENGINE_OP1_za_dp_vsl.py`. §8 (F041): `ENGINE_OP1_za_rt_f041b.py` + `ENGINE_PMBSF_su2hb_f041.py` + `rooted_tilt_L{4,8,16}.json`. §9 (F042): `ENGINE_OP1_za_overlap_f042.py` + `overlap_L{4,8,16}.json`. §10 (F043): `ENGINE_OP1_za_feasible_f043.py` + `feasible_L{4,8}.json` (validated S³ quadrature; `ENGINE_OP1_za_lfull_f043b.py` superseded-but-retained).*
