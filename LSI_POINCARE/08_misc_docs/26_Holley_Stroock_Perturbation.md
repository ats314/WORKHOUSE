# 26 — Holley-Stroock Perturbation and Convexification

## Abstract
We examine the **Holley-Stroock lemma** as a tool to handle small non-convexities in the potential. While powerful for single modes, we analyze its **volume blow-up** failure mode in lattice theories and discuss advanced "convexification via chord" strategies.

**Connected Files:**
- **[09] Local-to-Global:** Why we need volume-independent bounds.
- **[31] Strong Coupling:** A regime where HS works locally.
- **[25] Brascamp-Lieb:** The convex baseline.

---

## 1. The Holley-Stroock Lemma

### 1.1 Statement
Let $d\mu \propto e^{-S}$ and $d\tilde{\mu} \propto e^{-\tilde{S}}$.
Define the oscillation of the perturbation:
$$
\text{osc} = \sup(S - \tilde{S}) - \inf(S - \tilde{S})
$$
Then the spectral gaps satisfy:
$$
\lambda(\mu) \ge e^{-\text{osc}} \lambda(\tilde{\mu})
$$

### 1.2 Usage
If $S$ is non-convex but close to a convex $\tilde{S}$, we get a gap!

---

## 2. The Toy Model: Convexification by Chord

### 2.1 The Concave Dip
Consider the Haar-Wilson potential:
$$
S_\beta(\theta) = -2\log\left(\frac{\sin \theta}{\theta}\right) - \beta \cos \theta
$$
For $\beta > \beta_c$, it develops a concave dip near $\theta = 0$ (or boundary).

### 2.2 Chord Replacement
Replace the dip with the linear chord connecting the inflection points.
This creates a strictly convex $\tilde{S}$.

### 2.3 Numerical Values
*(From source: HAAR/04_HolleyStroock_Oscillation.md)*

| $\beta$ | Oscillation Factor $e^{\text{osc}}$ |
|---|---|
| 5 | 1.005 (Tiny) |
| 10 | 1.36 (Manageable) |
| 50 | 427.0 (Blow-up) |

---

## 3. The Volume Catastrophe

### 3.1 Extensive Scaling
On a lattice, $S_{total} = \sum S_{plaq}$.
If we convexify each plaquette:
$$
\text{osc}_{total} \approx |P(\Lambda)| \cdot \text{osc}_{single}
$$
The gap bound becomes:
$$
\lambda \ge e^{-L^4 \cdot \text{osc}} \lambda_{convex}
$$
This vanishes exponentially with volume! **HS cannot be used directly on the whole lattice.**

---

## 4. Advanced Strategies

To avoid volume blow-up, we must apply HS **locally** or **conditionally**.

### 4.1 Cluster Expansion
Treat the non-convexities as rare defects.
Use cluster expansion to control the ratio $Z_{nonconvex}/Z_{convex}$.

### 4.2 Conditional LSI
Condition on the "good set" where convexity holds.
Use HS only for the small fluctuations within the "bad set" boundaries.

---

## Summary

- **Holley-Stroock** is the "price of non-convexity".
- It works perfectly for **single links** or small blocks.
- It fails (volume catastrophe) for the **global system**.
- **Conclusion:** We must use **Lyapunov Drift** (File [08]) to globalize, not global Holley-Stroock.

---

## References
- **Source:** `04_HolleyStroock_Oscillation.md`
- R. Holley, D. Stroock, *Logarithmic Sobolev inequalities and stochastic Ising models* (1987).
