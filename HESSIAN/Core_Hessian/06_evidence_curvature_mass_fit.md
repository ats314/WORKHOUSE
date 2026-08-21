# Evidence Note: Curvature–Mass Proportionality Fit (E04)

*Project extraction (generated 2025-12-29).*

## 0. What this checks

The project proposes an **effective geometric mass scale** $\mu_{\mathrm{eff}}(\beta)$ computed from curvature/convexity bookkeeping, and asks whether it tracks the measured lattice mass gap $m_{\mathrm{lat}}(\beta)$ across a short scaling window.

The simplest falsifiable check is a proportionality fit:
\[
m_{\mathrm{lat}}(\beta)\;\approx\;k\,\mu_{\mathrm{eff}}(\beta),
\]
with **no intercept** (since both should vanish together in any deconfined/ungapped limit).

---

## 1. Data used

\[
\begin{array}{c|cc}
\beta & \mu_{\mathrm{eff}} & m_{\mathrm{lat}}\\ \hline
5.7 & 0.92 & 0.88\\
5.8 & 0.81 & 0.78\\
5.9 & 0.74 & 0.71\\
6.0 & 0.68 & 0.66\\
6.1 & 0.63 & 0.61
\end{array}
\]

---

## 2. Constrained least squares fit (no intercept)

The minimizer for $\sum_i (m_i - k\mu_i)^2$ is
\[
k = \frac{\sum_i \mu_i m_i}{\sum_i \mu_i^2}.
\]

### 2.1 Reproducible code

See the standalone script: `curvature_mass_fit.py`.

Core snippet:

```python
k = float(np.dot(mu_eff, m_lat) / np.dot(mu_eff, mu_eff))
pred = k * mu_eff
res = m_lat - pred

R2 = 1.0 - np.dot(res, res) / np.dot(m_lat - np.mean(m_lat), m_lat - np.mean(m_lat))
rms = float(np.sqrt(np.mean(res**2)))
```

### 2.2 Results

Using the dataset above:

- Best-fit slope:
  \[
  \boxed{k \approx 0.962363.}
  \]
- Coefficient of determination:
  \[
  \boxed{R^2 \approx 0.998237.}
  \]
- RMS residual:
  \[
  \boxed{\mathrm{RMS} \approx 0.00397.}
  \]

Residuals (data minus fit):
\[
m_{\mathrm{lat}}-k\mu_{\mathrm{eff}}
\approx
(-0.00537,\;0.00049,\;-0.00214,\;0.00520,\;0.00356).
\]

A plot is saved as `curvature_mass_fit.png`.

---

## 3. How to interpret this (without fooling yourself)

This correlation is *suggestive*, but it’s not yet a smoking gun, because:

1. The window is tiny (5 points).
2. $\mu_{\mathrm{eff}}$ is partly model-dependent (how you map curvature constants into a physical mass unit matters).
3. The fit is not yet stress-tested against changes in lattice action, group, observable definition, or scaling window.

Still: if $\mu_{\mathrm{eff}}$ is computed from local curvature geometry and tracks $m_{\mathrm{lat}}$ this closely, it’s a strong hint that the curvature-based “mass-from-geometry” mechanism is not numerically crazy.

---

## 4. Next experiments that would raise the credibility

1. **Change group:** repeat for $SU(2)$ and $SU(4)$; see whether $k$ stays $O(1)$ and how it scales with $N$.
2. **Change observable:** extract masses from different channels and see if $\mu_{\mathrm{eff}}$ predicts a consistent scale hierarchy.
3. **Scaling test:** verify that the inferred $\mu_{\mathrm{eff}}(\beta)$ matches asymptotic freedom expectations (log running), at least qualitatively.
4. **Increase the window:** add more $\beta$ points, especially deeper into weak coupling.
5. **Uncertainty:** attach error bars and do a weighted fit (right now the comparison is deterministic).

