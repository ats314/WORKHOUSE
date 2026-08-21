---
title: "Core Curvature Theorem: Local CD(ρ,∞) for Gauge-Invariant Observables"
author: "Project extraction"
date: "2025-12-29"
---

# Overview

This note extracts the project’s **interface theorem**: how a **horizontal Bakry--Émery curvature bound** turns into a **local curvature--dimension condition** \(CD(\rho,\infty)\) *for gauge-invariant observables*. This is where the geometry finally touches functional inequalities.

The key statement is Theorem 7.2, which pairs a horizontal curvature bound with a \(CD(\rho,\infty)\) inequality for gauge invariants on a uniform small-field ball. 【218:14†PART_II_SECTION_7_Core_Curvature_Theorem_and_Interface_to_Part_I_UPDATED.md†L1-L24】

---

# 1. Two structural facts used by the project

## 1.1 Gauge invariants have horizontal gradients

Let \(\mathcal A_\Lambda^{\mathrm{inv}}\) denote smooth gauge-invariant observables on \(M_\Lambda\). The project uses the standard observation:

\[
f\in \mathcal A_\Lambda^{\mathrm{inv}}
\quad\Longrightarrow\quad
\nabla f(U)\in H_U.
\]

Intuitively: gauge invariance means \(f\) is constant along gauge orbits, so its derivative annihilates vertical directions, hence the gradient lies in the horizontal complement. 【218:3†PART_II_SECTION_7_Core_Curvature_Theorem_and_Interface_to_Part_I_UPDATED.md†L29-L33】

## 1.2 Bochner--Bakry--Émery identity

For the diffusion generator \(L_\Lambda\) associated to \((M_\Lambda,g_\Lambda,\mu_\Lambda)\), the project invokes the pointwise identity
\[
\Gamma_{2,\Lambda}(f)
=
\|\nabla^2 f\|_{\mathrm{HS}}^2
+
\operatorname{Ric}_{\mu_\Lambda}(\nabla f,\nabla f),
\]
where \(\Gamma_\Lambda(f)=|\nabla f|_{g_\Lambda}^2\). 【218:3†PART_II_SECTION_7_Core_Curvature_Theorem_and_Interface_to_Part_I_UPDATED.md†L33-L37】

---

# 2. From horizontal curvature to a local CD inequality

Assume that on a region \(\Omega\subset M_\Lambda\), one has the **horizontal curvature bound**
\[
\operatorname{Ric}_{\mu_\Lambda}(U)(v,v)\ge \rho_{\mathrm{loc}}\,|v|^2
\quad
\forall U\in \Omega,\ \forall v\in H_U.
\]

Take \(f\in \mathcal A_\Lambda^{\mathrm{inv}}\). Then \(\nabla f\in H_U\), so on \(\Omega\),
\[
\operatorname{Ric}_{\mu_\Lambda}(\nabla f,\nabla f)
\ge
\rho_{\mathrm{loc}}\,|\nabla f|^2
=
\rho_{\mathrm{loc}}\,\Gamma_\Lambda(f).
\]
Since \(\|\nabla^2 f\|_{\mathrm{HS}}^2\ge 0\), the Bochner identity yields:
\[
\Gamma_{2,\Lambda}(f)
\ge
\rho_{\mathrm{loc}}\,\Gamma_\Lambda(f)
\qquad\text{on }\Omega.
\]
This is exactly a **local \(CD(\rho_{\mathrm{loc}},\infty)\) condition**, but *only for gauge-invariant observables*.

The project spells this out explicitly on the small-field ball \(B_r(U^{(0)})\). 【218:3†PART_II_SECTION_7_Core_Curvature_Theorem_and_Interface_to_Part_I_UPDATED.md†L39-L46】

---

# 3. Extracted statement (Theorem 7.2)

The project bundles the small-field horizontal curvature theorem and the induced \(CD\) inequality into:

> **Theorem 7.2 (Core curvature theorem).**  
> There exist \(\rho_{\mathrm{loc}}>0\) and \(r>0\), independent of the finite volume \(\Lambda\), such that on the small-field ball \(B_r(U^{(0)})\):
>
> 1. \(\operatorname{Ric}_{\mu_\Lambda}(U)\) is bounded below by \(\rho_{\mathrm{loc}}\) on horizontal vectors, and  
> 2. for every smooth gauge-invariant \(f\), one has
> \[
> \Gamma_{2,\Lambda}(f)(U)\ge \rho_{\mathrm{loc}}\,\Gamma_\Lambda(f)(U)
> \quad\forall U\in B_r(U^{(0)}).
> \]
【218:14†PART_II_SECTION_7_Core_Curvature_Theorem_and_Interface_to_Part_I_UPDATED.md†L1-L24】

---

# 4. Immediate consequences (local functional inequalities)

Part I of the project records the standard implication:

\[
CD(\rho,\infty)
\ \Rightarrow\
\text{Poincaré with constant }1/\rho
\ \text{ and LSI with constant }2/\rho.
\]
【158:0†Part_I_Section_3_Lyapunov_UPDATED.md†L5-L23】

In this project’s setting, the conclusion is **local and restricted**:

- it holds on \(B_r(U^{(0)})\), not globally, and
- it controls gauge-invariant observables, where the relevant gradients are horizontal.

This restriction is the key “hack” that makes curvature methods compatible with gauge symmetry.

---

# 5. What remains to turn this into physics

Theorem 7.2 is a powerful local estimate, but physics happens globally and at infinite volume. The project itself flags two remaining tasks:

1. show that \(\mu_\Lambda\) concentrates in (or returns quickly to) the small-field region, uniformly in \(\Lambda\); and  
2. propagate the local \(CD\) bound into a **global** Poincaré/LSI via Lyapunov or decomposition arguments. 【218:14†PART_II_SECTION_7_Core_Curvature_Theorem_and_Interface_to_Part_I_UPDATED.md†L40-L48】

The next extracted document isolates the project’s chosen propagation tool: local-to-global Poincaré via Lyapunov drift, adapted to a restricted class of observables.
