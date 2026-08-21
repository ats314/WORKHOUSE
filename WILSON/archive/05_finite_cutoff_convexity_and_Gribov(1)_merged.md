Document 5 — Finite-Cutoff Convexity Window, Gribov Region, and Gap

# Document 5: Finite-Cutoff Convexity Window, Gribov Region, and Spectral Gap

We now combine the Haar mass term and the Wilson Hessian bound to define a **convexity window** and relate it to a spectral gap via Bakry–Émery.

## 1. Convexity Window and Gribov Region

From Document 4, the horizontal Hessian satisfies
\[
  \langle A, \mathrm{Hess}_{\text{hor}} S_{\mathrm{eff}}(U) A\rangle
  \;\ge\; \rho_*(a)\,\|A\|^2,\qquad
  \rho_*(a) := c_0 a^2 g^2 - \beta C_V(N).
\]

Insert the lattice relation
\[
  \beta = \frac{2N}{g^2},
\]
and \(C_V(N)=\frac{6}{N}\). Then
\[
  \beta C_V(N)
  = \frac{2N}{g^2}\cdot \frac{6}{N}
  = \frac{12}{g^2}.
\]
Hence
\[
  \rho_*(a) = c_0 a^2 g^2 - \frac{12}{g^2}.
\]

**Definition 1.1 (Strong-Coupling Convexity Window).**  
For a fixed lattice spacing \(a>0\), the pair \((a,g)\) is said to be in the **convexity window** if
\[
  \rho_*(a) = c_0 a^2 g^2 - \frac{12}{g^2} > 0.
\]

Equivalently,
\[
  c_0 a^2 g^2 > \frac{12}{g^2}
  \quad\Longleftrightarrow\quad
  g^4 > \frac{12}{c_0 a^2}.
\]

So there is a strictly positive critical coupling
\[
  g_{\mathrm{crit}}(a) = \left(\frac{12}{c_0 a^2}\right)^{1/4},
\]
such that for \(g > g_{\mathrm{crit}}(a)\), the horizontal directions are uniformly convex.

**Definition 1.2 (Gribov Region and Horizon).**  
The **Gribov region** \(\Omega\subset\mathcal{C}\) is the set of configurations for which the horizontal Hessian (equivalently the Faddeev–Popov operator in a chosen gauge) is strictly positive definite. The point where the minimal horizontal eigenvalue hits zero is the **Gribov horizon**.

The inequality
\[
  c_0 a^2 g^2 > \beta C_V(N)
\]
is precisely the condition \(\rho_*(a)>0\) and identifies a parameter regime in which all configurations lie strictly inside the Gribov region.

**Physical interpretation.**

- \(c_0 a^2 g^2\) is a **quantum stiffness** term: it arises from the curvature of the compact group manifold via the Haar measure.
- \(\beta C_V(N)\) is an **entropic/potential pressure** term: it originates from the Wilson action’s tendency to flatten the energy landscape as the coupling weakens.

At the boundary \(c_0 a^2 g^2 = \beta C_V(N)\), the smallest horizontal eigenvalue of \(\mathrm{Hess} S_{\mathrm{eff}}\) touches zero: this is the Gribov horizon.

## 2. Bakry–Émery Curvature on Configuration Space

Let \(\mathcal{C}=G^{|B|}\) with product bi-invariant metric. The Ricci curvature of each factor \(G=SU(N)\) is positive; denote its lower bound by \(\rho_0>0\) at the identity and extended uniformly across the compact group. The product manifold retains a positive lower Ricci bound independent of the volume.

The Gibbs measure is
\[
  d\mu(U) = Z^{-1} e^{-S_{\mathrm{eff}}(U)} d\mathrm{vol}(U),
\]
and the associated Langevin generator is
\[
  L f = \Delta f - \langle \nabla S_{\mathrm{eff}},\nabla f\rangle
\]
on \((\mathcal{C},g)\). The carré du champ and its iterated version are
\[
  \Gamma(f) = \|\nabla f\|^2,\qquad
  \Gamma_2(f) = \frac{1}{2}\big(L\Gamma(f) - 2\Gamma(f,L f)\big).
\]

On a Riemannian manifold with potential \(S_{\mathrm{eff}}\),
\[
  \Gamma_2(f)
  = \|\nabla^2 f\|_{\mathrm{HS}}^2
    + \big\langle (\mathrm{Ric} + \nabla^2 S_{\mathrm{eff}})\nabla f,\nabla f\big\rangle.
\]

On vertical directions (along gauge orbits), the Ricci term alone gives a positive lower bound. On horizontal directions, we add the Hessian bound
\[
  \nabla^2_{\text{hor}} S_{\mathrm{eff}}(U) \succeq \rho_*(a)\,I.
\]
Thus the combination \(\mathrm{Ric} + \nabla^2 S_{\mathrm{eff}}\) is bounded below by
\[
  \rho_{\mathrm{BE}} := \min\{\rho_0,\rho_*(a)\} >0.
\]

**Proposition 2.1 (Bakry–Émery \(\mathrm{CD}(\rho_{\mathrm{BE}},\infty)\) for Lattice YM).**  
If \(c_0 a^2 g^2 > \beta C_V(N)\), then the Langevin generator \(L\) on \(\mathcal{C}\) satisfies
\[
  \Gamma_2(f) \;\ge\; \rho_{\mathrm{BE}}\,\Gamma(f),\qquad
  \rho_{\mathrm{BE}} = \min(\rho_0,\rho_*(a)) >0.
\]

## 3. Poincaré Inequality and Spectral Gap

By general Bakry–Émery theory, \(\mathrm{CD}(\rho_{\mathrm{BE}},\infty)\) implies:

- Poincaré inequality:
  \[
    \mathrm{Var}_\mu(f)
    \le \frac{1}{\rho_{\mathrm{BE}}}\int \|\nabla f\|^2 d\mu.
  \]
- Log-Sobolev inequality (hence hypercontractivity):
  \[
    \mathrm{Ent}_\mu(f^2)
    \le \frac{2}{\rho_{\mathrm{BE}}}\int \|\nabla f\|^2 d\mu.
  \]

Let \(H = -L\) as a self-adjoint operator on \(L^2(\mu)\). The Rayleigh–Ritz variational principle yields
\[
  \lambda_1(H)
  = \inf_{f\perp 1}
    \frac{\int \|\nabla f\|^2 d\mu}{\mathrm{Var}_\mu(f)}
  \;\ge\; \rho_{\mathrm{BE}} > 0.
\]

**Theorem 3.1 (Finite-Cutoff Lattice Mass Gap from Convexity).**  
Fix lattice spacing \(a>0\) and coupling \(g\) such that
\[
  c_0 a^2 g^2 > \beta C_V(N)
  \quad\Longleftrightarrow\quad
  g^4 > \frac{12}{c_0 a^2}.
\]
Then:

1. The effective action \(S_{\mathrm{eff}}\) is uniformly convex along horizontal directions with curvature \(\rho_*(a)>0\).
2. The curvature–dimension condition \(\mathrm{CD}(\rho_{\mathrm{BE}},\infty)\) holds for the Langevin generator.
3. The negative generator \(H=-L\) has a strictly positive spectral gap
   \[
     \Delta_H := \lambda_1(H) \ge \rho_{\mathrm{BE}} > 0,
   \]
   **uniform in the lattice volume**.

In other words, for each fixed finite cutoff \(a>0\) and sufficiently large bare coupling \(g\), the lattice Yang–Mills theory has a nonzero mass gap in this geometric/Langevin sense.


⸻
