# Exciting Extract 01 — Mass From Haar Geometry (Bakry–Émery Curvature Anchor)

## 1. Why this is exciting

A recurring obstruction in gauge theories is the presence of **flat directions** (gauge orbits) and **near-flat directions** (harmonic modes, large-field regions). This extract isolates a mechanism that is both geometrically clean and potentially reusable:

> **The reference geometry itself**—specifically the **positive Ricci curvature** of a compact Lie group with a bi-invariant metric—acts as a *curvature anchor* in the Bakry–Émery tensor.  
> When combined with the **nonnegativity** of the Wilson Hessian on physical directions, this yields a robust **local convexity / curvature lower bound** for the gauge-invariant sector.

This is conceptually “mass from geometry”: even before you discuss renormalization, anomalies, or delicate cancellations, the compact group geometry already contributes a definite positive term to \(\mathrm{Ric}_\mu\).

---

## 2. Setup: configuration manifold and Gibbs diffusion

Let \(G\) be a compact, connected Lie group, equipped with a bi-invariant Riemannian metric \(g_G\).  
For a finite lattice \(\Lambda\) with oriented edges \(E(\Lambda)\), define the configuration manifold
\[
M_\Lambda := G^{E(\Lambda)}
\]
with product metric \(g_\Lambda\) and Riemannian volume \(d\mathrm{vol}_{g_\Lambda}\) (equal to product Haar volume for a bi-invariant metric).

Let \(S_\Lambda\in C^2(M_\Lambda)\) be a gauge-invariant action and define the Gibbs measure
\[
d\mu_\Lambda(U)=Z_\Lambda^{-1}e^{-S_\Lambda(U)}\,d\mathrm{vol}_{g_\Lambda}(U).
\]

The symmetric diffusion generator on \(L^2(\mu_\Lambda)\) is
\[
L_\Lambda f = \Delta_{g_\Lambda}f - \langle \nabla S_\Lambda,\nabla f\rangle_{g_\Lambda},
\]
with carré du champ \(\Gamma(f)=|\nabla f|^2\). The Bakry–Émery tensor is
\[
\mathrm{Ric}_{\mu_\Lambda} := \mathrm{Ric}_{g_\Lambda}+\nabla^2 S_\Lambda.
\]

---

## 3. The Haar curvature anchor

### 3.1. Product Ricci on \(G^{E(\Lambda)}\)

Because \(g_G\) is bi-invariant on a compact group, \((G,g_G)\) is Einstein with strictly positive Ricci curvature:
\[
\mathrm{Ric}_G = \kappa_G\, g_G,\qquad \kappa_G>0.
\tag{3.1}
\]
Therefore the product manifold satisfies
\[
\mathrm{Ric}_{g_\Lambda} = \kappa_G\, g_\Lambda
\quad\text{(as tensors on }TM_\Lambda\text{),}
\tag{3.2}
\]
with \(\kappa_G\) independent of \(\Lambda\).

**Interpretation.** In Bakry–Émery language, the “baseline” curvature term \(\mathrm{Ric}_{g_\Lambda}\) is a strictly positive multiple of the metric, uniformly in the volume.

### 3.2. Exponential-coordinate viewpoint (optional but illuminating)

If one instead writes Haar volume in exponential coordinates near the identity,
\[
U=\exp(X),\qquad X\in\mathfrak g,
\]
then
\[
d\mathrm{Haar}(U)=J(X)\,dX,
\]
and the Jacobian potential \(S_H(X):=-\log J(X)\) satisfies the small-\(X\) expansion
\[
\nabla^2 S_H(0)=\frac{1}{3}\mathrm{Ric}_G.
\tag{3.3}
\]
So the same positivity appears either as:

- a geometric Ricci term \(\mathrm{Ric}_{g_\Lambda}\), or
- a convex “Haar mass potential” in flat coordinates.

---

## 4. Wilson Hessian positivity on physical directions

Let \(S_W\) denote the Wilson action (sum of plaquette terms) and write the full effective action as
\[
S_\Lambda = S_W + S_{\mathrm{add},\Lambda},
\]
where \(S_{\mathrm{add},\Lambda}\) is gauge-invariant and has a uniform lower Hessian bound
\[
\nabla^2 S_{\mathrm{add},\Lambda}(U)\ \ge\ -C_{\mathrm{add}}\,g_\Lambda(U)
\quad\forall U\in M_\Lambda,
\tag{4.1}
\]
with \(C_{\mathrm{add}}\ge 0\) independent of \(\Lambda\).

