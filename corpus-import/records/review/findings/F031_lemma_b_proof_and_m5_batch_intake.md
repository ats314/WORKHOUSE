# F031 — LEMMA B PROVED (certified no-monotonicity route) + session-P M5 batch intake (June 12, 2026, late night)

**Unit:** #52. **Verdict: the constant half of the M4 Tier-2 pin is CLOSED — Lemma B is now a theorem:** g(μ²) ≤ **G_BOUND = 0.018664535031 < 1/28** for all μ² ∈ (0, 15/28], hence C_inf(x) < 1/28 for every x ≥ 0 on the AF diagonal; combined with the triple-verified C-form reduction, **the uniform deterministic floors N\*_C ≥ 8 / N\* ≥ 7 are now conditional on Lemma A (cover domination) alone.** Proof: `programs/op1_defect_sparsity/LEM_OP1_lemma_b_proof_2026-06-12.md`; certificate `numerics/op12_theta/m4_scaling/ENGINE_OP1_lemma_b_cert.py` → `.json` — exact rational arithmetic end-to-end, gates **LB0–LB9 ALL PASS** (in-store cold run, 0.7 s certificate + 1.9 s validation). Secondarily: the **7 unprocessed session-P files** found in the uploads (same-day parallel-agent products the F029/F030 pass never reached) are deposited verbatim and their engines **cold-run verified on our stores — G-M1–G-M8 and G-A1–G-A6 ALL PASS, output jsons reproducing the uploads to ≤ 1 ULP**; their Lemma-A proof claims are **not yet independently reviewed** (ledger #53 opened).

## 1. The proof (what is new mathematically)

The route is F030 §4's no-monotonicity prediction, sharpened in three ways: (i) dropping e^{−μ²t} ≤ 1 on the head [0, T0] costs *zero* (not the sketched 0.008) because the head enters only as an upper bound; (ii) the ±(A/2)ln μ² terms cancel **exactly** between the E₁ extraction and the definition g = Y_inf − (A/2)ln(3/μ²) — the entire μ²-dependence of the final bound is one term (A/2)μ²T0 ≤ (A/2)(15/14) = 0.00509; (iii) only the **upper** half of the "two-sided Bessel bound" both prior notes called for is ever needed, via the (r⁴−1)⁺ structure. Single analytic input (proof note §3, fully elementary): **r(t) = √(4πt)·e^{−2t}I₀(2t) ≤ 1 + 1/(16t) + (2311/10⁴)/t² for t ≥ 4** — u-substitution of the I₀ integral representation, Taylor–Lagrange split at b = 4/5 (κ = (3/8)(5/3)⁵ = 3125/648 exact), Gaussian moments, and a wrap term killed by one rational check at t = 4 plus log-derivative monotonicity (125 < 512). Master bound (note §2, with Lemma E: 0 ≤ E₁(z)+γ+ln z ≤ z elementary):

  g(μ²) ≤ (3/4)H(2) + (A/2)[R⁺(2) + 15/14 − γ − ln 6],  H = ∫₀² tq⁴, R⁺ = ∫₂^∞(r⁴−1)⁺dt/t.

Certified pieces (exact rationals; directed rounding; π, γ_E cited intervals; ln 6 by atanh-series brackets): H_cert = 0.0317597 (true 0.0311718), R⁺_cert = 0.2121 (true 0.1395), assembly **G_BOUND = 0.018664535031**, margin to 1/28 = 0.0170498 (×1.91). Sanity: the bound's distance above the true sup C∞ = 0.0127921 decomposes as 0.00509 (μ²-uniformity term) + 0.00044 (H grid) + 0.00035 (R⁺ slack) = 0.00588, matching LB8's measured minimal end-to-end slack 0.005884 to three digits. **Monotonicity (the flagged one-page write-up of M5_AUDIT §6) is unnecessary**; if ever proved it sharpens the constant to C∞, cosmetically.

## 2. Batch intake — verdicts and provenance

Deposited verbatim (collision-checked, md5-verified at write time):

| File | Deposited at | md5 |
|---|---|---|
| ENGINE_OP1_m5_audit.py | numerics/op12_theta/m4_scaling/ | 170920cd77ca10c7f1c32fb444d657af |
| AUDIT_OP1_m5.json | same | f7733a664b9024f22ade14b19e8fc4c9 |
| ENGINE_OP1_m5b_region.py | same | 620dea26338bf60864e64811f920191f |
| CERT_OP1_m5b_region.json | same | e69d11a97f61c64279fb3973a3eaffac |
| M5_4_—_WARNING…ipynb → NB_OP1_m5_4_warning_free_limit_constant_audit.ipynb (ASCII-normalized) | same | 9abaa36689fd7752085be94e294149cd |
| AUDIT_OP1_m5_lemmas_2026-06-12.md | programs/op1_defect_sparsity/ | a471ef87f95f0901f38b2ae6546c3be7 |
| AUDIT_OP1_m5_4_region_2026-06-12.md | same | 5bd37af541f87ce12874459f12f9c711 |
| "M5 Deterministic Tier-2 Comparator Ceiling.docx" → PAPER_OP1_m5_deterministic_tier2_comparator_ceiling.docx | same | bfef9b0ca978be857cb2b391ecc3e228 |

