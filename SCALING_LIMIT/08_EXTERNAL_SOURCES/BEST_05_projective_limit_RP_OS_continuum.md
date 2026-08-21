# Projective-Limit Reflection Positivity and Continuum OS Reconstruction (Extracted)

This note extracts the “projective limit → continuum reflection positivity” argument and packages it in a way that can be dropped into a manuscript as infrastructure.

The key idea: **reflection positivity is stable under projective limits** as long as the reflection commutes with the coarse-graining projections.

---

## 1. Projective system of lattices and configuration spaces

Let \(\{a_n\}_{n\ge 1}\) be a decreasing sequence of lattice spacings with refinement maps.

For each \(a\), let \(\mathcal A_a\) be the compact configuration space of lattice gauge fields (e.g. \(G^{E(a)}\) with \(G=SU(3)\)) with its Borel \(\sigma\)-algebra.

Assume there are measurable coarse-graining projections
\[
\pi_{a\leftarrow b}:\mathcal A_b\to\mathcal A_a,\qquad b<a,
\]
satisfying the consistency relations
\[
\pi_{a\leftarrow b}\circ\pi_{b\leftarrow c} = \pi_{a\leftarrow c}.
\]

Define the projective limit space
\[
\mathcal A_\infty := \varprojlim_a \mathcal A_a
\]
and its cylindrical \(\sigma\)-algebra \(\mathcal F_{\mathrm{cyl}}\).

---

## 2. Projectively consistent measures

Let \(\mu_a\) be a probability measure on \(\mathcal A_a\).

### Assumption (projective consistency)
For all \(b<a\),
\[
(\pi_{a\leftarrow b})_\#\,\mu_b = \mu_a.
\]

### Theorem (Kolmogorov extension for the projective limit)
Under projective consistency, there exists a unique probability measure \(\mu_\infty\) on \((\mathcal A_\infty,\mathcal F_{\mathrm{cyl}})\) such that for each \(a\),
\[
(\pi_a)_\#\,\mu_\infty=\mu_a,
\]
where \(\pi_a:\mathcal A_\infty\to\mathcal A_a\) is the canonical projection.

---

## 3. Reflection operators and compatibility

Let \(\theta_a:\mathcal A_a\to\mathcal A_a\) be the lattice time reflection.

Let \(\theta_\infty:\mathcal A_\infty\to\mathcal A_\infty\) be the induced reflection defined by
\[
\pi_a\circ \theta_\infty = \theta_a\circ \pi_a.
\]

### Assumption (reflection–coarse-graining commutation)
For all \(b<a\),
\[
\pi_{a\leftarrow b}\circ\theta_b = \theta_a\circ\pi_{a\leftarrow b}.
\]

---

## 4. Reflection positivity is stable under the limit

Let \(\mathcal F^+_a\) be the positive-time algebra of observables on \(\mathcal A_a\) (supported in \(t\ge 0\)).

### Assumption (lattice reflection positivity)
For every \(a\) and every \(F\in \mathcal F^+_a\),
\[
\int_{\mathcal A_a} \overline{F}\,(\theta_a F)\,d\mu_a \ \ge\ 0.
\]

### Theorem (continuum reflection positivity on cylindrical observables)
For any cylindrical positive-time observable \(F\in\mathcal F^+_{\mathrm{cyl}}\),
\[
\int_{\mathcal A_\infty} \overline{F}\,(\theta_\infty F)\,d\mu_\infty \ \ge\ 0.
\]

#### Proof
If \(F\) is cylindrical, \(F=f\circ\pi_a\) for some \(a\). By reflection compatibility,
\[
\theta_\infty F = (\theta_a f)\circ\pi_a.
\]
Then
\[
\int_{\mathcal A_\infty}\overline{F}\,(\theta_\infty F)\,d\mu_\infty
=
\int_{\mathcal A_a}\overline{f}\,(\theta_a f)\,d\mu_a
\ge 0.
\]

---

## 5. Continuum OS reconstruction (minimal statement)

Given continuum reflection positivity, the Osterwalder–Schrader reconstruction applied to cylindrical observables yields:

- a Hilbert space \(\mathcal H_{\mathrm{OS},\infty}\),
- a cyclic vacuum \(\Omega\),
- a strongly continuous semigroup \(T_t\) of contractions induced by Euclidean time translations,
- and a self-adjoint generator \(H_\infty\ge 0\) with \(T_t=e^{-tH_\infty}\).

This “continuum OS layer” is then available for spectral statements.

---

## 6. Convergence of lattice OS semigroups (what you need if you want a continuum gap)

To pass a *uniform lattice gap* to the continuum Hamiltonian, you typically want:

1. A notion of consistent embeddings \(J_a:\mathcal H_{\mathrm{OS},a}\to \mathcal H_{\mathrm{OS},\infty}\) on a common core (cylindrical vectors).
2. Strong convergence of semigroups on that core:
   \[
   J_a\,T_t^{(a)} \ \to\ T_t^{(\infty)}\,J_a.
   \]
3. A functional-analytic principle (e.g. strong resolvent convergence) implying spectral stability of the gap.

This is the place where you pay attention to domains, cores, and the topology you put on the limit.

---

## 7. Why this module matters

Even independent of Yang–Mills:

- It’s a reusable lemma: **RP survives taking continuum limits defined by projective systems**.
- It isolates exactly what additional structure is required to say “OS reconstruction commutes with the continuum limit” in a rigorous operator sense.
