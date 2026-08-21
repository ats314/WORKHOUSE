# Polarity of Reducibles and a Stratified Parabolic Maximum Principle

**Purpose.** This note extracts a second core idea with “new-theory potential”:  
use **polarity/capacity-zero** of the *reducible/singular strata* in gauge orbit space to justify a **parabolic maximum principle** on a stratified quotient.

This is the technical escape hatch that lets the PBH/Riccati mechanism (see `EXTRACT_PBH_Riccati_Mass_Gap.md`) survive the fact that \(\mathcal{A}/\mathcal{G}\) is not a smooth manifold everywhere.

Primary sources in this project: `SYNTH_P18_gaussian_polarity.md` and `SYNTH_P20_stratified_parabolic_principle.md` (with lattice-level intuition also present in `SYNTH_P01_lattice_polarity.md`).

---

## 1. Why reducibles are a problem

Gauge orbit spaces \(\mathcal{A}/\mathcal{G}\) are **stratified**:
- a dense *regular stratum* of irreducible connections, where the gauge stabilizer is minimal;
- lower-dimensional strata of *reducibles*, where stabilizers are larger and the quotient develops singularities.

Analytically:
- PDEs on \(\mathcal{M}_{\mathrm{reg}}\) can break down at the singular set \(\Sigma\).
- Maximum principles and comparison arguments typically require either a boundary condition on \(\Sigma\) or a way to ignore \(\Sigma\).

The project’s key move is: **ignore \(\Sigma\)** because it is *polar* (capacity zero), so the diffusion underlying the PDE almost surely never hits it.

---

## 2. Polarity in one sentence (and why it’s perfect here)

Let \((\mathcal{E},\mathcal{D}(\mathcal{E}))\) be a Dirichlet form with associated diffusion process \(X_t\).  
A set \(\Sigma\) is **polar** if
\[
\mathbb{P}_x\big(\exists t\ge 0:\ X_t\in \Sigma\big)=0
\quad\text{for quasi-every }x.
\]
In many settings this is equivalent to \(\mathrm{Cap}(\Sigma)=0\).

**Translation.** If \(\Sigma\) is polar, stochastic trajectories “don’t see it.”  
So a PDE driven by that diffusion can often be treated as if \(\Sigma\) were absent.

---

## 3. Why reducibles should be polar (continuum heuristic)

### 3.1 Reducibles as infinite-codimension constraints

In Sobolev completions \(A\in H^s\) of gauge potentials, “being reducible” means:  
there exists a nontrivial Lie algebra element \(\phi\) such that
\[
d_A\phi = 0
\quad\text{(covariantly constant section)}.
\]
At the linear level, this imposes infinitely many independent constraints on \(A\).  
That is the origin of “infinite codimension.”

The project’s continuum polarity argument (P18) can be summarized as:

1. Define the bilinear bracket map (schematic)
\[
B(A,\phi) := [A,\phi].
\]
2. For generic \(A\), the image of \(B(A,\cdot)\) is “large.”  
3. Reducibles correspond to the failure of this largeness: \(A\) commutes with a nontrivial stabilizer direction \(\phi\).  
4. The set of such \(A\) is cut out by infinitely many independent linear functionals \(\Rightarrow\) an infinite-codimension set.

### 3.2 Gaussian polarity principle

A robust (though technical) statement from infinite-dimensional potential theory is:

> Closed affine subspaces of **infinite codimension** in a separable Hilbert space are polar for the Ornstein–Uhlenbeck (Gaussian) Dirichlet form.

This is one reason the project emphasizes **Gaussian polarity**: it is a relatively tractable polarity theorem in infinite dimensions.

**Important caveat.**  
The Yang–Mills measure is not Gaussian. The strategy is to:
- use a *Gaussian-dominated* regime (UV / asymptotically free scaling),
- or show absolute continuity / domination of the YM measure w.r.t. a Gaussian reference measure in the Sobolev topology of interest.

That domination is where the real technical grind lives.

---

## 4. Lattice intuition: codimension explosion

On a finite lattice, the configuration space is finite-dimensional \(G^{E}\).  
Reducibles correspond to configurations with larger stabilizers; these live in subvarieties of high codimension (the project claims codimension grows proportionally with number of bonds/links).

Even if the exact capacity threshold is delicate in low dimensions, the “codimension explosion” in large-dimensional configuration spaces makes the polarity intuition compelling: in huge dimension, most thin submanifolds are negligible for diffusion.

(If you want the polished finite-dimensional version, you’d want an explicit theorem of the form:  
smooth submanifold of dimension \(\le n-2\) has zero capacity for the Laplace Dirichlet form in dimension \(n\).)

---

## 5. Stratified parabolic maximum principle (the extracted gem)

The project’s stratified principle (P20) is, conceptually:

> If \(\Sigma\) is polar, then parabolic comparison on \(\mathcal{M}_{\mathrm{reg}}\) works “as if” the PDE were posed on a smooth manifold without boundary.

A typical statement (schematic) is:

Let \(u(t,x)\) be a bounded upper-semicontinuous function on \([0,T]\times\mathcal{M}\) such that:
- on \(\mathcal{M}_{\mathrm{reg}}\), \(u\) satisfies
  \[
  \partial_t u \le \Delta u + F(u)
  \]
  in the viscosity (or weak) sense;
- \(\Sigma=\mathcal{M}\setminus\mathcal{M}_{\mathrm{reg}}\) is polar for the diffusion generated by \(\Delta\).

Then the usual maximum principle bound holds:
\[
\sup_{x\in\mathcal{M}} u(t,x)
\le
\psi(t)
\]
where \(\psi\) solves the ODE \(\psi' = F(\psi)\) with \(\psi(0)=\sup u(0,\cdot)\).

### 5.1 Why polarity is exactly the right hypothesis

A probabilistic way to see it:

- On a smooth manifold, solutions of \(\partial_t u = \Delta u\) admit a representation
  \[
  u(t,x) = \mathbb{E}_x\big[u(0,X_t)\big].
  \]
- If \(X_t\) almost surely never hits \(\Sigma\), then the representation never samples boundary values on \(\Sigma\).
- Thus \(\Sigma\) behaves like a “removable” singular set for the parabolic problem.

---

## 6. How this plugs into PBH/Riccati

In the PBH mechanism, one needs a comparison principle for the minimal eigenvalue function \(\lambda_{\min}(t,x)\), which is defined on the regular stratum but may misbehave near reducibles.

The stratified principle supplies the missing logical step:

- derive the differential inequality for \(\lambda_{\min}\) on \(\mathcal{M}_{\mathrm{reg}}\),
- then propagate the inequality globally in time without imposing boundary conditions at \(\Sigma\),
- because \(\Sigma\) is polar.

This is precisely the kind of move that can turn “nice heuristic” into “actual theorem,” provided the polarity input is proven in the correct measure/Dirichlet-form setting.

---

## 7. What further work would make this bulletproof

1. **Identify the correct diffusion/Dirichlet form** associated to the PBH/vHJ operator on orbit space (not merely the Laplace–Beltrami form).
2. **Prove polarity of reducibles for that Dirichlet form**, not just for a Gaussian reference process.
3. **Prove quasi-continuity** and a usable capacity theory on the stratified orbit space (or work with a desingularization/local charts + removable singularities).
4. **Local-to-global control**: show the RG/PBH trajectory remains in a regime where the polarity comparison applies (e.g., away from orbit singularities in a quantitative way).

If those are achieved, the polarity/stratified principle becomes a powerful general tool: it would apply not just to Yang–Mills PBH flow, but to many PDEs on stratified moduli spaces in gauge theory.
