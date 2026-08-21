<!-- LIVE WORKING COPY as of June 12, 2026. Canonical history: E:\YANG\ORGANIZED\PROOF_MAP.md. NOTE: does not yet reflect PROOF_13/14/15 (see theory/under_review/ — pending Alex's review). -->

# Proof Map — What's Proven, What's Open, and How It Connects

This document maps every proof result, its mathematical content, its dependencies, and its status. Use this when you need to understand what the project has actually established.

**Primary location:** `ORGANIZED/01_PROOFS/`
**Original source files:** `DELETE/originals/infrared-glenn/CLEAN/` (archived for reference)

---

## The Core Mechanism (4 key results)

These four results form the backbone of the argument. Everything else supports or extends them.

### P04 — Haar Mass Mechanism ★ THE SPARK
**Primary:** `ORGANIZED/01_PROOFS/proven/P04_haar_mass_mechanism.md`
**Original:** `DELETE/originals/infrared-glenn/CLEAN/01_PROVEN/P04_haar_mass_mechanism.md`
**Proves:** Gauge-fixing in temporal gauge creates a positive curvature floor: σ_Haar ≥ (Ng₀²a²)/6 > 0
**How:** The Haar measure on SU(N) has a log-determinant that acts as an effective potential. Its Hessian is uniformly positive definite — this is geometric, not dynamical. It comes from the gauge group structure alone.
**Dependencies:** L01 (lattice setup)
**Why it matters:** This is the "spark" — the initial positive curvature that drives everything else. Without P04, there's no source term for the Riccati equation.

### P02 — Bakry-Émery Curvature-Dimension Condition
**Primary:** `ORGANIZED/01_PROOFS/proven/P02_bakry_emery_curvature.md`
**Original:** `DELETE/originals/infrared-glenn/CLEAN/01_PROVEN/P02_bakry_emery_curvature.md`
**Proves:** If a measure has uniformly convex Hessian (∇²S ≥ ρI), then the diffusion semigroup has spectral gap ≥ ρ.
**How:** Bochner identity → Γ₂ ≥ ρΓ → CD(ρ,∞) condition → Poincaré inequality with constant 1/ρ.
**Dependencies:** None (foundational result from probability theory)
**Why it matters:** This is the bridge between geometry (curvature) and analysis (spectral gap). It converts P04's curvature floor into a mass gap.

### P06 — Riccati Hessian Flow ★ THE ENGINE
**Primary:** `ORGANIZED/01_PROOFS/proven/P06_riccati_hessian_flow.md`
**Original:** `DELETE/originals/infrared-glenn/CLEAN/01_PROVEN/P06_riccati_hessian_flow.md`
**Proves:** The ODE dλ/dt = -2λ² + σ has a globally attractive fixed point at λ* = √(σ/2) > 0 when σ > 0.
**How:** Phase plane analysis of the Riccati equation. The nonlinear damping -2λ² is eventually overcome by the positive source σ.
**Dependencies:** Requires σ > 0 (from P04 + CONJ_B)
**Why it matters:** This is the "engine" — it converts a curvature source (σ) into a measurable mass (λ* = √(σ/2)). The mass gap IS the fixed point of this ODE.

### P14 — Conditional RG Flow Stability ★ THE THEOREM
**Primary:** `ORGANIZED/01_PROOFS/proven/P14_rg_flow_stability.md`
**Original:** `DELETE/originals/infrared-glenn/CLEAN/01_PROVEN/P14_rg_flow_stability.md`
**Proves:** IF five hypotheses hold, THEN the mass gap persists under renormalization group flow.
**Status:** CONDITIONAL — 3 of 5 hypotheses proven, 2 depend on CONJ_B.

The five hypotheses:
| # | Hypothesis | Status |
|---|---|---|
| H1 | Curvature bound: \|K\| ≤ C₀g(t)² | ✅ Proven (P13) |
| H2 | Trace bound: Σ max{λᵢ,0} ≤ H_Tr | ✅ Proven (P17) |
| H3 | Anomaly positivity: σ_anom ≥ σ_A > 0 | ❌ OPEN = CONJ_B |
| H4 | Asymptotic freedom: g(t) → 0 | ✅ Standard QFT |
| H5 | Initial gap: λ_min(T₀) ≥ λ* > 0 | ✅ Proven (P03) |

---

## Supporting Lattice Results

| Proof | What it proves | Dependencies | Status |
|---|---|---|---|
| P01 | Reducible configs have zero capacity (lattice polarity) | None | SOLID |
| P03 | Transfer matrix has spectral gap at strong coupling | None | SOLID |
| P05 | Poincaré inequality from curvature (applies P02 to P04) | P02, P04 | SOLID |
| P07 | Total effective curvature σ_eff > 0 | P04, CONJ_B | CONDITIONAL |
| P08 | Charge conjugation preserves curvature | P04 | SOLID |
| P09 | Wilson Hessian is positive definite | None | SOLID |
| P10 | Log-Sobolev inequality on lattice | P02, P04, P09 | SOLID |
| P12 | Anomaly source bounds (dual formulation) | None | SOLID |
| P13 | Curvature controlled by running coupling | None | SOLID |
| P16 | Fixed point lifting lemma | None | SOLID |
| P17 | LSI for loop groups | None | SOLID |
| P18 | Gaussian polarity (reducibles have zero capacity) | None | SOLID |
| P19 | 2D SU(2) toy model | None | SOLID |
| P20 | Wilson loop bounds (confinement) | None | SOLID |

---

## Open Conjectures

### CONJ_B — Global Anomaly Source Positivity ★ THE BOTTLENECK
**Primary:** `ORGANIZED/01_PROOFS/conjectural/NOTE_HAAR_conj_b_anomaly_source.md`
**Original:** `DELETE/originals/infrared-glenn/CLEAN/02_CONJECTURAL/NOTE_HAAR_conj_b_anomaly_source.md`
**Claims:** Hessian of gauge-fixing anomaly is uniformly positive EVERYWHERE on configuration space.
**What's proven:** Local version (near identity) — YES. Global version — NO.
**Why it's hard:** Gribov horizon creates singularities; beyond it, gauge-fixing may not be well-defined.
**Impact:** If true → lattice mass gap is fully proven. If false → RG argument collapses.

### CONJ_A — Log Forest UV Control
**Claims:** Non-perturbative UV control of effective action in continuum limit.
**Status:** OPEN. No progress beyond perturbative arguments.

### CONJ_C — Continuum Polarity
**Claims:** Reducible connections remain negligible (zero capacity) in continuum.
**Status:** Lattice version proven (P01); continuum transfer open.

### CONJ_D — Spectral-to-Physical Mass
**Claims:** Euclidean spectral gap = Hamiltonian mass gap via OS reconstruction.
**Status:** OPEN. Template exists but technical details incomplete.

### CONJ_IR — IR Boundary Conditions
**Claims:** Infrared boundary conditions don't destroy the gap.
**Status:** OPEN.

---

## Numerical Evidence

### E04 — Curvature-Mass Proportionality ★ KEY RESULT
**Primary:** `ORGANIZED/01_PROOFS/evidence/E04_curvature_mass_proportionality.md`
**Original:** `DELETE/originals/infrared-glenn/CLEAN/03_EVIDENCE/E04_curvature_mass_proportionality.md`
**Data:** SU(3) lattice, β ∈ [5.7, 6.1]
**Result:** m_lat = 0.962 × μ_eff, R² = 0.998
**Meaning:** The lattice mass gap tracks geometric curvature almost perfectly — strong evidence the mechanism is real.
**Caveat:** Finite lattice only. Does NOT prove continuum limit or rule out lattice artifacts.

---

## What Would Complete the Proof

1. **Prove CONJ_B globally** — rigorous argument around/beyond Gribov horizon
2. **Prove CONJ_C** — capacity transfer from lattice to continuum measure
3. **Prove CONJ_D** — Osterwalder-Schrader reconstruction preserving the gap
4. Formalize in Lean or publish in peer-reviewed journal
