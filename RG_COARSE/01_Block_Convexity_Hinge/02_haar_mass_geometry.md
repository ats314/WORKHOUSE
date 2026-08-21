# Haar mass from group geometry: a uniform on-site convexity term

## Scope

This note isolates the **Haar/Riemannian geometry** contribution that appears throughout the project under names like “Haar mass” or “Ricci floor.” The useful deliverable is an *explicit* (volume-independent) quadratic lower bound on the effective curvature matrix near the vacuum, and a clear statement of what this does and does not control.

---

## 1. Haar measure as Riemannian volume and the Bakry–Émery tensor

Let \(G\) be a compact Lie group equipped with a bi-invariant Riemannian metric \(g_G\). Let \(\mathrm{vol}_{g_G}\) denote its Riemannian volume, which equals Haar measure up to normalization.

On a finite lattice \(\Lambda\) with link set \(E(\Lambda)\), the configuration manifold is
\[
M_\Lambda := G^{E(\Lambda)}
\]
with product metric \(g_\Lambda=\bigoplus_{\ell\in E(\Lambda)}g_G\) and product volume \(\mathrm{vol}_{g_\Lambda}\).

Given an action \(S_\Lambda\in C^2(M_\Lambda)\), the Gibbs measure is
\[
d\mu_\Lambda(U)=Z_\Lambda^{-1}\,e^{-S_\Lambda(U)}\,d\mathrm{vol}_{g_\Lambda}(U).
\]

The central geometric object for \(\Gamma_2\) / Helffer–Sjöstrand is the **Bakry–Émery tensor**
\[
\mathrm{Ric}_{\mu_\Lambda}\;:=\;\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_\Lambda.
\tag{1.1}
\]
This is exactly where the Haar geometry contributes: \(\mathrm{Ric}_{g_\Lambda}\) is already present before any action is added.

---

## 2. Ricci of a compact bi-invariant group and the “Ricci floor”

For a compact semisimple \(G\) with a bi-invariant metric, the Ricci tensor satisfies a positive lower bound
\[
\mathrm{Ric}_{g_G}\ \ge\ \kappa_G\,g_G
\qquad\text{for some }\kappa_G>0.
\tag{2.1}
\]
(The project stresses: a nontrivial torus factor forces \(\kappa_G=0\) along flat directions; for Yang–Mills one takes \(G=\mathrm{SU}(N)\), so \(\kappa_G>0\) under standard normalizations.)

By product structure,
\[
\mathrm{Ric}_{g_\Lambda}\ \ge\ \kappa_G\,g_\Lambda
\quad\text{(block-diagonal across links),}
\tag{2.2}
\]
and crucially the constant \(\kappa_G\) is **independent of \(|\Lambda|\)**.

This is the first “uniformity miracle”: the on-site Ricci curvature does not degrade with volume.

---

## 3. Equivalent exponential-coordinate formulation: Jacobian \(\Rightarrow\) convex effective potential

The same contribution can be expressed as a local convexity of the Haar Jacobian in exponential coordinates.

Let \(\exp_G:\mathfrak g\to G\) be the exponential map. In geodesic normal coordinates at the identity,
\[
d\mathrm{vol}_{g_G}(\exp_G X)\;=\;J_G(X)\,dX,
\]
with \(J_G(0)=1\) and \(J_G\) smooth. Standard Riemannian normal-coordinate expansions give
\[
J_G(X)=1-\frac{1}{6}\mathrm{Ric}_{g_G}(X,X)+O(|X|^3).
\tag{3.1}
\]
Define the **Haar potential**
\[
S_H(X):=-\log J_G(X).
\]
Then
\[
S_H(X)=\frac{1}{6}\mathrm{Ric}_{g_G}(X,X)+O(|X|^3),
\qquad
\nabla^2 S_H(0)=\frac{1}{3}\mathrm{Ric}_{g_G}.
\tag{3.2}
\]
If (2.1) holds, then
\[
\nabla^2 S_H(0)\ \ge\ \frac{\kappa_G}{3}\,\mathrm{Id}_{\mathfrak g}.
\tag{3.3}
\]

