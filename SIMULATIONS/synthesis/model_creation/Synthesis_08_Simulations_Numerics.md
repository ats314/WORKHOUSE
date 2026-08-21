# Synthesis 08: Simulations and Numerics — Computational Verification

## Abstract

This synthesis extracts the computational verification layer of the HAAR mass gap project from 25 files (15 docs, 8 Python scripts, 2 CSV results). The simulations serve to:

1. **Test theoretical predictions** (decay bounds, curvature constants)
2. **Hunt for counterexamples** to Assumption A′
3. **Measure order-one quantities** (Cartan misalignment, curvature defect)
4. **Verify spectral bounds** at scale

---

# Chapter 1: Simulation Index

## 1.1 Six Core Simulation Extracts

From `SIMULATION_REVIEW_BEST_WORK_INDEX.md`:

| # | Extract | Focus |
|:--|:--------|:------|
| 1 | Determinant Reduction | Algebraic identity + stress checks + GPU speedups |
| 2 | Discrete de Rham | Cochain complex, Betti numbers, projection harness |
| 3 | Maxwell/C₀/DG Decay | Constants $C_0$, $D_E$, decay bounds, κ extraction |
| 4 | Lyapunov Drift | Drift inequality, β/scale convexity, constant linking |
| 5 | Failure Modes | Blocking, uniform covariance, φ-Hessian mismatch |
| 6 | q-Racah/Doob Toy | Diagonalizable toy gap machine, safe region scans |

## 1.2 Selection Criteria

Files chosen because they:
- Behave like **computational proofs** (machine-precision consistency)
- Create **reusable harnesses** (physics vs diagnostic separable)
- Reveal **potentially general structure** (same constant in different theorems)
- Are **toy-model pillars** (mathematically explicit, scalable)

---

# Chapter 2: Core Observables

## 2.1 Star Curvature Defect $\Phi(a)$

At link $\ell$, define:
$$
\Delta_\ell(U) := (\kappa_* - \lambda_{\min})_+
$$

where $\kappa_* = \lambda_{\min}(\mathsf{H}_W^{(\ell)}(U^{(0)}))$ is the vacuum reference.

Average:
$$
\Phi(a) := \mathbb{E}_{\mu_a}[\Delta_\ell(U)]
$$

**Prediction:** $\Phi(a)$ is order-one in lattice units and scale-stable under coarse graining.

## 2.2 Cartan Misalignment $r_\ell$

For six plaquettes incident to $\ell$, compute misalignment score $r_\ell \in [0,1]$:
- $r_\ell \approx 0$: near common Cartan direction (almost abelian)
- $r_\ell \approx 1$: strongly noncommuting (generic)

**Prediction:** $r_\ell$ is typically order-one; $\mathbb{P}(r_\ell \le \epsilon)$ is extremely rare.

---

# Chapter 3: Measurement Protocol

## 3.1 One-Page Protocol for $\Phi(a)$

**Inputs:**
- SU(3) Wilson gauge configurations at fixed $\beta$
- Link variables $U_\mu(x) \in SU(3)$

**Steps (per configuration):**
1. Sample batch of links $\{\ell_i\}_{i=1}^B$ uniformly
2. For each link:
   - Enumerate 6 plaquettes in Star($\ell$)
   - Compute plaquette holonomies
   - Gauge-fix at $\ell$ so $U_\ell = \mathbf{1}$
   - Assemble exact physical star Hessian $\mathsf{H}_W^{(\ell)}(U)$
   - Compute $\lambda_{\min}$
   - Record $\Delta_\ell = (\kappa_* - \lambda_{\min})_+$
   - Compute misalignment $r_\ell$
3. Average: $\widehat{\Phi}(a) = \frac{1}{B}\sum_i \Delta_{\ell_i}$

**Outputs:**
- $\widehat{\Phi}(a)$ with standard error
- Histogram of $r_\ell$; especially $\mathbb{P}(r_\ell < 0.1)$, $\mathbb{P}(r_\ell < 0.2)$
- Joint correlation $\text{corr}(\lambda_{\min}, r)$

---

# Chapter 4: Expected Outcomes

If the framework is correct:

| Prediction | Expected Outcome |
|:-----------|:-----------------|
| Misalignment rarity | $\mathbb{P}(r_\ell < 0.1)$ and $\mathbb{P}(r_\ell < 0.2)$ are tiny |
| Order-one defect | $\widehat{\Phi}(a) \sim \kappa_*$ (not exponentially small in $\beta$) |
| Stiffness ↔ alignment | Positive correlation between alignment and larger $\lambda_{\min}$ |
| Scale stability | Distribution of $\Delta_\ell$ remains order-one under coarse graining |

