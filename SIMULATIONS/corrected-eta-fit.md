# Correcting 4D Point-to-Point Exponential Fits: Removing the Power-Law Prefactor

## Abstract

A recurring numerical headache: in $d=4$ the massive Green’s function decays like
\[
G(r)\sim A\,r^{-3/2}e^{-\eta r},
\]
so a naive regression of $\log G(r)$ vs. $r$ tends to **overestimate** the exponential rate $\eta$ (because the $r^{-3/2}$ prefactor bends the curve).

This note records a simple fix used in the project:

> regress $\log|G(r)|+\tfrac{3}{2}\log r$ against $r$

which dramatically improves agreement with the theoretical $\eta_{\mathrm{th}}$ in the test cases shown.

---

## 1. The derivation

Assume in $d$ dimensions:
\[
G(r)\approx A\,r^{-\frac{d-1}{2}}e^{-\eta r}.
\]
Taking logs:
\[
\log|G(r)| \approx \log|A| - \eta r - \frac{d-1}{2}\log r.
\]
Therefore define the corrected log:
\[
y_{\mathrm{corr}}(r)\;\equiv\;\log|G(r)| + \frac{d-1}{2}\log r
\approx \log|A| - \eta r.
\]
Now a plain least-squares fit of $y_{\mathrm{corr}}(r)$ vs. $r$ returns an $\eta$ estimate that is far less biased by the power-law prefactor.

For $d=4$,
\[
y_{\mathrm{corr}}(r)=\log|G(r)|+\frac{3}{2}\log r.
\]

---

## 2. Corrected point-to-point fitting function

A minimal corrected estimator (as used in the project) is:

```python
import numpy as np

EPS = 1e-300

def fit_eta_point_corrected(G_pt: np.ndarray, rmin: int, rmax: int) -> float:
    # Fits log|G_pt(r)| + (3/2)log r  ≈ a - eta*r (4D prefactor removed)
    G_pt = np.asarray(G_pt).reshape(-1)
    Lc = G_pt.size

    rmin = max(1, int(rmin))           # r>=1 for log r
    rmax = min(int(rmax), Lc - 1)
    if rmax <= rmin:
        return float("nan")

    r_int = np.arange(rmin, rmax + 1, dtype=np.int64)
    r = r_int.astype(np.float64)

    y = np.log(np.maximum(np.abs(G_pt[r_int]), EPS))
    y_corr = y + 1.5 * np.log(r)

    # y_corr ≈ a - eta*r
    A = np.vstack([np.ones_like(r), -r]).T
    coef, *_ = np.linalg.lstsq(A, y_corr, rcond=None)
    return float(coef[1])
```

---

## 3. Results (free-field validation)

A test comparing multiple estimators reported:

- $\eta_{\mathrm{th}}$: theoretical rate
- `eta_proj_fit`: rate from a projected correlator fit (good)
- `eta_pt_raw`: naive point-to-point fit (overestimates)
- `eta_pt_corrected`: corrected point-to-point fit (moves toward theory)

| $m^2$ | $\eta_{\mathrm{th}}$ | $\eta_{\mathrm{proj\ fit}}$ | $\eta_{\mathrm{pt\ raw}}$ | $\eta_{\mathrm{pt\ corrected}}$ |
|---:|---:|---:|---:|---:|
| 0.010 | 0.099958 | 0.094613 | 0.239160 | 0.114863 |
| 0.020 | 0.141304 | 0.139329 | 0.279336 | 0.155039 |
| 0.050 | 0.223144 | 0.222899 | 0.358714 | 0.234418 |
| 0.100 | 0.314925 | 0.314901 | 0.448906 | 0.324609 |
| 0.300 | 0.541097 | 0.541097 | 0.673827 | 0.549530 |
| 0.500 | 0.693147 | 0.693147 | 0.826015 | 0.701718 |

The corrected estimator systematically reduces the bias relative to the naive point-to-point estimator, while remaining slightly above $\eta_{\mathrm{th}}$ in these runs (consistent with remaining lattice artifacts and fit-window choices).

---

## 4. Why this is worth keeping

This is not a new theorem, but it is a **high-leverage numerical trick**:

- It gives a cheap and robust cross-check on more elaborate estimators (projection fits, momentum-space pole fits).
- It generalizes immediately to any dimension $d$ by changing the prefactor correction to $\tfrac{d-1}{2}\log r$.
- In interacting theories, it can be used as a diagnostic to see whether you are truly in an asymptotic regime where a single mass dominates.

---

## 5. Next steps

1. **Automatic window selection** using plateau detection on the corrected slopes.
2. **Bootstrap error bars** over directions / rays.
3. **Interacting tests**: apply to $\phi^4$ quenches or gauge-fixed correlators and compare to known mass-gap benchmarks.
