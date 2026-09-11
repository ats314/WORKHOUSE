# The planar limit of the fourth-order band: every cumulant is N⁻⁷, every cluster's channels are N⁻³, two orders cancel identically — 2026-09-11

The β_N assembly is known exactly as rational functions of N
(`runs/beta_n_symbolic_rank_2026-09-04`, ADR 0029), and each cumulant is
known channel by channel over ℚ(N) (`runs/channels_symbolic_rank_2026-09-04`).
The corpus states the leading large-N term of the assembled coefficient,
`β_N ~ 6170/(9N⁷)`, and of the axial law `α_N ~ 640/N⁷` (GLUEBALL v3.1 §4,
MASTER_THEORY v4.3), and it names `τ = β/N³` as the variable in which a
rank-uniform theorem would have to live (NOTE_O4 §11, gap G16). Nothing had
asked *why* the fourth-order band is N⁻⁷, or what the large-N limit does to
the pieces the coefficient is assembled from. This run answers both by exact
arithmetic on the recorded forms.

## What is computed

`derive.py` reads the two records and writes `certificate.json`. All
arithmetic is exact (sympy rationals; the channel census uses reversed-
polynomial power-series division over ℚ, the same routine the suite uses).

1. The exact 1/N expansion of every closed form of the β_N assembly — the
   three second-order hops, the two-hop weight, the single-contact, fan and
   corner dressings of both pair geometries, both cube completions, π, ρ,
   C_shp, β_N, α_N and W₄ = α_N + β_N — in both C-parity sectors, through
   N⁻¹³.
2. The planar decomposition of β_N: the limit of each cluster term of
   `β_N = −16u + 32d − 16 corner + 848/(N(N²−1)³)`.
3. For each of the eight clusters of the channel record and both sectors: the
   leading power of every nonzero channel, the exact total of the N⁻³, N⁻⁵ and
   N⁻⁷ coefficients over all channels, and that total split by the channels'
   own leading power. The channels are re-summed and checked to equal the
   cumulant as an identity in ℚ(N).
4. Real-root isolation (Sturm, via `sympy.real_roots`) of every numerator,
   denominator and of the derivative of `N⁷ × form`, on the real axis N ≥ 3.
5. The band ratio W₄/W₂ as a rational function of N and its large-N law.

## Result

**Every fourth-order cumulant is O(N⁻⁷) in both sectors — the order of the
six-face cube completions — while its resolvent channels are O(N⁻³).** In all
sixteen cluster/sector pairs the N⁻³ and N⁻⁵ totals of the channels vanish
identically: two cancelled orders, in every cluster, with no exception.

| cluster | sector | nonzero channels | leading at N⁻³ / N⁻⁵ / N⁻⁷ | N⁻⁷ coefficient from the N⁻³, N⁻⁵, N⁻⁷ channels | cumulant × N⁷ |
|---|---|---|---|---|---|
| u (coplanar chain) | odd | 74 | 42 / 27 / 5 | −109/64 + 49/18 − 1 | 11/576 |
| u (coplanar chain) | even | 122 | 86 / 31 / 5 | −101/64 + 47/18 − 1 | 19/576 |
| u (bent) | odd | 74 | 42 / 27 / 5 | 109/64 − 49/18 + 1 | −11/576 |
| u (L) | odd | 74 | 42 / 27 / 5 | −109/64 + 49/18 − 1 | 11/576 |
| single, perpendicular | odd | 92 | 60 / 28 / 4 | 45/16 − 13/2 + 4 | 5/16 |
| single, perpendicular | even | 164 | 112 / 48 / 4 | −25/16 + 5 − 4 | −9/16 |
| single, coplanar | odd | 92 | 60 / 28 / 4 | −45/16 + 13/2 − 4 | −5/16 |
| fan, perpendicular | odd | 84 | 52 / 30 / 2 | 169/128 + 29/6 − 8 | −709/384 |
| fan, perpendicular | even | 138 | 94 / 42 / 2 | 1113/128 − 53/2 + 24 | 793/128 |
| fan, coplanar | odd | 84 | 52 / 30 / 2 | −169/128 − 29/6 + 8 | 709/384 |
| corner | odd | 87 | 56 / 28 / 3 | 397/64 − 31/9 + 8 | 6197/576 |
| corner | even | 141 | 98 / 40 / 3 | −37/64 − 67/9 − 8 | −9229/576 |

