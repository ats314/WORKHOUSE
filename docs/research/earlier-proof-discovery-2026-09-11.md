# Earlier-proof discovery integrated into the theory graph

11 September 2026. The archive discovery is now represented by source-pinned
statements, result records, exact controls, original-source imports and a
complete mapping of the keyword-hit digest set. The earlier files are the
source of these results. This integration supplies graph registration,
reviewed proof exposition, scoped controls and the explicit E12/E13 repairs.

Read the [canonical proofs](../derivations/earlier-proof-recovery.md),
[pinned result record](../../paper/research_notes/EARLIER_PROOF_RECOVERY_20260911.md),
[evidence package](../../runs/earlier_proof_recovery_2026-09-11/README.md), and
[task record](../../graph-tasks/2026-09-11-earlier-proof-integration.md).

## Complete accounting of the search

The retained search has 6,882 distinct keyword-hit contents. Of those, 4,827
already had native source inventory identities and 2,055 did not. Every content
now resolves to at least one NOTE node. The new archive has 2,072 entries:
the 2,055 newly inventoried contents and seventeen reviewed original-source
imports, including three auxiliary source/certificate files outside the keyword set.

The scan's original digest set is fixed by SHA-256 in
[coverage_summary.json](../../runs/earlier_proof_recovery_2026-09-11/coverage_summary.json).
Its [complete mapping](../../runs/earlier_proof_recovery_2026-09-11/keyword_coverage.jsonl)
records every graph identity and initial disposition. At the initial baseline,
6,680 keyword-hit contents were pending substantive review; 188 had pre-existing
reviews and fourteen were reviewed-source imports from this campaign.
After incorporating main through PR #158, 6,649 remain pending and 233
have registered source reviews. The immutable mapping keeps its initial dispositions.
These counts describe source review, not the number of proved mathematical claims.

The search includes supported text, PDF/DOCX extraction and archive members.
It does not include OCR of images, every binary format, inaccessible runtime
folders or Git-object-only history. The frozen
[coverage receipt](../../runs/earlier_proof_recovery_2026-09-11/discovery_receipts/COVERAGE.md)
records all exclusions and errors. Full keyword coverage is not a claim that
every file in the workspace has been semantically reviewed.

## Registered results

