# Hyperbolicity and Causality of the Vacuum Stiffness Scalar Sector

## Purpose and scope

This document isolates the causal-structure result for the covariant stiffness scalar: the linearized equation about any physical background is **strictly hyperbolic** with a Lorentzian effective characteristic metric, and its characteristic speed remains **subluminal**.

This closes a common loophole in k-essence–type models, where superluminal cones or elliptic regions can occur.

---

## Covariant scalar equation

Let \(\phi\) be a scalar with Lagrangian density depending on
\[
X:=\frac{g^{\mu\nu}\nabla_\mu\phi\,\nabla_\nu\phi}{a_0^2}.
\]
The field equation is
\[
\nabla_\mu\left(F'(X)\nabla^\mu\phi\right)=0.
\]
Define
\[
K(X):=F'(X),\qquad K'(X):=F''(X).
\]

For the vacuum stiffness constitutive law,
\[
K(X)=1-e^{-\sqrt{X}},\qquad
K'(X)=\frac{e^{-\sqrt{X}}}{2\sqrt{X}}\quad(X>0).
\]

---

## Linearization and principal symbol

Linearize about a background \(\phi_0\):
\[
\phi = \phi_0 + \varepsilon\,\varphi,\qquad 0<\varepsilon\ll 1,
\]
and define
\[
u_\mu:=\nabla_\mu\phi_0,\qquad
X_0:=\frac{g^{\mu\nu}u_\mu u_\nu}{a_0^2}.
\]

The principal part of the linearized operator is
\[
\left[
K(X_0)g^{\mu\nu}
+\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu
\right]\nabla_\mu\nabla_\nu\varphi.
\]

Define the effective inverse metric
\[
\boxed{
G^{\mu\nu}_{\rm eff}
:=
K(X_0)g^{\mu\nu}
+\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu.
}
\]
Characteristics satisfy
\[
G^{\mu\nu}_{\rm eff}\,\xi_\mu\xi_\nu=0.
\]

---

## Hyperbolicity conditions

The linearized equation is hyperbolic iff \(G^{\mu\nu}_{\rm eff}\) has Lorentzian signature. This reduces to the algebraic conditions
\[
K(X_0)>0,
\qquad
K(X_0)+2X_0K'(X_0)>0.
\]

For \(K(X)=1-e^{-\sqrt{X}}\),
\[
K(X)>0,\quad K'(X)>0\quad(X>0),
\]
and
\[
K(X)+2XK'(X)
=
1-e^{-\sqrt{X}}+\sqrt{X}e^{-\sqrt{X}}
=
1-e^{-\sqrt{X}}(1-\sqrt{X})>0.
\]

Thus
\[
\boxed{
G^{\mu\nu}_{\rm eff}\text{ is Lorentzian for all physical backgrounds.}
}
\]

---

## Characteristic speed bounds

In a local inertial frame where the background gradient is timelike,
\[
u^\mu=(\dot\phi_0,0,0,0),
\]
one finds
\[
G^{00}_{\rm eff}=-(K+2XK'),\qquad
G^{ij}_{\rm eff}=K\,\delta^{ij}.
\]

Hence the squared characteristic speed is
\[
\boxed{
c_s^2 = \frac{K(X_0)}{K(X_0)+2X_0K'(X_0)}.
}
\]

- Weak-field limit \(X_0\ll 1\): \(K\simeq\sqrt{X}\), \(K'\simeq (2\sqrt{X})^{-1}\), so
  \[
  c_s^2\to\tfrac12.
  \]

- Strong-field limit \(X_0\gg 1\): \(K\to 1\), \(K'\to 0\), so
  \[
  c_s^2\to 1.
  \]

Therefore
\[
\boxed{
\tfrac12 \le c_s^2 < 1
\quad\text{for all physical backgrounds.}
}
\]

**Consequences.** No elliptic regions, no gradient instabilities, no superluminal propagation in the scalar sector.

---

## Why this is structurally valuable

In many nonlinear scalar-gravity theories, changing the kinetic structure can introduce superluminal cones or ill-posed regions. Here the exponential constitutive law enforces positivity of both \(K\) and \(K+2XK'\), producing strict hyperbolicity and subluminal propagation across regimes.
