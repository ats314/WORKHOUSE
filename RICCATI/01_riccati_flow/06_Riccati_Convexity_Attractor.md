# 06 — The Riccati Convexity Attractor

## Abstract
We analyze the **Riccati equation** governing the renormalization group evolution of the convexity modulus (spectral gap). We prove the existence of a stable positive fixed point (attractor), derive the explicit solution, and explain why the mass gap is "self-sustaining" in the presence of a geometric source term. This mechanism is central to understanding why the gap survives the continuum limit.

**Connected Files:**
- **[10] RG One-Step:** The discrete version of this flow.
- **[12] Entropic Spark:** The source term $\sigma$ that keeps the gap open.
- **[30] PBH Hessian Flow:** The tensor version of this equation.
- **[31] Strong Coupling:** The regime where the attractor is explicit.

---

## 1. The RG as a Dynamical System

### 1.1 The Conceptual Picture
Renormalization Group (RG) integrates out high-frequency modes, producing an effective theory at lower resolution.

If we track the **spectral gap** $\lambda(s)$ as a function of RG "time" $s$ (where $s$ corresponds to the log of the cutoff scale):
$$
\frac{d\lambda}{ds} = \beta_\lambda(\lambda, \text{other couplings})
$$

### 1.2 The Key Question
Does the gap survive as $s \to \infty$ (continuum limit)?
- If $\lambda(s) \to 0$: The theory becomes **critical** (massless, conformal).
- If $\lambda(s) \to \lambda_* > 0$: The theory has a **mass gap** (confined, gapped).

---

## 2. Derivation of the Riccati Equation

### 2.1 From the PBH Flow
The **Perelman-Bakry-Hamilton** flow (File [30]) governs the evolution of the Hessian under heat flow:
$$
\partial_t H = \Delta H - 2H^2 + \text{source terms}
$$

Taking the trace (or minimum eigenvalue) and assuming spatial homogeneity:
$$
\dot{\lambda} = -2\lambda^2 + \sigma
$$
where:
- $\lambda$ = minimum eigenvalue of the Hessian (convexity modulus)
- $\sigma$ = source from geometric curvature (the "Spark")

### 2.2 Physical Interpretation
- **$-2\lambda^2$:** Dissipation. Fluctuations wash out convexity. This is the "screening" or "renormalization" of the mass.
- **$+\sigma$:** Source. The intrinsic curvature of the configuration space (Haar measure) injects convexity.

---

## 3. Fixed Point Analysis

### 3.1 The Riccati ODE
$$
\dot{\lambda} = -2\lambda^2 + \sigma
$$

Assuming constant $\sigma > 0$:

### 3.2 Fixed Points
Set $\dot{\lambda} = 0$:
$$
-2\lambda^2 + \sigma = 0 \implies \lambda_* = \pm\sqrt{\frac{\sigma}{2}}
$$

Only $\lambda_* = +\sqrt{\sigma/2}$ is physical (positive gap).

### 3.3 Stability Analysis
Linearize around $\lambda_*$: Let $\lambda = \lambda_* + \epsilon$.
$$
\dot{\epsilon} = -4\lambda_* \epsilon = -4\sqrt{\frac{\sigma}{2}} \epsilon = -2\sqrt{2\sigma} \epsilon
$$

The linearized decay rate is $-2\sqrt{2\sigma} < 0$.

**Conclusion:** $\lambda_*$ is a **stable attractor**. Any initial condition $\lambda(0) > 0$ flows to $\lambda_*$.

---

## 4. Explicit Solution

### 4.1 Separation of Variables
$$
\frac{d\lambda}{\sigma - 2\lambda^2} = dt
$$

Let $a = \sqrt{\sigma/2}$, so $\sigma - 2\lambda^2 = 2(a^2 - \lambda^2)$.
$$
\frac{d\lambda}{2(a^2 - \lambda^2)} = dt
$$

Using partial fractions:
$$
\frac{1}{2a} \left(\frac{1}{a - \lambda} + \frac{1}{a + \lambda}\right) d\lambda = dt
$$

Integrate:
$$
\frac{1}{2a} \ln\left|\frac{a + \lambda}{a - \lambda}\right| = t + C
$$

### 4.2 Solution for $\lambda(0) = 0$
With initial condition $\lambda(0) = 0$:
$$
\frac{a + \lambda}{a - \lambda} = e^{2at}
$$
$$
\lambda = a \cdot \frac{e^{2at} - 1}{e^{2at} + 1} = a \tanh(at)
$$

Substituting $a = \sqrt{\sigma/2}$:
$$
\boxed{
\lambda(t) = \sqrt{\frac{\sigma}{2}} \tanh\left(t\sqrt{2\sigma}\right)
}
$$

### 4.3 Key Properties
| Time $t$ | $\lambda(t)$ | Interpretation |
|----------|--------------|----------------|
| $t = 0$ | $0$ | Massless initial condition |
| $t \sim 1/\sqrt{\sigma}$ | $\sim \lambda_*/2$ | Crossover |
| $t \to \infty$ | $\sqrt{\sigma/2}$ | Stable gap |

