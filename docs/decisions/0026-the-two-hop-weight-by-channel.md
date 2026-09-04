# 26. The two-hop weight by channel: u is universal because every channel is

Date: 2026-09-04. Status: accepted. Runs the G14 plan step opened by ADR 0025
the same night; answers the question ADR 0020 left ("why one cumulant per
two-hop chain whatever the planes, a question about the Haar contraction
rather than the kernel"); bears on G14, C2, R2.

## Context

The Hodge form of the fourth-order kernel (ADR 0019) rests on one dynamical
input: that the two-hop chain cumulant `u` is the same on every two-hop
chain, whatever planes the three plaquettes lie in. ADR 0020 established it
at N = 3 on three chain types by computation and asked for the mechanism.
ADR 0025 gave `u` a closed form in N, a `(21, 28)` rational function whose
denominator factors — `9N²−16`, `2N²−3`, `3N²−2`, `4N²∓N−4` beside the
second-order ones — are resolvents of intermediate states, and proposed
reading the mechanism off them.

## What was computed

In the third engine every resolvent is applied as a sum of exact `H0`
eigencomponents, so every history's contribution can be tagged by the
energies of its intermediate states. Above `E0` those energies are, in units
of `C_F/2`, an even number of extra fundamental links plus, for each link a
history has doubled, the excess of that link's irrep: `0` (merged singlet),
`2(N−2)/(N−1)` (`Λ²F`), `2N²/(N²−1)` (adjoint), `2(N+2)/(N+1)` (`Sym²F`).
The labels are rank-independent (`workhouse.chain_channels`).

`runs/u_by_channel_2026-09-04`, N = 3..30, three chains:

1. **74 channels.** 58 in the direct term `P V R V R V R V P`, tagged by
   three energies, and 16 in the fold term, tagged by two — the same 74 at
   every rank and on every chain. Direct and fold nearly cancel: at N = 3
   they are `−1.203e−4` and `+1.292e−4` against `u = 8.9e−6`.
2. **Every channel is a product of resolvent factors.** Reconstructed
   exactly and verified on held-out ranks: the pure-fundamental chain is
   `−4/(N(N²−1)³)`; a doubled link in `Λ²` brings `2N−3` and `3N−4`, in
   `Sym²` `2N+3` and `3N+4`, in the adjoint `2N²−1` and `3N²−2`; two doubled
   links of different irreps bring `2N²−3` and `4N²∓N−4`. The 74 forms sum
   to the all-rank `u(N)` identically. The double zero `(N²−4)²` of `u` at the
   excluded rank is therefore a cancellation among channels, not a property
   of any one of them.
3. **Universality holds channel by channel.** The bent chain (P and R on
   opposite cube faces through a side face) equals the coplanar chain in
   every one of the 74 channels with the factor `−1`; the in-plane L chain —
   the connector's two shared links *adjacent*, the doubled-orbit geometry
   whose weight `u2 = 2u` is what makes `D = 0` in ADR 0019 — equals it in
   every channel with one sign. At every rank.

## Why this is the mechanism

The calculus knows nothing of planes. `H0` acts link by link; the Haar
integral acts link by link; the cluster's words are traces over links. Two
chains whose plaquettes share the same links in the same pattern are the
same abstract cluster, and differ only in the orientation of traversal on the
shared links — which is exactly the incidence sign of THM_FLUX Prop. 2, and
nothing else. For the straight and bent chains (shared links on opposite
edges of the connector) that is an isomorphism of clusters and the equality
is forced. The L chain is *not* isomorphic — its shared links meet at a
corner of the connector — and its channel-by-channel agreement is the
nontrivial fact: the per-channel resolvent products depend on which links
are doubled and in what irreps, not on where on the connector they sit.
So the universality of `u` is a property of the Haar contraction on the
doubled links, decided channel by channel, and the "dynamical input" of the
Hodge form is no longer an input.

## Decision

- G14's plan step "read the mechanism off u(N)" is `done`. What G14 still
  asks is narrower and stated in the ledger: `B = 0` is unpopulated by the
  carrier projection (ADR 0019), `D = 0` follows from `u2 = 2u`, and `u2 = 2u`
  is the L-chain equality above; the remaining question is whether the same
  channel-wise statement holds for the corner and fan dressings of the
  rotation orbit, whose closed forms ADR 0025 recorded.
- The forms and the equalities are T1 checks in the all-rank suite, reading
  the pinned run.

## Consequences

- `src/workhouse/chain_channels.py`; two checks in `all_rank`;
  `runs/u_by_channel_2026-09-04` with its reconstruction script and the 74
  closed forms pinned; G14 updated.
