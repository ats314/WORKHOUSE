\
---
title: "Haar curvature ⇒ Wilson mass (local Bakry–Émery positivity on horizontals)"
date: 2025-12-29
format: markdown+latex
---

## Abstract

On a finite lattice, consider the Wilson gauge action for $G=\mathrm{SU}(N)$ and endow configuration space $\mathscr{A}=G^E$ with the **product bi-invariant (Haar) metric**. For the Gibbs measure
\[
d\mu_\beta(U)=Z^{-1} e^{-S_\beta(U)}\,d\mathrm{vol}_g(U),
\qquad
S_\beta(U)=\beta\sum_{p\in P}\Bigl(N-\Re\Tr(U_p)\Bigr),
\]
we show (in a small-angle sector near the identity configuration) that the Bakry–Émery tensor
\[
\mathrm{Ric}_{\mu_\beta}=\mathrm{Ric}_g+\nabla^2 S_\beta
\]
is **strictly positive on horizontal (physical) directions**, with a lower bound of the form $(\kappa+\beta c_W)g$.

Interpreting $(\kappa+\beta c_W)$ as a **curvature-generated mass scale** gives a clean geometric mechanism for a local spectral gap and suggests a route toward RG-stable mass generation.

---

## 1. Setting

### 1.1 Lattice configuration space

Let $\Lambda$ be a finite hypercubic lattice and $E$ its oriented edge set. A lattice gauge field is
\[
U=(U_e)_{e\in E}\in \mathscr{A}:=G^E,\qquad G=\mathrm{SU}(N).
\]
Let $P$ be the set of oriented plaquettes, and for each $p\in P$ let
\[
U_p:=\prod_{e\in\partial p}^{\to} U_e
\]
be the oriented plaquette holonomy.

### 1.2 Geometry: pulled-back Haar metric

Equip $G$ with its bi-invariant metric induced by $\langle X,Y\rangle:=-\Tr(XY)$ on $\mathfrak{g}=\mathfrak{su}(N)$, and equip $\mathscr{A}=G^E$ with the product metric
\[
g:=\bigoplus_{e\in E} g_G.
\]
Write $\mathrm{vol}_g$ for the corresponding Riemannian volume.

### 1.3 Measure and Bakry–Émery tensor

Define the Gibbs measure
\[
d\mu_\beta(U)=Z^{-1} e^{-S_\beta(U)}\,d\mathrm{vol}_g(U).
\]
The Bakry–Émery tensor for $(\mathscr{A},g,\mu_\beta)$ is
\[
\mathrm{Ric}_{\mu_\beta}:=\mathrm{Ric}_g+\nabla^2 S_\beta.
\]

### 1.4 Horizontal directions

Gauge transformations act on $\mathscr{A}$ by vertex-wise conjugation. Let $V_U\subset T_U\mathscr{A}$ be the vertical subspace tangent to the gauge orbit at $U$. Define the **horizontal** subspace as its $g$-orthogonal complement
\[
H_U := V_U^{\perp_g}\subset T_U\mathscr{A}.
\]
All strict convexity estimates below are asserted on $H_U$.

---

## 2. Main theorem

### Theorem 2.1 (Local curvature positivity on horizontals)

Fix $\theta_0>0$. Define the small-angle sector
\[
\Omega_{\theta_0}:=\Bigl\{U\in\mathscr{A}: \|\log(U_p)\|\le \theta_0\ \text{for all plaquettes }p\Bigr\}
\]
(using the principal branch of the logarithm, defined for sufficiently small angles).

Then there exist constants $\kappa>0$ and $c_W=c_W(\Lambda,\theta_0)>0$ such that for all $U\in\Omega_{\theta_0}$ and all $X\in H_U$,
\[
\mathrm{Ric}_{\mu_\beta}(X,X)\;\ge\;(\kappa+\beta c_W)\,g(X,X).
\]

---

## 3. Proof ingredients

### Lemma 3.1 (Haar product Ricci curvature)

For $G=\mathrm{SU}(N)$ with bi-invariant metric $g_G$, there exists $\kappa>0$ such that
\[
\mathrm{Ric}_G = \kappa\, g_G.
\]
Consequently, on $\mathscr{A}=G^E$ with product metric $g$,
\[
\mathrm{Ric}_g=\kappa\, g.
\]

