---
title: "Hessian Flow, Riccati Inequalities, and (Conditional) Curvature Restoration"
author: "Project extraction (compiled)"
date: "2025-12-29"
---

## 0. What we’re trying to bottle

The project repeatedly uses a matrix-valued “reaction–diffusion” heuristic:

- the effective action \(S_t\) changes with a smoothing / RG-like parameter \(t\),
- the Hessian \(H_t=\nabla^2 S_t\) evolves by a PDE with a quadratic term in \(H_t\),
- and the smallest eigenvalue \(\lambda_{\min}(H_t)\) obeys a **Riccati-type inequality**.

Once you have a Riccati inequality of the form
\[
\dot\lambda \;\ge\; -\alpha \lambda^2 + \beta,
\qquad \alpha>0,\ \beta>0,
\]
you immediately get a *stable positive equilibrium*
\[
\lambda_*=\sqrt{\beta/\alpha},
\]
and hence a mechanism that prevents “persistent flat directions.”

---

## 1. Viscous Hamilton–Jacobi (vHJ) flow: definition

A clean finite-dimensional model is:

\[
S_t(x) := -\log\Big(P_t(e^{-S_0})(x)\Big),
\]
where \(P_t\) is the heat semigroup on \(\mathbb{R}^d\). Then \(S_t\) solves
\[
\partial_t S_t = \Delta S_t - \|\nabla S_t\|^2,
\]
up to an additive function of \(t\).

Define the Hessian field \(H_t(x)=\nabla^2 S_t(x)\).

---

## 2. Hessian evolution: the quadratic term

Differentiating twice yields a schematic matrix equation
\[
\partial_t H_t
= \Delta H_t - 2\,\mathrm{Sym}\big(\nabla^3 S_t[\nabla S_t,\cdot]\big)\; -\; 2(H_t)^2.
\]

### Sign sanity check

The term \(-(H_t)^2\) is negative semidefinite as a matrix.
By itself it does **not** push eigenvalues upward: it tends to decrease them.
So **restoration** (i.e. preventing \(\lambda_{\min}\) from collapsing) must come from *other positive contributions*:

- a “mass term” already present in \(S_t\) (e.g. Haar-induced quadratic term),
- curvature terms if the flow lives on a compact manifold (configuration space) rather than \(\mathbb{R}^d\),
- or additional source terms from integrating out modes (RG / anomaly source).

This is exactly why the project’s Appendix-D style inequality includes a \(+\beta\) source.

---

## 3. Riccati comparison principle (the part you can actually use)

Suppose you can dominate the evolution of the smallest eigenvalue by
\[
\frac{d}{dt}\lambda(t) \ge -\alpha \lambda(t)^2 + \beta,
\qquad \alpha>0,\ \beta\ge 0.
\]

Then:

- If \(\beta=0\), negative \(\lambda\) cannot be forced to increase without extra structure.
- If \(\beta>0\), solutions of the equality converge to \(\lambda_*=\sqrt{\beta/\alpha}\), and any supersolution is bounded below by the comparison solution.

In the lattice YM reading, \(\beta\) is the “mass-like” source term — the Haar quadratic contribution is the prime candidate.

---

## 4. Appendix-D style inequality (with a mass-like source)

The project’s “salvage” Appendix D phrases the general inequality as:

\[
\partial_t \lambda_{\min}(t,x)
\ \gtrsim\ 
-2\,\lambda_{\min}(t,x)^2 \;+\; c_0 \;-\; C,
\]
where \(c_0>0\) comes from a strictly convex mass term and \(C\) is an error budget from the diffusion/transport remainder.

This is the exact Riccati template above with \(\alpha=2\) and \(\beta=c_0-C\).

**Key conditional:** you need \(c_0>C\) uniformly in the region you care about.

---

## 5. Why this matters for Yang–Mills (the program link)

At finite cutoff, in exponential coordinates:

- the Haar measure supplies a **local quadratic term** \(c_0\|A\|^2\),
- you define a convex core where the Wilson Hessian cannot overwhelm it,
- and you try to show the flow spends enough time in that region.

Couple this with Outlier Exclusion (static tail control) and you have a plausible route to proving that typical configurations satisfy a Bakry–Émery curvature lower bound on long times.

Once that holds, standard functional inequalities can deliver a uniform spectral gap (in a suitable “local sector”).

---

## 6. Next-level technical work (the real dragons)

1. **Fix the sign conventions and geometry** for the actual configuration manifold \(\mathcal{C}_\Lambda = SU(N)^{|\mathcal{B}|}\) (with gauge quotient subtleties).
2. **Prove** that the remainder term \(C\) is uniformly controlled in \(\beta\) and volume *inside the convex core*.
3. **Show scaling compatibility** as \(a\to 0\): \(R_{\mathrm{conv}}(\beta(a))\) shrinks, so the restoration/outlier mechanism must beat that shrinkage.

If those three are solved, the Riccati mechanism becomes a serious structural ingredient, not a slogan.

