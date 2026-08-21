# 32 — Defect Gas Interpretation

## Abstract
We model "bad curvature" regions as a **dilute defect gas**. Competition between energy cost (Wilson) and entropy gain (Haar) keeps defects rare for large $\beta$. This justifies Local-to-Global gluing.

**Connected Files:**
- **[08] Lyapunov Drift:** Rigorous version.
- **[09] Local-to-Global:** Uses diluteness for gluing.

---

## 1. Defect Definition

A location $x$ is a "defect" if $\rho(x) < 0$ (negative curvature).
This happens when $\text{Tr}(U_p) \ll 1$.

---

## 2. Free Energy Balance

- **Energy cost:** $\Delta E \sim \beta$.
- **Entropy gain:** $\sim \log(\text{Haar volume})$.

Probability: $p \sim e^{-\beta}$.
For large $\beta$: Defects are exponentially rare.

---

## 3. Peierls Argument

Percolation requires $p > p_c$.
Since $p \sim e^{-\beta}$, defects don't percolate for large $\beta$.
The vacuum is a "solid" of positive curvature with rare "liquid" bubbles.

---

## References
- R. Peierls, *On Ising's model of ferromagnetism* (1936).
