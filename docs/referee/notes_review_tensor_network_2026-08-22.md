# Third notes review: TENSOR_NETWORK

**Date:** 2026-08-22. **Scope:** the folder's two flagship files,
`01_QRACAH_DOOB_GAP`, `05_TRANSFER_OPERATOR` (minus the already-reviewed
composite-operator file), and a full inventory-plus-contamination-map of
`06_LATTICE_QCD_SECTORS` (117 entries, ~66 unique digests). One reading
agent with recomputation duties; four independent numerical verifications
run during review. 17 verdicts recorded this pass (register: 84 reviewed,
1,513 pending).

## The contamination chain, closed

The curvature-mass R² ≈ 0.998 story is now fully reconstructed, end to
end, inside one folder:

1. `TESTING GEOMETRY AGAINST LATTICE MASS GAPS.txt` — a chat export whose
   script arrays are labeled `(EDIT)` placeholders — then presents "from
   your run ... you reported" numbers. **Running the script on its own
   placeholders reproduces every reported digit** (k = 0.962363,
   R² = 0.998237, RMS, all five residuals). No independent data ever
   existed.
2. `best_of_bundle_v2.zip` contains the previously-phantom
   `EVIDENCE_01_Curvature_Mass_Fit.md`, which upgrades that self-fit to
   "What This PROVES ... STRONG EVIDENCE FOR MECHANISM", plus the
   downstream fit and stress-test files — the complete laundering path
   from template to "best of" in one artifact, kept intact as the audit
   trail.
3. The self-fit is now a permanent T1 FINDING check: exact rational
   least squares through the origin on the placeholder pairs gives
   exactly k = 9333/9698 and R² = 21627127/21665332.
4. The counter-artifact: `clean_docset.zip` (2025-12-27) is the
   maintainer's own self-critical quarantine bundle ("evidence only") —
   the discipline arrived later, and independently.
5. One false positive cleared: `YM_MassGap_Lattice_Haar_Hessian_
   TransferGap.md` matches the numeric grep only via sqrt(3/8) = 0.6124
   — analytically independent, clean.

## The toy exponent, re-graded upward

`05_doob_qracah_analytic_bounds.md` derives ν = 1 exactly as q → 1 for
the Doob/q-Racah gap (off-diagonals O(ε), diagonal O(ε²)), and
window-tightening fits at review confirm the convergence (0.9691 →
0.9919 at N = 5). The archive's empirical ν ≈ 0.9668 — previously set
aside as an unanchored fit — is a finite-window estimate of a provable
exponent. The canonical toy statement (`02_doob_qracah...`) reproduces
exactly from the archive's own code (spectrum rebuilt to 1.1e-8), and
its uniform-in-N gap conjecture enters as a G18 toy isomorph. A
companion negative was recorded: at the default parameters the Doob
bulk is NOT the intermediate-Casimir representation (18% kernel error) —
a real outcome the archive had stored only as a protocol.

## What failed review

The folder's two flagships: `13_qRacah_Spectral_Gap.md` (its sole
original formula is underived, hypothesis-free, and internally
inconsistent by a factor of 2 with its own conventions) and
`14_Tensor_Network_HOTRG.md` (a fabricated-or-transplanted
χ_top ≈ (180 MeV)⁴ "matches MC within 10%" claim self-refuted by its own
limitations section). Also set aside: verbatim networkx library files
misfiled as project work.

## G18 finally has archive material

Three items, the first G18-relevant content in three folders of review:
the SU(3) Lanczos Hessian tables (the archive's only volume-scanned
SU(3) spectral data; independently consistency-checked at review —
regression intercepts 0.1257/0.1247 against the analytic Haar floor
0.125 — and showing no volume collapse of the convexity window in the
probed range); NOVEL_02's spacing-uniformity dichotomy (exemplary
hedging); and the Doob-toy uniformity conjecture with the Cheeger/
localization route as analytic leverage. All evidence-grade, all T3,
all now visible from `workhouse why G18`.

For G23, `BEST_05` supplies the HS/Combes-Thomas architecture reduced to
one named inequality — and the review's audit adds a third missing brick
its "one missing brick" framing omits (typicality does not convert a
good-set-local curvature bound into the global operator inequality the
HS step needs), recorded so the framing cannot harden.

## Verified identities banked for future checks

Quantum-6j recoupling unitarity (2.8e-15, three boundaries,
classical-limit cross-check); the q-Racah orthogonality PᵀWP = H
(1e-12, with the weight-positivity hypothesis still to be delimited);
the ν = 1 sympy re-derivation queued.

## Scope and negatives

Not reviewed: `02_Q6J_SYMBOLS`, `03_THETA_DEFORMATION`,
`04_HOTRG_METHODS`, `07_TOPOLOGICAL_SUSCEPTIBILITY`, `08_MISC`,
`synthesis`, `physics_extractions_v2`, the Manus-AI deliverable family
(inventoried and classified, review pending — self-labeled "Rigorous"
with heightened suspicion warranted), and the manuscript version
ladders (inventoried; shadow copies and version chains to be recorded
as duplicate/superseded in a cleanup pass). Nothing promotes past T3;
nothing was deleted.
