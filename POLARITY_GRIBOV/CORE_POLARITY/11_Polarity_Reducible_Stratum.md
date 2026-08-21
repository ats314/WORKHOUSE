# 11 — Polarity of the Reducible Stratum

## Abstract
We prove that the **reducible stratum** (configurations with enhanced symmetry) has **capacity zero** and is therefore **polar** — invisible to the stochastic dynamics. This justifies ignoring the singularities of the gauge orbit space when applying the convexity analysis of the Matrix Hinge.

**Connected Files:**
- **[22] Calladine Rigidity:** Counts the codimension of the strata.
- **[36] Horizontal Maximum:** Uses polarity to extend maximum principles.

---

## 1. Background: Stratified Spaces

### 1.1 The Gauge Orbit Space
The configuration space modulo gauge is:
$$
\mathcal{M} = \mathcal{A} / \mathcal{G}
$$
This is NOT a manifold — it has singularities.

### 1.2 The Strata
- **Principal stratum $\mathcal{M}^*$:** Generic connections. Stabilizer = center $Z(G)$.
- **Reducible strata $\mathcal{R}$:** Connections with larger stabilizer (e.g., Abelian).

For $G = SU(2)$:
- A connection is reducible if it preserves a splitting $\mathbb{C}^2 = L_1 \oplus L_2$.
- This happens when the connection takes values in a Cartan subalgebra.

### 1.3 Codimension
**Theorem (Singer-Marsden):**
$$
\text{codim}(\mathcal{R}) = \text{dim}(G/H)
$$
where $H$ is the stabilizer of a reducible.

For $SU(2) \to U(1)$: $\text{codim} = 3 - 1 = 2$.

---

## 2. Capacity Theory

### 2.1 Definition of Capacity
For a set $E \subset M$, the **capacity** is:
$$
\text{Cap}(E) = \inf\left\{ \int |\nabla u|^2 d\mu : u \ge 1_{E}, u \in W^{1,2} \right\}
$$

### 2.2 Capacity and Codimension
**Theorem:** In dimension $n$, a smooth submanifold of codimension $k$ has:
- Cap = 0 if $k \ge 2$.
- Cap $> 0$ if $k = 1$.

For the reducible stratum with codim $\ge 2$:
$$
\text{Cap}(\mathcal{R}) = 0
$$

### 2.3 Polar Sets
A set is **polar** if it has capacity zero.
Polar sets are invisible to diffusion processes:
$$
\mathbb{P}(\text{Brownian motion hits } \mathcal{R}) = 0
$$

---

## 3. The Proof for Yang-Mills

### 3.1 Dimension Counting
For $G = SU(N)$ on a lattice with $L^4$ sites:
- dim($\mathcal{A}$) = $4L^4 \cdot (N^2 - 1)$.
- dim($\mathcal{G}$) = $L^4 \cdot (N^2 - 1)$.
- dim($\mathcal{M}$) = $3L^4 \cdot (N^2 - 1)$.

For a reducible with stabilizer $U(1)$ (maximal):
- dim($\mathcal{R}$) = $3L^4 \cdot 1$ (Abelian connection moduli).

Codimension:
$$
\text{codim}(\mathcal{R}) = 3L^4 \cdot (N^2 - 1) - 3L^4 = 3L^4 \cdot (N^2 - 2)
$$

For $N = 2$: codim = $3L^4 \cdot 2 = 6L^4 \gg 2$. $\checkmark$

### 3.2 Local Hausdorff Dimension
Near a reducible, the orbit space has a cone singularity.
The Hausdorff dimension of the singularity is:
$$
\dim_H(\mathcal{R}) = \dim(\mathcal{M}) - \text{codim} = 3L^4(N^2-1) - 3L^4(N^2-2) = 3L^4
$$

This is much smaller than dim($\mathcal{M}$) = $3L^4(N^2-1)$.

---

## 4. Consequences for the Mass Gap

### 4.1 Convexity Extension
The Matrix Hinge (File [03]) might fail at reducible points (curvature discontinuity).
But since $\mathcal{R}$ is polar, the diffusion process never sees it.
**We can ignore $\mathcal{R}$ in the Bakry-Émery analysis.**

### 4.2 Maximum Principle
Maximum principles for the heat equation require continuity at the boundary.
Polar sets can be removed without affecting the maximum:
$$
\max_{\mathcal{M}} u = \max_{\mathcal{M}^*} u
$$

### 4.3 Spectral Gap
The spectral gap of the Laplacian on $\mathcal{M}$ equals that on $\mathcal{M}^*$.
Removing the polar set doesn't change the spectrum.

---

## 5. Contrast with the Abelian Case

### 5.1 $G = U(1)$
All connections are "reducible" (trivial stabilizer = full group).
The entire space is a single stratum.
There is no singularity.

But there is also **no Haar curvature** ($U(1)$ is flat).

### 5.2 The Non-Abelian Advantage
Non-Abelian groups have:
1. Positive Haar curvature (File [01]).
2. Polar reducibles (this file).

The singularities don't matter because they're measure-zero.
The curvature does matter because it's present everywhere else.

---

## 6. The Gribov Horizon

### 6.1 Definition
The **Gribov Horizon** is the boundary of the region in $\mathcal{A}$ where the Faddeev-Popov determinant is positive.
It is related to, but distinct from, the reducible stratum.

### 6.2 Polarity of the Horizon
The Gribov horizon has codimension 1 (a surface), so it has positive capacity.
However, it is the **boundary** of a domain, not a submanifold.
The stochastic quantization stays **inside** the Gribov region by construction.

### 6.3 Implication
We work on the "first Gribov region" $\Omega$, which is convex.
The reducibles are in the interior of $\partial \Omega$ but have zero capacity.
The horizon itself is like a reflecting boundary.

---

## Summary

The reducible stratum is "geometrically present" but "probabilistically invisible":
1. Codimension $\ge 2$ implies capacity zero.
2. Diffusion processes never hit polar sets.
3. Spectral gaps and curvature bounds extend across polar sets.

This justifies the "smooth analysis on singular spaces" approach of the mass gap program.

---

## References
- S. Donaldson, P. Kronheimer, *The Geometry of Four-Manifolds* (Stratification).
- M. Fukushima, *Dirichlet Forms and Symmetric Markov Processes* (Capacity).
- **File [22]** (Calladine) for dimension counting.
- **File [36]** (Horizontal Maximum) for the application.
