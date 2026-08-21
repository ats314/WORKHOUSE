# Fixed-Cutoff Mass Gap Engine (SU(2) Wilson): The “Good-Set Clustering → OS Gap” Pipeline

## Abstract
This note extracts the most *structurally complete* part of the project: a fixed-lattice-spacing (
$ a>0 $) mechanism that turns **a restricted Poincaré inequality on a small-field region** into **uniform exponential clustering** for local observables, and then into an **Osterwalder–Schrader (OS) Hamiltonian spectral gap**.  

The point of presenting this as an “engine” is that each module is (a) local, (b) finite-range, (c) stable under small quasi-local perturbations, and therefore potentially reusable in other lattice field theories.

What this note *does not* do: it does not claim an unconditional global Poincaré inequality for the full Gibbs measure. Extending from the small-field measure to the full measure requires additional “localization/typicality” input (see §6).

---

## 1. Setup
Let $\Lambda\subset\mathbb Z^4$ be a finite periodic lattice with spacing $a>0$, gauge group $G=\mathrm{SU}(2)$, and configuration manifold
\[
M_\Lambda := G^{E(\Lambda)}.
\]
Let $S_\Lambda$ be the Wilson action and
\[
\mathrm d\mu_\Lambda(U)=Z_\Lambda^{-1}e^{-S_\Lambda(U)}\,\mathrm d\mathrm{vol}(U)
\]
its Gibbs measure.

Let $\nabla$ and $\Delta$ be the Riemannian gradient/Laplacian on the product manifold $M_\Lambda$.

For $f\in C^\infty(M_\Lambda)$ define variance and Dirichlet energy
\[
\mathrm{Var}_{\mu_\Lambda}(f)=\int f^2\,\mathrm d\mu_\Lambda-\Bigl(\int f\,\mathrm d\mu_\Lambda\Bigr)^2,\qquad
\mathcal E_\Lambda(f)=\int |\nabla f|^2\,\mathrm d\mu_\Lambda.
\]

A (restricted) Poincaré inequality is of the form
\[
\mathrm{Var}_{\mu}(f)\le C_P\,\mathcal E(f).
\]

---

## 2. Small-field (“Good Set”) restriction
Introduce an averaged plaquette disorder functional $\mathcal B_\Lambda(U)$ (trace-defect average) and a small-field region
\[
K:=\{U\in M_\Lambda:\mathcal B_\Lambda(U)\le\varepsilon\}
\]
for a fixed threshold $\varepsilon>0$.

Write $\mu_K$ for the conditional measure $\mu_\Lambda(\cdot\mid K)$.

### Module A: Matrix-hinge restricted Poincaré inequality
The project’s *matrix hinge* mechanism is the statement that on $K$ the action has enough curvature/convexity in the **horizontal directions** (transverse to gauge) to yield
\[
\mathrm{Var}_{\mu_K}(f)\le C_{\mathrm{hinge}}\int_K |\nabla f|^2\,\mathrm d\mu_K.
\]
The point is not the exact constant, but the **volume-independence** (no $|\Lambda|$ blow-up).

*(Project sources: the Bakry–Émery curvature matrix development and hinge bookkeeping live in the “Bochner/\(\Gamma_2\)” and “Vacuum linearization” modules.)*

---

## 3. Covariance as a resolvent: Helffer–Sjöstrand representation
For local observables $F,G$ (cylinder functions), the Helffer–Sjöstrand (HS) representation expresses covariance under $\mu_K$ as a quadratic form of an inverse 1-form operator:
\[
\mathrm{Cov}_{\mu_K}(F,G)
\;=\;
\big\langle \mathrm dF,\; \mathcal L^{-1}\,\mathrm dG\big\rangle_{L^2(\mu_K)}
\]
with $\mathcal L$ a Witten-type operator on 1-forms.

In this project, the key refinement is that after restricting to **horizontal** 1-forms the effective operator becomes a “massive Maxwell-type” operator with strictly finite range.

*(Project sources: HS formalism and horizontal restriction live in the covariance/Maxwell modules; see also the notation ledger.)*

---

## 4. Finite range inverse decay: Combes–Thomas conjugation
### Module B: Abstract Combes–Thomas lemma
Let $M$ be a positive, self-adjoint operator on an $\ell^2$-type space over lattice links/forms, with **finite range** $R$ (matrix elements vanish beyond distance $R$). Assume a spectral gap $M\ge\lambda\,\mathrm{Id}$.

Then for suitable weights $e^{\alpha\,\mathrm{dist}(\cdot,\cdot)}$ one obtains exponential off-diagonal decay of the inverse kernel:
\[
\bigl|(M^{-1})(x,y)\bigr|\ \lesssim\ e^{-m\,\mathrm{dist}(x,y)}.
\]
The proof is the Combes–Thomas conjugation argument: conjugate $M$ by an exponential weight, control the commutator error using finite range, and invert using the spectral gap.

*(Project source: the abstract finite-range inverse decay lemma via Combes–Thomas conjugation.)*

---

## 5. Exponential clustering on $K$
Combining Module A (restricted Poincaré on $K$) + HS representation + Module B (Combes–Thomas decay of $\mathcal L^{-1}$) yields:

> **Clustering on the good set.** For local $F,G$ with separated supports,
> \[
> \bigl|\mathrm{Cov}_{\mu_K}(F,G)\bigr|\ \le\ C(F,G)\,e^{-m\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}
> \]
> with constants uniform in lattice volume.

The structural content is: **finite-range + spectral gap ⇒ inverse kernel decays ⇒ correlations decay**.

*(Project source: “Exponential clustering at fixed cutoff statement” + Combes–Thomas lemma.)*

---

## 6. From good-set clustering to an OS Hamiltonian gap
### What is already clean
If one has exponential decay in Euclidean time (not merely spatial distance) for the full (or suitably controlled) Euclidean measure, then standard OS reconstruction gives a Hamiltonian $H_a$ with
\[
\mathrm{gap}(H_a)\ \gtrsim\ \frac{\eta(a)}{a},
\]
where $\eta(a)$ is the dimensionless Euclidean decay rate.

### What remains as an interface
To upgrade clustering under $\mu_K$ to clustering under the full $\mu_\Lambda$, one needs a **localization/typicality** module that controls the covariance contribution from $K^c$ and the mixing term across the boundary.

This is exactly where the project isolates “gluing” and “coercivity/typicality” hypotheses.

---

## 7. Why this engine is exciting
This fixed-cutoff pipeline is more general than Yang–Mills:

- The HS+Combes–Thomas mechanism is a blueprint for proving **exponential clustering** from **functional inequalities** and **finite-range inverse decay**.
- The abstract Combes–Thomas lemma is reusable for any lattice operator with finite interaction range.
- The horizontal-restriction idea is a geometric way to remove gauge-degeneracies while keeping locality.

If you want “one module to generalize first,” generalize the Combes–Thomas inverse-decay lemma and the HS-to-Maxwell reduction to other compact Lie groups and other lattice gauge actions.
