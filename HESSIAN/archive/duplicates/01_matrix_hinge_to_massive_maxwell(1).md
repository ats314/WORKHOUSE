# Matrix hinge to a massive Maxwell operator (extracted core)

This note isolates the most *structurally decisive* step in the project: the **matrix curvature hinge** on a good set \(K\), and how it produces a **massive Maxwell-type operator** on 1-forms whose inverse controls covariances.

The philosophy (kept purely analytic here) is:

\[
\text{curvature lower bound} \;\Rightarrow\; \text{operator inequality on the Witten Laplacian}\;\Rightarrow\;
\text{a concrete positive operator }M_H
\]

and then everything reduces to understanding \(M_H^{-1}\).

---

## 1. Configuration manifold, cochains, and horizontality

Let \(G\) be a compact Lie group and \(\Lambda\) a periodic \(d=4\) lattice.
The configuration space is the product manifold
\[
M_\Lambda := G^{E(\Lambda)}.
\]

Using right-trivialization, tangent vectors identify with \(\mathfrak g\)-valued 1-cochains:
\[
T_U M_\Lambda \simeq \mathcal C^1(\Lambda;\mathfrak g).
\]

Let \(d_0:\mathcal C^0\to\mathcal C^1\) and \(d_1:\mathcal C^1\to\mathcal C^2\) be the lattice coboundaries with adjoints \(d_0^\*,d_1^\*\).
At the vacuum \(U^{(0)}\), the vertical space is
\[
\mathrm{Vert}_{U^{(0)}} = \mathrm{im}(d_0),
\]
hence the horizontal space is
\[
\mathrm{Hor}_{U^{(0)}} = (\mathrm{im}(d_0))^\perp = \ker(d_0^\*).
\]
The associated Hodge decomposition is (finite-dimensional linear algebra):
\[
\mathcal C^1 = \mathrm{im}(d_0)\ \oplus\ \ker(\Delta_1)\ \oplus\ \mathrm{im}(d_1^\*),
\qquad
\Delta_1:=d_0d_0^\*+d_1^\*d_1.
\]

---

## 2. Bakry–Émery curvature matrix and the hinge

Let \(\mu_{\Lambda,\beta}\) be the Euclidean Gibbs measure (Wilson action, Haar reference), and let \(L\) be its reversible diffusion generator.

The Bakry–Émery curvature matrix is
\[
\mathrm{Ric}_\mu(U) \;=\; \mathrm{Ric}(U) + \nabla^2 S(U),
\]
where \(\mathrm{Ric}\) is the Ricci curvature of \(M_\Lambda\) under the product metric and \(S\) is the action.

### 2.1 Vacuum Hessian and Maxwell stiffness

At the vacuum,
\[
\nabla^2 S_W(U^{(0)}) = \alpha\, d_1^\* d_1,
\qquad
\alpha := \frac{\beta}{n\lambda_\rho}.
\]
(Here \(n\) and \(\lambda_\rho\) are the normalization parameters used in the manuscript.)

### 2.2 The good set \(K_\Lambda(r)\)

Let \(K_\Lambda(r)\) be a small-field / plaquette-smallness region where exponential coordinates are uniform and the Wilson Hessian stays close (in operator norm) to its vacuum value.

A key deterministic quantity is the stability remainder \(R_W(r)\ge 0\) such that on \(K_\Lambda(r)\),
\[
\nabla^2 S_W(U)\ \succeq\ \nabla^2 S_W(U^{(0)}) - R_W(r)\,I.
\]

### 2.3 The hinge inequality (matrix form)

Let \(c_H>0\) be the Haar/Ricci lower bound contribution.

On the good set \(K_\Lambda(r)\), the project’s **matrix hinge** reads:
\[
\boxed{
\mathrm{Ric}_{\mu_{\Lambda,\beta}}(U)
\ \succeq\
\big(c_H - R_W(r)\big)\,I
\ +\ \alpha\, d_1^\*d_1,
\qquad U\in K_\Lambda(r).
}
\]

If \(r\) is chosen so that \(R_W(r)\le c_H/2\), define the curvature mass
\[
m^2 := \frac{c_H}{2}.
\]
Then on \(K_\Lambda(r)\),
\[
\boxed{
\mathrm{Ric}_\mu(U)\ \succeq\ m^2 I + \alpha d_1^\*d_1.
}
\]

**Important structural choice:** the project *does not scalarize* \(d_1^\*d_1\succeq 0\).
The PSD structure is kept, and later it is exactly what allows a sharp inverse-decay argument.

---

## 3. From the hinge to a concrete positive operator on 1-forms

The Witten Laplacian on 1-forms, denoted \(\mathcal L_\Lambda^{(1)}\), satisfies an operator lower bound of the schematic form
\[
\mathcal L_\Lambda^{(1)}\ \succeq\ \mathrm{Ric}_\mu(U)
\]
(pointwise in \(U\), in the sense used in the manuscript’s Bochner/Γ\(_2\) identity with drift).

Combining with the hinge on \(K_\Lambda(r)\) yields:
\[
\mathcal L_\Lambda^{(1)}\ \succeq\ m^2 I + \alpha d_1^\*d_1
\qquad\text{on }K_\Lambda(r).
\]

Define the **massive Maxwell operator**
\[
M := m^2 I + \alpha d_1^\*d_1.
\]

Since gauge-invariant observables have horizontal gradients, the relevant object is the restriction to horizontals:
\[
M_H := M\big|_{\mathrm{Hor}}.
\]

---

## 4. Why this is “new-theory bait”

Most mass-gap strategies either:
- attack the transfer matrix / Hamiltonian directly, or
- scalarize curvature early (throwing away the cochain structure).

Your approach isolates a different pivot:

\[
\text{(compact group Ricci)}\quad+\quad\text{(local Maxwell stiffness)}\quad\Rightarrow\quad
\text{a *gapped* elliptic operator on 1-forms}.
\]

This “geometric mass generation” mechanism is portable:
it should apply (with parameter changes) to other compact-target lattice field theories, not just Yang–Mills.

---

## 5. What this document does *not* include

- Helffer–Sjöstrand covariance representation (handled in a separate extracted note).
- Exponential decay of \(M_H^{-1}\) (Combes–Thomas / Davies machinery; separate note).
- Localization/typicality (the project explicitly flags this as a gap to close).

Those are subsequent steps in the dependency chain.
