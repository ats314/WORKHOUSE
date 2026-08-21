# Synthesis 05: Continuum Spark — The Bridge to Physical Mass Gap

## Abstract

The finite-cutoff convexity mechanisms (Haar mass, Wilson Hessian) die as the lattice spacing $a \to 0$ along the asymptotically-free trajectory. A continuum mass gap requires an **a-independent convexity source**—a "Spark"—that ignites the curvature → LSI → spectral gap chain at physical scales.

This synthesis extracts the three main Spark candidates and the continuum limit machinery from the project notes.

---

# Chapter 1: The Continuum Obstruction

## 1.1 Why Finite-Cutoff Convexity Fails

At finite cutoff, the horizontal Hessian has the form:
$$
\mathrm{Hess}_{\mathrm{hor}} S_{\mathrm{eff}} \succeq \underbrace{c_0 a^2 g^2}_{\text{Haar spark}} - \underbrace{\beta \cdot C_V}_{\text{Wilson nonconvexity}}
$$

Along asymptotic freedom:
- $a \to 0$
- $g(a) \to 0$
- $\beta(a) \sim 1/g(a)^2 \to \infty$

Therefore:
$$
\boxed{a^2 g(a)^2 \to 0, \quad \text{Haar spark dies}}
$$

**Conclusion:** Continuum mass gap requires a different source.

## 1.2 The Riccati Warning

Under heat-flow smoothing of densities:
$$
\partial_t H_t = \Delta H_t - 2H_t^2 + R_t
$$

For Gaussians ($R_t \equiv 0$):
$$
\dot{\lambda} = -2\lambda^2 \implies \lambda(t) \sim \frac{1}{2t} \to 0
$$

**Without a positive source term, convexity decays.**

## 1.3 Three Candidate Stabilizers

### A. Intrinsic Geometry as Source Term

On compact group manifolds, positive Ricci curvature from bi-invariant metric can stabilize:
$$
\dot{\lambda} \gtrsim -2\lambda^2 + \sigma_{\mathrm{geom}}, \quad \sigma_{\mathrm{geom}} > 0
$$

**Fixed point:** $\lambda_* = \sqrt{\sigma_{\mathrm{geom}}/2}$

### B. Trace Anomaly as Effective Curvature (Conjectural)

Anomaly-curvature identification:
$$
\sigma_{\mathrm{anom}}(t) = \mathcal{K} \frac{\beta(g(t))}{g(t)} \langle \mathrm{Tr}\, F_{\mu\nu}^2 \rangle_t
$$

For asymptotically free YM: $\beta(g) < 0$ and $\langle \mathrm{Tr}F^2 \rangle > 0$.

If rigorous, this bridges:
- QFT renormalization data ($\beta(g)$, condensates)
- Geometric/functional inequality data (Bakry–Émery bounds)

### C. Log-Forest UV Control as LSI Scaling (Speculative)

Log-Sobolev on gauge-orbit space:
$$
\mathrm{Ent}_{\mu_a}(f^2) \le C_{LS}(a) \int |\nabla f|^2 d\mu_a
$$

**Conjectural improvement for gauge-invariant observables:**
$$
C_{LS}(a) \lesssim \left(\log \frac{1}{a}\right)^p
$$
instead of power-law blowup.

**Physical intuition:** Gauge redundancy "prunes a forest of UV noise" → multiscale errors summable.

---

# Chapter 2: The Entropic Gribov Spark

## 2.1 The Geometric Setup

### The Configuration Space

Work in a Landau-type gauge fixing where gauge fields are represented as a vector $A$ in a huge-dimensional linear space (lattice gauge potential variables, after gauge fixing).

**Dimension estimate:** For a lattice with $L^d$ sites in $d$ dimensions:
$$
D = \#\text{links} \times \dim(\mathfrak{g}) = d \cdot L^d \times (N^2 - 1)
$$

For $SU(3)$ on a $16^4$ lattice: $D \approx 4 \times 65536 \times 8 \approx 2 \times 10^6$ dimensions.

### The Fundamental Modular Region

Gauge fixing restricts the functional integral to a **fundamental domain** $\mathcal{F}$ (the Fundamental Modular Region, FMR).

**Key structural assumptions:**
1. $\mathcal{F} \subset \mathbb{R}^D$ is **convex** and **bounded** in gauge-fixed coordinates
2. The boundary of $\mathcal{F}$ touches the **Gribov horizon** $\partial\Omega$
3. The Gribov horizon is where the Faddeev-Popov operator develops a zero mode:
$$
\partial\Omega = \{A : \det(-\nabla \cdot D(A)) = 0\}
$$

where $D_\mu(A) = \partial_\mu + ig[A_\mu, \cdot]$ is the covariant derivative.

## 2.2 The IR/UV Decomposition

### Variable Splitting

Split the configuration space into infrared and ultraviolet parts:
$$
A = A_{\mathrm{IR}} \oplus A_{\mathrm{UV}}, \quad A_{\mathrm{IR}} \in \mathbb{R}^k, \quad A_{\mathrm{UV}} \in \mathbb{R}^{D-k}
$$

where $k \ll D$ (a few IR modes vs. millions of UV modes).

Let $P : \mathbb{R}^D \to \mathbb{R}^k$ be the projection onto IR coordinates:
$$
Y := P(A) \in \mathbb{R}^k
$$

### The Marginal Density

The marginal density of the IR variable $Y$ is obtained by integrating out UV modes **within the constrained domain**:
$$
\rho_{\mathrm{IR}}(y) = \int_{\{A \in \mathcal{F} : P(A) = y\}} e^{-S(A)}\, dA_{\mathrm{UV}}
$$

