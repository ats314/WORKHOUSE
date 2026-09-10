# Ground-state and projection formalization

The new module is `C:/WORKHOUSE/REPO/lean/Workhouse/GroundStateAssembly.lean`.
It contains **36 proved theorems**, with no `sorry` or added axioms. Its strict
individual compilation and a separate axiom audit both exited successfully.
All 36 declarations depend only on `propext`, `Classical.choice`, and `Quot.sound`.
This agent did not run the aggregate build or edit shared registries.

The machine-readable declaration/source/dependency map is
[ground_state_mapping.json](ground_state_mapping.json). The exact compiler
axiom output is [ground_state_axioms.log](ground_state_axioms.log).

## What is now formalized

1. **The actual measure-comparison argument behind VA10 and BA2.** On an
   arbitrary measurable space, a probability density satisfying
   `m <= dmu/dnu <= M` transfers a reference Poincare constant `C` to `M*C/m`.
   The proof optimizes the variance center, compares the actual Bochner
   integrals, converts the a.e. density bounds into measure inequalities,
   and derives the target square-integrability from the upper bound. This
   part is not restricted to a finite discretization. The reference
   Poincare theorem and the model's density bounds remain explicit inputs.

2. **The noncommuting projection assembly behind VA11--VA12.** A finite
   family of self-adjoint idempotents on an arbitrary real inner product
   space has energy `sum norm(Q_i x)^2` and the exact common kernel.
   Symmetric local anticommutator coefficients with row bound `kappa`
   imply `G^2 >= (1-kappa)G`. Pairwise commutativity is never assumed.

3. **The spectral implication in finite and infinite dimensions.** A
   positive bounded operator satisfying `T^2 >= delta*T` has a gap `delta`
   on its full kernel complement. The infinite-dimensional proof constructs
   `sqrt(T)` with the continuous functional calculus, proves the estimate
   on `range(T)`, then extends it by continuity through
   `closure(range(T)) = (ker(T))^perp`. It assumes neither a gap nor an
   inverse, compactness, or discrete spectrum. A direct corollary proves
   VA12's projection assembly on arbitrary complex Hilbert spaces from
   the local anticommutator and row-budget inputs. The separate finite
   theorem proves the same implication through an orthonormal eigenbasis.
   Both map explicitly to **GST-3a -> GST-3b**, with their operator scopes
   retained; the original unbounded Bochner operator requires its domain
   and unbounded spectral implementation.

4. **The physical form transfer behind VA9/VA14.** For arbitrary real
   inner product spaces and an explicit form domain, an isometric
   ground-state identification and its exact form identity transfer local
   energy floors and approximate tensorization to every admissible
   physical vector. The proof does not require an excited eigenvector.

5. **The product-minorization covariance argument in VA16/BA7 on actual
   probability measures.** The joint measure's two marginal pushforwards
   are explicit. A density floor `alpha` relative to their product gives
   `Cov(f,g)^2 <= (1-alpha)^2 Var(f) Var(g)` for every real L2 block
   observable. The proof constructs the genuine measure
   `mu - alpha*(muX product muY)`, computes its two energies, and applies
   L2 Cauchy--Schwarz. Centering is performed inside the final proof.
   Finite-distribution counterparts remain available as separate theorems.

6. **GA20's exact Gram identity.** Every finite rectangular real amplitude
   array yields a sum-of-squares quadratic form and hence a positive
   semidefinite Gram form. This formalizes the audit's mathematical
   identity, without identifying those amplitudes as Schwinger functions.

7. **IF11's nontrivial-variance comparison.** A normalized actual density
   bounded below by `m` gives `Var_mu(f) >= m Var_nu(f)`, allowing the two
   measures' means to differ. The variance-minimization proof handles that
   difference. The application to the actual Wilson marginal and the Haar
   trace value `1/4` is recorded separately from this general theorem.

## Precise remaining successors

The real SU(2) elliptic Hamiltonian, its positive ground and heat semigroup,
the actual ground-state form-domain identity, and the conditional-projection
identification still need model-specific Lean constructions. The bounded
infinite-dimensional square-to-gap and projection assembly implications are
complete. The local angle-to-anticommutator implication and concrete model
identification remain distinct inputs.

BA20--BA25a already establish the actual ground-angle and variance estimates
analytically when `k/epsilon <= 1/256000`. This module does not change that
status: their Brownian-slab/KP implementation in Lean remains work. The
large-`k/epsilon` continuation is a distinct open analytic successor named
by BA26, not a consequence of missing Lean coverage.

GST's Riemannian Bochner/domain work and its trial-state min-max residual
comparison remain separate formalization tasks. The continuous covariance
bound is complete from actual marginals and a density floor; deriving that
floor from the mixed log-ground ratio and identifying the conditional
projection angle through disintegration remain separate. GA20's specific
rank statement is also separate from the Gram positivity theorem.

## Verification

```text
lake env lean -DwarningAsError=true -o .lake/build/lib/lean/Workhouse/GroundStateAssembly.olean Workhouse/GroundStateAssembly.lean
lake env lean -DwarningAsError=true C:/WORKHOUSE/navigation/reconciliation/2026-09-09/formalization/ground_state_axioms.lean
```

Both exited `0`. The module source SHA-256 at handoff is
`4e5474836257d0ee497eace202b54144411efcb46e8125d09d029b023dc06750`.
The JSON map also pins all five source derivations by SHA-256 and lists
every theorem's direct local dependencies and source sections.
The prior 24-theorem mapping and audit are retained byte-for-byte under
`ground_extension/preserved/`, with their original paths and hashes.
