# Reflection Positivity and OS Permanence Under Coarse Graining / Projective Limits
*(Why the constructive/QFT side of the project can survive the analytic machinery)*

## 0. What this module is doing in the project

Most analytic clustering arguments only tell you “correlations decay”.
To connect the lattice model to an actual Euclidean QFT (or a candidate continuum limit),
you also want the Osterwalder--Schrader (OS) structure:

- a reflection involution $\theta$,
- a positive-time algebra $\mathcal A_+$,
- reflection positivity (RP): $\langle \theta F \cdot F\rangle\ge 0$ for $F\in\mathcal A_+$,
- and the induced OS Hilbert space / semigroup.

The project’s Part 12 shows that this OS structure is **permanent** under two operations
you inevitably use in a constructive approach:

1. **reflection-equivariant coarse graining** (block maps / conditional expectations),
2. **projective limits** on cylinder observables (thermodynamic / continuum limiting procedures).

That permanence is the “physics glue”: it lets you do hard analysis at finite cutoff while
knowing the axioms you care about don’t evaporate under limits.

---

## 1. Reflection setup on a lattice

Fix a reflection hyperplane (or reflection map) $r$ on the lattice.
It induces an involution on configurations $U\mapsto \theta U$.

Let $\mathcal A$ be the algebra of cylinder observables.
Define the positive-time subalgebra $\mathcal A_+$ as observables supported in the “positive half”.

Reflection positivity (RP) is:
\[
\langle (\theta F)\,F\rangle_\mu \ge 0
\qquad\forall F\in \mathcal A_+.
\tag{RP}
\]

The OS reconstruction builds the Hilbert space completion of $\mathcal A_+/\mathcal N$
under $\langle \theta F\cdot F\rangle$ and defines the transfer semigroup from time translations.

---

## 2. Permanence under reflection-equivariant coarse graining

Let $\mathcal R$ be a coarse-graining map on observables (typically conditional expectation
onto a block $\sigma$-algebra or a pushforward by a block map).
Assume $\mathcal R$ is **reflection-equivariant**:
\[
\mathcal R(\theta F)=\theta\,\mathcal R(F).
\tag{Eq}
\]

Then the coarse-grained state $\mu' := \mu\circ\mathcal R^{-1}$ inherits RP:

\[
\langle (\theta F')F'\rangle_{\mu'} \ge 0
\qquad\forall F'\in \mathcal A'_+.
\]

**Proof idea (one line).**  
Write $F'=\mathcal R(F)$ with $F\in\mathcal A_+$, then use (Eq) and positivity of conditional expectation:
\[
\langle (\theta F')F'\rangle_{\mu'}
=
\langle \mathcal R(\theta F)\,\mathcal R(F)\rangle_\mu
\ge
\langle \mathcal R((\theta F)F)\rangle_\mu
=
\langle (\theta F)F\rangle_\mu\ge 0.
\]

---

## 3. Permanence under projective limits on cylinder observables

Let $(\mu_n)$ be a family of finite-volume measures with RP, and suppose:

- cylinder observables are consistent under restriction maps,
- $\mu_n$ has limit points on the cylinder algebra (tightness / Prokhorov-type),
- and the reflection map is compatible across $n$.

Then any projective limit $\mu_\infty$ inherits RP on the cylinder algebra:

\[
\langle (\theta F)F\rangle_{\mu_\infty}
=
\lim_{k\to\infty}\langle (\theta F)F\rangle_{\mu_{n_k}}
\ge 0
\qquad\forall F\in \mathcal A_+,
\]
because the RP inequality is closed under weak limits on bounded observables.

This is the mathematically clean statement of “OS structure survives the thermodynamic limit”.

---

## 4. Why this dovetails with Parts 6--10

The clustering mechanism (HS + massive Maxwell inverse decay + localization) is done at
**fixed cutoff** and typically on a high-probability event $K$.

Part 12’s permanence results ensure that:

- coarse-graining steps used to define $\mu(\cdot\mid K)$ or block observables
  can be done without breaking RP (provided the maps are reflection-equivariant), and
- any thermodynamic/projective limit you take later will retain OS structure.

So the analytic work does not “break the axioms”.

---

## Source pointers in the project

- Reflection plane and induced involution: `### 4.1 OS reflection plane, induced involution on configurations, positive-time algebra.txt`.
- Thermodynamic limit at fixed cutoff + permanence of OS structure: `## 11.1 Thermodynamic limit at fixed cutoff existence of limit points and permanence of OS structure.txt`.
- Reflection positivity permanence under coarse graining / projective limits: `## 12.1 Reflection positivity permanence under reflection-equivariant coarse graining and under projective limits on cylinder observables.txt`.
