# 4. The tier collapse, proposed as a degree bound

Date: 2026-08-21

## Status

Proposed. A conjectured mechanism for G14 with a falsifiable prediction — not
a theorem.

## Context

`MASTER_THEORY §5.2` records `B_shp = D_shp = 0` at every solved rank
(`N = 3,4,5,6` and stable `N ≥ 7`) and calls it *"a dynamical selection rule
with no proved mechanism."* G14 asks which it is: accident, selection rule, or
boundary-ideal remnant — and whether the `L⁻⁴` tier appears at fifth or sixth
order.

## The proposal

**The tier is a degree.** Clearing the denominator,

```
q·ε₄ = c₀·q + A_shp·q² + 4C_shp·e₂ + B_shp·(q·e₂) + D_shp·e₃
```

and the basis stratifies by total degree in the `aᵢ`:

| degree | basis | coefficient | observed |
|---|---|---|---|
| 1 | `q` | `c₀` | nonzero |
| 2 | `q²`, `e₂` | `A_shp`, `C_shp` | nonzero |
| 3 | `q·e₂`, `e₃` | `B_shp`, `D_shp` | **zero** |

Since `aᵢ ~ L⁻²`, degree 3 *is* the `L⁻⁴` tier. "The tier is not selected" and
"the numerator has no degree-3 part" are the same statement.

**One hop costs one degree.** The face-to-link Bloch incidence is the curl
matrix `∂₂ = [d]_×` with `dᵢ = e^{ikᵢ} − 1`, entries linear in `d`. It obeys

```
B B† = q·I − d·conj(d)ᵀ,      eigenvalues (0, q, q)
```

which reproduces the recorded second-order C-odd spectrum
`{E_flat, E_flat + t_N q(k) (×2)}` exactly, with the flat carrier as the
`d`-direction. Each entry is bilinear in `(d, conj d)`: one power of `a`.

**The bound.** Order `u^{2r}` is `r` hops, hence `2r` vertices each linear in
`d` or `conj(d)`, so the numerator has degree at most `r`:

| | order | degree ≤ | available | observed |
|---|---|---|---|---|
| r=1 | `u²` | 1 | `q` | `t_N q` — **matches** |
| r=2 | `u⁴` | 2 | `q, q², e₂` | forces `B = D = 0` |
| r=3 | `u⁶` | 3 | adds `q·e₂, e₃` | `B, D` may turn on |

The `r=1` row is a real check rather than a restatement: cubic symmetry permits
a degree-2 second-order term, and none appears.

## Decision

Record it as a **conjectured mechanism**, not a result. It rests on two
assumptions, stated so they can be attacked:

1. every perturbative vertex is linear in `d` or `conj(d)` — true of the
   incidence entries, but the full amplitude also carries colour factors and
   resolvents;
2. the energy denominators are `k`-independent — true at the one-plaquette
   level, where the unperturbed flux energies do not disperse.

If either fails, the count shifts.

## Consequences

**It answers G14's second half.** The `L⁻⁴` tier appears at **sixth** order,
not fifth: odd orders add no hop, which is consistent with the recorded fact
that every tromino numerator vanishes at `O(u³)` and the third-order operator
retains the second-order incidence structure.

**It is falsifiable by work already scheduled.** G9 computes `m₆`. If that run
returns `B_shp = D_shp = 0` again, the degree bound is *not* the mechanism and
G14 needs a different answer. If it returns them nonzero, the bound is the
reason and the "dynamical selection rule" was kinematics all along.

That link is the point of recording this now: it converts a dormant "why"
question into a prediction that an already-planned computation will settle.
