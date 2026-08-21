---
title: "Wilson Hessian, Discrete Hodge Decomposition, and the Haar Mass Mechanism (Extracted)"
author: "Project extraction (Parts 6, 9–10)"
date: "2025-12-28"
---

## Scope and status

This note extracts the **explicit finite-lattice quadratic analysis** around the vacuum:

1. the Wilson action has a Hessian equal to a discrete Maxwell operator,
2. gauge directions sit inside the kernel exactly as expected,
3. the Haar geometry supplies an **intrinsic positive quadratic term** (“Haar mass”)
   that lifts remaining degeneracies on physical directions.

Everything is on a finite lattice.

---

## 1. Linearization at the vacuum and discrete cochains

Fix a finite lattice $\Lambda$ (graph) with vertices $V(\Lambda)$ and oriented edges $E(\Lambda)$.
Let $\mathfrak g=\mathrm{Lie}(G)$ with an $\mathrm{Ad}$-invariant inner product $\langle\cdot,\cdot\rangle_G$.

### Definition 1.1 (Cochain spaces)

Let
\[
\mathcal C^0(\Lambda;\mathfrak g) := \mathfrak g^{V(\Lambda)},\qquad
\mathcal C^1(\Lambda;\mathfrak g) := \mathfrak g^{E(\Lambda)},
\qquad
\mathcal C^2(\Lambda;\mathfrak g) := \mathfrak g^{P(\Lambda)},
\]
where $P(\Lambda)$ is the set of oriented plaquettes.

Equip $\mathcal C^1$ with the product inner product
\[
\langle X,Y\rangle_{\mathcal C^1} := \sum_{\ell\in E(\Lambda)} \langle X_\ell, Y_\ell\rangle_G.
\]

### Definition 1.2 (Coboundary operators)

Let $d_0:\mathcal C^0\to\mathcal C^1$ be the discrete gradient (gauge derivative),
and $d_1:\mathcal C^1\to\mathcal C^2$ the discrete curl (plaquette curvature map).
Let $d_0^*,d_1^*$ denote adjoints with respect to the above inner products.

Define the discrete 1-form Laplacian
\[
\Delta_1 := d_0 d_0^* + d_1^* d_1.
\]

---

## 2. Gauge geometry = Hodge geometry at the vacuum

At the trivial configuration $U^{(0)}$, the tangent space identifies canonically as
\[
T_{U^{(0)}} M_\Lambda \cong \mathcal C^1(\Lambda;\mathfrak g).
\]

### Proposition 2.1 (Vertical directions are exact 1-forms)

The infinitesimal gauge action at the vacuum produces
\[
V_{U^{(0)}} \cong \mathrm{im}(d_0)\subset\mathcal C^1.
\]

### Proposition 2.2 (Hodge decomposition and physical horizontals)

There is an orthogonal Hodge decomposition
\[
\mathcal C^1
= \underbrace{\mathrm{im}(d_0)}_{\text{vertical / pure gauge}}
\oplus
\underbrace{\ker(\Delta_1)}_{\text{harmonic}}
\oplus
\underbrace{\mathrm{im}(d_1^*)}_{\text{co-exact (physical)}}.
\]

Accordingly, the physical horizontal subspace at the vacuum is
\[
H_{U^{(0)}} \;=\; \ker(\Delta_1)\ \oplus\ \mathrm{im}(d_1^*).
\]

---

## 3. Wilson action Hessian = discrete Maxwell operator

### Definition 3.1 (Wilson plaquette action)

Let $S_W$ be the Wilson action
\[
S_W(U)=\beta \sum_{p\in P(\Lambda)} \Big(1-\frac{1}{N}\mathrm{Re}\,\mathrm{tr}(U_p)\Big)
\quad\text{for }G=\mathrm{SU}(N),
\]
with the obvious analogue for general compact $G$ (using an $\mathrm{Ad}$-invariant class function).

Let $c_W>0$ denote the quadratic coefficient coming from the second variation at identity.

### Theorem 3.2 (Hessian at the vacuum)

At $U^{(0)}$,
\[
\nabla^2 S_W(U^{(0)}) \;=\; 2c_W\, d_1^* d_1,
\]
as a quadratic form on $\mathcal C^1(\Lambda;\mathfrak g)$.

Consequences:

- $\nabla^2 S_W(U^{(0)})$ is nonnegative;
- $\ker(\nabla^2 S_W(U^{(0)})) = \ker(d_1)$ (discrete closed 1-forms);
- restricted to $\mathrm{im}(d_1^*)$ (co-exact forms), it is strictly positive.

In words: the Wilson quadratic form is exactly the Maxwell energy $\|d_1 X\|^2$
around the vacuum.

---

## 4. Haar geometry supplies a universal quadratic term

### 4.1. Haar measure in exponential coordinates

Write a link variable near identity as $U_\ell=\exp(X_\ell)$ with $X_\ell\in\mathfrak g$.
Then the product Riemannian volume has density
\[
d\mathrm{vol}_{g_\Lambda}(U)
= \prod_{\ell\in E(\Lambda)} J_G(X_\ell)\, dX
= \exp\!\Big(-\sum_{\ell\in E(\Lambda)} S_H(X_\ell)\Big)\, dX,
\]
defining the **Haar potential** $S_H: \mathfrak g\to\mathbb R$.

The key point is that this contribution is **link-local** and therefore volume-uniform.

### Proposition 4.1 (Uniform convexity at the identity)

There exists $c_H>0$ depending only on $(G,g_G)$ such that, at $X=0$,
\[
\nabla^2 S_{H,\Lambda}(0)\ \ge\ c_H\,\mathrm{Id}_{\mathcal C^1},
\]
with $c_H$ independent of $\Lambda$.

Equivalently, near the vacuum the Haar density behaves like a universal Gaussian penalty
$\sim \exp(-c_H \|X\|^2)$ up to higher order terms.

---

## 5. Effective physical coercivity (Wilson + Haar)

Define the effective potential in flat coordinates:
\[
S_{\mathrm{eff},\Lambda}(X) := S_W(\exp X) + S_{H,\Lambda}(X).
\]

### Corollary 5.1 (Haar mass lifts physical degeneracies)

Restricted to the horizontal physical subspace $H_{U^{(0)}}$,
\[
\nabla^2 S_{\mathrm{eff},\Lambda}(0)\big|_{H_{U^{(0)}}}
=
\nabla^2 S_W(U^{(0)})\big|_{H_{U^{(0)}}}
+ c_0\,\mathrm{Id}_{H_{U^{(0)}}}
\ \ge\ c_0\,\mathrm{Id}_{H_{U^{(0)}}}
\]
for some $c_0>0$ depending only on $G$ (not on $\Lambda$).

This is the “Haar mass” mechanism: even if the Wilson Hessian vanishes on harmonic modes,
the Haar geometry supplies a universal positive quadratic term on *all* physical modes.

---

## 6. Why this matters

This local coercivity structure is the input that allows one to claim a **uniform small-field**
horizontal Bakry–Émery bound (Core Curvature Theorem) and then drive local-to-global
functional inequality arguments.

It is also a convenient point where gauge theory becomes “just” finite-dimensional
Riemannian geometry plus a structured local potential.

