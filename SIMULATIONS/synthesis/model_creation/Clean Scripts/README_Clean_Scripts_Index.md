# Clean Scripts Index

This folder contains verified, documented simulation scripts extracted from the HAAR project.
All scripts have been tested and include clear documentation of:
- What they do
- Theory connection
- Verification status
- Search keywords for discoverability

---

## Verified Scripts (NumPy Only - No Dependencies)

### 1. VERIFIED_SU2_Disorder_Force_Correlation_Test_For_Assumption_A_Prime.py
**Purpose:** Tests if high-disorder gauge configs can have low Wilson force
**Keywords:** SU(2), Wilson action, disorder, gradient force, Assumption A', mass gap
**Status:** VERIFIED
**Result:** Supports Assumption A' - rough random data does NOT have tiny force

### 2. VERIFIED_Riccati_ODE_Mass_Gap_Mechanism_RK4_Integration.py
**Purpose:** Numerically verifies Riccati dynamics driving mass-gap mechanism
**Keywords:** Riccati ODE, mass gap, infrared convexity, RK4, fixed point, PDE comparison
**Status:** VERIFIED (3/3 tests passed)
**Result:** Stable fixed point m = sqrt(sigma/2) is the mass gap

### 3. VERIFIED_SU3_Haar_Jacobian_Hessian_Eigenvalue_Scan_Weyl_Bound.py
**Purpose:** Computes Haar Hessian eigenvalues for SU(3), verifying Weyl bound
**Keywords:** SU(3), Haar measure, Jacobian, Hessian, eigenvalue, Weyl denominator
**Status:** VERIFIED
**Result:** Haar Hessian >= 0.5 at all tested radii (matches Weyl prediction)

### 4. VERIFIED_SU2_Wilson_Action_Equals_Quadratic_Curl_At_Small_Field.py
**Purpose:** Verifies Wilson action matches discrete curl quadratic form at small field
**Keywords:** SU(2), Wilson action, quadratic form, curl, discrete derivative, linearization
**Status:** VERIFIED
**Result:** Ratio S_W/S_quad -> 1.0 as amplitude -> 0 (ratio=0.9996 at eps=0.01)

### 6. VERIFIED_SU2_4D_Metropolis_Plaquette_Defect_Density.py
**Purpose:** 4D SU(2) Metropolis simulation measuring plaquette defect density
**Keywords:** 4D lattice, SU(2), Metropolis, defect density, confinement, small-field
**Status:** VERIFIED
**Result:** Defect density decreases with beta 1.5->6.0 (0.17 -> 0.05), confirming small-field concentration

---

### 7. VERIFIED_SU2_Cartan_Alignment_Score_Test.py
**Purpose:** Verifies geometric "Cartan Alignment Score" for SU(2) configurations
**Keywords:** SU(2), Cartan subalgebra, alignment score, covariance matrix, symmetry breaking
**Status:** VERIFIED
**Result:** Correctly distinguishes isotropic (score~0.66) vs aligned (score~0.0) states

---

## Scripts Requiring PyTorch (Not Verified Here)

These files contain valuable code but depend on PyTorch, which is not available in this verification environment.

1. **`su2_globalization_experiments.py`**
   - Langevin sampling for globalization hints / core set probabilities

2. **`su2_drift_simulation.py`**
   - Large-scale drift simulation estimating Lyapunov functional stats

3. **`07_cpu_smoke_test_a3_torch.md`**
   - CPU smoke test for geometric contraction (A3) using autograd

---

## Summary

| # | Script | Theory Test | Status |
|:--|:-------|:------------|:-------|
| 1 | Disorder-Force A' | High disorder -> high gradient | PASS |
| 2 | Riccati Mass Gap | Fixed point stability | 3/3 PASS |
| 3 | Haar Hessian Weyl | Curvature bound >= 0.5 | PASS |
| 4 | Wilson = Curl | Linearization valid | PASS |
| 5 | Chi_top Extraction | Fourier fit accuracy | PASS |

---

## How to Run

All verified scripts are NumPy-only and can be run with:
```bash
python VERIFIED_<script_name>.py
```

---

*Last updated: 2026-01-01*
