# Folder Guide: SCALING_LIMIT/

**Purpose:** Contains the continuum limit existence proof (Step 4) - THE MAIN OPEN PROBLEM

---

## What Is In This Folder (39,671 files, 7.4 GB)

⚠️ **CAUTION:** Most of this size is the RAG index (7.3 GB in `SCALING_LIMIT RAG/`).

The actual research content is in 8 subfolders:
- `01_MOSCO_CONVERGENCE/` (6 docs)
- `02_PROJECTIVE_LIMITS/` (5 docs)
- `03_TIGHTNESS_COMPACTNESS/` (3 docs)
- `04_CONSTANT_UNIFORMITY/` (3 docs)
- `05_COORDINATE_SCALING/` (2 docs)
- `06_RP_TRANSFER/` (5 docs)
- `07_CONTINUUM_CONSTRUCTION/` (4 docs)
- `08_EXTERNAL_SOURCES/` (varies)

**Total:** 28 research documents + synthesis files

---

## THE CENTRAL PROBLEM

This folder addresses: **Does the mass gap survive the continuum limit a → 0?**

### The Structure of Gap 1 (Scaling Limit)

```
Gap 1: Scaling Limit Existence
├── 1a. Tightness        (40%) - Subsequential limits exist
├── 1b. Mosco            (70%) - Forms converge variationally
├── 1c. Uniformity       (20%) - THE HARD PART
└── 1d. RP transfer      (80%) - OS reconstruction works
```

### Sub-Gap 1c: The Central Tension

**The Problem:**
- Wilson Hessian in U-coordinates: stays finite
- Wilson Hessian in A-coordinates (dimensionful): βa² → 0

**In asymptotic freedom:** β → ∞ but βa² → 0.

**What Must Be True:**
The curvature has THREE sources:
1. **Haar** - topological, survives any limit
2. **Wilson** - vanishes as βa² → 0
3. **Anomaly** - scale-independent (?)

**The claim:** Haar + Anomaly > Wilson loss

If Haar + Anomaly is bounded below by ρ₀ > 0, then the gap survives.

---

## Key Files to Read

| File | Size | Purpose |
|------|------|---------|
| `00_INDEX.md` | 4 KB | **READ THIS FIRST** - gap structure |
| `16_Constructive_Mass_Gap_Pipeline.md` | 6 KB | 4-phase pipeline |
| `18_Mosco_Convergence_Continuum.md` | 6 KB | Mosco theory |
| `04_CONSTANT_UNIFORMITY/*` | varies | The 20% sub-gap |

---

## What Is Mosco Convergence?

**Mosco convergence** = variational convergence of Dirichlet forms.

A sequence of forms E_n → E in Mosco sense if:
1. **liminf inequality:** E(f) ≤ liminf E_n(f_n) for f_n → f
2. **Recovery sequences:** For each f, ∃ f_n → f with E_n(f_n) → E(f)

**Why it matters:** Mosco convergence preserves spectral gaps!

---

## Attack Plan (from 00_INDEX.md)

1. **Phase 1:** Consolidate theory (partially done)
2. **Phase 2:** Close Sub-Gap 1a (tightness)
3. **Phase 3:** Close Sub-Gap 1c (uniformity) ← **THE HARD PART**
4. **Phase 4:** Complete Mosco identification

---

## Numerical Evidence Needed

For Sub-Gap 1c:
- RG flow simulations showing gap lower bound uniform in a
- Evidence that anomaly source ≥ σ* > 0
- Evidence that Haar + Anomaly dominates Wilson loss

**Where to look:** `COLAB_RUNS/`, `SIMULATIONS/`, Riccati flow notebooks

---

## Status

**Overall:** 50-60% complete

| Sub-Gap | Status | Blocking |
|---------|--------|----------|
| 1a. Tightness | ⚠️ 40% | Need Sobolev bounds |
| 1b. Mosco | ✅ 70% | Need identification |
| **1c. Uniformity** | ❌ 20% | **CENTRAL GAP** |
| 1d. RP transfer | ✅ 80% | Cylinder functions |

**This is where the proof is most incomplete.**
