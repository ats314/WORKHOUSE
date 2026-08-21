# F033 — LEMMA A CLOSED (compact window certified) ⟹ Tier-2 floors UNCONDITIONAL (June 12, 2026, late night)

**Unit:** #54. **Verdict: Lemma A (cover domination Φ_L⁴ − L⁻⁴ ≤ q⁴, every integer L ≥ 4, every t > 0) is PROVED.** The compact window τ ∈ (0, 0.31] is closed by this pass's certificate; τ ≥ 0.31 by the Region-A extension (§2 of the note); both sit on the F032-reviewed session-P proofs. **Consequence, with Lemma B (F031) and the verified reductions: T_C ≤ T̄(1/28) = 0.124806 < 1/8, hence N\*_C ≥ 8, T_full < 9/64, N\* ≥ 7 — for every integer L ≥ 4 on the AF diagonal, UNCONDITIONALLY** (comparator frame: m₀² = ½, v₀ = 1, Casimir). Both former Tier-2 pins are removed; the master M5 docx's two external inputs are now both theorems. Scope honesty unchanged: deterministic comparator ceiling only — no claim on (S), CONJ_B, or the continuum.

**Proof note:** `programs/op1_defect_sparsity/LEM_OP1_lemma_closure_2026-06-12.md`. **Certificate:** `numerics/op12_theta/m4_scaling/ENGINE_OP1_lemma_window_cert.py` → `.json` — gates **WB0–WB5 ALL PASS** (in-store cold run 7.4 s; md5 69aa61e6 / cbc49a80; resumable; mpmath dps 25, directed padding 10⁻¹⁸ vs certified margins ≥ 4.5·10⁻²).

## 1. What is new mathematically

**(i) Lemma W (contour-shifted wrap bound):** p_k(t) = e^{−2t}I_k(2t) ≤ e^{−tΛ\*(k/t)}·q(√(t²+k²/4)) — one-line Cauchy shift of the Fourier representation; prefactor-sharp (equality at k = 0; observed slack ≲ 1% in use; gate WB0 validates against true p_k on an adversarial grid). This is the tool both prior notes lacked: Chernoff alone loses the √(4πt) prefactor, fatal mid-window. Independent utility wherever the program needs wrap sums (OP-11 diagnostics, future bridge work).
**(ii) Λ\*-toolkit:** 2Λ\*(v) ≥ vΛ\*′(v) (from arcsinh w ≥ w/√(1+w²)) ⟹ E_m(τ,L) = τL²Λ\*(m/(τL)) nondecreasing in L — the **monotonicity that turns one certified L₀ = 12 sweep into all L ≥ 12**.
**(iii) Lemma R⁺:** r(t) = √(4πt)q(t) ≥ 1 for t ≥ 3 (the F031 machinery run in the lower direction; tails crude since e^{−π²t} ≤ 10⁻¹³ there). Supplies the subtraction floor x ≥ 1/√(4πτ) uniformly in L. Notably: this is the *lower Bessel bound* the monotonicity route wanted (M5_AUDIT §6) — needed only at t ≥ 3, where it is easy; r > 1 on [0.15, 3) remains unproved and unneeded.
**(iv) Region-A extension to τ₀ = 0.31:** the session-P constants had room (h_A2(0.31) = 0.8879 < 1); moves the corner off τ = 0.4 (true margin 0.0396) to τ = 0.31 where the certificate clears by 4.5–5.5%.
**(v) The min-form certificate (★):** D ≤ min{exact-difference, convexity} per cell — exact-difference is mandatory at the corner (y ≈ x; convexity loses ×2), convexity is mandatory at small τ (exact-difference pays bracket width/16π²τ², which explodes). The first engine draft used exact-difference alone and failed at τ = 3/144 — instructive failure, recorded in the note.

## 2. Certificate structure and results

Uniform branch (L ≥ 12): 560 directed τ-cells on [3/144, 0.31]; worst F = **0.9550** at the corner cell [0.3085, 0.31]. Small-τ: 5 dyadic cells + analytic τ¹⁰ tail (worst 0.049; tail 1.6·10⁻¹³ at 10⁻³). Per-L (4..11): head-kill endpoint checks (t_kill = 0.25…2.1, values 0.20–0.45 < 0.5, with the head bound increasing in t so one endpoint certifies the strip) + 760 cells each; worst D = **0.9494** (L = 4) … 0.9448, all at the corner. Validity: WB5 bound ≥ true D on 40 random samples (min gap 1.3·10⁻⁸ — tight exactly at the corner, as designed). R_MAX certified 1.19 via 600 cells (worst 1.18105).

## 3. Errata produced en route

(a) My session messages had called r(0.5) = 1.16748 "the peak" — **false**: true sup r ≈ 1.17511 near t ≈ 0.40 (the R_MAX cell sweep caught it; r(0.5) is just a sampled value). Recorded in the note §1 and CONVENTIONS. (b) Two hand-constants in the note's first draft (Region-A-ext (1+e)³ and the prefactor) were 4th-digit slack and corrected from the gate run (1.0427 / 1317.4 / 0.8879). Both caught by asserts — the hard-gate culture doing its job.

## 4. Status changes

(1) **Lemma A: OPEN (compact window) → PROVED.** (2) **M4 Tier-2: the uniform floors N\*_C ≥ 8 / N\* ≥ 7 are THEOREMS on the diagonal** — the deterministic side of OP-1 is now fully closed at every tier (Tier-1 finiteness F027; Tier-2 floors here; exact kernel certificates M1/M2). (3) The (S)-side and the v₀-scaling decision are **unchanged and are now the only open content of OP-1** — M3a's status as the bottleneck is sharpened, not relieved. (4) The master docx upgrade is fully enabled: its conditional header can now cite this note + F031 + F032. (5) Grounds split, stated precisely: structural lemmas = paper-proofs (§1, §5–6 of the note); numerical inequalities = machine-certified with directed padding (NOT exact-rational, unlike F031 — justification in note §8; padding 16 orders below margins).

## 5. Chain of custody

This result = session-P proofs (F032-reviewed) + F031 (Lemma B) + this pass's note + WB gate run, over the G-M1/Q4/Q5-verified reductions. Every link carries its own gate run and finding; no step rests on an unreviewed claim. Files: note; engine + json (md5s above); F033 (this); ledger #54; UNIF M4 ADDENDUM 3e; OPEN_PROBLEMS OP-1 Addendum 8; CONVENTIONS +1 row; READMEs; MANIFEST 86; STATE; SESSION_LOG.
