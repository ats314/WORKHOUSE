# The chain amplitude u, computed independently — 2026-09-02

The G3 route "chain amplitude u on the three-plaquette cluster" (ADR 0019),
run. `chain_amplitude.py` is the script as it ran; the same machinery is
`src/workhouse/chain_cluster.py`, and two checks in the kernel-orbits suite
re-derive everything below in seconds.

## What the pinned engine supplies, and what it does not

Three primitives from `corpus-import/programs/hodge_o4_adjudication`:
Wilson-word states, exact Haar inner products, the H0 (Fierz) action.
Everything else is here: the H0-closure of a word as an invariant block; the
resolvent as an exact polynomial in H0 on the block (H0 has rational spectrum,
so no Gram matrix and no Haar integral is needed to apply it); the projector
off the model space by `p(E0) = 0`, exact because the only states at the
one-plaquette energy are plaquettes — for SU(3) that includes the
antisymmetric fusion of two same-direction fluxes, which *is* the conjugate
plaquette; Hermitian fourth-order theory with `PVP = 0`; and Haar integrals
attempted only where link-charge conservation allows a nonzero value. The
first attempt built Gram matrices for every block and spent 33 minutes on
integrals the pruning now skips; this version runs in four seconds.

## Second order: the register, reproduced

| quantity | computed | register |
|---|---|---|
| C-odd shared-link hop, coplanar pair | `-5/612` | `t_3 = 5/612`, sign as in `S_sq` |
| C-odd shared-link hop, perpendicular pair | `+5/612` | the cross-plane sign of `S_sq` |
| C-even shared-link hop | `-11/306` | `T_PLUS_2` |
| C-odd per-neighbour leakage after the `-3/4` vacuum bubble | `-11/306` | `LEAK_2` |

## Fourth order: the chain amplitude

The cluster cumulant `W({P,Q,R}) - W({P,R})` of the `P -> R` element, on
Q-touched histories (the others are identical in both clusters and cancel),
C-odd projected:

| chain | u | X_QUANTUM |
|---|---|---|
| coplanar P–Q–R along an axis (`coplanar.log`) | `360421351/40327601932800` | `360421351/40327601932800` |
| bent: bottom, side, top face of a cube (`bent.log`) | `-360421351/40327601932800` | sign `S_PQ S_QR = -1` |

Exact, as rationals. The historical kernel's two-hop weight is reproduced on
both geometries with the sign the Hodge form requires, so the weight is one
number for geometrically different chains — the universality G14 had left as
its single dynamical input. The v10a.26 dump's u is `4.1327437` times this
and is wrong there. The C-even chain amplitude, `948253471/40327601932800`,
is new to the register.

## What this does not decide

C2. The two-hop sector is the constant `16u` on the cube-boundary carrier, so
`C_shp` does not see u. What changes is standing: the cold pipeline has a
demonstrated error in a sector whose shape it shares with the historical
kernel, and until that error is located and shown not to reach `rho` and
`pi~`, its sign-flipped values carry no independent weight.

| File | What it is |
|---|---|
| `chain_amplitude.py` | the script as run: validation, then the cumulant, with a live log |
| `coplanar.log`, `bent.log` | the two runs, four seconds each |
