# Case outside-pressure-schur

Reviewer label: outside-pressure-schur. Worktree C:/WORKHOUSE/worktrees/discovery-agents-20260911
(branch claude/discovery-agents-20260911). Discovery cache fingerprint 42678b342872ea53..., freshness
matched. Briefing retained at .graph-state/case-outside-pressure-schur/brief.json (targets
DERIV:WILSON_SC17_SPATIAL_CLOSURE:R12_R14, :ACTUAL_REFERENCE_DEFECT_BOUND, :R4_R9,
ROUTE:G19:bound-the-complete-signed-sc17-condition-01c5a0, DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE,
RESULT:W6_ENERGY_WEIGHTED_CT, DERIV:WILSON_TRUE_VACUUM_BLOCK_ESTIMATES:BA9_BA10).
Scratch register: cases/outside-pressure-schur/register (4 reviews, chain intact, `review validate` OK).

## Question

Is the outside-pressure Hessian W_B'' = ((H_out Omega)/Omega)'' of SC17 R12 the quantum analogue of the
classical marginal identity grad^2 V_eff = E_nu[grad^2_xx V] - Cov_nu(grad_x V) (EX-014 sec 3(1)), so that
D_b is a Schur-complement defect, R12a is EX-014's Gaussian sharpness check, and OP-3's sup M^2/gamma is
SC17's delta?

## Verdict in one line

No for R12 (rejected, with an exact replacement identity, verified numerically); yes for a different SC17
statement: EX-014 sec 3(3) is literally the marginal-curvature step of SC17 R10 (established,
reusable-ingredient), and OP-3's M^2/gamma is that same Schur operator (established, shared-operator, with
a scope restriction). It is not delta.

## Excerpts compared (regime stated for each)

1. docs/derivations/wilson-sc17-spatial-closure.md:698-756 (R12 at line 710, R12a at 733, R13 at 743,
   R14 at 748; the frozen-link sentence at 712-714), sha256
   d02e906ba0d52d20f3a1cf750347bc89da59ece4bb52d3fae955c71aae6daac8.
   Regime: finite periodic cubic SU(2) lattice Hamiltonian H = -eps Delta + k sum_p (1 - Tr U_p/2) at fixed
   spacing and finite volume; actual positive ground Omega; product Euclidean block chart; block coordinate
   x conditional on outside links b. Observable: block Hessian of the conditional Schrodinger potential
   U_b = V_B + W_B and Hess log Omega. Ledger: DERIV:...:R12_R14 (conditional, analytic, T3); the smallness
   bound is DERIV:...:ACTUAL_REFERENCE_DEFECT_BOUND (open), targeted by the untried G19 route. The criterion
   2 beta_s(A)^2 delta/eps < 1 appears at lines 610 (R6), 806 (sec 6) and 858-860 (LaTeX display).
2. notes/imported/EXTRACT_2026-09-01/EX-014-rg-schur-riccati.md:214-272 (sec 3; sec 4 at 273-311 and sec 7
   at 443-495 also read), sha256 fc55bb4934560183d5529822693ce7ad90ca9bc6f521546cb505d8e30f6cc703.
   Regime: classical finite-dimensional Euclidean R^n x R^m Gibbs density e^{-V}, V in C^2, MARGINAL over
   the fibre y; no lattice, no group, no volume limit. Its caveat (line 267) states the chart / gauge
   quotient / exponential-map Jacobian obligation for a compact group. 'solid' is the extractor's word;
   the notes.yaml verdict is 'import' (bears_on G19, G23), which promotes nothing past T3.
3. docs/derivations/wilson-sc17-spatial-closure.md:649-697 (R10 at 658, marginal-curvature step at 666,
   R11 at 687-690), same sha256 as item 1. Regime: classical Gibbs density exp(-Phi), Phi = -2 log Omega,
   on Euclidean coordinate blocks B, C conditional on their complement, uniform-in-fields Hessian floors;
   conclusion is an L2 conditional-projection angle and, via R9, the physical gap. Ledger
   DERIV:...:R10_R11 (conditional, analytic, T3).
