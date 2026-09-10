# Research goal and the path to it

Maintained scope guide, updated **9 September 2026** after the integration in
[PR #113](https://github.com/ats314/WORKHOUSE/pull/113). Read the
[current research map](current_research.md) for source-specific routes and the
[derivation proof map](derivation_formalization.md) for exact formal coverage.

## Governing objective

The objective is the Clay Yang-Mills existence and mass gap problem: a
nontrivial quantum Yang-Mills theory on four-dimensional Euclidean space,
for every compact simple gauge group, with the required field-theory axioms
and a strictly positive mass gap. The
[official problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
specifies the target. The maintainer established this research objective on
5 September 2026.

Progress means discharging a precise dependency of that construction, proving
a needed mechanism, or resolving a failed step with its strongest surviving
conclusion. A count of checks, formal lemmas or reviewed files measures work
performed; it does not measure distance to the theorem.

## Established inputs keep their scopes

The [result register](../ledger/results.yaml) records
`RESULT:WILSON_INFINITE_PHYSICAL_BAND` as proven: the actual infinite-volume
physical Wilson transfer and complete odd-band literal-source frame are
established on the stated small-coupling interval. G18 is discharged at its
registered fixed-spacing scope. Its historical route should not be restarted
as though the entire transfer or source-identification theorem were absent.

The September 9 [SC17 thermodynamic proof](derivations/wilson-sc17-thermodynamic-limit.md)
establishes its limiting ground law, closed form, full and physical gap, and
nonzero plaquette spectral-interval weight. The companion
[physical-time proof](derivations/wilson-sc17-physical-time-limit.md) identifies
the actual finite physical vacuum-correlation limit with that generator,
including the optimized endpoint. These are established analytic inputs in
their fixed-spacing regimes. Their incomplete Lean realization does not
change that mathematical standing.

The [flat-background source theorem](../paper/research_notes/G19_FLAT_HOLONOMY_SOURCES_AND_RANK_REPAIR_20260907.md),
finite-cell spectra, true-vacuum block estimates and Gaussian/selected
comparison results provide further inputs with different hypotheses.
Do not combine their constants across gauges, operators, parameter regimes
or physical clocks without proving the connecting identifications.

## Remaining obligations for the continuum target

| Obligation | Exact route to inspect | Required successor |
| --- | --- | --- |
| Uniform interacting comparison across spatial scales | [Selected inverse](derivations/wilson-selected-inverse-wall.md), `DERIV:WILSON_SELECTED_INVERSE_WALL:W6`; [SC17 continuation](derivations/wilson-sc17-spatial-closure.md), `DERIV:WILSON_SC17_SPATIAL_CLOSURE:R12_R14` | Establish the actual selected-pairing or full conditional reference-defect estimates with the vacuum, pressure, harmonic and moving-source terms included. |
| Summable scale transport | [Spatial Schur excess](derivations/wilson-spatial-schur-excess.md), `DERIV:WILSON_SPATIAL_SCHUR_EXCESS:SP7_SP10`, `:SP20_SP24`, `:SP25` | Realize the complete comparison and summable errors along a specified trajectory; retain the source metric and common physical clock. |
| Nontrivial continuum correlations and Euclidean symmetry | [Continuum manuscript](derivations/yangmills-continuum-balaban-multiscale-proof.md), `DERIV:YANGMILLS_CONTINUUM_BALABAN_MULTISCALE_PROOF:THEOREM_7_1`, `:THEOREM_7_2`, `:OS1`; [repair record](validation/wilson-g19-cauchy-repair.md) | Supply the missing summable increment, actual limiting fields/distributions and symmetry-restoration estimates. Preserve each entry's current conditional, disputed or open status. |
| Positive finite physical mass and observable weight | [Reconstruction](derivations/yangmills-reconstruction.md), `DERIV:YANGMILLS_RECONSTRUCTION:R1`, `:R6_R7`; [physical-time scope P10](derivations/wilson-sc17-physical-time-limit.md#p10-exact-scope-and-inputs-still-required-for-spatial-continuum) | Control physical energy and renormalized spectral measures through cutoff removal; identify the reconstructed generator and total observable family with the same limit. |
| Every compact simple gauge group | The group and representation hypotheses in the cited finite-cell, transfer and continuum sources | Extend the complete interacting continuum construction within those hypotheses; a theorem for a stated SU(N) or SU(2) regime does not silently cover every group. |

The fixed-spacing small-coupling constructions do not themselves control the
spatial continuum trajectory. The [continuum bridge](../paper/research_notes/G19_CONTINUUM_BRIDGE_INSERT.tex)
states the scale mismatch and its matching hypotheses. SC17 physical-time P10
likewise states why its bounded bare-bootstrap interval does not supply the
required large-parameter background comparison. These source conclusions
identify where a new mathematical estimate is needed.

## Formalization is a separate dependency chain

Use [the statement inventory](../ledger/derivation_statements.yaml) and
[formalization workflow](formalization_workflow.md) to select a whole statement
or a necessary ingredient. Actual cylinder derivatives, closed-form domains,
conditional projections, spectral measures and stochastic constructions must
be encoded faithfully when a theorem uses them. An abstract theorem with
uninstantiated model hypotheses remains scoped support for its source.

Report the exact obligation, proof or reproducible artifact, hypothesis
discharged, downstream theorem enabled and remaining blocker. Keep source
status, machine verification and local/pushed/merged state separate. A valid
novel proof is evaluated on its mathematics, independently of whether it
already appears in published literature or has a complete Lean translation.

## Historical development of the target

The earlier goal narrative below is retained with its source links. Its
"present", "now" and "next" refer to the September 5–7 stages it describes;
later September 9 results and the current route above determine present work.
It supplies history, not a second competing task queue.

<details>
<summary>Earlier goal narrative and September 5–7 route development</summary>

The objective is the Clay Yang-Mills existence and mass gap problem. The
[official statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
asks for a nontrivial quantum Yang-Mills theory on four-dimensional Euclidean
space, for every compact simple gauge group, satisfying the required field
theory axioms and possessing a strictly positive mass gap.

This is the governing research objective, established by the maintainer on
5 September 2026. A research iteration should remove an explicit obligation
on a route to that theorem, establish a necessary mechanism, or resolve a
specific failed step so the route can continue. Counting checks or adding
Taylor coefficients is not a measure of distance to the objective.

## What the present advance changes

The [complete Wilson construction](../paper/research_notes/G18_WILSON_INFINITE_VOLUME_PHYSICAL_BAND_20260905.md)
proves an actual infinite-volume transfer, a vacuum gap, and a complete
physical isolated odd band with a uniformly invertible literal-source frame
on one explicit small-coupling interval. The reconstructed Euclidean band
is the same entire spectral range. Its proof combines the nonlinear vacuum
coordinates, local unitary transport, anchored transfer activities, and a
bound on the whole source synthesis operator.

This finishes the actual Wilson infinite-volume and source-identification
stage in that regime. It turns the existing local calculations into a
controlled physical spectral object that a scale argument can act on.
The full theorem has analytic evidence; the exact controls certify their
declared finite identities and constants.

The [physical scale package](../paper/research_notes/G19_OS_BLOCKING_AND_REVERSE_MASS_MATCHING_20260905.md)
now adds an exact OS-history blocking intertwiner with the physical clock
retained. Its range and any remaining complement must be determined from
the actual history map; the new Gaussian observability theorem makes this
distinction explicit. A [corrected conditional-gradient theorem](../paper/research_notes/G19_CONDITIONAL_GRADIENT_REPAIR_20260905.md)
and [actual Wilson block calculation](../paper/research_notes/G19_WILSON_BLOCK_SCORE_AND_FIBER_OBSTRUCTION_20260905.md)
locate the failed raw averaging and diffusion premises.

The constructive replacement uses physical quantum energy. The
[compact rotor theorem](../paper/research_notes/G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md)
proves a fast vertical scale `1/a` for the specified Wilson blocks. The
[full coupled two-square theorem](../paper/research_notes/G19_WILSON_TWO_SQUARE_PHYSICAL_SHELLS_20260905.md)
also proves the entire block's physical gap and three lowest excited shells,
with real Wilson sources spanning that complete range. These supply a
physical local spectrum and source map for the scale comparison; they do
not yet identify the modes removed by an actual OS blocking map.
The [two-strip continuation](../paper/research_notes/G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md)
determines the first physical radial/mixed splitting with a controlled
remainder on an actual four-face graph. Its strips share a gauge constraint
and have additive Hamiltonians; surrounding interactions remain to be added.

The ultraviolet input now goes beyond isolated rotors and two-square
examples. A full physical finite-cell theorem gives the complete first
cluster from the original-link curl spectrum, while all-size planar and periodic three-dimensional
harmonic decompositions retain actual interfaces. The planar source frame
keeps its frequency weights; the three-dimensional link proof respects
Bianchi constraints and retains torus harmonic directions. The small curl frequencies on growing disks are
retained slow modes, so the theorem does not demand an impossible uniform
lower bound on the entire growing block's gap.

The [global vertical barrier](../paper/research_notes/G19_WILSON_GLOBAL_VERTICAL_BARRIER_20260905.md) supplies
a nonlinear comparison for every coarse holonomy of the actual two-face
blocks, with a full-fiber fast term and scalar coarse potential. The
[ground-bundle theorem](../paper/research_notes/G19_WILSON_GROUND_BUNDLE_RELATIVE_FORM_20260905.md) also controls
the true local projected coarse form with relative `O(g^2)` magnetic
error. The
[actual adjacent-strip complement](../paper/research_notes/G19_WILSON_ACTUAL_BLOCK_FAST_COMPLEMENT_20260905.md) now
also has a proved fast floor above the true full vacuum, and a closed
normalized Schur realization at fixed u. These remove specific single-block
premises. Uniform interacting-volume compression, coarse matching and
the actual source/history comparison remain the scale obligation.

The true-vacuum literal construction now resolves the projection choice
for additive Wilson blocks. It identifies the actual quantum marginal
and keeps the exact vacuum in the coarse source range. A complete
spectral argument gives a fast lower floor and an onto low source frame
uniformly over finitely or countably many copies, including a single
common Gauss constraint and its cross-block singlets. Separately, the
harmonic interface bound now controls the entire regulated Gaussian
quantum complement with the correctly weighted literal coordinate source.

These advances connect the source to the same vacuum and energy form as
the fast estimate. The exact central SU(2) score identity now disproves the proposed global
sublinear Fisher estimate. The remaining interacting comparison must
control the true-ground score on the relevant energy space and compare
the true coarse marginal. A small conditional fiber-ground derivative or
a raw Wilson Gibbs estimate is not that bound.

Exact Gaussian history reconstruction also repairs the object being
compared across scales. Reducing equal-time variables can leave the whole
fine physical history space observable. The useful successor is therefore
a controlled approximation of the actual generated transfer or memory,
with a proved low-energy projection and source map. A bound on the actual
OS complement is still useful when that complement exists; it is not the
general definition of eliminated configuration modes.

```mermaid
flowchart TD
  IR[Established infrared Wilson transfer and sources] -. generated effective theory matching required .-> RG[OPEN actual physical scale comparison]
  UV[Established finite-cell and nonlinear two-face forms] -. uniform interacting forms required .-> RG
  LS[Additive Wilson and regulated Gaussian literal fast/source bounds] -. interacting and local-history comparison required .-> RG
  FM[Exact quantum memory, dynamic cubic energy and full Gaussian inverse] -. complete nonlinear coefficient, harmonic control and remainder required .-> RG
  R[Reverse finite-mass and residue constraints] -. clock and renormalization required .-> RG
  RG -. controlled trajectory required .-> C[OPEN finite physical mass and continuum correlations]
  C -. field theory axioms and all groups required .-> YM[Clay Yang-Mills existence and mass gap]
```

Dashed arrows identify remaining hypotheses or constructions. The established
infrared theory and ultraviolet finite-block inputs meet at the open scale
comparison; neither is being presented as a continuum proof.

## Remaining obligations for the Clay theorem

| Obligation | Established input | What must still be proved |
|---|---|---|
| Remove the spatial lattice cutoff | The actual small-u Wilson transfer and source band; exact history intertwining; finite-cell physical spectra; all-size planar and three-dimensional harmonic interface comparisons. | Realize the interacting fast/source and generated-history comparison for the local Wilson block, prove uniform nonlinear physical form bounds with the harmonic constraints, flat variables and interfaces retained, and control approximation errors along a specified trajectory. |
| Retain a finite, positive physical mass | There is a positive transfer gap in electric-time units at each admitted fixed spatial scale. | Control the energy normalization and spectrum along that trajectory so a positive finite-energy physical excitation survives and the vacuum remains separated from all excitations. |
| Obtain a nontrivial continuum field theory | Actual Wilson multi-time correlations and their reflection-positive reconstruction are available at fixed spacing; the literal-source band is nonzero. | Produce renormalized limiting correlation distributions with nonzero physical content, the required regularity, full Euclidean symmetry and reconstruction axioms. |
| Control the physical observable space | The complete fixed-scale odd-band sources, finite-block real source shells, complete additive common-Gauss literal frames, and entire regulated Gaussian source bounds with their frequency weights. | Match actual gauge-invariant source algebras and renormalized spectral measures across scales, retain a nonzero physical residue, and control the intended channel. Exact vector observability alone need not imply cyclicity of every chosen invariant subalgebra. |
| Cover every compact simple gauge group | The finite-cell physical theorem applies to a faithful unitary representation of each stated compact connected group with simple Lie algebra, under its fixed-complex hypotheses. | Supply the interacting all-scale continuum construction for those groups. The current fixed-spacing odd-band route still has its own SU(N), N>=3 scope. |

The existing [continuum bridge](../paper/research_notes/G19_CONTINUUM_BRIDGE_INSERT.tex)
already identifies the central scale mismatch: in its Hamiltonian coordinate
u=g_H^-4, an asymptotically free trajectory reaches u tending to infinity,
whereas the proved analytic chart has a bounded small-u domain. It also
derives the required essential exponential behavior under its explicit
matching assumptions. These are established inputs, not reasons to stop.
They determine which kind of new estimate is needed.

## The next central target

The [flat-background source theorem](../paper/research_notes/G19_FLAT_HOLONOMY_SOURCES_AND_RANK_REPAIR_20260907.md)
now supplies uniform tangent control over the retained flat holonomies,
an explicit boundary source lift and a volume-independent linkwise
neighborhood of nonlinear source submersivity. It also proves that the
physical Coulomb source projection changes rank at enhanced stabilizers.
Use the smooth unreduced matrix observation and its exact coarse gauge
action for the compact-holonomy comparison; differentiating a global
fixed-rank physical source bundle is a failed route. Uniform interacting
vacuum, complete energy and history estimates are still required. The
ambient source lift does not itself construct their physical Schur map.

The [dynamic conditional covariance](../paper/research_notes/G19_DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY_20260906.md)
now gives a time-integrated connected cubic energy bound, uniform in volume
and bounded regulator at each fixed block scale, with bounded retained means
and local coefficient incidence. Quadratic-form domination carries its
synthesis bound to the actual full fast inverse. The
[exact full Gaussian Green operator](../paper/research_notes/G19_FULL_GAUSSIAN_FAST_GREEN_20260906.md)
also identifies that inverse on every chaos, keeping energy denominators and
all sectors with at least one fast excitation even for nonreducing sources.

The [actual local Wilson harmonic witness](../paper/research_notes/G19_WILSON_HARMONIC_CUBIC_OBSTRUCTION_20260906.md)
shows why an unlocalized regulator-uniform absolute exchange bound fails:
two retained harmonic coordinates supply divergent variance while the fast
gap stays positive. Its selected global plaquette sum cancels. The bounded-mean
estimate survives, and a complete calculation must preserve these distinctions.

The next target is the **complete nonlinear excess above the exact quadratic
memory**. Combine this cubic energy input with the quartic magnetic, electric
metric, Haar, moving-source, baseline cross and fast-form variation terms.
Control the spatial coefficients and interacting remainder with harmonic
localization, actual compact dynamics or proved cancellations. Complete source
and history matching and the physical scale trajectory remain open. The
[reproduction run](../runs/dynamic_fast_green_2026-09-06/README.md) preserves the three analytic
proofs and their separately scoped exact controls. The
[quadratic endpoint baseline](../paper/research_notes/G19_GAUSSIAN_PATH_ENDPOINT_BASELINE_20260906.md)
and first ground/source Lie cubic remain established inputs.

The preceding step joins three established mechanisms. The
[complete endpoint theorem](../paper/research_notes/G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md)
transports the entire additive physical low spectrum with high retained
sources controlled. The [actual local score theorem](../paper/research_notes/G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md)
and [excitation-support localization](../paper/research_notes/G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md)
give a uniform selected-source Schur estimate. The
[local covariant path block](../paper/research_notes/G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md)
gives an actual spatially local observation with the required uniform
transverse tangent and full regulated Gaussian source mechanism.

The remaining step is the actual interacting nonlinear fast/source and
generated-law comparison for that geometry. Endpoint positivity alone
does not erase memory, create a local Markov logarithm or assemble a
compatible scale hierarchy. A selected static source estimate alone does
not control its entire retained Schur complement. The conditional endpoint
clock budget states sufficient summable losses for a full gap, with those
interacting and hierarchy hypotheses still open.

The exact true-vacuum projection eliminates the additive product-vacuum
mismatch, and its common-Gauss fast floor survives without a copy-count
loss. Ambient interactions destroy the exact support decomposition used
in that proof. The next step is therefore a uniform comparison of the
interacting true-vacuum marginal and its complementary form, retaining
the actual metric and generated memory. The global sublinear Fisher candidate fails. The surviving criterion
requires coarse-gradient energy localization and an actual full-Q bound,
with high retained energies controlled before a full-gap conclusion.
Those uniform nonlinear Wilson estimates remain to be established. Flat harmonic directions still need
their actual quantization; a bound uniform in a positive Gaussian
regulator does not construct a vacuum at zero regulator.

Prove the uniform nonlinear energy comparison for the actual coupled Wilson
block family, using the retained harmonic slow space and interface bound as
inputs. Keep the generated temporal memory, induced kinetic mass, varying
vacuum energy and literal-source frequency factors. Specify the genuine
reflection/time-compatible history map and its invariant observable algebra.
Then compare its low-energy transfer and renormalized sources with the
controlled infrared endpoint, with errors summable in physical energy units.
The closed-form Schur theorem states sufficient form hypotheses and a
summable inverse-fast-energy budget. Their uniform Wilson realization,
including the full normalized coarse gap, remains the decisive open estimate.

The full two-square operator includes its real shared-edge coupling. Its
exact physical inversion symmetry improves the localization remainder but
is special to that graph; arbitrary blocks can retain cubic magnetic terms.
The next comparison must prove its own cancellations or bounds. The single
block's fast energy of order `1/a` is the desired eliminated scale, not a
finite continuum glueball mass.

Pursue the reverse direction alongside this construction: start from the
necessary behavior of a finite positive physical glueball mass and a
nonzero renormalized source spectral weight, then derive what an
intermediate coarse theory must preserve. Numerical continuum mass ratios
can distinguish candidate mechanisms but do not establish these bounds.
The Clay gap concerns every physical excitation; the present complete odd
band supplies a controlled sector and a nonzero source, not an identification
of the lightest continuum scalar glueball.

A proposed contraction must be tested on functions pulled back from coarse
variables. A small derivative of the forward block map is not automatically
a small derivative of conditional expectation. If this step fails, repair
the metric or covariance estimate and record the strongest valid recursion
before using the affine cascade. Reflection positivity and the physical
transfer identification must survive the chosen blocking operation.

Sharp temporal band-kernel matching remains an available supporting route
where it supplies the required clock or energy normalization. It is not
interchangeable with removing the spatial cutoff. New coefficient work is
justified when it settles a named obligation in this scale comparison.

## How progress is reported

Each update should state: the obligation being attacked; the exact new
statement or failed step; the proof or reproducible artifact; its downstream
consequence; and the next decisive calculation. Distinguish established,
conditional, numerically suggested and open statements, and separately
state whether their repository records are local, pushed or merged.

If no currently available route permits further progress, report that
inability and its precise mathematical obstruction. Exhausting the present
methods is not a proof that no future mathematical direction exists.

</details>
