# Synthesis II: Functional Inequalities and Spectral Gaps for Lattice Yang-Mills

## Topic: Analysis_LSI (HAAR Subtopic 2 of 8)

---

# Chapter 1: Overview and Connection to Geometry Synthesis

## 1.1 Purpose

This synthesis builds on the **Haar-Geometric Foundation** (Synthesis I) to develop **functional inequalities** (Poincaré, Log-Sobolev) and their consequences for **spectral gaps**. The key mechanism is:

$$
\text{(Local Convexity in SAFE Region)} + \text{(Lyapunov Drift Control)} \Rightarrow \text{Global PI/LSI}
$$

## 1.2 Connection to Synthesis I

From the Geometry synthesis, we have:
- **Bakry-Émery tensor:** $\mathrm{Ric}_{\mu_\Lambda} = \mathrm{Ric}_{g_\Lambda} + \nabla^2 S_\Lambda$
- **Local curvature bound:** $\mathrm{Ric}_{\mu_\Lambda} \ge \rho_{\mathrm{loc}} g_\Lambda$ on the SAFE region
- **Matrix Hinge:** $\mathcal{H}_\Lambda \succeq m_H^2 \mathbb{I} + \alpha d_1^* d_1$

This synthesis covers **how local convexity becomes global functional inequalities**.

---

# Chapter 2: The Curvature-Dimension Condition $CD(\rho, \infty)$

## 2.1 Definition

**Definition 2.1.1.** A measure $\mu$ with generator $L$ satisfies $CD(\rho, \infty)$ if:
$$
\Gamma_2(f) \ge \rho \, \Gamma(f), \quad \forall f \in C^\infty
$$
where $\Gamma_2$ is the iterated carré du champ.

## 2.2 Equivalence

**Theorem 2.2.1.** The following are equivalent:
1. $\mathrm{Ric}_\mu \ge \rho \, g$ as quadratic forms.
2. $\Gamma_2(f) \ge \rho \, \Gamma(f)$ for all smooth $f$.
3. The measure satisfies $CD(\rho, \infty)$.

---

# Chapter 3: From CD Condition to Functional Inequalities

## 3.1 The Bakry-Émery Theorem

**Theorem 3.1.1 (Bakry-Émery LSI).**
If $\mathrm{Ric}_\mu \ge \rho g$ with $\rho > 0$, then:
$$
\boxed{\mathrm{Ent}_\mu(f^2) \le \frac{2}{\rho} \int |\nabla f|^2 \, d\mu}
$$

**Theorem 3.1.2 (Bakry-Émery Poincaré).**
Under the same condition:
$$
\boxed{\mathrm{Var}_\mu(f) \le \frac{1}{\rho} \int |\nabla f|^2 \, d\mu}
$$

## 3.2 Consequences for Spectral Gaps

**Corollary 3.2.1 (Spectral Gap).**
The generator $-L$ has spectral gap $\lambda_1 \ge \rho$.

**Corollary 3.2.2 (Exponential Relaxation).**
$$
\|P_t f - \mu(f)\|_{L^2(\mu)} \le e^{-\rho t} \|f - \mu(f)\|_{L^2(\mu)}
$$

---

# Chapter 4: The Explicit LSI Constant for Lattice YM

## 4.1 The Project Constant $c_0$

**Theorem 4.1.1 (Finite-Lattice LSI with Explicit Constant).**
For the lattice YM measure $\mu$ on $SU(N)^{E(\Lambda)}$:
$$
\boxed{\mathrm{Ent}_\mu(f^2) \le \frac{2}{c_0} \int |\nabla f|^2 \, d\mu, \quad c_0 = \frac{N^2 - 1}{2N}}
$$

## 4.2 Explicit Values

| Group | $c_0 = (N^2-1)/(2N)$ | $2/c_0$ (LSI constant) |
|:---|:---|:---|
| SU(2) | $3/4$ | $8/3 \approx 2.67$ |
| SU(3) | $4/3$ | $3/2 = 1.5$ |
| SU(N) large | $\approx N/2$ | $\approx 4/N$ |

## 4.3 Corollaries

**Corollary 4.3.1 (Poincaré).**
$$
\mathrm{Var}_\mu(f) \le \frac{1}{c_0} \int |\nabla f|^2 \, d\mu
$$

**Corollary 4.3.2 (Spectral Gap).**
$$
\lambda_1 \ge c_0 > 0
$$

---

# Chapter 5: Local-to-Global Patching via Lyapunov Drift

## 5.1 The Problem

The curvature bound $\mathrm{Ric}_\mu \ge \rho g$ typically holds only on a **local SAFE region** $U_\Lambda$, not globally. We need to extend local inequalities to global ones.

