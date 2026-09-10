# T0: the only tier a document cannot argue with

A theorem here is proof-checked: Lean 4 compiles it, no `sorry`, standard axioms
only (`propext`, `Classical.choice`, `Quot.sound`). Nothing else in this
repository has that standing.

`make lean` builds it, with `--wfail` so a `sorry` fails rather than warns.
`make lean-setup` installs elan and the pinned toolchain first; see `README.md`.

## What belongs here

Formal statements from the research derivations, including rational and
polynomial algebra, Hilbert and Banach operators, measure-theoretic limits,
Dirichlet forms and their dependencies. The maintainer's September 9 request
explicitly extends the earlier algebra-only scope. Preserve precise hypotheses
and build the actual mathematical objects required by each statement.

If an invariant in `src/workhouse/invariants/` is exactly a formalized statement,
prefer promoting it rather than leaving it at T1. A useful abstract operator
lemma must state its remaining Wilson-specific realization inputs; it does not
by itself formalize a complete source document.

## What does not

Do not axiomatize a physics assumption to get a compiling theorem. The point of
formalizing is to *expose* the hypothesis an informal derivation left out; an
axiom that hides it inverts the exercise.

## A known shape

`rank_law_numerator` and `hopping_deficit_numerator` are stated with
denominators cleared, because `field_simp` left an uncleared inverse. That is a
tactic limitation, not a mathematical one — the cleared form is equivalent and
provable.
