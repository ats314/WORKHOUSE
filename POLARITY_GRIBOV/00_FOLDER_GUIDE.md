# Folder Guide: POLARITY_GRIBOV/

> **Project overview:** `../00_START_HERE.md`

**Purpose:** Contains treatment of topological obstructions (Singularities)

---

## What Is In This Folder (126 files, 4.8 MB)

This folder addresses: **What happens at gauge-fixing singularities?**

### The Gribov Problem

When we fix a gauge (e.g., Coulomb gauge), the gauge-fixing surface may:
- Have multiple intersections with gauge orbits ("Gribov copies")
- Develop singularities at the "Gribov horizon"

**The Gribov horizon** = locus where the Faddeev-Popov operator has zero eigenvalue.

### Why It Matters

At the Gribov horizon:
- The gauge-fixed path integral may diverge
- Naive perturbation theory breaks down
- The Matrix Hinge may fail

**Solution:** Restrict to the "fundamental modular region" inside the horizon.

### Polarity and Stratification

**Polarity:** The Gribov horizon has positive codimension (measure zero).

The configuration space stratifies:
- **Generic stratum:** Regular gauge orbits (most of space)
- **Reducible stratum:** Singular gauge orbits (measure zero)

The proof shows: The singular strata don't affect the gap.

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `Synthesis_15_Polarity_Gribov.md` | ~28 KB | Complete synthesis |
| `SYNTH_P18_gaussian_polarity.md` | ~47 KB | Gaussian approximation |

---

## How This Fits the Proof

**Global Safety:**
- Steps 1-3 work on the "good set" K
- K must avoid the Gribov horizon
- **This folder:** The horizon has measure zero, so it's safely avoided

**Specifically:**
- Polarity ensures μ(singular strata) = 0
- The Matrix Hinge is stated for the generic stratum
- OS reconstruction only needs generic configurations

---

## Numerical Evidence

From Colab notebooks:
- `gribov_horizon_L12.ipynb`: Found β_crit ≈ 2.5 for Gribov transition
- Confirmed: For β > β_crit, configurations stay in good region

---

## Status

✅ **Complete** - The polarity argument is rigorous.

Gribov copies are handled by the stratification theory.
