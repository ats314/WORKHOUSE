---
title: "Local-to-Global Poincaré and Log-Sobolev Engines via Lyapunov Drift (Extracted)"
author: "Project extraction (Parts 12–15, 14)"
date: "2025-12-28"
---

## Scope and status

This note extracts the **analytic engine** used to turn

- local curvature control on a “SAFE” region, plus
- a Foster–Lyapunov drift inequality controlling excursions,

into **global**, volume-uniform Poincaré and log-Sobolev inequalities.

The underlying analytic technology exists in the functional-inequality literature;
the project’s contribution is to package it into a lattice-gauge-ready module
with a clean constants ledger and a “two hypotheses to prove” interface
(YM-Local-FI and YM-Lyapunov).

---

## 1. Abstract diffusion framework (finite dimension)

Let $(M,g)$ be a smooth connected finite-dimensional Riemannian manifold,
let $S\in C^2(M)$, and let
\[
d\mu = Z^{-1} e^{-S}\, d\mathrm{vol}_g,\qquad 0<Z<\infty.
\]
Define the symmetric diffusion generator
\[
Lf=\Delta_g f-\langle\nabla S,\nabla f\rangle
\]
and the carré du champ $\Gamma(f)=|\nabla f|^2$.

The Bakry–Émery tensor is
\[
\mathrm{Ric}_\mu := \mathrm{Ric}_g + \nabla^2 S.
\]

---

## 2. The three ingredients (SAFE + local FI + Lyapunov drift)

### Ingredient A: local curvature on a SAFE region

Let $\Omega\subset M$ be a nonempty open set.
Assume a local curvature–dimension condition on $\Omega$:
\[
\Gamma_2(f)(x)\ \ge\ \rho_{\mathrm{loc}}\,\Gamma(f)(x),
\qquad \forall x\in\Omega,
\]
equivalently $\mathrm{Ric}_\mu\ge \rho_{\mathrm{loc}}\,g$ on $\Omega$.

### Ingredient B: local functional inequalities on a bounded core

Let $U\Subset\Omega$ be a bounded open set with $\mu(U)>0$.
Assume a local Poincaré inequality on $U$:
\[
\int_U (f-f_U)^2\,d\mu \ \le\ C_{\mathrm{P,loc}} \int_U \Gamma(f)\,d\mu.
\]
For log-Sobolev, assume a local LSI (or local super-Poincaré / local defective LSI)
on $U$ with constant $C_{\mathrm{LS,loc}}$.

### Ingredient C: Lyapunov drift

Assume there exists a Lyapunov function $W\ge 1$, constants $\alpha>0$, $\beta\ge 0$,
and a compact set $K\subset U$ such that
\[
LW \ \le\ -\alpha W + \beta\,\mathbf 1_K.
\]

---

## 3. Output: global Poincaré (spectral gap)

### Theorem 3.1 (Local-to-global Poincaré via Lyapunov drift)

Under Ingredients A–C, the measure $\mu$ satisfies a global Poincaré inequality:
\[
\mathrm{Var}_\mu(f) \ \le\ C_P \int_M \Gamma(f)\,d\mu,
\]
with an explicit constant $C_P$ depending only on
\[
\rho_{\mathrm{loc}},\ C_{\mathrm{P,loc}},\ \alpha,\ \beta,\ \mu(U),\ \mu(K),
\]
and a patching constant tied to cutoff functions supported in $U$.

Equivalently, the generator $L$ has a spectral gap $\lambda_1\ge 1/C_P$.

---

## 4. Output: global log-Sobolev (hypercontractivity)

### Theorem 4.1 (Local-to-global log-Sobolev via Lyapunov drift)

Assume Ingredients A and C, and assume also a local LSI input on $U$ (Ingredient B for entropy).
Then $\mu$ satisfies a global LSI:
\[
\mathrm{Ent}_\mu(f^2) \ \le\ C_{\mathrm{LS}} \int_M \Gamma(f)\,d\mu.
\]

A standard intermediate step is a **defective LSI**:
\[
\mathrm{Ent}_\mu(f^2) \ \le\ C' \int \Gamma(f)\,d\mu \;+\; D\int_K f^2\,d\mu,
\]
and then a “defective LSI + Poincaré $\Rightarrow$ true LSI” upgrade (Rothaus-type lemma)
removes the defect at the cost of enlarging the constant.

---

## 5. Specialization: finite-volume lattice Yang–Mills

For lattice YM at fixed cutoff:

- $M=M_\Lambda=G^{E(\Lambda)}$ with product metric;
- $\mu=\mu_\Lambda$ is the Gibbs measure $e^{-S_\Lambda}d\mathrm{vol}_{g_\Lambda}$;
- by the Core Curvature Theorem, one can take $\Omega_\Lambda = B_r(U^{(0)})$ with
  volume-uniform $\rho_{\mathrm{loc}}>0$.

The engine then reduces the Yang–Mills analytic workload to two explicit, volume-uniform tasks:

### Assumption YM-Local-FI (local FI on bounded small-field sets)

Choose bounded sets $K_\Lambda\subset U_\Lambda\Subset \Omega_\Lambda$ with geometric shape
uniform in $\Lambda$, and prove local Poincaré and local LSI bounds on $U_\Lambda$
for gauge-invariant observables, with constants independent of $\Lambda$.

### Assumption YM-Lyapunov (escape functional)

Construct gauge-invariant Lyapunov functions $W_\Lambda\ge 1$ satisfying
\[
L_\Lambda W_\Lambda \ \le\ -\alpha W_\Lambda + \beta\,\mathbf 1_{K_\Lambda},
\]
with $\alpha,\beta$ independent of $\Lambda$.

---

## 6. Why this module is publishable (even before the final mass-gap bridge)

Even if the “OS vs configuration gap” bridge is not yet solved, this engine produces a clean,
referee-proof statement:

> **If** YM-Local-FI and YM-Lyapunov hold, then the configuration-space Langevin dynamics for
> gauge-invariant observables has a **volume-uniform spectral gap** and a **volume-uniform LSI**.

That is already a strong, nonperturbative control statement about lattice Yang–Mills
in a genuinely geometric language.