4. corpus-import/theory/DOC_GOV_open_problems.md:90-107 (OP-3), sha256
   226b3f472f787cd928dbac7e88f3780e4ab795a8513b4b5545d4842f5b005da6. Regime: Euclidean lattice Wilson
   measure on Lambda_L, action S_a, blocks of fixed physical diameter, supremum as a -> 0; M = op norm of
   the mixed action Hessian, gamma = inf spec of the complement action Hessian. Graph node
   CORPUS:theory-doc-gov-open-problems-md (file node only).
5. notes/imported/RESEARCH_2026-08/Dynamic_Hessian_Riccati_Flow.tex:107-152, sha256
   4a3235840d7db4cbf29e1b1f419bbb3eb6cc5bd64454aec568d80f500f1d1b83. Regime: formal R^n heat flow of
   densities, eps = 1, no potential; compared with SC17 R1-R3 (lines 537-573).

## The decisive reading: an exact identity for W_B''

With u = log Omega, J = Hess u (blocks J_xx, J_xb, J_bb) and H_out = -eps Delta_b + V_out:

    W_B = (H_out Omega)/Omega = V_out - eps (Delta_b u + |grad_b u|^2)      [= BA10 of wilson-true-vacuum-block-estimates.md]
    W_B'' := Hess_x W_B = -2 eps J_xb J_xb^T + K_b J_xx,   K_b = -eps (Delta_b + 2 grad_b u . grad_b), entrywise

Consistency: the full stationary Riccati identity V'' = 2 eps (J^2) - K J with K = K_x + K_b (the ground
Doob generator) gives V_B'' + W_B'' = 2 eps J_xx^2 - K_x J_xx, exactly the eigenfunction equation of
Omega(., b) for -eps Delta_x + U_b. Gaussian case (J = -Omega_0 constant): K_b J_xx = 0, J_xb = -B, so
W_0'' = -2 eps BB* and V_0'' + W_0'' = 2 eps A^2: this is R12a / GC6 verbatim. With E = J + Omega_0
(E_xx = X, E_xb = Y in the notation of R2):

    D_b = 2 eps X^2 - 2 eps (AX + XA) - K_x X                     [stationary R1 restricted to the block]
    (W_B - W_0)'' = -2 eps (YY* - BY* - YB*) + K_b X              [the nonlinear pressure excess]

so the conditional criterion R5 with U_b = V_B + W_B is the projected full-space equation R2 with
K = K_x + K_b: the R2 cross terms 2 eps YY* - 2 eps (BY* + YB*) are minus the pressure excess without its
K_b part. Nothing here is an expectation or a covariance; the mixed term carries the kinetic coefficient
eps and no fibre stiffness C^{-1}.

Numerical confirmation (scratch only: cases/outside-pressure-schur/check_pressure_hessian.py and
check_pressure_hessian_conv.py, system Python 3.12 with numpy 2.3.5 / scipy 1.17.1; outputs *.out;
2-coordinate H = -eps Delta + eps z^T Omega_0^2 z + lam (x^4 + x^2 b^2 + b^4) on a Dirichlet box [-4,4]^2,
shift-invert eigsh, central differences, comparison on |x|,|b| <= 1.2):
- lam = 0, eps = 0.8, A = 1.5, B = 0.6, C = 2: W_B'' = -0.57589 vs -2 eps B^2 = -0.57600; V_B'' + W_B'' = 3.60011
  vs 2 eps A^2 = 3.60000; J_xx = -1.50023 vs -A. The classical Schur (marginal) precision A - B^2/C = 1.32 is
  a different number from the conditional precision A = 1.5 (and from sqrt(A^2 + B^2) = 1.616).
