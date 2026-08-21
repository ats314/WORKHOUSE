# 29 — Bakry-Émery Curvature-Dimension Theory

## Abstract
We review the **Bakry-Émery** $CD(\rho, N)$ condition, which unifies spectral gap, log-Sobolev, and diameter bounds under a single curvature framework. This is the "operating system" for the geometric mass gap analysis.

**Connected Files:**
- **[38] Bochner Identity:** The derivation engine.
- **[03] Matrix Hinge:** Verifies the $CD$ condition for YM.
- **[09] Local-to-Global:** Uses $CD$ for gluing.

---

## 1. The Carré du Champ Operators

### 1.1 First Order: $\Gamma$
For generator $L$ with invariant measure $\mu$:
$$
\Gamma(f, g) = \frac{1}{2}(L(fg) - fLg - gLf)
$$
On Riemannian manifolds: $\Gamma(f) = |\nabla f|^2$.

### 1.2 Second Order: $\Gamma_2$
$$
\Gamma_2(f) = \frac{1}{2}(L\Gamma(f) - 2\Gamma(f, Lf))
$$

By Bochner (File [38]):
$$
\Gamma_2(f) = \|\nabla^2 f\|_{HS}^2 + \text{Ric}_\mu(\nabla f, \nabla f)
$$

---

## 2. The $CD(\rho, N)$ Condition

### 2.1 Definition
The measure $\mu$ satisfies $CD(\rho, N)$ if:
$$
\Gamma_2(f) \ge \rho \Gamma(f) + \frac{1}{N}(Lf)^2
$$
for all smooth $f$.

### 2.2 Components
- **$\rho$:** Lower bound on (weighted) Ricci curvature.
- **$N$:** Effective dimension (can be $\infty$).

---

## 3. Consequences of $CD(\rho, N)$

### 3.1 Spectral Gap (Lichnerowicz)
If $\rho > 0$:
$$
\lambda_1(-L) \ge \rho
$$

### 3.2 Log-Sobolev Inequality
$$
\text{Ent}_\mu(f^2) \le \frac{2}{\rho} \int |\nabla f|^2 d\mu
$$

### 3.3 Diameter Bound (Bonnet-Myers)
If $\rho > 0$ and $N < \infty$:
$$
\text{diam}(M) \le \pi\sqrt{\frac{N-1}{\rho}}
$$

### 3.4 Hypercontractivity
The semigroup $P_t = e^{tL}$ is hypercontractive:
$$
\|P_t f\|_q \le \|f\|_p \quad \text{for } q = 1 + (p-1)e^{2\rho t}
$$

---

## 4. Horizontal Extension for Gauge Theory

### 4.1 The Problem
The Wilson action is flat along gauge orbits.
Full-space $CD$ is impossible.

### 4.2 The Solution
*(From source: UNIFY_02_Horizontal_Bakry_Emery_Core_Theorem.md)*

For gauge-invariant observables $f$:
$$
\nabla f(U) \in H_U \quad \text{(horizontal)}
$$

It suffices to verify **horizontal** curvature:
$$
\text{Ric}_\mu(U)(W,W) \ge \rho|W|^2 \quad \forall W \in H_U
$$

### 4.3 The Core Local Theorem
On $B_r(U^{(0)})$:
$$
\text{Ric}_{\mu_\Lambda}(U)(W,W) \ge \rho_{loc}|W|^2 \quad \forall W \in H_U
$$
with $\rho_{loc} = \kappa_G - C_{add}$ independent of lattice size.

---

## 5. Physical Interpretation

| Math | Physics |
|------|---------|
| $\rho > 0$ | Vacuum stiffness |
| $\lambda_1 \ge \rho$ | Mass gap ≥ curvature |
| $CD(\rho, \infty)$ | Infinite-dimensional limit exists |
| Horizontal $CD$ | Gauge-invariant observables gapped |

---

## Summary

Bakry-Émery theory is the unified framework:
1. Define curvature via $\Gamma_2$.
2. Check $CD(\rho, N)$ condition.
3. Read off all functional inequalities automatically.

For gauge theories, the **horizontal restriction** makes this framework applicable.

---

## References
- D. Bakry, M. Ledoux, *Analysis and Geometry of Markov Diffusion Operators* (2014).
- M. Ledoux, *The Concentration of Measure Phenomenon* (2001).
- **Source:** `UNIFY_02_Horizontal_Bakry_Emery_Core_Theorem.md`
