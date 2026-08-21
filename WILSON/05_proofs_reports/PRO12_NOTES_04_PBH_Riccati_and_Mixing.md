# PRO12 Notes 04 — PBH/Riccati from a Real RG Map, Source Positivity, and Mixing Control

## 0. Why this note exists
Three “hard steps” keep showing up as the exact place where the project becomes genuinely new:

1. Derive the PBH/Riccati inequality for the effective Hessian from an actual RG map (gradient-flow blocking / exact Polchinski-type equation), not as an axiom.
2. Prove positivity of the source term R(t) on the physical/horizontal sector.
3. Prove off-diagonal mixing stays controlled under coarse-graining so negative curvature cannot leak in.

The repo already has a clean *formal* PBH story; this note explains the shortest plausible route to making it non-formal.

---

## 1. The model PBH/Riccati inequality
The desired inequality for the (horizontal-restricted) effective Hessian is schematically

Ḣ(t) ≥ -2 H(t)² + R(t)

where

- H(t) is the Hessian (a symmetric operator on horizontals)
- R(t) is a “source” coming from geometry + RG forcing terms.

If R(t) is positive semidefinite on the physical sector, you get a convexity floor that persists.

The practical numerical form is:

⟨v, R(t) v⟩ = ⟨v, Ḣ(t) v⟩ + 2 ⟨H(t) v, H(t) v⟩  ≥ 0   for all horizontal v.

So you can test positivity by sampling random horizontal v and estimating the sign.

---

## 2. Where PBH should come from: exact effective-action flow
A promising “honest RG map” in the repo is **gradient-flow blocking**:

- evolve links by lattice Yang–Mills gradient flow (Wilson flow)
- define the induced effective action S_t[V] on flowed fields V via pushforward of the original measure.

There is a known exact functional differential equation for S_t (Yamamura 2016):

∂_t S_t[V] = Σ_{x,μ,a} ( ∂_{x,μ}^a S_t[V] · ∂_{x,μ}^a 𝒮_t[V]  -  ∂_{x,μ}^a ∂_{x,μ}^a 𝒮_t[V] )

for a chosen “flow action” 𝒮_t (often the Wilson action).

This is a nonabelian, gauge-covariant analogue of a Polchinski / Hamilton–Jacobi–Bellman equation.

**Key point:** once you have an equation of the form

Ṡ = ⟨∇S, ∇𝒮⟩ - Δ𝒮,

taking two derivatives in configuration space forces a Riccati structure: Hessians multiply.
That’s exactly where the “-2H²” term is supposed to come from.

---

## 3. The two technical traps
### Trap A: the Hessian lives on horizontals
The Hessian you need for LSI is the one relevant for gauge-invariant observables, i.e. restricted to the horizontal bundle via the projector P_U.
So “differentiate twice” must be interpreted as “differentiate twice, then Schur complement / project to horizontals”.

This is why mixing control matters: if the flow couples horizontals to vertical/ghost sectors too strongly, a naive positivity statement can fail.

### Trap B: source term sign is not automatic
Even if a Riccati structure appears, the leftover term R(t) contains:

- curvature terms (Ricci of the group manifold / bundle)
- commutators from covariant derivatives
- possible gauge-fixing / FP contributions

Showing that these combine to a positive operator on the physical sector is the genuine geometry-meets-QFT step.

The repo sketches a path where R(t) satisfies a maximum principle / heat-type inequality (so positivity propagates), but that must be made rigorous in the nonabelian horizontal setting.

---

## 4. Mixing control as a Schur complement / commutator problem
If you block-decompose the Hessian by “good sector” ⊕ “other sector”, then

H = [ A  B ; Bᵀ  C ].

The effective curvature on the good sector is controlled by the Schur complement

A - B C^{-1} Bᵀ.

So you need:

- C to have a safe positive lower bound, and
- B to be small enough (in norm) so the correction cannot flip the sign of A.

The repo’s locality/mixing lemmas suggest B decays rapidly with scale separation or spatial distance.
Numerically, you can probe this by building local projectors P_loc and estimating commutators:

‖[H, P_loc]‖  small  ⇒  weak mixing across the cut.

---

## 5. What to test numerically (small lattices are enough)
The Colab code shipped with these notes targets three concrete experiments:

1. **PBH finite-difference check**
   - define a flow map (Wilson flow or coordinate gradient flow)
   - compute H_t·v via HVPs
   - estimate ⟨v, Ḣ_t v⟩ by finite differences
   - report ⟨v, R_t v⟩ = ⟨v, Ḣ_t v⟩ + 2‖H_t v‖²

2. **Source positivity on horizontals**
   - compute v_h = P_U v by solving the FP equation
   - evaluate the R-quadratic form on v_h

3. **Mixing control diagnostics**
   - choose P_loc projecting to links in a spatial ball
   - estimate ‖[H, P_loc]‖ by random-vector power iteration
   - repeat after a blocking step to see whether mixing grows.

These don’t prove theorems, but they will brutally falsify any sign/mixing fantasy early.

---

## 6. How this upgrades H1 from axiom to output
If the numerical experiments consistently show:

- a positive SAFE curvature floor κ*
- a small perturbation δ from the action part
- PBH source positivity on horizontals
- controlled mixing under blocking

then the remaining analytic work is to replace “empirically positive” by “provably positive” using:

- explicit algebraic identities in su(2)/su(3)
- maximum principles for matrix inequalities along flow
- Schur complement estimates + locality bounds.

That is exactly the hinge work the project is trying to do.
