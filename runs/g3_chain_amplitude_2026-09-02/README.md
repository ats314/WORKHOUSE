# The two-hop weight u on three-plaquette chains — 2026-09-02

The G3 route "chain amplitude u on the three-plaquette cluster" (ADR 0019),
run to completion. ADR 0020 records the decision it led to.

**Result.** The C-odd fourth-order cumulant `W(P,Q,R) − W(P,R)` on the
`P → R` element is `s · 360421351/40327601932800` on every chain computed,
with `s = ±1` the product of the two signed shared-link incidences of THM_FLUX
Prop. 2. So `|u| = X_QUANTUM`, the historical exact kernel's two-hop weight,
**as a rational**, on all three chain types. The cold v10a.26 dump's `u` is
4.1327437 times this.

| chain | P, Q, R | incidence sign | C-odd cumulant | C-even cumulant |
|---|---|---|---|---|
| coplanar-coplanar | xy(0,0,0), xy(1,0,0), xy(2,0,0) | +1 | `+360421351/40327601932800` | `948253471/40327601932800` |
| coplanar-perpendicular | xy(0,0,0), xy(1,0,0), yz(2,0,0) | −1 | `−360421351/40327601932800` | `948253471/40327601932800` |
| perpendicular-perpendicular | xz(0,0,0), xy(0,0,0), yz(1,0,−1) | −1 | `−360421351/40327601932800` | `948253471/40327601932800` |

116 s on one CPU; 9,431 exact Haar integrals, none above the `(2,2)` family,
none slower than half a second; Krylov degree at most 34.

## What it uses, and what it does not

The pinned exact engine
(`corpus-import/programs/hodge_o4_adjudication/src/DATA_SU3_Exact_MarkedCluster_m4_Colab.py`)
supplies four primitives: `trace_state` (Wilson-word states),
`tensor_product` + `simplify_unitarity` (the word product), `h0_action` (the
electric operator by the SU(3) Fierz identity) and `haar_inner` (exact Haar
inner products), plus `CF = 4/3`. Everything else is in `chain_amplitude.py`:

- **the `H₀`-closure and the reduced resolvent**, as a Krylov minimal
  polynomial of `H₀` relative to each vector — no Gram matrix, no
  characteristic polynomial of a block. `H₀` preserves link occupation, so
  the polynomial's degree is the number of energies a vector touches, and
  the inverse of `E₀ − x` modulo its squarefree part, times the projector
  off `E₀`, is `Q (E₀ − H₀)⁻¹ Q`. The over-complete word basis descends
  correctly because the true operator is diagonalisable (docstring of
  `resolvent`); the `E₀` component the projector drops is the model space by
  Casimir counting (same docstring).
- **the assembly**, which is the engine's own
  (`build_exact_endpoint_fourth_order_ledgers`):
  `H₄ = D − A C₁ − C₁ᵀ A − ½(K₂N + NK₂) + A A J`, with `A = PVP` the SU(3)
  baryonic vertex `⟨P|V|P̄⟩ = 1`. The staged first attempt assumed `PVP = 0`;
  for the cumulant between link-disjoint endpoints the `A`-terms and `J`
  cancel anyway (docstring of `chain_cumulant`), which is why both give the
  same number.
- **the cumulant restricted to `Q`-touched histories**, the orderings of
  `{R̄, P, Q, Q̄}` on `|R⟩`, every other history being identical on both
  clusters; the fold terms come from the two-insertion moments on each
  cluster. Every matrix element is one-sided against a single-plaquette bra,
  which is what keeps every Haar family at `(2,2)` or below.
- **a triality reachability filter** at every stage: a word whose per-link
  charge signature cannot reach the bra's with the insertions that remain is
  dropped before its closure is built. Exact, because `H₀` keeps occupancy.

It never reads either kernel. `X_QUANTUM` appears only in the last lines of
the log, as the comparison.

## The second order first

Before any fourth-order number is read, the same assembly returns the
register's second-order constants from the primitives:

| quantity | computed | register |
|---|---|---|
| C-odd shared-link hop, coplanar pair | `−5/612` | `t_3 = 5/612`, the `S_□` sign |
| C-odd shared-link hop, perpendicular pair | `+5/612` | the cross-plane sign of `S_□` |
| C-even shared-link hop, both | `−11/306` | `T_PLUS_2` |
| C-odd per-neighbour leakage after the `−3/4` vacuum bubble | `−11/306` | `LEAK_2` |
| disjoint-pair hop, both sectors | `0` | — |

## What it decides

Which pipeline has standing on the two-hop sector: the historical exact
kernel's `u` is right, the cold dump's is off by 4.13. It cannot decide C2 —
`u` is band-invisible on the carrier, and `ρ`, `π̃` live on shared-link pairs
this cluster never isolates — and it promotes neither side.

## The first attempt

`first_attempt_cluster_pt.py`, `first_attempt_chain_cumulant.py` and
`first_attempt_second_order_validation.py` are the same-day staged version
(from the superseded draft PR #76, where they ran as `cluster_pt.py`,
`chain_cumulant.py`, `second_order_validation.py`). It validated the second order exactly, then spent 33 minutes on
Gram matrices of degree-3 words (each `(3,3)`-family Haar integral costs
about 9 s in this engine) and was killed without a fourth-order number.
Kept because the way it failed is the reason the second version has no
Gram at all.

## Files

| File | What it is |
|---|---|
| `chain_amplitude.py` | the run; `python chain_amplitude.py all` from this directory reproduces everything below in about two minutes |
| `console.log` | its complete output |
| `chain_amplitude_certificate.json` | every number above, as exact strings; the checks in the kernel-orbits suite read this |
| `first_attempt_*.py` | the staged version that did not finish |
| `SHA256SUMS` | the pin |
