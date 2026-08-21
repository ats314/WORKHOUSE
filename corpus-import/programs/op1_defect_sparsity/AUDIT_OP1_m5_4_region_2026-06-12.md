# M5.4–M5.8 audit + Theorem (Region A): cover domination proved for t ≥ 0.4·L²

**Date:** June 12, 2026
**Author:** session agent (lead math agent per DECISIONS #009), for Alex
**Engine:** `ENGINE_OP1_m5b_region.py` → `CERT_OP1_m5b_region.json` (gates G-A1..G-A6, all hard asserts, ALL PASS)
**Audited upload:** `M5_4___WARNING_FREE_LIMIT_CONSTANT_AUDIT_FOR_LEMMA_B.ipynb` — which in fact contains five blocks, M5.4 through M5.8. Companion to `AUDIT_OP1_m5_lemmas_2026-06-12.md` (same day).

**Headline:** (i) every quantitative claim in M5.4–M5.8 verifies, with three nits documented below; (ii) C∞ is now pinned **three independent ways to 1.4·10⁻¹³**; (iii) the continuum core of Lemma A now has **two independent proofs** (my analytic two-region argument; their 80-digit box certificate, reproduced here exactly); (iv) **new theorem proved in this note: the finite-L cover domination holds on all of Region A, t ≥ 0.4·L², every integer L ≥ 4** — so Lemma A is now open only on the compact window t/L² ∈ (0, 0.4]; (v) the pointwise "lattice ≤ continuum" bridge route I floated for that window is **falsified at leading order mid-window** (honest correction, §3) and replaced by a concrete per-L box route.

---

## 1. Audit verdicts, block by block

**M5.4 (warning-free limit constant).** The μ → 0 limit formula is exact: c·E1(μ²T₀) → c(−γ_E − ln T₀ − ln μ²), and with μ² = 48/(βL²) the −c·ln μ² term reproduces A·ln(L/4) + (A/2)·ln β plus A ln4 − (A/2)ln48, using (3/4)·2c = A and (3/4)c = A/2 — verified analytically. The geometric dyadic residual is clean numerics. One reconciliation: their center omits the positive tail beyond TMAX (kept only in the error band); adding its leading value, center + 0.75·c/(4·2²⁴) = 0.012792103146542, agrees with my independent G-M6 value 0.012792103146403 to **1.39·10⁻¹³** (G-A5), and their bracket contains it. **C∞ = 0.0127921031464, pinned by three structurally different computations** (M5.3 evaluation at x = 20; my second-order-subtracted quadrature; M5.4's limit formula).

**M5.5 (θ-limit audit).** Same object as my continuum core (their τ = my c, their R = my G). Grid and optimizer results match the proved picture: R < 1 everywhere, saturating only as τ → 0. The alarming row "Rmax = 1.0000000000000004, gap = +1.024·10³" at τ ≈ 4.5·10⁻¹¹ is machine-epsilon noise in R amplified by (4πτ)⁻² ≈ 3·10¹⁸ in the gap variable — correctly superseded by the mpmath treatment in M5.6b. Their proof-oriented regime split matches my two-region structure.

**M5.6/M5.6b (box certificate).** This is an independent **second proof of the continuum core**, certificate-level: crude-constant regimes (ε, η ≤ 3e^{−·}, (1+ε)⁴−1 ≤ 15ε) at the two ends plus an adaptive interval certificate with rigorous geometric θ-tails at 80 digits in the middle. I reproduce it exactly: first certified box R-bound 0.980657081547 on [0.05, 0.0609375] to 12 digits, and a 6-box certification of [0.05, 0.4] (G-A6). Two **wording nits, conclusions unaffected**: the small-τ margin m_s(τ) = ln(16π²τ²/45) + 1/(4τ) has m_s′ = (8τ−1)/(4τ²) < 0 on (0, 1/8), i.e. it is *decreasing*, which is exactly why checking the right endpoint τ = 0.05 suffices (their note says "increasing"); the large-τ margin m_l(τ) = 4π²τ − 2ln(4πτ) − ln45 is *increasing* for τ > 1/(2π²), which is why checking the left endpoint τ = 0.4 suffices (their note says "decreasing"). Both endpoint checks performed are the binding ones; the certificates stand as run.

**M5.7/M5.7b (finite-L maximizer).** Stable hybrid (image rep for τ < 0.04, spectral beyond) is the right construction. Finding confirmed: for every L ≤ 2048 the maximizer of E_L = (LΦ)⁴ − 1 − (Lq)⁴ rides the t → ∞ boundary with E → 0⁻ (their Emax ≈ −2.4·10⁻¹³ is float resolution at the boundary; the true supremum is 0, not attained). No interior dangerous window exists — the only saturations are the two trivial ends, matching the continuum picture.

**M5.8 (proof split).** The split at τ₀ = 0.4 is the right architecture, and their post-mixing numbers calibrate my theorem below precisely: their measured lhs/rhs at the τ = 0.4 corner is 0.337, against my analytic constant 0.3393 — sharp to 0.7%. Their compact-window maximizer shows a **uniform margin |E_L| ≥ 0.0396 on (0, 0.4], with the maximum at the τ = 0.4 boundary** — i.e. the open region's worst point adjoins the proved region.

## 2. THEOREM (Region A) — PROVED

**Theorem.** For every integer L ≥ 4 and every t ≥ 0.4·L²: Φ_L(t)⁴ − L⁻⁴ ≤ q(t)⁴.

Write τ = t/L², r = L·q(t), e = L·Φ_L(t) − 1, so the claim is (1+e)⁴ − 1 ≤ r⁴.

**Lemma R1 (spectral excess).** e = Σ_{n=1}^{L−1} e^{−4t sin²(πn/L)} ≤ 2Σ_{k≥1} e^{−16τk²} ≤ 2.0001·e^{−16τ} for τ ≥ 0.4.
*Proof.* Pair n ↔ L−n; for 1 ≤ k ≤ L/2, concavity of sin on [0, π/2] gives sin(πk/L) ≥ 2k/L, so 4t sin²(πk/L) ≥ 16τk². The k ≥ 2 tail is geometric: Σ_{k≥2}e^{−16τk²} ≤ e^{−48τ}Σ_{j≥0}e^{−80τj} ≤ e^{−19.2}/(1−e^{−32})·e^{−16τ}, giving the constant 2.0001. ∎

**Lemma R2 (Gaussian lower bound).** q(t) ≥ erf(π√t)/(2√(πt)) for all t > 0; hence r ≥ erf(π√t)/(2√(πτ)).
*Proof.* q(t) = (1/π)∫₀^π e^{−2t(1−cosθ)}dθ ≥ (1/π)∫₀^π e^{−tθ²}dθ = erf(π√t)/(2√(πt)), using 1 − cosθ ≤ θ²/2. ∎

*Proof of the Theorem.* (1+e)⁴ − 1 ≤ 4e(1+e)³ with e ≤ 2.0001e^{−6.4} = 3.324·10⁻³, so (1+e)³ ≤ 1.01. By R2 and t ≥ 0.4·16 = 6.4: erf(π√t) ≥ erf(7.947) ≥ 1 − e^{−63.1}/(7.9√π) ≥ 1 − 10⁻²⁷, so r⁴ ≥ (1 − 10⁻²⁶)/(16π²τ²). Therefore

  (1+e)⁴ − 1 − r⁴ ≤ [h_A(τ) − 1]·(1−10⁻²⁶)/(16π²τ²),  h_A(τ) := 4·2.0001·1.01·16π²·τ²e^{−16τ}/(1−10⁻²⁶) ≤ 1276.1·τ²e^{−16τ}·(1+10⁻²⁶).

τ²e^{−16τ} is decreasing for τ > 1/8, so on [0.4, ∞): h_A(τ) ≤ h_A(0.4) = 1276.1·0.16·e^{−6.4} = **0.33925 < 1**, and the left side is strictly negative. ∎

Gates: G-A1 (h_A ≤ 0.3395 on [0.4, 50], decreasing); G-A2 (Lemmas R1/R2 verified against exact kernels on adversarial (L, τ), slacks −3.2·10⁻²⁸ / +2.1·10⁻¹²); G-A3 (E_L < 0 directly on Region-A samples up to L = 2048, and the proof bound dominates the exact E_L). The constant is essentially sharp: M5.8's measured corner ratio is 0.337.

**Consequence.** Lemma A (cover domination, hence the entire M5 chain's A-side) is now open **only on the compact window τ ∈ (0, 0.4]**, where M5.8's audit shows a uniform numeric margin |E_L| ≥ 0.0396 with the maximum at the boundary joining this theorem.

## 3. Compact window: corrected route (an honest falsification)

Last note's §5 floated reducing the compact window to the continuum core by pointwise domination E_L ≤ E_cont. The corrected leading-order computation (G-A4, with the ±n doubling my first pass missed) **falsifies that route mid-window**: the ratio of the 1/L² corrections (Φ-side over q-side) is exactly 1 in the τ → 0 limit — an identity regime, since with wraps dead both corrections are the same lattice-dispersion object — rises to **1.46 at τ ≈ 0.085** (Φ-side wins: pointwise domination fails there), and decays to 0.038 by τ = 0.3 and 0.002 at the Region-A junction. Since Lemma A itself holds with margin throughout (continuum R ≤ 0.98 certified; lattice E ≤ −0.0396 measured), the failure is of the *route*, not the lemma. The workable route, now stated precisely: **per-L box certificates** on τ ∈ (0, 0.4] for 4 ≤ L ≤ L₀ — each L is a one-variable problem with exactly M5.6b's machinery, using cancellation-safe forms (image-tail at small τ, expm1-spectral at moderate τ) — plus a **uniform L ≥ L₀ argument** from the two-sided dispersion bounds x²(1 − x²/3) ≤ sin²x ≤ x² with n-stratification (small n: corrected Gaussian terms; n ≳ L/4: crude e^{−2τL²}-type kill). The small-τ end of every box closes by wrap-Chernoff (p_k(t) ≤ e^{−tΛ*(k/t)}, elementary Markov on the continuous-time walk). Assessment [opinion]: with Region A proved and the identity-regime structure understood, this is now a bounded bookkeeping task; the 0.0396 uniform margin is the budget, and nothing in the diagnostics threatens it.

## 4. Consolidated M5 status (supersedes §7 of the companion note)

| Item | Status |
|---|---|
| C-form reduction, C_CRIT, rational threshold 1/28 | **EXACT / triple-verified** |
| C∞ = 0.0127921031464 | **PINNED three ways to 1.4·10⁻¹³** (G-A5) |
| Lemma B monotonicity (D′ > 0) | gated with margin 3.5×; one-page elementary write-up flagged |
| Lemma A, continuum core | **PROVED twice** (analytic two-region; 80-digit box certificate, reproduced G-A6) |
| Lemma A, Region A (t ≥ 0.4L², all L ≥ 4) | **PROVED here** (§2; constant sharp to 0.7%) |
| Lemma A, compact window τ ∈ (0, 0.4] | REMAINING; route corrected (§3); uniform numeric margin 0.0396, worst point adjoins the theorem |
| Claim 1 (Φ_L ≤ 1/L + q) | PROVED (companion note §3) |
| Consequence once the compact window closes | T_C ≤ 0.11692 < 1/8 ⇒ **N\*_C ≥ 8, T_full < 9/64, N\* ≥ 7 uniformly** — Tier-2 pins removed |

Three nits for the working tree: M5.6's two monotonicity wordings (invert them; endpoint checks unchanged); M5.5's noise row (annotate, or defer to M5.6b); M5.4's center (either add the 0.75·c/(4·TMAX) tail to the center or keep it bracket-only — both honest, the bracket already is).

Suggested STATE.md line (owner to paste):
> M5/Tier-2 — Region A of Lemma A PROVED (AUDIT_OP1_m5_4_region_2026-06-12.md §2: t ≥ 0.4L², all L ≥ 4, constant 0.339 sharp to 0.7%); continuum core now proved twice (analytic + 80-digit box certificate, reproduced); C∞ pinned three ways to 1.4e-13; compact window τ ∈ (0, 0.4] is the sole remaining A-side item — pointwise-continuum route falsified (bridge ratio 1.46 at τ ≈ 0.085, identity regime at τ → 0), per-L box + uniform large-L dispersion route stated; Lemma B unchanged (constant pinned, write-up flagged).

## 5. Files, gates, reproduction

`ENGINE_OP1_m5b_region.py` (G-A1 h_A calculus; G-A2 Lemmas R1/R2 vs exact kernels; G-A3 direct Region-A E_L + domination; G-A4 corrected bridge diagnostic; G-A5 C∞ reconciliation; G-A6 box-certificate reproduction), `CERT_OP1_m5b_region.json`. Reproduce: `python3 ENGINE_OP1_m5b_region.py` (reads `/home/claude/AUDIT_OP1_m5.json` for G-A5). Dependencies: numpy, scipy. MD5s in the session message.
