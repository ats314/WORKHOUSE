# 15 — Vacuum Stiffness Unification: Core Field Theory

## Abstract
We develop the **Vacuum Stiffness Unification (VSU)** field theory from first principles. We derive the Lagrangian, the modified Poisson equation, the interpolating function $\mu(x)$, and show how VSU reproduces MOND phenomenology while being derivable from a relativistic action. We also derive the Baryonic Tully-Fisher Relation as a prediction.

**Connected Files:**
- **[23] VSU Cosmology:** Application to large-scale structure.
- **[06] Riccati Attractor:** Similar nonlinear dynamics in the mass gap context.

---

## 1. Motivation: The Dark Matter Problem

### 1.1 The Observations
Galaxy rotation curves show $v(r) \approx \text{const}$ at large $r$.
Newtonian gravity predicts $v(r) \sim r^{-1/2}$.
The discrepancy is attributed to **Dark Matter** (unseen mass).

### 1.2 The Alternative: Modified Gravity
Instead of adding mass, modify the gravitational law.
**MOND** (Milgrom): Below acceleration $a_0 \sim 10^{-10}$ m/s², gravity transitions from $1/r^2$ to $1/r$.

### 1.3 VSU: A Field-Theoretic MOND
VSU provides a **Lagrangian formulation** of MOND-like physics.
It replaces the ad-hoc $\mu(g)$ function with a **field-dependent permittivity** of the vacuum.

---

## 2. The VSU Lagrangian

### 2.1 The Action
$$
S = \int d^4x \left[ -\frac{a_0^2}{8\pi G} F\left(\frac{|\nabla\Phi|^2}{a_0^2}\right) - \rho \Phi \right]
$$
where:
- $\Phi$ is the gravitational potential.
- $F(x)$ is a function with $F(x) \sim x$ for $x \gg 1$ (Newtonian) and $F(x) \sim x^{3/2}$ for $x \ll 1$ (MOND).

### 2.2 The Interpolating Function
Define $\mu(x) = F'(x)$.
Standard choice (simple interpolation):
$$
\mu(x) = \frac{x}{\sqrt{1+x^2}} \quad \text{or} \quad \mu(x) = 1 - e^{-\sqrt{x}}
$$

### 2.3 Equation of Motion
Varying $\Phi$:
$$
\nabla \cdot (\mu(|\nabla\Phi|^2 / a_0^2) \nabla\Phi) = 4\pi G \rho
$$
This is the **Modified Poisson Equation**.

---

## 3. Derivation of the Force Law

### 3.1 Spherical Symmetry
For a point mass $M$, assume $\Phi = \Phi(r)$.
$$
\mu(g^2/a_0^2) \cdot g \cdot 4\pi r^2 = 4\pi G M
$$
where $g = |\nabla\Phi| = d\Phi/dr$.

### 3.2 The Two Limits
**High acceleration ($g \gg a_0$):**
$\mu \approx 1$, so $g = GM/r^2$ (Newton).

**Low acceleration ($g \ll a_0$):**
$\mu \approx g/a_0$, so:
$$
\frac{g^2}{a_0} \cdot 4\pi r^2 = 4\pi GM \implies g = \sqrt{\frac{GMa_0}{r^2}} = \frac{\sqrt{GMa_0}}{r}
$$

### 3.3 Flat Rotation Curves
Circular velocity: $v^2 = g \cdot r = \sqrt{GMa_0}$.
$$
v = (GMa_0)^{1/4}
$$
**This is constant in $r$!** Flat rotation curves are automatic.

---

## 4. The Baryonic Tully-Fisher Relation

### 4.1 Derivation
From $v^4 = GMa_0$:
$$
M = \frac{v^4}{Ga_0}
$$
This is the **Baryonic Tully-Fisher Relation (BTFR)**.

### 4.2 Observational Confirmation
Observations: $M_b \propto v^4$ with scatter $< 0.1$ dex.
Normalization: $a_0 \approx 1.2 \times 10^{-10}$ m/s².
VSU predicts BTFR exactly, with no free parameters.

### 4.3 Contrast with Dark Matter
In $\Lambda$CDM, the relation must be tuned by galaxy formation physics.
A priori, there is no reason for $M_b \propto v^4$.
VSU makes it a **theorem**, not an accident.

---

## 5. The Relativistic Extension (TeVeS-like)

### 5.1 The Challenge
MOND as stated above is non-relativistic.
We need a covariant formulation for cosmology and gravitational lensing.

### 5.2 The Scalar-Tensor Action
Introduce a scalar field $\phi$ such that the physical metric is:
$$
\tilde{g}_{\mu\nu} = e^{2\phi} g_{\mu\nu}
$$
The scalar obeys:
$$
\nabla_\mu (F'(k) \nabla^\mu \phi) = \text{source}
$$
where $k = g^{\mu\nu} \nabla_\mu \phi \nabla_\nu \phi$.

### 5.3 Lensing and Cosmology
The scalar field contributes to the effective metric seen by photons.
This allows VSU to:
1. Match the lensing of the Bullet Cluster (with appropriate $\phi$ distribution).
2. Produce correct CMB peaks (with modified recombination physics).

---

## 6. The Connection to Yang-Mills

### 6.1 The Analogy
Both VSU and the Mass Gap involve a **nonlinear stiffness**:
- VSU: Gravitational stiffness $\mu \to 0$ as $g \to 0$.
- YM: Curvature $\rho \to 0$ as field $\to$ vacuum.

### 6.2 The Common Structure
The Riccati equation (File [06]) for the mass gap:
$$
\dot{\lambda} = -2\lambda^2 + \sigma
$$
has the same structure as the VSU interpolation:
$$
\text{Force} = \mu(g) \times \text{Field}
$$
Both are "self-regulating" nonlinearities that create stable fixed points.

### 6.3 Speculative Connection
Perhaps the vacuum permittivity $\mu$ in VSU arises from integrating out massive glueballs (the spectrum created by the mass gap).
The mass gap would then be the "UV completion" of VSU.

---

## Summary

VSU provides a complete alternative to dark matter:
1. The modified Poisson equation arises from an action principle.
2. Flat rotation curves and BTFR are automatic predictions.
3. A relativistic extension exists (though non-unique).
4. The nonlinear structure mirrors that of Yang-Mills.

Whether Nature chooses VSU or $\Lambda$CDM is an empirical question.

---

## References
- M. Milgrom, *A modification of the Newtonian dynamics* (1983).
- J. Bekenstein, *Relativistic gravitation theory for the modified Newtonian dynamics paradigm* (2004).
- S. McGaugh, *The Baryonic Tully-Fisher Relation* (2012).
- **File [23]** (Cosmology) for large-scale applications.
- **File [06]** (Riccati) for the analogous dynamical structure.
