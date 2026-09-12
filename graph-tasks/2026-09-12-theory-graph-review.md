# Task Record: 2026-09-12-theory-graph-review

## Identity
- **Task ID:** `2026-09-12-theory-graph-review`
- **Date:** `2026-09-12`
- **Agent / Model:** Claude Code (remote session), configured `claude-opus-5`
- **Checkout:** `/home/user/WORKHOUSE` (remote clone; the workstation checkout is `C:\WORKHOUSE\REPO`)
- **Branch / Revision:** `claude/theory-graph-review-8bpt0t` @ `832b967`

## Target
- **Graph IDs:** `G19`, `G17`, `G9`, `G25`
- **Objective:** Review the current theory graph and recommend the next research
  steps. No mathematical claim, status, evidence level or route state is changed
  by this record.
- **Regime:** review only; the targets themselves span finite lattice,
  infinite volume at fixed spacing, and continuum.

## Start Snapshot
- **Snapshot Path:** `.graph-state/2026-09-12-theory-graph-review/start.json` (local; `.graph-state/` is gitignored)
- **Command:** `uv run --no-sync workhouse brief G19 G17 G9 G25 --json --out .graph-state/2026-09-12-theory-graph-review/start.json`
- **Fingerprint:** `36a8ece58ab40a49c9944f7a32bb06ba8e8c056c7de3ef1bfe4ea2be26e8efdf`
- **Freshness:** `unknown` — reason recorded by the briefing: *no successful
  index-generation input record exists*. This is the expected state of an
  ordinary clone: `.graph-state/index-inputs.json` does not travel with it.
  Saved index bytes were read; `verification.execution_state` is
  `not_started`, `executed = 0`, `cache_reused = 0`, `recorded = 677`. No
  check was executed for this request and no Lean build was run.

## Established Inputs
- **Reviewed Sources:** `docs/theory_graph_protocol.md` (SHA-256 matches the
  startup notice), `FRONTIER.md` §§1-7b, `docs/current_research.md`,
  `docs/research_goal.md`, `ledger/gaps.yaml` (`G25`, spine, `U1`-`U3`),
  `docs/derivations/w6-synchronized-m10-domination.md`,
  `graph-tasks/2026-09-11-m10-proof-repair.md`.
- **Dependencies:** none created. The review reads registered records only;
  retrieval of a relationship is not an assertion of its mathematical
  implication.

## Obligation
- **Investigated Statement:** none. This is a survey of the recorded frontier
  and of repository landing state.
- **Downstream Consequence:** a recommended ordering for the next iteration,
  plus two repository-hygiene items that are landing problems rather than
  mathematical ones.

## Ownership
- **Owned Files:** `graph-tasks/2026-09-12-theory-graph-review.md` (this file).
  No ledger, source document, check, Lean module or generated view is touched.
- **Shared Processes:** PR #157 (`codex/local-class-wick-20260911`, Codex) is
  open and **not** owned here; see Handoff.

## Work and Checks
- **Commands Executed:**
  - `uv run --no-sync workhouse brief --startup`
  - `uv run --no-sync workhouse brief G19 G17 G9 G25 --json --out .graph-state/2026-09-12-theory-graph-review/start.json`
  - `uv run --no-sync workhouse status`
  - `uv run --no-sync pytest tests -q -k "frontier or certified or catalogue"`
  - `uv run --no-sync pytest tests -q -k "stale or frontier or certified or catalogue or ledger"`
- **Outcomes:**
  - `status`: contradiction register empty of open entries; *Ledgers
    structurally sound*.
  - Generated-view tests: 36 passed in the narrow selection; the wider
    selection also exited 0. `FRONTIER.md`, `CERTIFIED.md` and `index/` are
    not stale at `832b967`.
  - Saved counts read from the graph, not re-executed here: 439 Lean theorems
    with 0 `sorry`, 677/677 registered T1/T2 checks.
  - No `make verify` / `make lean` run: no scientific or executable input
    changed in this task, so those are not required and a re-run would not be
    a fresh result for anyone else's commit.
- **Evidence Paths:** `.graph-state/2026-09-12-theory-graph-review/start.json`
  (local only, per the gitignore above).

## End Snapshot
- **Snapshot Path:** not taken. No graph input changed in this task, so the
  start snapshot remains the current observation. A live or fresh briefing
  would execute checks without a changed input to investigate.

## Handoff

### Recorded state, as read
The fourth-order charge-odd dispersion and the fixed-spacing infinite-volume
Wilson band and literal-source frame are established in their stated regimes
(`RESULT:WILSON_INFINITE_PHYSICAL_BAND`; G18 discharged at that scope; G3
discharged via ADR 0024). Nothing is open in the contradiction register. The
whole remaining distance to the governing Clay objective sits in G19's
spatial-continuum comparison and transport, with G17 carrying a valid
source-family formulation. No gap-level dependency edge is open, so the
useful ordering is the source-level route queue, not the gap tier list.

