# Reviewed theory-current integration, 10 September 2026

This run preserves the derivations developed during the read-only graph
exploration and their supplied independent review. The user subsequently
authorized integration, strict verification and GitHub merge. The received
review is preserved verbatim in [received_review.md](received_review.md);
its replay claims describe that review, not this run's fresh execution.

## Mathematical contribution

The [theorem register](../../paper/research_notes/THEORY_CURRENT_BRIDGES_20260910.md)
states the new results and their source lineage. Detailed arguments live in
[source currents and totality](../../docs/derivations/source-currents-and-spectral-totality.md)
and [geometry and Riccati connections](../../docs/derivations/theory-geometry-and-riccati-bridges.md).

The strongest physical coefficient result is the explicit current for the
actual fixed square's complete first residual, with
K_star=(48213-16675 sqrt(2))/20706224<1/840 for all radial finite-energy
sources. Its weak pairing uses fast test vectors. Finite-coupling remainder,
volume-uniform control and continuum transport remain separate obligations.

The variational estimate requires no inverse. The checked W6 composition
permits a degenerate lower energy while retaining its existing bounded-inverse
assumptions, without requiring a uniform inverse-norm estimate. The generally
nonunitary Schur congruence carries its retained metric. The sharp anisotropy
maximum is specific to three coordinates; scalar parity removes existing odd
Taylor coefficients without providing a fourth-order remainder.

## Proof recovery and new verification

[proof_recovery.json](proof_recovery.json) identifies the original task, log
line and SHA-256 of each preserved proof-call input under `recovered/`.
These inputs retain their original command syntax and historical scopes;
they are evidence, not an instruction to execute copied shell text.
The integrated [TheoryCurrentBridges.lean](../../lean/Workhouse/TheoryCurrentBridges.lean)
contains ten mathematical lemmas and one explicitly narrow algebraic helper.
Its fresh strict build and dependency export are recorded separately from
the source recovery.

Exact checks reconstruct the cometric/operator, Gaussian current moments,
radial budget, three-coordinate stationary/boundary algebra, secular moments,
source congruence and finite negative controls. They support specified parts
of the analytic source statements. The general form-domain, source-totality,
spectral and finite-coupling arguments are not certified by those finite
controls. `RESULT`/`DERIV`, `CHK` and `LEAN` retain their separate scopes.

The validation files record commands, actual outcomes and source fingerprints.
`SHA256SUMS` pins every file of this frozen run except itself. The live ledgers
and generated graph remain outside this run and may advance after landing.

## Reproduction

From a checkout with the locked Python environment and pinned Lean packages:

```text
uv sync --all-extras --frozen
uv run --no-sync python scripts/verify_source_current_bridges.py
uv run --no-sync python scripts/verify_theory_geometry_bridges.py
uv run --no-sync python scripts/export_lean_dependencies.py
uv run --no-sync python scripts/render_derivation_coverage.py
uv run --no-sync workhouse index -w
uv run --no-sync workhouse frontier --write
uv run --no-sync workhouse certified --write
```

The export performs the strict Lean build and audits standard transitive
axioms. Execute generators sequentially. Full regression and mathematical
verification accompany publication; the recorded run is not a claim that a
later modified checkout was checked.
