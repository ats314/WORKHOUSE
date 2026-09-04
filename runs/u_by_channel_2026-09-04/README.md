# The two-hop weight by channel, on three chain types, N = 3..30 — 2026-09-04

The G14 plan step, run. The two-hop cumulant `u` is decomposed by the
irreps of the links its intermediate states double (`workhouse.chain_channels`),
on the coplanar chain, the bent chain (P and R on opposite faces of a cube,
through a side face) and the in-plane L chain (the connector's two shared
links adjacent, the geometry of the doubled orbit), at every rank from 3 to 30.

## Result

- 74 channels — 58 in the direct term, tagged by the energies of the three
  intermediate states, and 16 in the fold term — at every rank, on every chain.
- Every channel of the coplanar chain is a rational function of N of low
  degree, reconstructed from part of the sweep and verified on the rest
  (`reconstruct_channels.py`, `channel_closed_forms.json`): a product of the
  resolvent factors its irreps bring. The pure-fundamental chain is
  `−4/(N(N²−1)³)`; `Λ²` brings `2N−3` and `3N−4`, `Sym²` brings `2N+3` and
  `3N+4`, the adjoint `2N²−1` and `3N²−2`, and the mixed pairs `2N²−3` and
  `4N²∓N−4`. The 74 forms sum to the all-rank `u(N)` identically.
- The bent chain agrees with the coplanar one in every channel with the
  factor `−1`, the L chain in every channel with one sign, at every rank: the
  universality of `u` across chain types, the dynamical input ADR 0019 left
  open, holds channel by channel.

## Files

| File | What it is |
|---|---|
| `u_by_channel.py` | the run: three chains, N = 3..30, about half an hour on one CPU |
| `console.log` | its complete output |
| `certificate.json` | every channel's C-odd value, per chain and rank |
| `reconstruct_channels.py` | the exact rational reconstruction of each coplanar channel in N |
| `reconstruct.log` | its output |
| `channel_closed_forms.json` | the 74 closed forms with their degrees and held-out counts |
| `SHA256SUMS` | the pin |
