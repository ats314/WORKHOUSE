---
title: "EXTRACT 02 — Local Horizontal Bakry–Émery Curvature for Lattice Yang–Mills"
date: "2025-12-29"
format: "markdown+latex"
source_files:
  - "PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound_UPDATED(1).md"
  - "PART_II_SECTION_7_Core_Curvature_Theorem_and_Interface_to_Part_I_UPDATED(1).md"
  - "PART_II_SECTION_3_Gauge_Orbits_and_Horizontal_Subspaces.md"
  - "PART_II_SECTION_2_Wilson_Action_and_Gauge_Invariance(1).md"
---

# Local horizontal curvature: a finite-volume \(CD(\rho,\infty)\) seed near the vacuum

This extract packages the project’s “small-field” curvature mechanism into a standalone statement.

## 1. Configuration space, gauge orbits, horizontals

Let \(G\) be a compact connected Lie group with a bi-invariant metric \(g_G\).  
For a finite lattice \(\Lambda\), define the configuration manifold
\[
M_\Lambda := G^{E(\Lambda)},
\]
with the product metric \(g_\Lambda\) and product Haar volume \(d\mathrm{vol}_{g_\Lambda}\).

The lattice gauge group \(\mathcal G_\Lambda\) acts on \(M_\Lambda\) by
\[
(g\cdot U)_{(x\to y)} \;=\; g_x\, U_{(x\to y)}\, g_y^{-1}.
\]

At each \(U\in M_\Lambda\), let

- \(V_U\subset T_U M_\Lambda\) be the **vertical** subspace tangent to the gauge orbit through \(U\),
- \(H_U:=V_U^\perp\) be its orthogonal complement (“horizontal” / physical directions).

**Key point:** for any smooth gauge-invariant observable \(f\), the gradient is horizontal:
\[
\nabla f(U)\in H_U.
\]

## 2. Gibbs measure and Bakry–Émery tensor

Let \(S_\Lambda\in C^2(M_\Lambda)\) be a smooth gauge-invariant effective action and define the finite-volume Gibbs measure
\[
d\mu_\Lambda(U) := Z_\Lambda^{-1} e^{-S_\Lambda(U)}\, d\mathrm{vol}_{g_\Lambda}(U).
\]

The Bakry–Émery Ricci tensor is
\[
\mathrm{Ric}_{\mu_\Lambda} \;=\; \mathrm{Ric}_{g_\Lambda} \;+\; \nabla^2 S_\Lambda.
\]

For \(f\in C^\infty(M_\Lambda)\), the Bochner/Bakry–Émery identity reads
\[
\Gamma_{2,\Lambda}(f)
=
\|\nabla^2 f\|_{\mathrm{HS}}^2
+
\mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f),
\]
so a lower bound on \(\mathrm{Ric}_{\mu_\Lambda}\) in the directions of \(\nabla f\) yields a curvature–dimension condition.

Since \(\nabla f\) is horizontal for gauge-invariant \(f\), it is enough to lower-bound \(\mathrm{Ric}_{\mu_\Lambda}\) **on horizontals**.

## 3. Local horizontal curvature bound at the vacuum

Let \(U^{(0)}\in M_\Lambda\) be the trivial configuration (all links \(=e\)).  
Assume:

1. **Group Ricci positivity.**
   \[
   \mathrm{Ric}_{g_\Lambda}\ge \kappa_G\, g_\Lambda
   \qquad\text{with }\kappa_G>0,
   \]
   uniformly in \(\Lambda\) (true since \(M_\Lambda\) is a product).

2. **Action decomposition and Hessian lower bound.**  
   Write \(S_\Lambda = S_W + S_{\mathrm{add},\Lambda}\), where:

   - \(S_W\) is the Wilson action,
   - \(S_{\mathrm{add},\Lambda}\) is any additional smooth gauge-invariant term (gauge-fixing, regulator, etc.) whose Hessian satisfies
     \[
     \nabla^2 S_{\mathrm{add},\Lambda}(U) \;\ge\; -C_{\mathrm{add}}\, g_\Lambda(U)
     \qquad\text{for all }U,
     \]
     with \(C_{\mathrm{add}}\ge 0\) independent of \(\Lambda\).

3. **Dominance of group curvature.**
   \[
     C_{\mathrm{add}} < \kappa_G.
   \]

At \(U^{(0)}\), the Wilson Hessian is nonnegative on horizontals (and strictly positive on the co-exact physical modes). Consequently, for every \(v\in H_{U^{(0)}}\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)
=
\mathrm{Ric}_{g_\Lambda}(v,v) + \nabla^2 S_\Lambda(U^{(0)})(v,v)
\;\ge\;
(\kappa_G - C_{\mathrm{add}})\,|v|^2.
\]
Define
\[
\rho_0 := \kappa_G - C_{\mathrm{add}} \;>\; 0.
\]

## 4. Persistence on a uniform small-field neighborhood

Define the minimal horizontal curvature eigenvalue
\[
\lambda_{\min}^H(U)
:=
\inf_{v\in H_U\setminus\{0\}}
\frac{\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)}{|v|_{g_\Lambda}^2}.
\]
Smooth dependence of \(U\mapsto H_U\) and \(U\mapsto \mathrm{Ric}_{\mu_\Lambda}(U)\) implies \(U\mapsto \lambda_{\min}^H(U)\) is continuous on the regular set.

Since \(\lambda_{\min}^H(U^{(0)})\ge \rho_0\), there exist \(r>0\) and \(\rho_{\mathrm{loc}}>0\) (e.g. \(\rho_{\mathrm{loc}}=\rho_0/2\)) such that
\[
\lambda_{\min}^H(U)\;\ge\;\rho_{\mathrm{loc}}
\qquad
\text{whenever } d_{g_\Lambda}(U,U^{(0)})\le r.
\]
The locality of the action and the product geometry allow \(r,\rho_{\mathrm{loc}}\) to be chosen **independently of \(\Lambda\)**.

## 5. Local \(CD(\rho,\infty)\) for gauge-invariant observables

Let \(f\) be a smooth gauge-invariant observable. For \(U\) in the small-field ball \(B_r(U^{(0)})\), \(\nabla f(U)\in H_U\), hence
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(\nabla f,\nabla f)\;\ge\;\rho_{\mathrm{loc}}\,|\nabla f|^2.
\]
The Bochner identity then yields the pointwise estimate
\[
\Gamma_{2,\Lambda}(f)(U) \;\ge\; \rho_{\mathrm{loc}}\, \Gamma_\Lambda(f)(U)
\qquad
(U\in B_r(U^{(0)})),
\]
i.e. a **local curvature–dimension condition**
\[
CD(\rho_{\mathrm{loc}},\infty)\quad\text{on }B_r(U^{(0)})
\]
for gauge-invariant observables.

## 6. Why this matters

- This is the finite-volume “seed curvature” input used later for local-to-global functional inequalities (Poincaré/LSI) via Lyapunov drift.
- Crucially, the statement is adapted to gauge invariance: only horizontals matter, and horizontals are exactly where gauge-invariant gradients live.
- The mechanism cleanly separates:
  - geometry (\(\kappa_G>0\)),
  - controlled nonconvexity of additional terms (\(C_{\mathrm{add}}\)),
  - and the (optional) extra positivity from the Wilson Hessian on physical modes.
