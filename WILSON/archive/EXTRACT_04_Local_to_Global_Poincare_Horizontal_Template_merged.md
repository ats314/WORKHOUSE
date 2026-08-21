---
title: "Local-to-Global Poincaré via Lyapunov Drift: a Horizontal/Gauge-Invariant Template"
author: "Project extraction"
date: "2025-12-29"
---

# Overview

This note extracts the **analytic propagation mechanism** the project proposes to go from:

- a **local** curvature bound in a “good” region \(\Omega\) (small-field),  
to
- a **global** spectral gap / Poincaré inequality for the full Gibbs measure.

The project’s Part III, Section 2 gives a general theorem in a finite-dimensional diffusion setting, and (crucially) remarks that the argument is robust under restricting to a **subclass of observables with gradients lying in a subbundle**—exactly what gauge invariance gives you. 【228:3†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature.md†L4-L14】【228:4†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature(1).md†L1-L6】

---

# 1. The abstract setting

Let \((M,g)\) be a finite-dimensional Riemannian manifold and
\[
d\mu = Z^{-1} e^{-S}\,d\mathrm{vol}_g.
\]
Let \(L = \Delta_g - \langle \nabla S,\nabla\cdot\rangle\) be the associated diffusion generator and \(\Gamma(f)=|\nabla f|^2\) the carré du champ.

Part III assumes:

1. **Local \(CD(\rho_{\mathrm{loc}},\infty)\) on a region \(\Omega\):**
\[
\Gamma_2(f)\ge \rho_{\mathrm{loc}}\,\Gamma(f)\qquad\text{on }\Omega.
\]
【228:2†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature(1).md†L42-L56】

2. **Lyapunov drift:** there exists \(W\ge 1\) and constants \(\alpha>0,\beta\ge 0\) and a compact \(K\subset\Omega\) such that
\[
LW \le -\alpha W + \beta\,\mathbf 1_K \quad\text{on }M.
\]
【228:8†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature(1).md†L1-L9】

3. **Local Poincaré on a bounded set \(U\subset\Omega\) containing \(K\):**
\[
\int_U (f-f_U)^2\,d\mu \le C_{\mathrm{loc}}\int_U \Gamma(f)\,d\mu.
\]
【228:8†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature(1).md†L10-L22】

---

# 2. The extracted mechanism

The project proves a “Lyapunov–\(\Gamma\)” estimate that controls the weighted \(L^2\) norm \(\int f^2 W\,d\mu\) by the Dirichlet form plus a local term on \(K\). 【228:0†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature.md†L22-L38】

Then it performs a decomposition:

- use the local Poincaré inequality on \(U\) to control \(\int_U f^2\),
- use Lyapunov to control \(\int_{U^c} f^2\) through tails of \(W\),
- combine the two into the **global** Poincaré inequality
\[
\mathrm{Var}_\mu(f)\le C_P \int_M \Gamma(f)\,d\mu.
\]
The writeup includes explicit bookkeeping showing how a finite \(C_P\) arises. 【228:15†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature.md†L15-L31】

---

# 3. The “horizontal restriction” remark (the gauge-theory lever)

The key extracted remark:

> The proof is robust when restricting to a subclass of observables whose gradients lie in a subbundle \(\mathcal H\subset TM\): replace \(\Gamma\) by \(\Gamma^{\mathcal H}(f)=|\nabla^{\mathcal H} f|^2\), and require curvature and Lyapunov only along \(\mathcal H\). 【228:4†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature(1).md†L1-L6】

In lattice Yang--Mills:

- the subbundle is the **horizontal bundle** \(H\),
- the subclass is **gauge-invariant observables** \(f\) (so \(\nabla f\in H\)),
- Part II supplies the local horizontal curvature bound on \(\Omega=B_r(U^{(0)})\). 【228:6†PART_II_SECTION_7_Core_Curvature_Theorem_and_Interface_to_Part_I.md†L7-L24】

This is the project's cleanest bridge from geometric curvature to global inequalities in the gauge-invariant sector.

---

# 4. What this reduces the Yang--Mills problem to

Part III summarizes the Yang--Mills application as a checklist:

1. **Local horizontal curvature on \(\Omega\)** (done in Part II).  
2. Construct a **Lyapunov function \(W_\Lambda\)** measuring deviation of plaquettes from identity, satisfying a drift inequality with constants independent of \(\Lambda\).  
3. Verify a **local Poincaré inequality** on a bounded subset \(U\subset\Omega\).  
4. Apply the theorem in the **gauge-invariant/horizontal** framework. 【228:4†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature(1).md†L22-L28】

The genuinely hard physics/analysis sits in step (2): designing a \(W_\Lambda\) that both sees “large-field” excursions and has a computable \(LW_\Lambda\) with \(\Lambda\)-uniform constants.

---

# 5. A concrete Lyapunov candidate (working sketch)

A natural (project-consistent) choice is a function that penalizes plaquette angles, e.g.
\[
W_\Lambda(U)=\exp\!\Big(c\sum_{p\in P(\Lambda)} \phi\big(r(U_p)\big)\Big)
\]
where \(U_p\) is the plaquette holonomy, \(r(U_p)=\arccos(\tfrac12\mathrm{ReTr}(U_p))\) is a class-function “angle”, and \(\phi\) is convex and grows for large angles.

This is not proven in the project; it is an actionable hypothesis suggested explicitly in the “template summary” paragraphs. 【228:5†PART_III_SECTION_2_Local_to_Global_Poincare_via_Lyapunov_and_Curvature.md†L22-L28】

If one can compute \(LW_\Lambda\) (for the lattice Yang--Mills Langevin generator) and show it is negative outside a small-field set, the global spectral gap follows.
