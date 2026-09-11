# Case w6-combes-thomas: Combes-Thomas on the hard block of F_g - z

Reviewer label: w6-combes-thomas. Worktree C:/WORKHOUSE/worktrees/discovery-agents-20260911
(revision fdaadc40, dirty: src/workhouse/discovery_lexicon.py). Briefing retained at
.graph-state/case-w6-combes-thomas/brief.json (target RESULT:W6_ENERGY_WEIGHTED_CT,
status conditional / analytic / T3; neighbours: four DOC:RECENT sources, G19,
RESULT:W6_RESIDUAL_CRITERION). Scratch register: cases/w6-combes-thomas/register
(4 reviews, chain intact, `review validate` = register valid). Nothing under any
scientific tree was written.

## Question

The soft-residual certificate (research/2026-09-10_w6_soft_residual/README.md, theorem
lines 23-45 and eq. (3) line 100) needs ||eta|| = O(g^beta) for
eta = rho_s - B* C^-1 rho_h with a hard block C >= cI uniformly in volume. Does the
hard block C of the vacuum-subtracted fast form F_g - z (W5) satisfy EX-012 (H1)
uniform positivity with a0 = c, (H2) finite range, (H3) bounded off-diagonal row sum
with volume-uniform constants, so that C^-1 decays (Combes-Thomas) and eta inherits
locality, converting the volume-uniform requirement into a local one? Is a0 = c the
"actual uniform lower floor for F_g" that wilson-selected-inverse-wall.md names as
missing? Is RESULT:W6_ENERGY_WEIGHTED_CT the same theorem as the EX-012 Theorem CT under
a different normalization, and has it been combined with the soft/hard split? Compare
with the OP-1 comparator M_a = m0^2 I + alpha d1* d1.

## Verdict in one paragraph

Same theorem, three homes, no bridge. The localization core of
RESULT:W6_ENERGY_WEIGHTED_CT (ct_repair.md CT5-CT7) is the EX-012 Theorem CT (Appendix
G) verbatim under (a0, R, B0) -> (kappa, R, J), in the energy-weighted normalization
B = D^-1/2 A D^-1/2 (so the decaying kernel is D^1/2 A^-1 D^1/2, CT8) and with truncated
weights for countable graphs; neither source cites the other and the September graph
holds no edge between them. But applying it to the hard block C of F_g - z does NOT
convert the volume-uniform eta requirement into a local one: (H2) and (H3) have no
referent for C, because C = P_h Q (H~_g - z) Q P_h is a block of a nonlocally compressed
many-body form and no orthogonal spatial block decomposition of H_h is constructed in any
September source (ct_repair.md section 6 item 2 lists it as an unproved input;
RESULT:W6_PROJECTED_LOCALITY_COUNTEREXAMPLE shows compression by Q destroys decay even
for H = I). (H1) with a0 = c is the README hypothesis itself, not an established Wilson
bound, and it is NOT the missing uniform floor for F_g named by the wall: the wall needs
the floor on all of Q inside (W5) (lines 130, 142) and the README (line 21) says its
certificate does not remove that requirement. The CT-on-F_g route was moreover already
attempted on 9 September (docs/derivations/yangmills-resolvent-localization-and-
dirichlet-gap.md, section 2) and audited: DERIV:...:SUBMITTED_W6_CLOSURE is `disputed`,
DERIV:...:LOCAL_KERNEL_IMPLICATION is `conditional` on exactly the actual-operator decay
that is missing here. The OP-1 comparator M_a is the EX-012 operator M_Lambda (same
operator, same C0 = 18) and is not the hard block C (CT_AUDIT.md section 3).

## The excerpts compared (path:lines, sha256 of the file in this checkout)

1. research/2026-09-10_w6_soft_residual/README.md:23-45 and :92-111
   sha256 f939ae6ddf794611c06d7c9951bd82f85e9254c813138d486ca12b4e4776dff6
   Regime: abstract bounded self-adjoint operators on H_s + H_h at fixed 0 < |g| <= g0;
   the Wilson successor (lines 92-111) is the finite spatial lattice, uniformly in
   volume; unbounded Wilson forms explicitly excluded (lines 106-108). Unregistered
   (no id in index/claims.jsonl).
