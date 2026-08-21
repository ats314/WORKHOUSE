# Curated Highlights — Yang–Mills Mass-Gap Project (January 2026 snapshot)

This curated set pulls out the **most novel / high-potential** components from the project files and rewrites them in a form that is:
- mathematically checkable,
- explicit about what is proven vs conjectural,
- and immediately useful for expert review.

## What this set is (and is not)

- **Not**: a finished Clay-proof of the 4D SU(3) Yang–Mills mass gap.
- **Yes**: a bundle of (i) rigorous finite-dimensional derivations, (ii) promising analytic lemmas, and (iii) simulation-backed phenomena that can plausibly be upgraded into *validated numerics* and then into publishable theorems.

## Contents (recommended reading order)

1. **vHJ Hessian flow + Riccati structure (rigorous in finite dimensions)**  
   `01_vhj_hessian_flow_riccati.md`

2. **Polarity/capacity of reducible strata (Gaussian reference + transfer lemma)**  
   `02_polarity_reducible_strata.md`

3. **q–6j classical limit with explicit error budget (small θ regime)**  
   `03_q6j_classical_limit_error_bounds.md`

4. **q-Racah Doob transform “mass-gap machine” (toy spectral lab)**  
   `04_qracah_doob_gap_lab.md`

5. **How to upgrade simulations into *rigorous* numerics (validated eigenvalue bounds, etc.)**  
   `05_rigorous_numerics_upgrade_plan.md`

6. **Conjectures and target lemmas (every overclaim rewritten honestly)**  
   `06_conjectures_target_lemmas.md`

7. **Candidate: uniform Wilson Hessian bound with HS-norm contraction tricks (promising!)**  
   `07_uniform_wilson_hessian_bound_candidate.md`

## The “big picture” idea tying the set together

A working meta-theory appears repeatedly across independent subprojects:

> **Coarse-graining tends to flatten curvature (a Riccati-like drain), but geometry/anomaly can inject a positive curvature source, producing a stable positive curvature floor.**

- In the **finite-dimensional vHJ model**, this statement is literally encoded in the Hessian PDE:  
  diffusion + transport + **(−2H²)** + source.
- In the **Haar Jacobian expansion**, group geometry produces a **mass-like quadratic term** near the identity in exponential coordinates.
- In the **q-Racah/Doob** toy lab, a ground-state transform turns a Hamiltonian into a Markov generator where the spectral gap is robust in a “safe” region.
- In the **polarity** work, the annoying reducible/Gribov-like strata become *capacity-zero* for Gaussian diffusions, suggesting they can be ignored for functional inequalities.

If a reviewer only reads one file: start with `01` and `07`.