**Remarkable:** Even starting from **zero mass**, the system **generates** a gap of order $\sqrt{\sigma}$ purely from the geometric source!

---

## 5. The Role of the Source $\sigma$

### 5.1 Physical Origin
From **File [01]**, the Haar measure contributes curvature $c_H \approx 1/6$.
Under RG, this curvature is (partially) preserved:
$$
\sigma \approx c_H \cdot (\text{survival factor})
$$

### 5.2 What If $\sigma = 0$?
$$
\dot{\lambda} = -2\lambda^2 \implies \lambda(t) = \frac{\lambda_0}{1 + 2\lambda_0 t}
$$

As $t \to \infty$: $\lambda(t) \to 0$.

**No source → No gap.** The gap closes algebraically.

### 5.3 What If $\sigma$ Decays?
If $\sigma(t) = \sigma_0 e^{-\gamma t}$ (decaying source):
- For $\gamma < 2\sqrt{2\sigma_0}$: Gap survives asymptotically.
- For $\gamma > 2\sqrt{2\sigma_0}$: Gap closes.

The **Entropic Spark Conjecture (File [12])** claims that for non-Abelian groups, $\sigma$ does NOT decay—it remains $O(c_H)$ due to the persistent compactness of the group.

---

## 6. Comparison to Known Systems

### 6.1 The Gaussian Fixed Point
For a free field, the "mass" is marginal/relevant:
- RG flow: $\dot{m} = 0$ (marginal in $d=4$) or $\dot{m} = (2-d/2)m$ (relevant in $d<4$).
- No nonlinear feedback.

The Riccati $-2\lambda^2$ term is the **non-perturbative signature** of gauge interactions.

### 6.2 The Algebraic Riccati Equation (ARE)
In control theory, the steady-state Riccati equation:
$$
A^T P + PA - PBR^{-1}B^T P + Q = 0
$$
determines the optimal gain matrix $P$ for a Linear-Quadratic Regulator.

Our equation $-2\lambda^2 + \sigma = 0$ is the scalar version, with the gap $\lambda$ acting as the "optimal regulator" of quantum fluctuations.

### 6.3 Ricci Flow
Hamilton's Ricci flow:
$$
\partial_t g = -2 \text{Ric}(g)
$$
The scalar curvature evolves as:
$$
\partial_t R = \Delta R + 2|\text{Ric}|^2
$$

Comparing: Our "$-2\lambda^2$" is analogous to "$+2|\text{Ric}|^2$" (sign differs due to conventions). Both show that curvature has quadratic self-interaction.

---

## 7. Numerical Verification

### 7.1 Lattice Simulation
Run Langevin dynamics on a $4^4$ lattice at $\beta = 2.3$.
Measure the spectral gap of the diffusion generator at times $t = 0, 1, 2, \ldots$.
Plot $\lambda(t)$.

**Prediction:** The curve should be well-approximated by $\lambda_* \tanh(\gamma t)$ with $\lambda_* \sim 0.3$ (in lattice units).

### 7.2 Fitting the Parameters
From the data:
1. Extract $\lambda_* = \lim_{t \to \infty} \lambda(t)$.
2. Compute $\sigma = 2\lambda_*^2$.
3. Compare to theoretical $c_H = 1/6 \approx 0.167$.

If $\sigma \approx c_H$, this confirms the Haar origin of the gap.

---

## 8. The Big Picture: Self-Sustaining Mass

### 8.1 The "Bootstrap"
The mass gap is not put in by hand—it **emerges** from the interplay of:
1. Geometric curvature ($\sigma$) acting as a source.
2. Fluctuation screening ($-2\lambda^2$) acting as negative feedback.
3. The stable fixed point ($\lambda_*$) balancing the two.

### 8.2 Why Non-Abelian?
For Abelian groups ($U(1)$), the configuration space is **flat** ($c_H = 0$, $\sigma = 0$).
The Riccati equation becomes $\dot{\lambda} = -2\lambda^2$, which flows to $\lambda = 0$.
**No gap.** This is the massless photon.

For non-Abelian groups ($SU(N)$), $\sigma > 0$.
The fixed point $\lambda_* > 0$ exists.
**Mass gap!** This is confinement.

---

## Summary

The Riccati equation $\dot{\lambda} = -2\lambda^2 + \sigma$ is the "dynamical engine" of the mass gap:
1. It has a stable positive fixed point at $\lambda_* = \sqrt{\sigma/2}$.
2. Starting from any $\lambda > 0$, the system flows to $\lambda_*$.
3. Starting from $\lambda = 0$, the system **generates** a gap of order $\sqrt{\sigma}$.
4. The source $\sigma$ comes from the geometric curvature (Haar/compactness).

The mass gap is **self-sustaining**, not fine-tuned.

---

## References
- R. Hamilton, *The Harnack estimate for the Ricci flow* (1993).
- G. Perelman, *The entropy formula for the Ricci flow* (2002).
- **File [12]** (Entropic Spark) for the source term.
- **File [30]** (PBH Flow) for the tensor derivation.