2. notes/imported/EXTRACT_2026-09-01/EX-012-combes-thomas.md:34-53 (Theorem CT, H1-H3
   at 44-46, boxed bound 49, Maxwell specialization 52-53)
   sha256 6469e3e341396b88b6842def7919ff3fe7025ec222764579a1e9b855fcd11430
   Regime: finite (stated: or countable bounded-degree) graph V, finite-dimensional
   fibre; application = finite periodic lattice link cochains, volume-uniform
   constants. Imported note; notes.yaml review[255] verdict `import` (T3);
   "solid" is the label of the extractor.
3. notes/imported/EXTRACT_2026-09-01/EX-011-matrix-hinge-chain.md:374-472 (section 6,
   statement 380-390; section 5 repair 306-372)
   sha256 6c86da82c5e9f499adefa0fee0f4001615cf897dec1923dad37f09602f683180
   Regime: V finite, arbitrary Hilbert fibre; section 5 application = classical
   Euclidean Gibbs measure on Lambda_L conditioned on a good set Omega, Witten
   Laplacian on one-forms indexed by links; hinge (i) Ric_mu >= m_H^2 conditional.
4. runs/recent_research_integration_2026-09-09/sources/w6_combes_thomas_20260909/
   ct_repair.md:36-140 (CT3-CT8), :189-260 (CT12-CT16), :291-310 (open inputs)
   sha256 168bf60d3b53af053df75a04d39c448d71abe709ff8e472c9d9927ce901ef430
   CT_AUDIT.md:94-112 (CT5 counterexample), :129-202 (CT6-CT12), :197-202 (g-uniformity)
   sha256 485adaa16795d0e36c4a2fd9be047d08f68e15850d1c858587dc8f064dbf94ea
   operator_audit.md:41-53 (F = Q H~ Q), :64-124 (positive jump counterexample)
   sha256 fb19c50ca333bcd8f7ab35cb78198b2f0f47c7f418e930815595330198a063f9
   Regime: abstract (orthogonal block sum assumed); Wilson application unrealized.
   Source of RESULT:W6_ENERGY_WEIGHTED_CT (ledger/recent_research.yaml:1073-1108,
   file sha256 aea2e5951720005cc4dce0772b6d3727a65c4806c23037565211b65da411b542).
5. docs/derivations/wilson-selected-inverse-wall.md:130-146 (W5) and :240-252
   sha256 c0473aca76790ef7adc6e9d90642f94a252d7052e02fa0b7ee79f92afd099cfe
   Regime: finite spatial Lambda, 0 < g <= g0, uniformly in volume; open wall
   DERIV:WILSON_SELECTED_INVERSE_WALL:W6 (status open, locator lines 221-264).
6. corpus-import/theory/DOC_GOV_open_problems.md:12-30 (OP-1) and :179 (Addendum 2)
   sha256 226b3f472f787cd928dbac7e88f3780e4ab795a8513b4b5545d4842f5b005da6
   Regime: Euclidean Lambda_L = (Z/LZ)^4 Wilson Gibbs measure; deterministic
   comparator on link cochains. Historical corpus text (June 2026 live copy).
7. notes/imported/EXTRACT_2026-09-01/EX-014-rg-schur-riccati.md:214-272 (section 3),
   :443-495 (section 7), sha256 fc55bb4934560183d5529822693ce7ad90ca9bc6f521546cb505d8e30f6cc703
   Regime: Euclidean R^n x R^m potentials (section 3); conditional expectations of
   random operators (section 7). Caveats confronted below.
8. docs/derivations/track-a-supported-statements.md:18-74 (W6-V, W6-E)
   sha256 26efd60d345eb4c961f33474170657e5eff7333a390a1b68841b0b76ecc0e693
9. docs/derivations/yangmills-resolvent-localization-and-dirichlet-gap.md:1-12 (audit
   banner), :40-80 (section 2, CT on F_g - z), :131-135 (frozen "Closed" claims).

## Proposed relationships (closed vocabulary) and register state

