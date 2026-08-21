# Folder Guide: HAAR/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains the geometric foundation - the "Haar Mass Mechanism"

---

## What Is In This Folder

The Haar folder contains research on why the gauge group's **compactness** creates a natural mass.

### The Key Insight
- SU(N) is a compact Lie group with positive Ricci curvature
- The Haar measure on SU(N) creates an "entropic well"
- This curvature acts like a mass term in the path integral
- **This is the "spark" that ignites the mass gap**

### Mathematical Statement

The Haar mass coefficient:
$$
\kappa_G = \frac{N^2 - 1}{2N}
$$

For SU(2): κ_G = 3/4
For SU(3): κ_G = 4/3

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `Synthesis_01_Haar_Geometry_Foundation.md` | ~20 KB | Complete synthesis |
| `Core_2__Configuration_Geometry_and_Differential_Calculus.md` | varies | Rigorous definitions |

---

## How This Fits the Proof

**Step 1 (Matrix Hinge) depends on:**
- Haar curvature (this folder)
- Wilson convexity (`WILSON/`)
- Combined into Hessian (`HESSIAN/`)

**The claim:** Ric_μ ≽ c_H + t d₁*d₁ where c_H comes from Haar.

---

## Status

✅ **Complete** - The Haar contribution is well-understood and formalized.

The remaining question is whether this contribution SURVIVES the continuum limit (handled in `SCALING_LIMIT/`).
