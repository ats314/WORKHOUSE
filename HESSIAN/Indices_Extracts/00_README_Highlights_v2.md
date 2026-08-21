# Project Highlights (Second-Pass Extract)

This file set contains **only the material that looked structurally reusable** (or potentially novel-in-assembly) after a second pass through:

- the project notes/appendices in `/mnt/data/`
- the Colab/PDF exports capturing the numerical experiments

Everything here is **finite-volume / finite-dimensional** unless explicitly marked otherwise.

## Documents (download these)

1. **Curvature-based mass-gap pipeline (analytic skeleton)**
   - File: `01_Curvature_Based_MassGap_Pipeline.md`
   - What changed in this second pass:
     - corrected the viscous Hamilton–Jacobi (vHJ) semigroup identity (removed the erroneous `+J_t` self-canceling term)
     - separated the **exact vHJ identity** from the **optional “source/anomaly” term** used as a modeling knob

2. **vHJ curvature-flow simulations (JAX)**
   - File: `02_vHJ_CurvatureFlow_Simulations.md`
   - What changed in this second pass:
     - corrected the PDE and the update step in the code blocks
     - reorganized the simulation results as “curvature spectra + Riccati fits” (quadratic / Haar / YM-quartic / SU(2) / SU(3))

3. **SU(3) lattice Hessian convexity mapping (JAX + HVP + Lanczos)**
   - File: `03_SU3_Lattice_Hessian_Convexity_Lanczos.md`
   - Status: kept essentially as-is (it was already internally consistent); added a couple of warnings about gauge/coordinate artifacts.

4. **q-Racah Doob-transform mass-gap toy model**
   - File: `04_qRacah_Doob_MassGap_Toy.md`
   - What changed in this second pass:
     - matched the code interface to the Colab exports (Doob transform return values, safety checks)
     - added the “flow classification” harness and a concrete composite transfer-operator implementation

5. **q–6j classical-limit error budget**
   - File: `05_q6j_Error_Budget.md`
   - What changed in this second pass:
     - aligned the amplitude-scaling discussion with Appendix E’s caveat (scaling depends on conventions; only a negative power is needed)

## What is intentionally *not* included

- Broad background on Bakry–Émery/LSI/PI beyond what is needed to state the pipeline cleanly.
- Any “continuum Yang–Mills mass gap proved” claims. (They are not supported by the current corpus.)
- Large conversational fragments that do not feed a derivation, a definition, or a reproducible numeric.

