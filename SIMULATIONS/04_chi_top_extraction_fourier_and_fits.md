# Extracting \(\chi_{\text{top}}\) from a \(\theta\)-scan: quadratic vs Fourier vs finite differences

This document is about *turning a set of computed free energies \(F(\theta)\)* into a robust estimate of the topological susceptibility
\[
\chi_{\text{top}}=\left.\frac{\partial^2 F}{\partial\theta^2}\right|_{\theta=0}.
\]

The project explores multiple extraction methods and finds that a periodic Fourier fit typically beats a naive polynomial fit in goodness-of-fit metrics.

**Source files:** `CLEAN S4.pdf`, `GETINNGO GOOD STUFF HERE.pdf`, `su2_4d_complete_standalone_FIXED.ipynb - Colab.pdf`, `QUADRATIC FIT.pdf`, `CHECK THIS RESULT.pdf`, `15z0k12ZyDBkk5Gw-EQz0YTohdbQU9ZwM.pdf`.

---

## 1. Definitions (what \(\chi_{\text{top}}\) actually is)

In field theory,
\[
F(\theta)=-\frac{1}{V}\log Z(\theta),
\qquad
\chi_{\text{top}}=\left.\frac{\partial^2 F}{\partial\theta^2}\right|_{\theta=0}
= \frac{\langle Q^2\rangle_{\theta=0}}{V}.
\]

In the project, \(F(\theta)\) is often computed as \(F=-\log|Z|\) from tensor-network contraction, sometimes without an explicit volume normalization. That’s fine as long as you’re consistent: the curvature still encodes the susceptibility *up to a known volume factor*.

---

## 2. Method A: quadratic fit near \(\theta=0\)

Given data points \(\{(\theta_i,F_i)\}\) with small \(|\theta_i|\), fit
\[
F(\theta)\approx a + b\,\theta + c\,\theta^2.
\]
Then
\[
\chi_{\text{top}} = \left.\frac{\partial^2 F}{\partial\theta^2}\right|_0 = 2c.
\]

**Diagnostics:**
- For a CP-symmetric construction, \(b\) should be \(\approx 0\).
- If your fit produces a large \(b\), the data likely violates the expected evenness in \(\theta\) (either physical CP breaking, or—more likely here—an artifact of how \(\theta\) was implemented).

Several notebooks print this explicitly (e.g. “Quadratic fit: \(F(\theta)=a+b\theta+c\theta^2\), \(\chi_{\text{top}}=2c\)”).

---

## 3. Method B: finite differences (central curvature)

If you have symmetric points around 0, the cleanest nonparametric estimator is:
\[
\chi_{\text{top}} \approx \frac{F(\Delta)-2F(0)+F(-\Delta)}{\Delta^2}.
\]

This is hard to apply if you only scan \([0,2\pi]\) without explicitly including negative angles, but you can use periodicity:
\[
F(-\Delta)=F(2\pi-\Delta),
\]
*if* your computed \(F\) respects \(2\pi\)-periodicity numerically.

---

## 4. Method C: Fourier series (the “physics-shaped” fit)

### 4.1 Why Fourier is natural

Because \(\theta\) is an angle, the exact theory satisfies:
- \(Z(\theta+2\pi)=Z(\theta)\),
- hence \(F(\theta)\) is \(2\pi\)-periodic (up to branch issues if you take logs naively).

So, fitting with a periodic basis is automatically “geometry compatible”.

In the project, a truncated Fourier ansatz is used (example):
\[
F(\theta)=a_0 + a_1\cos(2\theta)+b_1\sin(2\theta)+a_2\cos(4\theta)+b_2\sin(4\theta).
\]

Empirically, one notebook reports:
- Polynomial \(R^2\approx 0.071\),
- Fourier \(R^2\approx 0.951\),
with the note “Fourier fit respects the periodic nature of \(F(\theta)\)!” (see `CLEAN S4.pdf`).

### 4.2 How \(\chi_{\text{top}}\) comes out of the Fourier coefficients

General Fourier series:
\[
F(\theta)=a_0+\sum_{n\ge 1}\left(a_n\cos(n\theta)+b_n\sin(n\theta)\right).
\]

Then
\[
F''(\theta)= -\sum_{n\ge 1} n^2 \left(a_n\cos(n\theta)+b_n\sin(n\theta)\right),
\]
so at \(\theta=0\),
\[
\chi_{\text{top}} = F''(0)= -\sum_{n\ge 1} n^2 a_n.
\]

**Key point:** sine coefficients \(b_n\) do *not* contribute at \(\theta=0\) because \(\sin(0)=0\), but they are a diagnostic: if you expect \(F(\theta)\) to be even, you expect \(b_n\approx 0\).

#### For the project’s “even-harmonic” parameterization

If you fit only even harmonics \(n=2m\):
\[
F(\theta)=a_0+\sum_{m\ge 1} A_m \cos(2m\theta) \quad (\text{optionally plus sines}),
\]
then
\[
\chi_{\text{top}} = -\sum_{m\ge 1} (2m)^2 A_m = -4A_1 - 16A_2 - 36A_3 - \cdots.
\]

**Important consistency note:** some project notebooks compute \(\chi_{\text{top}} = 4\,a_1\) from the \(\cos(2\theta)\) coefficient. The mathematically correct relation for \(F\) as written is \(\chi_{\text{top}}=-4a_1\) **plus** contributions from higher harmonics like \(-16a_2\). If you only keep the \(m=1\) harmonic, then the consistent approximation is \(\chi_{\text{top}}\approx -4a_1\).

This sign matters physically.

---

## 5. A recommended robust workflow

1. **Compute \(F(\theta)\) on a dense grid near \(\theta=0\).**  
   Even 7–11 points in \([0,0.5]\) helps.
2. **Enforce known symmetries in the fit:**
   - If your construction should be even: fit *cosines only* (no sine terms).
3. **Compute \(\chi_{\text{top}}\) from the fit coefficients using the derivative formula.**
4. **Cross-check with a central finite-difference curvature** using the smallest available \(\Delta\).
5. **Only then** consider using full-\([0,2\pi]\) Fourier fits for global diagnostics.

---

## 6. Why using \(F(\pi)-F(0)\) is a weak estimator

Some project code uses
\[
\chi_{\text{top}} \approx \frac{2\big(F(\pi)-F(0)\big)}{\pi^2},
\]
which would be exact if \(F(\theta)-F(0)=\tfrac12\chi\theta^2\) held all the way out to \(\theta=\pi\). In real \(\theta\)-physics, it usually doesn’t; the function is periodic and often closer to a cosine.

So treat this as a *quick diagnostic*, not the final estimator.

---

## 7. Minimal “correct Fourier chi” code snippet

```python
import numpy as np

def chi_from_cos_series(theta, F, n_max=4):
    # Fit F(theta) = a0 + sum_{n=1..n_max} a_n cos(n theta)
    theta = np.asarray(theta)
    F = np.asarray(F)

    X = [np.ones_like(theta)]
    for n in range(1, n_max+1):
        X.append(np.cos(n*theta))
    X = np.column_stack(X)

    coeffs, *_ = np.linalg.lstsq(X, F, rcond=None)
    a0 = coeffs[0]
    a = coeffs[1:]  # a_n

    chi = -np.sum([(n+1)**2 * a[n] for n in range(n_max)])
    return chi, (a0, a)
```

This is the cleanest way to keep the derivative math consistent with the fit model.
