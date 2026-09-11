# CASE balaban-contraction (2026-09-11)

Reviewer label: `balaban-contraction`. Worktree `C:/WORKHOUSE/worktrees/discovery-agents-20260911`
(branch `claude/discovery-agents-20260911`, revision fdaadc40). Briefing retained at
`.graph-state/case-balaban-contraction/brief.json` (snapshot mode saved, freshness unknown,
579 recorded checks, 0 executed). Scratch register: `scratchpad/cases/balaban-contraction/register`.
Nothing under any scientific tree was written.

## 1. Question

`RESULT:BALABAN_MULTISCALE_CAUCHY_SUMMABILITY` (ledger/results.yaml:26-40) takes
"Contraction factor lambda = 1/9 <= 1/2 at each renormalization scale step" as its hypothesis;
`docs/research/graph-priorities-2026-09-10.md:39-45` says the dimension-five lemma alone does not
prove an L^-2 bound in the actual polymer derivative norm; EX-014 section 1 proves the analogous
cascade gain is C_RG = 1 for decimation and C_RG <= (1+O(r))/L^d only in the linearised
small-field chart for Karcher averaging. Which block map does the manuscript use for (6.10)/(7.6),
and is the L^(-2k) factor a proved gradient-intertwining contraction for that map on large-field
cells, or a power-counting statement? Sub-checks (i)-(iv) below.

## 2. The excerpts compared

**A (seed source).** `paper/research_notes/G19_DIMENSION_FIVE_IRRELEVANCE_LEMMA_20260910.md:206-234`
(file sha256 `6bf12c1d31e21d3e58a28ee53f7057b38e11a1495ffef9875763045e6c331510`).
Section 5 states the canonical scaling of a local operator's action contribution,
`Delta S_{k+1} ~ a_{k+1}^4 O_d = L^4 a_k^4 L^{-d} O_d = L^{-(d-4)} Delta S_k`, hence
`rho(6) = L^{-2} = 1/9` for L = 3, and Theorem 3 (lines 222-234) then asserts, without further
argument, `||K_{k+1}(single)|| <= L^{-2} ||K_k|| = (1/9)||K_k||`, "discharging equation (6.10)".
Section 6 (Theorem 4) asserts `|<O>_{k+1} - <O>_k| <= C_1 L^{-2k} g_k^2 + C_2 |g_{k+1}^2 - g_k^2|`.
Regime: continuum R^4, SU(N), the polymer Banach norm (6.3)-(6.4) of the manuscript; observable =
smooth gauge-invariant cylinder expectation.

**B (imported note).** `notes/imported/EXTRACT_2026-09-01/EX-014-rg-schur-riccati.md:41-121`
(file sha256 `fc55bb4934560183d5529822693ce7ad90ca9bc6f521546cb505d8e30f6cc703`), in particular
lines 47-58 (hypotheses A1-A3, conclusion `C_P^(n) <= L^2 C_RG C_P^(n+1) + C_block`), lines 80-96
(STEP 5: decimation `C_RG = 1` exactly; STEP 6: Karcher averaging `C_RG <= (1+O(r))/N`; STEP 7:
contraction iff `C_RG < L^{-2}`), line 116 (caveat: A2, A3 are hypotheses, not theorems), and
obstruction O3 at lines 839-893 (decimation cannot contract; averaging contracts only in the
linearised small-field chart). Regime: finite lattice `Lambda_n subset Z^4`, compact group
G = SU(2), Gibbs measure, Dirichlet form / Poincare constant, block-spin conditional expectation
`P f(V) = E[f | pi_n(U) = V]`.

**C (manuscript).** `docs/derivations/yangmills-continuum-balaban-multiscale-proof.md`
(file sha256 `55296902489318e28594a61d9fefc422a6b879a5c747751622bbbe353cddf711`):
Definition 3.1 (3.2)-(3.3) block map; Lemma 3.2; (3.7)-(3.9) minimiser constraint; Definition 4.1 and
Theorem 4.2 (lines 157-180); Definition 6.1 (6.3)-(6.4) norm; Theorem 6.2 lines 269-295 with
(6.9)-(6.10) at 286-292; Theorem 7.1 lines 317-340 with (7.5)-(7.6); repair record lines 561-586.

