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
identities, finite matrix algebra and scalar inequalities. They use no
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

Run the strict build and check the inventory before regenerating the graph,
frontier and verification catalogue. This prevents a compiled theorem from
being omitted from the curated map or left disconnected in the graph.

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
