# Task Record: 2026-09-10-r10-score-frame

## Identity
- **Task ID:** `2026-09-10-r10-score-frame`
- **Date:** `2026-09-10` (work continued past midnight local time into 2026-09-11 UTC)
- **Agent / Model:** Claude Code, Claude Fable 5.1 (`claude-fable-5-1`)
- **Checkout:** `C:\WORKHOUSE\worktrees\r10-score-frame-20260910` (task worktree of the canonical REPO)
- **Branch / Revision:** `claude/r10-score-frame-20260910 @ 3be5b0f9f9ee16ebdf751ae8a3a1551914a88059` (origin/main at start)

## Target
- **Graph IDs:** `G19`, `DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10` (priority 2 route), with `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10` read for scope only.
- **Objective:** A submitted derivation claimed `||A^(r)(g)||_(q_g->q_g) <= d_r g^(-r-1)`, r=0,1,2, for the complete R9 source/vacuum generator on the actual four-face square. Decide whether it closes R10; retain exactly what survives review.
- **Regime:** finite lattice (fixed twelve-edge compact square), positive coupling, fixed spectral window below the actual gap.

## Start Snapshot
- **Snapshot Path:** `.graph-state/r10-score-frame-20260910/start.json` (local, ignored; taken in the canonical REPO at the same revision)
- **Command:** `uv run --no-sync workhouse brief G19 --json --out .graph-state/r10-score-frame-20260910/start.json`
- **Fingerprint:** `57f146a85bfa101181f4f549d8d04462f55a670a726784528691702634164ad9`
- **Freshness:** saved snapshot; `workhouse brief --startup` reported "Saved graph: present; freshness not assessed". Not used as a current research basis beyond target identification.

## Established Inputs
- **Reviewed Sources:** `docs/derivations/w6-ground-jets-and-transport-budget.md` sections 1-5 (R1-R4, R8a-R8b, R9-R12; conventions, `chi_g=Omega'_g`, `h_g=1+e_g/gamma`, the rank-one `q_g` bound); `docs/derivations/w6-conditional-score-tail-control.md` (M6-M10, the dilated-score definition of `K_g`, M10 marked OPEN at line 486); `runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/compact_residual.md` C1-C2 (literal source projection, form-domain smoothness, transport ODE); `ledger/derivation_statements.yaml` records for R10 and M10; `ledger/gaps.yaml` G19 routes.
- **Dependencies:** `DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:GROUND_JETS` (R3, R4) is the only registered input the retained results rest on.

## Obligation
- **Investigated Statement:** R10 for the complete R9 generator `A(g) = [P'_g,P_g] + |nu_g><Omega_g| - |Omega_g><nu_g|`, `nu_g = chi_g - [P'_g,P_g]Omega_g`, in the energy operator norm `q_g -> q_g`.
- **Downstream Consequence:** R10 (or the direct R11 alternative) instantiates the conditional complete budget `M_j(s) <= c_j s^-j` (R11-R15) at the fixed-block scope. It does not supply interacting-volume constants.

