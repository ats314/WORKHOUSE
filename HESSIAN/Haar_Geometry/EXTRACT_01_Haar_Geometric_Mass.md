---
title: "EXTRACT 01 — Haar Geometric Mass: Bakry–Émery Positivity on Horizontal Directions"
date: "2025-12-31"
---

# Executive summary

The archive contains a particularly promising mechanism:  
a **strict lower bound** on the Bakry–Émery curvature
\[
  \mathrm{Ric}_{\mu_\beta}=\mathrm{Ric}_g+\beta\nabla^2 S_W
\]
on the **horizontal** subbundle (after gauge reduction), for small plaquettes / near the identity.

This bound is structurally stronger than the “nonnegative anomaly source” condition that earlier parts of the program were waiting for:
it provides an **explicit positive constant** that behaves like an emergent *mass parameter*.

This extract condenses the main theorem and its proof architecture from:

- `UNIF_CONJB_STRATEGY.md`
- `SYNTH_P04_haar_geometry_supplement.md`
- `PROOF_04_Geometric_Mass_Derivation.md`

# 1. Setup: lattice configuration geometry

Let $G=\mathrm{SU}(N)$ and let $\mathcal A_\Lambda = G^{E(\Lambda)}$ be the space of link variables on a finite lattice $\Lambda$.
Equip each $G$ factor with its bi‑invariant metric (Killing / trace metric) and $\mathcal A_\Lambda$ with the product metric $g$.

Let $S_W:\mathcal A_\Lambda\to\mathbb R$ be the Wilson plaquette action.
Define the Gibbs measure
\[
  d\mu_\beta(U)=Z_\beta^{-1}\,e^{-\beta S_W(U)}\,d\mu_{\mathrm{Haar}}(U).
\]

Gauge reduction: the gauge group $\mathcal G_\Lambda=G^{V(\Lambda)}$ acts on $\mathcal A_\Lambda$.
The tangent bundle splits into vertical + horizontal directions (with respect to a chosen connection),
and the project focuses on horizontal directions because physical fluctuations live there.

# 2. Bakry–Émery tensor and its physical interpretation

For $(\mathcal A_\Lambda,g,\mu_\beta)$, the Bakry–Émery tensor is
\[
  \mathrm{Ric}_{\mu_\beta}=\mathrm{Ric}_g+\nabla^2(\beta S_W)
  =\mathrm{Ric}_g+\beta\nabla^2 S_W.
\]

A uniform lower bound
\[
  \mathrm{Ric}_{\mu_\beta}\ \ge\ K\, g
\]
implies (via Bakry–Émery $\Gamma_2$ calculus) a Poincaré inequality and, under slightly stronger conditions,
a log‑Sobolev inequality. In the SWIM2 chain, those analytic inequalities are the bridge from geometry to **spectral gap**.

The key novel move here is: **$K$ is not put in by hand**, but arises from
Haar curvature + strict positivity of $\nabla^2 S_W$ on horizontals.

# 3. Main theorem (horizontal Bakry–Émery bound)

A central statement appearing in the unification layer is:

> **Theorem (horizontal Bakry–Émery positivity).**  
> On the horizontal bundle $H$, one has a lower bound of the form  
> \[
> \mathrm{Ric}_{\mu_\beta}\big|_H \ \ge\ (\kappa+\beta\,c_W)\,g\big|_H,
> \qquad c_W>0,
> \]
> at least in a small‑plaquette / near‑identity regime.

Here $\kappa>0$ is the constant Ricci curvature coefficient of the product Haar metric,
and $c_W$ is a positive constant coming from the Wilson Hessian restricted to horizontals.

## 3.1 Why this is structurally interesting

- $\kappa g$ is “built into” the compact group geometry.  
- $\beta\nabla^2 S_W$ is **dynamic** (depends on the action).  
- On horizontals, $\nabla^2 S_W$ is positive definite (in a neighborhood), so the total curvature is *strictly* positive.

In short: the measure $e^{-\beta S_W}\,d\mu_{\mathrm{Haar}}$ behaves like an **Ornstein–Uhlenbeck measure**
on a curved manifold, with an effective drift strength $\kappa+\beta c_W$.

# 4. Proof architecture: why $c_W>0$?

The supplement identifies an operator factorization for the Wilson Hessian:
\[
  \nabla^2 S_W(U)=C(U)^\* C(U) + E(U),
\]
where

- $C(U)$ is the linearization of the plaquette curvature map (discrete “curl”),
- $E(U)$ is an error term controlled by how close plaquettes are to the identity.

Restricting to horizontals (roughly “coexact 1‑forms”), $C(U)^\*C(U)$ has a **uniform spectral gap**
by discrete Hodge theory, hence
\[
  \nabla^2 S_W(U)\big|_{H_U}\ \ge\ c_W^0\,\mathrm{Id}
\]
for $U$ in a sufficiently small neighborhood, and the error term $E(U)$ can be dominated for small plaquettes.

This is the sense in which $c_W$ becomes positive.

# 5. The “geometric mass” constant

A recurring constant in the archive is
\[
  c_0=\frac{N^2-1}{2N},
\]
the fundamental Casimir‑like coefficient that appears in Haar Jacobians and small‑angle expansions.
The program’s interpretation is that $c_0$ (and its dressed versions $\kappa+\beta c_W$) functions as
a **geometrically generated mass scale**.

This interpretation is speculative, but it is an unusually clean place where group geometry injects a scale.

# 6. What needs to be done next

1. **Globalization**  
   The bound is clearest near the identity / small plaquettes.
   The mass gap problem ultimately needs global control on the support of $\mu_\beta$ for large $\beta$.

2. **Uniformity in lattice size / spacing**  
   Show the lower bound (or at least the induced functional inequality constants) are **uniform**
   in volume and in the approach to the continuum.

3. **Dictionary check: “anomaly source” vs “Hessian source”**  
   Earlier parts of the program refer to an “anomaly source” term $\Sigma_A$ in a PBH/Riccati evolution.
   The present theorem directly provides positivity of a *Hessian* contribution.
   One must verify that these are the same object (or that the difference is controllable).

4. **Continuum transport**  
   This is where Conjecture D (lifting LSI / spectral gap to continuum and then to mass gap) enters.

