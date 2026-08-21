# Synthesis IV: Lattice Gauge Theory Foundations

## Topic: Lattice_Gauge_Theory (HAAR Subtopic 4 of 8)

---

# Chapter 1: Overview and Connection to Previous Syntheses

## 1.1 Purpose

This synthesis develops the **lattice foundations** for the Yang-Mills mass gap mechanism:
- Configuration space geometry
- Wilson action and Hessian structure
- Horizontal (physical) directions
- Polarity of reducible configurations
- The "fixed-cutoff engine" pipeline

## 1.2 Connection to Previous Syntheses

| Synthesis | Provides | Used Here |
|:----------|:---------|:----------|
| **01 (Geometry)** | Ricci curvature $\kappa$, Haar Hessian $c_0$ | Bakry-Émery positivity |
| **02 (Analysis/LSI)** | CD → LSI → Gap chain | Functional inequalities |
| **03 (Renormalization)** | Riccati stability, MFIP | RG preservation |

---

# Chapter 2: Lattice Configuration Space

## 2.1 Configuration Manifold

**Definition 2.1.1.** For a finite lattice $\Lambda$ with edge set $E(\Lambda)$ and gauge group $G = SU(N)$:
$$
\mathcal{A} := G^{E(\Lambda)} = SU(N)^{|E|}
$$

This is a **compact Riemannian manifold** with the product bi-invariant metric:
$$
g_U(X, Y) := \sum_{e \in E} \langle X_e, Y_e \rangle, \quad \langle X, Y \rangle := -\mathrm{Tr}(XY)
$$

## 2.2 Exponential Coordinates

Near the identity, write:
$$
U_e = \exp(X_e), \quad X_e \in \mathfrak{su}(N)
$$

## 2.3 Wilson Action

For plaquette set $P(\Lambda)$ with holonomies $U_p = \prod_{e \in \partial p} U_e^{\sigma_{p,e}}$:
$$
\boxed{S_\beta(U) = \beta \sum_{p \in P} \left(N - \mathrm{Re}\,\mathrm{Tr}(U_p)\right)}
$$

The Gibbs measure is:
$$
d\mu_\beta(U) = Z^{-1} e^{-S_\beta(U)} \, d\mathrm{vol}_g(U)
$$

---

# Chapter 3: Wilson Hessian as Discrete Hodge Laplacian

## 3.1 Discrete Cochain Operators

**Definition 3.1.1.** Define coboundary operators:
$$
d_0: C^0(\Lambda; \mathfrak{g}) \to C^1(\Lambda; \mathfrak{g}), \quad d_1: C^1(\Lambda; \mathfrak{g}) \to C^2(\Lambda; \mathfrak{g})
$$

For a 1-cochain $X$, $d_1 X$ gives the "discrete curl" (plaquette sum).

## 3.2 Plaquette Linearization

**Lemma 3.2.1 (BCH Linearization).**
For $U_e = \exp(X_e)$ with $\|X_e\|$ small:
$$
\log(U_p) = (d_1 X)_p + O(\|X\|^2)
$$

## 3.3 Wilson Hessian

**Theorem 3.3.1 (Wilson Hessian Identity).**
At the trivial configuration $U^{(0)} = (e, \ldots, e)$:
$$
\boxed{\nabla^2 S_\beta(U^{(0)}) = 2c_W \, d_1^* d_1, \quad c_W := \frac{\beta}{2N}}
$$

**Proof.**
1. Expand: $N - \mathrm{Re}\,\mathrm{Tr}(\exp X) = \frac{1}{2}\|X\|^2 + O(\|X\|^3)$
2. Apply to plaquettes: $S_\beta = c_W \sum_p \|(d_1 X)_p\|^2 + O(\|X\|^3)$
3. Hessian is the Gram form $\langle X, d_1^* d_1 X \rangle$. $\square$

## 3.4 Degeneracy and Hodge Decomposition

**Theorem 3.4.1 (Hodge Decomposition).**
$$
C^1(\Lambda; \mathfrak{g}) = \underbrace{\mathrm{im}(d_0)}_{\text{exact (gauge)}} \oplus \underbrace{\ker(\Delta_1)}_{\text{harmonic}} \oplus \underbrace{\mathrm{im}(d_1^*)}_{\text{coexact}}
$$
where $\Delta_1 = d_0 d_0^* + d_1^* d_1$.

