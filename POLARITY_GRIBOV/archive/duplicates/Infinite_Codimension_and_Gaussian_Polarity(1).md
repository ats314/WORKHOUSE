# Infinite codimension of reducibles and Gaussian polarity

**Scope.** This document extracts the (largely self-contained) analytic core behind “polarity of the reducible stratum” in a Sobolev configuration space: the reducible set is constrained by infinitely many independent linear conditions, hence has infinite codimension, and is therefore a natural candidate for being polar (capacity zero) under Gaussian/OU Dirichlet forms.

**Primary source.**
- `SYNTH_P18_gaussian_polarity.md` (detailed analysis, including explicit “infinite rank” arguments).

---

## Setup: Sobolev configuration space and reducibles

Let \(\mathcal A\) denote a Sobolev space of connections on a principal \(G\)-bundle over a compact base (the source treats the abstract Sobolev setup; the precise base manifold is not essential for the extracted argument).

A connection \(A\in\mathcal A\) is **reducible** if there exists a nonzero \(\xi\) in an appropriate Sobolev space of adjoint-bundle sections such that
\[
D_A \xi = 0,
\]
i.e. \(\xi\) is covariantly constant with respect to \(A\).

Define the “reducible stratum”
\[
\Sigma \;:=\;\{A\in\mathcal A:\exists\,\xi\neq 0\text{ with }D_A\xi=0\}.
\]

For a fixed nonzero \(\xi\), define
\[
\Sigma_\xi \;:=\;\{A\in\mathcal A:\;D_A\xi=0\}.
\]

---

## The infinite codimension theorem

### Theorem (Infinite codimension of \(\Sigma_\xi\))

Fix \(\xi\neq 0\). Assume \(\xi\) has Sobolev regularity high enough to admit a continuous representative (e.g. \(k>2\) in dimension four, as in the source). Then \(\Sigma_\xi\) is contained in an affine subspace cut out by **infinitely many independent linear constraints**; in particular, it has infinite codimension in \(\mathcal A\).

### Proof (extracted core)

Write \(A=A_0+a\) with \(a\) in the model Hilbert space \(H\) of Sobolev one-forms. The covariant derivative is affine-linear in \(a\), so
\[
D_A\xi = D_{A_0}\xi + [a,\xi],
\]
and the constraint \(D_A\xi=0\) becomes a linear condition on \(a\):
\[
[a,\xi] = -D_{A_0}\xi.
\]

The source’s key device is to turn this into *infinitely many independent constraints* by point evaluations:

1. Since \(\xi\not\equiv 0\) and is continuous, there is an open set where \(\xi(x)\neq 0\).

2. Choose a countable family of disjoint balls \(B_n\) contained in that set, and choose points \(x_n\in B_n\).

3. For each \(n\), consider the linear functional on \(a\) given by evaluating \(a(x_n)\) (in a fixed trivialization) and projecting onto the \(\xi(x_n)\)-commutator directions. Concretely, for each \(n\) define a linear map
\[
T_n:H\to\mathfrak g,\qquad T_n(a)= [a(x_n),\,\xi(x_n)].
\]

4. The constraint \([a,\xi]= -D_{A_0}\xi\) forces
\[
T_n(a)=b_n
\]
for an associated right-hand side \(b_n\) determined by \(-D_{A_0}\xi(x_n)\).

5. Because the \(x_n\) are separated and \(\xi(x_n)\neq 0\), the maps \(T_n\) yield infinitely many independent conditions: one can vary \(a\) supported near \(x_n\) to change \(T_n(a)\) without affecting \(T_m(a)\) for \(m\neq n\).

Thus the total constraint map
\[
T=(T_1,T_2,\dots):H\to\mathfrak g^{\mathbb N}
\]
has infinite rank, and \(\Sigma_\xi\subset\{a:\;T(a)=b\}\) is (contained in) an affine subspace of infinite codimension.

\(\square\)

---

## Gaussian polarity target statement

A second extracted goal is to interpret the infinite-codimension property probabilistically.

### Target theorem (Gaussian polarity for \(\Sigma\), as stated in the source)

Let \(\mu_0\) be a Gaussian reference measure on \(\mathcal A\) (with the associated Ornstein–Uhlenbeck Dirichlet form). Then \(\Sigma\) has capacity zero:
\[
\mathrm{Cap}_{\mu_0}(\Sigma)=0.
\]

### Extracted status logic

The source cleanly reduces the polarity claim to:

- For each fixed \(\xi\), the set \(\Sigma_\xi\) is (contained in) an affine subspace of infinite codimension; such sets are natural candidates to be polar under Gaussian/OU capacity.
- To conclude polarity for \(\Sigma=\bigcup_{\xi\neq 0}\Sigma_\xi\), one needs a **countable reduction** (e.g. a countable dense family of \(\xi\)’s in a suitable topology together with a stability argument), because capacity is only countably subadditive.

This highlights the “missing bridge” needed to turn the geometric infinite-codimension theorem into a full polarity theorem for the union \(\Sigma\).

---

## Why this is “interesting physics/mathematics”

- Reducible connections are exactly the loci where gauge symmetry is “larger than generic” (stabilizers are nontrivial). If that locus is polar, it becomes *invisible* to the Dirichlet-form geometry governing stochastic quantization/functional inequalities.
- The extracted infinite-codimension mechanism is robust: it uses only (i) continuity of \(\xi\), and (ii) locality via disjoint supports.

---

## Immediate next steps suggested by the extracted corpus

1. **Countable reduction lemma.** Give a precise method to cover \(\Sigma\) by a countable union of \(\Sigma_{\xi_n}\) (or of slightly thickened sets whose capacities are summable).

2. **Capacity estimate for an infinite-codimension affine set.** Provide (or cite) a theorem: “affine subspace of infinite codimension is OU-polar”.

3. **Measure-change stability.** The program later needs polarity to persist under changing from \(\mu_0\) (Gaussian) to \(\mu\) (Yang–Mills), which suggests Mosco convergence / capacity stability as an interface.
