# 30 — PBH Hessian Flow

## Abstract
We derive the **Perelman-Bakry-Hamilton (PBH)** flow for the Hessian of the effective action under RG. This tensor flow is the "master equation" governing how curvature evolves, with the Riccati ODE (File [06]) as its scalar trace.

**Connected Files:**
- **[06] Riccati Attractor:** The scalar reduction.
- **[21] Gradient Flow:** The flow of the field itself.
- **[36] Horizontal Maximum:** Controls the eigenvalue evolution.

---

## 1. The Evolution of the Action

### 1.1 Heat-Type RG
Under coarse-graining (heat flow), the density $\rho = e^{-S}$ evolves as:
$$
\partial_t \rho = \Delta \rho
$$

The action $S = -\log \rho$ therefore satisfies:
$$
\partial_t S = \Delta S - |\nabla S|^2
$$
This is the **viscous Hamilton-Jacobi equation**.

### 1.2 Connection to Ricci Flow
Hamilton's Ricci flow: $\partial_t g = -2 \text{Ric}$.
The PBH flow is the **measure-valued analogue**.

---

## 2. Flow of the Hessian

### 2.1 Differentiating Twice
Taking $H = \nabla^2 S$, the Hessian:
$$
\partial_t H_{ij} = \Delta H_{ij} - 2 H_{ik} H_{kj} + \text{commutators}
$$

### 2.2 The Quadratic Term
The $-2H^2$ term is **dissipative**: it drives eigenvalues towards zero.
Without a source, $\dot{\lambda} = -2\lambda^2 \Rightarrow \lambda \to 0$.

### 2.3 The Source/Error Split
*(From source: 07_Horizontal_Tensor_Maximum_Principle.md)*

Write: $\partial_t H - \Delta H + 2H^2 = \Sigma - E$

Where:
- $\Sigma \succeq \sigma_* I$ (Haar curvature, anomaly sources)
- $\|E\|_{op} \le \varepsilon$ (projection errors, gluing)

---

## 3. The Riccati Reduction

### 3.1 Scalar Trace
Taking $\lambda = \text{tr}(H)/\dim$:
$$
\dot{\lambda} = -2\lambda^2 + \sigma - \varepsilon
$$

### 3.2 Fixed Point
If $\sigma - \varepsilon > 0$:
$$
\lambda_* = \sqrt{(\sigma - \varepsilon)/2}
$$

This is the **stable attractor** ensuring the gap survives.

---

## 4. Yang-Mills Specialization

### 4.1 The Horizontal Restriction
On the gauge orbit space, project to $H_U$:
$$
\partial_t (P H P) = P(\Delta H - 2H^2 + \Sigma)P + \text{commutators}
$$

### 4.2 Commutator Bounds
$$
[\Delta, P] \sim (\nabla P)\nabla + (\nabla^2 P)
$$
These are bounded on SAFE regions.

---

## 5. Implications

### 5.1 Gap Persistence
If the source survives errors ($\sigma_0 > \varepsilon_0$):
$$
\lambda_{\min}(H_t) \gtrsim \sqrt{\sigma_{eff}/2}
$$
after transient.

### 5.2 Downstream Chain
$$
\text{PBH Flow} \to \text{Riccati bound} \to \text{BE curvature} \to \text{Local gap} \to \text{Global gap}
$$

---

## Summary

The PBH flow is the tensor-level dynamics governing curvature under RG. The key insight: **a positive source from Haar geometry can counteract the dissipative $-H^2$ term, creating a stable non-zero fixed point**.

---

## References
- G. Perelman, *The entropy formula for the Ricci flow* (2002).
- R. Hamilton, *The Ricci flow on surfaces* (1988).
- **Source:** `07_Horizontal_Tensor_Maximum_Principle.md`
