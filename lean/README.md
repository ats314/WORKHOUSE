# Lean formalization

This directory contains the machine-checked mathematical layer. It includes
exact algebra, finite matrices, measures, bounded and unbounded operators,
analytic limits, and spectral arguments. Formalize the complete mathematical
statement under its actual hypotheses, including the constructions it needs.
There is no algebra-only restriction.

Start with the [formalization workflow](../docs/formalization_workflow.md).
The [generated proof map](../docs/derivation_formalization.md) locates each
source statement, its whole or partial Lean coverage, and the remaining work.
[FRONTIER.md](../FRONTIER.md) and [CERTIFIED.md](../CERTIFIED.md) report current
verification; the import root is [Workhouse.lean](Workhouse.lean).

## Build from the repository root

On Linux/macOS with Bash and Make:

```bash
make lean-setup
make lean
```

The first command uses [bootstrap-lean.sh](../scripts/bootstrap-lean.sh) to
install elan if needed and obtain the pinned toolchain and mathlib cache.
The second runs `lake build --wfail`. Lean is a separate setup from Python;
`make check` does not compile it. Downloads and builds can be substantial.

For native Windows, provision elan and put `lake` on `PATH` first; this
repository's installer is a Bash script, not a PowerShell installer. In
PowerShell, run these commands individually and stop on a nonzero exit code:

```powershell
Push-Location lean
lake exe cache get
lake build --wfail
Pop-Location
```

For the integrated build and dependency export on Windows, prefer the exporter
below: it builds imported project modules sequentially before the aggregate
build to avoid concurrent access failures in the shared mathlib cache. Coordinate
with other agents so only one full Lean build/export runs in this checkout.

[lean-toolchain](lean-toolchain), [lake-manifest.json](lake-manifest.json),
and [lakefile.toml](lakefile.toml) specify the toolchain and dependencies.
Use their pins; dependency upgrades are a separate reviewed change.

## Register and connect every proof

Add every theorem, including helpers, to
[ledger/theorems.yaml](../ledger/theorems.yaml). Import new modules from
`Workhouse.lean`. Keep registered short names unique across namespaces.

For derivation work, record precise `proof_sources` and update
[ledger/derivation_statements.yaml](../ledger/derivation_statements.yaml).
A statement's `lean` list means its complete stated claim is formalized;
`lean_support` names a narrower ingredient with its exact scope. A source
argument's mathematical status remains separate from its formal coverage.
Use `promotes` only when the complete named computational check is proved.

With the repository Python environment installed and `lake` on `PATH`:

```text
uv run --no-sync python scripts/export_lean_dependencies.py
```

The exporter runs strict Lean builds, reads elaborated proof/type dependencies
and transitive axioms, validates registration and source fingerprints, then
writes [ledger/lean_dependencies.json](../ledger/lean_dependencies.json).
It has no read-only `--check` or `--help` mode. A plain successful `lake build`
does not replace this export, and an export cannot establish faithful source
encoding without mathematical review. Only the standard axioms `propext`,
`Classical.choice`, and `Quot.sound` are accepted for registered theorems.

After proof or ledger changes, follow the
[ordered export, rendering, and checks](../docs/formalization_workflow.md#export-render-and-check)
before publication. Documentation-only changes do not require a Lean build or
scientific regeneration when those inputs are unchanged.

## Earlier integration records

The [supported Track A source](../docs/derivations/track-a-supported-statements.md)
and [verification run](../runs/track_a_formalization_2026-09-09/README.md) cover
`W6Residual`, `SC17Riccati`, `SourceTilt`, and `SourceRadiusGrowth`. These modules
include actual continuous-functional dual norms, a noncommutative fixed-point
construction, centered L2 sources, and independent product-measure variance
growth. The source records retain the separate physical-model identifications.

The [September integration run](../runs/recent_research_integration_2026-09-09/README.md)
and its [Lean report](../runs/recent_research_integration_2026-09-09/lean_integration_report.json)
are preserved evidence of that run. Use the current proof map and fresh build
results for the current checkout; a dated run does not certify later edits.
