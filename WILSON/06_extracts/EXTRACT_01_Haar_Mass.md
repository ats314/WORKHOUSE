---
title: "Haar Mass: How Riemannian (Haar) Volume Generates a Quadratic Term in Exponential Coordinates"
date: "2025-12-29"
---

# Haar Mass: how Riemannian volume becomes an effective quadratic potential

## Abstract

For a compact Lie group $G$ with a bi-invariant metric, the Haar measure is the Riemannian volume.
In geodesic normal coordinates near the identity, the volume density has the universal expansion
\[
\sqrt{\det g_{ij}(\theta)} \;=\; 1 - \frac16\,\mathrm{Ric}_{ij}(e)\,\theta^i\theta^j + O(|\theta|^3).
\]
Taking a negative logarithm converts the volume density into an **effective quadratic potential**
\[
S_H(\theta) := -\log\sqrt{\det g_{ij}(\theta)} \;=\; \frac16\,\mathrm{Ric}_{ij}(e)\,\theta^i\theta^j + O(|\theta|^3),
\]
whose Hessian at the identity is
\[
\nabla^2 S_H(0) \;=\; \frac13\,\mathrm{Ric}_G(e).
\]
Because $\mathrm{Ric}_G\ge \kappa_G g_G$ for compact semisimple $G$ (with $\kappa_G>0$ after normalization),
this quadratic term is **uniformly positive**. In the Bakry--Émery framework, it supplies a
dimension-free baseline curvature contribution (and hence a baseline spectral-gap mechanism)
for lattice gauge theories formulated on $M_\Lambda = G^{E(\Lambda)}$.

This note isolates the derivation, states it in a form convenient for curvature–dimension estimates,
and explains why it is natural to interpret this as a geometric “mass” term.

---

## 1. Normal-coordinate expansion of Riemannian volume

Let $(M,g)$ be a smooth Riemannian manifold and $x_0\in M$.
Let $\theta$ be geodesic normal coordinates centered at $x_0$, so that $\theta(x_0)=0$ and
\[
g_{ij}(0)=\delta_{ij},\qquad \partial_k g_{ij}(0)=0.
\]
A standard Riemannian geometry result gives the volume density expansion
\[
\sqrt{\det g_{ij}(\theta)}
= 1 - \frac{1}{6}\,\mathrm{Ric}_{ij}(x_0)\,\theta^i\theta^j + O(|\theta|^3).
\tag{1.1}
\]

### 1.1. Converting volume density into an effective potential

Define the *volume potential*
\[
S_H(\theta) := -\log\sqrt{\det g_{ij}(\theta)}.
\tag{1.2}
\]
Using $\log(1-a)= -a + O(a^2)$ and (1.1) with $a=\frac16\mathrm{Ric}_{ij}\theta^i\theta^j+O(|\theta|^3)$,
we obtain the universal quadratic expansion
\[
S_H(\theta)
= \frac{1}{6}\,\mathrm{Ric}_{ij}(x_0)\,\theta^i\theta^j + O(|\theta|^3).
\tag{1.3}
\]
Therefore, as a bilinear form on $T_{x_0}M$,
\[
\nabla^2 S_H(0) \;=\; \frac13\,\mathrm{Ric}_g(x_0).
\tag{1.4}
\]

---

## 2. Specialization to compact Lie groups: the “Haar mass”

Let $G$ be a compact Lie group with a bi-invariant metric $g_G$, and let $e$ be the identity.
Then Haar measure coincides with the Riemannian volume $d\mathrm{vol}_{g_G}$, and (1.4) gives:

**Proposition 2.1 (Hessian of the Haar volume potential).**  
In exponential coordinates $\theta\mapsto \exp_G(\theta)$ around $e$,
the negative log-density of Haar measure satisfies
\[
\nabla^2 S_H(0) \;=\; \frac13\,\mathrm{Ric}_G(e).
\tag{2.1}
\]

If $G$ is compact semisimple (e.g. $SU(N)$) and $g_G$ is normalized appropriately, then
\[
\mathrm{Ric}_G \;\ge\; \kappa_G\, g_G
\quad\text{for some }\kappa_G>0,
\tag{2.2}
\]
hence
\[
\nabla^2 S_H(0)\;\ge\; \frac{\kappa_G}{3}\,g_G.
\tag{2.3}
\]

### 2.1. Why call this a “mass” term?

If one rewrites the Haar measure in exponential coordinates as
\[
d\mathrm{vol}_{g_G}(\exp_G(\theta))
= e^{-S_H(\theta)}\,d\theta,
\]
then (1.3) says that, near $\theta=0$,
\[
d\mathrm{vol}_{g_G}(\exp_G(\theta))
\approx \exp\!\left(-\frac16\,\mathrm{Ric}_{ij}(e)\theta^i\theta^j\right)\,d\theta.
\]
This is precisely a Gaussian suppression of large $\theta$ with a positive quadratic form;
in field-theory language, a positive quadratic form is the local signature of a “mass term”.
The key feature is that it comes from **geometry alone**, before any action is introduced.

---

## 3. Lattice configuration manifold: product Haar geometry

Let $\Lambda$ be a finite lattice and $E(\Lambda)$ its set of oriented edges.
The configuration manifold is the finite product
\[
M_\Lambda = G^{E(\Lambda)}
\]
with product metric $g_\Lambda$ and product Haar volume.

Two facts matter for uniform estimates:

1. The Ricci tensor of a product is the sum of the Ricci tensors on the factors.
2. Each factor is the same compact group $(G,g_G)$.

Hence $\mathrm{Ric}_{g_\Lambda}$ is uniformly bounded below, independently of the number of factors:
\[
\mathrm{Ric}_{g_\Lambda} \;\ge\; \kappa_G\,g_\Lambda,
\tag{3.1}
\]
with the **same** $\kappa_G$ as in (2.2).

In other words, the Riemannian (Haar) geometry contributes a baseline positive curvature on the
full finite-volume configuration space, with a constant that does **not** degrade with volume.

---

## 4. Why this matters for Bakry--Émery curvature

For a Gibbs measure of the form
\[
d\mu_\Lambda \;=\; Z_\Lambda^{-1}\,e^{-S_\Lambda}\,d\mathrm{vol}_{g_\Lambda},
\]
the Bakry--Émery Ricci tensor is
\[
\mathrm{Ric}_{\mu_\Lambda}
\;=\; \mathrm{Ric}_{g_\Lambda} \;+\; \nabla^2 S_\Lambda.
\tag{4.1}
\]

Equation (3.1) says that even if $\nabla^2 S_\Lambda$ is only semibounded below by
\[
\nabla^2 S_\Lambda \ge -C\,g_\Lambda,
\]
one still gets a positive curvature lower bound as soon as $C<\kappa_G$:
\[
\mathrm{Ric}_{\mu_\Lambda} \ge (\kappa_G-C)\,g_\Lambda.
\]
This is the analytic heart of the “Haar mass” idea: the geometry supplies a volume-independent
curvature floor, and the interaction terms only need to avoid destroying it.
