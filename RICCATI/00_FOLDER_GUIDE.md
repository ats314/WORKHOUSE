# Folder Guide: RICCATI/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains the Riccati flow stability analysis (Step 4)

---

## What Is In This Folder (222 files, 15 MB)

This folder studies how **curvature evolves under RG (renormalization group) flow**.

### The Riccati Equation

The curvature ρ under coarse-graining satisfies a Riccati ODE:
$$
\frac{d\rho}{dt} = -a\rho^2 + b\rho + c
$$

**Key property:** This equation has a stable fixed point at:
$$
\rho^* = \frac{b + \sqrt{b^2 + 4ac}}{2a}
$$

If ρ starts positive and c > 0, it stays positive forever!

### Why It Matters

We need the spectral gap to survive infinitely many RG steps:
- Start with gap at lattice spacing a
- Coarse-grain: a → 2a → 4a → ...
- Need gap to stay positive as a → 0 (continuum)

**Riccati stability says:** If the curvature source σ > 0 persists, so does the gap.

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `Synthesis_03_Renormalization_Riccati.md` | ~24 KB | Complete synthesis |
| `Synthesis_05_Continuum_Spark.md` | ~36 KB | The "Spark" conjecture |
| `Core_9__Thermodynamic_Limit_and_OS_Gap_at_Fixed_Cutoff.md` | ~22 KB | Fixed cutoff |
| `SYNTH_P14_rg_flow_stability.md` | ~48 KB | Flow stability |

---

## The Curvature-Wilson Ratio

From Colab notebooks: The ratio C_Wr decreased 700× under two RG steps.
This shows curvature flowing toward a fixed point.

---

## How This Fits the Proof

**Step 4 (Continuum):**
1. At each scale a: gap exists (from Steps 1-3)
2. **This folder:** Riccati flow preserves gap under blocking
3. Need uniform lower bound: ρ(a) ≥ ρ₀ > 0 for all a

**The connection to Entropic Spark:**
- The source term c in Riccati comes from Haar curvature
- If Haar curvature ("Spark") persists → c > 0 → gap persists

---

## Status

✅ **Complete** - The Riccati analysis is rigorous.

**Open:** Does the Haar source survive continuum limit?
- This is the "Entropic Spark" conjecture
- Related to Sub-Gap 1c
