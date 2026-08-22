# Fifth notes review: the Appendix H full-proof audit

**Date:** 2026-08-22. **Scope:** the canonical proof source of G21 —
`MAXWELL/Decay_Estimates/Appendix_H__Davies_Type_Decay_Massive_Maxwell_
Green_Kernel(1).md` (single copy; the "(1)" is a download artifact) —
audited proposition by proposition, with its three dependency appendices
located and their cited items verified, plus the disposition of the whole
Decay_Estimates family (~20 documents). 21 verdicts recorded (register:
116 reviewed, 1,481 pending).

## Verdict on the proof: sound end to end

Every step checked: the Laplace representation (H.1.1), the Lipschitz
weight algebra (H.2.x), the conjugation and the off-diagonal structure of
the perturbation (H.3.1–H.3.2), **the no-factor-2 crux (Lemma H.3.3)** —
exact cosh symmetrization, range-1 restriction, row-sum via the
self-adjoint block Schur bound of Appendix G — the Gronwall closure
(H.3.5), the kernel extraction (H.4.1), the horizontal-sector restriction
(H.4.2), and the half-depletion optimization (H.4.3) delivering exactly
prefactor 2/m² with exponent arcosh(1 + m²/(2αC_bdy(M_1))).

Numerically: the conjugated-semigroup bound holds with ratio ≤ 0.97
(near-tight — the check has teeth); the kernel bound holds at six
(m², α) points on 2D and 3D tori with margins 0.187–0.314, reproducing
the registered check's 0.31; B.4.6's C₀ ≤ 3ν_P is tight on both tori;
and the archive's own sanity-check numeric note reproduces **bit for
bit** (imported, with its generating script).

Two flaws, recorded, neither voiding anything: H.4.4's proof asserts the
equality (H.4.9) where only ≤ holds (the conclusion survives via H.4.1
directly), and Prop A.9.5 (C₀ ≤ D_E) is stated with "Proof deferred" in
Appendix A — the one unproved upstream link, relevant only to the D_E
form of the exponent. The earlier finding is also confirmed from the
other side: the one-page COMBES_THOMAS streamline's factor-2 sketch does
not derive its own stated pair; Appendix H is the document that actually
proves it. The correct one-page streamline exists
(`02_davies_decay_maxwell_boundary_rowsum.md`) and its verdict says to
prefer it.

## The C_bdy name collision, settled

Three homonyms found and transcribed: the weight-profile constant
(Def A.9.4 — argument-free, proof-bearing, keeps the bare name), the
region-based constant (streamline §5.2 — always carries Ω), and a
region-subset variant (Def 5.1 of the quadratic-form note). The
region flavors are aliases requiring their argument; resolution recorded
in G21.

## G21 re-anchored and moved to partial

The registered bound was valid but chained through the deferred A.9.5 in
its D_E form; the entry now names C_bdy(M_1) as the canonical constant,
records both flaws, the collision resolution, the float guard (the
arcosh form loses 6082 ulps at small mass — evaluate η via arsinh), and
the two queued checks: the (m, α) sweep and the H.3.3 mechanism check,
which certifies exactly the step where the streamline's spurious factor
lived.

## Scope and negatives

The HS-covariance family (`04_helffer_sjostrand_and_greens_decay.md` and
kin — the U3/G14-adjacent layer) was deliberately left **pending**, not
set aside: it is the next review target when work resumes. Unverified
numeric side-notes were set aside with revisit conditions. Nothing
promotes past T3; the audit's passing does not certify the claim — the
checks do, and two more are queued.
