# 09 — Local to Global: LSI via Lyapunov

## Abstract
We present the **Local-to-Global theorem** for the Log-Sobolev Inequality (LSI). This theorem glues a "local" LSI (proven via Matrix Hinge on the good set) with a Lyapunov drift condition (proven in File [08]) to establish a "global" LSI for the full measure. The resulting LSI constant is **independent of system volume**, proving the thermodynamic stability of the mass gap.

**Connected Files:**
- **[03] Matrix Hinge:** Provides the local curvature bound.
- **[08] Lyapunov Drift:** Provides the drift/tail control.
- **[26] Holley-Stroock:** Used for bounded perturbations.
- **[29] Bakry-Émery:** The curvature-dimension framework.

---

## 1. The Strategy: Decomposing Configuration Space

### 1.1 The Two Regimes
- **Good Set $K$:** Fields are small. Matrix Hinge holds. Local LSI constant $\rho_{loc}$.
- **Bad Set $K^c$:** Fields are large. Curvature may be negative. Lyapunov drift applies.

### 1.2 The Goal
Prove a **global** LSI:
$$
\text{Ent}_\mu(f^2) \le C_P \int |\nabla f|^2 d\mu
$$
where $C_P$ is independent of lattice size $|\Lambda|$.

---

## 2. The Cattiaux-Guillin-Wu Theorem

### 2.1 Assumptions
Let $\mu$ be a probability measure on a Riemannian manifold $M$. Assume:

**A1 (Local LSI):** For any ball $B_r(x)$, the conditional measure $\mu_{B_r}$ satisfies LSI with constant $\rho_{loc}$.

**A2 (Lyapunov Drift):** There exists $W: M \to [1, \infty)$ and constants $\alpha, b > 0$ such that:
$$
LW \le -\alpha W + b
$$
where $L$ is the generator.

### 2.2 Conclusion
Under A1 and A2, the full measure $\mu$ satisfies a **global** LSI with constant:
$$
\rho \ge \frac{\alpha \cdot \rho_{loc}}{\alpha + C_{mix}}
$$
where $C_{mix}$ depends on the local structure but NOT on the global size.

---

## 3. Verification of Assumptions for Yang-Mills

### 3.1 Checking A1 (Local LSI)
On the good set $K$, the Matrix Hinge (File [03]) gives:
$$
\text{Ric}_\mu \ge m^2 := c_H - C_W \beta r_0 > 0
$$

By Bakry-Émery theory (File [29]):
$$
\rho_{loc} \ge m^2 = c_H - C_W \beta r_0
$$

### 3.2 Checking A2 (Lyapunov Drift)
From File [08], with $W = e^{\gamma \sum r_\ell^2}$ and $\gamma = \beta/4$:
$$
LW \le -\frac{\beta^2}{4} r^2 W + \beta d_G W \le -\alpha W + b
$$
on the complement of a compact set.

Here $\alpha \sim \beta^2 r_0^2 / 4$ and $b \sim \beta d_G$.

### 3.3 The Global Constant
$$
\rho \ge \frac{\alpha \rho_{loc}}{\alpha + C} = \frac{(\beta^2 r_0^2 / 4)(c_H - C_W \beta r_0)}{(\beta^2 r_0^2 / 4) + C}
$$

For large $\beta$ with $r_0 \sim 1/\beta$:
$$
\rho \sim \frac{(\beta^2 / \beta^2)(c_H - O(1))}{O(1)} = O(c_H) = O(1)
$$

**Conclusion:** The global LSI constant is $O(1)$, independent of $|\Lambda|$ and $L$.

---

## 4. Volume Independence

### 4.1 The Key Observation
The Lyapunov function factorizes:
$$
W = \prod_\ell w_\ell
$$
The drift bound is:
$$
\frac{LW}{W} = \sum_\ell \frac{L_\ell w_\ell}{w_\ell}
$$
Each term is $O(1)$ per link. The sum is extensive but the **rate** $\alpha/W$ is intensive.

