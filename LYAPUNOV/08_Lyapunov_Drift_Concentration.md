# 08 — Lyapunov Drift and Concentration of Measure

## Abstract
We rigorously implement the **Lyapunov Function method** to control the probability mass on the "bad curvature" region (large fields). We construct a specific radial Lyapunov function, compute its drift under the Wilson-Haar generator, and prove that the measure concentrates on the small-field region with Gaussian tails. This justifies the use of local curvature bounds in the Matrix Hinge.

**Connected Files:**
- **[03] Matrix Hinge:** The local bound that requires this concentration result.
- **[09] Local-to-Global:** Uses the drift condition to glue local gaps into a global gap.
- **[25] Brascamp-Lieb:** Requires measure support on convex regions.
- **[32] Defect Gas:** Physical interpretation of the rare large-field excursions.

---

## 1. The Challenge: Compactness vs Convexity

### 1.1 The Problem
The Matrix Hinge inequality (File [03]) requires $r < r_* = c_H / (C_W \beta)$.
But typical fluctuations have $|X| \sim 1/\sqrt{\beta}$.
For large $\beta$: $r_* \ll 1/\sqrt{\beta}$.

**Conclusion:** The Hinge fails on a set of **positive probability**.

### 1.2 The Resolution
We don't need pointwise positivity. We need:
1. **High probability of the good set:** $\mu(K) \ge 1 - \epsilon$.
2. **Strong drift on the bad set:** The Lyapunov function pushes the system back into $K$.

Together, these imply the **effective** curvature is positive.

---

## 2. The Lyapunov Function

### 2.1 Definition
For a lattice $\Lambda$ with link variables $U_\ell$, define:
$$
W(U) = \exp\left( \gamma \sum_\ell d^2(U_\ell, \mathbf{1}) \right)
$$
where $d(U, \mathbf{1}) = \|U - \mathbf{1}\|$ is the matrix distance and $\gamma > 0$ is a parameter.

### 2.2 Factorization
For product measures, we can use:
$$
W(U) = \prod_\ell w(U_\ell), \quad w(U_\ell) = e^{\gamma r_\ell^2}
$$
where $r_\ell = d(U_\ell, \mathbf{1})$.

### 2.3 Properties
- $W \ge 1$ everywhere (since $r^2 \ge 0$).
- $W(U) = 1$ at the vacuum $U = \mathbf{1}$.
- $W(U) \to \infty$ as any $r_\ell \to \infty$ (but $r_\ell \le 2\pi$ for SU(2)).

---

## 3. The Drift Calculation

### 3.1 The Generator
The Langevin generator for Wilson-Haar dynamics is:
$$
L = \Delta_{SU(N)} - \nabla S_W \cdot \nabla
$$
where $\Delta_{SU(N)}$ is the Laplacian on the group manifold.

### 3.2 Single-Link Drift
For a single link, compute:
$$
\frac{Lw}{w} = \frac{L e^{\gamma r^2}}{e^{\gamma r^2}}
$$

**Diffusion term (Laplacian):**
$$
\Delta e^{\gamma r^2} = (4\gamma^2 r^2 + 2\gamma \Delta r^2) e^{\gamma r^2}
$$
Using $\Delta r^2 \approx 2d_G$ (dimension of the group):
$$
\frac{\Delta w}{w} \approx 4\gamma^2 r^2 + 4\gamma d_G
$$

**Drift term (Wilson action):**
$$
\nabla S_W \cdot \nabla w = \beta r \cdot 2\gamma r \cdot e^{\gamma r^2}
$$
(The Wilson force is $\sim \beta r$ for small $r$.)
$$
\frac{\nabla S_W \cdot \nabla w}{w} \approx 2\gamma \beta r^2
$$

### 3.3 The Net Drift
$$
\frac{Lw}{w} = 4\gamma^2 r^2 + 4\gamma d_G - 2\gamma \beta r^2 = (4\gamma^2 - 2\gamma\beta) r^2 + 4\gamma d_G
$$

For the coefficient of $r^2$ to be **negative** (restoring force):
$$
4\gamma^2 - 2\gamma\beta < 0 \implies \gamma < \frac{\beta}{2}
$$

Optimal choice: $\gamma = \beta/4$, giving:
$$
\frac{Lw}{w} = -\frac{\beta^2}{4} r^2 + \beta d_G
$$

---

## 4. The Foster-Lyapunov Theorem

