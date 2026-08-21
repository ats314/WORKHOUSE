# Curvature-Based Mass-Gap Pipeline for Lattice Yang–Mills (Extracted Core)

## 0. Scope

This document isolates a **single high-leverage architecture** found across the project files:

> **Pipeline:**  
> Haar-geometry produces a **local convexity/curvature floor** (in exponential coordinates),  
> polarity/capacity removes reducible singular strata,  
> a smoothing flow (vHJ/Hessian-flow surrogate) controls curvature evolution via a **matrix Riccati mechanism**,  
> and Bakry–Émery functional inequalities turn curvature into a **spectral gap**, which feeds a standard clustering argument.

Most individual ingredients are standard in isolation; the *assembly* and the specific “Haar-as-curvature-source + Riccati propagation + polarity quarantine” structure is the core extracted idea.

Throughout: **finite volume** (finite lattice). Nothing here is automatically a continuum proof.

---

## 1. Finite-dimensional setting and the analytic target

### 1.1 Configuration space and Gibbs measure

On a finite lattice \(\Lambda\subset\mathbb{Z}^4\), a (compact) gauge group \(G\) and link variables \(U_\ell\in G\) give a finite-dimensional compact manifold
\[
\mathcal{M}_\Lambda \;=\; G^{|\text{links}(\Lambda)|}.
\]
The Wilson action \(S_\beta(U)\) defines the Gibbs measure
\[
d\mu_\beta(U)\;=\;Z_\beta^{-1}\,\exp(-S_\beta(U))\,dU,
\]
where \(dU\) is product Haar.

### 1.2 The “mass gap” proxy at finite volume

A natural analytic proxy for “mass gap” in finite volume is a **spectral gap** of a Markov generator (e.g., Langevin/heat-bath dynamics) reversible w.r.t. \(\mu_\beta\).
If a Poincaré inequality holds:
\[
\mathrm{Var}_{\mu_\beta}(f)\;\le\;\frac{1}{\lambda}\int_{\mathcal{M}_\Lambda}\|\nabla f\|^2\,d\mu_\beta,
\]
then \(\lambda\) is the gap of the generator in \(L^2(\mu_\beta)\) (for the standard diffusion/Langevin choice).

The pipeline focuses on deriving such inequalities from curvature.

---

## 2. Curvature → Functional inequalities → Gap (Bakry–Émery skeleton)

Let \(\mu(dx)\propto e^{-V(x)}dx\) on \(\mathbb{R}^n\), generator
\[
Lf=\Delta f-\nabla V\cdot \nabla f,
\]
and carré du champ \(\Gamma(f)=\|\nabla f\|^2\).
Then the Bakry–Émery identity reads
\[
\Gamma_2(f):=\frac12(L\Gamma(f)-2\Gamma(f,Lf))
= \|\nabla^2 f\|_{HS}^2+\langle(\nabla^2V)\nabla f,\nabla f\rangle.
\]
If \(\nabla^2V\succeq \rho I\), then \(\Gamma_2(f)\ge \rho\,\Gamma(f)\), implying LSI and Poincaré, hence a spectral gap \(\ge \rho\) (up to conventional constants depending on normalization).

**Project leverage point:** instead of trying to prove a global \(\nabla^2V\succeq\rho\) directly for the Wilson action, the files propose a mechanism that:
1) produces a *built-in* local \(\rho_0>0\) from Haar geometry in suitable coordinates,  
2) propagates it under a smoothing flow.

---

## 3. Haar Jacobian as a local curvature/convexity source

### 3.1 Exponential coordinates and Jacobian

For one link, write \(U=\exp(A)\) with \(A\in\mathfrak{g}\) near \(0\).
The pushforward of Haar to \(\mathfrak{g}\) has density
\[
dU \;=\; J(A)\,dA,\qquad 
J(A)=\det\!\left(\frac{\sinh(\mathrm{ad}_A/2)}{\mathrm{ad}_A/2}\right).
\]

Define an “effective potential”
\[
S_{\mathrm{Haar}}(A):=-\log J(A).
\]

### 3.2 Quadratic expansion (“Haar mass term”)

Using \(\log(\sinh x/x)=\tfrac{x^2}{6}+O(x^4)\), one obtains
\[
S_{\mathrm{Haar}}(A)
= c_0\,\|A\|^2 + O(\|A\|^4),
\qquad c_0>0 \text{ depends only on }G,
\]
so locally the Jacobian contributes a *strictly convex* quadratic form.

**Interpretation inside the project:** this is a *geometric* source of curvature in a small-field region in algebra coordinates. It is not a claim about a gauge-invariant “physical mass term”; it is a curvature effect of the group manifold when flattened into \(\mathfrak{g}\).

---

## 4. Polarity / capacity quarantine of reducible strata

The lattice (or continuum) configuration space has singular subsets (reducible strata) where gauge orbits are lower-dimensional; these are the familiar analytic troublemakers.

The extracted mechanism is:

1. Work first with a Gaussian reference measure \(\mu_0\) on a linear model space (e.g. a Hilbert space of connections / modes).
2. Show the reducible set \(\Sigma\) is a countable union of affine subspaces of infinite codimension; such sets have zero Gaussian capacity \(\mathrm{Cap}_{\mu_0}(\Sigma)=0\).
3. Transfer \(\mathrm{Cap}_{\mu_0}(\Sigma)=0\) to the interacting measure \(\mu\) provided \(d\mu/d\mu_0\) is essentially bounded on the region of interest.
4. Conclude \(\Sigma\) is *polar* for the diffusion, so functional inequalities can be checked on the complement with no change.

