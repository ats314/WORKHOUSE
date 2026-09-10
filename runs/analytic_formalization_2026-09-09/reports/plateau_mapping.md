# R4-R5 plateau formalization

Fourteen theorems in `lean/Workhouse/PlateauObstruction.lean` prove the actual exponential minimization and the positive two-mode obstruction in `docs/derivations/yangmills-reconstruction.md`, section 4. The source heading is preserved exactly in the machine-readable mapping.

The minimization proves both threshold cases: an admissible logarithmic critical time with the exact R5 theta-power value, and a time-zero optimum with value A + plateau. The assembled R4-R5 bound keeps the spectral upper estimate as an explicit premise.

The obstruction constructs strictly positive weights and energies. For every positive error and fast rate, the correlation remains beneath fast exponential decay plus that error for every nonnegative time, while no finite prefactor gives the fast exponential rate. This is a proof for actual real exponentials, not a recorded numerical observation.

All fourteen theorems passed `lake env lean -DwarningAsError=true --stdin` and individual `#print axioms` checks. Every dependency is among the standard Lean axioms `propext`, `Classical.choice`, and `Quot.sound`; there are no placeholders or introduced axioms. See `plateau_axioms.log`.

These proofs are scoped support of `DERIV:YANGMILLS_RECONSTRUCTION:R4_R5`. The operator spectral representation and R1 instantiation, the E=0 spectral-measure limit, and the literal three-by-three transfer representation remain separate obligations. No source file, existing registry, or shared import was edited.

| Theorem | Scope |
| --- | --- |
| `stationary_global_minimum` | For positive A and plateau, the explicit derivative-balance equation implies global minimization of the exponential objective over all real times; no minimum is assumed. |
| `logarithmic_time_is_stationary` | For A, plateau, a, b positive, t0=log(A*a/(plateau*b))/(a+b) satisfies the exact stationary balance. |
| `admissible_logarithmic_minimum` | Under plateau*b <= A*a and positivity, the logarithmic optimum is nonnegative and minimizes the objective over nonnegative physical times. |
| `endpoint_minimum` | If A*a <= plateau*b, the constrained objective is bounded below by its attained time-zero value A+plateau. |
| `interior_minimum_value` | The exact attained logarithmic minimum equals ((a+b)/a)*plateau*(A*a/(plateau*b))^(b/(a+b)), with every positive-factor condition explicit. |
| `theta_minimum_value` | The exact R5 power formula A^theta*plateau^(1-theta)/(theta^theta*(1-theta)^(1-theta)) for positive A, plateau and 0<theta<1. |
| `bound_time_rescaling` | Exact conversion between physical time and dimensionless time for E=eta*theta and nonzero eta. |
| `physical_time_minimum_value` | The exact R5 value at physical time log(A*(1-theta)/(plateau*theta))/eta, for positive eta and 0<theta<1; time admissibility is separately proved. |
| `r4_r5_interior_optimum` | Combines the explicit threshold, nonnegative optimizer, attained R5 formula, and global minimization over every nonnegative physical time. |
| `r4_r5_optimized_upper_bound` | Given the spectral scalar upper bound for every nonnegative time as an explicit premise, the proved optimizer implies the exact R5 mass bound. Does not assert an operator spectral representation. |
| `slow_mode_fits_positive_plateau` | The actual two-exponential correlation is positive and is bounded by fast decay plus its nonnegative slow-mode weight for all nonnegative times. |
| `rescaled_correlation_identity` | Exact faster-rate rescaling of the positive two-mode correlation exposes weight*exp((fast-slow)*t)+1. |
| `positive_slow_mode_prevents_faster_bound` | Any positive slow spectral weight with slow<fast defeats every finite nonnegative faster-decay prefactor at an explicitly constructed nonnegative time. |
| `arbitrarily_small_plateau_obstruction` | For every positive plateau and positive proposed fast rate, constructs positive weight below the plateau and positive slow energy below fast; the resulting positive two-mode correlation satisfies the plateau bound for all times and defeats every faster prefactor. |
