# 36 — Horizontal Tensor Maximum Principle

## Abstract
We derive the **Horizontal Tensor Maximum Principle** for symmetric endomorphisms evolving by a parabolic Riccati inequality. This is the "spine" connecting the PDE dynamics to the local Bakry-Émery curvature floor, and thus to the spectral gap.

**Connected Files:**
- **[11] Polarity:** Justifies working on the principal stratum.
- **[30] PBH Flow:** The PDE being controlled.
- **[06] Riccati:** The scalar reduction of this tensor principle.

---

## 1. The Parabolic Riccati Inequality

### 1.1 Setup
Let $H \subset TM$ be the horizontal subbundle with metric connection $\nabla^H$ and rough Laplacian $\Delta_H$.
Let $P_t \in \Gamma(\text{Sym}(H))$ be evolving by:
$$
(\partial_t - \Delta_H) P_t \succeq -\alpha P_t^2 + \Sigma_t, \quad \alpha > 0
\tag{MP}
$$

### 1.2 Source/Error Split
Assume:
$$
\Sigma_t(x) \succeq \sigma_*(t) I_H - E_t(x), \quad \|E_t(x)\|_{op} \le \varepsilon(t)
\tag{SE}
$$

---

## 2. The Main Result

### 2.1 Theorem (Hamilton Maximum Principle)
Define the minimal eigenvalue:
$$
\lambda(t) = \inf_{x \in M} \lambda_{\min}(P_t(x))
$$

Then $\lambda(t)$ is a viscosity supersolution of:
$$
\dot{\lambda}(t) \ge -\alpha \lambda(t)^2 + \sigma_*(t) - \varepsilon(t)
\tag{R}
$$

### 2.2 Corollary: Positive Source Survives Errors
If $\sigma_*(t) - \varepsilon(t) \ge \sigma_{eff} > 0$, then:
$$
\lambda(t) \gtrsim \sqrt{\sigma_{eff}/\alpha}
$$
after a transient.

**The key algebraic requirement:**
$$
\boxed{\sigma_0 > \varepsilon_0}
$$

---

## 3. Proof Sketch

### 3.1 Reduce to Scalar Test Function
At $t_0$, let $x_0$ realize the minimum eigenvalue with eigenvector $v_0 \in H_{x_0}$.
Extend $v_0$ by parallel transport to section $v$ with $(∇^H v)(x_0) = 0$.
Define $\phi(x,t) = \langle P_t(x) v(x), v(x) \rangle$.

### 3.2 Compute at the Minimum
Since $x_0$ is a spatial minimum of $\phi(\cdot, t_0)$:
- $(\Delta \phi)(x_0, t_0) \ge 0$
- By (MP): $(\partial_t - \Delta_H)\phi \ge -\alpha\lambda^2 + \sigma_* - \varepsilon$

### 3.3 Conclude
$$
\partial_t \lambda(t_0) \ge -\alpha \lambda(t_0)^2 + \sigma_*(t_0) - \varepsilon(t_0)
$$

---

## 4. Yang-Mills Translation

### 4.1 The Source $\sigma_0$
- **Intrinsic geometry:** $\text{Ric}^{\sharp}|_H$ on $SU(N)^{|E|}$ is strictly positive.
- **Haar Jacobian mass:** Contributes at finite cutoff.
- **Anomaly sources:** RG-evolved effective action.

### 4.2 The Error $\varepsilon_0$
- **Coarse-graining nonlocality**
- **Gauge projection artifacts:** $[Δ, Π]$ commutators
- **Interface gluing terms**

---

## 5. Downstream Impact

The constant:
$$
\alpha_{mix} = \inf_{t \ge 0} \ell(t)
$$
becomes the **local Bakry-Émery curvature floor** and hence determines:
- Poincaré constant
- LSI constant
- Local spectral gap

**The entire argument chain:**
$$
\text{Parabolic Hessian PDE} \Rightarrow \text{Riccati bound} \Rightarrow \text{Local BE curvature} \Rightarrow \text{Local gap} \Rightarrow \text{Global gap}
$$

---

## Summary

The Horizontal Tensor Maximum Principle is the rigorous machinery converting PDE dynamics into spectral bounds on stratified spaces. The "positive source survives errors" condition $\sigma_0 > \varepsilon_0$ is the quantitative test.

---

## References
- R. Hamilton, *The formation of singularities in the Ricci flow* (1995).
- **Source:** `07_Horizontal_Tensor_Maximum_Principle.md` (348 lines).
- **File [30]** PBH Flow for the evolution equation.
