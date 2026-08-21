# Exciting Extract 02 — Reflection Positivity as a Permanent Property (RG Pushforwards + Projective Limits)

## 1. Why this is exciting

Reflection positivity (RP) is the lynchpin that turns Euclidean measures into Hilbert spaces and Hamiltonians (OS reconstruction). In constructive programs, you need RP to survive:

- **coarse graining / blocking / RG maps**, and
- **limits** (thermodynamic, continuum, infinite volume).

This extract isolates two permanence lemmas that are completely first-principles and *model-independent*:

1. **RP survives reflection-equivariant pushforward.**
2. **RP survives projective limits** (at least on cylinder observables).

Together they suggest a general “RP is functorial” theory: if your RG maps respect the reflection structure, positivity cannot be destroyed by the act of coarse graining itself.

---

## 2. Reflection positivity: a Gram-matrix definition

A convenient measure-theoretic RP definition is:

- A probability space \((\Omega,\mathcal F,\mu)\),
- a measurable involution \(\theta:\Omega\to\Omega\) (\(\theta^2=\mathrm{id}\)),
- and a sub-\(\sigma\)-algebra \(\mathcal F_+\subset\mathcal F\) (“positive-time observables”).

> **Definition 2.1 (Reflection positivity).**  
> \((\Omega,\mathcal F,\mu,\theta;\mathcal F_+)\) is reflection positive if for any finite family
> \(F_1,\dots,F_n\in L^\infty(\mathcal F_+)\), the Gram matrix
> \[
> G_{ij}:=\int_\Omega \overline{F_i(\theta\omega)}\,F_j(\omega)\,d\mu(\omega)
> \]
> is positive semidefinite.

Equivalently (the \(n=1\) case),
\[
\int_\Omega \overline{F(\theta\omega)}\,F(\omega)\,d\mu(\omega)\ge 0
\quad\forall F\in L^\infty(\mathcal F_+).
\tag{2.1}
\]

---

## 3. Permanence under reflection-equivariant pushforward

### Theorem 3.1 (RP survives reflection-equivariant pushforward)

Let \((\Omega,\mathcal F,\mu,\theta;\mathcal F_+)\) be reflection positive.  
Let \((\Omega',\mathcal F',\theta';\mathcal F'_+)\) be another reflected measurable space.

Suppose \(P:\Omega\to\Omega'\) is measurable and satisfies:

1. **equivariance:** \(P\circ\theta = \theta'\circ P\),
2. **positive half preservation:** \(P^{-1}(\mathcal F'_+)\subset\mathcal F_+\).

Define \(\mu':=P_\#\mu\). Then \((\Omega',\mathcal F',\mu',\theta';\mathcal F'_+)\) is reflection positive.

**Proof.**  
Take any \(G_1,\dots,G_n\in L^\infty(\mathcal F'_+)\) and set \(F_i:=G_i\circ P\in L^\infty(\mathcal F_+)\). Then
\[
\int_{\Omega'} \overline{G_i(\theta'\omega')}\,G_j(\omega')\,d\mu'(\omega')
=
\int_{\Omega}\overline{G_i(\theta'P\omega)}\,G_j(P\omega)\,d\mu(\omega)
\overset{\text{equiv.}}=
\int_{\Omega}\overline{G_i(P\theta\omega)}\,G_j(P\omega)\,d\mu(\omega)
=
\int_\Omega \overline{F_i(\theta\omega)}\,F_j(\omega)\,d\mu(\omega).
\]
The right-hand Gram matrix is PSD by RP of \(\mu\), hence so is the left-hand Gram matrix. ∎

### Interpretation for RG / blocking

If \(P\) is your block map (from fine configurations to coarse ones), then:

- “equivariance” says blocking commutes with time reflection,
- “positive half preservation” says blocking does not mix past and future.

Under these conditions, RP is automatically inherited by the coarse measure.  
This is a **sufficient** condition, but it is exactly what you can engineer in RP-compatible blocking.

---

## 4. Permanence under projective limits

Now consider a directed index set \((\mathcal I,\preceq)\). For each \(i\in\mathcal I\), let
\[
(\Omega_i,\mathcal F_i,\mu_i,\theta_i;\mathcal F_{i,+})
\]
be a reflection positive system, and for \(j\preceq i\) let \(P_{i\to j}:\Omega_i\to\Omega_j\) be measurable maps such that:

1. **consistency:** \((P_{i\to j})_\#\mu_i=\mu_j\),
2. **equivariance:** \(P_{i\to j}\circ\theta_i=\theta_j\circ P_{i\to j}\),
3. **positive-half preservation:** \(P_{i\to j}^{-1}(\mathcal F_{j,+})\subset\mathcal F_{i,+}\).

Assume \(\{\mu_i\}\) is projectively consistent, so a projective limit measure \(\mu\) exists on the inverse limit space \(\Omega\), at least at the cylinder level (Kolmogorov extension theorem framework).

### Theorem 4.1 (RP passes to the projective limit on cylinder observables)

Under the assumptions above, the projective limit measure \(\mu\) is reflection positive on cylinder observables. Concretely: if \(F_1,\dots,F_n\) depend only on level \(i\) and are positive-half at that level, then the Gram matrix
\[
\int_\Omega \overline{F_p(\theta\omega)}\,F_q(\omega)\,d\mu(\omega)
\]
is PSD.

**Proof.**  
Write cylinder functions \(F_k=\widetilde F_k\circ\pi_i\), where \(\pi_i:\Omega\to\Omega_i\) is the canonical projection. Then, by definition of the projective limit,
\[
\int_\Omega \overline{F_p(\theta\omega)}\,F_q(\omega)\,d\mu(\omega)
=
\int_{\Omega_i}\overline{\widetilde F_p(\theta_i\omega_i)}\,\widetilde F_q(\omega_i)\,d\mu_i(\omega_i),
\]
using \(\pi_i\circ\theta=\theta_i\circ\pi_i\). The right-hand Gram matrix is PSD by RP of \(\mu_i\). ∎

---

## 5. What theory this points toward

These two permanence lemmas strongly suggest a clean conceptual structure:

> **Reflection positivity is a “monoidal positivity” property that is stable under reflection-equivariant morphisms and limits.**

Potential extensions that would elevate this into a larger theory:

1. **Markov kernels instead of deterministic pushforwards.**  
   Replace \(P\) by a reflection-equivariant Markov operator \(K(\omega,d\omega')\).  
   This would cover *noisy* coarse graining and stochastic RG steps.

2. **Operator-algebra formulation.**  
   View RP as positivity of a sesquilinear form on an algebra \(\mathcal A_+\) and study when completely positive maps preserve it.

3. **Category viewpoint.**  
   Objects: reflected probability spaces \((\Omega,\mu,\theta;\mathcal F_+)\).  
   Morphisms: reflection-equivariant coarse-graining maps preserving positive-half observables.  
   Then RP is simply “closed under morphisms,” and projective limits become categorical limits.

For lattice gauge theory, this is not mere aesthetic: it’s exactly what you need for a continuum OS reconstruction pipeline that does not lose positivity during blocking or limiting.
