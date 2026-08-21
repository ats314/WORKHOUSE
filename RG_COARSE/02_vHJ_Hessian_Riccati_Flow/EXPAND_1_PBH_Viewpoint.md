# Expansion of Section 1: The PBH Viewpoint (Horizontal vHJ on Gauge Orbit Space)

This note expands **Section 1 (“The PBH viewpoint”)** of `EXTRACT_PBH_Riccati_Mass_Gap.md` by making explicit:

- what “horizontal” means on gauge orbit space,
- why a **viscous Hamilton–Jacobi (vHJ)** PDE is a natural object in RG/coarse-graining,
- how to derive vHJ from a linear heat/Schrödinger-type evolution via a **Cole–Hopf (log-density) transform**, and
- how this sets up the PBH Hessian flow used later.

The goal is not to claim the YM mass gap is solved here, but to clarify the *mathematical mechanism* the project isolates.

---

## 1. Geometry: from configuration space to orbit space

### 1.1 Configuration space and gauge group (finite cutoff)

At a **finite cutoff** (lattice spacing \(a>0\) or Galerkin truncation), the configuration space is finite-dimensional:

- Lattice: \(\mathcal{A} \equiv \mathcal{C} = G^{E}\) with \(G=\mathrm{SU}(N)\) and \(E\) the set of oriented edges.
- Gauge group: \(\mathcal{G} = G^{V}\) with \(V\) the set of vertices.

Gauge acts by \(U_e \mapsto g_{s(e)}^{-1}U_e g_{t(e)}\).

The orbit space \(\mathcal{A}/\mathcal{G}\) is **not** a smooth manifold globally; it is a **stratified space**. Its **regular stratum** \(\mathcal{M}_{\mathrm{reg}}\) corresponds to irreducible (or “regular”) orbits.

### 1.2 Metric and the horizontal distribution

Equip \(\mathcal{A}\) with the product Riemannian metric induced by an \(\mathrm{Ad}\)-invariant inner product on \(\mathfrak{su}(N)\) (e.g. \(\langle X,Y\rangle=-\mathrm{Tr}(XY)\)).

At a point \(A\in\mathcal{A}_{\mathrm{reg}}\), the tangent splits into:

- **Vertical** (gauge) directions: \( \mathsf{V}_A := \{ D_A \phi : \phi \in \mathrm{Lie}(\mathcal{G})\}\),
- **Horizontal** directions: \( \mathsf{H}_A := \mathsf{V}_A^\perp\) w.r.t. the metric.

This choice matches a “Coulomb/Landau-type” gauge condition: horizontality is “orthogonal to pure gauge”.

The quotient \(\mathcal{M}_{\mathrm{reg}}=\mathcal{A}_{\mathrm{reg}}/\mathcal{G}\) inherits a Riemannian metric such that the projection \(\pi:\mathcal{A}_{\mathrm{reg}}\to\mathcal{M}_{\mathrm{reg}}\) is a Riemannian submersion. Informally: calculations on \(\mathcal{M}_{\mathrm{reg}}\) can be done upstairs using horizontal lifts.

### 1.3 Horizontal gradient and horizontal Laplacian

Let \(F\) be gauge-invariant, so \(F= f\circ \pi\) for some \(f\) on \(\mathcal{M}_{\mathrm{reg}}\).

- \(\nabla_H f\) is the unique horizontal vector field whose horizontal lift equals \((\nabla F)^{\mathrm{hor}}\) upstairs.
- \(\Delta_H f\) is the corresponding Laplace–Beltrami operator on \(\mathcal{M}_{\mathrm{reg}}\), computable via horizontal divergence of \(\nabla_H f\).

A practical mantra:

> **For gauge-invariant observables, “horizontal” is where the physics lives; “vertical” is gauge redundancy.**

---

## 2. Why a viscous Hamilton–Jacobi PDE is natural here

The project’s ansatz is the **horizontal viscous Hamilton–Jacobi** PDE:
\[
\partial_t S_t
= \Delta_H S_t - |\nabla_H S_t|^2 + J_t.
\tag{vHJ}
\]

Two strong motivations exist at finite cutoff.

### 2.1 Cole–Hopf derivation from heat/Schrödinger-type evolution

Let \(\rho_t\) be a positive density on \(\mathcal{M}_{\mathrm{reg}}\). Define
\[
S_t := -\log \rho_t.
\]

