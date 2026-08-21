Document 2 — Viscous Hamilton–Jacobi and Riccati Flow for the Hessian

# Document 2: Viscous Hamilton–Jacobi and Riccati Flow

This document captures the “dynamic convexity” machinery: how an effective action \(S_t\) evolves under a smoothing flow, and how its Hessian obeys a Riccati-type evolution.

## 1. Viscous Hamilton–Jacobi Equation

Let \((M,g)\) be a Riemannian manifold (eventually configuration space). Consider a family of densities \(\rho_t\) evolving by the heat equation
\[
  \partial_t \rho_t = \Delta \rho_t.
\]
Write
\[
  \rho_t(x) = Z_t^{-1} e^{-S_t(x)},
\]
where \(S_t\) is a time-dependent effective action and \(Z_t\) normalizes the density.

**Proposition 1.1 (vHJ Equation).**  
Up to an additive time-dependent constant, \(S_t\) satisfies
\[
  \partial_t S_t = \Delta S_t - \|\nabla S_t\|^2.
\]

*Proof.*  
Differentiate:
\[
  \partial_t \rho_t = -(\partial_t S_t + \partial_t \log Z_t)\,\rho_t.
\]
Compute
\[
  \Delta \rho_t
  = \nabla\cdot(-e^{-S_t}\nabla S_t)
  = -e^{-S_t}\Delta S_t + e^{-S_t}\|\nabla S_t\|^2
  = \rho_t(-\Delta S_t + \|\nabla S_t\|^2).
\]
Equating \(\partial_t\rho_t = \Delta \rho_t\) and dividing by \(\rho_t\) gives
\[
  -(\partial_t S_t + \partial_t\log Z_t)
  = -\Delta S_t + \|\nabla S_t\|^2.
\]
Absorb \(\partial_t\log Z_t\) into an additive time-dependent constant; the spatial part obeys
\[
  \partial_t S_t = \Delta S_t - \|\nabla S_t\|^2.
\]
∎

## 2. Hessian Evolution: Matrix Reaction–Diffusion

Let \(H_t = \nabla^2 S_t\) be the Hessian tensor. In local coordinates \(x=(x_i)\), write \(H_{ij} = \partial_i\partial_j S_t\).

**Theorem 2.1 (Hessian PDE).**  
In Euclidean space (or in normal coordinates, up to curvature terms),
\[
  \partial_t H_t = \Delta H_t - 2(\nabla S_t \cdot \nabla) H_t - 2 H_t^2.
\]

*Proof.*  
We work in \(\mathbb{R}^d\). The vHJ equation is
\[
  \partial_t S = \Delta S - \sum_k (\partial_k S)^2.
\]
Differentiate once:
\[
  \partial_t(\partial_i S)
  = \Delta(\partial_i S) - 2\sum_k (\partial_k S)(\partial_k\partial_i S).
\]
Differentiate again:
\[
  \partial_t(\partial_j\partial_i S)
  = \Delta(\partial_j\partial_i S)
    - 2\sum_k \partial_j\big[(\partial_k S)(\partial_k\partial_i S)\big].
\]
Expand:
\[
  \partial_t H_{ij}
  = \Delta H_{ij}
    - 2\sum_k\big[(\partial_j\partial_k S)(\partial_k\partial_i S)
                 + (\partial_k S)(\partial_j\partial_k\partial_i S)\big].
\]
The first term is \((H^2)_{ij}\). The second is advection:
\[
  \sum_k (\partial_k S)(\partial_k H_{ij})
  = (\nabla S\cdot\nabla) H_{ij}.
\]
Thus
\[
  \partial_t H_{ij}
  = \Delta H_{ij}
    - 2(\nabla S\cdot\nabla) H_{ij}
    - 2 (H^2)_{ij}.
\]
In matrix form:
\[
  \partial_t H_t = \Delta H_t - 2(\nabla S_t \cdot \nabla) H_t - 2 H_t^2.
\]
∎

This is a **matrix reaction–diffusion equation**: diffusion \(\Delta H_t\), advection along \(-\nabla S_t\), and a quadratic sink \(-2H_t^2\).

## 3. Riccati Inequality for the Smallest Eigenvalue

Let \(\lambda(t,x)\) denote the **smallest eigenvalue** of \(H_t(x)\), and let \(v(t,x)\) be a corresponding normalized eigenvector (\(\|v\|=1\)).

Formally,
\[
  \lambda(t,x) = \min_{\|u\|=1} \langle u, H_t(x) u\rangle.
\]

Differentiating \(\lambda = \langle v,H_t v\rangle\) in time, using symmetry of \(H_t\) and \(\|v\|=1\),
\[
  \partial_t \lambda = \langle v, (\partial_t H_t) v\rangle.
\]

Plug in the PDE for \(H_t\):
\[
  \partial_t \lambda
  = \langle v,\Delta H_t\,v\rangle
    - 2\langle v, (\nabla S_t\cdot\nabla)H_t\,v\rangle
    - 2\langle v,H_t^2 v\rangle.
\]
The last term is \(-2\lambda^2\).

The first two terms can be controlled using standard estimates (Bochner’s identity / Kato type inequalities) near spatial minima of \(\lambda\). At a point where \(\lambda\) is locally minimal in space, one has \(\nabla \lambda = 0\) and \(\Delta \lambda \ge 0\); one can show
\[
  \langle v,\Delta H_t v\rangle \ge \Delta \lambda.
\]
The advection term contributes \(-2(\nabla S_t\cdot\nabla)\lambda\).

**Theorem 3.1 (Riccati Inequality).**  
At points where \(\lambda\) is simple and sufficiently regular,
\[
  \partial_t \lambda
  \;\ge\; \Delta \lambda
          - 2(\nabla S_t\cdot\nabla)\lambda
          - 2\lambda^2.
\]

Heuristically, ignoring spatial derivatives (considering an ODE approximation),
\[
  \dot\lambda \gtrsim -2\lambda^2.
\]
Without a positive source, this tends to drive \(\lambda\) down to \(0\) over large “RG-time”.

## 4. Adding a Geometric Source Term

On a curved configuration manifold with intrinsic curvature or with an external “mass” source (like the Haar term on \(SU(N)\)), the Hessian PDE effectively picks up an additional positive term:
\[
  \partial_t H_t \approx \Delta H_t
  - 2(\nabla S_t\cdot\nabla)H_t
  - 2H_t^2
  + \Sigma_t,
\]
where \(\Sigma_t\) encodes curvature and measure effects.

If the smallest eigenvalue of \(\Sigma_t\) is bounded below by \(\sigma_*>0\), then the Riccati inequality becomes schematically
\[
  \partial_t \lambda \gtrsim -2\lambda^2 + \sigma_*.
\]

The associated scalar ODE
\[
  \dot \ell = -2\ell^2 + \sigma_*
\]
has a stable fixed point at
\[
  \ell_* = \sqrt{\sigma_*/2}.
\]

**Interpretation.**  
If you can **seed** the Hessian with some initial positive curvature and maintain a positive source term \(\sigma_*\) (from geometry / Haar measure / anomaly), the nonlinear \(-2H_t^2\) term can stabilize the minimal eigenvalue at a nonzero value instead of letting it decay to 0. This is the conceptual backbone behind the “primer vs sustainer” story: the lattice Haar mass primes convexity; the nonlinear Riccati flow sustains it under coarse-graining, at least conjecturally in the continuum limit.


⸻
