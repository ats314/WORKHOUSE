# Yang–Mills “Salvage Stack”: Master Index (Markdown+LaTeX)

This folder is a curated, *publishable-leaning* extraction of the project’s strongest components: proofs/derivations that are rigorous in finite dimension, plus computational confirmations that expose what still needs to be proven for Yang–Mills.

## Reading order (fastest path to the core idea)

1. **01_curvature_to_gap_framework.md**  
   Curvature (Bakry–Émery) → LSI/Poincaré → exponential mixing/clustering → Osterwalder–Schrader (OS) mass gap. The “if–then” theorem pipeline.

2. **02_hessian_flow_vHJ_riccati.md**  
   The coarse-graining semigroup model: vHJ equation, Hessian evolution, and the Riccati mechanism that explains why curvature tends to decay unless a positive source arrests it.

3. **03_haar_mass_term.md**  
   The *geometric* seed: the Haar Jacobian in exponential coordinates yields a strictly positive quadratic term (local mass-like curvature), with explicit Lie-algebra tracing.

4. **04_polarity_reducibles.md**  
   Removes a standard obstruction: reducible strata are polar (capacity zero) for the relevant Dirichlet forms, so functional inequalities are insensitive to them.

5. **05_su3_wilson_haar_hessian_numerics.md**  
   The computational confirmation: a JAX “Turbo SU(3) convexity engine” estimating the smallest Hessian eigenvalue via Hessian-vector products + Lanczos; multi-volume convexity window maps.

6. **06_q_racah_doob_and_transfer_operator.md**  
   A separate “spectral laboratory”: q-Racah Jacobi matrices → Doob transform → Markov generator gap; plus a composite transfer operator that tracks the gap.

7. **07_q6j_error_bound.md**  
   q-deformed 6j classical limit with an explicit small-\(\theta\) error bound, plus the numerical scan harness.

8. **08_open_problems_and_next_proofs.md**  
   What is *actually missing* for a Yang–Mills mass-gap theorem, phrased as concrete lemmas/conjectures with measurable targets.

## One-sentence unification

> The project builds a *curvature-stabilized* route to mass gaps: if you can keep a Bakry–Émery curvature lower bound alive under coarse-graining (vHJ/Hessian flow), then LSI + spectral gap + clustering + OS reconstruction give a Hamiltonian gap; the Haar measure provides a natural curvature “seed,” and numerics map when the SU(3) Wilson+Haar lattice action is locally convex.

