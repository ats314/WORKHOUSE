# Reflection Positivity Under Coarse Graining and Projective Limits
## (A structural lemma for OS permanence)

This note isolates a structural point that is easy to lose in the weeds:

> **Reflection positivity (OS positivity) is stable under any reflection-equivariant coarse graining,
> and also under projective limits on cylinder observables.**

This is not a numerical phenomenon; it is a categorical one.

---

## 1. OS reflection structure on a lattice

Let $X$ be the configuration space (e.g. $X=G^{E(\Lambda)}$ in finite volume or a projective limit space in infinite volume).
Fix a reflection hyperplane and let

- $\theta:X\to X$ be the induced involution (spacetime reflection),
- $\mathcal A$ be the algebra of bounded cylinder observables,
- $\mathcal A_+$ be the subalgebra depending only on the “positive-time” half.

A probability measure $\mu$ on $X$ is **reflection positive** if

\[
\mathbb E_\mu\big[f\cdot \theta f\big]\;\ge\;0
\qquad\text{for all }f\in \mathcal A_+.
\]

---

## 2. Coarse graining: the only condition that matters

Let $C:X\to X'$ be a measurable coarse-graining map to a coarser configuration space $X'$.
Assume $X'$ has its own reflection $\theta':X'\to X'$ and positive-time algebra $\mathcal A_+'$.

The condition needed is **reflection equivariance**:

\[
C\circ \theta \;=\; \theta'\circ C.
\]

(Informally: coarse graining “commutes with reflection.”)

Define the pushforward (coarse-grained) measure
\[
\mu' \;:=\; C_\#\mu.
\]

---

## 3. The permanence theorem (coarse graining)

**Theorem (RP permanence under reflection-equivariant coarse graining).**  
If $\mu$ is reflection positive on $(X,\theta,\mathcal A_+)$ and $C$ is reflection-equivariant,
then $\mu'=C_\#\mu$ is reflection positive on $(X',\theta',\mathcal A_+')$.

**Proof sketch (one line).**  
Given $f'\in \mathcal A_+'$, pull it back to $f=f'\circ C\in \mathcal A_+$ and compute
\[
\mathbb E_{\mu'}[f'\,\theta' f']
=
\mathbb E_{\mu}[ (f'\circ C)\,(\theta' f'\circ C)]
=
\mathbb E_{\mu}[ f\,\theta f]\ge 0,
\]
using equivariance to identify $\theta'f'\circ C=\theta(f'\circ C)$.

That’s it. No special property of gauge theory is used.

---

## 4. Projective limits: “RP is cylinder-stable”

Many constructions pass to an infinite-volume (or continuum) object via a projective family

\[
(X_i,\mu_i)_{i\in I},\qquad \pi_{ij}:X_j\to X_i,\quad i\preceq j,
\]

where $\mu_i$ are consistent under pushforward: $(\pi_{ij})_\#\mu_j=\mu_i$.

If each $X_i$ carries a reflection $\theta_i$ and the bonding maps are reflection-equivariant
\[
\pi_{ij}\circ \theta_j = \theta_i\circ \pi_{ij},
\]
then the projective limit measure (when it exists) is reflection positive on the **cylinder algebra**.

This is the same proof as in coarse graining: every cylinder function factors through some $\pi_i$,
where positivity is known.

---

## 5. Why this matters in the proof architecture

Reflection positivity is the hypothesis that lets you run Osterwalder–Schrader reconstruction and
translate **Euclidean exponential clustering** into a **Hamiltonian mass gap**.

The permanence lemmas mean you can decouple tasks:

- **Analytic task:** prove clustering / spectral gap at fixed cutoff on finite volumes.
- **Structural task:** ensure coarse graining and limits do not destroy OS positivity.

So long as RG/coarse graining is chosen reflection-equivariant, OS is a “bolt-on” property.

---

## 6. Continuum-limit hint

If one pursues a continuum measure as a projective limit of cylinder measures,
reflection positivity persists automatically provided the bonding maps are reflection-equivariant.
This turns “keep OS while taking a limit” from a delicate analytic constraint
into a clean design rule: **build reflection equivariance into your embeddings.**

---

## Cross references

- OS plane and positive-time algebra: `### 4.1 OS reflection plane, induced involution on configurations, positive-time algebra.txt`.
- Thermodynamic limit and permanence: `## 11.1 Thermodynamic limit at fixed cutoff existence of limit points and permanence of OS structure.txt`.
- Coarse graining and projective-limit permanence: `## 12.1 Reflection positivity permanence under reflection-equivariant coarse graining and under projective limits on cylinder observables.txt`.