A. RESULT:W6_ENERGY_WEIGHTED_CT -> EX-012:34-53, kind `equivalent-construction`,
   ESTABLISHED (2026-09-11-equivalent-construction-result-w6-energy-7cc1d2).
   Decisive reading: ct_repair.md lines 67-97: B >= kappa I bounded self-adjoint on an
   orthogonal block sum, B_BC = 0 for d > R, row and column sums <= J, choose mu with
   J(e^{mu R} - 1) <= kappa/2, conclude ||P_B B^-1 P_C|| <= (2/kappa) e^{-mu d}, explicit
   mu = R^-1 log(1 + kappa/(2J)); proof = truncated weight conjugation, Schur bound,
   Neumann inversion around B. EX-012 lines 42-50: A >= a0 I, range R, row sum B0,
   ||(A^-1)_xy|| <= (2/a0) exp(-eta dist), eta = (1/R) log(1 + a0/(2 B0)); proof = weight
   conjugation (Step 0-1), block Schur (Step 2, (star)), Neumann at half gap (Step 3).
   Identical statement, constants and mechanism. Differences (normalization/scope only):
   ct_repair conjugates the preconditioned B = D^-1/2 A D^-1/2 so the decaying object is
   the energy-weighted kernel D_B^1/2 P_B A^-1 P_C D_C^1/2 (CT8) - under D = I they
   coincide; truncated weights exp(mu min(d, L)) make the countable case rigorous (EX-012
   states countable V but conjugates by an unbounded weight; EX-011 section 6 states V
   finite); arbitrary Hilbert blocks E_B (EX-011 section 6 already allows an arbitrary
   fibre, EX-012 requires finite-dimensional). CT9-CT16 (energy-weighted local input,
   Schur synthesis, source-kernel estimate) are the genuinely new content of the RESULT
   and have no EX-012 counterpart. Not combined with the soft/hard split: the README
   (10 Sept) never mentions localization, CT, or ct_repair; the RESULT links only
   W6_RESIDUAL_CRITERION and G19. Proposal emitted (results surface): a bears_on
   fragment whose target must be a catalogue id; EX-012 has none (see inconsistencies).
   Independence of origin: yes - EX-012 extracts the 2026 corpus Appendix G; ct_repair
   (9 Sept 2026) reproves from scratch citing only Shen arXiv 1207.3782.

B. README:23-45 -> EX-012:34-53, kind `compatible-hypothesis`, REJECTED
   (2026-09-11-compatible-hypothesis-research-2026-09-1-17320f). Reason: not the same
   object under the same hypotheses. (H2)/(H3) presuppose l2(V; H0) with orthogonal
   block projections over a graph; the hard block C = P_h (F_g - z) P_h is a block of
   the compression Q H~ Q of the vacuum-subtracted many-body Hamiltonian
   (operator_audit.md lines 41-53; SP1 lines 44-58) and no orthogonal spatial block
   decomposition of H_h exists in any September source (ct_repair.md section 6 item 2).
   CT5 (CT_AUDIT.md lines 94-112): on a cycle of N sites with H = I and Q = I - |v><v|,
   Q A^-1 Q has entries -1/N at separation N/2, so no N-independent exponential rate
   exists although the bare operator has range zero - locality of C^-1 cannot be
   inferred from locality of H~. (H1) for C is the README hypothesis c; positive
   interface additions do not preserve the vacuum-subtracted floor (operator_audit.md
   section 2, exact rational counterexample with gap 1/100 -> 0). A bare (unweighted)
   CT on C would also re-import the horizontal-denominator failure CT3/CT17
   (||rho_n||^2/g^2 -> infinity in the exact torus model); only the energy-weighted form
   (CT8, with the README hypothesis ||C^-1/2 rho_h|| <= h|g| sqrt(b)) is compatible.

