# 24. The corner cluster from a third implementation, and the historical ledger that was here all along

Date: 2026-09-04. Status: accepted. Closes the last untried route on G3 and
discharges G3; resolves C2; amends ADR 0021's reading of the assembled
rotation element; bears on C10, G14 and U5.

## Context

ADR 0021 assembled the fourth-order rotation element `ρ` from cluster
cumulants and found a value neither recorded kernel holds. Every piece was
validated on an agreed record except two that only a perpendicular
shared-link pair has: the corner cluster (three faces at a cube vertex) and
the cube completion between adjacent faces, `53/768`. The route it left open:
a third implementation of the corner cluster, or the historical pipeline's
own face-resolved ledger, "which this repository does not hold".

## What was built

`workhouse.loopcalc`, a Wilson-loop calculus written from scratch that shares
no primitive with the pinned engine: `H0` by the Fierz identity as a rewiring
of index ports (a like pair swaps wires, an unlike pair is cut and crossed,
which is unitarity); Haar integrals by the U(N) Weingarten function as the
Gram pseudoinverse on `S_n`, with `det U = 1` inserted as `εε` on virtual
slots for the determinant families; the resolvent by per-link irrep
projectors, so every component is an exact `H0` eigenvector with a known
energy. It climbs the whole validation ladder in seconds — the four
second-order constants, `u = X_QUANTUM` with the right sign on three chain
types, `u_even`, the single-contact and shared-link dressings — and then
gives the corner cumulant to the digit: `−2580244782961/398756546697600`
C-odd, `−56022878647/4153714028100` C-even, all four orientation entries
identical to the run's. The premise all three corner implementations share,
that the `E0` eigenspace is exactly the plaquette span, was verified
computationally on 224 dropped components.

`workhouse.stage3i`. A survey of the corpus for the historical ledger found
it: `DATA_Y4_stagei_authority_fixture.xz.b85` decodes to the Stage-3I ledger
of 4,221 ordered words whose gzip hash is the `stage3i_input` the kernel
copies quote, and Stage 3J's rooted assembly, ported verbatim, turns it into
the pinned 189 records exactly. Grouping each word's rooted images by the
set of plaquettes it touches gives the historical kernel's own connected
cumulants — a reading Stage 3J never did.

