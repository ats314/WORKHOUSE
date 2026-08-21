# Curvature-Stable Coarse-Graining as a Mass-Gap Mechanism (Program + Proven Sub-Results)

## Abstract

This document distills the **core analytic mechanism** developed across the YANG 3 project files:

1. **Uniform convexity / Bakry–Émery curvature** of an effective action implies a **log–Sobolev inequality (LSI)** and hence a **spectral gap** for the Euclidean (Langevin/transfer) generator.
2. A **Gaussian coarse-graining** of the Gibbs density yields a **viscous Hamilton–Jacobi (vHJ)** evolution for the effective action. Differentiating gives a **Hessian flow** and a **Riccati-type lower bound** for the smallest Hessian eigenvalue.
3. For lattice Yang–Mills in exponential coordinates, the **Haar measure’s Jacobian** supplies a genuine **quadratic “geometric mass” curvature source** near the vacuum.
4. The principal open step is to **rigorously dominate the Wilson action’s negative curvature directions** by the Haar curvature (possibly after coarse-graining), uniformly along the **asymptotically free trajectory** \(\beta(a)\to\infty\).

The result is best read as a **proof program** whose scalar/finite-dimensional components are rigorous and whose Yang–Mills closure requires further analytic work. Numerical scans in the project files supply evidence for the required convexity windows.

---

## 1. Curvature \(\Rightarrow\) functional inequalities \(\Rightarrow\) gap (the analytic cascade)

Let \(\mu(dx)=Z^{-1} e^{-S(x)}dx\) on \(\mathbb{R}^n\) with \(S\in C^2\). Define the Langevin generator
\[
L f = \Delta f - \nabla S\cdot\nabla f .
\]

### 1.1 Bakry–Émery curvature as a Hessian condition

For diffusion generators of this type, the Bakry–Émery identity can be written schematically as
\[
\Gamma_2(f)=\|\nabla^2 f\|_{HS}^2 + \langle \nabla f, (\nabla^2 S)\nabla f\rangle .
\]

Hence a uniform Hessian lower bound
\[
\nabla^2 S(x)\succeq \rho I \quad \forall x
\]
implies the curvature-dimension inequality \(\Gamma_2\ge \rho\, \Gamma\).

### 1.2 Consequences: LSI and Poincaré (spectral gap)

Under \(\Gamma_2\ge \rho\Gamma\), the Gross log–Sobolev inequality holds with constant \(\rho\), and in particular the Poincaré inequality holds with the same constant:
\[
\mathrm{Var}_\mu(f)\le \frac{1}{\rho}\int |\nabla f|^2\, d\mu.
\]

This is the engine: **find (or generate) a uniform positive \(\rho\)** and you get a spectral gap for the Euclidean generator, which becomes a physical mass gap after the usual finite-volume \(\to\) infinite-volume and OS/transfer-matrix steps.

---

## 2. Coarse-graining as a PDE: the vHJ semigroup

Define the coarse-grained density by Gaussian convolution
\[
\rho_\ell \equiv C_\ell * e^{-S_0},
\qquad
S_\ell \equiv -\log \rho_\ell .
\]

Because \(\rho_\ell\) solves a heat equation in \(\ell\), \(S_\ell\) solves the viscous Hamilton–Jacobi equation
\[
\partial_\ell S_\ell = \Delta S_\ell - |\nabla S_\ell|^2 .
\]

This is a **structural** identity: it is not a heuristic RG analogy; it is the log-transform of the heat semigroup applied to \(e^{-S_0}\).

---

## 3. Hessian flow and the Riccati lower bound (finite-dimensional rigorous core)

Differentiating the vHJ equation yields evolution equations for:

- the gradient \(b_\ell=\nabla S_\ell\)
- the Hessian \(h_\ell=\nabla^2 S_\ell\)

In the simplest “source-free” setting, the smallest eigenvalue \(m_\ell(x)=\lambda_{\min}(h_\ell(x))\) satisfies a Riccati-type differential inequality of the form
\[
\partial_\ell m_\ell \gtrsim -c\, m_\ell^2,
\]
which integrates to
\[
m_\ell \;\gtrsim\; \frac{m_0}{1+c\,m_0\,\ell}.
\]