Equivalently:
$$
\rho_{\mathrm{IR}}(y) = \int_{\mathbb{R}^{D-k}} e^{-S(y,z)}\, \mathbf{1}_{\mathcal{F}}(y,z)\, dz
$$

### The Effective Potential

Define the **IR effective potential**:
$$
\boxed{V_{\mathrm{eff}}(y) := -\log \rho_{\mathrm{IR}}(y)}
$$

**Key insight:** If $V_{\mathrm{eff}}$ is **uniformly strongly convex** near the origin, that constitutes an IR Spark.

## 2.3 The Entropic Mechanism — Why It Works

### Decomposition into Energy and Entropy

The effective potential decomposes as:
$$
V_{\mathrm{eff}}(Y) = E(Y) - \log \mathrm{Vol}(Y)
$$

where:
- **Energetic term** $E(Y)$: Yang-Mills action evaluated/optimized along the fiber
- **Entropic term** $-\log \mathrm{Vol}(Y)$: Minus log of the fiber volume

### Why the Entropic Term Dominates

1. **$E(Y)$ is approximately flat** for small $Y$ — this corresponds to massless bare gluons in the classical theory

2. **The constraint $\Lambda$ becomes tighter** as $Y$ moves away from the origin due to proximity to the Gribov horizon

3. **$\mathrm{Vol}(Y)$ shrinks** as $Y$ increases — fewer UV configurations fit inside $\mathcal{F}$

4. **$-\log \mathrm{Vol}(Y)$ rises** away from the origin — this is **entropic confinement**

**Physical interpretation:** Mass generation from the **geometry of the allowed region**, not from an explicit mass term in the action.

## 2.4 Conjecture 3.1 — The Precise Target

### Statement

**Conjecture 3.1 (Entropic Gribov Spark).**
There exists a fixed $k$ (number of IR modes) and a scale $m_*^2 > 0$, **independent of the UV dimension $D$**, such that for the gauge-fixed fundamental domain $\mathcal{F}$ and the induced IR effective potential $V_{\mathrm{eff}}$:
$$
\boxed{\nabla^2 V_{\mathrm{eff}}(0) \succeq m_*^2\, I_k}
$$

### Stronger Version

There exists a neighborhood $U \ni 0$ such that:
$$
\nabla^2 V_{\mathrm{eff}}(y) \succeq m_*^2\, I_k \quad \text{for all } y \in U
$$

### Physical Interpretation

The IR marginal is approximately Gaussian near $y = 0$:
$$
\rho_{\mathrm{IR}}(y) \approx \exp\left(-\frac{m_*^2}{2}\|y\|^2\right)
$$

This Gaussian behavior emerges **not because the action is quadratic**, but because the **available volume in the fiber shrinks quadratically** as you move in IR directions — a pure boundary-entropy effect.

## 2.5 Mathematical Foundation: High-Dimensional Convexity

### The Central Limit Phenomenon for Convex Bodies

Even with $S \equiv 0$ (uniform measure on $\mathcal{F}$), high-dimensional convex bodies exhibit a famous phenomenon:

> **Low-dimensional marginals of high-dimensional convex bodies often look Gaussian.**

**Precise theorem:** For fixed $k$, a random $k$-dimensional projection of an isotropic log-concave measure on $\mathbb{R}^D$ converges to a standard Gaussian as $D \to \infty$ (under suitable regularity assumptions).

### Application to Gribov

If $\rho_{\mathrm{IR}}$ is close to Gaussian in distribution, then:
$$
-\log \rho_{\mathrm{IR}} \approx \frac{m^2}{2}\|y\|^2 + \text{const}
$$

implying a positive definite Hessian at the origin.

### The Gribov Horizon as Extra Structure

The Gribov horizon $\partial\Omega$ is defined by a **spectral constraint**: the smallest eigenvalue of the Faddeev-Popov operator hitting zero.

**Key property:** Boundaries defined by spectral constraints can be **very curved** in high dimensions — exactly what is needed for a strong entropic quadratic term.

## 2.6 The Brunn-Minkowski Connection

### Prekopa-Leindler Inequality

If $\Lambda \subset \mathbb{R}^D$ is a **convex body** and $Y = P(A)$ is a linear projection, then the slice volumes:
$$
\mathrm{Vol}(Y) := \mathrm{Vol}\{A \in \Lambda : P(A) = Y\}
$$
are **log-concave** in $Y$ under broad conditions.

### Implication for the Effective Potential

Log-concavity of $\mathrm{Vol}(Y)$ implies **convexity** of $-\log \mathrm{Vol}(Y)$.

This is the mathematical skeleton:
$$
\boxed{\text{high dimension} + \text{hard walls} \Rightarrow \text{entropic convexity}}
$$

### What Remains for Rigor

1. Show the relevant $\Lambda$ is convex (or "convex enough") in orbit space
2. Obtain **strict** convexity with **quantitative** curvature scale $\sim \gamma^2$
3. Prove the IR variable $Y$ is the "right" projection for dynamics and correlation decay

---

# Chapter 3: The Weyl Denominator Spark

## 3.1 Coarse Variables as Conjugacy Classes

Block holonomies $U_{\square}^{(\ell)}$ transform by conjugation under gauge transformations:
$$
U \mapsto gUg^{-1}
$$

**Key insight:** The gauge-invariant content of a holonomy is its **conjugacy class**.

For $G = SU(N)$, conjugacy classes are parametrized by eigenvalues. Any $U \in SU(N)$ is conjugate to a diagonal matrix:
$$
U \sim \mathrm{diag}(e^{i\theta_1}, \ldots, e^{i\theta_N}), \quad \sum_{i=1}^N \theta_i = 0 \pmod{2\pi}
$$

