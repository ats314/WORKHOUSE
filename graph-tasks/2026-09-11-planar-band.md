# Task Record: 2026-09-11-planar-band

## Identity
- **Task ID:** `2026-09-11-planar-band`
- **Date:** `2026-09-11`
- **Agent / Model:** Claude Code, Claude Fable 5.1 (`claude-fable-5-1`)
- **Checkout:** `C:\WORKHOUSE\worktrees\planar-band-20260911` (task worktree of the canonical REPO; the canonical checkout held another agent's untracked Hodge-tetrahedral files and was left untouched)
- **Branch / Revision:** `claude/planar-band-20260911 @ 7cf8a646521259a34a772d65c8740ef7597f0265` (origin/main at start)

## Target
- **Graph IDs:** `G16` (rank-uniform control in τ = β/N³), with `G14` and `G6` read for scope.
- **Objective:** derive the large-N law of the whole fourth-order band from the exact ℚ(N) forms of ADR 0029 and the channel record of ADR 0031: is the corpus's `β_N ~ 6170/(9N⁷)` a per-channel bound or a cancellation, what is the planar limit made of, and is the band a series in τ with N-independent coefficients through fourth order?
- **Regime:** strong-coupling series of the kernel's (0,2) basis at fixed order, every rank N ≥ 3 (the closed forms are regular there); large-N asymptotics of exact rational functions. No statement about β ~ N³ itself.

## Start Snapshot
- **Snapshot Path:** `.graph-state/planar-band-20260911/start.json` (local, ignored)
- **Command:** `workhouse brief G16 G14 G6 --json --out .graph-state/planar-band-20260911/start.json` (run with the canonical REPO's environment resolving this worktree's `src/`)
- **Fingerprint:** `53c360a5f3b69f3c9c221727c4ab8763ef44afceaf5c52dec4316344e9459df6`; status `ok`; checkout clean at `7cf8a64`
- **Freshness:** saved snapshot; `--startup` reported "Saved graph: present; freshness not assessed". Used for target identification only.

## Established Inputs
- `runs/beta_n_symbolic_rank_2026-09-04/closed_forms.json` (ADR 0029): the sixteen cumulant forms of the β_N assembly and the assembled β_N, C_shp, ρ, π over ℚ(N); check "every cumulant of the beta_N assembly is one rational function of N computed over Q(N)…" (T1, rank_field suite).
- `runs/channels_symbolic_rank_2026-09-04/certificate.json` (ADR 0031): eight clusters, 1,772 nonzero channel forms, both sectors, each channel a pinned num/den record.
- `constants.py`: `antiparallel_sum`, `parallel_sum`, `hopping`, `alpha_pen`, `HOPPING_LARGE_N`; CLAUDE.md non-negotiable 4 fixes the canonical coupling `u = β_N/(2N)`.
- Corpus statements read as claims: GLUEBALL v3.1 §4 (`β_N ~ 6170/(9N⁷) + 677903/(324N⁹)`, `W₄ ~ 11930/(9N⁷)`), NOTE_O4 §11 (τ = β/N³ matched-scaling target), MASTER_THEORY §4.3 (t_N large-N).

## Obligation
- **Investigated Statement:** large-N order and leading coefficient of every fourth-order cumulant and of every resolvent channel; the planar decomposition of β_N; W₄/W₂ in τ; sign and monotonicity of the N⁷-scaled forms on N ≥ 3.
- **Downstream Consequence:** an exact strong-coupling side for G16 (series rank-uniform in τ through fourth order, with a named mechanism), a large-N prediction for the sixth-order clusters of G9, and the planar decomposition as a structural fact for G14.

## Ownership
- **Owned Files:** new `src/workhouse/invariants/planar_band.py`, `tests/test_planar_band.py`, `runs/planar_band_2026-09-11/*`, `docs/decisions/0046-*.md`, this record; anchored edits to `src/workhouse/invariants/__init__.py` (one module name), `runs/index.yaml` (one appended entry), `ledger/gaps.yaml` (G16 detail), `docs/current_research.md` (one inserted section); regenerated `index/*.jsonl`, `FRONTIER.md`, `CERTIFIED.md`.
- **Shared Processes:** all Python ran with the canonical REPO's `.venv` and `PYTHONPATH` pointing at this worktree's `src/`. No Lean, `theory/`, `corpus-import/` or `ledger/results.yaml` change.

## Work and Checks
- **Derivation:** `runs/planar_band_2026-09-11/derive.py` (exact sympy arithmetic; reversed-polynomial series division for the channel census). Findings in its README and ADR 0046: every cumulant O(N⁻⁷) in both sectors; channels O(N⁻³) with N⁻³ and N⁻⁵ totals identically zero in all 16 cluster/sector pairs; `6170/9 = −16(11/576) + 32(5/16) − 16(6197/576) + 848`; `W₄/W₂ = (11930/27)u²/N⁴ → (5965/54)τ²`; no real pole or zero at N ≥ 3; `N⁷β_N`, `N⁷W₄`, `N⁷corner` strictly decreasing to their limits.
- **Suite:** "the planar limit of the fourth-order band (G16)", five T1 checks; `workhouse verify --only 'planar limit' --only 'two orders cancel' --only 'hop cancels one order' --only 'N^-(4k-1)' --only 'planar limits'` → 5/5, about 7 s. The channel check re-sums and re-expands all 1,772 channel forms in the flint field, reading no total from the run.
- **Tests:** `tests/test_planar_band.py` (3 tests) pass; `ruff check` and `ruff format --check` clean on the new files.
- **Failed idea, retained:** a label rule for channel order fails on 47 labels (certificate `label_rule_failures`); not claimed.
- **Unexecuted checks:** no Lean build (no Lean change). Full `make check` / `make verify` and CI results are recorded in the pull request.

## End Snapshot
- **Snapshot Path:** `.graph-state/planar-band-20260911/end.json` (local, ignored)
- **Command:** `workhouse brief G16 G14 G6 --json --live --out .graph-state/planar-band-20260911/end.json`
- **Fingerprint:** `dcc8fe2b550ed9eb1ecc04fd5aedd172026f72edf32d28e04b827733a4700ac2`; status `ok`; 597 registered checks with provenance `cache_reused`, 0 executed for the request (the five new checks had just been run by `workhouse verify` and `index -w`). Changed inputs since start: the owned files listed above only.

## Handoff
- **Established Result:** the fourth-order band's N⁻⁷ is a two-order cancellation inside every cluster, not a per-channel bound; the planar β_N is the cube completion less a quarter from the corner; the band is a series in τ² with N-independent limits through fourth order.
- **Failed Attempts / Obstructions:** none blocking; the per-label order rule is false.
- **Successor Obligation:** test the N⁻⁽⁴ᵏ⁻¹⁾ law at k = 3 on the G9 sixth-order clusters (expected channel content N⁻⁵, coefficient N⁻¹¹); the G16 overlap theorem itself is untouched.