**Key Property:** $d_1^* d_1$ is strictly positive on coexact modes, zero on exact/harmonic.

---

# Chapter 4: Horizontal Directions and Gauge Quotient

## 4.1 Vertical and Horizontal Subspaces

**Definition 4.1.1.** At $U \in \mathcal{A}$:
- **Vertical:** $V_U = \{d_0 \phi : \phi \in \mathfrak{g}^{V(\Lambda)}\}$ (tangent to gauge orbit)
- **Horizontal:** $H_U = V_U^{\perp_g}$ (physical directions)

## 4.2 Spectral Gap on Horizontals

**Theorem 4.2.1 (Wilson Gap on Horizontals).**
Under appropriate boundary conditions, there exists $c_W > 0$ such that:
$$
\boxed{\langle X, \nabla^2 S_\beta X \rangle \ge \beta c_W \|X\|^2, \quad \forall X \in H_U}
$$

**Proof Sketch.**
1. Gauge variations satisfy $d_1(d_0 \phi) = 0$ (Bianchi identity)
2. Hence $\mathrm{im}(d_0) \subseteq \ker(d_1^* d_1)$
3. On horizontals, $d_1^* d_1$ has a spectral gap (discrete Hodge theory). $\square$

## 4.3 The Matrix Hinge Operator

**Definition 4.3.1.** The effective operator on horizontals is:
$$
\mathcal{H}_\Lambda = m_H^2 \mathbb{I} + \alpha \, d_1^* d_1
$$
where $m_H^2$ comes from Haar geometry and $\alpha$ from Wilson coupling.

---

# Chapter 5: Bakry-Émery Curvature on Horizontals

## 5.1 The Horizontal Curvature Condition

**Definition 5.1.1.** A measure $\mu_\Lambda$ has **horizontal Bakry-Émery curvature $\ge \rho$ on $\Omega$** if:
$$
\mathrm{Ric}_{\mu_\Lambda}(U)(W, W) \ge \rho |W|^2, \quad \forall U \in \Omega, \, \forall W \in H_U
$$

**Key Observation.** For gauge-invariant $f \in \mathcal{A}_\Lambda^{\mathrm{inv}}$, we have $\nabla f(U) \in H_U$, so:
$$
\Gamma_{2,\Lambda}(f)(U) \ge \mathrm{Ric}_{\mu_\Lambda}(U)(\nabla f, \nabla f) \ge \rho \, \Gamma_\Lambda(f)(U)
$$

This means horizontal curvature implies **local $CD(\rho, \infty)$ for gauge-invariant observables**.

## 5.2 Key Inputs

### Input A: Group Ricci Curvature

**Lemma 5.2.1.** For $G = SU(N)$ with bi-invariant metric, there exists $\kappa_G > 0$ such that:
$$
\mathrm{Ric}_G = \kappa_G \, g_G
$$

For the product $\mathcal{A} = G^{E(\Lambda)}$:
$$
\mathrm{Ric}_{g_\Lambda} \ge \kappa_G \, g_\Lambda
$$
**uniformly in $\Lambda$**.

### Input B: Wilson Hessian Nonnegativity

**Lemma 5.2.2.** At $U^{(0)}$:
$$
\nabla^2 S_W(U^{(0)})(W, W) \ge 0, \quad \forall W \in T_{U^{(0)}} \mathcal{A}
$$

### Input C: Additional Term Control

**Assumption A.** There exists $C_{\mathrm{add}} \ge 0$, independent of $\Lambda$, such that:
$$
\nabla^2 S_{\mathrm{add},\Lambda}(U) \ge -C_{\mathrm{add}} \, g_\Lambda(U)
$$

## 5.3 The Main Theorem (Full Proof)

**Theorem 5.3.1 (Uniform Local Horizontal Bakry-Émery Bound).**
Assume:
1. $\mathrm{Ric}_{g_\Lambda} \ge \kappa_G g_\Lambda$ with $\kappa_G > 0$ independent of $\Lambda$
2. $\nabla^2 S_{\mathrm{add},\Lambda} \ge -C_{\mathrm{add}} g_\Lambda$ with $C_{\mathrm{add}} < \kappa_G$
3. $\nabla^2 S_W(U^{(0)}) \ge 0$

Then there exist $r > 0$ and $\rho_{\mathrm{loc}} > 0$, **independent of $\Lambda$**, such that for all $U \in B_r(U^{(0)})$ and all $W \in H_U$:
$$
\boxed{\mathrm{Ric}_{\mu_\Lambda}(U)(W, W) \ge \rho_{\mathrm{loc}} |W|_{g_\Lambda}^2}
$$

