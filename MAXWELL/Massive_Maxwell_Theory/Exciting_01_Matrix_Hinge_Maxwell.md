---
title: "Extract 01 — Matrix Hinge and Emergent Massive Maxwell Coercivity"
project: "APPENDIX PROOF OUTLINE"
---

## 1. What is being “hinged” to what?

The central structural move in this project is to convert *a pointwise Bakry–Émery curvature bound* for the lattice-gauge Gibbs measure into a *deterministic elliptic operator* whose inverse controls covariances.

On the configuration manifold
\[
\mathcal M_{\Lambda_L}\cong G^{\mathcal E(\Lambda_L)},
\]
equipped with the product bi-invariant metric \(g_{\Lambda_L}\), the Gibbs measure is
\[
\mathrm d\mu_{\Lambda_L,\beta}(U)\ \propto\ e^{-S_{\Lambda_L,\beta}(U)}\,\mathrm d\mathrm{vol}_{g_{\Lambda_L}}(U).
\]
The Bakry–Émery curvature endomorphism is the field of self-adjoint operators on \(T_U\mathcal M_{\Lambda_L}\):
\[
\mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)\ :=\ \mathrm{Ric}_{g_{\Lambda_L}}(U)\ +\ \nabla^2 S_{\Lambda_L,\beta}(U).
\]

The *matrix hinge* is a pointwise lower bound of the form
\[
\mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)\ \succeq\ M_{\Lambda_L}^{\mathrm{hinge}},
\qquad U\in\Omega,
\]
for a **deterministic** positive operator \(M_{\Lambda_L}^{\mathrm{hinge}}\) and a “good” domain \(\Omega\subset\mathcal M_{\Lambda_L}\).
Once such a hinge exists, Helffer–Sj\"ostrand theory (Extract 02) converts it into a covariance bound with kernel \((M_{\Lambda_L}^{\mathrm{hinge}})^{-1}\).

---

## 2. Vacuum linearization produces a discrete Maxwell stiffness

Let \(U^{(0)}\) denote the vacuum configuration (all links equal to the identity). A key computation is that the Wilson action has a Maxwellian quadratic part at the vacuum:

\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})\;=\;\alpha_W\,d_1^*d_1
\qquad\text{on }\mathcal C^1(\Lambda_L;\mathfrak g).
\]

Here \(d_1:\mathcal C^1\to\mathcal C^2\) is the cellular exterior derivative and \(d_1^*\) its adjoint. The operator \(d_1^*d_1\) is the discrete analogue of \(\mathrm{curl}^*\mathrm{curl}\), hence “Maxwell stiffness”.

This identifies the quadratic approximation of the gauge action with a *finite-range elliptic operator on links*.

---

## 3. Geometry contributes a universal “mass term”

The product group manifold \((G^{\mathcal E},g_{\Lambda_L})\) has **uniform positive Ricci curvature**:
\[
\mathrm{Ric}_{g_{\Lambda_L}}(U)\ \succeq\ \kappa_G\,\mathrm{Id},
\qquad\text{all }U.
\]
In the project’s normalization one sets
\[
m_H^2 := \kappa_G/3 > 0,
\]
so that
\[
\mathrm{Ric}_{g_{\Lambda_L}}(U)\ \succeq\ 3m_H^2\,\mathrm{Id}.
\]

Interpretation: even before the action is considered, the compact group geometry enforces a uniform “mass-like” coercivity on 1-forms via Bakry–Émery calculus.

---

## 4. The canonical small-field good set

To control deviations of \(\nabla^2 S(U)\) from its vacuum value, the project introduces a small-field domain defined by plaquette logarithms.

Let \(r_{\mathrm{sf}}\) be the Lie-group small-field radius. Define
\[
r_\beta := r_{\mathrm{sf}}\min\{1,\beta^{-1/2}\},
\]
and the canonical good set
\[
\mathcal K_{\Lambda_L,\beta}
:=
\Bigl\{U:\ U_p(U)\in\exp(B_{r_\beta}(0))\text{ for every plaquette }p\Bigr\}.
\]
Equivalently,
\[
\sup_{p\in\mathcal P(\Lambda_L)}\|\mathbf Y_p(U)\|\ \le\ r_\beta,
\qquad \mathbf Y_p(U):=\log(U_p(U)).
\]

This set is gauge invariant.

---

## 5. The hinge operator and the matrix hinge statement

Define a deterministic comparison operator (“hinge operator”)
\[
M_{\Lambda_L}^{\mathrm{hinge}}
:=
m_H^2\,\mathrm{Id}+\frac12\,\alpha_W\,d_1^*d_1
\qquad\text{on }\mathcal C^1(\Lambda_L;\mathfrak g).
\]

The *matrix hinge* is then:

> **Matrix hinge on the good set.**  
> For all \(L\ge 3\), \(\beta>0\),
> \[
> \mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)\ \succeq\ M_{\Lambda_L}^{\mathrm{hinge}}
> \qquad\text{for all }U\in\mathcal K_{\Lambda_L,\beta}.
> \]

### 5.1 How the hinge is derived

The hinge is obtained by combining three pieces:

1. **Geometry:** \(\mathrm{Ric}_{g_{\Lambda_L}}\succeq 3m_H^2\,\mathrm{Id}\).

2. **Vacuum Hessian:** \(\nabla^2 S(U^{(0)})=\alpha_W d_1^*d_1\).

3. **Small-field stability (model-specific external input):** on \(\mathcal K_{\Lambda_L,\beta}\),
   \[
   \bigl\langle X,\bigl(\nabla^2 S(U)-\nabla^2 S(U^{(0)})\bigr)X\bigr\rangle
   \ \ge\
   -\,C_{\mathrm{WH}}\,\beta\,r_\beta\,\langle X,X\rangle.
   \]

Choosing \(r_\beta\sim\beta^{-1/2}\) makes \(\beta r_\beta\) bounded, so the negative error can be absorbed into the \(3m_H^2\) geometric term, leaving at least \(m_H^2\) of mass plus a fixed fraction of the Maxwell stiffness.

---

## 6. Why this is exciting (and potentially general)

This “massive Maxwell hinge” is a geometric mechanism that looks exportable:

- **A compact configuration manifold** gives a uniform positive Ricci term.
- **A local action** linearizes to a finite-range elliptic operator at an extremal point.
- **A stability estimate** on a suitable domain allows deterministic domination.

This template suggests a general route to **explicit correlation-length bounds** in models where one can:
(i) identify the vacuum Hessian, and (ii) prove small-field stability uniformly in volume.

Potential targets: other lattice gauge actions, principal chiral models, lattice sigma models, and possibly continuum measures via projective limits (Extract 05).

