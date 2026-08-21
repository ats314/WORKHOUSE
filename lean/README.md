# T0 — the proof-checked core

What compiles here is proved. Nothing else in this repository is.

```bash
curl -fsSL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
export PATH="$HOME/.elan/bin:$PATH"
cd lean && lake exe cache get && lake build
```

`lake-manifest.json` pins every dependency revision, so the build is
reproducible even though `lakefile.toml` tracks mathlib's `master`.
`.lake/` is ~8 GB and gitignored.

## Scope, stated honestly

`Workhouse/Basic.lean` formalises the **exact-rational and polynomial-identity
layer** — 21 theorems, no `sorry`, standard axioms only
(`propext`, `Classical.choice`, `Quot.sound`).

That layer is real and it is now machine-checked. It is **not** the physics.
No perturbative derivation, no operator theory, and nothing touching the
disputed fourth-order kernel appears here, because none of that reduces to
rational arithmetic.

## What is proved

Second order all ranks (the rank law with denominators cleared, `t₃ = 5/612`,
`t₂ = 0`, the deficit identity), the third-order ledger identity, the sealed
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
