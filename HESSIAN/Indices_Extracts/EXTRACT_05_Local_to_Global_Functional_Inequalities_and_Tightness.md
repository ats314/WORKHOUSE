---
title: "EXTRACT 05 — Local-to-Global Functional Inequalities and Tightness: a Continuum-Limit Template"
date: "2025-12-29"
format: "markdown+latex"
source_files:
  - "PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature(1)(1).md"
  - "PART_III_SECTION_3_Local_to_Global_LSI_via_Lyapunov_and_Curvature.md"
  - "Part_I_Section_3_Lyapunov_UPDATED.md"
  - "P16_measure_tightness.md"
---

# From local curvature to global LSI, and from global LSI to tightness

This extract distills the analytic “plumbing” that connects geometric curvature inputs to global spectral gaps and then to continuum-limit compactness.

The key idea is modular:

1. **Local curvature \(CD(\rho_{\mathrm{loc}},\infty)\)** holds on a core region \(\Omega\) (e.g. small-field neighborhood).
2. A **Lyapunov drift** function \(W\) prevents the diffusion from spending too much time in the complement \(M\setminus\Omega\).
3. Local inequalities on \(\Omega\) are upgraded to **global** Poincaré and LSI.
4. Uniform LSI yields **concentration** and **tightness** for continuum subsequences.

## 1. General setting

Let \((M,g)\) be a smooth finite-dimensional Riemannian manifold and
\[
d\mu(x) = Z^{-1} e^{-S(x)}\, d\mathrm{vol}_g(x)
\]
a Gibbs probability measure with \(S\in C^2(M)\).

Let
\[
Lf = \Delta_g f - \langle\nabla S,\nabla f\rangle
\]
be the symmetric diffusion generator in \(L^2(\mu)\) and
\[
\Gamma(f)=|\nabla f|^2,\qquad
\Gamma_2(f)=\frac12\big(L\Gamma(f)-2\Gamma(f,Lf)\big)
\]
be the Bakry–Émery carré du champ operators.

## 2. Local curvature and local inequalities on bounded sets

Assume there exists an open region \(\Omega\subset M\) and a constant \(\rho_{\mathrm{loc}}>0\) such that
\[
\Gamma_2(f)(x) \ge \rho_{\mathrm{loc}}\,\Gamma(f)(x)
\qquad(\forall x\in\Omega,\ \forall f).
\]
This is a local \(CD(\rho_{\mathrm{loc}},\infty)\) condition.

On relatively compact \(U\Subset\Omega\), standard Bakry–Émery arguments yield **local** functional inequalities:

- Local Poincaré on \(U\): \(\mathrm{Var}_{\mu|_U}(f)\le C_{P,\mathrm{loc}}\int_U \Gamma(f)\,d\mu\).
- Local LSI on \(U\): \(\mathrm{Ent}_{\mu|_U}(f^2)\le C_{LS,\mathrm{loc}}\int_U \Gamma(f)\,d\mu\).

The constants depend on \(\rho_{\mathrm{loc}}\) and the geometry of \(U\), but not on the behavior of \(\mu\) far from \(U\).

## 3. Lyapunov drift condition (tail control)

A Lyapunov function is a smooth \(W:M\to[1,\infty)\) such that for some \(\alpha>0\), \(\beta\ge 0\), and a compact “small set” \(K\subset\Omega\),
\[
LW \le -\alpha W + \beta\,\mathbf 1_K.
\]
Intuitively, \(W\) is large in the tails and the inequality says: outside \(K\), the generator forces \(W\) to decrease on average. This is a rigorous form of “the diffusion is pulled back toward the core.”

## 4. Local-to-global upgrade

A standard conclusion in the literature (and the project’s Part III) is:

> **Template theorem (Lyapunov + local inequalities \(\Rightarrow\) global inequalities).**  
> If:
> 1. \(CD(\rho_{\mathrm{loc}},\infty)\) holds on \(\Omega\),
> 2. a Lyapunov drift inequality holds with \(K\subset\Omega\),
> 3. a local Poincaré (resp. local LSI) holds on some \(U\) with \(K\subset U\Subset\Omega\),
>
> then \(\mu\) satisfies a **global** Poincaré inequality (resp. global LSI), with constants depending on \(\rho_{\mathrm{loc}}\), \((\alpha,\beta)\), and the local constants on \(U\).

In particular, global LSI implies global Poincaré and hence a **spectral gap**:
\[
\lambda_1(-L)\;>\;0.
\]

### Horizontal variant (for gauge invariance)
If \(\Gamma\) is replaced by a horizontal carré du champ \(\Gamma^H(f)=|\nabla^H f|^2\) and one restricts to functions with horizontal gradients (e.g. gauge-invariant observables), the same logic applies: local horizontal curvature + Lyapunov drift + local inequalities \(\Rightarrow\) global inequalities in the physical sector.

This is precisely the interface intended by Part II \(\to\) Part III.

## 5. Uniform LSI \(\Rightarrow\) exponential moments and tightness

Assume now one has a family of measures \(\{\mu_a\}\) (e.g. lattice spacing \(a\to 0\)) satisfying a **uniform** log-Sobolev inequality:
\[
\mathrm{Ent}_{\mu_a}(f^2)\le C_{LS}\int \Gamma(f)\,d\mu_a
\quad\text{with }C_{LS}\text{ independent of }a.
\]

A standard Herbst argument yields Gaussian concentration for Lipschitz functionals and, in many settings, uniform exponential-moment bounds for suitable norms:
\[
\sup_a \int \exp\!\big(c\,\|A\|^2\big)\, d\mu_a(A) <\infty
\]
for some \(c>0).

If the ambient topology is chosen so that norm-balls are precompact (e.g. Sobolev embeddings / Rellich–Kondrachov compactness),
then one gets uniform tail estimates
\[
\mu_a(\|A\|>R) \le C e^{-cR^2},
\]
which implies **tightness**: for every \(\varepsilon>0\), there exists a compact \(K_\varepsilon\) with \(\mu_a(K_\varepsilon)\ge 1-\varepsilon\) for all \(a\).

Tightness plus Prokhorov \(\Rightarrow\) existence of convergent subsequences:
\[
\mu_{a_k}\Rightarrow \mu_{\mathrm{cont}}
\quad (a_k\to 0).
\]

## 6. Why this matters for the larger program

The project’s big logical leap is:

- Part II supplies a **local horizontal curvature bound** (small-field seed).
- Part I/III supply the Lyapunov-based upgrade mechanism to global Poincaré/LSI.
- A **uniform** global LSI across volumes and lattice spacings gives:
  - a uniform spectral gap on the lattice,
  - tightness and continuum subsequences,
  - and a pathway to a continuum theory with controlled functional inequalities.

The still-hard step is constructing Lyapunov functions (and/or proving small-field dominance) with constants uniform in the two limits: volume \(\to\infty\) and \(a\to 0\).
