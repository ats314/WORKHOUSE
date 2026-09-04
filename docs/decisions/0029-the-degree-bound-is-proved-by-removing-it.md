# 29. The degree bound is proved by removing it: the third engine over ℚ(N), and the corner and fan by channel

Date: 2026-09-04. Status: accepted. Discharges the condition ADR 0027 left on
the identity `β_N = P17(N²)/(N R20(N²))`; runs the G14 route "the same
channel decomposition for the corner and fan dressings"; bears on G14, C10,
R2, C2. Promotes the final polynomial identity to T0.

## Context

ADR 0025 reconstructed the fourth-order cluster cumulants as rational
functions of N from a rank sweep and verified them on held-out ranks; ADR
0027 assembled `β_N` from them at N = 4..70, found it equal to the corpus's
`P17(N²)/(N R20(N²))` at every rank, and could state the identity as rational
functions only "conditional on the assembled β being rational of degree at
most (17, 20) in N²" — 67 exact agreements, and a plausibility argument that
the engine's output is rational in N. The judge of ADR 0027's verification
made the point the required fix: *no "for all N" without a degree bound*.

The bound could have been argued from the engine's structure — Weingarten
denominators, energy denominators, a count of vertices — and then the 67
agreements would prove the identity by uniqueness of rational interpolation.
That argument was not made. What was done instead makes it unnecessary.

## What was built

`workhouse.symbolic_rank`: the third engine (`workhouse.loopcalc`) run over
the rational function field ℚ(N). Nothing in the engine but its two rank
predicates (`charge ≡ 0 mod N`, `|diff| ≤ N`), its Weingarten function and its
single-link spectra depends on the rank other than through rational
arithmetic in `C_F = (N²−1)/(2N)`, `1/(2N)` and `N^closed`. So: the scalars
become elements of ℚ(N) (a numerator and a monic denominator in
`flint.fmpq_poly`); the Weingarten function becomes the symbolic inverse of
the Gram matrix `N^cycles` on `S_n`; the single-link spectra become the SU(N)
quadratic Casimirs of the irreps a link's flux content can carry; and every
eigencomponent of every resolvent is verified to be an exact eigenvector of
every single-link `H0`. The two predicates were made functions in `loopcalc`
so that the symbolic run can override them; the per-rank engine is otherwise
untouched, and `tests/test_loopcalc.py` still holds.

A cumulant then comes out as *one rational function of N*, computed. The
two-hop weight takes eight seconds; the corner ten.

## What was found

**1. Every closed form is derived** (`runs/beta_n_symbolic_rank_2026-09-04`).
The second-order hops, the two-hop weight, the single-contact and fan
dressings of both pairs, the corner dressing and both cube completions, in
both C-parity sectors, are the rational functions ADR 0025 and ADR 0027
reconstructed — identically — and each specialises to the pinned per-rank
value at every rank of both records, N = 3..70. The degree bound of ADR 0027
is now the computed degree: `β_assembled` is `N⁻¹ g(N²)` with `g` of degree
(17, 20) because that is what the sum of the derived forms is.

**2. Why this is the per-rank engine's value, and where the argument stops.**
The two engines run the same word arithmetic and can differ only through the
rank predicates, the Weingarten function and the spectral decomposition. The
record certifies: no word ever carries every nonzero link flux at magnitude
≥ 5 (largest flux 6, every such word also carrying one ≤ 4), so the two
charge filters agree for N ≥ 5; every Haar family is balanced with n ≤ 3, so
the per-rank pseudoinverse is the inverse, which is the specialisation of the
symbolic one; and 21,556 eigencomponents are verified over ℚ(N), with the
103 distinct intermediate energies recorded. The resolvent denominators
`E0 − E` have exactly one integer root at N ≥ 4: at **N = 4**, from the state
`P³` with every link of the plaquette in `Λ³F` — which is `F̄` at N = 4, so
the state is degenerate with the plaquette. That is the per-rank engine's
"(4,0) family" path seen from the resolvent side. So for N ≥ 5 the closed
forms are the engine's values by argument; at N = 3 and N = 4 they are
regular and agree with the engine as a checked fact.

**3. The assembly collapses.** The coplanar single-contact and fan dressings
are the exact negatives of the perpendicular ones in the C-odd sector (and
equal in the C-even), as rational functions. With the pair cluster cancelling
(ADR 0027) the fans drop out of `ρ + π` entirely — which is why `R20` carries
none of the fan's factors `(4N ∓ 3)(4N ∓ 7)(4N² − 7)` — and

```
β_N = −16 u − 8(ρ + π) = −16 u + 32 d_single − 16 d_corner + 848/(N(N²−1)³),
```

three cluster cumulants and the adjacent-face cube completion, `α_N`
cancelling. Every denominator divides `N R20(N²)`, and over that common
denominator the weighted numerators sum to `P17(N²)` exactly: a polynomial
identity of degree 34 in N.

**4. The identity is a theorem.** `lean/Workhouse/Basic.lean` now carries
`P17`, `R20`, the three closed forms with their cofactors, the cleared
identity `betaN_assembled_numerator` (by `ring`), and
`betaN_from_three_cumulants`: `−16u + 32d − 16 corner − 8K = β_N` wherever
`N R20(N²) ≠ 0`. The T1 check it promotes is pure algebra on the same literal
forms; that the forms are the engine's output is the derivation check beside
it. `betaN_three` records that the formula's value at N = 3 is the assembled
`β₃` of ADR 0024, `β_historical + 25/64`.

