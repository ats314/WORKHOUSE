# Folder Guide: TENSOR_NETWORK/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Tensor network methods (HOTRG, TRG) for lattice gauge theory

---

## What Is In This Folder

The Tensor Network folder contains research on **tensor renormalization group** methods for computing lattice observables.

### Key Methods

1. **HOTRG:** Higher-Order Tensor RG - coarse-grains 2D lattice
2. **q-Racah Symbols:** Quantum 6j symbols for recoupling
3. **Topological Susceptibility:** χ_top from TRG

---

## Subfolders

| Folder | Purpose |
|--------|---------|
| `01_QRACAH_DOOB_GAP/` | q-Racah spectral gap analysis |
| `02_Q6J_SYMBOLS/` | Quantum 6j symbol calculations |
| `03_THETA_DEFORMATION/` | θ-angle deformation effects |
| `04_HOTRG_METHODS/` | HOTRG algorithm implementations |
| `05_TRANSFER_OPERATOR/` | Transfer matrix analysis |
| `06_LATTICE_QCD_SECTORS/` | Topological sectors |
| `07_TOPOLOGICAL_SUSCEPTIBILITY/` | χ_top calculations |

---

## Key Files

| File | Purpose |
|------|---------|
| `13_qRacah_Spectral_Gap.md` | Spectral gap from q-deformed symbols |
| `14_Tensor_Network_HOTRG.md` | HOTRG methodology |
| `q6j_low_spin_validation.py` | Numerical validation code |

---

## How This Fits the Proof

**Numerical Verification:** TRG methods provide non-perturbative numerical evidence for the mass gap. They verify the gap survives in different topological sectors.

**Status:** ✅ Complete (numerical evidence)
