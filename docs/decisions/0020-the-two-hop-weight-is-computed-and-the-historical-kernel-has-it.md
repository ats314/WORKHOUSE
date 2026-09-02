# 20. The two-hop weight u is computed twice, and the historical kernel has it exactly

Date: 2026-09-02. Status: accepted. Records the closing of the G3 route "chain amplitude u on the three-plaquette cluster" (ADR 0019) by two independent implementations; bears on G14 and C2. Promotes neither side of C2.

## Context

ADR 0019 reduced the fourth-order kernel to a Hodge polynomial plus one
operator, and the 144 records the two rival kernels agree on in shape to
`u S_□²`: one weight `u`, the fourth-order cumulant carried by every two-hop
chain `P → Q → R` with `Q` sharing a link with each endpoint. The kernels
disagree on that weight by a factor 4.1327437 while agreeing on `ν̃ = −5/48`,
so it is a genuine fourth disagreement, band-invisible on the carrier. It is
also the smallest fourth-order amplitude in the dispute that can be computed
from outside both pipelines: one chain, ten links, at most two fluxes per
link, no ε sector in any history that touches `Q`.

Two sessions ran the route on the same day. The first
(`runs/g3_chain_amplitude_2026-09-02`, `workhouse.chain_cluster`, merged as
PR #76) computed the coplanar and a perpendicular-perpendicular chain. The
second (`runs/g3_chain_amplitude_replication_2026-09-02`) was written by a
session that had only the first's abandoned draft, not its result, and
differs from it in construction. They agree on every number.

## What was computed

Both use the pinned exact engine (`DATA_SU3_Exact_MarkedCluster_m4_Colab.py`)
for primitives only: Wilson-word states, the word product with unitarity
simplification, the `H₀` (Fierz) action, and Haar inner products. Neither
reads either kernel. Both reproduce the register's second-order constants
from the primitives before reading a fourth-order number: `−5/612` for a
coplanar shared-link pair and `+5/612` for a perpendicular one (the `S_□`
sign pattern), `−11/306` for the C-even hop, `−11/306` for the C-odd
leakage once the neighbour's `−3/4` vacuum bubble is subtracted.

The replication differs at three points:

- **Resolvent.** A Krylov minimal polynomial of `H₀` relative to each
  vector, reduced modulo its squarefree part, in place of a block
  characteristic polynomial. No block is diagonalised; the degree is the
  number of energies a vector touches (34 at most). A polynomial identity
  on the lifted, over-complete word basis descends to the true operator,
  and the true minimal polynomial divides the squarefree part because the
  true operator is diagonalisable. The `E₀` component the projector drops
  is the model space and nothing else, by Casimir counting: four fundamental
  links closing into a 4-cycle is the only gauge-invariant way to total `8/3`.
- **Assembly.** `PVP` is not zero. `⟨P|V|P̄⟩ = 1` is the SU(3) baryonic
  vertex, and the engine's own assembly carries it as the scalar `a = ±1`
  per C-sector: `H₄ = D − A C₁ − C₁ᵀ A − ½(K₂N + NK₂) + A A J`. The
  replication uses that formula; the first run used the `PVP = 0` form.
  They agree because, in the cumulant `W(P,Q,R) − W(P,R)` between
  link-disjoint endpoints, every history that never inserts `Q` cancels,
  and so do the `A`-terms and `J`. On a shared-link pair they would not.
- **Geometries.** Three chain types, adding the coplanar-perpendicular
  chain on which the two hops carry opposite signs, with the incidence
  sign computed from link traversals and asserted against the cumulant.

Every matrix element in the replication is one-sided against a
single-plaquette bra, so no Haar family above `(2,2)` occurs: 9,431
integrals, none slower than half a second, 116 s in all.

## Result

On the coplanar-coplanar, coplanar-perpendicular and
perpendicular-perpendicular chains the C-odd cumulant is

    s · 360421351/40327601932800,   s = +1, −1, −1,

with `s` exactly the product of the two signed shared-link incidences of
THM_FLUX Prop. 2, i.e. the `(S_□²)_{PR}` entry. So `|u| = X_QUANTUM`, the
historical exact kernel's two-hop weight, as a rational, on all three chain
types and from two implementations. The C-even cumulant is
`948253471/40327601932800` on all three, a number neither kernel holds,
registered by value as `u_even`.

## Decision

- **G3.** The route is `done`, closed by both runs and their checks. It
  could not decide C2 and does not: `u` is band-invisible on the carrier,
  and `ρ`, `π̃` live on shared-link pairs the chain never isolates. It
  decides *standing*: the cold v10a.26 pipeline is wrong by 4.1327437 on the
  one fourth-order amplitude that has been checked from outside, twice, and
  until its error is located and shown not to reach `ρ` and `π̃`, its
  sign-flipped values carry no independent weight against the historical
  ones. The historical `C_shp` is not thereby established; it has lost its
  rival's credibility, not gained a proof.
- **G14.** The universality of `u` across chain types, the one dynamical
  input the Hodge form rested on, is now T1 on three clusters, sign included,
  from two assemblies. What remains is the mechanism: why one cumulant per
  two-hop chain whatever the planes, a question about the Haar contraction
  rather than the kernel.
- **C2.** Nothing is promoted. The record gains the replication beside the
  first run, side by side with both kernels' values.

## Consequences

- One `REPLICATION` check in the kernel-orbits suite reading the pinned
  certificate and comparing with the live first implementation, resting on
  the first run's `FINDING`. The two runs stay separate records under
  separate names; a replication merged into the thing it replicates is no
  longer one.
- The next bounded step in the same style is the shared-link pair itself:
  the P → Q fourth-order element on a two-plaquette cluster, which is where
  `ρ` and `π̃` live, and where the `PVP = 0` shortcut is no longer available.
  Its histories include the baryonic `{Q, Q, P̄, P̄}` and its Haar families
  reach `(3,0)³`; the replication measured one such integral at 264 s in
  this engine. That cost is the obstacle to price before the route is opened.
