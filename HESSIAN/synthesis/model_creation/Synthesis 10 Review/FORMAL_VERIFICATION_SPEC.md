# Formal Verification Specification

## Overview

This document identifies lemmas from Synthesis 10 that warrant formal verification
in a proof assistant (Lean 4 recommended, Isabelle/HOL or Coq as alternatives).

## Installation

### Lean 4 (Recommended)

```powershell
# Install elan (Lean version manager)
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | bash

# Or on Windows via scoop:
scoop install elan

# Initialize a new mathlib project
lake new synthesis10_formal math
cd synthesis10_formal
lake exe cache get  # Download mathlib cache
```

### Isabelle

Download from: https://isabelle.in.tum.de/

---

## Priority Lemmas for Formal Verification

### Tier 1: Critical Path (Must Verify)

| Lemma | Location | Statement | Difficulty |
|:------|:---------|:----------|:-----------|
| **vHJ Derivation** | Ch 2.2 | If $P_t = e^{-S_t}$ satisfies heat eq, then $\partial_t S = \Delta S - |\nabla S|^2$ | Medium |
| **Riccati Fixed Point** | Ch 4.1 | ODE $\dot\lambda = \sigma - 2\lambda^2$ has stable fixed point $\sqrt{\sigma/2}$ | Easy |
| **Haar Eigenvalue Bound** | Ch 25 | $\lambda_{\text{rad}}(\theta) \geq 1/6$ for all $\theta \in (0, \pi)$ | Medium |
| **Tensor Maximum Principle** | Ch 8.1 | Matrix parabolic PDE implies scalar comparison | Hard |

### Tier 2: Important Supporting Results

| Lemma | Location | Statement | Difficulty |
|:------|:---------|:----------|:-----------|
| **Bakry-Émery implies gap** | Ch 12 | CD($\rho$, $\infty$) $\Rightarrow$ Poincaré constant $\leq 1/\rho$ | Medium |
| **Helffer-Sjöstrand identity** | Ch 14 | Covariance = $\langle \nabla F, \mathcal{L}^{-1} \nabla G \rangle$ | Hard |
| **Hessian evolution** | Ch 3.1 | Second derivative of vHJ gives Riccati structure | Hard |

### Tier 3: Nice to Have

| Lemma | Location | Statement |
|:------|:---------|:----------|
| c_0 formula | Ch 24 | $(N^2-1)/2N$ is Haar mass coefficient |
| Defect gas decay | Ch 25 | BadMass$(\beta) \sim e^{-c\beta}$ |

---

## Lean 4 Stub: Riccati Fixed Point

```lean
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.Calculus.Deriv.Basic

/-- The Riccati ODE has a stable fixed point -/
theorem riccati_fixed_point (σ : ℝ) (hσ : 0 < σ) :
  let λ_star := Real.sqrt (σ / 2)
  σ - 2 * λ_star ^ 2 = 0 := by
  simp [Real.sq_sqrt (by linarith : σ / 2 ≥ 0)]
  ring
```

## Lean 4 Stub: Haar Eigenvalue Bound

```lean
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-- The Haar radial eigenvalue is minimized at the origin -/
theorem haar_eigenvalue_lower_bound (θ : ℝ) (hθ : 0 < θ) (hθ' : θ < Real.pi) :
  (1 / 2) * (1 / Real.sin θ ^ 2 - 1 / θ ^ 2) ≥ 1 / 6 := by
  sorry  -- Requires careful analysis of the function's derivative
```

---

## Isabelle Stub

```isabelle
theory Synthesis10
  imports "HOL-Analysis.Analysis"
begin

lemma riccati_fixed_point:
  fixes σ :: real
  assumes "σ > 0"
  shows "σ - 2 * (sqrt (σ / 2))^2 = 0"
  using assms by (simp add: power2_eq_square)

end
```

---

## Verification Status

| Lemma | SymPy | NumPy | JAX | Lean | Status |
|:------|:------|:------|:----|:-----|:-------|
| vHJ Derivation | ✓ | ✓ | ✓ | - | Numerically verified |
| Riccati Fixed Point | ✓ | ✓ | - | stub | Numerically verified |
| Haar Bound ≥ 1/6 | ✓ | ✓ | ✓ | stub | Numerically verified |
| Hessian Evolution | ✓ | - | ✓ | - | Partially verified |

---

## Next Steps

1. Install Lean 4 + mathlib
2. Formalize Tier 1 lemmas
3. Connect formal proofs to synthesis claims
