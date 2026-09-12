# Earlier proofs recovered from WORKHOUSE

The search found **seven priority findings that appear absent as substantive mathematical results from the checked theory graph**, plus **four earlier supporting derivations worth separate intake**. These are derivations already present in the research collection. This audit located them, read the selected arguments, checked their graph coverage, and reran narrowly scoped exact calculations.

Every selected source already has an inventory node. The missing work is to register the actual statements, assumptions, evidence, and dependencies so that the graph can use them. An inventory entry alone does not do that.

The comparison is pinned to live `origin/main` observed at **bc9da0233ceb72ed76739dc9b892d9c6ca1b50d5**. Main advanced during the audit; the new R10 registrations were compared and did not change the shortlist. Both graph revisions are retained. Exact source hashes and graph-query results are in [graph_comparison_final.json](C:/WORKHOUSE/research/earlier_proof_discovery_20260911/graph_comparison_final.json). Absence here means no corresponding substantive registration was found after source-name, terminology, and neighboring-result comparison. Original research and scientific graph inputs were preserved.

## Seven priority findings

| ID | Earlier result located | Missing graph statement | Evidence reviewed |
|---|---|---|---|
| F01 | Cubic quotient regularity trichotomy | Exact C^{1,1}, C^{3,1}, and analytic cases at Gamma | Analytic proof; exact expansion rerun |
| F02 | Equal-ray coefficient reconstruction | Four-parameter recovery with an independent intercept holdout | Analytic formulas; exact ray gates rerun |
| F03 | Obstruction to a uniformly localized finite translation frame | Consequence of the direction-dependent flat-band projector | Analytic contradiction; projector algebra rerun |
| F04 | Joint rank-volume monotone scaling | Sharp two-variable bound and joint limit | Analytic inequalities; exact derivative and endpoint gates rerun |
| F05 | Finite-order nested-quotient spectral reduction | Theorem joining local histories, Gram quotients, resolvents, folds, and connected readout | Proof and stated hypotheses read |
| F06 | Reduced B6 shell solver | Symmetry-reduced finite-coupling calculation with full-space residual certificates | Derivation and saved numerical certificates read |
| F07 | Persistence of an isolated matrix spectral atom | Conditional bridge from cutoff carrier data to a limiting pole | Measure-theoretic proof read |

### F01-F04: singular geometry, reconstruction, localization, and scaling

Source: [NOTE_FLUX_singular_geometry_derivations_2026-08-28.md](<C:/WORKHOUSE/ALL THEORY/theory/notes/NOTE_FLUX_singular_geometry_derivations_2026-08-28.md>). Companion: [ENGINE_FLUX_singular_geometry_derivations.py](<C:/WORKHOUSE/ALL THEORY/numerics/engines/ENGINE_FLUX_singular_geometry_derivations.py>).

The common dispersion is `Delta = A q + B e2 + 4 C e2/q + D e3/q`, where `a_i=4 sin²(k_i/2)`, `q=sum a_i`, and `e2,e3` are the elementary symmetric expressions in the three a_i.

**F01 — regularity trichotomy, [lines 75-104](<C:/WORKHOUSE/ALL THEORY/theory/notes/NOTE_FLUX_singular_geometry_derivations_2026-08-28.md:75>).** The extension at Gamma is C^{1,1} but not C² when C is nonzero; C^{3,1} but not C⁴ when C=0 and D is nonzero; and analytic when C=D=0. The proof identifies the leading homogeneous angular term. Cubic symmetry rules out a quadratic polynomial in the first case; in the second, coordinate-plane vanishing would require an even quartic to contain a degree-six factor. This is a usable analytic result, stronger than merely observing touching or nonanalyticity. Register it near flat-band geometry and G11 with the exact dispersion convention.

**F02 — equal-ray tomography, [lines 133-199](<C:/WORKHOUSE/ALL THEORY/theory/notes/NOTE_FLUX_singular_geometry_derivations_2026-08-28.md:133>).** On rays with one, two, or three equal nonzero a_i=a, the energies are `E1=Aa`, `E2=2(A+C)a+Ba²`, and `E3=(3A+4C)a+(3B+D/3)a²`. Writing Rj=Ej/a gives

`A=R1; B=m2; C=b2/2-A; D=3m3-9m2`, with independent holdout `b3=2b2-R1`.

