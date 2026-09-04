# The two-hop weight u, replicated by a second implementation — 2026-09-02

A second, independently written computation of the G3 route "chain amplitude
u on the three-plaquette cluster" (ADR 0019), run the same day as
`runs/g3_chain_amplitude_2026-09-02` and without reading it. It agrees with
that run on every number, and it differs from it in construction at three
points that matter, which is what makes it a replication rather than a rerun.
ADR 0020 records the decision.

**Result.** The C-odd fourth-order cumulant `W(P,Q,R) − W(P,R)` on the
`P → R` element is `s · 360421351/40327601932800` on every chain computed,
`s = ±1` the product of the two signed shared-link incidences of THM_FLUX
Prop. 2. So `|u| = X_QUANTUM`, the historical exact kernel's two-hop weight,
**as a rational**, on all three chain types below. The cold v10a.26 dump's
`u` is 4.1327437 times this.

| chain | P, Q, R | incidence sign | C-odd cumulant | C-even cumulant |
|---|---|---|---|---|
| coplanar-coplanar | xy(0,0,0), xy(1,0,0), xy(2,0,0) | +1 | `+360421351/40327601932800` | `948253471/40327601932800` |
| coplanar-perpendicular | xy(0,0,0), xy(1,0,0), yz(2,0,0) | −1 | `−360421351/40327601932800` | `948253471/40327601932800` |
| perpendicular-perpendicular | xz(0,0,0), xy(0,0,0), yz(1,0,−1) | −1 | `−360421351/40327601932800` | `948253471/40327601932800` |

116 s on one CPU; 9,431 exact Haar integrals, none above the `(2,2)` family,
none slower than half a second; Krylov degree at most 34.

## Where it differs from the first run

Both use the pinned exact engine
(`corpus-import/programs/hodge_o4_adjudication/src/DATA_SU3_Exact_MarkedCluster_m4_Colab.py`)
for primitives only: `trace_state`, `tensor_product` + `simplify_unitarity`,
`h0_action`, `haar_inner`, and `CF = 4/3`. Neither reads either kernel.

1. **The resolvent.** The first run takes the characteristic polynomial of
   `H₀` on each closure block. This one takes a Krylov minimal polynomial of
   `H₀` relative to each vector, whose degree is the number of energies the
   vector touches, and reduces every polynomial in `H₀` modulo it; the
   inverse of `E₀ − x` modulo the squarefree part, times the projector off
   `E₀`, is `Q (E₀ − H₀)⁻¹ Q`. No block is ever diagonalised. The docstring
   of `resolvent` carries the argument that this descends correctly from the
   over-complete word basis, and the Casimir count that the dropped `E₀`
   component is the model space and nothing else.
2. **The assembly.** The first run uses the Hermitian fourth-order form with
   `PVP = 0`. `PVP` is not zero: `⟨P|V|P̄⟩ = 1`, the SU(3) baryonic vertex
   (`P̄ ⊗ P̄` contains `P` through the ε-tensor), and the engine's own
   assembly carries it as the scalar `a = ±1` per C-sector,
   `H₄ = D − A C₁ − C₁ᵀ A − ½(K₂N + NK₂) + A A J`
   (`build_exact_endpoint_fourth_order_ledgers`). This run uses that formula.
   The `A`-terms and `J` cancel in the cumulant between link-disjoint
   endpoints (docstring of `chain_cumulant`), which is why both runs agree;
   they would not agree on a shared-link pair.
3. **The geometries.** The first run computes the coplanar chain and a
   perpendicular-perpendicular chain (bottom, side, top face of a cube).
   This one adds the coplanar-perpendicular chain, on which the two hops
   carry opposite signs, and uses a different perpendicular-perpendicular
   chain; the incidence sign is computed from the link traversals rather
   than assigned, and asserted against the cumulant's sign.

Two things are the same by design: every history that never inserts `Q`
cancels between the clusters, so only the orderings of `{R̄, P, Q, Q̄}` on
`|R⟩` are propagated; and every matrix element is taken one-sided against a
single-plaquette bra, which is what keeps every Haar family at `(2,2)` or
below. A triality reachability filter drops, at every stage, any word whose
per-link charge signature cannot reach the bra's with the insertions that
remain; exact, because `H₀` keeps occupancy.

## The second order first

Before any fourth-order number is read, the same assembly returns the
register's second-order constants from the primitives (also in the
certificate):

| quantity | computed | register |
|---|---|---|
| C-odd shared-link hop, coplanar pair | `−5/612` | `t_3 = 5/612`, the `S_□` sign |
| C-odd shared-link hop, perpendicular pair | `+5/612` | the cross-plane sign of `S_□` |
| C-even shared-link hop, both | `−11/306` | `T_PLUS_2` |
| C-odd per-neighbour leakage after the `−3/4` vacuum bubble | `−11/306` | `LEAK_2` |
| disjoint-pair hop, both sectors | `0` | — |

## What it decides

The same thing as the first run, now with two implementations behind it:
which pipeline has standing on the two-hop sector. It cannot decide C2 —
`u` is band-invisible on the carrier, and `ρ`, `π̃` live on shared-link pairs
this cluster never isolates — and it promotes neither side.

The one measurement it adds for the next route: the shared-link pair's own
fourth-order element, where `ρ` and `π̃` live, has baryonic histories
(`{Q, Q, P̄, P̄}`) whose Haar families reach `(3,0)³`; one such integral took
264 s in this engine. That cost is the obstacle to price before that route is
opened.

## Files

| File | What it is |
|---|---|
| `chain_amplitude.py` | the run; `python chain_amplitude.py all` from this directory reproduces everything above in about two minutes |
| `console.log` | its complete output |
| `chain_amplitude_certificate.json` | every number above, as exact strings; the replication check in the kernel-orbits suite reads this |
| `SHA256SUMS` | the pin |
