---
title: "Finite-Cutoff Outlier Exclusion from Haar-Dominated Tails (Wilson+Haar)"
author: "Project extraction (compiled)"
date: "2025-12-29"
---

## 0. Core claim (the part worth saving)

At fixed lattice spacing (finite cutoff), once you rewrite link variables in exponential coordinates,
the **Haar Jacobian alone** induces a quadratic lower bound that dominates the Wilson part in the tails.

This yields a clean probabilistic statement:

> If you can define a convexity radius \(R_{\mathrm{conv}}(\beta)\) where the full Hessian is positive,
> then the probability that **any** link exits that convex core is at most sub-Gaussian in \(R_{\mathrm{conv}}(\beta)^2\),
> up to a combinatorial factor \(|\mathcal{L}|\) (number of links).

This is the “static half” of keeping the dynamics in the good region.

---

## 1. Setup

Work in exponential coordinates \(U_\ell = \exp(iagA_\ell)\) on each link \(\ell\in\mathcal{L}\).
Write the effective action schematically as
\[
S(A) = S_W(A) + S_H(A),
\]
where \(S_W\) is Wilson (with coefficient \(\beta\) absorbed into notation), and \(S_H\) is the Haar measure action
\[
S_H(A) = -\log J(A).
\]

Let \(\mu_{\beta,\Lambda}\) denote the finite-volume measure on \(A\)-variables:
\[
\mu_{\beta,\Lambda}(dA) \propto e^{-S(A)}\,dA.
\]

---

## 2. Haar-dominated quadratic tail

Assume a tail-dominance bound:
\[
S(A)\ge \alpha \|A\|^2 - C_{\mathrm{tot}},
\]
so
\[
e^{-S(A)} \le e^{C_{\mathrm{tot}}}\, e^{-\alpha\|A\|^2}.
\]

This implies \(\mu_{\beta,\Lambda}\) is dominated by a centered Gaussian measure \(\nu\) with covariance \((2\alpha)^{-1}I\).

---

## 3. Sub-Gaussian tails for linear functionals

Let \(\ell:\mathbb{R}^d\to \mathbb{R}\) be linear with \(\|\ell\|_{\mathrm{op}}=1\).
Under \(\nu\), \(\ell(A)\) is 1D Gaussian so
\[
\nu(|\ell(A)|\ge t)\le 2e^{-\alpha t^2}.
\]
By domination \(\mu\le C_Z \nu\),
\[
\mu_{\beta,\Lambda}(|\ell(A)|\ge t)\le K e^{-\kappa t^2}
\]
for constants \(K,\kappa>0\) depending only on \(\alpha,C_{\mathrm{tot}},d\).

---

## 4. Convexity radius and the “bad set”

Assume you have established a convexity radius \(R_{\mathrm{conv}}(\beta)\) such that

**(CR) Static convexity radius.**  
If \(\|A\|_\infty := \max_{\ell\in\mathcal{L}}\|A_\ell\|\le R_{\mathrm{conv}}(\beta)\), then
\[
\nabla^2 S(A)\succeq m_\beta^2 I
\]
for some \(m_\beta^2>0\).

Define the bad set
\[
\mathcal{B}_\beta := \bigl\{A:\exists \ell\in\mathcal{L}\ \text{s.t.}\ \|A_\ell\|>R_{\mathrm{conv}}(\beta)\bigr\}.
\]

---

## 5. Theorem (finite-cutoff Outlier Exclusion)

**Theorem.** Under (CR) and the Haar-dominated tail assumptions, there exist \(K,\kappa>0\) such that
\[
\mu_{\beta,\Lambda}(\mathcal{B}_\beta)
\le |\mathcal{L}|\, K\, \exp\!\bigl(-\kappa\, R_{\mathrm{conv}}(\beta)^2\bigr).
\]

### Proof sketch (the “three union bounds” maneuver)

Fix a link \(\ell\) and write \(A_\ell\in \mathfrak{su}(3)\cong \mathbb{R}^8\) in an orthonormal basis
\(A_\ell=(a_1,\dots,a_8)\). If \(\|A_\ell\|>R\), then for some coordinate \(|a_i|>R/\sqrt{8}\).
Thus
\[
\mu(\|A_\ell\|>R) \le \sum_{i=1}^8 \mu(|a_i|>R/\sqrt{8})
\le 8K \exp(-\kappa' R^2).
\]
Now union bound over links:
\[
\mu(\mathcal{B}_\beta) \le \sum_{\ell\in\mathcal{L}}\mu(\|A_\ell\|>R_{\mathrm{conv}}(\beta))
\le |\mathcal{L}|\,K \exp\!\bigl(-\kappa R_{\mathrm{conv}}(\beta)^2\bigr).
\]
∎

---

## 6. Interpretation (why this is “useful physics”)

- It is **finite-cutoff** and **finite-dimensional**: no continuum YM measure needed.
- It upgrades the convex-core idea into a probabilistic statement: “nonconvexity is rare,” quantitatively.
- Combined with a dynamic restoration mechanism (Riccati/Hessian flow), it becomes plausible to argue:  
  *typical configurations get into the convex core and mostly stay there*.

The hard next step is to control how \(R_{\mathrm{conv}}(\beta(a))\) behaves under \(a\to 0\).