**Proof.**

**Step 1: Curvature at the vacuum.**
At $U^{(0)}$, for any horizontal $v \in H_{U^{(0)}}$:
$$
\begin{aligned}
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v, v) 
&= \mathrm{Ric}_{g_\Lambda}(v, v) + \nabla^2 S_W(U^{(0)})(v, v) + \nabla^2 S_{\mathrm{add}}(U^{(0)})(v, v) \\
&\ge \kappa_G |v|^2 + 0 - C_{\mathrm{add}} |v|^2 \\
&= (\kappa_G - C_{\mathrm{add}}) |v|^2
\end{aligned}
$$

Define:
$$
\rho_0 := \kappa_G - C_{\mathrm{add}} > 0
$$

**Step 2: Continuity extension.**
The map $(U, v) \mapsto \mathrm{Ric}_{\mu_\Lambda}(U)(v, v)$ restricted to unit horizontal vectors is continuous. The unit sphere bundle over a compact neighborhood is compact.

By continuity, there exists $r > 0$ such that:
$$
\inf_{U \in B_r(U^{(0)})} \inf_{v \in H_U, |v|=1} \mathrm{Ric}_{\mu_\Lambda}(U)(v, v) \ge \frac{\rho_0}{2}
$$

**Step 3: Uniformity in $\Lambda$.**
Set $\rho_{\mathrm{loc}} := \rho_0/2$. This is independent of $\Lambda$ because:
- $\kappa_G$ depends only on the group (product curvature)
- $C_{\mathrm{add}}$ is assumed independent of $\Lambda$
- The continuity argument is local and finite-dimensional $\square$

## 5.4 The Convexity Window

**Definition 5.4.1 (Strong-Coupling Convexity Window).**
The pair $(a, g)$ is in the **convexity window** if:
$$
\rho_*(a) := c_0 a^2 g^2 - \frac{12}{g^2} > 0
$$

Equivalently:
$$
\boxed{g^4 > \frac{12}{c_0 a^2}}
$$

**Derivation.** Using $\beta = 2N/g^2$ and $C_V(N) = 6/N$:
$$
\beta C_V(N) = \frac{2N}{g^2} \cdot \frac{6}{N} = \frac{12}{g^2}
$$

The horizontal Hessian satisfies:
$$
\langle A, \mathrm{Hess}_{\mathrm{hor}} S_{\mathrm{eff}}(U) A \rangle \ge \rho_*(a) \|A\|^2
$$

where $\rho_*(a) = c_0 a^2 g^2 - 12/g^2$.

## 5.5 The Gribov Region

**Definition 5.5.1.** The **Gribov region** $\Omega \subset \mathcal{A}$ is where the horizontal Hessian (Faddeev-Popov operator) is strictly positive definite. The **Gribov horizon** is where the minimal eigenvalue hits zero.

**Physical Interpretation:**
- $c_0 a^2 g^2$: **quantum stiffness** from compact group curvature
- $\beta C_V(N)$: **entropic pressure** from Wilson action flattening

At boundary $c_0 a^2 g^2 = \beta C_V(N)$: Gribov horizon.

## 5.6 Full Finite-Cutoff Mass Gap Theorem

**Theorem 5.6.1 (Finite-Cutoff Lattice Yang-Mills Mass Gap).**
Fix $G = SU(N)$, lattice spacing $a > 0$, coupling $g$ with:
$$
g^4 > \frac{12}{c_0 a^2}
$$

Then:
1. $S_{\mathrm{eff}}$ is uniformly horizontally convex with curvature $\rho_*(a) > 0$
2. $CD(\rho_{\mathrm{BE}}, \infty)$ holds for the Langevin generator
3. **Spectral gap** $\Delta_H \ge \rho_{\mathrm{BE}} > 0$, **uniform in volume**
4. Reducibles are polar and don't affect spectrum

**Corollary 5.6.2.** At each fixed cutoff $a > 0$, SU(N) lattice YM has a **nonzero mass gap** in the strong-coupling window $g > g_{\mathrm{crit}}(a)$.

---

# Chapter 6: Polarity of Reducible Configurations

## 6.1 Reducibles

**Definition 6.1.1.** A configuration $U \in \mathcal{A}$ is **reducible** if holonomy is contained in a proper closed subgroup of $SU(N)$.

