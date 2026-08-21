# Projected Bochner–Hessian Flow and Riccati Comparison for Gap Persistence

## Abstract

This note records a novel analytic framework appearing in the project: a **Projected Bochner–Hessian (PBH) flow** for the *horizontal Hessian* of an effective action along RG time. The PBH equation combines:

- a horizontal diffusion term \(\Delta_H h_t\),
- a transport term \(-2\nabla_{V_t}h_t\),
- a quadratic damping term \(-2h_t^2\) (Riccati-type),
- a forcing term \(S_{\mathrm{anom}}(t)=\nabla_H^2 J_t\),
- and geometric corrections \(\mathfrak G(S_t,h_t)\) controlled by curvature.

Under explicit hypotheses (curvature bound, trace bound, uniform positive anomaly source, asymptotic freedom, and an initial gap), one obtains a scalar Riccati inequality for the minimal eigenvalue \(\lambda_{\min}(t)\), yielding a uniform positive lower bound and a stable positive equilibrium.

---

## 1. Setting: finite-dimensional gauge orbit space at fixed cutoff

Work at a fixed finite cutoff (e.g., finite lattice or Galerkin truncation) where the *regular stratum* of the gauge orbit space is a smooth finite-dimensional Riemannian manifold
\[
\mathcal M_{\mathrm{reg}}=\mathcal A_{\mathrm{reg}}/\mathcal G.
\]

Let \(S_t:\mathcal M_{\mathrm{reg}}\to\mathbb R\) be a time-dependent effective action.  
Introduce the horizontal gradient and Hessian
\[
V_t:=\nabla_H S_t,\qquad h_t:=\nabla_H^2 S_t,
\]
a symmetric bilinear form on horizontal tangent vectors.

---

## 2. Horizontal viscous Hamilton–Jacobi equation

Assume \(S_t\) solves the horizontal viscous Hamilton–Jacobi PDE
\[
\partial_t S_t = \Delta_H S_t - |\nabla_H S_t|^2 + J_t,
\]
where \(J_t\) is an RG forcing/anomaly functional.

Define the *anomaly source tensor*
\[
S_{\mathrm{anom}}(t):=\nabla_H^2 J_t.
\]

---

## 3. The PBH flow for the horizontal Hessian

### 3.1 Formal derivation

Differentiate the Hamilton–Jacobi equation twice using the horizontal Levi–Civita connection. Schematically,

- \(\nabla_H^2(\Delta_H S_t)\) produces \(\Delta_H h_t\) plus curvature commutator terms;
- \(\nabla_H^2(|\nabla_H S_t|^2)\) produces a transport term and the quadratic term \(2h_t^2\);
- \(\nabla_H^2(J_t)=S_{\mathrm{anom}}(t)\).

Collecting terms gives the **Projected Bochner–Hessian flow**
\[
\boxed{
\partial_t h_t
=
\Delta_H h_t
-2\nabla_{V_t}h_t
-2h_t^2
+S_{\mathrm{anom}}(t)
+\mathfrak G(S_t,h_t).
}
\tag{PBH}
\]
Here \(\mathfrak G(S_t,h_t)\) bundles curvature terms and horizontal non-integrability corrections. (The project documents explicitly present this boxed equation as the PBH flow.)

### 3.2 Novelty note

The PBH flow is not a standard object in the Yang–Mills literature: it is a bespoke “RG-as-geometric-flow” formulation that allows one to import matrix maximum principles and Riccati comparison into the RG stability problem.

---

## 4. Hypotheses that lead to a Riccati inequality

Let \(\lambda_{\min}(t,x)\) denote the smallest eigenvalue of \(h_t(x)\) on horizontal unit vectors. The framework assumes:

### (Curv) Curvature bound (suppressed by \(g(t)^2\))

There exists \(C_0>0\) such that the horizontal sectional curvature satisfies
\[
|K_t(X,Y)|\le C_0\, g(t)^2
\qquad
\text{for all unit horizontal }X,Y,\ \forall t\ge 0,
\]
where \(g(t)\) is the running coupling.

### (Trace) Uniform trace bound

There exists \(H_{\mathrm{Tr}}<\infty\) such that
\[
\sum_i \max\{\lambda_i(t,x),0\}\le H_{\mathrm{Tr}}
\qquad \text{for all }t\ge 0,\ x\in\mathcal M_{\mathrm{reg}}.
\]

