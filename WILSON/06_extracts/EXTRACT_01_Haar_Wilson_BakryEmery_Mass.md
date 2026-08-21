---
title: "EXTRACT 01 — Mass from Geometry: Bakry–Émery Curvature from Haar + Wilson"
project: "SWIM2"
source_files:
  - "PROOF_04_Geometric_Mass_Derivation.md"
  - "SYNTH_P04_haar_geometry_supplement.md"
  - "SYNTH_P09_wilson_hessian.md"
status: "extracted synthesis"
---

# Mass from Geometry: Bakry–Émery Curvature from Haar + Wilson (Lattice)

## Abstract

This note isolates the *geometric mass mechanism* that keeps recurring across the project:

> Treat lattice gauge configurations as a Riemannian manifold (a product of compact Lie groups), and treat the lattice Gibbs measure as a weighted Riemannian volume. Then the **Bakry–Émery tensor**
\[
\mathrm{Ric}_{\mu} \;=\; \mathrm{Ric}_{g} \;+\; \nabla^2 S
\]
acts like a **mass-squared operator** on physical (horizontal) directions.

The project’s key claim is that, at least *near the identity / small-field region*, one has a uniform lower bound
\[
\mathrm{Ric}_{\mu_\beta}\big|_{\mathrm{hor}} \;\ge\; (\kappa + \beta\,c_W)\,g\big|_{\mathrm{hor}}
\qquad(\kappa>0,\; c_W>0),
\]
which implies local Poincaré / log-Sobolev inequalities and an effective mass scale
\[
m_{\mathrm{eff}}^2 \sim \kappa + \beta c_W.
\]

The novelty is not Bakry–Émery itself (classic), but the *identification* of a **scale-stable curvature floor** coming from the Haar-product geometry and the **horizontal positivity** of the Wilson Hessian as the “source” that seeds a gap.

---

## 1. Geometric setup (lattice configuration manifold)

Let \(G=\mathrm{SU}(N)\) and let \(E\) be the set of oriented lattice edges/links. A lattice gauge field is
\[
U=(U_e)_{e\in E}\in \mathscr{A}:=G^E.
\]

Equip \(G\) with a bi-invariant Riemannian metric \(g_G\) (e.g. induced by \(-\mathrm{Tr}\) on \(\mathfrak{su}(N)\)), and equip the product \(G^E\) with the product metric \(g\).

**Fact (Einstein property).** For compact simple \(G\) with bi-invariant metric, \(G\) is Einstein:
\[
\mathrm{Ric}_G = \kappa\, g_G,\qquad \kappa>0,
\]
and the product \(G^E\) inherits
\[
\mathrm{Ric}_{g} = \kappa\, g.
\]
(Here \(\kappa\) depends on metric normalization; in the project one convenient normalization is \(\kappa=\tfrac14 C_{\mathrm{adj}}\).)

---

## 2. The Gibbs measure and the Bakry–Émery tensor

Let the Wilson action be \(S_\beta:\mathscr{A}\to\mathbb{R}\), with coupling \(\beta\). Define the Gibbs measure
\[
d\mu_\beta(U) = Z_\beta^{-1}\,e^{-S_\beta(U)}\,d\mathrm{vol}_g(U),
\]
where \(d\mathrm{vol}_g\) is the Riemannian volume associated to \(g\).

The associated Bakry–Émery tensor is
\[
\mathrm{Ric}_{\mu_\beta} \;=\; \mathrm{Ric}_{g} \;+\; \nabla^2 S_\beta.
\]

### Why this object matters in this project

If \(\mathrm{Ric}_{\mu_\beta}\ge \rho\,g\) (as quadratic forms) for some \(\rho>0\), then the diffusion generator \(L=\Delta - \nabla S_\beta\cdot \nabla\) satisfies the curvature-dimension condition \(CD(\rho,\infty)\), implying:

- a Poincaré inequality (spectral gap \(\lambda_1\ge \rho\)),
- a log-Sobolev inequality (with constant \(\gtrsim \rho\)),

at least in the regimes where the bound is valid.

The project interprets this \(\rho\) as a “mass-squared” scale.

---

## 3. Horizontal (physical) directions and why they matter