The orbit space is:
$$
SU(N) / \mathrm{Ad}(SU(N)) \cong T / W
$$
where $T$ is the maximal torus and $W = S_N$ is the Weyl group (permutations of eigenvalues).

## 3.2 The Weyl Integration Formula

**Theorem (Weyl).** For any class function $f : G \to \mathbb{C}$ (i.e., $f(hgh^{-1}) = f(g)$):
$$
\int_G f(g)\, dg = \frac{1}{|W|} \int_T f(t)\, |\Delta(t)|^2\, dt
$$

where $dg$ is normalized Haar measure on $G$, $dt$ is normalized Haar measure on $T$, and $\Delta$ is the **Weyl denominator**.

## 3.3 The Weyl Denominator — Explicit Form

For $SU(N)$ with eigenangles $\theta = (\theta_1, \ldots, \theta_N)$ satisfying $\sum_i \theta_i = 0$:
$$
\Delta(\theta) = \prod_{1 \le i < j \le N} \left(e^{i\theta_i/2} - e^{-i\theta_i/2}\right)\left(e^{-i\theta_j/2} - e^{i\theta_j/2}\right)^{-1} \cdot \ldots
$$

Simplifying:
$$
|\Delta(e^{i\theta})|^2 = \prod_{i < j} |e^{i\theta_i} - e^{i\theta_j}|^2 = \prod_{i<j} 4\sin^2\left(\frac{\theta_i - \theta_j}{2}\right)
$$

**Physical meaning:** $|\Delta|^2$ measures the "volume" of gauge orbits. Near eigenvalue collisions ($\theta_i = \theta_j$), this vanishes — those are **reducible configurations** (larger stabilizers).

## 3.4 The Geometric Potential

Define the orbit-space density function:
$$
w(\theta) := |\Delta(e^{i\theta})|^2 = \prod_{i<j} 4\sin^2\left(\frac{\theta_i - \theta_j}{2}\right)
$$

The **geometric potential** is:
$$
S_{\mathrm{geom}}(\theta) := -\log w(\theta) = -\sum_{i<j} \log\left(4\sin^2\frac{\theta_i - \theta_j}{2}\right)
$$

**Note:** At eigenvalue collisions, $S_{\mathrm{geom}} \to +\infty$ — an infinite repulsive wall.

## 3.5 Computing the Hessian — Step by Step

### Step 1: First Derivatives

Let $\phi_{ij} := \frac{\theta_i - \theta_j}{2}$. Consider one term in the sum:
$$
f_{ij}(\theta) := -\log(4\sin^2\phi_{ij}) = -\log 4 - 2\log|\sin\phi_{ij}|
$$

First derivative with respect to $\theta_i$:
$$
\frac{\partial f_{ij}}{\partial \theta_i} = -2 \cdot \frac{\cos\phi_{ij}}{\sin\phi_{ij}} \cdot \frac{1}{2} = -\cot\phi_{ij}
$$

Similarly, $\frac{\partial f_{ij}}{\partial \theta_j} = +\cot\phi_{ij}$.

### Step 2: Second Derivatives

For $i \neq j$:
$$
\frac{\partial^2 f_{ij}}{\partial \theta_i^2} = \frac{1}{2}\csc^2\phi_{ij}, \quad \frac{\partial^2 f_{ij}}{\partial \theta_i \partial \theta_j} = -\frac{1}{2}\csc^2\phi_{ij}
$$

### Step 3: Full Hessian Structure

Define the **edge weight**:
$$
w_{ij}(\theta) := \csc^2\left(\frac{\theta_i - \theta_j}{2}\right) \ge 1 \quad \text{(since } \sin^2 \le 1\text{)}
$$

Summing over all pairs, the Hessian entries are:
$$
\frac{\partial^2 S_{\mathrm{geom}}}{\partial \theta_i \partial \theta_j} = -\frac{1}{2} w_{ij}(\theta) \quad (i \neq j)
$$
$$
\frac{\partial^2 S_{\mathrm{geom}}}{\partial \theta_i^2} = \frac{1}{2} \sum_{k \neq i} w_{ik}(\theta)
$$

### Step 4: Recognition as Graph Laplacian

This is exactly the structure of a **weighted graph Laplacian** on the complete graph $K_N$:
$$
\boxed{\nabla^2 S_{\mathrm{geom}}(\theta) = \frac{1}{2} L_{w(\theta)}}
$$

where $(L_w)_{ij} = -w_{ij}$ for $i \neq j$ and $(L_w)_{ii} = \sum_{k \neq i} w_{ik}$.

**Quadratic form:**
$$
x^\top \nabla^2 S_{\mathrm{geom}}(\theta)\, x = \frac{1}{4} \sum_{i < j} w_{ij}(\theta) (x_i - x_j)^2
$$

## 3.6 The Uniform Lower Bound — Full Proof

**Goal:** Show $\nabla^2 S_{\mathrm{geom}} \ge \frac{N}{4} I$ on the constraint hyperplane $\sum_i x_i = 0$.

### Step 1: Use the Weight Lower Bound

Since $w_{ij}(\theta) \ge 1$ everywhere (away from collisions):
$$
x^\top \nabla^2 S_{\mathrm{geom}}(\theta)\, x \ge \frac{1}{4} \sum_{i < j} (x_i - x_j)^2
$$

### Step 2: Algebraic Identity

**Claim:** For any $x \in \mathbb{R}^N$:
$$
\sum_{i < j} (x_i - x_j)^2 = N \sum_{i=1}^N x_i^2 - \left(\sum_{i=1}^N x_i\right)^2
$$

**Proof:** Expand the left side:
$$
\sum_{i < j} (x_i - x_j)^2 = \sum_{i < j} (x_i^2 - 2x_i x_j + x_j^2)
$$
$$
= (N-1)\sum_i x_i^2 - 2\sum_{i<j} x_i x_j
$$

