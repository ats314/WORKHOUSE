---
id: EX-002
title: "Exact convexity threshold for the SU(2) single-link Wilson+Haar model: beta_c = 4.413914663"
kind: derivation + numerical_result
status: solid
program: yang_mills
extracted_by: claude-opus-5, 2026-09-01
verification: independently recomputed; agrees with the corpus value to 11 significant figures
source_files:
  - HAAR/01_haar_mass/04_SU2_CALCULATIONS/02_SU2_SingleLink_BetaC.md
  - HAAR/01_haar_mass/04_SU2_CALCULATIONS/03_SU2_Concentration_BadMass.md
  - HAAR/synthesis/model_creation/Synthesis_01_Haar_Geometry_Foundation.md
related: EX-001 (the Haar Jacobian potential this builds on)
---

# Exact convexity threshold for the SU(2) single link

A small, clean, completely correct result. It is the sharpest exactly-solvable statement
in the corpus and is worth keeping on its own terms: a **closed-form threshold separating
global convexity from convexity failure** for the one-link Wilson + Haar model.

## Setup

One `SU(2)` link in the exponential chart, parametrized by the polar angle `θ ∈ (0,π)` of
the group element (so `θ` is the geodesic distance from the identity, `U = exp(θ n̂·T)`).
The total potential combines the Haar Jacobian term (`EX-001`) with the single-plaquette
Wilson term. Because the model is radially symmetric, the Hessian of the potential has
exactly two distinct eigenvalues at each `θ`:

- a **radial** eigenvalue `λ_rad(θ)` (the direction along `θ`),
- a **tangential** eigenvalue `λ_tan(θ)` (the sphere directions),

each a sum of a Haar and a Wilson contribution:
`λ_• = λ_•^H + λ_•^W`.

**Key structural observation (from the corpus, and correct):** `λ_tan(θ) > 0` for every
`β ≥ 0`, because both contributions are positive on `(0,π)`. **All convexity failure is
therefore radial.** This reduces a multi-dimensional convexity question to a
one-dimensional one, which is what makes the closed form possible.

The radial eigenvalue is

$$ \lambda_{\rm rad}(\theta) \;=\; \Big(\csc^{2}\theta - \frac{1}{\theta^{2}}\Big)
   \;+\; \frac{\beta}{2}\cos\theta . $$

The first bracket is the Haar contribution — positive and increasing on `(0,π)`, diverging
as `θ → π` (the antipode / conjugate point of `SU(2) ≅ S³`). The second is the Wilson
contribution, which is **negative for `θ > π/2`** and grows in magnitude with `β`. The
competition between them is the entire story.

## The threshold

Convexity fails exactly when `min_{θ∈(0,π)} λ_rad(θ) < 0`. At the threshold the minimum
touches zero, i.e. there is a **double root**:

$$ \exists\,\theta_\star \in (\pi/2, \pi):\qquad
   \lambda_{\rm rad}(\theta_\star) = 0
   \quad\text{and}\quad
   \lambda_{\rm rad}'(\theta_\star) = 0 . $$

Solving `λ_rad(θ) = 0` for `β` at fixed `θ ∈ (π/2, π)` (where `cos θ < 0`, so this is
well-defined) gives

$$ \beta(\theta) \;=\; -\,2\,\frac{\csc^{2}\theta - \theta^{-2}}{\cos\theta}, $$

and the threshold is the minimum of this curve:

$$ \boxed{\;\beta_c \;=\; \min_{\theta\in(\pi/2,\;\pi)}
   \left(-2\,\frac{\csc^{2}\theta - \theta^{-2}}{\cos\theta}\right)\;} $$

## Numerical value (independently verified)

| Quantity | Corpus | This recomputation | Agreement |
|---|---|---|---|
| `β_c` | 4.413914663162 | **4.413914663154** | 8.4 × 10⁻¹² |
| `θ_*` | 2.118504915119 | 2.118504085599 | 8.3 × 10⁻⁷ |

Consistency checks at the recomputed point: `λ_rad(θ_*, β_c) = 0.000e+00` and
`β'(θ_*) = −1.3e−07 ≈ 0`, confirming the double-root condition.

The larger discrepancy in `θ_*` is expected and benign: `β(θ)` is quadratic near its
minimum, so `θ_*` is intrinsically less well-determined than `β_c` — a `10⁻¹¹` error in
`β_c` corresponds to roughly a `10⁻⁶` uncertainty in `θ_*`. The two values are consistent.

## Interpretation

$$ \beta < \beta_c \approx 4.4139:\quad
\text{global convexity — Bakry-Émery curvature positive everywhere in the chart.} $$
$$ \beta > \beta_c:\quad
\text{convexity fails on an intermediate annulus } [\theta_-(\beta), \theta_+(\beta)]
\subset (\pi/2,\pi). $$

The failure region is an **annulus**, not a ball: convexity survives near the identity
(where Haar dominates) and near the antipode (where `csc²θ` diverges), and fails in
between. The corpus tracks `θ_±(β)` as functions of `β`, which is the right object.

## Why it matters

1. It is **exact**, which nothing else in the corpus's convexity analysis is.
2. It cleanly exhibits the mechanism the whole programme rests on — Haar curvature versus
   Wilson concavity — in a setting where both sides can be written down and solved.
3. It gives a concrete number to sanity-check the higher-dimensional SU(3) lattice scans
   against, and the reduction "all convexity failure is radial" is a genuinely useful
   structural observation.
4. Read alongside the obstruction results, it localizes the problem precisely: the
   convexity window is `β < 4.41`, i.e. **strong coupling**, while the asymptotically free
   continuum trajectory runs to `β → ∞`. This single link already shows the window and the
   physical trajectory moving in opposite directions.

## Reproduction

```python
import numpy as np
from scipy.optimize import minimize_scalar

beta = lambda th: -2.0*(1.0/np.sin(th)**2 - 1.0/th**2)/np.cos(th)
r = minimize_scalar(beta, bounds=(np.pi/2 + 1e-9, np.pi - 1e-9),
                    method='bounded', options={'xatol': 1e-14})
print(r.x, r.fun)      # 2.118504085599  4.413914663154
```

**Caveat (one line):** this is a single link with a one-plaquette term; it is a toy that
isolates the mechanism, not a lattice result. The corpus is clear about this.
