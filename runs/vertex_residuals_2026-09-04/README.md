# Where the universality identity lives — 2026-09-04

ADR 0030 found the two-hop weight universal between the straight and the
L-shaped chain history by history and integrand by integrand. This run asks at
which point of the contraction the two geometries become literally the same
word, so that the lemma to prove is stated about the right object.

## What is computed

For every one of the 124 (insertion sequence, channel) terms of the C-odd
direct term, on the reduced clusters over ℚ(N): every final integrand is taken
with its coefficient; some of its links are Haar-integrated with the engine's
own `haar_link` (each is a balanced n = 1 family, so the integration is the cut
`δδ/N`); adjacent `U U†` pairs of one link inside a trace are cancelled
(unitarity, an emptied trace being a factor N); and the residual words, written
over the role alphabet `l1, l2` (the shared links), `wP, wQ` (the end paths),
are summed with their coefficients and compared between the geometries.

| links integrated | residual vectors equal | totals equal | distinct residual words |
|---|---|---|---|
| the middle face's private links | 14 of 124 | 124 of 124 | see `certificate.json` |
| the middle face's private links and both end paths | **124 of 124** | 124 of 124 | the same set in both geometries |

## What it says

- The middle face's contribution is **not** the same function of its two
  shared links and the end paths in the two geometries. After its private
  links are integrated, the L chain carries words in which the end paths are
  threaded through one trace together with both shared links, and the straight
  chain does not; only the totals agree.
- Once the end faces' private paths are integrated as well — each closes its
  face's two shared-link letters into a hairpin — the residual is a formal word
  in the two shared links alone, and it is **the same word with the same
  coefficient in every term**, with no orientation flip.

- The third stage takes no integral: per term, the multisets of (Fierz
  coefficient, full Haar integral) pairs over the final integrands agree
  between the geometries, in all 124 terms. The integrands are in bijection
  with the same coefficient **and** the same Haar integral, although the
  words differ; the shared links carry Haar families of size up to three, the
  private links size one.

So the lemma behind channel-wise universality is an identity of Haar
integrals: two words that differ only in the middle face's private structure —
`… U₁ A U₂ B† …` with two private links against `… U₁ U₂ C† …` with one, every
other letter wired identically — have the same Haar integral. Integrating the
private links first does not make them the same function, so the identity is
not local to the middle face; it holds once the end faces' hairpins close the
shared-link letters. The proof has to be written at that level, over the
finite set of wiring patterns the Fierz rewirings produce on the four
shared-link letters.

## Files

| File | What it is |
|---|---|
| `residuals.py` | the run, about a minute on one CPU |
| `console.log` | its complete output |
| `certificate.json` | the three stages: counts, the residual word sets, the first mismatching term of the partial stage with both geometries' residual vectors, and the per-integrand pair comparison with the family sizes |
| `SHA256SUMS` | the pin |
