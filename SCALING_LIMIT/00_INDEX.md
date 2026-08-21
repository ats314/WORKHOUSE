# SCALING_LIMIT — Research Folder for Gap 1

> **Project overview:** `../00_START_HERE.md` | **This is the central bottleneck (Sub-Gap 1c)**

**Purpose:** Collect and synthesize all materials needed to prove the **continuum limit existence** for Yang-Mills mass gap.

**Created:** 2026-01-13

---

## Folder Structure

| Folder | Documents | Topic |
|:-------|:----------|:------|
| `01_MOSCO_CONVERGENCE/` | 6 | Mosco convergence of Dirichlet forms, curvature stability |
| `02_PROJECTIVE_LIMITS/` | 5 | Projective limits of measures, cylinder functions |
| `03_TIGHTNESS_COMPACTNESS/` | 3 | Tightness, polarity, Gaussian concentration |
| `04_CONSTANT_UNIFORMITY/` | 3 | Uniform curvature constants, RG intertwining |
| `05_COORDINATE_SCALING/` | 2 | Scale conventions, U vs A coordinates, IR decoupling |
| `06_RP_TRANSFER/` | 5 | Reflection positivity permanence, OS reconstruction |
| `07_CONTINUUM_CONSTRUCTION/` | 4 | Hand-off mechanism, heat kernel, UV/IR structure |
| `MODEL_CREATION/` | 0 | Output for synthesis document |

**Total:** 28 documents

---

## The Gap Structure

### What We Need to Prove

The scaling limit has 4 sub-components:

```
Gap 1: Scaling Limit Existence
├── 1a. Tightness of {μₐ}           → Subsequential limits exist
├── 1b. Mosco convergence           → Forms converge variationally  
├── 1c. Constant uniformity         → ρ(a) ≥ ρ₀ > 0 for all a
└── 1d. RP transfer                 → OS reconstruction works in limit
```

### Current Status by Sub-Gap

| Sub-Gap | Status | Blocking Issue |
|:--------|:-------|:---------------|
| **1a. Tightness** | ⚠️ 40% | Need explicit Sobolev bounds |
| **1b. Mosco** | ✅ 70% | Framework complete, need identification |
| **1c. Uniformity** | ❌ 20% | Wilson → 0, anomaly → finite question |
| **1d. RP transfer** | ✅ 80% | Cylinder function argument works |

---

## Research Questions

### Q1: Does the Wilson Hessian contribution survive?

**The Key Tension:**
- In U-coordinates (dimensionless): Hessian = $\frac{\beta}{N}d_1^*d_1$ → stays finite
- In A-coordinates (dimensionful): U = exp(aA), so $\nabla_U = a^{-1}\nabla_A$
- Net effect: Wilson contribution scales as $\beta a^2 \to 0$ under asymptotic freedom

**Resolution Strategy:**
- The **Haar mass** $\kappa_G = N/4$ is coordinate-independent
- The **anomaly source** provides scale-independent contribution  
- Need to prove: Haar + Anomaly > 0 in limit

### Q2: What is the correct continuum configuration space?

**Options:**
1. Projective limit of lattice configuration spaces
2. Distributional gauge fields (H⁻ˢ valued)
3. Holonomy-based path space

### Q3: Does the spectral gap survive the limit?

**Mosco Stability Theorem says:** If
- $\mathcal{E}_a \to \mathcal{E}$ in Mosco sense
- $\Gamma_{2,a}(f) \geq \rho_0 \Gamma_a(f)$ uniformly

Then
- $\Gamma_2(f) \geq \rho_0 \Gamma(f)$ in the limit

**The bottleneck:** Proving uniformity of ρ₀ in sub-gap 1c.

---

## Attack Plan

### Phase 1: Consolidate Theory (This Session)
- [x] Collect existing documents
- [ ] Create synthesis document
- [ ] Identify exactly what's proven vs. assumed

### Phase 2: Close Sub-Gap 1a (Tightness)
- [ ] Extract LSI → Gaussian concentration → tightness argument
- [ ] Verify Sobolev embedding conditions
- [ ] Formalize in Lean

### Phase 3: Close Sub-Gap 1c (Uniformity)  
- [ ] Analyze hand-off mechanism in detail
- [ ] Prove anomaly source ≥ σ* > 0
- [ ] Show Haar + Anomaly dominates Wilson loss

### Phase 4: Complete Mosco Identification
- [ ] Specify recovery sequences explicitly
- [ ] Prove limit form is the expected YM form
- [ ] Verify semigroup convergence

---

## Key Theorems to Prove/Formalize

| Theorem | Status | Location |
|:--------|:-------|:---------|
| LSI → Gaussian concentration | ✅ Proven | Synth05 |
| Gaussian concentration → tightness | ⚠️ Stated | 03_TIGHTNESS/ |
| Mosco liminf inequality | ⚠️ Stated | 01_MOSCO/ |
| Mosco recovery sequence | ❌ Missing | Need |
| Uniform curvature $\rho(a) \geq \rho_0$ | ❌ Missing | Central gap |
| RP permanence under projective limits | ✅ Proven | 06_RP_TRANSFER/ |
| OS reconstruction in limit | ✅ Proven | Synth02 |

---

## Provenance

Documents collected from:
- `REFLECTION_POSITIVITY/03_CONTINUUM_LIMITS/`
- `HESSIAN/Core_Hessian/`
- `RG_COARSE/01_Block_Convexity_Hinge/`
- `RG_COARSE/02_Anomaly_Trace_Sources/`
- `LYAPUNOV/OS_Reconstruction/`
- `POLARITY_GRIBOV/`
- `FILE DUMP/ALREADY SORTED SECOND PASS/`
