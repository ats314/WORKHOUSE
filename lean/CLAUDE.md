# T0: the only tier a document cannot argue with

A theorem here is proof-checked: Lean 4 compiles it, no `sorry`, standard axioms
only (`propext`, `Classical.choice`, `Quot.sound`). Nothing else in this
repository has that standing.

`make lean` builds it. Needs `elan` on PATH; see `README.md`.

## What belongs here

Pure rational and polynomial algebra — the rank law, the deficit identity, the
sealed-core arithmetic. If an invariant in `src/workhouse/invariants/` is
exactly that, prefer promoting it rather than leaving it at T1.

## What does not

Do not axiomatize a physics assumption to get a compiling theorem. The point of
formalizing is to *expose* the hypothesis an informal derivation left out; an
axiom that hides it inverts the exercise. The corpus's own note is blunt about
this: an unfinished or axiomatized mass-gap statement in a Lean tree is not
evidence.

## A known shape

`rank_law_numerator` and `hopping_deficit_numerator` are stated with
denominators cleared, because `field_simp` left an uncleared inverse. That is a
tactic limitation, not a mathematical one — the cleared form is equivalent and
provable.
