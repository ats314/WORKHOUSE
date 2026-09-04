# The two-hop weight and every dressing of the β_N assembly by resolvent channel, over ℚ(N) — 2026-09-04

The G14 route "the same channel decomposition for the corner and fan
dressings of the rotation orbit", run — and run over the field ℚ(N) rather
than at a sweep of ranks, so every channel is one rational function of N and
every comparison below is an identity, not an agreement at N = 3..30.

## What is computed

`workhouse.symbolic_rank.channels`: the three-cluster cumulant of
`loopcalc.cumulant`, split by channel. A history's direct term is tagged by
the labels of its three intermediate states and its fold terms by the labels
of their two, a label being *(extra fundamental links beyond the plaquette's
four, the irreps of the links carrying anything else)*, read off the
per-link energies of each verified eigencomponent rather than searched for.
Eight clusters, in the kernel's `(0,2)` basis, both C-parity sectors:

| cluster | channels | nonzero C-odd | nonzero C-even | seconds |
|---|---|---|---|---|
| `u_coplanar` — the straight coplanar chain | 122 | 74 | 122 | 50 |
| `u_bent` — P and R on opposite cube faces through a side face | 122 | 74 | 122 | 50 |
| `u_L` — the in-plane L chain (the connector's shared links adjacent) | 122 | 74 | 122 | 43 |
| `single_perp` — the perpendicular pair dressed by a plaquette on P | 164 | 92 | 164 | 53 |
| `single_cop` — the coplanar pair dressed by a plaquette on Q | 164 | 92 | 164 | 28 |
| `fan_perp` — the perpendicular pair with a third face on the shared link | 138 | 84 | 138 | 57 |
| `fan_cop` — the coplanar pair with a third face on the shared link | 138 | 84 | 138 | 59 |
| `corner` — the perpendicular pair with the face at the cube vertex | 141 | 87 | 141 | 57 |

The channels of each cluster sum to its cumulant of
`runs/beta_n_symbolic_rank_2026-09-04`.

## Result

1. **The 74 channels of u are identities in ℚ(N).** ADR 0026's 74 closed
   forms, reconstructed from a rank sweep, are the symbolic channels
   exactly; the finer per-link labelling distinguishes 122 channels, and the
   48 it adds vanish in the C-odd sector.
2. **u is universal channel by channel as an identity**: bent = −coplanar in
   every C-odd channel and equal in every C-even one, L = coplanar in every
   channel of both sectors. So `u2 = 2u` and the tier collapse
   `D = −6u + 3u2 = 0` hold at every rank, not only at the thirty swept.
3. **The fan dressing is universal channel by channel too**: the coplanar fan
   is minus the perpendicular fan in every one of its 84 C-odd channels and
   equal in every one of its 138 C-even channels. Its labels are the only
   ones carrying three-box irreps (`F³` and `F² ⊗ F̄` on the tripled link),
   which is where its own factors `4N ∓ 3`, `4N ∓ 7`, `4N² − 7` come from.
4. **The single-contact dressing is universal only in sum.** Between the
   straight chain (coplanar pair, dressing on Q) and the L-shaped chain
   (perpendicular pair, dressing on P), 76 of the 92 C-odd channels agree with
   the incidence sign, 8 agree with the wrong sign, and 8 are present in each
   geometry only; those 24 exceptional channels sum to zero across the two
   geometries. The exact negative `d_cop = −d_perp` is a cancellation between
   channels — a coincidence of sums in ADR 0026's sense — unlike u and the fan.
5. **The corner's channels.** 87 nonzero C-odd channels (31 direct, 24 in the
   two-face fold, 32 in the three-face fold); at most three doubled links in
   any direct-term state (the corner's faces pairwise share three different
   links; the fold's face-times-conjugate states have all four), never a
   tripled one. Every factor the corner adds to `R20` is the resolvent of an
   identified middle state, `E − E0 = (C_F/2)(2 + Σ excess)`:

   | factor | middle state |
   |---|---|
   | `3N² − 1` | (2, adj adj) |
   | `2N ∓ 1` | (2, adj adj adj) |
   | `4N² ∓ 2N − 5` | (2, adj lam lam), (2, adj sym sym) |
   | `4N² − 5` | (2, adj lam sym) |
   | `3N ∓ 5` | (2, lam lam), (2, sym sym) |

   Single channels carry the `n = 3` Weingarten poles `N = ±3`; the sum does
   not.
6. **β_N is a sum of resolvent products.** `−16 Σ u + 32 Σ d − 16 Σ corner +
   848/(N(N²−1)³)` over 254 channel terms equals `P17(N²)/(N R20(N²))`
   identically; every channel denominator is a product of the resolvent
   factors above (and `N`, `N ± 1`, `N ± 3`), of degree at most 7 in N, every
   numerator of degree at most 4. This answers the route's question: the
   corpus's all-rank formula is itself a sum of resolvent products, with the
   assembly's integer weights.

## Files

| File | What it is |
|---|---|
| `channels.py` | the run, about seven minutes on one CPU |
| `console.log` | its complete output |
| `certificate.json` | per cluster, per channel: the C-odd and C-even forms, factored and as integer coefficient lists |
| `SHA256SUMS` | the pin |
