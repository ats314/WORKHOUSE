---
title: "Curvature → Functional Inequality → Gap: Salvage-Core for Lattice YM–Style Programs"
author: "Project extraction (compiled)"
date: "2025-12-29"
---

## 0. Why this document exists

This note distills the “salvage-core” chain of rigorous implications that appears repeatedly across the project:

\[
\text{(uniform convexity / curvature)} \Rightarrow \text{(LSI)} \Rightarrow \text{(Poincaré)} \Rightarrow \text{(spectral gap)} \Rightarrow \text{(exponential clustering)}.
\]

The *programmatic* novelty (relative to standard textbook facts) is how the project tries to **manufacture a robust convex/curvature regime for lattice Yang–Mills at finite cutoff** using:

1. a **Haar-measure induced quadratic term** in exponential coordinates (a “geometric mass”),
2. a **convex-core radius** where the Wilson part can’t overwhelm that mass,
3. and a **static/dynamic mechanism** (Outlier Exclusion + Riccati/Hessian-flow) to keep typical configurations inside that core.

---

## 1. Functional inequality skeleton (reversible Markov generator)

Let \((X,\mathcal{B},\mu)\) be a probability space and let \(L\) be a self-adjoint, conservative Markov generator on \(L^2(\mu)\) with semigroup \(P_t=e^{tL}\).
The Dirichlet form is
\[
\mathcal{E}(f,f) := -\langle f,Lf\rangle_{L^2(\mu)}.
\]

### 1.1 Poincaré inequality \(\Leftrightarrow\) spectral gap

A Poincaré inequality
\[
\operatorname{Var}_\mu(f)\le \frac{1}{\lambda}\,\mathcal{E}(f,f)
\]
is equivalent to the statement that the nonzero spectrum of \(-L\) lies in \([\lambda,\infty)\), and to exponential \(L^2\)-decay of \(P_t\) on mean-zero functions.

### 1.2 Bakry–Émery curvature gives LSI and Poincaré

For diffusion-type generators of the form
\[
Lf = \Delta f - \nabla S\cdot \nabla f,
\]
Bakry–Émery theory relates lower bounds on \(\nabla^2 S\) (or more generally a \(\Gamma_2\ge \rho\,\Gamma\) condition) to functional inequalities. The scalar prototype in the project shows this cleanly.

---

## 2. Scalar “calibration layer”: uniform convexity gives a uniform gap

On a finite lattice \(\Lambda_L\subset \mathbb{Z}^4\), consider a scalar action
\[
S_\Lambda(\phi)
= \sum_{x\in\Lambda_L}\Big(\frac{m_0^2}{2}\phi_x^2+\frac{\lambda}{4}\phi_x^4\Big)
+\frac{\kappa}{2}\sum_{\langle x,y\rangle}(\phi_x-\phi_y)^2,
\qquad \lambda>0,\;\kappa\ge 0.
\]

If
\[
m_0^2 - 2d\kappa \ge \rho_*>0,\qquad (d=4),
\]
then
\[
\nabla^2 S_\Lambda(\phi)\succeq \rho_* I
\]
uniformly in \(\phi\) and in the volume. This implies (via Bakry–Émery) an LSI and a Poincaré inequality with constants of order \(\rho_*\), hence a **uniform spectral gap** for the finite-volume Langevin generator. 

This is not “new physics” — it’s the calibration that tells us *exactly what kind of convexity we must force in YM if we want the same inequality machine*.

---

## 3. Lattice Yang–Mills: Haar measure induces a quadratic “mass” term

### 3.1 Exponential coordinates and Jacobian

On a lattice, configurations are \(U=(U_b)_{b\in\mathcal{B}}\in SU(N)^{\mathcal{B}}\).
Near the identity, write on each link \(b\)
\[
U_b = \exp(iagA_b),\qquad A_b\in \mathfrak{su}(N).
\]

Under this change of variables, the Haar measure contributes a Jacobian density
\[
d\mu_{\mathrm{Haar}}(U_b)= J(A_b)\,dA_b,\qquad
J(A) = \det_{\mathfrak{g}}\!\left(\frac{\sinh(\operatorname{ad}_A/2)}{\operatorname{ad}_A/2}\right),
\]
so the induced “measure action” is
\[
S_{\mathrm{Haar}}(A):= -\log J(A).
\]

### 3.2 Quadratic expansion: positive Hessian at the origin

Using \(\sinh(x/2)/(x/2)=1+x^2/24+O(x^4)\), one finds
\[
S_{\mathrm{Haar}}(A)= c_0\,\|A\|^2 + O(\|A\|^4),
\qquad c_0>0 \;\text{(group-dependent)}.
\]

Operational meaning: **even before the Wilson action does anything**, the *measure* is already penalizing \(A\)-amplitudes quadratically. This is the project’s “free” UV curvature source.

---

## 4. From “mass term exists” to “gap mechanism”: convex core + locality

The project’s lattice YM strategy (finite cutoff) is:

1. Combine the Haar quadratic term with an upper bound on the Wilson Hessian to define a **convexity radius** \(R_{\mathrm{conv}}(\beta)\) such that
   \[
   \|A\|_\infty \le R_{\mathrm{conv}}(\beta)\quad \Rightarrow\quad \nabla^2 S(A)\succeq m_\beta^2 I.
   \]
2. Prove *typical configurations* remain in (or are driven into) this convex core:
   - **static:** Outlier Exclusion (a tail bound) for the event \(\|A\|_\infty>R_{\mathrm{conv}}\),
   - **dynamic:** Hessian-flow / Riccati inequalities that prevent persistent negative curvature.
3. Inside the core, use Bakry–Émery to get a uniform Poincaré (or LSI) constant for the *local sector*.
4. Combine with locality to turn that into **exponential clustering** of local observables, hence (after OS reconstruction) a candidate physical mass scale.

---

## 5. What’s actually “new” here?

None of the individual ingredients is exotic in isolation. The potentially novel thing is the *composition*:

- Haar measure gives a **unavoidable** local quadratic term.
- Convexity is treated as a **regional** property (convex core) rather than global.
- The program introduces a measurable, \(\beta\)-dependent “bad set” \(\mathcal{B}_\beta\) (outside the core) and tries to control it via:
  - static dominance/tails,
  - plus a dynamical restoration mechanism.

That’s a very “probability + geometry” way of thinking about the YM mass gap at finite cutoff.
