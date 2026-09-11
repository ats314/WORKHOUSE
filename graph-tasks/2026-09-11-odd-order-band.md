# Task Record: 2026-09-11-odd-order-band

## Identity
- **Task ID:** `2026-09-11-odd-order-band`
- **Date:** `2026-09-11`
- **Agent / Model:** Claude Code, Claude Fable 5.1 (`claude-fable-5-1`)
- **Checkout:** `C:\WORKHOUSE\worktrees\odd-order-planar-20260911` (task worktree of the canonical REPO; the canonical checkout was on another agent's Codex branch with uncommitted Hodge-tetrahedral work and was left untouched)
- **Branch / Revision:** `claude/odd-order-planar-20260911 @ b33f47d2` (origin/main at start, PR #146 merged)

## Target
- **Graph IDs:** `G16` (rank-uniform control in τ = β/N³), with `G14` and `G6` read for scope.
- **Objective:** ADR 0046 left the odd orders of the band unexamined. Derive their rank dependence: is the third-order hopping `B_3` the SU(3) member of a rank-uniform series with its own N-power, and what does the planar limit do to odd orders?
- **Regime:** strong-coupling series of the one-plaquette sector on Z³, fixed order, finite clusters; every rank N ≥ 3. No statement about convergence or about β ~ N³ itself.

## Start Snapshot
- **Snapshot Path:** `.graph-state/odd-order-20260911/start.json` (local, ignored)
- **Command:** `workhouse brief G16 G14 G6 --json --out .graph-state/odd-order-20260911/start.json` (canonical REPO `.venv`, `PYTHONPATH` at this worktree's `src/`)
- **Fingerprint:** `ef17b89eb96ad52b7844bf84e4b35edba79e9dffdc098b79f13a4c54ebaeab48`; status `ok`; checkout clean at `b33f47d`
- **Freshness:** saved snapshot; `--startup` reported "Saved graph: present; freshness not assessed". Used for target identification only.

## Established Inputs
- `src/workhouse/loopcalc.py` (ADR 0024) and `src/workhouse/symbolic_rank.py` (ADR 0029): the third engine and its ℚ(N) form; `Cluster.second_order`, `resolvent`, `haar_link` (determinant families one step from balance), `_charge_zero`.
- `constants.py`: `B_3`, `LEAK_3`, `D_3`, `T3_EVEN`, `D3_ODD_DOMINO`, `D3_EVEN_DOMINO`, `VAC3_DOMINO`, `hopping`; the domino engine `corpus-import/programs/one_plaquette/ENGINE_FLUX_su3_domino_d3.py` read for the des Cloizeaux sign convention (`H(3) = −PWRWRWP + ½{PWR²WP, PWP}`, `V = −yW`).
- ADR 0046 and `runs/planar_band_2026-09-11`: the even-order N⁻⁽⁴ᵏ⁻¹⁾ law and the τ² series.
- Corpus statements read as claims: MASTER_THEORY §4.4 (SU(3) third order), GLUEBALL v3.1 §4 (exceptional ranks N = 4, 5, 6 at fourth order), NOTE_O4 §11 (τ).

## Obligation
- **Investigated Statement:** the rank dependence of every third-order band element (towers, hops, leakages, both sectors) and, once the N = 4 hop came out identically zero, the general vanishing theorem behind it and the first surviving odd order of odd N.
- **Downstream Consequence:** exact absence of odd τ-terms in the planar limit at every fixed order (G16); the SU(3) third order identified as a determinant-family effect; a third independent certification of the SU(3) third-order ledger.

## Ownership
- **Owned Files:** new `src/workhouse/invariants/odd_order.py`, `tests/test_odd_order.py`, `runs/odd_order_band_2026-09-11/*`, `docs/decisions/0047-*.md`, `paper/research_notes/ODD_ORDER_CENTRE_PARITY_20260911.md`, this record; anchored edits to `src/workhouse/invariants/__init__.py` (one module name), `runs/index.yaml` (one appended entry), `ledger/gaps.yaml` (G16 detail), `ledger/documents.yaml` (one alias), `ledger/results.yaml` (one RESULT), `paper/SHA256SUMS` (one pin), `docs/current_research.md` (one inserted section); regenerated `index/*.jsonl`, `FRONTIER.md`, `CERTIFIED.md`.
- **Shared Processes:** all Python ran with the canonical REPO's `.venv` and `PYTHONPATH` pointing at this worktree's `src/`. No Lean, `theory/`, `corpus-import/` or `ledger/derivation_statements.yaml` change.

## Work and Checks
- **Derivation:** the centre-parity theorem (link set T; even N: no odd order; odd N: none below order N − 2, and at N − 2 only the one-plaquette vertex `−(N/(N+1))^{N−3}/((N−3)!)²`), in the research note and ADR 0047.
- **Run:** `runs/odd_order_band_2026-09-11/derive.py`: N = 3..7 towers/hops/leakages at orders 1–3 in both sectors, the vacuum energies, the ℚ(N) third-order hops, the vertex at odd N ≤ 13, the link set on blocks up to 6³. N = 3 reproduces `B_3`, `T3_EVEN`, `LEAK_3`, `D_3`, both domino diagonals and the vacuum route −9/32; N = 4, 6, 7 all zero; N = 5 towers ±25/144, hops and leakages zero; ℚ(N) hops identically zero.
- **Suite:** "the odd orders of the band are determinant families (G16)", seven T1 checks (N = 3 and N = 4 word-engine elements, the character towers at N = 3..9, the N = 5 cheap pair elements and the symbolic hops live; the rest pinned). A one-plaquette character engine (Pieri rule, Rayleigh–Schrödinger per sector) was added because the word engine's five-box determinant families at N = 5 are too expensive; it agrees with the word engine at N = 3, 4, 6, 7.
- **Tests:** `tests/test_odd_order.py` (4 tests); `ruff check` and `ruff format --check` clean on the new files.
- **Not done:** no `DERIV:` statement group in `ledger/derivation_statements.yaml` (the note is registered as a document alias and a `RESULT:` with scoped `supported_by` controls); no Lean. Full `make check` / `make verify` and CI results are recorded in the pull request.

## End Snapshot
- **Snapshot Path:** `.graph-state/odd-order-20260911/end.json` (local, ignored)
- **Command:** `workhouse brief G16 G14 G6 --json --live --out .graph-state/odd-order-20260911/end.json`
- **Fingerprint:** `b78e42413b0824fcfe54d1214cc25a2d66f7ba29e99499a8836e8b730d91f6be`; status `ok`; 608 registered checks with provenance `cache_reused`, 0 executed for the request, 0 failed (the seven new checks had just been run by `workhouse verify` and `index -w`). Changed inputs since start: the owned files listed above only.

## Handoff
- **Established Result:** `RESULT:ODD_ORDER_CENTRE_PARITY`. The band is an even series in u for every even N at every order and for odd N through order N − 3; the corpus's SU(3) third order is a determinant-family effect; the first odd order of odd N is the one-plaquette vertex at order N − 2.
- **Failed Attempts / Obstructions:** the word engine's direct N = 5 one-plaquette third order (a (5,0) determinant family on four links, 5!³ ε-contractions per word) did not finish in 40 minutes and was abandoned for the character engine; the symbolic ℚ(N) engine cannot evaluate the odd-N vertex by design. The vertex is derived by Peter–Weyl and checked by characters at N = 3, 5, 7, 9 and by the word engine at N = 3.
- **Successor Obligation:** the even orders' N⁻⁽⁴ᵏ⁻¹⁾ law at k = 3 (G9) is untouched; the fifth-order vertex at N = 7, `−(7/8)⁴/(4!)²`, is confirmed by the character engine but not by the word engine; the overlap theorem G16 asks for is untouched.