**D (September audit of B).** `paper/research_notes/G19_CONDITIONAL_GRADIENT_REPAIR_20260905.md`
(sha256 `429d4acecb762bf89b9523258ef5223ec6e4da45f1e66d03a826339680bf5e49`), sections 1 and 4,
registered as `RESULT:CONDITIONAL_GRADIENT_REPAIR` (status proven, evidence analytic, T3).
It cites B by the same sha256 and refutes B's STEP 6 direction.

Also read in full or at the cited sections: `G19_BALABAN_BLOCKING_REFLECTION_POSITIVITY_20260830.md`
(Lemma 2.1, Lemma 3.1, Proposition 4.1), EX-013 section 7 (lines 405-451), EX-014 section 3 caveat
and section 7 scope note, `docs/validation/wilson-g19-cauchy-repair.md` sections 1-3,
`ledger/gaps.yaml:895-912` and the live G19 plan step near line 1245,
`ledger/derivation_statements.yaml:2841-2930`, `ledger/documents.yaml:38-43, 371-376, 1124-1150`,
`src/workhouse/invariants/dimension_five_irrelevance.py`.

## 3. Findings on the four sub-checks

### (i) The norm, the block map, and the step that converts "no dimension-5 operator" into the norm bound

* **Norm.** Definition 6.1: `||K||_{rho_k,kappa_k} = sup_{Delta_0} sum_{X ni Delta_0} e^{kappa_k|X|}
  ||K(X,.)||_{C^n(Omega_s(X))}` with `||K(X,.)||_{C^n} = sum_{j<=n} rho_k^j/j! sup_{A in Omega_s(X)}
  sup_{||phi_i||_{L^2}<=1} |D^j K(X,A)[phi_1..phi_j]|`. Test directions are continuum L^2(R^4)
  functions at every scale; the domain is the small-field set only.
* **Block map.** Definition 3.1: `(Q_{B_k} z_k)_mu(x_Delta) = |Delta|^{-1} int_Delta
  Omega(x_Delta,y;B_k) z_{k,mu}(y) Omega(y,x_Delta;B_k) dy` on each coarse cell Delta of side
  `a_{k+1} = 3 a_k` (N = 81 fine cells), then scalar partition-of-unity interpolation (3.3). It is a
  deterministic, background-transported, barycentric (centered) arithmetic average of the adjoint
  fluctuation, linear in z_k for fixed B_k, and exists only through the small-field decomposition
  `A_k = B_k(A_{k+1}) + z_k` (3.6). The minimiser constraint (3.7)-(3.9) still uses the straight-line
  connection average `Q_k` of the full connection, which is not equivariant (Lemma 3.2 part 2).
  Lines 574-577 fix the design as deterministic, citing Proposition 4.1 of the RP note.
* **The converting step does not exist in either document.** In the manuscript, (6.10) is a polymer
  cell-count factor: a coarse polymer X has at least `L^4|X| = 81|X|` fine cells, so the weight
  `e^{kappa|X|}` changes and `sum_{X' supset X} e^{-(kappa_k L^4 - kappa_{k+1})|X'|} <= L^{-4} <= 1/81 < 1/2 = lambda`.
  After the `delta = 0` repair (`kappa_{k+1} = kappa_k`) the displayed inequality is asserted, not
  derived; either way it is an entropy statement about the weight, not a derivative bound and not a
  property of the block map. The repair record (579-586) replaces it: "the residual should be
  irrelevant with gain L^-2, because pure Yang-Mills carries no dimension-five ... operator", called
  "an operator enumeration plus power counting". The G19 note supplies exactly that: section 5 is
  canonical-dimension scaling under `x -> Lx`; Theorem 3 restates it in the norm with no computation
  of `D^j K_{k+1}` from `D^j K_k`, no choice of `rho_{k+1}/rho_k`, no treatment of multi-block
  polymers, and no covariance scaling. **The L^(-2k) factor is a power-counting statement**, in
  agreement with graph-priorities lines 39-45 and the route text at gaps.yaml:895-912.
