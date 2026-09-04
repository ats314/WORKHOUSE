# 25. The third engine at every rank: the fourth-order cumulants as functions of N

Date: 2026-09-04. Status: accepted. Follows ADR 0024 the same night; bears on
G14, C2, C10, G11, R2. Promotes the corpus's all-rank second order from
output-certified to re-derived at every rank, and records fourth-order
cumulants at ranks the corpus never computed.

## Context

ADR 0024's third engine, `workhouse.loopcalc`, took its single-link spectra
from the SU(3) Casimir table. Nothing else in it knew the rank: the Fierz
identity, the Weingarten function, the Haar determinant trick and the
energies are all functions of `N`. Replacing the table by the spectrum of the
single-link `H0` on the word's own block, computed from its characteristic
polynomial, makes the engine rank-generic (`set_rank`, `link_spectrum`), and
the same cumulants that decided C2 can be computed at any `N` in seconds.

The corpus holds all-rank formulas at second order (`t_N`, `ℓ_N`) and for two
fourth-order shape coefficients (`α_N`, `β_N`). It holds no fourth-order
cluster cumulant at any rank but 3.

## What was computed

`runs/rank_sweep_cumulants_2026-09-04`: for every `N` from 3 to 70, in the
kernel's `(0,2)` basis, the two second-order hops and both raw leakages, the
two-hop weight `u` in both sectors, and the three dressing classes of the
perpendicular pair (single contact, shared-link fan, corner) in both sectors.
A scratch sweep to `N = 100` served the reconstructions.

1. **Second order at every rank.** The coplanar hop is `−t_N`, the
   perpendicular hop `+t_N`, the C-even hop `ℓ_N = −2N(3N²−5)/((N²−1)(4N²−9)(2N²−1))`,
   and the raw leakage in *both* sectors is `ℓ_N − 1/C_F` — the leak = hop
   identity ADR 0023 derived at `N = 3`, now at every rank the engine reaches.
   Reconstructed from the engine's numbers alone, the two hops come back as
   the corpus's formulas exactly, verified on dozens of held-out ranks: the
   corpus's all-rank second order is re-derived, not merely reproduced.
2. **The cube completion at `N = 4, 5`** with the full `H0` dynamics is the
   closed form of ADR 0024, `−106/(N(N²−1)³)` adjacent and `−160/(N(N²−1)³)`
   opposite, at both ranks.
3. **Closed forms the corpus does not have.** By exact rational
   reconstruction from part of the sweep, verified on the rest:

   - single-contact dressing, C-odd:
     `2N³(N²−4)(10N²−13) / ((N²−1)³(4N²−9)²(2N²−1)²)`;
   - single-contact dressing, C-even: `−ℓ_N² / (2C_F)` — minus the C-even hop
     squared over the plaquette rest energy, identically in `N`;
   - the shared-link fan in both sectors: `(17, 24)` rational functions whose
     denominator adds `(16N²−9)(16N²−49)(4N²−7)` to the single contact's — the
     linear factors `4N ± 3`, `4N ± 7` are resolvents of the three-flux link;
   - the two-hop weight `u` in both sectors: `(21, 28)` rational functions
     whose denominator adds `(9N²−16)(2N²−3)(3N²−2)(4N²−N−4)(4N²+N−4)`; the
     C-odd numerator carries `(N²−4)²`, a double zero at the excluded rank
     where `t_N` has a single one;
   - the corner dressing in both sectors: `(23, 30)` rational functions
     whose denominator adds `(4N²−1)(9N²−25)(3N²−1)(4N²−5)(4N²−2N−5)(4N²+2N−5)`.

   The pair cluster, which needs the pure-six Haar family, is the one
   fourth-order cluster of the kernel with no all-rank form yet.
4. **The shape table with the resolved `C_shp`.** `β₃`, `W₄` and `λ_R` move
   up by `25/64`, `λ_M` by `25/128`, `α` and `λ_X` not at all; the near-Γ
   exclusion radius of G11, proportional to `√W₄`, grows by `1.346`. Two Lean
   theorems carry the `W₄` arithmetic.

## Decision

- The all-rank suite ("the third engine at every rank") records each closed
  form as a check that evaluates it at every pinned rank and recomputes one
  rank live, with the held-out count of its reconstruction in the detail. A
  reconstructed form is exact if the true function is rational of no higher
  degree than the fit — which it is, being a finite sum of Casimir-difference
  and Weingarten products — but the degree bound is not proved here, so the
  forms are recorded as verified at every swept rank, not as theorems.
- The corpus's "`β_N` is not to be substituted at `N = 3`" stays a rule about
  derivation; ADR 0024 already showed the number is right there. This ADR adds
  that the same engine that decided `N = 3` reproduces the corpus's all-rank
  second order at every rank it was asked, which is the standing on which the
  fourth-order all-rank forms above are offered.

## Consequences

- `loopcalc.set_rank`, `loopcalc.link_spectrum`; `tests/test_loopcalc.py`
  covers the table-versus-charpoly agreement and the all-rank second order.
- Suite `all_rank` (seven checks), constants `BETA_PEN_3_ASSEMBLED`,
  `W4_ASSEMBLED`, `LAMBDA_M_ASSEMBLED`, the shape-table check in the
  third-implementation suite, Lean `w4_shift_from_beta`,
  `w4_old_is_alpha_plus_beta`, and `singleContactEven_eq`: the C-even
  single-contact dressing is `−ℓ_N²/(2C_F)`, proved as a field identity.
- G14 gains the all-rank note; the run register gains the sweep.