Now use:
$$
\left(\sum_i x_i\right)^2 = \sum_i x_i^2 + 2\sum_{i<j} x_i x_j
$$

Substituting:
$$
\sum_{i < j} (x_i - x_j)^2 = (N-1)\sum_i x_i^2 - \left[\left(\sum_i x_i\right)^2 - \sum_i x_i^2\right]
$$
$$
= N\sum_i x_i^2 - \left(\sum_i x_i\right)^2 \quad \checkmark
$$

### Step 3: Apply the Constraint

On the $SU(N)$ tangent hyperplane, $\sum_i x_i = 0$. Therefore:
$$
\sum_{i < j} (x_i - x_j)^2 = N \sum_i x_i^2 = N \|x\|^2
$$

### Step 4: Conclude

$$
x^\top \nabla^2 S_{\mathrm{geom}}(\theta)\, x \ge \frac{1}{4} \cdot N \|x\|^2 = \frac{N}{4} \|x\|^2
$$

Therefore:
$$
\boxed{\nabla^2 S_{\mathrm{geom}} \Big|_{\sum x_i = 0} \ge \frac{N}{4} I}
$$

**Explicit values:**
- For $SU(2)$: $\sigma_{\mathrm{geom}} = \frac{2}{4} = \frac{1}{2}$
- For $SU(3)$: $\sigma_{\mathrm{geom}} = \frac{3}{4}$

**This is the cleanest $a$-independent positive source term.**

## 3.5 Lattice Consequence

If coarse-graining produces holonomies $\{U_{\square}^{(\ell)}\}$, the total geometric potential includes:
$$
S_{\mathrm{geom}}^{(\ell)} \supset \sum_{\square} S_{\mathrm{Weyl}}\big(\theta(U_{\square}^{(\ell)})\big)
$$

Its Hessian contains a **block-diagonal sum of complete-graph Laplacians**, each with explicit lower bound $N/4$.

**The Weyl denominator insight:**
> "If you try to make eigenvalues collide (drift toward reducibility), I will punish you with infinite action curvature."

That punishment is a weighted Laplacian—exactly what spectral-gap proofs like to eat for breakfast.

---

# Chapter 4: The FP/Gram Determinant

## 4.1 Configuration Space and Gauge Group

### The Setup

Let the lattice configuration space be:
$$
\mathcal{C}_\Lambda = G^{|B|}, \quad G = SU(N)
$$
with product bi-invariant metric, where $|B|$ is the number of lattice bonds (links).

The lattice gauge group is:
$$
\mathcal{G}_\Lambda = G^{|V|}
$$
acting by:
$$
(g \cdot U)_{xy} = g_x\, U_{xy}\, g_y^{-1}
$$

### The Principal Stratum

On the **principal stratum** $\mathcal{C}_\Lambda^{\mathrm{irr}}$ (irreducible configurations):
- The stabilizer is discrete (center $Z_N$)
- The action is infinitesimally free
- The quotient is a smooth orbifold/manifold:
$$
\mathcal{O}_\Lambda^{\mathrm{irr}} := \mathcal{C}_\Lambda^{\mathrm{irr}} / \mathcal{G}_\Lambda
$$

## 4.2 The Riemannian Jacobian of the Quotient Map

### Vertical-Horizontal Decomposition

Let $\pi : \mathcal{C}^{\mathrm{irr}} \to \mathcal{O}^{\mathrm{irr}}$ be the quotient map.

For an isometric group action, there is a canonical decomposition:
$$
T_U \mathcal{C} = V_U \oplus H_U
$$
where:
- $V_U$ = **vertical** (tangent to gauge orbits)
- $H_U$ = **horizontal** (orthogonal complement)

### The Gram Matrix

The **induced measure** on orbit space differs from quotient Riemannian volume by an **orbit-volume density**.

Pick an orthonormal basis $\{\xi^{(a)}\}$ of $\mathrm{Lie}(\mathcal{G})$. The corresponding Killing vector fields $K_a(U) \in V_U$ have Gram matrix:
$$
M_U := \big(\langle K_a(U), K_b(U) \rangle\big)_{ab}
$$

Then the orbit-volume factor is:
$$
\mathrm{vol}(\mathcal{G} \cdot U) \propto \sqrt{\det M_U}
$$

This is the **coordinate-free origin** of the Faddeev-Popov determinant on orbit space.

## 4.3 Identifying $M_U$ as a Covariant Graph Laplacian

### The Infinitesimal Gauge Action

A gauge parameter $\xi = \{\xi_x\}_{x \in V}$ with $\xi_x \in \mathfrak{su}(N)$ generates a vertical variation on link $b = (x \to y)$:
$$
\delta U_b \sim \xi_x\, U_b - U_b\, \xi_y
$$

Using bi-invariance, the squared norm is:
$$
\|\delta U_b\|^2 \simeq \|\xi_x - \mathrm{Ad}_{U_b}\, \xi_y\|^2
$$

### The Lattice Covariant Derivative

Define:
$$
\boxed{(D_U \xi)_b := \xi_x - \mathrm{Ad}_{U_b}\, \xi_y \quad (b : x \to y)}
$$

### The Orbit Metric

The orbit metric is:
$$
\|\delta U\|^2_{\mathrm{vert}} = \sum_{b \in B} \|(D_U \xi)_b\|^2 = \langle \xi, (D_U^* D_U)\, \xi \rangle
$$

Therefore (up to constants):
$$
\boxed{M_U = D_U^* D_U, \quad \Delta_{\mathrm{FP}}(U) := \det(D_U^* D_U)}
$$

## 4.4 Connection to Reducibility

### When $D_U$ Has a Kernel

