---
title: "Horizontal Bakry–Émery Curvature for Gauge-Invariant Sectors"
subtitle: "An analytic interface between gauge symmetry and Γ₂ calculus"
author: "Extracted and restructured from the project draft"
date: "2025-12-28"
---

## 0. Why this module is interesting

A recurring obstruction in gauge theories is that the **physical configuration space** is not the naïve manifold of fields: it is a *quotient* by gauge transformations. Quotients are often singular (strata, orbifold points, non-free actions), and “doing analysis on the quotient” quickly becomes a swamp.

This module isolates a clean workaround:

- Do **analysis on the unreduced manifold** \(M\),
- but restrict to **gauge-invariant observables** \(f\),
- and observe that for such \(f\), the gradient \(\nabla f\) is automatically **horizontal** (orthogonal to gauge orbits).
- Therefore, **only the Bakry–Émery curvature in horizontal directions matters** for the \(\Gamma_2\)-method.

This is conceptually close to:
- analysis on Riemannian submersions and quotients,
- sub-Riemannian / hypoelliptic curvature-dimension ideas,
- and the modern theory of synthetic curvature lower bounds on metric-measure quotients (e.g. \(RCD\) spaces),
but it stays finite-dimensional and concrete.

---

## 1. Geometric and probabilistic setup

Let \((M,g)\) be a smooth, connected, finite-dimensional Riemannian manifold and let
\[
d\mu = Z^{-1} e^{-S}\, d\mathrm{vol}_g,
\qquad S\in C^2(M),\quad 0<Z<\infty,
\]
be a Gibbs measure.

Define the diffusion generator
\[
L f := \Delta_g f - \langle \nabla S,\nabla f\rangle_g,
\]
and the carré du champ operator
\[
\Gamma(f,g) := \tfrac12\big(L(fg)-fLg-gLf\big)=\langle \nabla f,\nabla g\rangle_g,
\qquad \Gamma(f):=\Gamma(f,f)=|\nabla f|_g^2.
\]
The iterated carré du champ is
\[
\Gamma_2(f)
:=\tfrac12\big(L\Gamma(f)-2\Gamma(f,Lf)\big).
\]

### 1.1 Gauge symmetry

Assume a Lie group \(\mathcal G\) acts smoothly on \(M\) by **isometries** and preserves \(S\):
\[
S(g\cdot x)=S(x)\quad \forall g\in\mathcal G,\ x\in M.
\]
Then \(\mu\) is \(\mathcal G\)-invariant.

For each \(x\in M\), the **orbit**
\[
\mathcal O_x:=\{g\cdot x: g\in\mathcal G\}
\]
has tangent space
\[
V_x:=T_x\mathcal O_x \subset T_x M,
\]
the **vertical** subspace.

On the regular set where the orbit dimension is locally constant, define the **horizontal** subspace
\[
H_x:=V_x^\perp \subset T_x M,
\qquad T_x M = H_x \oplus V_x.
\]

### 1.2 Gauge-invariant observables have horizontal gradients

Let
\[
\mathcal A^{\mathrm{inv}} := \{f\in C^\infty(M): f(g\cdot x)=f(x)\ \forall g\in\mathcal G,\ x\in M\}.
\]

**Proposition 1 (Horizontal gradient of invariants).**  
If \(f\in \mathcal A^{\mathrm{inv}}\), then for every \(x\in M\) in the regular set,
\[
\nabla f(x)\in H_x.
\]

*Proof.*  
Fix \(x\) and a vertical vector \(v\in V_x\). Then there exists \(X\in\mathrm{Lie}(\mathcal G)\) such that \(v=X^\sharp(x)\), where \(X^\sharp\) is the fundamental vector field of the action. Since \(f\) is invariant,
\[
0=\frac{d}{dt}\Big|_{t=0} f(\exp(tX)\cdot x)=df_x(X^\sharp(x))=df_x(v).
\]
So \(df_x\) annihilates \(V_x\), hence \(\nabla f(x)\perp V_x\). ∎

This is the key “physics → geometry” bridge: gauge invariance forces the gradient into physical directions.

---

## 2. Bakry–Émery curvature and the horizontal restriction

Define the Bakry–Émery Ricci tensor (finite-dimensional setting)
\[
\mathrm{Ric}_\mu := \mathrm{Ric}_g + \nabla^2 S.
\]

The Bochner–Bakry–Émery identity gives, for smooth \(f\),
\[
\Gamma_2(f)=\|\nabla^2 f\|_{\mathrm{HS}}^2 + \mathrm{Ric}_\mu(\nabla f,\nabla f).
\]
In particular,
\[
\Gamma_2(f)\ge \mathrm{Ric}_\mu(\nabla f,\nabla f).
\]

