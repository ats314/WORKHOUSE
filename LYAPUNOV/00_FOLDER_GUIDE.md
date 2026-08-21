# Folder Guide: LYAPUNOV/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains Lyapunov drift analysis for concentration bounds (Step 2)

---

## What Is In This Folder (141 files, 11 MB)

This folder addresses: **How do we control configurations outside the good set K?**

### The Problem

The Matrix Hinge only holds on K (configurations close to vacuum).
On the "bad set" Kᶜ, curvature may be negative.

**We need to show:** The measure μ(Kᶜ) is exponentially small.

### Lyapunov Drift Functions

A **Lyapunov function** V is a "distance from vacuum" that satisfies:
$$
LV \le -\lambda V + b
$$

Where:
- L is the generator of the Langevin dynamics
- λ > 0 is the drift rate (pushes V down)
- b is a constant (allows V to grow a little)

**Consequence:** If V is large (far from vacuum), LV < 0, so V decreases.
This means: Configurations are pushed toward the good region.

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `Synthesis_05_Lyapunov_Methods.md` | ~49 KB | Complete synthesis |
| `07_Lyapunov_drift_and_uniform_in_volume.txt` | ~53 KB | Detailed theory |
| `SYNTH_P14_rg_flow_stability.md` | ~48 KB | RG stability |

---

## How This Fits the Proof

**Step 2 (Local-to-Global):**
1. Matrix Hinge holds on K (from `HESSIAN/`)
2. **This folder:** Lyapunov drift shows μ(Kᶜ) is small
3. Combine for global LSI (in `LSI_POINCARE/`)

**The claim for Appendix J:**
$$
\mu(K^c) \le C e^{-\alpha V_{min}}
$$

Where V_min is the minimum of V on the boundary of K.

---

## The Key Calculation

The Lyapunov function is typically:
$$
V(U) = \sum_p \vartheta(U_p)^2
$$

The drift LV involves:
- Laplacian from diffusion: pushes toward vacuum (good)
- Gradient: may push away (bad if curvature negative)
- The net effect must be negative drift

---

## Numerical Evidence

From Colab notebooks:
- `Untitled110.ipynb`: LV ≤ RHS verified (PASS)
- Drift inequality check: mean(LV) = -7.06, slack positive

---

## Connection to SCALING_LIMIT

For the continuum limit, we need:
- Lyapunov drift to be UNIFORM in lattice spacing a
- This feeds into Sub-Gap 1a (tightness)

---

## Status

✅ **Complete** - Lyapunov drift theory is established.

**Open:** Explicit quantitative bounds for specific choice of K.
- This is Appendix J
- Critical for the full proof
