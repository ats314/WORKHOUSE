# Folder Guide: HESSIAN/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains the Bakry-Émery curvature analysis and Matrix Hinge proofs

---

## What Is In This Folder (751 files, 165 MB)

The HESSIAN folder is one of the largest and most important. It contains:
- Bakry-Émery calculus (Γ₂ formalism)
- Matrix Hinge inequality proofs
- Curvature lower bound calculations
- Numerical verification of curvature positivity

### What Is Bakry-Émery?

A framework for studying curvature via second derivatives:
- Γ(f, g) = ⟨∇f, ∇g⟩ (carré du champ)
- Γ₂(f, g) = ½ L Γ(f,g) - Γ(f, Lg) - Γ(Lf, g)
- If Γ₂ ≥ ρΓ, then the generator L has spectral gap ≥ ρ

### The Matrix Hinge

**Key Theorem:** On the "good set" K of typical configurations:
$$
\text{Ric}_\mu \succeq c_H \cdot \mathbf{1} + \frac{\beta}{N} d_1^* d_1
$$

This lower bound has two parts:
1. **c_H** - constant from Haar curvature (always positive)
2. **d₁*d₁** - the discrete Maxwell operator (positive semi-definite)

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `Synthesis_10_Hessian_Riccati.md` | ~20 KB | Complete synthesis |
| `Appendix_E__Bakry_Emery_Calculus.md` | ~26 KB | Technical background |
| `Core_5__Local_Coercivity_and_Matrix_Hinge_on_Good_Set.md` | varies | Rigorous proof |

---

## How This Fits the Proof

**Step 1 (Matrix Hinge):**
- This folder PROVES the curvature lower bound
- The bound holds on the "good set" K

**Step 2 depends on this:**
- Uses Γ₂ ≥ ρΓ to derive Log-Sobolev inequality
- LSI gives spectral gap

---

## The "Good Set" K

The Matrix Hinge only holds on a subset K of configurations:
- K = configurations "close enough" to vacuum
- On K, curvature is strictly positive
- Off K (the "bad set" Kᶜ), curvature may be negative

**Critical question:** How small is the measure of Kᶜ?
- This is what Appendix J (Typicality) must prove
- Need: μ(Kᶜ) ≤ C exp(-α/a²) or similar

---

## Numerical Evidence in This Folder

The folder contains numerical tests of curvature positivity:
- Convexity scans across β values
- Eigenvalue computations of Hessian
- "15/15 PASS" results from Colab notebooks

---

## Status

✅ **Complete** - The Matrix Hinge is proven for the good set K.

**Open:** Quantitative bounds on μ(Kᶜ) - handled in `LYAPUNOV/` and Appendix J.
