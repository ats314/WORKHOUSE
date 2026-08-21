# Polarity of reducible strata: capacity-zero singular sets do not spoil gaps

## 0. Why polarity matters here

In gauge theories, the orbit space \(\mathcal{A}/\mathcal{G}\) is stratified; “reducible” configurations have larger stabilizers, and these strata are where Faddeev–Popov determinants vanish and Gribov talk begins.

From the viewpoint of **Dirichlet-form analysis**, the right notion of “negligible” is not merely measure zero, but **capacity zero**. Capacity-zero sets are *polar*: the associated diffusion almost surely never hits them, and functional inequalities (LSI/Poincaré) are insensitive to modifications on them.

This appendix isolates the clean statement needed by the curvature–gap program:

> Reducible strata are polar for the relevant Gaussian/lattice Dirichlet forms, and this property is stable under bounded-density perturbations.

---

## 1. Capacity and polar sets (Dirichlet forms)

Let \((E,\mu)\) be a measure space and \((\mathcal{E},\mathcal{D}(\mathcal{E}))\) a symmetric Dirichlet form on \(L^2(\mu)\). For an open set \(U\subset E\), define
\[
\mathrm{Cap}(U):=\inf\{\,\mathcal{E}(u,u)+\|u\|_{L^2(\mu)}^2:\ u\in\mathcal{D}(\mathcal{E}),\ u\ge 1\ \mu\text{-a.e. on }U\,\}.
\]
For a Borel set \(A\),
\(
\mathrm{Cap}(A):=\inf\{\mathrm{Cap}(U): A\subset U,\ U\text{ open}\}.
\)
A set \(A\) is **polar** if \(\mathrm{Cap}(A)=0\).

For diffusions with continuous paths associated to \((\mathcal{E},\mathcal{D}(\mathcal{E}))\), a polar set is hit with probability zero from \(\mu\)-a.e. starting point.

---

## 2. Gaussian (continuum-inspired) setting: reducibles are infinite-codimension

Let \(H\) be a separable Hilbert space of fields (a stand-in for connections in a fixed gauge) equipped with a Gaussian measure \(\gamma\) and the canonical Gaussian Dirichlet form
\[
\mathcal{E}(f,f)=\int\|\nabla f\|^2\,d\gamma.
\]
A typical reducibility condition has the form
\[
D_A\xi=0\quad\text{for some }\xi\neq 0,
\]
i.e. the existence of a nontrivial covariantly constant direction.

Heuristically (and in many concrete models), fixing \(\xi\neq 0\) makes \(A\) satisfy an **infinite set of independent linear constraints**, so the solution set \(\Sigma_\xi\) lies in an affine subspace of **infinite codimension**. Gaussian potential theory implies such sets have Gaussian capacity zero; hence their union over a countable family of \(\xi\)’s is polar.

**Takeaway:** reducibles are invisible to the Gaussian Dirichlet form.

---

## 3. Lattice setting: reducibles form a positive-codimension subvariety

On a finite lattice with bond set \(\mathcal{B}\), the configuration space is a compact manifold
\[
\mathcal{A}_\Lambda = G^{\mathcal{B}},\qquad G=SU(N),
\]
with product Haar measure. Reducible configurations can be characterized as those for which, after a gauge transform, all links commute with some non-central element. Concretely this yields polynomial matrix relations
\[
[U_b,P]=0\quad\text{for all }b\in\mathcal{B}
\]
for some nontrivial projector \(P\), showing the reducible set is a finite/countable union of lower-dimensional submanifolds (an algebraic subvariety) of **positive codimension**.

For standard elliptic diffusions on manifolds (e.g. lattice Langevin dynamics)
\[
L=\Delta_{G^{\mathcal{B}}}-\nabla S\cdot\nabla,
\]
submanifolds of sufficiently high codimension are polar. In this lattice context, reducibles are therefore polar for the associated Dirichlet forms.

---

## 4. Stability under bounded-density perturbations

The curvature–gap program often changes measures by multiplying by a Gibbs density \(e^{-S}\). If
\[
\frac{d\mu}{d\mu_0}\in L^\infty(\mu_0),
\]
then capacities and polar sets are stable under this perturbation (up to constants). In practice this means:

- if reducibles are polar for a convenient reference measure \(\mu_0\) (Gaussian or Haar),
- and the interacting measure \(\mu\) is a bounded-density perturbation of \(\mu_0\) on the region of interest,

then reducibles remain polar for \(\mu\).

This is exactly the kind of “singular strata do not matter” lemma needed to keep functional inequalities from being sabotaged by gauge-quotient singularities.

---

## 5. What this buys for the mass-gap program

In the curvature pipeline, one needs Poincaré/LSI for the Gibbs measure and wants to interpret it physically via OS reconstruction. Polarity lets you say:

- work on the irreducible stratum (where the geometry is smooth),
- prove inequalities there,
- extend them to the full space because capacity-zero sets don’t contribute.

It does *not* prove YM; it removes one of the classic “but what about Gribov?” analytic tripwires.
