# T0 — the proof-checked core

Successful strict Lean compilation certifies the exact formal statements
under their displayed hypotheses. The repository also records established
analytic proofs in `ledger/results.yaml`; their mathematical status is
separate from their machine-verification tier.

```bash
make lean-setup   # elan, the pinned Lean, mathlib's build cache — from the repo root
make lean         # proof-check
```

`make lean-setup` runs `scripts/bootstrap-lean.sh`, which the Lean CI job also
runs, so a local toolchain and CI's are installed by one recipe rather than two
that drift. It is idempotent and deliberately *not* part of `make bootstrap`:
`make check` never compiles Lean, so folding it in would charge every session a
multi-GB download for a tier it is not going to check.

`lake-manifest.json` pins every dependency revision, so the build is
reproducible even though `lakefile.toml` tracks mathlib's `master`.
`.lake/` is ~8 GB and gitignored.

`make lean` passes `--wfail`. Lean reports a `sorry` as a *warning*, so a plain
`lake build` exits 0 with one present — and the "no sorries" line the target
prints would then be an assertion rather than a check, which is the one thing
this repository is built not to do.

## Scope, stated honestly

The modules imported by `Workhouse.lean` formalize rational and polynomial
identities, finite matrix algebra, probability-measure comparison, bounded
operator inverses, unbounded-operator closability and analytic limit arguments. They use no
`sorry` and only standard axioms (`propext`, `Classical.choice`, `Quot.sound`).
The live theorem count is in `FRONTIER.md` §1.

That formal layer is T0. Exact computational derivations in
`src/workhouse/invariants/` have their own T1 scope; their finite controls
do not automatically certify general operator or Haar-integration theorems.
Analytic results can be proven while their full statements remain T3 for
machine verification. A scalar lemma supporting such a result certifies
its stated scalar implication, including the supplied hypotheses.

## Adding a formal statement

Put the theorem in the appropriate module, import new modules from
`Workhouse.lean`, and add every theorem name to `ledger/theorems.yaml`,
including helper lemmas. The register records the actual formal statement.
Leave `formalizes` and `promotes` empty when no entire named claim or check
is formalized; narrow supporting uses can be recorded in a result's scoped
`supported_by` entries instead. Compilation and those support edges do not
replace the required register entry.

Record its precise source statement in `ledger/derivation_statements.yaml`:
`lean` means the entire stated claim, while `lean_support` records an explicitly
scoped ingredient. Keep the source's analytic status independent of this coverage.

Run `python scripts/export_lean_dependencies.py` from the configured repository
environment. It runs the strict build, extracts elaborated type/proof constants
and transitive axioms, and checks every registered theorem. The generated
`ledger/lean_dependencies.json` pins its Lean inputs and records dependencies on
both project declarations and mathlib. The graph follows local definitions to
the next registered theorem. Regenerate the catalogue, frontier and certified
views after this export; stale exports are rejected.

The [derivation proof map](../docs/derivation_formalization.md) gives coverage and
remaining obligations for every current top-level derivation document.

## What is proved

Second order all ranks (the rank law with denominators cleared, `t₃ = 5/612`,
`t₂ = 0`, the deficit identity), the per-channel resolvent equation — the four
channel weights in closed form from the dimension/Casimir table, the two
family sums `A_N` and `B_N`, and the projector-to-cross-matrix-element
assembly `Σ η_ρ w_ρ = t_N` (PUB edition eqs. 11–12) as rational identities
with explicit non-vanishing hypotheses — the third-order ledger identity, the sealed
fourth-order core and the all-rank axial law at every exceptional rank, the
pencil relations including the blind holdout `λ_R = 2λ_M − λ_X` and the
25-point stencil zero-mode gate, the historical kernel's internal consistency
(`C` from `β`, width as `α + β`, the tier-collapse relation), Newton's identity
in three variables, the four checkpoint-extraction formulas, and the
finite-volume cycle count.

The later modules add the Wilson vacuum-chart and compression matrix
identities, the rooted scalar bound, the creator-parent algebra, and the
global vertical comparison's seven scalar lemmas. The latter certify the
strip factor, spectral-cap and affine assembly, two-sector scalar form,
and threshold inequality. They do not formalize elliptic operators,
SU(N) geometry, min-max arguments, or the full nonlinear fast complement.

## Style note

Two theorems are stated with denominators cleared rather than as rational
identities with non-vanishing side conditions. That is deliberate: the cleared
form is what the algebra actually says, and it needs no hypotheses to be true.

## September source integration

The September 1-9 integration adds these modules to the active `Workhouse.lean`
import root. Their individual statements and graph targets are in
`ledger/theorems.yaml`; theorem counts remain generated in `FRONTIER.md`.

| Module | Formalized content | Source |
|---|---|---|
| `VacuumChart` | Rank-one adjoints, corrected vacuum legs, endpoint cancellation | September 5 vacuum-chart package |
| `VacuumCompression` | Exact compression and vacuum-corner identities | September 5 compression package |
| `RootedScalarBounds` | Normalized Taylor lower bound | September 5 rooted-contraction package |
| `CreatorParent` | Star-ring square identities and parent-gap constant | September 5 creator-parent package |
| `GlobalWilsonVertical` | Spectral-cap and affine-comparison scalar implications | September 5 nonlinear-block package |
| `AnisotropyVariance` | Simplex variance, complete zero set, uniform bound, induced coefficient | September 8 anisotropy campaign |
| `WilsonSquareForce` | Sharp inverse-energy coefficient bound for every radial index and finite spectral synthesis | September 9 square-block campaign |
| `WilsonGridAlgebra` | Exact four-edge energy decomposition, bounds and constant kernel | September 9 compact-continuation campaign |
| `ResolventLocalization` | Infinite Neumann inverse, exact signed identity, cubic operator remainder, Schur minimization and infinite lattice sums | BF1–BF3, SP1–SP10, W4–W6 and localized pairing |
| `GroundStateAssembly` | Probability-measure density comparison, noncommuting projection assembly and explicit-domain physical gap transport | VA/BA assembly, GST and Gram positivity |
| `ThermodynamicLimit` | Actual weak-law and uniform-score limits, integration by parts, unbounded-operator closability, form-core limits and spectral interval mass | SC17 T12 and IF3–IF13 |
| `SpectralReconstruction` | Positive spectral-measure decay, support-gap exclusion, localization balancing and dense-family projection extension | Reconstruction R1–R7 |
| `PlateauObstruction` | Exact exponential optimization and positive slow-mode obstruction for every positive plateau | Reconstruction R4–R5 |

The five existing branch modules are copied without byte changes. The three
campaign modules retain the original eight anisotropy statements and add
proofs of the complete nodal criterion and the stated universal algebraic
bounds. Operator identification, infinite-dimensional domains and interacting
transport remain explicit in the source results they support.

The [integration report](../runs/recent_research_integration_2026-09-09/lean_integration_report.json)
records the successful strict build and the standard-axiom audit for all 46
integrated declarations. [The run](../runs/recent_research_integration_2026-09-09/README.md)
preserves their provenance and validation outputs.
