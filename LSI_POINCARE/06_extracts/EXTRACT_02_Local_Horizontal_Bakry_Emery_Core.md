---
title: "Local Horizontal Bakry--Émery Curvature for Lattice Yang--Mills: the Small-Field Core"
author: "Project extraction"
date: "2025-12-29"
---

# Overview

This note extracts what is (in my judgment) the project's sharpest structural result: a **uniform, finite-volume, small-field lower bound** on the Bakry--Émery curvature **restricted to horizontal (physical) directions**. This is the finite-volume “core estimate” needed to feed \(\Gamma\)-calculus into functional inequalities for **gauge-invariant observables**.

The project states this as Theorem 6.1 and also restates it as Lemma 7.1. 【218:6†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound(2).md†L1-L15】【218:3†PART_II_SECTION_7_Core_Curvature_Theorem_and_Interface_to_Part_I_UPDATED.md†L1-L21】

---

# 1. Geometric setting

Let \(\Lambda\) be a finite lattice and
\[
M_\Lambda := G^{E(\Lambda)}
\]
the space of lattice gauge fields, equipped with the product Riemannian metric \(g_\Lambda\) induced from a bi-invariant metric \(g_G\) on \(G\).

The Gibbs measure is taken relative to the **Riemannian volume reference**:
\[
d\mu_\Lambda(U)=Z_\Lambda^{-1}\,e^{-S_\Lambda(U)}\,d\mathrm{vol}_{g_\Lambda}(U),
\]
and the Bakry--Émery tensor is
\[
\operatorname{Ric}_{\mu_\Lambda}
=
\operatorname{Ric}_{g_\Lambda}+\nabla^2 S_\Lambda.
\]
【218:0†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound_UPDATED.md†L12-L28】

The project emphasizes working with the **horizontal subspace**
\[
H_U \subset T_U M_\Lambda,
\]
defined as the \(g_\Lambda\)-orthogonal complement to gauge orbits (vertical directions). 【218:0†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound_UPDATED.md†L6-L10】

---

# 2. The key “core constant” at the trivial configuration

Write the effective action as
\[
S_\Lambda = S_W + S_{\mathrm{add},\Lambda},
\]
where \(S_W\) is the Wilson action and \(S_{\mathrm{add},\Lambda}\) packages gauge-fixing / regulator / auxiliary terms. 【218:0†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound_UPDATED.md†L34-L42】

At the trivial configuration \(U^{(0)}\), the project records:

1. On horizontal directions, the Wilson Hessian is nonnegative. 【218:8†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound(2).md†L18-L22】

2. The additional term Hessian is bounded below by a uniform constant:
\[
\nabla^2 S_{\mathrm{add},\Lambda}(U)\ge -C_{\mathrm{add}}\,g_\Lambda(U),
\]
with \(C_{\mathrm{add}}\) chosen **independent of \(\Lambda\)** by locality/compactness considerations. 【218:4†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound_UPDATED.md†L24-L47】

3. The product Ricci tensor satisfies a uniform bound
\[
\operatorname{Ric}_{g_\Lambda}\ge \kappa_G\, g_\Lambda,
\]
with \(\kappa_G>0\) depending only on \((G,g_G)\), not on \(\Lambda\). 【218:2†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound_UPDATED.md†L25-L29】

Combining these, at \(U^{(0)}\) and for \(v\in H_{U^{(0)}}\),
\[
\operatorname{Ric}_{\mu_\Lambda}(v,v)
\ge
(\kappa_G - C_{\mathrm{add}})\,|v|_{g_\Lambda}^2.
\]
Thus if \(\kappa_G>C_{\mathrm{add}}\), the project defines the strictly positive core constant
\[
\rho_0 := \kappa_G - C_{\mathrm{add}} > 0.
\]
【218:10†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound(2).md†L1-L24】

---

# 3. From a pointwise bound to a uniform small-field neighborhood

Define the **minimal horizontal eigenvalue** of \(\operatorname{Ric}_{\mu_\Lambda}\) by
\[
\lambda_{\min}^H(U)
:=
\inf_{v\in H_U\setminus\{0\}}
\frac{\operatorname{Ric}_{\mu_\Lambda}(U)(v,v)}{|v|_{g_\Lambda}^2}.
\]
The project notes that \(U\mapsto \lambda_{\min}^H(U)\) is continuous on the regular set, and can be extended appropriately. 【218:12†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound_UPDATED.md†L1-L18】

Since \(\lambda_{\min}^H(U^{(0)})\ge \rho_0\), continuity implies:

> There exist \(r>0\) and \(\rho_{\mathrm{loc}}>0\) (e.g. \(\rho_{\mathrm{loc}}=\rho_0/2\)) such that
> \[
> \lambda_{\min}^H(U)\ge \rho_{\mathrm{loc}}
> \quad\text{whenever } d_{g_\Lambda}(U,U^{(0)})\le r.
> \]
【218:7†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound(2).md†L1-L12】

The crucial extra point is **volume-uniformity**: because the interaction pattern is local and \(M_\Lambda\) is a finite product of the same compact factor, the constants can be chosen independent of \(\Lambda\). 【218:11†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound_UPDATED.md†L8-L22】

---

# 4. Extracted statement (Theorem 6.1)

The project packages the preceding into:

> **Theorem 6.1 (Local horizontal Bakry--Émery curvature bound).**  
> Under the hypotheses \(\operatorname{Ric}_G\ge \kappa_G g_G\) and \(\nabla^2 S_{\mathrm{add},\Lambda}\ge -C_{\mathrm{add}}g_\Lambda\) with \(C_{\mathrm{add}}<\kappa_G\), there exist \(r>0\) and \(\rho_{\mathrm{loc}}>0\), depending only on \((\kappa_G,C_{\mathrm{add}})\) and local lattice structure (not on \(\Lambda\)), such that for all \(U\) with \(d_{g_\Lambda}(U,U^{(0)})\le r\) and all \(v\in H_U\),
> \[
> \operatorname{Ric}_{\mu_\Lambda}(U)(v,v)\ge \rho_{\mathrm{loc}}|v|_{g_\Lambda}^2.
> \]
【218:6†PART_II_SECTION_6_Local_Horizontal_Bakry_Emery_Bound(2).md†L1-L15】

---

# 5. Why this is potentially new/exciting (as a program)

Individually, each ingredient is classical: compact Lie group Ricci bounds, Hessian estimates, continuity. The potentially novel part is the **assembly** targeted at lattice Yang--Mills:

- The curvature bound is **horizontal** (tailored to gauge invariance),
- It is **uniform in finite volume**,
- It is expressed in a language (\(\Gamma\)-calculus) that interfaces cleanly with Poincaré/LSI machinery.

This estimate is the “small-field core” needed for a curvature-driven approach to quantitative mixing and (with additional steps) correlation decay for gauge-invariant observables.
