# Folder Guide: RG_COARSE/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains the RG coarse-graining maps (Step 4)

---

## What Is In This Folder (188 files, 8.6 MB)

This folder defines **how to coarse-grain the lattice gauge theory**.

### What Is Coarse-Graining?

**Block Spins:** Average fields over blocks of 2×2×2×2 sites.
- Fine lattice at spacing a → Coarse lattice at spacing 2a
- Repeat: 2a → 4a → 8a → ...
- In the limit: continuum theory at a → 0

### The RG Transformation

For gauge theory, coarse-graining is tricky:
- Must preserve gauge invariance
- Block link = product of link matrices in the block
- Action changes: S(a) → S(2a) with new coupling

The **Balaban construction** (1980s) provides a rigorous framework.

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `Synthesis_12_RG_Coarse.md` | ~41 KB | Complete synthesis |
| `SYNTH_P14_rg_flow_stability.md` | ~48 KB | Stability analysis |
| `safe_scan_results_scaled.png` | ~50 KB | Numerical visualization |

---

## How This Fits the Proof

**Step 4 (Continuum):**
1. Define blocking map: (U, μ_a) → (Ũ, μ_{2a})
2. Track gap under blocking (from `RICCATI/`)
3. Show gap is uniform: λ(a) ≥ λ₀ > 0 for all a

**The RG recursion:**
$$
C_P^{(n)} \le \gamma C_P^{(n+1)} + C_{\text{block}}
$$

With γ < 1 (contraction), this gives uniform bounds.

---

## Numerical Evidence

From Colab notebooks ("rg_blocking_balaban"):
- Verified κ → 0 under blocking (defect suppression)
- Confirmed Balaban's assumptions hold numerically

---

## Status

✅ **Blocking map defined** - The construction is rigorous.

**Open:** 
- Need to verify uniform curvature bound (Sub-Gap 1c)
- Connected to `SCALING_LIMIT/04_CONSTANT_UNIFORMITY/`
