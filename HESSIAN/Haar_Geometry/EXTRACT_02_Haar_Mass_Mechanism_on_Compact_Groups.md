---
title: "The Haar Mass Mechanism"
subtitle: "How compact Lie-group geometry produces a local quadratic confinement in exponential coordinates"
author: "Extracted and restructured from the project draft"
date: "2025-12-28"
---

## 0. Why this module is interesting

On a compact Lie group \(G\), the **Haar measure is not flat** in exponential coordinates. Near the identity, its Jacobian behaves like
\[
J(X) = 1 - \tfrac16 \mathrm{Ric}_e(X,X) + O(|X|^3),
\]
so the induced “Haar potential” \(S_H=-\log J\) has a **strictly positive Hessian** proportional to the Ricci tensor.

In lattice gauge theory, configuration space is a product \(G^{E(\Lambda)}\). The product Haar measure therefore contributes a **uniform** quadratic confinement per edge—an effect that behaves, in the Bakry–Émery language, like an intrinsic *mass term* coming from geometry.

This is not “mass generation” in the physical sense by itself, but it is a sharp and geometrically clean source of **positive curvature** and **local convexity** that can feed functional inequalities and spectral-gap arguments.

A potentially striking conceptual alignment is:

- For Abelian groups (e.g. \(U(1)\)), the bi-invariant metric is flat and \(\mathrm{Ric}=0\): **no Haar mass**.
- For non-Abelian compact semisimple groups (e.g. \(SU(N)\)), \(\mathrm{Ric}>0\): **positive Haar mass**.

That mirrors (heuristically!) the difference between Coulomb-like behavior in Abelian theories and mass-gap behavior expected in non-Abelian Yang–Mills—though one must not confuse local geometric convexity with a full physical mass gap.

---

## 1. Haar measure in exponential coordinates

Let \(G\) be a compact Lie group with a fixed **bi-invariant** Riemannian metric \(g_G\). Identify \(T_eG\simeq \mathfrak g\) with inner product \(\langle\cdot,\cdot\rangle_G\).

Let \(\exp_G:\mathfrak g\to G\) be the Lie exponential. For \(|X|\) sufficiently small, \(\exp_G\) is a diffeomorphism onto a neighborhood of the identity.

Define the local coordinate chart
\[
X\in \mathcal U_0\subset \mathfrak g \quad \longmapsto \quad U=\exp_G(X)\in G.
\]

In these **geodesic normal coordinates**, the Riemannian (Haar) volume is
\[
d\mathrm{vol}_{g_G}(U) = J_G(X)\, dX,
\]
where \(dX\) is Lebesgue measure on \(\mathfrak g\simeq \mathbb R^{\dim G}\), and \(J_G(X)>0\) is smooth.

Define the **Haar potential**
\[
S_H(X):= -\log J_G(X),
\]
so that \(J_G=e^{-S_H}\).

---

## 2. The key local expansion: Hessian of the Haar potential

A standard fact in Riemannian geometry is that in normal coordinates around a point \(x_0\),
\[
\sqrt{\det g_{ij}(X)}
= 1 - \frac16\,\mathrm{Ric}_{ij}(x_0)\,X^iX^j + O(|X|^3).
\]
Applied to \(x_0=e\in G\), this gives:

**Lemma 2.1 (Jacobian expansion at the identity).**  
In normal coordinates around \(e\),
\[
J_G(X)=1-\frac16\,\mathrm{Ric}_e(X,X)+O(|X|^3).
\]

Consequently, since \(\log(1+\varepsilon)=\varepsilon+O(\varepsilon^2)\),
\[
S_H(X)=-\log J_G(X)
= \frac16\,\mathrm{Ric}_e(X,X)+O(|X|^3).
\]

**Corollary 2.2 (Hessian at the identity).**  
The Hessian of \(S_H\) at \(0\in\mathfrak g\) satisfies
\[
\nabla^2 S_H(0) = \frac13\,\mathrm{Ric}_e
\]
as quadratic forms on \(\mathfrak g\). Equivalently,
\[
\nabla^2 S_H(0)(X,X)=\frac13\,\mathrm{Ric}_e(X,X).
\]

---

## 3. Positivity: when does Haar mass exist?

Assume a Ricci lower bound
\[
\mathrm{Ric}_e(X,X)\ge \kappa_G |X|_G^2\qquad (\kappa_G\ge 0).
\]
Then
\[
\nabla^2 S_H(0)\ge \frac{\kappa_G}{3}\,\mathrm{Id}.
\]
By continuity, there exist \(r>0\) and \(c>0\) such that for \(|X|\le r\),
\[
\nabla^2 S_H(X)\ge c\,\mathrm{Id}.
\]
So \(S_H\) is **strongly convex** near the identity.