This is a way to avoid “reducibles kill curvature” objections at the level of Dirichlet-form estimates.

---

## 5. Hessian-flow / vHJ smoothing as an RG surrogate (matrix Riccati mechanism)

### 5.1 vHJ equation for the log density

Let \(P_t\) be the Euclidean heat semigroup on \(\mathbb{R}^n\) and start with
\[
\rho_0(x)=e^{-S_0(x)}.
\]
Define \(\rho_t=P_t\rho_0\) and \(S_t=-\log\rho_t\). Then
\[
\partial_t S_t = \Delta S_t - \|\nabla S_t\|^2 + J_t,\qquad
J_t := \frac{\Delta\rho_t}{\rho_t}-\Delta\log\rho_t
     = \frac{\|\nabla\rho_t\|^2}{\rho_t^2}.
\]
This is a viscous Hamilton–Jacobi equation with a nonnegative source \(J_t\).

### 5.2 Hessian flow equation

Let \(H_t=\nabla^2 S_t\). Differentiating yields
\[
\partial_t H_t
=
\Delta H_t
-2(\nabla S_t\cdot\nabla)H_t
-2H_t^2
+\nabla^2 J_t.
\]
The key nonlinearity \(-2H_t^2\) is Riccati-type and tends to reduce positive eigenvalues over time.

### 5.3 Minimal-eigenvalue Riccati inequality (conditional form)

Let \(\lambda_{\min}(t,x)\) be the smallest eigenvalue of \(H_t(x)\).
A (maximum-principle style) heuristic yields at a spatial minimum of \(\lambda_{\min}\):
\[
\partial_t \lambda_{\min}
\;\gtrsim\;
-2\lambda_{\min}^2
+ v_{\min}^\top(\nabla^2 J_t)v_{\min}
\;-\; C_1,
\]
where \(C_1\) accounts for controlling \(\Delta H_t\) and for non-smoothness issues in \(\lambda_{\min}\) as an eigenvalue function.

**Core idea:** if one can lower-bound the source term
\[
v_{\min}^\top(\nabla^2 J_t)v_{\min} \;\ge\; c>0
\]
uniformly on an evolving “safe region”, then \(\lambda_{\min}\) satisfies a Riccati inequality with positive forcing and cannot collapse to \(-\infty\).

---

## 6. From a curvature floor to a finite-volume gap

If at some stage one has a uniform lower bound in the Bakry–Émery sense
\[
\nabla^2 S_t \succeq \rho\,I
\quad\text{(or the manifold analog: Ricci + Hessian)} ,
\]
then the standard implication is:
\[
\text{curvature } \rho \;\Rightarrow\; \text{LSI/Poincaré} \;\Rightarrow\; \text{spectral gap } \gtrsim \rho.
\]

Inside the project, the chain is:

- **Haar Jacobian** gives \(\rho_0>0\) in a local region near \(A=0\).
- **Polarity** says the bad reducible set is capacity zero, so can be ignored for diffusion estimates.
- **Hessian-flow Riccati control** is proposed to propagate \(\rho_0\) under smoothing/coarse-graining.

What remains (and is not supplied by the files as a proof) is a clean theorem that:
- identifies the correct smoothing flow corresponding to genuine YM RG / gradient flow, and
- verifies a uniform positive “source” term \(v^\top\nabla^2J_t v\) in the relevant region, with constants stable as volume grows.

---

## 7. Clustering template (finite volume)

Given a spectral gap for a local reversible dynamics plus standard locality assumptions (e.g., finite range interactions, Lieb–Robinson type bounds, or finite speed of propagation for the semigroup), one can derive exponential clustering:
\[
|\mathrm{Cov}_{\mu_\beta}(f,g)| \;\lesssim\; e^{-m\,\mathrm{dist}(\mathrm{supp}f,\mathrm{supp}g)}.
\]

The project contains this as a template rather than a completed estimate.

---

## 8. What this pipeline contributes (as extracted)

### Pipeline Architecture
A concrete dependency structure: Haar curvature source → polarity quarantine → Riccati propagation under smoothing → functional inequalities → gap → clustering.

### Rigidity Mechanism
The reducible set is treated as capacity-zero (polar) rather than as a geometric singularity that must be “controlled pointwise”.

### Implicit Theorem (conditional)
If one can exhibit a smoothing/RG flow for YM whose log-density satisfies a vHJ-type PDE with a uniform positive lower bound on \(\nabla^2 J_t\) in a safe region, then a Riccati lower bound yields a time-uniform curvature floor and hence a volume-uniform spectral gap.

This is not proven in the project files, but it is a crisp target statement.

---

## 9. Pointers to the code/experiments in this file set

- vHJ / Hessian-flow toy simulations: `02_vHJ_CurvatureFlow_Simulations.md`
- SU(3) lattice Hessian/Lanczos convexity experiment: `03_SU3_Lattice_Hessian_Convexity_Lanczos.md`
- q-Racah Doob toy mass-gap experiment (transfer-operator style): `04_qRacah_Doob_MassGap_Toy.md`
- q–6j error-budget derivations: `05_q6j_Error_Budget.md`