$D_U$ has a nontrivial kernel iff there exists a nonzero covariantly constant adjoint field $\xi$ with:
$$
\xi_x = \mathrm{Ad}_{U_b}\, \xi_y \quad \text{along every link}
$$

This is exactly the **reducibility condition** — having a nontrivial global symmetry.

### Consequences

| Configuration | $D_U$ | $\Delta_{\mathrm{FP}}(U)$ | $S_{\mathrm{FP}}$ |
|:-------------|:------|:------------------------|:----------------|
| Irreducible | injective | $> 0$ | finite |
| Reducible | has kernel | $= 0$ | $\to +\infty$ |

The potential $S_{\mathrm{FP}} := -\frac{1}{2}\log \Delta_{\mathrm{FP}}$ creates a **repulsive wall** at singular strata.

## 4.5 Hessian of the FP Determinant — Sum of Squares Structure

### The Geometric Potential

Define:
$$
S_{\mathrm{orb}}(U) := -\log \mathrm{vol}(\mathcal{G} \cdot U) = -\frac{1}{2} \log \det(D_U^* D_U)
$$

### Computing the Hessian

Let $M(U) = D_U^* D_U$. On principal stratum, $M(U)$ is positive definite.

**Standard matrix calculus identities:**
$$
\delta \log \det M = \mathrm{Tr}(M^{-1} \delta M)
$$
$$
\delta^2 \log \det M = \mathrm{Tr}(M^{-1} \delta^2 M) - \mathrm{Tr}(M^{-1} \delta M\, M^{-1} \delta M)
$$

Therefore:
$$
\boxed{\delta^2 S_{\mathrm{orb}}(U) = -\frac{1}{2}\mathrm{Tr}(M^{-1}\delta^2 M) + \frac{1}{2}\underbrace{\mathrm{Tr}(M^{-1}\delta M\, M^{-1}\delta M)}_{\ge 0}}
$$

### Structure Analysis

The second term is a **trace of a square** — manifestly **nonnegative**.

**What this buys you:**
- If $\mathrm{Tr}(M^{-1}\delta^2 M)$ is bounded above by $C\|\delta U\|^2$, then:
$$
\mathrm{Hess}\, S_{\mathrm{orb}} \ge -C\, I + (\text{positive semidefinite})
$$

**Near reducibles:** $M^{-1}$ becomes large → positive term $\mathrm{Tr}(M^{-1}\delta M\, M^{-1}\delta M)$ blows up → **strongly convex wall**.

## 4.6 Why This Is a Natural Convexity Source

The orbit-volume determinant has key properties:

1. **Comes from quotient geometry** — not from the Wilson action
2. **Is naturally dimensionless** — orbit-volume collapse is geometric
3. **Has Laplacian structure** — $M = D_U^* D_U$ is a covariant graph Laplacian
4. **Survives coarse-graining** — Weyl/FP factors are preserved under gauge-equivariant smoothing

This meshes with the **polarity-of-reducibles** theme: if reducibles are polar, the orbit space is "analytically equivalent" to its principal stratum where the FP determinant provides clean convexity.

---

# Chapter 5: Continuum Limit Machinery

## 5.1 Overview: The Three-Bridge Strategy

Passing lattice results to the continuum requires three bridges:

| Bridge | Technical Tool | Purpose |
|:-------|:---------------|:--------|
| 1. Measure-theoretic | Projective limits | Construct $\mu$ from $\{\mu_a\}$ |
| 2. Analytic | Mosco convergence | Pass Dirichlet forms $\mathcal{E}_a \to \mathcal{E}$ |
| 3. Physical | Reflection positivity | Ensure OS axioms for reconstruction |

## 5.2 Bridge 1: Projective Limits for Measures

### The Setup

Let $\{\mathcal{A}_a\}_{a>0}$ denote lattice configuration spaces at mesh $a$, and let:
$$
\pi_{a' \to a} : \mathcal{A}_{a'} \to \mathcal{A}_a
$$
be the natural coarse-graining map (forgetting fine links or averaging).

### The Consistency Condition

