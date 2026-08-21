# SOURCE_TRACKER — Synthesis 16: Combes-Thomas Decay

## Overview
Tracking files reviewed and findings for Topic 16 synthesis (Combes-Thomas Bounds & Green's Function Decay).

---

## Pass 1 (Overview & Core Bounds)

### Files Reviewed
1. `COMBES_THOMAS_BOUNDS/05_Combes_Thomas_Exponential_Decay.md`
2. `COMBES_THOMAS_BOUNDS/03_combes_thomas_inverse_decay.md`
3. `MAXWELL_GREEN/02_davies_combes_thomas_maxwell.md`

### Key Findings
- **Combes-Thomas Estimate:** $ \|\delta_{x} (H^{-1}) \delta_{y} \| \le \frac{2}{m^2} e^{-\mu |x-y|} $
- **Decay Rate:** $\mu_{CT} = \frac{1}{R} \log(1 + \frac{m^2}{K})$ where $K$ is operator norm.
- **Davies Improvement:** $\mu_{Dav} \sim m$ (linear in mass) vs $\mu_{CT} \sim m^2$ (quadratic) for small $m$.
- **YM Application:** $H = m^2 + t d^*d$. Mass $m$ comes from Haar measure/curvature.

### Chapters Added
- Chapter 1: The Combes-Thomas Decay Theorem
- Chapter 2: The Massive Maxwell Operator
- Chapter 3: Comparison with Davies Method

---

## Pass 2 (Davies-Maxwell & Green's Functions)

### Files Reviewed
1. `MAXWELL_GREEN/01_Davies_Maxwell_Green_Decay.md`
2. `MAXWELL_GREEN/03_maxwell_C0_decay_and_kappa_plateau.md`
3. `MAXWELL_GREEN/24_Davies_Resolvent_Decay.md`

### Key Findings
- **Davies Rate:** $\eta_{DG} = 2 \operatorname{arsinh}\left(\frac{m}{2\sqrt{\alpha C_0}}\right)$.
- **Linear Scaling:** For small $m$, $\eta_{DG} \sim m / \sqrt{\alpha C_0}$, recovering the physical Yukawa mass.
- **Row Sum Constant:** $C_0 \approx 43.9077$ (measured on L=16 lattice).
- **Plateau Method:** Extracting $\kappa$ requires prefactor correction $r^{-(d-1)/2}$.

### Chapters Added
- Chapter 4: The Davies Conjugation Estimator
- Chapter 5: Numerical Constants and Decay Verification
- Chapter 6: The $\kappa$-Plateau Method

---

## Pass 3 (Helffer-Sjostrand Covariance)

### Files Reviewed
1. `OS_REFLECTION_POSITIVITY/HELFFER_SJOSTRAND/C_Helffer_Sjostrand_and_Greens_decay.md`
2. `OS_REFLECTION_POSITIVITY/HELFFER_SJOSTRAND/02_helffer_sjostrand_matrix_covariance.md`

### Key Findings
- **Covariance Identity:** $\mathrm{Cov}(F,G) = \int \langle \nabla F, (\mathcal{L}^{(1)})^{-1} \nabla G \rangle d\nu$.
- **Reduction:** $(\mathcal{L}^{(1)})^{-1} \preceq M^{-1}$.
- **No Scalarization:** Matrix inverse preserves sparse geometric structure.

### Chapters Added
- Chapter 7: The Helffer-Sjostrand Covariance Formula
- Chapter 8: From Curvature to Correlation Decay

---

## Pass 4 (RAG Enhancement)

### Queries Planned
- "magnetic field bounds"
- "diamagnetic inequality"

### Files Reviewed
*Pending...*
