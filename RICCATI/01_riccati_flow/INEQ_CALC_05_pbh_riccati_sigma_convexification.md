---
title: "PBH Hessian Flow and Riccati Convexification"
subtitle: "Mass generation as a parabolic curvature fixed point"
status: "Speculative-but-proof-shaped synthesis"
date: "2025-12-31"
---

# 0. Thesis

A recurring idea in the project is to reframe RG evolution of effective actions as a **parabolic PDE**
on the gauge orbit space, then reduce tensor complexity to a scalar **Riccati inequality** whose stable fixed point is a **mass scale**.

This note consolidates the cleanest version of that mechanism.

---

# 1. Horizontal viscous Hamilton–Jacobi (vHJ) ansatz

Let $\mathcal M_{\mathrm{reg}}$ denote the regular stratum of the orbit space $\mathcal A/\mathcal G$
(or a finite-dimensional cutoff analogue), with horizontal differential operators $(\nabla_H,\Delta_H)$.

Let $S_t:\mathcal M_{\mathrm{reg}}\to\mathbb R$ be a scale-dependent effective action satisfying the vHJ-type PDE
\[
\partial_t S_t
=
\Delta_H S_t
-
|\nabla_H S_t|^2
+
J_t.
\tag{1.1}
\]

Define horizontal drift and Hessian:
\[
V_t:=\nabla_H S_t,
\qquad
h_t:=\nabla_H^2 S_t.
\]

---

# 2. Projected Bochner–Hessian (PBH) flow

Differentiating (1.1) twice and commuting derivatives yields a tensor PDE of the schematic form
\[
\boxed{
\partial_t h_t
=
\Delta_H h_t
-2\nabla_{V_t} h_t
-2 h_t^2
+ S_{\mathrm{anom}}(t)
+\mathfrak G(S_t,h_t),
}
\tag{2.1}
\]
where
\[
S_{\mathrm{anom}}(t) := \nabla_H^2 J_t
\]
and $\mathfrak G$ collects curvature/non-integrability correction terms (the “geometry drawer”).

The **Riccati nonlinearity** $-2h_t^2$ is the convexification engine.

---

# 3. Scalar Riccati inequality for the minimum eigenvalue

Let $\lambda_{\min}(t,x)$ be the minimum eigenvalue of $h_t(x)$ on horizontal directions.

A tensor maximum principle (or pointwise minimum argument) yields the inequality
\[
\partial_t \lambda_{\min}
\ \ge\
-2\lambda_{\min}^2
+
\sigma(t,x)
-
\varepsilon(t,x),
\tag{3.1}
\]
where
\[
\sigma(t,x):=\lambda_{\min}\big(S_{\mathrm{anom}}(t,x)\big),
\qquad
\varepsilon(t,x):=\text{projected contribution of }\mathfrak G.
\]

---

# 4. Dominance hypothesis and convexification

Assume:

1. **Uniform anomaly positivity:** $\sigma(t,x)\ge \sigma_A>0$ for $t$ large enough.
2. **Suppressed corrections:** $\varepsilon(t,x)\le \frac12\sigma_A$ for $t$ large enough.

Then (3.1) becomes the Riccati inequality
\[
\partial_t \lambda_{\min}
\ \ge\
-2\lambda_{\min}^2+\frac{\sigma_A}{2}.
\tag{4.1}
\]

Compare with the ODE
\[
y'(t)=-2y(t)^2+\frac{\sigma_A}{2}.
\tag{4.2}
\]
Its stable fixed point is
\[
y_\*=\sqrt{\frac{\sigma_A}{4}}.
\tag{4.3}
\]

Hence $\lambda_{\min}$ is driven to a strictly positive floor:
\[
\liminf_{t\to\infty}\ \inf_x \lambda_{\min}(t,x)\ \ge\ \sqrt{\frac{\sigma_A}{4}}.
\tag{4.4}
\]

---

# 5. Interpreting the fixed point as a mass scale

Uniform positivity of $h_t$ means uniform convexity of the effective action in physical directions.

In finite-dimensional cutoff settings, uniform convexity implies:

- a spectral gap for the associated Langevin generator (via Bakry–Émery),
- exponential clustering (via Helffer–Sjöstrand + kernel decay),
- and (with OS reflection positivity) a Hamiltonian mass gap.

Thus the PBH/Riccati mechanism offers a conceptual bridge:

> **Mass generation as a parabolic curvature fixed point forced by anomaly positivity.**

---

# 6. The “sigma positivity” bottleneck

The decisive input is the sign and size of
\[
\sigma(t,x)=\lambda_{\min}(\nabla_H^2 J_t(x)).
\]

A concrete decomposition strategy is
\[
\sigma_{\mathrm{eff}}
=
\sigma_{\mathrm{Haar}}
+
\sigma_{\mathrm{anom}}
+
\sigma_{\mathrm{corr}},
\]
where:

- $\sigma_{\mathrm{Haar}}$ is an entropic / geometric baseline (compact-group curvature),
- $\sigma_{\mathrm{anom}}$ is the trace-anomaly forcing (expected sign-definite in asymptotically free regimes),
- $\sigma_{\mathrm{corr}}$ collects corrections to be controlled by concentration/functional inequalities.

---

# 7. Numerical calibration: the entropic spark protocol

A practical lattice experiment can probe the curvature of an IR effective potential after gauge fixing:

- approximate the fundamental modular region (multi-start minimal Landau gauge),
- define an IR mode vector $Y$ from lowest Fourier components,
- estimate the Hessian $\nabla^2 V_{\mathrm{eff}}(0)$ by local covariance inversion,
- check volume stability and restart monotonicity of the smallest eigenvalue.

A stable positive eigenvalue gives a quantitative target for $\sigma_A$.

---

# 8. What must be proved to make PBH rigorous

A finite-cutoff rigorous theorem would require:

1. derivation of (1.1) from a specific RG formalism (FRG/Wetterich, PBH/Polchinski),
2. quantitative control of $\mathfrak G$ along the flow,
3. proof (or conditional proof) of $\sigma(t,x)\ge\sigma_A>0$ in the physical sector,
4. handling of orbit-space stratification (reducible configurations) in the maximum principle.

This is ambitious but unusually *well-posed*: it is a sign problem for a quadratic form, not an amorphous QFT mystery.
