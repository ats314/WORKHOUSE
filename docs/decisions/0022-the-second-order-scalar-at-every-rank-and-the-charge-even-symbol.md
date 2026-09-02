# 22. The second-order scalar is closed form at every rank, and the charge-even symbol is a theorem

Date: 2026-09-02. Status: accepted. Discharges the second-order half of G25; bears on C13, G24 and R2; records one FINDING against revision 5 of the publication edition. Promotes nothing at fourth order.

## Context

Revision 5 of the publication edition proves the charge-odd second-order
hopping `t_N` at every rank and the charge-odd scalar at `N = 3` only, as the
upstream identification `d_- = 1/2 + 12 leak_2` with `leak_2 = ell_3`; its
Corollary (global torus assembly) names the scalar `d_{2,N,L}` and never
writes it down. It identifies the charge-even Bloch symbol with the unsigned
incidence as a hypothesis, on the ground that the vacuum-mediated route
reaches every pair of plaquettes and its cancellation "has not been derived".
And it states the even split of the link-resolved two-cube census as a
conjecture with a falsifier that would need a census at `N >= 4`.

The maintainer asked for the strongest paper the theory in this repository
can carry. The three inputs the hopping uses — the fusion table, the
plaquette-loop energies, the centre-charge process census — determine all
three of the items above, and nobody had carried the bookkeeping out.

## What was derived

`src/workhouse/invariants/second_order.py`, eight checks, all T1; the
arithmetic layer in `lean/Workhouse/Basic.lean`, fifty-five new theorems.

1. **The on-site second-order scalar, both sectors, every rank.**
   `d_2 = sigma_N + 1/C_F + 12 ell_N`, where `sigma_N` is the reduced
   same-face route and the rest is what the vacuum subtraction leaves of the
   other `3L^3 - 1` plaquettes: twelve adjacent neighbours at `A_N + B_N`,
   `3L^3 - 13` link-disjoint ones at `-1/C_F`, against `3L^3 (-1/C_F)` from
   the vacuum. `L` cancels and thirteen bubbles survive, which is why the
   per-neighbour leakage is `ell_N` and not the bare channel sum. For
   `N >= 5` the odd same-face route is `-N/((N-1)(N+3)) - N/((N+1)(N-3))`,
   the two denominators being the two-flux gaps, and the tower collapses to
   `-12N/((N^2-1)(N^2-9))`: the same-face route and the bubble, each
   `O(1/N)`, cancel at leading order. `N = 3` (`Lambda^2 F = Fbar`, retained,
   removed by `Q`) and `N = 4` (`Lambda^2 F` real, cancelling in the odd
   combination and doubling in the even) are exceptional and stated.
2. **The charge-even second-order symbol is `ell_N` times the unsigned
   incidence.** On a link-disjoint pair the vacuum route `2/E_F` is cancelled
   by the doubly-excited exchange route `2/(E_F - 2E_F)`, whose two vectors
   coincide in the even sector where in the odd one they are orthogonal. On an
   adjacent pair all four oriented monomials carry `+1/2`, so every channel
   enters with sign `+1` whatever the orientations: `A_N + B_N + 1/C_F`. The
   `Gamma` splitting `12 ell_N` and, for even `L`, the bandwidth `16|ell_N|`
   are unconditional at order `u^2`; the third order stays conditional on the
   domino ledger.
3. **The census split is the orientation bookkeeping of the shared-link
   theorem.** The like family is reached by two monomials at `+1/2` each,
   one placing `F (x) F` and the other `Fbar (x) Fbar` on the shared link,
   with the same Weingarten weight; the mixed channels are self-conjugate and
   add. So `c_rho = c_rhobar = w_rho/2` on the like channels and `-w_rho` on
   the mixed ones at every rank, merging into one entry at `N = 4`.

At `N = 3` every number specialises to the register and to the independent
chain-amplitude engine's second-order table (both same-face routes, the
leakage before and after the bubble, the disjoint-pair hop in both sectors,
the orientation-blind even hop); and the two-cube `B = 6` connected diagonal
is the per-neighbour ledger face by face, a second confirmation from a
Clebsch–Gordan lineage that shares nothing with that engine.

## What the review found

Five skeptics with distinct lenses, an independent symbolic recomputation and
a judge were run over the derivation before it entered the paper (ADR 0005:
record the review, not only the result). No number and no step was refuted.
Four things changed:

- **The distant-pair cancellation is the corpus's at `N = 3`.** The
  flat-band manuscript's lemma on the vacuum-mediated route and the June 2026
  patch to its Section 6 already state it with the same two numbers. Revision
  5's "has not been derived" and "remains a separate requirement" were stale
  against their own pinned corpus — the failure mode `AGENTS.md` names, this
  time committed by the paper and caught by the review. The all-rank operator
  statement is what is new; the paper now says so, and `FINDING: revision 5
  called the charge-even vacuum-route cancellation underived; the pinned
  corpus proves it for distant pairs at N = 3` records the discrepancy.
- The process-completeness lemma assumes `p != p'`; the diagonal case is
  argued in the proof, including the `N = 4` coincidence where `+-4 = 0 mod 4`
  is the real six of `su(4)`.
- The census proposition is phrased on orientation monomials, which
  survives the self-conjugate `N = 4` case.
- No engine independent of this derivation exists at `N >= 4`, and the paper
  says so: a Haar-exact or Clebsch–Gordan second-order run at `N = 4` would be
  the first genuine test beyond `SU(3)`.

## Decision

- **G25.** The second-order half is discharged: the charge-even symbol is a
  theorem at order `u^2`, unconditionally, and its Gamma splitting `12 ell_N`
  is a rank-uniform statement. What remains of G25 is the third order, which
  waits on G3 as before.
- **The paper.** Revision 6 is revision 5 patched in place by forty anchored
  replacements, each required to match exactly once, so the maintainer's text
  is preserved wherever a result did not change it. It carries the three
  results, the fourth-order state of ADR 0019–0021, ninety-five proof-checked
  statements with a `\leanref` tag on each, the regenerated radius-two figure,
  and a coverage appendix; every `\chk` label resolves under the guard.
- **The Lean count.** `FRONTIER.md` undercounted the T0 layer by three because
  its regex did not allow an attribute before `theorem`; it now uses the
  certified scrape's pattern.

Nothing here touches the fourth-order dispute. `C_shp` has three recorded
values and none is promoted.

## Consequences

- `src/workhouse/invariants/second_order.py`, registered last in the suite
  order; its yielded constants (`TOWER_2_ODD_N`, `FLAT_2_ODD_N`,
  `ONSITE_2_EVEN_N`, `GAMMA_A1PP_2_N`, the `N = 4, 5` values, the same-face
  routes) are catalogue nodes reachable by value.
- `ledger/theorems.yaml` carries an entry for each new theorem; the twelve
  that formalise the electric window and the Riesz island arithmetic point at
  the checks whose finite arithmetic they close.
- `paper/`: the edition, its build, `coverage_rev6.tex`,
  `make_figure_radius2.py` and the figure, all pinned; `make_coverage.py`
  escapes raw specials in inherited labels, byte-identically for the earlier
  appendices.
- The next bounded step this opens is the `N = 4` second-order run named
  above, and the one it leaves where it was is the corner cluster for G3.
