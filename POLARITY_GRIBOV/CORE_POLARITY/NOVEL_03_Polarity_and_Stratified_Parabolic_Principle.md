# Polarity and Stratified Parabolic Principles in Gauge Orbit Spaces

## Abstract

Gauge orbit spaces \(\mathcal{M}=\mathcal{A}/\mathcal{G}\) are stratified: the regular stratum is a manifold, while reducible connections form singular strata.
Several core arguments in the project (tensor maximum principles, parabolic comparison for curvature) are formulated on \(\mathcal{M}_{\mathrm{reg}}\) and require control at the singular set.

A central structural idea in the corpus is:

> If the reducible set \(\Sigma\) is **polar** (capacity zero) for the relevant Dirichlet form, then parabolic comparison on \(\mathcal{M}_{\mathrm{reg}}\) behaves as if \(\Sigma\) were absent.

This document isolates that mechanism.

---

## 1. Capacity and polarity (Dirichlet-form viewpoint)

Let \((M,\mu)\) be a measure space carrying a strongly local Dirichlet form \(\mathcal{E}\) with domain \(\mathsf{D}(\mathcal{E})\subset L^2(\mu)\).
For a Borel set \(E\subset M\), the \(\mathcal{E}\)-capacity is
\[
\mathrm{Cap}_\mu(E)
:=\inf\Bigl\{\mathcal{E}(u,u)+\|u\|_{L^2(\mu)}^2:\ u\in\mathsf{D}(\mathcal{E}),\ u\ge 1\ \mu\text{-a.e. on a nbd of }E\Bigr\}.
\]
A set is **polar** if \(\mathrm{Cap}_\mu(E)=0\).

Polarity is the correct “smallness notion” for diffusions and maximum principles: polar sets are invisible to the diffusion associated to \(\mathcal{E}\).

---

## 2. Reducible strata as infinite-codimension constraints (continuum Gaussian reference)

The corpus proposes a continuum mechanism:

- reducibility is characterized by existence of a nonzero covariantly constant \(\xi\) (stabilizer field),
- the linear constraint map \(T_\xi(a)=[a,\xi]\) has infinite-dimensional range,
- therefore the reducible tangent space is of **infinite codimension**.

From this, the corpus asserts:

> For a Gaussian reference measure \(\mu_0\) (e.g. Ornstein–Uhlenbeck on a Sobolev space), a union of infinite-codimension affine subspaces is polar.

This is used as the “Gaussian polarity” input.

**Status within the corpus:** the infinite-codimension computation is stated; the polarity implication relies on an external abstract-Wiener-space capacity fact.

---

## 3. Lattice reducibles as algebraic varieties (finite-dimensional proxy)

On a finite lattice, the configuration space is compact finite-dimensional:
\[
\mathcal{C} = SU(N)^{|B(\Lambda)|}.
\]
Reducibility can be expressed as an algebraic constraint (existence of a covariantly constant adjoint field), so \(\Sigma\subset\mathcal{C}\) is a real algebraic variety.

The corpus then claims polarity from “positive codimension”.
That implication is **not correct in that generality** for Sobolev/Dirichlet capacities: codimension \(1\) submanifolds are typically nonpolar.

**What survives:**
The *strategy* is sound if strengthened to a correct capacity criterion:
a sufficient condition is that \(\Sigma\) have Sobolev \(W^{1,2}\)-capacity zero, which holds for sufficiently small Hausdorff dimension (e.g. dimension \(<\dim\mathcal{C}-2\) in Euclidean analogues).
Because the lattice configuration space dimension scales like \((N^2-1)|B(\Lambda)|\), a high-codimension \(\Sigma\) is plausibly polar once a correct criterion is invoked.

**Status within the corpus:** algebraic structure is explicit; the step “codim\(\ge 1\)\(\Rightarrow\) polar” must be repaired.

---

## 4. Stratified parabolic comparison (the “singularity removal” mechanism)

The corpus states a parabolic comparison principle on stratified spaces:

Let \(u\) solve (in viscosity/weak sense on \(\mathcal{M}_{\mathrm{reg}}\))
\[
\partial_t u \ge L u + F(u),
\]
and assume the singular set \(\Sigma\) is polar.
Then global lower bounds can be propagated by comparison with an ODE subsolution.

### Bridging Proposition (as used in the project)

Assume:

1. the curvature quantity \(\lambda(t,x)\) satisfies (on \(\mathcal{M}_{\mathrm{reg}}\))
   \[
   \partial_t \lambda \ge L\lambda -2\lambda^2 + \sigma_*,
   \]
2. \(\Sigma\) is polar for the Dirichlet form of \(L\).

Then \(\inf_x\lambda(t,x)\) is bounded below by the solution of the Riccati ODE
\[
\dot\lambda_{\min}=-2\lambda_{\min}^2+\sigma_*.
\]

**Interpretation:** once polarity is established, reducible singularities cannot obstruct the curvature lower bound, and hence cannot obstruct the Riccati fixed-point mechanism.

---

## 5. What appears new (within the corpus)

### Rigidity Mechanism
Polarity is used as an analytic device to **erase singular strata** from parabolic arguments in gauge orbit space.

### Pipeline Architecture
\[
\text{Polarity of }\Sigma\quad+\quad\text{parabolic inequality on }\mathcal{M}_{\mathrm{reg}}
\quad\Longrightarrow\quad\text{global curvature lower bound via ODE}.
\]

This is a nonstandard way to separate “singularity geometry” from “mass gap mechanism”.

---

## 6. Minimal missing lemma to make this operational

A single lemma dominates:

> **Capacity transfer lemma:** show that polarity (capacity zero) for \(\Sigma\) with respect to a Gaussian reference Dirichlet form implies polarity with respect to the interacting (Yang–Mills) Dirichlet form, at least locally or at fixed lattice spacing, with control uniform enough to pass to limits.

Without this, polarity remains a promising but incomplete interface.