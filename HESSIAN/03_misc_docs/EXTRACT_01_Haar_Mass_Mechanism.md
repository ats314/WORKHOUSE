---
title: "Haar Mass Mechanism: Jacobian-Induced Convexity in Lattice Gauge Theory"
author: "Project extraction"
date: "2025-12-29"
---

# Overview

This note extracts and reorganizes the **Haar-mass** idea from the project: the observation that the *Haar volume form* on a compact Lie group induces, in exponential coordinates, a **quadratic confining term** in the effective action. In the small-field regime this behaves like a *mass term* that can lift otherwise-flat directions (notably gauge directions) and contribute directly to **Bakry--Émery curvature** lower bounds.

The core ingredients appear in the project's Haar-measure section, including the coordinate expansion of the Riemannian volume density and the identification of the Hessian of the induced Haar potential with the group Ricci tensor. 【158:0†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L9-L33】【158:2†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L120-L140】

---

# 1. Setup: exponential coordinates and the Haar potential

Let \(G\) be a compact Lie group with a bi-invariant Riemannian metric \(g_G\), and write exponential coordinates near the identity:
\[
U(\theta)=\exp(\theta^a T_a),\qquad \theta\in\mathfrak g\simeq\mathbb R^n.
\]

In these coordinates, the Riemannian volume takes the form
\[
d\mathrm{vol}_G(U(\theta))=J_G(\theta)\,d\theta,
\qquad
J_G(\theta)=\sqrt{\det g(\theta)}.
\]
The project defines the associated **Haar potential**
\[
S_H(\theta):=-\log J_G(\theta).
\]
【158:0†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L9-L33】

On a finite lattice \(\Lambda\) with link set \(E(\Lambda)\), the configuration space is
\[
M_\Lambda = G^{E(\Lambda)},
\]
and the product Haar factor contributes the lattice Haar term
\[
S_{H,\Lambda}(X):=\sum_{\ell\in E(\Lambda)} S_H(X_\ell)
\]
in exponential coordinates \(X=(X_\ell)_\ell\in\mathfrak g^{E(\Lambda)}\). 【158:1†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L35-L58】

---

# 2. Derivation: volume density expansion and Hessian at the identity

In geodesic normal coordinates at the identity, the project uses the standard expansion
\[
g_{ij}(\theta)=\delta_{ij}-\frac13 R_{ikjl}(0)\,\theta^k\theta^l+O(|\theta|^3),
\]
hence
\[
\det g(\theta)=1-\frac13\operatorname{Ric}_{kl}(0)\,\theta^k\theta^l + O(|\theta|^3).
\]
This yields
\[
J_G(\theta)=1-\frac16\operatorname{Ric}_{kl}(0)\,\theta^k\theta^l+O(|\theta|^3),
\]
and therefore
\[
S_H(\theta)=-\log J_G(\theta)
= \frac16\,\operatorname{Ric}_{kl}(0)\,\theta^k\theta^l+O(|\theta|^3).
\]
【158:2†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L120-L140】

Differentiating twice at \(\theta=0\) gives the key identity:
\[
\nabla^2 S_H(0)=\frac13\,\operatorname{Ric}_G.
\]
This is recorded explicitly in the project as Proposition 5.1. 【158:3†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L145-L167】

---

# 3. Positivity and the "Haar mass" interpretation

Assume a **Ricci lower bound** for the group metric:
\[
\operatorname{Ric}_G \ge \kappa_G\, g_G,\qquad \kappa_G>0.
\]
Then
\[
\nabla^2 S_H(0)\ge \frac{\kappa_G}{3}\, g_G,
\]
so the Haar potential is strictly convex to second order at the identity. 【158:3†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L145-L167】

The project then packages this convexity into the language of an effective quadratic term:
\[
S_H(\theta)\approx \frac12\,c_H\,|\theta|^2,
\qquad c_H:=\frac{\kappa_G}{3},
\]
and explicitly interprets this as a **mass term** arising purely from geometry:
the Haar measure is not flat in exponential coordinates, and the Jacobian suppresses large excursions in \(\mathfrak g\). 【158:4†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L183-L207】

---

# 4. Why this matters for Yang--Mills: lifting flat directions

The project's Yang--Mills application decomposes directions into:

- **horizontal (physical)** directions (orthogonal to gauge orbits), and
- **vertical (gauge)** directions.

A crucial difficulty is that, at the trivial configuration, the Wilson action's Hessian typically has large null spaces tied to gauge symmetry. The extracted idea is:

> The Haar term supplies a strictly positive quadratic contribution in exponential coordinates that can help lift otherwise-flat modes, while the Wilson term supplies convexity in physical/horizontal directions.

The project makes this explicit in the combined small-field Hessian statement:
the Wilson Hessian contributes on horizontals, and the Haar Hessian contributes in gauge directions, yielding positivity on the combined physical+gauge decomposition (modulo chosen gauge-fixing conventions). 【158:4†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L183-L214】【158:5†PART_II_SECTION_5_Haar_Measure_and_Haar_Mass(1).md†L218-L236】

---

# 5. Theory hook: a geometric mass-gap mechanism (working hypothesis)

**Working hypothesis (not proved in the project):**
If one can propagate a local Bakry--Émery curvature lower bound (in the small-field region) to a global Poincaré inequality for the finite-volume lattice Yang--Mills measure, then one obtains a **volume-uniform spectral gap** for the associated diffusion generator on gauge-invariant observables.

The Haar mass mechanism is potentially novel in this program because it:

1. anchors the curvature lower bound in *intrinsic* group geometry (via \(\kappa_G\)),
2. provides an explicit and uniform quadratic contribution **independent of lattice volume**, and
3. interacts naturally with Bakry--Émery / \(\Gamma\)-calculus methods.

The next extracted documents show how this feeds into the local horizontal curvature bound and the functional-inequality pipeline.
