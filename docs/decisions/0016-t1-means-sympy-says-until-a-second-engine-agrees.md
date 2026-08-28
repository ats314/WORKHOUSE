# 16. T1 meant "sympy says" until a second engine agreed

Date: 2026-08-28. Status: accepted. Extends ADR 0010.

## Context

`CLAUDE.md` defines T1 as "re-derived symbolically from stated definitions,
exactly". Read carefully, that sentence has a hole in it: *by what?* Every
exact value in this repository — every all-rank law, every registered rational,
every `simplify(lhs - rhs) == 0` — came out of one library. A `cancel` that
dropped a factor, a `Rational` that normalised wrongly, a `diff` that lost a
term: any of those would produce a wrong exact value that 210 checks would
agree with unanimously, because they all ask the same engine.

That is the same shape as trusting a single proof kernel, which is the argument
`lean4checker` exists to answer at T0. ADR 0010 already settled the principle
for adopting a tool: **a tool earns adoption only if it serves a tier
transition an open claim actually needs**, and it adopted python-flint for
exactly that reason at T2, where Arb enclosures replaced asserted float
precision with a machine guarantee.

The same dependency, already declared, supplies the missing evidence class one
tier up. flint has no `simplify` — but it has univariate polynomial arithmetic
with exact gcd, and that is enough, because a rational function is a pair of
polynomials and two of them are equal exactly when their normal forms are.

## Decision

**`src/workhouse/cross_check.py` recomputes the T1 layer in flint, and
`workhouse verify --cross-check` shows the table.**

1. **`Rat` is a rational function over Q on `fmpq_poly`**, normalised on
   construction by exact gcd with a monic denominator, so `==` is structural
   equality of normal forms rather than a cross-multiplication at comparison
   time. A zero denominator raises; it does not propagate. Denominator
   normalisation rescales numerators, so a claim about a *numerator* — the
   monotonicity cubic — is checked by exact division, not by comparing two
   polynomials that need not be the same one.

2. **Independent construction is declared per witness, not assumed.** Eighteen
   of the twenty-seven are typed out from the corpus's own printed closed
   forms and read no sympy expression at all; the other nine re-normalise a
   value sympy produced, which still witnesses `cancel` and is a weaker thing.
   The distinction is a field on the record and it is printed, because "27
   agree" would otherwise read as twenty-seven independent derivations.

3. **What crosses the boundary is coefficients.** Where a sympy expression has
   to be compared, `fraction(together(expr))` puts it over a common denominator
   — `together` does not cancel, so no trust is placed in the operation under
   test — and `Poly.all_coeffs()` reads the coefficients off. Everything after
   that is flint.

4. **A negative control is registered as a check.** A comparison that cannot
   fail proves nothing about the thing compared, so one of the four checks
   shows the engine *rejecting* a deliberately wrong construction (`t_N` with
   `4N**2-9` mistyped as `4N**2-8`) and *accepting* the same law written over
   an expanded denominator — and records that the wrong law agrees with the
   right one at 0 of 7 sampled integer points, so the comparison is structural
   rather than a sample.

## Consequences

**What this witnesses: the arithmetic.** A bug in `Rational`, `cancel`,
`together`, `diff` or `simplify` that produced a wrong exact value would be
caught, because flint recomputes the same quantity through entirely different
code and the two normal forms would differ.

**What it does not witness: the derivation.** If a formula in `constants.py` is
the wrong formula, both engines compute the same wrong thing, exactly, and
agree. This is a witness, not a proof, and the module says so in its first
paragraph rather than leaving a reader to work it out. It does not create a
tier, it does not promote anything, and a witness disagreement would be a
`FINDING`, not a repair.

**Coverage is honest about its own edges.** The witnesses cover the all-rank
laws, the one derivative claim, and the registry values that the corpus gives a
*formula* for. A constant the corpus states only as a literal is deliberately
absent: there is no second derivation to disagree with, and listing it would
inflate the count with rows that cannot fail. Checks whose content is a set
equality, a count, or a file digest are not algebra and are out of scope.

**Nothing about C2 moves.** `C_shp (historical)` is among the recomputed
values, from its own stated `(beta_pen - 2 alpha_3)/16`. That re-derives the
historical side from the historical side's formula and says nothing whatever
about the v10a.26 side, which has no formula to re-derive. C2 stays open.

## What was refused

A third engine. Two disagreeing engines localise a bug; three would mostly add
install cost. A `simplify` on the flint side — there isn't one, and the point
is that there doesn't need to be. And a claim that this makes T1 into T0: the
tier vocabulary is closed, `AGENTS.md` forbids a fourth, and two agreeing
computer algebra systems are still two computer algebra systems.
