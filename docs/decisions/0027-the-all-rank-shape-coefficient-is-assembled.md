# 27. The all-rank shape coefficient is assembled: β_N from cluster cumulants at every rank

Date: 2026-09-04. Status: accepted. Bears on C2, C10, G14, R2; promotes the
corpus's all-rank fourth-order shape formula from output-certified to
re-derived at every rank it was stated for.

## Context

The corpus states the fourth-order shape coefficient at every rank as
`β_N = P17(N²)/(N R20(N²))`, boxed "for N ≥ 4" in GLUEBALL v3.1 with the
caution that it must not be substituted at N = 3, output-certified by the
all-rank program (`corpus-import/programs/y4_allrank`) and, in this
repository, transcribed into `channel_ledger` and read by two checks as a
claim. Nothing had ever re-derived it. ADR 0024 found that at N = 3 the
formula's value is what the cluster assembly gives once the historical
kernel's cube shortfall is corrected; ADR 0025 made the engine rank-generic;
ADR 0026 decomposed the two-hop weight. The remaining question was whether
the whole coefficient — pair clusters, dressings, corner, cube, two-hop
weight — sums to the corpus's formula at ranks above 3.

## What was computed

`runs/beta_n_from_assembly_2026-09-04`, N = 4..70. The pair cluster is the
plain Hermitian fourth order on the two-face cluster
(`loopcalc.pair_element`), exact for N ≥ 4: the first-order vertex
`⟨P̄|V|P⟩` is the determinant family `(3, 0)`, zero unless N = 3, and for
N ≥ 5 no fourth-order pair history reaches a determinant family, since a
baryon needs N fluxes and a history has four insertions and one initial
face. At N = 4 the `(4, 0)` family enters the pair element's Haar integrals
and the engine's determinant trick makes it infeasible there — about fifteen
thousand inner products at well over four seconds each; two attempts were
stopped after 23 CPU-minutes with none complete. It is also not needed at
any rank, because the pair cluster cancels (next section); at N = 4 the nine
other cumulants are computed and the pair entries are recorded as null. With
the dressings, corner and two-hop weight of the rank sweep and the
adjacent-face cube completion, in the kernel's `(0,2)` basis,

```
pi(N)   = pair_cop + 18 d_cop + 2 s_cop
rho(N)  = pair_perp + 14 d_perp + 2 s_perp + 2 corner − 106/(N(N²−1)³)
C(N)    = −alpha_N/8 − u(N) − (rho + pi)/2
beta(N) = 8 A_N + 16 C(N)
```

is `P17(N²)/(N R20(N²))` exactly, as rationals with denominators of up to a
hundred digits, at every rank from 4 to 70 (`certificate.json`, 67 ranks,
every `equal: true`). The stacked pair, a control, is exactly zero at every
rank where computed.

## The closed forms, and what drops out

`reconstruct_beta.py` finds, for each certified quantity, the lowest-degree
form `N^s g(N²)` through the first `dp + dq + 1` ranks that reproduces every
remaining rank (`closed_forms.json`). Three things fall out.

- **The pair cluster drops out of the shape coefficient.** The coplanar and
  perpendicular two-face clusters are one abstract graph up to conjugating
  one face: the shared link is traversed oppositely by the coplanar pair and
  in the same direction by the perpendicular one, and a bijection of the
  seven links (with reversals) carries one cluster's words onto the other's
  only by conjugating an odd number of faces. The engine's value depends only
  on that abstract graph, so the two pair elements agree entry by entry under
  `Q ↔ Q̄` (checked live at N = 5, all four entries), their C-even blocks are
  equal and their C-odd blocks are exact negatives — at every rank, whatever
  the determinant families do. `pair_cop(N) + pair_perp(N) ≡ 0`, so
  `(ρ + π)/2` never sees the pair cluster and `C(N)` is a sum of dressings,
  corner, two-hop weight and cube alone. The record confirms it at 66 ranks
  and as closed forms; at N = 3 the 2026-09-02 record's two pair values are
  equal in its conjugate basis, i.e. negatives in the kernel's.
- **The pair cluster's continuation has a double pole at N = 3**, coefficient
  `5/1088`: the PVP = 0 form's energy denominators degenerate exactly where
  the `(3,0)` determinant family — three fluxes on a link forming the
  singlet — becomes possible. This is the mechanism behind the corpus's
  "β_N's compact formula must not be substituted at N = 3": it is true of
  the pair cluster and false of β_N, because β_N never contains the pair
  cluster.
