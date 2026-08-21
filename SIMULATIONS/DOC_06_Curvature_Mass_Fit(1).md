# DOC 06 — Numerical Evidence: Curvature Scale Tracks the Lattice Mass Gap

## 0. Purpose

This note reproduces the small numerical experiment recorded in:

- `EVIDENCE_01_Curvature_Mass_Fit.md`

The experiment checks a simple model:

\[
m_{\rm lat}(\beta) \approx k\,\mu(\beta),
\]

where \(\mu(\beta)\) is a proposed *curvature-derived* scale, and \(m_{\rm lat}(\beta)\) is the measured lattice mass gap.

## 1. Data (as recorded)

\[
\beta = [5.7, 5.8, 5.9, 6.0, 6.1]
\]
\[
\mu(\beta) \approx [0.92, 0.81, 0.74, 0.68, 0.63]
\]
\[
m_{\rm lat}(\beta) \approx [0.88, 0.78, 0.71, 0.66, 0.61]
\]

## 2. Constrained proportionality fit (zero intercept)

We fit \(m_{\rm lat} = k\mu\) with
\[
k = \frac{\mu\cdot m}{\mu\cdot \mu}.
\]

### Python reproduction

```python
import numpy as np

mu   = np.array([0.92, 0.81, 0.74, 0.68, 0.63])
mLat = np.array([0.88, 0.78, 0.71, 0.66, 0.61])

k    = float(np.dot(mu, mLat) / np.dot(mu, mu))
pred = k * mu
res  = mLat - pred

R2 = 1.0 - np.dot(res, res) / np.dot(mLat - np.mean(mLat), mLat - np.mean(mLat))
rms = np.sqrt(np.mean(res**2))

print("k =", k)
print("R^2 =", R2)
print("RMS residual =", rms)
print("residuals =", res)
```

### Output

- \(k \approx 0.962363\)
- \(R^2 \approx 0.998237\)
- RMS residual \(\approx 0.00397\) (lattice units)
- residuals \(\approx [-0.00537, 0.000486, -0.00215, 0.00559, 0.00371]\)

A plot is provided in `curvature_mass_fit.png`.

## 3. Optional: unconstrained linear regression (with intercept)

If one fits \(m_{\rm lat} = k\mu + b\), the best-fit intercept is small but nonzero:
- \(k \approx 0.9292\)
- \(b \approx 0.0255\)
- \(R^2 \approx 0.99953\)

This can be interpreted either as:
- subleading corrections not captured by the simple proportional model, or
- finite-lattice artifacts / normalization mismatch in \(\mu(\beta)\).

## 4. Interpretation (what this supports and what it does not)

### What it supports
- The curvature-derived scale \(\mu(\beta)\) tracks the measured gap extremely well across this window.
- The proportionality constant is near 1, suggesting the curvature scale is not merely “dimensionally compatible” but close in magnitude.

### What it does not settle
- **Continuum scaling:** the decisive test is whether \(\mu(\beta)\) follows asymptotic freedom scaling as \(a\to 0\).
- **Universality:** five points is not a proof; one needs more \(\beta\) values, different volumes, and ideally different definitions of \(\mu\).

## 5. Next numerical test that matters

A scaling test consistent with asymptotic freedom would compare \(\mu(\beta)\) to the expected form (schematically)
\[
\mu(\beta) \sim \Lambda \,(b_0 g^2)^{-b_1/(2b_0^2)}\,\exp\!\left(-\frac{1}{2b_0 g^2}\right),
\quad g^2 \sim \frac{2N}{\beta},
\]
and check whether the fitted \(\Lambda\) is stable across windows and observables.

