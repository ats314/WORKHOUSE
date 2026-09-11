# Case m10-brascamp-lieb: Brascamp-Lieb fibrewise Poincare for the M10 conditional-score domination

Investigator label: m10-brascamp-lieb. Date: 2026-09-11. Worktree: C:/WORKHOUSE/worktrees/discovery-agents-20260911.
Scratch register: this directory, `register/` (5 reviews, 5 proposals, chain valid). Nothing under any scientific tree was written.

## Question

Does the Brascamp-Lieb conditional-variance bound Var_{nu_x}(f) <= E_{nu_x}[grad_y f^T C^{-1} grad_y f]
(EX-014 sec 3), applied to the ground-weighted fibre measure mu_g(.|w) on level sets of w with the fibre
Hessian read off the Agmon phase (RESULT:W6_CONDITIONAL_AGMON_GEOMETRY, S7) and the S12 tangency, give the
fibrewise Poincare inequality H1/H2 name (score-frame lines 400-402) and hence a candidate form of
M10 = K_g(w) <= C0 + C1 g^-2 E[V|w] on the well tube? Where does the fibre Hessian lose positivity?

## Verdict in one paragraph

A real but strictly chart-local connection. EX-014 sec 3 (2) is, word for word, the "chart-restricted
Poincare bound" that the tail-control note SUPPOSES at lines 253-255 and that the score-frame note names as
its next target at lines 400-402. In the g-independent Morse coordinate eta of B6 the fibre potential is
2S/g^2 + O(1) with Hess_eta(2S/g^2) = 2 g^-2 I exactly, so on any convex eta-ball inside the well chart
Brascamp-Lieb (or its Bakry-Emery form, the alternative proof of EX-014 (3)) yields Var_chart(F|q) <=
(1+o(1)) g^2 E_chart|d_eta F|^2 provided log A_g has bounded second eta-derivatives uniformly in g (or, by
Holley-Stroock, merely the C^0 relative comparison a0 + O(sqrt h) that S3 supplies). Fed the synchronized
score, this reproduces S14 (the M10 shape C0 + C1 g^-2 E[V|Q] on the tube); fed the undilated score it gives
the H1 shape kappa_0 g^-2 on the chart. It cannot give M10 as stated: each fibre {U2 U3 = Q} is the closed
9-manifold SU(2)^3, so by EX-005 Lemma A the fibre potential -2 log Psi_g has a strictly negative Hessian
direction on a positive-measure subset of every fibre at every g; a global fibrewise Brascamp-Lieb does not
exist, and the S15 complement term must be handled by measure, exactly as S6 says. The "antipodal
degeneration" is quantitative: the constrained-potential fibre Hessian at the S4 minimizer has two
eigenvalues vanishing linearly, lambda_1 = lambda_2 = (pi - theta)/(2 sqrt 2) (1 + o(1)).

## Excerpts compared (path:lines, SHA-256 of file bytes, regime)

1. notes/imported/EXTRACT_2026-09-01/EX-014-rg-schur-riccati.md:214-272,
   sha256 fc55bb4934560183d5529822693ce7ad90ca9bc6f521546cb505d8e30f6cc703.
   Statement (2): if C(x,y) > 0 then Cov_{nu_x}(grad_x V) <= E[B C^-1 B^T]; proof by Brascamp-Lieb,
   Var_nu(f) <= E[grad f^T (Hess W)^-1 grad f] for d nu ~ e^-W dy with Hess W > 0. Alternative proof of (3):
   C >= gamma I gives the Poincare inequality Var <= gamma^-1 E|grad_y f|^2 (Bakry-Emery). Caveat line 267:
   all four statements are Euclidean R^n x R^m; transfer to G^E needs a chart, a gauge-fixed horizontal
   projection and the exponential-map Jacobian. Regime: finite-dimensional Euclidean Gibbs fibre, no
   coupling constant, no lattice. Imported-note status word "solid" is the extractor's judgement only.
