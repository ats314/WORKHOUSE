# The checking layer

This package implements exact checks, numerical controls, source validation and
the claim graph. Keep mathematical status, evidence level and repository
verification tier separate. A valid analytic argument remains an established
input even while its complete formalization is pending; a finite check proves
only its recorded scope.

## Exact stays exact

Corpus rationals are `sympy.Rational`. Values the corpus records only as
floating point are Python floats named with a `_NUM` suffix. A float that reads
as exact is the most dangerous bug in this codebase, and
`tests/test_constants.py` guards the boundary.

Any function taking a rank or extent must `sympify()` its argument. `hopping(3)`
returning `0.00816...` instead of `5/612` is a bug this repository has already
shipped once.

## Adding an invariant

Register it on a suite in the module for its subject under `invariants/`,
cite the corpus section *and the
document*, and return `(passed, detail)` where `detail` carries the numbers a
reader needs to argue with you. `tests/test_invariants.py` picks it up with no
separate test to write.

Declare actual input checks with `rests_on=(...)`. Use `tier=2` when the
conclusion depends on floating point or a tolerance, and retain exact SymPy
values for T1. Keep analytic proof statements and scoped computational support
separate in the source ledgers. Formalize reusable algebraic or analytic
arguments in the appropriate Lean module using the
[formalization workflow](../../docs/formalization_workflow.md).

A check whose detail line is a restatement of its name is documentation wearing
a check's clothes. `"close enough"` is not a finding; `3.0e-15 = 31 ulps` is.

## Never widen a tolerance

If a check fails, it found something. Three possibilities: a bug in the check, a
transcription slip in the registry, or a real discrepancy in the corpus. For the
third, add an explicit `FINDING:` check that *asserts* the discrepancy.

## Files

- `constants.py` — the curated registry, with provenance and corpus status
- `invariants/` — every T1/T2 check, one module per subject; `__init__` fixes
  the order the suites register in, `_core` holds the plumbing
- `frontier.py` — computes `FRONTIER.md`; do not hand-write what it derives
- `ledger.py` — loads and structurally validates governing, contradiction and gap records
- `results.py` — analytic result statements, hypotheses, source pins and scoped controls
- `claims.py` — collects authored claims and verifier metadata into the catalogue
- `derivation_statements.py` — validates source-pinned `DERIV:` groups and their full/scoped proof links
- `lean_dependencies.py` — validates the generated kernel dependency export, source fingerprints and transitive axioms
- `recent_research.py` — validates preserved campaign sources and authored result/route records
- `study_graph.py` — validates literature study claims and their curated source relationships
- `graph.py` — computes `index/graph.jsonl`, every recorded edge between claims
- `navigator.py` — `workhouse why`: one id's whole evidence neighborhood
- `atlas.py` — the graph as one self-contained HTML page; a view, never checked in
- `corpus_index.py` — exact rationals in code, certificates, notebooks
- `corpus_registry.py` — near-miss, multiple, and coverage sweeps over the whole corpus
- `tier_collapse.py`, `near_gamma.py`, `settlement.py`, `payloads.py` — one investigation each
- `even_sector.py` — the charge-even Bloch cubic, and the finite lattice it is checked against
- `haar_epsilon.py` — exact SU(3) Haar integrals with the ε-tensors kept as ε's; the engine's projectors, a reduction the engine's partitions cannot do (ADR 0021)
- `chain_cluster.py` — the first implementation of the chain-amplitude route (ADR 0020)
- `symbolic_rank.py` — the third engine (`loopcalc`) run over the field Q(N): the fourth-order cumulants as rational functions of N, derived (ADR 0029)
- `rigor.py` — certified Arb enclosures for T2 comparisons (ADR 0010); the only sanctioned route to arb
- `triage.py` — read-only survey of an unpinned archive
- `notes.py` — the notes register: archive inventories, review verdicts, intake rules

## Preserve source and dependency semantics

Derivation source hashes are over exact received bytes. Lean export fingerprints
decode UTF-8 and normalize only CRLF/CR to LF (`utf8-lf`) so Git checkout line
endings do not invalidate an unchanged proof. Do not apply this normalization
to evidence hashes. Read text with an explicit encoding and serialize repository
paths with `/` so Linux and Windows produce the same catalogue.

`derivation_statements.py` emits whole-statement `formalizes` links separately
from scoped `supported_by` ingredients. It does not promote the source node
from T3. `lean_dependencies.py` compares registered project dependencies with
the elaborated declaration records, follows local helpers, and rejects missing
declarations, nonstandard theorem axioms, stale inputs and cycles. Exact kernel
use is distinct from the curated mathematical source argument. Neither loader
should run the graph collector or execute source documents to validate them.

When changing these semantics, use fixtures that exercise malformed records,
changed source bytes, missing declarations, partial proof scopes and mismatched
dependencies. Run the affected tests before the broader required checks. For
Lean changes, strictly rebuild and export dependencies before regenerating the
proof map and scientific views. Do not edit an export to satisfy a test.

Work in the selected canonical checkout, preserve other agents' edits and stage
exact owned paths. A change only to this guide uses the
[documentation maintenance checks](../../docs/documentation_maintenance.md);
it does not require a new computation or scientific-view regeneration. Follow
the root [working agreement](../../CLAUDE.md) for green publication and accurate
local/pushed/merged completion status.
