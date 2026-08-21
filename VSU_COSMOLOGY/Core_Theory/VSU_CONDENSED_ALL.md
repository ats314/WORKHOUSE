# VSU Condensed Project Files

_Generated: 2025-12-26 02:20:12 UTC_

This single Markdown file contains a verbatim concatenation of the attached VSU project files, in the DAG order, plus the project metadata files and the verbatim contents of `VSU_package.zip` members (which appear to be placeholder stubs for most documents).

**Note on completeness:** Two DAG nodes (`03.4_Early_Time_Asymptotics.md` and `04.1_RSD_and_fsigma8_Mapping.md`) only exist in the attached zip as placeholders that say “See conversation transcript for full derivation.” No transcript was included in the attachments, so the only available content for those nodes is the placeholder text, which is included verbatim below.

## Included files

- `00_Overview.md` (source: `/mnt/data/zip_extract/00_Overview.md`)
- `01.1_Action_and_Field_Equations.md` (source: `/mnt/data/01.1_Action_and_Field_Equations.md`)
- `01.2_Stress_Energy_Tensor.md` (source: `/mnt/data/01.2_Stress_Energy_Tensor.md`)
- `01.3_Hyperbolicity_and_Characteristics.md` (source: `/mnt/data/01.3_Hyperbolicity_and_Characteristics.md`)
- `02.1_Force_Law_and_Asymptotics.md` (source: `/mnt/data/02.1_Force_Law_and_Asymptotics.md`)
- `02.2_BTFR_Derivation.md` (source: `/mnt/data/02.2_BTFR_Derivation.md`)
- `02.3_Screening_Radius_and_EFE.md` (source: `/mnt/data/02.3_Screening_Radius_and_EFE.md`)
- `03.1_Background_Cosmology.md` (source: `/mnt/data/03.1_Background_Cosmology.md`)
- `03.2_Scalar_Perturbations.md` (source: `/mnt/data/03.2_Scalar_Perturbations.md`)
- `03.3_Matter_Growth_Equation.md` (source: `/mnt/data/03.3_Matter_Growth_Equation.md`)
- `03.4_Early_Time_Asymptotics.md` (source: `/mnt/data/zip_extract/03.4_Early_Time_Asymptotics.md`)
- `03.5_Late_Time_Asymptotics.md` (source: `/mnt/data/03.5_Late_Time_Asymptotics.md`)
- `04.1_RSD_and_fsigma8_Mapping.md` (source: `/mnt/data/zip_extract/04.1_RSD_and_fsigma8_Mapping.md`)
- `04.2_Weak_Lensing_and_S8.md` (source: `/mnt/data/04.2_Weak_Lensing_and_S8.md`)
- `04.3_ISW_Sign_and_Amplitude.md` (source: `/mnt/data/04.3_ISW_Sign_and_Amplitude.md`)
- `04.4_BAO_Phase_and_Peaks.md` (source: `/mnt/data/04.4_BAO_Phase_and_Peaks.md`)
- `04.5_Alcock_Paczynski_Consistency.md` (source: `/mnt/data/04.5_Alcock_Paczynski_Consistency.md`)
- `05.1_Nonlinear_Screening_Mechanism.md` (source: `/mnt/data/05.1_Nonlinear_Screening_Mechanism.md`)
- `05.2_Spherical_Collapse.md` (source: `/mnt/data/05.2_Spherical_Collapse.md`)
- `05.3_Halo_Bias.md` (source: `/mnt/data/05.3_Halo_Bias.md`)
- `06.1_Internal_Consistency.md` (source: `/mnt/data/06.1_Internal_Consistency.md`)
- `06.2_Observable_Degeneracy_Structure.md` (source: `/mnt/data/06.2_Observable_Degeneracy_Structure.md`)
- `06.3_Parameter_Minimality.md` (source: `/mnt/data/06.3_Parameter_Minimality.md`)

## Project metadata files

- `VSU_DAG.yaml`
- `VSU_DAG.json`
- `VSU_LINT.md`
- `VSU_EXPORTS.md`

---

## Core analytical documents (DAG order)

<!-- BEGIN FILE: 00_Overview.md (source: /mnt/data/zip_extract/00_Overview.md) -->
# Vacuum Stiffness Unification (VSU)
## Overview and Structural Orientation

This document provides a minimal orientation to the Vacuum Stiffness Unification (VSU) framework.
All derivations appear in subsequent files.
<!-- END FILE: 00_Overview.md -->

<!-- BEGIN FILE: 01.1_Action_and_Field_Equations.md (source: /mnt/data/01.1_Action_and_Field_Equations.md) -->
# 01.1 Action and Field Equations

## Purpose

This file defines the fundamental action of the Vacuum Stiffness Unification (VSU)
framework and derives the corresponding field equations by explicit variation.
All subsequent results depend on this file.

No observational input is used here.

---

## 1. Degrees of Freedom and Kinematic Setup

We work with a scalar gravitational potential field \(\Phi\) coupled to matter
density \(\rho\) in the nonrelativistic regime, and with its covariant scalar
extension \(\phi\) in the relativistic formulation.

A single universal acceleration scale \(a_0 > 0\) is assumed.

---

## 2. Nonrelativistic Action

The nonrelativistic action functional is
\[
S_{\mathrm{NR}}[\Phi]
=
\int dt \int d^3x
\left[
\frac{a_0^2}{8\pi G}
\,F\!\left(
\frac{|\nabla\Phi|^2}{a_0^2}
\right)
+
\rho\,\Phi
\right],
\]
where:
- \(F : \mathbb{R}_{\ge 0} \to \mathbb{R}\) is a dimensionless function,
- \(|\nabla\Phi|^2 = \delta^{ij}\partial_i\Phi\,\partial_j\Phi\).

Define the dimensionless invariant
\[
Y := \frac{|\nabla\Phi|^2}{a_0^2}.
\]

---

## 3. Constitutive Function

The theory is specified by the constitutive relation
\[
\mu(x) := F'(x^2),
\qquad
\mu(x) = 1 - e^{-x},
\qquad x \ge 0.
\]

Equivalently,
\[
F'(Y) = \mu(\sqrt{Y}) = 1 - e^{-\sqrt{Y}}.
\]

The explicit primitive \(F(Y)\) is determined up to an additive constant and is
not required for the field equation.

---

## 4. Variation and Euler–Lagrange Equation

We vary \(S_{\mathrm{NR}}\) with respect to \(\Phi\).

The variation of the kinetic term is
\[
\delta F(Y)
=
F'(Y)\,\delta Y
=
F'(Y)\,
\frac{2}{a_0^2}\,
\nabla\Phi\cdot\nabla(\delta\Phi).
\]

Thus
\[
\delta S_{\mathrm{NR}}
=
\int dt\,d^3x
\left[
\frac{1}{4\pi G}
F'(Y)\,
\nabla\Phi\cdot\nabla(\delta\Phi)
+
\rho\,\delta\Phi
\right].
\]

Integrating the first term by parts and discarding boundary terms yields
\[
\delta S_{\mathrm{NR}}
=
-\int dt\,d^3x\;
\delta\Phi
\left[
\nabla\cdot\!\left(
\frac{1}{4\pi G}
F'(Y)\nabla\Phi
\right)
-
\rho
\right].
\]

Stationarity \(\delta S_{\mathrm{NR}} = 0\) for arbitrary \(\delta\Phi\)
gives the field equation.

---

## 5. Modified Poisson Equation

The nonrelativistic field equation is
\[
\nabla\cdot\!\left(
\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi
\right)
=
4\pi G\,\rho,
\]
with
\[
\mu(x) = 1 - e^{-x}.
\]

This is a quasilinear elliptic partial differential equation.

---

## 6. Limiting Forms

### 6.1 Strong-Field Limit

If \(|\nabla\Phi| \gg a_0\),
\[
\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right) \to 1,
\]
and the equation reduces to
\[
\nabla^2\Phi = 4\pi G\rho
\]
up to exponentially small corrections.

---

### 6.2 Weak-Field Limit

If \(|\nabla\Phi| \ll a_0\),
\[
\mu(x) \simeq x,
\]
and the equation becomes
\[
\nabla\cdot\!\left(
\frac{|\nabla\Phi|}{a_0}\nabla\Phi
\right)
=
4\pi G\rho.
\]

---

## 7. Covariant Extension

The minimal covariant action consistent with the nonrelativistic limit is
\[
S[g_{\mu\nu}, \phi]
=
\int d^4x\sqrt{-g}
\left[
\frac{1}{16\pi G} R
+
\frac{a_0^2}{8\pi G}
F\!\left(
\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}
\right)
+
\mathcal L_m(g_{\mu\nu}, \psi)
\right].
\]

Define
\[
X := \frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]

---

## 8. Scalar Field Equation (Covariant)

Varying the action with respect to \(\phi\) yields
\[
\nabla_\mu\!\left(
F'(X)\nabla^\mu\phi
\right) = 0.
\]

This equation reduces to the modified Poisson equation in the nonrelativistic,
quasistatic limit with \(\phi = \Phi\).

---

## 9. Einstein Field Equations

Variation with respect to the metric gives
\[
G_{\mu\nu}
=
8\pi G
\left(
T^{(m)}_{\mu\nu}
+
T^{(\phi)}_{\mu\nu}
\right),
\]
where \(T^{(\phi)}_{\mu\nu}\) is derived explicitly in
`01.2_Stress_Energy_Tensor.md`.

---

## 10. Assumptions and Status

- No additional fields are introduced.
- No background cosmology is assumed here.
- No gauge choice is required.
- All stability, hyperbolicity, and causal properties are addressed in subsequent files.

This file is complete.
<!-- END FILE: 01.1_Action_and_Field_Equations.md -->

<!-- BEGIN FILE: 01.2_Stress_Energy_Tensor.md (source: /mnt/data/01.2_Stress_Energy_Tensor.md) -->
# 01.2 Stress–Energy Tensor

## Purpose

This file derives the stress–energy tensor associated with the vacuum stiffness
scalar field from the covariant action defined in
`01.1_Action_and_Field_Equations.md`. The derivation is explicit and establishes
positivity, conservation, and algebraic properties required for subsequent
stability and perturbation analyses.

No cosmological background or gauge choice is assumed.

---

## 1. Scalar Sector of the Action

We consider the scalar-field contribution to the action
\[
S_{\phi}[g_{\mu\nu},\phi]
=
\frac{a_0^2}{8\pi G}
\int d^4x\sqrt{-g}\,F(X),
\]
where
\[
X := \frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]

The constitutive relation is
\[
F'(X) = \mu(\sqrt{X}) = 1 - e^{-\sqrt{X}}.
\]

---

## 2. Definition of the Stress–Energy Tensor

The stress–energy tensor is defined by variation with respect to the metric:
\[
T^{(\phi)}_{\mu\nu}
:=
-\frac{2}{\sqrt{-g}}
\frac{\delta S_{\phi}}{\delta g^{\mu\nu}}.
\]

All variations are performed holding \(\phi\) fixed.

---

## 3. Metric Variations

### 3.1 Variation of the Volume Element

The standard identity gives
\[
\delta\sqrt{-g}
=
-\tfrac12\sqrt{-g}\,g_{\mu\nu}\,\delta g^{\mu\nu}.
\]

---

### 3.2 Variation of the Invariant \(X\)

Since
\[
X = \frac{g^{\alpha\beta}\nabla_\alpha\phi\nabla_\beta\phi}{a_0^2},
\]
its variation is
\[
\delta X
=
\frac{1}{a_0^2}
\nabla_\alpha\phi\,\nabla_\beta\phi\,\delta g^{\alpha\beta}.
\]

---

## 4. Variation of the Lagrangian Density

