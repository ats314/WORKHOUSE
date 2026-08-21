---
title: "Polarity of Reducible Strata (Capacity-Zero Singular Set): Why Gauge-Quotient Singularities Don’t Bite"
author: "Project extraction (compiled)"
date: "2025-12-29"
---

## 0. What “polarity” buys you

In this project, several key arguments (maximum principles for eigenvalue PDEs, functional inequalities on the quotient, etc.) want to work on the *regular stratum* of the gauge quotient. The obvious worry is:

> “But the quotient has singular strata (reducible connections). Do those wreck analysis?”

The polarity result says: **no**, at least at finite cutoff, and plausibly in a Gaussian reference setting in the continuum-inspired limit.

A polar set is “invisible” to the diffusion/Dirichlet-form analysis: it has **capacity zero** and is almost surely avoided by the associated stochastic process.

---

## 1. Capacity and polar sets (Dirichlet form viewpoint)

Given a quasi-regular Dirichlet form \((\mathcal{E},\mathcal{D}(\mathcal{E}))\) on \((\mathcal{X},\mu)\), the capacity of a set \(E\subset\mathcal{X}\) is defined by
\[
\mathrm{Cap}(E)
= \inf\Big\{
  \mathcal{E}(u,u) + \int u^2\,d\mu\;:\;
  u\in\mathcal{D}(\mathcal{E}),\ u\ge 1\ \text{near }E
\Big\}.
\]
A set is **polar** if \(\mathrm{Cap}(E)=0\). For the associated Markov process \(X_t\), polar sets are almost surely never hit.

---

## 2. Finite-dimensional intuition: codimension matters

For Brownian motion in \(\mathbb{R}^n\), the hitting probability of a linear subspace depends on the codimension \(m\):

- \(m=1,2\): the subspace is typically hit with positive probability.
- \(m\ge 3\): the subspace is polar (capacity zero).

This “codimension ≥ 3” threshold is the correct rule of thumb to remember in finite dimensions.

---

## 3. Lattice YM: reducibles form a positive-codimension algebraic variety

At finite cutoff, the configuration space is a compact manifold:
\[
\mathcal{C}_\Lambda = SU(N)^{|B(\Lambda)|}.
\]

The set \(\Sigma_\Lambda\) of reducible configurations is an algebraic subset; in concrete finite-dimensional models it has codimension that grows with lattice size (so it is “thin” in a strong sense).

One then combines:

1. diffusion potential theory on compact manifolds (polar sets include high-codimension submanifolds),
2. countable subadditivity of capacity (since \(\Sigma_\Lambda\) decomposes into a countable union of submanifolds),
3. and a capacity comparison under bounded change of measure.

Since the lattice YM Gibbs measure is absolutely continuous w.r.t. product Haar with bounded density on finite volume, capacity-zero transfers.

Conclusion: **at finite cutoff**,
\[
\mathrm{Cap}_{\mu_{\Lambda,\mathrm{YM}}}(\Sigma_\Lambda)=0.
\]

---

## 4. Continuum-inspired version: Gaussian reference OU measure

On an infinite-dimensional Hilbert space \(H\) with a centered nondegenerate Gaussian \(\gamma\), the OU Dirichlet form is
\[
\mathcal{E}_0(F,F) = \int_H \|\nabla F(x)\|_H^2\,d\gamma(x).
\]

The reducible set decomposes into a countable union of constraint sets \(\Sigma_\xi\) defined by \(D_A\xi=0\).
The project’s key functional-analytic input is that each constraint map has **infinite rank**, so \(\Sigma_\xi\) sits inside an affine infinite-codimension subset — polar for the Gaussian reference form — and hence \(\Sigma\) is polar by subadditivity.

Transferring polarity from \(\gamma\) to the true YM measure requires a controlled change-of-measure condition (Kato/Novikov-type), which is explicitly flagged as the hard analytic step.

---

## 5. Why polarity is a structural enabler in this project

- It justifies applying **maximum principles** “as if” there were no boundary/singularity at reducible strata.
- It allows functional inequalities proved on the regular stratum to extend to the full space modulo capacity-zero modifications.
- It “de-singularizes” the gauge quotient for stochastic quantization arguments: the Langevin process almost surely lives on the regular stratum.

This is one of the most valuable *rigorous* components because it protects the analytic machinery from a geometric landmine.

