# 15. The graph carries routes, check dependencies, yielded values and manuscript labels

Date: 2026-09-01. Status: accepted.

## Context

ADR 0007 built the graph as the substrate every "what bears on X" question was
missing, and ADR 0009 reached it into the corpus. On 2026-09-01 a session that
had read `FRONTIER.md`, the ledgers and the invariant sources in the order the
brief prescribed, and had never run `workhouse why`, recommended as the next
step for C2 a route the repository had already closed two days earlier. The
closure existed — in a run README and in one check's detail line — and the
graph could not surface it, because four kinds of relationship the repository
relies on were not edges:

- **Checks rested on checks, and the graph had no edge between any two of its
  265 check nodes.** A window theorem's check delegated to a Casimir shelf and
  a cycle census; nothing recorded it. `derive` could cite documents outward
  but could not render a derivation inside the T1 layer.
- **Attempts at a gap were prose.** G3's plan steps lived in one free-text
  YAML field, and the run that killed one of them was linked to the gap, not
  to the step. `why G3` listed leads and elided the plan.
- **A value a check computed existed only in its detail line.** The
  perpendicular cube coefficient `-11/192` was derived on 2026-08-30 and no
  search by value could reach it, in a corpus whose join keys are exact
  rationals.
- **The manuscripts' `\chk` labels were verified but not joined.** The guard
  proved every label resolved; the graph could not say which editions print
  a check, and the claim-to-check map was maintained by hand in
  `paper/README.md`, where it had drifted once.

## Decision

Four joins, each curated at the point the fact is authored, and none inferred.

1. **`rests_on`.** `suite.check(..., rests_on=(...))` names the registered
   checks a check takes as inputs. The graph emits `rests_on` edges, requires
   every name to resolve to exactly one check, and rejects a cycle. Declared,
   never inferred from source.
2. **Routes.** A gap's plan steps are catalogue nodes (`ROUTE:<gap>:<step>`)
   with a closed state vocabulary — `untried`, `live`, `dead`, `done` — and
   two curated edge fields: `closed_by` (the run, check or ADR that settled
   the step) and `cannot_decide` (the claim an instrument is structurally
   unable to reach). The ledger validator rejects a step without a state and
   a `dead` or `done` step with neither a closer nor prose. `why <gap>`
   prints routes by state; FRONTIER §7 and the session brief carry them for
   the cheapest decisive gap. This is a new closed vocabulary, on plan steps,
   not on claims: the three claim axes of `AGENTS.md` are untouched, and the
   field mirrors the existing `GAP_STATES` lifecycle one level down.
3. **`yields`.** A check may return a third element, `{NAME: value}`, and each
   becomes a catalogue constant with the check as its origin, carrying the
   check's tier while it passes and T3 when it fails. A `float` is refused
   unless the name carries `_NUM` — the registry's boundary, enforced where a
   number is born. A yielded name may not shadow a registered constant.
4. **`labels`.** Every legended edition in `paper/` emits one `labels` edge
   per distinct `\chk` label, through the same parser the manuscript guard
   uses, so the two cannot disagree.

Two smaller changes ride along because the same session tripped on them:
`workhouse index -w` iterates to a fixpoint (a check prints the graph's edge
count into its own detail line, so one pass leaves the two files a generation
apart), and `verify --only` repeats.

## What it does not do

No edge is inferred. A route's state is what its author wrote; a run closes a
route only if the ledger says so. Nothing here promotes a claim past the tier
its check establishes, and a yielded value is exactly as established as the
check that yields it.

## Consequences

`why G3` now answers "what has been tried" in one screen: two routes done,
one live, two dead with their closers, one untried. `search -11/192` lands on
the check that derived it. `why 'PUBLICATION rev5'` lists the 107 checks the
edition rests on, computed. The brief opens with the graph rather than with a
reading order, because the reading order is what produced the failure.
