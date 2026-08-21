# One Operator in Three Guises: Wilson Hessian, Gibbs Generator, and Heat Flow

This note isolates a single object that keeps reappearing across the proof pipeline and the simulations:

\[
M \;=\; m^2 I \;+\; \alpha\, d_1^\* d_1,
\qquad
m^2>0,\ \alpha>0,
\]

acting on lattice $1$-cochains with values in the Lie algebra $\mathfrak g$ (and restricted to the horizontal/gauge-orthogonal sector when needed).
It shows up as:

1. a **Hessian** (small-field Wilson action curvature / stiffness),
2. a **Gibbs/Witten operator** (the “second quantized” diffusion generator on $1$-forms),
3. a **heat-flow kernel controller** (through the inverse $M^{-1}$ and its exponential off-diagonal decay).

The value of this “triple appearance” is that it welds *geometry* (curvature), *stochastics* (mixing and drift), and *spectral theory* (Green kernel decay) into one mechanism.

---

## 1. Lattice configuration space and the Wilson diffusion

Let $\Lambda$ be a finite periodic lattice (e.g. a 4D torus) and set

\[
M_\Lambda := G^{E(\Lambda)},
\]

with product bi-invariant metric. The Wilson Gibbs measure has density

\[
d\mu_{\Lambda,\beta}(U) \;\propto\; e^{-S_{\Lambda,\beta}(U)}\, d\mathrm{vol}_{g_\Lambda}(U).
\]

The associated reversible diffusion generator on smooth observables $f$ is

\[
L_\Lambda f \;=\; \Delta_\Lambda f \;-\;\langle\nabla S_{\Lambda,\beta}, \nabla f\rangle_{g_\Lambda},
\]

with carré-du-champ

\[
\Gamma_\Lambda(f,g)=\langle\nabla f,\nabla g\rangle_{g_\Lambda}.
\]

---

## 2. Curvature matrix: Bochner–Bakry–Émery identity

The “effective curvature” relevant for functional inequalities is not just the Riemannian Ricci tensor, but

\[
\mathrm{Ric}_{\mu_{\Lambda,\beta}}
\;:=\;
\mathrm{Ric}_{g_\Lambda} \;+\; \nabla^2 S_{\Lambda,\beta}.
\]

The Bochner–Bakry–Émery identity reads

\[
\Gamma_{2,\Lambda}(f)
\;=\;
\|\nabla^2 f\|_{\mathrm{HS}}^2
\;+\;
\mathrm{Ric}_{\mu_{\Lambda,\beta}}(\nabla f,\nabla f).
\]

This is the “matrix hinge” entry point: if you can lower-bound $\mathrm{Ric}_{\mu}$ by a *positive operator* on tangent vectors, you get Poincaré/LSI-type control.

---

## 3. The matrix hinge: $m^2 I + \alpha d_1^\* d_1$ on a good set

On a small-field / “good” event $K_\Lambda(r)$ (plaquette holonomies near $\mathbf 1$ so exponential coordinates and Taylor control are uniform), the project files establish the hinge-type lower bound

\[
\mathrm{Ric}_{\mu_{\Lambda,\beta}}(U)
\;\succeq\;
m^2 I \;+\; \alpha\, d_1^\*d_1
\qquad
\text{(on horizontal directions),}
\]

with the identifications

\[
m^2 = \frac{c_H}{2}, \qquad \alpha=\frac{\beta}{n\lambda_\rho},
\]

where $c_H>0$ comes from the group/Haar geometry term and $\lambda_\rho$ is the representation-dependent normalization constant (see the project's notation file).

Conceptually:

- $m^2 I$ is a **geometric “mass” floor** (compact group curvature / Haar Jacobian contribution).
- $\alpha d_1^\*d_1$ is the **Maxwell stiffness** (discrete curl–curl term on $1$-cochains).

This is the first guise: **Hessian / stiffness**.

---

## 4. Helffer–Sjöstrand: covariance is an inverse Witten Laplacian

For reversible diffusions, the Helffer–Sjöstrand identity expresses covariance via an inverse operator on $1$-forms:

\[
\mathrm{Cov}_{\mu_{\Lambda,\beta}}(F,G)
\;=\;
\left\langle
\nabla F,\,
\big(\mathcal L^{(1)}\big)^{-1}\nabla G
\right\rangle_{L^2(\mu)},
\]

where the “lifted” operator on $1$-forms is

\[
\mathcal L^{(1)}
\;=\;
(-L_\Lambda)\otimes I \;+\; \mathrm{Ric}_{\mu_{\Lambda,\beta}}.
\]

On the good set, the hinge implies

\[
\mathcal L^{(1)} \;\succeq\; M \;=\; m^2 I + \alpha d_1^\*d_1,
\]

hence

\[
(\mathcal L^{(1)})^{-1} \;\preceq\; M^{-1}.
\]

This is the second guise: **Gibbs/Witten operator** (diffusion generator on $1$-forms).

---

## 5. Exponential clustering is “just” Green-kernel decay

Once covariance is bounded by $M^{-1}$, exponential clustering reduces to:

> **Prove off-diagonal decay of the kernel $(M^{-1})_{b,b'}$ in the link-graph distance.**

The project builds two routes:

- a **Combes–Thomas** finite-range inverse-decay lemma (very robust),
- a sharper **Davies method** rate for the massive Maxwell operator.

Either way, you obtain

\[
\big\|(M^{-1})_{b,b'}\big\|_{\mathrm{op}}
\;\le\;
C\,e^{-\eta\,\mathrm{dist}_E(b,b')},
\]

with $\eta>0$ uniform in volume.

This is the third guise: **heat-flow / Green-kernel controller**.

---

## 6. Why this is exciting (and not just bookkeeping)

The same operator $M$ simultaneously:

- **pinches curvature** (via $\mathrm{Ric}_\mu$),
- **pinches covariance** (via $(\mathcal L^{(1)})^{-1}$),
- **pinches mixing/flow** (via the semigroup $e^{tL_\Lambda}$).

In physical language: the object that suppresses fluctuations locally is the same object that suppresses correlations at distance and accelerates relaxation.

The simulation logs strengthen this picture by empirically verifying drift decompositions and a remarkably rigid “affine Laplacian law” linking the Laplacian part of $LV$ to the plaquette action density (see `04_simulation_certificates.md`).

---

## 7. Continuum-limit hint (architecture, not a miracle)

If one pursues a continuum limit, the most natural upgrade is to treat $(\mathcal E_a,\mu_a)$ as a *Dirichlet-form family*, with

\[
\mathcal E_a(f,f) = \int \|\nabla_a f\|^2\,d\mu_a.
\]

The operator-triad viewpoint suggests an orderly target:

- identify the scaling of $M_a$ (or its continuum analog on divergence-free $1$-forms),
- prove Mosco convergence of the forms on a cylinder core,
- transfer spectral-gap information via lower semicontinuity.

That is a rigorous road, even if it is steep.

---

## Cross references

- Analytic core: Bochner/BE, HS, and the hinge appear in Part 6 and the notation/constants ledger.
- Green kernel decay: Part 9 and its Davies refinements.
- OS / Euclidean-to-Hamiltonian bridge: Part 10–11.
- Coarse graining + RP permanence: Part 12.
- Numerical evidence: `04_simulation_certificates.md`.
