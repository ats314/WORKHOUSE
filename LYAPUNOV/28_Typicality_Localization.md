# 28 — Typicality and Localization

## Abstract
We resolve the tension between local analytic control (which requires small fields) and global thermodynamics (which involves large fluctuations) using the concept of **Typicality**. By combining restricted functional inequalities with Lyapunov drift, we show that "bad" regions are exponentially rare and do not spoil the global mass gap.

**Connected Files:**
- **[09] Local-to-Global:** The gluing engine.
- **[08] Lyapunov Drift:** The mechanism ensuring return to the core.
- **[32] Defect Gas:** The physical picture of rare bad regions.

---

## 1. The Localization Problem

### 1.1 "Good" vs "Bad" Sets
- **Core Set $K$:** Small fields, convex potential, positive curvature.
- **Rough Region $M \setminus K$:** Large fields, possible concavity, Gribov copies.

Functional inequalities are easy to prove on $K$ (restricted Poincaré/LSI) but hard globally.

### 1.2 The Strategy
1. Prove restricted inequalities on $K$.
2. Prove drift condition: dynamics naturally return to $K$.
3. "Glue" them to get global inequalities with constants independent of volume.

---

## 2. Restricted Functional Inequalities

### 2.1 Restricted LSI
Assume on the core set $K$:
$$
\text{Ent}_{\mu^K}(f^2) \le 2 C_{LSI}(K) \int_K \|\nabla f\|^2 d\mu^K
$$
This is plausible because $K$ has positive Bakry-Émery curvature (via Matrix Hinge [03]).

---

## 3. Lyapunov Drift and Exponential Tails

### 3.1 Foster-Lyapunov Condition
*(From source: CURATED_04_Drift_Gluing_Typicality.md)*

There exists a Lyapunov function $V \ge 1$ (e.g., $V = e^{\eta S}$) such that:
$$
L V \le -\lambda V + b \mathbf{1}_K
$$
This implies that the process descends rapidly outside $K$ and regenerates inside $K$.

### 3.2 Tail Bound
$$
\int V d\mu \le \frac{b}{\lambda} \mu(K) < \infty
$$
This yields exponential concentration for the disorder observable $D(U) \sim S(U)$:
$$
\mu(D \ge t) \lesssim e^{-ct}
$$

### 3.3 Uniformity
Crucially, if the drift rate $\lambda$ is local, the concentration is **uniform in total volume**.

---

## 4. Typicality Estimates

### 4.1 Concentration of Measure
If global LSI holds, Lipschitz functions concentrate:
$$
\mu(|f - \mathbb{E}f| \ge t) \le \exp\left(-\frac{t^2}{2C_{LSI}L^2}\right)
$$

### 4.2 The "Bad Set" is Rare
Let $K_\Lambda(\epsilon)^c$ be the set where the average plaquette action exceeds $\epsilon$.
$$
\mu(K_\Lambda(\epsilon)^c) \le \exp(-c_{typ} |P(\Lambda)|)
$$
The probability of being " globally bad" is exponentially small in the volume.

---

## 5. Covariance Decomposition

To prove clustering $\text{Cov}(f,g) \to 0$, we split based on typicality:

$$
\text{Cov}(f,g) = \underbrace{\text{Cov}_{\mu^K}(f,g)}_{\text{Fast decay on } K} + \underbrace{\text{Error terms}}_{\text{Controlled by tails}}
$$

With exponential tails, the error terms are negligible, and the global decay is controlled by the geometry of $K$.

---

## 6. The "Gap" in the Argument: Force Non-Cancellation

To prove the drift condition (3.1), we need:
$$
\langle \nabla S, \nabla V \rangle \ge c V \quad \text{outside } K
$$
This requires that the gradient of the action (the force) does not vanish when the action is large.
This is **GAP-FC-02**. (See File [27] Cartan Alignment).

---

## Summary

**Typicality** allows us to:
1. Focus analytic proofs on the "good" core $K$.
2. Treat the rest of configuration space as a "dilute gas" of defects.
3. Quantify the error purely in terms of rare event probabilities.

This replaces the "Cluster Expansion" of the 1980s with a modern "Functional Inequality + Concentration" framework.

---

## References
- **Source:** `CURATED_04_Drift_Gluing_Typicality.md`
- P. Cattiaux at al., *A constructive approach to Log-Sobolev inequalities* (2010).
- M. Hairer, J. Mattingly, *Spectral gaps in Wasserstein distances* (2008).
