# Part II — Lattice Yang–Mills as a Curvature–Controlled Gibbs Measure  
## Section 1 — Lattice Configuration Manifold and Riemannian Metric

In this section we set up the **finite-volume configuration manifold** for lattice gauge fields and endow it with a natural Riemannian structure. This gives the geometric backbone needed to apply the Part I machinery to lattice Yang–Mills.

We work completely at the level of finite lattices and compact Lie groups; no continuum or renormalization limit is considered here.

---

## 1.1. Finite lattice and combinatorial structure

Fix:

- A spatial dimension \(d \in \mathbb{N}\) (typically \(d=4\) in Yang–Mills applications),
- A finite hypercubic lattice \(\Lambda \subset \mathbb{Z}^d\) with periodic or fixed boundary conditions.

### 1.1.1. Sites, oriented edges, plaquettes

We denote:

- The set of sites (vertices) by
  \[
  V(\Lambda) := \Lambda.
  \]
- The set of **oriented edges** by
  \[
  E(\Lambda) := \{ (x,\mu) : x\in\Lambda,\ 1\le\mu\le d,\ x+\hat\mu\in\Lambda \},
  \]
  where \(\hat\mu\) is the unit vector in direction \(\mu\). The edge \((x,\mu)\) connects \(x\) to \(x+\hat\mu\).
- The set of **plaquettes** \(P(\Lambda)\), i.e. oriented elementary squares spanned by pairs of coordinate directions \((\mu,\nu)\) with \(1\le\mu<\nu\le d\), based at sites \(x\) such that \(x,x+\hat\mu,x+\hat\nu,x+\hat\mu+\hat\nu \in \Lambda\).

We will not need a detailed indexing of plaquettes in this section; it suffices that \(P(\Lambda)\) is finite.

### 1.1.2. Graph viewpoint

We may equivalently view \((V(\Lambda),E(\Lambda))\) as a finite oriented graph with underlying undirected edges
\[
\{\{x,x+\hat\mu\} : (x,\mu)\in E(\Lambda)\}.
\]

The precise boundary conditions and edge identifications (periodic vs. open) affect only global topology, not the local differential geometry developed here.

---

## 1.2. Gauge group and single-link manifold

Let \(G\) be a compact, connected Lie group. In Yang–Mills applications we typically take
\[
G = SU(N),
\]
with \(N\ge 2\). For this section, all statements hold for general compact \(G\) with a fixed bi-invariant metric.

### 1.2.1. Lie group structure

- \(G\) is a smooth manifold of dimension \(n_G := \dim G < \infty\),
- Its Lie algebra \(\mathfrak{g} := T_e G\) is a finite-dimensional real Lie algebra,
- The group operations (multiplication and inversion) are smooth.

### 1.2.2. Bi-invariant Riemannian metric on \(G\)

We fix once and for all a **bi-invariant Riemannian metric** \(g_G\) on \(G\), i.e.:

- For each \(h\in G\), left and right translations
  \[
  L_h : G\to G, \quad L_h(U) := hU,
  \qquad
  R_h : G\to G, \quad R_h(U) := Uh,
  \]
  are isometries:
  \[
  (L_h)^* g_G = g_G, \qquad (R_h)^* g_G = g_G.
  \]

Such a metric exists for any compact Lie group; it can be obtained, for example, by averaging an arbitrary inner product on \(\mathfrak{g}\) over the group.

We write:

- \(\langle \cdot,\cdot\rangle_G\) for the inner product on \(\mathfrak{g}\) induced by \(g_G\) at the identity,
- \(|X|_G^2 := \langle X,X\rangle_G\) for \(X\in\mathfrak{g}\),
- \(d\mathrm{vol}_{g_G}\) for the corresponding Riemannian volume form on \(G\).

This volume form coincides (up to normalization) with the normalized **Haar probability measure** on \(G\), which we denote by \(dU\).

### 1.2.3. Right-invariant identification of tangent spaces

Bi-invariance implies in particular right-invariance:

