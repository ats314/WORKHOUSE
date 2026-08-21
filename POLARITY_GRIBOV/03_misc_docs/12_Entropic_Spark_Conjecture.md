# 12 — The Entropic Spark Conjecture

## Abstract
We formulate the **Entropic Spark Conjecture**: the geometric curvature $\sigma$ arising from the Haar measure acts as a persistent **source term** in the RG flow of the mass gap, preventing the gap from closing in the continuum limit. We provide physical motivation, mathematical formulation, and discuss verification strategies.

**Connected Files:**
- **[01] Haar Mass:** The origin of $\sigma$.
- **[06] Riccati Attractor:** The ODE that requires $\sigma > 0$.
- **[30] PBH Flow:** The tensor-level formulation.
- **[35] Open Problems:** Lists this as a key conjecture.

---

## 1. The Problem: Scaling of the Gap

### 1.1 Dimensional Analysis
Physical mass gap: $m_{phys}$ with dimension [length]$^{-1}$.
Lattice mass gap: $\hat{m} = a \cdot m_{phys}$ (dimensionless).

For Asymptotic Freedom:
$$
\hat{m}(a) \sim \Lambda_{QCD} \cdot a \to 0 \quad \text{as } a \to 0
$$

### 1.2 The Danger
The Riccati equation (File [06]) is:
$$
\dot{\lambda} = -2\lambda^2 + \sigma
$$
If $\sigma$ also scales to zero as $a \to 0$, the fixed point $\lambda_* = \sqrt{\sigma/2}$ vanishes.
**The gap would close.**

### 1.3 The Spark Hypothesis
**Conjecture:** The geometric source $\sigma$ does NOT vanish in the continuum limit.
$$
\sigma \ge \sigma_0 > 0 \quad \forall a
$$

---

## 2. Physical Motivation

### 2.1 Topological Origin
The curvature $c_H$ comes from the compactness of $SU(N)$.
Compactness is a **topological** property, not a metric one.
It survives any continuous deformation, including the $a \to 0$ limit.

### 2.2 Anomaly Interpretation
In QFT, the conformal anomaly generates a trace $\langle T^\mu_\mu \rangle \ne 0$ even in classically scale-invariant theories.
The "Spark" could be the **gravitational** or **topological anomaly** of the gauge measure.

For Yang-Mills:
$$
\langle T^\mu_\mu \rangle = \frac{\beta(g)}{2g^3} F^2
$$
The beta function $\beta(g) \ne 0$ implies scale is broken.

### 2.3 Index Theorems
The Atiyah-Singer index theorem relates:
$$
\text{Index}(D) = \int \text{(curvature forms)}
$$
The index is topological (integer).
The curvature integral is geometric.
The Haar curvature $c_H$ is related to the Euler characteristic of the group.

---

## 3. Mathematical Formulation

### 3.1 Definition
Let $\mu_a$ be the Wilson-Haar measure on lattice spacing $a$.
Let $\text{Ric}_a$ be the Bakry-Émery Ricci curvature.

Define:
$$
\sigma(a) = \inf_{U \in K_a} \lambda_{\min}(\text{Ric}_a(U))
$$
where $K_a$ is the "good set" from Lyapunov analysis.

### 3.2 The Conjecture (Precise)
There exists $\sigma_0 > 0$ such that:
$$
\lim_{a \to 0} \sigma(a) \ge \sigma_0
$$

Equivalently, in RG units (at scale $\mu \sim 1/a$):
$$
\sigma(\mu) \to \sigma_\infty > 0 \quad \text{as } \mu \to \infty
$$

### 3.3 Relation to the Mass Gap
If the Spark Conjecture holds:
$$
\lambda_* = \sqrt{\frac{\sigma_0}{2}} \implies m_{phys} = \frac{\lambda_*}{a} \cdot a = \lambda_* \cdot \frac{1}{a} \cdot a = \lambda_*
$$
Wait, that's wrong. Let me reconsider the scaling.

