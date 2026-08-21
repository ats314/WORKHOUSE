---
title: "Selection B — Haar Potential and Local Convexity on Compact Lie Groups"
date: "2025-12-28"
---

# Abstract

In compact lattice gauge theories the base Riemannian volume/Haar measure is not an inert background object: written in exponential coordinates it contributes an *intrinsic convex potential* (the negative log Jacobian of the exponential map). Near the identity, the Hessian of this Haar potential is proportional to the Ricci tensor.
This note records the expansion and its consequences for volume–uniform curvature bounds on $G^{E(\Lambda)}$.

# 1. Haar density in exponential coordinates

Let $G$ be a compact Lie group equipped with a bi-invariant Riemannian metric induced by an $\mathrm{Ad}$-invariant inner product
$\langle\cdot,\cdot\rangle$ on $\mathfrak g$.

Let $\exp:\mathfrak g\to G$ be the exponential map.
In normal coordinates $g=\exp(X)$ near the identity, the Riemannian volume is
\[
d\mathrm{vol}_G(g) = J_G(X)\,dX,
\]
where $dX$ denotes Lebesgue measure in $\mathfrak g$ under the chosen inner product.

A convenient closed form for $J_G$ is
\[
J_G(X) \;=\; \det\nolimits_{\mathfrak g}\!\left(\frac{\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X/2}\right),
\]
equivalently a product over roots in a Cartan subalgebra description.

Define the **Haar potential**
\[
S_{\mathrm H}(X) := -\log J_G(X).
\]

# 2. Second-order expansion and curvature

## Proposition 2.1 (Quadratic expansion of the Haar potential)

As $X\to 0$ one has
\[
S_{\mathrm H}(X)
=
\frac16\,\mathrm{Ric}_G(X,X)\ +\ O(\|X\|^3),
\]
so in particular
\[
\nabla^2 S_{\mathrm H}(0) \;=\; \frac13\,\mathrm{Ric}_G,
\]
as quadratic forms on $\mathfrak g$.

### Proof sketch

In geodesic normal coordinates, the Riemannian volume form has the classical expansion
\[
J_G(X)=1-\frac16\,\mathrm{Ric}_G(X,X)+O(\|X\|^3).
\]
Taking $-\log$ yields the claimed expansion and Hessian. ∎

## Corollary 2.2 (Local convexity from positive Ricci)

Assume $\mathrm{Ric}_G \ge \kappa_G\,g_G$ for some $\kappa_G>0$ (true for a compact simple group under standard normalization).
Then
\[
\nabla^2 S_{\mathrm H}(0) \;\ge\; \frac{\kappa_G}{3}\,I.
\]
By continuity, there exists $r_{\mathrm H}>0$ and $c_{\mathrm H}>0$ such that for all $\|X\|\le r_{\mathrm H}$,
\[
\nabla^2 S_{\mathrm H}(X)\ \ge\ c_{\mathrm H}\,I.
\]

# 3. Product groups and volume–uniform constants

For a finite lattice $\Lambda$ with edge set $E(\Lambda)$, the configuration manifold is
\[
M_\Lambda=G^{E(\Lambda)}.
\]
In exponential coordinates on each edge $U_e=\exp(X_e)$,
the product Haar measure reads
\[
d\mathrm{Haar}_\Lambda(U)
=
\prod_{e\in E(\Lambda)} J_G(X_e)\,dX_e.
\]
Thus the **total Haar potential** is additive:
\[
S_{\mathrm{Haar},\Lambda}(U)=\sum_{e\in E(\Lambda)} S_{\mathrm H}(X_e).
\]

## Proposition 3.1 (Block-diagonal Haar Hessian)

The Hessian of $S_{\mathrm{Haar},\Lambda}$ is block diagonal across edges, hence the lower bound
\[
\nabla^2 S_{\mathrm{Haar},\Lambda}(U)\ \ge\ c_{\mathrm H}\,I
\quad\text{on the set }\{U:\ \|X_e\|\le r_{\mathrm H}\ \forall e\}
\]
holds with the **same constant $c_{\mathrm H}$**, independent of $|E(\Lambda)|$.

### Proof

A direct sum of convex functions is convex with the same modulus, and block diagonality preserves the pointwise lower bound. ∎

# 4. Why this matters for lattice Yang–Mills

In the Gibbs density
\[
\mu_\Lambda(dU) \propto e^{-S_\Lambda(U)}\,d\mathrm{Haar}_\Lambda(U),
\]
the Haar contribution is part of the *reference measure* rather than the action.
But analytically, it behaves like an extra potential with a curvature-driven positive Hessian near the vacuum.
In the Bakry–Émery tensor
\[
\mathrm{Ric}_{\mu_\Lambda} = \mathrm{Ric}_{M_\Lambda} + \nabla^2 S_\Lambda,
\]
one may equivalently view the drift as coming from an effective total potential $S_\Lambda + S_{\mathrm{Haar},\Lambda}$ in Euclidean coordinates.

This “geometric mass term” is a robust mechanism:
- it is gauge invariant,
- it is volume–uniform on product groups,
- it dovetails with Wilson’s plaquette potential to produce a positive horizontal curvature in small-field regimes.

# 5. Forward directions (speculative but actionable)

A clean way to mechanize this in the full YM program is:

1. **Quantify the convexity radius $r_{\mathrm H}$** for a given $G$ (e.g. $SU(N)$) under the metric normalization used in the Wilson action.
2. **Stability under coarse graining**: check whether the Haar convexity survives block-spin maps or gradient flow (a promising route to volume-uniform Lyapunov drift).
3. **Nonperturbative comparison**: treat the Haar potential as the anchor potential in a Holley–Stroock perturbation from the interacting Wilson action.