* **Even granting Theorem 3, the seed's hypothesis is applied to the wrong sequence.** (6.5) has the
  forcing term `C_ind g_k^2` (regeneration of dimension-6 operators by the one- and two-loop graphs).
  The manuscript's own (6.14), `||K_k|| <= lambda^k ||K_0|| + C_ind sum_{j<k} lambda^{k-1-j} g_j^2`,
  with lambda = 1/9 and g_k^2 from (6.12) (b_0 = 11N/48pi^2, N = 3, L = 3) gives
  `||K_k|| -> (9/8) C_ind g_k^2 = O(1/k)`: scratch script `check_614_recursion.py` reports
  `K_k/g_k^2 = 1.28, 1.21, 1.15, 1.14, 1.13` at k = 1, 10, 50, 100, 200 and `K_k * k = 6.6, 7.0, 7.2`
  at k = 50, 100, 200, partial sums 7.2, 16.5, 21.2, 26.1 at n = 10, 50, 100, 200. The G19 note's
  Theorem 4 replaces this by `C_1 L^{-2k} g_k^2`, which would need `C_ind = 0`. So the geometric tail
  bound `sum_{k>=j} lambda^k <= 2 lambda^j` is a true arithmetic identity about a sequence that the
  manuscript's (6.5) does not produce; the (7.6) increment stays O(g_k^2), which is the non-summable
  defect wilson-g19-cauchy-repair.md section 1 already recorded.

### (ii) The (A3) constant of the manuscript's map outside the small-field region

* On any cell where `A_k = B_k + z_k` is defined, `z -> Q_{B_k} z` is a transported arithmetic
  average over N = L^4 = 81 sub-cells; adjoint transport is unitary, so in the flat adjoint chart the
  pullback satisfies `|grad_z (F o Q)|^2 = (1/N) |grad_Y F|^2` -- this is EX-014 STEP 6's number with
  N = 81 instead of 16.
