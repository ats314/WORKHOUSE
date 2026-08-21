# C. Gaussian Polarity, Capacity Comparison, and the “Gribov/Reducible Sets are Negligible” Strategy

This is one of the cleaner “salvage” ideas in the project:

> Treat gauge-singular or reducible strata (Gribov horizons, reducible connections) as **capacity-zero / polar sets**, so they do not affect Dirichlet forms, functional inequalities, or spectral gaps.

The idea is not that these sets do not exist, but that (in the right analytic sense) they are “too thin” to matter.

---

## C1. What “polar / capacity-zero” means (finite-dimensional intuition)

For a diffusion process \(X_t\) (e.g. Brownian motion or Ornstein–Uhlenbeck),
a set \(E\) is **polar** if \(X_t\) almost surely never hits \(E\) starting from a typical point.

In Dirichlet form language, polarity is controlled by (Newtonian) capacity:
\[
\mathrm{Cap}(E)=0 \quad\Rightarrow\quad E\ \text{is polar}.
\]

For Gaussian measures and OU processes, there are classical criteria:
- sets of codimension \(\ge 2\) behave “like polar” for Brownian/OU,
- “thin” stratified subsets can have capacity zero even if they are not measure-zero in a naive sense.

---

## C2. Why reducible strata plausibly become polar (project argument)

Reducible connections are those with stabilizer larger than the center.  
In configuration-space terms, reducibility imposes constraints that look like:

- “connection lies in a proper subalgebra along some direction”, or
- “holonomy commutes with a nontrivial subgroup”.

Heuristically, these are high-codimension algebraic conditions.  
The project’s Gaussian argument (infinite-dimensional flavor) is:

1. A reducible locus behaves like a union of affine subspaces of **large codimension**.
2. Such sets are polar for the OU process under a Gaussian reference measure.
3. If the YM measure is absolutely continuous w.r.t. the Gaussian reference in the relevant regime,
   then capacities are comparable and polarity transfers.

This is compelling as a strategy, but it lives or dies on the comparison step.

---

## C3. Capacity comparison (the key technical hinge)

A typical template:

Let \(\gamma\) be a Gaussian reference measure on a finite-dimensional space, and let
\[
d\mu = Z^{-1} e^{-V}\,d\gamma
\]
with \(V\) sufficiently regular and not too wild.

Then one can often show:
\[
c_1\,\mathrm{Cap}_\gamma(E)\ \le\ \mathrm{Cap}_\mu(E)\ \le\ c_2\,\mathrm{Cap}_\gamma(E),
\]
for constants \(c_1,c_2\) depending on bounds on \(V\), \(\nabla V\), etc.  
So \(\mathrm{Cap}_\gamma(E)=0 \Rightarrow \mathrm{Cap}_\mu(E)=0\).

**In finite volume**, this kind of comparison is plausible under boundedness / local control assumptions.

**In the continuum limit**, the constants can blow up, and comparison becomes much harder.

---

## C4. Why this matters for mass gap technology

Functional inequalities (Poincaré / LSI) are about Dirichlet forms:
\[
\mathcal{E}(f,f) = \int |\nabla f|^2\,d\mu.
\]

If the “bad set” is polar, then:
- it can be ignored in quasi-everywhere statements,
- boundary conditions or singularities there do not change the essential spectrum,
- local arguments can avoid heavy gauge-fixing machinery.

So polarity is a way to *avoid getting trapped in gauge-fixing pathology.*

---

## C5. Status (honest)

- The **Gaussian polarity** statements are standard and robust.
- The interpretation of **reducible/Gribov strata** as “thin enough” is plausible.
- The missing piece is a **tight capacity comparison** that survives
  the YM interactions and (especially) the continuum limit.

This is a high-value direction because it potentially removes an entire cluster of objections with one analytic tool.

---
