# LEMMA A (cover domination) — CLOSURE OF THE COMPACT WINDOW

**Date:** June 12, 2026 (late night, pass F033; directly after the F032 review)
**Author:** session agent (lead math agent, DECISIONS #009)
**Status: PROVED — modulo the gate run** `numerics/op12_theta/m4_scaling/ENGINE_OP1_lemma_window_cert.py` (gates WB0–WB5; see §8 for the exact grounds split: the structural lemmas are paper-proofs below; the finitely many numerical inequalities they reduce to are machine-certified with directed padding).
**Companions:** Region-A theorem + continuum core + Claim 1 (session-P notes, reviewed-proved F032); Lemma B (proved F031).

---

## 0. Statement and consequence

**Theorem (Lemma A, full).** For every integer L ≥ 4 and every t > 0:

> Φ_L(t)⁴ − L⁻⁴ ≤ q(t)⁴,  Φ_L(t) = (1/L)Σ_{n=0}^{L−1} e^{−4t sin²(πn/L)}, q(t) = e^{−2t}I₀(2t).

**Corollary (unconditional Tier-2 floors).** Integrating Lemma A against t e^{−μ²t} gives T_C(L) ≤ Y_inf(μ²_L)/α_W² (the M5.3 reduction, verified G-M6/G-M7/Q1–Q2), so C_L ≤ C_inf(x_L); by **Lemma B** (F031) C_inf < 1/28; by the **C-form envelope reduction** (G-M1, triple-verified) T_C(L) ≤ T̄(1/28) = 0.124806 < 1/8. Hence, in the OP-12 comparator frame (m₀² = ½, v₀ = 1, Casimir convention, AF diagonal L = 4eˣ, β = 28/5 + (11/8π²)x):

> **N\*_C ≥ 8 and (with T_H = 1/(m₀⁴L⁴) ≤ 1/64) T_full < 9/64, so N\* ≥ 7 — for every integer L ≥ 4 on the diagonal, UNCONDITIONALLY.**

Both former Tier-2 pins are removed. Scope honesty: this closes the *deterministic comparator ceiling* — it does not advance (S), CONJ_B, or any continuum statement (the master docx's scope clause is unchanged; its two external inputs are now both theorems).

**Decomposition of the proof.** Region A (t ≥ 0.4L²) was proved by session-P and reviewed in F032. Here: (§2) the Region-A argument *extends* to t ≥ 0.31L²; (§5) a uniform theorem covers L ≥ 12, τ = t/L² ∈ (0, 0.31]; (§6) per-L certificates cover L = 4..11 on the same window. Together with Region A-ext these tile {L ≥ 4} × (0, ∞).

---

## 1. Toolkit (all elementary; gate WB0)

**(T1)** arcsinh w ≥ w/√(1+w²) for w ≥ 0 (derivatives: 1/√(1+w²) ≥ (1+w²)^{−3/2}).
**(T2)** Λ\*(v) := v·arcsinh(v/2) + 2 − √(4+v²) = ∫₀^v arcsinh(s/2) ds, so Λ\*′(v) = arcsinh(v/2), Λ\* is increasing and convex, Λ\*(0) = 0.
**(T3)** 2Λ\*(v) ≥ v·Λ\*′(v): g := 2Λ\* − vΛ\*′ has g(0) = 0 and g′ = Λ\*′ − vΛ\*″ = arcsinh(v/2) − (v/2)/√(1+v²/4) ≥ 0 by (T1).
**(T4)** E_m(τ, L) := τL²·Λ\*(m/(τL)) is **nondecreasing in L** at fixed (τ, m): ∂_L E_m = τL(2Λ\*(v) − vΛ\*′(v)) ≥ 0 by (T3), v = m/(τL). Likewise L·arcsinh(c/L) is nondecreasing in L (same inequality), so the geometric tail ratio in §5 improves with L.
**(T5)** Λ\*(mv) ≥ Λ\*(v) + (m−1)v·arcsinh(v/2) for m ≥ 1 (convexity + Λ\*′ increasing).
**(T6)** q is strictly decreasing (F031 §1.1), and Φ_L(t) = Σ_{j∈ℤ} e^{−2t}I_{jL}(2t) (DFT identity, used throughout the program).

**Lemma W (wrap bound; the new tool).** For every integer k ≥ 0 and t > 0:

> p_k(t) := e^{−2t}I_k(2t) ≤ e^{−tΛ\*(k/t)} · q(√(t² + k²/4)).

*Proof.* p_k(t) = (1/2π)∫_{−π}^{π} e^{−2t(1−cos ω)} e^{−ikω} dω. The integrand is entire in ω and 2π-periodic along the real direction, so the contour may be shifted to Im ω = −α, α ≥ 0 (Cauchy; the vertical segments at Re ω = ±π cancel by periodicity). On the shifted contour |e^{−ik(u−iα)}| = e^{−kα} and Re[1 − cos(u−iα)] = 1 − cosh α · cos u, hence
p_k ≤ e^{−kα} (1/2π)∫ e^{−2t(1−cosh α cos u)} du = e^{−kα + 2t(cosh α − 1)} · e^{−2t cosh α} I₀(2t cosh α).
Choosing sinh α = k/(2t) makes the exponent −tΛ\*(k/t) (the Legendre point) and t cosh α = √(t²+k²/4). ∎

Lemma W is prefactor-sharp: at k = 0 it is equality, and gate WB0 verifies p_k ≤ bound on an adversarial (k, t) grid (observed slack ≲ 1% in the regimes used — the bound loses only the curvature of the saddle).

**Lemma R⁺ (r ≥ 1 beyond t = 3).** r(t) := √(4πt)·q(t) ≥ 1 for all t ≥ 3.
*Proof.* In q = (1/π)∫₀^π e^{−2t(1−cosθ)}dθ use 1 − cosθ ≤ θ²/2 − θ⁴/24 + θ⁶/720 on [0, π] (alternating series, terms decreasing) and e^z ≥ 1+z with z = t(θ⁴/12 − θ⁶/360) ≥ 0 (θ² ≤ 30 on [0,π]):
q ≥ (1/π)∫₀^π e^{−tθ²}(1 + tθ⁴/12 − tθ⁶/360)dθ. Extend the (positive) 1- and θ⁴-integrals to [0,∞) minus explicit [π,∞) tails, and the (subtracted) θ⁶-integral to [0,∞) whole. Gaussian moments give, after multiplying by √(4πt):
r(t) ≥ 1 + 1/(16t) − 1/(384t²) − ε_tail(t), with ε_tail collecting the [π,∞) tails: ε_tail ≤ √(4πt)·[e^{−π²t}/(2π²t·…) + (t/12)·(e^{−π²t}/2π)(π⁴/t)(1 + 2/(π²t) + 2/(π⁴t²))]/π. For t ≥ 3, e^{−π²t} ≤ e^{−29.6} ≈ 1.4·10⁻¹³ makes ε_tail ≤ 10⁻¹⁰, while 1/(16t) − 1/(384t²) ≥ 1/(16t)·(1 − 1/(24t)) ≥ 0.0205 at t = 3. Hence r ≥ 1.020 > 1 for t ≥ 3 (gate WB0 pins the constants). ∎

**R_MAX (global cap).** r(t) ≤ R̄ := 1.19 for all t > 0: for t ≥ 4 by F031 (1 + 1/(16t) + 0.2311/t² ≤ 1.031); on (0, 4] by 600 directed cells r ≤ √(4πt_b)·q⁺(t_a) (gate WB0, worst cell 1.18105). The true sup is r ≈ 1.17511 near t ≈ 0.40 — *not* r(0.5) = 1.16748 as session messages had loosely said; the cell sweep caught this (F033 erratum). R̄ enters only the small-τ branch, whose margin is ×20.

---

## 2. Region-A extension: t ≥ 0.31·L² (gate WB1)

Re-run the (F032-verified) Region-A argument with τ₀ = 0.31 in place of 0.4. The three τ-dependent constants: tail factor 2(1 + e^{−48τ₀}/(1−e^{−80τ₀})) ≤ 2.0001 (e^{−14.88} = 3.4·10⁻⁷); e ≤ 2.0001·e^{−4.96} = 0.014027 so (1+e)³ ≤ 1.0427; erf(π√(0.31·16)) ≥ 1 − 10⁻²⁰. Then h_A2(τ) := 4·2.0001·1.0427·16π²·τ²e^{−16τ}/(1−10⁻²⁰) ≤ 1317.4·τ²e^{−16τ}, and h_A2(0.31) = **0.8879 < 1**, decreasing on [0.31, ∞) (τ²e^{−16τ} decreases past τ = 1/8). All other steps of the Region-A proof are τ₀-independent. **Theorem (Region A-ext): Φ_L⁴ − L⁻⁴ ≤ q⁴ for all integer L ≥ 4, t ≥ 0.31L².** (Purpose: the compact-side corner moves from τ = 0.4 — true margin ≈ 0.040 — to τ = 0.31, where the certified bounds below clear 1 by ≈ 5–6%.)

---

## 3. The certificate quantity

Fix L and τ ∈ (0, 0.31], t = τL². Write x = Lq(t), y = LΦ_L − Lq = 2LΣ_{m≥1}p_{mL}(t). The claim Φ_L⁴ − L⁻⁴ ≤ q⁴ is D := (x+y)⁴ − x⁴·… precisely: (LΦ_L)⁴ − 1 ≤ (Lq)⁴, i.e. **D := (x+y)⁴ − x⁴ ≤ 1**. By Lemma W and (T6) [q decreasing ⟹ q(√(t²+k²/4)) ≤ q(t)]:

> y/x ≤ Ȳ(τ, L) := 2 Σ_{m≥1} ρ_m(τ,L) e^{−E_m(τ,L)},  ρ_m := q(√(t²+m²L²/4))/q(t) ≤ 1,

with the m ≥ 4 tail dominated geometrically via (T5): step ratio ≤ e^{−L·arcsinh(3/(2τL))}. And with certified brackets r̲ ≤ r(t) ≤ r̄:

> **D ≤ min{ [ r̄⁴ (1+Ȳ)⁴ − r̲⁴ ] / (16π²τ²), 4Ȳ(1+Ȳ)³·r̄⁴/(16π²τ²) }.** (★)

(Both forms are valid upper bounds; each is essential in its regime. At the corner y ≈ x and the convexity form loses a factor ≈ 2 — exact-difference wins. At small τ, y is exponentially dead but the exact-difference form pays the *bracket width* r̄⁴ − r̲⁴ ≈ 4(r̄−1) divided by 16π²τ², which explodes — convexity wins, paying the width only ∝ Ȳ. The first engine draft used exact-difference alone and failed exactly there; the min-form is the certificate.)

## 4. Brackets used in (★)

r̄: for t ≥ 4, r̄ = 1 + 1/(16t) + 0.2311/t² (F031); for t ∈ (0, 4], per-cell √(4πt_b)q⁺(t_a). r̲: for t ≥ 3, r̲ = 1 (Lemma R⁺) in the uniform branch; per-cell √(4πt_a)q⁻(t_b) in the per-L branch (sharper). ρ_m: per-cell ≤ q⁺(√(t_a²+m²L²/4))/q⁻(t_b); in the uniform branch simply ρ_m ≤ 1 (the ratio is within 0.5% of 1 at L ≥ 12 — dropping it preserves validity and the L-monotonicity below).

## 5. Uniform theorem: L ≥ 12, τ ∈ (0, 0.31] (gates WB2–WB3)

**Monotonicity in L (the heart).** At fixed τ, each ingredient of the (★)-bound with ρ ≡ 1 is nonincreasing in L ≥ 12: e^{−E_m(τ,L)} by (T4); the tail ratio by (T4)'s second clause; r̄ = 1 + δ(τL²) since δ is decreasing; and r̲ = 1 is L-free, valid for all L ≥ 12, τ ≥ 3/144 by Lemma R⁺ (t = τL² ≥ 144τ ≥ 3). Hence

> sup_{L ≥ 12} D(L, τ) ≤ F(τ) := [ (1+δ(144τ))⁴ (1+Ȳ(τ,12))⁴ − 1 ] / (16π²τ²),

and it suffices to certify F(τ) ≤ 1 − margin on [3/144, 0.31]. Directed τ-cells [a,b]: numerator with δ(144a) (δ decreasing in τ) and Ȳ(b,12) (E_m decreasing in τ: ∂_τ E_m = L²(Λ\* − vΛ\*′) ≤ 0; tail ratio likewise worsens with τ), denominator 16π²a². Gate WB2 sweeps ~130 cells; representative values of F: 0.69 at τ = 1/8, 0.946 at the τ = 0.31 corner (the binding end), ≤ 0.05 below τ = 0.05.

**Small-τ branch, τ ≤ 3/144 (gate WB3).** Here wraps are dead and the crude form suffices: D ≤ 4Ȳ(1+Ȳ)³·R̄⁴/(16π²τ²) with Ȳ(τ,12) ≤ 2.1·e^{−E₁(τ,12)} (the m ≥ 2 tail is < 5% of m = 1 here). Dyadic cells [τ, 2τ] down to τ = 10⁻³ (E₁ decreasing in τ ⟹ e^{−E₁} at the right edge; 1/τ² at the left edge), then the analytic tail: Λ\*(v) ≥ v(arcsinh(v/2) − 1) for v ≥ 1 (√(4+v²) ≤ v + 2/v) gives E₁(τ,12) ≥ 12(ln(1/(12τ)) + ln 2·… ≥ 12(arcsinh(1/(24τ)) − 1), so e^{−E₁}/τ² ≤ (12e·τ)¹²/τ² = e¹²12¹²τ¹⁰ → 0 monotonically; at τ = 10⁻³ the whole bound is < 10⁻¹⁵. All L ≥ 12 are covered simultaneously by (T4).

## 6. Per-L certificates: L = 4..11, τ ∈ (0, 0.31] (gate WB4)

For each L separately, (★) with all four bracket refinements (r̄, r̲, ρ_m per-cell as in §4; exact E_m(τ, L); three explicit wrap terms + (T5)-geometric tail). Directed τ-cells on [τ_kill(L), 0.31]. Below τ_kill(L): the **head kill** — y ≤ 2L·(t^L/L!)e^{−2t+t²/(L+1)}(1 + geometric) [I_k(2t) ≤ (t^k/k!)e^{t²/(k+1)}, from the series], x+y ≤ L (Φ_L ≤ 1), so D ≤ 4y(x+y)³ ≤ 8L⁴(t^L/L!)e^{−2t+t²/(L+1)}(1+ε); the right side is increasing in t on (0, L/2) (log-derivative L/t − 2 + 2t/(L+1) > 0), so a single right-endpoint check at t_kill(L) certifies the whole head. t_kill chosen per L with the endpoint value ≤ 0.5 (e.g. t_kill(4) = 0.25). Representative certified margins (gate WB4): ≈ 5–8% at each L's binding cell (the τ = 0.31 corner for small L; τ ≈ 1/8 plays no role — the binding regime is the corner everywhere).

## 7. Assembly

Region A-ext (§2: τ ≥ 0.31, all L ≥ 4) ∪ Uniform (§5: L ≥ 12, τ ∈ (0, 0.31]) ∪ Per-L (§6: L = 4..11, τ ∈ (0, 0.31]) = {all integer L ≥ 4} × (0, ∞). **Lemma A is proved.** With F031 and the cited reductions, the Corollary of §0 follows. ∎

## 8. Grounds, sharpness, remarks

**Grounds.** §§1–3, 5-structure, 6-structure: paper-proofs (elementary; reviewed constants where they touch F032 material). The finitely many numerical inequalities (cell sweeps WB2–WB4, toolkit constants WB0–WB1) are machine-certified at mpmath dps 25 with directed padding 10⁻¹⁸ on every comparison — *not* exact-rational (unlike F031's certificate): the certificate involves thousands of transcendental evaluations; the padding is 16 orders below the certified margins (≥ 0.05). Gate WB5 additionally verifies bound-validity (★) ≥ true D on a random (L, τ) sample.

**Sharpness (certified values, gate run).** The corner τ = 0.31 binds everywhere: worst uniform cell F = 0.9550 (at [0.3085, 0.31]); worst per-L cells D = 0.9448–0.9494 (all at the corner; L = 4 the largest). Certified margins 4.5–5.5% against bound-to-truth gaps ≈ 1% (Lemma W's saddle-curvature price; WB5's tightest validity sample gap 1.3·10⁻⁸). Pushing τ₀ below ≈ 0.28 would need the next Λ\*-correction; unnecessary.

**Remarks.** (i) Lemma W is of independent use wherever the program needs wrap sums with sharp prefactors (e.g., OP-11 diagnostics). (ii) The proof consumes Lemma R⁺ — the *lower* Bessel bound the monotonicity route wanted (M5_AUDIT §6) — but only down to t = 3, where it is easy; the full r > 1 for t ≥ 0.15 remains unproved and unneeded. (iii) Everything is now in place for the master-doc upgrade: its "external heat-kernel input" header can cite this note + F032's review of Region A/core, and its §4 numerical pin cites F031.
