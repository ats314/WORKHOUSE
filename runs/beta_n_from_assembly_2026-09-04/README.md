# The fourth-order shape coefficient from the cluster assembly at every rank N = 4..70, against the corpus's all-rank β_N — 2026-09-04

The corpus states the fourth-order shape coefficient at every rank as
`β_N = P17(N²)/(N R20(N²))`, "for N ≥ 4", output-certified by its all-rank
program and never re-derived. This run assembles `β_N` from cluster cumulants
computed by the third engine (`workhouse.loopcalc`), which reads no kernel,
no engine and no corpus formula, and compares the two exactly.

## What is assembled

At N ≥ 5 the pair cluster is the plain Hermitian fourth order on the two-face
cluster (`loopcalc.pair_element`): the first-order vertex is the determinant
family `(3, 0)`, zero unless N = 3, and no pair history reaches a determinant
family at all. At N = 4 the `(4, 0)` family enters and the engine's determinant
trick makes the pair element infeasible (about fifteen thousand inner products
at well over four seconds each; two attempts stopped after 23 CPU-minutes with
none complete) — and unnecessary, since the pair cluster cancels between the
coplanar and the perpendicular pair (below): at N = 4 the nine other cumulants
are computed and the pair entries are recorded as `null`. Those nine do reach
`(4,0)` families in their three-face words, so the N = 4 row rests on the
engine's determinant trick, a path the adversarial verification of ADR 0027 did
not audit: N ≥ 5 agrees with its path audited, N = 4 agrees with its path
unaudited. With the dressings,
the corner and the two-hop weight from
`runs/rank_sweep_cumulants_2026-09-04` and the adjacent-face cube completion
`−106/(N(N²−1)³)`, everything in the kernel's `(0,2)` basis:

```
pi(N)   = pair_cop + 18 d_cop + 2 s_cop
rho(N)  = pair_perp + 14 d_perp + 2 s_perp + 2 corner + K_adj
C(N)    = -alpha_N/8 - u(N) - (rho + pi)/2,     alpha_N = 640/(N(N^2-1)^3)
beta(N) = 8 A_N + 16 C(N),                      A_N = alpha_N/4
```

The link-disjoint (stacked) pair is computed as a control and is exactly zero
at every rank.

## Result

`beta_assembled(N) = P17(N²)/(N R20(N²))` exactly, as rationals, at every rank
from 4 to 70. The corpus's all-rank shape coefficient is re-derived by an
independent route at every rank it was stated for, and (ADR 0024) at N = 3 as
well.

## The closed forms, and what drops out

`reconstruct_beta.py` finds, for each certified quantity, the lowest-degree
form `N^s g(N²)` through the first `dp + dq + 1` ranks N ≥ 5 that reproduces
every remaining rank (`closed_forms.json`, `reconstruct.log`):

| quantity | shape | degrees in N² | held-out ranks |
|---|---|---|---|
| pair cluster, coplanar | `N⁻¹ g(N²)` | (14, 17) | 34 |
| pair cluster, perpendicular | the exact negative | (14, 17) | 34 |
| single-contact dressing, coplanar | `−2N³(N²−4)(10N²−13) / ((N²−1)³(4N²−9)²(2N²−1)²)` | (4, 7) | 54 |
| fan dressing, coplanar | `N⁻¹ g(N²)` | (9, 12) | 44 |
| `C_shp(N)` | `N⁻¹ g(N²)` | (17, 20) | 28 |
| `β(N)` | `N⁻¹ g(N²)` | (17, 20) | 28 |

- `pair_cop(N) + pair_perp(N) ≡ 0`: the pair cluster drops out of `C_shp` and
  of `β_N` entirely, at every rank and as closed forms. Structurally: the two
  clusters are one abstract graph up to conjugating one face (the shared link is
  traversed oppositely by the coplanar pair, in the same direction by the
  perpendicular one), the engine's value depends only on that graph, so the pair
  elements agree entry by entry under `Q ↔ Q̄` and the C-odd blocks are
  negatives whatever the determinant families do. The 2026-09-02 record's two
  N = 3 pair values are equal in its conjugate basis, i.e. negatives in the
  kernel's.
- The pair cluster's continuation has a double pole at N = 3 with
  `(N−3)²`-coefficient `5/1088` — the PVP = 0 form's energy denominators
  degenerate exactly where the `(3,0)` determinant family becomes possible.
  `β_N` never sees it, which is why the corpus's formula, boxed "for N ≥ 4",
  is in fact right at N = 3 (ADR 0024).
- `cancel(β_form(N) − P17(N²)/(N R20(N²))) = 0`: the identity as rational
  functions, conditional on the assembled β being rational of degree at most
  (17, 20) in N². The rank-by-rank equality stands on its own.

## Files

| File | What it is |
|---|---|
| `beta_from_assembly.py` | the run: about twelve minutes on one CPU for N = 5..70, then `python beta_from_assembly.py 4` (one minute) for the N = 4 row |
| `console.log` | its complete output |
| `certificate.json` | per rank: the three pair clusters, the coplanar dressings, pi, rho, C, both betas and their equality |
| `reconstruct_beta.py` | the closed forms in N (flint, exact) and the symbolic comparison with P17/(N R20) |
| `reconstruct.log`, `closed_forms.json` | its output |
| `SHA256SUMS` | the pin |
