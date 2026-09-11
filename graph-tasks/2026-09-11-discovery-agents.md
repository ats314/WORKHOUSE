# Discovery layer for autonomous agents

Task: 2026-09-11-discovery-agents. Owner: Claude Fable 5.1 (Claude Code desktop
session) with bounded read-only research collaborators, disjoint implementation
collaborators and blind fixture authors.

Checkout: `C:/WORKHOUSE/worktrees/discovery-agents-20260911`; branch
`claude/discovery-agents-20260911`; initial revision `acc3e91` (origin/main after
PR #141; its post-merge CI run 34555918807 completed green on all six jobs).
This is a software and retrieval task, not a mathematical claim adjudication.
Ownership is recorded in the outer workspace at
`navigation/tasks/2026-09-11-discovery-agents.md`; the maintained documents
revised here were preserved first under
`navigation/preserved/2026-09-11-discovery-agents/MANIFEST.json`.

## Maintainer decisions recorded at the start

The maintainer answered eight direction questions before implementation:
agents in autonomous sessions are the consumers; all four connection kinds
matter (reusable ingredients, disagreements and scope restrictions, forgotten
archive results, literature links); the index may extend to outer-workspace
text; registration is proposal files only, with review state versioned outside
the scientific ledgers; no local embedding models are to be evaluated in this
session; and the theory graph (`ledger/`, `index/`) must never be modified by
discovery tooling.

## Target and start snapshot

Targets are the seeds of the cross-source case studies, selected from the
current research map by a read-only obligations reader:
`DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10`,
`DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE`,
`RESULT:BALABAN_MULTISCALE_CAUCHY_SUMMABILITY` and
`RESULT:W6_ENERGY_WEIGHTED_CT`. They exercise the tooling; they set no
mathematical priority and no status changes.

- start: `.graph-state/2026-09-11-discovery-agents/start.json`; file SHA-256
  `15c589f0e7441fd2da292ba6e2dc2891362bf2ff68627d8250103dde820278db`;
  `snapshot_fingerprint`
  `44431377cbd6a844dc1dff2eecf3077f1d533fa04190514d9ee144322e640569`;
  saved mode; freshness `unknown` (fresh worktree without a local
  index-generation record); executed checks 0; saved `index/claims.jsonl`
  SHA-256 `628c3160…`, `index/graph.jsonl` `8a0b706a…`.

The research-map MCP server connected to this session was assessed read-only:
it is a separate project index (101 arXiv papers under the NEURAL CLAUDE
folder, built 2026-08-28, no WORKHOUSE content) and plays no role here.

## Ownership

Owned and changed in this worktree: `src/workhouse/discovery.py`,
`discovery_index.py`, `discovery_graph.py`, `discovery_present.py` (new),
`discovery_scope.py` (new), `discovery_review.py` (new),
`discovery_lexicon.py` (new), `discovery_pairs.py` (new), the `discover`
section of `src/workhouse/cli.py`, `scripts/benchmark_discovery.py`,
`scripts/evaluate_discovery.py` (new), `tests/test_discovery*.py`,
`tests/fixtures/discovery_heldout_queries.json` and
`tests/fixtures/discovery_heldout_plans/` (new), `graph-tasks/discovery/`
(new: scope, lexicon, review register, proposals), `docs/graph_discovery.md`,
`docs/theory_graph_protocol.md` (discovery paragraph), `README.md` (one
sentence), `docs/documentation_manifest.json`,
`docs/research/graph-discovery-agents-2026-09-11.md` (new),
`docs/benchmarks/graph-discovery-agents-2026-09-11.md` (new), this record and
its evidence directory. Not written: `ledger/`, `index/`, `theory/`,
`corpus-import/`, `lean/`, `docs/derivations/`, `docs/decisions/`, `paper/`,
`FRONTIER.md`, `CERTIFIED.md`; `git status --short` over those trees was
empty at every checkpoint and `ledger.validate` returned no problems.

Collaborators: six read-only readers (research-map server, engine profile,
ledger shapes, open obligations, outer corpus inventory, agent usability) and
one completeness critic; four blind fixture authors and one validator; five
implementers on disjoint files (external scope, review register, lexicon and
plans, pair dossier, evaluation harness); four blind plan authors; four
case-study investigators each checked by a skeptic. Every collaborator was
forbidden to write the scientific inputs or run `workhouse index`, `verify`
or `make regen`.

## Work and checks

Engine: local-push personalized PageRank with an exact L1 residual (power
iteration retained as the reference), one freshness walk per response with
files checked by `lstat` rather than resolved, lazy path steps, math-aware
passage boundaries, compact rank-ordered output with named omissions,
sub-query fusion, unlinked passages as connection candidates with a reserved
quota, identical-passage collapse with `also_at`, an `--internal-only`
switch, a pre-registered weak-match hint, UTF-8 output on Windows pipes.
Warm search fell from about 1.10 s to 0.43 s on the development fixture
(16/16, MRR 0.7068 against 0.6985) before the external roots were indexed.

External scope: `graph-tasks/discovery/scope.yaml` (21 enabled roots, tier 3
declared but disabled); the real build indexed 906 external sources and
13,872 external passages with 833 byte-identical aliases skipped; cache about
236 MB; junctions refused; stat-based re-check for external files.

Review register and proposals: `workhouse discover review add|list|show|mark|
replay|validate` and `discover propose`, hash-chained records, closed
vocabularies, refusal of `contradictions` and of every scientific path.
A smoke cycle on the real corpus with a scratch register left `ledger/` and
`index/` untouched.

Lexicon and plans: 57 concepts, 471 cited variants; `discover plan` and
`discover lexicon`. Pair dossier: `discover pair A B`.

Evaluation (worktree at `fdaadc4`, cache `52c54e76…`): held-out recall at ten
25/30 (MRR 0.560) for the default search, 26/30 (MRR 0.688) with blind
agent plans, 22/30 (MRR 0.526) with automatic lexicon expansion; six of six
exact controls first; zero of six negatives empty under any configuration;
link recovery of hidden curated edges at five 25% (MRR 0.170) for
`connections` against 10% (0.056) for retrieval alone. Development fixture:
16/16 (MRR 0.678) default, 15/16 (0.595) with automatic expansion. Reports:
`evidence/2026-09-11-discovery-agents/{heldout,dev}-evaluation.{json,md}`.

Focused tests for every discovery module passed at each commit (`ruff check`
and `ruff format --check` clean); `scripts/check_docs.py` reported 37
maintained files and 553 links with no errors. The full local suite at
`07392a5` passed 1882 tests with 4 skips and no failures (about 12 minutes);
repository-wide `ruff check` and `ruff format --check` were clean over 536
files. Remote CI is recorded in the handoff below.

## Limitations

- Automatic lexicon expansion lowered recall on both fixtures; search never
  expands a query on its own, and plans need an agent's judgement.
- No configuration abstains on a negative control; the weak-match hint is
  coverage information, not a verdict.
- Near-duplicate archive copies with different chunk boundaries still
  compete with repository originals; only byte-identical passages collapse.
- A CLI process with external roots spends about 0.7 s hashing external
  files at engine start; a batch session amortizes it.
- The research-map server is unrelated and remains registered user-wide;
  removing or renaming that registration is the maintainer's decision.

## Case studies

Four cross-source investigations ran the tooling end to end and were each
checked by an independent skeptic; the
[case-study report](../docs/research/graph-discovery-case-studies-2026-09-11.md)
records the readings, the narrowings and what did not hold. Outcomes, as
retained in the review register (sixteen records, chain intact, three
proposal files, none applied):

- Combes-Thomas: the localization core of `RESULT:W6_ENERGY_WEIGHTED_CT` is
  the imported EX-012/EX-011 theorem under a renaming (established, narrowed to
  the localization core; proposal on the documents surface); the question's own
  mechanism for the soft-residual certificate is refuted by the README's `C = 1`
  realization (rejected).
- Outside pressure: the hypothesised Schur-complement identification is false;
  an exact identity for the outside-pressure Hessian replaces it, and SC17
  R10's marginal-curvature step is literally EX-014 section 3(3) (established;
  proposal on the documents surface), as is the imported Riccati flow note's
  Hessian evolution against SC17 R1 (established; proposal).