* `RESULT:CONDITIONAL_GRADIENT_REPAIR` section 1 (lines 11-40) shows that this 1/N belongs to the
  pullback `F o B`, whereas the (A3) hypothesis bounds the gradient of the conditional expectation
  `Pf`, whose sharp constant for arithmetic averaging is 1 in the quotient metric `B B*` and m = N in
  the raw coarse metric (attained by f = y). Section 4 (lines 139-160): the physical rescaling gives
  coefficient `m/L^2` (= 81/9 = 9 for the manuscript's L = 3, d = 4), not `L^2/m`; "correct physical
  rescaling does not create a geometric contraction". Hence, correctly oriented,
  **C_RG(Q_{B_k}) = 1 in the quotient metric, the same as decimation, in every chart**; the
  block-map-gradient route yields `r = L^2 C_RG = 9 > 1`, no contraction.
* Outside the small-field region the map is not defined on z_k at all: Definition 4.1's large-field
  condition (`|F| > g_k^kappa a_k^{-2}` or `|z_k| > g_k^{-kappa'} a_k^{-1}`) routes the cell through
  Theorem 4.2's action damping `exp(-c_lf g_k^{-epsilon_0}|Y|)`, whose Case 1 constant is stated
  (line ~166) to be supplied by "the irrelevance lemma of the repair record ... together with its
  L^-2 gain". So on large-field cells there is no gradient-intertwining bound; there is a damping
  bound that is itself conditional on the same power-counting lemma (Theorem 4.2 <- lemma;
  Theorem 6.2 <- Theorem 4.2 and lemma; Theorem 7.1 <- Theorem 6.2).
* EX-014's own caveats apply to any transfer: section 3 is Euclidean R^n x R^m and supplies no chart,
  gauge quotient or exponential-map Jacobian for a compact group; section 7's lemma is stated not to
  apply to Wilsonian blocking; A2 and A3 are hypotheses, not theorems (line 116).

### (iii) Is the averaging-constraint defect the EX-013 section 7 obstruction? No.

* EX-013 section 7 (= EX-014 O4): no Markov kernel Pi can be both a conditional expectation onto
  gauge-invariant block variables (A5) and gauge-covariant (A4), because the fixed set of the coarse
  gauge action on `G^{E(Lambda_{a'})}` is empty. Its escape (1) is a deterministic, covariant but not
  invariant blocking map -- exactly Balaban's `P(U)` and the manuscript's `Q_{B_k}`.
* The manuscript's open defect (lines 561-577) is different: (a) (3.7)-(3.9), (3.11), (4.7), (5.3),
  (5.5) use the straight-line connection average `Q_k`, whose equivariance fails through the
  inhomogeneous term `-(partial g) g^{-1}` (Lemma 3.2 part 2, check `_connection_average`, residual
  1/16) -- a covariance failure of a deterministic map; (b) the scalar partition-of-unity
  interpolation (3.3) adds adjoint values living at different barycenters without transport
  (`_adjoint_interpolation`, the `T_3` / `Ad(g_2)` counterexample sending the penalty density from 1
  to 0). Neither (A4)+(A5) is in play; the map is deterministic, and lines 574-577 keep it so because
  of Proposition 4.1 of the RP note, which is a third, distinct no-go (reflection-equivariant Markov
  blocking does not preserve reflection positivity).
* Verdict: EX-013 section 7 is consistent with, and motivates, the deterministic choice; it does not
  describe the equivariance defect of the connection average or of the interpolation kernel.

### (iv) Status texts (reported, not edited)

See section 7 below.

## 4. Proposed relationships in the closed vocabulary (scratch register)

| review id | seed -> target | kind | state | reason in one line |
| --- | --- | --- | --- | --- |
| `2026-09-11-seed-vs-ex014-s1-037d31` | `RESULT:BALABAN_MULTISCALE_CAUCHY_SUMMABILITY` -> `EX-014...md:41-121` | shared-operator | **rejected** | different objects: polymer-norm lambda supplied by power counting vs Poincare-cascade gradient constant C_RG of a finite-lattice conditional expectation; neither argument uses or restricts the other |
| `2026-09-11-thm62-vs-ex014-o3-555462` | `DERIV:...:THEOREM_6_2` -> `EX-014...md:839-893` | scope-restriction | **rejected** | Theorem 6.2's lambda is not a block-map gradient constant ((6.10) is cell counting, replaced by power counting); O3 closes one route to lambda but attaches no small-field restriction to (6.5); the map is undefined on large-field cells |
| `2026-09-11-condgrad-vs-ex014-s1-d681f7` | `RESULT:CONDITIONAL_GRADIENT_REPAIR` -> `EX-014...md:41-121` | disagreement | **established** | same object (the (A3) constant of a linear averaging block map in the flat chart), contradictory value: EX-014 gives (1+O(r))/N, the September note proves 1 (quotient metric) or m (raw metric) and refutes r = L^2 C_RG = 1/4 |

Proposal fragments emitted (read): `proposal-condgrad-ex014-documents.yaml` and
`proposal-condgrad-ex014-results.yaml`. The tool's FILL placeholder resolves to the catalogue id
`NOTE:EXTRACT_2026-09-01:ex-014-rg-schur-riccati-md-fc55bb` (index/graph.jsonl:1113, 22613-22614).
The documents surface is the right one: `ledger/documents.yaml` alias `CONDITIONAL_GRADIENT_REPAIR`
(line 371-376) already says in prose "Corrects the EX-014 averaging direction and scale conversion"
but carries no `bears_on` to that NOTE id; the results surface has no disagreement field (tool note).
Checklist items hypotheses_compared / regime_stated / normalization_compared /
independence_of_origin_checked / falsifier_stated are answered in the established reason and here:
falsifier = a linear test function f = y (or any nonconstant linear pullback) for which
`|grad_y Pf|^2 <= (1/m) E[|grad_x f|^2 | y]` holds in the raw coarse metric; the September note shows
it fails with constant m. Independence of origin: D is a September derivation that cites B; it is
not copied prose.

## 5. Existing graph witnesses

* Seed: outgoing `depends_on RESULT:DIMENSION_FIVE_OPERATOR_IRRELEVANCE`, `supported_by` two CHK
  nodes (`multiscale-cauchy-expectation-increment--62b2b1`, `hypercubic-anisotropic-directional-varia-442910`),
  `cites CITE:G19_DIMENSION_FIVE_IRRELEVANCE`, `bears_on G19`; no incoming edges. Both CHK nodes
  compute arithmetic only (3^-2 = 1/9 < 1/2; sum 9^-k = 9/8; lim (1/9)^k = 0).
* `DERIV:...:THEOREM_7_1` (status open) has no edge to the seed; the priority-5 route at
  gaps.yaml:895-912 targets THEOREM_7_1 and `depends_on RESULT:COMMON_SPACE_CONTRACTIVE_DRIFT`.
* EX-014 NOTE node: `bears_on G19, G23`; incoming `bears_on` from
  `CITE:SEPT_DOC_NEXT_PATH_WILSON_TRANSFER_2026_09_08_09f54613`; `contains` from
  `ARCHIVE:EXTRACT_2026-09-01`. No edge from `CITE:`/`RESULT:CONDITIONAL_GRADIENT_REPAIR`.
* Pair dossiers A-D: registered relations none in every case.

## 6. Exact next check (one hour)

1. **Forcing-term check (already reproducible).** Iterate the manuscript's (6.14) with lambda = 1/9
   and (6.12) for k <= 200 (`check_614_recursion.py` in this directory) and substitute into
   (7.5)-(7.6). Observe `||K_k|| -> (9/8) C_ind g_k^2 = O(1/k)` and a logarithmically divergent
   telescoped tail. This settles that Theorem 4 of the G19 note does not follow from Theorem 3 plus
   (6.5) unless `C_ind = 0`; the seed's hypothesis is therefore not the hypothesis Theorem 7.1 needs.
2. **Hypothesis comparison in the norm.** Write `D^1 K_{k+1}(X', A_{k+1})[phi]` from (7.4) with
   `A_k = B_k(A_{k+1}) + z_k`; the chain rule passes through `DB_k(A_{k+1})[phi]`, the derivative of
   the minimiser map (a coarse-to-fine injection) whose `L^2(R^4) -> L^2(R^4)` operator norm is O(1)
   under the continuum normalisation of (6.4), not L^-2. Check whether any `rho_{k+1}/rho_k` is
   specified in the manuscript or the G19 note that would produce the factor L^-2 in
   `||.||_{rho,kappa}`; none is. If none, Theorem 3's `||K_{k+1}(single)|| <= (1/9)||K_k||` has no
   derivation in that norm and should stay a power-counting heuristic.

## 7. Registration inconsistencies noticed (outputs, not tasks)

1. Manuscript lines 584-586 ("is not yet in this repository") and the live G19 plan step in
   gaps.yaml near line 1245 ("it is not in this repository", `closed_by: []`) versus
   `ledger/documents.yaml:38-43` (alias `G19_DIMENSION_FIVE_IRRELEVANCE`, standing repo) and
   `ledger/results.yaml:7-40` (two RESULTs, status proven) registered on 2026-09-10.
2. `RESULT:BALABAN_MULTISCALE_CAUCHY_SUMMABILITY` proven with `bears_on G19`, and the G19 note's
   summary table marking Theorem 7.1 "Proven strictly" and Theorem 7.2 "Fully Certified", versus
   `derivation_statements.yaml` THEOREM_7_1 `open` ("printed O(1/k) bound alone is not summable"),
   THEOREM_7_2 `conditional`, THEOREM_6_2 `conditional` ("still requires the irrelevance lemma"),
   and the route text at gaps.yaml:895-912 ("A dimension-five exclusion or a formal scaling power
   alone does not supply the quantitative transformed norm"). No edge joins the RESULT to
   THEOREM_7_1; consistent only under the reading that the RESULT is an abstract geometric-series
   fact whose hypothesis is unverified for the actual norm.
3. `graph-priorities-2026-09-10.md:39-45` (same date as the note) disagrees explicitly with the
   note's Theorem 3 about the L^-2 bound in the polymer derivative norm.
4. The `supported_by` scopes on the seed appear swapped: "Cauchy geometric decay factor lambda < 1"
   is attached to the check that computes `sum 9^-k = 9/8`, and "Geometric series tail sum bound
   2 lambda^j" is attached to the SO(4)-anisotropy check that computes `lim (1/9)^k = 0`; and the
   check detail `dimension_five_irrelevance.py:107` ("expectation values form a provable Cauchy
   sequence in C") overstates an arithmetic identity.
5. The G19 note (section 1) cites "ledger/gaps.yaml:L1053"; the step now sits near line 1245
   (line drift; the manuscript reference to line 579 is still correct).
6. `ledger/documents.yaml:376` records in prose that CONDITIONAL_GRADIENT_REPAIR corrects EX-014,
   with no graph edge to `NOTE:EXTRACT_2026-09-01:ex-014-rg-schur-riccati-md-fc55bb` (the
   established review above is the proposal for that edge).

## 8. Why this deserves attention for the Clay objective chain

THEOREM_7_1 is the single input of THEOREM_7_2 (existence of the continuum measure), which feeds
OS0-OS4 (Theorems 8.1-8.2) and the mass gap of Theorem 9.1. The G19 note's wording, the seed's
`proven` status and its `bears_on G19` invite the reading that the priority-5 route on THEOREM_7_1
has been discharged. The reading here shows two independent reasons it has not: the contraction
constant is canonical power counting with no derivation in the norm (6.3)-(6.4), and even granted,
the forcing term in (6.5) keeps `||K_k|| = O(g_k^2)`, so (7.6) remains O(1/k). The route's decisive
test (one genuine normalised blocking step with observable transport, gaps.yaml:895-912) remains
the actual next step; the established disagreement record removes the block-map-gradient route from
consideration for both decimation and averaging maps.

## 9. What does NOT hold

* Not: the manuscript's lambda in (6.5)/(6.10) is a gradient-intertwining constant of its block map.
* Not: EX-014's Karcher value `C_RG <= (1+O(r))/L^d` is a contraction of the (A3) constant
  (refuted by `RESULT:CONDITIONAL_GRADIENT_REPAIR`; the 1/N is the pullback factor).
* Not: the averaging-constraint defect (561-577) is the EX-013 section 7 no-go.
* Not: the seed's tail bound establishes Theorem 7.1 (wrong sequence; forcing term dropped).
* Not shown: that no summable increment bound exists. The graph-priorities alternatives (a matched
  O(g_k^3) remainder, or a common-space Lipschitz map with summable parameter drift) remain open.
* No claim about the actual Wilson RG map: `RESULT:CONDITIONAL_GRADIENT_REPAIR` is a configuration-
  form Dirichlet theorem, "not an OS energy comparison"; its refutation of EX-014 is exact only in the
  flat linearised chart both texts use.

## 10. Retrieval observations (measured)

* search1 (September vocabulary; `search1.json`): 10 direct hits, abstention coverage 0.688,
  weak_match false. EX-014 section 1 passage (lines 91-96) at rank 9; manuscript repair-record passage
  580-589 rank 4; G19 note Theorem 3 passage (222-234) rank 5; THEOREM_6_2 rank 2; rank 1 was an
  external pre-reconciliation copy of the proof map (`ext:research/...derivation_formalization.md`).
* `discover plan`: the lexicon matched zero concepts for the question (`concepts: []`); the plan
  carried only the user query until four reformulations were added by hand (`plan-edited.json`).
* search2 (fused, 5 sub-queries; `search2.json`): EX-014 section 1 passage rank 1 overall with
  per-query ranks q1 = 10, q2 = 2, q3 = 10, q5 = 27; EX-014 section 2 passage rank 2; G19 note
  passages ranks 5-6; THEOREM_6_2 in the related group rank 2 (q1 rank 2). Abstention weak_match true
  (coverage 0.354 over 65 content terms), as expected for a multi-vocabulary fusion.
* search3 (pure EX-014 vocabulary; `search3-ex014-vocab.json`): EX-014 ranks 1-2; three external
  archive synthesis copies of the same C_RG table ranks 3-6 (`ext:archive-synth-copy/Synthesis_15/16/11`);
  corpus-import pmbsf protocol rank 7; THEOREM_6_2 rank 8. The related group surfaced
  `RESULT:CONDITIONAL_GRADIENT_REPAIR` at rank 2 and the dead route
  `ROUTE:G19:infer-a-scale-contraction-from-the-forwa-c194d2` at rank 1 -- this reverse-direction
  search is how the one established pair was found; the September-vocabulary searches placed
  CONDITIONAL_GRADIENT_REPAIR only at related rank 5 (search2) and not in search1's top 10.
* `discover connections` on the seed: 122 record candidates, 57 passage candidates, passage quota 3,
  5 already-connected excluded. Top records: `CITE:YM_BALABAN_MULTISCALE` (path through the two CHK
  witnesses), `RESULT:COMMON_SPACE_CONTRACTIVE_DRIFT`, G18/G19 September results; the three passage
  slots went to `ext:tmp` and `ext:inbox` copies of the Cauchy repair and the G19 continuation, so
  EX-014 did not appear as a connections candidate at the default quota.
* Pair dossiers suggested literature-bearing (A, C), compatible-hypothesis (B), documentary (D),
  all confidence low; the readings decided rejected, rejected, (C not registered), established.
* The discovery cache fingerprint changed mid-session (52c54e76... at search time, 42678b34... when
  the reviews were recorded) because `docs/graph_discovery.md` was edited on disk by another agent;
  the review records carry the tool's `fingerprint_note`. All recorded source hashes matched.

## 11. Files in this directory

`plan.json`, `plan-edited.json`, `search1.json`, `search2.json`, `search3-ex014-vocab.json`,
`connections.json`, `pair-A-seed-vs-ex014-s1.json`, `pair-B-thm62-vs-ex014-o3.json`,
`pair-C-g19thm3-vs-ex014-step7.json`, `pair-D-condgrad-vs-ex014-s1.json`,
`check_614_recursion.py`, `proposal-condgrad-ex014-documents.yaml`,
`proposal-condgrad-ex014-results.yaml`, `register/` (3 reviews, `validate`: chain intact).
