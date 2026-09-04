# 22. Sector-wise monotonicity in the coupling runs the wrong way for the gap

Date: 2026-09-03. Status: accepted — a negative result, recorded per ADR 0005.

## Context

Alex proposed, in conversation, the one route across the coupling axis that
had not been pushed to the end. A proof of the gap at weak coupling does not
need to control the vacuum in between; it needs an inequality — a
monotonicity or a correlation bound — that holds at every `β` and carries the
gap from small `β`, where the strong-coupling series proves it, to large `β`.
Griffiths' inequalities do exactly this for Ising: a correlation that is
nondecreasing in `β` and positive at `β_0` stays positive above `β_0`, and
that is how Ising results cross phases. The known obstruction is that the
inequalities fail for non-abelian groups — but they fail for Wilson-loop
observables. The electric-flux free energies `F_e(β, L)` of 't Hooft's
sectors are `Z_N`-valued, center-symmetry objects, abelian in the way the
inequalities need. Nobody had asked whether they are monotone in `β`, sector
by sector; if they are, strong coupling proves the whole axis.

The question has a yes/no answer, and this repository holds the exact
strong-coupling sector data to attack it. Nothing in the corpus had tried it:
the only "Griffiths" and "Ginibre" hits in 950 files are Ginibre-matrix Haar
sampling in notebooks.

## What was computed

Three T1 checks in `src/workhouse/invariants/string_tension.py`, all from the
certified series and symbolic where the rank allows. They do not attempt the
inequality. They read off the one thing the argument needs from it, which is
its direction.

1. **The leading flux gap decreases in `u` for every `N`.** One unit of
   electric flux through a straight winding line of length `L` charges `L`
   links in the fundamental at `(g²/2) C_F` each, and `g² = u^{-1/2}`, so the
   zeroth-order sector gap is `C_F L / (2√u)` with derivative
   `-(N²-1) L / (8N u^{3/2})`. Symbolic in `N`, `u`, `L`; the numerator
   factors as `(N-1)(N+1)L`, positive for `N ≥ 2`. At `N = 3` it is
   `σ_0 L/√u` with `σ_0 = 2/3`.

2. **Through fifth order the direction survives every correction.** The
   gap per unit length is `u^{-1/2} σ(u) = Σ σ_n u^{n-1/2}`, so its slope is
   `Σ (n - 1/2) σ_n u^{n-3/2}`. With `σ_0 > 0` and every certified
   `σ_2, …, σ_5 < 0`, all five slope coefficients are negative:
   `-1/3, -11/51, -305/816, …`. Every term is negative on **all** of
   `u > 0`, so the truncated gap decreases on the whole half-line, not only
   near `u = 0`, and the same derivative comes out of the Kogut–Pearson–
   Shigemitsu coordinate `x = 2u`. The check rests on the two parity checks
   that fix the signs of `σ_3` and `σ_5`, because a parity slip there would
   flip two of the five terms.

3. **Reweighting is not a repair.** Multiplying by `u^k` makes the leading
   slope `(k - 1/2) σ_0`, positive for every `k ≥ 1`. So the small-`u`
   direction of any polynomially weighted gap is chosen by the weight, and
   whether it keeps increasing at large `u` is the continuum question itself
   (G19's necessary scaling law sends the lattice gap to zero faster than any
   power of `u`). An increasing weighted gap at strong coupling carries no
   information about weak coupling.

## Decision

The route closes `dead` on G19, `cannot_decide: [G19]`, before the inequality
itself was attempted, because a sign settles it.

The Ising argument transports a quantity that **increases** in `β`: order
established at `β_0` persists above it. Confinement is the small-`β` phase.
The electric-flux gap, in lattice units, **decreases** in `β` from its very
first term and at every certified order after. So a sector-wise monotonicity
in `β`, if it holds at all, is monotone decreasing, and a decreasing quantity
that is positive at small `β` is bounded **above** at large `β` by its
strong-coupling value and bounded below by nothing. It cannot establish a gap
at weak coupling. This is independent of whether the group is abelian: where
Griffiths' inequalities do hold — Ising, `Z_N` gauge fields — they carry the
*ordered* (deconfined, twist-expensive) phase upward in `β`, which is the
wrong phase for a confinement proof. By 't Hooft's electric–magnetic duality
the magnetic (twist) free energies run the other way, and that direction
proves that deconfinement, once present, persists to larger `β` — a true and
useless statement for the gap. That last paragraph is T3 reasoning; only the
sign of the electric gap is checked.

What is **not** settled: whether `F_e(β)` is in fact monotone in `β` for
`SU(N)`. It is left open, and it is now irrelevant to G19.

**Falsifier for the closure** — what would revive the route: a functional of
the sector free energies, defined without knowledge of the large-`β`
behaviour, that is increasing in `β` at small `β` **and** whose positivity at
large `β` implies a gap. The three checks say no polynomial weight is one.
An exponential weight `e^{c√u}` with `c` tuned to G19's scaling law is
circular. Nothing else is known.

## Consequences

- `ledger/gaps.yaml`: G19 carries its first `plan` step, `dead`,
  `closed_by` the three checks and this ADR, `cannot_decide: [G19]`.
- `literature/index.yaml`: `T_HOOFT_1979` (the sector definitions,
  `supplies-method`, not yet obtained) and `GINIBRE_1970` (the inequality,
  `confusable` — recorded so the analogy is not re-proposed as a route).
- The string-tension suite yields `FLUX_GAP_SLOPE_0 = -1/3` and
  `SIGMA_SLOPE_2 = -11/51`, so `workhouse search` reaches the direction by
  value.
- No sector census was consumed. The census would have been needed for the
  inequality itself; the sign was cheaper, which is the *Prefer decisive
  calculations* rule of `AGENTS.md` doing what it is for.
