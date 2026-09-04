# The fourth-order cumulants of the β_N assembly over ℚ(N): every closed form derived, the degree bound proved — 2026-09-04

ADR 0025 and ADR 0027 reconstructed the fourth-order cluster cumulants and the
assembled shape coefficient as rational functions of N from a rank sweep,
verified them on held-out ranks, and stated the identity
`β_assembled(N) = P17(N²)/(N R20(N²))` as rational functions "conditional on
a degree bound". This run removes the condition: the third engine
(`workhouse.loopcalc`) is run over the rational function field ℚ(N) itself
(`workhouse.symbolic_rank`), so every cumulant is *computed* as one rational
function of N, and its degree is whatever it is.

## What is computed

With N an indeterminate — scalars in ℚ(N), the Weingarten function as the
symbolic inverse of the Gram matrix `N^cycles` on S_n, the single-link spectra
as the SU(N) quadratic Casimirs of the irreps a link's flux content can carry,
and every eigencomponent of every resolvent verified to be an exact
eigenvector of every single-link `H0` — in the kernel's `(0,2)` basis:

| quantity | cluster | degrees in N | seconds |
|---|---|---|---|
| second-order hops, C-odd and C-even | coplanar and perpendicular pairs | (3, 6) | 0.3 |
| two-hop weight `u`, both sectors | coplanar chain | (21, 28) | 8 |
| single-contact dressing, both sectors | perpendicular pair; coplanar pair | (7, 14) | 10 + 9 |
| shared-link fan, both sectors | perpendicular pair; coplanar pair | (17, 24) | 13 + 11 |
| corner dressing, both sectors | perpendicular pair | (23, 30) | 10 |
| cube completions, adjacent and opposite | six-face cube | (0, 7) | 40 |

Every one is the rational function ADR 0025 / ADR 0027 reconstructed,
identically, and every one specialises to the pinned per-rank value at every
rank of `runs/rank_sweep_cumulants_2026-09-04` (N = 3..70) and
`runs/beta_n_from_assembly_2026-09-04` (N = 4..70): 16 quantities, no rank
disagreeing (`certificate.json`, `specialisation`).

## Why this is a derivation of the per-rank values, and where it stops

The per-rank engine and the ℚ(N) engine run the same word arithmetic; they
can differ only through the rank predicates, the Weingarten function and the
spectral decomposition. The certificate (`audit`) records what makes them
agree for every N ≥ 5:

- **fluxes.** The largest net flux any word carries on a link is 6, and every
  word with a nonzero flux carries one of magnitude ≤ 4, so "0 mod N" and
  "0" are the same filter for N ≥ 5;
- **families.** Every Haar family integrated is balanced, the largest being
  (3, 3), so with n ≤ 3 ≤ N the per-rank pseudoinverse Weingarten function is
  the inverse, which is the specialisation of the symbolic one;
- **resolvents.** 21,556 eigencomponents verified over ℚ(N); of the 103
  distinct intermediate energies, the resolvent denominators `E0 − E` have
  exactly one integer root ≥ 4, at **N = 4**, from the state `P³` with every
  link of the plaquette in `Λ³F` — which at N = 4 is `F̄`, so the state is
  degenerate with the plaquette. That is the per-rank engine's "(4,0)
  family" path in resolvent form.

So for N ≥ 5 the closed forms are the values the engine computes, by
argument; at N = 3 and N = 4 they agree with the engine as a checked fact
(the forms are regular there and match every pinned N = 3, 4 value).

## The assembly

- `d_cop + d_perp = 0` and `s_cop + s_perp = 0` identically in the C-odd
  sector (the coplanar and perpendicular dressings are equal in the C-even
  sector): with the pair cluster cancelling (ADR 0027), the fans drop out of
  `ρ + π` entirely — which is why `R20` carries none of the fan's factors
  `(4N ∓ 3)(4N ∓ 7)(4N² − 7)` — and

  ```
  β_N = −16 u − 8(ρ + π) = −16 u + 32 d − 16 corner + 848/(N(N²−1)³)
  ```

  three cluster cumulants and the adjacent-face cube completion, `α_N`
  cancelling.
- `β_assembled(N) − P17(N²)/(N R20(N²)) = 0` in ℚ(N), degrees (34, 41) in N.
  With denominators cleared over `N R20(N²)` this is a polynomial identity
  of degree 34, proved in Lean (`betaN_assembled_numerator`,
  `betaN_from_three_cumulants` in `lean/Workhouse/Basic.lean`).

## Files

| File | What it is |
|---|---|
| `derive.py` | the run, about two minutes on one CPU |
| `console.log` | its complete output |
| `closed_forms.json` | every closed form: factored, and as integer numerator/denominator coefficient lists |
| `certificate.json` | the specialisation of every form at every pinned rank, and the audit |
| `SHA256SUMS` | the pin |
