# 10. External tools enter through evidence tiers, with named triggers

Date: 2026-08-21. Status: accepted.

## Context

The maintainer commissioned an external survey (ChatGPT, 2026-08-21) of
specialized tools that could complement the Lean core: SageMath,
python-flint/Arb, nauty/Traces, Lean Blueprint, RTNI, Singular/OSCAR, FORM,
SumOfSquares.jl, SLEPc, PhysLean, Gappa, CrossHair, and cross-prover
formalization. The survey was competent and its evidence taxonomy (kernel
proof / exact symbolic / certified enclosure / numerical evidence) matches
this repository's tier system. This ADR records the independent review and
the decision, so the survey's work is durable and the rejections are
arguable rather than silent.

The deciding principle: **a tool earns adoption only if it serves a tier
transition an open claim actually needs.** Every dependency is a
reproducibility cost for a repository whose promise is "re-check everything
in a second," so breadth is a cost, not a feature.

## Decision

**Adopted now — python-flint (Arb ball arithmetic).** The one proposal that
supplies a genuinely new evidence class. T2 today rests on float
comparisons whose own precision is asserted, not proved ("evalf(25) is
surely enough"). Arb enclosures replace that with a machine guarantee: an
`arb` comparison returns True only when provable from disjoint enclosures,
so a strict inequality certified through `workhouse.rigor` is a theorem of
interval arithmetic, not a hope about rounding. This does NOT create a new
tier and does not touch rule 5: an enclosure-certified check is still T2 —
"certified" here means the *comparison* is rigorous, never that the claim
is proved. First use: the one-ulp Delta_Gamma FINDING, where the previous
method was 25-digit sympy evaluation and the new method certifies both
directions of the discrimination. Remaining precision-sensitive T2 checks
migrate as they are touched, not in a sweep.

**Adopted when G3 engine work begins — nauty/Traces (pynauty).** Canonical
graph labels and automorphism groups are exactly the marked-cluster
engine's dedup and symmetry-factor problem, and getting those wrong is a
silent double-count. Engine tooling, not an evidence layer; the trigger is
the first G3 computation that enumerates clusters beyond hand-verifiable
size.

**Rejected — Lean Blueprint.** Its function already exists natively:
`ledger/theorems.yaml` maps each Lean theorem to the claims it formalizes
and the checks it promotes, and `tests/test_graph.py`
(`test_theorem_map_is_complete_and_sound`, `test_the_t0_layer_is_in_the_
catalogue`) verifies declarations exist and the map is complete both ways.
Blueprint would duplicate a validated mechanism behind a heavier
LaTeX-and-web toolchain. The survey could not have known this; the
rejection is recorded so the next survey does.

**Rejected — a second general-purpose prover (Rocq/MathComp, Isabelle).**
Agreeing with the survey: a second proof silo without an explicit
cross-prover objective is maintenance without evidence.

**Deferred, each behind a named trigger** (adopt when the trigger fires,
not before):

- *SageMath / OSCAR / Singular* — when an open claim needs Gröbner bases,
  syzygies, or symmetric-function machinery that sympy cannot finish.
  Sympy's exact rationals already cover the T1 layer; a second CAS adds an
  install measured in gigabytes for no new evidence class.
- *FORM (or Cadabra)* — when a series computation (G7's native sigma_6
  rerun, or the G3 engine at higher order) exceeds sympy's expression
  capacity in memory or wall-clock. FORM is the right tool for that wall;
  adopting it before the wall is speculative complexity.
- *RTNI / PyRTNI2* — if an independent U(N) cross-check of the tetrahedral
  Haar-resolvent contractions is wanted. Its core is U(N); the program's
  novel content is SU(3) determinant/epsilon sectors, which RTNI cannot
  check — so it can corroborate the unoriginal part only. (CAO_2023 §6.2
  states in print that SU(N) Weingarten calculus is "far less developed";
  the scarcity is the literature's, and RTNI does not fill it.)
- *SLEPc/slepc4py* — when a spectral computation outgrows scipy/ARPACK.
- *SumOfSquares.jl* — when some claim needs a polynomial positivity
  certificate; none currently does. Any SOS output would be numerical
  evidence until rationalized and re-checked exactly, as the survey itself
  says.
- *Gappa* — subsumed by Arb for this repository's needs (we certify value
  enclosures, not floating-point program transformations).
- *CrossHair* — falsification search is welcome in spirit, but the
  repository's checks are already executable falsifiers; effort goes into
  more checks, not a second harness.
- *PhysLean* — inspect before any large new Lean formalization, in case a
  definition is reusable; no action until then.

## Consequences

- `python-flint` joins the core dependencies; `src/workhouse/rigor.py`
  wraps it with exact-entry semantics (doubles and sympy Rationals enter
  enclosures exactly) and is the only sanctioned route to arb in checks.
- Deferred tools' triggers live in this ADR. Firing one means a PR that
  cites the computation that hit the wall — the same visibility rule as
  everything else here.
- The failure mode this ADR prevents: tool accretion by plausibility. Every
  entry above either serves a named claim's tier transition or names what
  would have to happen before it does.
