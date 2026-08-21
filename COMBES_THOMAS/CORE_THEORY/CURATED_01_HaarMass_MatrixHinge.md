# Haar mass and the matrix hinge inequality on lattice Yang–Mills

## Overview

This note isolates a geometric mechanism that is unusually *clean* in lattice gauge theory:

- the **Ricci curvature** of the compact gauge group \(G\) (with its bi-invariant metric) contributes a **uniform positive term** in the Bakry–Émery curvature,
- while the Wilson action contributes a **discrete Maxwell operator** \(d_1^\*d_1\) at the vacuum,
- and a small-field condition controls the nonlinear remainder.

The outcome is a *matrix hinge inequality*:
\[
\mathcal H_\Lambda(U)\ \succeq\ m_{\mathrm H}^2\,I\ +\ \alpha\, d_1^\*d_1,
\qquad U\in K_\Lambda(r),
\]
with constants independent of the volume \(|\Lambda|\).

This lower bound is a key input for Helffer–Sjöstrand covariance representations and Combes–Thomas decay.

---

## 1. Setup

Let \(G\) be a compact Lie group (for the project: \(G=\mathrm{SU}(2)\) or \(\mathrm{SU}(N)\)).
Fix a faithful unitary representation \(\rho\) and define the plaquette energy
\[
\vartheta(g)\ :=\ 1-\frac1n\Re\operatorname{Tr}(\rho(g)),
\qquad 0\le \vartheta\le 2.
\]

Let \(\Lambda\subset\mathbb Z^d\) be a finite periodic lattice.
Write \(E(\Lambda)\) for oriented links, \(P(\Lambda)\) for plaquettes.
A configuration is \(U\in G^{E(\Lambda)}\).
For each plaquette \(p\), let \(U_p(U)\in G\) be the ordered product around \(p\).

The Wilson action is
\[
S_\Lambda(U)\ :=\ \beta \sum_{p\in P(\Lambda)} \vartheta(U_p(U)).
\]

### Riemannian structure and gradients

Equip each factor \(G\) with the bi-invariant Riemannian metric induced by \(-\operatorname{Tr}\) on \(\mathfrak g\).
The product manifold \(M_\Lambda:=G^{E(\Lambda)}\) carries the product metric.
Write \(\nabla\) for the Riemannian gradient on \(M_\Lambda\), and \(\nabla_\ell\) for the component at a link \(\ell\in E(\Lambda)\).

---

## 2. Bakry–Émery curvature matrix and “Haar mass”

For the Gibbs measure
\[
\mu_{\Lambda,\beta}(dU)\ \propto\ e^{-S_\Lambda(U)}\,dU,
\]
the Bakry–Émery carré du champ calculus yields a curvature term acting on gradients,
\[
\mathrm{Ric}_{M_\Lambda}\ +\ \mathrm{Hess}\,S_\Lambda(U).
\]

### Definition (curvature matrix)

Define the (matrix-valued) Bakry–Émery curvature operator on 1-forms / gradients:
\[
\mathcal H_\Lambda(U)\ :=\ \mathrm{Ric}_{M_\Lambda}\ +\ \mathrm{Hess}\,S_\Lambda(U).
\]

Because \(M_\Lambda\) is a product of compact Lie groups with a bi-invariant metric, its Ricci tensor is a positive multiple of the identity in each tangent space:
\[
\mathrm{Ric}_{M_\Lambda}\ \succeq\ c_{\mathrm H}\,I,
\]
where \(c_{\mathrm H}>0\) depends only on \(G\) and the normalization of the metric, **not** on \(\Lambda\) and **not** on \(\beta\).

This constant is the project’s **Haar mass** source: it is a uniform positivity that comes from the geometry of the Haar measure on \(G\), not from the action.

---

## 3. Vacuum Hessian and the discrete Maxwell operator

Let \(U^\star\) denote the vacuum configuration (all links equal to the identity).
A standard linearization of the plaquette map around \(U^\star\) yields that the Hessian of the Wilson action at the vacuum has the discrete Maxwell form:
\[
\mathrm{Hess}\,S_\Lambda(U^\star)\ =\ \beta\,\mathsf M_\Lambda,
\qquad
\mathsf M_\Lambda \approx d_1^\*d_1,
\]
where \(d_1\) is the lattice coboundary (1-cochains \(\to\) 2-cochains) and \(d_1^\*\) its adjoint.
Up to conventional normalization constants (depending only on \(d\) and the choice of metric), this is the usual quadratic Yang–Mills action.

