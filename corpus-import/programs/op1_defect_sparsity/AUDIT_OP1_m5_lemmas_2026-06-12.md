# M5 audit: Tier-2 ceiling pin removal — verdicts, two proved lemmas, corrected pin statement

**Date:** June 12, 2026
**Author:** session agent (lead math agent per DECISIONS #009), for Alex
**Engine:** `ENGINE_OP1_m5_audit.py` → `AUDIT_OP1_m5.json` (gates G-M1..G-M8, all hard asserts, ALL PASS)
**Audited uploads:** `NB_OP1_m5_tier_2_ceiling_pin_auditor.ipynb`, `_M5_1___HEAT_KERNEL_BESSEL_FINITE_CERTIFICATE___TAIL_PIN_TEST.ipynb`, `M5_3___COVER_DOMINATION_CLOSURE_ROUTE.ipynb` (M5_2 referenced therein, not uploaded — its two exported facts, C_CRIT and the L = 47 peak, are both independently confirmed below). The re-uploaded `ENGINE_OP1_m4_tc_closed_form.py/.json` are MD5-identical to my deposit.

**Headline:** the M5 chain is sound and the Tier-2 pins are now reduced to **two scalar lemmas (A: cover domination; B: one renormalized constant)**, of which I prove two pieces of Lemma A outright today (Claim 1, lattice-exact; the continuum core, with explicit margins) and reduce Lemma B to a single number with the monotonicity step gated and its analytic skeleton written. One statement-level error found and fixed: the **B-form pin of M5_1/the auditor is asymptotically false as written** (§2); the C-form of M5_3 is the correct pin and everything numerical survives unchanged.

---

## 1. Audit verdicts per notebook

**`_M5_TIER_2_CEILING_PIN_AUDITOR` — algebra exact, data verified, statement superseded.** γ = 11/(8π²) equals the deposited 2·33/(48π²) exactly; A/γ = 3/44 exact; **Bcrit = 57/1210 is the exact rational** at which the B-form ceiling hits T_C = 1/8 — verified by hand: with β₀ = 28/5 and γ/A = 44/3, the ceiling condition 72(21/55 − B) = (28/5 − 44B/3)² is satisfied at B = 57/1210, both sides equal to 2916/121 = (54/11)². All 17 table rows match my deposited closed-form values (spot-checked at machine precision). Two nits: (i) the printed `floor(1/Tbar)=7` at B = Bcrit is a float artifact — at T = 1/8 exactly, 1/T = 8 and N\*_C ≥ 8 still holds; the reduction is sound at and below Bcrit; (ii) the headline lemma statement is the B-form — see §2.

**`_M5_1` (finite Bessel certificate) — design sound, scan verified, statement superseded.** One-sided wrapping (Y_upper = 0.75·(val + |err| + tail)) is correct upper-bound hygiene; the conservative tail envelope is valid; every integer L ∈ [4, 4096] scanned; dense closed-form cross-checks at 7 L-values agree to ≤ 5·10⁻¹³ with my deposited engine's representation. Max B_L = 0.0184734 at L = 4096, margin 0.02863 — all finite claims stand. The "remaining theta-tail lemma" as stated (B-form for all L) is the item corrected in §2.

**`M5_3` (cover-domination closure) — the correct architecture; all quantitative claims independently confirmed.** My independent implementation (different cutoffs, different tail subtraction at second order with closed-form ∫e^{−μ²t}t⁻² term) reproduces: **C_CRIT = 0.036241888089667** (G-M1, agreement 1.4·10⁻¹⁴ with M5_2's exported value via my own bisection on the envelope maximum); C_inf at four reference x to ≤ 4.7·10⁻¹¹ (G-M6); **C∞ = 0.012792103146** (quad err 3·10⁻¹²). The envelope algebra T_C ≤ 36(Ax + (A/2)ln β + C)/β² is exact (T_C = 36Y/β²). One methodological note: the Lemma-A audit tracks the worst *gap*, which peaks in the numerically dead large-t region (both sides ~ 0, catastrophic cancellation — hence the tiny negative "gaps" and near-zero "ratios" in its printout); the informative diagnostic is the **ratio**, which my G-M3 audit tracks: max ratio < 1 on adversarial grids including odd/prime L ∈ {5,7,9,11,13,17,23,31,47,63,101,129,255}, with the nontrivial-window maximum 0.99131 at (L,t) = (7, 0.496) — exactly the small-c saturation zone the continuum theory predicts (§4).

## 2. FINDING F1 — the B-form pin is asymptotically false; the C-form is the pin

B_L = C_L + (A/2)·ln β(L), and since C_L is bounded (≤ C∞ by §5–§6) while (A/2)ln β(L) → ∞, **B_L is unbounded**: it crosses 57/1210 at x = ln(L/4) ≈ 9818.9, i.e. β ≈ 1373 (G-M2). So the auditor/M5_1 statement "Y_L ≤ A·ln(L/4) + 57/1210 for every integer L ≥ 4" is **false for astronomically large L** — irrelevant to every scanned number, fatal to the lemma as written. The (A/2)ln β term comes from the diagonal's mass μ² = 48/(βL²) carrying a 1/β beyond the pure 1/L² scaling; M5_3's renormalization subtracts it, and C_inf(x) genuinely converges (flat to 12 digits from x = 20).

**Replacement pin (use this wording everywhere the B-form appears):**
> For all integer L ≥ 4 on the AF diagonal, C_L := α_W(L)²T_C(L) − A·ln(L/4) − (A/2)·ln β(L) ≤ **1/28**. Then T_C(L) ≤ max_{x≥0} 36(Ax + (A/2)ln β(x) + 1/28)/β(x)² = 0.124806 < 1/8, hence N\*_C ≥ 8, T_full < 9/64, N\* ≥ 7, uniformly on the diagonal.

The rational 1/28 = 0.0357 is a clean sub-critical threshold (G-M1: Tbar(1/28) = 0.124806, floor 8); the true critical constant is C_CRIT = 0.0362419 (numerically defined); the actual envelope constant is C∞ = 0.0127921 — margin 2.8× to 1/28. Conclusions T_C < 1/8, N\*_C ≥ 8, N\* ≥ 7 are unaffected on every L ever computed; only the *for-all-L statement* needed the C-form.

## 3. Claim 1 — lattice-exact cover bound (PROVED)

**Claim 1.** For every integer L ≥ 2 and every t ≥ 0: Φ_L(t) ≤ 1/L + q(t), where Φ_L(t) = (1/L)Σ_{n=0}^{L−1} e^{−4t sin²(πn/L)} (= Σ_{j∈ℤ} e^{−2t}I_{jL}(2t)) and q(t) = e^{−2t}I₀(2t) = ∫₀¹ e^{−4t sin²(πu)} du.

*Proof.* Write f(u) = e^{−4t sin²(πu)}, so Φ_L − 1/L = (1/L)Σ_{n=1}^{L−1} f(n/L) and q = ∫₀¹ f. f is symmetric about u = 1/2 and decreasing on [0, 1/2]. For 1 ≤ n ≤ ⌊L/2⌋: f(n/L) ≤ L∫_{(n−1)/L}^{n/L} f(u)du (left-endpoint comparison on the decreasing half). For ⌈L/2⌉ ≤ n ≤ L−1, the mirror image gives f(n/L) ≤ L∫_{n/L}^{(n+1)/L} f. The intervals used are pairwise disjoint subsets of [0,1] (for L even they tile [0,1] exactly; for L odd the central interval ((L−1)/2L, (L+1)/2L) is unused). Summing: (1/L)Σ_{n=1}^{L−1} f(n/L) ≤ ∫₀¹ f = q. ∎

Gate G-M4: max over all scanned (L,t) of Φ_L − 1/L − q is −2.8·10⁻⁴ (satisfied with slack at the tightest sampled point).

**Why Claim 1 alone does not close Lemma A.** Inserting Φ ≤ q + 1/L into Y_L produces cross terms; the leading one is (3/4)(4/L)∫t q³e^{−μ²t}dt ≈ 3√β·(4π)^{−3/2}√π/√48 ≈ 0.017√β ≈ **0.043** at β ≈ 6.2 — larger than the entire available margin C_CRIT − C∞ = 0.0234. The genuine Lemma A (with the −L⁻⁴ on the left) is needed; Claim 1 is one of its two proved ingredients.

## 4. Continuum core of Lemma A (PROVED)

In the scaling window t = cL², Lemma A is equivalent (exactly, after Jacobi θ-duality) to:

**Lemma A-core.** G(c) := 16π²c²(θ(c)⁴ − 1) < 1 for every c > 0, where θ(c) = Σ_{n∈ℤ} e^{−4π²cn²}. Equivalently (Jacobi: θ̂(c) = 2√(πc)·θ(c), θ̂(c) = Σ_{k∈ℤ}e^{−k²/(4c)}): θ̂(c)⁴ ≤ 1 + 16π²c².

*Proof.* Two regions.
(a) **c ≥ 1/8.** Let ε = θ − 1 = 2Σ_{n≥1}e^{−4π²cn²} ≤ 2e^{−4π²c}(1 + e^{−12π²c}/(1−e^{−20π²c})) ≤ 2.0000003·e^{−4π²c} (at c = 1/8, e^{−12π²/8} < 10⁻⁶). Then θ⁴ − 1 ≤ 4ε(1+ε)³ ≤ 4ε·(1.014438)³ ≤ 4.1758·ε (ε is decreasing, ε(1/8) = 0.014438). Since c²e^{−4π²c} is decreasing on [1/8, ∞) (its maximum is at c = 1/(2π²) < 1/8), G(c) ≤ 16π²·4.1758·2.0000003·c²e^{−4π²c} ≤ 16π²·8.3516·(1/64)e^{−π²/2} = **0.1482 ≤ 0.149**. (Grid value of the true sup on this region: 0.1381, G-M5.)
(b) **0 < c ≤ 1/8.** Dual side: s = θ̂ − 1 = 2Σ_{k≥1}e^{−k²/(4c)} ≤ 2e^{−1/(4c)}(1 + e^{−3/(4c)}/(1−e^{−5/(4c)})) ≤ 2.005·e^{−1/(4c)} (since e^{−3/(4c)} ≤ e^{−6} here). Using (1+s)⁴ − 1 ≤ 4s(1+s)³, it suffices that h(c) := s(c)(1+s(c))³/(4π²c²) ≤ 1. Both e^{−1/(4c)}/c² (derivative positive iff c < 1/8) and (1+s)³ are increasing on (0, 1/8], so h is increasing and h(c) ≤ h(1/8) = [2.005e^{−2}·(1+2.005e^{−2})³]/(4π²/64) = **0.9039 < 1**. Hence θ̂⁴ ≤ 1 + 0.904·16π²c² ≤ 1 + 16π²c², i.e. G(c) ≤ 1 − 0.096·16π²c² < 1, with saturation only as c → 0. ∎

Gate G-M5 confirms: G < 1 on a 600-point grid spanning c ∈ [6·10⁻⁴, 25] (max 0.99994 at the smallest c, exactly the c → 0 saturation, which on the lattice is the harmless small-t side where the wrap terms are superexponentially dead and the −L⁻⁴ subtraction does the work); sup over c ≥ 1/8 is 0.1381 ≤ 0.149; the margin form 1 − G ≥ 0.096·16π²c² holds at every grid point below 1/8; h(1/8) = 0.903937 matches the hand value.

## 5. Lemma A — what remains (REMAINING, with toolset)

The full lattice statement Φ_L(t)⁴ − L⁻⁴ ≤ q(t)⁴ for all L ≥ 4, t > 0 now needs only the bridge between the exact lattice objects and the proved scaled core: writing x = Lq(t), y = Lw(t) with w = Φ_L − q = 2Σ_{m≥1}p_{mL}(t), p_k(t) = e^{−2t}I_k(2t), the inequality is (x+y)⁴ − x⁴ ≤ 1, and §4 proves its scaling-window limit with margin ≥ 0.096·16π²c² (and ≥ 0.85 absolute for c ≥ 1/8-side). The bridge estimates are elementary but genuinely fiddly: (i) rigorous q-bounds with near-sharp constant — q(t) ≤ 0.2947·t^{−1/2} + 0.682·e^{−0.9194t} follows from the two-region 1−cosθ ≥ 11θ²/12 (θ ≤ 1) / ≥ 0.4597 (θ ≥ 1) split, only 4.5% lossy in the leading constant; (ii) wrap bounds — the elementary Chernoff p_k(t) ≤ inf_λ e^{−λk+2t(coshλ−1)} = e^{−tΛ*(k/t)}, Λ*(v) = v·arcsinh(v/2) + 2 − √(4+v²); (iii) geometric domination of the wrap sum via Turán log-concavity of ν ↦ I_ν, giving w ≤ 2p_L·q/(q − p_L). Assessment [opinion]: a focused half-day of bookkeeping with no conceptual obstruction; the margins (≥ 8.5% in the worst window, far more elsewhere) absorb the stated losses. Flagged as the single remaining analytic item on the A side.

## 6. Lemma B — reduced to one number (RIGOROUS-MODULO-QUADRATURE; write-up flagged)

Define D(μ²) := (3/(64π²))ln(1/μ²) + K_q − Y_inf(μ²) (the deficit of Y_inf from its own asymptote). Then D′(μ²) = (3/4)∫₀^∞ t²e^{−μ²t}[q(t)⁴ − (16π²t²)⁻¹]dt exactly (the asymptote's derivative reproduces the (16π²t²)⁻¹ counter-term under the same weight). The integrand has a single sign change at t* where r(t) := q(t)·√(4πt) crosses 1 (r(0.1) = 0.927, r(0.15) = 1.040 ⇒ t* ∈ (0.10, 0.15)); the head is bounded: ∫₀^{t*} t²e^{−μ²t}·(16π²t²)⁻¹dt ≤ t*/(16π²) ≤ 9.5·10⁻⁴, so head ≥ −7.2·10⁻⁴ after the 3/4. Gate G-M8: D′(μ²) > 0 across the entire diagonal range μ² ∈ (0, 0.5357], with minimum +2.57·10⁻³ at the x = 0 end (quad err 4·10⁻¹⁵) — the positive tail beats the head by 3.5× at the worst point. Hence **C_inf is increasing in x, so sup_{x≥0} C_inf = C∞ = 0.012792103146 ± 3·10⁻¹²** (G-M6, independent implementation, matches M5_3 to 4.7·10⁻¹¹), and Lemma B is the single inequality **C∞ ≤ 1/28** — true with factor 2.8. Status: the monotonicity is proved modulo the gated quadrature sign (analytic skeleton above; the one missing elementary piece is a provable lower bound showing r(t) > 1 for t ≥ 0.15, e.g. a second-order Laplace bound on the integral representation — flagged, one page). The constant C∞ itself is a 1D integral of q⁴, evaluated with explicit tail remainders (second-order subtraction, closed-form ∫e^{−μ²t}t⁻² term, truncation remainder ≤ 2c/(2T₁²) = 4·10⁻¹²).

## 7. Consolidated M5 status

| Item | Status |
|---|---|
| Exact reduction algebra (3/44, 57/1210, envelope T_C = 36(Ax+(A/2)lnβ+C)/β², C_CRIT) | **VERIFIED EXACT / independently reproduced** (G-M1) |
| Finite certificates: every integer L ∈ [4, 4096], B_L and T_C | **VERIFIED** (M5_1 scan + my cross-checks; one-sided bounds) |
| B-form pin for all L | **FALSE as stated** (F1); replaced by C-form, no numerical impact |
| C-form pin: C_L ≤ 1/28 ⇒ N\*_C ≥ 8, N\* ≥ 7 uniform | **EXACT REDUCTION** (G-M1) |
| Lemma A: Claim 1 (Φ_L ≤ 1/L + q) | **PROVED** (§3, lattice-exact) |
| Lemma A: continuum core G(c) < 1 | **PROVED** (§4, explicit two-region constants 0.149 / margin form via h(1/8) = 0.904) |
| Lemma A: lattice bridge | **REMAINING** (§5, toolset listed; flagged) |
| Lemma B: C_inf increasing, C∞ = 0.0127921031 ≤ 1/28 | **RIGOROUS-MODULO-QUADRATURE** (G-M6/G-M8; one-page elementary write-up flagged) |
| Integrated domination C_L ≤ C_inf(x_L), L = 4..256; finite peak | **VERIFIED**; peak C_L = 0.0097790 at **L = 47** (confirms M5_2), C_L(4) = 0.0082276, C_L(256) = 0.0097055 |
| Consequence once A + B close | T_C ≤ Tbar(C∞) = 0.11692 < 1/8 ⇒ **N\*_C ≥ 8, T_full < 9/64, N\* ≥ 7 uniformly on the diagonal** — both former Tier-2 pins (anchored B; extrapolation) removed |

## 8. Miscellany

(i) Float nit: at B = Bcrit or C = C_CRIT exactly, Tbar = 1/8 and N\*_C ≥ 8 still holds (1/T = 8); printed floors of 7 there are float artifacts. (ii) **Stale upload flag:** the uploaded `NOTE_FLUX_s_chessboard_route_2026-06-12.md` is the pre-correction draft (its §5 proof uses the unlicensed per-element dissemination); the authoritative corrected version (per-cell k_x-pattern proof, §6 structural caveat, sharpened STATE line) is the one in `/mnt/user-data/outputs/` from this session's earlier deposit — please replace the copy in the working tree. (iii) M5_2 was not uploaded; both of its exported facts used here (C_CRIT; the L = 47 peak) are independently confirmed, so nothing in this note depends on trusting it.

Suggested STATE.md lines (owner to paste):
> M5/Tier-2 — pins reduced to two scalar lemmas (AUDIT_OP1_m5_lemmas_2026-06-12.md): B-form pin found asymptotically false (crossing x ≈ 9.8·10³), replaced by C-form C_L ≤ 1/28 (exact reduction ⇒ N\*_C ≥ 8, N\* ≥ 7 uniform); finite certificate every integer L ≤ 4096 verified; Lemma A: Claim 1 PROVED + continuum core PROVED (margins 0.904/0.149), lattice bridge remaining (toolset listed); Lemma B: reduced to C∞ = 0.0127921031 ≤ 1/28, monotonicity gated (D′ > 0, min 2.6·10⁻³), elementary write-up flagged; envelope constant at C∞ gives Tbar = 0.11692.

## 9. Files, gates, reproduction

`ENGINE_OP1_m5_audit.py` (G-M1 C_CRIT bisection + rational 1/28; G-M2 B-form divergence; G-M3 ratio-based Lemma-A adversarial scan; G-M4 Claim 1; G-M5 continuum core two-region; G-M6 independent C_inf; G-M7 finite-vs-infinite domination + C_L profile; G-M8 D′ sign), `AUDIT_OP1_m5.json`. Reproduce: `python3 ENGINE_OP1_m5_audit.py` with `/mnt/user-data/uploads/ENGINE_OP1_m4_tc_closed_form.py` importable. Dependencies: numpy, scipy. MD5s in the session message.
