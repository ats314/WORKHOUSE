# Folder Guide: COLAB_RUNS/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains GPU simulation notebooks for numerical verification

---

## What Is In This Folder (186 notebooks, 31 MB)

This folder contains **Jupyter notebooks** run on Google Colab with NVIDIA A100 GPUs.

### Purpose

The notebooks verify specific claims in the proof numerically:
- Curvature positivity checks
- Spectral gap computations
- Wilson loop measurements
- RG flow stability tests

---

## Extraction Status

A previous session extracted 57 documents, but they are **superficial**:
- Most are 256-2500 bytes
- Only contain summaries, not full code/output
- Need to be replaced with comprehensive extraction

**Location:** `_PROOFS/`, `_RESULTS/`, `_ALGORITHMS/`, `_DERIVATIONS/`

---

## Key Notebooks to Re-Extract

| Notebook | Key Result | Proof Component |
|----------|------------|-----------------|
| `Untitled93.ipynb` | Mass gap restored at t=0.26 | Theorem 1(A) |
| `Untitled89.ipynb` | Convexity 15/15 PASS | Matrix Hinge |
| `Untitled127.ipynb` | Continuum certificate | Core-10 |
| `Untitled47-48.ipynb` | Gauss-Bonnet exact | Geometry |
| `Untitled125.ipynb` | Green's function decay | Combes-Thomas |
| `Untitled105.ipynb` | Defect density scan | RG stability |
| `Untitled110.ipynb` | Laplacian drift PASS | Lyapunov |
| `trg_ising_colab.ipynb` | TRG bug identified | HOTRG |

---

## Extraction Guidelines (for future sessions)

When extracting from notebooks:

1. **Include full code cells** that produce the result
2. **Include complete output** - not truncated
3. **Map to proof component** - which Core/Appendix does this verify?
4. **Note numerical values** precisely
5. **Flag any failures or anomalies**

**Bad extraction:** "Mass gap restored at t=0.26" (50 bytes)
**Good extraction:** Full code + full output + mathematical context (5+ KB)

---

## Technical Details

- **Hardware:** NVIDIA A100 (Colab)
- **Frameworks:** JAX, PyTorch, NumPy
- **Lattice sizes:** L = 2 to 32 (mostly 4-16)
- **Gauge groups:** SU(2), SU(3), U(1)

---

## Status

🔄 **Partially extracted** - Need comprehensive re-extraction.

**Priority:** Focus on results that verify Sub-Gap 1c (uniformity).