New engine: ENGINE_OP1_lemma_b_cert.py md5 **81ec15b382a535b704931451387d5a0e** (deposited copy == run copy, verified).

**Cold runs (this pass, our stores).** Path shim only (single sed `/home/claude/` → run dir; `ENGINE_OP1_m4_tc_closed_form.py` import satisfied from our m4_scaling deposit; m5b reads m5_audit's json for G-A5): `ENGINE_OP1_m5_audit.py` **G-M1–G-M8 ALL PASS** (~40 s; C_CRIT independent bisection = 0.036241888089667; B-form crossing x = 9818.9; ratio-scan window max 0.991306 at (7, 0.496); Claim-1 scan; continuum-core grid h(1/8) = 0.903937; C∞ = 0.012792103146; C_L profile peak 0.0097790339 at L = 47; D′ min +2.574e-3 at μ² = 0.5357). `ENGINE_OP1_m5b_region.py` **G-A1–G-A6 ALL PASS** (h_A max 0.33925 at τ = 0.4 decreasing; R1/R2 slacks −3.2e-28/+2.1e-12; Region-A worst E_L = −9.9e-5 with proof-bound domination; bridge ratio max 1.4642 at τ = 0.085 [the falsification diagnostic]; C∞ reconciliation 1.39e-13; box certificate 0.980657081547 reproduced exactly, 6 boxes on [0.05, 0.4]). **Output jsons vs uploaded jsons: 27 + 17 common numeric keys, worst relative deviation 0 and 1.1e-16** — full reproduction.

**Master docx identified.** `M5 Deterministic Tier-2 Comparator Ceiling` = the program write-up: status header "conditional theorem / theorem with external heat-kernel input" — the input being Abelian heat-kernel refinement monotonicity (p_{T_L}(t,0,0) − L^{−d} decreasing under torus refinement), which after the M → ∞ cover limit **is exactly Lemma A**; its §4 pins the constant by "M5.4 residual-integral audit … rigorous numerical upper pin C\*∞ < 0.013". **This pass replaces that numerical pin with a proof** (weaker constant 0.018665, sufficient: < 1/28); nothing else in the docx is affected. (Display-math note: OMML equations partially invisible to plain-text extraction — content cross-checked against the md notes, which carry it; not the F026 stripped-export pathology as far as the checked sections go, but a full equation-level read was not performed.)

## 3. What was NOT verified this pass (honest boundary)

The session-P notes' **Lemma-A proof claims**: Claim 1 (Φ_L ≤ 1/L + q, M5_AUDIT §3), the continuum core G(c) < 1 (two proofs: analytic two-region §4; M5.6b 80-digit box certificate), the **Region-A theorem** (t ≥ 0.4L², all L ≥ 4, M5_4 note §2 with Lemmas R1/R2), and the compact-window route assessment (§3). Their gates pass cold on our stores — that is *evidence of reproducibility, not independent review* (the same distinction F030 drew for M5.1). Line-by-line review = **ledger #53**, and its outcome decides whether the A-side open window is τ ∈ (0, 0.4] (Region A stands) or all of (0, ∞) (it does not). The B-form-falsity finding (their F1) needed no new review: it is F028's own quantifier measurement, independently restated; the C-form reduction and 1/28 threshold were already double-verified (F030 Q4/Q5 + their G-M1, re-run here).

## 4. Status changes

(1) **Lemma B: OPEN → PROVED** (no conditions; two cited classical constants). (2) Tier-2 uniform floors: conditional on (Lemma A + Lemma B) → **conditional on Lemma A alone**. (3) The M5 docx's constant-side input upgraded from audit-grade to theorem (weaker constant, same conclusion). (4) The monotonicity item (M5_AUDIT §6 flagged page, G-M8) reclassified: pin-irrelevant, refinement-only. (5) New citable constant with a quoting rule (CONVENTIONS row): **G_BOUND = 0.018664535031 is the *proved* envelope; C_sat = 0.0127921031 the *measured* sup** — quote the right one for the claim being made. (6) A-side: open window τ ∈ (0, 0.4] *conditional on #53*; M5.8's uniform numeric margin there (|E_L| ≥ 0.0396, worst point at the τ = 0.4 junction) is the budget the per-L box route must beat.

## 5. Files, gates, reproduction; incidents

This pass deposits: the proof note, ENGINE_OP1_lemma_b_cert.py/.json (run `python3 ENGINE_OP1_lemma_b_cert.py` — modes cert/float/all; mpmath only), the 8 intake files above, ledger rows #52 DONE/#53 PENDING, UNIF plan M4 ADDENDUM 3d, OPEN_PROBLEMS OP-1 Addendum 7, CONVENTIONS G_BOUND row, both READMEs, MANIFEST (82 files), STATE, SESSION_LOG. Incidents (all handled, details SESSION_LOG): outputs-mount truncated-snapshot sync of the engine mid-session (repaired; deposited == run copy by md5); container-scoped background jobs (cold runs redone foreground-chunked); a pkill self-match (no damage). Grounds: §1 derived-and-machine-certified (exact-rational chain; LB gates); §2 machine-verified reproduction + provenance; §3–4 status assessments, labeled; nothing heuristic presented as more.
