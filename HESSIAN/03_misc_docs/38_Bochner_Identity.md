# 38 — The Bochner-Weitzenböck Identity

## Abstract
We derive the **Bochner-Weitzenböck identity**, the geometric engine powering all curvature-dimension bounds in the mass gap proof. This identity relates the "rough Laplacian" $\nabla^* \nabla$ to the Hodge Laplacian $\Delta$ via the Ricci curvature and is the foundation for the Bakry-Émery theory.

**Connected Files:**
- **[29] Bakry-Émery:** The framework built on this identity.
- **[03] Matrix Hinge:** The application to gauge theory.
- **[04] HS Covariance:** Uses the $\Gamma_2$ operator.

---

## 1. The Classical Bochner Formula (Riemannian)

### 1.1 For Functions (0-forms)
On a Riemannian manifold $(M, g)$ with Laplacian $\Delta$ and gradient $\nabla$:
$$
\frac{1}{2} \Delta |\nabla f|^2 = |\nabla^2 f|^2 + \langle \nabla f, \nabla \Delta f \rangle + \text{Ric}(\nabla f, \nabla f)
$$

### 1.2 For 1-Forms (Weitzenböck)
For a 1-form $\omega$:
$$
\Delta^{(1)} \omega = \nabla^* \nabla \omega + \text{Ric}(\omega, \cdot)
$$
where $\Delta^{(1)} = dd^* + d^* d$ is the Hodge Laplacian.

---

## 2. The Carré du Champ Operators

### 2.1 First-Order: $\Gamma$
$$
\Gamma(f, g) = \frac{1}{2}(L(fg) - f Lg - g Lf) = \langle \nabla f, \nabla g \rangle
$$

### 2.2 Second-Order: $\Gamma_2$
$$
\Gamma_2(f) = \frac{1}{2}(L\Gamma(f, f) - 2\Gamma(f, Lf)) = \|\nabla^2 f\|^2 + \text{Ric}_\mu(\nabla f, \nabla f)
$$

where $\text{Ric}_\mu = \text{Ric} + \nabla^2 V$ for measure $\mu = e^{-V}$.

---

## 3. The Bakry-Émery Extension

### 3.1 For Weighted Manifolds
If $\mu = e^{-V} dV_g$, then:
$$
\Gamma_2(f) = \|\nabla^2 f\|^2 + \text{Ric}_\mu(\nabla f, \nabla f)
$$

### 3.2 The $CD(\rho, N)$ Condition
If $\Gamma_2(f) \ge \rho \Gamma(f) + \frac{1}{N}(Lf)^2$, we say $\mu$ satisfies $CD(\rho, N)$.

---

## 4. Application to Gauge Theory: Horizontal Restriction

### 4.1 The Problem
On $M_\Lambda = G^{|E|}$, the Wilson action is flat along gauge orbits.
A full-space Hessian lower bound is **impossible**.

### 4.2 The Solution: Horizontal Bakry-Émery
Gauge-invariant observables have gradients in the **horizontal space** $H_U = (T\mathcal{O}_U)^\perp$.
It suffices to verify:
$$
\text{Ric}_\mu(U)(W, W) \ge \rho |W|^2 \quad \forall W \in H_U
$$

### 4.3 The Core Local Theorem
*(From source: UNIFY_02_Horizontal_Bakry_Emery_Core_Theorem.md)*

> **Local Horizontal Curvature Theorem:**
> If $\kappa_G > C_{add}$, then there exist $r > 0$ and $\rho_{loc} > 0$, independent of $\Lambda$, such that on $B_r(U^{(0)})$:
> $$\text{Ric}_{\mu_\Lambda}(U)(W,W) \ge \rho_{loc} |W|^2 \quad \forall W \in H_U$$

This is the **central geometric move** of the proof.

---

## 5. Consequences

### 5.1 Spectral Gap (Lichnerowicz)
If $\text{Ric}_\mu \ge \rho$:
$$
\lambda_1(-L) \ge \rho
$$

### 5.2 Log-Sobolev (Bakry-Émery)
$$
\text{Ent}(f^2) \le \frac{2}{\rho} \int |\nabla f|^2 d\mu
$$

### 5.3 Diameter (Bonnet-Myers)
If $CD(\rho, N)$ with $\rho > 0$ and $N < \infty$:
$$
\text{diam}(M) \le \pi \sqrt{\frac{N-1}{\rho}}
$$

---

## Summary

The Bochner-Weitzenböck identity is the "derivation engine" converting curvature into spectral bounds. The horizontal restriction is the key innovation that makes this machinery work for gauge theories.

---

## References
- S. Bochner, *Vector fields and Ricci curvature* (1946).
- D. Bakry, *L'hypercontractivité et son utilisation* (1994).
- **Source:** `UNIFY_02_Horizontal_Bakry_Emery_Core_Theorem.md`