- lam = 0.15: identity residual 2.96e-2, 1.23e-2, 7.4e-3 at h = 0.050, 0.033, 0.025 (h^2 scaling, i.e.
  discretisation of a fourth derivative of log Omega, not a missing term); the eigenfunction identity
  holds to 6.5e-4 on the finest grid.
- Size of the pieces: max|-2 eps J_xb^2| = 0.574 vs max|K_b J_xx| = 0.27 (lam = 0.15); 1.16 vs 0.58
  (eps = 1, A = 1, B = 0.9, C = 1.6, lam = 0.3). The non-Gaussian pressure excess is dominated by K_b J_xx,
  the outside Doob generator acting on the block log-Hessian, which a frozen-link Hamiltonian ground
  (h_B(b) without W_B; BA4/BA9) omits entirely.

## Precise relationships (closed vocabulary) and register states

A. DERIV:WILSON_SC17_SPATIAL_CLOSURE:R12_R14 -> EX-014:214-272, kind equivalent-construction: REJECTED.
   (i) W_B'' is pointwise in (x, b) with no E_nu and no Cov. (ii) The conditioning direction is opposite:
   V_eff is the marginal on the retained coordinate; U_b is the fibre potential at frozen b. (iii) R12a says
   the conditional Gaussian precision is the diagonal block A (removing +2 eps BB* from V_0''); EX-014's
   sharpness check says the marginal Gaussian precision is the Schur complement A - BC^{-1}B^T. Different
   objects, and the B-term plays opposite roles. (iv) The nonlinear excess is quadratic in the mixed
   log-Hessian defect Y plus K_b X, not a covariance. (v) EX-014 sec 7 (lambda_min(E[H|G]) >= E[lambda_min H|G])
   needs a literal conditional-expectation step; R5-R8 use sup_b in ||.||_(s,infty) and average nothing, so
   it bounds nothing in D_b. The only available average, E_{Omega(x,.)^2 db}[W_B''] = -2 eps E[J_xb J_xb^T]
   <= 0, kills K_b J_xx but is not the norm R5 needs. (vi) R13/R14 come from [-eps Delta, chi]; EX-014 sec 3(1)
   has no kinetic operator, so no analogue exists there (a cutoff would enter EX-014 only through a weighted
   Poincare / Brascamp-Lieb boundary term in sec 3(2)-(3), a different step).
B. DERIV:WILSON_SC17_SPATIAL_CLOSURE:R10_R11 -> EX-014:214-272, kind reusable-ingredient: ESTABLISHED.
   SC17 line 666 'marginal C curvature at least 2(a_C - h_BC^2/a_B)' is EX-014 sec 3(3) alpha - M^2/gamma with
   alpha = 2a_C, gamma = 2a_B, M = 2h_BC, by the same Poincare-only proof (EX-014 lines 245-249); same
   hypotheses (C^2 density, uniform fibre floor, uniform mixed-Hessian norm), same regime
   (finite-dimensional Euclidean blocks, classical Gibbs density), same open chart / gauge-quotient
   obligation on the compact group. Normalisation compatible (floors written 2a so that a is a log-Omega
   curvature). Independent origin (EX-014 extracts HESSIAN/Core_Hessian/02_RG_Hessian_Schur_Stability.md and
   09_rg_schur_complement_curvature.md, extraction 2026-09-01; SC17 sec 3 is dated 9 September 2026).
   EX-014 additionally supplies, for the same step, the Brascamp-Lieb sharpening sec 3(2), the Prekopa
   no-loss theorem sec 3(4), the Gaussian sharpness of the constant, and the sec 4 obstruction that the
   covariance loss is exactly the deficit (so R11's angle budget cannot be improved by marginalisation
   alone). Falsifier: exhibit a density exp(-Phi) satisfying the R10 hypotheses whose marginal curvature is
   below 2(a_C - h^2/a_B); EX-014's proof excludes it, which is why the relation is 'ingredient', not
   'dependency': SC17 proves the step itself.