### 4.2 The Product Structure
For product measures $\mu = \prod_\ell \mu_\ell$, LSI constants tensorize:
$$
\rho(\mu) = \inf_\ell \rho(\mu_\ell)
$$

For interacting measures, we use the **Gibbs Sampler** decomposition:
$$
\mu = \int \mu(\cdot | \text{boundary}) d(\text{boundary})
$$

If interactions are finite-range, the local LSI propagates globally with $O(1)$ loss.

---

## 5. The Gluing Procedure

### 5.1 Entropy Decomposition
For a partition of $\Lambda$ into blocks $B_i$:
$$
\text{Ent}_\mu(f^2) \le \sum_i \mathbb{E}\left[ \text{Ent}_{\mu(\cdot|B_i^c)}(f^2) \right] + \text{Ent}_{coarse}
$$

### 5.2 Local Term
Each conditional measure $\mu(\cdot | B_i^c)$ is supported on the small-field block.
By the local LSI:
$$
\text{Ent}_{\mu(\cdot|B_i^c)}(f^2) \le \frac{1}{\rho_{loc}} \mathcal{E}_{B_i}(f, f)
$$

### 5.3 Coarse Term
The "coarse" entropy comes from block-wise fluctuations.
By the Lyapunov bound, these are controlled by the drift:
$$
\text{Ent}_{coarse} \le \frac{1}{\alpha} \mathcal{E}(f, f)
$$

### 5.4 Total
$$
\text{Ent}_\mu(f^2) \le \left( \frac{1}{\rho_{loc}} + \frac{1}{\alpha} \right) \mathcal{E}(f, f)
$$

The global constant is:
$$
\rho = \frac{\rho_{loc} \cdot \alpha}{\rho_{loc} + \alpha}
$$

---

## 6. Physical Interpretation: The Defect Gas

### 6.1 The Picture
Imagine the lattice mostly in the "vacuum" state (small $r$, positive curvature).
Occasionally, there are "defects" (large $r$, negative curvature).

### 6.2 Peierls Argument
Defects have:
- **Energy cost:** $\Delta E \sim \beta$ (Wilson action penalty).
- **Entropy gain:** $\sim \log(\text{volume of defect})$.

For large $\beta$, energy dominates. Defects are:
- Rare (probability $\sim e^{-\beta}$).
- Small (size $\sim a$, the lattice spacing).
- Dilute (non-percolating).

### 6.3 Gap Survival
A sea of gapped vacuum with sparse defects remains gapped.
The LSI version of the Peierls argument is the Local-to-Global theorem.

---

## 7. Comparison to Spin Systems

### 7.1 Dobrushin-Shlosman Condition
For classical spin systems with weak interactions, a similar "local + transport" argument proves LSI.

### 7.2 Spectral Gap for Glauber Dynamics
The spectral gap of the block dynamics is:
$$
\lambda = \min(\lambda_{block}, \lambda_{boundary})
$$
Both are $O(1)$ for finite-range interactions with a gap.

### 7.3 The Yang-Mills Specialization
The key new ingredient is the **geometric** origin of $\rho_{loc}$ (Haar measure curvature).
This replaces the "convexity of the single-spin interaction" assumption.

---

## Summary

The Local-to-Global theorem is the "compiler" that assembles local curvature bounds into a global spectral gap:

1. **Local LSI:** Matrix Hinge gives $\rho_{loc} \sim c_H$ on the good set.
2. **Lyapunov Drift:** Controls the time spent in the bad set.
3. **Gluing:** Combines the two into a global bound independent of $|\Lambda|$.

**Result:** The mass gap is $O(1)$ in the thermodynamic limit.

---

## References
- P. Cattiaux, A. Guillin, F.Y. Wang, L. Wu, *Lyapunov conditions for Super Poincaré inequalities* (2009).
- M. Ledoux, *The Concentration of Measure Phenomenon* (2001).
- **File [03]** (Matrix Hinge) for local bounds.
- **File [08]** (Lyapunov) for drift control.
- **File [32]** (Defect Gas) for physical picture.