### 2.1 Horizontal curvature lower bound

**Definition 2 (Horizontal Bakry–Émery lower bound).**  
We say \((M,g,\mu,\mathcal G)\) satisfies a horizontal curvature bound with constant \(\rho>0\) on a set \(\Omega\subset M\) if
\[
\mathrm{Ric}_\mu(x)(v,v)\ge \rho\,|v|_g^2
\qquad \forall x\in \Omega,\ \forall v\in H_x.
\]
We denote this informally by
\[
\mathrm{Ric}_\mu|_{H}\ge \rho\, g|_{H}\quad \text{on }\Omega.
\]

### 2.2 Horizontal curvature ⇒ CD(\(\rho,\infty\)) on invariants

**Theorem 3 (Horizontal curvature implies \(CD(\rho,\infty)\) on invariants).**  
Assume \(\mathrm{Ric}_\mu|_{H}\ge \rho\, g|_H\) on \(\Omega\subset M\). Then for all gauge-invariant \(f\in \mathcal A^{\mathrm{inv}}\),
\[
\Gamma_2(f)(x)\ge \rho\,\Gamma(f)(x)\qquad \forall x\in \Omega.
\]

*Proof.*  
For invariant \(f\), Proposition 1 gives \(\nabla f(x)\in H_x\). Therefore on \(\Omega\),
\[
\Gamma_2(f)(x)\ge \mathrm{Ric}_\mu(\nabla f,\nabla f)(x)\ge \rho\,|\nabla f(x)|_g^2=\rho\,\Gamma(f)(x).
\]
∎

So the full \(CD(\rho,\infty)\) inequality is inherited by the invariant sector *even if the curvature bound fails in vertical directions*.

---

## 3. Functional inequalities in the gauge-invariant sector

If \(\Omega=M\) and the horizontal bound holds globally, the standard Bakry–Émery semigroup argument yields:

- Poincaré inequality
  \[
  \mathrm{Var}_\mu(f)\le \frac1\rho \int_M |\nabla f|_g^2\,d\mu,
  \qquad \forall f\in \mathcal A^{\mathrm{inv}},
  \]
- Log-Sobolev inequality
  \[
  \mathrm{Ent}_\mu(f^2)\le \frac2\rho \int_M |\nabla f|_g^2\,d\mu,
  \qquad \forall f\in \mathcal A^{\mathrm{inv}}.
  \]

If the bound holds only on a **small-field region** \(\Omega\), then it produces **local** Poincaré/LSI on bounded \(U\Subset \Omega\), which can be upgraded to global inequalities via Lyapunov drift criteria (see the project’s Part III).

---

## 4. Conceptual connections and “potentially new” angles

### 4.1 Quotients without quotients

The quotient \(M/\mathcal G\) can be singular. The approach here avoids constructing it:
\[
\text{do analysis on } M \text{ but test only on } \mathcal A^{\mathrm{inv}}.
\]
This is morally “analysis on the quotient” without the quotient.

A natural next step is to formalize this as:
- an analysis on a stratified space,
- or a synthetic curvature-dimension statement for the metric-measure quotient (when defined).

### 4.2 Relation to sub-Riemannian curvature-dimension

In sub-Riemannian geometry, one studies diffusions whose carré du champ sees only a subbundle \(\mathcal H\subset TM\). Here the diffusion is elliptic on \(M\), but the **observables** are constrained so that \(\nabla f\in H\). Analytically, this is remarkably similar.

This suggests importing:
- generalized curvature-dimension inequalities for distributions,
- tools for singular bundles and bracket-generating hypotheses,
into gauge-invariant \(\Gamma_2\) calculus.

### 4.3 Toward infinite-dimensional gauge fields

Nothing in this module is infinite-dimensional. But it is exactly the sort of finite-volume statement one might hope to stabilize under:
- volume limits \(|\Lambda|\to\infty\),
- lattice spacing limits \(a\to 0\),
- and perhaps renormalization.

If a *uniform* horizontal curvature mechanism survives these limits, it becomes a candidate analytic backbone for a mass-gap program.

---

## 5. What further work would strengthen this module

1. **Singular orbits and stratification.**  
   Extend the “horizontal calculus” through non-regular strata, possibly using:
   - stratified differential geometry,
   - mollification and approximation on invariant functions,
   - or a maximum principle adapted to stratifications.

2. **Quantitative stability under local perturbations.**  
   Make precise “how much negative Hessian in \(S\)” is tolerable before horizontal curvature is lost.

3. **Uniformity in families.**  
   For a family \((M_\Lambda,g_\Lambda,\mu_\Lambda)\), identify conditions ensuring \(\rho\) is independent of \(\Lambda\). This is crucial for any mass-gap interpretation.