---

# Chapter 5: Maxwell Green Kernel Verification

## 5.1 Operator and Bound

Invert on periodic $L^4$ lattice:
$$
M = m^2 I + \alpha \Delta_1, \quad \Delta_1 = d_1^* d_1
$$

Verify bound:
$$
|(M^{-1})_{bb_0}| \le \frac{2}{m^2} e^{-\eta \cdot d_E(b, b_0)}
$$

## 5.2 Measured Results (L=16, m²=0.3, α=1)

```
D_E (measured) = 18
C0(Delta1) (measured) = 43.9077

Exponents:
eta_DG(D_E) = 0.1290
eta_DG(C0)  = 0.0826
eta_CT(C0)  = 0.00341

Bound verification:
[DG_DE] max_ratio = 1.412e-01 (passes)
[DG_C0] max_ratio = 1.412e-01 (passes)
[CT_C0] max_ratio = 1.412e-01 (passes)
```

**All theoretical bounds satisfied numerically.**

## 5.3 Gauge-Fixing Experiment

In Feynman gauge ($\xi = \alpha$):
```
Old C0 (curlcurl): 43.9077
New C0 (Feynman gauge): 8.0000  (= 2d = 8)
```

Row-sum constant collapses to scalar coordination number.

---

# Chapter 6: A100 GPU Workload Design

## 6.1 Target: Adversarial Search for Counterexamples

Directly test:
- **GAP-FC-02:** Does $\mathcal{B}_\Lambda \ge \epsilon_0$ force $\|\nabla S\| \ge c_0$ uniformly?
- **GAP-FC-04:** How fast does $\mu(\mathcal{B}_\Lambda \ge \epsilon_0)$ decay with volume?

## 6.2 Optimization Problem

Run many configurations in parallel (batch $B$):
$$
\min_U \|\nabla S(U)\|^2 \quad \text{subject to} \quad \mathcal{B}_\Lambda(U) \ge \epsilon_0
$$

Implemented with penalty:
$$
\min_U \|\nabla S(U)\|^2 + \lambda \cdot \text{ReLU}(\epsilon_0 - \mathcal{B}_\Lambda(U))^2
$$

## 6.3 Interpretation

- If optimizer fails to find $\|\nabla S\| \approx 0$ while keeping disorder high → evidence FOR A′
- If it finds such configurations → genuine obstruction discovered

## 6.4 Scaling

| Parameter | Small Test | A100 Scale |
|:----------|:-----------|:-----------|
| Batch | 1024 | 4096-8192 |
| L | 4-8 | 12-20 |
| Precision | float64 | float32 (mixed) |

---

# Chapter 7: Existing Numerical Results

## 7.1 Exact-Force Search (SU(2), 2D)

> Driving $\|\nabla S\|$ down forces plaquette disorder to collapse toward vacuum.
> No rough configurations with near-zero force were found.

**Supports A′ as energy-landscape fact** (not a proof).

## 7.2 GPU Measurements (SU(3), 4D Wilson)

| Observable | Measured Value |
|:-----------|:---------------|
| Cartan misalignment $r$ | mean ≈ 0.75 |
| $\mathbb{P}(r < 0.2)$ | 0 (over ~30,000 links) |
| Star Hessian $\lambda_{\min}$ | mean ≈ -2.09 |
| Mean defect $\widehat{\Phi}_{\delta K}$ | ≈ 14.09 (with $\kappa_* \approx 12$) |

**Strong qualitative match to "near-Cartan rarity + order-one defect" theory.**

---

# Chapter 8: Python Scripts Inventory

## 8.1 Available Scripts

| Script | Purpose |
|:-------|:--------|
| `code_exact_force_su2_2d.py` | Exact force search for counterexamples |
| `haar_hessian_scan_su3.py` | SU(3) Haar Hessian eigenvalue computation |
| `su2_drift_simulation.py` | Drift & Laplacian measurement (18KB) |
| `su2_a100_stress_test.py` | Adversarial "Force Proxy" Hunt (14KB) |
| `su2_globalization_experiments.py` | Global Core thresholds |
| `su3_haar_hessian_scan.py` | SU(3) Weyl/Haar Hessian eigenvalues |

## 8.2 Code Style

- PyTorch on GPU
- Quaternion representation for SU(2)
- FFT for Fourier-space inversions
- Batched parallel configurations

---

# Chapter 9: vHJ Curvature Flow Simulations