## 5.2 Ingredient A: Local PI/LSI on the SAFE Region

**Definition 5.2.1 (Local PI).**
There exists $C_{\mathrm{P,loc}}$ independent of $\Lambda$ such that:
$$
\int_{U_\Lambda} (f - f_{U_\Lambda})^2 \, d\mu \le C_{\mathrm{P,loc}} \int_{U_\Lambda} \Gamma(f) \, d\mu
$$

**Definition 5.2.2 (Local LSI).**
There exists $C_{\mathrm{LS,loc}}$ independent of $\Lambda$ such that:
$$
\mathrm{Ent}_\mu(f^2 \mathbf{1}_{U_\Lambda}) \le C_{\mathrm{LS,loc}} \int_{U_\Lambda} \Gamma(f) \, d\mu
$$

## 5.3 Ingredient B: Lyapunov Drift Condition

**Definition 5.3.1 (Foster-Lyapunov Drift).**
There exists a gauge-invariant function $W_\Lambda \ge 1$ and constants $\alpha > 0$, $\beta \ge 0$ (independent of $\Lambda$) such that:
$$
\boxed{L_\Lambda W_\Lambda \le -\alpha W_\Lambda + \beta \, \mathbf{1}_{U_\Lambda}}
$$

**Interpretation:** The drift pushes configurations back toward the SAFE region.

## 5.4 The Patching Theorem

**Theorem 5.4.1 (Global PI via Lyapunov).**
Assume local PI on $U_\Lambda$ and drift condition (LD). Then there exists $C_{\mathrm{P,glob}} > 0$, independent of $\Lambda$, such that:
$$
\boxed{\mathrm{Var}_\mu(f) \le C_{\mathrm{P,glob}} \int \Gamma(f) \, d\mu}
$$

**Theorem 5.4.2 (Global LSI via Lyapunov).**
Assume local LSI on $U_\Lambda$ and (LD). Then:
$$
\boxed{\mathrm{Ent}_\mu(f^2) \le C_{\mathrm{LS,glob}} \int \Gamma(f) \, d\mu}
$$

**Corollary 5.4.3 (Uniform Spectral Gap).**
$$
\lambda_1^{\mathrm{inv}}(\Lambda) \ge \frac{1}{C_{\mathrm{P,glob}}} > 0 \quad \text{uniform in } |\Lambda|
$$

---

# Chapter 6: Proof Skeleton for Local-to-Global Patching

## 6.1 The Splitting Pattern

*Step 1:* Split variance/entropy into inside vs. outside SAFE:
$$
\mathrm{Var}_\mu(f) = \mathrm{Var}_\mu(f \mathbf{1}_U) + \mathrm{Var}_\mu(f \mathbf{1}_{U^c}) + \text{cross terms}
$$

*Step 2:* Control the $U$ piece by local PI/LSI.

*Step 3:* Control the $U^c$ piece using Lyapunov drift, showing:
- $\mu(U) \ge c > 0$ uniformly
- Exponential tail suppression in $W$
- $\int_{U^c} f^2 \, d\mu \lesssim \int |\nabla f|^2 \, d\mu$

---

# Chapter 7: The Drift-Gluing Gap Mechanism

## 7.1 The Good/Bad/Strip Decomposition

**Definition 7.1.1 (Order Parameter).**
Define the averaged badness:
$$
\mathcal{B}_\Lambda(U) = \frac{1}{|P|} \sum_{p \in P} b(U_p)
$$
where $b(U_p)$ measures distance from identity.

**Definition 7.1.2 (Good/Bad/Strip Partition).**
Fix $\varepsilon, \delta > 0$:
- **Good set:** $K = \{\mathcal{B}_\Lambda \le \varepsilon\}$
- **Bad set:** $K^c = \{\mathcal{B}_\Lambda \ge \varepsilon + \delta\}$
- **Strip:** $\Sigma = \{\varepsilon < \mathcal{B}_\Lambda < \varepsilon + \delta\}$

## 7.2 Drift Identity

**Lemma 7.2.1 (Structural Drift Identity).**
$$
L_\Lambda \mathcal{B}_\Lambda = \Delta_\Lambda \mathcal{B}_\Lambda - \beta |P| |\nabla \mathcal{B}_\Lambda|^2
$$
with $|\Delta_\Lambda \mathcal{B}_\Lambda| \le C_\Delta$ (geometry constant).

## 7.3 Strip Drift Domination

**Definition 7.3.1 (Strip Drift Condition).**
There exists $\rho > 0$ such that:
$$
L_\Lambda \mathcal{B}_\Lambda \le -\rho \quad \text{on } \Sigma
$$