*Sketch.* Compact Lie groups with bi-invariant metrics are Einstein. The Ricci tensor on a product acts componentwise.

---

### Lemma 3.2 (Quadratic expansion of the Wilson plaquette)

If $U_p=\exp(\theta_p)$ with $\|\theta_p\|$ small, then
\[
\Re\Tr(\exp(\theta_p))
= N - \frac12\|\theta_p\|_{\mathrm{HS}}^2 + O(\|\theta_p\|^3),
\]
hence
\[
S_\beta(U)
= \frac{\beta}{2}\sum_{p\in P}\|\theta_p\|_{\mathrm{HS}}^2 + O(\theta^3).
\]

*Sketch.* Expand $\exp(\theta_p)$ and use that $\theta_p\in\mathfrak{su}(N)$ is traceless and skew-Hermitian.

---

### Lemma 3.3 (Wilson Hessian is $\ge 0$ and strictly $>0$ on horizontals)

Let $X=(X_e)_{e\in E}\in T_U\mathscr{A}$ be a right-invariant variation, i.e. $U_e(t)=U_e\exp(tX_e)$. In the small-angle sector,
\[
\delta^2 S_\beta[X] = \beta\sum_{p\in P}\|\theta_p'(X)\|^2 + O(\|X\|^3),
\]
where $\theta_p'(X)$ is the linearized plaquette angle. In particular,
\[
\nabla^2 S_\beta\;\ge\;0\quad\text{on }T_U\mathscr{A}.
\]

Moreover, the kernel of the quadratic form contains the vertical (pure gauge) directions. Restricting to horizontals, there exists $c_W>0$ such that
\[
\nabla^2 S_\beta(X,X) \ge \beta c_W\, g(X,X),
\qquad X\in H_U,
\]
uniformly over $U\in\Omega_{\theta_0}$.

*Sketch.* The plaquette angle linearization is a gauge-covariant discrete curl:
\[
\theta_p'(X) = \sum_{e\in\partial p} \sigma_{p,e}\,\mathrm{Ad}_{\text{transport}}(X_e),
\]
hence $\delta^2 S_\beta[X]$ is a sum of squared norms and is nonnegative. Gauge (gradient) variations cancel around plaquettes, producing the vertical kernel. On the horizontal complement the associated operator is (up to the adjoint transports) of the form $C^\ast C$ with strictly positive bottom eigenvalue.

---

## 4. Proof of Theorem 2.1

Let $U\in\Omega_{\theta_0}$ and $X\in H_U$.

By Lemma 3.1,
\[
\mathrm{Ric}_g(X,X)=\kappa\,g(X,X).
\]

By Lemma 3.3,
\[
\nabla^2 S_\beta(X,X)\ge \beta c_W\, g(X,X).
\]

Therefore,
\[
\mathrm{Ric}_{\mu_\beta}(X,X)
=\mathrm{Ric}_g(X,X)+\nabla^2 S_\beta(X,X)
\ge (\kappa+\beta c_W)\,g(X,X).
\]
This proves the claim.

\(\square\)

---

## 5. Interpretation and limits

### 5.1 Functional inequalities and a local gap

A uniform lower bound on $\mathrm{Ric}_{\mu_\beta}$ (in the Bakry–Émery sense) implies Poincaré and log-Sobolev inequalities (hence a spectral gap) for the diffusion generator
\[
L = \Delta_g - \nabla S_\beta\cdot\nabla,
\]
at least within the small-field tube where the estimate holds.

### 5.2 “Mass from curvature”

Heuristically, on physical modes the Hessian contributes a quadratic restoring force. The effective “mass scale” suggested by the estimate is
\[
m_{\mathrm{eff}}^2 \sim \kappa+\beta c_W.
\]

### 5.3 What remains nontrivial

1. **Globalization:** extending beyond the small-angle sector (Gribov horizon / large-field behavior).
2. **Uniformity:** controlling $c_W$ under RG/coarse-graining and in the continuum limit.
3. **Continuum lifting:** showing the curvature lower bound survives $a\to 0$ in a physically normalized way (via Mosco/OS machinery).

