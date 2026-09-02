# The chain amplitude u on a three-plaquette cluster — 2026-09-02, PENDING

The G3 route "chain amplitude u on the three-plaquette cluster" (ADR 0019):
an independent fourth-order assembly that uses the pinned exact engine only
for Wilson-word states, Haar inner products and the H0 (Fierz) action, with
its own closure, Gram, resolvent and degenerate perturbation theory
(Hermitian fourth-order form, `PVP = 0`).

## What is established

`second_order_validation.py` reproduces the register exactly, from the
primitives and textbook second-order theory:

| quantity | computed | register |
|---|---|---|
| C-odd shared-link hop, coplanar pair | `-5/612` | `t_3 = 5/612`, sign as in `S_sq` |
| C-odd shared-link hop, perpendicular pair | `+5/612` | the cross-plane sign of `S_sq` |
| C-even shared-link hop | `-11/306` | `T_PLUS_2 = -11/306` |
| C-odd per-neighbour leakage, after subtracting the neighbour's vacuum bubble `-3/4` | `-11/306` | `LEAK_2 = -11/306` |

So the machinery is sound at second order, and the sign pattern of the
shared-link hop is the one the Hodge form of the kernel uses.

## What is not

`chain_cumulant.py` computes `W({P,Q,R}) - W({P,R})` for the `P -> R`
element on Q-touched histories (the histories that never insert the
connector are identical in both clusters and cancel). Its cost is in the
Haar integrals with three link matrices on a shared link, up to 13 s each.
The first run was killed after 33 minutes of CPU without finishing and
without a progress signal, because its output was piped through `tail`.
**No fourth-order number is recorded here.** The route stays `untried` in
`ledger/gaps.yaml` until a run completes with a visible log and a stated
time cap.

| File | What it is |
|---|---|
| `cluster_pt.py` | the block-wise exact perturbation theory on a cluster |
| `second_order_validation.py` | the table above, and a cost probe of the fourth-order words |
| `chain_cumulant.py` | the cumulant for the coplanar and bent chains; unfinished |