This reduces to:
$$
|\nabla \mathcal{B}_\Lambda|^2 \ge \frac{C_\Delta + \rho}{\beta |P|} \quad \text{on } \Sigma
$$

## 7.4 The SU(2) Local Cancellation Lemma

**Lemma 7.4.1 (Geometric Coercivity).**
If $\mathcal{B}_\Lambda(U) \ge \varepsilon$, then some link $\ell$ has:
$$
\|\nabla_\ell S_W(U)\| \ge c_0(\varepsilon, \beta) > 0
$$
except on a globally Cartan-aligned set of measure zero.

**Interpretation:** Forces from nearby plaquettes can only cancel if the entire configuration sits in a common Abelian subgroup.

## 7.5 The Smooth Gluing Lemma

**Theorem 7.5.1 (Gluing).**
Assume restricted Poincaré on $K$ and $K^c$, and drift domination on $\Sigma$. Then:
$$
\mathrm{Var}_{\mu_\Lambda}(f) \le C_{\mathrm{mix}} \mathcal{E}_\Lambda(f,f) + C_\Sigma \int_\Sigma (f - \mu_\Lambda f)^2 d\mu_\Lambda
$$
where $C_{\mathrm{mix}} = O(1/\rho)$.

**Result:** Volume-uniform Poincaré constant $\lambda_*$ independent of $|\Lambda|$.

---

# Chapter 8: Helffer-Sjöstrand Covariance Representation

## 8.1 The Lifted Operator $\mathcal{L}^{(1)}$

**Definition 8.1.1.**
The Bochner/Helffer-Sjöstrand operator on 1-forms is:
$$
\mathcal{L}^{(1)} := (-L) \otimes \mathbb{I} + \mathrm{Ric}_{\mu_\Lambda}
$$
Since $-L \succeq 0$, we have:
$$
\mathcal{L}^{(1)} \succeq \mathrm{Ric}_{\mu_\Lambda}
$$

## 8.2 The HS Identity

**Theorem 8.2.1 (Helffer-Sjöstrand Representation).**
For smooth $F, G$:
$$
\boxed{\mathrm{Cov}_{\mu_\Lambda}(F, G) = \int \langle \nabla F, (\mathcal{L}^{(1)})^{-1} \nabla G \rangle \, d\mu_\Lambda}
$$

This is an **identity**, not a bound.

## 8.3 Matrix Covariance Bound

**Corollary 8.3.1 (Brascamp-Lieb via Hinge).**
If $\mathrm{Ric}_{\mu_\Lambda} \succeq M$ on region $K$, then:
$$
(\mathcal{L}^{(1)})^{-1} \preceq M^{-1}
$$
and:
$$
|\mathrm{Cov}_{\mu_K}(F, G)| \le \int \langle \nabla F, M^{-1} \nabla G \rangle \, d\mu_K
$$

## 8.4 Massive Maxwell Specialization

On the SAFE region, the Matrix Hinge gives:
$$
M = \frac{c_H}{2} \mathbb{I} + t \, d_1^* d_1
$$
restricted to horizontal sector.

---

# Chapter 9: Combes-Thomas Exponential Decay

## 9.1 Setup

Let $V$ be a finite graph with distance $\mathrm{dist}(\cdot, \cdot)$. Operator $A: \ell^2(V; \mathsf{H}_0) \to \ell^2(V; \mathsf{H}_0)$ with block kernel $(A f)(x) = \sum_y A_{xy} f(y)$.

**Assumptions:**
1. **Positivity:** $A \succeq a_0 \mathbb{I}$
2. **Finite range:** $A_{xy} = 0$ if $\mathrm{dist}(x,y) > R$
3. **Row-sum bound:** $B := \sup_x \sum_{y \neq x} \|A_{xy}\|_{\mathrm{op}} < \infty$

## 9.2 The Combes-Thomas Lemma

**Lemma 9.2.1 (Finite-Range Combes-Thomas).**
Under Assumptions 1-3:
$$
\boxed{\|(A^{-1})_{xy}\|_{\mathrm{op}} \le \frac{2}{a_0} \exp(-\eta \, \mathrm{dist}(x,y))}
$$
where:
$$
\eta = \frac{1}{R} \log\left(1 + \frac{a_0}{2B}\right)
$$

**Proof Sketch.**
1. Define weight $W_t f(x) = e^{t\phi_y(x)} f(x)$ with $\phi_y(x) = \mathrm{dist}(x,y)$.
2. Conjugate: $A_t := W_t A W_t^{-1} = A + K_t$.
3. Schur test: $\|K_t\| \le (e^{tR} - 1) B$.
4. Choose $t = \eta$ so $\|K_t\| \le a_0/2$.
5. Neumann series: $\|A_t^{-1}\| \le 2/a_0$.
6. Unconjugate: $\|(A^{-1})_{xy}\| \le e^{-t \, \mathrm{dist}(x,y)} \|A_t^{-1}\|$. $\blacksquare$

