---
title: "EXTRACT 03 — Stratified Parabolic Comparison via Polarity (and the Riccati Mass-Gap Driver)"
date: "2025-12-29"
format: "markdown+latex"
source_files:
  - "P20_stratified_parabolic_principle.md"
  - "P18_gaussian_polarity.md"
  - "P01_lattice_polarity.md"
---

# Parabolic comparison on stratified spaces: when singular strata are polar

This extract isolates a mechanism that is potentially reusable far beyond Yang–Mills:

> If the singular set of a stratified space has **capacity zero** (is *polar*) for the relevant Dirichlet form, then parabolic comparison principles can be run on the regular stratum as if the singular set were not there.

## 1. Stratified setup

Let \(\mathcal M\) be a stratified space with regular stratum \(\mathcal M_{\mathrm{reg}}\) and singular set \(\Sigma=\mathcal M\setminus\mathcal M_{\mathrm{reg}}\).

Let \(L\) be a diffusion generator on \(\mathcal M_{\mathrm{reg}}\) with symmetric Dirichlet form \((\mathcal E,\mathcal D(\mathcal E))\) on \(L^2(\mu)\) for a probability measure \(\mu\).

### Polarity (capacity zero)

For a Borel set \(E\subset \mathcal M\), define the \(W^{1,2}\)-capacity (relative to \((\mathcal E,\mu)\)) schematically by
\[
\mathrm{Cap}_\mu(E)
=
\inf\Big\{\mathcal E(u,u)+\|u\|_{L^2(\mu)}^2:\ u\in\mathcal D(\mathcal E),\ u\ge 1\ \text{near }E\Big\}.
\]

We say \(E\) is **polar** if \(\mathrm{Cap}_\mu(E)=0\).  
A standard consequence: the diffusion associated to \(L\) starting in \(\mathcal M_{\mathrm{reg}}\) hits \(E\) with probability \(0\).

> Technical note (important): for the classical Dirichlet form of Brownian motion in \(\mathbb R^n\), codimension \(\ge 2\) (or more generally Hausdorff dimension below the \(n-2\) threshold) is the usual route to capacity zero. Codimension \(1\) sets are typically *not* polar.  
> In the lattice YM setting, the configuration-space dimension is enormous and the reducible locus is claimed to have very large codimension, so the intended regime is consistent with “codimension \(\gg 2\)” polarity heuristics. The exact threshold should be checked against the specific Dirichlet form.

## 2. A stratified parabolic comparison principle

Let \(u:[0,T]\times \mathcal M_{\mathrm{reg}}\to\mathbb R\) satisfy, in a suitable weak sense,
\[
\partial_t u \;\ge\; Lu + F(u),
\]
where \(F:\mathbb R\to\mathbb R\) is nondecreasing (comparison-friendly).

### Theorem (stratified parabolic maximum principle, polar singular set)
Assume:

1. **Polarity:** \(\mathrm{Cap}_\mu(\Sigma)=0\).
2. **Initial nonnegativity:** \(u(0,x)\ge 0\) for all \(x\in\mathcal M_{\mathrm{reg}}\).
3. **Regularity:** \(u\) is regular enough on \(\mathcal M_{\mathrm{reg}}\) for standard parabolic arguments (or Feynman–Kac) to apply locally.

Then
\[
u(t,x)\ge 0\quad\text{for all }t\in[0,T],\ x\in\mathcal M_{\mathrm{reg}}.
\]

### Proof idea (mechanism-level)
- By polarity, diffusion paths \(X_t\) driven by \(L\) starting in \(\mathcal M_{\mathrm{reg}}\) almost surely never hit \(\Sigma\) at finite times.
- Along such paths, one may apply the usual smooth-manifold parabolic maximum principle (or a Feynman–Kac representation) *without* boundary terms from \(\Sigma\).
- Monotonicity of \(F\) gives comparison, so initial nonnegativity propagates.

This is the mechanism claimed in the project’s stratified parabolic principle.

## 3. Application template: a Riccati driver for curvature positivity

Suppose one has a scalar quantity \(\lambda(t,x)\) (e.g. the smallest eigenvalue of a horizontal Bakry–Émery curvature tensor) satisfying a semilinear inequality
\[
\partial_t \lambda \;\ge\; L\lambda \;-\; 2\lambda^2 \;+\; \sigma_*,
\]
with \(\sigma_*>0\) a uniform source term.

Assume the singular set \(\Sigma\) (e.g. reducibles) is polar for \((\mathcal E,\mu)\).  
Then comparison against the ODE
\[
\dot\ell(t) = -2\ell(t)^2 + \sigma_*,\qquad \ell(0)=\inf_x \lambda(0,x),
\]
yields the pointwise lower bound
\[
\lambda(t,x)\;\ge\;\ell(t)\qquad (t>0,\ x\in\mathcal M_{\mathrm{reg}}).
\]

The Riccati ODE has a stable fixed point
\[
\ell_* = \sqrt{\frac{\sigma_*}{2}},
\]
so any mechanism producing the inequality above forces \(\lambda\) to become uniformly positive at late times (a “mass-gap scale” in the project’s language).

## 4. Where polarity enters Yang–Mills

The project proposes two supporting polarity claims:

- **Lattice polarity of reducibles:** reducible configurations form a high-codimension algebraic subset of \(G^{E(\Lambda)}\), and such sets are argued to be polar for the lattice Dirichlet form.  
- **Gaussian polarity in the continuum:** under Gaussian reference measures (abstract Wiener space), infinite-codimension linear subspaces are polar for Ornstein–Uhlenbeck-type Dirichlet forms, suggesting reducibles should be polar in the continuum limit as well.

In both cases, polarity is not just measure-zero; it is the stronger statement needed to justify a maximum-principle argument on the regular stratum without boundary conditions on \(\Sigma\).
