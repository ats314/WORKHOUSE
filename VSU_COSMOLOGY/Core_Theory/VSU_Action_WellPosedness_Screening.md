---
title: "Vacuum Stiffness Scalar Theory"
subtitle: "Action, field equation, hyperbolicity, and intrinsic screening"
status: "Referee-safe synthesis of the project’s core field-theory pieces"
---

# Vacuum Stiffness Scalar Theory
## Action, PDE structure, and regime control

### Abstract
This document extracts the most “physics-facing” technical core of the Vacuum Stiffness Unification (VSU) framework:
1) the **AQUAL-type action** and the resulting quasilinear elliptic field equation in the nonrelativistic limit,  
2) a **covariant k-essence completion** used to discuss stability/hyperbolicity, and  
3) the **intrinsic screening** mechanism (operator saturation) that recovers the Newtonian/GR regime at high acceleration.

The emphasis is on **well-posedness and regime control**, not on interpretive claims.

---

# 1. Nonrelativistic action and field equation (AQUAL sector)

## 1.1 Action
Let \(\Phi\) be the gravitational potential sourced by matter density \(\rho\).
Introduce the dimensionless invariant
\[
Y := \frac{|\nabla\Phi|^2}{a_0^2}.
\]
The AQUAL-type action is
\[
S_{\rm AQUAL}[\Phi]
=
-\frac{a_0^2}{8\pi G}\int_{\mathbb R^3} F(Y)\,d^3x
\;-\;
\int_{\mathbb R^3}\rho\,\Phi\,d^3x.
\]

## 1.2 Constitutive law (the “stiffness” function)
Define
\[
\mu(s) := 1-e^{-s},\qquad s:=\sqrt{Y}=\frac{|\nabla\Phi|}{a_0},
\]
and take
\[
F'(Y)=\mu(\sqrt{Y}).
\]
(Equivalently: \(F\) is an explicit primitive of \(1-e^{-\sqrt{Y}}\).)

## 1.3 Euler–Lagrange equation
Varying \(S_{\rm AQUAL}\) yields the quasilinear elliptic PDE
\[
\nabla\cdot\big(\mu(|\nabla\Phi|/a_0)\,\nabla\Phi\big)=4\pi G\rho.
\]

This is the operational definition of the “stiffness”: the operator’s coefficients depend on \(|\nabla\Phi|\).

---

# 2. Regimes and intrinsic screening (nonlinear operator saturation)

## 2.1 High-acceleration (saturated) regime
If \(s=|\nabla\Phi|/a_0\gg 1\), then \(\mu(s)\to 1\), so the equation reduces to
\[
\nabla^2\Phi \approx 4\pi G\rho,
\]
i.e. standard Poisson gravity.

This is “intrinsic screening”: no extra field is required to turn the modification off.

## 2.2 Low-acceleration (unsaturated) regime
If \(s\ll 1\), then \(\mu(s)\sim s\), and the operator reduces to the deep-MOND type scaling.
For spherical symmetry, one gets the usual algebraic relation
\[
g\,\mu(g/a_0)=g_N
\quad\Rightarrow\quad
g\sim \sqrt{a_0\,g_N}\quad(s\ll 1),
\]
where \(g=|\nabla\Phi|\) and \(g_N\) is the Newtonian field.

## 2.3 Characteristic transition radius
For an isolated mass \(M\), define
\[
r_s := \sqrt{\frac{GM}{a_0}}.
\]
At \(r\ll r_s\) one is typically in the saturated regime; at \(r\gg r_s\), in the unsaturated regime.
This is a diagnostic transition scale, not an added parameter.

## 2.4 Environmental dependence (EFE) as boundary-condition physics
Because the operator is nonlinear (superposition fails), internal solutions depend on asymptotic boundary conditions.
If a subsystem is embedded in a background external field \(\nabla\Phi_{\rm ext}\), one imposes
\[
\nabla\Phi(x)\to \nabla\Phi_{\rm ext}\quad (|x|\to\infty).
\]
Linearizing around a background where \(|\nabla\Phi_{\rm ext}|/a_0\gg 1\) produces an *effective* Poisson equation for internal perturbations—hence suppression of low-acceleration anomalies in strong environments.

---

# 3. Covariant completion and hyperbolicity (k-essence sector)

## 3.1 Covariant action
Introduce a scalar field \(\phi\) and the invariant
\[
X:= -\frac{1}{2}g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi.
\]
A covariant k-essence action is
\[
S[\phi,g]
=
\int d^4x\,\sqrt{-g}\,K(X)
\;+\;S_{\rm m}[g,\Psi],
\]
with a choice \(K\) engineered so that the weak-field, quasi-static limit reproduces the AQUAL constitutive relation.

## 3.2 Field equation and principal symbol
The k-essence field equation is
\[
\nabla_\mu\big(K_X\,\nabla^\mu\phi\big)=0,
\]
with principal symbol governed by the effective metric
\[
G^{\mu\nu} = K_X\,g^{\mu\nu} + K_{XX}\,\nabla^\mu\phi\,\nabla^\nu\phi.
\]

Hyperbolicity and well-posedness require:
- **no ghost:** \(K_X>0\),
- **gradient stability:** \(c_s^2>0\), where
\[
c_s^2=\frac{K_X}{K_X+2XK_{XX}}.
\]

## 3.3 Characteristic speeds for the chosen \(K(X)\)
The project computes explicit \(c_s^2\) behavior for the adopted constitutive choice, and shows a stable range \(0<c_s^2<1\) with controlled limits in the “deep” and “saturated” regimes.

---

# 4. What looks technically strong here
The most solid pieces (in referee terms) are:
- a clean variational principle for the nonrelativistic PDE,
- explicit regime limits showing recovery of Poisson/GR at high acceleration,
- an explicit hyperbolicity analysis in the covariant completion.

These are the ingredients that make “screening without auxiliary sectors” mathematically meaningful: the nonlinearity itself is the screen.

---

# Dependencies in the project
Extracted primarily from:
- `01.1_Action_and_Field_Equations.md`
- `01.3_Hyperbolicity_and_Characteristics.md`
- `05.1_Nonlinear_Screening_Mechanism.md`