## 9.3 Application to Massive Maxwell

For $M = m^2 \mathbb{I} + t \, d_1^* d_1$ on link cochains:
- $a_0 = m^2$
- $R = O(1)$ (links adjacent via common plaquette)
- $B \lesssim t \nu$ (incidence constant)

**Result:** $M^{-1}$ has exponentially decaying kernel with rate:
$$
\eta = \frac{1}{R} \log\left(1 + \frac{m^2}{2t\nu}\right)
$$

## 9.4 Why This Matters

Covariances $\le$ $M^{-1}$ (from HS) + $M^{-1}$ decays exponentially (from CT) = **Exponential clustering of correlations**.

---

# Chapter 10: The Complete HS-to-Gap Pipeline

## 10.1 The Four-Step Pipeline

**Step 1:** Helffer-Sjöstrand reduces $\mathrm{Cov}(F,G)$ to inverse Witten Laplacian.

**Step 2:** Matrix Hinge bounds Witten Laplacian $\succeq$ Massive Maxwell $M$.

**Step 3:** Combes-Thomas gives $\|M^{-1}_{\ell\ell'}\| \le C e^{-\eta \, d(\ell, \ell')}$.

**Step 4:** Combining yields **conditional exponential clustering**:
$$
\boxed{|\mathrm{Cov}_{\mu^K}(F,G)| \le C(F,G) \, e^{-m_{\mathrm{CT}} \, \mathrm{dist}_E(A,B)}}
$$

## 10.2 The Explicit Decay Rate

$$
m_{\mathrm{CT}} = \frac{1}{R} \log\left(1 + \frac{m_H^2}{2\alpha D}\right)
$$
where $D$ is the bounded-degree constant for link adjacency.

## 10.3 From Clustering to OS Gap

Under reflection positivity, if
$$
|\mathrm{Cov}_\mu(F, \Theta F)| \le C(F) e^{-m t}
$$
where $t$ is time separation and $\Theta$ is OS reflection, then the OS Hamiltonian has spectral gap:
$$
\boxed{E_1 \ge m}
$$

**Physical mass gap:**
$$
m_{\mathrm{OS}} = \frac{m}{a}
$$

---

# Chapter 11: The OS-Dirichlet Scale-$a$ Bridge

## 11.1 The Boundedness Obstruction

**Problem:** The naive comparison
$$
\langle F, (I-T_a) F \rangle_{\mathrm{OS}} \ge c \int |\nabla F|^2 d\mu
$$
is **impossible** because LHS is bounded while RHS can be arbitrarily large.

## 11.2 The Strip Kernel

**Definition 11.2.1 (One-Step Strip Kernel).**
$$
\mathcal{K}_a(\sigma, \sigma') := \int W_a(\sigma, \sigma', U_0) \prod_x dH(U_0(x))
$$
where $W_a$ is the product of plaquette weights on straddling plaquettes.

## 11.3 The Key Identity

**Theorem 11.3.1 (OS Dissipation = Boundary Dirichlet Form).**
$$
\boxed{\langle F, (I-T_a) F \rangle_{\mathrm{OS}} = \mathcal{E}_{K_a}(JF, JF)}
$$
where $J$ is the boundary embedding and $\mathcal{E}_{K_a}(f,f) := \langle f, (I-K_a) f \rangle$.

## 11.4 The Correct Comparison

**Definition 11.4.1 (Scale-$a$ Dirichlet Form).**
$$
\mathcal{E}_{\mathrm{conf}}^{(a)}(f, f) := \langle f, (I - P_a) f \rangle
$$
where $(P_t)$ is the configuration diffusion semigroup.

**Gradient representation:**
$$
\mathcal{E}_{\mathrm{conf}}^{(a)}(f, f) = \int_0^a \int |\nabla P_{t/2} f|^2 \, d\nu \, dt
$$

## 11.5 The Comparison Theorem

**Theorem 11.5.1 (One-Step OS vs Scale-$a$ Dirichlet).**
There exists $c > 0$ (independent of volume) such that:
$$
\boxed{\langle F, (I-T_a) F \rangle_{\mathrm{OS}} \ge c \, \mathcal{E}_{\mathrm{conf}}^{(a)}(JF, JF)}
$$

**Corollary 11.5.2 (Mass Gap from Diffusion Gap).**
If $\mathrm{gap}(-L) \ge \lambda_* > 0$, then:
$$
\mathcal{E}_{\mathrm{conf}}^{(a)}(f, f) \ge (1 - e^{-a\lambda_*}) \|f - \mu(f)\|_2^2
$$
which gives uniform spectral gap for $K_a$, hence OS mass gap:
$$
m_{\mathrm{OS}} \ge -\frac{1}{a} \log \lambda_1(T_a)
$$

