# 32. The universality lemma of the two-hop weight, proved by exhaustion on the fourth-order family

Date: 2026-09-04. Status: accepted. Closes, for fourth order, the route on G14
that ADR 0029 opened and ADR 0030 and ADR 0031 sharpened; bears on G14, C2.

## Context

The tier collapse `B = D = 0` of the fourth-order kernel is the Hodge form of
ADR 0019 plus one dynamical input: the two-hop weight `u` is one function of N
on every two-hop chain geometry. ADR 0029 established that as an identity in
ℚ(N) channel by channel; ADR 0030 found it holds history by history and
integrand by integrand; ADR 0031 located it as an identity of Haar integrals
of words that differ only in the middle face's private structure, and asked for
the finite case analysis.

## The lemma

On the reduced clusters the two chains share `P = Tr(U₁ W_P)` and
`R = Tr(U₂ W_R)`. The straight middle face is `Tr(U₁† A U₂ B)`, two private
links of weight one; the L middle face is `Tr(U₁† C U₂†)`, one private link of
weight two in `A`'s place, the second shared link traversed the other way.
Define **φ** on words: delete `B, B†`, joining predecessor to successor; rename
`A, A†` to `C, C†`; reverse the second shared link.

> **Lemma.** Let `w` be any word obtained from `P^a P̄^a R^b R̄^b X X̄` by permuting the
> out-targets of the letters on one shared link among themselves (the Fierz
> swaps act on like pairs; every permutation is allowed here) and then applying
> Fierz cuts to unlike pairs of shared-link letters that a history can bring
> into one resolvent-projected state (so never X's own letter against X̄'s), each
> cut rewiring the two wires across and counting an emptied cycle as a loop of
> N. Then `∫ w = ∫ φ(w)`.

For `a, b ≤ 2`, the multiplicities fourth order reaches, the lemma is checked
on the family (`runs/universality_lemma_2026-09-04`): every swap word for
`a = b = 1` (576, at two ranks and over ℚ(N)), `(2, 1)` and `(1, 2)` (17,280
each); every cut word for `a = b = 1` (384) and ten-percent samples for `(2, 1)`
and `(1, 2)`; a one-percent sample of the 518,400 swap words of `(2, 2)`. Every
word passes. Two controls locate the lemma's scope: on arbitrary wirings of the
same letters φ does not preserve the integral, and cutting X's letter against
X̄'s, which no history can do because they sit on opposite sides of the
amplitude, breaks it as well. The identity is a property of the family the
Fierz rewirings generate, not of the map.

## Why the lemma is the mechanism

In every surviving fourth-order history the middle face appears once on each
side of the amplitude: a history with `X X̄` on one side leaves the private
links in the adjoint after the resolvent, and the final integral kills it. So
the private letters are never projected, the Fierz rewirings act on the
shared-link letters only and identically in both geometries, and every
integrand of the straight chain is a word of the family. Part A of the record
checks that φ is exactly the correspondence the histories induce: in all 124
(sequence, channel) terms it maps the 536 straight integrands bijectively onto
the L integrands with the same coefficient. With the lemma, every term of the
two-hop weight agrees between the geometries, hence every channel, hence
`u_L = u_straight`, hence `u₂ = 2u`, hence `D = 0`; `B = 0` is the carrier
projection. The tier collapse at fourth order now rests on the incidence
algebra of the cubical complex and a finite, checked identity of Haar
integrals.

## What is not proved

- The lemma for arbitrary `a, b`. The family grows with the order; sixth order
  reaches `a, b ≤ 3`, and the `(2, 2)` case and the larger cut families are
  sampled rather than exhausted.
  The natural conjecture is that the lemma holds for all `a, b`; an inductive
  proof would move the mechanism from "checked at fourth order" to "proved at
  every order".
- The same statement for the single-contact dressing and the fan. Their
  history-level agreement is verified (ADR 0030) and the same φ-type argument
  applies, but this record covers the two-hop weight only.
- A closed-form reason. The exhaustion shows the identity is true on the
  family and false outside it; it does not say in one line why. The two-rank
  agreement is proof for each word because the integrals are rational
  functions of N of degree bounded by the Weingarten sums involved, but the
  reader who wants the identity as a formula does not have it yet.

## Decision

- A fifth check in the suite "private-link paths as single links; universality
  history by history" reads the record.
- G14's universality route is `live`: closed at fourth order for the two-hop
  weight by this record, with the general-order statement and the dressings
  as what remains.

## Consequences

- `runs/universality_lemma_2026-09-04`; the check; the route; this ADR.
- Next: the inductive proof over `a, b`, the same construction for the
  single-contact dressing and the fan, and the three-hop chains at sixth order
  on the reduced clusters, where the family and the lemma are tested together.
