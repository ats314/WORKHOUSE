---
title: "vHJ / Hessian Flow as Curvature-Stable Coarse-Graining: Riccati Law and Measured Universality"
date: "2026-01-01"
---

## 1. What this document extracts

The project contains a **finite-dimensional** renormalization/coarse-graining prototype:

- start with a density \(\rho_t\) evolving under heat flow,
- reparametrize \(\rho_t = Z_t^{-1}e^{-S_t}\),
- derive a PDE for \(S_t\) and for its Hessian \(H_t=\nabla^2 S_t\).

This is then interpreted as a curvature-evolution model for RG, with numerics suggesting:

1. a **Riccati law** for the minimal Hessian eigenvalue,
2. a nearly **universal decay constant** \(\alpha\) across modes,
3. and the possibility of arresting curvature decay by adding a **Haar source term**.

---

## 2. vHJ equation from the heat equation (standard derivation)

Assume \(\rho_t>0\) solves the heat equation on \(\mathbb{R}^n\):
\[
  \partial_t \rho_t = \Delta \rho_t.
\]
Write
\[
  \rho_t(x) = Z_t^{-1} e^{-S_t(x)}.
\]
A direct computation yields (up to an additive time-dependent constant):
\[
  \partial_t S_t = \Delta S_t - |\nabla S_t|^2.
\]
This is the viscous Hamilton–Jacobi (vHJ) equation.

---

## 3. Hessian flow and the Riccati mechanism

Let \(H_t = \nabla^2 S_t\).
Differentiating the vHJ equation produces a parabolic evolution equation for \(H_t\).
In many settings, one obtains a differential inequality for the minimal eigenvalue
\[
  \lambda(t) := \lambda_{\min}(H_t)
\]
of the schematic form
\[
  \lambda'(t) \ge -2\lambda(t)^2
\]
(“Riccati decay”), possibly plus additional source terms.

The project’s use of this is conceptual:

- Gaussian smoothing destroys curvature unless a positive source term exists.
- A positive source term can stabilize \(\lambda(t)\) at a positive plateau.

---

## 4. Project’s “Haar source” modification (programmatic extension)

The project proposes adding a positive curvature source \(c_0\) (motivated by the SU(3) Haar Jacobian mass term):
\[
  \lambda'(t) \ge -2\lambda(t)^2 + 2c_0.
\]
This ODE has a stable positive fixed point
\[
  \lambda_* = \sqrt{c_0}.
\]
Interpreted literally, this would mean curvature does not decay to zero along the RG flow if the Haar contribution is strong enough.

**Status:** This is a programmatic bridge step: it is not automatically valid for lattice Yang–Mills without proving that the effective action along coarse-graining inherits a source term of this form.

---

## 5. Numerical evidence recorded in the project (vHJ PDE simulation)

A recorded run (4D grid \(L=24\), viscosity \(\nu=0.01\), \(t\in[0,500]\)) fits multiple curvature modes to the Riccati prediction
\[
  \lambda_{\mathrm{pred}}(t) = \Big(\frac{1}{\lambda_0}+\alpha t\Big)^{-1}.
\]

The fitted \(\alpha\) values:

| Mode | \(\alpha\) |
|---:|---:|
| 0 | 0.0010030 |
| 1 | 0.0010025 |
| 2 | 0.0010028 |
| 3 | 0.0010026 |

Mean and relative variation:
\[
  \bar\alpha \approx 0.0010027,\qquad
  \frac{\sigma_\alpha}{\bar\alpha}\approx 0.04\%.
\]

A separate long-trajectory check for mode 0 compares measured \(\lambda(t)\) to \(\lambda_{\mathrm{pred}}(t)\) at \(t=100,200,300,400,500\), with reported relative errors \(\sim 10^{-5}\)–\(10^{-4}\).

**Interpretation (finite-dimensional):** the vHJ/Hessian flow prototype behaves as if \(\lambda(t)\) is governed by an effective Riccati law with an empirically stable \(\alpha\).

---

## 6. Why this matters for the larger pipeline

This vHJ package is the project’s candidate replacement for “Gaussian RG,” because it:

- has a clean PDE derivation,
- gives an explicit curvature evolution,
- and appears numerically stable in 4D.

If one could connect lattice Yang–Mills coarse-graining to a semigroup with the same curvature evolution structure, then:

- a Haar-like curvature source could stabilize convexity across scales,
- enabling LSI and spectral-gap arguments downstream.

---

## 7. What would upgrade this from prototype to theorem component

1. **Semigroup identification:** a precise statement of the coarse-graining semigroup for YM and why it satisfies a vHJ-type evolution for an effective action \(S_t\).
2. **Locality/carré-du-champ control:** to justify turning curvature bounds into LSI/gap bounds in the interacting model.
3. **Source-term theorem:** an analytic lemma proving that Haar geometry contributes a nonvanishing positive curvature source along the coarse-graining flow (not just at \(t=0\)).
