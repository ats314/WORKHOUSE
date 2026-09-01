---
id: EX-001
title: "The Haar Jacobian potential and its Hessian at the identity: Hess V_Haar(0) = (N/12)·I"
kind: derivation + theorem
status: solid
program: yang_mills
extracted_by: claude-opus-5, 2026-09-01
verification: closed form derived here, confirmed numerically for SU(2), SU(3), SU(4), SU(5) to machine precision
corpus_had: the SU(3) value 0.2500001983 numerically, and "1/6 per link" for SU(2), as separate unexplained constants
this_extraction_adds: the closed form N/12, the derivation, isotropy, and the reconciliation of the two constants
source_files:
  - SIMULATIONS/safe_scan_tracked_v2.py
  - SIMULATIONS/su3_haar_hessian_scan_results.csv
  - SIMULATIONS/su3_haar_hessian_scan.py
  - HAAR/01_haar_mass/05_SU3_CALCULATIONS/Selected_Analytic_Haar_Jacobian_Entropic_Mass_SU3.md
  - WILSON/03_decay_bounds/04_helffer_sjostrand_and_greens_decay.md
reproduction: 02_extracted/verification_scripts/haar_hessian_check.py
---

# The Haar Jacobian potential on SU(N)

This is the entropic/geometric mass source that the whole corpus is built on. The corpus
computed it numerically and used the resulting numbers in many places, but never wrote
down the closed form. It has one, it is clean, and it is derived below.

## Setup

Work in the exponential chart on `SU(N)`. Write `X ∈ 𝔰𝔲(N)` (anti-Hermitian, traceless) and
`U = exp(X)`. Pushing Haar measure to the chart produces a Jacobian, and the associated
potential is

$$ V_{\text{Haar}}(X) \;=\; -\log \det \big( d\exp_X \big), \qquad
   d\exp_X \;=\; \frac{1 - e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}. $$

Fix the basis used throughout the corpus,

$$ T_a = \tfrac{i}{2}\lambda_a , \qquad a = 1,\dots,N^2-1, $$

with `λ_a` the generalized Gell-Mann matrices normalized by `tr(λ_aλ_b) = 2δ_ab`. Then

$$ \langle X, Y\rangle := 2\,\operatorname{tr}(X^\dagger Y)
   \quad\Longrightarrow\quad \langle T_a, T_b\rangle = \delta_{ab}, $$

so `{T_a}` is orthonormal and coordinates `x_a` are defined by `X = Σ_a x_a T_a`.

## Derivation

Let `f(z) = (1 - e^{-z})/z`, an entire function with `f(0) = 1`. Then
`V_Haar(X) = -\log\det f(\operatorname{ad}_X) = -\operatorname{tr}\log f(\operatorname{ad}_X)`.

**Step 1 — expand `log f`.**
$$ f(z) = 1 - \tfrac{z}{2} + \tfrac{z^2}{6} - \cdots
\;\Longrightarrow\;
\log f(z) = \Big(-\tfrac{z}{2} + \tfrac{z^2}{6}\Big) - \tfrac12\Big(\tfrac{z}{2}\Big)^{2} + O(z^3)
= -\tfrac{z}{2} + \tfrac{z^{2}}{24} + O(z^{3}). $$

**Step 2 — take the trace.**
$$ V_{\text{Haar}}(X) = \tfrac12 \operatorname{tr}(\operatorname{ad}_X)
   - \tfrac{1}{24}\operatorname{tr}(\operatorname{ad}_X^{2}) + O(X^{3}). $$
`𝔰𝔲(N)` is semisimple, so `tr(ad_X) = 0`: the linear term vanishes and the identity is a
critical point.

**Step 3 — use the Killing form.** For `𝔰𝔲(N)`,
$$ \operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y) = B(X,Y) = 2N\operatorname{tr}(XY). $$
For anti-Hermitian `X`, `tr(X²) = -tr(X^†X) = -\|X\|_{HS}^2`, hence
`tr(ad_X²) = -2N\|X\|_{HS}^2` and

$$ \boxed{\;V_{\text{Haar}}(X) = \frac{N}{12}\,\|X\|_{HS}^{2} + O(X^{3})\;} $$