### Recommended next steps, cheapest decisive first
1. **Clear the landing state before starting new mathematics.** PR #157
   ("Integrate all-rank local Wick spectrum and sign theorem") is open, draft,
   and `mergeable_state: dirty` — it conflicts with `main` at `832b967`, which
   already contains a local merge of its content plus the M10 repair. It also
   reports **no check runs at all** on head `6feae907`, and its own body says
   exact-head CI and final receipts are still pending. That is precisely the
   failure ADR-era note of 2026-09-05 and the completion rule exist to
   prevent: finished work reading as unlanded. Its owner (Codex) should merge
   the base into the branch, re-run verification at the exact head, and merge
   or close it deliberately — the conflict must be resolved without discarding
   either side.
2. **The M10 successor (G19 route 1) is the sharpest open estimate.** The
   repair discharged the centered complement outside enlarged minimizing-set
   tubes and fixed the parameter-derivative criterion; its own §7 and the
   2026-09-11 handoff name exactly three remaining hypotheses: uniform
   polynomial relative-amplitude control, actual tube moments, and the actual
   normal/angular comparison on the established antipodal geometry. Those
   inputs are registered `proven`
   (`RESULT:W6_ANTIPODAL_GAUGE_NORMAL_COERCIVITY`,
   `RESULT:W6_ANTIPODAL_ANGULAR_REDUCTION`,
   `...:ACTUAL_SOURCE_MOMENT`), and the route records no unresolved completion
   input. Start at S14 tube moments, since the amplitude bound and the angular
   comparison both consume them.
3. **R10 (G19 route 2) is independent work, not a consequence of M10.** The
   spine says so explicitly. H4 now follows from H0 and the first ground jet,
   so H0-H3 are the whole order-zero obligation; decompose the complete
   generator into vacuum and conditional-source parts and test the proposed
   `g` powers on the full energy graph rather than on ground vectors. This is
   the right second worker if two agents run in parallel.
4. **Of the three untried G19 routes, prefer the interacting-grid comparison
   (route 3).** Its decisive next test is small and concrete — two genuinely
   coupled adjacent blocks, full conditional/source form with interfaces, a
   local estimate whose constants sum without a block-count factor — and
   uniformity in block count is the obligation that the fixed-block results
   structurally cannot supply. The SC17 signed defect (route 4) and the
   normalized-RG summable increment (route 5) are larger and should wait.
5. **G17 is load-bearing and has one untried route, but do not treat it as a
   gate.** Its unrestricted exponential-radius inference is refuted; the task
   is to identify the exact source operator, normalization and norm consumed
   by the selected spectral comparison and to prove a replacement preserves
   it. Worth one session to write down the candidate norm and the
   `(M(2α)^n − M(α)^{2n})/n` comparison, then stop at the precise interacting
   inequality still required rather than reaching for a radius bound.
6. **Bounded-cost side work, if a cheap finite computation is wanted:** G9's
   assembled sixth-order cluster (route 6) has all five source inputs proven
   and determines whether local RUR survives; `G25`'s fourth-order C-even side
   is *absent* rather than T3 and is explicitly downstream of the O(u^4)
   weight cards, so it is not independent work and should not be queued as if
   it were. `G6`/`G7`/`G8` remain the tier-1 regeneration items.
7. **Literature intake is the lowest-risk backlog.** A large share of the
   `G17`/`G19`/`G23` method papers — the Balaban 1985/1987 entries, the
   Brydges-Fröhlich-Seiler series, Glimm-Jaffe, `BBIJ_1984`, `KP_1986`,
   `T_HOOFT_1979` — are `not-yet-obtained`. Several are named inputs of the
   routes recommended above, so obtaining them changes what route 5 can cite.

### Not recommended
Re-running `make verify`, `make lean` or a live briefing as part of this
review: no input changed, and a repeat pass is not a new result. Likewise do
not reopen G18's fixed-spacing route, or read the M10 counterexample (some
permitted Q8 cutoffs fail M10) as a refutation of the synchronized successor —
it closes a route, not the target.

- **Established Result:** none claimed. Review only.
- **Failed Attempts / Obstructions:** none newly recorded. Saved graph
  freshness could not be established in this clone (`unknown`, reason above);
  a `matched` receipt requires a local `workhouse index -w` provenance record.
- **Successor Obligation:** resolve PR #157's conflict and exact-head CI
  (Codex, owner), then prove the S14 tube moments for the synchronized S13
  field as the M10 successor.