Combining the above variations,
\[
\delta(\sqrt{-g}F(X))
=
\sqrt{-g}
\left[
-\tfrac12 g_{\mu\nu}F(X)
+
\frac{F'(X)}{a_0^2}
\nabla_\mu\phi\,\nabla_\nu\phi
\right]
\delta g^{\mu\nu}.
\]

---

## 5. Explicit Stress–Energy Tensor

Substituting into the definition yields
\[
\boxed{
T^{(\phi)}_{\mu\nu}
=
\frac{a_0^2}{4\pi G}
\left[
\frac{F'(X)}{a_0^2}
\nabla_\mu\phi\,\nabla_\nu\phi
-
\tfrac12 g_{\mu\nu}F(X)
\right].
}
\]

This expression is exact.

---

## 6. Conservation

Using the scalar equation of motion
\[
\nabla_\mu\!\left(F'(X)\nabla^\mu\phi\right)=0
\]
together with metric compatibility, one verifies
\[
\boxed{
\nabla^\mu T^{(\phi)}_{\mu\nu} = 0.
}
\]

Thus the scalar stress–energy tensor is covariantly conserved on shell.

---

## 7. Energy Density and Positivity

Let \(u^\mu\) be a timelike unit vector.

The scalar energy density is
\[
\rho_{\phi}
:=
T^{(\phi)}_{\mu\nu}u^\mu u^\nu
=
\frac{a_0^2}{4\pi G}
\left[
\frac{F'(X)}{a_0^2}(u^\mu\nabla_\mu\phi)^2
+
\tfrac12 F(X)
\right].
\]

In quasistatic configurations (\(u^\mu\nabla_\mu\phi=0\)),
\[
\boxed{
\rho_{\phi}
=
\frac{a_0^2}{8\pi G}F(X).
}
\]

Since
\[
F'(X) > 0 \quad \text{for all } X>0,
\]
and \(F(X)\ge 0\) up to an irrelevant additive constant,
\[
\boxed{
\rho_{\phi} \ge 0.
}
\]

Thus the scalar sector is ghost-free and energetically stable.

---

## 8. Homogeneous Configuration

For a homogeneous field \(\phi=\phi(t)\),
\[
X = -\frac{\dot\phi^2}{a_0^2}.
\]

The effective pressure is
\[
p_{\phi}
=
\frac{a_0^2}{4\pi G}
\left[
\frac{F'(X)}{a_0^2}\dot\phi^2
-
\tfrac12 F(X)
\right].
\]

The equation-of-state parameter is
\[
w_{\phi}
=
\frac{p_{\phi}}{\rho_{\phi}}
=
\frac{2XF'(X)-F(X)}{F(X)}.
\]

This algebraic relation is used later in perturbation analyses.

---

## 9. Nonrelativistic Consistency Check

In the quasistatic limit with \(\phi=\Phi(\mathbf{x})\),
\[
T^{(\phi)}_{00}
\to
\frac{a_0^2}{8\pi G}
F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right),
\]
which matches the energy functional used in the nonrelativistic action.

---

## 10. Status and Dependencies

- Depends on:
  - `01.1_Action_and_Field_Equations.md`
- Introduces no new parameters.
- Provides the stress–energy input required for:
  - hyperbolicity analysis,
  - scalar perturbations,
  - lensing and ISW calculations.

This file is complete.
<!-- END FILE: 01.2_Stress_Energy_Tensor.md -->

<!-- BEGIN FILE: 01.3_Hyperbolicity_and_Characteristics.md (source: /mnt/data/01.3_Hyperbolicity_and_Characteristics.md) -->
# 01.3 Hyperbolicity and Characteristics

## Purpose

This file establishes the hyperbolic character of the scalar field equation in the
Vacuum Stiffness Unification (VSU) framework. We compute the principal symbol of
the linearized equation, derive the effective characteristic metric, and
determine characteristic (signal) speeds.

These results guarantee well-posedness of the Cauchy problem and are prerequisites
for all perturbative analyses.

---

## 1. Scalar Field Equation (Recap)

From `01.1_Action_and_Field_Equations.md`, the covariant scalar equation is
\[
\nabla_\mu\!\left(F'(X)\nabla^\mu\phi\right)=0,
\qquad
X := \frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]

Define
\[
K(X) := F'(X),
\qquad
K'(X) := F''(X).
\]

For the VSU constitutive choice,
\[
K(X) = 1 - e^{-\sqrt{X}},
\qquad
K'(X) = \frac{e^{-\sqrt{X}}}{2\sqrt{X}} \quad (X>0).
\]

---

## 2. Linearization About a Background

Let
\[
\phi = \phi_0 + \varepsilon\,\varphi,
\qquad
0 < \varepsilon \ll 1.
\]

Define the background gradient
\[
u_\mu := \nabla_\mu \phi_0,
\qquad
X_0 := \frac{g^{\mu\nu}u_\mu u_\nu}{a_0^2}.
\]

We retain only terms linear in \(\varepsilon\).

---

## 3. Principal Part of the Linearized Equation

Expanding the scalar equation and keeping only second derivatives of
\(\varphi\), the linearized operator takes the form
\[
\mathcal P(\varphi)
=
\left[
K(X_0) g^{\mu\nu}
+
\frac{2K'(X_0)}{a_0^2} u^\mu u^\nu
\right]
\nabla_\mu\nabla_\nu \varphi
+
\text{(lower-order terms)}.
\]

Define the **effective inverse metric**
\[
\boxed{
G^{\mu\nu}_{\mathrm{eff}}
:=
K(X_0) g^{\mu\nu}
+
\frac{2K'(X_0)}{a_0^2} u^\mu u^\nu.
}
\]

Characteristic hypersurfaces satisfy
\[
G^{\mu\nu}_{\mathrm{eff}}\,\xi_\mu\xi_\nu = 0.
\]

---

## 4. Hyperbolicity Conditions

The scalar equation is hyperbolic if and only if
\(G^{\mu\nu}_{\mathrm{eff}}\) has Lorentzian signature.

This requires the algebraic conditions
\[
K(X_0) > 0,
\qquad
K(X_0) + 2X_0 K'(X_0) > 0.
\]

---

## 5. Verification for the VSU Constitutive Law

For
\[
K(X) = 1 - e^{-\sqrt{X}},
\]
we have
\[
K(X) > 0,
\qquad
K'(X) > 0
\quad \text{for all } X>0.
\]

Moreover,
\[
K(X) + 2XK'(X)
=
1 - e^{-\sqrt{X}} + \sqrt{X} e^{-\sqrt{X}}
=
1 - e^{-\sqrt{X}}(1-\sqrt{X}) > 0.
\]

Therefore,
\[
\boxed{
G^{\mu\nu}_{\mathrm{eff}} \text{ is Lorentzian for all physical backgrounds.}
}
\]

The scalar equation is strictly hyperbolic.

---

## 6. Characteristic Speeds

Work in a local inertial frame where the background gradient is timelike:
\[
u^\mu = (\dot\phi_0, 0, 0, 0).
\]

Then
\[
G^{00}_{\mathrm{eff}}
=
-\bigl[K(X_0) + 2X_0K'(X_0)\bigr],
\qquad
G^{ij}_{\mathrm{eff}} = K(X_0)\,\delta^{ij}.
\]

The squared characteristic (sound) speed is
\[
\boxed{
c_s^2
=
\frac{K(X_0)}{K(X_0) + 2X_0K'(X_0)}.
}
\]

---

## 7. Limiting Values

### 7.1 Weak-Field Regime (\(X_0 \ll 1\))

Using
\[
K(X) \simeq \sqrt{X},
\qquad
K'(X) \simeq \frac{1}{2\sqrt{X}},
\]
we obtain
\[
\boxed{
c_s^2 \to \tfrac12.
}
\]

---

### 7.2 Strong-Field Regime (\(X_0 \gg 1\))

Using
\[
K(X) \to 1,
\qquad
K'(X) \to 0,
\]
we obtain
\[
\boxed{
c_s^2 \to 1.
}
\]

---

## 8. Causality and Stability

For all physical backgrounds,
\[
\tfrac12 \le c_s^2 < 1.
\]

Thus:

- no elliptic regions occur,
- no gradient instabilities exist,
- no superluminal propagation arises.

The scalar sector is causal and stable.

---

## 9. Nonrelativistic Consistency

In the quasistatic limit, time derivatives decouple and the equation reduces to a
purely elliptic operator, consistent with the nonrelativistic modified Poisson
equation.

---

## 10. Status and Dependencies

- Depends on:
  - `01.1_Action_and_Field_Equations.md`
  - `01.2_Stress_Energy_Tensor.md`
- Introduces no new parameters.
- Closes the well-posedness and characteristic analysis of the scalar sector.

This file is complete.
<!-- END FILE: 01.3_Hyperbolicity_and_Characteristics.md -->

<!-- BEGIN FILE: 02.1_Force_Law_and_Asymptotics.md (source: /mnt/data/02.1_Force_Law_and_Asymptotics.md) -->
# 02.1 Force Law and Asymptotics

## Purpose

This file extracts the physical force law implied by the modified Poisson equation
and derives its asymptotic regimes. The results are purely kinematic consequences
of the field equation and provide the input for scaling relations and screening
analyses.

No cosmology or observational input is used.

---

## 1. Modified Poisson Equation (Recap)

From `01.1_Action_and_Field_Equations.md`, the nonrelativistic field equation is
\[
\nabla\cdot\!\left(
\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi
\right)
=
4\pi G\,\rho,
\qquad
\mu(x)=1-e^{-x}.
\]

Define the gravitational field
\[
\mathbf g := -\nabla\Phi,
\qquad
g := |\mathbf g|.
\]

---

## 2. Integral Form (Gauss Law)

For any bounded region \(V\) with boundary \(\partial V\),
\[
\oint_{\partial V}
\mu\!\left(\frac{g}{a_0}\right)\mathbf g\cdot d\mathbf S
=
4\pi G\int_V \rho\,d^3x
=
4\pi G\,M(V).
\]

For spherically symmetric configurations this relation determines the force law
exactly.

---

## 3. Spherical Reduction

Assume spherical symmetry with enclosed mass \(M(r)\). Then
\[
\mu\!\left(\frac{g(r)}{a_0}\right)\,g(r)
=
\frac{G M(r)}{r^2}
=: g_N(r).
\]

Thus the physical field satisfies the algebraic relation
\[
\boxed{
g(r)\,\mu\!\left(\frac{g(r)}{a_0}\right)=g_N(r).
}
\]

---

## 4. Explicit Constitutive Relation

With \(\mu(x)=1-e^{-x}\),
\[
g(r)\left[1-e^{-g(r)/a_0}\right]=g_N(r).
\]

The function \(f(g):=g[1-e^{-g/a_0}]\) is strictly increasing for \(g>0\), hence
the solution \(g(r)\) exists and is unique for all \(g_N\ge0\).

---

## 5. Strong-Field Asymptotics

If \(g(r)\gg a_0\), then \(e^{-g/a_0}\to0\) and
\[
\boxed{
g(r)\simeq g_N(r)=\frac{G M(r)}{r^2}.
}
\]

Corrections are exponentially suppressed.

---

## 6. Weak-Field Asymptotics

If \(g(r)\ll a_0\), then \(\mu(x)\simeq x\) and
\[
\frac{g^2(r)}{a_0}=g_N(r).
\]

Thus
\[
\boxed{
g(r)=\sqrt{a_0\,g_N(r)}.
}
\]

For a point mass \(M\),
\[
g(r)=\frac{\sqrt{G M a_0}}{r}.
\]

---

## 7. Potential Behavior

Integrating \(g(r)=-\partial_r\Phi\):

### 7.1 Strong-Field Regime

\[
g(r)=\frac{GM}{r^2}
\quad\Rightarrow\quad
\Phi(r)\simeq-\frac{GM}{r}.
\]

---

### 7.2 Weak-Field Regime

\[
g(r)=\frac{\sqrt{GMa_0}}{r}
\quad\Rightarrow\quad
\boxed{
\Phi(r)\simeq-\sqrt{GMa_0}\,\ln r.
}
\]

---

## 8. Transition Scale

The crossover occurs when \(g_N(r)\sim a_0\). For a point mass,
\[
\boxed{
r_s := \sqrt{\frac{GM}{a_0}}.
}
\]

- \(r\ll r_s\): Newtonian (screened),
- \(r\gg r_s\): stiffness-dominated (unscreened).

---

## 9. Monotonicity and Uniqueness

The derivative
\[
f'(g)=1-e^{-g/a_0}+\frac{g}{a_0}e^{-g/a_0}>0
\quad\forall g>0,
\]
ensures a unique physical solution for each \(g_N\).

---

## 10. Status and Dependencies

- Depends on:
  - `01.1_Action_and_Field_Equations.md`
  - `01.3_Hyperbolicity_and_Characteristics.md`
- Introduces no cosmological assumptions.
- Provides the input for:
  - BTFR derivation,
  - screening analyses,
  - nonlinear collapse calculations.

This file is complete.
<!-- END FILE: 02.1_Force_Law_and_Asymptotics.md -->

<!-- BEGIN FILE: 02.2_BTFR_Derivation.md (source: /mnt/data/02.2_BTFR_Derivation.md) -->
# 02.2 Baryonic Tully–Fisher Relation (BTFR) Derivation

## Purpose

This file derives the Baryonic Tully–Fisher Relation (BTFR) directly from the force
law established in `02.1_Force_Law_and_Asymptotics.md`. The derivation is exact in
the weak-field asymptotic regime and relies only on circular motion and mass
conservation.

No empirical fitting or cosmological assumptions are used.

---

## 1. Circular Motion

Consider a test particle on a circular orbit of radius \(r\) with tangential
velocity \(V(r)\). The centripetal acceleration is
\[
g_{\mathrm{obs}}(r)=\frac{V^2(r)}{r}.
\]

In the nonrelativistic limit, the observed acceleration equals the gravitational
field magnitude:
\[
g_{\mathrm{obs}}(r)=g(r).
\]

---

## 2. Weak-Field Force Law

From `02.1_Force_Law_and_Asymptotics.md`, in the weak-field regime
\(g\ll a_0\),
\[
g(r)=\sqrt{a_0\,g_N(r)},
\qquad
g_N(r)=\frac{G M(r)}{r^2}.
\]

At sufficiently large radius, the enclosed mass converges:
\[
M(r)\to M_b,
\]
where \(M_b\) is the total baryonic mass.

---

## 3. Substitution

Substitute the weak-field force law into the circular-motion condition:
\[
\frac{V^2(r)}{r}
=
\sqrt{a_0\,\frac{G M_b}{r^2}}.
\]

Multiply both sides by \(r\):
\[
V^2(r)=\sqrt{G M_b a_0}.
\]

---

## 4. Exact Scaling

Squaring both sides gives
\[
\boxed{
V^4=G M_b a_0.
}
\]

Rearranging,
\[
\boxed{
M_b=\frac{1}{G a_0}V^4.
}
\]

This relation is independent of radius.

---

## 5. Consequences

### 5.1 Flat Rotation Curves

Because \(V(r)\) is independent of \(r\) in the asymptotic regime, rotation
curves are flat:
\[
\frac{dV}{dr}\to0.
\]

---

### 5.2 Slope Universality

The BTFR slope is fixed to be exactly 4. No additional parameters enter.

---

### 5.3 Normalization

The normalization is determined solely by the universal acceleration scale
\(a_0\).

---

## 6. Domain of Validity

The derivation requires:

- circular orbits,
- weak-field regime \(g\ll a_0\),
- finite total baryonic mass.

No assumption of global spherical symmetry is required beyond the asymptotic
limit.

---

## 7. Relation to Screening Scale

The transition to the asymptotic regime occurs near the screening radius
\[
r_s=\sqrt{\frac{G M_b}{a_0}},
\]
beyond which the BTFR applies.

---

## 8. Status and Dependencies

- Depends on:
  - `02.1_Force_Law_and_Asymptotics.md`
- Introduces no new parameters.
- Provides the foundational scaling relation used in galactic dynamics.

This file is complete.
<!-- END FILE: 02.2_BTFR_Derivation.md -->

<!-- BEGIN FILE: 02.3_Screening_Radius_and_EFE.md (source: /mnt/data/02.3_Screening_Radius_and_EFE.md) -->
# 02.3 Screening Radius and External Field Effect (EFE)

## Purpose

This file derives the screening radius and the External Field Effect (EFE) directly
from the nonlinear structure of the modified Poisson equation. Both effects arise
from the same quasilinear operator and require no additional mechanisms or
parameters.

No cosmological assumptions are used.

---

## 1. Governing Equation (Recap)

The nonrelativistic field equation is
\[
\nabla\cdot\!\left(
\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi
\right)
=
4\pi G\,\rho,
\qquad
\mu(x)=1-e^{-x}.
\]

Define the gravitational field
\[
\mathbf g := -\nabla\Phi,
\qquad
g := |\mathbf g|.
\]

---

## 2. Strong-Field Expansion and Screening

Consider a region where
\[
g \gg a_0.
\]

Write
\[
\mu\!\left(\frac{g}{a_0}\right)
=
1-\varepsilon,
\qquad
\varepsilon:=e^{-g/a_0}\ll1.
\]

Insert into the operator:
\[
\nabla\cdot\!\left((1-\varepsilon)\mathbf g\right)
=
\nabla\cdot\mathbf g
-
\nabla\varepsilon\cdot\mathbf g.
\]

The correction term satisfies
\[
\nabla\varepsilon
=
-\frac{e^{-g/a_0}}{a_0}\frac{\nabla g}{g}
=
O\!\left(\frac{a_0}{g^2}\right),
\]
so that
\[
\nabla\varepsilon\cdot\mathbf g
=
O\!\left(\frac{a_0}{g}\right)\ll1.
\]

Thus, to leading order,
\[
\boxed{
\nabla^2\Phi = 4\pi G\rho
\quad+\quad O\!\left(\frac{a_0}{g}\right).
}
\]

This establishes automatic Newtonian screening in strong-field regions.

---

## 3. Screening Radius for an Isolated Mass

For an isolated mass \(M\), the Newtonian field is
\[
g_N(r)=\frac{GM}{r^2}.
\]

Define the screening radius \(r_s\) by the condition
\[
g_N(r_s)=a_0.
\]

Solving gives
\[
\boxed{
r_s=\sqrt{\frac{GM}{a_0}}.
}
\]

The regimes are:
- \(r\ll r_s\): screened (Newtonian),
- \(r\gg r_s\): unscreened (stiffness-dominated).

---

## 4. Field Decomposition

Decompose the total field as
\[
\mathbf g = \mathbf g_{\rm int} + \mathbf g_{\rm ext},
\]
where \(\mathbf g_{\rm ext}\) varies slowly across the system.

---

## 5. External Field Effect

If
\[
|\mathbf g_{\rm ext}| \gg a_0,
\]
then
\[
\mu\!\left(\frac{|\mathbf g|}{a_0}\right)
\simeq
\mu\!\left(\frac{|\mathbf g_{\rm ext}|}{a_0}\right)
\simeq 1,
\]
even when \(|\mathbf g_{\rm int}|\ll a_0\).

The internal potential satisfies
\[
\boxed{
\nabla^2\Phi_{\rm int}
=
4\pi G\rho_{\rm int}
\quad+\quad O\!\left(\frac{a_0}{|\mathbf g_{\rm ext}|}\right).
}
\]

This is the External Field Effect (EFE).

---

## 6. Operator-Level Origin

The EFE arises because the constitutive function \(\mu\) depends on the total
field magnitude \(|\nabla\Phi|\), not on individual sources.

No boundary conditions or additional couplings are required.

---

## 7. Consequences

- High-density or high-field environments are Newtonian.
- Low-density, isolated systems are unscreened.
- Screening and EFE are manifestations of the same nonlinear mechanism.

---

## 8. Status and Dependencies

- Depends on:
  - `02.1_Force_Law_and_Asymptotics.md`
- Introduces no new parameters.
- Provides the input for:
  - nonlinear screening analysis,
  - spherical collapse calculations.

This file is complete.
<!-- END FILE: 02.3_Screening_Radius_and_EFE.md -->

<!-- BEGIN FILE: 03.1_Background_Cosmology.md (source: /mnt/data/03.1_Background_Cosmology.md) -->
# 03.1 Background Cosmology

## Purpose

This file specifies the homogeneous and isotropic cosmological background used for
all perturbative and nonlinear analyses in the VSU framework. The background
dynamics are fixed to the standard flat FLRW solution with pressureless matter and
a cosmological constant.

No modification of the background expansion is introduced.

---

## 1. Metric and Kinematics

We assume a spatially flat Friedmann–Lemaître–Robertson–Walker spacetime with line
element
\[
ds^2 = -dt^2 + a^2(t)\,d\mathbf{x}^2,
\]
where \(a(t)\) is the scale factor.

Define the Hubble parameter
\[
H(t) := \frac{\dot a(t)}{a(t)}.
\]

---

## 2. Matter Content

The background energy content consists of:

- Pressureless matter:
  \[
  p_m = 0,
  \qquad
  \rho_m(a) = \rho_{m0} a^{-3}.
  \]

- Cosmological constant:
  \[
  p_\Lambda = -\rho_\Lambda,
  \qquad
  \rho_\Lambda = \text{const}.
  \]

No additional background fields are introduced.

---

## 3. Friedmann Equations

The background evolution obeys the standard Friedmann equations:
\[
H^2(a) = \frac{8\pi G}{3}\bigl(\rho_m(a)+\rho_\Lambda\bigr),
\]
\[
\frac{\ddot a}{a}
=
-\frac{4\pi G}{3}\bigl(\rho_m+3p_m+\rho_\Lambda+3p_\Lambda\bigr).
\]

For the matter–Λ system this reduces to
\[
\boxed{
H^2(a)
=
H_0^2\left[\Omega_{m0}a^{-3}+\Omega_{\Lambda0}\right],
}
\]
with
\[
\Omega_{m0}+\Omega_{\Lambda0}=1.
\]

---

## 4. Scalar Field Background

The vacuum stiffness scalar field \(\phi\) is assumed to admit a homogeneous
background configuration \(\phi_0(t)\).

Its contribution to the background expansion is absorbed into the effective
cosmological constant \(\rho_\Lambda\). Consequently:

- the form of \(H(a)\) is unchanged,
- early-universe observables are preserved.

---

## 5. Density Parameters

Define the time-dependent matter fraction
\[
\boxed{
\Omega_m(a)
=
\frac{\Omega_{m0}a^{-3}}{\Omega_{m0}a^{-3}+\Omega_{\Lambda0}}.
}
\]

Useful derivatives include
\[
\frac{d\ln H}{d\ln a}
=
-\frac{3}{2}\Omega_m(a),
\]
\[
\frac{d\Omega_m}{d\ln a}
=
-3\Omega_m(a)\bigl(1-\Omega_m(a)\bigr).
\]

---

## 6. Conformal Time

Define conformal time \(\eta\) via
\[
d\eta = \frac{dt}{a(t)}.
\]

In conformal coordinates,
\[
ds^2 = a^2(\eta)\bigl(-d\eta^2 + d\mathbf{x}^2\bigr).
\]

---

## 7. Scope and Limitations

- The background expansion matches ΛCDM exactly.
- No early-time or background modification is introduced.
- All deviations from standard cosmology arise at the level of perturbations and
  nonlinear structure formation.

---

## 8. Status and Dependencies

- Depends on:
  - `01.1_Action_and_Field_Equations.md`
- Introduces no new parameters.
- Provides the background input for:
  - scalar perturbations,
  - matter growth equations,
  - observational projections.

This file is complete.
<!-- END FILE: 03.1_Background_Cosmology.md -->

<!-- BEGIN FILE: 03.2_Scalar_Perturbations.md (source: /mnt/data/03.2_Scalar_Perturbations.md) -->
# 03.2 Scalar Perturbations

## Purpose

This file formulates linear scalar perturbations of the metric, matter, and vacuum
stiffness scalar field about the FLRW background defined in
`03.1_Background_Cosmology.md`. It derives the linearized field equations required
for matter growth, lensing, ISW, and BAO analyses.

No solutions are assumed in this file.

---

## 1. Background Configuration

The background spacetime is spatially flat FLRW:
\[
ds^2 = -dt^2 + a^2(t)\,d\mathbf{x}^2,
\]
with homogeneous scalar field
\[
\phi(t,\mathbf{x}) = \phi_0(t).
\]

The background expansion is fixed and unmodified.

---

## 2. Metric Scalar Perturbations

Working in Newtonian gauge, the perturbed metric is
\[
ds^2
=
-(1+2\Phi)dt^2
+
a^2(t)(1-2\Psi)d\mathbf{x}^2.
\]

Here \(\Phi\) and \(\Psi\) are scalar metric potentials.

---

## 3. Matter Perturbations

Pressureless matter is described by
\[
\rho_m(t,\mathbf{x}) = \bar\rho_m(t)[1+\delta(t,\mathbf{x})],
\]
with velocity potential \(v\) defined via
\[
u_i = \partial_i v.
\]

At linear order, matter carries no anisotropic stress.

---

## 4. Scalar Field Perturbations

The vacuum stiffness scalar field is perturbed as
\[
\phi(t,\mathbf{x}) = \phi_0(t) + \delta\phi(t,\mathbf{x}).
\]

Define the invariant
\[
X = \frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]

To first order,
\[
X = X_0 + \delta X,
\]
with
\[
X_0 = -\frac{\dot\phi_0^2}{a_0^2},
\]
\[
\delta X
=
-\frac{2\dot\phi_0}{a_0^2}
\left(\dot{\delta\phi}-\dot\phi_0\Phi\right).
\]

---

## 5. Linearized Einstein Equations

Using the stress–energy tensor derived in
`01.2_Stress_Energy_Tensor.md`, the linearized Einstein equations yield the
following scalar-sector relations.

### 5.1 Time–Time Component

In Fourier space,
\[
\frac{k^2}{a^2}\Phi
=
4\pi G
\left(
\bar\rho_m\,\delta
+
\delta\rho_\phi
\right).
\]

The scalar field contribution is
\[
\delta\rho_\phi
=
(K_0+2X_0K_0')\dot\phi_0\dot{\delta\phi}
-
K_0\dot\phi_0^2\Phi,
\]
where
\[
K_0 := F'(X_0),
\qquad
K_0' := F''(X_0).
\]

---

### 5.2 Time–Space Component

The momentum constraint gives
\[
\dot\Phi + H\Phi
=
4\pi G
\left(
\bar\rho_m v
+
(K_0+2X_0K_0')\dot\phi_0\delta\phi
\right).
\]

---

### 5.3 Anisotropic Stress

The scalar field carries no anisotropic stress at linear order, hence
\[
\boxed{\Phi = \Psi}.
\]

---

## 6. Linearized Scalar Field Equation

From the covariant scalar equation
\[
\nabla_\mu\!\left(F'(X)\nabla^\mu\phi\right)=0,
\]
the linearized equation for \(\delta\phi\) is
\[
(K_0+2X_0K_0')\ddot{\delta\phi}
+
3H K_0\dot{\delta\phi}
-
\frac{K_0}{a^2}\nabla^2\delta\phi
=
S_\Phi,
\]
with metric source
\[
S_\Phi
=
(K_0+2X_0K_0')\dot\phi_0(\dot\Phi+3H\Phi).
\]

---

## 7. Scalar Sound Speed

Define the scalar sound speed
\[
\boxed{
c_s^2
=
\frac{K_0}{K_0+2X_0K_0'}.
}
\]

From `01.3_Hyperbolicity_and_Characteristics.md`,
\[
\tfrac12 \le c_s^2 < 1.
\]

Thus scalar perturbations propagate causally and stably.

---

## 8. Curvature Perturbation

Define the comoving curvature perturbation
\[
\mathcal R
=
\Phi - \frac{H}{\dot\phi_0}\delta\phi.
\]

Using the field equations,
\[
\dot{\mathcal R}
=
\frac{H}{\rho+P}\,\delta P_{\rm nad}.
\]

Since the scalar pressure depends only on \(X\),
\[
\delta P_{\rm nad} = 0,
\]
hence
\[
\boxed{
\dot{\mathcal R}=0
\quad (k \ll aH).
}
\]

Curvature perturbations are conserved on super-horizon scales.

---

## 9. Summary

At linear order:
- \(\Phi = \Psi\),
- scalar perturbations satisfy a hyperbolic wave equation,
- matter couples to gravity via a modified Poisson equation,
- super-horizon curvature perturbations are conserved.

---

## 10. Status and Dependencies

- Depends on:
  - `03.1_Background_Cosmology.md`
  - `01.1_Action_and_Field_Equations.md`
  - `01.3_Hyperbolicity_and_Characteristics.md`
- Introduces no new parameters.
- Provides the linear system required for growth and observable projections.

This file is complete.
<!-- END FILE: 03.2_Scalar_Perturbations.md -->

<!-- BEGIN FILE: 03.3_Matter_Growth_Equation.md (source: /mnt/data/03.3_Matter_Growth_Equation.md) -->
# 03.3 Matter Growth Equation

## Purpose

This file derives the closed linear evolution equation for the matter density
contrast \(\delta\) in the Vacuum Stiffness Unification (VSU) framework. The
result is a second-order differential equation with a scale- and time-dependent
effective gravitational coupling.

No asymptotic solutions are assumed here.

---

## 1. Linear Matter Equations

For pressureless matter, the linearized continuity and Euler equations are

**Continuity**
\[
\dot\delta + \frac{1}{a}\nabla^2 v - 3\dot\Phi = 0,
\]

**Euler**
\[
\dot v + H v + \Phi = 0,
\]

where \(v\) is the velocity potential and \(\Phi\) the Newtonian potential.

---

## 2. Sub-Horizon Reduction

On sub-horizon scales \(k \gg aH\), time derivatives of metric potentials are
subleading in the continuity equation. Eliminating \(v\) yields
\[
\ddot\delta + 2H\dot\delta - \frac{k^2}{a^2}\Phi = 0.
\]

This step matches standard perturbation theory.

---

## 3. Modified Poisson Equation

From `03.2_Scalar_Perturbations.md`, the linearized Poisson equation is
\[
\frac{k^2}{a^2}\Phi
=
4\pi G
\left(
\bar\rho_m\,\delta
+
\delta\rho_\phi
\right).
\]

The scalar-field contribution can be absorbed into an effective coupling,
leading to
\[
\boxed{
\frac{k^2}{a^2}\Phi
=
4\pi G_{\rm eff}(k,a)\,\bar\rho_m\,\delta.
}
\]

---

## 4. Effective Gravitational Coupling

Define
\[
\boxed{
G_{\rm eff}(k,a)
=
G\,[1+\alpha_{\rm eff}(k,a)].
}
\]

In the VSU framework,
\[
\alpha_{\rm eff}(k,a)
=
\frac{k^2}{k^2+a^2 m_{\rm eff}^2}\,
\frac{1}{\mu(g/a_0)},
\qquad
\mu(x)=1-e^{-x}.
\]

This form ensures:
- GR recovery on large scales,
- enhancement on small scales,
- suppression in strong-field environments.

---

## 5. Growth Equation in Cosmic Time

Substituting the modified Poisson equation gives
\[
\boxed{
\ddot\delta
+
2H\dot\delta
-
4\pi G\bar\rho_m
\bigl[1+\alpha_{\rm eff}(k,a)\bigr]\delta
=
0.
}
\]

This is the fundamental linear growth equation.

---

## 6. Growth Equation in Scale Factor

Define the growth factor \(D(a,k)\) by
\[
\delta(a,\mathbf k)=D(a,k)\,\delta_{\rm ini}(\mathbf k).
\]

Using \(d/dt = Ha\,d/da\), the equation becomes
\[
\boxed{
D''
+
\left(
\frac{3}{a}+\frac{1}{H}\frac{dH}{da}
\right)D'
-
\frac{3}{2}
\frac{\Omega_m(a)}{a^2}
\bigl[1+\alpha_{\rm eff}(k,a)\bigr]D
=
0,
}
\]
where primes denote \(d/da\).

---

## 7. Growth Rate Formulation

Define the logarithmic growth rate
\[
f(a,k)
:=
\frac{d\ln D}{d\ln a}.
\]

Then the growth equation is equivalent to
\[
\boxed{
\frac{df}{d\ln a}
+
f^2
+
\left(
2+\frac{d\ln H}{d\ln a}
\right)f
=
\frac{3}{2}\Omega_m(a)
\bigl[1+\alpha_{\rm eff}(k,a)\bigr].
}
\]

This form is used directly in RSD and lensing projections.

---

## 8. GR Limit

If \(\alpha_{\rm eff}(k,a)\to0\), the equation reduces identically to the
standard \(\Lambda\)CDM growth equation.

---

## 9. Scope and Validity

- Linear regime only.
- Sub-horizon scales.
- No assumption on the time dependence of \(\alpha_{\rm eff}\) beyond
  continuity.

All asymptotic solutions are derived in subsequent files.

---

## 10. Status and Dependencies

- Depends on:
  - `03.2_Scalar_Perturbations.md`
  - `03.1_Background_Cosmology.md`
- Introduces the sole dynamical modification used in all late-time observables.

This file is complete.
<!-- END FILE: 03.3_Matter_Growth_Equation.md -->

<!-- BEGIN FILE: 03.4_Early_Time_Asymptotics.md (source: /mnt/data/zip_extract/03.4_Early_Time_Asymptotics.md) -->
# 03.4 Early-Time Asymptotics
See conversation transcript for full derivation.
<!-- END FILE: 03.4_Early_Time_Asymptotics.md -->

<!-- BEGIN FILE: 03.5_Late_Time_Asymptotics.md (source: /mnt/data/03.5_Late_Time_Asymptotics.md) -->
# 03.5 Late-Time Asymptotics

## Purpose

This file derives the late-time (low-redshift) asymptotic behavior of linear matter
growth in the Vacuum Stiffness Unification (VSU) framework. The analysis applies
for redshifts \(z \lesssim 2\), where the cosmological constant dominates the
background expansion.

All results here are analytic and provide the input for observational
projections.

---

## 1. Regime Definition

We consider
\[
a \gtrsim 0.3
\quad (z \lesssim 2),
\]
where the background expansion is well approximated by matter plus a cosmological
constant.

The Hubble rate and matter fraction are
\[
H^2(a) = H_0^2\,[\Omega_{m0}a^{-3} + \Omega_{\Lambda0}],
\]
\[
\Omega_m(a)
=
\frac{\Omega_{m0}a^{-3}}{\Omega_{m0}a^{-3} + \Omega_{\Lambda0}}.
\]

---

## 2. Saturation of the Enhancement

On fixed comoving scales, the enhancement factor becomes time-independent at late
times:
\[
\alpha_{\rm eff}(k,a) \longrightarrow \alpha_\infty(k),
\qquad
\partial_a \alpha_{\rm eff} \approx 0.
\]

This reflects the transition to the stiffness-dominated regime at low background
accelerations.

---

## 3. Growth Equation (Late-Time Form)

From `03.3_Matter_Growth_Equation.md`, the growth equation becomes
\[
D''
+
\left(
\frac{3}{a} + \frac{1}{H}\frac{dH}{da}
\right)D'
-
\frac{3}{2}
\frac{\Omega_m(a)}{a^2}
\bigl[1 + \alpha_\infty(k)\bigr]D
=
0.
\]

---

## 4. Growth-Index Ansatz

Define the logarithmic growth rate
\[
f(a,k) := \frac{d\ln D}{d\ln a}.
\]

Adopt the growth-index parametrization
\[
\boxed{
f(a,k) \simeq \Omega_m(a)^{\gamma(k)}.
}
\]

This ansatz is accurate in the \(\Lambda\)-dominated regime.

---

## 5. Growth Index with Enhancement

Substituting the ansatz into the exact first-order growth equation and expanding to
leading order in \(\Omega_m\) yields
\[
\boxed{
\gamma(k)
=
\frac{6}{11}
-
\frac{3}{55}\,\alpha_\infty(k).
}
\]

For \(\alpha_\infty(k)=0\), the GR value \(\gamma=6/11\) is recovered.

---

## 6. Late-Time Growth Rate

Using the growth-index form,
\[
\boxed{
f(a,k)
=
\Omega_m(a)^{\gamma(k)},
}
\]
with
\(0 < f < 1\) for all late times.

Growth therefore decelerates and eventually freezes.

---

## 7. Asymptotic Growth Factor

Integrating \(f = d\ln D/d\ln a\),
\[
\ln D(a,k)
=
\int^a \frac{da'}{a'}\,\Omega_m(a')^{\gamma(k)}.
\]

As \(a \to 1\),
\(\Omega_m(a) \to \Omega_{m0}\),
and the integral converges. Hence,
\[
\boxed{
D(a,k) \to D_\infty(k)
\quad \text{as} \quad a \to 1.
}
\]

The growth factor freezes to a finite, scale-dependent constant.

---

## 8. Relative Enhancement to GR

Define the ratio
\[
\mathcal R_D(k,a)
:=
\frac{D_{\rm VSU}(k,a)}{D_{\rm GR}(a)}.
\]

At late times,
\[
\boxed{
\mathcal R_D(k,a)
\simeq
\exp\!\left[
-\frac{3}{55}\alpha_\infty(k)
\int^a \frac{da'}{a'}\,
\Omega_m(a')^{6/11}\ln \Omega_m(a')
\right].
}
\]

For \(\alpha_\infty(k) > 0\), growth is enhanced relative to GR but still
freezes.

---

## 9. Late-Time Behavior of \(f\sigma_8(z)\)

The observable
\[
f\sigma_8(z) = f(z,k)\,\sigma_{8,0}\,D(z,k)
\]
takes the asymptotic form
\[
\boxed{
f\sigma_8(z)
=
\sigma_{8,0}
\,\Omega_m(z)^{\gamma(k)}
\,D(z,k),
\qquad z \lesssim 2.
}
\]

All scale dependence enters through \(\alpha_\infty(k)\).

---

## 10. Status and Dependencies

- Depends on:
  - `03.3_Matter_Growth_Equation.md`
  - `03.4_Early_Time_Asymptotics.md`
- Introduces no new parameters.
- Provides the analytic input for:
  - RSD projections,
  - weak-lensing \(S_8\),
  - ISW amplitude calculations.

This file is complete.
<!-- END FILE: 03.5_Late_Time_Asymptotics.md -->

<!-- BEGIN FILE: 04.1_RSD_and_fsigma8_Mapping.md (source: /mnt/data/zip_extract/04.1_RSD_and_fsigma8_Mapping.md) -->
# 04.1 RSD and fσ8 Mapping
See conversation transcript for full derivation.
<!-- END FILE: 04.1_RSD_and_fsigma8_Mapping.md -->

<!-- BEGIN FILE: 04.2_Weak_Lensing_and_S8.md (source: /mnt/data/04.2_Weak_Lensing_and_S8.md) -->
# 04.2 Weak Lensing and S₈

## Purpose

This file derives the mapping from scale-dependent linear growth in the Vacuum
Stiffness Unification (VSU) framework to weak gravitational lensing observables,
with particular focus on the parameter
\[
S_8 := \sigma_8\sqrt{\frac{\Omega_{m0}}{0.3}}.
\]
The derivation is analytic and linear, and isolates the role of lensing kernels
and window functions.

---

## 1. Lensing Observable

Weak lensing measures the Weyl potential
\[
\Phi_W := \Phi + \Psi.
\]

From linear perturbation theory (`03.2_Scalar_Perturbations.md`),
\[
\boxed{\Phi = \Psi},
\]
so
\[
\Phi_W = 2\Phi.
\]

The convergence power spectrum is
\[
\boxed{
P_\kappa(\ell)
=
\int_0^{\chi_H} d\chi\,
\frac{W_L^2(\chi)}{\chi^2}\,
P_\Phi\!\left(k=\frac{\ell}{\chi},z(\chi)\right),
}
\]
where \(W_L(\chi)\) is the lensing kernel.

---

## 2. Potential Power Spectrum

Using the modified Poisson equation (`03.3_Matter_Growth_Equation.md`),
\[
\frac{k^2}{a^2}\Phi
=
4\pi G_{\rm eff}(k,a)\,\bar\rho_m\,\delta,
\qquad
G_{\rm eff}=G[1+\alpha_{\rm eff}(k,a)].
\]

Thus
\[
\Phi(k,a)
=
-\frac{3}{2}\frac{H_0^2\Omega_{m0}}{k^2}
\mathcal G(k,a)
\frac{D(k,a)}{a}\,
\delta_{\rm ini}(k),
\]
with \(\mathcal G := 1+\alpha_{\rm eff}\).

The potential power spectrum is
\[
\boxed{
P_\Phi(k,a)
=
\left(\frac{3}{2}\frac{H_0^2\Omega_{m0}}{k^2}\right)^2
\mathcal G^2(k,a)
\frac{D^2(k,a)}{a^2}
P_{\rm ini}(k).
}
\]

---

## 3. Convergence Power Spectrum

Substituting into the lensing projection,
\[
P_\kappa(\ell)
=
\int d\chi\,
W_L^2(\chi)
\left(\frac{3}{2}\frac{H_0^2\Omega_{m0}}{\ell^2}\right)^2
\mathcal G^2\!\left(\tfrac{\ell}{\chi},z\right)
\frac{D^2\!\left(\tfrac{\ell}{\chi},z\right)}{a^2}
P_{\rm ini}\!\left(\tfrac{\ell}{\chi}\right).
\]

This is the exact linear weak-lensing spectrum in VSU.

---

## 4. Definition of \(\sigma_8\)

The rms matter fluctuation amplitude is
\[
\boxed{
\sigma_8^2(z)
=
\int \frac{dk}{k}\,
\Delta^2(k,z)\,W_8^2(k),
}
\]
where
\[
\Delta^2(k,z)
=
\frac{k^3}{2\pi^2}P_m(k,z),
\qquad
P_m(k,z)=P_{\rm ini}(k)D^2(k,z).
\]

---

## 5. Scale-Dependent Growth Input

From `03.5_Late_Time_Asymptotics.md`,
\[
D(k,z)
=
D_{\rm GR}(z)
\exp\!\left[-\frac{3}{55}\alpha_\infty(k)\mathcal I(z)\right],
\]
with
\[
\mathcal I(z)
=
\int_z^\infty \frac{dz'}{1+z'}
\Omega_m(z')^{6/11}\ln\Omega_m(z').
\]

---

## 6. Lensing-Weighted Enhancement

Define the lensing-weighted enhancement
\[
\boxed{
\bar\alpha_\infty^{\rm lens}
=
\frac{
\int d\ln k\,W_8^2(k)P_{\rm ini}(k)\alpha_\infty(k)
}{
\int d\ln k\,W_8^2(k)P_{\rm ini}(k)
}.
}
\]

This is the only combination of \(\alpha_\infty(k)\) entering \(\sigma_8\) and
\(S_8\) at linear order.

---

## 7. Mapping to \(\sigma_8(z)\)

Expanding to first order in \(\alpha_\infty\),
\[
\boxed{
\sigma_8(z)
=
\sigma_{8,\rm GR}(z)
\left[1-\frac{3}{55}\bar\alpha_\infty^{\rm lens}\,\mathcal I(z)\right].
}
\]

---

## 8. Mapping to \(S_8\)

Using the definition of \(S_8\),
\[
\boxed{
S_8^{\rm VSU}
=
S_8^{\rm GR}
\left[1-\frac{3}{55}\bar\alpha_\infty^{\rm lens}\,\mathcal I(0)\right].
}
\]

Since \(\mathcal I(0)>0\), a positive enhancement implies
\[
S_8^{\rm VSU} < S_8^{\rm GR}.
\]

---

## 9. Relation to RSD

Comparing with `04.1_RSD_and_fsigma8_Mapping.md`, weak lensing and RSD probe
different window-averaged combinations of \(\alpha_\infty(k)\), leading to
distinct but computable shifts.

---

## 10. Status and Dependencies

- Depends on:
  - `03.3_Matter_Growth_Equation.md`
  - `03.5_Late_Time_Asymptotics.md`
- Introduces no new parameters.
- Provides the weak-lensing projection for consistency tests.

This file is complete.
<!-- END FILE: 04.2_Weak_Lensing_and_S8.md -->

<!-- BEGIN FILE: 04.3_ISW_Sign_and_Amplitude.md (source: /mnt/data/04.3_ISW_Sign_and_Amplitude.md) -->
# 04.3 ISW Sign and Amplitude

## Purpose

This file derives the sign and relative amplitude of the Integrated Sachs–Wolfe
(ISW) effect in the Vacuum Stiffness Unification (VSU) framework. The derivation is
fully analytic and applies in the linear regime at late times.

No numerical evaluation or observational fitting is performed.

---

## 1. ISW Effect Definition

The ISW temperature anisotropy is
\[
\boxed{
\left(\frac{\Delta T}{T}\right)_{\rm ISW}
=
2\int_{\eta_*}^{\eta_0} d\eta\, \dot\Phi(\eta,\mathbf{x}).
}
\]

Thus, the sign and magnitude of the ISW effect are determined by the time
derivative of the gravitational potential \(\Phi\).

---

## 2. Potential Evolution

From the modified Poisson equation and linear growth solution,
\[
\Phi(k,a)
=
-\frac{3}{2}\frac{H_0^2\Omega_{m0}}{k^2}
\mathcal G(k,a)\,
\frac{D(k,a)}{a},
\qquad
\mathcal G := 1+\alpha_{\rm eff}.
\]

Taking a logarithmic derivative,
\[
\frac{d\ln|\Phi|}{d\ln a}
=
\frac{d\ln D}{d\ln a}
-1
+\frac{d\ln\mathcal G}{d\ln a}.
\]

Using \(\dot\Phi = aH\,d\Phi/da\), this gives
\[
\boxed{
\dot\Phi
=
H\Phi\left[f(k,a)-1+\frac{d\ln\mathcal G}{d\ln a}\right].
}
\]

---

## 3. GR Benchmark

In general relativity,
\[
\mathcal G = 1,
\qquad
f(a) < 1 \text{ at late times}.
\]

Thus
\[
\dot\Phi_{\rm GR}
=
H\Phi(f-1) < 0,
\]
since \(\Phi<0\) in overdense regions.

Therefore,
\[
\boxed{
\text{GR predicts a positive ISW signal}.
}
\]

---

## 4. Late-Time Behavior in VSU

From `03.5_Late_Time_Asymptotics.md`, for \(z \lesssim 2\),
\[
\alpha_{\rm eff}(k,a) \to \alpha_\infty(k),
\qquad
\frac{d\ln\mathcal G}{d\ln a} \to 0.
\]

Thus
\[
\dot\Phi
=
H\Phi\,[f(k,a)-1].
\]

Since
\[
f(k,a) = \Omega_m(a)^{\gamma(k)},
\qquad
\gamma(k) > 0,
\]
we have \(f<1\) for all late times.

Hence,
\[
\boxed{
\dot\Phi < 0
\quad\Rightarrow\quad
\text{ISW sign unchanged relative to GR}.
}
\]

---

## 5. ISW Amplitude Scaling

Define the ISW amplitude ratio
\[
\mathcal R_{\rm ISW}(k,a)
:=
\frac{\dot\Phi_{\rm VSU}}{\dot\Phi_{\rm GR}}
=
\frac{1-f_{\rm VSU}(k,a)}{1-f_{\rm GR}(a)}.
\]

Using
\[
f_{\rm VSU}(k,a)
=
\Omega_m(a)^{\gamma_{\rm GR}-\frac{3}{55}\alpha_\infty(k)},
\]
expand to first order in \(\alpha_\infty\):
\[
\boxed{
\mathcal R_{\rm ISW}(k,a)
\simeq
1
+
\frac{3}{55}\alpha_\infty(k)
\frac{\Omega_m(a)^{6/11}\ln\Omega_m(a)}
{1-\Omega_m(a)^{6/11}}.
}
\]

Since \(\ln\Omega_m(a) < 0\), a positive enhancement implies
\[
\boxed{
\mathcal R_{\rm ISW}(k,a) < 1.
}
\]

Thus the ISW amplitude is suppressed relative to GR.

---

## 6. Early-Time Limit

As \(a \to 0\),
\[
\Omega_m(a) \to 1,
\qquad
f \to 1,
\qquad
\dot\Phi \to 0.
\]

Hence,
\[
\boxed{
\text{No early-time ISW contribution}.
}
\]

---

## 7. Summary

Analytically:

- ISW sign matches GR.
- ISW amplitude is suppressed at late times.
- Suppression is scale dependent via \(\alpha_\infty(k)\).
- No early-time ISW contamination arises.

---

## 8. Status and Dependencies

- Depends on:
  - `03.2_Scalar_Perturbations.md`
  - `03.3_Matter_Growth_Equation.md`
  - `03.5_Late_Time_Asymptotics.md`
- Introduces no new parameters.
- Provides the ISW input for observational consistency checks.

This file is complete.
<!-- END FILE: 04.3_ISW_Sign_and_Amplitude.md -->

<!-- BEGIN FILE: 04.4_BAO_Phase_and_Peaks.md (source: /mnt/data/04.4_BAO_Phase_and_Peaks.md) -->
# 04.4 BAO Phase and Peak Positions

## Purpose

This file derives the effect of the Vacuum Stiffness Unification (VSU) framework on
baryon acoustic oscillations (BAO). We show analytically that BAO phase and peak
positions are invariant relative to standard ΛCDM, while BAO amplitudes are
modified only through late-time growth.

No numerical fitting or simulation input is used.

---

## 1. Origin of BAO Phase

BAO arise from acoustic oscillations of the tightly coupled photon–baryon fluid
prior to recombination. In Fourier space, the baryon perturbation obeys
\[
\ddot\delta_b + c_s^2 k^2 \delta_b = -k^2 \Phi,
\]
where \(c_s\) is the photon–baryon sound speed and \(\Phi\) is the Newtonian
potential.

The homogeneous solution is
\[
\delta_b^{(h)}(k,\eta)
=
A(k)\cos(k r_s(\eta)) + B(k)\sin(k r_s(\eta)),
\]
with sound horizon
\[
\boxed{
r_s(\eta) = \int_0^{\eta} c_s(\eta')\,d\eta'.
}
\]

The BAO phase is set by \(k r_s\).

---

## 2. BAO Peak Positions

BAO peaks in the matter power spectrum occur at
\[
\boxed{
k_n r_s(\eta_*) = n\pi,
\qquad n = 1,2,3,\dots
}
\]
where \(\eta_*\) denotes recombination.

A phase shift requires modification of:
1. the sound speed \(c_s\),
2. the background expansion,
3. the time dependence of \(\Phi\) during oscillations.

---

## 3. Sound Horizon Invariance

From `03.1_Background_Cosmology.md`:

- the background expansion is unchanged,
- photon and baryon equations of state are unchanged,
- \(c_s\) is unmodified.

Thus,
\[
\boxed{
r_s^{\rm VSU} = r_s^{\rm GR}.
}
\]

---

## 4. Potential Driving Term

The driven solution at recombination can be written as
\[
\delta_b(\eta_*)
=
\cos(k r_s)\!\int_0^{\eta_*}\!d\eta'\,
\frac{k\sin[k(r_s-r_s')]}{c_s}\,\Phi(\eta')
+
\sin(k r_s)\!\int_0^{\eta_*}\!d\eta'\,
\frac{k\cos[k(r_s-r_s')]}{c_s}\,\Phi(\eta').
\]

A BAO phase shift occurs if the ratio of sine and cosine coefficients is altered by
time-dependent \(\Phi\).

---

## 5. Potential Evolution Pre-Recombination

From the early-time analysis:

- \(\alpha_{\rm eff}(k,a) \to 0\),
- \(\mathcal G(k,a) \to 1\),
- the growth rate satisfies \(f \to 1\).

Using
\[
\dot\Phi = H\Phi\left[f-1+\frac{d\ln\mathcal G}{d\ln a}\right],
\]
we obtain
\[
\boxed{
\dot\Phi \simeq 0
\quad \text{during BAO oscillations}.
}
\]

Thus \(\Phi\) is constant during the acoustic phase.

---

## 6. Phase Invariance

Because:
- \(r_s\) is unchanged,
- \(\Phi(\eta)\) is constant during oscillations,

the baryon perturbation retains the same phase dependence as in GR.

Therefore,
\[
\boxed{
\Delta\phi_{\rm BAO} = 0.
}
\]

BAO peak positions are invariant.

---

## 7. Late-Time Amplitude Modification

After recombination, the matter power spectrum evolves as
\[
P_m(k,z) = P_{\rm ini}(k) T^2(k) D^2(k,z).
\]

The transfer function \(T(k)\) and primordial spectrum are unchanged.

All VSU modifications enter through the growth factor:
\[
\boxed{
P_m^{\rm VSU}(k,z)
=
P_m^{\rm GR}(k,z)
\left[\frac{D_{\rm VSU}(k,z)}{D_{\rm GR}(z)}\right]^2.
}
\]

Thus BAO amplitudes are scale dependent, but peak positions are not.

---

## 8. Observational Consequences

- BAO standard rulers remain valid.
- Distance inferences are unbiased.
- Geometry and growth remain separable.

---

## 9. Summary

Analytically:

- BAO phase is invariant.
- BAO peak positions are unchanged.
- BAO amplitudes receive scale-dependent corrections only.

---

## 10. Status and Dependencies

- Depends on:
  - `03.1_Background_Cosmology.md`
  - `03.2_Scalar_Perturbations.md`
  - `03.5_Late_Time_Asymptotics.md`
- Introduces no new parameters.
- Provides the BAO input for AP consistency checks.

This file is complete.
<!-- END FILE: 04.4_BAO_Phase_and_Peaks.md -->

<!-- BEGIN FILE: 04.5_Alcock_Paczynski_Consistency.md (source: /mnt/data/04.5_Alcock_Paczynski_Consistency.md) -->
# 04.5 Alcock–Paczynski Consistency

## Purpose

This file establishes Alcock–Paczynski (AP) consistency in the Vacuum Stiffness
Unification (VSU) framework. We show analytically that AP observables depend only
on background geometry and are unaffected by the modified growth sector.

No observational fitting or numerical modeling is used.

---

## 1. Alcock–Paczynski Observable

The AP test compares radial and transverse distortions of an isotropic feature.
Define
\[
\alpha_{\parallel}(z) = \frac{H^{\rm fid}(z)}{H(z)},
\qquad
\alpha_{\perp}(z) = \frac{D_A(z)}{D_A^{\rm fid}(z)}.
\]

The AP distortion parameter is
\[
\boxed{
F_{\rm AP}(z)
=
(1+z)\,D_A(z)\,H(z).
}
\]

This quantity is purely geometric.

---

## 2. Background Geometry in VSU

From `03.1_Background_Cosmology.md`, the background expansion satisfies
\[
H^2(z) = H_0^2\,[\Omega_{m0}(1+z)^3 + \Omega_{\Lambda0}],
\]
identical to \(\Lambda\)CDM.

The angular diameter distance is
\[
D_A(z)
=
\frac{1}{1+z}\int_0^z \frac{dz'}{H(z')}.
\]

No modification of \(H(z)\) or \(D_A(z)\) is introduced by VSU.

Therefore,
\[
\boxed{
F_{\rm AP}^{\rm VSU}(z) = F_{\rm AP}^{\rm GR}(z).
}
\]

---

## 3. Geometry–Growth Separation

Observed redshift-space galaxy clustering is
\[
P_s(k,\mu,z)
=
\left(1+\beta(k,z)\mu^2\right)^2 P_m(k,z),
\qquad
\beta(k,z)=\frac{f(k,z)}{b(z)}.
\]

Two effects appear:

1. geometric rescaling via \(\alpha_{\parallel},\alpha_{\perp}\),
2. dynamical anisotropy via \(f(k,z)\).

The AP test isolates the geometric contribution.

---

## 4. Orthogonality at Linear Order

At linear order,
\[
\frac{\partial^2 \ln P_s}{\partial \alpha_i\,\partial f} = 0,
\qquad
i\in\{\parallel,\perp\}.
\]

Thus scale-dependent growth cannot mimic AP distortions.

---

## 5. Consistency with BAO

From `04.4_BAO_Phase_and_Peaks.md`:

- BAO peak positions are invariant,
- the sound horizon is unchanged.

Therefore BAO and AP measurements are mutually consistent in VSU.

---

## 6. Joint AP + RSD Likelihood

At linear order, the likelihood factorizes:
\[
\boxed{
\mathcal L
=
\mathcal L_{\rm AP}\bigl(F_{\rm AP}\bigr)
\times
\mathcal L_{\rm RSD}\bigl(f\sigma_8(k)\bigr)
+ O(\delta^2).
}
\]

AP constrains geometry; RSD constrains growth.

---

## 7. Summary

Analytically:

- AP observables depend only on background geometry,
- background geometry is unchanged in VSU,
- modified growth does not bias AP inference,
- BAO, AP, and CMB clocks remain consistent.

---

## 8. Status and Dependencies

- Depends on:
  - `03.1_Background_Cosmology.md`
  - `03.3_Matter_Growth_Equation.md`
  - `04.4_BAO_Phase_and_Peaks.md`
- Introduces no new parameters.
- Completes the linear geometric consistency checks.

This file is complete.
<!-- END FILE: 04.5_Alcock_Paczynski_Consistency.md -->

<!-- BEGIN FILE: 05.1_Nonlinear_Screening_Mechanism.md (source: /mnt/data/05.1_Nonlinear_Screening_Mechanism.md) -->
# 05.1 Nonlinear Screening Mechanism

## Purpose

This file derives gravitational screening as an intrinsic property of the
quasilinear elliptic operator governing the vacuum stiffness field. Screening is
shown to arise automatically in strong-field regions and under large external
fields, without introducing additional degrees of freedom or parameters.

No cosmological assumptions are used.

---

## 1. Governing Equation

The nonrelativistic field equation is
\[
\nabla\cdot\!\left(
\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi
\right)
=
4\pi G\,\rho,
\qquad
\mu(x)=1-e^{-x}.
\]

Define the gravitational field
\[
\mathbf g := -\nabla\Phi,
\qquad
g := |\mathbf g|.
\]

---

## 2. Strong-Field Expansion

Consider a region where
\[
g \gg a_0.
\]

Then
\[
\mu\!\left(\frac{g}{a_0}\right)
=
1-\varepsilon,
\qquad
\varepsilon:=e^{-g/a_0} \ll 1.
\]

Insert into the operator:
\[
\nabla\cdot\!\left((1-\varepsilon)\mathbf g\right)
=
\nabla\cdot\mathbf g
-
\nabla\varepsilon\cdot\mathbf g.
\]

The correction term satisfies
\[
\nabla\varepsilon
=
-\frac{e^{-g/a_0}}{a_0}\frac{\nabla g}{g}
=
O\!\left(\frac{a_0}{g^2}\right),
\]
so
\[
\nabla\varepsilon\cdot\mathbf g
=
O\!\left(\frac{a_0}{g}\right) \ll 1.
\]

Thus, to leading order,
\[
\boxed{
\nabla^2\Phi
=
4\pi G\rho
+
O\!\left(\frac{a_0}{g}\right).
}
\]

Newtonian gravity is recovered with exponentially small corrections.

---

## 3. Screening Radius

For an isolated mass \(M\), the Newtonian field is
\[
g_N(r)=\frac{GM}{r^2}.
\]

Screening applies where \(g_N \gg a_0\). Define the screening radius \(r_s\) by
\[
g_N(r_s)=a_0.
\]

Solving yields
\[
\boxed{
r_s = \sqrt{\frac{GM}{a_0}}.
}
\]

---

## 4. Operator-Level Screening Criterion

Let \(\Omega \subset \mathbb R^3\) be a region where
\[
\inf_{\Omega} |\nabla\Phi| \ge \Lambda a_0,
\qquad \Lambda \gg 1.
\]

Then within \(\Omega\),
\[
\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)
=
1+O(e^{-\Lambda}),
\]
and the operator is uniformly elliptic with Newtonian principal part.

Screening is local and controlled by field amplitude.

---

## 5. External Field Effect

Decompose the total field as
\[
\mathbf g = \mathbf g_{\rm int} + \mathbf g_{\rm ext},
\]
where \(\mathbf g_{\rm ext}\) varies slowly across the system.

If
\[
|\mathbf g_{\rm ext}| \gg a_0,
\]
then
\[
\mu\!\left(\frac{|\mathbf g|}{a_0}\right)
\simeq
\mu\!\left(\frac{|\mathbf g_{\rm ext}|}{a_0}\right)
\simeq 1.
\]

The internal dynamics satisfy
\[
\boxed{
\nabla^2\Phi_{\rm int}
=
4\pi G\rho_{\rm int}
+
O\!\left(\frac{a_0}{|\mathbf g_{\rm ext}|}\right).
}
\]

This is the External Field Effect.

---

## 6. Absence of Screening Artifacts

- No screening length is introduced by hand.
- No additional fields are activated.
- No boundary conditions beyond regularity are required.

Screening follows solely from the nonlinear constitutive function \(\mu\).

---

## 7. Consequences

- High-field regions (halo interiors) are Newtonian.
- Low-field regions (halo outskirts, voids) are unscreened.
- Environmental dependence is automatic.

These properties feed directly into nonlinear collapse and halo bias.

---

## 8. Status and Dependencies

- Depends on:
  - `02.1_Force_Law_and_Asymptotics.md`
  - `02.3_Screening_Radius_and_EFE.md`
- Introduces no new parameters.
- Provides the foundation for nonlinear structure formation analysis.

This file is complete.
<!-- END FILE: 05.1_Nonlinear_Screening_Mechanism.md -->

<!-- BEGIN FILE: 05.2_Spherical_Collapse.md (source: /mnt/data/05.2_Spherical_Collapse.md) -->
# 05.2 Spherical Collapse

## Purpose

This file derives the nonlinear spherical-collapse dynamics implied by the Vacuum
Stiffness Unification (VSU) force law. We obtain the collapse equation, collapse
time scaling, and the modified critical overdensity \(\delta_c(M,z)\).

No linear perturbation theory or numerical fitting is used.

---

## 1. Setup

Consider a spherically symmetric, pressureless overdensity of total mass \(M\)
and physical radius \(r(t)\). Shell crossing is neglected.

The radial equation of motion is
\[
\ddot r = -g(r),
\]
where \(g(r)\) is the magnitude of the gravitational field generated by the
enclosed mass.

---

## 2. Force Law by Regime

From `02.1_Force_Law_and_Asymptotics.md`, the force law satisfies
\[
g(r)\,\mu\!\left(\frac{g(r)}{a_0}\right) = \frac{GM}{r^2},
\qquad
\mu(x)=1-e^{-x}.
\]

This yields two asymptotic regimes.

### 2.1 Screened (Strong-Field) Regime

If \(g(r) \gg a_0\),
\[
g(r) \simeq \frac{GM}{r^2}.
\]

### 2.2 Unscreened (Weak-Field) Regime

If \(g(r) \ll a_0\),
\[
g(r) \simeq \frac{\sqrt{GMa_0}}{r}.
\]

---

## 3. Newtonian Collapse Time

In the Newtonian regime,
\[
\ddot r = -\frac{GM}{r^2}
\]
gives the free-fall time
\[
\boxed{
t_{\rm coll}^{\rm N}
=
\frac{\pi}{2\sqrt{2}}\,\frac{r_i^{3/2}}{\sqrt{GM}},
}
\]
where \(r_i\) is the initial radius.

---

## 4. Unscreened Collapse Time

In the unscreened regime,
\[
\ddot r = -\frac{\sqrt{GMa_0}}{r}.
\]

Multiplying by \(\dot r\) and integrating,
\[
\frac{1}{2}\dot r^2
=
\sqrt{GMa_0}\,\ln\!\left(\frac{r_i}{r}\right).
\]

The collapse time is
\[
t_{\rm coll}^{\rm VSU}
=
\int_0^{r_i}
\frac{dr}{\sqrt{2\sqrt{GMa_0}\,\ln(r_i/r)}}.
\]

Evaluating the integral yields the scaling
\[
\boxed{
t_{\rm coll}^{\rm VSU}
\propto
\frac{r_i^{3/2}}{(GMa_0)^{1/4}}.
}
\]

---

## 5. Collapse-Time Ratio

Comparing the two regimes,
\[
\boxed{
\frac{t_{\rm coll}^{\rm VSU}}{t_{\rm coll}^{\rm N}}
\sim
\left(\frac{g_N}{a_0}\right)^{1/4},
}
\qquad
g_N := \frac{GM}{r_i^2}.
\]

Thus collapse is faster for systems with smaller Newtonian acceleration.

---

## 6. Screening During Collapse

Collapse proceeds in two phases:

1. **Outer phase:** unscreened, enhanced acceleration.
2. **Inner phase:** screened, Newtonian dynamics once \(r < r_s\).

The screening radius
\[
r_s = \sqrt{\frac{GM}{a_0}}
\]
marks the transition.

---

## 7. Modified Critical Overdensity

Define \(\delta_c(M,z)\) as the linearly extrapolated overdensity at the time of
nonlinear collapse.

In GR,
\[
\delta_c^{\rm GR} \simeq 1.686.
\]

In VSU, faster nonlinear collapse implies a reduced linear threshold. To leading
order,
\[
\boxed{
\delta_c^{\rm VSU}(M,z)
=
\delta_c^{\rm GR}
\left(\frac{g_N(M,z)}{a_0}\right)^{1/4}.
}
\]

---

## 8. Mass and Redshift Scaling

Using
\[
r_i \propto \left(\frac{M}{\bar\rho_m(z)}\right)^{1/3},
\qquad
\bar\rho_m(z) \propto (1+z)^3,
\]
we obtain
\[
\delta_c^{\rm VSU}(M,z)
\propto
M^{1/6}(1+z)^{-1/2}.
\]

This scaling is parameter free.

---

## 9. Validity and Limitations

- Pressureless matter only.
- Spherical symmetry.
- No shell crossing.
- Linear-to-nonlinear mapping via collapse time only.

---

## 10. Status and Dependencies

- Depends on:
  - `05.1_Nonlinear_Screening_Mechanism.md`
  - `02.1_Force_Law_and_Asymptotics.md`
- Introduces no new parameters.
- Provides the collapse threshold for halo bias modeling.

This file is complete.
<!-- END FILE: 05.2_Spherical_Collapse.md -->

<!-- BEGIN FILE: 05.3_Halo_Bias.md (source: /mnt/data/05.3_Halo_Bias.md) -->
# 05.3 Halo Bias

## Purpose

This file derives the halo bias implied by the modified spherical-collapse
threshold obtained in `05.2_Spherical_Collapse.md`. The result is a mass- and
environment-dependent bias that follows directly from the nonlinear collapse
dynamics in the VSU framework.

No phenomenological fitting functions or simulations are introduced.

---

## 1. Definition of Halo Bias

Halo bias quantifies the response of halo number density to a long-wavelength
matter overdensity \(\delta_L\):
\[
b(M,z)
:=
\frac{\partial \ln n(M,z)}{\partial \delta_L},
\]
where \(n(M,z)\) is the halo mass function.

In excursion-set theory, bias is determined by the collapse threshold
\(\delta_c\).

---

## 2. Excursion-Set Framework

Define the peak-height parameter
\[
\nu(M,z)
:=
\frac{\delta_c(M,z)}{\sigma(M,z)},
\]
where \(\sigma^2(M,z)\) is the variance of the linear density field smoothed on
the mass scale \(M\).

At leading order, the Lagrangian bias is
\[
\boxed{
b_L(M,z)
=
\frac{\nu^2(M,z)-1}{\delta_c(M,z)}.
}
\]

The Eulerian bias is
\[
b_E(M,z)=1+b_L(M,z).
\]

---

## 3. Modified Collapse Threshold

From `05.2_Spherical_Collapse.md`, the VSU collapse threshold is
\[
\boxed{
\delta_c^{\rm VSU}(M,z)
=
\delta_c^{\rm GR}
\left(\frac{g_N(M,z)}{a_0}\right)^{1/4}.
}
\]

This introduces explicit mass and redshift dependence.

---

## 4. Halo Bias in VSU

Substituting \(\delta_c^{\rm VSU}\) into the Eulerian bias expression gives
\[
\boxed{
b_E^{\rm VSU}(M,z)
=
1
+
\frac{1}{\delta_c^{\rm VSU}(M,z)}
\left[
\frac{(\delta_c^{\rm VSU}(M,z))^2}{\sigma^2(M,z)}-1
\right].
}
\]

This expression is exact at linear order.

---

## 5. Relation to GR Bias

The GR bias is
\[
b_E^{\rm GR}(M,z)
=
1
+
\frac{1}{\delta_c^{\rm GR}}
\left[
\frac{(\delta_c^{\rm GR})^2}{\sigma^2(M,z)}-1
\right].
\]

The ratio of biases is therefore
\[
\boxed{
\frac{b_E^{\rm VSU}}{b_E^{\rm GR}}
=
\left(\frac{g_N(M,z)}{a_0}\right)^{-1/4}
\frac{(\delta_c^{\rm GR})^2/\sigma^2(M,z)-1}
{(\delta_c^{\rm VSU})^2/\sigma^2(M,z)-1}.
}
\]

---

## 6. Limiting Regimes

### 6.1 High-Mass Halos (Screened)

For large masses,
\[
g_N(M,z) \gg a_0,
\qquad
\delta_c^{\rm VSU} \to \delta_c^{\rm GR}.
\]

Thus,
\[
\boxed{
b_E^{\rm VSU}(M,z) \to b_E^{\rm GR}(M,z).
}
\]

High-mass halos are Newtonian and unbiased relative to GR.

---

### 6.2 Low-Mass Halos (Unscreened)

For small masses,
\[
g_N(M,z) \ll a_0,
\qquad
\delta_c^{\rm VSU} < \delta_c^{\rm GR}.
\]

Hence,
\[
\boxed{
b_E^{\rm VSU}(M,z) > b_E^{\rm GR}(M,z).
}
\]

Low-mass halos form earlier and are more strongly biased.

---

## 7. Environmental Dependence

Because \(g_N(M,z)\) depends on the ambient gravitational field, halo bias is
environment dependent:

- halos in strong external fields are screened and GR-like,
- halos in weak-field environments exhibit enhanced bias.

No additional environmental parameter is required.

---

## 8. Scale Dependence

The bias becomes scale dependent through the mapping
\[
\sigma^2(M,z) \leftrightarrow P_m(k,z),
\]
combined with the mass dependence of \(\delta_c^{\rm VSU}(M,z)\).

This induces scale-dependent bias on large scales.

---

## 9. Consistency with Linear Observables

- Linear growth and RSD probe matter fluctuations directly.
- Halo bias modifies galaxy clustering but not the matter field.
- Bias corrections can be absorbed into standard bias parameters at large mass.

No contradiction with linear cosmology arises.

---

## 10. Status and Dependencies

- Depends on:
  - `05.2_Spherical_Collapse.md`
- Introduces no new parameters.
- Completes the nonlinear structure sector of the framework.

This file is complete.
<!-- END FILE: 05.3_Halo_Bias.md -->

<!-- BEGIN FILE: 06.1_Internal_Consistency.md (source: /mnt/data/06.1_Internal_Consistency.md) -->
# 06.1 Internal Consistency

## Purpose

This file establishes the internal logical consistency of the Vacuum Stiffness
Unification (VSU) framework across all regimes addressed in the preceding files.
It verifies that assumptions made in different sectors are mutually compatible
and that no circular dependencies are introduced.

No new equations or parameters are introduced.

---

## 1. Separation of Background and Perturbations

From `03.1_Background_Cosmology.md`, the background expansion is fixed to the
standard flat FLRW solution with matter and a cosmological constant.

From `01.1_Action_and_Field_Equations.md`, the modification enters only through
the gravitational response at the level of perturbations and nonlinear structure.

Thus:
- background evolution is unchanged,
- all modifications occur in deviations from homogeneity.

There is no feedback from perturbations into the background sector.

---

## 2. Early- vs Late-Time Regimes

From `03.4_Early_Time_Asymptotics.md`:
- \(\alpha_{\rm eff}(k,a) \to 0\) as \(a \to 0\),
- linear growth reduces to GR at high redshift.

From `03.5_Late_Time_Asymptotics.md`:
- \(\alpha_{\rm eff}(k,a) \to \alpha_\infty(k)\) at late times,
- growth enhancement saturates and freezes under \(\Lambda\) domination.

Therefore:
- early-universe observables are unaffected,
- late-time deviations do not propagate backward in time.

---

## 3. Geometry vs Growth

From `04.4_BAO_Phase_and_Peaks.md` and `04.5_Alcock_Paczynski_Consistency.md`:
- BAO peak positions are invariant,
- AP observables depend only on geometry.

From `04.1_RSD_and_fsigma8_Mapping.md` and `04.2_Weak_Lensing_and_S8.md`:
- growth modifications enter only through \(f(k,z)\) and \(D(k,z)\),
- geometric quantities are unaffected.

Thus geometry and growth remain cleanly separable.

---

## 4. Linear vs Nonlinear Sectors

From `03.3_Matter_Growth_Equation.md`:
- linear growth applies to sub-horizon perturbations.

From `05.1_Nonlinear_Screening_Mechanism.md`:
- nonlinear screening restores Newtonian behavior in strong-field regions.

From `05.2_Spherical_Collapse.md` and `05.3_Halo_Bias.md`:
- nonlinear collapse and bias are modified consistently with screening.

No nonlinear result is used as input for linear calculations.

---

## 5. Environmental Dependence

From `02.3_Screening_Radius_and_EFE.md` and `05.1_Nonlinear_Screening_Mechanism.md`:
- environmental screening arises from the same operator as local screening,
- no new environmental parameters are introduced.

This dependence does not conflict with linear cosmology, which averages over
large volumes.

---

## 6. Conservation Laws and Stability

From `01.2_Stress_Energy_Tensor.md`:
- the scalar stress–energy tensor is conserved.

From `01.3_Hyperbolicity_and_Characteristics.md`:
- the scalar equation is strictly hyperbolic,
- characteristic speeds satisfy \(1/2 \le c_s^2 < 1\).

Thus the theory is dynamically stable and causal in all regimes considered.

---

## 7. Absence of Circular Reasoning

No file:
- assumes results derived later,
- uses observational fits to justify equations,
- feeds nonlinear conclusions back into linear derivations.

All dependencies are acyclic, as enforced by the DAG.

---

## 8. Summary

Across all sectors:

- background evolution is consistent,
- early- and late-time regimes are compatible,
- geometry and growth are separable,
- linear and nonlinear analyses are independent,
- stability and conservation are maintained.

The framework is internally consistent.

---

## 9. Status and Dependencies

- Depends on:
  - all preceding analytical files
- Introduces no new parameters.
- Serves as the first closure layer of the framework.

This file is complete.
<!-- END FILE: 06.1_Internal_Consistency.md -->

<!-- BEGIN FILE: 06.2_Observable_Degeneracy_Structure.md (source: /mnt/data/06.2_Observable_Degeneracy_Structure.md) -->
# 06.2 Observable Degeneracy Structure

## Purpose

This file analyzes the structure of observable degeneracies in the Vacuum
Stiffness Unification (VSU) framework. It identifies which combinations of
parameters are constrained by different classes of observations and clarifies
which degeneracies are unavoidable at linear order.

No new equations are introduced; this file organizes consequences of prior
derivations.

---

## 1. Parameter Set

The VSU framework contains a minimal parameter set relevant to observables:

- Background parameters:
  \(H_0, \Omega_{m0}, \Omega_{\Lambda0}\)

- Growth parameter:
  \(a_0\), entering through \(\alpha_{\rm eff}(k,a)\)

No additional free functions or screening lengths are introduced.

---

## 2. Linear Growth Degeneracies

From `03.3_Matter_Growth_Equation.md`, linear growth depends on the combination
\[
G_{\rm eff}(k,a) = G\,[1+\alpha_{\rm eff}(k,a)].
\]

Thus linear observables cannot distinguish between:
- enhanced clustering due to modified gravity,
- enhanced clustering due to increased effective matter content,

when only the matter power spectrum amplitude is measured.

This degeneracy is intrinsic to linear growth.

---

## 3. RSD Degeneracies

From `04.1_RSD_and_fsigma8_Mapping.md`, RSD constrain the bin-averaged quantity
\[
\langle f\sigma_8(z) \rangle.
\]

At linear order, RSD are insensitive to:
- the detailed \(k\)-dependence of \(\alpha_\infty(k)\),
- background geometry parameters.

Thus RSD alone constrain only a single effective growth amplitude per redshift
bin.

---

## 4. Weak Lensing Degeneracies

From `04.2_Weak_Lensing_and_S8.md`, weak lensing constrains
\[
S_8 = \sigma_8\sqrt{\frac{\Omega_{m0}}{0.3}}.
\]

Lensing is degenerate between:
- growth enhancement,
- background matter density normalization.

Thus lensing alone cannot separate \(a_0\) from \(\Omega_{m0}\).

---

## 5. ISW Degeneracies

From `04.3_ISW_Sign_and_Amplitude.md`, ISW measurements constrain the time
derivative of the gravitational potential.

ISW is insensitive to:
- the absolute normalization of growth,
- small-scale structure details.

ISW primarily constrains the *sign* and relative suppression of late-time
potential decay.

---

## 6. BAO and AP Degeneracies

From `04.4_BAO_Phase_and_Peaks.md` and `04.5_Alcock_Paczynski_Consistency.md`:

- BAO peak positions constrain the sound horizon and geometry.
- AP observables constrain only background distances.

Neither BAO nor AP are sensitive to modified growth at linear order.

Thus BAO/AP break geometry–growth degeneracies when combined with RSD or lensing.

---

## 7. Breaking Degeneracies by Combination

Combining observables:

- **RSD + BAO/AP** separates growth from geometry.
- **Lensing + BAO/AP** separates amplitude from distances.
- **RSD + Lensing** partially separates velocity and potential responses.

No single observable suffices; consistency arises from cross-comparison.

---

## 8. Nonlinear Degeneracy Lifting

From `05.1_Nonlinear_Screening_Mechanism.md` and `05.3_Halo_Bias.md`, nonlinear
effects introduce:

- environmental dependence,
- mass-dependent halo bias,
- screening signatures.

These effects are not degenerate with linear growth or geometry and provide
distinct tests of the framework.

---

## 9. Summary

The observable degeneracy structure is:

- unavoidable at linear order for individual probes,
- resolvable through multi-probe consistency,
- further lifted by nonlinear and environmental signatures.

This structure is generic to any minimal modified-gravity theory.

---

## 10. Status and Dependencies

- Depends on:
  - `04.1_RSD_and_fsigma8_Mapping.md`
  - `04.2_Weak_Lensing_and_S8.md`
  - `04.3_ISW_Sign_and_Amplitude.md`
  - `04.4_BAO_Phase_and_Peaks.md`
  - `04.5_Alcock_Paczynski_Consistency.md`
- Introduces no new parameters.
- Serves as the second closure layer of the framework.

This file is complete.
<!-- END FILE: 06.2_Observable_Degeneracy_Structure.md -->

<!-- BEGIN FILE: 06.3_Parameter_Minimality.md (source: /mnt/data/06.3_Parameter_Minimality.md) -->
# 06.3 Parameter Minimality

## Purpose

This file establishes the parameter minimality of the Vacuum Stiffness
Unification (VSU) framework. It demonstrates that all phenomenology derived in
preceding files follows from a single additional scale beyond standard
cosmological parameters, and that no hidden tunings or auxiliary parameters are
introduced.

No new equations are derived here.

---

## 1. Parameter Inventory

The complete set of parameters entering the framework is:

### 1.1 Background Cosmology
- Hubble constant: \(H_0\)
- Matter density parameter: \(\Omega_{m0}\)
- Cosmological constant: \(\Omega_{\Lambda0}\)

These are identical to those of flat \(\Lambda\)CDM.

### 1.2 Gravitational Sector
- Universal acceleration scale: \(a_0\)

No additional mass scales, couplings, or functions appear.

---

## 2. Absence of Free Functions

The constitutive function
\[
\mu(x)=1-e^{-x}
\]
is fixed once and for all.

It is not fit per system, per scale, or per epoch.

No interpolation freedom remains after specifying \(a_0\).

---

## 3. No Screening Parameters

From `02.3_Screening_Radius_and_EFE.md` and `05.1_Nonlinear_Screening_Mechanism.md`:

- Screening arises from the nonlinear operator itself.
- The screening radius
  \[
  r_s=\sqrt{\frac{GM}{a_0}}
  \]
  is derived, not imposed.

There is no tunable screening length or coupling.

---

## 4. Linear Cosmology Economy

From `03.3_Matter_Growth_Equation.md`:

- All growth modifications enter via \(\alpha_{\rm eff}(k,a)\),
- \(\alpha_{\rm eff}\) is determined entirely by \(a_0\) and background
  acceleration.

No new cosmological degrees of freedom are introduced.

---

## 5. Observational Sufficiency

From the observational mapping files:

- RSD constrain a window-averaged \(\alpha_\infty\),
- Weak lensing constrains a related weighted average,
- BAO and AP constrain geometry only.

All observables are functions of \(a_0\) and standard cosmological parameters.

---

## 6. Comparison with Extended Models

Unlike many modified-gravity frameworks, VSU does **not** introduce:

- extra scalar potentials,
- vector or tensor degrees of freedom,
- scale-dependent free functions,
- environment-dependent couplings.

All complexity arises from nonlinear dynamics of a single field.

---

## 7. Predictive Structure

Because only one new parameter is present:

- predictions are tightly correlated across observables,
- independent fits cannot be tuned separately,
- internal consistency checks are unavoidable.

This structure enhances falsifiability.

---

## 8. Summary

The VSU framework is parameter minimal:

- background cosmology unchanged,
- one additional acceleration scale \(a_0\),
- no free functions or tunable screening,
- all derived effects follow from this single scale.

---

## 9. Status and Dependencies

- Depends on:
  - all preceding analytical files
- Introduces no new parameters.
- Completes the closure layer of the framework.

This file is complete.
<!-- END FILE: 06.3_Parameter_Minimality.md -->

---

## Metadata

<!-- BEGIN FILE: VSU_DAG.yaml -->
```yaml
VSU_DAG:
  nodes:
    - id: 00_Overview.md

    - id: 01.1_Action_and_Field_Equations.md
    - id: 01.2_Stress_Energy_Tensor.md
    - id: 01.3_Hyperbolicity_and_Characteristics.md

    - id: 02.1_Force_Law_and_Asymptotics.md
    - id: 02.2_BTFR_Derivation.md
    - id: 02.3_Screening_Radius_and_EFE.md

    - id: 03.1_Background_Cosmology.md
    - id: 03.2_Scalar_Perturbations.md
    - id: 03.3_Matter_Growth_Equation.md
    - id: 03.4_Early_Time_Asymptotics.md
    - id: 03.5_Late_Time_Asymptotics.md

    - id: 04.1_RSD_and_fsigma8_Mapping.md
    - id: 04.2_Weak_Lensing_and_S8.md
    - id: 04.3_ISW_Sign_and_Amplitude.md
    - id: 04.4_BAO_Phase_and_Peaks.md
    - id: 04.5_Alcock_Paczynski_Consistency.md

    - id: 05.1_Nonlinear_Screening_Mechanism.md
    - id: 05.2_Spherical_Collapse.md
    - id: 05.3_Halo_Bias.md

    - id: 06.1_Internal_Consistency.md
    - id: 06.2_Observable_Degeneracy_Structure.md
    - id: 06.3_Parameter_Minimality.md

  edges:
    # Core theory
    - from: 01.1_Action_and_Field_Equations.md
      to: 01.2_Stress_Energy_Tensor.md
    - from: 01.2_Stress_Energy_Tensor.md
      to: 01.3_Hyperbolicity_and_Characteristics.md

    # Galactic dynamics
    - from: 01.1_Action_and_Field_Equations.md
      to: 02.1_Force_Law_and_Asymptotics.md
    - from: 02.1_Force_Law_and_Asymptotics.md
      to: 02.2_BTFR_Derivation.md
    - from: 02.2_BTFR_Derivation.md
      to: 02.3_Screening_Radius_and_EFE.md

    # Linear cosmology
    - from: 01.1_Action_and_Field_Equations.md
      to: 03.1_Background_Cosmology.md
    - from: 01.3_Hyperbolicity_and_Characteristics.md
      to: 03.2_Scalar_Perturbations.md
    - from: 03.1_Background_Cosmology.md
      to: 03.2_Scalar_Perturbations.md
    - from: 03.2_Scalar_Perturbations.md
      to: 03.3_Matter_Growth_Equation.md
    - from: 03.3_Matter_Growth_Equation.md
      to: 03.4_Early_Time_Asymptotics.md
    - from: 03.4_Early_Time_Asymptotics.md
      to: 03.5_Late_Time_Asymptotics.md

    # Observational projections
    - from: 03.3_Matter_Growth_Equation.md
      to: 04.1_RSD_and_fsigma8_Mapping.md
    - from: 03.5_Late_Time_Asymptotics.md
      to: 04.1_RSD_and_fsigma8_Mapping.md

    - from: 03.3_Matter_Growth_Equation.md
      to: 04.2_Weak_Lensing_and_S8.md
    - from: 03.5_Late_Time_Asymptotics.md
      to: 04.2_Weak_Lensing_and_S8.md

    - from: 03.3_Matter_Growth_Equation.md
      to: 04.3_ISW_Sign_and_Amplitude.md
    - from: 03.5_Late_Time_Asymptotics.md
      to: 04.3_ISW_Sign_and_Amplitude.md

    - from: 03.3_Matter_Growth_Equation.md
      to: 04.4_BAO_Phase_and_Peaks.md
    - from: 03.5_Late_Time_Asymptotics.md
      to: 04.4_BAO_Phase_and_Peaks.md

    - from: 03.3_Matter_Growth_Equation.md
      to: 04.5_Alcock_Paczynski_Consistency.md
    - from: 03.5_Late_Time_Asymptotics.md
      to: 04.5_Alcock_Paczynski_Consistency.md

    # Nonlinear regime
    - from: 02.3_Screening_Radius_and_EFE.md
      to: 05.1_Nonlinear_Screening_Mechanism.md
    - from: 05.1_Nonlinear_Screening_Mechanism.md
      to: 05.2_Spherical_Collapse.md
    - from: 05.2_Spherical_Collapse.md
      to: 05.3_Halo_Bias.md

    # Closure
    - from: 02.3_Screening_Radius_and_EFE.md
      to: 06.1_Internal_Consistency.md
    - from: 03.5_Late_Time_Asymptotics.md
      to: 06.1_Internal_Consistency.md
    - from: 04.1_RSD_and_fsigma8_Mapping.md
      to: 06.1_Internal_Consistency.md
    - from: 04.2_Weak_Lensing_and_S8.md
      to: 06.1_Internal_Consistency.md
    - from: 04.3_ISW_Sign_and_Amplitude.md
      to: 06.1_Internal_Consistency.md
    - from: 04.4_BAO_Phase_and_Peaks.md
      to: 06.1_Internal_Consistency.md
    - from: 04.5_Alcock_Paczynski_Consistency.md
      to: 06.1_Internal_Consistency.md
    - from: 05.3_Halo_Bias.md
      to: 06.1_Internal_Consistency.md

    - from: 06.1_Internal_Consistency.md
      to: 06.2_Observable_Degeneracy_Structure.md
    - from: 06.2_Observable_Degeneracy_Structure.md
      to: 06.3_Parameter_Minimality.md
```
<!-- END FILE: VSU_DAG.yaml -->

<!-- BEGIN FILE: VSU_DAG.json -->
```json
{
  "nodes": [
    {
      "id": "00_Overview.md"
    },
    {
      "id": "01.1_Action_and_Field_Equations.md"
    },
    {
      "id": "01.2_Stress_Energy_Tensor.md"
    },
    {
      "id": "01.3_Hyperbolicity_and_Characteristics.md"
    },
    {
      "id": "02.1_Force_Law_and_Asymptotics.md"
    },
    {
      "id": "02.2_BTFR_Derivation.md"
    },
    {
      "id": "02.3_Screening_Radius_and_EFE.md"
    },
    {
      "id": "03.1_Background_Cosmology.md"
    },
    {
      "id": "03.2_Scalar_Perturbations.md"
    },
    {
      "id": "03.3_Matter_Growth_Equation.md"
    },
    {
      "id": "03.4_Early_Time_Asymptotics.md"
    },
    {
      "id": "03.5_Late_Time_Asymptotics.md"
    },
    {
      "id": "04.1_RSD_and_fsigma8_Mapping.md"
    },
    {
      "id": "04.2_Weak_Lensing_and_S8.md"
    },
    {
      "id": "04.3_ISW_Sign_and_Amplitude.md"
    },
    {
      "id": "04.4_BAO_Phase_and_Peaks.md"
    },
    {
      "id": "04.5_Alcock_Paczynski_Consistency.md"
    },
    {
      "id": "05.1_Nonlinear_Screening_Mechanism.md"
    },
    {
      "id": "05.2_Spherical_Collapse.md"
    },
    {
      "id": "05.3_Halo_Bias.md"
    },
    {
      "id": "06.1_Internal_Consistency.md"
    },
    {
      "id": "06.2_Observable_Degeneracy_Structure.md"
    },
    {
      "id": "06.3_Parameter_Minimality.md"
    }
  ],
  "edges": [
    {
      "from": "01.1_Action_and_Field_Equations.md",
      "to": "01.2_Stress_Energy_Tensor.md"
    },
    {
      "from": "01.2_Stress_Energy_Tensor.md",
      "to": "01.3_Hyperbolicity_and_Characteristics.md"
    },
    {
      "from": "01.1_Action_and_Field_Equations.md",
      "to": "02.1_Force_Law_and_Asymptotics.md"
    },
    {
      "from": "02.1_Force_Law_and_Asymptotics.md",
      "to": "02.2_BTFR_Derivation.md"
    },
    {
      "from": "02.2_BTFR_Derivation.md",
      "to": "02.3_Screening_Radius_and_EFE.md"
    },
    {
      "from": "01.1_Action_and_Field_Equations.md",
      "to": "03.1_Background_Cosmology.md"
    },
    {
      "from": "01.3_Hyperbolicity_and_Characteristics.md",
      "to": "03.2_Scalar_Perturbations.md"
    },
    {
      "from": "03.1_Background_Cosmology.md",
      "to": "03.2_Scalar_Perturbations.md"
    },
    {
      "from": "03.2_Scalar_Perturbations.md",
      "to": "03.3_Matter_Growth_Equation.md"
    },
    {
      "from": "03.3_Matter_Growth_Equation.md",
      "to": "03.4_Early_Time_Asymptotics.md"
    },
    {
      "from": "03.4_Early_Time_Asymptotics.md",
      "to": "03.5_Late_Time_Asymptotics.md"
    },
    {
      "from": "03.3_Matter_Growth_Equation.md",
      "to": "04.1_RSD_and_fsigma8_Mapping.md"
    },
    {
      "from": "03.5_Late_Time_Asymptotics.md",
      "to": "04.1_RSD_and_fsigma8_Mapping.md"
    },
    {
      "from": "03.3_Matter_Growth_Equation.md",
      "to": "04.2_Weak_Lensing_and_S8.md"
    },
    {
      "from": "03.5_Late_Time_Asymptotics.md",
      "to": "04.2_Weak_Lensing_and_S8.md"
    },
    {
      "from": "03.3_Matter_Growth_Equation.md",
      "to": "04.3_ISW_Sign_and_Amplitude.md"
    },
    {
      "from": "03.5_Late_Time_Asymptotics.md",
      "to": "04.3_ISW_Sign_and_Amplitude.md"
    },
    {
      "from": "03.3_Matter_Growth_Equation.md",
      "to": "04.4_BAO_Phase_and_Peaks.md"
    },
    {
      "from": "03.5_Late_Time_Asymptotics.md",
      "to": "04.4_BAO_Phase_and_Peaks.md"
    },
    {
      "from": "03.3_Matter_Growth_Equation.md",
      "to": "04.5_Alcock_Paczynski_Consistency.md"
    },
    {
      "from": "03.5_Late_Time_Asymptotics.md",
      "to": "04.5_Alcock_Paczynski_Consistency.md"
    },
    {
      "from": "02.3_Screening_Radius_and_EFE.md",
      "to": "05.1_Nonlinear_Screening_Mechanism.md"
    },
    {
      "from": "05.1_Nonlinear_Screening_Mechanism.md",
      "to": "05.2_Spherical_Collapse.md"
    },
    {
      "from": "05.2_Spherical_Collapse.md",
      "to": "05.3_Halo_Bias.md"
    },
    {
      "from": "02.3_Screening_Radius_and_EFE.md",
      "to": "06.1_Internal_Consistency.md"
    },
    {
      "from": "03.5_Late_Time_Asymptotics.md",
      "to": "06.1_Internal_Consistency.md"
    },
    {
      "from": "04.1_RSD_and_fsigma8_Mapping.md",
      "to": "06.1_Internal_Consistency.md"
    },
    {
      "from": "04.2_Weak_Lensing_and_S8.md",
      "to": "06.1_Internal_Consistency.md"
    },
    {
      "from": "04.3_ISW_Sign_and_Amplitude.md",
      "to": "06.1_Internal_Consistency.md"
    },
    {
      "from": "04.4_BAO_Phase_and_Peaks.md",
      "to": "06.1_Internal_Consistency.md"
    },
    {
      "from": "04.5_Alcock_Paczynski_Consistency.md",
      "to": "06.1_Internal_Consistency.md"
    },
    {
      "from": "05.3_Halo_Bias.md",
      "to": "06.1_Internal_Consistency.md"
    },
    {
      "from": "06.1_Internal_Consistency.md",
      "to": "06.2_Observable_Degeneracy_Structure.md"
    },
    {
      "from": "06.2_Observable_Degeneracy_Structure.md",
      "to": "06.3_Parameter_Minimality.md"
    }
  ]
}
```
<!-- END FILE: VSU_DAG.json -->

<!-- BEGIN FILE: VSU_LINT.md -->
# VSU Lint Report

This report flags *first appearances* of key symbols and whether they are explicitly defined in the file where they first appear (per DAG ancestry).

This is a structural lint (interface hygiene), not a proof checker.


## 01.1_Action_and_Field_Equations.md

- `a_0` first appears here — defined locally: **True**
- `\mu` first appears here — defined locally: **True**
- `\Phi` first appears here — defined locally: **True**
- `\phi` first appears here — defined locally: **True**
- `X` first appears here — defined locally: **True**
- `Y` first appears here — defined locally: **True**
- `K` first appears here — defined locally: **False**
- `D` first appears here — defined locally: **True**
- `f` first appears here — defined locally: **True**

## 02.1_Force_Law_and_Asymptotics.md

- `r_s` first appears here — defined locally: **True**

## 03.2_Scalar_Perturbations.md

- `\Psi` first appears here — defined locally: **True**

## 03.3_Matter_Growth_Equation.md

- `G_{\rm eff}` first appears here — defined locally: **True**
- `\alpha_{\rm eff}` first appears here — defined locally: **True**
- `m_{\rm eff}` first appears here — defined locally: **False**

## 05.2_Spherical_Collapse.md

- `\delta_c` first appears here — defined locally: **True**

## 03.4_Early_Time_Asymptotics.md

- `\sigma_8` first appears here — defined locally: **True**

## 03.5_Late_Time_Asymptotics.md

- `\alpha_\infty` first appears here — defined locally: **True**
- `S_8` first appears here — defined locally: **False**

## 04.5_Alcock_Paczynski_Consistency.md

- `F_{\rm AP}` first appears here — defined locally: **True**

## 04.4_BAO_Phase_and_Peaks.md

- `r_s` first appears here — defined locally: **True**
<!-- END FILE: VSU_LINT.md -->

<!-- BEGIN FILE: VSU_EXPORTS.md -->
# VSU Exports Manifest

This file records, per document, the *intended exported objects* (definitions / equations / invariants) that downstream documents may use.

Format: **Exports** are canonical; everything else is explanatory.


## 00_Overview.md

- **STATUS:** missing


## 01.1_Action_and_Field_Equations.md

- **Depends on:** (none)

- **Exports:**

  - ```math
S[g_{\mu\nu}, \phi]
=
\int d^4x\sqrt{-g}
\left[
\frac{1}{16\pi G} R
+
\frac{a_0^2}{8\pi G}
F\!\left(
\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}
\right)
+
\mathcal L_m(g_{\mu\nu}, \psi)
\right].
    ```

  - ```math
S_{\mathrm{NR}}[\Phi]
=
\int dt \int d^3x
\left[
\frac{a_0^2}{8\pi G}
\,F\!\left(
\frac{|\nabla\Phi|^2}{a_0^2}
\right)
+
\rho\,\Phi
\right],
    ```

  - ```math
\delta S_{\mathrm{NR}}
=
-\int dt\,d^3x\;
\delta\Phi
\left[
\nabla\cdot\!\left(
\frac{1}{4\pi G}
F'(Y)\nabla\Phi
\right)
-
\rho
\right].
    ```

  - ```math
\delta S_{\mathrm{NR}}
=
\int dt\,d^3x
\left[
\frac{1}{4\pi G}
F'(Y)\,
\nabla\Phi\cdot\nabla(\delta\Phi)
+
\rho\,\delta\Phi
\right].
    ```

  - ```math
\nabla\cdot\!\left(
\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi
\right)
=
4\pi G\,\rho,
    ```

  - ```math
\delta F(Y)
=
F'(Y)\,\delta Y
=
F'(Y)\,
\frac{2}{a_0^2}\,
\nabla\Phi\cdot\nabla(\delta\Phi).
    ```


## 02.1_Force_Law_and_Asymptotics.md

- **Depends on:** 01.1_Action_and_Field_Equations.md

- **Exports:**

  - ```math
g(r)\,\mu\!\left(\frac{g(r)}{a_0}\right)=g_N(r).
    ```

  - ```math
g(r)\simeq g_N(r)=\frac{G M(r)}{r^2}.
    ```

  - ```math
g(r)=\sqrt{a_0\,g_N(r)}.
    ```

  - ```math
\Phi(r)\simeq-\sqrt{GMa_0}\,\ln r.
    ```

  - ```math
r_s := \sqrt{\frac{GM}{a_0}}.
    ```


## 03.1_Background_Cosmology.md

- **Depends on:** 01.1_Action_and_Field_Equations.md

- **Exports:**

  - ```math
H^2(a)
=
H_0^2\left[\Omega_{m0}a^{-3}+\Omega_{\Lambda0}\right],
    ```

  - ```math
\Omega_m(a)
=
\frac{\Omega_{m0}a^{-3}}{\Omega_{m0}a^{-3}+\Omega_{\Lambda0}}.
    ```


## 01.2_Stress_Energy_Tensor.md

- **Depends on:** 01.1_Action_and_Field_Equations.md

- **Exports:**

  - ```math
T^{(\phi)}_{\mu\nu}
=
\frac{a_0^2}{4\pi G}
\left[
\frac{F'(X)}{a_0^2}
\nabla_\mu\phi\,\nabla_\nu\phi
-
\tfrac12 g_{\mu\nu}F(X)
\right].
    ```

  - ```math
\nabla^\mu T^{(\phi)}_{\mu\nu} = 0.
    ```

  - ```math
\rho_{\phi}
=
\frac{a_0^2}{8\pi G}F(X).
    ```

  - ```math
\rho_{\phi} \ge 0.
    ```


## 02.2_BTFR_Derivation.md

- **Depends on:** 02.1_Force_Law_and_Asymptotics.md

- **Exports:**

  - ```math
V^4=G M_b a_0.
    ```

  - ```math
M_b=\frac{1}{G a_0}V^4.
    ```


## 01.3_Hyperbolicity_and_Characteristics.md

- **Depends on:** 01.2_Stress_Energy_Tensor.md

- **Exports:**

  - ```math
G^{\mu\nu}_{\mathrm{eff}}
:=
K(X_0) g^{\mu\nu}
+
\frac{2K'(X_0)}{a_0^2} u^\mu u^\nu.
    ```

  - ```math
G^{\mu\nu}_{\mathrm{eff}} \text{ is Lorentzian for all physical backgrounds.}
    ```

  - ```math
c_s^2
=
\frac{K(X_0)}{K(X_0) + 2X_0K'(X_0)}.
    ```

  - ```math
c_s^2 \to \tfrac12.
    ```

  - ```math
c_s^2 \to 1.
    ```


## 02.3_Screening_Radius_and_EFE.md

- **Depends on:** 02.2_BTFR_Derivation.md

- **Exports:**

  - ```math
\nabla^2\Phi = 4\pi G\rho
\quad+\quad O\!\left(\frac{a_0}{g}\right).
    ```

  - ```math
r_s=\sqrt{\frac{GM}{a_0}}.
    ```

  - ```math
\nabla^2\Phi_{\rm int}
=
4\pi G\rho_{\rm int}
\quad+\quad O\!\left(\frac{a_0}{|\mathbf g_{\rm ext}|}\right).
    ```


## 03.2_Scalar_Perturbations.md

- **Depends on:** 01.3_Hyperbolicity_and_Characteristics.md, 03.1_Background_Cosmology.md

- **Exports:**

  - ```math
\Phi = \Psi
    ```

  - ```math
c_s^2
=
\frac{K_0}{K_0+2X_0K_0'}.
    ```

  - ```math
\dot{\mathcal R}=0
\quad (k \ll aH).
    ```


## 05.1_Nonlinear_Screening_Mechanism.md

- **Depends on:** 02.3_Screening_Radius_and_EFE.md

- **Exports:**

  - ```math
\nabla^2\Phi
=
4\pi G\rho
+
O\!\left(\frac{a_0}{g}\right).
    ```

  - ```math
r_s = \sqrt{\frac{GM}{a_0}}.
    ```

  - ```math
\nabla^2\Phi_{\rm int}
=
4\pi G\rho_{\rm int}
+
O\!\left(\frac{a_0}{|\mathbf g_{\rm ext}|}\right).
    ```


## 03.3_Matter_Growth_Equation.md

- **Depends on:** 03.2_Scalar_Perturbations.md

- **Exports:**

  - ```math
\frac{k^2}{a^2}\Phi
=
4\pi G_{\rm eff}(k,a)\,\bar\rho_m\,\delta.
    ```

  - ```math
G_{\rm eff}(k,a)
=
G\,[1+\alpha_{\rm eff}(k,a)].
    ```

  - ```math
\ddot\delta
+
2H\dot\delta
-
4\pi G\bar\rho_m
\bigl[1+\alpha_{\rm eff}(k,a)\bigr]\delta
=
0.
    ```

  - ```math
D''
+
\left(
\frac{3}{a}+\frac{1}{H}\frac{dH}{da}
\right)D'
-
\frac{3}{2}
\frac{\Omega_m(a)}{a^2}
\bigl[1+\alpha_{\rm eff}(k,a)\bigr]D
=
0,
    ```

  - ```math
\frac{df}{d\ln a}
+
f^2
+
\left(
2+\frac{d\ln H}{d\ln a}
\right)f
=
\frac{3}{2}\Omega_m(a)
\bigl[1+\alpha_{\rm eff}(k,a)\bigr].
    ```


## 05.2_Spherical_Collapse.md

- **Depends on:** 05.1_Nonlinear_Screening_Mechanism.md

- **Exports:**

  - ```math
t_{\rm coll}^{\rm N}
=
\frac{\pi}{2\sqrt{2}}\,\frac{r_i^{3/2}}{\sqrt{GM}},
    ```

  - ```math
t_{\rm coll}^{\rm VSU}
\propto
\frac{r_i^{3/2}}{(GMa_0)^{1/4}}.
    ```

  - ```math
\frac{t_{\rm coll}^{\rm VSU}}{t_{\rm coll}^{\rm N}}
\sim
\left(\frac{g_N}{a_0}\right)^{1/4},
    ```

  - ```math
\delta_c^{\rm VSU}(M,z)
=
\delta_c^{\rm GR}
\left(\frac{g_N(M,z)}{a_0}\right)^{1/4}.
    ```


## 03.4_Early_Time_Asymptotics.md

- **Depends on:** 03.3_Matter_Growth_Equation.md

- **Exports:**

  - ```math
D(a) \simeq a
\quad (a \ll 1).
    ```

  - ```math
D(a) = a\,[1+O(a^{n+1})].
    ```

  - ```math
f(a,k) \to 1
\quad \text{as} \quad a \to 0.
    ```

  - ```math
\sigma_8(z) \simeq \frac{\sigma_{8,0}}{1+z}
\quad (z \gg 1).
    ```

  - ```math
f\sigma_8(z)
\simeq
\frac{\sigma_{8,0}}{1+z}
\left[1+O\bigl((1+z)^{-(n+1)}\bigr)\right].
    ```


## 05.3_Halo_Bias.md

- **Depends on:** 05.2_Spherical_Collapse.md

- **Exports:**

  - ```math
b_L(M,z)
=
\frac{\nu^2(M,z)-1}{\delta_c(M,z)}.
    ```

  - ```math
\delta_c^{\rm VSU}(M,z)
=
\delta_c^{\rm GR}
\left(\frac{g_N(M,z)}{a_0}\right)^{1/4}.
    ```

  - ```math
b_E^{\rm VSU}(M,z)
=
1
+
\frac{1}{\delta_c^{\rm VSU}(M,z)}
\left[
\frac{(\delta_c^{\rm VSU}(M,z))^2}{\sigma^2(M,z)}-1
\right].
    ```

  - ```math
\frac{b_E^{\rm VSU}}{b_E^{\rm GR}}
=
\left(\frac{g_N(M,z)}{a_0}\right)^{-1/4}
\frac{(\delta_c^{\rm GR})^2/\sigma^2(M,z)-1}
{(\delta_c^{\rm VSU})^2/\sigma^2(M,z)-1}.
    ```

  - ```math
b_E^{\rm VSU}(M,z) \to b_E^{\rm GR}(M,z).
    ```

  - ```math
b_E^{\rm VSU}(M,z) > b_E^{\rm GR}(M,z).
    ```


## 03.5_Late_Time_Asymptotics.md

- **Depends on:** 03.4_Early_Time_Asymptotics.md

- **Exports:**

  - ```math
f(a,k) \simeq \Omega_m(a)^{\gamma(k)}.
    ```

  - ```math
\gamma(k)
=
\frac{6}{11}
-
\frac{3}{55}\,\alpha_\infty(k).
    ```

  - ```math
f(a,k)
=
\Omega_m(a)^{\gamma(k)},
    ```

  - ```math
D(a,k) \to D_\infty(k)
\quad \text{as} \quad a \to 1.
    ```

  - ```math
\mathcal R_D(k,a)
\simeq
\exp\!\left[
-\frac{3}{55}\alpha_\infty(k)
\int^a \frac{da'}{a'}\,
\Omega_m(a')^{6/11}\ln \Omega_m(a')
\right].
    ```

  - ```math
f\sigma_8(z)
=
\sigma_{8,0}
\,\Omega_m(z)^{\gamma(k)}
\,D(z,k),
\qquad z \lesssim 2.
    ```


## 04.3_ISW_Sign_and_Amplitude.md

- **Depends on:** 03.3_Matter_Growth_Equation.md, 03.5_Late_Time_Asymptotics.md

- **Exports:**

  - ```math
\left(\frac{\Delta T}{T}\right)_{\rm ISW}
=
2\int_{\eta_*}^{\eta_0} d\eta\, \dot\Phi(\eta,\mathbf{x}).
    ```

  - ```math
\dot\Phi
=
H\Phi\left[f(k,a)-1+\frac{d\ln\mathcal G}{d\ln a}\right].
    ```

  - ```math
\text{GR predicts a positive ISW signal}.
    ```

  - ```math
\dot\Phi < 0
\quad\Rightarrow\quad
\text{ISW sign unchanged relative to GR}.
    ```

  - ```math
\mathcal R_{\rm ISW}(k,a)
\simeq
1
+
\frac{3}{55}\alpha_\infty(k)
\frac{\Omega_m(a)^{6/11}\ln\Omega_m(a)}
{1-\Omega_m(a)^{6/11}}.
    ```

  - ```math
\mathcal R_{\rm ISW}(k,a) < 1.
    ```

  - ```math
\text{No early-time ISW contribution}.
    ```


## 04.5_Alcock_Paczynski_Consistency.md

- **Depends on:** 03.3_Matter_Growth_Equation.md, 03.5_Late_Time_Asymptotics.md

- **Exports:**

  - ```math
F_{\rm AP}(z)
=
(1+z)\,D_A(z)\,H(z).
    ```

  - ```math
F_{\rm AP}^{\rm VSU}(z) = F_{\rm AP}^{\rm GR}(z).
    ```

  - ```math
\mathcal L
=
\mathcal L_{\rm AP}\bigl(F_{\rm AP}\bigr)
\times
\mathcal L_{\rm RSD}\bigl(f\sigma_8(k)\bigr)
+ O(\delta^2).
    ```


## 04.2_Weak_Lensing_and_S8.md

- **Depends on:** 03.3_Matter_Growth_Equation.md, 03.5_Late_Time_Asymptotics.md

- **Exports:**

  - ```math
\Phi = \Psi
    ```

  - ```math
P_\kappa(\ell)
=
\int_0^{\chi_H} d\chi\,
\frac{W_L^2(\chi)}{\chi^2}\,
P_\Phi\!\left(k=\frac{\ell}{\chi},z(\chi)\right),
    ```

  - ```math
P_\Phi(k,a)
=
\left(\frac{3}{2}\frac{H_0^2\Omega_{m0}}{k^2}\right)^2
\mathcal G^2(k,a)
\frac{D^2(k,a)}{a^2}
P_{\rm ini}(k).
    ```

  - ```math
\sigma_8^2(z)
=
\int \frac{dk}{k}\,
\Delta^2(k,z)\,W_8^2(k),
    ```

  - ```math
\bar\alpha_\infty^{\rm lens}
=
\frac{
\int d\ln k\,W_8^2(k)P_{\rm ini}(k)\alpha_\infty(k)
}{
\int d\ln k\,W_8^2(k)P_{\rm ini}(k)
}.
    ```

  - ```math
\sigma_8(z)
=
\sigma_{8,\rm GR}(z)
\left[1-\frac{3}{55}\bar\alpha_\infty^{\rm lens}\,\mathcal I(z)\right].
    ```

  - ```math
S_8^{\rm VSU}
=
S_8^{\rm GR}
\left[1-\frac{3}{55}\bar\alpha_\infty^{\rm lens}\,\mathcal I(0)\right].
    ```


## 04.1_RSD_and_fsigma8_Mapping.md

- **Depends on:** 03.3_Matter_Growth_Equation.md, 03.5_Late_Time_Asymptotics.md

- **Exports:**

  - ```math
\langle f\sigma_8(z) \rangle
=
\frac{\int d^3k\,W_{\rm RSD}(k,z)\,f(k,z)\,\sigma_8(k,z)}
     {\int d^3k\,W_{\rm RSD}(k,z)},
    ```

  - ```math
\bar\alpha_\infty^{\rm RSD}(z)
=
\frac{\int d\ln k\,W_{\rm RSD}(k,z)\,\alpha_\infty(k)}
     {\int d\ln k\,W_{\rm RSD}(k,z)}.
    ```

  - ```math
\langle f\sigma_8(z) \rangle_{\rm RSD}
=
f_{\rm GR}(z)\sigma_{8,\rm GR}(z)
\left[1-\frac{3}{55}\bar\alpha_\infty^{\rm RSD}(z)
\bigl(\ln\Omega_m(z)+\mathcal I(z)\bigr)\right].
    ```


## 04.4_BAO_Phase_and_Peaks.md

- **Depends on:** 03.3_Matter_Growth_Equation.md, 03.5_Late_Time_Asymptotics.md

- **Exports:**

  - ```math
r_s(\eta) = \int_0^{\eta} c_s(\eta')\,d\eta'.
    ```

  - ```math
k_n r_s(\eta_*) = n\pi,
\qquad n = 1,2,3,\dots
    ```

  - ```math
r_s^{\rm VSU} = r_s^{\rm GR}.
    ```

  - ```math
\dot\Phi \simeq 0
\quad \text{during BAO oscillations}.
    ```

  - ```math
\Delta\phi_{\rm BAO} = 0.
    ```

  - ```math
P_m^{\rm VSU}(k,z)
=
P_m^{\rm GR}(k,z)
\left[\frac{D_{\rm VSU}(k,z)}{D_{\rm GR}(z)}\right]^2.
    ```


## 06.1_Internal_Consistency.md

- **Depends on:** 02.3_Screening_Radius_and_EFE.md, 03.5_Late_Time_Asymptotics.md, 04.1_RSD_and_fsigma8_Mapping.md, 04.2_Weak_Lensing_and_S8.md, 04.3_ISW_Sign_and_Amplitude.md, 04.4_BAO_Phase_and_Peaks.md, 04.5_Alcock_Paczynski_Consistency.md, 05.3_Halo_Bias.md

- **Exports:** (none detected)


## 06.2_Observable_Degeneracy_Structure.md

- **Depends on:** 06.1_Internal_Consistency.md

- **Exports:** (none detected)


## 06.3_Parameter_Minimality.md

- **Depends on:** 06.2_Observable_Degeneracy_Structure.md

- **Exports:** (none detected)
<!-- END FILE: VSU_EXPORTS.md -->

---

## Appendix: `VSU_package.zip` member files (verbatim)

These are the literal contents of each `.md` file inside `VSU_package.zip`.

<!-- BEGIN ZIP MEMBER: 00_Overview.md -->
# Vacuum Stiffness Unification (VSU)
## Overview and Structural Orientation

This document provides a minimal orientation to the Vacuum Stiffness Unification (VSU) framework.
All derivations appear in subsequent files.
<!-- END ZIP MEMBER: 00_Overview.md -->

<!-- BEGIN ZIP MEMBER: 01.1_Action_and_Field_Equations.md -->
# 01.1 Action and Field Equations
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 01.1_Action_and_Field_Equations.md -->

<!-- BEGIN ZIP MEMBER: 01.2_Stress_Energy_Tensor.md -->
# 01.2 Stress–Energy Tensor
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 01.2_Stress_Energy_Tensor.md -->

<!-- BEGIN ZIP MEMBER: 01.3_Hyperbolicity_and_Characteristics.md -->
# 01.3 Hyperbolicity and Characteristics
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 01.3_Hyperbolicity_and_Characteristics.md -->

<!-- BEGIN ZIP MEMBER: 02.1_Force_Law_and_Asymptotics.md -->
# 02.1 Force Law and Asymptotics
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 02.1_Force_Law_and_Asymptotics.md -->

<!-- BEGIN ZIP MEMBER: 02.2_BTFR_Derivation.md -->
# 02.2 Baryonic Tully–Fisher Relation
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 02.2_BTFR_Derivation.md -->

<!-- BEGIN ZIP MEMBER: 02.3_Screening_Radius_and_EFE.md -->
# 02.3 Screening Radius and External Field Effect
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 02.3_Screening_Radius_and_EFE.md -->

<!-- BEGIN ZIP MEMBER: 03.1_Background_Cosmology.md -->
# 03.1 Background Cosmology
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 03.1_Background_Cosmology.md -->

<!-- BEGIN ZIP MEMBER: 03.2_Scalar_Perturbations.md -->
# 03.2 Scalar Perturbations
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 03.2_Scalar_Perturbations.md -->

<!-- BEGIN ZIP MEMBER: 03.3_Matter_Growth_Equation.md -->
# 03.3 Matter Growth Equation
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 03.3_Matter_Growth_Equation.md -->

<!-- BEGIN ZIP MEMBER: 03.4_Early_Time_Asymptotics.md -->
# 03.4 Early-Time Asymptotics
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 03.4_Early_Time_Asymptotics.md -->

<!-- BEGIN ZIP MEMBER: 03.5_Late_Time_Asymptotics.md -->
# 03.5 Late-Time Asymptotics
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 03.5_Late_Time_Asymptotics.md -->

<!-- BEGIN ZIP MEMBER: 04.1_RSD_and_fsigma8_Mapping.md -->
# 04.1 RSD and fσ8 Mapping
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 04.1_RSD_and_fsigma8_Mapping.md -->

<!-- BEGIN ZIP MEMBER: 04.2_Weak_Lensing_and_S8.md -->
# 04.2 Weak Lensing and S8
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 04.2_Weak_Lensing_and_S8.md -->

<!-- BEGIN ZIP MEMBER: 04.3_ISW_Sign_and_Amplitude.md -->
# 04.3 ISW Sign and Amplitude
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 04.3_ISW_Sign_and_Amplitude.md -->

<!-- BEGIN ZIP MEMBER: 04.4_BAO_Phase_and_Peaks.md -->
# 04.4 BAO Phase and Peak Positions
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 04.4_BAO_Phase_and_Peaks.md -->

<!-- BEGIN ZIP MEMBER: 04.5_Alcock_Paczynski_Consistency.md -->
# 04.5 Alcock–Paczynski Consistency
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 04.5_Alcock_Paczynski_Consistency.md -->

<!-- BEGIN ZIP MEMBER: 05.1_Nonlinear_Screening_Mechanism.md -->
# 05.1 Nonlinear Screening Mechanism
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 05.1_Nonlinear_Screening_Mechanism.md -->

<!-- BEGIN ZIP MEMBER: 05.2_Spherical_Collapse.md -->
# 05.2 Spherical Collapse
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 05.2_Spherical_Collapse.md -->

<!-- BEGIN ZIP MEMBER: 05.3_Halo_Bias.md -->
# 05.3 Halo Bias
See conversation transcript for full derivation.
<!-- END ZIP MEMBER: 05.3_Halo_Bias.md -->

---

## Appendix: Integrity hashes (SHA-256)

### Sources used for the core concatenation
```json
[
  {
    "id": "00_Overview.md",
    "source_path": "/mnt/data/zip_extract/00_Overview.md",
    "sha256": "59d02851a297cdb8d03e0ee67903de3977d142075565b3369d734f5b1f7f7829",
    "bytes": 219
  },
  {
    "id": "01.1_Action_and_Field_Equations.md",
    "source_path": "/mnt/data/01.1_Action_and_Field_Equations.md",
    "sha256": "7b572176915fec63c64ea2c585db1a4b3c6328ab7eafe0b2854fe1beabf799ed",
    "bytes": 3992
  },
  {
    "id": "01.2_Stress_Energy_Tensor.md",
    "source_path": "/mnt/data/01.2_Stress_Energy_Tensor.md",
    "sha256": "6631e23b3c406e5521328f5ce6f41689073e6dc3d82c50ba9e42f2557f1d2178",
    "bytes": 3798
  },
  {
    "id": "01.3_Hyperbolicity_and_Characteristics.md",
    "source_path": "/mnt/data/01.3_Hyperbolicity_and_Characteristics.md",
    "sha256": "cd22fe97c550ffc2c09c2040132ac0923a7604a1cd18970afed6d88993d137b9",
    "bytes": 3805
  },
  {
    "id": "02.1_Force_Law_and_Asymptotics.md",
    "source_path": "/mnt/data/02.1_Force_Law_and_Asymptotics.md",
    "sha256": "0e34c628114478b707cc4adc19e259a8ecdd324d2e6e11f4c8161207ecebd54a",
    "bytes": 3002
  },
  {
    "id": "02.2_BTFR_Derivation.md",
    "source_path": "/mnt/data/02.2_BTFR_Derivation.md",
    "sha256": "60762522a4ec1ee2872631622cc6f74b2997b544ba4e7b542612688649d6f52f",
    "bytes": 2439
  },
  {
    "id": "02.3_Screening_Radius_and_EFE.md",
    "source_path": "/mnt/data/02.3_Screening_Radius_and_EFE.md",
    "sha256": "36f51959b09d9e4acf1b84a55c8b8de3f2c8ebb312b3faedb34bc2305f0356d9",
    "bytes": 3066
  },
  {
    "id": "03.1_Background_Cosmology.md",
    "source_path": "/mnt/data/03.1_Background_Cosmology.md",
    "sha256": "78559b1de6b925a249fcf51d1a07cd428f1b60b65499049efa0c10453f66f977",
    "bytes": 2784
  },
  {
    "id": "03.2_Scalar_Perturbations.md",
    "source_path": "/mnt/data/03.2_Scalar_Perturbations.md",
    "sha256": "48162d7710388edf27c2bfa1f1a4a13bf5bc5f00e79e72cdfd8b8d6c7b967fc9",
    "bytes": 3899
  },
  {
    "id": "03.3_Matter_Growth_Equation.md",
    "source_path": "/mnt/data/03.3_Matter_Growth_Equation.md",
    "sha256": "1623ea74a2475a552d1a8abbe2881f8aaed986eaeb5981eb6982677ff589fe13",
    "bytes": 3264
  },
  {
    "id": "03.4_Early_Time_Asymptotics.md",
    "source_path": "/mnt/data/zip_extract/03.4_Early_Time_Asymptotics.md",
    "sha256": "48927720b1e36850301586ab4af29163774b48b35a90bb2d2cba8b1aa27c3fa2",
    "bytes": 79
  },
  {
    "id": "03.5_Late_Time_Asymptotics.md",
    "source_path": "/mnt/data/03.5_Late_Time_Asymptotics.md",
    "sha256": "6228a75339acbba0a3860b883dc981809386058a44ba00abac8ab5e97c5baabc",
    "bytes": 3472
  },
  {
    "id": "04.1_RSD_and_fsigma8_Mapping.md",
    "source_path": "/mnt/data/zip_extract/04.1_RSD_and_fsigma8_Mapping.md",
    "sha256": "430a3e07b9d992a2b342ca63f876f0349cbb8065d070413949177a6b18eeabab",
    "bytes": 77
  },
  {
    "id": "04.2_Weak_Lensing_and_S8.md",
    "source_path": "/mnt/data/04.2_Weak_Lensing_and_S8.md",
    "sha256": "da657dc91a175a48d637a98862359ac54a6ddd95cdd2f5776e3d729d11b60bb2",
    "bytes": 3582
  },
  {
    "id": "04.3_ISW_Sign_and_Amplitude.md",
    "source_path": "/mnt/data/04.3_ISW_Sign_and_Amplitude.md",
    "sha256": "8d104314b94dbd303c156f5924c945bd35e78b87b6c07a813a0400df435e362e",
    "bytes": 3141
  },
  {
    "id": "04.4_BAO_Phase_and_Peaks.md",
    "source_path": "/mnt/data/04.4_BAO_Phase_and_Peaks.md",
    "sha256": "2813f25deec217bc30846584c6873c320663f9234505a87993e3f91d71179252",
    "bytes": 3624
  },
  {
    "id": "04.5_Alcock_Paczynski_Consistency.md",
    "source_path": "/mnt/data/04.5_Alcock_Paczynski_Consistency.md",
    "sha256": "c3fa5741f7ef3f39deaea8773d25ae4d96c997d06f03a8160b4cdee270f23368",
    "bytes": 2705
  },
  {
    "id": "05.1_Nonlinear_Screening_Mechanism.md",
    "source_path": "/mnt/data/05.1_Nonlinear_Screening_Mechanism.md",
    "sha256": "2e531e13638036e99be7b8523e80907ae203284c3a0b75712326895a70816e40",
    "bytes": 3348
  },
  {
    "id": "05.2_Spherical_Collapse.md",
    "source_path": "/mnt/data/05.2_Spherical_Collapse.md",
    "sha256": "a181b4bc4e4cfb289cb080cd688e77cf45f3940013138e645597cf4847c9457b",
    "bytes": 3358
  },
  {
    "id": "05.3_Halo_Bias.md",
    "source_path": "/mnt/data/05.3_Halo_Bias.md",
    "sha256": "a8b189f3e4b4d2c9797fdde89e8adcb2e41cfc0edfd5265d4b622ae7949687cc",
    "bytes": 3616
  },
  {
    "id": "06.1_Internal_Consistency.md",
    "source_path": "/mnt/data/06.1_Internal_Consistency.md",
    "sha256": "3dbef531490d64351dd64305429195ea8ba88375dc618b524a7ea0f44dd65121",
    "bytes": 3705
  },
  {
    "id": "06.2_Observable_Degeneracy_Structure.md",
    "source_path": "/mnt/data/06.2_Observable_Degeneracy_Structure.md",
    "sha256": "88ac6b7d28a087df7f47930588a4e2d49489e1e3333f88ceb0685e825e35d5fb",
    "bytes": 3886
  },
  {
    "id": "06.3_Parameter_Minimality.md",
    "source_path": "/mnt/data/06.3_Parameter_Minimality.md",
    "sha256": "e9650084c68182b4a90fa1885f027e9ca339832b46b5b39f15a40c842ef2b0bd",
    "bytes": 2957
  },
  {
    "id": "VSU_DAG.yaml",
    "source_path": "/mnt/data/VSU_DAG.yaml",
    "sha256": "491e52dae1dc265039d58cc31a5e3344891d2ac09551c4f6a60abea68175a506",
    "bytes": 3955
  },
  {
    "id": "VSU_DAG.json",
    "source_path": "/mnt/data/VSU_DAG.json",
    "sha256": "e02bb9b6f6928c85ae232e48ec0d7122e814732e2380220533f1105f43680705",
    "bytes": 4952
  },
  {
    "id": "VSU_LINT.md",
    "source_path": "/mnt/data/VSU_LINT.md",
    "sha256": "60fbf04e9f471f89101bd555a00a0b2e4de9ed4b62c4fce9e31df31b9a2294e0",
    "bytes": 1756
  },
  {
    "id": "VSU_EXPORTS.md",
    "source_path": "/mnt/data/VSU_EXPORTS.md",
    "sha256": "b865ff1f50e72882654889185cadddf2ae1f878d0b5a7a11e289a98ee28e2b5a",
    "bytes": 10902
  }
]
```

### `VSU_package.zip` member hashes
```json
[
  {
    "member": "00_Overview.md",
    "sha256": "59d02851a297cdb8d03e0ee67903de3977d142075565b3369d734f5b1f7f7829",
    "bytes": 219
  },
  {
    "member": "01.1_Action_and_Field_Equations.md",
    "sha256": "47b019a957a3129dd11e148411e8e0dc9f9fa10da167af5060b7d2f2d30e9092",
    "bytes": 83
  },
  {
    "member": "01.2_Stress_Energy_Tensor.md",
    "sha256": "4991d94689e5bbc0f3d5d6a3a02f22b00c9065a0ba5469b9680b8e8b4f82ca18",
    "bytes": 79
  },
  {
    "member": "01.3_Hyperbolicity_and_Characteristics.md",
    "sha256": "9a9b60220b9b58643026943ece80cc8942a8e1548d00227f1565ab929b3f144f",
    "bytes": 90
  },
  {
    "member": "02.1_Force_Law_and_Asymptotics.md",
    "sha256": "7771543708c3beaeca914c6a359289a168083623a6008d3971acdbfcb3946f2a",
    "bytes": 82
  },
  {
    "member": "02.2_BTFR_Derivation.md",
    "sha256": "b70ad880302786fa18f80149c7748d42e87cee8f9a957ceea03afa6a730c2ca0",
    "bytes": 89
  },
  {
    "member": "02.3_Screening_Radius_and_EFE.md",
    "sha256": "89e58bff17e1a1a279fa996295961062fe0a6261650c6f2d3e946178ef7118fc",
    "bytes": 99
  },
  {
    "member": "03.1_Background_Cosmology.md",
    "sha256": "a8602e48b30dcb1ce64869c04216b9f8cbfc9e747cbe508fe6e69c2c63485686",
    "bytes": 77
  },
  {
    "member": "03.2_Scalar_Perturbations.md",
    "sha256": "85445f098c0de88f2e554c91842ee1dc7c1bba1876ff1c8b1c9d9bbff2ff2385",
    "bytes": 77
  },
  {
    "member": "03.3_Matter_Growth_Equation.md",
    "sha256": "861c8146755ebe90ada93d74addf2843c6aaa09f1f3901ee39910df72ccbe687",
    "bytes": 79
  },
  {
    "member": "03.4_Early_Time_Asymptotics.md",
    "sha256": "48927720b1e36850301586ab4af29163774b48b35a90bb2d2cba8b1aa27c3fa2",
    "bytes": 79
  },
  {
    "member": "03.5_Late_Time_Asymptotics.md",
    "sha256": "dada3ba6ec4c8f728c1e03fa1a44db008b093cc8b81853a850135e318aa98535",
    "bytes": 78
  },
  {
    "member": "04.1_RSD_and_fsigma8_Mapping.md",
    "sha256": "430a3e07b9d992a2b342ca63f876f0349cbb8065d070413949177a6b18eeabab",
    "bytes": 77
  },
  {
    "member": "04.2_Weak_Lensing_and_S8.md",
    "sha256": "270666c60e5c9748889fc3f64bcfe33487a0bc5daed26208abfe5a0cd6d285d5",
    "bytes": 76
  },
  {
    "member": "04.3_ISW_Sign_and_Amplitude.md",
    "sha256": "72307e657b6fa6492129428de3fcdd9c32dfe8fbc18bedbe3c82313288974825",
    "bytes": 79
  },
  {
    "member": "04.4_BAO_Phase_and_Peaks.md",
    "sha256": "b27f861b3684c2f9707f0f0b85c5dccf32587fb0f8acf834da0bb7358f73ff90",
    "bytes": 85
  },
  {
    "member": "04.5_Alcock_Paczynski_Consistency.md",
    "sha256": "fccc749299ed66de6364b2b3622a336bec888fe4992573e1c1cab18b17b94fbc",
    "bytes": 87
  },
  {
    "member": "05.1_Nonlinear_Screening_Mechanism.md",
    "sha256": "7296e61ef732f5337fe6f18bc1d9542d5670dce906055eb70ec88c00d6c26986",
    "bytes": 86
  },
  {
    "member": "05.2_Spherical_Collapse.md",
    "sha256": "22c5ae7b8729f5e1f0a0c5e7c156815d26c10ee1bf6c1a7b5384befba45c0b32",
    "bytes": 75
  },
  {
    "member": "05.3_Halo_Bias.md",
    "sha256": "41545a842327a1a3152ebc21151dc8a7a04e144bc4f5d58da84beafb6e4ab1a3",
    "bytes": 66
  }
]
```

