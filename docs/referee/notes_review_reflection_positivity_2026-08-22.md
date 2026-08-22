# Second notes review: REFLECTION_POSITIVITY

**Date:** 2026-08-22. **Scope:** `01_OS_RECONSTRUCTION` (26 documents — the
G23 splice hunt), `04_GAP_BRIDGES` (20 documents), `05_TRANSFER_MATRIX`
(1 document). Two reading agents with spot-check duties; six load-bearing
steps machine-verified during review; 46 verdicts recorded in
`ledger/notes.yaml` (this pass: 27 extract, 1 import, 12 set-aside, 6
superseded/duplicate against in-archive successors). Register after this
pass: 67 reviewed, 1,530 pending.

## The headline: the archive diagnosed its own splice

G23's hole (2) — the chain proves decay in Langevin time where OS
reconstruction needs it in Euclidean time — was recorded from the one
document the first pass extracted. This pass establishes that document is
the *outlier*: at least ten of its siblings name "diffusion time ≠
Euclidean time" as the missing analytic step; the Gaussian toy note
refutes the naive bridge quantitatively (exact relation Δ = √λ_diff, now a
certified FINDING check: at m² = 4 the transfer gap arccosh(3) is provably
below λ = 4); and the scale-a family replaces the refuted raw-gradient
target with a bounded, falsifiable one. The review then ran the check the
archive never ran: against the *true slice marginal*, the corrected
comparison passes the Gaussian test with a uniform constant c ≈ 1/2,
while against the wrong measure it degenerates — identifying the
ν-measure premise (asserted via "a Markov property," never proved) as the
crux of the whole route. G23's entry is reworded accordingly: the splice
stands as open mathematics, and the archive holds both the diagnosis and
the corrected target. Nothing is closed: the "Theorem 5.1" label in the
most advanced attack is demoted to target-plus-plan (its Step C gluing
and its isometry premise are unproven, and the archive's own highlights
document already labels the same statement "target form").

## The transfer-matrix answers

- **No rigorous strong-coupling gap derivation exists in the archive.**
  The closest candidate assumes the operator-state overlap c₁ ≠ 0 as an
  unexamined bullet, uses the static-source (area-law) channel where the
  vacuum-sector glueball channel is needed, and has no
  convergent-expansion control. The rigorous counterpart is the
  Osterwalder–Seiler-era literature and MUNSTER_1985_TM.
- **G18 is untouched.** Nothing anywhere addresses volume-uniform
  overlap of smeared operators with the spectrum; the archive *assumes*
  what G18 asks. Recorded on G18's behalf as an informative absence.
- The best conditional documents quarantine their hypotheses honestly
  (the imported `03_Conditional_MassGap_Pipeline.tex`, `iter2`,
  `3_fixed_cutoff_su2`); the imported .tex is the archive's own
  refutation of the uniform-convexity mechanism (vacuum floor ~ cβL⁻²).

## Machine-verified findings from this pass (all now registered checks or recorded verdicts)

1. **Gaussian-toy bridge refutation** (certified): arccosh(3) < 4 at
   m² = 4; ratio ω/λ ≈ 2 at m² = 1/4 — the naive Δ ≥ λ_diff is false
   and the true scaling is the square root.
2. **Localization plateau** (certified): the iter2 covariance error is
   n-independent, so e⁻²⁵ is provably below the 8μ(K^c) plateau at
   n = 50 — the boxed gap extraction (9.3) does not follow as written.
3. **One-step spectral lemma** (exact): inf over the orthocomplement is
   1 − λ₁ — the verified skeleton reducing the bridge to one inequality.
4. Reversed inequality in `04_reflection_positivity_os_dirichlet_bridge`
   §3 (≤ where ≥ is needed) — recorded in its verdict, §4's lemmas
   extracted.
5. Direction slip in `SYNTH_CONJ_D` (displays K ≥ cH², needs ≤) —
   recorded in its verdict.
6. SU(2) "Haar mass" coefficient: reviewer computes 1/3 under the
   document's own convention vs the claimed 3/4 (= C_F pattern-matched);
   doubly refuted by the imported .tex's L⁻² obstruction. A repo check
   awaits an independent convention re-derivation; until then the claim
   is set aside and must not be cited.

## Status contradictions recorded

`MG_Constructive_Mass_Gap_Pipeline.md` stamps "proved component" on items
its own siblings label external inputs ("No part of this chain is proved
inside the project corpus" — the imported .tex). The .tex is the
trustworthy account. Same pattern as the first pass: the archive's honest
documents win against its confident ones, and the register now says so
in a form that cannot be un-said.

## Scope and negatives

Reviewed this pass: 47 unique digests across three directories.
Not reviewed: `02_RP_FUNDAMENTALS` (beyond the no-go already set aside),
`03_CONTINUUM_LIMITS`, `06_PIPELINES_ROADMAPS`, `07_NUMERICAL_TESTS`,
`08_MISC`, and `EXTRACT_05_From_Functional_Inequalities...` (left
pending). The extract verdicts on the six "module" documents
(rp_os_gap_extraction, Appendix_L, Core_3, RG-persistence, typicality,
dichotomy) record claims, not certified proofs — their deeper spot-checks
belong to a later pass and their verdicts say so. Nothing in this review
promotes any claim past T3, and nothing deletes a byte.
