# Coherence sweep for the 4D lattice scalar propagator: extracting $\kappa$ and diagnosing the zero-mode floor

## Overview

This note extracts a clean methodological nugget from the scalar simulations:

1. A “coherence sweep” that checks theoretical decay parameters against numerical extraction of the mass gap (via $\kappa$) across $(L,m^2)$.
2. A diagnostic: at larger $L$ the naïve extraction can fail badly for some $(L,m^2)$.
3. A proposed fix: **floor truncation** based on the expected finite-volume zero-mode floor $G(\infty)\sim 1/(m^2 L^d)$ — which in the current setting is too aggressive and produces NaNs, highlighting how to tune it.

---

## Theoretical expectation for the lattice decay parameter

For the free lattice scalar operator with nearest-neighbor coupling $\alpha$ and mass term $m^2$,
the correlation decay along an axis is controlled by a lattice “mass” parameter $\kappa$ satisfying
\[
\cosh(\kappa) = 1 + \frac{m^2}{2\alpha},
\qquad\Rightarrow\qquad
\kappa_{\mathrm{exp}} = \operatorname{arcosh}\!\left(1+\frac{m^2}{2\alpha}\right).
\]

In $d$ dimensions, the propagator has a power-law prefactor times an exponential:
\[
G(r)\sim r^{-(d-1)/2}\,e^{-\kappa r}.
\]
So a corrected “point-to-point” extraction removes the prefactor:
\[
\log|G(r)| + \frac{d-1}{2}\log r \sim -\kappa r + \text{const}.
\]

---

## Reported coherence sweep output (selected)

A run reported in the logs (device=cuda) produced the following axis-extracted values.

### Raw axis extraction vs expectation (4D)

| L | m^2 | κ_expected | κ_axis | |κ_axis−κ_expected| |
|---:|---:|---:|---:|---:|
| 64 | 0.1 | 0.314924 | 0.318929 | 0.004005 |
| 64 | 0.2 | 0.443568 | 0.446694 | 0.003126 |
| 64 | 0.3 | 0.541097 | 0.543593 | 0.002496 |
| 96 | 0.1 | 0.314924 | 0.319602 | 0.004678 |
| 96 | 0.2 | 0.443568 | 0.294039 | 0.149529 |
| 96 | 0.3 | 0.541097 | 0.228628 | 0.312469 |

Interpretation: for $L=64$ the extraction matches the theoretical expectation extremely well, but for $L=96$ at $m^2=0.2,0.3$ the extracted $\kappa$ is catastrophically wrong. This is consistent with a **finite-volume floor / plateau contamination** problem.

---

## Diagnosing the floor: the $p=0$ mode

On a periodic box, the propagator includes the $p=0$ contribution:
\[
G_{\text{floor}} \approx \frac{1}{m^2 L^d}.
\]
When the true exponential tail becomes smaller than this constant, the log-slope method breaks, because you are no longer fitting $e^{-\kappa r}$ — you are fitting a constant plus noise.

---

## Proposed fix: floor truncation (current behavior)

The code introduces a truncation rule: only use radii where $|G(r)|$ exceeds a multiple of the floor.
\[
|G(r)| \;>\; \texttt{floor\_mult}\cdot\frac{1}{m^2 L^d}.
\]

A run with `floor_mult=30` produced NaNs (no valid fit windows), at least for $L=64$:

| L | m^2 | κ_expected | κ_axis (floor-trunc) |
|---:|---:|---:|---:|
| 64 | 0.1 | 0.314924 | NaN |
| 64 | 0.2 | 0.443568 | NaN |
| 64 | 0.3 | 0.541097 | NaN |

Interpretation: `floor_mult=30` is too strict in the current implementation, even in regimes where the raw extraction worked.

---

## Code fragments (from the project)

### Floor estimate and truncation criterion

```python
# In d dimensions with volume L^d:
floor = 1.0 / (m2 * (L**d))
thresh = floor_mult * floor
# only include radii r where |G(r)| > thresh
```

### Skeleton: κ extraction with floor truncation

```python
def scalar_kappa_floor_trunc(Gp, L, m2, alpha=1.0, d=4, floor_mult=30.0,
                             rmin=2, rmax_frac=0.49,
                             win_min=6, min_points=8):
    # Extract kappa from real-space propagator with a floor cutoff:
    # include only radii where |G(r)| > floor_mult/(m2 L^d)

    floor = 1.0/(m2*(L**d))
    thresh = floor_mult*floor

    # 1) compute G(r) along axis (or a ray)
    # 2) keep only r with abs(G(r)) > thresh
    # 3) fit corrected log slope over windows
    # 4) return kappa_axis (or NaN if no valid windows)
    ...
```

---

## What further work could expand this into something “theorem-grade”

1. **Project out the zero mode explicitly** in momentum space:
   \[
   \tilde G(p=0)\leftarrow 0
   \]
   before inverse FFT. That removes the floor rather than censoring data.
2. **Adaptive floor multiplier:** choose the smallest multiplier that preserves a minimum number of fit windows (e.g., enforce at least 3 windows of length ≥ `win_min`).
3. Use **weighted regression** in the tail (errors grow with distance); fit to
   \[
   G(r)=A\,r^{-(d-1)/2} e^{-\kappa r} + G_{\text{floor}}
   \]
   directly.
4. Extend the sweep across more $L$ and $m^2$ and build an automated decision rule for “fit trustworthy / not trustworthy,” i.e. computer-assisted diagnostics.

---

## Notes on novelty

The physics of the zero-mode floor is standard. The novel bit is the *workflow*:
- a systematic coherence sweep across parameters,
- explicit reporting of failure modes,
- and a principled attempt to enforce a floor-aware selection rule (which can be improved into a robust pipeline).
