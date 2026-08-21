# BEST_03 — Effective Metric / Hyperbolicity for the Scalar Sector (and the Sign-Domain Tension)

## 1. Scalar equation and constitutive functions (project definition)

The scalar equation used in the project is
\[
\nabla_\mu\!\left(F'(X)\nabla^\mu\phi\right)=0,
\qquad
X:=\frac{g^{\mu\nu}\nabla_\mu\phi\,\nabla_\nu\phi}{a_0^2}.
\]

The project notation in `01.3_Hyperbolicity_and_Characteristics.md` sets
\[
K(X):=F'(X),\qquad K'(X):=F''(X).
\]

For the constitutive choice (as written there),
\[
K(X)=1-e^{-\sqrt{X}},
\qquad
K'(X)=\frac{e^{-\sqrt{X}}}{2\sqrt{X}}
\quad (X>0).
\]

---

## 2. Principal part and effective inverse metric (as derived in `01.3`)

Linearize \(\phi=\phi_0+\varepsilon\varphi\) and define \(u_\mu:=\nabla_\mu\phi_0\), \(X_0:=g^{\mu\nu}u_\mu u_\nu/a_0^2\).

The principal (second-derivative) part of the linearized operator is
\[
\mathcal P(\varphi)=
\left[
K(X_0)g^{\mu\nu}
+
\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu
\right]\nabla_\mu\nabla_\nu\varphi
+\text{(lower order)}.
\]

This defines the **effective inverse metric**
\[
\boxed{
G^{\mu\nu}_{\rm eff}
=
K(X_0)g^{\mu\nu}
+
\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu.
}
\]

Characteristic covectors \(\xi_\mu\) satisfy
\[
G^{\mu\nu}_{\rm eff}\,\xi_\mu\xi_\nu=0.
\]

---

## 3. Hyperbolicity conditions stated in the project file

The project file states that strict hyperbolicity follows if
\[
K(X_0)>0,
\qquad
K(X_0)+2X_0K'(X_0)>0.
\]

For \(X_0>0\), it records that \(K>0\), \(K'>0\), and therefore the conditions hold.

---

## 4. Characteristic speed formula (as recorded)

In a local frame with a timelike background gradient \(u^\mu=(\dot\phi_0,0,0,0)\), `01.3` records
\[
c_s^2=\frac{K(X_0)}{K(X_0)+2X_0K'(X_0)}.
\]
and gives limiting values \(c_s^2\to 1/2\) for \(X_0\ll 1\) and \(c_s^2\to 1\) for \(X_0\gg 1\).

---

## 5. The sign-domain tension (why this is still a novelty-relevant “fixpoint”)

The same file simultaneously:

- uses the explicit constitutive expressions \(K(X)=1-e^{-\sqrt{X}}\) and \(K'(X)=e^{-\sqrt{X}}/(2\sqrt{X})\), which are written only for \(X>0\), and
- chooses a **timelike** background gradient \(u^\mu=(\dot\phi_0,0,0,0)\), which for the project’s metric signature conventions implies \(X_0<0\).

This is not an algebraic nitpick: it is a domain mismatch between the constitutive law and the background class used to compute characteristics.

### Minimal consistency options suggested by the project corpus (not resolved inside it)

To make the hyperbolicity/characteristic analysis usable in cosmology, one of the following must be supplied somewhere in the theory stack:

1. a demonstrated restriction to background classes with \(X\ge 0\) in the regimes where the constitutive law is applied, or  
2. an explicit extension of \(F(X)\), \(F'(X)\), \(F''(X)\) to \(X<0\) consistent with the intended dynamics.

These repair options are not carried out in the project files provided; they are “missing bridges”.

---

## Source pointers (project-local)

- `01.3_Hyperbolicity_and_Characteristics.md`: effective metric definition, hyperbolicity inequalities, and recorded \(c_s^2\) limits.
- `03.2_Scalar_Perturbations.md`: uses \(X_0=-\dot\phi_0^2/a_0^2\) in cosmological backgrounds (domain tension with \(X>0\) constitutive expression).