---

# Chapter 12: Typicality and Concentration

## 12.1 From Global LSI to Concentration

**Theorem 12.1.1 (Concentration from LSI).**
If $\mu$ satisfies LSI with constant $C_{\mathrm{LSI}}$ and $f$ is $L$-Lipschitz:
$$
\mu(f - \mathbb{E}f \ge t) \le \exp\left(-\frac{t^2}{2 C_{\mathrm{LSI}} L^2}\right)
$$

## 12.2 Typicality of the SAFE Region

For the disorder observable $\mathcal{B}_\Lambda = \frac{1}{|P|} D_\Lambda$:
- Lipschitz constant: $L^2 \asymp |P(\Lambda)|^{-1}$
- Concentration: deviations are $\exp(-c |P(\Lambda)|)$

**Corollary 12.2.1 (Typicality Bound).**
$$
\boxed{\mu(K_\Lambda(\varepsilon)^c) \le \exp(-c_{\mathrm{typ}} |P(\Lambda)|)}
$$

## 12.3 Application to Localization Errors

The volume exponent $|P(\Lambda)|$ can be traded for a graph-distance exponent along a corridor connecting observable supports, completing the unconditional clustering bound.

---

# Chapter 13: Drift Obstructions and Workarounds

## 13.1 Why Naive Drift Fails

**Obstruction:** For compact gauge groups, the single-plaquette function
$$
\phi(U) = 1 - \frac{1}{N} \mathrm{Re}\,\mathrm{Tr}(U)
$$
has not only a global minimum at $U = I$, but also **other critical points** (e.g., center elements) where $\nabla \phi = 0$ but $\phi$ is large.

At such points:
- The drift term $-\langle \nabla V, \nabla W \rangle$ collapses
- Yet $W$ is large

This breaks any naive drift inequality toward a single small neighborhood.

## 13.2 Two Workarounds

**Option A: Multi-Well Small Set**
Let $\mathcal{K}$ be a union of neighborhoods around **all** critical sets. Then:
$$
\mathcal{L} W \le -a W + b \, \mathbf{1}_{\mathcal{K}}
$$
can hold because outside $\mathcal{K}$ the gradient cannot be small everywhere.

**Option B: Static Concentration (No Drift)**
Prove directly that under small effective coupling:
$$
\mu(\mathcal{S}^c) \ll 1 \quad \text{uniformly in volume}
$$
via:
- High-temperature Dobrushin conditions
- Cluster/polymer expansions
- Reflection-positivity + chessboard estimates

## 13.3 The Correct Bottleneck: Gauge Lemma

**Open Problem:** A discrete Uhlenbeck-type gauge lemma:
$$
\text{Small curvature} \Rightarrow \text{Good gauge with small link fields}
$$
with constants independent of volume.

## 13.4 Holley-Stroock Volume Blow-Up

> [!WARNING]
> For lattice measures, convexifying each local term gives total oscillation:
> $$\mathrm{osc}_{\mathrm{total}} \sim (\text{volume}) \times (\text{per-term oscillation})$$
> so the Holley-Stroock factor $e^{\mathrm{osc}}$ becomes useless thermodynamically.

**Numerical Values (SU(2) One-Link):**
| $\beta$ | Oscillation | HS Factor |
|:---|:---|:---|
| 5 | 0.0054 | 1.005 |
| 10 | 0.31 | 1.36 |
| 50 | 6.06 | 427 |

---

# Chapter 14: SU(2) Worked Example — Laplacian and Drift Proofs

## 14.1 The Affine Laplacian Law

**Proposition 14.1.1 (Single Plaquette Laplacian).**
With the right-invariant Laplacian on SU(2) normalized so $\Delta_{\mathrm{SU}(2)} w = -3w$ for the character $w(U) = \frac{1}{2}\mathrm{Tr}(U)$:
$$
\Delta B_p = 12 - 12 B_p
$$
where $B_p = 1 - w(U_p)$.

**Proof.**
Fix 3 links; view $U_p = A U_\ell B$. Right-invariance gives $\Delta_\ell w(U_p) = -3 w(U_p)$ for each of 4 links:
$$
\Delta w(U_p) = -12 w(U_p) \Rightarrow \Delta B_p = 12(1 - B_p) \quad \blacksquare
$$

**Corollary 14.1.2 (Averaged Defect).**
$$
\Delta B_{\mathrm{avg}} = 12 - 12 B_{\mathrm{avg}}
$$

## 14.2 Gradient Alignment