Assume \(\rho_t\) solves a linear parabolic equation with potential:
\[
\partial_t \rho_t = \Delta_H \rho_t - J_t\,\rho_t.
\tag{Lin}
\]

Then compute using \(\rho_t=e^{-S_t}\):

- \(\partial_t \rho_t = -e^{-S_t}\,\partial_t S_t\),
- \(\Delta_H(e^{-S_t}) = e^{-S_t}\left(-\Delta_H S_t + |\nabla_H S_t|^2\right)\).

Plugging into (Lin) and dividing by \(e^{-S_t}\) gives exactly:
\[
\partial_t S_t = \Delta_H S_t - |\nabla_H S_t|^2 + J_t,
\]
i.e. (vHJ).

So (vHJ) is **exactly** the log-density form of a linear diffusion-with-potential equation.

Interpretation:
- \(\Delta_H \rho_t\): coarse-graining / smoothing (heat-kernel convolution).
- \(J_t\rho_t\): Jacobian, anomaly, or “local weight” correction.
- \(|\nabla_H S_t|^2\): nonlinear term produced by the log transform.

### 2.2 Stochastic control / large deviations interpretation

The same vHJ equation appears as the **Hamilton–Jacobi–Bellman** PDE for controlled diffusions.
Very roughly: \(S_t\) behaves like a rate function for a diffusion on configuration space (or orbit space), and \(J_t\) is the running “cost”. This is conceptually aligned with RG as a flow of effective free energies.

This is not used as a formal proof, but it gives intuition for why the vHJ structure is ubiquitous whenever you smooth a probability density and then take a logarithm.

---

## 3. What is \(J_t\) in this program?

In the PBH flow pipeline, the *Hessian* of \(J_t\) is the key input:
\[
S_{\mathrm{anom}}(t) := \nabla_H^2 J_t.
\]

This is why \(J_t\) is called the “anomaly source”: it becomes a positive forcing term in the *Hessian* evolution (PBH). In lattice language, \(J_t\) can be thought of as encoding:

- measure Jacobians (Haar, Faddeev–Popov),
- determinants from integrating out modes,
- trace anomaly contributions.

The project’s conditional theorems essentially ask:

> Can we show \(S_{\mathrm{anom}}(t)\) is uniformly positive on physical (horizontal) directions?

If yes, the downstream Riccati mechanism turns that into a persistent positive lower bound for the Hessian eigenvalues (a mass scale).

---

## 4. Why horizontality matters for PDEs

Working on \(\mathcal{M}_{\mathrm{reg}}\) instead of \(\mathcal{A}\) is not just philosophical: it avoids spurious degeneracies.

- On \(\mathcal{A}\), the action has flat gauge directions; Hessians have gauge zero-modes.
- On \(\mathcal{M}_{\mathrm{reg}}\), those modes are quotiented out; the Hessian “means something” physically.

Caveat: \(\mathcal{A}/\mathcal{G}\) is stratified. The singular locus (reducibles) can obstruct global PDE arguments unless you have a way to ignore it (e.g., polarity/capacity-zero results used elsewhere in the project).

---

## 5. Minimal “finite cutoff theorem” one could aim to prove

A realistic theorem statement at finite cutoff (lattice/Galerkin) might look like:

1. \(\mathcal{M}_{\mathrm{reg}}\) is a smooth Riemannian manifold (regular stratum).
2. A positive density \(\rho_t\) evolves by (Lin) for \(t\ge 0\).
3. Define \(S_t=-\log\rho_t\). Then \(S_t\) solves (vHJ).
4. If \(J_t\) is smooth and \(\rho_t\) stays positive, all derivatives used in PBH are justified.

This would turn the vHJ ansatz from “physically motivated” into an actual derived statement (within the chosen coarse-graining scheme).

---

## 6. Why this is genuinely interesting

The PBH program is essentially:

> **Mass generation = curvature/convexity generation under a parabolic RG.**

Section 1 is where that worldview is born: *once you accept a diffusion-like coarse-graining and take a log*, a Hamilton–Jacobi nonlinearity is forced on you. Then the Hessian evolution inherits the Riccati term \(-2h^2\), which is exactly the “damping vs forcing” competition that later creates a stable positive fixed point (mass).

