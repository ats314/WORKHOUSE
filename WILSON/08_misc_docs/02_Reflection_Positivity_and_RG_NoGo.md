# Reflection positivity permanence and a nonabelian Markovian coarse-graining no-go

This note extracts two structural results from the project:

1. **Permanence principles**: reflection positivity (OS positivity) is stable under reflection-equivariant pushforwards and under projective limits on cylinder observables.

2. **A sharp no-go theorem**: for a nontrivial nonabelian compact Lie group, one cannot have an *exact* reflection-equivariant **Markov** coarse-graining kernel with an exact “projection” property for link holonomies. Such a kernel would force commutativity.

These statements do not prove a mass gap, but they strongly constrain what a viable cross-scale RG architecture can look like.

---

## 1. OS reflection positivity (brief reminder)

Let $(\Omega,\mathcal F,\mu)$ be a probability space carrying lattice gauge configurations.
Let $\theta$ be a reflection map on configurations induced by reflecting the lattice across a time-zero hyperplane.
Let $\mathcal A_+$ be the algebra of observables supported in positive times.

**Reflection positivity** is the condition
\[
\langle F,\; \theta F \rangle_\mu \;\ge\;0
\qquad\forall F\in \mathcal A_+,
\]
where $\langle\cdot,\cdot\rangle_\mu$ is the $L^2(\mu)$ inner product.

---

## 2. Permanence under reflection-equivariant pushforwards

Let $\pi:\Omega\to\Omega'$ be measurable and assume $\pi\circ\theta = \theta'\circ\pi$ for a reflection $\theta'$ on $\Omega'$.

**Lemma (Pushforward preserves reflection positivity).**  
If $\mu$ is reflection positive on $(\Omega,\theta)$ then $\mu'=\pi_\#\mu$ is reflection positive on $(\Omega',\theta')$.

*Proof sketch.* For $F'\in \mathcal A_+'$ set $F=F'\circ\pi\in\mathcal A_+$. Then
\[
\langle F',\theta'F'\rangle_{\mu'}
=
\langle F,\theta F\rangle_\mu
\ge 0.
\]

A related lemma states that reflection positivity is preserved under weak limits of measures, provided cylinder observables are controlled (a standard compactness argument).

---

## 3. Permanence under projective limits (cylinder observables)

Suppose $\{\mu_n\}$ is a projective system of reflection-positive measures on increasing cylinder $\sigma$-algebras, with compatible marginals.
Under mild tightness conditions, the projective limit $\mu$ is reflection positive.

This “thermodynamic/perfect-action” interface is the clean way to pass OS positivity across limits.

---

## 4. The nonabelian no-go: exact Markovian coarse graining forces commutativity

The project isolates an obstruction that can be stated purely algebraically.

### 4.1 Informal statement
Assume there exists a **Markov kernel** $K(U,dV)$ from fine configurations $U$ to coarse configurations $V$ that:

- is reflection-equivariant, and  
- satisfies an exact “projection property” (coarse link holonomy is an exact conditional expectation of a fine holonomy functional).

Then, for a nontrivial compact Lie group $G$ with faithful irreducible representation, this cannot hold unless $G$ is abelian.

### 4.2 Why the obstruction is real
Exact Markovian coarse graining with exact holonomy projection essentially defines a group-homomorphic map from the fine path groupoid to the coarse path groupoid.
In a nonabelian group, the required factorization for all paths forces commutativity (the coarse variable would have to preserve ordered products exactly, which is incompatible with noncommutativity unless the image lies in a common abelian subgroup).

### 4.3 What must give
To build a cross-scale architecture that preserves OS positivity and still yields a continuum theory, one must weaken at least one ingredient:

- allow **approximate** projection with quantified error,  
- enlarge the state space (introduce **edge modes / boundary degrees of freedom** on block boundaries),  
- use non-Markovian coarse graining,  
- or use a gauge-fixed / stochastic-gauge interface that is only equivariant “in distribution.”

The no-go theorem is useful because it stops one from spending years chasing an impossible exact RG kernel.

---

## 5. Research directions opened by this constraint

1. **Approximate Markov kernels**: define a metric on cylinder algebras and quantify how projection error propagates through OS positivity and Hamiltonian reconstruction.

2. **Edge-mode RG**: treat block boundaries as carrying additional group variables; coarse holonomy becomes a constrained product including edge modes. This can restore nonabelian structure without exact homomorphism constraints.

3. **Stochastic gauge choice**: sample a gauge fixing along with the coarse configuration so the effective map is not a deterministic conditional expectation of noncommutative products.
