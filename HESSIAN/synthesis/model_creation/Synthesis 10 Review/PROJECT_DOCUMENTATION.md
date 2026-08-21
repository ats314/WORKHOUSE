# Synthesis 10 Review: Mathematical Instrument Panel

## Overview

This project provides a comprehensive toolkit for mathematically auditing the **Synthesis 10: Hessian & Riccati Flow** document. The toolkit implements multiple verification layers following the principle of "hostile environment testing."

---

## Directory Structure

```
Synthesis 10 Review/
├── Synthesis_10_Hessian_Riccati.md   # Main synthesis document (2600 lines)
├── FORMULA_REFERENCE.md              # Key formulas extracted for consistency checking
├── AUDIT_FINDINGS.md                 # Verified results and issues found
├── FORMAL_VERIFICATION_SPEC.md       # Lean proof specifications
│
├── verify_math.py                    # NumPy numerical verification
├── symbolic_verify.py                # SymPy symbolic verification
├── jax_verify.py                     # JAX autodiff verification
├── limit_probes.py                   # Boundary case analysis
├── randomized_falsify.py             # 100K sample stress testing
├── dimensional_analysis.py           # Scaling/dimensional checks
├── run_all_tests.py                  # Master test runner
│
└── synthesis10_lean/                 # Lean formal proofs (copy)
```

**Primary Lean location:** `C:\Users\ats31\.gemini\lean_projects\synthesis10_lean`

---

## Tool Inventory

### 1. NumPy Verification (`verify_math.py`)

**Purpose:** Numerical falsification - evaluate formulas at many points to find counterexamples.

```powershell
cd "c:\...\Synthesis 10 Review"
python verify_math.py
```

**Tests:**
- Haar eigenvalue global bound (≥ 1/6)
- c₀ coefficient values
- Critical β for convexity loss
- Riccati fixed point convergence

---

### 2. SymPy Symbolic (`symbolic_verify.py`)

**Purpose:** Algebraic sanity - limits, Taylor series, identity verification.

```powershell
python symbolic_verify.py
```

**Tests:**
- Haar eigenvalue limit as θ → 0 (= 1/6)
- Taylor expansion: λ = 1/6 + θ²/30 + O(θ⁴)
- Riccati fixed point residual = 0
- vHJ derivation step-by-step

---

### 3. JAX Autodiff (`jax_verify.py`)

**Purpose:** Automatic differentiation - verify Hessian/gradient formulas directly.

```powershell
python jax_verify.py
```

**Tests:**
- vHJ derivation match (ΔP/P vs -ΔS + |∇S|²)
- Hessian of |∇S|² gives 2H² + drift
- SU(2) Haar action Hessian eigenvalues
- Random point falsification

---

### 4. Limit Probes (`limit_probes.py`)

**Purpose:** Test formulas at boundary cases where errors hide.

```powershell
python limit_probes.py
```

**Tests:**
- Small θ limit (θ → 0)
- Large θ limit (θ → π)
- Large β (strong coupling)
- Abelian U(1) limit

---

### 5. Randomized Falsification (`randomized_falsify.py`)

**Purpose:** Generate 100K random inputs to stress-test claims.

```powershell
python randomized_falsify.py
```

**Tests:**
- Compare two derivation paths
- Symbolic vs numeric cross-check
- Hunt for bound violations
- Numerical stability near singularities

---

### 6. Dimensional Analysis (`dimensional_analysis.py`)

**Purpose:** Detect formulas that scale incorrectly.

```powershell
python dimensional_analysis.py
```

**Checks:**
- Gap formula Δ ≥ √(c₀/2)/a [CONSISTENT]
- RG stability g⁴ > 24/(c₀a²) [FLAGGED]
- Dichotomy λ_lat/a scaling [FLAGGED]

---

### 7. Run All Tests (`run_all_tests.py`)

**Purpose:** Execute entire verification suite.

```powershell
python run_all_tests.py
```

---

## Formal Verification (Lean 4)

### Current Status

Lean 4.26.0 and mathlib are installed, but there's a Windows/Lake issue with file paths. Options:

1. **Use WSL (recommended)** - install Linux subsystem
2. **Use core Lean only** - simplified proofs without mathlib
3. **Wait for mathlib fix** - proofs ready when environment works

### Lean Files Location

```
C:\Users\ats31\.gemini\lean_projects\synthesis10_lean\
├── lakefile.toml
├── Synthesis10.lean          # Root import
└── Synthesis10/
    ├── RiccatiFixedPoint.lean  # σ - 2λ² = 0 at λ = √(σ/2)
    ├── HaarMassCoeff.lean      # c₀ = (N²-1)/(2N)
    └── GapFormula.lean         # Δ ≥ √(c₀/2)/a
```

### Building in WSL (after WSL install)

```bash
# In WSL (Ubuntu):
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | bash
source ~/.profile

cd /mnt/c/Users/ats31/.gemini/lean_projects/synthesis10_lean
lake exe cache get
lake build Synthesis10
```

---

## Key Formulas Verified

| Formula | Location | Status |
|:--------|:---------|:-------|
| vHJ: ∂ₜS = ΔS - |∇S|² | Ch 2.2 | ✓ Verified |
| Riccati: λ̇ = σ - 2λ² | Ch 4.1 | ✓ Verified |
| Fixed point: λ_* = √(σ/2) | Ch 4.1 | ✓ Verified |
| Haar bound: λ ≥ 1/6 | Ch 25 | ✓ Verified |
| c₀ = (N²-1)/2N | Ch 24 | ✓ Verified |
| Gap: Δ ≥ √(c₀/2)/a | Ch 24 | ✓ Verified |

---

## Notation Issues Fixed

Two dimensional clarifications were added to the synthesis:

1. **Ch 32 (RG Stability):** Added note explaining g has units [length]
2. **Ch 48 (Dichotomy):** Added note explaining λ_lat/a gives [mass²]

---

## Installed Tools

| Tool | Version | Purpose |
|:-----|:--------|:--------|
| Python | 3.11 | Core runtime |
| NumPy | installed | Numerical computation |
| SciPy | installed | Scientific functions |
| SymPy | 1.14.0 | Symbolic math |
| JAX | installed | Autodiff |
| Git | 2.52.0 | Version control |
| Lean | 4.26.0 | Formal proofs |
| elan | 4.1.2 | Lean version manager |

---

## Next Steps After WSL Install

1. **Install WSL:** Run `wsl --install` as Administrator, restart
2. **Setup Ubuntu:** Create user, install elan
3. **Build Lean proofs:** `lake build Synthesis10`
4. **Verify all proofs compile**
5. **Continue auditing Chapters 7-54**

---

## Quick Reference: Run Verification

```powershell
# Full test suite
cd "c:\Users\ats31\.gemini\antigravity\playground\scalar-cluster\CLEANUP TEST\HESSIAN\MODEL CREATION\Synthesis 10 Review"
python run_all_tests.py

# Individual tests
python verify_math.py           # NumPy
python symbolic_verify.py       # SymPy
python jax_verify.py            # JAX
python limit_probes.py          # Limits
python randomized_falsify.py    # Random
python dimensional_analysis.py  # Dimensions
```
