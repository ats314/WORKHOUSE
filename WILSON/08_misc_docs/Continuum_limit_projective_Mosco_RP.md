# Continuum limit: projective measures, Mosco convergence, and reflection-positivity transfer

## Purpose

The project files outline a "three-bridge" strategy for passing lattice control to the continuum:

1. **Projective limits** for measures $\mu_a$ to obtain a continuum Euclidean field measure $\mu$.
2. **Mosco convergence** (a variational convergence) of Dirichlet forms to pass semigroup/spectral information to the limit.
3. **Reflection positivity transfer** to ensure OS reconstruction still works in the continuum.

This note extracts that architecture and flags the biggest unresolved issue: **how the convexity/spectral constants scale with lattice spacing $a$**.

---

## 1. The measure-theoretic bridge: projective limits

Let $\{\mathcal A_a\}_{a>0}$ denote the lattice configuration spaces at mesh $a$, and let $\pi_{a'\to a}:\mathcal A_{a'}\to\mathcal A_a$ be the natural coarse-graining map (forgetting fine links or averaging).

A projective system of measures is a family $\{\mu_a\}$ such that
\[
(\pi_{a'\to a})_\#\mu_{a'} = \mu_a
\qquad (a'<a).
\]

If, in addition, the family is tight in a suitable topology, a projective-limit theorem (Kolmogorov/Prokhorov style) produces a limit probability measure $\mu$ on a continuum configuration space $\mathcal A$ whose cylinder measures agree with $\mu_a$.

**This is attractive for gauge theory** because gauge fields are naturally specified by holonomies on links/paths, and "restriction to a coarser graph" is canonical.

---

## 2. Reflection positivity in the limit

Assume each lattice measure $\mu_a$ is reflection positive with respect to a time hyperplane. For each $a$, reflection positivity means:
\[
\langle \Theta F \cdot F\rangle_{\mu_a} \ge 0
\quad
\text{for all }F \text{ supported in positive times.}
\]

A common transfer argument is:

1. Reflection-positive inequalities hold for **cylinder functions** (depending on finitely many links).
2. Cylinder functions are stable under pullback/pushforward by the projective maps.
3. If the projective limit measure $\mu$ exists and agrees on cylinders, then the same inequality holds under $\mu$ for cylinder functions.
4. By density/closure, one extends reflection positivity to an appropriate function class in $L^2(\mu)$.

If successful, OS reconstruction can be carried out at the limit measure $\mu$, yielding a continuum Hilbert space and a semigroup of time translations.

---

## 3. The analytic bridge: Mosco convergence of Dirichlet forms

Given a symmetric Markov semigroup $P_t^a$ on $L^2(\mu_a)$ with generator $L_a$, define the Dirichlet form
\[
\mathcal E_a(f,f) := \langle f, -L_a f\rangle_{L^2(\mu_a)}.
\]

**Mosco convergence** $\mathcal E_a \to \mathcal E$ (together with tightness and core density conditions) implies:

- strong resolvent convergence of generators,
- convergence of semigroups on a dense class,
- and lower semicontinuity of spectral quantities.

Heuristically, this is the right tool to pass Poincaré/LSI-type bounds to the limit, provided the constants remain controlled.

---

## 4. The scaling bottleneck: do the constants survive $a\to 0$?

Everything above is powerless if the key constants degenerate as $a\to0$.

The project contains two competing scaling intuitions:

### (A) Haar baseline survives

One line of thought emphasizes that the Haar geometry gives a **dimensionless** curvature baseline (in link variables), and thus a nonvanishing constant $\kappa_*>0$ at each scale. If this persists through the continuum construction, it would provide an RG-stable convexity anchor.

### (B) Wilson quadratic term collapses

Another scaling argument notes that if one writes link variables as $U=\exp(aA)$ with continuum field $A$, then derivatives in $U$ correspond to $a$-scaled derivatives in $A$. In naive continuum scaling,
\[
S_W \sim \beta \sum_p a^4\, \|F\|^2,
\]
while discrete gradients scale like $a^{-1}$ (or $a^{-2}$ for Laplacian-type operators), leading to an apparent factor $\beta a^2$ in the Hessian. With asymptotic freedom $\beta\sim \log(1/a)$, the product $\beta a^2\to0$.

If correct, this would mean the Wilson contribution to convexity disappears in the limit, leaving only the Haar/metric effects.

### The real issue: coordinate conventions matter

These statements can be consistent only after choosing a **precise identification** between:

- the tangent norm on $SU(3)$,
- the normalization of the lattice gauge coupling $\beta$,
- and the scaling $U=\exp(aA)$.

Because convexity is a *second derivative* object, it is extremely sensitive to whether one differentiates with respect to $U$-coordinates (dimensionless) or $A$-coordinates (dimensionful).

A publishable continuum argument must fix this carefully and track how the metric rescales.

---

## 5. A concrete checklist for making the continuum step real

1. **Define the continuum configuration space** $\mathcal A$ and the projective maps $\pi_{a'\to a}$ explicitly.
2. Prove **tightness** (or an equivalent compactness criterion) for $\{\mu_a\}$.
3. Show **reflection positivity** is stable under the projective limit on cylinder functions.
4. Define the diffusion Dirichlet forms $\mathcal E_a$ with a consistent scaling and prove Mosco convergence.
5. Establish that the **spectral gap / LSI constants do not vanish** under the chosen scaling.
6. Reconstruct the OS Hilbert space and prove that the limiting Hamiltonian has a nonzero gap.

---

## Provenance in this project

This note is synthesized primarily from:

- `Continuum Limit and Scaling.txt` (the scaling discussion and the claim that only certain curvature contributions survive),
- `Comparing Diffusion and OS Gaps.txt` (Mosco convergence / resolvent and reflection positivity transfer architecture),
- `Full Proof Attempt at 12-10-25 Many holes.txt` (continuum preparation and the need for an additional continuum-limit argument).

