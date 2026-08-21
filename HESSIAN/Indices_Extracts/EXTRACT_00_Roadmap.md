---
title: "PROVEN vs PARTS — Extracted Core Mechanisms (Roadmap)"
date: "2025-12-29"
format: "markdown+latex"
---

# Roadmap: a curvature-and-flow route to a Yang–Mills mass gap

This note is an edited extraction of the core mechanisms appearing throughout the project files.  
It is intended to make the logical architecture explicit, and to isolate the pieces that look most reusable (even beyond Yang–Mills).

## 0.1 The master picture

The project repeatedly exploits a small set of interlocking ideas:

1. **Geometry of configuration space (Haar / Ricci).**  
   On the lattice configuration manifold
   \[
     M_\Lambda \;=\; G^{E(\Lambda)}
   \]
   with product bi-invariant metric, the **Riemannian Ricci tensor is uniformly positive** when \(G\) is compact and simple with the usual normalization.  
   In exponential coordinates, the same positivity appears as a **local strictly convex “Haar potential”** (a quadratic contribution to \(-\log\) of the Haar Jacobian), i.e. a built-in “mass-like” term.

2. **Gauge symmetry and horizontality.**  
   Gauge-invariant observables have gradients that lie in the horizontal (physical) subbundle \(H_U\subset T_U M_\Lambda\).  
   This means curvature bounds only need to hold **on horizontals** to control the physical sector.

3. **Bakry–Émery curvature \(\Rightarrow\) local functional inequalities.**  
   For a Gibbs measure \(d\mu\propto e^{-S}d\mathrm{vol}\), the Bakry–Émery tensor
   \[
     \mathrm{Ric}_\mu \;=\; \mathrm{Ric}_g + \nabla^2 S
   \]
   controls \(\Gamma_2\) via the Bochner identity and implies a curvature–dimension condition \(CD(\rho,\infty)\).  
   On bounded regions, \(CD(\rho,\infty)\) yields local Poincaré and local log-Sobolev inequalities.

4. **Lyapunov drift \(\Rightarrow\) local-to-global upgrade.**  
   A Lyapunov condition of the form
   \[
     LW \le -\alpha W + \beta \mathbf 1_K
   \]
   controls the tails and upgrades local inequalities (in a “small-field” core) to global inequalities with explicit constants.

5. **Uniform LSI \(\Rightarrow\) tightness \(\Rightarrow\) continuum subsequences.**  
   A uniform log-Sobolev inequality yields Herbst concentration and exponential moment bounds, which imply tightness of the measures in suitable Sobolev topologies.  
   Tightness gives subsequential continuum limits by Prokhorov’s theorem.

6. **Parabolic comparison + polarity \(\Rightarrow\) propagation of positivity across singular strata.**  
   The orbit space (or the horizontal bundle) is generally **stratified**, with singular sets (reducibles) where a naive maximum principle might fail.  
   The project proposes to neutralize this by proving the singular set has **capacity zero** (“polarity”), so diffusion paths almost surely avoid it.  
   This allows a **stratified parabolic maximum principle** and hence a comparison argument for curvature-eigenvalue evolution.

7. **Riccati mechanism \(\Rightarrow\) quantitative mass gap from a positive source.**  
   Once a curvature-eigenvalue \(\lambda(t,x)\) satisfies a semilinear inequality of the schematic form
   \[
     \partial_t \lambda \;\ge\; \Delta \lambda - 2\lambda^2 + \sigma_*
   \]
   with \(\sigma_*>0\) (the “anomaly source”), comparison gives an ODE lower bound
   \[
     \dot \ell = -2\ell^2 + \sigma_*,
   \]
   whose stable fixed point \(\ell_*=\sqrt{\sigma_*/2}\) is the candidate **mass gap scale**.

## 0.2 Why these pieces are exciting (and potentially exportable)

- The **Haar/Ricci \(\leftrightarrow\) mass term** correspondence is an explicit bridge between group geometry and convexity of the effective measure.
- The **horizontal Bakry–Émery** viewpoint cleanly isolates the physically relevant sector without requiring a global curvature bound on all directions.
- The **polarity + stratified parabolic comparison** mechanism is a general tool for “PDE/semigroup methods on stratified quotients,” and seems reusable well outside lattice YM (e.g., moduli spaces, gauge orbit spaces, singular stochastic dynamics).
- The **Riccati mass-gap mechanism** is a sharp mathematical template: if one can identify a uniform positive source \(\sigma_*\) and verify the differential inequality for \(\lambda\), the rest is essentially forced.

## 0.3 What remains nontrivial

The roadmap identifies precisely where the hard physics/analysis enters:

- Proving a **global** or “high-probability” curvature bound (beyond a small-field neighborhood) with constants uniform in volume and lattice spacing.
- Constructing Lyapunov functions with **uniform** drift constants \((\alpha,\beta)\) for the lattice family.
- In the stratified argument, proving **polarity/capacity-zero** statements with the *correct* codimension thresholds for the relevant Dirichlet form.
- Establishing the **evolution inequality** for the minimal horizontal eigenvalue \(\lambda\) under the intended RG / PBH flow in a fully controlled way.

The following extracted notes expand the project’s main lemmas and “mechanism proofs” into standalone, publication-style chunks.