2. docs/derivations/w6-conditional-score-tail-control.md:249-270 (B6-B8 consequences; the Suppose at 253-255)
   and :473-495 (M.4, the M10 target), sha256 d04ae01d29d33cc5bfcc01abf1844f3e0692d682810ac01ee947a6ec93375471.
   Regime: actual fixed twelve-edge SU(2) square, true ground Psi_g, normalized chart-restricted conditional
   law, 0 < g < g_*; M10 is nu_g-a.e. on every fibre.
3. docs/derivations/w6-conditional-transport-obstruction.md:127-139 (S7 Gaussian conditional phase,
   B(0)), :285-315 (S12-S13 synchronized tangency), :317-375 (S6 all-fibre target, S14-S15, two-sphere
   warning at 364-366), sha256 33f5cefc2105ec3ec354edacce46371cfede62a2e46ec1557cacc5ae80f473e5.
   Regime: fixed square; S7 is the q -> 0 Gaussian jet; S6 is the all-fibre small-g target.
4. docs/derivations/w6-source-generator-score-frame.md:313-321 (H0-H4) and :400-402 (fibrewise Poincare
   named as next target), sha256 20b070cb78311187d8e28170ac6179aca8ca0646e868c72c113e902500b68b01.
   Regime: fixed square, UNDILATED score partial_g log Omega_g (K^0_g, not the K_g of M10).
5. notes/imported/EXTRACT_2026-09-01/EX-005-obstruction-global-cd.md:31-78 (Lemma A and its positive-measure
   remark), sha256 b3a9c999d3af1d0e999cfa2325233761445e34ea6a833fd4f62e33a55ada99eb. Regime: closed
   connected Riemannian manifold, any smooth non-constant function; no coupling.
6. notes/imported/EXTRACT_2026-09-01/EX-002-su2-convexity-threshold.md:16-95 (one-link SU(2) radial
   eigenvalue csc^2 theta - theta^-2 + (beta/2) cos theta, beta_c = 4.4139),
   sha256 cfa4816a177c45a98c96c05ec45a48820f0606ac6942fe41e40bf187c43e2ff0. Regime: one link, exponential
   chart, fixed beta (strong-coupling window).

## Proposed relationships (closed vocabulary), states and register ids

| id | seed | target | kind | state |
|---|---|---|---|---|
| 2026-09-11-scope-restriction-deriv-w6-conditional-s-276637 | DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10 | EX-014:214-272 | scope-restriction | established |
| 2026-09-11-reusable-ingredient-docs-derivations-w6-4b668e | docs/derivations/w6-conditional-score-tail-control.md:249-270 | EX-014:214-272 | reusable-ingredient | established |
| 2026-09-11-compatible-hypothesis-result-w6-conditio-0a3886 | RESULT:W6_CONDITIONAL_AGMON_GEOMETRY | EX-014:214-272 | compatible-hypothesis | established |
| 2026-09-11-scope-restriction-deriv-w6-conditional-t-3fef66 | DERIV:W6_CONDITIONAL_TRANSPORT_OBSTRUCTION:M10_SYNCHRONIZED_SCORE | EX-005:31-78 | scope-restriction | established |
| 2026-09-11-reusable-ingredient-deriv-w6-source-gene-9bc83c | DERIV:W6_SOURCE_GENERATOR_SCORE_FRAME:CONDITIONAL_ENERGY_H0_H4 | EX-014:214-272 | reusable-ingredient | established |

Proposal fragments are in register/proposals/. Cautions for whoever applies them: (a) every fragment needs
the NOTE catalogue id of the imported note in place of the passage locator
(NOTE:EXTRACT_2026-09-01:ex-014-rg-schur-riccati-md-fc55bb and
NOTE:EXTRACT_2026-09-01:ex-005-obstruction-global-cd-md-b3a9c9, both notes.yaml verdict `import`); the
fragment's own hint `workhouse why notes/imported/...` fails because `why` takes an id, not a path;
(b) `propose --surface derivation` emits a `depends_on` fragment for the two scope-restriction records, the
wrong field for a restriction; land those as `remaining` text on the DERIV records (the pair dossier's own
"registrable_as" says route cannot_decide / supported_by scope / derivation remaining), never as depends_on;
(c) the reusable-ingredient fragments are bears_on-grade at most: the chart Poincare is not yet used in any
existing argument, so depends_on is not warranted either.

## Existing graph witnesses

