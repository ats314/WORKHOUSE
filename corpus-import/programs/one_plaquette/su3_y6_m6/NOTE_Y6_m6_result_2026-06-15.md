# m₆ — sixth-order glueball rest mass: RESULT (provisional, exact-internal)

**Source: Alex's own pipeline.** The complete m₆ contraction was computed by the
`SU3_Y6_M6_EXACT_INTERNAL_V1` release (in `C:\Users\...\Downloads\SU3_Y6_M6_EXACT_INTERNAL_V1_RELEASE.zip`;
also `SU3_Y6_M6_COMPLETE_DRIVER_V2.zip`, `NB_Y6_su3_m6_certified_recompute.ipynb`). I
located these on 2026-06-15 after initially failing to search Downloads — the result existed already.

## Value (project convention u = β/6 = 1/g_H⁴)

m₆ = −156998370765216917515896262601525405897211506214753116643443873 / 4880681791275629050759264798095652027950878794719744000000 ≈ **−32167.303151**

c₆ = −4270353824428899200786427191557487127249971701568661364147801 / 265509089445394220361304005016403470320527806432754073600 ≈ −16083.645  (for m₁₊₋/√σ = √6 Σ cₙuⁿ)

Rest-mass series: m(u) = 8/3 + u + (11/306)u² − (109151/249696)u³ + q₄u⁴ + q₅u⁵ + m₆u⁶ + O(u⁷).

## Census/contraction scale (from the release)

247,326,161 connected supports → 3,094,806 ordered words → 264,910 topology blocks
(205,699 nonzero at Γ) → 10,907,384 global path choices, summed as 229 exact rational shards.

## Status: PROVISIONAL (exact-internal) — per Alex's own README

"Exact within the enumerated one-flux des-Cloizeaux construction; independent second
implementation or historical comparison still required before theorem-level promotion."
The magnitude is anomalously large vs q₂…q₅ (O(1)); the audit traces it to a small family of
high-multiplicity, low-path-dimension Γ blocks (largest shard ≈29% of the abs total), not to
numerical instability. **Order-six introduces structures absent at order ≤5** (degree-8 (4,4)/(7,1)
carriers, double resonances), which the q₅-gate does not exercise — hence the genuine need for an
independent contraction.

## Internal gates that pass (release certificates)

- `Y5_GAMMA_REDUCTION_REGRESSION`: the same Γ-reduction reproduces q₅ EXACTLY.
- `Y6_FOLDED_32_PATTERN_CHECKS`: 32 resonance-pattern folded weights vs an RS recurrence.
- `Y6_M6_DOMINANT_ANCHOR`: 8 blocks, each −1980693/2048 (folded −243/16384 × Γ 65208), sum −1980693/256.
- `verify_y6_batched_vs_naive`: batched == naive on 120 blocks. Shard recombination exact.

## Independent cross-check done HERE (this session)

`ENGINE_Y6_m6_independent_fold_check.py`: the project's σ₅-certified des-Cloizeaux module
(`y6_folded_descloizeaux_preflight.folded_coefficient`) **agrees with the release's fold formula
on 500 random 5-denominator vectors** and **reproduces the dominant anchor −243/16384 and the
−1980693/256 eight-block sum exactly**. This independently validates the FOLD layer (incl. the
resonance handling) of the m₆ computation. The full color/topology contraction is NOT
independently re-implemented here — that remains the outstanding second implementation.

## To run / fully re-verify (Alex's drivers)

`NB_Y6_su3_m6_certified_recompute.ipynb` (or `su3_y6_m6_pipeline_complete.py auto`)
verifies the archives + reruns the dominant anchor + reports m₆/c₆. The full independent
re-contraction needs the five large exact intermediates (`Y6_GAMMA_TOPOLOGY_BLOCKS.tsv`,
`Y6_CLASS_ENERGY_SPECTRA.bin`, `Y6_EXACT_LOCAL_PATH_TENSORS.json.gz`, `Y6_ENERGY_CLASSES.tsv`,
`Y6_GLOBAL_FOLDED_WEIGHT_CATALOG.tsv`); SHA-256s are in `Y6_M6_EXACT_CERTIFICATE.json`.