Gauge transformations act on \(\mathscr{A}=G^E\). Let the infinitesimal gauge directions define a vertical subbundle; choose a horizontal distribution (e.g. from a gauge-fixing condition) and let
\[
P_0:\;T\mathscr{A}\to T\mathscr{A}
\]
denote the orthogonal projection onto horizontal directions.

The “physical Hessian” is the restriction
\[
H_{\mathrm{phys}} \;:=\; P_0^\top (\nabla^2 S_\beta)\,P_0,
\]
and the geometric claim is a positive lower bound on \(H_{\mathrm{phys}}\) *near the identity region*.

---

## 4. Wilson Hessian positivity on horizontals (local, near identity)

A recurring technical pivot in the project is:

> Near the identity (small plaquette angles), the Wilson action is strictly convex on horizontal directions.

Formally, there exists a neighborhood \(\mathcal{U}\subset \mathscr{A}\) of the identity configuration such that
\[
P_0^\top (\nabla^2 S_\beta)(U)\,P_0 \;\ge\; \beta\,c_W\, g
\qquad\text{for all }U\in\mathcal{U},
\]
for some constant \(c_W>0\).

### How this connects to the “lattice Hodge” picture (P09-style)

In the quadratic/small-field regime, the Wilson Hessian becomes (schematically) a discrete Laplacian-type operator \(M\) on 1-cochains:
\[
H_W|_{\mathrm{phys}} \approx \beta\,M,
\]
with decomposition into:

- **Gauge** directions: kernel (pure gauge variations),
- **Toron / harmonic** directions (on periodic lattices): kernel of \(M\) but not gauge,
- **Reduced physical** directions (coexact / co-closed with harmonics removed): strictly positive spectrum.

This decomposition is crucial because it isolates *where strict positivity really lives* (and what must be quotiented out).

---

## 5. The curvature floor: Haar geometry + Wilson convexity

Combining the Einstein property of the Haar product metric and the local Wilson convexity yields the core inequality:

\[
\mathrm{Ric}_{\mu_\beta}\big|_{\mathrm{hor}}
=
\mathrm{Ric}_g\big|_{\mathrm{hor}} + \nabla^2 S_\beta\big|_{\mathrm{hor}}
\;\ge\;
(\kappa + \beta c_W)\,g\big|_{\mathrm{hor}}.
\]

Interpretation:

- \(\kappa\) is a **background curvature floor** from the configuration manifold geometry (scale-stable for a fixed group/metric choice).
- \(\beta c_W\) is a **dynamical convexity** term (depends on coupling and on being in the near-identity region).

This is one of the most “theory-extendable” pieces of the project: the idea that *a measure on a curved configuration manifold* can carry a built-in curvature floor which, once projected to physical directions, behaves like a gapping mechanism.

---

## 6. What is genuinely new here (and what is not)

### Not new
- Bakry–Émery curvature-dimension theory.
- “Uniform convexity \(\Rightarrow\) Poincaré/LSI”.

### Potentially new / worth pushing
- **Viewing the Haar-product configuration manifold curvature \(\kappa\) as a physical input** (a seed for a gap mechanism), especially when combined with horizontal projection.
- **Making “Wilson Hessian positivity on horizontals” a modular lemma** that can be propagated under RG (instead of proving a mass gap directly from correlators).
- **Separating**: (i) local curvature positivity (geometric/analytic) from (ii) OS reconstruction (QFT bridge).

---

## 7. Immediate next steps to strengthen this mechanism

1. **Globalize beyond “near identity”.**  
   The current bound is local in field space. A credible path is to add a Lyapunov function / coercive barrier to control excursions (see the project’s Lyapunov-themed prongs).

2. **Quantify constants carefully.**  
   Determine \(\kappa\) and \(c_W\) with explicit normalization and track how they scale with lattice spacing \(a\).

3. **Track the toron/harmonic sector.**  
   Either impose boundary conditions eliminating \(H^1\) or treat torons as a separate topological sector in the OS reconstruction step.

4. **Connect to continuum via tightness / lifting.**  
   The curvature floor alone does not give a continuum mass gap unless you can pass to the continuum measure and control the projection onto local observables.

