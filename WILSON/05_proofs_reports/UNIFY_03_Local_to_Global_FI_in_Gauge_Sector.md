# UNIFY 03 — Local-to-Global Functional Inequalities in the Gauge-Invariant Sector (Lyapunov + Local Curvature)

## Purpose of this extract

A local \(CD(\rho_{\mathrm{loc}},\infty)\) statement on a small-field region is powerful, but not enough by itself: the Gibbs measure still has support on *all* of \(M_\Lambda\).

This note extracts the **analytic upgrade mechanism** used throughout the project:

> Local curvature + a Lyapunov drift condition + a local functional inequality  
> \(\Longrightarrow\) global Poincaré / global log-Sobolev.

Crucially, the method is robust under restricting the carré du champ to a **subbundle** \(\mathcal H\subset TM\). In lattice gauge theory, the relevant choice is \(\mathcal H=H\), the horizontal (physical) bundle.

---

## 1. Setting: a Gibbs diffusion and its carré du champ

Let \((M,g)\) be a smooth finite-dimensional Riemannian manifold and let
\[
d\mu = Z^{-1} e^{-S}\,d\mathrm{vol}_g,
\qquad S\in C^2(M).
\]
Consider the symmetric diffusion generator
\[
Lf = \Delta_g f - \langle \nabla S,\nabla f\rangle.
\]

The carré du champ and its iteration are
\[
\Gamma(f,g) = \langle \nabla f,\nabla g\rangle,
\qquad
\Gamma_2(f)=\frac12\big(L\Gamma(f)-2\Gamma(f,Lf)\big).
\]

### Horizontal / subbundle variant

Given a subbundle \(\mathcal H\subset TM\), define the restricted carré du champ
\[
\Gamma^{\mathcal H}(f) := |\nabla^{\mathcal H} f|^2.
\]
All the local-to-global arguments remain valid when:

- the curvature bound is assumed only along \(\mathcal H\),
- the Lyapunov drift is verified with \(\Gamma^\mathcal H\),
- we restrict to functions whose gradients lie in \(\mathcal H\).

In gauge theory: \(\mathcal H=H\) and gauge-invariant observables satisfy \(\nabla f\in H\).

---

## 2. The local inputs

### 2.1 Local curvature–dimension on a region \(\Omega\)

Assume there exist an open \(\Omega\subset M\) and \(\rho_{\mathrm{loc}}>0\) such that
\[
\Gamma_2(f)(x)\ge \rho_{\mathrm{loc}}\,\Gamma(f)(x)
\quad \forall x\in \Omega,\ \forall f\in C^\infty(M).
\]
(Or replace \(\Gamma\) by \(\Gamma^{\mathcal H}\) if working in a subbundle framework.)

This implies local gradient bounds and, on bounded subsets of \(\Omega\), local Poincaré and local LSI with constants controlled by \(\rho_{\mathrm{loc}}\) and the geometry of the set.

### 2.2 A Lyapunov drift condition

A Lyapunov function is a \(C^2\) function \(W\ge 1\) such that
\[
LW \le -\alpha W + \beta\,\mathbf 1_K
\]
for some \(\alpha>0\), \(\beta\ge 0\), and compact \(K\subset \Omega\).

Intuition: outside \(K\) the diffusion drifts back toward \(\Omega\), preventing “escape” into bad regions.

### 2.3 A local functional inequality near \(K\)

Assume \(K\subset U\subset \Omega\) with \(U\) bounded and a local Poincaré (or local LSI) holds on \(U\). This can often be obtained from the local \(CD(\rho_{\mathrm{loc}},\infty)\) condition plus boundedness of \(U\), but it is convenient to keep it explicit.

---

## 3. Output I: global Poincaré via Lyapunov + local Poincaré

A key technical step is a Lyapunov–\(\Gamma\) estimate, controlling \(\int f^2W\,d\mu\) by the Dirichlet form plus a local term.

> **Lyapunov–\(\Gamma\) estimate (prototype form).**  
> If \(LW \le -\alpha W + \beta \mathbf 1_K\), then there exist \(C_1,C_2\) such that
> \[
> \int f^2 W\,d\mu
> \le C_1 \int \Gamma(f)\,d\mu + C_2\int_K f^2\,d\mu.
> \]

Combining this with a local Poincaré inequality on \(U\supset K\), one obtains:

> **Local-to-Global Poincaré (template).**  
> Local \(CD(\rho_{\mathrm{loc}},\infty)\) on a large-measure region in \(\Omega\), plus a Lyapunov drift toward a compact \(K\subset\Omega\), plus a local Poincaré on \(U\supset K\), implies a global Poincaré inequality
> \[
> \mathrm{Var}_\mu(f) \le C_P\int \Gamma(f)\,d\mu.
> \]
> (And similarly with \(\Gamma^\mathcal H\) in the subbundle setting.)

Thus the generator \(-L\) has a positive spectral gap \(\lambda_1\ge 1/C_P\).

---

## 4. Output II: global LSI via Lyapunov + local LSI

With the same local curvature and Lyapunov framework, replacing the local Poincaré input by a local log-Sobolev inequality yields a global LSI:

> **Local-to-Global LSI (template).**  
> Local \(CD(\rho_{\mathrm{loc}},\infty)\) on \(\Omega\), a Lyapunov drift toward \(K\subset\Omega\), and a local LSI on \(U\supset K\) imply a global LSI
> \[
> \mathrm{Ent}_\mu(f^2) \le C_{\mathrm{LS}} \int \Gamma(f)\,d\mu.
> \]
> Again, the statement persists under restriction to a subbundle \(\mathcal H\).

Global LSI implies global Poincaré, hypercontractivity, and strong concentration inequalities—analytic “rigidity” that is particularly valuable when attempting uniform-in-volume estimates.

---

## 5. Specialization to lattice Yang–Mills: what is gained, what is still missing

For finite lattice Yang–Mills at fixed spacing:

- Part II provides a **uniform local horizontal curvature** bound on a small-field ball
  \(\Omega=B_r(U^{(0)})\) (horizontal \(CD(\rho_{\mathrm{loc}},\infty)\) for gauge invariants).
- The local-to-global machine above then reduces the global problem to two concrete analytic tasks:

1. **Construct a Lyapunov function \(W_\Lambda\)** measuring “distance from the vacuum” (e.g. built from plaquette energy) with a drift inequality
   \[
   L_\Lambda W_\Lambda \le -\alpha W_\Lambda + \beta\mathbf 1_{K_\Lambda}
   \]
   with \(\alpha,\beta\) uniform in \(\Lambda\).

2. **Verify a local FI** (Poincaré/LSI) on a bounded small-field region \(U\subset\Omega\), again uniformly in \(\Lambda\).

If these are achieved, one obtains **volume-uniform global Poincaré/LSI for gauge-invariant observables**, hence a uniform spectral gap for the configuration-space generator \(-L_\Lambda^{\mathrm{inv}}\).

---

## 6. Why this extract is “promising”

This analytic pattern is not new in probability theory, but the project’s potentially fertile contribution is to **align it with gauge geometry**:

- the “good region” \(\Omega\) is where horizontal Bakry–Émery curvature is provably positive;
- the Lyapunov drift is the mechanism for bringing typical configurations back toward \(\Omega\);
- the restriction to horizontals is what makes the inequalities relevant to gauge-invariant physics.

If one can make the Lyapunov part *uniform in \(\Lambda\)*, the resulting functional inequalities are **dimension-free** (do not degrade as the lattice grows), which is exactly the kind of structural stability a mass-gap program wants as input.

