# 28. The T1 triplet at Γ: the near-Γ obstacle is a symmetry fact, and the flat band is isolated on the punctured zone

Date: 2026-09-04. Status: accepted. Bears on G11 (the near-Γ touching gate),
G17, G18; touches C2 (why a scalar re-anchoring could never decide it).

## Context

The corpus lists as open "a uniform near-Γ isolated-band theorem": the
second-order separation between the flat band and the two dispersive bands is
`t(u) q_a(k)`, of order `u²|k|²`, while the fourth-order kernel is of order
`u⁴`, so the two are said to compete for `|k| ≲ u`, and "a fixed-momentum
coefficient theorem is not a band theorem" (MASTER_THEORY §12). The ledger's
answer so far was G11's exclusion radius `|k| ≥ K u` with `K ≈ 17–24`
(`near_gamma.py`, the `uniformity` suite), inside which nothing was claimed.
That radius was derived from the premise that "the O(u⁴) operator does not
shrink at all" near Γ. It does shrink, and by symmetry.

## The observation

Two facts remove the competition rather than bounding it.

1. **At `k = 0` the three plaquette orientations are one irreducible triplet
   of the cubic group**, the `T₁` of the `1⁺⁻` channel: the three
   polarisations of a spin-1 state at rest. Every cubic-covariant effective
   Hamiltonian is therefore a *scalar* on that subspace, by Schur, at every
   order in `u`. The triple degeneracy at Γ is exact and unavoidable, and it
   is not an obstacle: it is what a vector particle at rest looks like.
2. **Inversion kills the linear term**, so every order's deviation from its
   Γ scalar is `O(|k|²)`, not just the second order's. On the Hodge form this
   is explicit: `H4(k) − s I` is built from `L↑`, `Λ = B B†` and its
   cross-plane half, all vanishing quadratically at Γ.

With the Hodge Laplacian `L↓ + L↑ = q_a I` (so `Λ = q_a P_t`, `L↑ = q_a P_c`
with `P_c` the carrier projector), the fourth-order kernel decomposes exactly:

```
H4(k) − s I = q_a(k) [ (−ν̃ + 2C) P_c + ε(k) P_t ] − 2C diag(a₁, a₂, a₃),
ε(k) = u q_a − 8u − π̃ ,      a_i = 4 sin²(k_i/2),
```

The carrier coefficient is `−ν̃ + 2C = A + 2C = β/8`: the assembled `β₃/8`
exactly, which is how the shape coefficient enters the isolation constant. So
`‖H4(k) − s I‖ ≤ C_iso q_a(k)` with
`C_iso = max(|−ν̃ + 2C|, sup|ε|) + 2|C|`. For the assembled `C_shp` the carrier
coefficient dominates (`−ν̃ + 2C ≥ 4u − π̃`) and `C < 0`, so
`C_iso = −ν̃ = 5/48` exactly; numerically the supremum of the ratio over the
zone is `5/48`, attained on an axis, so the bound is tight. By Weyl's
inequality the three eigenvalues of `M(k) = t(u) Λ(k) + u⁴ (H4(k) − sI)`
satisfy

```
E₁(k) − E₀(k) ≥ q_a(k) ( t(u) − 2 C_iso u⁴ ) ≥ q_a(k) u² ( t₃ − (5/24) u² ) > 0
```

at every `k ≠ 0`, for every `0 < u < u* = √(t₃ / (2 C_iso)) = √(2/51) ≈ 0.198`
(using `t(u) ≥ t₃ u²`, since `b₃ > 0`). The lowest band is the carrier's, its
eigenvector within a `k`-uniform angle of `ψ(k)` (Davis–Kahan), and the
projected one-band Hamiltonian is well defined on the whole punctured zone.
**No exclusion radius.** With the historical `C_shp` the constant is
`C_iso ≈ 0.112` and `u* ≈ 0.191`; the conclusion does not depend on which
side of C2 one reads.

## Corollary: a band theorem at fourth order

The carrier expectation of the centered kernel is the corpus's dispersion,
exactly as Laurent polynomials: `ψ†(H4 − sI)ψ = A q_a² + 4C e₂` with
`‖ψ‖² = q_a`, i.e. `A q_a + 4C e₂/q_a`, the `B = D = 0` shape. With the
isolation gap above, the Kato–Temple inequality gives, for the lowest band of
`M(k) = t(u)Λ + u⁴(H4 − sI)`,

```
| E₀(k) − u⁴ ( A q_a + 4C e₂/q_a ) |  ≤  C_iso² u⁶ q_a(k) / ( t₃ − 2 C_iso u² )
```

uniformly on the punctured zone, for every `u < u*`. So at this order a
fixed-momentum coefficient theorem *is* a band theorem: the fourth-order
dispersion is the band's dispersion, with a remainder two orders down and
proportional to the same `q_a` that closes at Γ. On `T_L³` every `k ≠ 0` has
`q_a ≥ 4 sin²(π/L)`, so the finite-volume isolation at fourth order closes as
`L⁻²` with the same constants — the corpus's `Δ^{(2)}_{N,L}` statement,
carried two orders up.

## What is claimed, and what is not

Claimed, at T1: the irreducibility (character norm 48), the scalar at Γ
(`s = q_band^(4)` for either kernel, since `C` multiplies an operator that
vanishes at Γ — which is also why a scalar re-anchoring could never decide
C2), the absence of a linear term, the Hodge-Laplacian identities, the exact
decomposition, the constant `5/48` and the threshold `2/51`; at T0, the
rational arithmetic of the constant and the threshold and the positivity of
the relative gap below it; at T2, the tightness of the bound.

Not claimed: anything about the sum of all orders. Each order `n` has the
same structure by the same symmetry — `H_n(k) − s_n I = O(q_a)` with some
constant `C_n` — so the fixed-order isolation holds at every order below a
threshold `u*_n`, but bounding the constants uniformly is the convergence
question of G17, untouched here. Nor is anything claimed about the continuum
limit; the boundary in `CLAUDE.md` §4 stands.

## Decision

- A new suite, `gamma_isolation`, with the seven checks above (five T1, two T2).
- Six Lean theorems: the sign of `π̃`, the domination condition, the sign of
  the assembled `C_shp`, `C_iso = 5/48`, `u*² = 2/51`, and the positivity of
  the relative gap below it.
- G11's near-Γ gate is recorded as discharged at fourth order; its interval
  half (outward-rounded π) is untouched. The corpus's §12 sentence is a
  claim, not evidence, and is not edited.

## Consequences

The near-Γ region is no longer a place where the fourth-order results are
silent. Whatever a future band theorem needs from the fourth order, it can
take from the whole zone.
