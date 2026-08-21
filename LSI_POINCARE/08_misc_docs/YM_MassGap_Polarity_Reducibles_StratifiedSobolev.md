# Polarity of Reducible Connections and Stratified Sobolev Control

> **Purpose.** Extract the polarity/capacity technology the project uses to stop the singular set \(\Sigma\) (reducible connections / non-free gauge orbits) from acting like a boundary for PDE, Dirichlet forms, and stochastic dynamics.

---

## 1. The singular set and why it matters

Let \(\mathcal{A}\) denote a configuration space of connections and \(\mathcal{G}\) the gauge group. The orbit space
\[
\mathcal{M} := \mathcal{A}/\mathcal{G}
\]
is **stratified**. The regular stratum \(\mathcal{M}_{\mathrm{reg}}\) consists of irreducible connections (free gauge action), while the singular set \(\Sigma\) corresponds to reducible connections.

The main technical worry is that PDE estimates (maximum principles, integration by parts, elliptic regularity) on \(\mathcal{M}_{\mathrm{reg}}\) could fail because \(\Sigma\) behaves like an irregular boundary.

---

## 2. Capacity and polarity

Fix a probability measure \(\mu\) on \(\mathcal{M}\) and a Dirichlet form \(\mathcal{E}\) (typically the one associated with the Langevin generator).

For a set \(E\subset \mathcal{M}\), the \(W^{1,2}\)-capacity can be defined (heuristically) by
\[
\mathrm{Cap}_\mu(E)
:= \inf\Big\{\mathcal{E}(u,u) + \|u\|_{L^2(\mu)}^2 \;:\; u\ge 1 \text{ on a neighborhood of }E\Big\}.
\]

A set \(E\) is **polar** (for the diffusion associated with \(\mathcal{E}\)) if \(\mathrm{Cap}_\mu(E)=0\).

**Interpretation.**
If \(\Sigma\) is polar, then a diffusion started \(\mu\)-a.e. never hits \(\Sigma\). For analysis, \(\Sigma\) is too thin to contribute boundary terms.

---

## 3. Finite-dimensional lattice polarity: codimension mechanism

On a finite lattice, the configuration space is finite-dimensional:
\[
\mathcal{C}=G^{|B|},
\qquad \dim(\mathcal{C})=|B|\,(N^2-1).
\]

The reducible locus is described by having a nontrivial stabilizer (centralizer larger than the center). A standard way to estimate its size is to parameterize stabilizers via block decompositions \(k+(N-k)\) and compute the dimension drop.

### 3.1 Dimension drop for reducibility
For \(G=\mathrm{SU}(N)\), a typical reducible stratum corresponds to a subgroup \(S(\mathrm{U}(k)\times\mathrm{U}(N-k))\), whose dimension is
\[
\dim S(\mathrm{U}(k)\times\mathrm{U}(N-k)) = k^2+(N-k)^2-1.
\]
Thus the codimension inside \(\mathrm{SU}(N)\) is
\[
(N^2-1) - \big(k^2+(N-k)^2-1\big) = 2k(N-k).
\]
Across \(|B|\) independent link variables, one expects a codimension scaling like
\[
\mathrm{codim}(\Sigma) \;\gtrsim\; 2k(N-k)\,|B|.
\]

In particular, for any nontrivial split \(1\le k\le N-1\), we have \(2k(N-k)\ge 2(N-1)\), which is already large for \(N\ge 3\), and becomes very large when multiplied by \(|B|\).

### 3.2 Capacity consequence (finite dimension)
For Sobolev \(W^{1,2}\) capacity in \(\mathbb{R}^d\), smooth submanifolds of codimension \(\ge 3\) are polar (sufficient condition).

Therefore, if the reducible locus in \(\mathcal{C}\) has codimension \(\ge 3\), it is capacity-zero with respect to any measure absolutely continuous with a bounded density relative to the Riemannian volume measure.

> **Caution.** Codimension \(\ge 1\) is *not* sufficient for polarity in finite dimensions; hypersurfaces generally have positive capacity. The safe sufficient condition is codimension \(\ge 3\) (or more generally, Hausdorff dimension \(< d-2\)).

Because \(|B|\) is typically large, the lattice reducible set is expected to be polar except possibly in tiny lattices.

---

## 4. Infinite-dimensional Gaussian polarity (key lemma)

The project’s continuum strategy uses a Gaussian reference measure \(\mu_0\) on a Hilbert/Sobolev completion \(H\) of gauge fields.

### 4.1 Infinite-rank commutator map
A core structural lemma is:

**Lemma (infinite-rank commutator map).**  
If \(\xi\) is a nontrivial stabilizer section for a reducible connection, then the linear map
\[
T_\xi: H \to H,
\qquad T_\xi(a)=[a,\xi],
\]
has **infinite rank** (constructed by building infinitely many compactly supported perturbations \(a_n\) with disjoint supports whose brackets with \(\xi\) stay nonzero).

This implies that the tangent space to the reducible stratum has **infinite codimension** in the ambient Gaussian space.

### 4.2 Gaussian polarity of infinite-codimension sets
In an abstract Wiener space, closed affine subspaces of infinite codimension are polar for the Ornstein–Uhlenbeck process, hence have zero \(\mu_0\)-capacity.

Thus:

**Theorem (Gaussian polarity, project form).**
\[
\mathrm{Cap}_{\mu_0}(\Sigma)=0.
\]

---

## 5. Transfer of polarity under change of measure

To transport polarity from \(\mu_0\) to the Yang–Mills measure \(\mu\), the project uses a general bridge:

**Lemma (capacity equivalence under \(L^p\) density, schematic).**  
If \(\mu\ll \mu_0\) with Radon–Nikodym derivative \(h=\frac{d\mu}{d\mu_0}\in L^p(\mu_0)\) for some \(p>1\), then
\[
\mathrm{Cap}_{\mu_0}(E)=0 \;\Rightarrow\; \mathrm{Cap}_{\mu}(E)=0,
\]
for sets \(E\) measurable in the Sobolev-capacity sense.

This is the analytic “bridge” that would make continuum polarity a corollary once the integrability of \(h\) is proven.

---

## 6. The stratified parabolic maximum principle (why polarity is *used*)

With polarity established, one can aim to prove **comparison/maximum principles on the regular stratum** despite stratification:

- Solve (weakly) a parabolic inequality on \(\mathcal{M}_{\mathrm{reg}}\)
\[
\partial_t u \ge Lu + F(u,t,x),
\]
where \(L\) is the diffusion generator.
- Use polarity to show \(\Sigma\) contributes no boundary term.
- Conclude positivity preservation, enabling a global lower bound on curvature eigenvalues (and hence a spectral gap).

This is the project’s intended functional-analytic core linking “thinness of \(\Sigma\)” to “global control of the Riccati/Hessian evolution”.

---

## 7. Minimal checklist to make this airtight in the continuum

1. Specify the abstract Wiener space \((H,E,\mu_0)\) precisely for gauge fields on \(M\).
2. Prove the commutator lemma in the exact Sobolev topology used (including gauge covariance).
3. State the Gaussian polarity theorem being invoked (reference, conditions).
4. Prove (or assume) an \(L^p\) bound for \(d\mu_{\mathrm{YM}}/d\mu_0\) strong enough to transfer capacity zero.
5. Prove the stratified maximum principle for the Dirichlet form on \(\mathcal{M}\).

Once these are done, \(\Sigma\) is no longer a structural obstruction: it becomes a “ghost boundary” that the dynamics ignores.