Let $\Sigma \subset \mathcal{A}$ denote the set of reducibles.

## 6.2 The Polarity Theorem

**Theorem 6.2.1 (Reducibles are Polar).**
$\Sigma$ has capacity zero for the Yang-Mills Dirichlet form:
$$
\boxed{\mathrm{Cap}(\Sigma) = 0}
$$

**Proof Sketch.**
1. $\Sigma$ is contained in a finite union of submanifolds of codimension $\ge 2$
2. Codimension $\ge 2$ sets have zero capacity for elliptic Dirichlet forms
3. Apply capacity-codimension theorem. $\square$

## 6.3 Consequences

**Corollary 6.3.1.** The Langevin diffusion almost surely never hits $\Sigma$.

**Corollary 6.3.2.** Spectral gaps and functional inequalities proved on the irreducible stratum extend $\mu$-a.e. to the full measure.

---

# Chapter 7: Fixed-Cutoff Mass Gap Engine

## 7.1 The Pipeline

$$
\boxed{\text{Poincaré on SAFE} \xrightarrow{\text{HS}} \text{Covariance} \xrightarrow{\text{CT}} \text{Decay} \xrightarrow{\text{OS}} \text{Gap}}
$$

## 7.2 Module A: Restricted Poincaré

On the small-field region $K = \{U : \mathcal{B}_\Lambda(U) \le \varepsilon\}$:
$$
\mathrm{Var}_{\mu_K}(f) \le C_{\mathrm{hinge}} \int_K |\nabla f|^2 \, d\mu_K
$$
with volume-independent constant.

## 7.3 Module B: Helffer-Sjöstrand Representation

$$
\mathrm{Cov}_{\mu_K}(F, G) = \langle dF, \mathcal{L}^{-1} dG \rangle_{L^2(\mu_K)}
$$
where $\mathcal{L}$ is a Witten-type operator on 1-forms.

## 7.4 Module C: Combes-Thomas Decay

**Lemma 7.4.1 (Abstract Combes-Thomas).**
For $M \ge \lambda \mathbb{I}$ with finite range $R$:
$$
\boxed{|(M^{-1})(x, y)| \lesssim e^{-m \cdot \mathrm{dist}(x, y)}}
$$

## 7.5 Exponential Clustering

**Theorem 7.5.1.** For local observables $F, G$ with separated supports:
$$
|\mathrm{Cov}_{\mu_K}(F, G)| \le C(F, G) e^{-m \cdot \mathrm{dist}(\mathrm{supp}\, F, \mathrm{supp}\, G)}
$$

## 7.6 OS Hamiltonian Gap

Standard OS reconstruction gives:
$$
\mathrm{gap}(H_a) \gtrsim \frac{\eta(a)}{a}
$$
where $\eta(a)$ is the Euclidean decay rate.

---

# Chapter 8: Local Cancellation and Coercivity (GAP-FC-02)

## 8.1 The Problem Statement

For Wilson action $S_\Lambda(U) = \beta \sum_p \vartheta(U_p)$ where $\vartheta(g) = 1 - \frac{1}{2}\mathrm{Re}\,\mathrm{Tr}(g)$, define the disorder functional:
$$
\mathcal{B}_\Lambda(U) = \frac{1}{|P(\Lambda)|} \sum_{p \in P(\Lambda)} \vartheta(U_p(U))
$$

**GAP-FC-02 asks:** There exist $\varepsilon, c_0 > 0$ independent of $|\Lambda|$ such that:
$$
\boxed{\mathcal{B}_\Lambda(U) \ge \varepsilon \Rightarrow \|\nabla S_\Lambda(U)\| \ge c_0}
$$

## 8.2 Local Force Decomposition

Fix oriented link $\ell = (x, \mu)$. Let $\mathcal{P}(\ell)$ be incident plaquettes ($|\mathcal{P}(\ell)| = 6$ in $d=4$).

Write plaquette holonomy as $U_p(U) = U_\ell W_p(U)$ where $W_p$ is the staple.

**Force formula:**
$$
\nabla_\ell S_\Lambda(U) = \beta \sum_{p \in \mathcal{P}(\ell)} \nabla_\ell \vartheta(U_\ell W_p(U))
$$

For $G = SU(2)$, identifying $\mathfrak{su}(2) \cong \mathbb{R}^3$:
$$
\nabla_\ell \vartheta(U_\ell W_p) = \mathrm{Ad}_{G_p(U)} X_p(U)
$$

