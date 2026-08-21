# UNIFORMITY_ASYMPTOTIC_FREEDOM

## Topic Overview
This folder addresses the **key remaining problem** in the Yang-Mills mass gap proof:

> "The architecture is complete; the key remaining problem is **uniformity under asymptotic freedom**."

## The Core Question
How to ensure that the spectral gap constant σ (or equivalently η(a)/a) remains **uniformly bounded away from zero** as the lattice spacing a → 0 along the asymptotically free trajectory?

## Key Mechanisms Being Explored

### 1. Geometric Source Terms (σ_geom)
- Scale-independent source from Weyl Jacobian / FP determinant
- Ricci curvature lower bound on compact group manifolds
- Heat kernel coarse-graining preserves Weyl denominator

### 2. Riccati Convexity Attractor
- Fixed point at λ* = √(σ/2) is stable
- Gap is "self-sustaining" if σ > 0 persists
- For non-Abelian groups, σ comes from Haar/compactness

### 3. Entropic Gribov Spark
- Alternative IR convexity from boundary entropy
- Conjecture: m*² > 0 independent of UV cutoff
- Connection to high-dimensional convexity

### 4. RG Monotonicity / Lyapunov
- Scale-stable defect functional Φ(a)
- If η(a) ≥ Φ(a) in lattice units → uniformity

## Sub-Gaps to Close

| # | Gap | Status |
|:--|:----|:-------|
| 1 | Prove σ_geom = O(1) in physical units as a → 0 | OPEN |
| 2 | Verify Riccati attractor stability under RG | OPEN |
| 3 | Test Entropic Gribov Spark numerically | OPEN |
| 4 | Connect LSI constant to physical mass | OPEN |

## Related Folders
- `SCALING_LIMIT/` - Continuum construction and limits
- `RICCATI/` - Riccati flow and convexity attractor
- `POLARITY_GRIBOV/` - Entropic spark and Gribov horizon
- `RG_COARSE/` - RG coarse-graining and gap transfer
- `HAAR/` - Haar measure geometry and curvature

## Key References (from RAG)
1. `06_Riccati_Convexity_Attractor.md` - Why gap survives via stable fixed point
2. `07_heat_kernel_weyl_denominator_scale_independent_sigma_geom.md` - Scale-independent source
3. `RECOMMENDED_04_Entropic_Gribov_Spark_Conjecture_v2.md` - Alternative IR convexity
4. `01_pillarL_geometric_mass_gap_expanded.md` - Step C: scale-independent source term

---

*Created: 2026-01-13*
*Status: New topic folder for central open problem*