- **The symbolic identity.** The assembled β's closed form, `N⁻¹ g(N²)` with
  `g` of degree (17, 20), is determined by 38 ranks and confirmed on the
  other 28; `cancel(β_form − P17(N²)/(N R20(N²))) = 0`. This is the identity
  as rational functions, conditional on the assembled β being a rational
  function of degree at most (17, 20) in N², which the engine's structure
  makes plausible (every cumulant is a finite sum of Weingarten values,
  Fierz coefficients and resolvent energies, all rational in N once N exceeds
  the longest word on a link) but which no check proves. The rank-by-rank
  equality at N = 4..70 stands on its own.

The coplanar dressings have their own closed forms: single contact
`−2N³(N²−4)(10N²−13) / ((N²−1)³(4N²−9)²(2N²−1)²)`, the fan a (9, 12) form
in N², both confirmed on more than 40 held-out ranks.

## What it means

The corpus's all-rank shape coefficient is a sum of eleven cluster cumulants
per rank, each computed by an engine that reads no kernel, no engine and no
corpus formula, agreeing to the digit with a formula produced years earlier
by a different program with different primitives. Together with ADR 0024 the
formula holds at N = 3 as well, so the corpus's "separate exact SU(3) value"
and its determinant-sector explanation (trap 2 and trap 3 of the corpus
`CLAUDE.md`, C10) are retired: the fourth-order shape coefficient is one
rational function of N from N = 3 up, with no exceptional rank.

What is not claimed: the pair cluster is computed here only at N ≥ 5 (at
N = 3 the historical ledger, the 2026-09-02 assembly and their agreement are
the evidence; at N = 4 nothing computes it, and nothing needs it); and the
symbolic identity is conditional on a degree bound, as the previous section
says.

## Decision

- Three T1 checks in the all-rank suite: the structural one finds the link
  bijection and compares the pair elements entry by entry at N = 5; the rank
  one reads the pinned run at every rank and recomputes N = 5 end to end; the
  closed-form one re-evaluates every closed form at every certified rank,
  adds the two pair forms, and compares the β form with the corpus's as a
  rational function.
- C10 gains its closing note; G14 gains the statement that `β_N` is a sum of
  cluster cumulants; the register's all-rank entry is annotated.
- Adversarial verification before recording: five independent lenses
  (transcription of P17/R20 against the corpus, the rank-generic formula,
  the Haar-family premises, the assembly bookkeeping, independence of the
  two computations); their findings and the residual caveats are in the
  section below.

## Verification findings

Five independent skeptics, each told to refute the claim through one lens,
then a judge; all six ran before this ADR was written (the workflow's
transcript is not in the repository; what they established is restated here
as claims a reader can re-run). Verdict: **sound with caveats, nothing
refuted.** Recorded as a T1 pointwise check at N = 4..70, with the identity
as rational functions conditional as stated above.

What the lenses established, each by its own computation:

- *Transcription.* `P17` and `R20` parsed programmatically out of the v3.1
  appendix (sha256 `924d5b26…f254`, matching `theory/SHA256SUMS` and manifest
  row A02) are equal as sympy polynomials to `channel_ledger.P17`, `R20`;
  `beta_formula(N)` equals, as exact rationals, the June-2026 independent
  rerun kernels at N = 7..18, the low-rank table at N = 4, 5, 6 and the
  structured `P402/D409` expression at N = 4..40. The ledger's formula is the
  function the corpus's program produced, not merely the document's text.
- *Formula.* `C = −α_N/8 − u − (ρ + π)/2` is the Hodge form with `π̃ = π + 2u`,
  `ν̃ = ν + 4u` substituted; the carrier projection giving `A = −ν̃`,
  `B = D = 0`, `4C` = the coefficient of `R` is amplitude-free incidence
  algebra, hence rank-independent. Universality of the two-hop weight was
  verified on all 50 non-shared-link `S□²` keys (85 bridging cumulants) at
  N = 4, 5, 6; both cube completions at N = 5, 6, 7; the end-to-end Hodge
  assembly at N = 5, 6, 7 gives `B = D = 0` and `8A + 16C = β_N` exactly.
- *Haar families.* On the two-face cluster the whole `PVP` block vanishes for
  N ≥ 4 by charge counting, and at N ≥ 5 no fourth-order pair history reaches
  a determinant family (exhaustive enumeration of all 4⁴ insertion sequences,
  both geometries, N = 3..8); an instrumented `pair_element` at N = 5, 6 saw
  only the families (1,1), (2,2), (3,3), no determinant path, and `n ≤ 3 < N`
  so the Weingarten function is the exact inverse. Positive controls: at
  N = 3 the plain form is refused at the `(6,0)` family; at N = 4 it reaches a
  `(0,4)` family.