The Riccati equation is for the **dimensionless** gap $\hat{m}$.
$$
\frac{d\hat{m}}{d\log\mu} = -2\hat{m}^2 + \sigma
$$
At fixed point: $\hat{m}_* \sim \sqrt{\sigma}$.
Physical mass: $m_{phys} = \hat{m}_* / a \sim \sqrt{\sigma}/a$.

For this to be finite as $a \to 0$, we need $\sigma \sim a^2$.
But then $\sqrt{\sigma} \sim a$, so $m_{phys} \sim a/a = O(1)$.

**Refined Conjecture:** The source $\sigma$ scales as $a^2$ (canonical dimension of a mass$^2$):
$$
\sigma(a) = \sigma_0 a^2 \implies m_{phys} = \sqrt{\sigma_0/2} = \text{const}
$$

---

## 4. Evidence

### 4.1 Perturbative
In perturbation theory, the entropy of the path integral measure is:
$$
\log Z = -\int (\text{det}(\Delta_A))^{1/2} \sim \int \log(\Lambda_{UV})
$$
The UV cutoff $\Lambda \sim 1/a$ generates logarithmic divergences.
These contribute to the running of the coupling, which sources the mass.

### 4.2 Non-Perturbative (Monte Carlo)
Lattice simulations show:
- The string tension $\sigma_{QCD} \approx (440 \text{ MeV})^2$ is stable as $a \to 0$.
- The glueball mass $m_{0^{++}} \approx 1.7$ GeV is stable.

These are indirect evidence that $\sigma_0 \ne 0$.

### 4.3 Strong Coupling Expansion
At $\beta \ll 1$ (File [31]):
$$
\hat{m} \sim \log(1/\beta) \to \infty
$$
The gap is huge. Obviously $\sigma > 0$ in this regime.

The question is whether this connects smoothly to weak coupling.

---

## 5. Counter-Arguments and Resolutions

### 5.1 Objection: Flat Directions
The coset $SU(N)/U(1)^{N-1}$ is a flag manifold.
Some directions have zero curvature.

**Resolution:** The Lyapunov weighting suppresses these directions.
The $\inf$ in $\sigma$ is over the **typical** configurations, not the measures-zero extrema.

### 5.2 Objection: Conformal Window
For $SU(N)$ with many fermions, there is a "conformal window" where the theory flows to a fixed point with $m = 0$.

**Resolution:** Pure Yang-Mills (no fermions) is NOT in the conformal window.
The beta function is strictly negative for all $g$.

### 5.3 Objection: Instantons
Instanton gas might disorder the vacuum, closing the gap.

**Resolution:** Instantons are topological and contribute to $\chi_{top}$, not to the mass gap.
The mass gap is in the trivial topological sector.

---

## 6. Verification Strategy

### 6.1 Numerical
Compute $\sigma(a)$ directly by:
1. Generating configurations at spacing $a$.
2. Computing $\lambda_{\min}(\nabla^2 S)$ on the good set.
3. Extrapolating $a \to 0$.

**Prediction:** $\sigma(a) \sim c_0 a^2$ with $c_0 \sim c_H \times (\text{wave function renormalization})$.

### 6.2 Analytic
Prove that the Haar Jacobian survives the infinite-volume and continuum limits.
This requires controlling the "entropy" of high-curvature regions.

---

## Summary

The Entropic Spark Conjecture is the "soul" of the mass gap:

1. The Haar measure injects curvature $c_H$ into the path integral.
2. Under RG, this curvature acts as a source $\sigma$ in the Riccati equation.
3. If $\sigma > 0$ uniformly, the gap $\lambda_*$ is forced to stay positive.
4. The mass gap is "self-sustaining" rather than fine-tuned.

Proving this conjecture would complete the Mass Gap proof.

---

## References
- G. 't Hooft, *The Conceptual Basis of Quantum Field Theory* (Anomalies).
- M. Atiyah, I. Singer, *The Index of Elliptic Operators*.
- **File [01]** (Haar Mass) for the origin.
- **File [06]** (Riccati) for the dynamical system.
- **File [35]** (Open Problems) for risk assessment.