- For each \(U\in G\), the differential of the right translation \(R_U\) gives an isometric identification
  \[
  dR_U\big|_e : (\mathfrak{g},\langle\cdot,\cdot\rangle_G) \to (T_U G, g_G).
  \]

This allows us to represent any tangent vector \(X_U\in T_U G\) uniquely as
\[
X_U = dR_U\big|_e(X), \quad X\in\mathfrak{g},
\]
and define its norm by \(|X_U|_{g_G} = |X|_G\).

We will later use this identification to write gradients and Hessians in terms of Lie algebra coordinates.

---

## 1.3. Configuration manifold for the finite lattice

Given the finite oriented edge set \(E(\Lambda)\) and the group manifold \(G\), we define the **finite-volume configuration manifold** as the Cartesian product
\[
M_\Lambda := G^{E(\Lambda)}.
\]

A point \(U\in M_\Lambda\) is an assignment
\[
U = (U_\ell)_{\ell\in E(\Lambda)}, \quad U_\ell \in G.
\]

This is the usual configuration space of lattice gauge fields (link variables) on \(\Lambda\).

### 1.3.1. Product manifold structure

As a finite Cartesian product of smooth manifolds, \(M_\Lambda\) is itself a smooth manifold of dimension
\[
\dim M_\Lambda = |E(\Lambda)| \cdot \dim G = |E(\Lambda)|\, n_G.
\]

We denote points of \(M_\Lambda\) by \(U = (U_\ell)_{\ell\in E(\Lambda)}\). For each \(\ell\), the projection
\[
\pi_\ell : M_\Lambda \to G, \quad \pi_\ell(U) = U_\ell,
\]
is smooth.

The tangent space at \(U\) splits canonically as a product:
\[
T_U M_\Lambda \cong \bigoplus_{\ell\in E(\Lambda)} T_{U_\ell} G.
\]

Under the right-invariant identifications \(T_{U_\ell}G \cong \mathfrak{g}\), we can equivalently view
\[
T_U M_\Lambda \cong \mathfrak{g}^{E(\Lambda)}.
\]

---

## 1.4. Product Riemannian metric on \(M_\Lambda\)

We now endow \(M_\Lambda\) with a Riemannian metric built as the product of the single-link metrics \(g_G\).

### 1.4.1. Definition of the product metric

For each \(U\in M_\Lambda\) and tangent vectors
\[
V = (V_\ell)_{\ell\in E(\Lambda)},\quad W = (W_\ell)_{\ell\in E(\Lambda)} \in T_U M_\Lambda,
\]
we define
\[
g_\Lambda(U)(V,W)
:= \sum_{\ell\in E(\Lambda)} g_G(U_\ell)(V_\ell,W_\ell).
\]

This is the standard product Riemannian metric on \(G^{E(\Lambda)}\). In particular:

- The tangent bundle splits as
  \[
  TM_\Lambda \cong \bigoplus_{\ell\in E(\Lambda)} \pi_\ell^*(TG),
  \]
  and the inner product is the direct sum of the inner products on each factor.
- Under the right-invariant identifications \(T_{U_\ell}G \cong \mathfrak{g}\), we can write
  \[
  g_\Lambda(U)(V,W)
  = \sum_{\ell\in E(\Lambda)} \langle X_\ell,Y_\ell\rangle_G,
  \]
  where \(V_\ell=dR_{U_\ell}(X_\ell)\), \(W_\ell=dR_{U_\ell}(Y_\ell)\) for unique \(X_\ell,Y_\ell\in\mathfrak{g}\).

### 1.4.2. Norms and volume form

The norm of a tangent vector \(V\in T_U M_\Lambda\) is
\[
|V|_{g_\Lambda}^2
= \sum_{\ell\in E(\Lambda)} |V_\ell|_{g_G}^2.
\]

The corresponding Riemannian volume form is the product of the single-link volume forms:
\[
d\mathrm{vol}_{g_\Lambda}(U)
= \prod_{\ell\in E(\Lambda)} d\mathrm{vol}_{g_G}(U_\ell)
= \prod_{\ell\in E(\Lambda)} dU_\ell,
\]
where \(dU_\ell\) denotes the normalized Haar probability measure on \(G\).

