# PRO12 Notes 03 — Haar Jacobian Curvature Floor and the SAFE-Region Constants

## 1. Why the Haar measure shows up as a convex potential
On a single link, write the group element in exponential coordinates:

U = exp(X),   X ∈ 𝔤.

The Haar measure in these coordinates is

Haar(dU) = J(X) dX,

where J(X) is the Jacobian determinant of the exponential map.

If the lattice YM measure is

μ(dU) ∝ exp(-S_W(U)) Haar(dU),

then in X-coordinates (relative to Lebesgue dX) the negative log density is

S_eff(X) = S_W(exp X) - log J(X)
         = S_W(exp X) + V_Haar(X)

with the **Haar potential**

V_Haar(X) := -log J(X).

This is important because Bakry–Émery curvature contains ∇²V.
Even if the Riemannian Ricci term is too small / complicated, a strongly convex V_Haar can supply a uniform curvature floor.

---

## 2. The Lie-algebra formula for J(X)
A standard compact Lie group identity expresses J(X) using the adjoint map ad_X : 𝔤 → 𝔤,

ad_X(Y) := [X,Y].

One has the matrix-function identity

J(X) = det( (I - exp(-ad_X)) / ad_X ).

The key numerical trick is to avoid dividing by ad_X (which has zero modes for every X) by using the integral representation

(I - exp(-A)) / A = ∫_0^1 exp(-sA) ds.

So you can compute J(X) stably as

J(X) = det( ∫_0^1 exp(-s ad_X) ds ).

This form is also autodiff-friendly.

---

## 3. Local Hessian constants at the identity
Using anti-Hermitian generators with Tr(T_a T_b) = -½ δ_ab, the Hessian of V_Haar at X=0 is isotropic.
Numerically (double precision, autodiff Hessian), you get:

- SU(2): eigenvalues ≈ 1/6 ≈ 0.166666…
- SU(3): eigenvalues ≈ 1/4 = 0.25

These match the repo’s SAFE-region ledger constant

κ* ≈ 0.25   (SU(3)).

---

## 4. What the “SAFE region” is doing
Define a ball in right-invariant exponential coordinates on each link, e.g.

‖X_ℓ‖ ≤ R0.

In this region, you want two uniform operator bounds:

1. Haar curvature floor:

   λ_min( ∇²V_Haar(X) ) ≥ κ*

2. Wilson variation smallness:

   sup_{‖X‖≤R0} ‖ ∇²S_W(exp X) - ∇²S_W(exp 0) ‖ ≤ δ.

Then you can lower bound the total “curvature operator” in horizontals by

κ* - δ.

The repo packages this as a per-step degradation factor

α = 1 - δ/κ*.

For SU(3), the ledger values are

- κ* ≈ 0.25
- δ ≈ 0.006
- α ≈ 0.976

meaning SAFE-region curvature is robust under many coarse-graining steps.

---

## 5. How to reproduce κ* numerically (small linear algebra, big payoff)
Because dim 𝔰𝔲(3)=8, the “single-link” Hessian is just 8×8.
That means you can scan κ* on a radius ball by brute force:

1. sample X uniformly / quasi-uniformly in ‖X‖≤R0
2. compute the 8×8 Hessian (or HVPs + Lanczos)
3. record the minimum eigenvalue.

The repo also points out that doing this in right-invariant coordinates makes the operator norms comparable across the SAFE region.

The provided Colab code does this with autodiff Hessian–vector products and a tiny Lanczos routine.

---

## 6. Why this matters for the “H1 as output” program
If you can certify κ*>0 on a SAFE patch and you have a drift/Lyapunov argument that returns you to that patch, you can upgrade local convexity into global LSI.
The missing pieces are then:

- derive the PBH/Riccati inequality from an actual RG map / flow equation,
- prove the source term is positive in the horizontal/local sector,
- show off-diagonal mixing does not destroy the local curvature lower bound.

Those are exactly the targets of the numerical experiments.