## 9.1 The vHJ-to-Hessian Pipeline

The simulations test the theoretical pipeline:
$$
\text{Heat-kernel coarsening} \to \text{vHJ equation} \to \text{Hessian flow} \to \text{Riccati curvature}
$$

## 9.2 Numerical Setup

**Source files:** `YANG3_02_vHJ_hessian_flow_riccati.md`, `02_vHJ_CurvatureFlow_Simulations_v2.md`

- SU(2)/SU(3) lattice configurations
- Compute effective action $S_t$ at multiple RG scales
- Track minimum Hessian eigenvalue $\lambda_{\min}(t)$

## 9.3 Key Observations

| Metric | Measured | Theory |
|:-------|:---------|:-------|
| Riccati decay exponent $\alpha$ | $\sim 0.00079$ | Haar-stabilized |
| Late-time $\lambda_{\min}$ | Positive | Fixed point |
| Scale stability | Confirmed | MFIP recursion |

The curvature flow stabilizes rather than blowing down, supporting the Riccati stabilization hypothesis.

---

# Chapter 10: Riccati Dynamics Numerical Verification

## 10.1 The Riccati Equation

$$
\dot{\lambda}(t) = -2\lambda(t)^2 + \sigma(t)
$$

**Fixed points** for constant $\sigma > 0$:
$$
\lambda_\pm = \pm\sqrt{\frac{\sigma}{2}}
$$

- $\lambda_+$ is **stable** (attractor)
- $\lambda_-$ is **unstable** (threshold)

## 10.2 RK4 Numerical Verification

**Constant source $\sigma = 1$:**

| $\lambda(0)$ | $\lambda(10)$ | $\lambda_* = \sqrt{1/2}$ |
|:-------------|:--------------|:-------------------------|
| -0.5 | 0.7071067812 | 0.7071067812 |
| 0 | 0.7071067812 | 0.7071067812 |
| 1 | 0.7071067812 | 0.7071067812 |
| 2 | 0.7071067812 | 0.7071067812 |

All initial conditions above $\lambda_-$ converge to $\lambda_*$.

**Oscillatory source $\sigma(t) = 1 + 0.5\sin(t)$:**

Comparison bounds predict: $0.5 \le \liminf \lambda \le \limsup \lambda \le 0.866$

Late-time observation: $\lambda(t) \in [0.5203, 0.8598]$ ✓

## 10.3 Physical Interpretation

The stable fixed point:
$$
m := \sqrt{\frac{\sigma_*}{2}}
$$

is the **infrared convexity scale** that translates into physical mass gap.

---

# Chapter 11: Plaquette Defect Density (NumPy SU(2))

## 11.1 Gauge-Invariant Diagnostic

For plaquette $U_p$:
$$
r(U_p) = \arccos\left(\frac{1}{2}\text{ReTr}(U_p)\right)
$$

Defect density = fraction of plaquettes with $r(U_p) > r_{\text{crit}}$

## 11.2 Measured Results (L=3, r_crit=1.9)

| β | acceptance | ⟨½ReTr(U_p)⟩ | defect density |
|:--|:-----------|:-------------|:---------------|
| 1.5 | 0.804 | 0.192 | 0.175 |
| 3.0 | 0.685 | 0.340 | 0.099 |
| 6.0 | 0.522 | 0.469 | 0.054 |

**Key observation:** Defect density **drops with β**, consistent with concentration in small-field regime.

## 11.3 Connection to Theory

> For sufficiently large β, the Gibbs measure spends most mass where plaquettes are close to identity.

This supports the Lyapunov drift strategy.

---

# Chapter 12: RG Intertwining Test (JAX)

## 12.1 Target: Test Assumption A3

Empirically estimate:
$$
C_{\text{RG}}^{\text{emp}} \approx \sup_{U,v} R(U,v), \quad R(U,v) := \frac{|\nabla(F_v \circ \pi)(U)|^2}{(|\nabla F_v|^2 \circ \pi)(U)}
$$

for geodesic (Karcher) averaging block-spin map $\pi$ on SU(2).

## 12.2 Expected Outcomes

In small-field regime ($\sigma = 0.02$-$0.08$):
- `mean_R` ≈ $1/N = 1/16 ≈ 0.0625$
- `max_R` stable as batch size increases

If `max_R` climbs above 0.1 at small sigma → Karcher iteration leaving normal neighborhood.

## 12.3 Stress Test

Increase σ and watch if ratio stays controlled. Blow-up indicates A3 is small-field only (need different π like decimation).

---

# Chapter 13: HOTRG and Tensor Network Simulations

