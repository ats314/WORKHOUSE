# Derivation priorities and their exact consequences

Review dated **10 September 2026**. Start with the actual conditional-score
estimate M10 and the complete source-transport energy estimate R10, or its
direct mixed-form substitute. They are bounded mathematical successors to the
new fixed-square results. Develop the interacting spatial comparison and SC17
pressure estimate alongside them; the continuum RG drift remains a separate
target. This ordering expresses a research recommendation, not a theorem that
every route to the governing objective must pass through these estimates.

The [current research map](../current_research.md) and
[research goal](../research_goal.md) retain the established inputs: the
fixed-spacing infinite-volume Wilson transfer and complete odd-band source
frame, SC17 thermodynamic ground law and closed physical form, and the actual
physical-time correlation identification. Their analytic proofs remain
established under their stated hypotheses. Incomplete Lean realization does
not reopen those theorems. Applying them along a spatial-refinement trajectory
requires new model and scale comparisons.

| Established input | Next derivation and source | Consequence when its hypotheses hold |
| --- | --- | --- |
| The actual fixed-square source-potential moment, `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:ACTUAL_SOURCE_MOMENT`. | **M10:** prove `K_g(w) <= C0 + C1 W_g(w)` for the actual conditional dilation-adjusted score, with nonnegative constants uniform as `g -> 0`. See [conditional-score analysis, M.4–M.5](../derivations/w6-conditional-score-tail-control.md), `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10`. | The proved M11–M15 implications give all-source score weighting and a uniform Hardy criterion, recorded in `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_WEIGHT_FROM_M10`. This controls the first source derivative into L2; it does not by itself provide energy-valued higher derivatives. |
| Raw Hamiltonian, ground-energy and ground-vector derivative scaling through order three, `DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:GROUND_JETS`. | **Complete source energy transport:** prove `\|\|A^(r)(g)\|\|_(q_g -> q_g) <= d_r g^(-r-1)` for `r=0,1,2`, using the actual R9 generator, or directly prove the weaker mixed-form bounds R11. See [ground jets and transport, sections 4–5](../derivations/w6-ground-jets-and-transport-budget.md), `DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10`. | R11–R12 supply `M_j(s) <= c_j s^-j` for the complete transported residual, including source motion and vacuum subtraction. `DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:COMPLETE_BUDGET` then gives the subdivision error budget; actual grid matching and clock changes remain explicit inputs. |
| Fixed-square quantum energy estimates and the Gaussian shared-edge fast compression with its covariance-weighted source. | **Interacting spatial comparison:** replace the extensive ground-energy constant by a linked or local centered-energy estimate; prove the interacting fast floor, source transport and actual coarse-theory matching discrepancy. See [ground jets and transport, section 6](../derivations/w6-ground-jets-and-transport-budget.md), `DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:INTERACTING_GRID_COMPARISON`. | Makes the fixed-block comparison usable on growing interacting grids. Along a specified trajectory, summable complete comparison and source errors enable the scale-transport conclusions of `DERIV:WILSON_SPATIAL_SCHUR_EXCESS:SP20_SP24` and `:SP25`; a Gaussian fast floor alone does not supply these hypotheses. |
| The actual flat Gaussian polynomial semigroup budget R4a and the exact coupled potential-pressure cancellation R12a. | **SC17 full signed defect:** bound `(V_B-V_0)'' + (W_B-W_0)''`, with `W_B=(H_out Omega)/Omega`, on the actual compatible source fiber. Include metric, moving-projector and cutoff terms. See [SC17, Part III](../derivations/wilson-sc17-spatial-closure.md), `DERIV:WILSON_SC17_SPATIAL_CLOSURE:ACTUAL_REFERENCE_DEFECT_BOUND`. | An actual bound `2 beta_s(A)^2 delta/epsilon < 1` enables `:R4_R9`. A compatible strict reference-angle margin additionally enables `:R10_R11` and its assembled physical gap. The polynomial reference budget does not itself establish exponential spatial decay or the reference-angle margin. |
| The polymer Banach algebra, repaired small-field threshold, and the proved `RESULT:COMMON_SPACE_CONTRACTIVE_DRIFT` criterion. | **Actual RG and normalized-source drift:** after marginal subtraction, prove a quantitative irrelevant-remainder norm bound and summable changes of the complete scale map and observable. See [Balaban repair record](../derivations/yangmills-continuum-balaban-multiscale-proof.md) and [Cauchy repair, R1–R11](../validation/wilson-g19-cauchy-repair.md), `DERIV:YANGMILLS_CONTINUUM_BALABAN_MULTISCALE_PROOF:THEOREM_7_1`. | Supplies the missing Cauchy hypothesis for the actual expectations. A complete matched `O(g_k^3)` remainder or a common-space Lipschitz map/source estimate with summable parameter drift are sufficient alternatives. Limiting field regularity, symmetry, physical mass and observable weight still require their own hypotheses. |
| Exact Hodge splitting and actual fourth-order support, `RESULT:HODGE_FESHBACH_SPLITTING` and `RESULT:TIER_COLLAPSE_ACTUAL_H4_SUPPORT`. | **G9 minimal sixth-order calculation:** assemble the complete sixth-order contribution on the smallest connected plaquette support capable of the extra shape, retaining Haar/Gram quotients, electric denominators, Q projections, folds and rooted subtraction. See [current Hodge consequences](../current_research.md) and the [G9 register](../../ledger/gaps.yaml). | Tests whether the completed cleared carrier symbol has a component outside `{q,q^2,e_2,q e_2,e_3}`. This can settle a bounded higher-order shape question; a local support calculation does not finish the global sixth-order census. The algebraic identity `sigma(RUR)=4 e_2^2` does not prove that sixth-order dynamics produces it without cancellation. |
| Corrected raw partition and bounded-footprint bounds, plus the independent-source radius obstruction: `DERIV:TRACK_A_SUPPORTED:G17_P`, `:G17_V`, `:G17_I`. | **G17 source reformulation:** choose a source normalization, norm or topology whose footprint control survives the free product-law test, then prove that it retains the spectral-comparison input and nonzero observable weight. See [supported G17 statements](../derivations/track-a-supported-statements.md). | Provides a candidate replacement for the unrestricted exponential-source radius route. Another scalar coupling threshold cannot repair that route's source-growth obstruction. This is a sufficient-route investigation, not a prerequisite for every already established infinite-volume theorem. |