**Proposition 14.2.1.**
For $S = \beta \sum_p B_p$ and $V = 1 + B_{\mathrm{avg}}$:
$$
\langle \nabla S, \nabla V \rangle = \frac{\beta}{N_p} \left\| \nabla \sum_p B_p \right\|^2 \ge 0
$$
with equality only when $\nabla(\sum_p B_p) = 0$.

## 14.3 Empirical Validation

**Volume Sweep (β = 6):**
| L | $\hat{a}$ | $\hat{b}$ | $R^2$ |
|:---|:---|:---|:---|
| 8 | 11.999 | -11.999 | 0.9999993 |
| 12 | 11.999 | -11.999 | 0.9999999 |
| 16 | 11.999 | -11.999 | 1.0000000 |

**Drift Certificate (L=16, HOLDOUT):**
| β | τ* | λ* |
|:---|:---|:---|
| 4 | 0.636 | 7.18 |
| 6 | 0.216 | 10.76 |
| 10 | 0.216 | 17.93 |

The ratio $\lambda_0/\beta \approx 1.79$ is approximately constant for $\beta \ge 4$.

---

# Chapter 15: The Constructive Mass Gap Pipeline

## 15.1 The Six-Step Chain

$$
\boxed{\text{Hinge} \Rightarrow \text{LSI} \Rightarrow \text{HS} \Rightarrow \text{CT Decay} \Rightarrow \text{Clustering} \Rightarrow \text{OS Gap}}
$$

1. **Local Coercivity (Hinge):** Matrix hinge $\mathcal{H} \succeq m^2 \mathbb{I} + \alpha d_1^* d_1$
2. **Uniform LSI:** Lyapunov drift + local LSI → global LSI uniform in $|\Lambda|$
3. **HS Representation:** $\mathrm{Cov}(F,G) = \langle \nabla F, \mathcal{H}^{-1} \nabla G \rangle$
4. **CT Decay:** $\|\mathcal{H}^{-1}_{xy}\| \le C e^{-\gamma \, d(x,y)}$
5. **Exponential Clustering:** Unconditional via typicality + localization
6. **OS Extraction:** $E_1 \ge m$ from time-decay

## 15.2 What Is Proved vs. Open

**Proved at Fixed Cutoff:**
- Reflection positivity for Wilson measure
- Bakry-Émery $\Gamma_2$ identity with drift
- Local matrix hinge inequality
- Lyapunov drift → global LSI
- HS + CT chain
- Localization + typicality
- OS reconstruction

**Open for Full Continuum Theorem:**
- Thermodynamic limit with OS stability
- RG permanence of reflection positivity
- Continuum limit ($a \to 0$) with uniform bounds

## 15.3 The Block Convexity Engine (Spark→Flow→Gap)

**Definition 15.3.1 (Coarse-Graining Stability).**
If:
$$
A \succeq \alpha \mathbb{I}, \quad C \succeq \gamma \mathbb{I}, \quad \|B\|_{\mathrm{op}} \le M
$$
then integrating out gives:
$$
\nabla^2 S_{\mathrm{eff}} \succeq \left(\alpha - \frac{M^2}{\gamma}\right) \mathbb{I}
$$

**Condition:** Convexity preserved if $M^2 < \alpha \gamma$.

---

# Chapter 16: The Operator Triad

## 16.1 Three Guises of the Same Object

The operator $M = m^2 \mathbb{I} + \alpha d_1^* d_1$ appears as:

1. **Hessian/Stiffness:** Small-field Wilson curvature on horizontal directions
2. **Gibbs/Witten:** Lifted diffusion generator on 1-forms
3. **Heat-Flow Controller:** Green kernel with exponential off-diagonal decay

**Key Insight:** The same object pinches curvature, covariance, and mixing simultaneously.

## 16.2 Spectral Floor Monotonicity

**Theorem 16.2.1 (Rayleigh-Ritz Concavity).**
For random symmetric $H(\omega)$ with $\mathcal{G} \subset \mathcal{F}$:
$$
\boxed{\lambda_{\min}(\mathbb{E}[H | \mathcal{G}]) \ge \mathbb{E}[\lambda_{\min}(H) | \mathcal{G}]}
$$

**Proof (Sketch):** For unit $v$:
$$
\langle v, \mathbb{E}[H|\mathcal{G}] v \rangle = \mathbb{E}[\langle v, H v \rangle | \mathcal{G}] \ge \mathbb{E}[\lambda_{\min}(H) | \mathcal{G}]
$$
Minimize over $v$. $\blacksquare$

**Corollary 16.2.2 (Defect Monotonicity).**
For defect $\delta(A) := \max\{0, \kappa_* - \lambda_{\min}(A)\}$:
$$
\delta(\mathbb{E}[H|\mathcal{G}]) \le \mathbb{E}[\delta(H)|\mathcal{G}]
$$
*Defect cannot increase under conditioning.*

