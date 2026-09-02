# 20. The two-hop weight u is computed independently, and the historical kernel has it exactly

Date: 2026-09-02. Status: accepted. Closes the G3 route "chain amplitude u on the three-plaquette cluster" (ADR 0019); bears on G14 and C2. Promotes neither side of C2.

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

## What was computed

`runs/g3_chain_amplitude_2026-09-02`, 116 s on CPU, exact rationals throughout.

- The pinned exact engine (`DATA_SU3_Exact_MarkedCluster_m4_Colab.py`) is used
  for four primitives only: Wilson-word states, the word product with
  unitarity simplification, the `H₀` (Fierz) action, and Haar inner products.
  The `H₀`-closure, the reduced resolvent, the C-parity projection and the
  cluster cumulant are the run's own, and nothing in it reads either kernel.
- The resolvent `Q (E₀ − H₀)⁻¹ Q` is an exact polynomial in `H₀`: `H₀`
  preserves link occupation, so the minimal polynomial of `H₀` relative to a
  vector has degree equal to the number of energies the vector touches (34 at
  most here), and the inverse of `E₀ − x` modulo its squarefree part, times
  the projector off `E₀`, is the resolvent. No Gram matrix is ever formed.
  The word basis is over-complete (for SU(3) the antisymmetric fusion of two
  same-direction fluxes *is* the conjugate plaquette), but a polynomial
  identity on the lifted matrix descends to the true operator, and the true
  minimal polynomial divides the squarefree part because the true operator
  is diagonalisable. The `E₀` eigencomponent the projector drops is the model
  space and nothing else, by Casimir counting: four fundamental links closing
  into a 4-cycle is the only gauge-invariant way to total `8/3`.
- The fourth-order assembly is the engine's own,
  `H₄ = D − A C₁ − C₁ᵀ A − ½(K₂N + NK₂) + A A J`, with `A = PVP` the SU(3)
  baryonic vertex `P ↔ P̄` at unit weight, not zero. In the cumulant
  `W(P,Q,R) − W(P,R)` every history that never inserts `Q` cancels, and
  between link-disjoint endpoints so do the `A`-terms and `J`; what survives
  is the direct term over the orderings of `{R̄, P, Q, Q̄}` and the fold from
  the two-insertion moments of each cluster. Every matrix element is taken
  one-sided against a single-plaquette bra, so no Haar family above `(2,2)`
  occurs; 9,431 integrals, none slower than half a second.
- Before any fourth-order number is read, the same assembly returns the
  register's second-order constants from the primitives: `−5/612` for a
  coplanar shared-link pair and `+5/612` for a perpendicular one (the `S_□`
  sign pattern), `−11/306` for the C-even hop in both, and `−11/306` for the
  C-odd per-neighbour leakage once the neighbour's `−3/4` vacuum bubble is
  subtracted.

## Result

On the coplanar-coplanar, coplanar-perpendicular and
perpendicular-perpendicular chains the C-odd cumulant is

    s · 360421351/40327601932800,   s = +1, −1, −1,

with `s` exactly the product of the two signed shared-link incidences of
THM_FLUX Prop. 2, i.e. the `(S_□²)_{PR}` entry. So `|u| = X_QUANTUM`, the
historical exact kernel's two-hop weight, as a rational and on all three
chain types. The C-even cumulant is `948253471/40327601932800` on all three,
a number neither kernel holds, registered by value as `u_even`.

## Decision

- **G3.** The route is `done`. It could not decide C2 and does not: `u` is
  band-invisible on the carrier, and `ρ`, `π̃` live on shared-link pairs the
  chain never isolates. It decides *standing*: the cold v10a.26 pipeline is
  wrong by 4.1327437 on the one fourth-order amplitude that has been checked
  from outside, and until its error is located and shown not to reach `ρ`
  and `π̃`, its sign-flipped values carry no independent weight against the
  historical ones. The historical `C_shp` is not thereby established; it has
  lost its rival's credibility, not gained a proof.
- **G14.** The universality of `u` across chain types, the one dynamical
  input the Hodge form rested on, is now T1 on three clusters, sign included.
  What remains is the mechanism: why one cumulant per two-hop chain whatever
  the planes, a question about the Haar contraction rather than the kernel.
- **C2.** Nothing is promoted. The record gains the independent value and
  the statement about standing, side by side with both kernels' values.

## Consequences

- Three checks in the kernel-orbits suite, reading the pinned certificate:
  the exact agreement (T1), the second-order reproduction (T1), and the cold
  ratio as a `FINDING` (T2). The run is the reproduction; the checks pin it.
- The first attempt the same day is kept as `first_attempt_*`: it validated
  the second order exactly and then spent 33 minutes on Gram matrices of
  degree-3 words. The record of how it failed is the reason the second
  version has no Gram at all.
- The next bounded step in the same style is the shared-link pair itself:
  the P → Q fourth-order element on a two-plaquette cluster, which is where
  `ρ` and `π̃` live. Its histories include the baryonic `{Q, Q, P̄, P̄}` and its
  Haar families reach `(3,0)³`, which this engine evaluates in minutes each;
  the cost is measured (one such integral, 264 s) and is the obstacle to
  price before that route is opened.