None. All five pair dossiers: registered relations none, shared witnesses 0, no dependency or exploratory
path. The EX-014 and EX-005 passages map to no claim id; the notes exist only as NOTE:EXTRACT_2026-09-01
catalogue records.

## The four checks

(i) Fibre Hessian on the tube. Psi_g = g^-6 A_g exp(-S/g^2) gives -2 log Psi_g = 12 log g - 2 log A_g + 2S/g^2,
so Hess_eta(-2 log Psi_g) = (2/g^2) Hess_eta S - 2 Hess_eta log A_g (+ Hess log J if Haar is traded for the
chart Lebesgue measure). In the synchronized angle deviations (a,b,c) at q = 0, S7 gives S_2 - min S_2 =
|a+b|^2/4 + |c|^2/4 + (sqrt6/12)|a-b-c|^2, i.e. Hess S = B(0) = 2M per colour with eigenvalues
1, (1+sqrt6)/4 -+ sqrt(63 - 6 sqrt6)/12 = 0.28320, 1.44154 (scratch sympy hessian_floor_check.py, consistent
with the registered m^T B(0) m = (6+sqrt6)/24 = 0.352062). Floor: Hess(-2 log Psi_g) >= (0.5664/g^2) I - O(1)
near the well, c = 2 lambda_min(B(0)) independent of g. In the B6 Morse coordinate the floor is 2/g^2 exactly.
Not theta-uniform: scratch mpmath scan (fiber_hessian_theta.py) of the constrained-potential fibre Hessian at
the S4 minimizer (gradient 1e-22, V = v_*(theta) to 1e-6 on every theta) gives eigenvalues
{2-sqrt2, 2, 2+sqrt2} (x3) at theta -> 0 and {0, 0, sqrt2-1, sqrt2 (x3), sqrt2+1, 2 sqrt2 (x2)} at theta = pi;
lambda_1 = lambda_2 = 0.3535 (pi - theta) -> (pi - theta)/(2 sqrt 2). The two soft directions are the U(1)
(stabilizer of Q) doublet that becomes the tangent plane of the antipodal two-sphere.

(ii) Brascamp-Lieb fibrewise. K_g(w) = Var(sigma_g|w) <= E[grad_eta sigma_g^T (Hess W)^-1 grad_eta sigma_g | chart].
SF6 supplies -(g^2/2) Delta_mu sigma_g = 4 g^-3 (V - <V>), a Laplacian, not the pointwise fibre gradient BL
needs; the usable chain is K^0 <= lambda_min(B)^-1 J_g^chart (H1 from H2 on the chart), not K^0 from SF6
directly. For the synchronized dilated score, grad_eta sigma_g = grad_eta F / g^3 + grad_eta a_g with
F = 2S - ZS; S12 tangency kills grad_eta F at m(q), and the S14 Taylor bound |F(q,eta)-F(q,0)| <=
c_F(|q||eta|^2 + |eta|^3) gives |grad_eta F| <= c(|q||eta| + |eta|^2), so BL returns
K^chart <= (g^2/c)(c_F^2 g^-6 (|q|^2 E|eta|^2 + E|eta|^4) + c_a^2 g^-2) = C0 + C1 |q|^2/g^2 with the
Gaussian moments E|eta|^{2j} ~ g^{2j}, the same numbers S14 obtains from the tube moments directly. BL
therefore replaces the tube-moment hypothesis by the Hessian floor plus amplitude regularity; it adds no
new estimate on the tube.

(iii) Shape. On the tube the output is C0 + C1 |q|^2 g^-2 <= C0 + C1' g^-2 E[V|Q] via v_*(theta) >= 2 theta^2/pi^2:
the M10 shape, and it is S14. For the undilated score the fast part is 2S/g^3 (no tangency needed since
grad_eta S(m(q)) = 0 by definition of the constrained minimum); for a quadratic phase the BL bound on Var(S)
is (g^2/2) E[grad S^T (Hess S)^-1 grad S] = g^2 E[S - S_min] = g^4/4 per fast dimension, INDEPENDENT of the
Hessian eigenvalues (true value g^4/8), hence Var(2S/g^3 | chart) <= 9 g^-2: the H1 shape kappa_0 g^-2 with
kappa_0 = 9 (actual 9/2) on the chart, degeneration-uniform in the quadratic model. H2 follows on the chart
from the gradient moment (g^2/2) E|grad(2S/g^3)|^2 = 2 g^-2 per dimension without any Poincare. So one
computation gives the chart parts of M10, H1 and H2; H0, H3, H4 (source energies of conditional
expectations) are untouched.

