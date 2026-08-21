---
title: "Selection C — Wilson Hessian and Discrete Hodge Decomposition"
date: "2025-12-28"
---

# Abstract

The Wilson plaquette action is strictly convex only in the *physical* directions: its Hessian degenerates along gauge orbits.
Near the vacuum, the quadratic approximation of the Wilson action identifies its Hessian with a discrete Yang–Mills operator
\[
d_1^\ast d_1
\]
acting on $\mathfrak g$–valued 1–cochains. Discrete Hodge theory cleanly separates gauge directions (exact 1–forms) from physical directions (coexact 1–forms). This is the algebraic engine behind horizontal coercivity in the curvature program.

# 1. Cochain notation on a finite lattice

Let $\Lambda$ be a finite oriented cell complex (e.g. a finite box in $\mathbb Z^d$) with edge set $E(\Lambda)$ and plaquette set $P(\Lambda)$.
Let $\mathfrak g$ be the Lie algebra of a compact Lie group $G$ with $\mathrm{Ad}$–invariant inner product $\langle\cdot,\cdot\rangle$.

Define $\mathfrak g$–valued cochains:
\[
C^0(\Lambda;\mathfrak g)\cong \mathfrak g^{V(\Lambda)},\qquad
C^1(\Lambda;\mathfrak g)\cong \mathfrak g^{E(\Lambda)},\qquad
C^2(\Lambda;\mathfrak g)\cong \mathfrak g^{P(\Lambda)}.
\]

Let $d_0:C^0\to C^1$ and $d_1:C^1\to C^2$ denote the discrete exterior derivatives (coboundary operators).
Equip $C^k$ with the product inner product induced by $\langle\cdot,\cdot\rangle$.

# 2. Wilson action and small-field parameterization

Fix inverse coupling $\beta>0$ and write the Wilson action as
\[
S_W(U)\ :=\ \frac{\beta}{N}\sum_{p\in P(\Lambda)} \mathrm{Re}\,\mathrm{Tr}\big(I - U_p\big),
\]
where $U_p$ is the ordered product of edge variables around the plaquette $p$.

Near the vacuum configuration $U^{(0)}\equiv I$, write each link variable as
\[
U_e=\exp(A_e),\qquad A_e\in\mathfrak g,\quad \|A_e\|\ll 1.
\]
Let $A\in C^1(\Lambda;\mathfrak g)$ denote the collection $(A_e)_e$.

## Lemma 2.1 (Plaquette expansion)

For each plaquette $p$,
\[
U_p = \exp\big((d_1 A)_p + O(\|A\|^2)\big),
\]
where $(d_1A)_p$ is the discrete curvature 2–cochain.

### Proof sketch

Expand the ordered product of exponentials around $p$ and use the Baker–Campbell–Hausdorff formula.
At linear order, the holonomy is the alternating sum of the edge Lie algebra elements, i.e. $(d_1A)_p$. ∎

## Lemma 2.2 (Quadratic expansion of the plaquette potential)

For small $X\in\mathfrak g$,
\[
\mathrm{Re}\,\mathrm{Tr}(I-e^X) = \frac12\,\langle X,X\rangle + O(\|X\|^3),
\]
under the standard metric/trace normalization.

### Proof sketch

Expand $e^X=I+X+\frac12X^2+O(\|X\|^3)$ and use $\mathrm{Tr}(X)=0$ in a compact semisimple Lie algebra representation. ∎

## Proposition 2.3 (Quadratic form of the Wilson action)

Combining the above,
\[
S_W(U)
=
\frac{\beta}{2N}\sum_{p\in P(\Lambda)} \|(d_1 A)_p\|^2 + O(\|A\|^3)
=
\frac{\beta}{2N}\,\langle A,\ d_1^\ast d_1 A\rangle\ +\ O(\|A\|^3).
\]

In particular, the Hessian at the vacuum is
\[
\nabla^2 S_W(U^{(0)}) \;\simeq\; \frac{\beta}{N}\, d_1^\ast d_1
\quad\text{on } C^1(\Lambda;\mathfrak g).
\]

# 3. Gauge directions and discrete Hodge decomposition

Infinitesimal gauge transformations at the vacuum act by
\[
A \mapsto A + d_0\phi,\qquad \phi\in C^0(\Lambda;\mathfrak g).
\]
Thus $\mathrm{im}(d_0)$ is the tangent to the gauge orbit (vertical space) at $U^{(0)}$.

Discrete Hodge decomposition states (under appropriate boundary conditions)
\[
C^1(\Lambda;\mathfrak g)\ =\ \mathrm{im}(d_0)\ \oplus\ \mathrm{im}(d_2^\ast)\ \oplus\ \mathcal H^1,
\]
where $\mathcal H^1$ is the space of harmonic 1–cochains.

- **Exact 1–forms** $\mathrm{im}(d_0)$ are pure gauge (vertical).
- **Coexact 1–forms** $\mathrm{im}(d_2^\ast)$ are divergence-free physical directions (horizontal at vacuum).
- **Harmonic 1–forms** $\mathcal H^1$ are topological zero modes (absent on a contractible box with Dirichlet-type boundary conditions).

## Proposition 3.1 (Kernel and coercivity structure)

At the vacuum,
\[
d_1(d_0\phi)=0,
\]
so $\mathrm{im}(d_0)\subseteq \ker(d_1)$ and hence $\mathrm{im}(d_0)\subseteq \ker(d_1^\ast d_1)$.

On the orthogonal complement $\mathrm{im}(d_0)^\perp$ (and after removing $\mathcal H^1$ if present),
the operator $d_1^\ast d_1$ is strictly positive.

### Consequence (horizontal Wilson convexity)

If $\Lambda$ is simply connected with boundary conditions eliminating harmonic 1–forms, then there exists $\lambda_{\min}>0$ such that
\[
\langle A,\ d_1^\ast d_1 A\rangle \ \ge\ \lambda_{\min}\,\|A\|^2
\quad\text{for all } A\in \mathrm{im}(d_0)^\perp.
\]
This is the analytic meaning of “Wilson action is convex in physical directions.”

# 4. How this plugs into curvature methods

In a Bakry–Émery curvature computation for a Gibbs measure with density $e^{-S_W}$, the relevant tensor is
\[
\mathrm{Ric}_{\mu} = \mathrm{Ric}_{M_\Lambda} + \nabla^2 S_W + \cdots .
\]
Because $\nabla^2 S_W$ has a gauge kernel, one should test it only on horizontal vectors. The above identifies
the horizontal coercivity constant explicitly with a spectral gap of $d_1^\ast d_1$ on coexact forms.

This gives a clean roadmap:

1. Use discrete Hodge theory to identify horizontal directions at the vacuum.
2. Prove stability of the coercivity lower bound in a small-field neighborhood (continuity of the Hessian).
3. Combine with Ricci positivity of $G^{E(\Lambda)}$ and the Haar convexity term to obtain a **uniform horizontal curvature bound**.

