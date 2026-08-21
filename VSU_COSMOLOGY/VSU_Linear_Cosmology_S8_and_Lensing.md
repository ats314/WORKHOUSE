---
title: "VSU Linear Cosmology and Weak Lensing"
subtitle: "Late-time growth asymptotics and an explicit S₈ mapping (with code)"
status: "Referee-safe derivation + numeric evaluation"
---

# VSU Linear Cosmology and Weak Lensing
## Late-time growth asymptotics and the S\(_8\) mapping

### Abstract
This document extracts and re-derives (in a compact way) the project’s most useful *precision-cosmology* calculation:
- the **late-time asymptotics** for the modified growth factor,
- how that scale-dependent growth enters **weak lensing**, and
- an explicit linear-order mapping for the observable
\[
S_8 \equiv \sigma_8\sqrt{\Omega_{m0}/0.3},
\]
including a direct numerical evaluation of the key integral \(I(0)\) at \(\Omega_{m0}=0.23\).

The output is deliberately conservative: the effect is **directionally correct**, but its magnitude is perturbative unless the enhancement parameter is large.

---

# 1. Background expansion (kept \(\Lambda\)CDM-like)
The project’s baseline linear analysis keeps the background expansion
\[
H^2(a)=H_0^2\left[\Omega_{m0}a^{-3}+(1-\Omega_{m0})\right],
\]
so that most CMB distance priors are not immediately spoiled by background changes.

---

# 2. Modified linear growth and late-time asymptotics

## 2.1 Growth equation with a scale-dependent enhancement
Write the linear growth as \(D(k,a)\) with the usual GR solution \(D_{\rm GR}(a)\).
In VSU, the effective Poisson sector is modified by a factor \(1+\alpha(k,a)\), yielding a modified growth equation of schematic form:
\[
D'' + \left(2+\frac{H'}{H}\right)D' 
\;=\;
\frac{3}{2}\Omega_m(a)\big[1+\alpha(k,a)\big]D,
\]
where primes are derivatives with respect to \(\ln a\).

## 2.2 Late-time asymptotics
Assume \(\alpha(k,a)\to \alpha_\infty(k)\) at late times, and solve perturbatively about GR.
The files derive:
\[
D(k,a)=D_{\rm GR}(a)\,
\exp\!\left[-\frac{3}{55}\,\alpha_\infty(k)\,I(a)\right],
\]
where
\[
I(a)= -\int_a^\infty \Omega_m(a')^{6/11}\,\ln\Omega_m(a')\,d\ln a'.
\]

Using \(d\ln a = -dz/(1+z)\), this becomes (for \(a=1\), i.e. \(z=0\)):
\[
I(0)= -\int_0^\infty \Omega_m(z)^{6/11}\,\ln\Omega_m(z)\,\frac{dz}{1+z},
\]
with
\[
\Omega_m(z)=\frac{\Omega_{m0}(1+z)^3}{\Omega_{m0}(1+z)^3 + (1-\Omega_{m0})}.
\]

Because \(\ln\Omega_m(z)\le 0\), the overall \(I(0)\) is **positive**.

---

# 3. Weak lensing and a lensing-weighted enhancement

Weak lensing probes a line-of-sight projection of the potential power spectrum \(P_\Phi\), weighted by a kernel.
In the project’s approximation, the modified Poisson relation contributes a multiplicative factor \([1+\alpha(k,a)]\), leading to a lensing-weighted effective parameter \(\alpha_{\rm lens}\) defined by smoothing over the relevant window functions.

At first order in the modification, the project derives the compact mapping:
\[
S_8^{\rm VSU}
=
S_8^{\rm GR}
\left[
1-\frac{3}{55}\,\alpha_{\rm lens}\,I(0)
\right].
\]

Since \(I(0)>0\) and \(\alpha_{\rm lens}>0\) (enhanced effective coupling), the correction is **negative**:
\[
S_8^{\rm VSU} < S_8^{\rm GR}.
\]

---

# 4. Explicit numerical evaluation of \(I(0)\) (code + result)

## 4.1 Python code (Colab-ready)
```python
import numpy as np
from scipy.integrate import quad

def omega_m_z(z, om0):
    E2 = om0*(1+z)**3 + (1-om0)
    return om0*(1+z)**3 / E2

def I0(om0, zmax=1000.0):
    # I(0) = - ∫_0^∞ Ω_m(z)^(6/11) ln Ω_m(z) /(1+z) dz
    def integrand(z):
        om = omega_m_z(z, om0)
        return (om**(6/11) * np.log(om)) / (1+z)
    val, err = quad(integrand, 0.0, zmax, limit=200)
    return -val  # makes it positive

def s8_ratio(alpha_lens, I0_val):
    return 1.0 - (3/55)*alpha_lens*I0_val

OM0 = 0.23
I0_val = I0(OM0)
print("I(0) =", I0_val)

for alpha in [0.01, 0.05, 0.10, 0.15, 0.23]:
    r = s8_ratio(alpha, I0_val)
    print(alpha, r, (r-1)*100)
```

## 4.2 Output for \(\Omega_{m0}=0.23\)
Evaluating the integral gives:
\[
I(0)\approx 0.46041\quad (\Omega_{m0}=0.23).
\]

Then, for example:
- \(\alpha_{\rm lens}=0.10\) gives \(S_8^{\rm VSU}/S_8^{\rm GR}\approx 0.99749\) (a \(-0.25\%\) shift),
- \(\alpha_{\rm lens}=0.23\) gives \(S_8^{\rm VSU}/S_8^{\rm GR}\approx 0.99422\) (a \(-0.58\%\) shift).

---

# 5. Interpretation (conservative)
This calculation is valuable because it:
- fixes the **sign** of the effect analytically,
- makes the dependence on \(\alpha_{\rm lens}\) explicit,
- and shows that for perturbative \(\alpha_{\rm lens}\), the shift is *small*.

So: it is a *directionally correct* alleviation mechanism, but it cannot by itself produce a 5–10% shift unless \(\alpha_{\rm lens}\) is pushed into a non-perturbative regime or combined with additional background/geometry changes.

---

# Dependencies in the project
Extracted primarily from:
- `03.5_Late_Time_Asymptotics.md`
- `04.2_Weak_Lensing_and_S8.md`