This is exactly the kind of inequality that lets you propagate “curvature seeds” through coarse-graining: curvature can decay, but it cannot instantly vanish, and (with sources) it can stabilize at a positive plateau.

---

## 4. Yang–Mills-specific inputs (geometry + gauge subtleties)

### 4.1 Polarity of reducible connections

Reducible connections occupy singular strata in the gauge quotient. The project collects a strategy (via Gaussian capacity comparisons) to show these strata are **polar** (capacity zero) for Gaussian-type Dirichlet forms, and thus can be neglected in the LSI/spectral gap analysis (which is quasi-sure).

This is meant to remove a major analytic obstruction: you want your curvature argument to run on the smooth stratum without being wrecked by measure-zero-but-singular sets.

### 4.2 Haar measure as a curvature source (geometric mass)

In exponential coordinates \(U=\exp(iA)\), Haar measure takes the form
\[
dU = J(A)\, dA,
\]
and near the identity one has
\[
-\log J(A) = c_0 \,\mathrm{Tr}(A^2) + O(\|A\|^4),
\qquad c_0>0 \text{ (group-dependent)}.
\]

This contributes a **strictly positive quadratic term** to the effective action (per link), even when the Wilson action is flat at lowest order in these coordinates.

### 4.3 Wilson action as a curvature eroder

Numerical Hessian scans in the files strongly suggest the Wilson term introduces negative-curvature directions away from the origin, with an approximate erosion law of the form
\[
\lambda_{\min}(\nabla^2 S_{\mathrm{Wilson+Haar}}(A))
\approx c_0 - C\,\beta\, r^2,
\qquad r\sim \|A\|_\infty,
\]
leading to an empirical “static convexity radius”
\[
R(\beta)\;\approx\;\sqrt{\frac{c_0}{C\,\beta}}.
\]

This is not yet a theorem—but it is the **right quantitative target** for analysis.

---

## 5. What is “new” here (as a research direction)

The novelty is not any single classical lemma (Bakry–Émery, LSI, etc.). The novelty is the *architecture*:

- Treat **curvature** (uniform Hessian lower bounds) as the *primary conserved quantity* you must preserve under coarse-graining.
- Use the **vHJ semigroup** as the mathematically correct coarse-graining evolution for \(-\log\) densities.
- Use **group geometry (Haar Jacobian)** as an intrinsic “mass-like” curvature source.
- Remove gauge-singularity issues by showing **reducible strata are polar** and therefore irrelevant to the functional-inequality machinery.

If these pieces can be closed for 4D Yang–Mills uniformly in the continuum limit, the rest of the mass-gap chain becomes standard (but technically heavy).

---

## 6. Concrete next analytic targets

1. **A rigorous small-field bound** for the Wilson Hessian:
   \[
   \|\nabla^2 S_W(A)\|\le C_{\mathrm{SU(3)}}\,\beta\,\|A\|^2
   \quad \text{(or similar)},
   \]
   in the same coordinates used in the numerics.

2. **A provable convexity radius** \(R(\beta)\) (even if crude), consistent with the scaling \(R(\beta)\sim \beta^{-1/2}\).

3. **A “source” term analysis** in the vHJ/Hessian flow matching the Haar-induced quadratic curvature, to show curvature stabilizes at \(\lambda_\ast>0\) after coarse-graining (or after a controlled “restoration” time).

4. **Uniformity in \(a\to 0\)** along \(\beta(a)\to\infty\): show the post-restoration curvature lower bound does not collapse.

---

## Sources in the project

Primary derivations for this document are distributed across:

- expanded finite-dimensional proof stack (`massgap_expanded.md`)
- vHJ/Hessian-flow notes (`doc2_vHJ_Hessian_Flow.txt`)
- functional-inequality toolbox (`doc1_Functional_Inequalities_and_Spectral_Gap_Tools.txt`)
- reducible polarity/capacity notes (`doc3_...`, `doc5_...`)
- SU(3) lattice Hessian/convexity scans and code logs (12/2–12/3 code PDFs and text exports)
- q-deformed toy pillar (01–05 q-Racah/q-flow documents)

