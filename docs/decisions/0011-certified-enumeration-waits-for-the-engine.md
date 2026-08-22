# 11. Second tool survey: certified enumeration waits for the engine

Date: 2026-08-22. Status: accepted. Companion to ADR 0010, same principle:
a tool earns adoption only when it serves a tier transition an open claim
actually needs, and every dependency is a reproducibility cost.

## Context

The maintainer commissioned a second external survey (ChatGPT, 2026-08-21,
read-only, deliberately additive to the first): Graphillion/TdZdd,
VeriPB/CakePB, CaDiCaL + LRAT-in-Lean, FiniteFlow/FireFly, INTLAB, IBEX,
leanprover/lp, Macaulay2 SchurRings/InvariantRing, LinBox, Normaliz/4ti2,
Sollya/FPTaylor, TensorKit.jl, GroupMath, GAP packages, ore_algebra,
HiRep/GPT, Loogle, Alectryon.

Ground-truthed before deciding: unlike a survey written from vibes, this
one's claim-to-gap attributions are all real — G13 IS the
shortest-history classification gap, G15 IS the symbolic-N Gram
transcript, G11 IS interval rigor and the near-Gamma gates, G17 IS the
PC-2 free-energy reduction, and the 3895-vs-3850 topology distinction is
verbatim in gaps.yaml. The survey's own evidence-ceiling column and its
closing boundary — none of this supplies G17's estimate, G18's bridge, or
G19's continuum limit — are correct and adopted as stated.

## Decision: zero immediate adoptions, three pre-approved pipelines

Pass 1 adopted Arb because an existing check upgraded the same day.
Nothing in pass 2 upgrades an existing check today: every candidate
serves work that has not started. So nothing is installed now, and the
best proposals are pre-approved with named triggers, so firing one is a
PR citing the computation that needs it, not a fresh debate.

**Pre-approved 1 — certified enumeration for G3/G13** (Graphillion or
TdZdd for ZDD-compressed history families; VeriPB + CakePB, or CaDiCaL
with LRAT checked in Lean, for completeness certificates). Trigger: the
first G3/G13 enumeration that exceeds what two independent Python routes
(the repo's current pattern: definitional recursion vs literal
enumeration) can cross-check. This is the survey's best idea, and its own
caveat is adopted as a rule: the certificate certifies the Boolean/ZDD
encoding, so T0 is reachable only if the physics-to-encoding step is
itself proved in Lean; until then the ceiling is a certified T1.
pynauty (ADR 0010) shares this trigger — canonical labels and compressed
families are complementary halves of the same engine.

**Pre-approved 2 — finite-field reconstruction for G15**
(FiniteFlow/FireFly). Trigger: a symbolic-N Gram computation that sympy
cannot finish. Rule adopted from the survey's own caveat: raw
reconstruction is probabilistic, so any reconstructed rational function
enters only after exact substitution checks at held-out points and
degree-bound verification — the same posture as the existing CRT
certificates.

**Pre-approved 3 — exact representation-theory cross-checks for G14/G15**
(Macaulay2 SchurRings/InvariantRing, or the GAP packages via the ADR 0010
Sage gate). Trigger: a Schur-functor or invariant-ring identity the
tier-collapse work needs and sympy cannot derive. The survey is right
that these do not evaluate Haar integrals or explain a cancellation —
cross-check only.

**Deferred, same wall-logic as ADR 0010:** LinBox (exact sparse linear
algebra past sympy's comfort), Normaliz/4ti2 (only if a claim is actually
reduced to linear Diophantine form; their blindness to temporal ordering
and energy denominators is the survey's own warning), TensorKit.jl +
SUNRepresentations.jl (if a numerical G18 transfer-spectrum probe is ever
commissioned; T2 forever), ore_algebra (conjecture generation, T3 by
construction, behind the Sage gate), HiRep/GPT (no G19 benchmark program
exists), leanprover/lp (revisit if a G17 sublemma is actually
rational-affine; the survey itself calls it new and narrow), Alectryon.

**Rejected:** INTLAB (a MATLAB dependency to do what the already-adopted
Arb stack does natively — see Consequences), IBEX (no claim needs
box-certified root isolation, and it emits no independently checkable
proof object), GroupMath (Mathematica dependency), Sollya/FPTaylor (this
repository certifies values, not floating-point program transformations;
Arb subsumes the need — the same reasoning that rejected Gappa).

**Practice, not adoption:** Loogle is a search engine for Mathlib and
costs nothing to use during Lean work; use it.

## Consequences

- The one actionable output that fires today is aim, not installation:
  **G11's near-Gamma touching gates are the next migration target for
  workhouse.rigor** — the survey looked for a tool for G11 and the honest
  answer is that ADR 0010 already adopted it. Interval-certifying those
  gates needs no new dependency.
- The certified-enumeration pipeline is the standing answer to "how will
  the G3 engine's completeness be trusted at scale," recorded before the
  scale exists.
- Same failure mode named as ADR 0010: tool accretion by plausibility.
  Two surveys, twenty-plus candidates, one installed library — because
  exactly one upgraded a check that exists.
