# 23 — VSU: Linear Cosmology and Observables

## Abstract
We verify the **Vacuum Stiffness Universe (VSU)** framework against linear cosmological observables. By deriving the modified growth equation and effective gravitational coupling, we show that the $S_8$ tension can be relieved while maintaining precise consistency with BAO and AP geometric probes.

**Connected Files:**
- **[15] VSU Core Theory:** The relativistic field theory.
- **[01] Haar Mass:** The origin of the vacuum stiffness.
- **[39] Summary:** The big picture.

---

## 1. Background Geometry

*(From source: VSU_COSMOLOGY/VSU_04_Linear_Cosmology_and_Observables.md)*

### 1.1 Metric
Standard flat FLRW: $ds^2 = -dt^2 + a^2(t) d\mathbf{x}^2$.
Matter + Lambda background:
$$
H^2(a) = H_0^2 [\Omega_{m0} a^{-3} + \Omega_{\Lambda 0}]
$$
**Crucial:** The background expansion is **identical** to $\Lambda$CDM.
Therefore, all geometric rulers (sound horizon $r_s$, angular diameter distance $D_A$) are unchanged.

### 1.2 Implications
- **BAO:** Peak positions are **invariant**.
- **Alcock-Paczynski (AP):** $F_{AP}(z)$ is **invariant**.
This "geometry lock" is a key feature, satisfying the precision data from DESI/Euclid.

---

## 2. Linear Perturbations

### 2.1 Newtonian Gauge
$$
ds^2 = -(1+2\Phi)dt^2 + a^2(1-2\Psi)d\mathbf{x}^2
$$
In this scalar theory, anisotropic stress is negligible:
$$
\Phi = \Psi
$$

### 2.2 Modified Poisson Equation
The vacuum stiffness modifies the effective Newton constant:
$$
\frac{k^2}{a^2} \Phi = 4\pi G_{\text{eff}}(k,a) \bar{\rho}_m \delta
$$
$$
G_{\text{eff}}(k,a) = G [1 + \alpha_{\text{eff}}(k,a)]
$$
where $\alpha_{\text{eff}}$ represents the screening/antiscreening of the stiffness field.

---

## 3. The Growth Equation

### 3.1 ODE for Growth Factor $D(a,k)$
$$
D'' + \left(\frac{3}{a} + \frac{1}{H}\frac{dH}{da}\right) D' - \frac{3}{2} \frac{\Omega_m(a)}{a^2} [1 + \alpha_{\text{eff}}] D = 0
$$

### 3.2 Growth Index $\gamma$
Parameterizing $f = d\ln D / d\ln a \approx \Omega_m^\gamma$:
$$
\gamma(k) \approx \frac{6}{11} - \frac{3}{55} \alpha_\infty(k)
$$
If $\alpha_\infty > 0$ (stiffness enhances gravity): Growth is **faster**, $\sigma_8$ increases.
If $\alpha_\infty < 0$ (stiffness resists clustering): Growth is **slower**, $\sigma_8$ decreases.

---

## 4. The $S_8$ Tension

### 4.1 The Observation
Weak lensing surveys (Kids, DES) consistently measure $S_8 \equiv \sigma_8 \sqrt{\Omega_m/0.3}$ lower than the Planck $\Lambda$CDM prediction.

### 4.2 The VSU Resolution
We require $\alpha_{\text{eff}} < 0$ on non-linear scales ($k \sim 1 \text{ Mpc}^{-1}$).
This implies a **repulsive** (or stiff) correction to the potential.

### 4.3 Analytic Ratio
$$
\mathcal{R}_D = \frac{D_{VSU}}{D_{GR}} \approx \exp\left( 0.021 \alpha_\infty \right)
$$
To lower $S_8$ by 5%, we need roughly $\alpha_\infty \approx -2.5$.

---

## 5. Other Observables

### 5.1 ISW (Integrated Sachs-Wolfe)
$$
\dot{\Phi}_{VSU} \approx \dot{\Phi}_{GR} \left( 1 + \frac{3}{55} \alpha_\infty (\dots) \right)
$$
The sign of the ISW effect remains standard (late-time decay of potentials), but the amplitude is modulated.

### 5.2 Weak Lensing Kernel
$$
P_\kappa(\ell) = \int d\chi \frac{W_L^2}{\chi^2} P_\Phi(k,z)
$$
Lensing probes the integrated potential $\Phi+\Psi = 2\Phi$.
It is directly sensitive to $G_{\text{eff}}$.

---

## 6. Consistency Check

| Observable | $\Lambda$CDM | VSU | Status |
|------------|--------------|-----|--------|
| $H(z)$ | Baseline | Same | ✅ Safe |
| BAO Peaks | Baseline | Same | ✅ Safe |
| Sub-horizon Growth | $\gamma \approx 0.55$ | $\gamma(k)$ | 🎯 Target |
| ISW | Dark Energy decay | Modified amplitude | ❓ Testable |
| GW Propagation | $c_T = c$ | $c_T = c$ | ✅ Safe |

---

## Summary

VSU offers a precise surgical instrument: it modifies **structure growth** via vacuum stiffness without breaking the **expansion history** that is tightly constrained by CMB and BAO. This makes it a viable candidate for resolving the $S_8$ tension.

---

## References
- **Source:** `VSU_04_Linear_Cosmology_and_Observables.md`
- Planck 2018 Cosmology Parameters.
- DES Year 3 Results.