## Ownership
- **Owned Files:** new `docs/derivations/w6-source-generator-score-frame.md`; anchored additions to `ledger/derivation_statements.yaml` (new `CITE:W6_SOURCE_GENERATOR_SCORE_FRAME` block with five statements; one sentence appended to the R10 record's `remaining`), `ledger/documents.yaml` (one alias), `ledger/gaps.yaml` (R10 route: two `depends_on` entries and one status paragraph), `docs/current_research.md` (one sentence group); regenerated `docs/derivation_formalization.md`, `index/*.jsonl`, `FRONTIER.md`, `CERTIFIED.md`; this record.
- **Shared Processes:** all regeneration ran inside this worktree with the canonical REPO's Python environment resolving this worktree's `src/` (verified by import path). No Lean, `runs/`, `theory/` or `paper/` changes. PR #136 (Codex, antipodal M10) was open and touches the same ledgers; this task appends anchored entries only. Ownership record: `C:\WORKHOUSE\navigation\tasks\2026-09-10-r10-score-frame.md`.

## Work and Checks
- **Review verdict:** the closure claim fails at six steps, recorded in section 6 of the new document. The decisive one: the argument invokes `sup_w Var(sigma_g|w) <= C g^-2` as "the score bound", which is a fiberwise statement stronger than the open M10 and is itself the open content; only the averaged bound (R4) is established.
- **Retained results (analytic, fixed positive g, T3):** SF1-SF5 ground-frame representation of the complete R9 generator, including the exact identification `nu_g = P_g chi_g = m_g(w) Omega_g` with `m_g = E[sigma_g|w] = (1/2) partial_g log h_g`; SF6-SF7 score Poisson equation `-(g^2/2) Delta_mu sigma_g = 4 g^-3 (V - <V>)` with purely magnetic forcing, `L_g[chi_g] = 4 g^-3 Cov(sigma_g,V)`, `integral K^0_g dnu_g <= 4 e_g h_g/(gamma g^2)`; SF7e exact fiber energy identity. Conditional: SF9, the r=0 case of R10 under H0-H4 with explicit `d_0`.
- **Commands Executed:** `workhouse brief --startup`; `workhouse brief G19 --json --out ...`; anchored patch script (each anchor asserted unique); `derivation_statements.validate` on the live ledger (no errors); `scripts/check_docs.py` (0 errors, 0 warnings); `scripts/render_derivation_coverage.py`; `workhouse index -w`; `workhouse frontier --write`; `workhouse certified --write`; focused pytest (see outcomes). Exact outcomes are appended below at closeout.
- **Outcomes:** `derivation_statements.validate` on the live ledger returned no errors and the five new `DERIV:` ids appear in the claim records. `scripts/check_docs.py`: 31 maintained files, 529 local links, 0 errors, 0 warnings. `render_derivation_coverage.py`: proof map now 28 documents and 222 statement groups (also refreshed the kernel theorem count, 400 to 431, which main's committed copy had drifted from). `workhouse index -w`: 17382 claims, 28 symbols, 29302 graph records. `pytest tests/test_research_priorities.py tests/test_graph_conformance.py`: 76 passed. `pytest tests/test_derivation_statements.py tests/test_frontier.py tests/test_certified.py tests/test_lean_dependencies.py`: 68 passed, 1 failed (`test_frontier_md_is_current`, because the first `frontier --write` ran from the wrong working directory and wrote an identical file into the canonical REPO, which it left unchanged); after regenerating `FRONTIER.md` inside the worktree, `test_frontier_md_is_current` and `test_certified_md_is_current` pass. `CERTIFIED.md` is unchanged by this task. Line endings of regenerated files normalized to LF.
- **Evidence Paths:** PR checks on GitHub for the pushed head; local logs kept in the session scratchpad only.
- **Unexecuted checks:** no Lean build (no Lean change); no full `make verify` (no invariant or scientific-check input changed); no numerical replay of the actual four-face model. A one-dimensional rotor check of SF6 was reported by the maintainer in chat and is not repository evidence.

## End Snapshot
- **Snapshot Path:** `.graph-state/r10-score-frame-20260910/end.json` (local, ignored)
- **Command:** `workhouse brief G19 --json --live --out .graph-state/r10-score-frame-20260910/end.json`
- **Fingerprint:** `84ef995bf9eb8de8a7b1f4f1c19f87e3f424be1a61b1fa88b7ff3e65ec372549`; status `ok`; 579 registered checks with provenance `cache_reused` (no fresh execution requested; no scientific check input changed). The fingerprint differs from the start snapshot because the ledgers and generated index changed.

## Handoff
- **Established Result:** the complete R9 generator is exactly expressible through the undilated ground score on level sets of `w`; the first ground jet is driven by the magnetic fluctuation alone; the order-zero R10 bound is equivalent in difficulty to five fiberwise conditional-energy estimates whose averaged forms hold.
- **Failed Attempts / Obstructions:** the submitted full closure of R10 is rejected (six recorded steps). Not a dead route: the failure is averaged-to-pointwise regularity on level sets of `w`, the same wall M10 names for a different score.
- **Successor Obligation:** `DERIV:W6_SOURCE_GENERATOR_SCORE_FRAME:CONDITIONAL_ENERGY_H0_H4`. Natural first attack: a fiberwise Poincare-type inequality for `-Delta_mu` on level sets of `w`, uniform in `g`, which with SF6 would give H1 and H2. Orders r=1,2 of R10 need a separate treatment because the second-jet forcing contains the electric term.