Near the trivial configuration \(U^{(0)}\) (all links \(=e\in G\)), Wilson’s Hessian satisfies (in right-invariant coordinates)
\[
\nabla^2 S_W(U^{(0)}) \simeq c\,\beta\, d_1^*d_1,
\tag{4.2}
\]
where \(d_1\) is the discrete coboundary from edges to plaquettes. In particular:

- \(\nabla^2 S_W(U^{(0)})\ge 0\) as a quadratic form,
- it is strictly positive on co-exact (“physical”) modes, and
- it vanishes on pure gauge directions (and possibly harmonic modes).

---

## 5. The core “mass from geometry” lemma

Let \(H_U\subset T_U M_\Lambda\) denote the horizontal (gauge-invariant / physical) subspace (orthogonal complement of gauge directions), so that for gauge-invariant \(f\),
\[
\nabla f(U)\in H_U.
\]

### Lemma 5.1 (Haar curvature anchor dominates bounded negative Hessians)

Assume \(\kappa_G>C_{\mathrm{add}}\) and set \(\rho_0:=\kappa_G-C_{\mathrm{add}}>0\). Then at the trivial configuration,
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)\ \ge\ \rho_0\,|v|^2
\qquad\forall v\in H_{U^{(0)}}.
\tag{5.1}
\]

**Proof.**
By definition,
\[
\mathrm{Ric}_{\mu_\Lambda}
=\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_W+\nabla^2 S_{\mathrm{add},\Lambda}.
\]
Evaluate on \(v\in H_{U^{(0)}}\):
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)
=\kappa_G|v|^2 + \nabla^2 S_W(U^{(0)})(v,v)+\nabla^2 S_{\mathrm{add},\Lambda}(U^{(0)})(v,v).
\]
Use \(\nabla^2 S_W(U^{(0)})(v,v)\ge 0\) and \(\nabla^2 S_{\mathrm{add},\Lambda}(U^{(0)})(v,v)\ge -C_{\mathrm{add}}|v|^2\) to get
\[
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)\ge (\kappa_G-C_{\mathrm{add}})|v|^2=\rho_0|v|^2.
\]
∎

### Lemma 5.2 (Uniform local extension by continuity)

There exist \(r>0\) and \(\rho_{\mathrm{loc}}>0\), independent of \(\Lambda\), such that for all \(U\) with \(d_{g_\Lambda}(U,U^{(0)})\le r\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ \ge\ \rho_{\mathrm{loc}}|v|^2
\qquad\forall v\in H_U.
\tag{5.2}
\]

**Proof idea.**
Both \(U\mapsto \mathrm{Ric}_{\mu_\Lambda}(U)\) and \(U\mapsto H_U\) vary continuously on the regular set. The function
\[
U\mapsto \inf\{\mathrm{Ric}_{\mu_\Lambda}(U)(v,v): v\in H_U,\ |v|=1\}
\]
is continuous and is \(\ge\rho_0\) at \(U^{(0)}\), hence stays \(\ge \rho_0/2\) in a small ball. ∎

---

## 6. What theory this points toward

This “Haar curvature anchor” suggests a reusable template:

1. **Compact group configuration manifold:** \(G^{E}\) with product bi-invariant metric.
2. **Gauge invariance:** physical observables live in horizontal directions.
3. **Action decomposition:** a nonnegative “physical Hessian” term + bounded-below remainder.
4. **Result:** uniform **local Bakry–Émery curvature** on a small-field region, giving local FI’s (Poincaré/LSI).

This could be abstracted into a general theorem for:

- lattice gauge theories with compact structure group,
- principal bundle discretizations on general graphs,
- sigma models valued in compact homogeneous spaces,
- or any Gibbs diffusion on \(G^n\) with a symmetry quotient.

A particularly interesting “bigger theory” direction is:

> **Bakry–Émery geometry on orbit spaces (quotients).**  
> Formalize curvature lower bounds for **invariant observables** under compact group actions, using horizontal distributions and curvature formulas for Riemannian submersions.

---

## 7. Next work needed (to turn this into a publishable contribution)

1. **Quantify \(\kappa_G\)** under a chosen normalization and spell out explicit constants.  
2. **Control the horizontal bundle** globally or specify a regularity regime (avoid reducibles / fix a slice).  
3. **Make the Wilson Hessian lower bound quantitative** on a chosen physical subspace (e.g., co-exact modes) with a clean lattice-dependent constant.  
4. **Extend beyond the small-field ball**: this is exactly where Lyapunov drift + local-to-global FI machinery enters (Parts 12–14).

This extract is the cleanest “geometric seed crystal” in the project: it is local, robust, and conceptually sharp.