(The bent and L chains and the coplanar dressings in the C-even sector repeat
their partners' rows, as ADR 0031's channel universality requires.) The
channels whose *own* leading order is N⁻⁷ are in every cluster exactly the
channels with no nontrivial irrep on any link — the pure-singlet direct terms
and the singlet folds — and they contribute an integer to the N⁻⁷ coefficient
(−1, ±4, ±8, 24); the rest of the coefficient is the N⁻⁷ tail of channels that
began two or one orders higher. A naive rule "leading power = −3 − 2 × (states
without an irrep)" fails on 47 labels (recorded in `label_rule_failures`); the
order of a channel is not a function of its label alone.

**The second-order hop has the same structure one level down.** The two
channel sums are `A_N = −1/N − 3/(2N³) − …` and `B_N = −1/N − 5/(4N³) − …`,
and `t_N = B_N − A_N = 1/(4N³) − 1/(16N⁵) − …`: one cancelled order. So at
order 2k the channel content is N⁻⁽²ᵏ⁻¹⁾, k orders cancel, and the band
coefficient is N⁻⁽⁴ᵏ⁻¹⁾ — verified for k = 1 (N⁻³) and k = 2 (N⁻⁷).

**In the corpus's variable τ = β/N³ the band is rank-uniform through fourth
order.** With the canonical coupling `u = β_N/(2N)` (CLAUDE.md non-negotiable
4; `u = β/6` at SU(3)), `W₂ = 12 t_N u²` and `W₄ = (α_N + β_N) u⁴`:

```
W₂ / (2C_F)  =  (3/4) τ² (1 + O(N⁻²)),
W₄ / W₂      =  (11930/27) u²/N⁴ (1 + (1407353/429480)/N² + …)  =  (5965/54) τ² (1 + O(N⁻²)),
```

exactly the matched-scaling structure NOTE_O4 §11 extrapolated from second
order, now with the fourth-order coefficient computed. This is a statement
about the strong-coupling series, not the overlap theorem G16 asks for.

**The planar limit of β_N is the cube completion.** The pieces of
`β_N = −16u + 32d − 16 corner + 848/(N(N²−1)³)` tend to

| term | limit × N⁷ | share of 6170/9 |
|---|---|---|
| −16 u | −16 · 11/576 = −11/36 | −0.045 % |
| 32 d | 32 · 5/16 = 10 | 1.46 % |
| −16 corner | −16 · 6197/576 = −6197/36 | −25.1 % |
| adjacent-face cube completion (848) | 848 | 123.7 % |

and `−11/36 + 10 − 6197/36 + 848 = 6170/9` exactly; the next term
`677903/(324 N⁹)` and `W₄ ~ 11930/(9N⁷)` agree with the corpus.

**Sign and monotonicity.** No numerator or denominator of any form of the
assembly has a real root at N ≥ 3; `N⁷β_N`, `N⁷W₄` and `N⁷ corner_N` are
positive and decrease strictly (no critical point on N ≥ 3) to their planar
limits: `N⁷β_N` from 994.16 at N = 3 to 685.56. `N⁷u` has one critical point
above 3 (recorded), so the two-hop weight is the one cluster that is not
monotone in this normalisation.

## Where it stops

- The N⁻⁽⁴ᵏ⁻¹⁾ law is verified at k = 1, 2 and is a conjecture beyond; the
  mechanism it names — connected cumulants losing k orders against their
  channel content — is the thing to test on the sixth-order clusters (G9).
- τ-uniformity of the *series* is not the rank-uniform spectral theorem G16
  asks for; the series is not controlled at β ~ N³.
- Everything is in the kernel's (0,2) basis with the recorded conventions;
  nothing here changes any claim's status.

## Files

| File | What it is |
|---|---|
| `derive.py` | the computation; run from the repository root with the project environment |
| `certificate.json` | every expansion, decomposition, root count and channel total |
| `console.log` | the run's console output |
| `SHA256SUMS` | pins of the above |

Reproduce any of it: `workhouse verify --only 'planar limit'` (suite "the planar
limit of the fourth-order band (G16)", five T1 checks, about seven seconds).