C. corpus-import/theory/DOC_GOV_open_problems.md:90-107 -> DERIV:...:R10_R11, kind shared-operator:
   ESTABLISHED with a scope restriction. OP-3's sup M^2/gamma is the Schur curvature-degradation operator;
   in SC17 it is h_BC^2/a_B (R10) and kappa_A (R11), c_BC^2 <= h^2/(a_B a_C) = M^2/(alpha gamma). OP-3 applies
   it to the Euclidean Wilson action S_a with a -> 0; SC17 applies it to Phi = -2 log Omega at fixed spacing
   with h = ||A_BC|| + r, a = a_0 - r. It is NOT SC17's delta: delta is a potential-Hessian defect (units
   2 eps A^2, entering through beta_s^2 delta/eps ~ delta/(2 eps a^2)) and reaches R10-R11 only through r_-
   of R7. OP-3's 'what's known' bullets (Schur identity proven; sigma_geom = h^vee/2) are not inherited:
   corpus-import/theory/notes/NOTE_FLUX_novel_derivations.md:322-338 records the corpus's own 'Theorem B'
   rho_eff >= N/2 - M^2/gamma as unsupported (precondition H_etaeta > 0 fails on 100 percent of Haar links at
   beta = 0; sign artifact of a negative gamma).
D. notes/imported/RESEARCH_2026-08/Dynamic_Hessian_Riccati_Flow.tex:107-152 -> DERIV:...:R1_R3, kind
   scope-restriction: ESTABLISHED. The tex Hessian evolution d_t h = Delta h - 2 (grad S . grad) h - 2 h^2 is
   SC17 R1 at eps = 1, V = 0 under h = -J, S = -u; SC17 adds -V'', the constant reference precision and
   R2/R3. The tex's scalar Riccati step drops diffusion and advection heuristically with an unspecified
   anomaly source; SC17 R8 keeps K_t and uses a weighted Banach-algebra Duhamel bound. Not the question's
   pair; recorded because the question named the file and EX-014 secs 8-11 are the same machinery.

## Existing graph witnesses

For A and B: none (EX-014 passages have no graph identity; `connections` for R12_R14 and R10_R11 returned
only SC17/G19/G23-family records and external tmp/ reviews). For C: CORPUS:theory-doc-gov-open-problems-md
is a file node with no relation to any SC17 record. For D: none. Nearest registered structure:
R12_R14 <-depends_on- ACTUAL_REFERENCE_DEFECT_BOUND <-targets- ROUTE:G19:bound-the-complete-signed-sc17-condition-01c5a0
(untried), whose decisive test reads 'derive outside-pressure and projector derivatives ... check the
Gaussian cancellation exactly, then bound the remaining full expression'. The identity above is that
outside-pressure derivative. Edges touching R12_R14 in index/graph.jsonl: CITE:WILSON_SC17 bears_on and
contains, ACTUAL_REFERENCE_DEFECT_BOUND depends_on, R12_R14 depends_on R1_R3; nothing from
CITE:SEPT_DOC_WILSON_G19_GAUSSIAN_REVIEW.

## Proposal fragments (scratch register only; nothing applied)

- register/proposals/2026-09-11-reusable-ingredient-...-a8c7a3-derivation.yaml emits `depends_on` with a
  FILL for a catalogue id that does not exist (imported-note passages carry none). Do NOT apply as
  depends_on: SC17 proves the step itself. The -documents.yaml variant has the same unfillable target. The
  honest landing is a `bears_on` addition on the EX-014 entry of ledger/notes.yaml naming
  DERIV:WILSON_SC17_SPATIAL_CLOSURE:R10_R11; `propose` has no notes surface (tool gap, reported below).
- register/proposals/2026-09-11-shared-operator-...-a11327-documents.yaml: `bears_on:
  DERIV:WILSON_SC17_SPATIAL_CLOSURE:R10_R11` from the OP-3 document alias; apply only with the scope note
  (S_a vs Phi; a -> 0 vs fixed spacing; not delta).
