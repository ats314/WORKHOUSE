# Cross-source case studies with the discovery tooling

11 September 2026. Four investigations ran the second-iteration discovery
tools end to end on live obligations, each followed by an independent
skeptic instructed to refute the proposed connection. Every reading, its
evidence and the skeptic's narrowing are retained in the
[review register](../../graph-tasks/discovery/README.md) (sixteen records,
chain intact) and under
[the task evidence](../../graph-tasks/evidence/2026-09-11-discovery-agents/cases/)
(case files, pair dossiers, searches, plans, scratch computations). Nothing
was written to a scientific ledger: three proposal files were emitted for the
pairs a skeptic would register, and applying any of them remains a reviewed
hand edit. Scratch computations cited below are T3 at best.

## Method

For each seed the investigator retained a briefing, searched in the September
derivation vocabulary, wrote a plan with `discover plan` and their own
reformulations, ran `discover connections`, compared the most promising pairs
with `discover pair`, read both sources in full at the cited lines, and
recorded each pair through `discover review add` and `mark` in a scratch
register. A skeptic then re-read the cited lines with the instruction to find
the missing hypothesis, regime crossing, normalization mismatch or circular
citation. The register carries the investigator's reasoning as the note and
the skeptic's narrowing as the final reason.

## Case 1: the Combes-Thomas theorem has three homes and no bridge

Seed `RESULT:W6_ENERGY_WEIGHTED_CT` against
`notes/imported/EXTRACT_2026-09-01/EX-012-combes-thomas.md:34-53`, kind
`equivalent-construction`, **established** (skeptic: holds, narrower scope).

The localization core CT5-CT7 of the September repair note (the source of the
RESULT) is the imported Theorem CT of EX-012, and EX-011 section 6, under the
renaming `(a0, R, B0) -> (kappa, R, J)`: same hypotheses (uniform floor,
finite off-diagonal range, bounded off-diagonal row sum), same conclusion
`||inverse block|| <= (2/floor) exp(-(1/R) log(1 + floor/(2 rowsum)) dist)`,
same three-step proof. The skeptic checked each step. What the September
note adds is the `D^(+-1/2)` energy weighting (CT8) and the truncated-weight
limit. Neither source cites the other and the graph holds no link; the
natural landing is the existing `bears_on G21` scope of the RESULT plus a
documentary link, which the emitted proposal
`2026-09-11-equivalent-construction-result-w6-energy-03f46a-documents.yaml`
describes. Two companion pairs also survived: the soft-residual README's hard
block floor is not the uniform floor the selected-inverse wall still names as
missing (`scope-restriction`, established), and OP-1's Birman-Schwinger
comparator is EX-012's massive lattice Maxwell operator with the same row-sum
constant 18 (`shared-operator`, established, documentary by design).

The question's own mechanism was refuted: applying Combes-Thomas to the hard
block of the vacuum-subtracted fast form does not convert the volume-uniform
residual requirement into a local one. The README's own failed realization
has hard block `C = 1`, which satisfies every Combes-Thomas hypothesis while
the residual hypothesis still fails, so hard-block decay is neither necessary
nor sufficient (`compatible-hypothesis`, rejected).

Why it matters: `DERIV:WILSON_SELECTED_INVERSE_WALL:W6` is the named open
wall on the G19 scale trajectory, and three September documents each
re-derive or assume the same localization theorem without citing the imported
statement the corpus already holds. One registered statement of the theorem
with its true hypothesis list removes that duplication.

## Case 2: the outside-pressure Hessian is a Riccati source, not a Schur defect

Seed `DERIV:WILSON_SC17_SPATIAL_CLOSURE:R12_R14` against
`EX-014-rg-schur-riccati.md:214-272`, kind `equivalent-construction`,
**rejected**, and replaced by an exact identity.

The hypothesis that the outside-pressure Hessian `W_B''` is the quantum
analogue of the classical identity `Hess V_eff = E[Hess_xx V] - Cov(grad_x V)`
is false. With `u = log Omega` and the outside potential independent of the
block coordinate (the BA4 convention both sources use), the investigator found
and the skeptic verified symbolically

    Hess_x W_B = -2 eps J_xb J_xb^T + K_b J_xx,   K_b = -eps (Delta_b + 2 grad_b u . grad_b),

pointwise in the block and outside coordinates, with no fibre expectation,
covariance or Schur complement; the Gaussian case reproduces R12a. Two
consequences the skeptic added are worth an agent's attention: the identity
makes the R5 self-consistency loop circular in the sup-norm as a matter of
algebra (the excess contains terms linear in the unknown), and because `K_b`
is in divergence form for `Omega^2 db`, the fibre average of the
outside-generator term vanishes identically, so a weighted-L2-in-b version of
the defect sees only the signed term `-2 eps E[J_xb J_xb^T] <= 0`.

Three pairs survived. SC17 R10's marginal-curvature step, "marginal C
curvature at least `2(a_C - h_BC^2/a_B)`", is EX-014 section 3(3),
`alpha - M^2/gamma` with `alpha = 2a_C`, `gamma = 2a_B`, `M = 2h_BC`, by the
same Poincare-only proof and with the same open compact-group chart obligation
on both sides (`reusable-ingredient`, established; proposal
`2026-09-11-reusable-ingredient-deriv-wilson-sc17-sp-b65ece-documents.yaml`).
The imported Riccati flow note's Hessian evolution is SC17 R1 at `eps = 1`,
`V = 0` term by term (`scope-restriction`, established; proposal emitted).
OP-3's smallness quantity is the same Schur degradation operator, but its
`alpha` is a Haar-Jacobian floor that another corpus-import note shows is
unbounded below, so that pair is documentary only (`shared-operator`,
established with that narrowing).

