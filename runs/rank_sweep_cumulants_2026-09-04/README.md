# The fourth-order cluster cumulants at every rank N = 3..70 — 2026-09-04

The third engine (`workhouse.loopcalc`) with its single-link spectra taken
from the block characteristic polynomial instead of the SU(3) Casimir table
(`link_spectrum`, `set_rank`), run at every rank from 3 to 70 on the clusters
that decide the fourth-order kernel. All values are in the kernel's own (0,2)
basis, the x-then-z traversal of the perpendicular face. Nothing here reads
the engine, a kernel, or the corpus.

## What is computed, per rank

| key | quantity | cluster |
|---|---|---|
| `hop_odd`, `hop_perp_odd`, `hop_even` | second-order shared-link hops | coplanar and perpendicular pairs |
| `leak_odd_raw`, `leak_even_raw` | second-order per-neighbour leakage, vacuum bubble not yet added | pair minus single |
| `u_odd`, `u_even` | the two-hop weight on the coplanar chain | P → Q → R, three coplanar faces |
| `single_odd`, `single_even` | the single-contact dressing of the perpendicular pair | X = (0,1) at (1,0,0) |
| `fan_odd`, `fan_even` | the shared-link fan dressing | X = (0,1) at (0,−1,0) |
| `corner_odd`, `corner_even` | the corner dressing | X = (1,2) at (1,0,0) |

At N = 3 the row is the registered SU(3) set: `u = X_QUANTUM`, `u_even`, the
corner `+2580244782961/398756546697600`, the single contact `+385/1997568`,
the fan `−135671797/105250609440`.

## What the sweep establishes

- The second-order hops equal the corpus's all-rank `t_N` and `ell_N` at every
  swept rank, and the raw leakage equals `ell_N − 1/C_F` in both sectors at
  every rank: the leak = hop identity of ADR 0023, rank by rank.
- The fourth-order cumulants at N ≥ 4 exist nowhere in the corpus. Rational
  functions of N reconstructed from part of the sweep and verified on the
  remaining ranks are recorded by the all-rank suite (see its checks for the
  forms and the held-out counts); the sweep itself is the evidence at each rank.

## Files

| File | What it is |
|---|---|
| `rank_sweep.py` | the run, about twelve minutes on one CPU |
| `console.log` | its complete output |
| `certificate.json` | every value above for N = 3..70; the all-rank suite reads this |
| `SHA256SUMS` | the pin |
