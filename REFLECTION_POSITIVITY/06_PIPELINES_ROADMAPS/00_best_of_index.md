# Best-of package index: curvature → LSI → gap (and the places it can fail)

*Generated 2025-12-29.*

This folder is a **curated extraction** of the parts of the project that look
most promising as *a real program* (not just a hopeful collage):

> **Nonperturbative mass gap from geometry + functional inequalities**, bootstrapped across RG and pushed to the continuum.

It’s a wild idea — but it has a crisp spine:
\[
\text{(local Bakry–Émery curvature)}\;\Rightarrow\;\text{LSI}\Rightarrow\;\text{diffusion gap}
\Rightarrow\;\text{OS Hamiltonian gap}.
\]

The interesting novelty here is not any single theorem (most ingredients are classical),
but the **way the project tries to glue them** in a gauge theory setting.

---

## Reading order (recommended)

### A. The SAFE-region certificate (local convexity)

1. `From Local to Global LSI with Drift and TIghten the LSI Spectral Gap Chain.txt`  
   Contains the headline numerical claim (min physical eigenvalue $\approx 0.248$) and the SAFE constants $(\kappa_*,\delta,\alpha)$.

2. `01_geometric_curvature_mass_safe.md`  
   Cleaned explanation of the SAFE curvature mechanism and why Haar geometry matters.

3. `H_phys_spec.md` + `h_phys_tools.py`  
   **Code-level definition** of the “physical Hessian” operator $H_{\mathrm{phys}}$ (cluster + gauge projector + Schur complement route).

4. `07_safe_scan_repro_v2.md` + `safe_scan_tracked_v2.py`  
   Reproducible Haar-only scan and a clear statement of what must be added to reproduce the full table.

---

### B. Getting from “local convexity” to “global LSI” (the hard bridge)

5. `08_drift_return_safe.md`  
   Drift/return-to-SAFE is one plausible approach, but it’s fragile in gauge settings.

6. `02_rg_stable_lsi_gap_drift.md`  
   A broader map of bridge options, including high-temperature Dobrushin/Zegarlinski routes when drift is too hard.

---

### C. RG and marginalization (keeping curvature when you integrate out modes)

7. `09_rg_schur_complement_curvature.md`  
   The explicit Schur-complement / marginalization lemma: *integrating out fast modes does not destroy strong convexity* under clean hypotheses.

---

### D. “Geometric Hessian flows” and UV control (the exotic ingredient)

8. `03_pbh_hessian_flow_uv_log_forest.md`  
   PBH-type projected flow + Riccati comparison gives a route to *re-amplify curvature*.

(Underlying project notes also exist: see `PROOF_07_UV_Log_Forest_Control.md` and `PROOF_11_Infinite_Curvature_Flow.md`.)

---

### E. Continuum and OS reconstruction (turn diffusion gap into mass gap)

9. `04_mosco_convergence_curvature_lifting.md`  
   Mosco convergence + stability of functional inequalities in the continuum limit.

10. `05_os_reconstruction_mass_gap_bridge.md`  
   How a uniform diffusion/spectral gap yields an OS Hamiltonian mass gap.

(Underlying project proofs: `PROOF_10_Mosco_Convergence.md`, `PROOF_12_OS_Reconstruction.md`.)

---

### F. Evidence and falsifiability

11. `06_evidence_curvature_mass_fit.md` + `curvature_mass_fit.py` + `curvature_mass_fit.png`  
   The eyebrow-raising $R^2\approx 0.998$ curvature–mass fit (currently 5 points).

12. `10_fit_stress_test_v2.md` + `fit_stress_test.py`  
   How to stress-test that fit responsibly (more $\beta$, error bars, other groups/channels).

---

### G. Making “Haar geometry is really there” rigorous

13. `11_haar_gauge_fixing_rigorous.md`  
   A cleaned argument that gauge fixing + FP determinants can genuinely induce Haar-type geometry on the reduced variables.

(Underlying project proof: `PROOF_03_Haar_Measure_Anomaly.md`.)

---

## Why this selection

These pieces are the ones that:

- make **quantitative claims** you can reproduce or falsify,
- introduce **nontrivial glue** between fields (geometry ⇄ probability ⇄ lattice gauge theory ⇄ QFT reconstruction),
- and have clear “next theorem” targets.

Everything else in the repository is either auxiliary, incomplete, or currently downstream of these bottlenecks.

