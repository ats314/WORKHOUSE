# LEMMA B PROOF — INDEPENDENT REVIEW

**Date:** June 12, 2026 (this session = "session-P" in the F031 ledger)
**Reviewer:** lead math agent (DECISIONS #009), session-P
**Object under review:** `LEM_OP1_lemma_b_proof_2026-06-12.md` + `ENGINE_OP1_lemma_b_cert.py` (pass F031, parallel session)
**Review engines (this note):** `ENGINE_OP1_lemma_b_cert.py` rerun (this container) + `ENGINE_Y6_lemma_b_review_checks.py` → `LEM_MISC_lemma_b_review_checks.json`, gates **LR2–LR5 ALL PASS**

---

## 1. Verdict

**PROOF CONFIRMED. Lemma B is PROVED and now independently reviewed.**

For all μ² ∈ (0, 15/28]:  g(μ²) = Y_inf(μ²) − (A/2)ln(3/μ²) ≤ G_BOUND = 0.018664535031… < 1/28,
hence C_inf(x) < 1/28 for all x ≥ 0 on the AF diagonal. Every analytic step checks by hand; the
certified rational chain reruns identically in this container; four reviewer-side gates with a
structurally independent implementation confirm the bound, the master-bound proposition itself,
and the two delicate links (§3 wrap absorption, far-field Bessel validity). No errors found.
Four nits, none affecting validity (§5).

With the cited C-form envelope reduction (m5_audit G-M1, independently re-verified by their F030
Q4/Q5), the Tier-2 pin T_C ≤ T̄(1/28) = 0.124806 < 1/8 ⇒ N\*_C ≥ 8, T_full < 9/64, N\* ≥ 7 is now
**conditional on Lemma A only** (compact window τ ∈ (0, 0.4]; Region A is covered by the theorem
in `AUDIT_OP1_m5_4_region_2026-06-12.md` §2).

---

## 2. Hand-verification record (every step of §§1–5 checked)

**§1 Preliminaries.**
- (1.1) Integral representation q(t) = (1/π)∫₀^π e^{−2t(1−cosθ)}dθ: Wallis/series argument correct;
  strict monotone decrease of q immediate from the representation. ✓
- (1.2) tq⁴ = (c/t)r⁴ identity: t·r⁴/(16π²t²) = r⁴/(16π²t). ✓  (3/4)c = A/2 exact. ✓
- (1.3) Diagonal identity **exact**: ln(1/μ²) = lnβ + 2x − ln3 ⇒ Ax + (A/2)lnβ = (A/2)(ln(1/μ²)+ln3),
  so C_inf(x) = g(μ²(x)) with no approximation. ✓
- (1.4) μ²(0) = 3/(28/5) = 15/28 exact; μ² strictly decreasing in x; range (0, 15/28]. ✓

**§2 Master bound.**
- Lemma E: φ(z) = E₁(z) + ln z, φ′ = (1−e^{−z})/z ∈ (0,1), φ(0⁺) = −γ (classical limit, cited and
  disclosed); 0 ≤ ∫₀^z(1−e^{−s})/s ds ≤ z since 0 ≤ 1−e^{−s} ≤ s. ✓
- Three-way split absolutely convergent (q ≤ 1 on the head; |r⁴−1| ≤ const/t on [T0,∞) by §3). ✓
- (i) Head: e^{−μ²t} ≤ 1 on a nonnegative integrand — head bounded by H(T0) at **zero cost**. ✓
- (ii) Middle: ∫_{T0}^∞ e^{−μ²t}(c/t)dt = c·E₁(μ²T0) by s = μ²t. ✓ exact.
- (iii) Tail (·)⁺ step checked **both signs pointwise**: if r⁴ ≥ 1, e^{−μ²t} ≤ 1 gives ≤ (c/t)(r⁴−1)⁺;
  if r⁴ < 1, LHS < 0 = (c/t)(r⁴−1)⁺. ✓ — this is the step that removes any need for a lower Bessel
  bound; legitimate and the key structural idea.
- Assembly: c·E₁(μ²T0) ≤ c[−γ − lnT0 + μ²T0] + c·ln(1/μ²); the ±(A/2)ln(1/μ²) terms **cancel
  exactly** against the definition of g; only +(A/2)μ²T0 ≤ (A/2)·M·T0 survives. ✓ With T0 = 2:
  M·T0 = 15/14, ln(3T0) = ln6. ✓ The Proposition is correct as stated.

**§3 Bessel upper bound (t ≥ 4).**
- Substitution θ = 2arcsin u: 1−cosθ = 2u², dθ = 2du/√(1−u²), limits 0→1. ✓
- (a) Taylor–Lagrange in v = u² for (1−v)^{−1/2}: f″(v) = (3/4)(1−v)^{−5/2}; remainder coefficient
  ≤ (3/8)(1−b²)^{−5/2} at b = 4/5: (9/25)^{−5/2} = (5/3)⁵ ⇒ **κ = 3125/648 exact**
  (3·3125/(8·243) = 9375/1944 = 3125/648). ✓
- (b) [b,1] piece: e^{−4tu²} ≤ e^{−(64/25)t}, measure factor (2/π)∫_b¹(1−u²)^{−1/2}du ≤ 1. ✓
- (c) Extension [0,b] → [0,∞) valid (positive integrand, upper bound — the polynomial bound is only
  needed on [0,b], where it was derived). Gaussian moments with a = 4t:
  √π·{1/(4√t), 1/(32t^{3/2}), 3/(256t^{5/2})}. ✓ all three recomputed.
- (d) ×2√(πt): r ≤ 1 + 1/(16t) + (3κ/64)/t² + 2√(πt)e^{−(64/25)t}; 3κ/64 = 9375/41472. ✓
- (e) Wrap absorption: (lnψ)′ = 5/(2t) − 64/25 < 0 for t ≥ 4 (125 < 512 ✓); at t = 4:
  ψ(4) = 64√π·e^{−10.24} = 4.0512·10⁻³ < dC = C₂ − 9375/41472 = 2091792/414720000 = 5.0439·10⁻³
  (rational cross-multiplication of dC recomputed: 2311·41472 − 9375·10000 = 95,841,792 − 93,750,000
  = 2,091,792 ✓). Directed rounding in the rational check correct: √π ≤ 17724539/10⁷ (upper),
  e^{−x} ≤ 1/S_n(x) (upper). ✓ **Tightest analytic link in the proof — ratio 1.245** (see LR5);
  valid with room.

**§4 Certified evaluation.**
- q⁺ = I₀⁺·exp⁺ brackets: I₀ series tail geometrically dominated (term ratio t²/(k+1)² decreasing,
  valid for t² < (K+1)², here 16 < 841); e^{−x} ≤ 1/S_n(x) from e^x ≥ S_n(x). ✓ true upper bounds.
- H cells: q decreasing ⇒ ∫_a^b tq⁴ ≤ q(a)⁴(b²−a²)/2. ✓
- R[2,4] cells: r⁴ = 16π²t²q⁴ ≤ 16π²₊b²q⁺(a)⁴ (π² upper, t ≤ b, q ≤ q(a)); ln(b/a) ≤ (b−a)/a. ✓
  **Cell-skip logic checked**: if the cell's r⁴ upper bound ≤ 1, then r⁴ − 1 ≤ 0 on the whole cell
  ⇒ (r⁴−1)⁺ ≡ 0 there — skipping is valid, not an omission. ✓
- R[4,∞): r⁴−1 ≤ (1+δ)⁴−1 ≤ 4δ(t)(1+δ(4))³ with δ decreasing; ∫₄^∞ δ(t)dt/t = 1/64 + C₂/32
  **closed form recomputed**: ∫₄^∞[1/(16t²) + C₂/t³]dt = 1/64 + C₂/32. ✓ δ(4) = 1/64 + C₂/16. ✓

**§5 Assembly — directed rounding directions all verified.**
- X = R⁺ + μ²T0 − γ − ln6 ≤ X̄ = R_cert + 15/14 − γ₋ − ln6₋ (each replacement increases). ✓
- X̄ < 0 asserted **before** the multiplication, then (A/2)·X̄ ≤ (A/2)₋·X̄ since A/2 ≥ (A/2)₋ and
  X̄ < 0 — engine uses A2_LO = (3/64)/π²₊, the correct direction for a negative bracket. ✓
- G_BOUND = (3/4)H_cert + (A/2)₋X̄ is a true upper bound for g on the whole range; exact-rational
  comparison to 1/28. ✓
- Sanity decomposition: uniformity cost (A/2)(15/14) = 0.005089 + (3/4)·(H excess) ≈ 4.4·10⁻⁴
  + (A/2)·(R⁺ excess) ≈ 3.5·10⁻⁴ ≈ 0.005880 vs measured min end-to-end slack 0.005884 (LB8) /
  0.005873 (LR2). ✓ internally consistent to three digits.

---

## 3. Engine rerun (this container)

`python3 ENGINE_OP1_lemma_b_cert.py all` (engine reconstructed byte-faithful from the delivered document; it
was not on disk in this session): **ALL GATES PASS in 4.3 s**, every reported number identical to
the proof note —

| gate | result |
|---|---|
| LB0/LB0b | exact structure, diagonal identity, Lemma E ✓ |
| LB1 | q⁺ brackets valid; worst rel width **1.26·10⁻³²** |
| LB2 | Bessel bound on [4, 2·10⁴]; min slack 5.404·10⁻¹⁰ at t = 19877 (far end, as predicted) |
| LB3 | H_true = 0.031171809, H_cert = 0.031759698 (excess 5.88·10⁻⁴) |
| LB4 | R⁺ numeric [2,600] = 0.139501, R_cert = 0.212103 |
| LB5 | π/γ intervals + ln6 bracket ✓ |
| LB6 | **G_BOUND = 0.018664535031 < 1/28; margin 0.017049750683 (ratio 1.9135)** |
| LB7 | C_inf reference rows reproduced, worst dev 9.64·10⁻¹² |
| LB8 | g ≤ G_BOUND on 10-pt grid; min slack 0.005884 at μ² = 0.001 |

Rerun record: `LEM_MISC_lemma_b_cert_rerun.json` (deposited).

---

## 4. Independent reviewer gates (LR2–LR5, ALL PASS)

- **LR2 — independent end-to-end.** g(μ²) ≤ G_BOUND on a fresh 10-point grid including the exact
  endpoint 15/28 and off-engine-grid points, computed with **my** Y_inf implementation (scipy
  quadrature, T0 = 24, second-order tail subtraction — structurally different code path from the
  engine's mpmath splitting). Min slack 0.005873 at μ² = 10⁻⁵. ✓
- **LR3 — master-bound integrity chain.** With TRUE (unrounded) H, R⁺, γ, ln6:
  g(μ²) ≤ RHS_true(μ²) ≤ RHS_true(15/28) = **0.017880806** ≤ G_BOUND = 0.018664535 at
  μ² ∈ {15/28, 0.1, 0.001}. This verifies the **Proposition itself pointwise**, not merely the
  certified assembly; the 7.8·10⁻⁴ gap between RHS_true(M) and G_BOUND equals the deliberate
  certificate excesses (H: 4.4·10⁻⁴, R⁺: 3.5·10⁻⁴). ✓
- **LR4 — Bessel far field.** Bound holds to t = 10⁵ (5× beyond LB2's grid); slack·t² → 0.21352,
  matching the asymptote C₂ − 9/512 = 0.21352 to five digits. The bound's t⁻² cushion is the full
  C₂ − 9/512 — **no crossing is possible at large t**; the t = 19877 minimum in LB2 is a grid-edge
  artifact of a monotonically *safe* decay, not a near-failure. ✓
- **LR5 — tightest link.** ψ(4) = 4.05116·10⁻³ < dC = 5.04387·10⁻³, safety ratio **1.245** —
  the narrowest analytic margin anywhere in the proof, confirmed valid. ✓

---

## 5. Nits (none affect validity)

1. **LB1 assert vs actuality.** The engine asserts worst relative bracket width ≤ 10⁻¹⁵; actual
   width is 1.26·10⁻³² (and the note correctly states ≤ 1.3·10⁻³²). The assert is merely loose.
2. **"LB9"** is bookkeeping only (runtime + json write) — no mathematical content; the docstring's
   "gates LB0–LB9" slightly oversells the count. Cosmetic.
3. **Wrap link headroom.** ψ(4) ≤ dC at ratio 1.245 is the proof's tightest step. Robust as is,
   but any future attempt to shrink C₂ below ≈ 0.2301 breaks this link first — worth knowing
   before anyone "optimizes" C₂. (For the record, C₂ could not go below 3κ/64 + ψ(4) ≈ 0.2301
   without restructuring the wrap absorption.)
4. **Lemma E's γ-limit** (φ(z) → −γ) is cited rather than derived; properly disclosed in their
   grounds ledger, and γ's numeric interval is gate-checked (LB5). Acceptable.

---

## 6. Supersession and consolidated Tier-2 status

**Supersession (my side).** `AUDIT_OP1_m5_lemmas_2026-06-12.md` §6 reduced Lemma B to
"C∞ ≤ 1/28 + flagged monotonicity write-up (D′ > 0)". That route is now **unnecessary for the
pin**: this proof needs no monotonicity, no lower Bessel bound, and no certified C∞. My gate G-M8
(D′ > 0 numerically, min 2.6·10⁻³) remains as supporting evidence for the *cosmetic* upgrade path
G_BOUND → C∞ = 0.0127921, nothing more. The flagged write-up is withdrawn from the critical path.

**Tier-2 pin ledger after this review:**

| item | status |
|---|---|
| C-form envelope reduction (T_C ≤ max 36(Ax+(A/2)lnβ+C)/β²) | PROVED, triple-verified (G-M1, F030 Q4/Q5) |
| Threshold T̄(1/28) = 0.124806 < 1/8 | exact-rational, gated both sessions |
| **Lemma B** (C_inf(x) < 1/28 ∀x ≥ 0) | **PROVED — this review confirms** (G_BOUND = 0.018665, margin ratio 1.91) |
| Lemma A, Region A (τ ≥ 0.4) | PROVED my side (`M5_4_AUDIT_AND_REGION_A` §2) — *their* intake F031, **not yet reviewed by them** |
| Lemma A, Claim 1 + continuum core | PROVED my side (`M5_AUDIT_AND_LEMMAS` §§3–4) — same mutual-review status |
| Lemma A, compact window τ ∈ (0, 0.4] | **OPEN — the sole remaining item.** Route on file: per-L box certificates (M5.6b machinery) for 4 ≤ L ≤ L₀ + uniform large-L via dispersion stratification; budget = uniform margin 0.0396 |

Once Lemma A's compact window closes (and the mutual reviews complete), **N\*_C ≥ 8 / N\* ≥ 7
become unconditional on the AF diagonal.**

**Mutual-review state.** This note discharges the review of their Lemma B. Symmetrically, their
F031 marks my Claim-1 / continuum-core / Region-A proofs as "intake, not yet independently
reviewed" — that review (theirs of mine) is the open bookkeeping item on the A side, alongside
the compact-window mathematics itself.

**Suggested STATE.md line:**
`2026-06-12: Lemma B PROVED + independently reviewed (G_BOUND=0.018665<1/28, margin ratio 1.91; ENGINE_OP1_lemma_b_cert.py rerun clean + LR2-LR5 pass). Tier-2 pin (N*_C>=8, N*>=7) now conditional on Lemma A compact window tau in (0,0.4] ONLY. Monotonicity write-up withdrawn from critical path (cosmetic upgrade only).`

---

## 7. Files (deposited this session)

- `LEM_O4_lemma_b_review_2026-06-12.md` — this note
- `ENGINE_Y6_lemma_b_review_checks.py` / `LEM_MISC_lemma_b_review_checks.json` — reviewer gates LR2–LR5
- `LEM_MISC_lemma_b_cert_rerun.json` — full gate output of `ENGINE_OP1_lemma_b_cert.py all` rerun in this container

**Grounds ledger:** §2 derived (hand verification of a delivered proof); §§3–4 machine-certified
in this container (gate runs cited); §6 status table rests on the cited session notes. The one
labeled-opinion item: nit 3's C₂ ≈ 0.2301 floor is a quick derived estimate (3κ/64 + ψ(4)), not
gate-backed — irrelevant to validity.
