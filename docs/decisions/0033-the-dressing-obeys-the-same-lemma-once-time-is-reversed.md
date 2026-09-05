# 33. The single-contact dressing obeys the same lemma, once time is reversed

Date: 2026-09-04. Status: accepted. Extends ADR 0032 from the two-hop weight to
the single-contact dressing; bears on G14, C2.

## Context

ADR 0032 proved, by exhaustion on the fourth-order family, that the two-hop
weight `u` is one function of N on both chain geometries: a map φ on words sends
each straight integrand to its L integrand with the same Fierz coefficient, and
the Haar integral is φ-invariant on every word the Fierz rewirings can generate.
It listed the single-contact dressing as the next case, with the remark that the
same argument applies. That remark was not checked, and the first attempt to
check it failed.

## What failed, and why

The natural comparison, the L cluster's integrands against the straight
cluster's under ADR 0030's correspondence (reverse time, swap the end roles,
conjugate one end face), agreed term by term as ADR 0030 found, but the
integrands paired off with equal coefficient and equal Haar value in only 52 of
the 128 (sequence, channel) terms. Refining the channel labels by which link
carries the non-fundamental irrep changed nothing: 128 of 128 fine channels
agree, 52 of 128 pair off. For a while this read as the dressing's identity
living one level up, a sum over the Fierz expansion rather than a word-by-word
identity.

It was the staging. A history's integrands are the words left after the
resolvent projectors are expanded, and which words appear depends on which side
of the amplitude each expansion is written on, though the sum never does. The
engine writes two expansions on the ket side and one on the bra side. The
correspondence reverses time. Staging the straight cluster from the other end,
one expansion on the ket side and two on the bra side, every one of the 128
terms pairs off, 560 integrands, and every integrand has the Haar integral of
its image over ℚ(N). The 52 is kept in the record as what it was.

## The lemma for the dressing

Each geometry has one face carrying both shared links, the hub: straight
`Q = Tr(U_e† A U_x B)`, L `P = Tr(U_e U_x C)`, the two-hop chain's middle face
again, but here an end of the cumulant rather than the inserted face. **φ**:
delete `A, A†`; rename `B, B†` to `C, C†`; reverse the link `e`; conjugate. The
map is built from the roles read off the reduced words. The abstract family is
ADR 0032's with the roles of the two shared links exchanged, and the mirror
image (reverse every cycle, exchange the links) carries the one onto the other
and φ onto φ; `runs/dressing_lemma_2026-09-04` runs the family directly all the
same, on the same counts as the two-hop record (576, 17,280, 17,280, a
one-percent sample of 518,400; 384, 2,052, 2,052), every word φ-invariant, the
control failing as it should.

## What this settles

Every universality the fourth-order assembly uses now rests on one finite,
checked identity of Haar integrals on the Fierz-reachable family: the two-hop
weight, which carries the tier collapse `D = 0` (ADR 0032), and the
single-contact dressing, which carries the `32d` of
`β_N = −16u + 32d − 16·corner + 848/(N(N²−1)³)` (ADR 0029). The corner has no
partner geometry to be universal against, and the fan cancels out of `β_N`
altogether. The fan's own channel-by-channel agreement (ADR 0029) is a different
kind of statement, an exchange of the end and dressing roles on a single cluster
of three faces around one link, and is not needed anywhere; it is not pursued.

## What is not proved

- The lemma for arbitrary `a, c`, as for the two-hop weight. The natural
  conjecture is that it holds at every multiplicity; an inductive proof would
  carry both universalities to every order at once, since the two families are
  mirror images.
- A closed-form reason. Both exhaustions say the identity is true on the family
  and false outside it, not why in one line.

## Decision

- A sixth check in the suite "private-link paths as single links; universality
  history by history" reads the record.
- G14's universality route stays `live`, now closed at fourth order for both the
  two-hop weight and the dressing, with the general-order statement as what
  remains.

## Consequences

- `runs/dressing_lemma_2026-09-04`; the check; this ADR.
- The lesson, for the next comparison of two geometries: when the
  correspondence reverses time, stage the histories from the matching end
  before concluding anything about the integrands.
- Next: the inductive lemma over the multiplicities, on the mirror-symmetric
  family, and the three-hop chains at sixth order on the reduced clusters.
