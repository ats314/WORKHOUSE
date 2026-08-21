---
title: "EXTRACT 01 — Haar Measure in Exponential Coordinates and the Haar Mass Term"
date: "2025-12-29"
format: "markdown+latex"
source_files:
  - "PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md"
---

# Haar measure \(\Rightarrow\) a local convexity (“mass”) contribution

## 1. Setup: a compact Lie group with a bi-invariant metric

Let \(G\) be a compact, connected Lie group equipped with a **bi-invariant** Riemannian metric \(g_G\).  
Let \(\mathfrak g\) be its Lie algebra, and use the Lie exponential map
\[
\exp_G : \mathfrak g \to G.
\]
For a bi-invariant metric, \(\exp_G\) coincides with the Riemannian exponential at the identity \(e\in G\), so \(\theta\in\mathfrak g\) is a normal coordinate near \(e\).

Fix an orthonormal basis \(\{e_i\}_{i=1}^{n_G}\) of \((\mathfrak g,\langle\cdot,\cdot\rangle_G)\) and write
\[
\theta = \sum_{i=1}^{n_G} \theta^i e_i \qquad (\theta^i\in\mathbb R).
\]

## 2. Haar volume density in geodesic normal coordinates

In a normal coordinate chart at \(e\), the Riemannian volume form has the form
\[
d\mathrm{vol}_{g_G}(U) \;=\; J_G(\theta)\, d\theta,
\]
where \(d\theta\) is Euclidean Lebesgue measure on \(\mathbb R^{n_G}\) and \(J_G(\theta)=\sqrt{\det(g_{ij}(\theta))}\) is the Jacobian density.

Standard Riemannian normal-coordinate expansions give
\[
J_G(\theta)
\;=\;
1 \;-\; \frac{1}{6}\,\mathrm{Ric}_{ij}(e)\,\theta^i\theta^j \;+\; \mathcal O(|\theta|^3),
\]
where \(\mathrm{Ric}_{ij}(e)\) are the components of the Ricci tensor at \(e\).

### Haar potential
Define the **Haar potential**
\[
S_H(\theta) \;:=\; -\log J_G(\theta).
\]
Using \(\log(1+\varepsilon)=\varepsilon+\mathcal O(\varepsilon^2)\) and the fact that \(J_G(\theta)=1+\mathcal O(|\theta|^2)\), one obtains
\[
S_H(\theta)
=
\frac{1}{6}\,\mathrm{Ric}_{ij}(e)\,\theta^i\theta^j \;+\; \mathcal O(|\theta|^3).
\]

In particular,
\[
\left.\frac{\partial^2 S_H}{\partial \theta^i\partial\theta^j}\right|_{\theta=0}
\;=\;
\frac{1}{3}\,\mathrm{Ric}_{ij}(e).
\]
Equivalently, as a bilinear form on \(\mathfrak g\),
\[
\nabla^2 S_H(0) \;=\; \frac{1}{3}\,\mathrm{Ric}_G(e).
\]

## 3. Positivity: “mass from Haar geometry”

Assume the group has a Ricci lower bound
\[
\mathrm{Ric}_G \;\ge\; \kappa_G\, g_G
\qquad\text{(quadratic form sense),}
\]
with \(\kappa_G>0\) (true for compact simple groups in standard normalizations).

Then
\[
\nabla^2 S_H(0) \;\ge\; \frac{\kappa_G}{3}\, \mathrm{Id}_{\mathfrak g}.
\]

Thus, near \(\theta=0\), \(S_H\) is strictly convex and has a quadratic lower bound:
\[
S_H(\theta) \;\ge\; \frac{\kappa_G}{6}\,|\theta|^2 \;+\; \mathcal O(|\theta|^3).
\]

This is the sense in which the Haar measure contributes an intrinsic **local quadratic “mass term”** in exponential coordinates.

## 4. Lattice configuration manifold: product Haar potential

Let \(\Lambda\) be a finite lattice, \(E(\Lambda)\) its edge set, and
\[
M_\Lambda \;=\; G^{E(\Lambda)}
\]
the configuration manifold with the product metric \(g_\Lambda\) and product Haar (Riemannian) volume \(d\mathrm{vol}_{g_\Lambda}\).

Near the trivial configuration \(U^{(0)}\) (all links equal to \(e\)), exponential coordinates assign \(\theta_\ell\in\mathfrak g\) to each edge \(\ell\):
\[
U_\ell = \exp_G(\theta_\ell).
\]

The product volume form becomes
\[
d\mathrm{vol}_{g_\Lambda}(U)
=
\prod_{\ell\in E(\Lambda)} J_G(\theta_\ell)\,d\theta_\ell
=
\exp\!\left(-\sum_{\ell\in E(\Lambda)} S_H(\theta_\ell)\right)\, d\theta,
\]
where \(d\theta\) is Lebesgue measure on \(\mathfrak g^{E(\Lambda)}\).

Define the lattice Haar potential
\[
S_{H,\Lambda}(\theta) := \sum_{\ell\in E(\Lambda)} S_H(\theta_\ell).
\]
Then its Hessian at the trivial configuration is block-diagonal with the single-link Hessians:
\[
\nabla^2 S_{H,\Lambda}(0)
=
\bigoplus_{\ell\in E(\Lambda)} \nabla^2 S_H(0)
\;\ge\;
\frac{\kappa_G}{3}\,\mathrm{Id}_{\mathfrak g^{E(\Lambda)}}.
\]

By continuity, there exists a radius \(r>0\) such that on a small-field ball \(\|\theta\|\le r\),
\[
\nabla^2 S_{H,\Lambda}(\theta) \;\ge\; c_H\,\mathrm{Id}
\qquad\text{for some } c_H>0 \text{ independent of }\Lambda.
\]

## 5. Two equivalent viewpoints (important for later)

There are two equivalent ways to “bookkeep” this contribution:

1. **Riemannian-volume reference.**  
   Work with reference measure \(d\mathrm{vol}_{g_\Lambda}\) and Gibbs density \(e^{-S_W}\).  
   Then the Bakry–Émery tensor is
   \[
     \mathrm{Ric}_\mu = \mathrm{Ric}_{g_\Lambda} + \nabla^2 S_W.
   \]
   The “Haar mass” is encoded in \(\mathrm{Ric}_{g_\Lambda}\).

2. **Flat Lebesgue reference (exponential coordinates).**  
   Work with reference measure \(d\theta\) and include \(S_{H,\Lambda}\) in the action.  
   Then the effective potential is \(S_W + S_{H,\Lambda}\) and the strict convexity is explicit at the level of \(\nabla^2(S_W+S_{H,\Lambda})\).

In either picture, the geometric conclusion is the same: **near the vacuum, Haar geometry produces uniform convexity** that can be used as the seed curvature lower bound for Bakry–Émery methods.
