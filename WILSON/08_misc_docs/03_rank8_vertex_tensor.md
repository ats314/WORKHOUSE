# Rank-8 vertex tensors for 4D $SU(2)$ models from fusion trees and quantum $6j$ symbols

**Source notebooks:** `SU2_4D_Rank8_FINAL.ipynb`, `SU2_4D_PHASE2_FIXED.ipynb`

## 1. Motivation: why a rank-8 object appears in 4D

On a 4D hypercubic lattice, a site (vertex) has 8 incident oriented links:
\[
(\pm \hat x,\ \pm \hat y,\ \pm \hat z,\ \pm \hat t).
\]

A tensor-network representation of the partition function typically assigns:

- indices (degrees of freedom) to links (or dual objects),
- local tensors at vertices/plaquettes enforcing constraints and encoding weights,
- global contraction producing $Z$.

If link indices are representation labels (spins $j$), then the vertex tensor is naturally **8-valent**.

The project builds such an 8-valent tensor using quantum-group recoupling data, i.e. $q$-dimensions and $q$-$6j$ symbols.

---

## 2. The fusion-tree construction used in the notebooks

A generic 8-valent intertwiner space is large. A common computational trick is to choose a **fusion tree** (a binary bracketing) and express the vertex amplitude as a sum over internal fusion channels.

The implemented ansatz takes a particularly simple fusion tree: split the 8 legs into two groups of four and couple each group through a shared internal spin $k$.

Let the eight external spins be
\[
(j_1,j_2,j_3,j_4,j_5,j_6,j_7,j_8),
\]
and let $w(j)$ be a per-leg weight (taken to be the quantum dimension in the notebooks):
\[
w(j)=d_j^{(q)}=[2j+1]_q.
\]

Then the rank-8 tensor element is constructed schematically as
\[
T_{j_1\ldots j_8}
=
\Bigl(\prod_{a=1}^{8} w(j_a)\Bigr)
\sum_{k\in\mathcal{J}}
w(k)\,
\begin{Bmatrix}
j_1 & j_2 & k\\
j_3 & j_4 & k
\end{Bmatrix}_q
\begin{Bmatrix}
j_5 & j_6 & k\\
j_7 & j_8 & k
\end{Bmatrix}_q,
\]
with $\mathcal{J}$ the set of allowed internal spins (truncated by $j_{\max}$).

### Selection rules

The $6j$ factors automatically enforce triangle constraints, so many tensor entries vanish. In practice this sparsity is crucial.

---

## 3. Why this looks like “local categorical data”

In representation-category language, $6j$ symbols encode associativity (the $F$-move). A tensor element constructed as a product of $6j$’s and quantum dimensions is exactly the sort of building block one sees in:

- spin network evaluations,
- state-sum / TQFT partition functions,
- tensor-network models built from fusion categories.

The project’s distinctive move is to use **$q=e^{i\theta}$**, so that the same local tensor becomes a *$\theta$-dependent* tensor.

That shifts the burden of $\theta$-physics from “global topological sector sums” to “local deformation of fusion data.”

---

## 4. Practical notes from the implementation

### 4.1 Caching and canonical ordering

Because many permutations of $(j_1,\dots,j_6)$ correspond to the same $6j$ symbol up to symmetry, the code uses canonical ordering and memoization.

This is essential: without caching, rank-8 tensor construction becomes prohibitively expensive even for modest $j_{\max}$.

### 4.2 Normalization

After filling $T$, the code normalizes by the maximum absolute entry:
\[
T \leftarrow \frac{T}{\max |T|},
\]
and accumulates the logarithm of the normalization factor to reconstruct $\log Z$ later during HOTRG steps.

This is a standard stabilization trick in tensor contractions.

---

## 5. What’s “novel-potential” here

The fusion-tree formula above is not new by itself. The potentially new ingredient is conceptual:

> Use $U_q(\mathfrak{su}(2))$ recoupling data at $q=e^{i\theta}$ as a *local surrogate* for a $\theta$-term.

If correct (or correct in a controlled limit), this gives a clean pathway to sign-problem-free $\theta$ physics with tensor networks.

If not equivalent to Yang–Mills, it is still a concrete and computable family of $4$D state-sum models parameterized by $\theta$.

---

## 6. Next steps for strengthening the construction

1. **Tree-independence test:** Change the fusion tree (different bracketing of 8 legs) and check whether $Z(\theta)$ is invariant. True invariance would indicate coherent categorical data; failure would mean the ansatz depends on an arbitrary choice.

2. **Include additional local structure:** Standard lattice gauge theory has plaquette weights depending on the coupling. A more faithful model would include those weights in addition to (or instead of) pure quantum-dimension weights.

3. **Gauge invariance constraints:** Explicitly encode and verify local gauge constraints, not just triangle constraints.

