# Project Highlights (Extracted)

This file set extracts only the parts of the project that look **structurally novel** or **high-leverage** (either genuinely new, or a nonstandard assembly of standard components that could be pushed into something publishable).

## Documents

1. **Curvature-based mass-gap pipeline (lattice YM)**
   - **File:** `01_Curvature_Based_MassGap_Pipeline.md`
   - **Content:** A coherent analytic pipeline linking:
     - Haar Jacobian in exponential coordinates as a local “curvature source”
     - Polarity/capacity removal of reducible strata
     - Hessian-flow / Riccati control for curvature under smoothing (RG surrogate)
     - Functional inequalities → spectral gap → (template) clustering

2. **vHJ curvature-flow simulations**
   - **File:** `02_vHJ_CurvatureFlow_Simulations.md`
   - **Content:** Reproducible JAX code + the observed Riccati-type decay law for curvature/eigenvalues in 4D toy models.

3. **SU(3) lattice Hessian convexity experiment (Lanczos/HVP)**
   - **File:** `03_SU3_Lattice_Hessian_Convexity_Lanczos.md`
   - **Content:** JAX prototype that estimates the smallest Hessian eigenvalue for a lattice action using Hessian–vector products and Lanczos, plus example outputs.

4. **q-Racah Doob-transform “mass-gap” toy model**
   - **File:** `04_qRacah_Doob_MassGap_Toy.md`
   - **Content:** Exact finite-state Markov generators built from q-Racah Jacobi matrices; a clean definition of a “gap” and a numerical scaling exponent near \(q\to 1^-\). Includes reproducible Python.

5. **q–6j classical-limit error budget**
   - **File:** `05_q6j_Error_Budget.md`
   - **Content:** Explicit small-\(\theta\) expansions for q-integers and q-factorials and a propagated (conditional) error bound for q–6j symbols; includes a small numerical verification for the q-integer/factorial bounds.

---

## Notes on what is *not* included

Large volumes of standard background (e.g., full treatments of Poincaré/LSI theory, generic lattice YM reviews) are not replicated unless they are necessary to make the extracted material self-contained.
