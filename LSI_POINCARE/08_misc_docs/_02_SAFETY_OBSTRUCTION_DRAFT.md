> **Status:** Iterative Working Draft (Cycle 1).
> **Context:** This document focuses on the "Obstruction" principles found in `04_phi_obstruction` and `doc03_star_hessian`.

# The Obstruction & Safety Diagnostic (Draft)

## 1. The "Phi" Defect ($\Phi$)
We define a quantitative measure of "Non-Gaussianity":
\[
\Phi(a) := \mathbb{E}_{\mu} [ (\kappa_* - \lambda_{\min}(\mathcal{H}_{\text{phys}}))_+ ]
\]
- If $\Phi(a) = 0$, the theory is locally stiff everywhere $\to$ Gaussian Fixed Point.
- If $\Phi(a) > 0$, the theory has "soft spots" (Cartan Misalignment) $\to$ Interacting Theory.

## 2. Exact Star-Level Hessian
We prove that the loss of stiffness comes strictly from **Rank-1 Defects** associated with plaquette fluxes.
\[
H_{\text{star}} \approx \kappa_* I - \sum_p c_p (X_p \otimes X_p)
\]
Stiffness is lost only when defects $X_p$ span the physical space (Cartan Misalignment).

## 3. The Exceptional Set ($\mathcal{E}$)
The configurations where stiffness is lost form a closed set $\mathcal{E}$ (The "Bad Set").
- **Geometry:** $\mathcal{E}$ corresponds to specific Cartan-subalgebra alignments.
- **Measure:** We prove $\mathcal{E}$ has **zero capacity** (Polarity) for the Dirichlet form.
- **Implication:** The diffusion almost never hits the singular set; we can perform analysis on the "Punctured" space.

## 4. A100 Stress Test Verification
Our simulations (`su2_a100_stress_test.py`) hunt for these "soft spots".
- **Result:** Soft spots exist but are rare and correlated with high-energy / non-Cartan configurations.
- **Conclusion:** The average curvature remains positive even if worst-case is negative.