### 3.1 Abelian vs non-Abelian

- If \(G\) is a torus \(U(1)^k\), the bi-invariant metric is flat: \(\mathrm{Ric}\equiv 0\). Then \(S_H\) has **no quadratic confinement** to second order.

- If \(G\) is compact semisimple with the standard bi-invariant metric (e.g. minus the Killing form on each simple factor), \(\mathrm{Ric}\) is positive definite. Then \(S_H\) contributes a strictly positive quadratic form.

This is the sense in which the Haar measure contributes a **local mass-like quadratic term** near the identity.

---

## 4. Lattice configuration space: product Haar mass is uniform in volume

Let \(E(\Lambda)\) be the set of oriented edges of a finite lattice \(\Lambda\). The lattice configuration manifold is
\[
M_\Lambda := G^{E(\Lambda)}.
\]
The product Haar volume equals the Riemannian volume for the product metric:
\[
d\mathrm{vol}_{g_\Lambda}(U)=\prod_{\ell\in E(\Lambda)} d\mathrm{vol}_{g_G}(U_\ell).
\]

In exponential coordinates \(U_\ell=\exp_G(X_\ell)\), define the product Jacobian
\[
J_\Lambda(X):=\prod_{\ell} J_G(X_\ell),
\qquad X=(X_\ell)_{\ell\in E(\Lambda)}\in \mathfrak g^{E(\Lambda)}.
\]
Then
\[
d\mathrm{vol}_{g_\Lambda}(U)=J_\Lambda(X)\,dX
=\exp\!\Big(-\sum_{\ell} S_H(X_\ell)\Big)\,dX.
\]
Define the lattice Haar potential
\[
S_{H,\Lambda}(X):=\sum_{\ell\in E(\Lambda)} S_H(X_\ell).
\]

**Proposition 4.1 (Uniform Haar convexity).**  
If \(\mathrm{Ric}_e\ge \kappa_G g_G\) on \(G\), then
\[
\nabla^2 S_{H,\Lambda}(0)\ge \frac{\kappa_G}{3}\,\mathrm{Id}
\]
on \(\mathfrak g^{E(\Lambda)}\), and this lower bound is **independent of \(\Lambda\)**.

So the “Haar mass per edge” does not deteriorate as the lattice grows.

---

## 5. Two equivalent viewpoints: curvature vs potential

There are two equivalent ways to account for this effect in Bakry–Émery analysis:

1. **Riemannian-volume reference (curvature viewpoint).**  
   Work on \((M_\Lambda,g_\Lambda)\) with reference measure \(d\mathrm{vol}_{g_\Lambda}\).  
   Then Haar enters via \(\mathrm{Ric}_{g_\Lambda}\ge \kappa_G g_\Lambda\).

2. **Flat reference in Lie algebra (potential viewpoint).**  
   Work on \((\mathfrak g^{E(\Lambda)},\text{Euclidean})\) with reference \(dX\).  
   Then Haar enters as an additional potential \(S_{H,\Lambda}\) with \(\nabla^2 S_{H,\Lambda}(0)\ge (\kappa_G/3)\mathrm{Id}\).

Mathematically they encode the same second-order information.

---

## 6. What could be “new theory” here?

The bare statement “Haar Jacobian has Ricci in its Taylor expansion” is classical. The potentially novel part is **using it as a structural input** for gauge-theory functional inequalities and mass-gap heuristics:

- Haar mass provides a *geometric* baseline curvature constant \(\kappa_G\) that is:
  - independent of volume,
  - present for non-Abelian groups,
  - absent for Abelian groups.

This suggests treating \(\kappa_G\) as an analytic “marker” for whether curvature-based functional inequalities have a chance to be volume-uniform in the physical sector.

A programmatic conjecture one could try to formalize is:

> The existence (and size) of a uniform Bakry–Émery curvature window near the vacuum in lattice gauge theory correlates with the semisimple (positively Ricci-curved) component of the gauge group.

This is not a mass-gap theorem—but it is a crisp geometric lever that does *not* exist in scalar Euclidean models.

---

## 7. Further work that would strengthen this mechanism

1. **Beyond the identity neighborhood.**  
   Quantify how far the strong convexity region extends and how it interacts with the Wilson action away from the vacuum.

2. **Interaction with gauge orbits.**  
   Understand how Haar mass competes with degeneracies along gauge orbits and with toron modes on periodic lattices.

3. **Scaling limits.**  
   Track how the constants depend on lattice spacing and on the normalization of \(g_G\) under renormalization.

4. **Synthetic curvature on quotients.**  
   Explore whether the quotient metric-measure space \(M_\Lambda/\mathcal G_\Lambda\) inherits synthetic curvature lower bounds in a form that reflects Haar mass.