`workhouse.cellular.c_full`. Every cube link lies in exactly two faces, so
once both are present its adjoint component can never return to the target;
the exact cube completion is the primitive law extended to multi-loop
intermediates. The adjacent-face term is `−106/(N(N²−1)³)`: the primitive
`−88` (the off-axis run's `S_4 = −11`) plus ten multi-loop orderings at `−18`.
At `N = 3` that is `−53/768`, the run's number, now also from the third
engine with the full `H0` dynamics.

## What was found

1. **The historical kernel and the assembly agree on every cluster of the
   rotation record but one.** Pair, fourteen chains, two fans, two corners:
   identical rationals in both sectors. The corner cumulant is therefore the
   historical pipeline's own number as well as three implementations'.
2. **The one difference is the adjacent-face cube completion**, `−31/1536`
   in the historical ledger against `−53/768`. The ledger holds 8 of the 24
   insertion orderings, each with exactly the weight the multi-loop model
   assigns it (`2, 1, 4, 2, 8, 8, 2, 4` in units of `1/1536`); the sixteen it
   lacks sum to `−25/512`. The opposite-face completion in the same ledger has
   all 24 orderings. This is an enumeration shortfall of the June-2026
   pipeline, localised to one cluster.
3. **ADR 0021 read `ρ` in the conjugate basis.** All 24 cross-plane records
   equal `ρ` times the x-then-z `L↓` incidence, `+1` on `xy(0) → xz(0)`; the
   second-order hop in that traversal is `+5/612 = t_3 · (+1)`; and every
   C-odd component of the historical ledger is the negative of the run's
   `(2,0)`-traversal value while every C-even one is identical — the
   signature of conjugating the `(0,2)` face and nothing else. So in the
   kernel's basis `ρ_assembled = −RHO_CLUSTER = −0.0405972`, and
   `ρ_historical − ρ_assembled = 25/512`, the cube term alone.
4. **In the kernel's basis the assembled `C_shp` is `C_historical + 25/1024`
   = `−13035490122347/550663802582400 = −0.0236723`.** Put into the 24 records
   and solved over the whole zone, `A = 5/48`, `B = D = 0`, no residual. This
   is the rational the register already holds as `C_SHP_CONTINUATION_SHIFTED`
   — the value the all-rank `β_N` formula gives at `N = 3`, whose derivation
   by continuation was retracted on 2026-08-30 because the substitution is
   forbidden. The retraction stands; the number the forbidden route produced
   is the one the assembly reaches. The corpus's "determinant sectors shift
   `C` by `−25/1024` at `N = 3`" (C10, trap 3 of the corpus `CLAUDE.md`) is
   this shortfall, on a cluster that has no determinant sector; and U5's
   predicted `Δ(ρ + π̃) = −25/512` is realised as the historical kernel's
   shortfall, not as the ε-sector, which the 2026-09-02 run measured at
   `−55/6936`. U5 stays refuted on its stated mechanism.

## Decision

- **G3.** The route "the corner cluster from a third implementation, or from
  the historical pipeline's own face-resolved ledger" is `done`, by both
  halves at once.
- **C2 is resolved.** The fourth-order off-axis coefficient is
  `C_SHP_HISTORICAL + 25/1024 = −13035490122347/550663802582400`, and both
  recorded kernels are wrong on `ρ` — the historical by sixteen missing
  cube orderings, the cold dump on `u`, `π` and `ρ` alike. The session
  first left the status flip to the maintainer, since non-negotiable 2
  reserves adjudication; the maintainer's answer the same night was to make
  the common-sense decision and proceed. What the rule prevents —
  adjudication by preference or by the look of a rational — is not what
  happened here: every component but one is the historical pipeline's own
  number, and the one is explained ordering by ordering. So the ledger
  marks C2 `resolved` and G3 `discharged`, the registry's two `disputed`
  entries become `superseded` (historical) and `falsified` (v10a.26)
  beside a `proven` entry for the assembled value, the 2026-09-02 reading
  is marked superseded, and the rule files say what closed it. Nothing is
  deleted: the sides stay listed, as C1's and C15's do.
- **G14.** The adjacent-face completion has a closed form at every rank,
  `−106/(N(N²−1)³)`, ratio `53/80` to the opposite-face `−160`; the Hodge
  form's single weight on `L↑` is confirmed to be a reparametrisation.
- **ADR 0021** is amended, not withdrawn: the assembly was right, its basis
  was not. The check "C_shp from the assembled amplitudes is a third value"
  keeps verifying the certificate's arithmetic and says so in its detail.

## Consequences

- `src/workhouse/loopcalc.py`, `src/workhouse/stage3i.py`, `cellular.c_full`;
  `tests/test_loopcalc.py`, `tests/test_stage3i.py`.
- Suite "the third implementation and the historical ledger": nine T1
  checks, three of them `FINDING`s; yields `CUBE_COMPLETION_ADJACENT_4`,
  `CUBE_COMPLETION_ADJACENT_N`, `CUBE_COMPLETION_ADJACENT_HISTORICAL_4`,
  `PAIR_CORNER_DRESSING_EVEN`, `RHO_ASSEMBLED`, `C_SHP_ASSEMBLED`.
- `runs/g3_corner_third_implementation_2026-09-04/`: all 58 three-cluster
  cumulants of the three pairs from the third engine, the cube completion in
  both bases, the multi-loop closed form, the reassembled ledger by cluster,
  the assembled element in the kernel's basis.
- Lean: `cubeCompletionAdjacent` with its split and `N = 3` value, the cube
  shortfall `25/512`, and the `C_shp` shift identity.
- Ledger: C2 sides and note; C10 and U5 notes; G3 route and next steps; G14
  note; two symbols.
