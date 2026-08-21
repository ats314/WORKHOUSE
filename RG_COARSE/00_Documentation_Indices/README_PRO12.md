# PRO12 Extracted Notes: Curvature–LSI–Mass Gap Program

**Build date:** 2025-12-29

This file set distills the most *potentially generative* derivations in the project into self-contained Markdown+LaTeX notes.

## What I treated as “high potential”
The project’s core “engine” is a chain that tries to turn **geometric convexity/curvature** into a **log-Sobolev inequality (LSI)**, then into a **spectral gap**, then into a **Yang–Mills mass gap**, while carefully keeping **gauge invariance** and **reflection positivity** on the physical sector.

The documents below are written to be readable *independently*, but they form a pipeline:

1. **PBH / Riccati geometric mechanism** (how a uniform curvature floor might be produced and RG-stabilized).
2. **UV control + Mosco convergence** (how to pass functional inequalities and curvature bounds to the continuum).
3. **IR/topology decoupling + polarity** (why global slow/topological modes and singular strata do not kill the local gap).
4. **OS reconstruction on the physical sector** (how to extract a Hamiltonian and interpret exponential decay as a particle mass).

## Files and reading order

1. `DOC_01_LSI_to_OS_MassGap.md`  
   **LSI ⇒ exponential decay ⇒ OS reconstruction ⇒ Hamiltonian mass gap** (physical-sector careful).

2. `DOC_02_LSI_Gribov_FP_GaugeIndependence.md`  
   **How (uniform) convexity / LSI is used to justify gauge-fixing and avoid Gribov issues** (as a working mechanism).

3. `DOC_03_PBH_Riccati_Geometric_Machine.md`  
   **Perelman–Bakry–Hessian (PBH) flow** and the **Riccati lower bound** as a curvature-to-gap stabilizer.

4. `DOC_04_Mosco_Curvature_Stability.md`  
   **Mosco convergence** + **stability of Bakry–Émery/CD(ρ,∞)** ⇒ lifting LSI and spectral gaps to the continuum.

5. `DOC_05_IR_Decoupling_and_Polarity.md`  
   **Exact locality ⇒ IR/topology decoupling**, plus **polarity (capacity zero)** for reducible/singular strata.

6. `DOC_06_Curvature_Mass_Fit.md`  
   A tiny **numerical sanity check**: `m_lat ≈ k μ` with `R^2 ≈ 0.998`, and a reproduction script.

## Two “make-or-break” items for next work
1. **Uniform lattice LSI (H1):** either prove it, or replace it by a weaker condition that is provable and still implies a gap.
2. **Scaling / beta function:** demonstrate that the curvature scale produced by the mechanism matches asymptotic freedom scaling (not just “some log”).