Why it matters: the untried priority-4 route
`DERIV:WILSON_SC17_SPATIAL_CLOSURE:ACTUAL_REFERENCE_DEFECT_BOUND` needs a
volume-uniform bound on the complete signed defect; the identity says which
object that defect is and which average makes it signed.

## Case 3: the Balaban contraction factor is power counting, and the real disagreement was already registered

Seed `RESULT:BALABAN_MULTISCALE_CAUCHY_SUMMABILITY` against EX-014 section 1,
kind `shared-operator`, **rejected**.

The manuscript's `lambda = 1/9` is a polymer cell-count factor `L^-4`
(lines 286-291) replaced by the dimension-five irrelevance lemma, which the
G19 note supplies only as canonical power counting with no derivation in the
weighted polymer norm; the block map never enters, so EX-014's finite-lattice
Poincare cascade constant is a different object. The investigator's scratch
iteration of the manuscript's (6.14) with the forcing term gives
`||K_k|| -> (9/8) g_k^2 = O(1/k)`, so the geometric tail bound of (7.6) is
applied to a sequence (6.5) does not produce. That reading agrees with
`docs/research/graph-priorities-2026-09-10.md` and disagrees with the G19
note's summary table, which the investigator reported as an inconsistency to
review, not to reconcile.

One cross-family relation is mathematically correct: `RESULT:CONDITIONAL_GRADIENT_REPAIR`
refutes EX-014 STEP 6's `C_RG <= (1+O(r))/N`. The skeptic strengthened the
proof (for `f = F(Bx)` with `F(y) = y`, `Pf = F` for every fine measure, so
the constant is `m`, not `1/m`) and found a second inversion in STEP 4. But
the relation is not new: `ledger/gaps.yaml` already records it as the dead
route `ROUTE:G19:infer-a-scale-contraction-from-the-forwa-c194d2`, closed by
that RESULT, and the RESULT's own scope text states the refutation. The
register therefore holds it as established with the existing registration
named, and the investigator's `bears_on` proposals were withdrawn as the
wrong surface (`disagreement`, established, no proposal). Two observations
remain for a human: the `supported_by` scopes on the seed RESULT appear
swapped between two checks, and the manuscript's line 584-586 text and the
live G19 plan step describe the same missing derivation differently.

## Case 4: Brascamp-Lieb reaches the well tube and nothing beyond it

Seed `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10` against
EX-014 section 3, five pairs; the skeptic withdrew three and narrowed two.

What survives: on the well tube in the g-independent Morse coordinate, the
normalized chart-restricted conditional law on a convex ball satisfies a
Poincare inequality with constant `(g^2/2)(1+o(1))` by Neumann Bakry-Emery,
conditional on the S3 amplitude comparison. That is the chart Poincare bound
the tail-control derivation supposes at lines 249-270, so the pair is a
bearing on that supposition (`reusable-ingredient`, established with tube-only
scope, never a `depends_on`). The Agmon-geometry RESULT's positive
nine-dimensional phase is EX-014's floor hypothesis in the RESULT's own
near-well scope (`compatible-hypothesis`, established there and nowhere else).

What does not hold: the claim that Brascamp-Lieb is the next target of the
score-frame derivation (that target is a whole-level-set diffusion Poincare
inequality, which Brascamp-Lieb cannot deliver); the `kappa_0 = 9` figure
for H1 (a Gaussian-model number that ignores the differentiated amplitude
control S6 names as missing); and the two pairs that restated EX-014's own
Euclidean caveat and S6's antipodal warning as restrictions. The skeptic also
corrected the scratch numerics: the theta scan computed the potential Hessian
in Lie coordinates, not the conditional phase Hessian, and the S5 calibration
gives `B G B = Hess V` at a critical point, not half of it. One pointer from
the skeptic is worth recording for M10: a Poincare inequality with constant
`O(g^2)` on the whole compact fibre does not need convexity when the phase has
a unique nondegenerate minimum, by the harmonic approximation of the spectral
gap.

## What the tooling did and did not do

- In every case the cross-family passage was absent from the top ten when
  the question was phrased in the September vocabulary (EX-014 section 1 at
  rank 9 in the Balaban case; EX-014 and EX-005 absent in the M10 case;
  EX-012, EX-011 and OP-1 absent in the Combes-Thomas case; EX-014, OP-3 and
  the Riccati note absent in the pressure case). Plans with the agent's own
  reformulations brought EX-014 to rank 1 in the Balaban case and the
  imported notes into the Combes-Thomas and pressure shortlists; in the M10
  case they did not, and the investigator reached EX-014 through
  `connections` passage candidates and direct reading.
- `connections` returned imported-note passages only through the passage
  quota; no imported note is a graph record, so witness explanation cannot
  reach them.
- The pair dossier's markers and hypothesis cues were used in every case;
  its kind suggestion was overridden by the readers in six of sixteen pairs.
- Tool defects the investigators reported: `discover propose` addresses
  `ledger/results.yaml` although some RESULT records live in
  `ledger/recent_research.yaml`; a record-to-passage proposal on the
  `derivation` or `documents` surface carries an unfillable placeholder
  because imported passages have no catalogue id; the `derivation` surface
  emits a `depends_on` fragment for a `scope-restriction`; and the lexicon's
  focused expansion appended tokenizer fragments of `C^-1` and `a0` to a
  sub-query (fixed after the studies).
- Registration inconsistencies observed, all reported and none edited: the
  soft-residual campaign of 10 September has no ledger record; the
  resolvent-localization derivation still reads "Criterion W6: Closed" while
  its statement is disputed; the Balaban RESULT's `supported_by` scopes
  appear swapped; and the G19 note's summary table marks Theorem 7.1 proven
  while the manuscript and the priorities note say its input is not derived.
