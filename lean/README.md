# T0 — the proof-checked core

What compiles here is proved. Nothing else in this repository is.

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

`Workhouse/Basic.lean` formalises the **exact-rational and polynomial-identity
layer** — no `sorry`, standard axioms only (`propext`, `Classical.choice`,
`Quot.sound`). The live theorem count is in `FRONTIER.md` §1.

That layer is real and it is now machine-checked. It is **not** the physics.
No perturbative derivation, no operator theory, and nothing touching the
disputed fourth-order kernel appears here, because none of that reduces to
rational arithmetic.

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

## Style note

Two theorems are stated with denominators cleared rather than as rational
identities with non-vanishing side conditions. That is deliberate: the cleared
form is what the algebra actually says, and it needs no hypotheses to be true.
