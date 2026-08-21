---
title: "EXTRACT 02 — Projected Bochner–Hessian Flow: Riccati Comparison as a Mass-Gap Engine"
project: "SWIM2"
source_files:
  - "SYNTH_P06_riccati_hessian_flow.md"
  - "SYNTH_P14_rg_flow_stability.md"
  - "SYNTH_P20_stratified_parabolic_principle.md"
status: "extracted synthesis"
---

# Projected Bochner–Hessian Flow: Riccati Comparison as a Mass-Gap Engine

## Abstract

This note extracts the project’s “dynamical” mass-gap engine:

1. Model the RG/gradient-flow evolution of an effective action \(S_t\) as a *viscous Hamilton–Jacobi* equation on (regular) gauge orbit space.
2. Differentiate twice to get a *Projected Bochner–Hessian (PBH) flow* for the Hessian \(h_t=\nabla_H^2 S_t\).
3. Use a (tensor) parabolic maximum principle to convert PBH into a **scalar Riccati inequality** for the smallest eigenvalue \(\lambda_{\min}(t)\).
4. Conclude: if the effective source \(\sigma(t)\) stays uniformly positive (after controlling geometric corrections), then \(\lambda_{\min}(t)\) is bounded away from zero and flows to a positive fixed point — interpreted as a mass gap.

What’s exciting is the *structural modularity*: the hard QFT content gets localized into a handful of explicit hypotheses (anomaly positivity, curvature suppression, trace control), while the PDE mechanism becomes a rigid comparison theorem.

---

## 1. The viscous Hamilton–Jacobi ansatz

On the regular orbit space \(\mathcal{M}_{\mathrm{reg}}\), posit a flow
\[
\partial_t S_t \;=\; \Delta_H S_t \;-\; |\nabla_H S_t|^2 \;+\; J_t.
\]
Here:

- \(\nabla_H,\Delta_H\) are the horizontal gradient/Laplacian (i.e. projected to physical directions),
- \(J_t\) is a forcing term that encodes RG effects (often linked to anomaly / beta-function data in the project narrative).

Define:
\[
V_t := \nabla_H S_t,
\qquad
h_t := \nabla_H^2 S_t.
\]

---

## 2. The PBH flow for the Hessian

Differentiating the viscous HJ equation yields the schematic PBH evolution:
\[
\partial_t h_t
=
\Delta_H h_t
- 2\nabla_{V_t} h_t
- 2 h_t^2
+ S_{\mathrm{anom}}(t)
+ \mathfrak{G}(S_t,h_t).
\]

- The term \(-2 h_t^2\) is the **Riccati nonlinearity**.
- \(S_{\mathrm{anom}}(t)=\nabla_H^2 J_t\) is the **source** term.
- \(\mathfrak{G}\) is a **geometric correction** (curvature of orbit space, non-integrability of horizontals, etc.).

This is the point where the project strongly echoes Hamilton’s matrix maximum principle from Ricci flow: a tensor PDE generates a scalar inequality for the smallest eigenvalue.

---

## 3. From tensor PDE to scalar inequality (minimum eigenvalue)

Let \(\lambda_{\min}(t,x)\) be the smallest eigenvalue of the symmetric bilinear form \(h_t(x)\). Under appropriate smoothness and avoidance of singular strata, one can argue:

- At a spacetime point where \(\lambda_{\min}\) achieves a minimum (over \(x\)), the diffusion and transport contributions are nonnegative in the comparison sense.
- The quadratic term contributes \(-2\lambda_{\min}^2\).
- The source term contributes \(\ge \sigma(t)\) where
  \[
  \sigma(t):=\inf_{x\in\mathcal{M}_{\mathrm{reg}}}\inf_{\|v\|=1}\langle v,S_{\mathrm{anom}}(t,x)v\rangle.
  \]
- The geometric correction is bounded by something suppressed by \(g(t)^2\) (asymptotic freedom hypothesis).

This yields the differential inequality (schematic):
\[
\partial_t \lambda_{\min}(t)
\;\ge\;
-2\lambda_{\min}(t)^2
+
\sigma(t)
-
\mathrm{Err}(t),
\]
where \(\mathrm{Err}(t)\) is a controlled correction, typically \(\mathrm{Err}(t)\lesssim g(t)^2 H_{\mathrm{Tr}}\) in the project’s conditional theorem.

---

## 4. Riccati comparison = “gap forcing”

Drop the error term (or dominate it by reducing \(\sigma\)) and compare to the ODE
\[
\dot{\ell}(t) = -2\ell(t)^2 + \sigma_{\min},\qquad \sigma_{\min}:=\inf_t \sigma(t) >0.
\]

Then:

- If the comparison is valid, \(\lambda_{\min}(t)\ge \ell(t)\) for all \(t\).
- The ODE has stable fixed point
  \[
  \ell_\ast = \sqrt{\frac{\sigma_{\min}}{2}} >0,
  \]
  so the flow *forces* a strictly positive lower bound.

This is the project’s cleanest “engine”: once the inequality is obtained, the rest is ODE.

> **Caveat** (important): the Riccati ODE can blow up to \(-\infty\) in finite time if the initial value is too negative. So the comparison-based argument needs either (i) a non-too-negative initial lower bound, or (ii) a diffusion mechanism that prevents the global minimum from following the ODE blow-down.

---

## 5. Conditional RG stability (the project’s modular hypothesis list)

The project’s conditional theorem packages the needed inputs as:

1. **Curvature suppression:** \(|K_t|\lesssim g(t)^2\).
2. **Trace control:** \(\mathrm{Tr}(h_t^+)\le H_{\mathrm{Tr}}\) uniformly.
3. **Uniform source positivity:** \(\sigma(t)\ge \sigma_A>0\).
4. **Asymptotic freedom:** \(g(t)\to 0\) in the relevant regime.
5. **Initial positivity:** \(\lambda_{\min}(T_0)\ge \lambda_\ast>0\) at some scale.

Given these, one gets for large \(t\):
\[
\partial_t\lambda_{\min}(t) \ge -2\lambda_{\min}(t)^2 + \frac{\sigma_A}{2},
\]
and hence a persistent positive lower bound.

---

## 6. Why this feels “theory-generating”

The PBH+comparison structure is abstract enough to travel:

- It can be applied to other gauge groups (or sigma models) where the configuration space is a curved manifold and the action defines a measure.
- It suggests a general principle:  
  **a uniformly positive forcing term in the Hessian flow makes convexity (hence a gap) an attractor.**
- It reframes “mass gap” as a geometric property of an evolving functional under coarse-graining.

---

## 7. Next research moves that would actually de-risk the program

1. **Write the PBH derivation cleanly in one consistent framework.**  
   (Finite-dimensional cutoff first; then limit.)

2. **Make the tensor maximum principle rigorous on a stratified orbit space.**  
   This is where polarity/capacity ideas enter (see EXTRACT 03).

3. **Identify the physical meaning of \(J_t\) and prove \(\nabla_H^2J_t\ge 0\).**  
   This is the “anomaly source positivity” bottleneck (see EXTRACT 04).

4. **Prove uniform bounds that are stable under RG blocking.**  
   Trace bounds, curvature bounds, and projection consistency are the pieces that can fail under naive coarse-graining.

