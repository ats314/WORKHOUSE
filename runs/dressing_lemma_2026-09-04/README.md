# The single-contact dressing obeys the two-hop lemma, once time is reversed — 2026-09-04

ADR 0032 proved the universality of the two-hop weight `u` on the fourth-order
family and left the single-contact dressing `d` as "the same φ-type argument
applies", unverified. This run verifies it, and records the one thing that had
to be understood first: which way to stage the histories.

## The setting, on the reduced clusters

Each single-contact geometry has one face carrying both shared links, the
**hub**; the other end face is its neighbour across the link `e`, the dressing
`X` its neighbour across the link `x`. In the coplanar (straight) cluster the hub
is `Q = Tr(U_e† A U_x B)`, two private links of weight one; in the perpendicular
(L) cluster it is `P = Tr(U_e U_x C)`, one private link of weight two. This is
the two-hop chain's middle face again, except that the hub is an **end** of the
cumulant, not the inserted face. ADR 0030's correspondence between the two
dressings reverses time, swaps the end roles and conjugates one end face, and
found them equal history by history up to the incidence sign.

**φ** on straight words: delete `A` and `A†`, joining each one's predecessor to
its successor; rename `B, B†` to `C, C†`; reverse the letters on the link `e`;
conjugate the whole word. The reversal is a relabelling the Haar integral does
not see; the conjugation is the time reversal, and the integrals are real.

## The staging

A history's integrands are the words left after the resolvent projectors have
been expanded; which words appear depends on which side of the amplitude each
expansion is written on, though their sum does not. The correspondence reverses
time, so the straight cluster has to be staged from the other end: one resolvent
expansion on the ket side and two on the bra side, against the L cluster's two
and one. Staged that way, every term's integrands pair off. Staged naively (two
on the ket side for both), the (coefficient, value) multisets agree in only 52
of 128 terms while every term's total agrees; that number is kept in the
certificate as the artifact it was.

## What is checked

- **Part A: φ is the history correspondence.** For every one of the 128
  (sequence, channel) terms of the C-odd direct term, φ maps the straight
  cluster's integrands bijectively onto the L cluster's with the same
  coefficient up to the incidence sign `−1`: 560 integrands, 128 of 128 terms.
  Every one of the 560 integrands has the same Haar integral as its image, over
  ℚ(N). The map is built from the roles read off the reduced words, not typed.
- **Parts B and C: the family.** The abstract family is
  `runs/universality_lemma_2026-09-04`'s with the roles of the two shared links
  exchanged: hub letters `x_e → A → x_x → B → x_e`, neighbours `E^a Ē^a` on the
  link `e` and `X^c X̄^c` on the link `x`, every permutation of out-targets within
  a shared link (a superset of the Fierz like-pair swaps), then the Fierz cuts of
  unlike pairs a history can bring into one projected state, an emptied cycle
  counted as a loop of N. `∫ w = ∫ φ(w)` on all of it: swaps `a = c = 1`
  exhaustively (576 words, two ranks and ℚ(N)), `(2, 1)` and `(1, 2)`
  exhaustively (17,280 each), `(2, 2)` on a one-percent sample of the 518,400;
  cuts `a = c = 1` exhaustively (384), `(2, 1)` and `(1, 2)` on ten-percent
  samples of the swaps (2,052 each).
- **Part D: the control.** On arbitrary wirings of the same letters φ does not
  preserve the integral: 96 of 300 random wirings at `a = c = 1` and 29 of 300 at
  `(2, 2)` happen to agree, the rest do not. The identity is a property of the
  family, not of the map.

The mirror image (reverse every cycle, exchange the two links) carries this
family onto the two-hop family and this φ onto that lemma's φ, so parts B to D
are the two-hop lemma's mirror; they are run here directly rather than argued.

## What this proves

The single-contact dressing is one rational function of N on both geometries,
`d_perp = −d_cop` channel by channel, for the same reason the two-hop weight
is: a finite identity of Haar integrals on the Fierz-reachable family. With ADR
0032, every universality the fourth-order assembly uses rests on that one
identity; the corner has no partner geometry, and the fan drops out of `β_N`
altogether (ADR 0029). The assembly `β_N = −16u + 32d − 16·corner + 848/(N(N²−1)³)`
takes its `32d` from this.

What is not proved: the identity for arbitrary `a, c`, which higher orders need,
and a closed-form reason. Both are as for the two-hop weight.

## Files

| File | What it is |
|---|---|
| `lemma.py` | the run; `PARTS` selects parts, `OUT_SUFFIX` names the certificate |
| `console.log` | its complete output |
| `certificate.json` | parts A to D with every count, φ described from the roles |
| `SHA256SUMS` | the pin |
