# Massive lattice Maxwell phase scan: renormalized mass extraction by dispersion fit

This note extracts the “momentum-space dispersion fit” method used to estimate a renormalized mass \(m_R\) in a massive 4D lattice Maxwell simulation, and the resulting coupling scan.

---

## Configuration (as implemented)

A large periodic lattice was used with parameters printed explicitly:
- lattice size \(L=32\) in \(d=4\),
- bare mass squared \(m^2_{\text{bare}}=0.3\),
- gauge parameter \(\alpha=1.0\) (Feynman gauge),
- Langevin step \(dt=0.02\),
- total Langevin steps \(n_{\text{langevin}}=2000\) with burn-in \(=500\),
- measurement stride \(=20\),
- coupling scan \(\lambda\in\{0.0,0.1,0.5,1.0,1.5,2.0,3.0,5.0\}\) with multiple chains per \(\lambda\).

---

## Mass extraction by low-momentum fit

The analysis fits the inverse propagator vs. lattice momentum squared at low momentum:
\begin{equation}
G^{-1}(\hat p)\approx A\,\hat p^2 + B,
\end{equation}
where the positive intercept \(B\) is treated as a mass-gap indicator (“screened” behavior). The code performs a linear fit on the low-\(\hat p^2\) bins and reads \(B=p_{\mathrm{poly}}(0)\).

A “renormalized mass” estimate is then constructed from the fitted coefficients (as implemented):
```python
z = np.polyfit(bin_means_p2[:20], bin_means_invG[:20], 1)  # low momentum fit
p_poly = np.poly1d(z)
intercept = p_poly(0)

m_R_extracted = math.sqrt(intercept / z[0]) * math.sqrt(m2_bare)
```

---

## Coupling scan results: \(m_R\) vs. \(\lambda\)

The printed renormalization table is:
\begin{align}
\lambda=0.0&:\; m_R=0.1532\\
\lambda=0.1&:\; m_R=0.1781\\
\lambda=0.5&:\; m_R=0.2551\\
\lambda=1.0&:\; m_R=0.3246\\
\lambda=1.5&:\; m_R=0.3835\\
\lambda=2.0&:\; m_R=0.4320\\
\lambda=3.0&:\; m_R=0.5135\\
\lambda=5.0&:\; m_R=0.6337
\end{align}

---

## Why this is usable going forward

- The method ties \(m_R\) directly to a *measurable spectral feature* (positive intercept of \(G^{-1}\) vs \(\hat p^2\)).
- The scan produces a monotone increasing \(m_R(\lambda)\) over a wide range of couplings in this dataset.

Concrete next steps for tightening this into publishable “evidence”:
1. Add uncertainty quantification: jackknife over chains / fit windows.
2. Check volume dependence: repeat for multiple \(L\), and compare \(m_R\) extracted from momentum-space fits vs coordinate-space exponential decay.
3. Verify fit stability: vary the number of low-momentum bins used in the regression and record sensitivity.
