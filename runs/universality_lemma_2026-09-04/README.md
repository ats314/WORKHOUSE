# The universality lemma of the two-hop weight, proved by exhaustion on the fourth-order family — 2026-09-04

The last unexplained input of the tier collapse (G14) was that the two-hop weight
`u` is the same rational function of N on the straight and on the L-shaped chain.
ADR 0030 found this holds history by history, ADR 0031 that it is an identity of
Haar integrals of words differing only in the middle face's private structure.
This run proves that identity on the whole family of words a fourth-order
history can produce, by exhaustion, and checks that the family is the right one.

## The setting, on the reduced clusters

Both chains have `P = Tr(U₁ W_P)` and `R = Tr(U₂ W_R)` with `W_P, W_R` the
weight-three end paths. The straight middle face is `X_S = Tr(U₁† A U₂ B)` with two
private links of weight one; the L middle face is `X_L = Tr(U₁† C U₂†)` with one
private link of weight two, sitting where `A` sits, and the second shared link
traversed the other way. In every surviving history the middle face appears once
on each side of the amplitude (the histories with `X X̄` on one side have their
private links in the adjoint after the resolvent and integrate to zero), so the
private letters are never projected and the Fierz rewirings act on the shared-link
letters only, identically in the two geometries.

**φ** acts on words: delete `B` and `B†`, joining each one's predecessor to its
successor; `A, A†` become `C, C†`; reverse the second shared link.

## What is checked

- **Part A: φ is the history correspondence.** For every one of the 124
  (sequence, channel) terms of the C-odd direct term, φ maps the straight chain's
  integrands bijectively onto the L chain's with the same coefficient: 536
  integrands, 124 of 124 terms.
- **Part B: the swap family.** Starting from the product of face words
  `P^a P̄^a R^b R̄^b X X̄`, every permutation of the out-targets among the letters on
  one shared link (a superset of what the Fierz like-pair swaps generate) gives a word `w`, and
  `∫ w = ∫ φ(w)` for every one of them: `a = b = 1` exhaustively (576 words, at two
  ranks and over ℚ(N)), `(a, b) = (2, 1)` and `(1, 2)` exhaustively (17,280 words
  each), `(2, 2)` on a one-percent sample of the 518,400.
- **Part C: the cut family.** A Fierz cut acts on an unlike pair of shared-link
  letters: the wire into each continues to the other's successor, both letters go,
  and an emptied cycle is a closed index loop worth N, counted here as the engine
  counts it. The pairs a history can cut are those that can share a
  resolvent-projected state, so never X's own letter with X̄'s, which sit on
  opposite sides of the amplitude. Every set of up to two such cuts per link on
  top of every like-pair swap: `a = b = 1` exhaustively (384 words at two ranks),
  `(2, 1)` and `(1, 2)` on a ten-percent sample of the swaps (2,052 words each).
  `∫ w = ∫ φ(w)` throughout. Cutting X's letter against X̄'s, which no history
  does, breaks the identity; so does swapping a U with a U†.
- **Part D: the control.** On arbitrary wirings of the same letters, φ does not
  preserve the integral: most random wirings disagree. The lemma is a property of
  the family the histories generate, not of the map.

## What this proves

For the fourth-order two-hop weight: every history's straight-chain integrand and
its L-chain image have the same Fierz coefficient (part A) and the same Haar
integral (parts B and C cover every word the family contains for the
multiplicities fourth order reaches, `a, b ≤ 2`). Summing over histories,
`u_L = u_straight` channel by channel, as ADR 0029 computed. Together with the
Hodge form of the kernel (ADR 0019) this makes the tier collapse `B = D = 0` a
theorem whose only computational input is now a finite, exhaustively checked
identity rather than a rank sweep or a symbolic evaluation of the cumulant.

What is not proved: the identity for arbitrary `a, b`, which sixth and higher
orders would need. The exhaustion is over the fourth-order family; the general
statement is the natural inductive extension and is stated as G14's next step.

## Files

| File | What it is |
|---|---|
| `lemma.py` | the run; `PARTS` selects parts, `OUT_SUFFIX` names the certificate |
| `console.log` | its complete output |
| `certificate.json` | parts A to D with every count |
| `SHA256SUMS` | the pin |