**Step 4 — convert to the orthonormal coordinates.** Since
`⟨X,X⟩ = 2\|X\|_{HS}^2 = Σ_a x_a^2`, we get `\|X\|_{HS}^2 = \tfrac12 Σ_a x_a^2`, so
`V_Haar = (N/24) Σ_a x_a^2` and

$$ \big(\operatorname{Hess} V_{\text{Haar}}(0)\big)_{ab}
   \;=\; \frac{\partial^{2}V}{\partial x_a \partial x_b}\Big|_{0}
   \;=\; \frac{N}{12}\,\delta_{ab}. $$

## Result

> **Proposition.** In the exponential chart on `SU(N)` with the orthonormal basis
> `T_a = (i/2)λ_a`, the Haar Jacobian potential `V_Haar = -\log\det(d\exp)` has a critical
> point at the identity, and its Hessian there is **isotropic**:
> $$ \operatorname{Hess} V_{\text{Haar}}(0) \;=\; \frac{N}{12}\; I_{N^2-1}. $$

Isotropy is not an assumption — it comes out of the computation, and is confirmed
numerically below (min and max eigenvalues agree to machine precision). This matters: it
means the Haar source contributes the *same* curvature in every direction, with no
preferred subspace, so it cannot by itself distinguish gauge from physical modes.

## Numerical confirmation

Independent implementation (`verification_scripts/haar_hessian_check.py`): builds the
`𝔰𝔲(N)` basis, forms `ad_X` in that basis, evaluates `f(ad_X)` by its entire power series
`Σ_k (-A)^k/(k+1)!` (avoiding the removable singularity at `z=0` and the degenerate
eigendecomposition at the origin), takes `-\log\det`, and differentiates twice with torch
autograd in float64.

| Group | dim | Hessian min eig | Hessian max eig | N/12 |
|---|---:|---:|---:|---:|
| SU(2) | 3 | 0.166666667 | 0.166666667 | 0.166666667 |
| SU(3) | 8 | 0.250000000 | 0.250000000 | 0.250000000 |
| SU(4) | 15 | 0.333333333 | 0.333333333 | 0.333333333 |
| SU(5) | 24 | 0.416666667 | 0.416666667 | 0.416666667 |

Exact agreement, and min = max in every case (isotropy).

## Reconciling the corpus's constants

The corpus carries several numbers for "the Haar coefficient" and they were never
reconciled. They are now:

| Corpus value | Where | What it actually is |
|---|---|---|
| `0.2500001983` | `su3_haar_hessian_scan_results.csv` at `r=0` | `N/12` for `N=3` — **correct** |
| "1/6 per link, exponential chart" | `WILSON/03_decay_bounds/` | `N/12` for `N=2` — **correct, same formula** |
| `0.25` returned by `safe_scan_tracked_v2.py` | script output | same as above — **correct** |
| `c₀ = 0.125` | `su3_haar_hessian_scan.py` convexity scan | an **independent quadratic regulator** `c₀Σ‖A‖_F²` added to the Wilson action, *not* the Haar Jacobian term. Half of `N/12`; the coincidence is numerical, not structural. |
| `0.290892665` | `safe_scan_results_scaled.csv` | a *rescaled* variant under a different inner-product normalization; the ratio `0.2909/0.25 = 1.1636` records the rescaling, not new physics |
| `c₀ = (N²-1)/(2N)` | `lean/YangMills/HaarMassCoeff.lean`, `MasterTheorem.lean` | the **quadratic Casimir of the fundamental**, `C₂(F)` — a different quantity entirely (`4/3` for SU(3)), not the Haar Hessian |

The last row is the important one: the Lean development's `haar_coeff` is `C₂(F)`, while
the numerics compute `N/12`. For `SU(3)` these are `1.333…` and `0.25` — a factor of
`16/3`. **Any argument that uses one where it means the other is off by that factor.**

## What this does and does not give

It gives a genuine, exact, isotropic positive curvature contribution `N/12` from the Haar
measure alone, at the identity, in the exponential chart — a real geometric fact about
`SU(N)` and a legitimate ingredient in a Bakry-Émery estimate at fixed lattice spacing.

**Caveat (one line, see `03_verification/VER-002`):** these are lattice-chart quantities;
converting to the physical field `A = θ/(ag)` reinstates an `a²g²` factor, which is why an
`O(1)` constant here does not survive as a continuum mass.
