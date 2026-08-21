# Folder Guide: LSI_POINCARE/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains the Log-Sobolev and Poincaré inequality derivations (Step 2)

---

## What Is In This Folder (333 files, 21 MB)

This folder contains the **functional inequalities** that convert curvature into spectral gap.

### What Are These Inequalities?

**Poincaré Inequality:**
$$
\text{Var}_\mu(f) \le C_P \int |\nabla f|^2 d\mu
$$
- C_P is the "Poincaré constant"
- Controls variance by gradient
- Implies spectral gap λ₁ ≥ 1/C_P

**Log-Sobolev Inequality (LSI):**
$$
\text{Ent}_\mu(f^2) \le C_{LS} \int |\nabla f|^2 d\mu
$$
- Stronger than Poincaré
- Ent(g) = ∫ g log(g/⟨g⟩) dμ
- Controls concentration

**Relationship:**
- Bakry-Émery curvature ρ > 0 ⟹ LSI with C_LS = 2/ρ
- LSI ⟹ Poincaré with C_P ≤ C_LS
- LSI ⟹ exponential concentration

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `Synthesis_02_Analysis_LSI.md` | ~26 KB | Complete synthesis |
| `Appendix_E__Bakry_Emery_Calculus.md` | ~26 KB | BE framework |
| `01_Geometric_Spectral_Stability_HandOff_v5.md` | ~20 KB | Stability analysis |

---

## How This Fits the Proof

**Step 2 (Local-to-Global):**
1. Matrix Hinge gives: Γ₂ ≥ ρΓ on good set K (from `HESSIAN/`)
2. Lyapunov drift controls escape from K (from `LYAPUNOV/`)
3. **This folder:** Combine to get global LSI

**Result:** The diffusion generator L has spectral gap λ ≥ ρ₀ > 0.

---

## The Local-to-Global Problem

The curvature bound Γ₂ ≥ ρΓ only holds on the good set K.
To get a GLOBAL inequality, we need:

1. **Lyapunov function V** with drift LV ≤ -λV + b
2. **Patching:** Glue local Poincaré inequalities together
3. **Result:** Global LSI with possibly different constant

This is the content of the "Local-to-Global" argument in Core files 5-8.

---

## Numerical Evidence

Colab notebooks verified:
- Spectral gap exists for various β, L values
- Gap may decrease with system size (need uniformity)

---

## Status

✅ **Complete** - The LSI derivation from curvature is rigorous.

**The remaining question:** Is the LSI constant UNIFORM in the continuum limit?
- This is core Sub-Gap 1c
- Handled in `SCALING_LIMIT/`