C. DERIV:WILSON_SELECTED_INVERSE_WALL:W6 -> README:92-111, kind `scope-restriction`,
   ESTABLISHED (2026-09-11-scope-restriction-deriv-wilson-selected-ebc64d). Decisive
   reading: wall line 130 "Suppose F_g - z >= f > 0" on the whole fast space inside
   (W5), line 142 uses f in the cubic remainder (2 t0 t2 + g0 t2^2)/f, lines 249-251
   name "an actual uniform lower floor for F_g" as still required; README lines 28-29
   need C >= cI on H_h only plus S >= s|g|^alpha (degenerating), line 21: "It does not
   remove the separate fast-floor requirement elsewhere in W5". So a0 = c is the wall
   floor restricted to the hard block and used only inside W6-E (track-a lines 61-74);
   it is not the missing F_g floor. Same normalization (A_g = F_g - z, t = t1 p, b[p]);
   README eq. (3) restates the open coupled ground/source estimate of the wall for the
   corrected residual, it does not prove it. Proposal emitted (derivation surface):
   the tool offers only depends_on/lean_support, and the wall does NOT depend on the
   README, so the emitted depends_on fragment must not be applied; the correct landing
   is a bears_on from a future record of the README onto DERIV:...:W6 once the README
   is registered.

D. DOC_GOV_open_problems.md:12-30 -> EX-012:52-53, kind `shared-operator`, ESTABLISHED
   (2026-09-11-shared-operator-corpus-import-theory-doc-ddee67). M_a = m0^2 I +
   alpha_W d1* d1 on oriented links (OP-1 line 18) = M_Lambda = m^2 I + alpha d1* d1 on
   C^1(Lambda; g) (EX-012 line 52); same unit-incidence convention; C0 = C_partial = D_E
   = 18 in d = 4 in both (OP-1 Addendum 2 line 179; EX-012 line 268). Shared operator
   registers no scientific edge (ADR 0007); proposal (documents surface) emitted only
   to show the FILL requirement; nothing to apply. What it settles for the question:
   M_a is a configuration-independent deterministic cochain operator in a classical
   Birman-Schwinger argument on the Wilson Gibbs measure; the W6 hard block is a block
   of a compressed quantum form on wavefunctions; CT_AUDIT.md lines 65-92 reject the
   identification of the fast form with a cochain Laplacian plus curvature
   endomorphism ("different operators and Hilbert spaces"). The OP-1 record is also a
   warning: its CT chain was 10^5-10^6 slack against measured theta (Addendum 3, line
   56) and the Davies rate only tightens by x133-172 (line 179); EX-012 section 1 gives
   factor 65 at m^2 = 0.3; CT_AUDIT lines 200-201 M_4(mu) ~ 16 mu^-4 would amplify this
   in any Schur synthesis.

## Existing graph witnesses

- RESULT:W6_ENERGY_WEIGHTED_CT -> bears_on -> RESULT:W6_RESIDUAL_CRITERION, G19;
  supported_by the four DOC:RECENT files. No edge to any EX-011/EX-012 passage (imported
  notes carry no catalogue id: `no_graph_identity` in `connections`).
- DERIV:WILSON_SELECTED_INVERSE_WALL:W6 (open) depends_on W4_W5; lean_support
  signed_resolvent_identity, variational_residual_identity, inverse_energy_le_dual,
  factored_residual_dual_bound, factored_w6_bound (bounded-operator scope only).
- DERIV:YANGMILLS_RESOLVENT_LOCALIZATION_AND_DIRICHLET_GAP:LOCAL_KERNEL_IMPLICATION
  (conditional): "given uniform massive exponentially decaying kernels and a finite-range
  perturbation ..." - the already-registered conditional form of the very implication
  the question proposes; its closure sibling SUBMITTED_W6_CLOSURE is `disputed`.
- CORPUS:programs-pmbsf ... NOTE_PMBSF_master_pass19 lines 3748-3757 (Lemma H.6.1):
  corpus-side conditional template "HS hinge + Combes-Thomas inverse decay +
  localization algebra => fixed-cutoff clustering" with five recorded gaps; classical
  Gibbs regime, not the quantum fast form. Lemma Q (pmbsf, honest status section 14)
  is open and nothing in this case rests on it.
- Pair A/B/C/D dossiers: registered relations none; shared witnesses none (record
  candidates from `connections` all share only the hub G19, degree 502).

## Caveats confronted

- EX-014 section 3 (Brascamp-Lieb Schur bound, alpha - M^2/gamma) is the classical
  Euclidean analogue of the soft Schur floor S >= D_floor - ||B||^2/c; its caveat (line
  267: chart, gauge quotient, exponential-map Jacobian) applies, and beyond that F_g is
  not a marginal Hessian at all - it is a compression of a quantum form. The one
  transferable piece, (4) "joint floor kappa => Schur complement floor kappa", is pure
  linear algebra the README already contains as its identity (1). Nothing in EX-014
  section 3 supplies c.