On the lattice configuration space, with linkwise exponential coordinates \(U_\ell=\exp_G(X_\ell)\),
\[
d\mathrm{vol}_{g_\Lambda}(U)=\prod_{\ell}J_G(X_\ell)\,\prod_{\ell}dX_\ell
=\exp\!\Big(-\sum_{\ell}S_H(X_\ell)\Big)\prod_{\ell}dX_\ell.
\tag{3.4}
\]
Thus the Haar measure acts like an additional effective potential
\[
S_{H,\Lambda}(X):=\sum_{\ell\in E(\Lambda)}S_H(X_\ell)
\]
with uniform quadratic Hessian floor
\[
\nabla^2 S_{H,\Lambda}(0)\ \ge\ \frac{\kappa_G}{3}\,\mathrm{Id}_{\mathcal C^1(\Lambda;\mathfrak g)}.
\tag{3.5}
\]

---

## 4. What this actually buys in the Yang–Mills lattice setting

### 4.1 Local curvature on a small-field region

If the action decomposes as \(S_\Lambda=S_W+S_{\mathrm{add},\Lambda}\) and you have a global lower bound
\[
\nabla^2 S_{\mathrm{add},\Lambda}\ \ge\ -C_{\mathrm{add}}\,g_\Lambda
\quad\text{with }C_{\mathrm{add}}\text{ independent of }\Lambda,
\tag{4.1}
\]
then on any region where the Wilson Hessian is nonnegative (or sufficiently controlled), you obtain a local Bakry–Émery lower bound
\[
\mathrm{Ric}_{\mu_\Lambda}
=
\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_W + \nabla^2 S_{\mathrm{add},\Lambda}
\ \ge\
(\kappa_G-C_{\mathrm{add}})\,g_\Lambda
\quad\text{(on that region).}
\tag{4.2}
\]
The project’s “Core curvature theorem” is exactly the implementation of this implication in a ball around the vacuum, and with the subtlety that only **horizontal** directions matter for gauge-invariant observables.

### 4.2 Lifting horizontal harmonic modes (“mass term” intuition)

At the vacuum, the Wilson quadratic form (second variation of \(S_W\)) is the discrete Maxwell operator \(d_1^*d_1\), which is nonnegative and has a kernel that includes harmonic and gauge directions.

The Ricci/Haar contribution is an on-site term \(\simeq \kappa_G\,\mathrm{Id}\). In the exponential-coordinate picture, this looks like adding a strictly convex quadratic term \(\sum_\ell \frac{\kappa_G}{6}|X_\ell|^2\) to the effective potential.

This is the precise sense in which Haar geometry supplies a “mass” that:

* does **not** depend on \(|\Lambda|\),
* lifts residual zero-modes on the horizontal sector when combined with the Wilson Hessian,
* enters exactly where the Helffer–Sjöstrand covariance representation wants it: inside the curvature matrix \(\mathrm{Ric}_{\mu_\Lambda}\).

---

## 5. Limits of the Haar-mass mechanism

1. The Haar/Ricci term is **local** and does not by itself produce correlation decay; it must be paired with the structured long-range coupling encoded in \(d_1^*d_1\) (via a Green’s-function estimate), and with a localization/globalization step to get global statements.

2. The Ricci floor is **metric-normalization dependent**. Any final “physical mass” statement must track how \(\kappa_G\) rescales with your choice of \(\langle\cdot,\cdot\rangle_{\mathfrak g}\) and with the lattice spacing convention (if inserted).

3. Haar mass is a **cutoff** object: making it survive \(a\downarrow 0\) at the correct physical scale requires a controlled continuum construction (project permanence lemmas), not just fixed-\(a\) geometry.