- *Bookkeeping.* An independent census at N = 5 of every plaquette sharing a
  link with each pair: 18 + 2 for the coplanar, 14 + 2 + 2 for the
  perpendicular, one value per class, the certificate's values in the `(0,2)`
  basis; the adjacent-face cube completion `−53/34560 = −106/(5·24³)` in the
  `(0,2)` traversal and `+53/34560` in `(2,0)`; the raw sums reassemble the
  certificate's `π`, `ρ`, `β` at N = 5 and, with the pinned N = 3 values,
  ADR 0024's `ρ`, `C` and `β_3`.
- *Independence.* `loopcalc` imports only the standard library (flint and
  sympy inside two functions), reads no file, carries no long literal; the
  corpus's `α_N` never enters the assembled side (`8A + 16C = −16u − 8(ρ + π)`
  identically); the multiplicities are lattice geometry, not fits; perturbing
  any of the six integer constants by ±1 breaks the equality at every rank,
  and solving for the cube coefficient from the corpus value returns −106.

Required fixes from the judge, and how each is met:

1. *No "for all N" without a degree bound.* The identity is stated above as
   pointwise at N = 4..70 and, as rational functions, conditional on the
   assembled β having degree at most (17, 20) in N²; the closed-form check
   says so in its detail line.
2. *Cite the completed record, not the README.* The claim rests on
   `runs/beta_n_from_assembly_2026-09-04/certificate.json` (67 ranks, every
   `equal: true`) and `console.log`; the README was ahead of its log while
   N = 4 ran and now is not.
3. *The N = 4 pathway, separately.* At N = 4 the pair cluster is not computed
   (infeasible, and cancelling); the nine other cumulants come from the rank
   sweep and this record's coplanar dressings, whose three-face words do
   reach `(4,0)` families, so N = 4 rests on the engine's determinant trick
   (pseudoinverse Weingarten at `n > N` plus the ε insertion), a path no lens
   audited. **N ≥ 5: agrees, path audited. N = 4: agrees, path unaudited.**
4. *Premises every lens took as given*, recorded as open routes on G14: that
   `D − ½{H₂, V₂}` is the correct Hermitian fourth-order effective
   Hamiltonian when `PVP = 0`; the rank-generic resolvent (`link_spectrum`
   roots, dropping the `E₀` component, vacuum intermediates) at N ≥ 5; the
   completeness of the eleven-cumulant decomposition at general N, which
   rests on the charge-counting argument alone; the on-site amplitude `σ`,
   which no lens checked (it enters only the constant).

Caveats the judge asked to be stated, stated:

- Independence is of values and code, not of framework. The Hodge form, the
  `8A + 16C` map and the engine's normalisations were fixed against the
  corpus's own N = 3 kernel records; N ≥ 4 is out of sample, but the choice
  of what to compute is corpus-derived.
- The corpus formula is output-certified only: its generator chain was never
  cold-regenerated end to end, the reduction `P402/D409 → P17/R20` is checked
  here only through the structured-expression note (its certificate is
  absent from the repository), and the walled-Brauer scripts and word data
  are not in the repository. Agreement is evidence for both pipelines, not
  proof of either.
- Universality of `u`, the cube closed forms and the class equalities were
  verified live only at N = 4..7 (the census at N = 5 only); higher ranks
  rest on the sweep's single representative per class.
- At N = 3 the assembly gives the formula's continuation value, which differs
  from the corpus's stated `β_3` by the `−25/64` the corpus attributes to the
  determinant sector and ADR 0024 to the historical kernel's cube shortfall.
  The identity claimed here is for N ≥ 4; N = 3 is ADR 0024's.
- A common bug in the engine's primitives would propagate identically into
  the census and the record; agreement with an independently produced
  eighteen-coefficient rational function at 67 ranks is the only guard.

Provenance of the corpus formula, in one sentence: `β_N = P17(N²)/(N R20(N²))`
is transcribed in `channel_ledger` (2026-08-30) from the v3.1 detailed
document (Appendix A and §11), verified coefficient for coefficient; it is
the "paper v0.8" reduction of the canonical `P402(N)/D409(N)` expression
produced on 2026-06-14 by the walled-Brauer stable-rank contraction program
(symbolic for N ≥ 7, exceptional-rank determinant-sector checks at
N = 4, 5, 6), output-certified by saved exact kernels but never
cold-regenerated end to end; the reduction certificate and the bulk
generator scripts are not in this repository.

## Consequences

- `loopcalc.pair_element`; the run record; the check; ledger notes on C10
  and G14; this ADR.