### (Anom) Uniform positive anomaly source

There exists \(\sigma_A>0\) with
\[
\inf_{x\in\mathcal M_{\mathrm{reg}}}\ \inf_{\|v\|=1}
\langle v,S_{\mathrm{anom}}(t,x)v\rangle \;\ge\;\sigma_A
\qquad\forall t\ge 0.
\]

### (AF) Asymptotic freedom

\[
\lim_{t\to\infty} g(t)=0.
\]

### (Init) Initial gap

At some time \(T_0\), \(\lambda_{\min}(T_0,\cdot)\ge \lambda_\ast>0\).

---

## 5. Bounding the geometric correction term

Under (Curv) and (Trace), the PBH correction satisfies a pointwise bound of the form
\[
|\langle \mathfrak G(S_t,h_t), v\otimes v\rangle|
\le C_1\, g(t)^2\,\|h_t\|_{\mathrm{Tr}}
\le C_1\, g(t)^2\,H_{\mathrm{Tr}}
\qquad (\|v\|=1),
\]
for some constant \(C_1>0\).

This is the key estimate: it turns geometric complexity into a small \(O(g(t)^2)\) perturbation.

---

## 6. Matrix maximum principle → scalar Riccati inequality

Evaluating (PBH) on a minimal-eigenvalue unit eigenvector \(v_0(t,x)\), and applying the standard tensor maximum principle heuristics:

- diffusion \(\Delta_H h_t\) does not decrease the minimum,
- transport \(-2\nabla_{V_t}h_t\) does not decrease the minimum,
- the quadratic term gives \(-2\lambda_{\min}^2\),
- the anomaly source gives \(+\sigma_A\),
- the correction term is bounded by \(\pm C_1 g(t)^2H_{\mathrm{Tr}}\).

Thus one obtains a **scalar differential inequality**
\[
\partial_t \lambda_{\min}(t)
\;\ge\;
-2\lambda_{\min}(t)^2
+\sigma_A
-C_1 g(t)^2 H_{\mathrm{Tr}}.
\tag{Riccati-ineq}
\]

---

## 7. Dominance in the asymptotically free regime

By (AF), choose \(T_1\ge T_0\) so that for \(t\ge T_1\),
\[
C_1 g(t)^2H_{\mathrm{Tr}} < \frac{\sigma_A}{2}.
\]
Then for \(t\ge T_1\),
\[
\partial_t \lambda_{\min}(t)
\;\ge\;
-2\lambda_{\min}(t)^2
+\frac{\sigma_A}{2}.
\tag{Riccati-UV}
\]

---

## 8. Riccati comparison and positive equilibrium

Consider the autonomous ODE
\[
\dot\lambda = -2\lambda^2+\frac{\sigma_A}{2}.
\]
It has a stable equilibrium
\[
\lambda_{\mathrm{eq}}
=
\sqrt{\frac{1}{2}\cdot\frac{\sigma_A}{2}}
=
\frac{\sqrt{\sigma_A}}{2}.
\]
By standard ODE comparison principles, if \(\lambda_{\min}(T_1)\ge \lambda_0>0\), then
\[
\lambda_{\min}(t)\ge \min\{\lambda_0,\lambda_{\mathrm{eq}}\}
\qquad \forall t\ge T_1,
\]
and in fact \(\lambda_{\min}(t)\) is driven toward the positive equilibrium scale.

This is the analytic “engine”: *positive forcing + Riccati damping + small geometric error* \(\Rightarrow\) persistent gap.

---

## 9. What remains to make this unconditional

This PBH/Riccati pipeline reduces the mass-gap persistence problem to verifying the hypotheses in a single coherent package.

Key missing pieces are:

1. **Nonperturbative positivity of \(S_{\mathrm{anom}}\) on horizontals.**  
   This is Conjecture B in the project’s language.

2. **Derivation of the PBH flow with precise control of \(\mathfrak G\)** in the exact gauge-orbit geometry (including gauge-fixing subtleties).

3. **Uniformity across cutoffs**: ensuring that the constants \(\sigma_A,H_{\mathrm{Tr}},C_1\) behave well in the continuum limit.

Even as a conditional theorem, PBH is valuable because it clarifies exactly where “physics intuition” enters and how it must be quantified.