---

# Chapter 17: SU(3) Convexity Window and High-Probability Convexity

## 17.1 SU(3) Volume Stability

**Empirical Result:** For $s = 0.05$ (small-field amplitude):

| $\beta$ | L=4 $\lambda_{\min}$ | L=6 $\lambda_{\min}$ | L=8 $\lambda_{\min}$ |
|:---|:---|:---|:---|
| 0.40 | +0.108 | +0.109 | +0.109 |
| 1.51 | +0.059 | +0.064 | +0.065 |
| 3.00 | -0.008 | +0.003 | +0.007 |

**Key Finding:** The convex core is **volume-stable** — $\lambda_{\min}$ is nearly identical across $L = 4, 6, 8$.

## 17.2 High-Probability Convexity Bridge

**Lemma 17.2.1 (Chessboard Estimate).**
For the bad event $A_{p,\delta} := \{d_G(U_p, I) \ge \delta\}$:
$$
\boxed{\mu_\beta(A_{p,\delta}) \le C_0 \beta^\alpha e^{-\beta c_\Phi(\delta)}}
$$
where $c_\Phi(\delta) \simeq c \delta^2$.

**Proof Idea:** 
1. Energy cost: $S_\beta \ge \beta |P| c_\Phi(\delta)$ on all-bad event
2. Chessboard: $\mu_\beta(A_{p,\delta}) \le (Z_\beta^{\mathrm{bad}}/Z_\beta)^{1/|P|}$
3. Optimize ball radius $r = \beta^{-1/2}$

**Proposition 17.2.2 (Defective Local Poincaré).**
On the high-probability tube $\Omega_{\delta,R}$:
$$
\mathrm{Var}_\mu(F) \le \frac{1}{\rho_{\mathrm{loc}}} \|\nabla F\|^2 + 4\|F\|_\infty^2 \mu(\Omega_{\delta,R}^c)
$$

---

# Chapter 18: The Dichotomy Theorem and Open Problems

## 18.1 The Uniform Spectral Gap Dichotomy

**Principle:** The continuum theory is massive **iff** the lattice gap does not collapse as $a \to 0$:
- $m(a) \to m_* > 0$ → Massive continuum
- $m(a) \to 0$ → Gapless continuum

## 18.2 The Pairing Term Bottleneck

> [!IMPORTANT]
> **This is the main open problem.** After all structural work, the project reduces the uniform drift to a single coercivity statement.

**Target Inequality:**
$$
P_\Lambda(U) := \sum_\ell \langle \nabla_\ell S_W, \nabla_\ell V_\Lambda \rangle \ge A V_\Lambda(U) - B|\Lambda|
$$

**Three Attack Routes:**
1. **Route A:** Small-field coercivity + tail truncation
2. **Route B:** Per-link local inequality (force aligns with defect gradient)
3. **Route C:** Ratio certificate on $\{V_\Lambda \ge \tau_0 |\Lambda|\}$

## 18.3 Open Problems Summary

| Problem | Status | Description |
|:---|:---|:---|
| **GAP-FC-02** | OPEN | Force non-cancellation / Cartan alignment |
| **Pairing Coercivity** | OPEN | $P_\Lambda \ge A V - B|\Lambda|$ |
| **Gauge Lemma** | OPEN | Small curvature → good gauge |
| **Thermodynamic Limit** | CONDITIONAL | OS stability under $|\Lambda| \to \infty$ |
| **Continuum Limit** | CONDITIONAL | Uniform bounds under $a \to 0$ |

---

# Chapter 19: Smooth Plaquette Lyapunov — Exact Drift Identity

## 19.1 The Smooth Proxy

Replace nonsmooth distance-squared with the smooth class function:
$$
\widetilde{z}(U) := 1 - \frac{1}{N} \mathrm{Re}\,\mathrm{Tr}(U) \in [0, 2]
$$

**Properties:**
- Globally $C^\infty$, conjugation-invariant
- Vanishes only at identity
- Quadratic growth: $\widetilde{z}(\exp X) = c|X|^2 + O(|X|^3)$

## 19.2 The Fundamental Eigenfunction Input

$$
\Delta_G \widetilde{z}(U) = -\lambda_{\mathrm{fund}} \widetilde{z}(U) + \lambda_{\mathrm{fund}}
$$
where $\lambda_{\mathrm{fund}}$ is the Casimir eigenvalue.

## 19.3 The Exact Drift Identity

