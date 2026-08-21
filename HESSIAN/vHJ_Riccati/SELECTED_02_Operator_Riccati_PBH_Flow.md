\
---
title: "Operator Riccati / PBH flow: a comparison principle for a protected curvature floor"
date: 2025-12-29
format: markdown+latex
---

## Abstract

The project’s central dynamical idea is to treat “renormalization / coarse-graining” as an evolution of an **effective action** $S_t$ (or free energy) and track the evolution of its (physical) Hessian $H(t)=\nabla^2 S_t$.

A recurring model equation in the project files is an **operator Riccati equation**
\[
\partial_t H(t) = -2H(t)^2 + \mathcal{R}(t),
\]
where $\mathcal{R}(t)$ is a source term (“curvature injection”) combining Haar geometry, anomaly contributions, and controlled corrections.

This note isolates the cleanest first-principles part: how *positivity of the source* forces a **uniform eigenvalue floor** for $H(t)$, i.e. a mass-gap mechanism.

---

## 1. Minimal model: operator Riccati inequality

Let $\mathcal{H}$ be a real Hilbert space and let $H(t)$ be a family of bounded self-adjoint operators on $\mathcal{H}$.

Assume $H(t)$ satisfies the differential inequality (in quadratic-form sense)
\[
\partial_t H(t) \succeq -2H(t)^2 + \sigma\,I
\qquad (t\ge 0)
\]
for some constant $\sigma>0$.

Define the smallest spectral value
\[
\lambda(t) := \inf\sigma(H(t)).
\]

### Proposition 1.1 (Scalar Riccati lower bound)

Under the above assumptions, $\lambda(t)$ satisfies the scalar differential inequality
\[
\dot\lambda(t)\ge -2\lambda(t)^2 + \sigma,
\]
in the sense of upper Dini derivatives. In particular, for all $t\ge 0$,
\[
\lambda(t)\ge \underline\lambda(t),
\]
where $\underline\lambda$ is the solution of the scalar Riccati ODE
\[
\dot{\underline\lambda} = -2\underline\lambda^2+\sigma,\qquad \underline\lambda(0)=\lambda(0).
\]

*Proof sketch.* Pick a unit vector $v(t)$ approximating the ground eigendirection (or use a minimizing sequence for the Rayleigh quotient). Differentiate
\[
\langle v, H v\rangle
\]
along time, estimate with $\partial_t H\succeq -2H^2+\sigma I$, and use
\[
\langle v, H^2 v\rangle \ge \langle v, H v\rangle^2
\]
(Cauchy–Schwarz for the spectral measure). Standard arguments give the Dini derivative bound.

---

### Corollary 1.2 (Protected floor)

Let
\[
\lambda_* := \sqrt{\sigma/2}.
\]
Then any solution of $\dot\lambda=-2\lambda^2+\sigma$ with initial data $\lambda(0)\ge 0$ satisfies
\[
\lambda(t)\ge \min\{\lambda(0),\lambda_*\}
\quad\text{for all }t\ge 0,
\]
and in fact $\lambda(t)\to \lambda_*$ as $t\to\infty$.

So: **a strictly positive source $\sigma$ forces a strictly positive asymptotic fixed point**.

---

## 2. Where the source term comes from in the project

In the lattice “mass-from-curvature” theorem, the Bakry–Émery tensor reads
\[
\mathrm{Ric}_{\mu_\beta}=\mathrm{Ric}_g+\nabla^2 S_\beta,
\]
and on horizontal directions near identity it is bounded below by $(\kappa+\beta c_W)g$.

In the project’s flow language, this is interpreted as an initial positive curvature floor, feeding an evolution of the physical Hessian with a positive injection term (Haar + anomaly).

A generic decomposition used in the project notes is:
\[
\sigma_{\mathrm{eff}}(t) = \sigma_{\mathrm{Haar}}(t) + \sigma_{\mathrm{anomaly}}(t) + \sigma_{\mathrm{corr}}(t).
\]

- $\sigma_{\mathrm{Haar}}$ is geometric and positive at the lattice scale.
- $\sigma_{\mathrm{anomaly}}$ is expected to be positive if the nonperturbative $\beta$-function has the usual sign structure.
- $\sigma_{\mathrm{corr}}$ are corrections that must be controlled so they cannot cancel positivity.

When one proves a lower bound $\sigma_{\mathrm{eff}}(t)\ge \sigma_0>0$ (in the relevant local block), Proposition 1.1 yields a protected eigenvalue floor $\lambda(t)\ge \sqrt{\sigma_0/2}$ — the “mass gap mechanism.”

---

## 3. Stratified spaces, polarity, and “why singularities might not kill it”

A serious obstruction in gauge theory is that the natural configuration space (gauge quotient) is **stratified** (reducibles / orbit-type singularities). Maximum principles and comparison estimates can fail if singular sets are not controlled.

The project introduces a strategy: show the singular set is **polar** (capacity zero) for the relevant Dirichlet form. Then “almost everywhere” arguments, quasi-continuity, and form methods can let comparison principles go through on the regular stratum.

This is ambitious, but the conceptual glue is:

1. Prove the operator-Riccati inequality on the regular stratum.
2. Show singular strata have capacity $0$.
3. Apply parabolic comparison quasi-everywhere, hence preserve positivity.

---

## 4. What makes this potentially new

The scalar Riccati mechanism is classical. The *project’s novel move* is the claim that **Yang–Mills coarse-graining drives an operator-Riccati inequality whose source term has geometric positivity contributions** (Haar curvature and anomaly), allowing one to turn a very QFT-ish problem into a robust comparison principle.

If this can be made fully rigorous, it is a reusable template:

- any QFT where the effective action Hessian obeys such inequalities would inherit a “mass from curvature injection” phenomenon,
- and the remaining hard work becomes: proving $\sigma_{\mathrm{eff}}(t)\ge \sigma_0>0$ uniformly and controlling singular strata.

---

## 5. Concrete next steps to harden this into a theorem

1. **Derive the operator evolution** $\partial_t H=-2H^2+\mathcal{R}$ from an explicit RG scheme (even in a controlled approximation, e.g. block-spin for a finite lattice).
2. **Prove a coercive lower bound** on $\mathcal{R}$ in the local/horizontal block.
3. **Quantify errors** from off-diagonal mixing (local vs topological) and show they are smaller than the geometric floor.
4. Replace heuristic “maximum principle in infinite dimensions” with **Dirichlet-form semigroup** methods (contractivity + domination).