Two distinct nonzero a values determine the slopes and intercepts. The graph already uses other high-symmetry checkpoint extractions; this equal-ray protocol and its unused consistency check are a separate result. It supplies a direct test for future coefficient extraction and shape identification.

**F03 — no uniformly localized finite translation frame, [lines 203-265](<C:/WORKHOUSE/ALL THEORY/theory/notes/NOTE_FLUX_singular_geometry_derivations_2026-08-28.md:203>).** For the rank-one fiber away from Gamma, a finite family of exponentially localized translation generators cannot both span the fiber and retain a uniform positive lower frame bound. Analytic generators plus such a bound would extend the projector continuously, contradicting its different directional limits. The compact cube generator instead has frame floor `4 sin²(pi/L)`, collapsing like L^{-2}. This explains why finite-volume generation does not give a uniformly conditioned localized basis as volume grows.

The same section gives the dipolar principal kernel proportional to `(delta_ij |x|²-3x_i x_j)/|x|⁵`. Its principal Fourier differentiation is consistent; the printed O(|x|^{-4}) remainder was not independently established here. Keep the asymptotic remainder separate when registering the frame theorem.

**F04 — sharp joint rank-volume law, [lines 269-354](<C:/WORKHOUSE/ALL THEORY/theory/notes/NOTE_FLUX_singular_geometry_derivations_2026-08-28.md:269>).** With the established rational hopping t_N and `Delta^(2)=4 t_N u² sin²(pi/L)`, the quantity `G(N,L)=N³ L² Delta^(2)/u²` increases in both variables for integers N,L>=3 and obeys **405/68 <= G(N,L) < pi²**, with joint limit pi² as both tend to infinity. The note also proves t_N decreases for real N>=3.

The graph already contains N³t_N monotonicity and the exact quarter-deficit in `src/workhouse/invariants/rank_law.py:40,60`, plus `LEAN:hopping_deficit_numerator`. Those ingredients are already covered. The missing registration is the joint rank-volume statement and sharp endpoint. Its scope is the recorded second-order quantity.

The companion engine completed **16/16 exact gates** in this audit. See [the execution log](C:/WORKHOUSE/research/earlier_proof_discovery_20260911/singular-geometry-verifier.log). These support the algebra; they are not a Lean proof of every analytic statement in the note.

### F05: finite-order nested-quotient spectral reduction

Source: [full derivation, hypotheses and proof, lines 178-547](C:/WORKHOUSE/WORK_SINCE_LAST_SESSION/FINITE_ORDER_NESTED_QUOTIENT_SPECTRAL_REDUCTION_THEOREM_FULL_DERIVATION_2026-08-28.md:178).

At a fixed perturbative order, an energy-decorated finite quotient graph determines the connected effective operator under explicit locality, finite reachable quotient, nonresonance, fold-completeness, support bookkeeping, and normalization hypotheses. Supporting lemmas establish bounded support, Gram-null decoupling, and exact history merging. The full theorem is at lines 447-547.

A useful distinction is retained: rooted scalar Möbius readout and an operator shape quotient have different output spaces. A shape-dependent operator cannot be discarded as a scalar energy shift. The proof also requires ordered support-union convolution before rooted subtraction.

The graph contains several ingredients and a master-document citation, but I found no registration of this full theorem. It belongs alongside the exact effective-Hamiltonian and connected-support results and bears on G13. The supplied hypotheses remain part of the statement; this theorem alone does not prove the unrestricted classification of shortest temporal histories. No new Lean compilation was performed.

### F06: B6 shell reduction with residual certificates

Source: [B6_SHELL_BLOCK_KRYLOV_REDUCTION_2026-08-28.md, lines 1-115](C:/WORKHOUSE/WORK_SINCE_LAST_SESSION/B6_SHELL_BLOCK_KRYLOV_REDUCTION_2026-08-28.md:1). Evidence: [saved certificate](C:/WORKHOUSE/WORK_SINCE_LAST_SESSION/b6_shell_block_krylov_reduction_certificate.json).

For the retained SU(3) open-cube B6 operator K6(u)=E-uM, the noncommuting word construction gives radial dimensions **67, 155, and 133** for the three cubic carriers: 355 representative coordinates, or 798 after symmetry multiplicities, compared with 1,916 charge-odd and 3,864 physical coordinates in the retained model. The rank decision uses the source's relative SVD cutoff 10^{-10}.