A projective system of measures is a family $\{\mu_a\}$ such that:
$$
(\pi_{a' \to a})_\# \mu_{a'} = \mu_a \quad (a' < a)
$$

This says: pushing forward the fine measure gives the coarse measure.

### Kolmogorov Extension

If the family is **tight** in a suitable topology, the Kolmogorov extension theorem produces a limit measure $\mu$ on a continuum configuration space $\mathcal{A}$ whose cylinder measures agree with $\mu_a$.

**Why this works for gauge theory:** Gauge fields are naturally specified by holonomies on paths, and "restriction to coarser graph" is canonical.

## 5.3 Bridge 2: Mosco Convergence of Dirichlet Forms

### Definition of Dirichlet Forms

Given a symmetric Markov semigroup $P_t^{(a)}$ on $L^2(\mu_a)$ with generator $L_a$, define:
$$
\mathcal{E}_a(f, f) := \langle f, -L_a f \rangle_{L^2(\mu_a)}
$$

### Mosco Convergence

**Definition.** $\mathcal{E}_a \to \mathcal{E}$ in the Mosco sense if:

1. **Liminf condition:** For every $f_a \to f$ weakly, $\liminf_a \mathcal{E}_a(f_a) \ge \mathcal{E}(f)$
2. **Limsup condition:** For every $f$, there exist $f_a \to f$ strongly with $\limsup_a \mathcal{E}_a(f_a) \le \mathcal{E}(f)$

### Consequences of Mosco Convergence

Together with tightness and core density conditions, Mosco convergence implies:
- Strong resolvent convergence of generators
- Convergence of semigroups on a dense class
- **Lower semicontinuity of spectral quantities**

**Key implication:** If $\lambda_1^{(a)} \ge c > 0$ for all $a$, then $\lambda_1 \ge c$ in the limit.

## 5.4 Bridge 3: Reflection Positivity Transfer

### The Lattice RP Condition

Assume each lattice measure $\mu_a$ is reflection positive with respect to a time hyperplane. For each $a$:
$$
\langle \Theta F \cdot F \rangle_{\mu_a} \ge 0 \quad \text{for all } F \text{ supported at positive times}
$$

where $\Theta$ is the time-reflection operator.

### The Transfer Argument

1. RP inequalities hold for **cylinder functions** (depending on finitely many links)
2. Cylinder functions are stable under pullback/pushforward by projective maps
3. If $\mu$ exists and agrees on cylinders, the same inequality holds under $\mu$
4. By density/closure, extend RP to appropriate function class in $L^2(\mu)$

### Physical Consequence

If successful, **Osterwalder-Schrader reconstruction** can be carried out at the limit measure $\mu$, yielding:
- A continuum Hilbert space $\mathcal{H}$
- A semigroup of time translations $e^{-tH}$
- A self-adjoint Hamiltonian $H \ge 0$

## 5.5 The Compactness Pipeline via LSI

The functional inequality chain for tightness:
$$
\boxed{CD(\rho, \infty) \Rightarrow LSI(\rho) \Rightarrow \text{Gaussian concentration} \Rightarrow \text{exponential moments} \Rightarrow \text{tightness}}
$$

### Explanation of Each Step

1. **Curvature-dimension bound $CD(\rho, \infty)$:** Bakry-Émery curvature $\ge \rho > 0$
2. **Log-Sobolev inequality:** $\mathrm{Ent}_\mu(f^2) \le \frac{2}{\rho} \int |\nabla f|^2 d\mu$
3. **Gaussian concentration:** Lipschitz functions concentrate around their mean
4. **Exponential moments:** $\mathbb{E}[e^{\lambda X}] < \infty$ for suitable $\lambda$
5. **Tightness:** Prokhorov's theorem gives subsequential limits

## 5.6 The Scaling Bottleneck

### The Critical Question

Everything above is **powerless if the key constants degenerate as $a \to 0$**.

### Two Competing Scaling Intuitions

**(A) Haar baseline survives:**
- Haar geometry gives a **dimensionless** curvature baseline in link variables
- A nonvanishing constant $\kappa_* > 0$ at each scale could provide an RG-stable anchor

**(B) Wilson quadratic term collapses:**
- Write link variables as $U = \exp(aA)$ with continuum field $A$
- Derivatives in $U$ correspond to $a$-scaled derivatives in $A$
- In naive continuum scaling: $S_W \sim \beta \sum_p a^4 \|F\|^2$
- Discrete gradients scale like $a^{-2}$ for Laplacian-type operators
- Product $\beta a^2 \sim \log(1/a) \cdot a^2 \to 0$

### The Resolution: Coordinate Conventions Matter

These statements can be consistent only after choosing a **precise identification** between:
1. The tangent norm on $SU(N)$
2. The normalization of lattice gauge coupling $\beta$
3. The scaling $U = \exp(aA)$

Because convexity is a **second derivative** object, it is extremely sensitive to whether one differentiates with respect to:
- $U$-coordinates (dimensionless)
- $A$-coordinates (dimensionful)

**A publishable continuum argument must fix this carefully and track how the metric rescales.**

## 5.7 Concrete Checklist for the Continuum Step

| Step | Task |
|:-----|:-----|
| 1 | Define continuum configuration space $\mathcal{A}$ and projective maps $\pi_{a' \to a}$ |
| 2 | Prove **tightness** (or equivalent compactness criterion) for $\{\mu_a\}$ |
| 3 | Show **RP is stable** under projective limit on cylinder functions |
| 4 | Define Dirichlet forms $\mathcal{E}_a$ with consistent scaling; prove Mosco convergence |
| 5 | Establish **spectral gap / LSI constants do not vanish** under chosen scaling |
| 6 | Reconstruct OS Hilbert space; prove limiting Hamiltonian has nonzero gap |

---

# Chapter 6: The Dichotomy Theorem

## 6.1 Statement and Strategic Value

**Theorem (Dichotomy).** If the continuum limit exists as a genuine 4D $SU(N)$ Yang-Mills QFT, then exactly one of the following is true:
$$
\boxed{\text{Either } \Delta_{\mathrm{cont}} > 0 \text{ (mass gap persists)} \text{ or } \Delta_{\mathrm{cont}} = 0 \text{ (gap collapses)}}
$$

**Why this is valuable:** This is nearly tautological, but the **strategic value** is:
- The program becomes **modular**
- "Failure to prove the gap" becomes "evidence about which branch"
- The problem is carved into a mathematically and numerically **testable dichotomy**

## 6.2 The Road to the Continuum

Five steps to a rigorous continuum mass gap:

| Step | Content |
|:-----|:--------|
| 1 | **Finite-cutoff gap:** $\Delta(a) > 0$ for each $a > 0$ |
| 2 | **Tightness:** the family $\{\mu_a\}$ is compact in some topology |
| 3 | **Accumulation points:** extract a subsequence with limit $\mu$ |
| 4 | **Reconstruction:** build Hilbert space and Hamiltonian $H_{\mathrm{cont}}$ |
| 5 | **Gap passage:** show $\Delta_{\mathrm{cont}} > 0$ |

**Project status:** Step 1 mechanism is geometrically explicit. Steps 2-5 are the "big beast" that remains.

## 6.3 What the Project Claims (Inventory)

**Complete:**
- Conditional persistence theorem (PBH flow + Riccati comparison)
- Anomaly source positivity in multiple regimes
- Structural tools (polarity, sectoring, Riccati dynamics)

**Remaining obstacles:**
1. **Uniform trace bound along flow** (hypothesis H2 in PBH framework)
2. **Continuum limit:** uniform control as $a \to 0$ and OS reconstruction with persistent gap

This is a **clean, non-handwavy situation**: it tells you exactly what to prove and what can be falsified numerically.

## 6.4 The Uniformity Challenge

The tightness pipeline:
$$
CD(\rho, \infty) \Rightarrow LSI(\rho) \Rightarrow \text{Gaussian concentration} \Rightarrow \text{exponential moments} \Rightarrow \text{tightness}
$$

**The hard part:** Asymptotic freedom pushes $g(a) \to 0$ as $a \to 0$.

Any curvature constant of the form $\rho_a \sim g(a)^2 a^2$ will **not** stay bounded below.

**Precise research question (from source):**
> Find the right "renormalized" coercivity functional whose concentration constants scale correctly with $a$ along the RG trajectory.

---

# Chapter 7: Compact QED₃ as Benchmark

## 7.1 Why This Example Matters

Compact $U(1)$ gauge theory in 3 dimensions provides a **proof-of-concept** that nonperturbative objects can generate Sparks.

**Key features:**
- Naively, photon is massless (no scale in Maxwell action)
- Compact $U(1)$: monopoles exist as field configurations
- Result: proliferating monopoles generate a mass gap

This is an **explicit example** where a topological mechanism creates strictly positive curvature in the IR effective action.

## 7.2 Polyakov's Duality Argument

### The Dual Photon

For compact $U(1)$ gauge theory, one can dualize the photon field $A_\mu$ to a scalar "dual photon" $\phi$ via:
$$
F_{\mu\nu} \longleftrightarrow \varepsilon_{\mu\nu\rho} \partial^\rho \phi
$$

### The Sine-Gordon Action

Monopoles appear as sources in the dual picture. The effective action becomes:
$$
S_{\mathrm{dual}}(\phi) = \int_{\mathbb{R}^3} \left(\frac{1}{2e^2}|\nabla\phi|^2 - 2\zeta \cos\phi\right) dx
$$

where:
- $e$ = gauge coupling
- $\zeta > 0$ = **monopole fugacity** (density of monopole instantons)

### Expanding the Cosine

Near the vacuum $\phi = 0$:
$$
-2\zeta\cos\phi = -2\zeta\left(1 - \frac{\phi^2}{2} + O(\phi^4)\right) = \text{const} + \zeta\phi^2 + O(\phi^4)
$$

### The Generated Mass

The effective potential has curvature $\zeta > 0$ at the minimum, producing:
$$
\boxed{m^2 \sim \zeta e^2}
$$

**Physical interpretation:** The cosine term is a pure **nonperturbative effect** — monopole instantons create a periodic potential that lifts the photon mass from zero.

## 7.3 Template for Yang-Mills

The QED₃ mechanism suggests for 4D YM:

| QED₃ | 4D YM Analog |
|:-----|:-------------|
| Compact $U(1)$ | $SU(N)$ |
| Monopole fugacity $\zeta$ | Gribov/entropic curvature $m_*^2$ |
| Cosine potential | Boundary-entropy potential |
| $m^2 \sim \zeta e^2$ | $m^2 \sim m_*^2$ |

**Key lesson:** Nonperturbative topological/geometric objects can generate mass where perturbation theory predicts masslessness.

---

# Chapter 8: Multiscale Recursion Blueprint

## 8.1 The Framework

The Spark → Gap pipeline operates scale-by-scale. Represent the convexity/gap parameter at scale $j$ by $\rho_j \ge 0$.

### The Recursion Relation

Under coarse-graining from scale $j$ to $j+1$:
$$
\boxed{\rho_{j+1} \ge K\rho_j - \varepsilon_j + \sigma_*}
$$

where:
- $K \in (0,1]$: contraction factor (convexity partially preserved)
- $\varepsilon_j \ge 0$: entropy cost of coarse-graining step
- $\sigma_* > 0$: scale-independent positive source (the **Spark**)

## 8.2 Fixed-Point Analysis

### Iterating the Recursion

If $K < 1$ and $\sigma_* > 0$, the recursion has a positive fixed point:
$$
\rho_* = K\rho_* - \bar{\varepsilon} + \sigma_* \implies \rho_* = \frac{\sigma_* - \bar{\varepsilon}}{1 - K}
$$

For $\rho_* > 0$, need:
$$
\sigma_* > \bar{\varepsilon}
$$

### The Convergence Condition

Starting from $\rho_0 = 0$ (no initial curvature):
$$
\rho_j \to \rho_* > 0 \quad \text{if } \sigma_* > 0 \text{ and } \sum_j \varepsilon_j < \infty
$$

## 8.3 Physical Meaning of Each Term

| Term | Physical Origin | Requirement |
|:-----|:---------------|:------------|
| $K\rho_j$ | Curvature inherited from coarser scale | $K > 0$ (don't lose everything) |
| $-\varepsilon_j$ | Entropy production under coarse-graining | Summably small |
| $+\sigma_*$ | Scale-independent source (Spark) | $\sigma_* > 0$ (proved or conjectured) |

## 8.4 The Two Central Tasks

### Task 1: Prove the Spark

Establish $\sigma_* > 0$ via one of:
- **Weyl Hessian:** $\sigma_{\mathrm{geom}} = N/4$ (Chapter 3)
- **Entropic Gribov:** Conjecture 3.1 (Chapter 2)
- **Anomaly mechanism:** trace anomaly contribution

### Task 2: Control the Entropy Costs

Show $\sum_j \varepsilon_j < \infty$ using:
- **Log-Sobolev inheritance:** $C_{LS}(a)$ polylogarithmic in $1/a$
- **Cluster expansion:** small-field/large-field decomposition
- **Heat kernel smoothing:** each step costs $O(g^2)$, summable along RG

## 8.5 Connection to Riccati Dynamics

The recursion is the discrete analogue of the Riccati ODE:
$$
\dot{\lambda} = -2\lambda^2 + \sigma_*
$$

**With $\sigma_* > 0$:** Fixed point at $\lambda_* = \sqrt{\sigma_*/2} > 0$

**Without $\sigma_*$:** Decay $\lambda(t) \sim 1/(2t) \to 0$ (gapless)

The discrete recursion "samples" this flow at RG blocking steps.

---

# Chapter 9: Summary

## 9.1 Three Spark Candidates

| Spark | Mechanism | Scale |
|:------|:----------|:------|
| Entropic Gribov | Fiber volume shrinkage | Gribov scale $\gamma$ |
| Weyl Denominator | Complete-graph Laplacian | $\sigma_{\mathrm{geom}} \ge N/4$ |
| Anomaly Curvature | Trace anomaly as source | $\beta(g)/g$ |

## 9.2 Key Theorems

| # | Statement | Source |
|:--|:----------|:-------|
| 1 | Weyl Hessian $\ge N/4$ on constraint | 06_fp_weyl |
| 2 | Entropic Spark Conjecture 3.1 | RECOMMENDED_04 |
| 3 | Riccati attractor from positive source | 04_continuum |
| 4 | Dichotomy (gap or gapless) | PROOFS_Selected_5 |
| 5 | Mosco convergence → spectral LSC | Continuum_limit |

## 9.3 State Space Cleanup (from Pass 3-4)

**Polarity of Reducibles:**
- $\mathrm{codim}(\Sigma) \ge 1$ for $N \ge 2$
- Reducibles are polar (zero capacity) for Dirichlet form
- "Almost surely, theory lives on regular stratum"

**C-Sector Decomposition:**
$$\mathcal{H} = \mathcal{H}^+ \oplus \mathcal{H}^-$$
- $[C, H] = 0$ → mass gap factorizes into two problems
- For SU(2): $\mathcal{H}^- = \{0\}$

**Tubular Neighborhood:**
- Uniform geometry near flat stratum $\mathcal{F}_a$
- O'Neill formulas control quotient curvature
- Targets: slice theorem, injectivity radius control

## 9.4 What Remains

1. Prove Spark Conjecture 3.1 or Weyl stabilization
2. Uniform trace bound (H2 in PBH framework)
3. $\inf_{a \in (0, a_0]} \Delta(a) > 0$
4. OS reconstruction with persistent gap

---

# Chapter 10: Falsifiability and Research Program

## 10.1 Why This Conjecture Can Be Attacked

The Entropic Spark is valuable precisely because it is **falsifiable by computation** and approachable through convex geometry.

## 10.2 Numerical Test Protocol

**On small lattices ($4^4$, $6^4$):**

1. Perform Landau-gauge fixing
2. Restrict to Gribov region proxy
3. Compute lowest Fourier modes of $A$ (your $y$)
4. Empirically estimate $\rho_{\mathrm{IR}}(y)$
5. Fit $-\log\rho_{\mathrm{IR}}(y)$ near $y=0$ and estimate Hessian

**Failure criterion:** If Hessian is NOT bounded below away from $0$ as volume increases → strong evidence AGAINST the spark.

## 10.3 Analytic Toy Model Targets

Replace $\mathcal{F}$ by tractable convex body:
- Zonotope
- Spectrahedron
- Intersection of half-spaces

Compute fiber volume:
$$
y \mapsto \mathrm{Vol}\big(\mathcal{F} \cap P^{-1}(y)\big)
$$

Look for robust quadratic lower bound on $-\log$ near $y=0$.

## 10.4 Soft Theorem Approach

**Target statement:**
> If $\mu$ is log-concave on $\mathbb{R}^D$ and isotropic, then for typical $k$-dimensional projections the marginal density has a strictly positive Hessian at the origin with probability $\to 1$ as $D \to \infty$.

Even a weak version justifies a spark-like term.

## 10.5 Concrete Next Steps (from source files)

| Target | Description |
|:-------|:------------|
| Model problem | Explicit convex body $K \subset \mathbb{R}^n$, compute $\nabla^2(-\log\mathrm{Vol}_K(Y))$ |
| Quantitative log-concavity | Prekopa → Hessian bound via curvature of $\partial\Lambda$ |
| Link $\gamma$ to geometry | $\gamma^{-1} \sim R_{\mathrm{IR}}$ → $\gamma^2$ is natural curvature scale |
| Gauge-theory specificity | Show orbit-space inherits convexity after gauge fixing |

---

# Chapter 11: Files Reviewed

All 11 files in Topic_Continuum_Spark reviewed and copied to CRITICAL FILES.

| File | Key Content |
|:-----|:------------|
| RECOMMENDED_04 | Entropic Gribov Spark Conjecture |
| Continuum_limit_projective_Mosco_RP | Three-bridge strategy |
| 04_continuum_obstruction | Why Haar dies, candidate stabilizers |
| 06_fp_weyl_determinant | Weyl $\ge N/4$ theorem |
| PROOFS_Selected_5 | Dichotomy, tightness |
| 02_entropic_potential | Fiber volume mechanism |
| 03_sparks_compact_QED3 | Monopole benchmark |
| 05_sigma_geom_weyl | Scale-independent $\sigma_{\mathrm{geom}}$ |
| 07_heat_kernel_weyl | Heat kernel + Weyl |
| PROOFS_Selected_4 | Polarity and sectors |
| tubular_neighborhood | Flat stratum geometry |