## 13.1 Rank-8 Vertex Tensor Construction

For the 4D hypercubic lattice, construct rank-8 local tensors:
- 8 legs corresponding to the 8 adjacent cells
- Spin weights from representation theory
- q-deformed 6j symbols for θ-term

## 13.2 HOTRG Coarse-Graining

The project uses a simplified HOTRG surrogate:
1. Reshape rank-8 tensor to matrix $M$ of size $D^4 \times D^4$
2. SVD truncate to top $K$ singular values
3. Reshape back to rank-8
4. Track log-normalization for $\log Z(\theta)$

## 13.3 Curvature RG from HOTRG

**Source:** `01_curvature_rg_riccati_hotrg.md`

| RG Step | $\rho_k$ | $M_k$ | Status |
|:--------|:---------|:------|:-------|
| Initial | 0.5 | - | Seed |
| Step 1 | 0.48 | 0.05 | ✓ |
| Step 2 | 0.46 | 0.04 | ✓ |
| Step 3 | 0.45 | 0.03 | ✓ |

Curvature remains bounded under iterated RG, consistent with MFIP recursion.

---

# Chapter 14: Convex Core Outlier Exclusion Theorem

## 14.1 The Core Claim

In exponential coordinates $U_\ell = \exp(iagA_\ell)$:
> The Haar Jacobian induces a quadratic lower bound that dominates Wilson in the tails.

This yields:
$$
S(A) \ge \alpha \|A\|^2 - C_{\text{tot}}
$$

## 14.2 Outlier Exclusion Theorem

**Theorem:** Under Haar-dominated tail assumptions and convexity radius $R_{\text{conv}}(\beta)$:
$$
\mu_{\beta,\Lambda}(\mathcal{B}_\beta) \le |\mathcal{L}| \cdot K \cdot \exp(-\kappa R_{\text{conv}}(\beta)^2)
$$

where $\mathcal{B}_\beta = \{A : \exists \ell \text{ s.t. } \|A_\ell\| > R_{\text{conv}}(\beta)\}$.

## 14.3 Physical Interpretation

- **Finite-cutoff**, **finite-dimensional** — no continuum YM measure needed
- Upgrades convex-core idea: "nonconvexity is rare" (quantitatively)
- Hard next step: control $R_{\text{conv}}(\beta(a))$ under $a \to 0$

---

# Chapter 15: Admissibility as Structural Layer

## 15.1 Meta-Theory Seed

> **Physical admissibility is not a specific equation; it's a test suite of inequalities that a candidate model must satisfy to be deployable.**

Across project tracks:
- **Gravity:** Convexity of $\mathcal{H}(|\nabla\Phi|/a_0)$
- **Lattice gauge:** Reflection positivity + operator inequalities → spectral gap

## 15.2 ALPO Simulation Results

Direction-dependent stiffness oscillator with energy audit:

| c_load | P_load (W) | P_base (W) | P_k (W) | η_load/base |
|:-------|:-----------|:-----------|:--------|:------------|
| 0 | 0 | 0.140 | 0.101 | 0 |
| 8 | 1.53 | 1.02 | 0.70 | 1.50 |
| 16 | 1.94 | 1.27 | 0.79 | 1.52 |

**Key insight:** A "stiffness diode" is not automatically passive. $P_k > 0$ means stiffness modulation injects energy.

---

# Chapter 16: PRO12 Colab Code Architecture

## 16.1 Core Components

| Component | Purpose |
|:----------|:--------|
| Horizontal projector | Gauge-invariant physical Hessian |
| Wilson + Haar action | Finite-cutoff effective action |
| Hessian-vector products | Autodiff HVP for Lanczos |
| Lanczos eigensolver | Extremal eigenvalue extraction |

## 16.2 Diagnostics

1. **PBH/Riccati source-term test:** `pbh_source_quadratic_form`
   - Returns (min, mean, max) of $v^\top R v$ over random horizontal vectors
   - If $\ge 0$ in SAFE regime → evidence for source positivity

2. **Off-diagonal mixing proxy:** `commutator_norm_estimate`
   - Estimates $\|[H, P_{\text{loc}}]\|$
   - Small + decreasing under flow → mixing control claims verified

## 16.3 Stage Progression

| Stage | Demo | What to see |
|:------|:-----|:------------|
| 1 | `--demo linear` | λ_min ≈ κ (constant co-closed modes) |
| 2 | `--demo su2` | Nonlinear SU(2) with covariant projection |
| 3 | `--demo su3` | Full SU(3) at β=6.0 |

---

