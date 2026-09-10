# Hodge and polymer formalization scope correction

The [successor source](../../docs/derivations/hodge-polymer-supported-statements.md)
records six exact groups: abstract Hodge kernels and carrier actions, rank-one
operator identities, syntactic word enumeration, supplied rational polynomial
identities, and scalar geometric majorants. The two subject modules contain
36 registered declarations. Their physical computational-check promotions are
empty; the actual incidence results receive only scoped support.

The corrected Laplacian is U=ψψ† and the normalized projector is P=U/q.
Their carrier actions are separately proved. The operator RUR factorization
is also proved directly from the rank-one hypothesis, independently of the
syntactic word predicate and supplied carrier polynomials.

[source_manifest.json](source_manifest.json) preserves the received pending
Lean files and theorem registry with their original bytes and paths. Earlier
overclaims remain in those snapshots as historical evidence. The worktree's
base was GitHub main `42b0762e4ce382efa153a969e8bb44bb77537844`; unrelated
canonical-checkout changes were preserved.

The single coordinated [strict export log](strict_export.log) records all
project module builds, the strict aggregate build and the completed kernel
export: 389 registered theorems and 821 project declarations. The exporter
accepts only propext, Classical.choice and Quot.sound as transitive axioms.
This verifies the declarations and their dependencies, not their application
to an uninstantiated physical model.

Reproduce with the pinned repository environments, in order:

```text
python scripts/export_lean_dependencies.py
python scripts/render_derivation_coverage.py
workhouse index -w
workhouse frontier --write
workhouse certified --write
pytest tests/test_hodge_polymer_scope.py tests/test_derivation_statements.py tests/test_lean_dependencies.py
```

The full repository regression and mathematical checks, and CI at the landed
revision, remain the integration gates. Their execution status belongs to the
tested revision and final landing report rather than to the received sources.