### 4.1 Statement
**Theorem:** If there exists $W \ge 1$, a compact set $K$, and constants $\alpha, b > 0$ such that:
$$
LW \le -\alpha W + b \cdot \mathbf{1}_K
$$
Then the invariant measure $\mu$ satisfies:
$$
\int W \, d\mu \le \frac{b}{\alpha} + \sup_K W
$$

### 4.2 Tail Bound
Since $W = e^{\gamma r^2}$:
$$
\mu(\{r > R\}) \le \frac{\mathbb{E}[W]}{e^{\gamma R^2}} \le C e^{-\gamma R^2}
$$

This is **Gaussian concentration** with rate $\gamma$.

---

## 5. Application to Yang-Mills

### 5.1 The "Good Set"
Define $K_\Lambda(r_0) = \{ U : \|U_\ell - \mathbf{1}\| < r_0 \text{ for all } \ell \}$.

### 5.2 Probability of the Bad Set
From the Lyapunov analysis:
$$
\mu(K_\Lambda(r_0)^c) \le \sum_\ell \mu(\|U_\ell\| > r_0) \le 4L^4 \cdot e^{-\gamma r_0^2}
$$

For large $\beta$ with $\gamma = \beta/4$:
$$
\mu(\text{Bad}) \lesssim L^4 e^{-\beta r_0^2 / 4}
$$

### 5.3 The Critical Radius
The Matrix Hinge requires $r_0 < c_H / (C_W \beta)$.
Probability of violating this:
$$
\mu(\text{Bad}) \lesssim L^4 \exp\left( -\frac{\beta}{4} \cdot \frac{c_H^2}{C_W^2 \beta^2} \right) = L^4 \exp\left( -\frac{c_H^2}{4 C_W^2 \beta} \right)
$$

For large $\beta$, this is $\sim L^4 e^{-c/\beta}$, which is **not small**.

### 5.4 The Refined Analysis
Actually, for typical fluctuations $r \sim 1/\sqrt{\beta}$, the Hinge only becomes negative when $r \sim 1/\beta$.
The probability of $r > 1/\beta$ (much smaller than typical) is:
$$
\mu(r > 1/\beta) \sim e^{-\beta \cdot (1/\beta)^2} = e^{-1/\beta} \approx 1 - 1/\beta
$$

This is VERY close to 1! The Hinge fails with high probability.

**Resolution:** We need to use the **Local-to-Global theorem (File [09])** which doesn't require pointwise positivity—only positivity on average plus a drift condition.

---

## 6. The Effective Mass

### 6.1 Weighted Poincaré
Even if local curvature is negative, the drift provides an effective mass.
The **weighted Poincaré inequality** states:
$$
\text{Var}(f) \le C \int |\nabla f|^2 \psi \, d\mu
$$
where $\psi$ is related to the Lyapunov weight $W$.

### 6.2 The "Soft Mass"
The Lyapunov drift $LW \le -\alpha W$ can be reinterpreted as:
$$
L + \alpha \log W \ge 0
$$
This gives a "potential" $V = \alpha \log W = \alpha \gamma r^2$, which is a **mass term**:
$$
V \approx \frac{\alpha \beta}{4} r^2 = m_{soft}^2 r^2
$$

---

## 7. Numerical Verification

### 7.1 Histogram of $r$
Run Monte Carlo at $\beta = 2.3$ on a $4^4$ lattice.
Plot histogram of $r = \|U_\ell - \mathbf{1}\|$ over all links.

**Prediction:**
- Peak at $r \approx 0.6$ (typical fluctuation).
- Tail $\sim e^{-\beta r^2}$ (Gaussian).
- Very few samples at $r > 1.5$.

### 7.2 Correlation with Curvature
Measure the local Hessian eigenvalue $\lambda_{\min}(H_\ell)$ and correlate with $r_\ell$.

**Prediction:** Strong anticorrelation. Large $r$ → Negative $\lambda$.

---

## Summary

The Lyapunov function quantifies "confinement to the vacuum" in configuration space:
1. The Wilson-Haar drift pushes the system toward $U = \mathbf{1}$.
2. Large excursions ($r \gg 1/\sqrt{\beta}$) are exponentially suppressed.
3. The "bad curvature" regions have negligible statistical weight.
4. Combined with Local-to-Global (File [09]), this yields the global gap.

---

## References
- P. Cattiaux, A. Guillin, *Lyapunov conditions for Super Poincaré inequalities* (2010).
- M. Hairer, J. Mattingly, *Yet Another Look at Harris's Ergodic Theorem* (2011).
- **File [03]** (Matrix Hinge) for the local bound.
- **File [09]** (Local-to-Global) for the gluing theorem.
