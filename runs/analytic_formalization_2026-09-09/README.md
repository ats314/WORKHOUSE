# Analytic formalization — September 9, 2026

This run freezes 110 new Lean theorems in five analytic modules,
their elaborated dependencies and standard-axiom audit, and the exact source
statements they support. The complete repository export covers
290 registered theorems. All 20 top-level derivation sources
are preserved byte for byte in `sources/`.

The [statement inventory](ledger/derivation_statements.yaml) distinguishes
whole-statement proofs from scoped ingredients and keeps explicit hypotheses
and successors. The [kernel export](ledger/lean_dependencies.json) records
actual type and proof dependencies, including mathlib. `verification.json`
states the checked scope. Mathematical source status is not changed by the
remaining formalization work.

These proofs supply operator, measure, limit and spectral mechanisms. They do
not by themselves construct the complete Wilson cylinder/generator/SDE model,
discharge complete interacting source matching, or prove the spatial continuum
Yang-Mills theorem. Follow the current `docs/derivation_formalization.md` for
successor work; this run is immutable evidence of this stage.

`preserved-validators/` retains the original imported scripts before formatting-only
changes made to satisfy the repository lint gate. Earlier audit reports keep
their original hashes and have not been re-pinned.

Reproduce the live modules in the canonical checkout:

```powershell
uv run --no-sync python scripts/export_lean_dependencies.py
uv run --no-sync python scripts/render_derivation_coverage.py --check
uv run --no-sync pytest tests/test_derivation_statements.py tests/test_lean_dependencies.py
```

The snapshot contains the five new modules; the live import root also requires
the unchanged earlier modules and the pinned mathlib toolchain. Its module
source hashes are raw local bytes; portable kernel fingerprints use UTF-8 with
line endings normalized to LF only. All snapshot files have raw SHA-256 pins.
