---
title: "EXTRACT 04 — Polarity and a Stratified Parabolic Maximum Principle"
date: "2025-12-31"
---

# Executive summary

Gauge theory configuration spaces are not smooth manifolds globally.
After gauge reduction, **reducible configurations** form a singular locus.
Analytic arguments (heat flow, maximum principles, convexity propagation) typically break at such sets.

The SWIM2 archive contains a clever solvent:

1. Show the singular locus is **polar** (capacity zero) for the relevant Dirichlet form.
2. Prove a **stratified parabolic maximum principle** on $M\setminus\Sigma$ that extends across a polar set $\Sigma$.

This is not a mass gap by itself; it is a technical bridge that can let “positivity of a source”
propagate globally even when the space has singular strata.

This extract is based on:

- `SYNTH_P01_lattice_polarity.md`
- `SYNTH_P18_gaussian_polarity.md`
- `SYNTH_P20_stratified_parabolic_principle.md`
- (motivation) the PBH/Riccati flow documents (`SYNTH_P06_*`)

# 1. Polar sets and why they matter

Let $(M,g,\mu)$ be a metric measure space with a Dirichlet form $\mathcal E$.
A set $\Sigma\subset M$ is **polar** if its capacity is zero:
\[
  \mathrm{Cap}(\Sigma)=0.
\]

Intuitively: a polar set is so small that
Sobolev functions (the natural domain of $\mathcal E$) can ignore it.
Analytically, it behaves like “no boundary”.

In gauge theory, the reducible locus can be singular but still polar;
if so, maximum principles and functional inequalities can be run on $M\setminus\Sigma$
and then extended across $\Sigma$.

# 2. Lattice polarity (finite dimensional, but nontrivial)

The archive includes a lattice theorem asserting that, for a finite lattice and compact group,
the reducible set has capacity zero (in the relevant Sobolev/Dirichlet sense).
This is the rigorous “toy model” version of the continuum claim.

# 3. Gaussian polarity (infinite-dimensional heuristic)

A second strand argues polarity of similar “bad sets” under Gaussian/Wiener-type measures,
which is closer in spirit to the continuum Yang–Mills measure construction.

The message is: polarity is plausible beyond the finite-dimensional lattice setting,
but the continuum proof is a separate problem.

# 4. Stratified parabolic maximum principle (core tool)

The archive proves a parabolic maximum principle of the following flavor.

Let $\Sigma\subset M$ be closed with $\mathrm{Cap}(\Sigma)=0$,
and assume $u=u(t,x)$ is sufficiently regular on $(0,T]\times(M\setminus\Sigma)$.

If
\[
  \partial_t u - \Delta u \ \ge\ F(u)
\quad\text{on }(0,T]\times(M\setminus\Sigma),
\]
for a monotone nonlinearity $F$, and if $u(0,\cdot)\ge m$ (or $u(0,\cdot)\ge 0$),
then the lower bound propagates for all $t\in[0,T]$ *without imposing boundary conditions on $\Sigma$*.

The proof strategy is classic maximum principle + barrier functions,
except the barriers are engineered using the capacity-zero property to avoid leakage at $\Sigma$.

# 5. Why this is exciting in the mass gap program

The PBH/Riccati mechanism wants to apply a maximum principle to something like
the smallest eigenvalue $h(t,x)$ of a Hessian evolving under a parabolic operator on configuration space.

In the gauge-reduced setting:

- $x$ lives in a stratified quotient space,
- reducibles $\Sigma$ are exactly where naive PDE tools can fail.

If $\Sigma$ is polar and the stratified parabolic principle applies,
one can (in principle) propagate $h\ge \underline h(t)$ globally,
thus converting a *local* curvature/convexity input into a *global* analytic inequality.

# 6. What remains to be proved / clarified

1. **Continuum polarity of reducibles**  
   The hard leap is to show the reducible locus is polar for the continuum Dirichlet form
   associated with the limiting Yang–Mills measure.

2. **Regularity of the PBH variable**  
   To apply a maximum principle to $h(t,x)$ one needs a notion of weak solution and enough regularity
   (or viscosity structure) compatible with “minimum eigenvalue” nonlinearities.

3. **Compatibility with projection (horizontals)**  
   The horizontal projection itself can become singular near reducibles; the analysis must be robust to that.

If these can be settled, this “polarity + parabolic principle” becomes a powerful general technique:
it is a way to run PDE positivity arguments on spaces with gauge-theoretic singularities.

