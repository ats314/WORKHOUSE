# 46. The fourth-order band is N⁻⁷ because two orders cancel in every cluster, and the band is rank-uniform in τ through fourth order

Date: 2026-09-11. Status: accepted. Bears on G16, G14, G6; changes no claim's
status.

## Context

ADR 0029 computed every fourth-order cumulant of the β_N assembly as one
rational function of N, and ADR 0031 split each into resolvent channels that
are themselves rational functions of N. The corpus records the leading large-N
term `β_N ~ 6170/(9N⁷)` (GLUEBALL v3.1 §4) and, in NOTE_O4 §11, extrapolates
from second order that the strong-coupling mobility and the local weak-well
series select the same variable `τ = β/N³` — gap G16, "rank-uniform control in
τ", where "neither fixed-regime series supplies an overlap theorem". No one
had asked what the large-N limit does to the pieces, or why the coefficient
is N⁻⁷ when its ingredients need not be.

## What was computed

`runs/planar_band_2026-09-11`: exact 1/N expansions of all sixteen closed
forms and of the 1,772 nonzero channel forms of the channel record, the
planar decomposition of β_N, Sturm root isolation on N ≥ 3, and the band
ratio W₄/W₂. Suite "the planar limit of the fourth-order band (G16)", five T1
checks, re-derives all of it in about seven seconds; the channel check re-sums
every channel form in the flint field and re-expands it, reading no total from
the run.

## Decision: record three facts and one conjecture

1. **Every fourth-order cumulant is O(N⁻⁷) in both sectors while its channels
   are O(N⁻³).** In each of the sixteen cluster/sector pairs the N⁻³ and N⁻⁵
   channel totals vanish identically. The cancellation is not visible in any
   channel and not a property of the C-odd sector: the C-even cumulants cancel
   the same two orders. The second-order hop is the same phenomenon one level
   down: `A_N, B_N = −1/N + O(N⁻³)` and `t_N = 1/(4N³) + O(N⁻⁵)`.

2. **The planar limit of β_N is the cube completion.** In
   `β_N = −16u + 32d − 16 corner + 848/(N(N²−1)³)` the limits are
   `u → 11/576`, `d → 5/16`, `corner → 6197/576`, and
   `−11/36 + 10 − 6197/36 + 848 = 6170/9`: the six-face term supplies 124 %
   of the planar coefficient, the corner removes 25 %, the two-face clusters
   contribute 1.4 %. All three N⁷-scaled quantities `β_N`, `W₄`, `corner_N`
   decrease strictly to their limits on N ≥ 3 with no real pole or zero there.

3. **The band is rank-uniform in τ through fourth order.** With the canonical
   `u = β_N/(2N)`, `W₂/(2C_F) = (3/4)τ²(1 + O(N⁻²))` and
   `W₄/W₂ = (5965/54)τ²(1 + O(N⁻²))`. This is the matched-scaling structure of
   NOTE_O4 §11 made exact at the next order. It is a statement about the
   series, not the overlap theorem G16 asks for.

4. **Conjecture, with its mechanism named.** At order 2k the channel content
   is N⁻⁽²ᵏ⁻¹⁾ and k orders cancel, so the band coefficient is N⁻⁽⁴ᵏ⁻¹⁾ — the
   exponent that makes every order of the band, relative to the plaquette
   energy, an N-independent multiple of τ²ᵏ. Verified at k = 1, 2. The test is
   the sixth-order clusters of G9: channel content N⁻⁵, coefficient N⁻¹¹.

## What was tried and did not hold

A label rule for the order of a channel — "leading power = −3 − 2 × (number
of intermediate states carrying no irrep), capped at −7" — fails on 47 of the
1,772 channel forms; they are listed in the certificate. The channels whose
own order is N⁻⁷ are exactly the all-singlet ones in every cluster, and they
contribute an integer to the N⁻⁷ coefficient, but the cancellation of the two
higher orders is not a per-label statement.

## Consequences

- G16's strong-coupling side is exact through fourth order; its detail
  records this and what remains (the overlap theorem, and the k ≥ 3 law).
- G6's fixed-rank holdout question is answered for every quantity of the
  assembly by the closed forms themselves; nothing in this ADR discharges it,
  because G6 asks about the stored per-rank certificates.
- For G9, the sixth-order route now has a sharp large-N prediction to check
  against: two orders of cancellation on top of N⁻⁵ channel content, and a
  cube-dominated planar limit if the pattern of fourth order persists.
