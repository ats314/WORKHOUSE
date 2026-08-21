# Curvature-Based Mass-Gap Pipeline (Finite-Volume Analytic Skeleton)

## 0. Scope and epistemic status

This document extracts a *pipeline architecture* that is spread across the project files:

1. **A local convexity / curvature floor** is supplied by group geometry (Haar Jacobian in exponential coordinates) and/or an explicit quadratic mass term.
2. **Singular strata** (reducible connections / enhanced stabilizers) are treated as **capacity-zero / polar** for the relevant Dirichlet forms, so they do not obstruct functional inequalities.
3. A diffusion/coarse-graining surrogate (the **viscous Hamilton–Jacobi semigroup**) admits a **Hessian flow** with a Riccati-type mechanism that predicts how curvature decays or stabilizes.
4. **Bakry–Émery** converts a uniform curvature floor into **LSI/Poincaré** constants, hence a **finite-volume spectral gap** for the associated Langevin generator.
5. **Locality + gap** gives a standard exponential clustering template.

Nothing in this document is, by itself, a 4D continuum Yang–Mills mass-gap proof. The pipeline is a *structured attempt* to isolate exactly what must be proved (or simulated) to make such a route viable.

---

## 1. Finite-dimensional setting and the analytic target

Let \(S:\mathbb{R}^n\to\mathbb{R}\) be a smooth effective action and define the Gibbs measure
\[
\mu(dx)=Z^{-1}e^{-S(x)}dx.
\]

Consider the (overdamped) Langevin generator
\[
L = \Delta - \nabla S\cdot \nabla,
\]
which is symmetric in \(L^2(\mu)\) with Dirichlet form
\[
\mathcal{E}(f,f)=\int |\nabla f|^2\,d\mu.
\]

**Target (finite volume):** prove a uniform Poincaré constant
\[
\mathrm{Var}_\mu(f)\le \frac{1}{\lambda}\,\mathcal{E}(f,f),
\]
and, ideally, a log–Sobolev constant
\[
\mathrm{Ent}_\mu(f^2)\le \frac{2}{\rho}\,\mathcal{E}(f,f),
\]
with constants \(\lambda,\rho\) stable under the intended finite-volume family.

---

## 2. Curvature \(\Rightarrow\) functional inequalities (Bakry–Émery skeleton)

For \(L=\Delta-\nabla S\cdot \nabla\), Bakry–Émery identifies the “curvature” with the Hessian of \(S\).

A standard sufficient condition is the uniform convexity bound
\[
\nabla^2 S(x)\succeq \rho\,I \quad\text{for all }x,
\]
which implies a curvature-dimension inequality \(CD(\rho,\infty)\). Under this condition one gets:

- a log–Sobolev inequality with constant \(\rho\),
- a Poincaré inequality with constant \(\lambda\ge \rho\),
- hence a spectral gap lower bound for \(-L\) by \(\rho\).

**What is “nontrivial” here in the project:** the point is not the theorem; it is the attempt to manufacture a *uniform* lower bound on \(\nabla^2 S\) in a Yang–Mills-like lattice setting by combining:
- Haar geometry (Section 3),
- polarity/capacity removal of singular strata (Section 4),
- a curvature-evolution control mechanism under coarse-graining (Section 5).

---

## 3. Haar Jacobian as a curvature/convexity source (lattice YM coordinates)

On a compact Lie group \(G\) (e.g. \(SU(N)\)), parametrize a link variable by exponential coordinates
\[
U=\exp(A),\qquad A\in\mathfrak{g}.
\]
In these coordinates, Haar measure has a Jacobian of the form
\[
dU = J(A)\,dA,
\qquad
J(A)=\det\!\left(\frac{\sinh(\mathrm{ad}_A/2)}{\mathrm{ad}_A/2}\right).
\]

Expanding at \(A=0\),
\[
-\log J(A) = c_0\,\mathrm{Tr}(A^2) + O(\|A\|^4),
\qquad c_0>0 \ \text{(Casimir-dependent)}.
\]

**Extracted implication:** at small field amplitude (in exponential coordinates), the measure contributes a strictly convex quadratic “mass-like” term. This is a *geometric* curvature source independent of the Wilson action.

**Conditional limitation:** the expansion is local in \(A\). A global uniform convexity statement requires controlling charts (large fields, coordinate singularities) or proving that the diffusion/measure does not spend time there (Section 4).

---

## 4. Polarity / capacity quarantine of reducible strata

For lattice YM configuration spaces \(G^{\mathcal{B}}\) (finite-dimensional compact manifolds), the reducible set (enhanced stabilizer) is a finite union (or countable union across stabilizer types) of positive-codimension algebraic subvarieties.

For elliptic diffusions, such submanifolds are expected to be **polar** (hitting probability zero), and hence **capacity-zero** for the associated Dirichlet form.

In the Gaussian reference model for connections in a Hilbert space (Ornstein–Uhlenbeck Dirichlet form), any affine subspace of infinite codimension is polar. If a Yang–Mills-type measure is absolutely continuous with respect to the Gaussian reference with sufficiently controlled Radon–Nikodym derivative, capacity comparison transfers polarity.

**Extracted role in the pipeline:** this is the “singular-set removal” step. If reducibles are capacity-zero, they do not obstruct global functional inequalities (LSI/Poincaré), because those are stable under removal of capacity-zero sets.

