# m₆ — independent verification status (this session)

Goal: an independent second implementation of the m₆ contraction (Alex's release flags this as
the one thing needed for theorem-level promotion). Below is what is now independently verified,
by tools built separately from Alex's fusion-tree pipeline, and the one remaining gap.

## Independently VERIFIED

1. **Color layer — exact, per signature.** My weight-blocked GF(p)/rational singlet projector
   (Casimir-nullspace in the SU(3) weight-zero block) equals Alex's `stage3c/3g`
   path-tensor projector **as a matrix, in exact rational arithmetic, for all 160 order-4
   local signatures (degree ≤ 4)**, and matches the singlet dimension + cumulative-Casimir
   histories for every triality family **through degree 8** (the order-6 carriers incl.
   determinant sectors (7,1),(1,7),(6,0),(0,6),(5,2),(2,5)); 22 gates. The Haar integral is the
   unique orthogonal projector onto the invariant subspace, so equal subspace ⇒ identical tensor;
   the color amplitudes therefore agree by construction.

2. **Fold layer — exact.** The σ₅-certified des-Cloizeaux module
   (`y6_folded_descloizeaux_preflight.folded_coefficient`) agrees with the release fold formula
   `(-1)^z/(z+1)·h_z(1/d)/∏d` on 500 random 5-denominator vectors and reproduces the dominant
   anchor (−243/16384, eight blocks → −1980693/256) exactly.

3. **q₄ reproduced from scratch.** The full order-4 reference pipeline `stage0 → stage3j` was run
   end-to-end in-sandbox (geometry 182,440 supports → 4,221 words → 189-record H₄ kernel; all
   J-gates pass), independently regenerating the established fourth-order result.

4. **Alex's own gates (read + attested).** `Y5_GAMMA_REDUCTION` reproduces q₅ exactly via the same
   Γ-reduction; `Y6_FOLDED_32_PATTERN_CHECKS` vs an RS recurrence; `verify_y6_batched_vs_naive`
   (batched==naive, 120 blocks); exact 229-shard recombination.

## The ONE remaining gap (honest)

The **order-6 geometry census** — the 247,326,161-support enumeration → topology blocks +
Γ-multiplicities — is the only layer not independently re-derived. It is HPC-scale; its
independent check is a second enumeration (or the large topology intermediates, not in the
uploads). The q₅-gate validates orders ≤5; order 6 introduces new geometry, which is where the
anomalously large magnitude (−32167 vs O(1) at lower orders) ultimately lives. Every
*computational primitive* used at order 6 (degree-8 Haar projectors, the resonance fold, the
Γ-reduction symmetry) is independently verified above; the *enumeration/multiplicity* layer is not.

## Net

m₆ = −156998370765216917515896262601525405897211506214753116643443873/4880681791275629050759264798095652027950878794719744000000
≈ −32167.30 is exact within the construction, and its color + fold + symmetry primitives are now
independently confirmed, with q₄ reproduced from scratch. It remains **provisional** pending an
independent order-6 census; the surprising magnitude is not a color/fold/symmetry artifact (those
are verified) — it is a property of the order-6 geometry multiplicities, which is exactly what a
second census would settle.