Thus, **the Riemannian volume on \(M_\Lambda\) is exactly the product Haar measure** on all links.

---

## 1.5. Product Ricci curvature

The Ricci curvature of the product manifold \((M_\Lambda,g_\Lambda)\) is obtained from the Ricci curvature of \((G,g_G)\).

### 1.5.1. Ricci curvature of a bi-invariant compact group

Let \(\operatorname{Ric}_G\) denote the Ricci tensor of \((G,g_G)\). For a compact, connected Lie group with bi-invariant metric, \(\operatorname{Ric}_G\) is left- and right-invariant and hence determined by an \(\mathrm{Ad}\)-invariant bilinear form on \(\mathfrak{g}\). In particular, there exists a constant \(\kappa_G \in \mathbb{R}\) such that
\[
\operatorname{Ric}_G \ge \kappa_G\, g_G
\]
as quadratic forms.

For the usual choices of normalization (e.g. minus the Killing form on each simple ideal, as in \(G=SU(N)\)), one has \(\kappa_G>0\). The exact value of \(\kappa_G\) is not needed in this section; only a uniform lower bound matters.

### 1.5.2. Product Ricci curvature

For a finite product of Riemannian manifolds \((M_i,g_i)\), the Ricci tensor of the product \(\big(\prod_i M_i,\bigoplus_i g_i\big)\) is the direct sum of the Ricci tensors:
\[
\operatorname{Ric}_{\prod_i M_i}
= \bigoplus_i \operatorname{Ric}_{M_i}.
\]

In our setting, each factor is \((G,g_G)\), so
\[
\operatorname{Ric}_{g_\Lambda}
= \bigoplus_{\ell\in E(\Lambda)} \operatorname{Ric}_G
= \kappa_G \bigoplus_{\ell\in E(\Lambda)} g_G
= \kappa_G\, g_\Lambda.
\]

Thus \((M_\Lambda,g_\Lambda)\) is also an Einstein manifold with constant \(\kappa_G\), and we have the uniform lower bound
\[
\operatorname{Ric}_{g_\Lambda} \ge \kappa_G\, g_\Lambda,
\]
with \(\kappa_G\) independent of \(\Lambda\).

This is the **geometric curvature contribution** from the Haar part of the measure, before adding any action-dependent potential \(S_\Lambda\).

---

## 1.6. Summary of Section 1 — Geometric Backbone for Lattice Gauge Fields

We have defined, for each finite lattice \(\Lambda\):

1. The configuration manifold
   \[
   M_\Lambda = G^{E(\Lambda)}
   \]
   of link variables, a finite-dimensional smooth manifold.

2. A natural product Riemannian metric \(g_\Lambda\) on \(M_\Lambda\) built from a fixed bi-invariant metric on \(G\).

3. The corresponding Riemannian volume form \(d\mathrm{vol}_{g_\Lambda}\), which is exactly the product Haar measure on link variables.

4. The Ricci tensor of \((M_\Lambda,g_\Lambda)\), which satisfies
   \[
   \operatorname{Ric}_{g_\Lambda} = \kappa_G\, g_\Lambda
   \]
   for some constant \(\kappa_G\) depending only on the group and the metric normalization, but **not** on \(\Lambda\).

In subsequent sections of Part II we will:

- Introduce the lattice Yang–Mills action \(S_\Lambda\) (Wilson action, gauge-fixing, and Haar-Jacobian contributions),
- Compute (or bound) the Hessian \(\nabla^2 S_\Lambda\) on the physical (gauge-orthogonal) directions,
- And combine this with \(\operatorname{Ric}_{g_\Lambda} = \kappa_G g_\Lambda\) to obtain a **horizontal Bakry–Émery curvature lower bound**
  \[
  \operatorname{Ric}_{\mu_\Lambda} = \operatorname{Ric}_{g_\Lambda} + \nabla^2 S_\Lambda \;\ge\; \rho_* g_\Lambda
  \]
  in the sense required by the abstract Hypothesis H\(_{\mathrm{curv}}\) of Part I.
