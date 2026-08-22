# Fourth notes review: the analysis spine's supports

**Date:** 2026-08-22. **Scope:** LSI_POINCARE, LYAPUNOV, RICCATI (644
files, 379 unique digests; the already-reviewed SAFE/Schur/drift/PBH
digests skipped). One reading agent with recomputation duties; twelve
documents reviewed in depth, 12 verdicts recorded (register: 96 reviewed,
1,501 pending). Three new checks (132 → 135).

## The first document-vs-document adjudication

Two archive documents state opposite things about the same ODE
(λ' = −2λ² + σ): a Manus-AI "Rigor level: 10/10 — Publication-Ready"
proof claims global existence for ALL initial data with a numerical table
to match; the maintainer's own SIM verification note records finite-time
blow-up below λ₀ = −√(σ/2) with an explicit correction paragraph.
Recomputation settles it completely: the SIM note's outputs reproduce to
every printed digit (12 digits), while the proof document's Theorem 2.2
contains a sign error, both of its numerical tables are false (one
contradicting its own Remark 3.4), and its physics corollary is 20% off
its own formula. The adjudication is now a registered T2 FINDING check
that integrates the ODE both ways. The pattern to remember: **the
archive's honest instruments keep beating its confident documents, and
the recorded margin is now digit-for-digit.**

## What earned import (4 documents)

- **The Section 7 drift manuscript** (Lemmas 7.1–7.41): the mature form
  of the entire Lyapunov program — smooth proxy replacing the
  cut-locus-broken d_G², exact drift identity, uniform closure with
  explicit constants, and the single open input quarantined as
  Assumption 7.38 (pairing coercivity = G22). Prop 7.39's κ-arithmetic
  recomputed by hand: correct.
- **PART III Section 3**: the *correct* local-to-global LSI assembly
  (defective LSI + Rothaus upgrade), superseding the folder's
  unconditional-tight-LSI version of the same argument.
- **The SIM Riccati note**: the adjudication's winner, bit-faithful to
  its own code.
- **The Dynamic Hessian Riccati .tex**: the sound core of the
  re-amplification mechanism (all three flow equations re-derived by
  hand at review), correctly scoped and restricted.

## The G22 reduction, now doubly derived and pinned

Two independently written documents (the Section 7 manuscript and
G_drift_full_algebra) derive the same volume-uniform constants —
C_V = 8C_Δ + 8C_grad, C_Γ = 64ν C_grad — and a registered check now
proves their specializations identical. A third route (the pulse-door
Dobrushin template, the batch's most-duplicated file at 7 copies)
reframes G22 as "compute q < 1" — a genuinely different attack; no q has
ever been computed, which is a well-posed future check. The explicit
Wilson-action drift note contributes the exact pairing identity
⟨∇S_W, ∇B⟩ = β|P||∇B|² and correct rough-plaquette combinatorics, with
its remaining input being G22's Cartan-alignment problem under another
name.

## The c₀ claim, disciplined

DOC4's "explicit LSI constant" c₀ = (N²−1)/(2N) is exactly the
fundamental quadratic Casimir — now a registered exact check (SU(2) 3/4,
SU(3) 4/3), with the factor-4 convention trap pinned (the archive's own
simulations use the normalization where the same eigenvalue reads 3).
The leap from Haar geometry to Ric_μ ≥ c₀ for the *interacting* measure
remains unsupported and stands in recorded conflict with the cβL⁻²
vacuum-floor obstruction. Synthesis_02 enters as the spine's best
self-inventory with its internal contradiction recorded (its Ch. 15.2
"proved" list vs its own Ch. 18 OPEN register — Ch. 18 is right).

## Negatives and open items

- The RICCATI folder contains **no trace of the riccati-su3-optimizer
  connection** (greps for optimizer/gradient-descent come back empty) —
  if that link is documented anywhere, it is not in this archive; worth
  asking the maintainer where it lives.
- One unverified citation flagged (Cattiaux–Guillin AIHP volume) —
  recorded as unverified, not as an error.
- Not yet reviewed: the WILSON, HESSIAN, MAXWELL mirror copies (covered
  by digest), the LSI archive/ subfolder, one chat export
  ("Extending Local LSI via Lyapunov Drift.txt") and the appendix
  ledgers. MAXWELL's Appendix H — G21's proof source — remains the
  highest-priority unreviewed single document.

Nothing in this review promotes any claim past T3; nothing was deleted.
