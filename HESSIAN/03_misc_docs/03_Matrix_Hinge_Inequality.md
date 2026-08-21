# 03 — The Matrix Hinge Inequality

## Abstract
The **Matrix Hinge Inequality** combines the Haar curvature (File [01]) and the Wilson Hessian (File [02]) into a unified operator lower bound. This is the central geometric result: on the "good set" $K_\Lambda(r)$, the Bakry-Émery curvature is bounded below by a **massive Maxwell operator**, implying the mass gap.

**Connected Files:**
- **[01] Haar Mass:** Provides $c_H I$.
- **[02] Wilson Hessian:** Provides $d_1^* d_1$.
- **[04] HS Covariance:** Uses this bound.
- **[05] Combes-Thomas:** Converts to exponential decay.

---

## 1. The Curvature Matrix

### 1.1 Definition
*(From source: CURATED_01_HaarMass_MatrixHinge.md)*

The Bakry-Émery curvature operator on gradients:
$$
\mathcal{H}_\Lambda(U) := \text{Ric}_{M_\Lambda} + \text{Hess } S_\Lambda(U)
$$

### 1.2 Component Analysis
- **Ricci term:** $\text{Ric}_{M_\Lambda} \succeq c_H I$ (uniform in $\Lambda$, from bi-invariant Haar metric).
- **Wilson Hessian at vacuum:** $\text{Hess } S_\Lambda(U^*) = \beta \mathsf{M}_\Lambda \succeq \beta c_M d_1^* d_1$.

---

## 2. The Small-Field Region

### 2.1 Definition
Let $z_p(U) = d_G(U_p(U), e)$ and define:
$$
K_\Lambda(r) = \{ U : z_p(U) \le r \text{ for all } p \in P(\Lambda) \}
$$

### 2.2 Taylor Remainder Control
On $K_\Lambda(r)$, there exists $R_W(r) \to 0$ as $r \to 0$ such that:
$$
\text{Hess } S_\Lambda(U) \succeq \text{Hess } S_\Lambda(U^*) - \beta R_W(r) I
$$

---

## 3. The Matrix Hinge Lemma

### 3.1 Statement
*(From source: CURATED_01_HaarMass_MatrixHinge.md)*

**Lemma (Matrix Hinge):** Fix $r > 0$ so small that $\beta R_W(r) \le \frac{1}{2} c_H$. Then for every finite periodic lattice $\Lambda$ and every $U \in K_\Lambda(r)$:
$$
\boxed{
\mathcal{H}_\Lambda(U) \succeq m_H^2 I + \alpha \, d_1^* d_1
}
$$
where:
$$
m_H^2 := \frac{1}{2} c_H, \qquad \alpha := \beta c_M
$$

### 3.2 Proof
For $U \in K_\Lambda(r)$:
$$
\mathcal{H}_\Lambda(U) = \text{Ric}_{M_\Lambda} + \text{Hess } S_\Lambda(U) \succeq c_H I + (\text{Hess } S_\Lambda(U^*) - \beta R_W(r) I)
$$

By choice of $r$: $c_H I - \beta R_W(r) I \succeq \frac{1}{2} c_H I$.
Also: $\text{Hess } S_\Lambda(U^*) \succeq \beta c_M d_1^* d_1$.

Combining:
$$
\mathcal{H}_\Lambda(U) \succeq \frac{1}{2} c_H I + \beta c_M d_1^* d_1 \quad \square
$$

---

## 4. Why This Is Exciting

### 4.1 Uniformity in Volume
No constant depends on $|\Lambda|$. This is the correct scaling for a mass-gap mechanism.

### 4.2 Geometric Origin of Mass
The scalar term $m_H^2 I$ comes from $\text{Ric}_{M_\Lambda}$, i.e., from the **Haar geometry of $G$**, not from adding a mass by hand.

### 4.3 Flexible Pattern
The same mechanism applies to any compact target manifold where:
- A vacuum Hessian identifies a discrete elliptic operator.
- The geometry supplies a uniform Ricci floor.

---

## 5. Physical Interpretation

| Mathematical | Physical |
|--------------|----------|
| $m_H^2 I$ | **Entropic mass** from group compactness |
| $\alpha d_1^* d_1$ | **Energetic stiffness** from Wilson action |
| $K_\Lambda(r)$ | **Vacuum neighborhood** (small fields) |
| Hinge positivity | **Mass gap** mechanism |

---

## 6. Downstream Consequences

### 6.1 Helffer-Sjöstrand (File [04])
$$
\text{Cov}(F, G) = \langle \nabla F, \mathcal{H}^{-1} \nabla G \rangle
$$
The inverse is well-defined because $\mathcal{H} \succeq m_H^2 > 0$.

### 6.2 Combes-Thomas (File [05])
$$
|(\mathcal{H}^{-1})_{xy}| \le C e^{-m_H |x-y|}
$$
Exponential decay of correlations.

---

## 7. Numerical Values for SU(2)

| Constant | Formula | Value |
|----------|---------|-------|
| $c_H$ | $\frac{1}{6}$ (from $\text{Ric}_{SU(2)}$) | $0.167$ |
| $m_H^2$ | $\frac{1}{2} c_H$ | $0.083$ |
| $c_M$ | Normalization-dependent | $O(1)$ |
| $r_*$ | Critical radius | $O(1/\beta)$ |

---

## Summary

The Matrix Hinge is the **heart of the geometric mechanism**:
1. Haar curvature provides a uniform floor.
2. Wilson stiffness adds the Maxwell operator.
3. Together, they bound the Bakry-Émery curvature away from zero.
4. This implies all downstream spectral gaps.

---

## References
- **Source:** `CURATED_01_HaarMass_MatrixHinge.md` (175 lines).
- D. Bakry, M. Ledoux, *Analysis and Geometry of Markov Diffusion Operators* (2014).
- **File [01]** for Haar mass derivation.
- **File [02]** for Wilson Hessian analysis.
