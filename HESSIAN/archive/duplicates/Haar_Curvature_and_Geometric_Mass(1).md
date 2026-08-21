# Haar curvature and geometric mass

**Scope.** This document extracts (and cleans into a single narrative) the “Haar–Bakry–Émery mass mechanism” arguments: a *purely geometric* curvature floor from the compact gauge group, plus an optional *action-driven* convexity contribution, together yielding a *mass-like scale* via Poincaré/LSI on configuration space.

**Primary sources.**
- `PROOF_04_Geometric_Mass_Derivation.md` (core Bakry–Émery mass derivation).
- `SYNTH_P04_haar_geometry_supplement.md` (geometry of compact groups; horizontal convexity discussion).

---

## Configuration space and measure

Let \(G\) be a compact Lie group (e.g. \(SU(N)\)). For a finite lattice with edge set \(E\), the configuration space is
\[
\mathscr A \;:=\; G^{E}
\]
equipped with the product bi-invariant Riemannian metric \(g\) induced from a bi-invariant metric on \(G\).

For a “Wilson-type” action \(S_\beta:\mathscr A\to\mathbb R\) at inverse coupling \(\beta>0\), define the probability measure
\[
\mu_\beta(dU)\;=\;\frac{1}{Z_\beta}\,e^{-S_\beta(U)}\,d\mathrm{vol}_g(U).
\]

---

## Bakry–Émery curvature tensor

Define the Bakry–Émery tensor of \((\mathscr A,g,\mu_\beta)\) by
\[
\mathrm{Ric}_{\mu_\beta} \;:=\; \mathrm{Ric}_g \;+\;\nabla^2 S_\beta,
\]
where \(\nabla^2 S_\beta\) is the Riemannian Hessian. (This is the \(CD(\rho,\infty)\) object in the Bakry–Émery theory.)  

A central extracted criterion is the curvature lower bound
\[
\mathrm{Ric}_{\mu_\beta}\;\ge\;\rho_0\,g
\qquad(\rho_0>0),
\]
in the sense of quadratic forms.

---

## Purely geometric curvature floor from Haar geometry

### Ricci curvature of compact groups (baseline floor)

For a compact Lie group \(G\) with a bi-invariant metric,
\[
\mathrm{Ric}_G \;=\;\kappa\, g_G,
\qquad \kappa>0,
\]
with \(\kappa=\tfrac14 c_{\mathrm{adj}}\) proportional to the quadratic Casimir in the adjoint representation, and the product space inherits the same lower bound:
\[
\mathrm{Ric}_g \;=\;\kappa\, g\quad\text{on }\mathscr A.
\]

**Interpretation.** Even before adding any action term, the configuration manifold \(\mathscr A=G^E\) has strictly positive Ricci curvature.

---

## Action-driven convexity contribution

The extracted “mass mechanism” uses that, in the regimes where the Wilson action is (horizontally) convex,
\[
\nabla^2 S_\beta\;\ge\;\beta\,c_W\,g
\quad\text{(on horizontal directions, in a small-angle tube).}
\]
Then
\[
\mathrm{Ric}_{\mu_\beta}\;\ge\;(\kappa+\beta c_W)\,g
\quad\text{(on horizontals).}
\]
The key point is the **sign**: \(\kappa>0\) is geometric, and \(\beta c_W\) is a further (optional) positive reinforcement.

---

## The geometric mass theorem

### Theorem (Geometric mass from Bakry–Émery curvature)

Assume a Bakry–Émery curvature bound
\[
\mathrm{Ric}_{\mu_\beta} \;\ge\; \rho_0\,g
\]
(typically with \(\rho_0=\kappa\) from Haar geometry, or \(\rho_0=\kappa+\beta c_W\) on the convex subspace).

Then the diffusion generator associated to \(\mu_\beta\) has a spectral gap \(\ge \rho_0\), and the corresponding two-point correlations decay with correlation length bounded by
\[
\xi \;\lesssim\;\frac{1}{\sqrt{\rho_0}}.
\]

In lattice units, this supplies an effective “mass scale”
\[
m_{\mathrm{eff}}^2 \;\sim\; \rho_0,
\]
and in physical units (spacing \(a\)) the heuristic scaling is
\[
m_{\mathrm{phys}}^2 \;\sim\;\frac{\rho_0}{a^2}.
\]

### Proof sketch (as extracted)

The Bakry–Émery criterion \(CD(\rho_0,\infty)\) implies a Poincaré inequality (and, in standard settings, an LSI) with constant \(\rho_0\), which yields exponential decay for the \(L^2(\mu_\beta)\)-semigroup. Translating semigroup decay to correlation decay gives the stated correlation-length bound.

---

## Why this is “interesting physics”

- The baseline \(\kappa>0\) is **nonperturbative and geometric**, and does not depend on the number of degrees of freedom: it comes from the compactness and positive Ricci curvature of \(G\).
- If one can control the locality/horizontality conditions so that \(\beta c_W\) survives a continuum limit, the mechanism becomes a candidate for a **geometric origin of a mass gap**.

---

## Immediate next steps suggested by the extracted corpus

1. **Make the horizontal convexity regime precise.** Replace “small-angle tube” by an explicit neighborhood and explicit \(c_W\) (or an averaged \(c_W\)).

2. **Compatibility with gauge reduction.** Track precisely what happens under quotienting by gauge (or gauge fixing) so that the curvature lower bound is not an artifact of redundant directions.

3. **Scaling.** Identify which part of \(\rho_0\) is stable under coarse-graining; in particular, whether the \(\kappa\) contribution persists as a lower bound for *physical* observables after reconstruction.
