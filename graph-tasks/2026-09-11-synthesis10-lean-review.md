# Review of the Synthesis10 Lean modules cited as formal support

## Identity

- Task: `2026-09-11-synthesis10-lean-review`; date: 2026-09-11; agent: Claude Opus 5.
- Checkout: `C:/WORKHOUSE/worktrees/synthesis10-lean-review-20260911`,
  branch `claude/synthesis10-lean-review-20260911`, created from
  `origin/main` at `0b667161` (PR #154 merge).
- Prior observation checkout: `C:/WORKHOUSE/REPO`, `workspace/main` at
  `b9651bea3d772d3968eaddce72f0c6ad316928db`, which was 17 commits behind
  `origin/main` at the time of reading. `origin` was fetched read-only; no
  branch, remote or working tree in `REPO` was modified.
- Continuation: none. This record does not replace an earlier one.

## Target

Graph IDs briefed: `R2`, `C5`, `R14`, `G7` — the claims carrying the two
coefficients that the reviewed material is cited alongside (`t_n` with
`t_3 = 5/612`, and `sigma_series` including `sigma_5`).

Precise question: five synthesis documents dated 2026-09-11
(`MASTER_THEORY_SECOND_DEEP_DIVE_HISTORICAL_SECRETS.md`,
`VERIFIABLE_DERIVATIONS_AND_PROOFS_MASTER_CATALOG.md`,
`NON_GRAPH_DERIVATIONS_AND_PROOFS_MASTER_DOSSIER.md`,
`NOVEL_THEORY_GRAPH_DERIVATIONS_DOSSIER.md`,
`derivation_statements_novel_proposals.yaml`) cite 31 modules of the
archived `synthesis10` Lean 4 library as `Lean Support` / `lean_support`
for analytic Yang-Mills statements. **Does that library formalize the
statements it is cited for?**

Regime: the modules are finite Lean 4 files; the question is about what
their statements quantify over, not about any lattice or continuum limit.

## Start snapshot

- Retained: `graph-tasks/evidence/2026-09-11-synthesis10-lean-review/start.json`
  (taken in `REPO` at `b9651bea`, before the 17-commit gap was closed).
  `snapshot_fingerprint` `a2579b06151ba8623abd5f643ac62a8c5cd27304502e2d80e49be9186c05afda`;
  input-manifest SHA-256 `a68b18001ffddc1415dc3c5efdb439a6f9c528006fe69341cd9f48062cf13bef`;
  freshness `matched`; mode `saved`; `executed: 0`, `cache_reused: 0`,
  `recorded: 611`; Lean `executed: false`, provenance `saved coverage`.
- **The 611 recorded checks are historical snapshot contents, not 611 fresh
  executions by this task.** This task executed no registered check.
- Because that snapshot predates 17 upstream commits, it cannot isolate this
  task's change. A same-revision baseline was therefore also retained:
  `baseline.json`, fingerprint `d31bcc593597e664...`, input-manifest
  `1f61251d4990abc3...`, taken at `0b667161` with `ledger/notes.yaml` at its
  committed bytes.

## Established inputs

Reviewed directly (read, not merely retrieved):

- `ARCHIVE/collections/05_LEAN/synthesis10_source/` — 71 `.lean` files, 6,315
  lines. Read in full: `RicciCurvature.lean`, `DriftCertificates.lean`,
  `ReflectionPositivity.lean`. Read structurally (imports, declaration forms,
  proof tactics, whole-tree greps): all 71.
- Inventory rows for these files in `notes/WORKHOUSE_FULL_2026-09-07.jsonl`.
  All 31 cited modules resolve to inventory digests, and **all 31 digests were
  recomputed from the archive bytes and matched** (`sha256sum` vs the inventory
  `digest` field).

Retrieved and read for status only:

- `ledger/symbols.yaml` — `t_n` (`values: ["5/612"]`, `claims: [R2]`) and
  `sigma_series` (`values` include
  `-137767222189182735950309/2009803206414863779920000`, `claims: [C5, R14, G7]`).
- `ledger/notes.yaml` verdict vocabulary and `src/workhouse/notes.py:validate`.

## Obligation

Exact statement investigated: *the 31 cited `synthesis10` modules establish, in
Lean, the analytic statements the synthesis documents attach them to.*

Finding: **refuted for all 31.** The statements do not quantify over the
objects of the analytic claims.

- Whole-library structural basis: across all 71 modules, **0** import
  `MeasureTheory`, `LieGroup`, `Topology`, `ContinuousLinearMap` or `Integral`.
  No module can therefore carry a measure, a Haar metric, a Riemannian
  curvature tensor or an unbounded operator. Occurrences of `SU(` (23 files)
  and `Haar` (16 files) are in docstrings and identifiers, not in types.
  Proof bodies are dominated by scalar arithmetic and identity: 51 `by linarith`,
  31 `by norm_num`, 16 `rfl`, and 17 proofs that return a hypothesis unchanged.
- Three statements read in full, quoted exactly in the proposal, are
  tautologies: `pairing_coercivity ... (h : pairing >= -c) : pairing >= -c := h`;
  `rp_pushforward_preservation (mu_rp : Prop) ... : mu_rp := h_rp`;
  `product_ricci_bound ... : kappa_G * v_sq <= kappa_G * v_sq := by linarith`.
- `RicciCurvature.lean:25` defines `ricci_constant_su (N) : Q := N / 2`, which
  **contradicts** the `kappa_G = N/4` the documents cite it to support, and
  `ricci_constant_su2 = 1` where `N/4` gives `1/2`.

Downstream consequence: the 31 files move from *inventoried, not yet reviewed*
to a recorded `set-aside` verdict, so the register answers the next agent that
meets these citations. No claim, symbol, gap or result changes.

Sub-claim confirmed rather than refuted, and recorded so it is not
over-read: the library contains **0** occurrences of `sorry`. One `axiom`
(`CarreDuChamp.lean`) and three `native_decide` modules (`HOTRGMethods`,
`HypercubicLattice`, `SixJSymmetry`) account exactly for the documents'
"67 of 71 clean" figure. The count is accurate; an empty statement proved
cleanly is still empty.

## Ownership

Files changed by this task, and only these:

- `ledger/notes.yaml` — 31 appended `reviews:` entries (append only; no
  existing entry altered).
- `graph-tasks/2026-09-11-synthesis10-lean-review.md` — this record.
- `graph-tasks/discovery/proposals/2026-09-11-synthesis10-lean-set-aside.md`.
- `graph-tasks/evidence/2026-09-11-synthesis10-lean-review/{start,baseline,end}.json`.

No archive file was read-modified; `ARCHIVE/` and `ALL THEORY/` were opened
read-only. No scientific source, claim, symbol, gap, result, generated index,
remote or PR was changed. `C:/WORKHOUSE/REPO` was left untouched apart from
its ignored `.graph-state/` snapshot directory.

## Work and checks

Commands executed, with outcomes:

| Command | Outcome |
| --- | --- |
| `workhouse brief R2 C5 R14 G7 --json --out .../start.json` | `status: ok`, `errors: []`, freshness `matched`, mode `saved` |
| `sha256sum` over the 31 cited `.lean` files vs inventory digests | 31/31 matched |
| `workhouse.notes.validate()` after the edit | **0 problems** |
| `from workhouse import results; results.load()` | ok |
| `from workhouse import derivation_statements as d; d._checked()` | ok |
| `workhouse status` | "Ledgers structurally sound." |
| `workhouse brief ... --out .../baseline.json` (committed bytes) | retained |
| `workhouse brief ... --out .../end.json` (after edit) | retained |

Isolation check: between `baseline.json` and `end.json`, taken at the same
revision `0b667161`, **the only differing input file is `ledger/notes.yaml`,
and the `targets` payloads are byte-identical.** This change records reviews
and alters no mathematical claim.

Limitations and unexecuted checks:

- No Lean was compiled. Nothing here reports the library as building or
  failing to build; the observation is that no `lakefile` sits beside the
  source (only a stray `lean-toolchain` under `synthesis10_config/`), so this
  checkout holds no evidence it has ever been built.
- Three modules were read in full; the other 28 rest on the whole-library
  structural facts above plus their own declaration forms. That basis is
  recorded in each entry's reason so a reviewer can disagree per file.
- Four modules (`HOTRGMethods`, `IntegrableGauge`, `NonPlaceholder`,
  `MaxwellOperator`) do use real `Matrix (Fin n) (Fin n)` types over R/C.
  They do finite linear algebra, which is still not the analytic statement;
  none of the four is among the 31 cited modules, and none is set aside here.
- 11,848 rows of `WORKHOUSE_FULL_2026-09-07` remain unreviewed. This task
  reviewed 31.
- No registered Python or Lean check was executed; both briefings ran in
  `saved` mode with `executed: 0`.
- `end.json` reports freshness `unknown`, the expected value for a fresh
  worktree with no `.graph-state/index-inputs.json`; it is not a staleness
  finding.

## End snapshot

- `graph-tasks/evidence/2026-09-11-synthesis10-lean-review/end.json`,
  fingerprint `db8ee9a4068a65d9...`, input-manifest `75aa6d49ec058ffd...`,
  revision `0b667161`, freshness `unknown`, mode `saved`, `executed: 0`.
- Changed input relative to the same-revision baseline: `ledger/notes.yaml`
  only, as shown above.

## Handoff

**Established.** The 31 `synthesis10` modules cited as formal support by the
2026-09-11 synthesis documents do not formalize the statements they are cited
for, and are now recorded `set-aside` with per-file reasons. A reviewer meeting
`Lean Support: BochnerBakryEmery.lean` in a future document can now see that the
register has read it.

**Not established, and explicitly not claimed.** Nothing here bears on whether
the underlying analytic arguments are correct — only on whether this Lean
library formalizes them. `M10` remains open; `G19` remains open; `SP20-SP24`
remain conditional. This task did not touch them.

**Separately recorded as out of scope for this change.** The same audit found
two source-level discrepancies that are *not* registrable as notes verdicts and
are left for a successor:

1. The documents quote `sigma_5` as
   `+137767222189182735950309/2009803206414863779920000` and call it the
   "physical-sign" value. The certificate's own
   `sigma5_exact_value_uvariate` field is **negative**, and `ledger/symbols.yaml`
   registers the negative value under `sigma_series`, consistent with its note
   that odd physical coefficients carry `(-1)**n`. The positive number is the
   reduced magnitude (`kps_exact` / `sigma5_reduced_value`). The registered
   value is correct; the documents' sign label is not.
2. The documents pin SHA-256
   `021558ce5bea60e43f757d76c1b8122f15f355c1e5174304f440cce5d98d422b` to
   `two_cube_b6_codd_o2_connected_kernel_certificate.json`. That digest is the
   **manifest's**; the certificate hashes to `bb6a51ef64de61f9...`, which is
   what the manifest itself records. Both artifacts are intact.

**Successor.** Review the remaining `05_LEAN` inventory rows, or close the
`workhouse notes --queue` backlog for `WORKHOUSE_FULL_2026-09-07` on a
higher-signal slice than this one.
