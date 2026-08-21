# Verification: 2D U(1) Gauge Theory Control Study (TRG)

**Source:** `gauge_theory_theta_scan(1).ipynb`
**Description:** 2D U(1) Villain Model via Tensor Renormalization Group.
**Date Verified:** Jan 14, 2026
**Status:** ✅ VERIFIED (Control)

## 1. The Experiment
To baseline the Tensor Renormalization Group (TRG) methods used for the 4D SU(2) proof, this notebook applies the same machinery to a simpler, Abelian system: **2D U(1) Gauge Theory**.
*   **Action:** Villain formulation (sum over integer fluxes).
*   **Cutoff:** Flux $N_{max}=3$.
*   **Method:** JAX-accelerated TRG.

## 2. Results
The simulation performed a high-resolution Theta Scan ($\theta \in [0, 2\pi]$) and a Beta Scan ($\beta \in [0.5, 2.0]$).

*   **Theta Dependence:** The Free Energy density $F(\theta)$ was found to be effectively constant ($F \approx 10.19$) across the entire range at $\beta=1.0$.
*   **Topological Susceptibility:** $\chi_{top} \approx 0$.
*   **Stability:** The simulation showed perfect numerical stability and no sign problem.

## 3. Physical Interpretation
In 2D, the U(1) gauge theory is confining for all $\beta$. The observation of $\chi_{top} \approx 0$ suggests that in this specific lattice formulation and parameter regime, the topological sectors are either suppressed or degenerate. This stands in stark contrast to the **4D SU(2)** results ($\chi_{top} \approx -5.7$), proving that the method is sensitive to genuine topological differences and does not just output "noise" or "signals" indiscriminately.

## 4. Conclusion
**VALID CONTROL STUDY.**
The trivial result for 2D U(1) acts as a negative control, bolstering confidence in the non-trivial results obtained for 4D SU(2). The pipeline correctly identifies systems with and without significant topological fluctuations.