- register/proposals/2026-09-11-scope-restriction-...-72e01b-derivation.yaml: same FILL problem; the
  correct landing is documentary (notes.yaml bears_on), not depends_on.

## Exact next check (about one hour)

Take cases/outside-pressure-schur/check_pressure_hessian.py and replace the toy potential by a
two-coordinate one-plaquette potential in the exponential chart of the actual SU(2) block (one block angle
x, one outside angle b; include the S^3 metric factor of SC17 lines 570-573 as the first-order chart
correction), at eps = 1 and lambda = k/eps = 1/72 and 0.03 (the SC17 sec 6 points). From the numerically
exact ground state compute the three pieces of D_b separately, (V_B - V_0)'', -2 eps (YY* - BY* - YB*) and
K_b X, each in sup norm over |b| <= pi. Decide: (a) whether ||K_b X||_infty is bounded by the mixed-defect
size r that R7 outputs. It is not a priori: it needs second b-derivatives of X, which ||E||_(s,infty) does
not control; if it is not, the R5 hypothesis with U_b = V_B + W_B is not closable in that norm and the R2
form, where K_b is evolution rather than source, is the one to bootstrap. (b) Whether the resulting delta
is below the sec 6 number delta <= eps lambda^(3/2)/24 = 1.35e-5 at lambda = 1/72, which SC17 obtained from
the quartic plaquette trace alone, i.e. from (V_B - V_0)'' with no pressure excess. If the measured
pressure excess exceeds that budget, the proposed window of sec 6 needs its delta revised; if not, the
identity supplies the missing outside-pressure-derivative term of the G19 route's decisive test.

## Why this deserves attention for the Clay objective chain

The open target ACTUAL_REFERENCE_DEFECT_BOUND (G19, priority 4) requires a volume-uniform bound on D_b
including W_B''. The identity makes W_B'' a function of Hess log Omega alone (no separate pressure object,
no conditional-law construction) and shows exactly what the frozen-link picture omits: K_b J_xx, which in
the toy is half the size of the Gaussian piece. It also shows that the sec 6 delta, obtained from the
quartic plaquette trace, budgets only (V_B - V_0)'' and none of the pressure excess; the criterion value
0.084 at lambda = 1/72 has headroom only if the pressure excess stays below about 1e-4 in the same units.
On the positive side, the established B link gives SC17 sec 3 a fully written proof, its sharpness, and the
sec 4 obstruction, for the same regime and hypotheses; the C link ties the corpus's OP-3 to the current
derivation at the correct point (R10-R11, not R5/R12) and blocks the tempting but wrong identification of
M^2/gamma with delta. The negative A result prevents an agent from importing EX-014 sec 4 / sec 7
monotonicity into the SC17 pressure budget.

## What does NOT hold

- W_B'' is not E[.] - Cov(.); D_b is not a Schur-complement defect; R12a is not EX-014's Gaussian sharpness
  check (conditional block A versus marginal Schur complement A - BC^{-1}B^T); OP-3's M^2/gamma is not delta.
- EX-014 sec 7 bounds nothing in D_b: no conditional-expectation step exists in R5-R8; the lemma itself says
  it does not apply to Wilsonian blocking, and here the object is a fibre potential, not a blocked Hessian.
- R13/R14 have no analogue in EX-014 sec 3(1).
- Nothing here bounds ||D_b||_(s,infty); the G19 route stays untried. No chart, gauge quotient or S^3 metric
  term was computed; all excerpts are Euclidean-chart statements and the compact-group transfer is open in
  both source families (EX-014 line 267; SC17 lines 570-573). Lemma Q (pmbsf) was not used.
- The toy numbers are a scratch T2-type sanity check of an algebraic identity on R^2, not a lattice result.

## Retrieval observations (measured)

