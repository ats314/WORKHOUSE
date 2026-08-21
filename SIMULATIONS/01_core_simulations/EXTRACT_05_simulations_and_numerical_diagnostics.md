# Simulations & Numerical Diagnostics (Verified Extracts)
*(Code + outputs that genuinely feed back into the proof strategy)*

This document only records simulation outputs that appear **verbatim** in the project files, and that
either (i) validate a key analytic inequality, (ii) diagnose an obstruction, or (iii) calibrate constants
that appear in the proofs.

---

## 1. Massive Maxwell inverse decay: predicted $\eta$ vs observed $\eta_{\mathrm{obs}}$

### 1.1 Bound verification and observed envelope slope (RUN 124)

`RUN 124.pdf` contains a decay-envelope diagnostic for the massive Maxwell Green kernel:

- measured link-graph degree: $D_E=18$,
- rigorous exponent (Davies/DG formula with $D_E$): $\eta_{\mathrm{DG}}(D_E)=0.129010$,
- observed envelope-fit exponent (fit range $n\in[2,15]$): $\eta_{\mathrm{obs}}\approx 0.338367$,
- shell-ratio check passes (max ratio at $n=0$ is $\approx 1.41\times 10^{-1}$).

**Extracted output (from the PDF text):**
```text
D_E (measured)=18
eta_DG(D_E)=0.129010
...
==== Observed decay (envelope fit) ====
fit range n=[2,15]
eta_obs ≈ 0.338367  (compare to eta_DG=0.129010)
```

**Why it matters.**  
The analytic pipeline only needs a conservative lower bound on $\eta_M$ to close Part 10,
but the *large slack* between $0.129$ and $0.338$ makes it plausible that your
$C_0/C_\partial$ refinements can meaningfully sharpen the final clustering exponent.

---

### 1.2 Bound verification with a large row-sum constant (MAXWELL SIMS)

`MAXWELL SIMS.txt` contains a brute-force verification script for the periodic-lattice Green kernel.
In that run:

- $D_E=18$,
- a computed row-sum constant is reported as $C_0\simeq 43.9077$,
- the exponents printed are:
  \[
  \eta_{\mathrm{DG}}(D_E)=0.129010,\quad
  \eta_{\mathrm{DG}}(C_0)=0.082635,\quad
  \eta_{\mathrm{CT}}(C_0)=0.003410,
  \]
- and the “max ratio” check passes (same max ratio across exponents, attained at $d=0$).

**Extracted output:**
```text
Geometry: D_E=18, C0=43.9077
Params: m^2=0.3, alpha=1.0
...
[DG (Deg)] eta=0.129010 | Max Ratio=0.1412 @ d=0
[DG (C0) ] eta=0.082635 | Max Ratio=0.1412 @ d=0
[CT (C0) ] eta=0.003410 | Max Ratio=0.1412 @ d=0
```

**Why it matters.**  
This confirms the core Part 9 claim (finite-range + gap $\Rightarrow$ exponential inverse decay)
in an explicit test case, *and* it illustrates a subtle point for vector/Maxwell operators:
taking absolute values for row sums can be very conservative because it destroys sign cancellations.

---

## 2. A remarkably clean Laplacian law (drift bookkeeping)

`12-21-25 SIM.txt` reports a high-precision affine “Laplacian law” for the averaged badness
($B_{\mathrm{avg}}$) under the generator:

\[
\Delta B_{\mathrm{avg}} \approx 12 - 12\,B_{\mathrm{avg}},
\]
with an extremely tight linear fit.

**Extracted output:**
```text
============================ PROOF A: affine Laplacian law for Vbar ============================
Fit: lap ≈ a + b*Bavg
 a=11.999129 b.=-11.998889
 R^2=0.999999311895
 max|residual|=1.835367e-02   RMS(resid)=4.179669e-03
Hypothesis check: lap ≈ 12 -12*Bavg
```

**Why it matters.**  
This is exactly the kind of empirical check you want before investing time in formalizing a
generator identity: it strongly suggests the model’s Laplacian bookkeeping is not the weak link.

---

## 3. Sign mechanism: gradient pairing is positive on all sampled configurations

`12-21-25 GEMINI CODE.txt` contains a “Sign Check” for the pairing alignment
$\langle g_S, g_V\rangle$:

