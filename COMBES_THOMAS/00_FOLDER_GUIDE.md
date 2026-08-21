# Folder Guide: COMBES_THOMAS/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains decay estimates for the Green's function (Step 3)

---

## What Is In This Folder (114 files, 4.3 MB)

This folder contains proofs that the **inverse Hessian decays exponentially**.

### The Combes-Thomas Argument

For a positive operator H with gap m²:
$$
|(H^{-1})_{xy}| \le C e^{-m|x-y|}
$$

**In words:** The Green's function (inverse of H) decays exponentially with distance.

### Why It Matters

From `HELFFER_SJOSTRAND/`: Cov ≤ ⟨∇, H⁻¹ ∇⟩

If H⁻¹ decays exponentially:
- Covariances decay exponentially
- Correlation length is finite
- **This is the mass gap**

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay.md` | ~17 KB | Main theorem |
| `Appendix_H__Davies_Type_Decay.md` | varies | Massive Maxwell case |
| `Core_7__Conditioned_Exponential_Clustering.md` | varies | Application |
| `05_simulation_appendix_maxwell_and_a100_su2.md` | ~19 KB | Numerical verification |

---

## The Massive Maxwell Operator

Near vacuum, the Hessian looks like:
$$
M_H = c_0 \cdot \mathbf{1} + \frac{\beta}{N} d_1^* d_1
$$

This is the **massive Maxwell operator** (discrete Laplacian + mass).

Combes-Thomas gives decay rate:
$$
m = \sqrt{c_0} \quad \text{(roughly)}
$$

---

## How This Fits the Proof

**Step 3 (Clustering):**
1. Hessian ≽ M_H (from `HESSIAN/`)
2. HS formula: Cov ≤ ⟨∇, M_H⁻¹ ∇⟩ (from `HELFFER_SJOSTRAND/`)
3. **This folder:** M_H⁻¹ decays as exp(-m|x-y|)
4. Therefore: correlations decay exponentially

**Step 4 needs:**
- Decay rate m to be uniform in lattice spacing a
- Connected to `SCALING_LIMIT/` Sub-Gap 1c

---

## Numerical Evidence

From Colab notebooks:
- Green's function computed on L=12-16 lattices
- Exponential decay visually confirmed
- Davies bound verified: η_obs > η_theory

---

## Status

✅ **Complete** - The decay theory is rigorous and numerically verified.

**Open:** Uniformity of decay rate in continuum limit.