The smallest decisive checks follow the missing implications. For M10, retain
every coarse fiber, including rare fibers, and keep the actual conditional
potential and compact score. For R10, test energy regularity of the source
derivative: a bounded map into L2 can still be unbounded into the energy space,
as the companion's explicit example shows. For SC17, the first complete
calculation must reproduce cancellation of the Gaussian `BB*` term before
estimating the nonlinear excess. For G17, test a proposed new norm on the
independent product law before attempting the interacting estimate.

Absence of a dimension-five gauge-invariant operator is a useful starting
lemma for the RG route. It does not alone prove an `L^-2` bound in the actual
polymer derivative norm, its coarse-action subtraction constant, or the
normalized observable increment. The blocking symmetry and marginal
subtraction must be specified, and the resulting remainder estimate must be
proved. The [Cauchy repair](../validation/wilson-g19-cauchy-repair.md) retains
the exact source derivative and partition-function covariance term; neither
can be removed by citing Gaussian parity alone.

Interpret the priority graph by mathematical role:

The selected routes live in `ledger/gaps.yaml` under each gap's `plan`.
Their `frontier` metadata records a unique priority, optional exact target,
scope, consequence and decisive test. The graph emits `targets` to the
objective and `bears_on` to the stated downstream relevance. An explicit
`blocked_by` edge names an unfinished completion input within that chosen
route; it is separate from curated work order. `FRONTIER.md` and
`workhouse why` expose these records without converting relevance into a
proof dependency. Completion targets and blockers use authored-status
G/C/RESULT/DERIV/ROUTE nodes, not whole-document citations or Lean coverage.

The SC17 target is the separate open
`DERIV:WILSON_SC17_SPATIAL_CLOSURE:ACTUAL_REFERENCE_DEFECT_BOUND`.
Proving or formalizing the R12–R14 identities does not complete that
uniform model estimate. Similarly, M10 and R10 are specific sufficient
routes: an alternative score estimate or a direct R11 proof can be
registered as its own route without requiring M10 or R10.

- A proved statement can be an established input even when its machine tier
  is T3. Status, evidence and verification tier answer different questions.
- `depends_on` records an actual mathematical input of the named statement.
  A shared gap, nearby topic, or proposed work order does not establish that
  dependency. A result's `bears_on` connection is not itself a proof input.
- `formalizes` denotes coverage of the whole named source statement;
  `supported_by` denotes the recorded ingredient. An abstract proved
  implication retains its actual model hypotheses when used as support.
- A sufficient route is not a necessary obstruction to every possible
  solution. M10 does not become a prerequisite of R10, and R10 does not
  exclude a direct R11 proof. Alternative routes must remain alternatives.
- A priority entry should identify its source, missing hypothesis, regime
  and conditional downstream consequence. Counts of outgoing edges or
  missing formalizations are not a mathematical measure of priority.

Report progress as: hypothesis discharged, downstream theorem now applicable,
then the precise remaining model or scale input. Keep any new conditional
estimate separate from a claim that the continuum object has been constructed.