| Source section | Stable result | Scope |
| --- | --- | --- |
| E1 | `RESULT:EARLIER_CUBIC_QUOTIENT_REGULARITY` | Local differentiability at the cubic Gamma point for the specified four-shape formula. |
| E2 | `RESULT:EARLIER_EQUAL_RAY_IDENTIFICATION` | Exact finite linear identification in the displayed basis; extra shapes require more data. |
| E3 | `RESULT:EARLIER_LOCALIZED_FRAME_OBSTRUCTION` | Infinite-volume uniform localization obstruction and exact finite-volume frame conditioning; no dipolar remainder estimate. |
| E4 | `RESULT:EARLIER_JOINT_RANK_VOLUME_SCALING` | Second-order coefficient and finite-volume scaling only; L=2 is excluded by an exact countercontrol. |
| E5a | `RESULT:EARLIER_FINITE_ORDER_SUPPORT` | Finite support combinatorics; not finite local Hilbert dimension. |
| E5b | `RESULT:EARLIER_GRAM_NULL_OPERATOR_QUOTIENT` | Exact finite-dimensional physical quotient, with domains and invariance explicit. |
| E5c | `RESULT:EARLIER_DECORATED_HISTORY_MERGING` | Decorated dynamic programming; matching an endpoint alone is insufficient. |
| E5d | `RESULT:EARLIER_NESTED_QUOTIENT_REDUCTION` | Conditional finite-order reconstruction; no unrestricted G13 classification or momentum-shape absorption into a scalar shift. |
| E6a | `RESULT:EARLIER_SHELL_SYMMETRY_RITZ_CONTROL` | Analytic isotypic reduction and full-space residual theorem; no uniform branch identification. |
| E6b | `RESULT:EARLIER_B6_RETAINED_KRYLOV_CAMPAIGN` | Historical finite-campaign numerical evidence only, with 355 representative coordinates and 798 including multiplicities. |
| E7 | `RESULT:EARLIER_ISOLATED_POSITIVE_MATRIX_ATOM` | Source-visible spectral pole theorem; no actual-source construction, unseen-sector gap or exact triplet stability. |
| E8 | `RESULT:EARLIER_CONDITIONAL_SPECTRAL_FLOOR` | Finite matrix conditional Jensen statement; a marginalized Hessian can have an additional covariance subtraction. |
| E9 | `RESULT:EARLIER_D4_DISJOINT_STAPLE_COORDINATES` | Exact incidence theorem; no statistical independence or force-rank conclusion. |
| E10 | `RESULT:EARLIER_POSITIVE_SECTOR_PHASE_ISOLATION` | Sector-polynomial algebra; no general positive non-Abelian representation or efficient sign-problem solution. |
| E11 | `RESULT:EARLIER_VSU_BOUNDED_DOMAIN_WELLPOSEDNESS` | Bounded-domain variational theorem for the specified constitutive model; whole-space and far-field limits remain separate. |
| E12 | `RESULT:EARLIER_DETERMINANT_PARITY_REPAIR` | Corrected exact determinant identity with all six row orders checked; original source preserved unchanged. |
| E13 | `RESULT:EARLIER_MOVING_ADJOINT_FORCE_DERIVATIVE` | Exact derivative correction; the historical transversality/tube estimate requires a separate repaired proof. |
| E14 | `RESULT:EARLIER_SPHERE_EQUAL_COUPLING_COVARIANCE` | Genus-zero same-coupling covariance only; no cross-class or higher-dimensional plaquette closure. |
| E15 | `RESULT:EARLIER_SU3_POSITIVITY_BOUNDARIES` | Exact countercontrols to generic loop or coefficientwise positivity; no refutation of fully summed elementary-plaquette covariance. |
| E16 | `RESULT:EARLIER_REFLECTION_ADAPTED_BLOCKING` | Specified deterministic raw blocking geometry; extra field partitions, stochastic kernels and multistep effective actions need their own hypotheses. |
| E17 | `RESULT:EARLIER_CORNER_BLOCKING_REFLECTION_DEFECT` | Exact local failure of this intertwining convention; not a proof that every blocked measure violates reflection positivity. |

These twenty-one result records remain T3 for whole-statement machine
certification. Twenty are registered as proven with analytic evidence. The
B6 campaign remains conditional numerical evidence with retained historical
outputs. Fourteen native T1 checks rederive their own exact controls, including
the original sixteen-gate engine and the Q(i) corner-blocking trace witness.
Their `supported_by` links state the calculation actually checked.

E12 restores the missing determinant row-permutation parity. E13 restores the
moving force's own derivative. The original unqualified formulas remain
queryable as falsified DERIV statements, alongside the corrections. The
SU(2) affine Casimir law already had a native check, and the G19 stochastic
blocking counterexample already had a route record; these are linked as
existing work rather than counted as missing discoveries.

## Explicit successors

The four open `DERIV:EARLIER_PROOF_RECOVERY:` statements are
`DIPOLAR_REMAINDER`, `PHYSICAL_CARRIER_REALIZATION`,
`STAPLE_TRANSVERSALITY_REPAIR`, and `VSU_WHOLE_SPACE`.

The proven statements become available under their actual hypotheses. None
closes the complete continuum Wilson construction, all-shell source totality,
unequal-coupling higher-dimensional covariance or the unrestricted shortest
physical-history classification. Those are distinct application obligations.

## Verification and continuation

The [manual task record](../../graph-tasks/2026-09-11-earlier-proof-integration.md)
records executed validation and end-snapshot provenance. Whole-statement Lean
coverage was not added; existing kernel registrations and the dependency export
were left unchanged. Use `workhouse why RESULT:EARLIER_NESTED_QUOTIENT_REDUCTION`
or `workhouse why DERIV:EARLIER_PROOF_RECOVERY:PHYSICAL_CARRIER_REALIZATION` to
follow the graph from the recovered inputs to their successors. Use
`workhouse notes --queue` and the coverage mapping for further source review.
