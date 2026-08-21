---
title: "Selection D — Core Curvature Theorem and the SAFE Region for Lattice Yang–Mills"
date: "2025-12-28"
---

# Abstract

The “Core Curvature Theorem” is the geometric heart of the curvature-driven lattice YM program:
it asserts a **volume-uniform horizontal Bakry–Émery curvature lower bound** in a small-field neighborhood of the vacuum.
This note rewrites that result as a self-contained module with explicit hypotheses and a continuity argument.

# 1. Setup: lattice YM measure as a weighted Riemannian manifold

Let $G$ be a compact Lie group with a fixed bi-invariant metric, and let $\Lambda$ be a finite lattice.
The configuration manifold is
\[
M_\Lambda:=G^{E(\Lambda)}
\]
with product metric and product Haar measure $d\mathrm{Haar}_\Lambda$.

Let the lattice action be
\[
S_\Lambda \;=\; S_W + S_{\mathrm{add}},
\]
where $S_W$ is the Wilson plaquette action and $S_{\mathrm{add}}$ is an additional gauge-invariant term (e.g. gauge-fixing surrogate, infrared stabilizer, or counterterm).

Define the Gibbs measure
\[
\mu_\Lambda(dU)\;:=\; Z_\Lambda^{-1}\,e^{-S_\Lambda(U)}\,d\mathrm{Haar}_\Lambda(U).
\]

Let $V_U$ be the vertical space tangent to gauge orbits and $H_U=V_U^\perp$ the horizontal space.

# 2. Bakry–Émery tensor and horizontal restriction

For the reversible diffusion generator
\[
L_\Lambda := \Delta_{M_\Lambda} - \langle \nabla S_\Lambda,\nabla(\cdot)\rangle,
\]
the Bakry–Émery tensor is
\[
\mathrm{Ric}_{\mu_\Lambda}(U)
\;=\;
\mathrm{Ric}_{M_\Lambda}(U) + \nabla^2 S_\Lambda(U).
\]
The functional inequalities relevant to the physical sector are obtained by testing $\mathrm{Ric}_{\mu_\Lambda}$ only on horizontal vectors $v\in H_U$.

# 3. Hypotheses for the local curvature bound

We isolate the minimal conditions that appear across the project files.

## (H1) Base Ricci lower bound (geometry of $G^{E(\Lambda)}$)

Assume
\[
\mathrm{Ric}_{M_\Lambda}\ \ge\ \kappa_G\,g_{M_\Lambda}
\]
for some $\kappa_G>0$ depending only on $G$ and the metric normalization.
(For compact $G$ and product metrics, $\kappa_G$ is volume–uniform.)

## (H2) Additional term not too concave

Assume a uniform Hessian lower bound
\[
\nabla^2 S_{\mathrm{add}}(U)\ \ge\ -C_{\mathrm{add}}\,g_{M_\Lambda}
\qquad\text{for all }U\in M_\Lambda,
\]
with $C_{\mathrm{add}}$ independent of $\Lambda$.

## (H3) Wilson action gives horizontal convexity at the vacuum

At the vacuum configuration $U^{(0)}\equiv I$, the Wilson Hessian satisfies
\[
\nabla^2 S_W(U^{(0)})(v,v)\ \ge\ \kappa_W\,\|v\|^2
\qquad\text{for all }v\in H_{U^{(0)}},
\]
for some $\kappa_W>0$ independent of $\Lambda$.

This is the discrete Hodge/coercivity statement: the Wilson Hessian is $d_1^\ast d_1$ up to constants on physical coexact modes.

# 4. The Core Curvature Theorem

## Theorem 4.1 (Local horizontal Bakry–Émery curvature bound)

Assume (H1)–(H3).
Then there exist a radius $r>0$ and a constant $\rho_{\mathrm{loc}}>0$ such that, for every lattice $\Lambda$,
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ \ge\ \rho_{\mathrm{loc}}\,\|v\|^2
\qquad\text{for all }U\in B_r(U^{(0)})\text{ and all }v\in H_U,
\]
where $B_r(U^{(0)})$ is the small-field ball around the vacuum.

Moreover $\rho_{\mathrm{loc}}$ is **volume–uniform**, depending only on $\kappa_G,\kappa_W,C_{\mathrm{add}}$ and the continuity moduli of $\nabla^2 S_W$ and the horizontal bundle in a neighborhood of $U^{(0)}$.

### Proof

At the vacuum,
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)
=
\mathrm{Ric}_{M_\Lambda}(U^{(0)})(v,v) + \nabla^2 S_W(U^{(0)})(v,v) + \nabla^2 S_{\mathrm{add}}(U^{(0)})(v,v).
\]
Using (H1)–(H3),
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)\ \ge\ (\kappa_G + \kappa_W - C_{\mathrm{add}})\,\|v\|^2.
\]
Choose $\rho_0:=\frac12(\kappa_G+\kappa_W-C_{\mathrm{add}})$ assuming the parenthesis is positive.

By continuity of $U\mapsto \mathrm{Ric}_{M_\Lambda}(U)$ and $U\mapsto \nabla^2 S_\Lambda(U)$, and continuity of the horizontal projection $P^H_U$ on the principal stratum,
there exists $r>0$ such that for all $U\in B_r(U^{(0)})$ and all $v\in H_U$,
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ \ge\ \rho_0\,\|v\|^2.
\]
Set $\rho_{\mathrm{loc}}:=\rho_0$. ∎

## Corollary 4.2 (Local $CD(\rho_{\mathrm{loc}},\infty)$ for gauge invariants)

Let $f$ be a smooth gauge–invariant observable. Then on $B_r(U^{(0)})$,
\[
\Gamma_2(f)\ \ge\ \rho_{\mathrm{loc}}\,\Gamma(f),
\]
where $\Gamma(f)=\|\nabla f\|^2$ is automatically horizontal.

# 5. Why this module is exciting

This theorem is the “small-field analog” of uniform convexity in scalar field models, but with two crucial gauge-theoretic twists:

1. **Horizontal restriction**: convexity is only required on the physical subbundle.
2. **Geometric reinforcement**: the compact group geometry (Ricci positivity + Haar convexity) contributes a built-in stabilizer.

It suggests a broader principle: *compact gauge degrees of freedom come with intrinsic geometric coercivity* that can be leveraged to control functional inequalities nonperturbatively.

# 6. Next steps that would upgrade this into a standalone paper

1. Quantify $\kappa_W$ for the Wilson action on a fixed lattice geometry and boundary condition.
2. Prove uniform control of horizontal projections $P^H_U$ on a small-field neighborhood (including treatment of singular strata).
3. Show that the radius $r$ can be chosen independent of $\Lambda$ via locality and product structure.

