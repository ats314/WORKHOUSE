# 31. The universality identity lives on the fully contracted shared links

Date: 2026-09-04. Status: accepted. Follows ADR 0030 the same evening; bears
on G14. States the lemma the tier-collapse mechanism reduces to, at the level
where it is true.

## Context

ADR 0030 established that the two-hop weight is the same rational function of
N on the straight and the L-shaped chain for every time-ordered insertion
sequence separately, and that within each such term the final integrands are
in value-preserving bijection. It conjectured that the mechanism is local to
the middle face: that `Tr(U₁ A U₂ B†)` with two private links behaves like
`Tr(U₁ U₂ C†)` with one private link of double weight under every rewiring of
its shared-link letters. Before writing that out, this run asked where in the
contraction the two geometries become literally the same word.

## What was computed

`runs/vertex_residuals_2026-09-04`. For every one of the 124 (sequence,
channel) terms of the C-odd direct term, on the reduced clusters over ℚ(N),
each final integrand is Haar-integrated over a chosen set of links with the
engine's own `haar_link` (every such link is a balanced n = 1 family, so the
integration is the cut `δδ/N`), adjacent `U U†` pairs of one link are
cancelled inside each trace, and the residual words over the role alphabet
`l1, l2` (shared links), `wP, wQ` (end paths) are summed with their
coefficients and compared between the two geometries.

- Integrating the middle face's private links only: the residual vectors,
  functions of the shared links and the end paths, agree in **14 of 124**
  terms. The straight chain leaves four distinct residual words, the L chain
  twelve; in the L chain the end paths are threaded through one trace
  together with both shared links, in the straight chain they are not. The
  totals agree in every term, as they must.
- Integrating the end paths as well: every shared-link letter cancels by
  unitarity and the residual is the **empty word**, so each term is a pure
  number, and it is **the same number in all 124 terms**.
- Taking no integral at all: per term, the multiset of (Fierz coefficient,
  full Haar integral) pairs over the final integrands is the same in both
  geometries, in all 124 terms over 718 integrands. The integrands are in
  bijection with the same coefficient **and** the same Haar integral, though
  the words differ; the shared links carry Haar families of size up to three,
  the private links size one.

## What it means

The conjecture of ADR 0030, taken as an identity of the middle face's
contribution as a function of its shared links and the end paths, is false.
The identity is one of Haar integrals of whole words, and its statement is now
exact:

> Two words that differ only in the middle face's private structure — the
> straight `… U₁ A U₂ B† …` with two private links of weight one against the L
> `… U₁ U₂ C† …` with one private link of weight two, every other letter wired
> identically — have the same Haar integral, for every wiring the Fierz
> rewirings produce on the four shared-link letters.

Integrating the private links first does not make the two words the same
function of what remains, so the identity is not local to the middle face; it
closes once the end faces' hairpins have closed the shared-link letters.

The energies match by the path lemma (ADR 0030); the Haar values match because
every private link met here is an n = 1 family whose integration is a cut, the
second cut of the straight chain paying its `1/N` with one extra closed loop.
The wirings the Fierz rewirings can produce on four letters of two links are
finitely many, so the lemma is a finite case analysis. It has not been written
out; the route on G14 now says exactly what is to be checked.

## Decision

- The record is pinned and registered; a fourth check in the suite "private-
  link paths as single links; universality history by history" reads it.
- G14's universality route carries the exact lemma.

## Consequences

- `runs/vertex_residuals_2026-09-04`; the check; the route; this ADR.
- The finite case analysis, and its Weingarten arithmetic in Lean, is the next
  step; after it the reduced clusters can carry the three-hop chains at sixth
  order, where the lemma's scope is tested.