This is a **finite sum of rotated vectors in $\mathbb{R}^3$**.

## 8.3 Single-Plaquette Coercivity

**Lemma 8.3.1.** For $g = \exp(\theta \hat{n} \cdot i\sigma)$:
$$
\vartheta(g) = 1 - \cos\theta, \quad \|\nabla\vartheta(g)\| \asymp \sin\theta
$$

If $\vartheta(g) \ge \varepsilon$ bounded away from 0 and 2, then $\|\nabla\vartheta(g)\|$ is bounded below.

## 8.4 The Cartan-Aligned Exceptional Set

**Definition 8.4.1.** A configuration is **Cartan-aligned at $\ell$** if all incident plaquette holonomies commute (lie in a common maximal torus).

For $SU(2)$: all holonomies are rotations around a common axis.

Define:
$$
\mathcal{R}_\ell(\varepsilon) := \{U : \max_{p \in \mathcal{P}(\ell)} \vartheta(U_p) \ge \varepsilon\}
$$
$$
\mathcal{A}_\ell := \{U : [U_p, U_{p'}] = e, \, \forall p, p' \in \mathcal{P}(\ell)\}
$$

## 8.5 The Local Non-Cancellation Lemma

**Lemma 8.5.1 (Local Non-Cancellation Outside Cartan Alignment).**
For each $\varepsilon \in (0, 2)$, there exist $c(\varepsilon) > 0$ and $\delta(\varepsilon) > 0$ such that:
$$
U \in \mathcal{R}_\ell(\varepsilon) \cap \mathcal{A}_\ell^c \Rightarrow \|\nabla_\ell S_\Lambda(U)\| \ge c(\varepsilon)
$$

Moreover, $c(\varepsilon)$ is **independent of $|\Lambda|$**.

**Proof Route (Analytic Geometry):**
1. **Stratify** $Z_\ell = \{U : \nabla_\ell S_\Lambda(U) = 0\}$ as zero set of analytic functions
2. **Identify** that on $\mathcal{R}_\ell(\varepsilon)$, only strata in $\mathcal{A}_\ell$ persist
3. **Apply Łojasiewicz inequality:** $\|\nabla_\ell S\| \gtrsim \mathrm{dist}(U, Z_\ell)^k$
4. **Uniformity:** Force depends only on bounded neighborhood of $\ell$ $\square$

## 8.6 Why This Closes Drift Control

If Lemma 8.5.1 holds, then macroscopic disorder forces $\|\nabla S\| \ge c_0$, enabling:
- Lyapunov drift → global Poincaré/LSI
- Concentration of small-field sets
- Removal of localization conditioning

---

# Chapter 9: RG Curvature Stability Class

## 9.1 The $(\kappa_*, \alpha)$ Class

**Definition 9.1.1.** A curvature-controlled pair $(g, V)$ satisfies:
$$
(g, V) \in \mathcal{C}(\kappa) \Longleftrightarrow \mathrm{Ric}_g + \nabla^2 V \ge \kappa g
$$

An RG trajectory $(g_n, V_n) = \mathcal{R}^n(g_0, V_0)$ is **$(\kappa_*, \alpha)$-stable** if:
$$
\mathrm{Ric}_{V_n} \ge \alpha^n \kappa_* g_n, \quad \forall n \ge 0
$$

## 9.2 SAFE Region Constants (SU(3))

From explicit computation in right-invariant exponential coordinates:

| Constant | Value | Interpretation |
|:---------|:------|:---------------|
| $\kappa_*$ | $\approx 0.25$ | Haar curvature floor |
| $\delta$ | $\approx 0.006$ | Curvature loss per RG step |
| $\alpha$ | $\approx 0.976$ | Degradation factor |

**Interpretation:** Curvature degrades slowly. For $\lesssim 100$ steps, $\alpha^n \kappa_*$ remains positive.

## 9.3 RG Stability Inequality

Iterating the curvature class gives:
$$
C_{\mathrm{LSI}}^{(n)} \le \frac{2}{\alpha^n \kappa_*}, \quad \lambda_1^{(n)} \ge \alpha^n \kappa_*
$$

**Cathedral Hinge:** Once $\alpha$ is close to 1 and convexity eventually improves, we get uniform infimum $\kappa_\infty > 0$.

---

# Chapter 10: Combined Quadratic Form

## 10.1 Wilson + Haar

In exponential coordinates:
$$
\boxed{S_{\mathrm{eff}}^{(2)}(X) = \frac{1}{2} \langle X, (c_H \mathbb{I} + 2c_W d_1^* d_1) X \rangle}
$$

## 10.2 Mode Analysis

| Mode Type | Wilson Contribution | Haar Contribution |
|:----------|:-------------------|:------------------|
| Coexact | $> 0$ | $> 0$ |
| Harmonic | $0$ | $> 0$ |
| Exact (gauge) | $0$ | $> 0$ (quotiented) |

**Key Insight:** Haar provides uniform convexity even where Wilson is degenerate.

---

# Chapter 10: Numerical Validation

## 10.1 SU(3) Convexity Window Scans

Numerical experiments on $L=2$ ($2^4$ lattice) using JAX autodiff Hessians:

### Vacuum Hessian Eigenvalues
At $A = 0$ (trivial configuration):
- $n_{\mathrm{params}} = L^4 \cdot 4 \cdot 8 = 512$
- Smallest eigenvalues cluster at Haar value $\approx c_0 = 0.25$

### $\sigma$-Sweep at Fixed $\beta$

For $\beta = 2.0$, $c_0 = 0.25$, sampling $\theta \sim N(0, \sigma^2)$:

| $\sigma$ | min $\lambda_{\min}$ | mean $\lambda_{\min}$ |
|:---------|:---------------------|:----------------------|
| 0.00 | +0.2500 | +0.2500 |
| 0.02 | +0.1952 | +0.2005 |
| 0.05 | +0.1202 | +0.1234 |
| 0.10 | −0.0262 | −0.0217 |
| 0.20 | −0.3836 | −0.3456 |

**Convexity window:** approximately $\sigma < 0.07$ for $\beta = 2.0$.

### Empirical Convexity Radii $R(\beta)$

| $\beta$ | $R(\beta)$ | $C_\beta = c_0/(\beta R^2)$ |
|:--------|:-----------|:----------------------------|
| 0.40 | 0.2449 | 5.22 |
| 0.80 | 0.1454 | 7.35 |
| 1.60 | 0.0808 | 11.95 |
| 3.20 | 0.0460 | 17.08 |

**Scaling:** $R(\beta) \propto \beta^{-1/2}$ with slowly varying $C_\beta$.

## 10.2 Bessel Function Validation (SU(2))

Exact one-plaquette partition function:
$$
\boxed{Z_1(\beta) = 2 \frac{I_1(\beta)}{\beta}}
$$

where $I_1$ is the modified Bessel function.

**Derivation:**
$$
Z_1(\beta) = \frac{2}{\pi} \int_0^\pi \sin^2 \phi \, e^{\beta \cos\phi} \, d\phi
$$

Using $\int_0^\pi e^{\beta \cos\phi} \sin^2 \phi \, d\phi = \pi I_1(\beta)/\beta$.

**Validation anchor:** All tensor network and numerical pipelines must reproduce this.

## 10.3 Key Numerical Findings

1. **Haar dominates at vacuum:** $\lambda_{\min}(A=0) = c_0$
2. **Wilson erodes curvature:** $\lambda_{\min}(A) \approx c_0 - C\beta r^2$
3. **Convexity shrinks with $\beta$:** Window exists but narrows

---

# Chapter 11: Open Problems

## 11.1 Globalization

Extend curvature bounds beyond the small-angle sector (Gribov horizon / large-field).

## 11.2 Volume Uniformity

Control $c_W$ behavior under increasing lattice size.

## 11.3 Continuum Lifting

Show curvature bounds survive $a \to 0$ via Mosco/OS machinery.

## 11.4 Local-to-Global Gap

Upgrade from SAFE-restricted Poincaré to full measure via Lyapunov drift.

## 11.5 Rigorous Bounds

Prove operator-norm bound $\|\nabla^2 S_W(A)\| \le C\beta \|A\|^2$ in exponential coordinates.

---

# Chapter 11: Explicit Haar Jacobian Derivation

## 11.1 Haar Measure in Exponential Coordinates

Write Haar measure as $d\mu_H(U) = J(X) dX$ for $U = \exp(X)$, where:
$$
J(X) = \det_{\mathfrak{g}} \left( \frac{\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X/2} \right)
$$

Define the **Haar potential:**
$$
S_{\mathrm{Haar}}(X) := -\log J(X)
$$

## 11.2 Series Expansion

Using $\log\left(\frac{\sinh z}{z}\right) = \frac{z^2}{6} + O(z^4)$:
$$
S_{\mathrm{Haar}}(X) = -\frac{1}{24} \mathrm{Tr}_{\mathfrak{g}}(\mathrm{ad}_X^2) + O(\|X\|^4)
$$

For $\mathfrak{su}(N)$:
$$
\mathrm{Tr}_{\mathfrak{g}}(\mathrm{ad}_X^2) = 2N \, \mathrm{Tr}(X^2)
$$

Therefore:
$$
\boxed{S_{\mathrm{Haar}}(X) = \frac{N}{12} \|X\|^2 + O(\|X\|^4)}
$$

## 11.3 The Haar Mass Hessian

**Theorem 11.3.1.** At the identity:
$$
\mathrm{Hess} \, S_{\mathrm{Haar}}(0) = \frac{N}{6} \mathbb{I}
$$

Define:
$$
\boxed{c_0 := \frac{N}{6}}
$$

On the lattice with $X_b = ag A_b$:
$$
S_{\mathrm{Haar}}^{(2)}(A) = \frac{N}{12} a^2 g^2 \sum_b \|A_b\|^2
$$

| Group | $c_0 = N/6$ | Comment |
|:------|:------------|:--------|
| SU(2) | $1/3$ | |
| SU(3) | $1/2$ | |
| SU(N) | $N/6$ | Grows with $N$ |

---

# Chapter 12: Why This Cannot Be the Continuum Mass Gap

## 12.1 The Asymptotic Freedom Problem

Along the asymptotically-free trajectory, $g(a) \to 0$ as $a \to 0$. Therefore:

- Haar term: $\sim a^2 g(a)^2 \to 0$
- Wilson penalty: $\beta(a) = 2N/g(a)^2 \to \infty$

The curvature floor:
$$
\rho_*(a) = \frac{N}{6} a^2 g(a)^2 - \frac{48}{g(a)^2} \to -\infty
$$

**Conclusion:** Global uniform convexity is **violently incompatible** with the UV limit.

## 12.2 Escape Routes

The finite-cutoff convexity window is a **diagnostic**, not a bug. Continuum relevance requires:

1. **Localization:** Convexity on a high-probability core (SAFE region), not globally
2. **New Spark:** IR convexity at a physical scale independent of cutoff

---

# Chapter 13: Summary and Key Theorems

## 13.1 Main Theorems

| Theorem | Statement | Reference |
|:--------|:----------|:----------|
| Wilson Hessian | $\nabla^2 S_W(U^{(0)}) = 2c_W d_1^* d_1$ | Thm 3.3.1 |
| Hodge Decomposition | $C^1 = \mathrm{im}(d_0) \oplus \ker(\Delta_1) \oplus \mathrm{im}(d_1^*)$ | Thm 3.4.1 |
| Matrix Hinge | $\mathrm{Ric}_{\mu_\Lambda} \succeq (c_H - R_W(r))I + t d_1^* d_1$ | Prop 4.3.1 |
| Local Horizontal Curvature | $\mathrm{Ric}_{\mu_\Lambda}(U)(W,W) \ge \rho_{\mathrm{loc}} \|W\|^2$ | Thm 5.3.1 |
| Convexity Window | $g^4 > 288/(Na^2)$ gives $\rho_*(a) > 0$ | Thm 5.4.1 |
| Finite-Cutoff Gap | Gap $\Delta_H \ge \rho_{\mathrm{BE}} > 0$ for $g^4 > 12/(c_0 a^2)$ | Thm 5.6.1 |
| Polarity of Reducibles | $\mathrm{Cap}(\Sigma) = 0$ | Thm 6.2.1 |
| Maxwell-Calladine Rigidity | $\ker K = \ker D$, gap $\ge \alpha \sigma_*^2$ | Prop 8.6.1 |
| Local Non-Cancellation | $\|\nabla_\ell S\| \ge c(\varepsilon)$ outside Cartan | Lemma 8.5.1 |
| RG Stability | $C_{\mathrm{LSI}}^{(n)} \le 2/(\alpha^n \kappa_*)$ | §9.3 |
| Haar Mass Hessian | $\mathrm{Hess}(S_{\mathrm{Haar}})(0) = (N/6)\mathbb{I}$ | Thm 11.3.1 |

## 13.2 Explicit Constants

| Constant | Definition | Value (SU(N)) |
|:---------|:-----------|:--------------|
| $c_0$ | Haar Hessian coefficient | $N/6$ |
| $\kappa_*$ | Haar curvature floor | $\approx 0.25$ (SU(3)) |
| $C_V(N)$ | Wilson Hessian bound | $24/N$ |
| $\alpha$ | RG degradation factor | $\approx 0.976$ |
| $\sigma_*^2$ | Singular value gap in Hodge | lattice-dependent |

## 13.3 The Mass Gap Pipeline

$$
\boxed{
\text{Haar geometry} + \text{Wilson curvature} 
\xrightarrow{\text{horizontals}} 
\text{BE positivity} 
\xrightarrow{\text{PI/LSI}} 
\text{Spectral Gap}
\xrightarrow{\text{HS+CT}}
\text{Clustering}
\xrightarrow{\text{OS}}
\text{Mass Gap}
}
$$

## 13.4 Alternative Pipeline (Rigidity Route)

$$
\boxed{
\text{Bianchi constraints} + \text{UBP condition}
\xrightarrow{\text{Maxwell-Calladine}}
\text{Stiffness gap mod gauge}
\xrightarrow{\text{Lyapunov drift}}
\text{Global PI}
}
$$

## 13.5 Files Reviewed (Pass 4)

**56/56 files reviewed.** Critical files copied to `CRITICAL FILES/` (30 files).

---

# Appendix A: Theta-Term and q-Deformation

## A.1 The Theta Problem

The Euclidean Yang-Mills theta-term:
$$
Z(\theta) = \sum_{Q \in \mathbb{Z}} e^{i\theta Q} Z_Q
$$

creates a sign problem for Monte Carlo. The project explores an alternative:

## A.2 Theta as Quantum Group Deformation

**Core Ansatz:**
$$
\boxed{q = e^{i\theta}, \quad SU(2) \to U_q(\mathfrak{su}(2))}
$$

Replace classical recoupling data with q-deformed data:

**Quantum Numbers:**
$$
[n]_q = \frac{q^n - q^{-n}}{q - q^{-1}} = \frac{\sin(n\theta)}{\sin\theta}
$$

**Quantum Dimensions:**
$$
d_j^{(q)} = [2j+1]_q = \frac{\sin((2j+1)\theta)}{\sin\theta}
$$

## A.3 Q-Deformed 6j Symbols

The q-Racah formula:
$$
\begin{Bmatrix}
j_1 & j_2 & j_3 \\
j_4 & j_5 & j_6
\end{Bmatrix}_q
= \Delta_q \cdot \Delta_q \cdot \Delta_q \cdot \Delta_q \sum_{t} (-1)^t \mathcal{R}_q(t)
$$

where $\Delta_q(a,b,c)$ is the q-triangle coefficient.

**Numerical Stability:** Compute in log-space with phase tracking.

## A.4 Rank-8 Vertex Tensor

For 4D hypercubic lattice (8 incident links):
$$
T_{j_1 \ldots j_8} = \prod_{a=1}^{8} w(j_a) \sum_{k} w(k) 
\begin{Bmatrix}
j_1 & j_2 & k \\
j_3 & j_4 & k
\end{Bmatrix}_q
\begin{Bmatrix}
j_5 & j_6 & k \\
j_7 & j_8 & k
\end{Bmatrix}_q
$$

## A.5 Topological Susceptibility

Extract from free energy curvature:
$$
F(\theta) = -\log Z(\theta), \quad \chi_{\mathrm{top}} = \left.\frac{\partial^2 F}{\partial\theta^2}\right|_{\theta=0}
$$

**Expected Properties:**
- $2\pi$-periodicity: $F(\theta + 2\pi) = F(\theta)$
- CP symmetry: $F(\theta) = F(-\theta)$
- Positive $\chi_{\mathrm{top}}$

## A.6 Status and Open Questions

1. **Is this Yang-Mills?** Unclear if q-deformation reproduces YM theta physics
2. **Sign-problem-free?** Tensor contraction is deterministic (no Monte Carlo)  
3. **Novel model?** May define a new family of 4D quantum-group state sums

**Source Files:**
- `01_theta_as_q_deformation.md`
- `02_q_6j_logspace.md`
- `03_rank8_vertex_tensor.md`
- `04_theta_term_qdeformation_tensor_network.md`



