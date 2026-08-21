# Projected Bochner–Hessian Flow and the Riccati Mass-Gap Mechanism

**Purpose.** This note extracts (and slightly reorganizes) the core novel idea in the project:  
recasting the **RG evolution of Yang–Mills effective actions** into a **geometric parabolic PDE** on the *gauge orbit space*, then turning a complicated tensor evolution into a **scalar Riccati inequality** whose stable fixed point is a **mass gap**.

This is primarily synthesized from the project’s PBH/RG stability and Riccati analyses (notably `SYNTH_P14_rg_flow_stability.md`, `SYNTH_P06_riccati_hessian_flow.md`, and the stratified/parabolic principle framework in `SYNTH_P20_stratified_parabolic_principle.md`).

---

## 1. The PBH viewpoint

Let \(\mathcal{M}_{\mathrm{reg}}\) denote the *regular stratum* of the gauge orbit space \(\mathcal{A}/\mathcal{G}\), equipped with the metric induced by the \(L^2\) inner product on connections (or its finite-dimensional lattice/Galerkin analogue).  

Let \(S_t:\mathcal{M}_{\mathrm{reg}}\to\mathbb{R}\) denote a scale-dependent “effective action” (think: Wilsonian/FRG effective action, or a viscous Hamilton–Jacobi surrogate).

### 1.1 Horizontal viscous Hamilton–Jacobi equation

The guiding ansatz is the **horizontal viscous Hamilton–Jacobi (vHJ)** equation
\[
\partial_t S_t
= \Delta_H S_t \; - \; \lvert\nabla_H S_t\rvert^2 \; + \; J_t,
\tag{vHJ}
\]
where
- \(\nabla_H, \Delta_H\) are the horizontal gradient/Laplacian on \(\mathcal{M}_{\mathrm{reg}}\), and  
- \(J_t\) is the forcing term (the “anomaly source”, often tied to the beta function / trace anomaly).

Define the *horizontal drift* and *horizontal Hessian*
\[
V_t := \nabla_H S_t,
\qquad
h_t := \nabla_H^2 S_t \quad (\text{a symmetric 2-tensor}).
\]

---

## 2. Deriving the PBH flow for the Hessian

Differentiate (vHJ) twice using the Levi–Civita connection on \(\mathcal{M}_{\mathrm{reg}}\). The schematic identities used are classical:

1. Commuting Hessian with Laplacian introduces curvature:
\[
\nabla^2 (\Delta f)
= \Delta (\nabla^2 f) \; + \; \mathcal{R} * \nabla^2 f \; + \; (\nabla\mathrm{Ric}) * \nabla f,
\]
for a smooth \(f\) on a Riemannian manifold.

2. Differentiating the quadratic drift term produces the Riccati nonlinearity:
\[
\nabla^2(\lvert\nabla f\rvert^2)
= 2(\nabla^2 f)^2 + 2\nabla_{\nabla f}(\nabla^2 f) + (\text{curvature terms}).
\]

Under the project’s “horizontal projection” bookkeeping, this yields the **Projected Bochner–Hessian (PBH) flow**
\[
\boxed{
\partial_t h_t
=
\Delta_H h_t
-2\nabla_{V_t} h_t
-2 h_t^2
+ S_{\mathrm{anom}}(t)
+ \mathfrak{G}(S_t,h_t),
}
\tag{PBH}
\]
where
\[
S_{\mathrm{anom}}(t) := \nabla_H^2 J_t
\]
and \(\mathfrak{G}\) collects the curvature/non-integrability correction terms (the “geometric junk drawer”).

**What is conceptually new here (as a package).**  
Bochner identities, tensor maximum principles, and RG/vHJ heuristics are all old friends.  
But packaging them into a *single* PBH Hessian flow on orbit space, with explicit hypotheses that isolate what needs proving (\(\sigma>0\), curvature control, trace control, etc.), is the distinctive move of this project.

---

## 3. From tensor PDE to scalar Riccati inequality

Let \(\lambda_{\min}(t,x)\) be the minimal eigenvalue of \(h_t(x)\) (restricted to horizontal/physical directions).

### 3.1 Local eigenvalue inequality (regular stratum)

At a spacetime point \((t_0,x_0)\) where \(\lambda_{\min}\) achieves its spatial minimum (or by using a tensor maximum principle directly), the diffusion and transport terms do not decrease the minimum eigenvalue. The Riccati term contributes \(-2\lambda_{\min}^2\). Hence one gets the schematic inequality
\[
\partial_t \lambda_{\min}
\ge
-2\lambda_{\min}^2
+
\sigma(t,x)
-
\varepsilon(t,x),
\tag{*}
\]
with
\[
\sigma(t,x) := \lambda_{\min}\big(S_{\mathrm{anom}}(t,x)\big),
\qquad
\varepsilon(t,x) := \text{the projected contribution of }\mathfrak{G}.
\]