- Balaban: the seed's contraction factor is power counting, not a block-map
  constant (rejected); the refutation of EX-014 STEP 6 by
  `RESULT:CONDITIONAL_GRADIENT_REPAIR` is correct but already registered as a
  dead route in `ledger/gaps.yaml` (established, no proposal).
- Brascamp-Lieb and M10: survives only as a tube-scoped chart Poincare bearing
  and a near-well hypothesis match; three pairs withdrawn by the skeptic.

The investigators' registration inconsistencies (unregistered soft-residual
campaign, "Criterion W6: Closed" text against a disputed status, apparently
swapped `supported_by` scopes on the Balaban RESULT, the G19 note's summary
table against the manuscript's own text) are reported in the case-study page
and were not edited.

## End snapshot

- end: `.graph-state/2026-09-11-discovery-agents/end.json`, retained as
  `evidence/2026-09-11-discovery-agents/end.json`; file SHA-256
  `ff4e9643b48080ca…`; `snapshot_fingerprint` `a54b7d72f3671ab8…`; saved mode;
  freshness `unknown`; executed checks 0. The saved `index/claims.jsonl`
  (`628c3160…`) and `index/graph.jsonl` (`8a0b706a…`) digests are identical to
  the start snapshot: no scientific catalogue, source, tier or edge changed.
  The fingerprint differs because the input manifest includes the new and
  changed discovery code.

## Handoff

Established here: the tooling and its evaluation, with the case studies as
worked examples and the register as their retained state. No mathematical
status changed. Downstream: an agent applying any of the three proposals
does so by hand after the checklist, in a reviewed pull request; the exact
identity for the outside-pressure Hessian and the Combes-Thomas single
registration are the two readings most worth a human's hour. Remaining
successors for the tooling: near-duplicate collapse across chunk boundaries,
a proposal surface for `recent_research.yaml` results, a catalogue identity
for imported passages, and an abstention signal that separates paraphrased
positives from negatives.