(iv) EX-014 caveat confronted. Chart: supplied by B6 (g-independent parametric Morse coordinate) on the
well tube only. Gauge quotient: the fibre already conditions on Q; the residual gauge is simultaneous
conjugation; at regular Q its stabilizer U(1) fixes the S4 point (no orbit zero mode at the minimizer) and
sigma_g is invariant; at Q = -I the whole minimizing two-sphere is one orbit of the SU(2) stabilizer, giving
two zero modes of exactly the type EX-014 line 264 item (b) names; along that orbit the invariant score has
zero variance, so theta = pi itself is harmless, but for 0 < pi - theta <~ g^2 the soft doublet
(lambda ~ (pi - theta)/(2 sqrt 2)) has Gaussian width g/sqrt(lambda) exceeding any fixed chart: a crossover
window where neither the Morse chart nor gauge invariance controls the two soft directions. Jacobian: in the
exponential chart the Haar radial term csc^2 theta - theta^-2 is positive and increasing (EX-002), so it
helps convexity; in the Morse chart it is a g-independent O(1) Hessian term dominated by 2/g^2. The EX-002
threshold beta_c = 4.41 concerns the one-link Wilson term at theta > pi/2 at fixed beta (strong coupling) and
has no small-g analogue on the tube; EX-002 is not an obstruction here.

## What does NOT hold (failure set)

1. No global fibrewise Brascamp-Lieb at any g or Q: each fibre is the closed manifold SU(2)^3 (EX-005 Lemma A,
   with negative-Hessian set of positive measure). The chart complement and the S15 conditional-mean gluing
   are exactly the parts BL cannot touch, and they are where M10 lives after S6.
2. No theta-uniform Hessian floor: lambda_min(theta) ~ (pi - theta)/(2 sqrt 2) (scratch numeric, potential
   Hessian; the phase Hessian B(q) away from q = 0 is computed nowhere in the repository).
3. Amplitude regularity: BL needs uniform second eta-derivatives of log A_g (or C^0 via Holley-Stroock);
   S3 supplies C^0 on a smaller neighbourhood; S6 assumes only the first fast derivative of a_g. Not established.
4. EX-014 sec 7 (conditional spectral-floor monotonicity) is not applicable: the object here is a conditional
   variance (a Fisher/covariance term), the very term EX-014 sec 4 says defeats that inequality. Not used.
5. Lemma Q (corpus-import/programs/pmbsf, sec 14) is open and was not used; the lexicon PMBSF
   "Stein-coupling" variant of brascamp-lieb is irrelevant to this fibre problem. No corpus-import/theory/under_review
   material was used.
6. M10 remains open. Nothing here changes the status of M10, H0-H4, R10 or the interacting-grid comparison.

## Exact next check (about one hour)

Compute the conditional phase Hessian B(theta) along the S4 graph for all 0 < theta < pi, not only the q -> 0
jet of S7: at the S4 point solve the fibre eikonal relation B G_fib B = Hess_fib V / 2 numerically with the
S5 electric cometric restricted to the fibre (mpmath, 9x9), and tabulate lambda_min(B(theta)). Then, in the
one-dimensional soft-direction model with the actual compact density exp(-2S/g^2) on a circle of radius
comparable to the chart, quadrature the variance of 2S/g^3 across the crossover pi - theta ~ g^2 for
g = 0.3, 0.1, 0.03 and check whether it stays <= C g^-2 (M10 budget: W_g >= v_*(theta)/g^2 ~ 4.69 g^-2 there).
Outcome: either the antipodal degeneration costs a constant (M10 g^-2 budget respected through the crossover
and the remaining problem is purely the S15 complement) or the budget breaks in the window, which would
locate a genuine obstruction to the synchronized M10 on fibres with 1 + w <~ C g^4.

