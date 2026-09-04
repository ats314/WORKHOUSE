# Private-link paths as single links, and universality history by history — 2026-09-04

The first two steps of the plan for proving the channel-wise universality
behind the tier collapse (G14), run over ℚ(N) with `workhouse.symbolic_rank`.

## Part 1: the path-reduction lemma, used

A face's private links — those in no other face of the cluster — enter every
history word only through their product along the face, and by Peter–Weyl
`D^r(U_a U_b U_c) = D^r(U_a) D^r(U_b) D^r(U_c)`: the links of a private path
always carry one and the same irrep, so the path is one Haar link whose
single-link `H0` is `k` times the usual one, `k` its length.
`loopcalc.reduced_words` collapses every maximal private run to such a link
and records `k` in `LINK_WEIGHT`; `Cluster(faces, reduced=True)` builds the
cluster from the collapsed words. The eight three-face clusters of the β_N
assembly, recomputed channel by channel on the reduced cluster:

| cluster | effective links (weights) | C-odd channels | C-even channels | full → reduced |
|---|---|---|---|---|
| straight chain (u) | 3, 3 | 74 = 74 | 122 = 122 | 55 s → 8 s |
| L chain (u) | 2, 3, 3 | 74 = 74 | 122 = 122 | 56 s → 6 s |
| bent chain (u) | 3, 3 | 74 = 74 | 122 = 122 | 56 s → 8 s |
| single contact, perpendicular | 2, 3, 3 | 92 = 92 | 164 = 164 | 65 s → 9 s |
| single contact, coplanar | see certificate | 92 = 92 | 164 = 164 | 33 s → 9 s |
| fan, perpendicular | see certificate | 84 = 84 | 138 = 138 | 61 s → 5 s |
| fan, coplanar | see certificate | 84 = 84 | 138 = 138 | |
| corner | see certificate | 87 = 87 | 141 = 141 | 59 s → 16 s |

Every channel of both sectors is the same rational function of N on the
reduced cluster as on the full one, and the totals agree
(`certificate.json`, `reduced_vs_full`). The reduced clusters are the ones a
proof can be written on: two shared links and a few weighted private ones.

## Part 2: universality history by history

The C-odd direct term of a cumulant is tagged by the time-ordered sequence of
the four inserted faces as well as by the channel labels of its three
intermediate states, on the reduced clusters.

- **The two-hop weight.** The straight chain and the L chain have the same 32
  insertion sequences and the same 124 (sequence, channel) terms, and every
  term agrees with ratio 1. Universality is not a property of sums over
  histories: it holds for each history type separately.
- **The single-contact dressing.** The straight chain dresses Q, the L chain
  dresses P. With the roles read as they stand, no term of one geometry
  matches any of the other; reversing time (the sequence and the labels)
  alone matches none either; reversing time, swapping the two end roles and
  conjugating one end face matches all 128 terms with ratio −1, the incidence
  sign. This is the history-level form of the corrected channel comparison
  of ADR 0029.

## Part 3: integrand by integrand

For every one of the 124 (sequence, channel) terms of the two-hop weight, the
final integrands — the words whose Haar integrals the term sums, each taken
with its coefficient times its integral — are compared between the straight
and the L chain as multisets of values. They coincide in every term, although
the words themselves never do (the middle face's private links are two links
of weight one in the straight chain and one link of weight two in the L
chain). So the two geometries' history expansions are in value-preserving
bijection integrand by integrand. That is the level at which the proof has to
work, and the difference it has to explain is one splitting: in the straight
chain the middle face's two private links close the two shared-link letters
through two separate Haar contractions, in the L chain through one, and the
extra factor `1/N` of the second contraction is paid back by one extra closed
index loop.

## Files

| File | What it is |
|---|---|
| `reduce.py` | the run, about fifteen minutes on one CPU |
| `console.log` | its complete output |
| `certificate.json` | parts 1 to 3: the channel comparisons, the history comparisons under each candidate correspondence, the integrand comparison |
| `SHA256SUMS` | the pin |
