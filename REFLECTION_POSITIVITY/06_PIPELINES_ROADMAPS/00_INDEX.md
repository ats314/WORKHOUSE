# Selected notes extracted from chat + project files

This folder contains a small set of technical notes that were judged to be the most promising / structurally useful pieces in the current project materials.

## Files

1. **01_matrix_hinge_to_massive_maxwell.md**
   - Derivation chain: localized Bakry–Émery “matrix hinge” on a small-field set $K_\Lambda(r)$ and Helffer–Sjöstrand/Witten-Laplacian covariance identity, reducing correlation control to a massive Maxwell resolvent $(m^2I+\alpha d_1^*d_1)^{-1}$.

2. **02_davies_decay_massive_maxwell.md**
   - Self-contained Davies conjugation proof of exponential off-diagonal decay for $(L+m^2)^{-1}$ with exponent $\eta=2\operatorname{arsinh}(m/(2\sqrt{C_0}))$, including the boundary row-sum refinement $C_{\partial}(L)$.

3. **03_local_cancellation_SU2.md**
   - Formulation of Assumption (A') (macroscopic disorder forces a nontrivial Wilson force) and the remaining finite-dimensional geometric obstacle: ruling out cancellations among transported plaquette forces except on an exceptional “aligned Cartan” set.

4. **04_dirichlet_form_coarse_graining_Og2.md**
   - Candidate renormalization step phrased at the level of Dirichlet forms: conditional expectation coarse-graining, energy decomposition $f=Pf+(I-P)f$, and why a blockwise conditional Poincaré inequality yields an $O(g(a)^2)$ energy loss bound.  Also records an incompatibility lemma for naive gauge-covariant Markov kernels.

5. **05_exact_force_su2_2d_numerics.md**
   - Exact-force gradient-descent toy code for 2D $SU(2)$ Wilson action (script + outputs + small-seed table), used to search for rough configurations with near-zero force.

6. **06_reflection_positivity_permanence.md**
   - Abstract lemmas: reflection positivity is preserved under reflection-equivariant Markov coarse graining and under projective limits on cylinder observables.