# Chapter 17: Failure Modes and Diagnostics

## 17.1 Known Failure Modes

From `SIMULATION_REVIEW_BEST_WORK_INDEX.md` Extract 5:

| Failure Mode | Detection | Cause |
|:-------------|:----------|:------|
| Blocking artifacts | Large variance ratio | Gauge-fixing boundary effects |
| Uniform covariance | Flat decay | Finite-size contamination |
| φ-Hessian mismatch | Eigenvalue disagreement | Linearization breakdown |

## 17.2 Diagnostic Protocol

1. **Variance stability check:** Compare $\mathrm{Var}(\lambda_{\min})$ across batches
2. **Decay profile verification:** Plot $\log|G_{bb'}|$ vs distance
3. **Gauge-fixing monitor:** Track Landau gauge residual

## 17.3 Recovery Strategies

- **Blocking:** Use larger margin from boundaries
- **Uniform covariance:** Increase lattice size
- **Mismatch:** Reduce field amplitude in SAFE region

---

# Chapter 18: Clean Verified Scripts Extraction

A `Clean Scripts/` directory has been created to house verified, independent simulation codes extracted from the project.

## 18.1 Verification Protocol
Each script was:
1. **Extracted** from original notes or code files
2. **Refactored** to be standalone (NumPy only)
3. **Executed** to verify theoretical predictions (e.g. fixed point stability, error scaling)
4. **Renamed** with descriptive, searchable titles

## 18.2 Verified Artifacts (6 Scripts)
| Script | Physical Test | Status |
|:-------|:--------------|:-------|
| `VERIFIED_SU2_Disorder_Force_Correlation_Test_For_Assumption_A_Prime.py` | Disorder $\neq$ Zero Force | PASS |
| `VERIFIED_Riccati_ODE_Mass_Gap_Mechanism_RK4_Integration.py` | Mass Gap Fixed Point | PASS |
| `VERIFIED_SU3_Haar_Jacobian_Hessian_Eigenvalue_Scan_Weyl_Bound.py` | Haar Convexity $\ge 0.5$ | PASS |
| `VERIFIED_SU2_Wilson_Action_Equals_Quadratic_Curl_At_Small_Field.py` | Wilson $\to$ Curl Linearization | PASS |
| `VERIFIED_Topological_Susceptibility_Chi_Top_Extraction_Fourier_Fit.py` | $\chi_{\text{top}}$ Fourier Extraction | PASS |
| `VERIFIED_SU2_4D_Metropolis_Plaquette_Defect_Density.py` | Small-Field Concentration | PASS |
| `VERIFIED_SU2_Cartan_Alignment_Score_Test.py` | Cartan Alignment Geometry | PASS |

---

# Chapter 19: Files Reviewed

| Pass | File | Key Content |
|:-----|:-----|:------------|
| 1 | `SIMULATION_REVIEW_BEST_WORK_INDEX.md` | Curated index of 6 simulation extracts |
| 1 | `05_simulation_appendix_maxwell_and_a100_su2.md` | Maxwell kernel, gauge fixing, A100 workload |
| 1 | `doc06_numerics_protocol_results.md` | Measurement protocol, expected outcomes |
| 2 | `EXTRACT_04_Riccati_Mass_Gap_Mechanism_with_Simulation.md` | Riccati dynamics + RK4 verification |
| 2 | `EXTRACT_05_Simulation_Plaquette_Defects_Numpy_SU2.md` | Plaquette defects NumPy code |
| 2 | `05_jax_a3_rg_intertwining_test.md` | JAX skeleton for A3 testing |
| 3 | `YM_extract_02_outlier_exclusion_convex_core.md` | Convex core theorem |
| 3 | `05_admissibility_layer_alpo_simulation.md` | ALPO simulation with energy audit |
| 3 | `PRO12_CODE_README.md` | Colab code architecture |
| 4 | `code_exact_force_su2_2d.py` | Exact force script (extracted) |
| 4 | `haar_hessian_scan_su3.py` | Haar Hessian scan (extracted) |
| 4 | `EXTRACT_05_Simulation_SU2_Wilson_Quadratic_Check.md` | Wilson quadratic check (extracted) |
| 4 | `04_chi_top_extraction_fourier_and_fits(1).md` | Chi-top extraction (extracted) |
| 4 | `su2_drift_simulation.py` | Large-scale drift (PyTorch, noted) |
| 4 | `su2_globalization_experiments.py` | Globalization (PyTorch, noted) |
| 4 | `07_cpu_smoke_test_a3_torch.md` | A3 smoke test (PyTorch, noted) |
