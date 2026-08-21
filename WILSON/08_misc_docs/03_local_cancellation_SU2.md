# Assumption (A') and the local cancellation problem for $SU(2)$ Wilson force

## 1. Disorder functional and coercivity hypothesis

Let $G=SU(2)$.  For a finite lattice $\Lambda$, define the plaquette disorder observable
\[
\mathcal B_\Lambda(U)
:= \frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)}\Big(1-\frac12\Re\mathrm{Tr}(U_p(U))\Big),
\qquad 0\le \mathcal B_\Lambda\le 2.
\]
Let $S_\Lambda=\beta\sum_{p}\Phi(U_p)$ be the Wilson action.

A coercivity input used in the fixed-cutoff drift-domination program can be phrased as:

> **Assumption (A').**  There exist constants $\varepsilon_0>0$ and $c_0(\varepsilon_0,\beta)>0$, independent of volume $|\Lambda|$, such that
> \[
> \mathcal B_\Lambda(U)\ge \varepsilon_0\quad\Longrightarrow\quad \|\nabla S_\Lambda(U)\|_{g_\Lambda}\ge c_0(\varepsilon_0,\beta).
> \]

This is an energy-landscape statement: configurations with macroscopic plaquette disorder cannot be approximate stationary points of the Wilson action.

## 2. Linkwise force decomposition

Fix an oriented link $\ell\in E(\Lambda)$.  Denote the linkwise gradient by $\nabla_\ell S_\Lambda(U)\in T_{U_\ell}G\cong\mathfrak{su}(2)$ (right-trivialized).

The Wilson force at $\ell$ can be written schematically as a sum over plaquettes incident to $\ell$:
\[
\nabla_\ell S_\Lambda(U)
= \sum_{p\ni \ell} \sigma_{p,\ell}\,\mathrm{Ad}_{g_{p,\ell}(U)}\big(X_p(U)\big),
\qquad
X_p(U):=\nabla\Phi\big(U_p(U)\big)\in\mathfrak{su}(2),
\]
where:

- the signs $\sigma_{p,\ell}\in\{\pm 1\}$ depend on the relative orientation of $p$ and $\ell$;
- the transports $g_{p,\ell}(U)\in SU(2)$ are products of nearby link variables determined by the plaquette boundary;
- $\mathrm{Ad}$ denotes the adjoint representation.

In $d=4$, each link is incident to $m=6$ plaquettes, organized as three transverse pairs.

## 3. Single-plaquette coercivity

For $SU(2)$, the plaquette energy and the plaquette force are linked by compactness:

> **Lemma 3.1 (single-plaquette lower bound).**  For every $\varepsilon>0$ and fixed $\beta>0$ there exists $c_1(\varepsilon,\beta)>0$ such that
> \[
> 1-\frac12\Re\mathrm{Tr}(U_p)\ge \varepsilon
> \quad\Longrightarrow\quad
> \|X_p\|\ge c_1(\varepsilon,\beta).
> \]

This isolates the remaining difficulty: $\nabla_\ell S$ is a **sum** of transported plaquette-force vectors, so cancellations are possible.

## 4. Local cancellation lemma (geometric input)

A clean sufficient statement for (A') is a link-local “no-cancellation except on an exceptional aligned set” lemma.

> **Lemma 4.1 (local cancellation $\Rightarrow$ aligned Cartan).**  Fix $\varepsilon>0$ and a link $\ell$.  Suppose at least one incident plaquette satisfies
> \(
> 1-\frac12\Re\mathrm{Tr}(U_p)\ge \varepsilon.
> \)
> Then either
> \[
> \|\nabla_\ell S_\Lambda(U)\|\ge c(\varepsilon,\beta)
> \]
> for a constant $c(\varepsilon,\beta)>0$ independent of $|\Lambda|$, or else the incident plaquette forces are all aligned in a common Cartan axis and the transports $\mathrm{Ad}_{g_{p,\ell}(U)}$ preserve that axis (an exceptional lower-dimensional condition).

If Lemma 4.1 holds with a uniform constant, then (A') follows by an incidence-counting argument: macroscopic disorder forces a positive density of rough plaquettes, hence there exists at least one link with a rough incident plaquette, hence $\|\nabla S\|$ is bounded below.

## 5. What must be proved to make Lemma 4.1 referee-complete

A fully rigorous proof of Lemma 4.1 must check the following finite-dimensional items.

1. **Transport constraints.**  The adjoint rotations $\mathrm{Ad}_{g_{p,\ell}(U)}$ are not arbitrary elements of $SO(3)$; they are constrained products of neighboring link variables.  The exceptional set must respect these constraints.

2. **Closedness / empty interior.**  Show the exact cancellation locus (or near-cancellation locus) is closed and has empty interior inside the set where at least one incident plaquette is $\varepsilon$-rough.

3. **Quantitative separation.**  On the compact set
\[
\{U:\ \exists p\ni\ell\text{ with }1-\tfrac12\Re\mathrm{Tr}(U_p)\ge \varepsilon\}\setminus \mathcal E,
\]
where $\mathcal E$ is the exceptional aligned set, the continuous function $U\mapsto\|\nabla_\ell S(U)\|$ attains a positive minimum.

4. **Uniformity.**  The constant must depend only on $(\varepsilon,\beta)$ (and group normalizations), not on $|\Lambda|$.

## 6. Numerical evidence (supporting only)

Exact-force gradient-descent experiments in a 2D $SU(2)$ torus toy model (random and checkerboard Cartan initializations, varying $L$) showed that driving $\|\nabla S\|$ toward zero collapses the disorder toward the vacuum, and did not exhibit rough configurations with near-zero force.  This is consistent with (A') but does not replace a proof.