- sample count: $6144$,
- positive alignments: $6144/6144$,
- significance estimate: $\log_{10} p\approx -1849.2$.

It also reports Laplacian residual diagnostics in the same run.

**Extracted output:**
```text
[SIGN CHECK]
 Total Samples: 6144
 Positive Alignments: 6144
 Pass Rate: 100.00%

 Significance: log10(p) ≈ -1849.2

[LAPLACIAN RESIDUALS]
 RMS Residual: 0.0010906
 Max Residual: 0.0055670
```

**Why it matters.**  
This is not a proof of coercivity, but it is strong evidence that the “cross-term sign dragon”
is not typically active near the vacuum regime you care about.

That supports the project’s pivot:
prove HS/hinge on a typical set $K^\star$, rather than demand global deterministic coercivity.

---

## 4. Drift certificate audit (a compact “health check”)

The same file reports a certificate-style audit at a given parameter $\tau$:

**Extracted output:**
```text
CERTIFICATE AUDIT @ tau=0.3883
c_min = 11.313536
d_max = -11.035192
rho_min = 1.966589
rho_min > 0 : OK
d_max < 0 : OK
```

**Why it matters.**  
The quantities here are consistent with a robust “restoring tendency” on the sampled ensemble,
and help justify treating a *mean-below-threshold* estimate as the remaining bottleneck (Assumption 8.19′).

---

## 5. A real obstruction diagnostic: blocking can generate large negative modes

`RUN 124.pdf` also contains a “$\Phi$-obstruction” diagnostic comparing a fine configuration
to a blocked one. The extracted summary indicates:

- fine configuration: $\lambda_{\min}\approx -36.7331$ with defect $\approx 37.2331$,
- blocked configuration: $\lambda_{\min}\approx -71.7594$ with defect $\approx 72.2594$,
- $\Phi$ increases from $\Phi_{\mathrm{fine}}\approx 39.5972$ to $\Phi_{\mathrm{block}}\approx 68.2991$.

**Extracted output (numbers appear explicitly; one line is truncated by PDF extraction):**
```text
[000] fine   lam_min≈-36.7331  defect≈37.2331 | ... | blocked lam_min≈-71.7594  defect≈72.2594
Phi_fine≈39.5972
Phi_block≈68.2991
Delta Phi = Phi_block - Phi_fine ≈ 28.7019
```

**Why it matters.**  
This is strong evidence that “coercivity survives coarse graining” is *not* something to assume.
It directly motivates:

- defining a blockwise typical set $K^\star$ carefully,
- proving hinge control *on $K^\star$*, not after arbitrary blocking.

---

## 6. Minimal reproducible code fragments

### 6.1 Exponent formulas used in Part 9

```python
import math

def eta_CT(m2: float, alpha: float, C: float, R: int = 1) -> float:
    # Combes–Thomas-style (log) exponent
    return (1.0 / R) * math.log(1.0 + m2 / (2.0 * alpha * C))

def eta_DG(m2: float, alpha: float, C: float) -> float:
    # Davies/DG exponent: arcosh(1+m2/(2αC)) = 2 asinh(m/(2 sqrt(αC)))
    m = math.sqrt(m2)
    return 2.0 * math.asinh(m / (2.0 * math.sqrt(alpha * C)))
```

### 6.2 Linear fit for the Laplacian law

```python
import numpy as np

def fit_affine_law(Bavg: np.ndarray, lap: np.ndarray):
    X = np.stack([np.ones_like(Bavg), Bavg], axis=1)
    coef, *_ = np.linalg.lstsq(X, lap, rcond=None)
    a_hat, b_hat = float(coef[0]), float(coef[1])
    lap_pred = a_hat + b_hat * Bavg
    resid = lap - lap_pred
    r2 = 1.0 - (resid@resid) / (np.sum((lap - lap.mean())**2) + 1e-12)
    return a_hat, b_hat, r2, float(np.max(np.abs(resid))), float(np.sqrt(np.mean(resid**2)))
```

---

## Source pointers

- Maxwell decay diagnostics (envelope fit): `RUN 124.pdf`.
- Maxwell bound verification (C0 vs degree): `MAXWELL SIMS.txt`.
- Laplacian law fit: `12-21-25 SIM.txt`.
- Sign check + certificate audit: `12-21-25 GEMINI CODE.txt`.
