---
title: "Selection E — Local-to-Global Functional Inequalities via Lyapunov Drift"
date: "2025-12-28"
---

# Abstract

A recurring obstruction in geometric approaches to lattice gauge theory is that curvature bounds are typically **local** (valid in a small-field regime), while mass gap and concentration require **global** inequalities with constants uniform in volume. The project files contain a robust analytic bridge: combine *local* curvature/LSI (or local Poincaré) with a *global Lyapunov drift* that pulls trajectories back into the good region.

This note isolates the core statement as a reusable lemma factory.

# 1. Reversible diffusions and Dirichlet forms

Let $(M,g)$ be a smooth compact manifold and let
\[
\mu(d x) = Z^{-1} e^{-S(x)}\,d\mathrm{vol}(x)
\]
be a smooth probability measure. Consider the reversible generator
\[
L := \Delta - \langle \nabla S, \nabla(\cdot)\rangle,
\]
symmetric in $L^2(\mu)$.

Define the Dirichlet form
\[
\mathcal E(f,f) := \int \|\nabla f\|^2\,d\mu.
\]

# 2. Local functional inequalities on a “SAFE” region

Fix a region $\Omega\subset M$ (“SAFE core”, e.g. a small-field ball).
Assume that on $\Omega$ one has a local Poincaré inequality:
\[
\mathrm{Var}_{\mu(\cdot\mid \Omega)}(f)
\ \le\
C_{\mathrm{PI}}^{\Omega}\int_{\Omega}\|\nabla f\|^2\,d\mu(\cdot\mid\Omega),
\]
or a local log–Sobolev inequality:
\[
\mathrm{Ent}_{\mu(\cdot\mid \Omega)}(f^2)
\ \le\
C_{\mathrm{LSI}}^{\Omega}\int_{\Omega}\|\nabla f\|^2\,d\mu(\cdot\mid\Omega).
\]

In the Bakry–Émery program, these local inequalities are typically obtained from a local curvature bound
\[
\mathrm{Ric}_\mu \ge \rho_{\mathrm{loc}}\,g\quad\text{on }\Omega.
\]

# 3. Lyapunov drift: controlling the complement of the SAFE core

A Lyapunov function is a nonnegative function $W:M\to[1,\infty)$ such that
\[
L W \ \le\ -\alpha\,W\ +\ \beta\,\mathbf 1_{\Omega},
\tag{Lyap}
\]
for constants $\alpha>0$, $\beta\ge0$.

Intuition: outside $\Omega$ the process experiences a deterministic drift forcing it back toward $\Omega$.
This provides tail control and prevents “escape to bad curvature regions” from dominating the spectral behavior.

# 4. Global Poincaré from local curvature + Lyapunov drift

## Theorem 4.1 (Local PI + Lyapunov drift $\Rightarrow$ global PI)

Assume:

1. A local Poincaré inequality holds on $\Omega$ with constant $C_{\mathrm{PI}}^{\Omega}$.
2. A Lyapunov drift condition (Lyap) holds for some $W$ with constants $\alpha,\beta$.

Then $\mu$ satisfies a global Poincaré inequality
\[
\mathrm{Var}_\mu(f)
\ \le\
C_{\mathrm{PI}}\int \|\nabla f\|^2\,d\mu,
\]
with an explicit $C_{\mathrm{PI}}$ depending only on $C_{\mathrm{PI}}^{\Omega}$ and $(\alpha,\beta)$.

### Proof idea

Decompose $f$ into its fluctuations on $\Omega$ and on $M\setminus\Omega$.
Use (Lyap) to control the $L^2$ mass of $f$ outside $\Omega$ by the Dirichlet form (a weighted Poincaré inequality),
then patch with the local inequality on $\Omega$. ∎

# 5. Global LSI from local LSI + Lyapunov drift

## Theorem 5.1 (Local LSI + Lyapunov drift $\Rightarrow$ global LSI)

Assume:

1. A local (possibly defective) log–Sobolev inequality holds on $\Omega$.
2. A Lyapunov drift (Lyap) holds.

Then $\mu$ satisfies a global log–Sobolev inequality
\[
\mathrm{Ent}_\mu(f^2)
\ \le\
C_{\mathrm{LSI}}\int \|\nabla f\|^2\,d\mu
\]
with constant $C_{\mathrm{LSI}}$ controlled explicitly by the local constants and the drift parameters.

### Proof idea

Apply the standard defective-LSI-to-LSI upgrade using Lyapunov control of tails (a Herbst-type argument + localization). ∎

# 6. Specialization to lattice Yang–Mills

On $M_\Lambda=G^{E(\Lambda)}$ with Gibbs measure $\mu_\Lambda$:

- The SAFE region $\Omega_\Lambda$ is the small-field neighborhood where horizontal curvature is uniformly positive.
- The **local** inequalities come from the core curvature theorem.
- The missing piece is to build a **volume-uniform** Lyapunov function.

A natural candidate is a “field energy” measuring distance from the vacuum, such as
\[
W(U)=1+\sum_{p\in P(\Lambda)} \mathrm{dist}_G(U_p,I)^2
\quad\text{or}\quad
W(U)=\exp\Big(\eta\sum_{p} \mathrm{dist}_G(U_p,I)^2\Big),
\]
chosen so that $LW$ produces a strict negative drift outside $\Omega_\Lambda$ by convexity of the Wilson action.

# 7. Why this module has theory-building potential

This Lyapunov patching method is not tied to YM; it is a general “local geometry $\Rightarrow$ global concentration” principle for interacting compact systems.

It hints at a future “curvature-stable RG” strategy:

- show local curvature on a mesoscopic SAFE core,
- use Lyapunov drift to prevent escape,
- iterate under coarse graining while keeping constants uniform.

That is structurally similar to the renormalization group, but with *functional inequalities* as monotone control parameters.

