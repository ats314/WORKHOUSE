# Folder Guide: WILSON/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains analysis of the Wilson lattice action and its Hessian

---

## What Is In This Folder

The Wilson folder studies the **lattice gauge action** - how we discretize Yang-Mills.

### The Wilson Action

$$
S_W = \beta \sum_p \left(1 - \frac{1}{N}\text{Re Tr}(U_p)\right)
$$

Where:
- β = inverse coupling (large β = weak coupling)
- U_p = plaquette = product of link variables around elementary square
- The sum is over all plaquettes p

### Key Results

1. **Convexity:** The Wilson action has positive second derivative near vacuum
2. **Hessian Identity:** At vacuum, Hessian = (β/N) d₁*d₁ (discrete Maxwell operator)
3. **Physical interpretation:** Plaquette energy creates stiffness

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `NOTE_OP1_synthesis_04_lattice_gauge_theory.md` | ~20 KB | Complete synthesis |
| `Core_4__Vacuum_Linearization_and_Discrete_Maxwell_Structure.md` | varies | Rigorous proof |

---

## How This Fits the Proof

**Step 1 (Matrix Hinge):**
- Wilson Hessian = (β/N) d₁*d₁
- Combined with Haar: Total curvature ≽ (1/6)𝟙 + (β/N) d₁*d₁

**The d₁*d₁ operator** is the discrete Laplacian on 1-forms (gauge fields).

---

## The Tension with Continuum Limit

In the continuum limit (a → 0):
- We use dimensionful coordinates A where U = exp(aA)
- The Wilson contribution scales as βa² → 0

**This is why Sub-Gap 1c is the central problem:** 
The Wilson contribution vanishes, and we need Haar + Anomaly to dominate.

---

## Status

✅ **Complete** - The Wilson action analysis is rigorous.

The question is what happens in the continuum limit (handled in `SCALING_LIMIT/`).