## Why it deserves attention for the Clay objective chain

M10 -> M11-M15 -> uniform Hardy tail-resistance -> quantile source-energy criterion -> R10 source-derivative
bound (G19 route). The local Morse repair (tail-control sec 3) has three unproved inputs; this reading turns
one of them, the chart Poincare, into a consequence of the already-proved Agmon Hessian positivity and the
textbook Brascamp-Lieb inequality, and it sharpens the vague "antipodal degeneration" into a measurable
crossover window 1 + w <~ C g^4 with an explicit rate. It does not close M10; it tells the next agent exactly
which fibres and which term (S15 complement) still carry the whole difficulty.

## Retrieval observations (measured)

- September-vocabulary single phrasing: EX-014 sec 3 absent from the 10 direct hits and 5 related rows;
  abstention coverage 0.529, weak_match false. The top rows were the H0-H4 DERIV, score-frame passages,
  M10 (related rank 1) and RESULT:W6_CONDITIONAL_AGMON_GEOMETRY (related rank 4).
- 11-query plan (7 lexicon-expanded sub-queries all carrying the token M10 + 4 agent reformulations in
  EX-014/EX-005/EX-002 vocabulary): EX-014 and EX-005 absent from all 15 rows of the --full response; every row
  carries ranks only under q1-q7; the four reformulations q8-q11 contributed no surviving row. Fusion with
  seven M10-token sub-queries displaces every cross-family passage. abstention weak_match true, coverage 0.27.
- Own-vocabulary single queries: q8 (Schur/marginalisation/nu_x) -> EX-014:211-223 rank 1, :226-232 rank 2,
  coverage 0.812; q9 (conditional Poincare / Bakry-Emery / gamma^-1) -> EX-014:247-249 rank 3, :221-226 rank 6
  (ranks 1, 2, 4 are ext:tmp sc17-hessian review notes), weak_match true, coverage 0.417;
  q10 (Lemma A vocabulary) -> EX-005:23-26 rank 1, :73-79 rank 4, coverage 0.833.
- `connections` on the M10 seed: 7 record candidates, all W6/G19; 3 passage candidates, all external
  ext:research W6 campaign copies; no cross-family passage at all.
- Lexicon `brascamp-lieb` cites EX-004:766 and a PMBSF note but not EX-014:214-272, the full write-up; a
  variant citing EX-014 would let `plan` reach it.
- Two discovery cache fingerprints alternated across commands in one session (52c54e76... for search, plan and
  connections; 42678b34... for every pair call and the --full plan search), each reporting freshness matched;
  the review evidence entries therefore record different fingerprints.

## Registration inconsistencies noticed (outputs, not tasks)

- DERIV:W6_SOURCE_GENERATOR_SCORE_FRAME:CONDITIONAL_ENERGY_H0_H4 carries an anchor but no line range: the
  pair dossier resolves it to the whole document (lines 1-405), unlike the other DERIV records (M10 473-495,
  synchronized 317-375, both verified against the files).
- The imported-note passages carry no claim ids; a bears_on to EX-014 or EX-005 must target the NOTE
  catalogue id, which the propose fragments leave as FILL, and the hint they print (`workhouse why <path>`)
  is rejected by `why`.
- `discover propose --surface derivation` emits depends_on for kind scope-restriction (see above).
- RESULT:W6_CONDITIONAL_AGMON_GEOMETRY scope text and S2/S6 agree on the antipodal two-sphere; no
  inconsistency there. Score-frame lines 20-21 ("M10 ... not implied by, and does not imply, anything here")
  and the H0-H4 remaining text are consistent with this reading: the shared ingredient is the chart Poincare,
  not an implication between K^0_g and K_g.

## Scratch files

brief: .graph-state/case-m10-brascamp-lieb/brief.json (worktree, runtime tree). Here: search-main.json,
plan.json (edited, 11 queries), search-plan.json, search-plan-full.json, search-q8-ex014-schur.json,
search-q9-ex014-poincare.json, search-q10-ex005-lemmaA.json, connections-m10.json, pair-A..E json,
hessian_floor_check.py/.json, fiber_hessian_theta.py/.json, register/.