- EX-014 section 7 (conditional-expectation floor monotonicity) does not apply to
  Wilsonian blocking (line 473) and does not apply here either: Q H~ Q is not a
  conditional expectation, and operator_audit.md section 2 shows even a positive
  Dirichlet-jump addition can drive the vacuum-subtracted excitation gap to zero.
- Lemma Q (pmbsf section 14) is open; not used.
- corpus-import/theory/under_review/* banners: not touched by this case;
  DOC_GOV_open_problems.md is in corpus-import/theory (historical June 2026 copy,
  no under-review banner) and is read as a claim, not a status.
- Imported-note status words: EX-012 "solid" x9 and EX-011 "solid/conditional" are
  extractor labels; the notes.yaml verdict `import` promotes nothing past T3.

## What does NOT hold

1. CT on the hard block does not convert the volume-uniform requirement on eta into a
   local one. It relocates it: to the construction of an orthogonal spatial block
   decomposition of H_h compatible with Q, with finite-range, bounded-row-sum blocks of
   C and of the coupling G = B* D_h^-1/2 (energy-weighted). CT5 says compression can
   make such a decomposition impossible; ct_repair section 6 item 2 says it is unproved.
2. a0 = c is not the missing uniform lower floor for F_g. W5 still needs
   F_g - z >= f on all of Q for the cubic remainder; the README says so at line 21.
3. The route "Davies/CT decay of (F_g - z)^-1 plus range-2 locality of d_{g,QQ}" was
   submitted on 9 Sept (resolvent-localization document, section 2) with a scalar
   surrogate and an assumed floor F_g - z >= m_fast^2/2; the audit did not identify
   the surrogate with the Wilson operator; the closure record is `disputed`. The
   hard-block variant inherits both missing identifications.
4. The OP-1 massive Maxwell bounds do not transfer to C (different Hilbert spaces).
5. Even where CT applies, the small-mu amplification M_d(mu) ~ 16 mu^-4 and the factor
   65 to 10^6 slack recorded in EX-012/OP-1 mean the CT (log) exponent is the wrong
   instrument for constants; the Davies (arcosh) exponent or the exact kernel is what
   the corpus itself fell back to.

## The exact next check (one hour, finite exact computation plus one comparison)

Computation (Fractions/numpy, N <= 64): take the successful README realization
A0 = diag(2g^2, 1), Ag = [2g^2, g^2; g^2, 1], t = (0, 1) per site, form the direct sum
over a cycle of N sites with nearest-neighbour hard-hard coupling epsilon (range 1), and
compress by the nonlocal Q = I - |v><v| with v the normalized constant vector on the
hard coordinates (the CT5 projection). Define H_h = hard coordinates inside Q, C = P_h Q
Ag Q P_h. Report, for g in {1/4, 1/8}, epsilon in {0, 1/10}, N in {8, 16, 32, 64}:
(a) lambda_min(C) versus N (is c uniform?); (b) max over |x-y| = N/2 of |(C^-1)_xy|
versus N (exponential decay or the -1/N tail of CT5?); (c) sup over unit sources of
||eta||/(g^2 sqrt(b[p])) with eta = P_s rho - B* C^-1 P_h rho, versus N. Outcome (b)
non-decaying at any epsilon settles that a nonlocal Q alone defeats hard-block CT; (c)
bounded with (b) non-decaying would show the README eta hypothesis can hold WITHOUT
kernel decay, i.e. that CT is not the mechanism to look for.

Comparison: put ct_repair CT5 side by side with EX-011 section 5 Part B (i)-(ii)
(lines 320-323). On the EX-011 one-form lift (direct sum over links b of
L^2(mu^Omega; g)) the range R = 1 and B0 <= B_S are PROVED uniformly in volume (Step 2)
and only the floor (i) is conditional; the W6 hard block has the opposite profile
(floor assumed, range/row sum undefined). The agent should state whether the W6 signed
pairing <R0 t1 p, d_{g,QQ} R_g t1 p> can be written as a Helffer-Sjostrand covariance of
the ground measure |Omega_0|^2 (the "ground-transformed scalar diffusion commuted with
derivatives" that operator_audit.md lines 55-61 mentions); if it can, the EX-011
link-indexed orthogonal decomposition is available for free and the open input reduces
to a Hessian floor of the conditional score - which is the object the
W6_CONDITIONAL_SCORE results already study. If it cannot, the block-decomposition input
stays open and CT is not the next lever.

## Why it deserves attention for the Clay objective chain

W6 (DERIV:WILSON_SELECTED_INVERSE_WALL:W6) is the named wall on the G19 scale trajectory
(it feeds SP20-SP24 via the selected inverse bound). Three separate September documents
(resolvent-localization 9 Sept, ct_repair 9 Sept, soft-residual 10 Sept) each re-derive
or assume a Combes-Thomas-type decay on the fast form without referencing each other or
the imported Appendix G/E theorem the corpus already holds as "the one unconditionally
correct link" (EX-012 section 1). Registering the localization theorem once, with its
single true hypothesis list (orthogonal block decomposition + floor + range + row sum),
makes the actual open input explicit and stops the wall from being re-attacked with the
decay theorem: the missing object is the block decomposition of the compressed hard
sector (or an HS lift that supplies one), not the decay estimate.

## Retrieval observations (measured)

- Search 1 (question in September derivation vocabulary, 22 content terms, external
  roots on): direct top-10 = soft-residual README at ranks 1 and 3, RESULT:
  W6_ENERGY_WEIGHTED_CT at 8, and seven external archive near-duplicates of Appendix
  G/E/A (ext:archive-appendices x3, archive-manuscripts x2, archive-proofs x2) at
  2,4,5,6,7,9,10. EX-012, EX-011, OP-1 and the wall: absent. abstention coverage
  0.591, weak_match false. Related (graph channel via G19 only): SP20_SP24,
  WILSON_LITERAL_COARSE_FORM, WILSON_LITERAL_VACUUM_COARSE_SOURCES,
  WILSON_COMMON_GAUSS_LITERAL_FAST_COMPLEMENT, GAUSSIAN_QUANTUM_FAST_SOURCES.
- Plan: lexicon matched combes-thomas, ground-state, selected-inverse, volume-uniform
  and emitted 6 rows; deleted 4 (ground-state fraction/density, uniform spectral gap:
  miss the sense), kept "selected inverse-energy" (q2) and "block inverse" (q3, cited
  EX-011:374); added q4 EX-012 vocabulary (1.0), q5 EX-011 vocabulary (1.0), q6 OP-1
  vocabulary (0.8), q7 recent-research vocabulary (1.0), q8 Schur-split vocabulary (1.0).
  Lexicon rows arrived with a literal " -1 -1" suffix in their text (stripped by hand).
- Search 2 (8 sub-queries, externals on): fused direct top-10 = RESULT:
  W6_ENERGY_WEIGHTED_CT rank 1 (q7 rank 1; q1 12; q3 13; q4 19; q5 31; q8 19);
  ext:research/w6_combes_thomas_20260909/CT_AUDIT.md:141-158 rank 3 (q7 2, q1 14, q3 16,
  q5 16); ct_repair.md:94-117 rank 7 (q3 1, q7 4, q8 16, q1 53); CT_AUDIT.md:158-175
  rank 9 (q8 4, q3 5); external archive duplicates at 2,4,5,6,8,10 (under q4 they rank
  2,3,5,8,9,16). EX-012 section 1, EX-011 section 6 and OP-1: absent from the fused
  top-10 under every phrasing, including their own vocabulary (q4, q5, q6). Related:
  DERIV:SOURCE_CURRENT_BRIDGES:SCB0B, RESULT:SOURCE_CURRENT_BOUNDED_W6,
  LEAN:variational_residual_identity, LEAN:variational_residual_error_bound,
  DERIV:TRACK_A_SUPPORTED:W6_E (q8 14). abstention coverage 0.329, weak_match true
  (85 content terms - expected for a fused plan).
- Search 3 (q4 phrasing alone, --internal-only): EX-012:1-13 rank 1, RESULT:
  W6_ENERGY_WEIGHTED_CT 2, EX-012:41-49 (the H1-H3 statement) rank 3, EX-011:835 rank 8,
  EX-011:457-466 rank 9; related: corpus OP-1 red_davies toolkit rank 1, DOC:RECENT
  ct_repair.md 3, CT_AUDIT.md 5. Measured conclusion: the cross-family imported note
  is reachable (rank 3) only with external roots excluded; with them on it is displaced
  by at least six near-duplicate archive write-ups of the same theorem (EX-012 line 57
  lists them), which the byte-identical alias collapse does not merge.
- connections RESULT:W6_ENERGY_WEIGHTED_CT: 132 record / 58 passage candidates, 6
  excluded as already connected, passage quota 3; top-10 = 7 records (all sharing only
  the hub G19, degree 502) + 3 passages that are three copies of one archive passage
  (horizontal-sector Green operator). Candidate 5, CITE:SEPT_DOC_YANGMILLS_RESOLVENT_
  LOCALIZATION_AND_DIRICHLET_GAP:44-57, was the one lead that mattered (the audited
  prior CT-on-F_g attempt); EX-012/EX-011/OP-1 never appeared.
- Pair dossiers: all four suggested kinds at confidence low; A suggested
  reusable-ingredient, B/C/D shared-operator. The "shared exact tokens alpha, eta" in
  B are symbol collisions (README alpha = soft-floor exponent, EX-012 alpha = Maxwell
  coupling; README eta = corrected residual vector, EX-012 eta = decay rate); the
  dossier regime marker labels the RESULT "continuum" because its G19 link text
  contains the word. Review records carry "evidence was produced against a different
  discovery cache than the one observed when this review was recorded": the checkout
  file src/workhouse/discovery_lexicon.py is dirty, so the implementation hash drifted
  between the pair calls and `review add`; `replay` will report the mismatch.
- Discovery roots do not include runs/, so ct_repair.md/CT_AUDIT.md are searchable only
  through the external "research" root (ext:research/w6_combes_thomas_20260909/...) or
  as DOC:RECENT records; the checkout copies under runs/ are passage-invisible.

## Commands run (all from the worktree, uv run --no-sync workhouse ...)

brief RESULT:W6_ENERGY_WEIGHTED_CT --json --out .graph-state/case-w6-combes-thomas/brief.json
discover search "<question, September vocabulary>" --json --out cases/.../search1.json
discover plan "<question>" --json --out cases/.../plan.json   (then edited by hand)
discover search "<question>" --queries-file cases/.../plan.json --json --out cases/.../search2.json
discover search "<question>" --queries-file cases/.../plan.json --json --full --out cases/.../search2_full.json
discover search "<EX-012 phrasing>" --internal-only --json --out cases/.../search3_internal.json
discover connections RESULT:W6_ENERGY_WEIGHTED_CT --json --out cases/.../connections.json
discover pair RESULT:W6_ENERGY_WEIGHTED_CT notes/imported/EXTRACT_2026-09-01/EX-012-combes-thomas.md:34-53 --json --out cases/.../pairA.json
discover pair research/2026-09-10_w6_soft_residual/README.md:23-45 notes/imported/EXTRACT_2026-09-01/EX-012-combes-thomas.md:34-53 --json --out cases/.../pairB.json
discover pair research/2026-09-10_w6_soft_residual/README.md:92-111 docs/derivations/wilson-selected-inverse-wall.md:240-252 --json --out cases/.../pairC.json
discover pair corpus-import/theory/DOC_GOV_open_problems.md:12-30 notes/imported/EXTRACT_2026-09-01/EX-012-combes-thomas.md:52-53 --json --out cases/.../pairD.json
discover review add (x4) ... --reviewer w6-combes-thomas --register cases/.../register
discover review mark (x4 reviewing; A, C, D established; B rejected) --register cases/.../register
discover propose A --surface results / C --surface derivation / D --surface documents --register cases/.../register
discover review validate --register cases/.../register   (4 reviews; chain intact; register valid)
discover lexicon list; why RESULT:W6_ENERGY_WEIGHTED_CT; why RESULT:W6_RESIDUAL_CRITERION