The saved 201-point g-grid on [1,2] reports a maximum full-space Ritz residual about **8.78e-14**, with historical crossing g=1.3039546641713. These are retained numerical results, not reruns from this audit. The exact Hermitian residual implication is useful: a full-space Ritz residual bounds distance to the full retained spectrum at the tested parameter.

The graph already records B6 second-order closure and related truncation/sign results. I found no corresponding finite-coupling word reduction or residual-certificate registration. Register exact symmetry/residual statements separately from the saved floating-point run. The word spaces are not asserted to be invariant, and a grid does not certify every coupling or every branch.

### F07: isolated-pole persistence under matrix-measure convergence

Source: [WORKHOUSE_CARRIER_TO_PARTICLE_PROOF_DOSSIER.md, lines 607-730](C:/WORKHOUSE/WORK_SINCE_LAST_SESSION/WORKHOUSE_CARRIER_TO_PARTICLE_PROOF_DOSSIER.md:607).

The theorem uses positive 3-by-3 matrix spectral measures with total mass I, convergence of Laplace transforms including zero time, intervals shrinking to M>0, a uniform matrix residue floor z_*I, and a uniformly empty surrounding annulus. Scalarization and the Portmanteau inequalities give a limiting atom with `nu({M}) >= z_*I` and an empty punctured annulus. An irreducible symmetry representation gives the stated scalar form by Schur's lemma.

This is a complete conditional argument worth exposing in the graph. Current positive-Laplace, moving-time spectral-gap, and nonzero finite-energy-weight results are related but do not state this isolated-atom persistence theorem. Appropriate neighbors include `RESULT:OS_KERNEL_MOVING_TIME_GAP` and `DERIV:OS_KERNEL_GAP:WEIGHT`, with differing assumptions explicit.

The source distinguishes a source-visible pole from a gap for the entire physical sector. Actual residue, annulus, convergence, and source-totality requirements must remain visible; the lemma does not itself discharge them.

## Four further earlier derivations worth intake

These are useful mathematical arguments missing as explicit registrations in the checked graph. Novelty relative to graph coverage is distinct from a claim of first publication.

| ID | Source and accepted scope | Review result and boundary |
|---|---|---|
| F09 | [Conditional spectral floor, lines 14-82](C:/WORKHOUSE/09_ARCHIVE/sorted_second_pass/01_conditional_spectral_floor_monotonicity.md:14) | The Rayleigh proof gives lambda_min(E[H given G]) >= E[lambda_min(H) given G] for integrable finite symmetric matrices on a common space, with the corresponding convex defect bound. A noncommuting exact example passed. This does not identify a coarse effective Hessian, which can contain an additional covariance term. Infinite-dimensional forms need extra assumptions. |
| F10 | [Disjoint staple coordinates in D=4, lines 51-180](C:/WORKHOUSE/09_ARCHIVE/sorted_second_pass/LYAPUNOV_09_appendix_disjoint_staple_coordinates_d4.md:51) | Six incident staples admit six distinct link coordinates, each affecting only its own staple in the star. The coordinate proof is sound; all 12 periodic lattice/direction cases at L=3,4,5 passed. Probabilistic independence needs its own interaction assumptions. |
| F11 | [Positive-sector phase isolation, lines 28-114](C:/WORKHOUSE/09_ARCHIVE/sorted_second_pass/LATTICE_QCD_phase_isolation_principle.md:28) | Positive sector weights and additive integer charge give generating-polynomial contractions with nonnegative coefficients; phase enters through the final substitution z=exp(i theta). A finite transfer-polynomial check passed. General gauge-theory positivity and cancellation cost do not follow from this rearrangement. |
| F12 | [VSU convex Poisson problem, lines 43-243](C:/WORKHOUSE/09_ARCHIVE/sorted_second_pass/VSU_Convex_Poisson_WellPosedness.md:43) | The action for mu(x)=1-exp(-x) is strictly convex with the stated Hessian eigenvalues. On the stated bounded domain, coercivity and the direct method give a unique weak minimizer. Four exact constitutive/asymptotic checks passed. The later whole-space limit, logarithmic normalization, and far-field assertions need separate work. Use a separate research branch in the graph. |

## Exclusions from the missing-result count

