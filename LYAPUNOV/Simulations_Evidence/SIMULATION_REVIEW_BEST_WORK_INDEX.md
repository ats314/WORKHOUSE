# Simulation Review: Best Work Extracts (Dec 2–20, 2025)

This folder contains a curated set of **Markdown + LaTeX** notes distilled from the project’s December 2–20, 2025 simulation runs.

These are chosen because they either:

- behave like **computational proofs** (identity-level, machine-precision consistency), or
- create **reusable harnesses** that make “physics vs diagnostic” separable, or
- reveal a **potentially general structure** (e.g., the same constant appearing in different theorems), or
- are a **toy-model pillar** that is mathematically explicit and can be scaled / stress-tested.

## Contents

1. **Determinant Reduction Theorem & Stress Suite**  
   File: `01_determinant_reduction_theorem.md`  
   Focus: algebraic reduction identity + exhaustive stress checks + GPU speedups.

2. **Discrete de Rham / Topology Checks + Projection Harness**  
   File: `02_discrete_derham_and_projection_harness.md`  
   Focus: cochain complex identities, Betti numbers, and gauge/harmonic projection as a spectral “unit test.”

3. **Maxwell / C₀ / DG Decay Bounds + κ Plateau Extraction**  
   File: `03_maxwell_C0_decay_and_kappa_plateau.md`  
   Focus: constants \(C_0\), \(D_E\), decay inequalities, and the prefactor-correct κ estimator.

4. **Lyapunov Drift Fits, Convexity Scans, and Constant Linking**  
   File: `04_drift_convexity_and_constant_linking.md`  
   Focus: drift inequality checks, β/scale convexity collapse, and the \(b \sim C_0\) “numerical rhyme.”

5. **Failure Modes That Are Probably *Not* Physics**  
   File: `05_failure_modes_blocking_covariance_phi.md`  
   Focus: blocking making curvature worse, uniform-covariance coarse graining, and the φ-Hessian factor mismatch.

6. **q‑Racah / Doob / Gap Toy Pillar (Speculative but Structured)**  
   File: `06_qracah_doob_toy_gap_pillar.md`  
   Focus: an explicitly diagonalizable toy mass-gap machine + “safe region” scans.

## How to read

These notes are written to be:

- **copyable into a paper draft**, and
- **actionable as a runbook**: for each claim, you’ll find the minimal reproducible measurement and the diagnostic that separates real failure from an estimator bug.

---

*Note:* Some items included are explicitly labeled **speculative**: they are included because the structure is promising, not because the final theorem is proven.
