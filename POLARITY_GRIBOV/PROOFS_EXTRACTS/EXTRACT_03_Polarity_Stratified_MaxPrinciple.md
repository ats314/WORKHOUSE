---
title: "EXTRACT 03 — Polarity and Stratified Maximum Principles: Making Singular Gauge Strata Harmless"
project: "SWIM2"
source_files:
  - "SYNTH_P18_gaussian_polarity.md"
  - "SYNTH_P20_stratified_parabolic_principle.md"
  - "SYNTH_CONJ_C_continuum_polarity.md"
status: "extracted synthesis"
---

# Polarity and Stratified Maximum Principles: Making Singular Gauge Strata Harmless

## Abstract

Gauge orbit spaces are not manifolds globally; they are **stratified spaces** with singular strata (reducible connections, Gribov-type issues, etc.). Many analytic arguments (maximum principles, PDE comparison, stochastic representations) break when trajectories can “hit” singularities.

The project’s proposed fix is to show the singular strata are **polar** (capacity zero) for the relevant diffusion/Dirichlet-form structure. Then:

- the associated stochastic process almost surely never reaches the singular set,
- no boundary conditions are needed there,
- standard parabolic comparison arguments apply on the regular stratum as if it were a manifold.

This is a powerful idea because it lets the PBH/Riccati mechanism ignore the worst geometric pathology, *provided polarity can be transferred from a Gaussian reference measure to the Yang–Mills measure.*

---

## 1. Capacity and polar sets (why “measure zero” is not enough)

For diffusion processes, “measure zero” does not guarantee avoidance: Brownian motion in \(\mathbb{R}^2\) hits points with positive probability even though points have Lebesgue measure zero.

The right notion is **capacity** (in Dirichlet form theory). A set \(\Sigma\) is **polar** if
\[
\mathrm{Cap}_\mu(\Sigma)=0,
\]
which implies the diffusion associated to the Dirichlet form avoids \(\Sigma\) almost surely.

---

## 2. Infinite-codimension heuristic → polarity (Gaussian reference)

The project proves a key geometric lemma in a Sobolev setup:

> Reducible connections form a subset with **infinite codimension** in the affine Sobolev space of connections.

Mechanism (as used in the project’s argument):

1. A reducible connection admits a nonzero covariantly constant adjoint field \(\xi\).
2. Linearizing the reducibility condition gives a commutator map
   \[
   T_\xi(a) = [a,\xi]
   \]
   between Sobolev spaces.
3. By choosing infinitely many disjoint supports, one constructs infinitely many orthogonal images \(T_\xi(\alpha_n\otimes Y)\), proving \(\mathrm{ran}(T_\xi)\) is infinite dimensional, so the kernel has infinite codimension.

Then the project invokes an infinite-dimensional analogue of the finite-dimensional fact:
> Brownian motion avoids sets of codimension \(\ge 3\).

In an Ornstein–Uhlenbeck / Gaussian Dirichlet form setting, affine subspaces of infinite codimension are expected to be polar. The project uses this as the foundation for:

\[
\mathrm{Cap}_{\mu_0}(\Sigma)=0
\quad\text{for a Gaussian reference measure }\mu_0.
\]

---

## 3. The stratified parabolic comparison principle (core “engine lemma”)

Let \(\mathcal{M}_{\mathrm{reg}}\) be the regular stratum and \(\Sigma\) the singular set with \(\mathrm{Cap}_\mu(\Sigma)=0\).

For a supersolution on \(\mathcal{M}_{\mathrm{reg}}\):
\[
\partial_t u \ge L u + F(u),
\quad F \text{ nondecreasing},
\]
the project asserts a stratified maximum principle:

> If \(u(0,\cdot)\ge 0\) then \(u(t,\cdot)\ge 0\) for all \(t>0\).

Proof idea (project’s strategy):

- Use a stochastic representation (Feynman–Kac / diffusion semigroup).
- By polarity, the diffusion never hits \(\Sigma\), so the process stays on \(\mathcal{M}_{\mathrm{reg}}\).
- Apply the standard smooth-manifold comparison principle along trajectories.

This is the missing analytic “bridge” that allows PBH flow (EXTRACT 02) to survive the presence of gauge singularities.

---

## 4. The bottleneck: transferring polarity to the Yang–Mills measure (Conjecture C)

The project labels the key missing step as a continuum transfer conjecture:

> If \(\Sigma\) is polar for a Gaussian reference measure \(\mu_0\), then \(\Sigma\) remains polar for the Yang–Mills measure \(\mu_{\mathrm{YM}}\).

A plausible sufficient condition is some form of absolute continuity:
\[
\mu_{\mathrm{YM}} \ll \mu_0
\quad\text{with enough control on densities to preserve capacity-zero sets.}
\]

This is nontrivial: capacities depend on the Dirichlet form, not only on the measure as a set function.

---

## 5. Why this matters beyond Yang–Mills

If correct, this polarity/stratification move is a reusable technique for:

- nonlinear sigma models on orbit spaces,
- gauge theories with more complicated moduli-space singularities,
- stochastic quantization on stratified targets.

It suggests a general template:

> **Singularities are tolerable if they are polar for the dynamics you use.**  
> Then PDE/semigroup methods can proceed on the regular stratum without imposing ad hoc boundary data on singular loci.

---

## 6. Concrete further work (what would make this rigorous)

1. **State the Dirichlet form precisely** on \(\mathcal{M}\) and its closure on \(\mathcal{M}_{\mathrm{reg}}\).
2. **Prove polarity for the Gaussian reference** with a publishable level of detail (identify the exact OU process and capacity notion).
3. **Prove a capacity comparison theorem** under perturbations of the Dirichlet form and density changes (this is the technical heart of Conjecture C).
4. **Demonstrate the stratified maximum principle** in the chosen analytic setting (weak solutions, quasi-continuous representatives, etc.).

