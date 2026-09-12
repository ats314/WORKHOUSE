# Local SU(N) class spectra: exact continuation

This standalone campaign develops the archived one-plaquette weak-well results.
The selected input is the traceless Gaussian covariance and the Wilson cosine
potential, in the conventions of `ENGINE_SUN_codd_local_gap_exact.py`.

The construction uses the lowering operator D=Delta/2 and its terminating
exponential to resolve Gaussian oscillator shells in Q(N). It avoids rank-by-rank
interpolation and singular Gram matrices at small rank. The next calculation
recovers both parity sectors through beta^-1 and attempts the following order.

Status: calculation and proof under development. `wick_gap.py` checks the full
polynomial eigen-equation coefficient by coefficient, including normalization
and the vanishing resonant-shell obstruction.

The finite formal oscillator computation does not alone bound the remainder of
the compact-group eigenvalues, control interacting plaquettes or remove a cutoff.
The source archive and canonical scientific checkout remain unchanged.
