# 34. Analytic results have their own graph nodes

Date: 2026-09-05. Status: accepted.

## Context

The rooted Wilson contraction and analytic infinite-lattice creator limit
were recorded together in the status text of one completed G18 route.
The graph could show that the route was done, but could not separately
answer which proof established the contraction, what the limit depended
on, or which results the next operator task could use. A live check detail
still described the nonlinear rooted estimate as open.

This was a missing representation, not missing mathematics. The existing
catalogue already distinguished claim status, evidence and machine tier,
but a source document, a finite control and an analytic theorem did not
have distinct connected records in this continuation.

## Decision

Add `ledger/results.yaml` with stable `RESULT:` ids and catalogue kind
`result`. Each record carries the existing status/evidence vocabulary, a
precise statement, hypotheses, scope, a pinned citation source and source
section. It uses existing edge types:

- `cites` links the result to its proof document.
- `depends_on` names mathematical inputs.
- `bears_on` records consequences or relevance without asserting derivation.
- `supported_by` names controls, each with a required explanation of the
  exact finite, scalar, numerical or formal substatement it establishes.

Routes can name `RESULT:` and `CITE:` closers and declare their own
`depends_on` inputs. The generator preserves these authored relationships;
it does not infer them from shared terminology. Validation checks source
pins, endpoint resolution, required scope and dependency cycles.

The full analytic records retain machine tier T3 while using `proven` and
`analytic` where the derivation establishes that status. No metadata join
promotes a theorem to T0 or T1. Full formal or symbolic certification must
be represented by the actual theorem or check. This preserves the existing
three axes instead of making machine tier a substitute for mathematical
truth.

## Alternatives and consequences

Keeping the results inside G18 route prose would preserve the discovery
failure. Citation aliases alone would identify files but would still
conflate a file with the several results it contains. Reusing the Lean
theorem register would incorrectly suggest formal certification.

The small result register adds one maintained source, but enables separate
queries for the endpoint equation, contraction, coefficient locality,
analytic limit and obstruction. Their direct connections now lead to the
open physical realization and excited-range routes. Fixed-order chart and
compression results remain separate usable inputs. C2 and the all-rank
assembly are program context, not invented premises of the contraction.

Current navigation is maintained in `docs/current_research.md`. Frozen
proofs and runs retain their original bytes and stage-specific conclusions.
The completion workflow in `CLAUDE.md` now explicitly includes graph and
documentation integration followed by landing green work on `main`.

## Validation

Focused tests reject malformed records, missing verification scope,
unresolved references, changed or unpinned proof sources and dependency
cycles. Existing tests still check the generated catalogue, graph and
frontier against their source files. Query the new records with
`workhouse why RESULT:WILSON_ROOTED_CONTRACTION` and
`workhouse why RESULT:WILSON_CREATOR_LIMIT`.