**F08 is already represented.** The [SU(2) affine plaquette Laplacian proof](C:/WORKHOUSE/09_ARCHIVE/sorted_second_pass/05_affine_laplacian_law_analytic_proof.md:54) derives Delta B_p=12-12B_p in its round-S3 metric convention. Current check `CHK:notes-program-safe-davies-coercivity-g20-05d038:fundamental-casimir-c-0--n-2-1--2n-exact-3816b3` explicitly contains the same four-links-times-three identity. Its earlier source could improve provenance, but the identity is not missing. The exact metric and coefficient checks passed here.

Two other sources need specific repairs before their full printed statements can be accepted:

- [Determinant reduction, line 32](C:/WORKHOUSE/09_ARCHIVE/sorted_second_pass/01_determinant_reduction_theorem.md:32): the two-row formula omits row-permutation parity. For x=(0,1,0), u=(1,0,0), and v=(0,0,1), the actual determinant is -1 while the printed orientation gives +1. The reduction survives with the correct parity factor.
- [Transversality derivative, line 127](C:/WORKHOUSE/09_ARCHIVE/sorted_second_pass/LYAPUNOV_08_transversality_rank3_and_binomial_tail_drift.md:127): varying the selected link also varies its own plaquette force. Differentiating Ad_g X_j needs the derivative of X_j as well as the adjoint term. F10 does not remove that term. The printed rank/tube argument needs a repaired derivative before its later probabilistic conclusions are imported.

These exclusions rest on current coverage or specific calculations, not on whether the claimed research is conventional. All originals were preserved.

## Search coverage and reproducibility

The physical inventory listed **192,937 paths**, including hidden and ignored files, archives, preserved checkouts, earlier brain-session revisions, notebooks, Python, Lean, Markdown, TeX, PDF, and Word files. Exact-byte deduplication across paths left **15,227 searched text contents** and **6,882 keyword-hit contents**. Keywords included proof/proofs, prove/proved/proves, theorem, lemma, derivation, proposition, corollary, and QED. Three oversized compressed numerical payloads were also fully streamed for keywords, with zero hits. The supplemental pass covered `.resolved` revisions, TAR/GZ/7z/ZST, a large research-library ZIP, and a malformed notebook's recovered text.

This is a workspace-wide keyword census with detailed mathematical review of selected findings, not a claim that all 6,882 hits have been fully verified. External papers, logs, inventories, and implementation notes are among the hits. The [candidate queue by region](C:/WORKHOUSE/research/earlier_proof_discovery_20260911/CANDIDATE_QUEUE.md) and [full machine-readable queue](C:/WORKHOUSE/research/earlier_proof_discovery_20260911/combined_keyword_candidates.jsonl) retain them for retrieval without calling them new proofs.

Known limits: runtime/dependency directories and generated catalogue copies were excluded; compatibility junctions were not followed as duplicate roots; 57 traversal errors remain in test/cache/temp locations; corrupt test fixtures and a Word owner-lock file are not readable documents. Binary arrays, image-only equations, databases, spreadsheets, slides, and Git object history were not semantically searched. See [coverage details](C:/WORKHOUSE/research/earlier_proof_discovery_20260911/COVERAGE.md), [the first-pass log](C:/WORKHOUSE/research/earlier_proof_discovery_20260911/scan_summary.json), and [the supplement log](C:/WORKHOUSE/research/earlier_proof_discovery_20260911/supplement_summary.json).

Executed validation: the original singular-geometry engine passed 16 exact gates; [eleven additional exact diagnostics](C:/WORKHOUSE/research/earlier_proof_discovery_20260911/selected_exact_checks.json) passed, including the determinant counterexample. The B6 numerical campaign was not rerun, Lean was not compiled, and graph claim statuses were not changed.

## Registration order

1. Register F01-F04 together with their shared source and replayed engine; split analytic statements from individual exact checks and retain existing rank-law dependencies.
2. Register F05 with every finite-order hypothesis and the scalar/operator distinction.
3. Register F07 as a conditional matrix-measure theorem with its application requirements explicit.
4. Register F06 as separate analytic reduction/residual facts and source-pinned numerical evidence.
5. Intake F09-F12 with the stated scopes; attach F08's earlier source to the existing check instead of duplicating it.

No registration was performed in this search task. The handoff includes this report, exact source identities, graph comparisons, a retained search queue, execution logs, and saved start/end graph snapshots.
