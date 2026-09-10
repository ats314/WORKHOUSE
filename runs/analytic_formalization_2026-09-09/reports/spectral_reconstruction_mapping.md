# Positive spectral measures and observable completeness

[SpectralReconstruction.lean](../../../../REPO/lean/Workhouse/SpectralReconstruction.lean) contains **22 strictly checked theorems** implementing the analytic mechanism and finite models in `docs/derivations/yangmills-reconstruction.md`, equations R1–R3 and R6–R7. The exact declaration/source/dependency map is [spectral_reconstruction_mapping.json](spectral_reconstruction_mapping.json).

The finite positive measure is on nonnegative real energies. Integrability of `exp(-t E)` is proved from its boundedness for every nonnegative time. Positivity of the actual integral gives `sigma([0,a]) <= exp(a t) C(t)`. If `C(t) <= A exp(-eta t)`, the infinite-time limit forces every `sigma([0,a])=0` for `a<eta`. Countable exhaustion then gives `sigma([0,eta))=0`. This is a measure-theoretic proof for arbitrary finite positive measures, not an atomic calibration.

The localization theorem substitutes the admissible radius `R=eta*t/(alpha+beta)` into the actual two-parameter correlation estimate and proves the resulting positive rate `eta*beta/(alpha+beta)`. It is composed with the spectral-measure exclusion theorem.

The observable-completeness step uses actual bounded continuous linear maps and a family whose linear span is dense. Given the spectral projection-norm identity and a common rate, every low-energy projection vanishes first on that family and then on the whole space. The correlation and localization prefactors may depend on the observable. The combined theorem performs the entire R6/R7-to-R1-to-projection implication.

R2 is formalized for arbitrary finite mode and time sets with complex coefficients: the actual reflection kernel equals the weighted sum of squared complex mode amplitudes and is positive semidefinite for nonnegative weights. The time convention is exact: `E=-log(r)/a`, `E>=0` for positive contraction modes, and `r^n=exp(-a*n*E)`.

R3 uses the actual complex 3-by-2 matrix. Its conjugate-transpose Gram matrix is exactly `diag(2,3)`, its Euclidean squared-norm excess is the second coordinate's squared norm, and its lower frame bound is two. The summed three-observable correlator is exactly `2*r1^n+3*r2^n`. After retaining only row `(0,1)`, the explicit nonzero vector `(1,0)` is invisible.

The remaining application work is to construct the physical Hamiltonian, its positive spectral measures and projection-norm identities, establish OS totality of the centered observables, and prove the actual uniform Yang–Mills localization estimate. Those are explicit inputs, not conclusions inferred from this interface. The optional integer-radius ceiling variant is not included.

All 22 theorems passed `lake env lean -DwarningAsError=true --stdin` and individual `#print axioms` inspection. Only `propext`, `Classical.choice` and `Quot.sound` occur; there are no `sorry` or new axiom declarations. Module SHA-256: `bf97a2b07c1ae25ea84f482d0db1b426dce88e9d5218668384ba07a039289f89`.