For the rest of this note, fix a normalization constant \(c_{\mathrm M}>0\) such that
\[
\mathsf M_\Lambda\ \succeq\ c_{\mathrm M}\, d_1^\*d_1.
\]

---

## 4. Small-field region and nonlinear remainder control

Let \(z_p(U):=d_G(U_p(U),e)\), where \(d_G\) is the Riemannian distance on \(G\), and define the small-field event
\[
K_\Lambda(r)\ :=\ \bigl\{U:\ z_p(U)\le r\ \text{for all}\ p\in P(\Lambda)\bigr\}.
\]

On \(K_\Lambda(r)\), smoothness of \(\vartheta\) and the plaquette map implies a uniform Taylor remainder bound: there is a function \(R_W(r)\to 0\) as \(r\downarrow 0\) such that
\[
\mathrm{Hess}\,S_\Lambda(U)
\ \succeq\
\mathrm{Hess}\,S_\Lambda(U^\star)\ -\ \beta\,R_W(r)\,I,
\qquad U\in K_\Lambda(r).
\]
All constants implicit in this bound depend only on \(G,d,\rho\), not on \(\Lambda\).

---

## 5. Matrix hinge inequality

### Lemma (matrix hinge)

Fix \(r>0\) so small that
\[
\beta\,R_W(r)\ \le\ \frac12\,c_{\mathrm H}.
\]
Then for every finite periodic lattice \(\Lambda\) and every \(U\in K_\Lambda(r)\),
\[
\boxed{
\mathcal H_\Lambda(U)\ \succeq\ m_{\mathrm H}^2\,I\ +\ \alpha\,d_1^\*d_1,
}
\]
where one may take
\[
m_{\mathrm H}^2:=\frac12\,c_{\mathrm H},
\qquad
\alpha:=\beta\,c_{\mathrm M}.
\]

#### Proof

For \(U\in K_\Lambda(r)\),
\[
\mathcal H_\Lambda(U)
=
\mathrm{Ric}_{M_\Lambda}\ +\ \mathrm{Hess}\,S_\Lambda(U)
\ \succeq\
c_{\mathrm H} I\ +\ \Bigl(\mathrm{Hess}\,S_\Lambda(U^\star)-\beta R_W(r)I\Bigr).
\]
By the choice of \(r\), \(c_{\mathrm H}I-\beta R_W(r)I\succeq \tfrac12 c_{\mathrm H}I\).
Also \(\mathrm{Hess}\,S_\Lambda(U^\star)=\beta\mathsf M_\Lambda\succeq \beta c_{\mathrm M} d_1^\*d_1\).
Putting these together gives
\[
\mathcal H_\Lambda(U)
\ \succeq\
\frac12 c_{\mathrm H}I\ +\ \beta c_{\mathrm M}\, d_1^\*d_1,
\]
which is the claimed bound. \(\square\)

---

## 6. Why this is exciting

1. **Uniformity in volume.** No constant depends on \(|\Lambda|\). This is the correct scale for a mass-gap mechanism.

2. **Geometric origin of mass.** The scalar term \(m_{\mathrm H}^2 I\) comes from \(\mathrm{Ric}_{M_\Lambda}\), i.e. from the Haar geometry of \(G\). This is conceptually different from “adding a mass term by hand”.

3. **A flexible pattern.** The same mechanism should apply to other compact target manifolds and other lattice actions where (i) a vacuum Hessian identifies a discrete elliptic operator and (ii) the geometry supplies a uniform Ricci floor.

---

## 7. Next technical steps

To turn this hinge inequality into distance-decay of correlations, one combines:

- Helffer–Sjöstrand covariance representation (a resolvent of \(\mathcal H_\Lambda(U)\) acting on gradients),
- Combes–Thomas conjugation to obtain exponential decay of the inverse of \(m_{\mathrm H}^2 I+\alpha d_1^\*d_1\) on the link graph.

Those are isolated in separate notes in this curated bundle.
