---
title: "Core Curvature Theorem for Finite-Volume Lattice Yang–Mills (Extracted)"
author: "Project extraction (Parts 6, 9–11)"
date: "2025-12-28"
---

## Scope and status

This note extracts the **finite-lattice, theorem-level geometric statement** that drives the rest of the program:

> a *volume-uniform* local **horizontal Bakry–Émery curvature lower bound** near the vacuum for lattice Yang–Mills.

Everything here is finite dimensional (fixed lattice spacing, finite volume). No infinite-dimensional Laplacians appear.

---

## 1. Finite-lattice configuration geometry

### Definition 1.1 (Lattice and configuration manifold)

Let $\Lambda$ be a finite periodic box (or any finite graph embedded in $\mathbb{Z}^d$) with vertex set $V(\Lambda)$ and oriented edge set $E(\Lambda)$.
Fix a compact connected Lie group $G$ with a bi-invariant Riemannian metric $g_G$.

Define the finite-dimensional configuration manifold
\[
M_\Lambda := G^{E(\Lambda)},
\]
equipped with the product metric $g_\Lambda := g_G^{\otimes E(\Lambda)}$ and the corresponding Riemannian volume
$d\mathrm{vol}_{g_\Lambda}$ (product Haar/Riemannian volume).

### Definition 1.2 (Gauge group and vertical/horizontal splitting)

Let the lattice gauge group be
\[
\mathcal G_\Lambda := G^{V(\Lambda)},
\]
acting by the usual lattice gauge transformations on links.
At each $U\in M_\Lambda$, the **vertical space** is
\[
V_U := T_U(\mathcal G_\Lambda \cdot U)\subset T_U M_\Lambda,
\]
and we define the **horizontal space** by orthogonality (on the regular set)
\[
H_U := V_U^\perp \subset T_U M_\Lambda.
\]

For any smooth gauge-invariant observable $f\in \mathcal A_\Lambda^{\mathrm{inv}}$, its gradient $\nabla f(U)$ is horizontal:
\[
\nabla f(U)\in H_U.
\]

---

## 2. Gibbs diffusion and Bakry–Émery curvature

### Definition 2.1 (Action, Gibbs measure, generator)

Consider an effective action
\[
S_\Lambda(U) = S_W(U) + S_{\mathrm{add},\Lambda}(U),
\]
where $S_W$ is the Wilson plaquette action and $S_{\mathrm{add},\Lambda}$ is any additional smooth gauge-invariant term.

Define the Gibbs measure on $M_\Lambda$:
\[
d\mu_\Lambda(U) := Z_\Lambda^{-1}\, e^{-S_\Lambda(U)}\, d\mathrm{vol}_{g_\Lambda}(U).
\]

The associated symmetric diffusion generator (Langevin generator) is
\[
L_\Lambda f = \Delta_{g_\Lambda} f - \langle \nabla S_\Lambda, \nabla f\rangle_{g_\Lambda},
\]
with carré du champ $\Gamma_\Lambda(f)=|\nabla f|^2$ and $\Gamma_{2,\Lambda}$ defined by the standard $\Gamma_2$ calculus.

### Definition 2.2 (Bakry–Émery tensor)

The Bakry–Émery tensor is
\[
\mathrm{Ric}_{\mu_\Lambda} := \mathrm{Ric}_{g_\Lambda} + \nabla^2 S_\Lambda.
\]

---

## 3. The extracted theorem

### Assumption 3.1 (Uniform lower bound on the additional terms)

Assume there is a constant $C_{\mathrm{add}}\ge 0$, independent of $\Lambda$, such that
\[
\nabla^2 S_{\mathrm{add},\Lambda}(U)\ \ge\ -C_{\mathrm{add}}\; g_\Lambda(U),
\qquad \forall U\in M_\Lambda.
\]

Assume also that $G$ has a positive Ricci lower bound
\[
\mathrm{Ric}_{G} \ \ge\ \kappa_G\, g_G
\qquad\text{for some }\kappa_G>0,
\]
so that (by the product structure)
\[
\mathrm{Ric}_{g_\Lambda} \ \ge\ \kappa_G\, g_\Lambda
\qquad\text{with the same }\kappa_G.
\]

### Theorem 3.2 (Core curvature theorem; finite-volume, small-field, horizontal)

Let $\rho_0 := \kappa_G - C_{\mathrm{add}}>0$.
Let $U^{(0)}\in M_\Lambda$ be the trivial configuration.

Then there exist constants $r>0$ and $\rho_{\mathrm{loc}}>0$,
depending only on $\kappa_G$, $C_{\mathrm{add}}$, and local lattice geometry (bounded degree),
such that **for every finite lattice $\Lambda$**:

1. (**Uniform local horizontal curvature bound**) For all $U$ in the small-field ball
\[
B_r(U^{(0)}) := \{U\in M_\Lambda : d_{g_\Lambda}(U,U^{(0)})\le r\}
\]
and all horizontal vectors $v\in H_U$,
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ \ge\ \rho_{\mathrm{loc}}\; |v|_{g_\Lambda}^2.
\]

2. (**Local horizontal curvature–dimension condition**) For every smooth gauge-invariant observable
$f\in \mathcal A_\Lambda^{\mathrm{inv}}$ and every $U\in B_r(U^{(0)})$,
\[
\Gamma_{2,\Lambda}(f)(U)\ \ge\ \rho_{\mathrm{loc}}\;\Gamma_\Lambda(f)(U).
\]
Equivalently, the system satisfies a **local** $CD(\rho_{\mathrm{loc}},\infty)$ condition
when tested on gauge-invariant functions.

*Sketch of mechanism.* At $U^{(0)}$, positivity comes from the group Ricci term (Haar geometry)
plus the Hessian structure of the Wilson action on physical modes (Part 9), with the bounded negative
contribution from $S_{\mathrm{add},\Lambda}$.
A continuity argument in $U$ yields the uniform ball $B_r$ and constant $\rho_{\mathrm{loc}}$.

---

## 4. Why this is the “right” local theorem

- It is **intrinsically finite-dimensional**: $(M_\Lambda,g_\Lambda)$ is a compact Riemannian manifold.
- It is **gauge-correct**: it only asserts curvature positivity along horizontal (physical) directions.
- It is **volume-uniform**: $r$ and $\rho_{\mathrm{loc}}$ do not deteriorate as $|\Lambda|\to\infty$.
- It is exactly the kind of hypothesis needed by Lyapunov/patching arguments to build
volume-uniform Poincaré/LSI estimates later.

---

## 5. What is *not* claimed here

This theorem is a **local** statement near $U^{(0)}$.
It does not on its own yield a global mass gap or global functional inequalities;
those require controlling excursions outside the small-field region (Lyapunov drift)
and proving local functional inequalities with uniform constants on bounded subsets.

