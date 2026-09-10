# Resolvent, Schur and infinite-lattice formalization

`C:\WORKHOUSE\REPO\lean\Workhouse\ResolventLocalization.lean` adds **28 checked theorems**. The final strict compiler run, followed by `#print axioms` for every theorem, succeeded. No theorem uses `sorry` or a new axiom. The ring resolvent identity uses no axioms; the others use only `propext`, `Classical.choice` and `Quot.sound`.

The complete declaration-to-source mapping and local/mathlib dependencies are in [resolvent_mapping.json](resolvent_mapping.json). Each theorem's source comments also carry the equation or section identifier.

## Mathematical progress

- **Background BF1:** an infinite Neumann series constructs the inverse of `1+C` in any unital Banach algebra. Its left and right inverse laws, norm bound and inverse-difference bound are proved. The actual real Hilbert-space pairing is controlled by `theta/(1-theta)`. Conjugating by a symmetric inverse-square-root realization gives the weighted source-coordinate estimate.
- **BF1 / spatial SP7–SP9 inverse remainder:** the actual inverse satisfies `R=1-C+C²-C³R`, and the operator norm of its quadratic approximation error is at most `norm(C)³/(1-norm(C))`. Arbitrary bounded left/right source maps retain this cubic bound with their norm factors. The corresponding Hilbert-space selected pairing is also proved.
- **Spatial SP3–SP4 / selected W4 / background BF3:** actual Hilbert-space square completion proves the graph correction `-R v` attains the Schur value. Positivity proves global minimization. In the normalized small symmetric perturbation case, inverse existence, coercivity and uniqueness are derived from the norm bound.
- **Resolvent localization, section 2.1:** the noncommutative second-resolvent identity and its signed Hilbert pairing are proved with explicit inverse and symmetry hypotheses.
- **Resolvent localization, section 2.3:** summable envelopes imply absolute convergence of the actual infinite double kernel pairing. Every finite subvolume obeys the same majorant. The integer geometric series and its product on every finite-dimensional integer lattice have the exact stated sum. The conditional localization corollary is an infinite-dimensional theorem, not a finite lattice test.

## Source correction retained

The submitted localization proposal omits a source-support factor when bounding a nonsingleton compact support by its supremum norm. `finite_source_propagation` proves the correct bound using its full l1 mass. For a singleton the expressions agree. The original source remains unchanged.

The proposal's audit also rejects identifying its massive surrogate with the actual Wilson operator, setting the previously defined scalar frustration to zero, and deriving a uniform physical gap merely from ground conjugation. This module does not revive those claims.

## Remaining formalization obligations

These proofs cover bounded normalized operators on real Hilbert spaces. To transfer them to the full source statements still requires the closed unbounded form realization, compatible common domains and form-dual cross-functional extensions. The sharp two-sided order bound SP5, energy derivative and induced source metric SP6, assembly of the full W5/SP9 remainder from its direct, force and inverse components, actual Wilson small-field and charged-sector differential arguments, and the actual Wilson localization hypotheses are not formalized here. The inverse component now has its explicit cubic operator bound.

No declarations from this module should promote an entire multi-equation derivation. The graph should attach each proof to the precise bounded/operator or summability component listed in the JSON and retain the remaining successor obligations.

## Verification

- Strict Lean compilation: `lake env lean -DwarningAsError=true --stdin`, with the unchanged module source followed by all 28 `#print axioms` commands, exit 0.
- Source has no `sorry` or `axiom` declarations.
- Only the assigned new Lean module and this mapping pair were edited by this agent. Root integration of imports, theorem ledgers and generated graph is separate.
