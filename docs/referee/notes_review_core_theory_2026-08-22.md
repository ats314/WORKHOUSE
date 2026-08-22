# First notes review: the COMBES_THOMAS curated core

**Date:** 2026-08-22. **Scope:** the archive's own best-of package
(`COMBES_THOMAS/CORE_THEORY/00_best_of_index.md`, "Generated 2025-12-29")
plus the five pieces its Project Synthesis calls publishable — 20 documents
across 11 unique digests reviewed by three reading agents with mandatory
spot-check duties, every verdict recorded in `ledger/notes.yaml`. This
document is the evidence; the register carries the judgements.

The maintainer asked the right question before this began: "it could be
full of nonsense — is the repo prepared to ingest that and weed it out?"
This review is the answer, and the answer is yes — in both directions.
The weed-out found real rot in the headline artifacts, and the same pass
found genuinely correct, salvageable, promotable material the rot was
obscuring. Both are recorded with the same care, because a set-aside with
its reason is more useful to the next attempt than silence (the ADR 0005
principle, applied to the maintainer's own program).

## The program under review

A fixed-cutoff mass-gap strategy for SU(2)/SU(3) lattice Yang-Mills:
local Bakry-Emery curvature => LSI => diffusion gap => OS Hamiltonian
gap, with a SAFE-region curvature certificate as the quantitative core,
Combes-Thomas/Davies decay as the analytic kernel, and an RG story
carrying the constants across scales. Disjoint from the strong-coupling
series corpus (zero shared coefficient signatures — inventory fact).

## What failed review, and how it was caught

1. **The SAFE headline (min physical eigenvalue ~ 0.248) is unreproduced
   and its source tables appear constructed.** The sole source is a raw
   AI-chat export whose radial tables are contradicted by the archive's
   own scan CSVs (flat 0.2500 -> 0.2501) and by independent recomputation
   here; the "physical" column is the Haar column minus exactly
   delta = 0.006 at every radius but one; the "empirical" Wilson-norm
   table is the analytic envelope evaluated pointwise; kappa* = 0.25 is
   adopted upward from its own derived 0.201; the same document carries
   two contradictory values for the same Jacobian Hessian (0.049 vs
   0.29), both wrong (true value 1/4, closed form). The number 0.248 is
   quoted identically in at least seven documents — all tracing to that
   one table; no document anywhere states a lattice size; the operator
   was specified after the fact and its code never executed. One archive
   note escalates the sampled minimum into a claimed universal bound
   ("for all ||X|| <= 0.05") — a scan laundered into a certificate.

2. **The R^2 ~ 0.998 curvature-mass fit has zero evidential weight.**
   The five data points trace to the unedited "(EDIT)" placeholder
   arrays of the AI-supplied script template; the cited source document
   does not exist in the archive; mu_eff is never operationally defined;
   m_lat has no observable, volume, or error bar. Even at face value:
   the free-intercept fit is better than the through-origin fit (raw
   r^2 0.99953 > 0.99824), the intercept test cannot resolve the one
   physical prediction (F(1,3) = 8.26, p ~ 0.064), and residual RMS sits
   1.4x above the data's own two-decimal rounding floor. The downstream
   stress-test note's LOO and bootstrap arithmetic is genuine and
   reproduces exactly — correct arithmetic performed downstream of a
   vacuum.

3. **The nonabelian no-go ("exact equivariant Markov coarse-graining
   forces commutativity") is asserted in >= 9 files and proved in 0.**
   Its one-paragraph argument silently treats conditional expectation as
   multiplicative. The only proved obstruction in the archive (RICCATI
   04_no_go section 2 — audited, valid) is a different statement holding
   for all nontrivial compact groups, so it cannot source an
   abelian/nonabelian dichotomy. Recorded before repetition launders it
   into "established".

4. **The alpha = 0.976 RG-degradation iteration contradicts its own
   one-step bound.** The note derives a subtractive loss (kappa - delta
   per step: zero at ~42 steps, kappa* - 100*delta = -0.35) then boxes a
   multiplicative alpha^n formula (positive forever) with no argument
   converting one into the other. The sibling Schur note independently
   calls 0.976 a placeholder.

5. **Smaller but recorded:** the tubular-neighborhood reduction's
   plausibility step is backwards (the flat stratum is the
   maximal-stabilizer singular locus, not the regular region); the
   Cartan-alignment "6 constraints vs 3 DOF" counting is invalid as
   stated (stationarity at a link is 3 equations, not 6, and six
   bounded vectors in R^3 sum to zero with no common Cartan direction —
   explicit counterexample: three orthogonal antipodal pairs); the
   64,000-configuration "counterexample hunt" is random sampling with no
   descent, reported through an extensive norm with no lattice size; the
   drift note's italicized impossibility principle is one category too
   strong (refuted in general by the Meyn-Tweedie converse) though its
   center-critical-point observation is correct.

## What survived review

- **The H_phys operational definition** (spec + code): audited correct,
  self-contained, imported verbatim (`notes/imported/RESEARCH_2026-08/`).
  Notable: nothing in the archive ever ran it — the program's central
  operator has never produced a number.
- **The safe-scan reproducibility pair**: the archive's own falsification
  apparatus; independently reimplemented here and confirmed to six
  digits, including the identification of 0.291 as a reverse-fitted
  normalization artifact. Imported verbatim.
- **The Davies/Combes-Thomas bound for the massive Maxwell 1-form
  kernel** (canonical proof source: MAXWELL Appendix H, not the
  one-page streamline whose sketch carries a spurious factor 2 that
  cancels in the exponent but voids the prefactor derivation as
  sketched): the arcosh/arsinh exponent identity is exact, the O(m)
  upgrade is real, and the bound verified numerically on a 6x6 periodic
  lattice with margin <= 0.31 for both exponents. The strongest
  technical result in the package. Name-collision hazard recorded:
  C_partial denotes two different constants in the streamline vs
  Appendix H — a symbols.yaml warning candidate.
- **The block-convexity / Schur-complement mechanism**: classical and
  correct (Brascamp-Lieb; the alpha = 1 marginalization theorem's
  linear-algebra core verified by hand); its own section 4 honestly
  explains why gauge RG is not plain marginalization — which, read
  beside the proved (A4)+(A5) obstruction, is the honest replacement for
  the alpha = 0.976 story.
- **The OS-reconstruction chain and Mosco program**: sound conditional
  architecture with one recorded splice — section 2 proves decay in
  Langevin time, section 4 needs it in OS Euclidean time, and the
  bridge between them is a different theorem with different hypotheses,
  never stated.
- **The center-critical-point obstruction** to naive Lyapunov candidates
  (exact values: phi(-I) = 2 for SU(2), phi(omega*I) = 3/2 for SU(3)) —
  correct, clean, and check-ready.
- **The coercivity conjecture itself** (rough + non-Cartan-aligned =>
  force bounded below) remains a legitimate falsifiable target once
  separated from its invalid counting argument.

## Machine-check candidates that fell out (ranked)

1. T2: the Davies bound on a small periodic lattice (both exponents,
   stated margin), seeded from the numerical verification done here.
2. T1/T0: arcosh(1 + 2x^2) = 2 arsinh(x) — pure algebra, Lean-ready.
3. T1/T0: V_Haar(x) = |x|^2/8 + O(|x|^4) exactly in the code's
   normalization, so the Hessian at 0 is I/4 — pins the only
   well-defined constant in the SAFE ledger.
4. T1: the Schur lemma H >= kappa*I => Schur(H) >= kappa*I.
5. T1 FINDING: the alpha^n vs kappa - n*delta discrepancy
   (kappa* - 100*delta = -7/20 < 0).
6. T1 FINDING: three orthogonal antipodal pairs refute the 6-vs-3
   Cartan counting.
7. T1: center elements are critical points of Re Tr with the exact
   values above.
8. T2 FINDING: the SAFE radial table is not produced by any code in the
   archive; the reproducible profile is flat.

## The scaffolding decision (open, for the maintainer)

Recording `extract` verdicts for the survivors requires ledger targets
that do not exist yet: the analysis-side program has no claims in
`ledger/gaps.yaml`. The proposal on the table: register the program's
spine as new gap entries (the SAFE certificate with the FINDINGs
attached, the Davies bound with its T2 path, the coercivity conjecture
with its falsifier, the OS chain with the time-splice gap named), then
land the held extractions and the checks above. That is a deliberate
extension of the repository's charter from one program to two, taken by
visible PR — not silently. Until then, the reviewed-but-unextracted
documents remain `pending` in the register, which is the honest state.

## Scope and negatives

Reviewed: 11 unique digests (the curated core). Not yet reviewed: the
remaining ~1,586 pending documents, including the OS_REFLECTION_POSITIVITY
and MAXWELL manuscript layers the core cites as proof sources (Appendix H
was consulted as a cross-reference, not fully reviewed). Duplicate
topology noted throughout: every core document exists in 2-9 byte-identical
copies across topic folders, and the synthesis cites one phantom filename
that exists nowhere. Nothing in this review promotes any claim past T3,
and nothing in it deletes a byte.