**5. The corner and fan by channel** (`runs/channels_symbolic_rank_2026-09-04`,
the G14 route). `symbolic_rank.channels` splits a three-cluster cumulant by
the labels of its intermediate states — *(extra fundamental links, the
irreps of the links carrying more)*, read off each verified component's
per-link energies rather than searched for — and returns each channel as a
rational function of N in both sectors. Eight clusters:

- *u*: ADR 0026's 74 channels are identities in ℚ(N); the per-link labelling
  distinguishes 122, the 48 extra vanishing in the C-odd sector. **u is
  universal channel by channel as an identity**: bent = −coplanar and
  L = coplanar in every channel of both sectors. So `u2 = 2u` and the tier
  collapse `D = −6u + 3u2 = 0` hold at every rank N ≥ 5, given the six-orbit
  structure of the kernel and `B` unpopulated (ADR 0019): the corpus's
  "dynamical selection rule with no proved mechanism" is the Hodge form plus
  an identity in ℚ(N).
- *fan*: universal channel by channel too — coplanar = −perpendicular in all
  84 C-odd channels, equal in all 138 C-even. The two fans are one abstract
  cluster (three faces around a link, two coplanar), and this is the forced
  case. Its labels alone carry three-box irreps (`F³`, `F² ⊗ F̄` on the
  tripled link), the origin of `4N ∓ 3`, `4N ∓ 7`, `4N² − 7`.
- *single contact*: **universal only in sum.** Between the straight chain and
  the L-shaped chain, 76 of the 92 C-odd channels agree with the incidence
  sign, 8 agree with the wrong sign, 8 are present in each geometry only, and
  the 24 exceptional channels sum to zero across the two geometries. The exact
  negative `d_cop = −d_perp` is a cancellation between channels — a
  "coincidence of sums" in the sense ADR 0026's route anticipated, here found
  rather than feared, and recorded.
- *corner*: 87 C-odd channels (31 direct, 24 two-face fold, 32 three-face
  fold), at most three doubled links in a direct-term state, never a tripled
  one; every factor the corner adds to `R20` is the resolvent of an identified
  middle state: `3N² − 1` from (2, adj adj), `2N ∓ 1` from (2, adj adj adj),
  `4N² ∓ 2N − 5` from (2, adj lam lam) and (2, adj sym sym), `4N² − 5` from
  (2, adj lam sym), `3N ∓ 5` from (2, lam lam) and (2, sym sym). Single
  channels carry the n = 3 Weingarten poles `N = ±3`; the sum does not.
- **β_N is a sum of resolvent products**: 254 channel terms with the
  assembly's integer weights, every denominator a product of the resolvent
  factors above (and `N`, `N ± 1`, `N ± 3`) of degree ≤ 7, every numerator of
  degree ≤ 4, summing to `P17(N²)/(N R20(N²))` identically. The route's
  question — whether the corpus's all-rank formula is itself a sum of
  resolvent products — is answered: it is.

## What is not claimed

- The engine's premises are unchanged: the Hermitian `PVP = 0` fourth-order
  form, the dropping of the `E0` components (that the `E0` eigenspace on the
  reachable words is the plaquette span), the vacuum intermediates, and the
  completeness of the eleven-cumulant decomposition stay the open routes of
  G14 they were. The ℚ(N) run certifies that the *spectral decomposition* is
  exact and that the *specialisation* is faithful for N ≥ 5; it does not audit
  what the engine drops.
- At N = 4 the agreement of the forms with the per-rank engine is checked,
  not derived; the resolvent denominator that vanishes there is named.
- The pair cluster is not computed over ℚ(N); it cancels (ADR 0027) and the
  record does not need it.
- Universality channel by channel is computed, not explained. The route
  opened below asks for the explanation.

## Decision

- Suite "the third engine over Q(N): closed forms derived, the degree bound":
  ten T1 checks — the derivation (one dressing live over ℚ(N), every form
  against every pinned rank), the specialisation audit, the
  coplanar-perpendicular negatives and the three-cumulant form, the final
  polynomial identity (promoted by the Lean theorems), u's 74 channels as
  identities, u's universality channel by channel, the fan's, the
  single-contact finding, the corner's channels and their resolvent factors,
  and β_N as a sum of resolvent products.
- Lean: `P17`, `R20`, `betaN`, the three closed forms, four cofactor lemmas,
  `betaN_assembled_numerator`, four `_over_R20` lemmas,
  `assembly_three_cumulants`, `betaN_from_three_cumulants`, `betaN_three`,
  `betaN_four`.
- G14: the corner/fan route is `done`; the resolvent-audit and N = 4 routes
  gain what the ℚ(N) run covers and what it does not; a new route asks for a
  proof of channel-wise universality from the Haar contraction, and for why
  the single-contact dressing needs its 24 exceptional channels to cancel.
- Two run records, both pinned; `symbols.yaml` notes that the dressings and
  the two-hop weight are now derived; `runs/index.yaml` gains both records.

## Consequences

- `src/workhouse/symbolic_rank.py`; the two rank predicates in `loopcalc`;
  `src/workhouse/invariants/rank_field.py`; `tests/test_symbolic_rank.py`;
  `runs/beta_n_symbolic_rank_2026-09-04`,
  `runs/channels_symbolic_rank_2026-09-04`; the Lean block; this ADR.
