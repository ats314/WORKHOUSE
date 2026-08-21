# 3. The near-Gamma caveat becomes an explicit radius

Date: 2026-08-21

## Status

Accepted. Partially discharges G11.

## Context

`GLUEBALL §18.3` records a warning and stops there: near Gamma the `O(u²)`
isolation gap closes like `u²|k|²` while the `O(u⁴)` operator does not shrink,
so below some radius the ordering of the expansion fails. Until that radius is
named, a coefficient theorem at fixed momentum "must not be promoted to a
uniformly isolated near-Gamma band theorem."

An unquantified caveat blocks promotion indefinitely, because there is no
condition anyone can check.

## Decision

State the radius.

The carrier sits at `E_flat(u)`, the dispersive branches at
`E_flat(u) + t(u)q(k)`, so the isolation gap is `t(u)q(k)` with
`q(k) = Σᵢ 4sin²(kᵢ/2)`. Since `b₃ > 0`, `t(u) ≥ t₃u²`. Requiring the
fourth-order spread `W₄u⁴` to occupy at most a fraction `θ` of that gap:

```
θ · t₃u² · q(k)  ≥  W₄u⁴
```

Bound `q` from below with **Jordan's inequality** rather than the small-`k`
approximation, so the result holds across the whole zone rather than only near
Gamma: `sin` is concave on `[0,π]`, hence above its chord `2x/π` on `[0,π/2]`;
substituting `x → x/2` and squaring gives `q(k) ≥ (4/π²)|k|²`, with equality at
`k = 0` **and at the zone corner** — the bound is tight, not slack. Then

```
|k| ≥ K·u,     K = (π/2)·√(W₄ / (θ t₃))
```

At `θ = 1/2`: `K = 17.04` (historical kernel), `K = 23.66` (v10a.26).

## Consequences

**The criterion does not depend on C2.** `K` enters only through `√W₄`, so the
larger of the two disputed bandwidths bounds both. `K = 23.66` is valid
whichever kernel the adjudication selects — this can be stated now, before G3
runs.

**It bounds the coupling range where the claim means anything.** `K·u < π`
requires `u < 0.133` at `θ = 1/2` (`u < 0.188` at `θ = 1`). Above that the
excluded ball covers the zone and there is no near-Gamma statement to make.

**It quantifies what is given up.** The excluded fraction grows as `u³`: 0.18%
at `u = 0.02`, 2.79% at `u = 0.05`, 22.36% at `u = 0.10`.

## What this is not

A *sufficient* criterion from a conservative bound, not the sharp constant. It
says nothing about behaviour inside the ball — touching, level crossing, or
degeneracy there is untouched. And it is not the outward-rounded interval
arithmetic over the zone edges that forms the other half of G11.

G11 is therefore partially discharged, not closed. What remains is sharpening
`K`, analysing the interior, and the interval-rigor half.
