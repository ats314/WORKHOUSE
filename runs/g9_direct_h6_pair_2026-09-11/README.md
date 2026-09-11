# Direct sixth order on actual clusters over Q(N): one face complete, the pair stages scripted — 2026-09-11

The open G9 route asks for the direct sixth-order effective operator on the
smallest connected multi-plane plaquette support, and ADR 0046 asks the same
clusters a sharper question: does the N⁻⁽⁴ᵏ⁻¹⁾ law hold at k = 3, with channel
content N⁻⁵ and three cancelled orders? This run builds the engine, certifies
it three ways, answers the k = 3 question on the one-face cluster exactly, and
leaves the two shared-link pairs as scripted stages.

## What is computed

`derive.py` runs from the repository root with the project environment. Stages:

| stage | what it does | status in this record |
|---|---|---|
| `validate` | at N = 11: the general Bloch recursion (`workhouse.sixth_order_cluster.bloch_hermitian`) equals the closed word formula (F6) of `G9_SIXTH_ORDER_COMBINED` entry by entry at orders 2, 4, 6 on one face; its order 2 equals `Cluster.second_order` and its order-4 block equals `loopcalc.pair_element` on both shared-link pairs; its C-odd, C-even and vacuum energies equal the character-basis engine (`workhouse.sixth_order_characters`) at every order 0..6 | executed, `validate.json`, 84 s |
| `single` | one face over Q(N): recursion, the seven pieces of (F6), the vacuum, the character engine, with the symbolic audit (largest Weingarten family, largest flux, resolvent denominators) | executed, `single.json`, about 8 minutes |
| `pair_perpendicular`, `pair_coplanar` | the two shared-link pairs over Q(N) through order six, both C sectors, hop and on-site elements, vacuum | **not executed** (hours over Q(N) at the current engine speed; see below) |
| `expand` | 1/N expansions of everything in the stage files | run on `single.json` only, by the suite |
| `certificate` | assembles `certificate.json` | not produced |

Three engines share the arithmetic of the answer but not its derivation:

- **the Bloch recursion** `K_n = P V χ_(n-1)`, `χ_n = D(V χ_(n-1) − Σ χ_(n-j) K_j)` with the canonical Hermitian metric `M^(1/2) K M^(-1/2)`: no `PVP = 0` assumption, no dropped odd order;
- **the word formula (F6)** in `A_m, B_m, C_2`, evaluated by resolvent powers so every Haar integral has a plaquette as bra — the engine that scales to a pair;
- **the character basis**: the plaquette holonomy as one Haar link, Pieri rules on mixed irreps `(λ; μ)`, Casimir energies. No loop word, no Fierz rewiring, no Weingarten function anywhere.

## Result

**On the one-face cluster the ADR 0046 law holds at k = 3, with the mechanism it named.**
Over Q(N), with V = +(χ_F + χ_F̄) (the `loopcalc` sign; even orders are convention-free):

| order 2k | odd − vacuum | even − vacuum | every (F6) piece | unsubtracted energy, vacuum |
|---|---|---|---|---|
| 2 | −12 N⁻³ − 120 N⁻⁵ … | −8 N⁻³ … | — | N⁻¹ |
| 4 | −152 N⁻⁷ − 6824 N⁻⁹ … | −120 N⁻⁷ … | — | N⁻⁵ |
| 6 | −(10388/3) N⁻¹¹ − (9505576/27) N⁻¹³ … | −2880 N⁻¹¹ … | N⁻⁵ (all seven; {A₃,B₃} vanishes by charge) | N⁻⁹ |

At sixth order the seven pieces of (F6) are each O(N⁻⁵); their sum is O(N⁻⁹),
equal to the vacuum's order, and the vacuum subtraction removes one more: the
cumulant is O(N⁻¹¹). Three orders cancel — N⁻⁵, N⁻⁷, N⁻⁹ — exactly "channel
content N⁻⁽²ᵏ⁻¹⁾, k orders cancel" for k = 3. The C-odd/C-even splitting at order
six is −(1748/3) N⁻¹¹.

The exact N = 11 one-face values (all three engines): H6 odd
= −36535503856137460933/955579482444166594560000000, vacuum
= −15692900201/1793652016665600000.

## Where it stops

- **The pairs are not computed to sixth order.** Over Q(N) the perpendicular pair's
  fourth order takes 71 s with the word formula; sixth order was still running
  after 40 minutes at integer rank and was stopped. The stages are written and
  their fourth order is validated against `pair_element`. To run them:

  ```text
  python runs/g9_direct_h6_pair_2026-09-11/derive.py pair_perpendicular pair_coplanar expand certificate
  ```

  Each stage writes its own JSON on completion, so the two pair stages can run in
  separate processes. The suite reads `pair_*.json` when present.
- **No SU(3) number.** Sixth-order words carry fluxes up to 8, so the Q(N) forms
  specialise to the per-rank engine for N ≥ 9 only; at N = 3 the pure-six and
  higher determinant families enter, which `loopcalc` refuses and
  `haar_epsilon` handles only for the pinned engine's states. The physical
  direct F = σ(H6) of the route remains open.
- The one-face result is a scalar on-site term; it constrains no q e₂/e₃ shape.

## Engine changes made for this run

- `loopcalc._project_link` applies each Lagrange projector to Krylov powers of the
  single-link H0 (H0 acts #energies times per group instead of #energies²); the
  factored form is kept as `_project_link_factored` and both agree exactly on every
  vector compared (tests).
- `symbolic_rank.Symbolic(min_rank=...)`: the flux audit threshold is a parameter
  (fourth order never reaches 5; sixth order declares 9). The label table extends
  to eight boxes; a monomial-denominator fast path in `RF`.

## Files

| file | what it is |
|---|---|
| `derive.py` | the computation, stage by stage |
| `validate.json`, `validate.log` | integer-rank agreement of the engines |
| `single.json`, `single.log` | the one-face Q(N) forms, pieces, vacuum, audit |

Reproduce the certified part: `workhouse verify --only 'one face over Q(N)'`
(suite "G9 direct sixth order on one face and the shared-link pairs, any rank").
