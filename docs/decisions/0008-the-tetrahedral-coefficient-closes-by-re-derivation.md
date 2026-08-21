# 8. The tetrahedral coefficient closes by re-derivation

Date: 2026-08-21

## Status

Accepted. Discharges G5 and resolves C15.

## Context

The corpus asserts the tetrahedral local Haar-resolvent coefficient

```
c_{2,prim}(N) = -8 / (N (N² - 1))
```

as the r = 2 row of its primitive completion law (transcript
`#-Final-unified-theory.txt` ~170), while the mobility theorem that motivates
the calculation says, twice, that no artifact exists for it
(`THM_FLUX_hodge_cellular_circuit_mobility_theorem.md` §5, §6: "remains to be
calculated", "do not yet contain the corresponding local SU(N) Haar–resolvent
coefficient"). A FINDING in the restored-payloads suite machine-checks that no
pinned path, manifest row, or reference SHA for a tetrahedral certificate
exists anywhere. So C15 could not close by shipping. It could only close by
re-derivation — and the definition of the thing to re-derive was never written
down in one place.

## Decision

Reconstruct the definition from the corpus's own certified instances, then
read it at r = 2. The reconstruction (in `workhouse.cellular`) has exactly
three ingredients, each independently anchored:

1. **Merge factor.** A primitive insertion merges the current fundamental loop
   with a face loop along a connected, oppositely oriented shared path. The
   only group integral involved is the fundamental-pair Haar moment, whose
   coefficient is the n = 1 Weingarten value 1/N (Gram-inverse route, as the
   published-comparisons suite already walks at n = 2). Contracting the shared
   path link by link gives exactly (1/N)·Tr(AB) for *every* path length —
   `(1/N)^k` from the pair moments times `N^(k-1)` closed colour loops. The
   transcript states this as a hypothesis; the shipped prism notebook assumes
   it flatly; here it is derived.

2. **Electric convention.** Isotropic Kogut–Susskind `H₀ = (1/2)ΣE²`: a
   fundamental loop of length L costs `L·C_F/2`. At N = 3 this is the
   certified pentagonal pair `E_SIDE = 8/3`, `E_CAP = 10/3`, and the certified
   one-plaquette rest energy `e_flat(0) = 8/3`. Every intermediate simple loop
   supplies one resolvent `1/(E₀ − E_j)`; all intermediates are longer than
   the endpoints, so all r−1 denominators are negative and the history sign is
   `(−1)^(r−1)` — which is the `(−1)^(r+1)` the quarantined master v3 bolts
   onto its unsigned counts as erratum 9, now derived rather than asserted.

3. **Geometry.** Endpoints are two faces in the family's retained sector;
   the remaining faces are inserted in every temporal order; each merge must
   leave a single simple loop (enforced, not assumed).

## Why this counts as the corpus's definition and not ours

The convention is pinned by *over-determination*. One engine, one convention,
reproduces at once:

- the sealed-core cube row, **sign included**: 24 orderings in the corpus's
  three multiplicity-8 temporal classes with per-history amplitudes
  (−8, −8, −4) in E₀ units (818.txt ~3963), `S₄ = −20`,
  `c₄ = −160/(N(N²−1)³) → −5/48` at N = 3, `α_pen = 4|c₄|`;
- the triangular prism's printed `64/(N(N²−1)²)` (square sector, S₃ = 16,
  6 histories) *and* the shipped notebook's `24/(N(N²−1)²)` (cap sector,
  S = 6) — dissolving the 24-vs-64 pair as an endpoint-sector distinction,
  the way ADR 0002 dissolved C1 as an anchoring distinction; 818.txt ~3402
  records the supersession of 24 by 64 as exactly that sector choice;
- the pentagonal prism's "120 histories, S₅ = 70, c₅(3) = 35/384" verbatim
  (cap sector);
- the notebook's closed Catalan family `(−1)^(n−1) 2^(n−1) C(2n−2, n−1)` for
  the n-gonal cap sectors, re-derived for n = 3..6 from the resolvent
  enumeration.

Only after all of that is the same convention read at r = 2: the tetrahedron
has two temporal histories, each through the single 4-link intermediate loop
(denominator `−C_F/2`), every ordered endpoint pair agreeing:

```
S₂ = −4,     c_{2,prim}(N) = −8 / (N (N² − 1)),     c_{2,prim}(3) = −1/3.
```

Outcome (a): the asserted value is exact. The mobility theorem's proposed
falsification — "if symmetry or representation theory kills this coefficient"
— did not occur: the unique primitive circuit (1,1,1,1) gives w_min = 4, the
scoped bound (C6's survivor) allows r = 2 = w_min − 2, and the primitive local
weight at that order is nonzero at every rank.

## Scope, stated before anyone asks

These are **primitive simple-loop-channel** coefficients, which is how the
corpus itself scopes the law. Fierz side channels, folded and linked terms,
and determinant sectors are outside it — the corpus's own fifth-order
determinant dressing `δc_{5,det} ≠ 0` corrects the pentagonal row's physical
value (C18's refutation of "center-only circuits are dark"), and the
pentagonal O(u⁴) cap hop shows a primitive-family order is not automatically
the leading physical transport (C6). Nothing in G5 asserts that the
tetrahedral carrier physically disperses: survival after cycle compression and
Q projection is U3's question, and the honest statement is that the *local
weight gate* is now passed for a third geometry while the *compression gate*
remains uncomputed for the tetrahedron.

## Consequences

- C15: `resolved`; G5: discharged. The restored-payloads FINDING stays: the
  corpus artifact is still absent, and shipping still could not have closed
  this.
- The (−1)^(r+1) erratum of the quarantined master, the (−8,−8,−4) temporal
  classes of 818.txt, the notebook's Catalan family, and the printed table are
  now one theorem-shaped statement instead of four unlinked assertions.
- One U3-adjacent statement was computable soundly and is now checked: the
  tetrahedral second-order **primitive proper-return operator is exactly
  scalar** on the face space (−6 in C_F units for every face, three 4-link
  returns at weight −2 each), so primitive returns renormalize the rest energy
  and cannot produce shape dispersion. That is a *consistent partial point*
  for U3, not a verdict: the pentagonal precedent is 28 histories vanishing
  *individually after exact Q projection*, and the Fierz/physical-quotient
  layer needed to ask that question of the tetrahedron is not built here.
- The cheapest next falsification test the law now admits is U3's remaining
  half: compute the tetrahedral Q-projected proper-return contributions and
  see whether the two-vanishings mechanism (tier collapse ↔ pentagonal proper
  returns) extends or breaks.
