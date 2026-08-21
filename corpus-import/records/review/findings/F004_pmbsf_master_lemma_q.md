# F004 — PMBSF pass-19 master + Lemma Q complex (#33), and Decision #007

**Date:** June 12, 2026 | **Read:** master §0.5 TL;DR (through pass 16) + changelog + TOC structure; Lemma Q section heads (Paper §4); LCI_TOSJ reduction (structure); supporting docs at head level. The master is 6,475 lines with appendices A–S — deeper appendix reads remain available on demand; the TL;DR is the program's own audited summary and was read fully.

## Status architecture (the program's own terms)

A **rigorous conditional reduction** of SU(2) lattice YM coercivity (fixed projected spectral window, periodic 4-lattice) to one stochastic input. "Not a mass-gap proof… the final stochastic input is open and is essentially equivalent to the mass-gap problem itself." The open input appears in two forms across passes: **(M′)_SU(2)** (hard-indicator cluster cumulant decay, hierarchy levels; level (iii): Σ_{p'}|Cov(X_p,X_{p'})|tr(A_pA_{p'}) ≤ Cq²κ_Λ²) and **Lemma Q** (conditional rare-source factorization), with pass-19's LCI ⇒ TOS+J ⇒ source-radius reduction and **pass-10's minimal target**:

    |Cov_W(X_{p,η}, X_{p',η})| ≤ C q_η² e^{−m d(p,p')},  uniform in Λ  —  "the first SU(2) breach point."

## Unconditionally proved (per the master; not re-derived here)

Deterministic spine PTO-1/2/3 with closed-form κ_Λ; sharp Bernoulli plaquette-incidence Bernstein (margin 0.615 at the v9 worst corner); **Theorem FNG Stage 1: the Q₈ finite-group firewall closes at β ≥ 61.16** (complete finite non-Abelian validation of the architecture); Lemma A (incident PTO overlap); Lemma C (trace-to-quadratic bridge, certificate ≤ 0.3039).

## Failed/retired routes (now carried into the OP-1 dossier §5)

Global HB-q² Matrix-Stein absorption (v15 audit: η_cov 0.40–1.23 vs target 0.25); edge-Bernoulli comparator v6b (Wilson/edge ratio 1.23–1.55). Previously recorded: A′ budget, trace-weighted WEAK.

## The spectral-window direction (passes 11–16) — and a deep convergence

Appendices J–S build the case that restricting to the **coexact subspace + spectral window** produces a positive projected Bakry–Émery floor at the working corner (ρ\* ≈ 2.2–2.3; Gaussian and Wilson MCMC samples at L=6, 8; all eigenvalues positive across every sample). Pass-16's sharpened conjecture: **ρ\*(L) → κ_G as L → ∞** — "the geometric Ricci floor does all asymptotic work." κ_G is the *same* Haar curvature floor that anchors P04 in the main chain. **Flag (high value):** when unit #7 reviews P04/Core Curvature, cross-read against Appendices O–S — the two programs may share one mechanism at infinite volume. Recorded as observation; no claim.

Also notable: honest-correction culture is structural (fourth honesty correction: an era formula off by 4× found and fixed; v17b m\* extrapolation explicitly walked back; pass-13 "the gap is undone explicit work, not a hidden closure").

## Decision #007 (executed this pass)

Lemma Q / (M′) = canonical M3 form (M3a); comparator = interface (M3b). Translation note written: `programs/op1_defect_sparsity/NOTE_PMBSF_lemmaq_comparator_translation.md` — object dictionary (X_p ↔ D(U); q_η ↔ ρ₁; tr(A_pA_p') ↔ G_P²; κ_Λ ↔ T_full; (M′)(iii) ↔ ρ-weighted kernel sums; pass-10 target ↔ dossier §3 ρ₂ bound), group/parameter gaps (SU(2)β3.5/heat-bath/window ↔ SU(3)β5.6–7.2/Wilson/Hodge), assembly path for M4, failed-routes carry-over. Dossier M3 → M3a/M3b in both copies; STATE updated.

## Actionables

- Alex: M3a is now a single boxed inequality with an attack route — everything downstream is staged.
- Agent next: #34 (paper lines vs publication bundle manifest), #3 (PROOF_13/14/15 structural review), #35 (notebook/PDF identification).
- Standing: κ_G convergence cross-read at #7; reconcile δ_bond/η conventions when drafting M3b.
