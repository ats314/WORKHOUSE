# Recommended Core Roadmap Version 2

This is the “recommended subset” of the project, updated to include three items that were previously only listed as *next steps*:

1) a localization-to-global-gap theorem template,  
2) a concrete entropic-spark experiment protocol,  
3) a plan for sharpening the Wilson mixed-derivative bound.

Nothing here claims a solution of the 4D **continuum** Yang–Mills mass gap. What *is* here is a coherent mechanism stack:

\[
\textbf{Spark} \;\Longrightarrow\; \textbf{Flow} \;\Longrightarrow\; \textbf{Gap},
\]
plus an explicit “obstruction → localization” workaround.

---

## The recommended bundle read in this order

1. **RECOMMENDED_01_Finite_Cutoff_Haar_Wilson_Windows_v2.md**  
   Finite-cutoff convexity window from Haar vs Wilson curvature; clean constants; why it dies in the continuum; why the mixed-term constant \(24/N\) appears.

2. **RECOMMENDED_02_Global_BE_Obstruction_and_Localization_v2.md**  
   The global Bakry–Émery obstruction (why the naive global curvature constant must go to \(-\infty\) as \(\beta\to\infty\)), and why you should localize.

3. **RECOMMENDED_06_Localization_Theorem_Template.md**  
   Turns “localize” into a theorem-shaped template:
   local Poincaré/LSI on a core \(K_a\) + exit-time / Dirichlet-capacity control on \(K_a^c\) ⇒ global spectral gap.

4. **RECOMMENDED_03_Block_Convexity_Engine_v2.md**  
   The portable “Flow” mechanism: Schur complement + Brascamp–Lieb = quantitative convexity propagation under coarse graining.

5. **RECOMMENDED_08_Wilson_Mixed_Derivative_Sharpening.md**  
   A targeted note on the key constant in Flow: how to improve \(\|B\|_{\mathrm{op}}\) beyond the safe \(24/N\), especially on typical sets or with better coarse variables.

6. **RECOMMENDED_05_Riccati_Flow_Anomaly_Sustainer_v2.md**  
   The Hessian flow / Riccati equation picture: how convexity can decay and what kind of positive “source term” would sustain it.

7. **RECOMMENDED_04_Entropic_Gribov_Spark_Conjecture_v2.md**  
   The candidate continuum Spark: Gribov/FMR geometry induces an IR quadratic well for coarse modes (“entropic Spark”).

8. **RECOMMENDED_07_Entropic_Spark_Experiment_Protocol.md**  
   A concrete numerical protocol to test the entropic Spark on small lattices (gauge-fixing proxy + low-mode marginal + estimate \(\nabla^2 V_{\mathrm{eff}}(0)\)).

9. **RECOMMENDED_09_3D_Compact_QED_Worked_Example.md**  
   A worked sanity anchor: in compact QED\(_3\), monopoles provide a real nonperturbative Spark that feeds the same Spark–Flow–Gap pipeline.

---

## What this bundle achieves

- A rigorous **finite-cutoff** convexity window (useful as an anchor regime).
- A clean statement of the **continuum obstruction** for global curvature methods.
- A **localization toolkit** that turns the obstruction into an actionable two-part target.
- A reusable “Flow” inequality that reduces RG stability to bounding a single mixed block.
- A concrete **Spark candidate** (entropic Gribov) plus a practical experiment to pressure-test it.
- A toy model where Spark–Flow–Gap aligns with known mass generation (compact QED\(_3\)).

---

## The three “needle movers” now upgraded to recommended notes

- **Localization theorem template:** RECOMMENDED_06  
- **Entropic spark experiment:** RECOMMENDED_07  
- **Wilson mixed-derivative sharpening:** RECOMMENDED_08

These are the most direct ways the project can become either (i) falsifiable or (ii) provable.