- q0, September vocabulary ('outside pressure Hessian conditional positive eigenfunction signed defect
  Gaussian cancellation Schur complement'): direct ranks 1-10 all SC17/G19 family (ROUTE:G19 route 1,
  R12_R14 record 2, ACTUAL_REFERENCE_DEFECT_BOUND 4, external tmp/ SC17 agent reviews 3, 5, 6, 8); EX-014,
  OP-3 and the tex absent from the top 10 direct and top 5 related; abstention weak_match False, coverage
  0.75.
- plan.json (8 sub-queries: q0; lexicon 'curvature defect', 'marginalising', 'effective potential'; mine:
  q4 'effective action Hessian equals fibre expectation of the xx block minus covariance of the gradient',
  q5 'Brascamp-Lieb Schur complement block convexity engine alpha minus M squared over gamma
  marginalisation', q6 'block-Schur dominance mixed Hessian fiber coercivity M(B)^2/gamma(B) sigma_geom',
  q7 'vHJ Hessian evolution matrix Riccati reaction diffusion minus two h squared smallest eigenvalue'):
  EX-014:211-223 (sec 3 statement) fused direct rank 5, rank 1 under q4, 20 under q6, 59 under q7;
  EX-014:255-257 (sharpness check) fused rank 8, rank 5 under q6. Fused ranks 1-3 are external
  archive-reviewed copies of the corpus 'Block RG Convexity Stability' theorem alpha - M^2/gamma
  (unified-proof ParT 2.md:125-133, unified-proof-part2-fixed.md:128-136, 06_RG_Hessian_stability.md:17-44,
  the last at q5 rank 3). OP-3 (DOC_GOV_open_problems.md:90-107) did NOT appear in the top 10 even under
  q6 written in its own words (its Unicode operator notation does not tokenise); the tex did not appear
  under q7 (archive Synthesis_08/13 copies took q7 ranks 5 and 17). R12_R14 fell to related rank 2 (q1
  rank 2). Abstention weak_match True, coverage 0.292 over 48 content terms, correctly flagging that no
  single row matches the fused question.
- connections: R12_R14 gave 10 candidates (3 already-linked excluded), record candidates all same-family,
  passage quota filled by external tmp/ reviews; R10_R11 gave G23 routes, VA14_VA19, YM_GPU_AUDIT and
  external passages. Neither seed would have reached EX-014 or OP-3 without the q4/q6 reformulations.
- pair dossiers: A shared-operator low (rule 8, 'shared symbol-like tokens without a hypothesis-level
  match', which agrees with the reading); B shared-operator low; C reusable-ingredient low (rule 9, 0 exact
  tokens); D shared-operator medium (delta, lambda, partial_i, partial_t; lexicon riccati-flow).

## Registration inconsistencies noticed (outputs, not tasks)

1. The ledger record CITE:SEPT_DOC_WILSON_G19_GAUSSIAN_REVIEW says 'GC5/GC6 already enter SC17
   R4A/R12_R14', and SC17 lines 737-738 link the review as 'the source and normalization for this
   cancellation', but index/graph.jsonl carries no edge between that record and R12_R14 (or any
   WILSON_SC17 record); its edges are `cites` to CITE:* documents only.
2. `discover propose --surface derivation` and `--surface documents` for a record -> imported-note passage
   both emit an unfillable catalogue-id placeholder; there is no `notes` surface although
   ledger/notes.yaml carries `bears_on` (EX-014: [G19, G23]).
3. OP-3's 'what's known' bullets are contradicted inside corpus-import by
   NOTE_FLUX_novel_derivations.md sec 6 (Theorem B unsupported); no ledger contradiction, route or
   cannot_decide names this.
4. The orchestrator's briefing target RESULT:W6_ENERGY_WEIGHTED_CT has no registered relation to the SC17
   Part III chain (incoming none; neighbours only DOC:RECENT w6_combes_thomas files).
