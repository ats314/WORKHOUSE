# 30. Private-link paths are single links, and universality holds history by history

Date: 2026-09-04. Status: accepted. Runs the first two steps of the plan
opened by ADR 0029 for proving the channel-wise universality behind the tier
collapse; bears on G14. Corrects one reading of ADR 0029 within the same day.

## Context

ADR 0029 found the two-hop weight, the fan and the single-contact dressing
universal channel by channel across the cluster geometries they occur in,
as identities in ℚ(N), and asked for a proof from the Haar contraction. The
plan: collapse each cluster to the smallest model that computes the same
thing, locate the whole difference between two geometries in one object,
and find the level at which the identity holds.

## What was done

**The path-reduction lemma.** A face's private links enter every history
word only through their product along the face, so by Peter–Weyl the links of
a private path always carry one and the same irrep, and the path is one Haar
link whose single-link `H0` is `k` times the usual one. `loopcalc.reduced_words`
collapses every maximal private run to such a link (`LINK_WEIGHT`), the
single-link `H0` and the spectra are scaled by the weight, and channel labels
count a weight-`k` link `k` times. Recomputed on the reduced clusters over
ℚ(N), all eight three-face cumulants of the β_N assembly are the same channel
by channel in both sectors, five to ten times faster
(`runs/path_reduction_2026-09-04`, part 1). The reduced two-hop chains are:
two shared links, two end paths of weight three, and the middle face's
private links — two links of weight one in the straight chain, one link of
weight two in the L chain. That is the whole difference between the two
geometries.

**Universality history by history.** Tagging the direct term by the
time-ordered sequence of the four inserted faces as well as by the channel
labels, the straight and the L chain agree in every one of their 124
(sequence, channel) terms, ratio 1 (part 2). Finer still, within every term
the final integrands — coefficient times Haar integral — form the same
multiset of values in both geometries, although the words never coincide
(part 3). Universality is a value-preserving bijection of integrands, not a
coincidence of sums, and the object a proof has to handle is the one
splitting: two private contractions closing the shared-link letters in the
straight chain against one in the L chain, the second contraction's `1/N`
paid back by one extra closed index loop.

**The single-contact dressing, corrected.** ADR 0029 first recorded the
single-contact dressing as "universal only in sum", with 24 exceptional
channels cancelling across the two geometries. That reading paired the
channel labels naively, and the labels list the intermediate states in time
order from the ket end while the straight chain dresses Q and the L chain
dresses P. Reversing time, swapping the two end roles and conjugating one
end face, all 128 (sequence, channel) terms agree with ratio −1, and at the
channel level all 92 C-odd and 164 C-even channels do. The correction is in
ADR 0029's own check and text; this ADR records where it came from.

## What it means

With every cumulant of β_N universal integrand by integrand, the mechanism of
the tier collapse is one lemma about one face: a word `Tr(U₁ A U₂ B†)` with
two independent private links behaves, under every Fierz rewiring with the
shared-link letters of its neighbours and the final Haar integration,
exactly like `Tr(U₁ U₂ C†)` with one private link of double weight. The
energies match by the path lemma; the Haar values match because a private
link that appears once with its conjugate contracts as `δδ/N` and the extra
contraction closes one more loop. Written out, that is the proof; it has not
been written out.

## Decision

- `loopcalc.reduced_words`, `LINK_WEIGHT`, `link_weight`; `Cluster(...,
  reduced=True)`; `cumulant(..., reduced=True)`; `symbolic_rank.channels(...,
  reduced=True)` with weighted labels; `tests/test_path_reduction.py`.
- Suite "private-link paths as single links; universality history by
  history": three T1 checks reading the record, one recomputing the reduced
  chain live at N = 3.
- G14: the route "prove channel-wise universality from the Haar contraction"
  gains its reduced statement; the run is registered.

## Consequences

- The reduced clusters make sixth order tractable: the three-hop chains
  collapse the same way.
- The next step is the written proof of the one-face lemma, and its Lean
  form for the Weingarten arithmetic.
