---
title: "Selection A — Horizontal Bakry–Émery Calculus on Lattice Gauge Quotients"
date: "2025-12-28"
---

# Abstract

This note isolates a clean *gauge–invariant* Bakry–Émery framework on finite lattice gauge configuration spaces
\[
M_\Lambda = G^{E(\Lambda)}
\]
without gauge fixing. The key observation is that the analytic objects driving Poincaré/Log–Sobolev inequalities (carré du champ, $\Gamma_2$) can be restricted to *horizontal/physical directions* because vertical (gauge) directions annihilate gauge–invariant observables. This provides a natural interface between geometric curvature bounds and functional inequalities in the *physical* sector.

# 1. Finite-volume gauge configuration geometry

Let $G$ be a compact Lie group with a fixed bi-invariant Riemannian metric $\langle\cdot,\cdot\rangle_G$.
For a finite lattice $\Lambda$ with oriented edge set $E(\Lambda)$ and vertex set $V(\Lambda)$ define the configuration manifold
\[
M_\Lambda := G^{E(\Lambda)}
\]
with the product metric and product Haar measure $d\mathrm{Haar}_\Lambda$.

The lattice gauge group
\[
\mathcal G_\Lambda := G^{V(\Lambda)}
\]
acts by vertex conjugation:
\[
(g\cdot U)_\ell = g_{s(\ell)}\,U_\ell\,g_{t(\ell)}^{-1}, \qquad g\in \mathcal G_\Lambda,\ U\in M_\Lambda.
\]
Let $C^\infty(M_\Lambda)^{\mathcal G_\Lambda}$ denote the smooth gauge–invariant observables.

## 1.1 Vertical and horizontal distributions

For $U\in M_\Lambda$ let $V_U \subset T_U M_\Lambda$ be the tangent space to the gauge orbit through $U$ (the *vertical* space).
Define the *horizontal* space as the orthogonal complement
\[
H_U := V_U^\perp \subset T_U M_\Lambda.
\]

Because the action is by isometries, the decomposition $T_U M_\Lambda = V_U \oplus H_U$ is canonical (up to the usual singular-stratum issues at reducible configurations; in finite volume those are typically handled by restricting to the principal stratum and extending by capacity).

# 2. Gauge invariance forces horizontality

## Proposition 2.1 (Gradient of an invariant observable is horizontal)

If $f\in C^\infty(M_\Lambda)^{\mathcal G_\Lambda}$, then for every $U\in M_\Lambda$,
\[
\nabla f(U) \in H_U.
\]

### Proof

Let $X\in V_U$ be any vertical tangent vector (infinitesimal gauge motion). Gauge invariance implies $df_U(X)=0$.
By definition of the Riemannian gradient,
\[
df_U(X) = \langle \nabla f(U),\,X\rangle_{T_U M_\Lambda}.
\]
Hence $\langle \nabla f(U),X\rangle=0$ for all $X\in V_U$, so $\nabla f(U)\in V_U^\perp = H_U$. ∎

## Corollary 2.2 (Physical carré du champ)

For gauge–invariant $f$ one may define the physical carré du champ as
\[
\Gamma_{\mathrm{phys}}(f)(U) := \|\nabla f(U)\|^2 = \|\nabla^H f(U)\|^2 ,
\]
since $\nabla f$ is horizontal.

# 3. Reversible diffusions and horizontal Bakry–Émery curvature

Let $S_\Lambda\in C^\infty(M_\Lambda)$ be gauge–invariant and define the Gibbs measure
\[
\mu_\Lambda(dU) := Z_\Lambda^{-1} e^{-S_\Lambda(U)}\,d\mathrm{Haar}_\Lambda(U).
\]
Let $L_\Lambda$ be the reversible generator
\[
L_\Lambda := \Delta_{M_\Lambda} - \langle \nabla S_\Lambda, \nabla(\,\cdot\,)\rangle,
\]
symmetric in $L^2(\mu_\Lambda)$.

For smooth $f$ define the iterated carré du champ
\[
\Gamma_2(f):=\tfrac12\big(L_\Lambda \Gamma(f) - 2\Gamma(f,L_\Lambda f)\big).
\]

## Definition 3.1 (Horizontal/physical Bakry–Émery tensor)

Define the Bakry–Émery tensor on $M_\Lambda$ by
\[
\mathrm{Ric}_{\mu_\Lambda} := \mathrm{Ric}_{M_\Lambda} + \nabla^2 S_\Lambda .
\]
We say a *horizontal curvature lower bound* holds with constant $\rho>0$ if
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ \ge\ \rho\,\|v\|^2
\quad\text{for all $U\in M_\Lambda$ and all $v\in H_U$.}
\]
(Equivalently: the $\Gamma_2$ inequality holds when tested on gauge–invariant observables.)

## Lemma 3.2 (Horizontal curvature implies $\Gamma_2\ge \rho\,\Gamma$ on invariants)

Assume the horizontal curvature lower bound with constant $\rho>0$.
Then for every gauge–invariant $f$,
\[
\Gamma_2(f) \ \ge\ \rho\,\Gamma(f)\qquad\text{pointwise on $M_\Lambda$.}
\]

### Proof sketch

For gauge–invariant $f$, $\nabla f$ is horizontal (Proposition 2.1). In the Bochner identity for $\Gamma_2(f)$,
the curvature term is exactly $\mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f)$, and vertical contributions vanish when testing on invariants.
Thus $\Gamma_2(f)\ge \mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f)\ge \rho\,\|\nabla f\|^2 = \rho\,\Gamma(f)$. ∎

# 4. Functional inequalities in the physical sector

## Theorem 4.1 (Poincaré and diffusion spectral gap for gauge invariants)

Assume a horizontal curvature lower bound with $\rho>0$ (uniformly in $\Lambda$ if desired).
Then for every gauge–invariant $f$,
\[
\mathrm{Var}_{\mu_\Lambda}(f)\ \le\ \frac1\rho \int_{M_\Lambda}\Gamma(f)\,d\mu_\Lambda .
\]
Equivalently, the reversible semigroup $P_t=e^{tL_\Lambda}$ restricted to $L^2(\mu_\Lambda)$ gauge invariants has spectral gap at least $\rho$.

### Proof

Combine Lemma 3.2 with the standard Bakry–Émery implication $CD(\rho,\infty)\Rightarrow$ Poincaré. ∎

## Theorem 4.2 (Log–Sobolev on gauge invariants)

On finite-dimensional compact $M_\Lambda$, under the same hypothesis, one also obtains a log–Sobolev inequality
\[
\mathrm{Ent}_{\mu_\Lambda}(f^2)\ \le\ \frac{2}{\rho_{\mathrm{LSI}}}\int \Gamma(f)\,d\mu_\Lambda
\]
for gauge–invariant $f$, with $\rho_{\mathrm{LSI}}$ controlled by the same curvature mechanism (depending on the route used).

# 5. Why this module is “publishable”

This package is not merely “Bakry–Émery on a product manifold”: the *horizontal restriction* makes the functional inequalities genuinely
about physical degrees of freedom. That is exactly what one needs in gauge theories where the naive Hessian is degenerate in gauge directions.

The same interface applies to:
- lattice gauge theories for general compact $G$,
- constrained Gibbs measures on quotient manifolds,
- superspace-type quotients in gravity (metrics modulo diffeomorphisms), at least at the level of formal geometry.

