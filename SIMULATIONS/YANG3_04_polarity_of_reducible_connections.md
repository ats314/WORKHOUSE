# Polarity of Reducible Connections via Gaussian Capacity Comparison

## Abstract

Gauge theories have a notorious analytic nuisance: the configuration space modulo gauge has singular strata (reducible connections), and gauge-fixing can introduce degeneracies. The YANG 3 proof stack develops a clean workaround:

1. Model the (gauge-fixed) configuration space locally as an infinite-dimensional linear space equipped with a Gaussian reference measure.
2. Use known results: **countable unions of infinite-codimension affine subspaces are polar** (capacity zero) for Gaussian Dirichlet forms.
3. Transfer polarity from the Gaussian reference to the interacting measure (e.g. Yang–Mills-type Gibbs measures) via **capacity comparison** under absolute continuity.

The conclusion is that reducible strata can be ignored **quasi-surely** for the functional inequality arguments (LSI/Poincaré), allowing one to work on the smooth stratum without being derailed by gauge singularities.

---

## 1. Capacity and polarity (Dirichlet-form language)

Let \((\mathcal{E},\mathcal{D}(\mathcal{E}))\) be a Dirichlet form on a probability space \((X,\mu)\). The (1-)capacity of a set \(E\subset X\) is
\[
\mathrm{Cap}_\mu(E)
= \inf \left\{ \mathcal{E}(u,u)+\|u\|_{L^2(\mu)}^2 : u\in \mathcal{D}(\mathcal{E}),\ u\ge 1\ \mu\text{-a.e. on }E\right\}.
\]

A set is **polar** if it has capacity zero:
\[
\mathrm{Cap}_\mu(E)=0.
\]
Polar sets are negligible for quasi-sure statements: diffusion processes associated to \(\mathcal{E}\) avoid them with probability 1.

---

## 2. Gaussian polarity results (infinite codimension \(\Rightarrow\) capacity zero)

Let \(\gamma\) be a nondegenerate Gaussian measure on a separable Banach/Hilbert space \(H\), with associated Ornstein–Uhlenbeck Dirichlet form \(\mathcal{E}_\gamma\).

Classical results (Feyel–Pradelle, Kusuoka–Stroock) show:

- If \(E\) is contained in a countable union of affine subspaces of **infinite codimension**, then
  \[
  \mathrm{Cap}_\gamma(E)=0.
  \]

Intuition: infinite codimension is “smaller than measure zero” in a diffusion sense; the OU process almost surely never hits it.

---

## 3. Capacity comparison (transfer polarity to interacting measures)

Let \(\mu\) be an interacting measure absolutely continuous with respect to \(\gamma\):
\[
d\mu = f\, d\gamma.
\]

Under boundedness/integrability conditions on \(f\) (and in many cases using log–Sobolev or sector-condition controls), one has capacity comparison inequalities of the form
\[
\mathrm{Cap}_\mu(E)\le C\, \mathrm{Cap}_\gamma(E).
\]

Hence \(\mathrm{Cap}_\gamma(E)=0\Rightarrow \mathrm{Cap}_\mu(E)=0\): polarity transfers.

This is the key step that makes the reducible-set removal robust: it is not tied to the free Gaussian measure alone.

---

## 4. Application: reducible connections are polar

In gauge theory, a connection is reducible if its stabilizer under the gauge group is larger than the center. In local linearized coordinates, reducibility implies the field takes values in a **proper Lie subalgebra** after gauge transformation. In the continuum/infinite-dimensional limit, the set of such fields is modeled as a countable union of affine subspaces of infinite codimension.

Therefore, for the Gaussian reference \(\gamma\),
\[
\mathrm{Cap}_\gamma(\Sigma_{\mathrm{red}})=0,
\]
and by capacity comparison,
\[
\boxed{
\mathrm{Cap}_\mu(\Sigma_{\mathrm{red}})=0.
}
\]

Interpretation:

- Reducible strata are negligible for quasi-sure analytic statements.
- Functional inequalities (Poincaré/LSI) can be developed on the smooth stratum without “blowing up” on reducibles.

---

## 5. Why this matters for the mass-gap program

The curvature-based program seeks:

- a uniform Bakry–Émery lower bound for an effective action,
- leading to an LSI and a spectral gap.

Gauge singularities could, in principle, ruin such an argument if they carried non-negligible capacity. Polarity avoids this: you can discard reducibles without changing the diffusion’s spectral properties in the relevant sense.

---

## Further work

1. Identify the **minimal hypotheses** on the interacting density \(f\) required for the capacity comparison in the Yang–Mills lattice-to-continuum scaling.
2. Strengthen the geometric description of reducible strata in the chosen coordinate charts to justify the “infinite codimension union of affine subspaces” structure rigorously.
3. Connect polarity to practical gauge-fixing choices (e.g., Landau gauge) to ensure numerical/analytic treatments are aligned.

