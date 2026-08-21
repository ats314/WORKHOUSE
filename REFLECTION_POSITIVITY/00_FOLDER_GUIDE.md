# Folder Guide: REFLECTION_POSITIVITY/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains Osterwalder-Schrader reconstruction (Step 3)

---

## What Is In This Folder (128 files, 21 MB)

This folder addresses: **How do we go from Euclidean path integral to Hamiltonian?**

### The Problem

We work in **Euclidean signature** (imaginary time):
- Path integral over field configurations
- Correlations decay in Euclidean time
- This is statistical mechanics

But physics needs **Lorentzian signature** (real time):
- Quantum mechanical Hamiltonian H
- States in Hilbert space
- Mass gap = lowest eigenvalue of H above ground state

### Osterwalder-Schrader Reconstruction

**The OS axioms** guarantee:
- If Euclidean correlations satisfy reflection positivity (RP)
- Then there exists a Hamiltonian and Hilbert space

**Key theorem:** Exponential decay in Euclidean time ⟹ mass gap in Hamiltonian

$$
\langle O(0) O(t) \rangle \sim e^{-mt} \quad \Longrightarrow \quad \text{gap}(H) \ge m
$$

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `Synthesis_02_Reflection_Positivity_OS_Reconstruction.md` | ~39 KB | Complete synthesis |
| `Appendix_K__Reflection_Positivity_for_Wilson.md` | varies | RP proof for Wilson |
| `Appendix_L__OS_Reconstruction_and_Gap_Extraction.md` | varies | Reconstruction theorem |
| `Core_3__OS_Framework_at_Fixed_Cutoff.md` | varies | Rigorous setup |
| `Core_9__Thermodynamic_Limit_and_OS_Gap.md` | varies | Fixed cutoff gap |

---

## How This Fits the Proof

**Step 3 (Clustering → Gap):**
1. Exponential clustering proven (from `COMBES_THOMAS/`)
2. Wilson measure satisfies RP (proven in Appendix K)
3. **This folder:** OS reconstruction gives Hamiltonian gap

**The key step:**
$$
\text{Euclidean clustering } + \text{ RP } \Longrightarrow \text{Hamiltonian mass gap}
$$

---

## What Is Reflection Positivity?

RP is a constraint on correlations:
- Reflect configurations across a hyperplane (t = 0)
- θ(O) = reflected observable
- ⟨O · θ(O)⟩ ≥ 0 for all O

**Geometric meaning:** The Euclidean path integral "looks like" a quantum theory.

---

## Numerical Verification

Colab notebooks verified RP for Wilson action on small lattices.

---

## Status

✅ **Complete** - OS reconstruction is a standard result, properly applied here.

**For continuum limit:** Need RP to persist under scaling limit.
- This is Sub-Gap 1d (80% complete)
- Handled in `SCALING_LIMIT/06_RP_TRANSFER/`