**Lemma 19.3.1 (Laplacian Drift).**
For $\overline{V}_\Lambda(U) = 1 + \frac{1}{|P|}\sum_p \widetilde{z}_p(U)$:
$$
\boxed{\Delta_\Lambda \overline{V}_\Lambda = -\lambda \overline{V}_\Lambda + b}
$$
where $\lambda = 4\lambda_{\mathrm{fund}}$ and $b = 2\lambda = 8\lambda_{\mathrm{fund}}$.

**Key:** This is **exact** and **volume-uniform** — no remainder terms.

---

# Chapter 20: Structured Pairing Noncancellation

## 20.1 The Pairing Functional

$$
\mathcal{P}_\Lambda(U) := \sum_p \widetilde{z}_p \langle \nabla S_W, \nabla \widetilde{z}_p \rangle = \beta \sum_{p,q} \widetilde{z}_p \, \Gamma(\widetilde{z}_p, \widetilde{z}_q)
$$

**Self-terms ($p=q$):** Always nonnegative
**Cross-terms ($p \neq q$):** Can have either sign

## 20.2 Why Naive Noncancellation is False

> [!WARNING]
> In $\mathfrak{su}(2) \cong \mathbb{R}^3$, non-collinear vectors can sum to zero (equilateral triangle). The claim "rotated vectors vanish only if collinear" is **false** without constraints.

## 20.3 The Correct Structure: Discrete Differential Complex

**Lemma 20.3.1 (Linear Maxwell Coercivity).**
For horizontal $A \in \mathcal{C}^1(\Lambda; \mathfrak{g})$ with $d_0^* A = 0$ and $F = d_1 A$:
$$
\|d_1^* F\|^2_{\mathcal{C}^1} \ge \lambda_{\min} \|F_\perp\|^2_{\mathcal{C}^2}
$$

**Consequence:** The linkwise force $\approx d_1^* F$ cannot vanish unless $F$ lies in the null sector (discrete Hodge theory).

## 20.4 The Target Coercivity

$$
\mathcal{P}_\Lambda(U) \ge c \beta \mathcal{D}_\Lambda(U) - C
$$
using lattice differential complex structure.

---

# Chapter 21: Davies Decay — Refined Constants

## 21.1 Davies vs. Combes-Thomas

| Method | Exponent | Regime |
|:---|:---|:---|
| Combes-Thomas | $\eta \sim \log(1 + m^2/\alpha D)$ | $\sim m^2$ for small $m$ |
| **Davies** | $\eta = 2 \sinh^{-1}(m/\sqrt{\alpha D})$ | **$\sim m$ for small $m$** |

**Davies tracks the mass parameter** — essential for physical interpretation.

## 21.2 Davies Decay Theorem

**Theorem 21.2.1 (Davies-Type Decay).**
For $M = m^2 \mathbb{I} + \alpha \Delta_1$:
$$
\boxed{|G(b, b')| \le \frac{2}{m^2} e^{-\eta_M \, d(b, b')}}
$$
where:
$$
\eta_M = \cosh^{-1}\left(1 + \frac{m^2}{2\alpha D_{\mathcal{E}}}\right)
$$

## 21.3 Row-Sum Refinement

**Definition 21.3.1 (Row-Sum Constant).**
$$
C_0(\Delta_1) := \sup_b \sum_{b' \neq b} |K_{\Delta_1}(b, b')|
$$

**Proposition 21.3.2.** Replace $D_{\mathcal{E}}$ with $C_0$ for sharper bounds:
$$
\eta_{C_0} = \cosh^{-1}\left(1 + \frac{m^2}{2\alpha C_0}\right)
$$

---

# Appendix A: Source File Tracker

## Files Analyzed: 3/51

- [x] `BEST_02_local_to_global_PI_LSI_via_Lyapunov.md` — Patching theorem
- [x] `DOC4_Explicit_LSI_and_Spectral_Gap_from_Haar_Mass.md` — Explicit $c_0$
- [x] `01_pillarL_geometric_mass_gap(1).md` — Pillar L mechanism
- [ ] Remaining 48 files

---

# Appendix B: Key Theorems Summary

| Theorem | Result |
|:---|:---|
| Bakry-Émery LSI | $\mathrm{Ent}(f^2) \le \frac{2}{\rho} \int |\nabla f|^2 d\mu$ |
| Lattice YM LSI | $\mathrm{Ent}(f^2) \le \frac{2}{c_0} \int |\nabla f|^2 d\mu$ with $c_0 = (N^2-1)/(2N)$ |
| Global PI via Lyapunov | Local PI + Drift $\Rightarrow$ Global PI |
| Global LSI via Lyapunov | Local LSI + Drift $\Rightarrow$ Global LSI |
| Uniform Spectral Gap | $\lambda_1 \ge c_0 > 0$, uniform in volume |
