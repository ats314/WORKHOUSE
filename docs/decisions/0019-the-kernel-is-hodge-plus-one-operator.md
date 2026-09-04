# 19. The fourth-order kernel is a Hodge polynomial plus one operator, and C_shp is that operator's weight

Date: 2026-09-01. Status: accepted. Amends U5 (`ledger/gaps.yaml`); bears on G14, G3, C2.

## Context

The corpus already has the algebra. GLUEBALL v3.1 §6.2 defines the down and
up Laplacians on plaquettes, `L↓ = ∂₂†∂₂` and `L↑ = ∂₃∂₃†`, proves `L↓L↑ = 0`
and that every polynomial in them acts on the harmonic sector by its constant
term; THM_FLUX Prop. 2 identifies the signed shared-edge adjacency as
`S_□ + 4I = B†B`, and reads the second-order flatness as `H⁽²⁾ = a₂I + t_N S_□`.
§7 pulls the fourth-order kernel back to cubes as a "generalized Hodge pencil".
What no document recorded is whether the fourth-order kernel *itself* lies in
that algebra, and if not, by how much.

## What was computed

Incidence algebra on records, `src/workhouse/kernel_orbits.py`, exact.

1. The unit sign pattern of the two disputed orbits — the 24 cross-plane
   records of `rho` and the 12 coplanar records of `pi` — **is** the
   off-diagonal of `L↓`, i.e. `S_□ = L↓ − 4I`, exactly.
2. `S_□²`, as an operator product on records, is the 132-record skeleton plus
   the 12-record doubled orbit at unit weight (so `u2 = 2u` is the two coplanar
   paths), plus a diagonal shadow: −4 on the normal keys, −2 on the in-plane
   keys, +12 on site. The 144 records the two rival kernels agree on in shape
   are `u S_□²`, and the `−4u` the normal orbit carries beyond `−5/48` is that
   shadow, not a correction to the cube channel.
3. With `ν̃ = ν + 4u`, `π̃ = π + 2u`, `σ̃ = σ − 12u` and `R` the cross-plane half
   of `S_□` (equivalently minus the cross-plane half of `L↑`):

       H₄ = −ν̃ (L↑ − 2) + u S_□² − π̃ S_□ + σ̃ I − 2 C_shp R

   holds on all 189 records of the historical kernel exactly, with
   `ν̃ = −5/48`, and on the v10a.26 dump to 1e-13 relative, with the same `ν̃`.
4. On the cube-boundary carrier `L↓ψ = 0` and `L↑ψ = e₁ψ`, so every term but
   the last is a scalar there: `A = −ν̃ = 5/48` with no `u` in it, `B = D = 0`
   with nothing to cancel, and `4C e₂` is the projection of `−2C R` alone.

## Decision

- **G14.** The tier collapse is the Hodge structure of the kernel: the only
  operator outside the algebra of the two Laplacians is `R`, and `R` projects to
  pure `e₂`. The "why a product" question closes — it is a square. What remains
  is one dynamical input, the universality of `u` across all two-hop chains,
  the fourth-order form of Prop. 2's "the same local fusion coefficient
  multiplies every surviving shared-edge pair".
- **C2.** `C_shp` is the coefficient of the single non-Hodge operator, and the
  carrier is an exact eigenvector of `H₄` iff `C_shp = 0`. The disagreement is
  four numbers `(u, ρ, π̃, σ̃)`; `u` and `σ̃` reach the carrier band only through
  its constant, so C2 is exactly `C_shp = −5/96 − (ρ + π̃)/2`. The 4.13× scale
  on `u` is a real fourth disagreement (`ν̃` agrees, so no normalisation
  relates the kernels) and is band-invisible on the carrier.
- **U5, amended.** Its step "the primitive cube-completion channel IS the
  normal orbit, so `Δν = 0`, hence `Δu = 0`" is withdrawn: eps-blindness fixes
  `ν̃`, which is the same statement as `ΔA = 0`, and constrains `u` not at all.
  The two recorded kernels are the witness. The prediction survives as
  `Δ(ρ + π̃) = −25/512`, with `u`, `u2`, `σ̃` free; the check is renamed
  `CORRECTED PREDICTION` and its yielded constants replaced.
- **G3.** A new untried route, the chain amplitude `u` on the three-plaquette
  cluster: it cannot decide C2, but it decides which pipeline is trustworthy on
  a quantity far smaller than the perpendicular-pair assembly.

Nothing prefers either side of C2 and nothing is promoted.

## Consequences

- Four checks in the kernel-orbits suite, two T1 and one T2 for the form and
  one T1 correction; `kernel_orbits` carries the incidence machinery
  (`down_laplacian`, `up_laplacian`, `compose`, `hodge_form`, `hodge_records`,
  `acts_as`).
- `ledger/symbols.yaml` gains `pi~` and `sigma~` as coined names, registered
  by value.
- The identity `L↓L↑ = 0` on the cubic complex and `S_□ψ = −4ψ` are pure
  incidence algebra and are candidates for `lean/Workhouse/`.
