# LEMMA B (M5 / Tier-2 C-form pin) — PROOF

**Date:** June 12, 2026 (late session, pass F031)
**Author:** session agent (lead math agent, DECISIONS #009), continuing F030 §4 and the M5 batch
**Status: PROVED** — derived and machine-certified. Every inequality below is either fully elementary or evaluated in **exact rational arithmetic with directed rounding**; the only non-self-contained inputs are cited intervals for the classical constants π and γ_E (gate LB5) and the already-triple-verified C-form envelope reduction (cited, not re-proved).
**Engine:** `numerics/op12_theta/m4_scaling/ENGINE_OP1_lemma_b_cert.py` → `LEM_OP1_lemma_b_cert.json`, gates **LB0–LB9 ALL PASS** (June 12, 2026; certificate part 0.7 s, full run 2.6 s).

---

## 0. Statement

**Theorem (Lemma B).** On the AF diagonal (L = 4eˣ, β(x) = 28/5 + (11/8π²)x, μ²(x) = 48/(β(x)L²), x ≥ 0):

> C_inf(x) ≤ **G_BOUND = 0.018664535031…** < **1/28** for every x ≥ 0,

where C_inf(x) = Y_inf(μ²(x)) − A·x − (A/2)·ln β(x), Y_inf(μ²) = (3/4)∫₀^∞ t e^{−μ²t} q(t)⁴ dt, q(t) = e^{−2t}I₀(2t), A = 3/(32π²).

**Corollary (with the C-form reduction, cited).** Via the exact envelope reduction T_C ≤ max_{x≥0} 36(Ax + (A/2)ln β + C)/β² — independently verified twice (m5_audit G-M1; F030 Q4/Q5) — and conditional on **Lemma A** (cover domination Φ_L⁴ − L⁻⁴ ≤ q⁴, which transfers C_L ≤ C_inf(x_L)):

> T_C(L) ≤ T̄(1/28) = 0.124806 < 1/8, hence **N\*_C ≥ 8, T_full < 9/64, N\* ≥ 7, for every integer L ≥ 4 on the diagonal.**

Lemma B was the constant-side half of the two-lemma split (F030 §1); it is now closed. The pin's sole remaining input is Lemma A (open only on the compact window τ = t/L² ∈ (0, 0.4] per the Region-A theorem of `AUDIT_OP1_m5_4_region_2026-06-12.md` §2, intake under review — see F031).

**Route.** This is the no-monotonicity route predicted in F030 §4, sharpened: dropping e^{−μ²t} ≤ 1 on the head makes the head cost *zero* (not 0.008); the ±(A/2)ln μ² terms cancel *exactly* between the E₁ expansion and the definition of g; and only the **upper** half of the Bessel two-sided bound is ever needed. The flagged monotonicity write-up (M5_AUDIT §6: D′ > 0, r > 1 beyond 0.15) is **not needed** for the pin; if proved later it sharpens G_BOUND to C∞ = 0.0127921 but changes no conclusion.

---

## 1. Preliminaries (all elementary)

**(1.1) Integral representation.** q(t) = (1/π)∫₀^π e^{−2t(1−cos θ)} dθ. *Proof:* expand e^{z cos θ} (z = 2t) in powers; odd powers of cos integrate to 0 on [0, π] (symmetry about π/2); even: (1/π)∫₀^π cos^{2k}θ dθ = C(2k,k)/4ᵏ (Wallis); and C(2k,k)/(4ᵏ(2k)!) = 1/(4ᵏ(k!)²) reproduces the I₀ series Σ (z/2)^{2k}/(k!)². Multiplying by e^{−z} gives the claim. Hence 0 < q ≤ 1 and **q is strictly decreasing**: q′(t) = −(2/π)∫₀^π (1−cosθ) e^{−2t(1−cosθ)} dθ < 0.

**(1.2) Notation.** c := 1/(16π²); A = (3/2)c, so **(3/4)c = A/2** exactly. r(t) := √(4πt)·q(t), so that t q⁴ = (c/t)·r⁴ identically.

**(1.3) Diagonal identity and the one-variable reduction.** μ² = 48/(βL²) = 3/(βe^{2x}) gives ln(1/μ²) = ln β + 2x − ln 3, hence A·x + (A/2)ln β = (A/2)(ln(1/μ²) + ln 3) **exactly**, and

  C_inf(x) = g(μ²(x)), g(μ²) := Y_inf(μ²) − (A/2)·ln(3/μ²).

**(1.4) Range.** β(x) ≥ 28/5 and e^{2x} ≥ 1 give μ² ∈ (0, **15/28**], with μ²(0) = 3·5/28 = 15/28 exactly (gate LB0; β increasing and e^{2x} increasing make μ² strictly decreasing in x, though only the range bound is used). So Lemma B is the one-variable statement: **g(μ²) ≤ G_BOUND < 1/28 on (0, 15/28]**.

---

## 2. The master bound

**Lemma E.** For all z > 0: 0 ≤ E₁(z) + γ + ln z ≤ z, where E₁(z) = ∫_z^∞ s⁻¹e^{−s}ds.
*Proof.* φ(z) := E₁(z) + ln z has φ′(z) = (1 − e^{−z})/z ∈ (0, 1), and φ(z) → −γ as z → 0⁺ (the classical limit, equivalent to γ's integral definition; cited). Hence φ(z) + γ = ∫₀^z (1−e^{−s})/s ds ∈ [0, z] since 0 ≤ 1−e^{−s} ≤ s. ∎ (Numerically spot-verified across the used range, gate LB0b.)

**Proposition (master bound).** For every T0 > 0 and every μ² ∈ (0, M], M := 15/28:

  **g(μ²) ≤ (3/4)·H(T0) + (A/2)·[ R⁺(T0) + M·T0 − γ − ln(3T0) ]**

with H(T0) := ∫₀^{T0} t q⁴ dt and R⁺(T0) := ∫_{T0}^∞ (r⁴−1)⁺ dt/t.

*Proof.* Write (4/3)Y_inf(μ²) = ∫₀^{T0} t e^{−μ²t} q⁴ dt + ∫_{T0}^∞ e^{−μ²t}(c/t) dt + ∫_{T0}^∞ e^{−μ²t}(c/t)(r⁴−1) dt, using t q⁴ = (c/t)r⁴ (1.2); each piece converges absolutely (q ≤ 1; §3 bounds |r⁴−1| ≤ const/t on [T0,∞)). Then:
(i) head: e^{−μ²t} ≤ 1 and the integrand is ≥ 0, so the first piece is ≤ H(T0) — *the head costs nothing*;
(ii) middle: exactly c·E₁(μ²T0) (substitute s = μ²t);
(iii) tail: e^{−μ²t}(c/t)(r⁴−1) ≤ (c/t)(r⁴−1)⁺ pointwise (whatever the sign of r⁴−1), so the third piece is ≤ c·R⁺(T0) — *no lower bound on r is needed anywhere*.
By Lemma E, c·E₁(μ²T0) ≤ c(−γ − ln T0 + μ²T0) + c·ln(1/μ²). Multiply the three bounds by 3/4, use (3/4)c = A/2, and subtract (A/2)ln(3/μ²) = (A/2)ln 3 − (A/2)ln(1/μ²)·(−1): the **(A/2)ln(1/μ²) terms cancel exactly**, leaving g(μ²) ≤ (3/4)H(T0) + (A/2)[R⁺(T0) − γ − ln T0 + μ²T0 − ln 3]. Bound μ²T0 ≤ M·T0. ∎

We take **T0 = 2**, so M·T0 = 15/14 and ln(3T0) = ln 6. All μ²-dependence has been absorbed into the single term (A/2)·15/14 = 0.005089…, which is the dominant cost of the bound's uniformity (see §5 sanity decomposition).

---

## 3. The Bessel upper bound (the single analytic input)

**Proposition.** For all t ≥ 4: **r(t) ≤ 1 + 1/(16t) + C₂/t²**, with C₂ = 2311/10000.

*Proof.* Substituting θ = 2 arcsin u in (1.1) (1−cosθ = 2u², dθ = 2du/√(1−u²)):

  q(t) = (2/π)∫₀¹ e^{−4tu²}(1−u²)^{−1/2} du.

Split at b = 4/5.
**(a) On [0, b]:** with v = u², Taylor–Lagrange for f(v) = (1−v)^{−1/2} (f″(v) = (3/4)(1−v)^{−5/2}) gives (1−u²)^{−1/2} = 1 + u²/2 + (3/8)(1−ξ)^{−5/2}u⁴ for some ξ ∈ (0, u²) ⊂ (0, b²), hence ≤ 1 + u²/2 + κu⁴ with **κ = (3/8)(1−b²)^{−5/2} = (3/8)(5/3)⁵ = 3125/648** (exact rational).
**(b) On [b, 1]:** e^{−4tu²} ≤ e^{−4tb²} and (2/π)∫_b¹(1−u²)^{−1/2}du = 1 − (2/π)arcsin b ≤ 1.
**(c)** Extend the [0, b] integral to [0, ∞) (positive integrand, upper bound) and use the Gaussian moments ∫₀^∞ e^{−4tu²}{1, u², u⁴} du = √π·{1/(4√t), 1/(32t^{3/2}), 3/(256t^{5/2})}:

  q(t) ≤ (2/√π)[1/(4√t) + 1/(64t^{3/2}) + 3κ/(256t^{5/2})] + e^{−(64/25)t}.

**(d)** Multiply by √(4πt) = 2√(πt):

  r(t) ≤ 1 + 1/(16t) + (3κ/64)/t² + 2√(πt)·e^{−(64/25)t}, 3κ/64 = **9375/41472** = 0.226056….

**(e) Wrap term.** ψ(t) := 2√(πt)·t²·e^{−(64/25)t} has (ln ψ)′ = 5/(2t) − 64/25 < 0 for t ≥ 4 (since 5/(2t) ≤ 5/8 < 64/25; integers: 125 < 512), so ψ is decreasing there, and at t = 4 the exact-rational check (gate LB6/wrap, directed rounding: √π ≤ 17724539/10⁷, e^{−256/25} ≤ 1/S₈₀(256/25))

  ψ(4) = 64√π·e^{−256/25} ≤ 4.06·10⁻³ < C₂ − 9375/41472 = 2091792/414720000 = 5.044·10⁻³

gives 2√(πt)e^{−(64/25)t} ≤ (C₂ − 9375/41472)/t² for all t ≥ 4. Combining (d)+(e) proves the Proposition. ∎

*Validity cross-check (gate LB2):* the bound vs high-precision r(t) on a 500-point grid spanning [4, 2·10⁴]: min slack +5.4·10⁻¹⁰ at the far end — positive everywhere, decaying like (C₂ − 9/512)/t² exactly as the true expansion r = 1 + 1/(16t) + (9/512)/t² + O(t⁻³) predicts. The grid is consistency; the proof above is the warrant.

*Remark.* Only this **upper** bound is used. F030 §4 asked for two-sided control; the master bound's (·)⁺ structure halves the requirement.

---

## 4. Certified evaluation of H(2) and R⁺(2)

All quantities below are computed in **exact rational arithmetic** (Python `fractions`), with directed rounding at the two cited constants. Series brackets: q(a) ≤ q⁺(a) := I₀⁺(2a)·exp⁺(−2a), where I₀⁺ = 28-term partial sum + geometric tail (term ratio a²/(K+1)² < 1) and exp⁺(−2a) = 1/S₆₀(2a) using e^x ≥ S_n(x) for x ≥ 0. Bracket validity and width ≤ 1.3·10⁻³² rel — gate LB1.

**(4.1) H(2) ≤ H_cert = 0.0317596977….** q decreasing (1.1) gives ∫_a^b t q⁴ dt ≤ q(a)⁴(b²−a²)/2 per cell; 256 uniform cells on [0, 2]. True value 0.0311718… (LB3); certified excess 5.9·10⁻⁴.

**(4.2) R⁺(2) ≤ R_cert = 0.2121034….** Two pieces:
- **[2, 4]:** 32 cells; on [a, b]: (r⁴−1)⁺ ≤ (16π²₊·b²·q⁺(a)⁴ − 1)⁺ (note r⁴ = 16π²t²q⁴ — only π² enters, no square roots) and ∫_a^b dt/t ≤ (b−a)/a (from ln(1+x) ≤ x). Sum: 0.1122218….
- **[4, ∞):** by §3, r⁴ − 1 ≤ (1+δ(t))⁴ − 1 ≤ 4δ(t)(1+δ(4))³ with δ(t) := 1/(16t) + C₂/t² (decreasing), and ∫₄^∞ δ(t) dt/t = 1/64 + C₂/32 in closed form. Piece: 4(1+δ(4))³(1/64 + C₂/32) = 0.0998824….

Numeric truth of R⁺(2) is 0.1395 (LB4); the certified excess (≈0.073) costs only (A/2)·0.073 ≈ 3.5·10⁻⁴ in the final bound — deliberately generous cells, the budget is wide.

---

## 5. Assembly and result

With γ ≥ γ₋ = 0.5772156649015328 (cited interval; LB5), ln 6 ≥ ln6₋ (rational bracket via ln 6 = 4 atanh(1/3) + 2 atanh(1/5), positive series + geometric tail; width < 10⁻⁴¹; LB5), and A/2 = 3/(64π²) ∈ [(3/64)/π²₊, (3/64)/π²₋]:

  X̄ = R_cert + 15/14 − γ₋ − ln6₋ = **−1.0854434…** < 0,
  (A/2)₋ · X̄ = **−0.0051552…** (directed: negative bracket × lower factor),
  **G_BOUND = (3/4)·H_cert + (A/2)₋·X̄ = 0.018664535031… < 1/28 = 0.035714285714…**

Margin **0.0170497507** (ratio 1.91), gate LB6, exact rational comparison. This proves the Theorem; the Corollary follows from the cited C-form reduction. ∎

**Sanity decomposition (why the bound sits where it does).** G_BOUND − C∞ = 0.018665 − 0.012792 = 0.005872, and indeed: (A/2)(15/14) = 0.005089 [the uniformity cost — the only term that remembers μ² > 0] + (3/4)(H excess) = 4.4·10⁻⁴ + (A/2)(R⁺ excess) = 3.5·10⁻⁴, total 0.005880 — matching gate LB8's measured minimal end-to-end slack 0.005884 at μ² = 0.001 to three digits. The bound is tight exactly where it should be, and end-to-end float verification confirms g(μ²) ≤ G_BOUND across (0, 15/28] (10-point grid, LB8) with the deposited C_inf reference rows reproduced to 9.6·10⁻¹² (LB7).

---

## 6. Remarks and status

**(a) What is and is not cited.** Self-contained: everything in §§1–4 except (i) the classical limit defining γ (Lemma E) and the numeric intervals for π, γ_E — both gate-checked against 60-digit values (LB5); (ii) the C-form envelope reduction and its threshold T̄(1/28) = 0.124806 — cited from m5_audit G-M1, independently re-verified by F030 Q4/Q5 (two engines, 1.4·10⁻¹² agreement). The constant 1/28 < C_CRIT = 0.0362419 is the clean rational sub-critical threshold introduced by the M5 audit note.

**(b) Relation to the monotonicity route.** M5_AUDIT_AND_LEMMAS §6 reduced Lemma B to "C∞ ≤ 1/28 + a flagged one-page monotonicity write-up" (D′(μ²) > 0, needing r(t) > 1 for t ≥ 0.15). That route is now **unnecessary** for the pin: this proof needs no monotonicity, no lower Bessel bound, and no certified value of C∞. If the monotonicity page is ever written, it upgrades G_BOUND to the sharp sup C∞ = 0.0127921031464 (pinned three ways to 1.4·10⁻¹³, M5_4 audit G-A5) — a cosmetic improvement; every downstream conclusion is identical.

**(c) Tier-2 pin status after this note.** Lemma B **PROVED** (this note). Lemma A: Claim 1 + continuum core + Region A (t ≥ 0.4L²) carry proofs in the session-P notes (`M5_AUDIT_AND_LEMMAS`, `M5_4_AUDIT_AND_REGION_A`, intake F031 — **not yet independently reviewed**); the compact window τ ∈ (0, 0.4] is the sole remaining open item on the A side. Once Lemma A closes, N\*_C ≥ 8 / N\* ≥ 7 become unconditional on the diagonal.

**(d) Master-doc upgrade.** The M5 docx (§4) pins C\*∞ < 0.013 by "rigorous numerical upper pin (M5.4 residual-integral audit)". This note **replaces the numerical pin with a proof** at the weaker-but-proved constant 0.018665 < 1/28; the docx's conditional structure (its §2 heat-kernel refinement input ≡ Lemma A) is unchanged.

**(e) Reproduction.** `python3 ENGINE_OP1_lemma_b_cert.py` (modes: `cert` = pure-rational LB0/LB6, `float` = validation gates; dependency: mpmath only). Engine + json deposited beside the other m4_scaling engines; gate list in the engine docstring.

**Grounds ledger:** §§1–5 derived-and-machine-certified (exact rational chain; gate run cited). §3 validity additionally float-cross-checked (LB2). §6(c) status claims rest on the cited findings; the session-P proof claims are labeled not-yet-reviewed. No conjecture-grade content in this note.