---

## 5. Coarse-graining surrogate: viscous Hamilton–Jacobi semigroup and Hessian flow

### 5.1 Exact vHJ semigroup identity (no external source)

Let \(P_\ell=e^{\ell\Delta}\) be the Euclidean heat semigroup and define
\[
S_\ell(x):=-\log\big(P_\ell e^{-S_0}\big)(x).
\]
Then \(S_\ell\) satisfies the **viscous Hamilton–Jacobi** equation
\[
\partial_\ell S_\ell = \Delta S_\ell - \|\nabla S_\ell\|^2.
\]

This is an identity; there is **no** additional term in the pure heat-semi\-group case.

### 5.2 Optional “source/anomaly” term (modeling knob)

Several project notes also consider a sourced variant
\[
\partial_\ell S_\ell = \Delta S_\ell - \|\nabla S_\ell\|^2 + J_\ell(x),
\]
where \(J_\ell\) is **not** determined by the heat semigroup; it is an *external term* intended to encode extra structure (e.g. measure/Jacobian effects, block-spin coarse graining artifacts, etc.).

Any use of \(J_\ell\) must therefore be treated as **conditional**:
> “If the intended coarse-graining map induces a vHJ-type PDE with source \(J_\ell\) whose Hessian \(\nabla^2J_\ell\) is positive enough, then curvature can be stabilized.”

### 5.3 Hessian flow and Riccati mechanism

Let \(b_\ell=\nabla S_\ell\) and \(H_\ell=\nabla^2 S_\ell\). Differentiating gives (Euclidean setting):
\[
\partial_\ell H_\ell
=
\Delta H_\ell
-2(b_\ell\cdot\nabla)H_\ell
-2H_\ell^2
\quad (\text{plus } \nabla^2 J_\ell \text{ in the sourced case}).
\]

The term \(-2H_\ell^2\) is the Riccati nonlinearity. Formally, at a point and in an eigen-direction of \(H_\ell\) with eigenvalue \(\lambda\), it suggests an inequality of the schematic form
\[
\partial_\ell \lambda \lesssim -2\lambda^2 + \text{(source)} + \text{(transport/diffusion terms)}.
\]

**Extracted use:** this provides a *quantitative diagnostic* for how a curvature floor should decay (or stabilize) under smoothing/coarse-graining. It also motivates the empirical fits of the form
\[
\lambda(\ell)\approx \frac{1}{a+\alpha \ell}
\]
seen in the numerical experiments.

---

## 6. From curvature floor to finite-volume gap

Conditional theorem schema (finite-dimensional):

- If one can ensure \(\nabla^2 S \succeq \rho I\) uniformly in the volume/parameters on the region that carries all \(\mu\)-mass up to capacity-zero sets,
- then Bakry–Émery yields LSI(\(\rho\)) and Poincaré(\(\rho\)),
- hence a spectral gap \(\lambda_1(-L)\ge \rho\).

The novelty claim is **not** this theorem, but the *planned mechanism* to supply the hypothesis in a YM-like setting:
\[
\text{(Haar curvature floor)} + \text{(polarity quarantine)} + \text{(curvature propagation under RG-like flow)}.
\]

---

## 7. Clustering template (finite volume)

A standard template used in the project notes is:

- if the generator decomposes locally \(L_\Lambda=\sum_x L_x\) with finite range,
- and Poincaré holds uniformly with constant \(\lambda>0\),

then covariances of local observables \(F,G\) with separated supports satisfy
\[
|\mathrm{Cov}_{\mu_\Lambda}(F,G)|
\le C e^{-c\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)} \,
\|\nabla F\|_{L^2(\mu_\Lambda)}\|\nabla G\|_{L^2(\mu_\Lambda)}.
\]

---

## 8. What (if anything) is potentially novel here?

**Novel-in-assembly pipeline:** the project does not claim new functional-inequality theorems. The potentially new element is the *particular coupling* of:

- Haar Jacobian as a built-in curvature source in exponential coordinates,
- capacity/polarity as a clean way to remove reducible singular strata from the functional-inequality problem,
- Hessian-flow/Riccati as a curvature-propagation diagnostic under coarse-graining,
- with explicit numerical probes (separate documents) designed to measure the relevant curvature quantities.

Whether this can be upgraded from “architecture + numerics” to a theorem hinges on proving a genuine coarse-graining map with controlled \(J_\ell\), or proving uniform convexity without needing such a flow.

---

## 9. Where this comes from in the project tree

Key source files in `/mnt/data/` include:

- `YM_Salvage_Stack_Appendix_C_Haar_Mass_Term_Lattice_YM.txt` (Haar Jacobian expansion)
- `YM_Salvage_Stack_Appendix_B_Polarity_Gaussian_and_Lattice.txt`, `doc3_Gaussian_Polarity_and_Capacity.txt`, `doc5_Polarity_Reducible_Connections_Gaussian.txt` (polarity/capacity)
- `doc2_vHJ_Hessian_Flow.txt`, `YM_Salvage_Stack_Appendix_D_Hessian_Flow_and_Riccati.txt` (Hessian flow / Riccati structure)
- `doc1_Functional_Inequalities_and_Spectral_Gap_Tools.txt`, `doc6_Finite_Volume_Clustering_Template.txt` (gap→clustering templates)

