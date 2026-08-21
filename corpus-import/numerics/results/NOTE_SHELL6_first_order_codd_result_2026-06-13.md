# Shell-6 C-odd glueballs: the first-order (O(y)) computation

**Date:** 2026-06-13
**Status of each claim is labeled [gate-backed] or [conjecture]. No values are asserted that aren't reproduced by the script `shell6_first_order_codd_band.py` or the Monte-Carlo runs cited.**

## Question

Does the first-order magnetic perturbation order the hexagon-built exotic C-odd
channels — in particular, does 0^{--} sit above or below 3^{+-}? GPT correctly
flagged that this is an **O(y) question first** (two length-6 loops can differ by a
single plaquette, so P_6 V P_6 need not be scalar), and that we must settle the
first order before doing O(y^2). This note settles it.

## Setup

The degenerate model space at the shell is spanned by the zero-momentum simple
fundamental Wilson loops of length 6. First-order degenerate PT diagonalizes
`H^(1) = -y P_6 (sum_p (Tr U_p + Tr U_p^dag)) P_6` inside that space.

## Gate-backed results

1. **Basis is complete at shell 6.** [gate-backed] Enumerating closed
   non-backtracking 6-loops with 6 distinct fundamental links — *allowing*
   vertex-touching — gives exactly the same 44 loops as the self-avoiding
   enumeration (12 planar rectangles, 2 axes; 32 twisted hexagons, 3 axes). The
   incompleteness GPT found at length 8 (414 -> 576) has **no analogue at length 6**;
   nothing is missing here.

2. **First-order moves are corner-pushes, all among hexagons.** [gate-backed]
   The only way one plaquette keeps a 6-loop a 6-loop is to swap two cyclically
   adjacent perpendicular steps (push a corner across the plaquette diagonal). There
   are 96 such oriented edges, **all among the twisted hexagons**; rectangles have
   zero (and the single plaquette has zero — the same fact that makes the ground
   1^{+-} band flat).

3. **SU(3) amplitude is uniform +1/3, sign-free.** [gate-backed: hand + Monte Carlo,
   N = 2-3 x 10^5] For a corner-push L <-> L' differing by plaquette p, the matrix
   element factorizes into five Haar contractions ∫ U U^dag = (1/3) δδ, tracing to
   (1/3)^5 · 3^4 = **+1/3**. Only the plaquette orientation that runs the two shared
   edges *opposite* to L contributes; the other vanishes (double-U). The four-loop
   check gives `<L'|V|L> = <L̄'|V|L̄> = +1/3` and `<L̄'|V|L> = <L'|V|L̄> = 0`: the
   magnetic term connects L only to the consistently-oriented L', never to its
   reverse, so the oriented adjacency has **no missing edges**.

4. **Per-move hop = +1/6 y, identical in C-even and C-odd; self-energy = 0.**
   [gate-backed] Because the cross terms (L ↔ reverse-L') vanish, both Re and Im
   sectors get the *same* +1/6 y per move (no C-parity sign flip). No single
   plaquette returns a loop to itself, so the first-order diagonal is exactly 0.

5. **C-odd band, block-diagonalized by O_h x C** (units y; gates: adjacency
   Hermitian, commutes with all 48 O_h elements and with reversal):

   | channel | cubic irrep | first-order energy / y |
   |---|---|---|
   | 0^{--} | A_1^{--} | 0 |
   | 3^{+-} | A_2^{+-} | 0 |
   | 2^{--} | E^{--}, T_2^{--} | 0, 0 |
   | 2^{+-} | T_2^{+-} | 0 |
   | **1^{+-} (excited)** | T_1^{+-} (mult 2) | **± √2 / 3 ≈ ± 0.4714** |

## Conclusion

**At first order, the hexagon-built exotic C-odd channels (0^{--}, 3^{+-}, 2^{--},
2^{+-}) are exactly degenerate** — the corner-push adjacency annihilates every one of
those cubic combinations (eigenvalue 0). The *only* shell-6 C-odd state that disperses
at O(y) is the **excited 1^{+-}**, which splits by ± √2/3 y.

Therefore the ordering of 0^{--} versus 3^{+-} is **not resolved at first order; it is
an O(y^2) effect.** This confirms GPT's instinct that the second-order des-Cloizeaux
correction is the operative computation — but now rigorously: the basis is complete,
the amplitude is derived and Monte-Carlo-checked rather than guessed, and the
first-order degeneracy is a theorem of the (verified) first-order operator, not an
artifact of an unsigned ansatz. Because A_1, A_2, E, T_2 are different irreps, nothing
forces them to stay degenerate, so they generically split at O(y^2) (nonzero, finite).

## What this corrects from earlier in the session

- The initial framing "shell-6 splits only at O(y^2) because all states are C-odd"
  conflated two things. There **is** O(y) structure (the corner-push hopping, +1/6 y),
  but it leaves the exotic channels degenerate; so the *ordering* is O(y^2) after all,
  for a more specific reason than originally stated.
- A hand-derived C-even = -1/6 sign flip was **wrong**; the Monte Carlo shows both
  sectors share +1/6 y (cross terms vanish). Corrected.

## Conjecture (labeled)

The O(y) degeneracy — the corner-push adjacency annihilating the exotic C-odd
channels while the excited vector disperses — structurally echoes the Gauss-law flat
band of the ground 1^{+-}. Whether that protection persists (keeping some of these
channels degenerate at higher order) or breaks at O(y^2) is **open** and is exactly
what the next computation tests. [conjecture]

## Next step (now rigorously motivated)

Second-order des-Cloizeaux correction within the shell-6 C-odd manifold: extend the
two-holonomy abstract-domino engine to the 6-loop basis (higher-degree trace words,
intermediate length-8 states), and read the O(y^2) splitting of A_1^{--} vs A_2^{+-}
vs E^{--}/T_2^{--}. That is the computation that actually orders 0^{--}, 3^{+-}, 2^{--}.