### 3.2 The project’s “dominance” hypothesis

The PBH stability result is conditional on a dominance statement of the form:

- **Uniform anomaly positivity:** \(\sigma(t,x)\ge \sigma_A>0\).
- **Geometric corrections are suppressed:** \(\varepsilon(t,x)\lesssim g(t)^2\,\mathrm{Tr}_+(h_t)\), with \(g(t)\to 0\) in the UV.

This yields, for large enough \(t\),
\[
\partial_t \lambda_{\min}
\ge
-2\lambda_{\min}^2 + \frac{\sigma_A}{2}.
\tag{Riccati-ineq}
\]

### 3.3 Comparison with a Riccati ODE

Let \(\underline\lambda(t)\) solve the ODE
\[
\underline\lambda'(t) = -2\underline\lambda(t)^2 + \frac{\sigma_A}{2}.
\tag{Riccati}
\]
This ODE has stable fixed point
\[
\underline\lambda_* = \sqrt{\frac{\sigma_A}{4}}.
\]

By a standard comparison principle (scalar parabolic + ODE comparison), one concludes
\[
\lambda_{\min}(t,\cdot)\ge \underline\lambda(t)
\quad\Rightarrow\quad
\liminf_{t\to\infty}\lambda_{\min}(t,\cdot)
\ge
\sqrt{\frac{\sigma_A}{4}}.
\]

---

## 4. Interpreting \(\lambda_{\min}\) as a mass scale

Heuristically:
- \(h_t\) is the Hessian of the effective action in physical directions.
- A uniform positive lower bound on \(h_t\) is **uniform convexity** of the effective action.
- Uniform convexity implies a **spectral gap** for the associated Langevin generator, and (under reconstruction/sector-identification) a **mass gap** for the quantum Hamiltonian.

In this “geometric RG” picture, the mass gap is not conjured from thin air; it is the stable fixed point of a Riccati competition:
- nonlinear damping \(-2\lambda^2\) vs.
- positive anomaly forcing \(+\sigma\).

---

## 5. Where the hard work actually lives

PBH + Riccati is a clean machine. The world is not obligated to be clean.  
The machine demands several nontrivial inputs:

1. **Derivation/meaning of (vHJ)** from an RG framework (FRG/Wetterich, Wilsonian coarse-graining, etc.).  
2. **Control of \(\mathfrak{G}\)** (curvature/non-integrability) along the RG trajectory.  
3. **Uniform positivity of the anomaly Hessian** on the physical sector (the project’s “\(\sigma>0\)” bottleneck).  
4. **Singularities:** \(\mathcal{A}/\mathcal{G}\) is stratified; reducibles sit in lower strata. The maximum principle needs to survive this (see `EXTRACT_Polarity_Stratified_Max_Principle.md`).

---

## 6. Why this is an exciting bridge

This PBH/Riccati pipeline suggests a broader viewpoint:

> **“Mass generation as curvature control under a parabolic RG.”**

It rhymes with:
- Hamilton's tensor maximum principles in Ricci flow,
- Bakry–Émery curvature forcing functional inequalities,
- viscous Hamilton–Jacobi as a nonlinear heat flow for an action functional.

If the missing hypotheses can be nailed down rigorously, the PBH approach is a plausible *new bridge* between nonperturbative QFT and geometric analysis.

---

## Appendix A. A minimal checklist for a rigorous version

A fully rigorous theorem would likely be stated for a finite-dimensional cutoff theory first:

1. \(\mathcal{M}_{\mathrm{reg}}\) is a smooth Riemannian manifold, embedded as the regular stratum of a stratified space \(\mathcal{M}\).
2. \(S_t\) is smooth on \(\mathcal{M}_{\mathrm{reg}}\) and solves (vHJ) there.
3. \(S_{\mathrm{anom}}=\nabla_H^2 J_t\) satisfies \(\sigma(t,x)\ge\sigma_A>0\).
4. \(\mathfrak{G}\) satisfies a quantitative bound \(|\langle \mathfrak{G},v\otimes v\rangle|\le Cg(t)^2\,\mathrm{Tr}_+(h_t)\).
5. \(\mathrm{Tr}_+(h_t)\) remains uniformly bounded.
6. The singular set \(\Sigma:=\mathcal{M}\setminus\mathcal{M}_{\mathrm{reg}}\) is polar for the relevant diffusion (so the maximum principle can be applied “as if” \(\Sigma\) were absent).

Then the Riccati comparison gives a uniform positive lower bound on \(\lambda_{\min}\) for \(t\) large.
