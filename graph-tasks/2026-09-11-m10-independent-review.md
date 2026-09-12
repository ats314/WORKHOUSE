# Independent review of the M10 completion claim

Date: 2026-09-11. Reviewer: Codex.

## Identity and scope

Reviewed checkout: `C:/WORKHOUSE/worktrees/m10-score-domination-20260911`.
Branch: `antigravity/m10-score-domination-20260911`.
Local and remote submitted revision: `85675ed28afaec49c642e75ccd2074c4833af327`.
The checkout was initially clean. Live GitHub main was `66eb40cb1e4316f97ead0c3e8bd9b6aa8710aaf5`; its commit describes PR 147, the positive-time kernel gap criterion. GitHub returned no PR, in any state, for the submitted branch. The supplied `/pull/new/` URL is a PR creation link.

Targets:
- `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10`
- `DERIV:W6_SYNCHRONIZED_M10_DOMINATION:FULL_SCORE_DOMINATION_M10`

Question: Does the submitted argument establish uniform conditional-score domination for the actual four-face compact SU(2) quantum ground law under S13, including the antipodal transition?

## Retained graph evidence

- Start: `.graph-state/2026-09-11-m10-independent-review/start.json`.
- End: `.graph-state/2026-09-11-m10-independent-review/end.json`.
- Both snapshot fingerprints: `6e64b16331c8091b25fc7b82b40aece157acddea724c0adda48a73a3b643a829`.
- Input-manifest digest: `65ecc124a739ebd4ebdefddf5cb82eb86cf98c4af3c52537e7b21446e736f9b3`.
- Mode: saved; freshness unknown because no successful local index-generation provenance exists. These briefings executed no mathematical checks. Scientific inputs were unchanged between snapshots; this review record was added afterwards.

## Verdict

Request changes to the completion claim. The exact synchronized tangency, quadratic-jet Euler cancellation, potential floor, antipodal magnetic spectrum, and exact endpoint gauge invariance are valid ingredients. The full M10 theorem is not established by this submission. This review identifies missing implications, not a counterexample to M10 for the actual ground state.

### P1 — Differentiating the spatial WKB remainder is unjustified

Source: `docs/derivations/w6-synchronized-m10-domination.md:137-144`.

An expansion in spatial C-infinity norms does not by itself control the derivative of its remainder with respect to h or g. The identity partial_g = 2g partial_h supplies no bound on partial_h. The companion code substitutes a truncated formal expansion, so it cannot detect a bad differentiated remainder.

For an explicit check of this implication, let A(g,eta)=1+eta*g^4*sin(g^-6), on a bounded eta interval and small positive g, and Z=eta*partial_eta. This is positive and equals 1+O(g^4) in every spatial C^k norm. At eta=0 the spatial gradient of partial_g log A + g^-1 Z log A equals

`5*g^3*sin(g^-6) - 6*g^-3*cos(g^-6)`.

It is not O(1/g). SymPy independently confirmed this identity with zero residual. This example is not asserted to solve the Wilson eigenvalue equation; it demonstrates why a parameter-differentiated eigenfunction estimate is necessary.

The cited Klein–Rosenberger theorem is Theorem 6.5 of arXiv:2005.13852 (2020), not a 2005 paper. Its equation (6.9) and subsequent elliptic bootstrap provide spatial comparison estimates under Hypothesis 6.1. The submission needs a parameter-derivative estimate and a verified domain of applicability covering its claimed tubes, rather than differentiating a spatial remainder.

Source checked: https://arxiv.org/html/2005.13852#S6

### P1 — The conditional complement bound assumes its missing analytic inputs

Source: `docs/derivations/w6-synchronized-m10-domination.md:179-190`.

The local Psi denominator cancellation is correct. The rare-fiber normalization h_g(Q) remains. The proof then asserts a uniformly weighted differentiated-ground estimate, a uniform action gap, and a matching lower bound for h_g(Q), without establishing those estimates for the actual family.

In particular, the constant 4(sqrt(2)-1) comes from the Hessian of the magnetic potential in a specified chart. It is not an established lower bound for the Agmon phase Hessian. The source `w6-antipodal-magnetic-geometry.md`, A5–A7, explicitly separates these objects. A Hessian at a minimum also does not establish a global complement gap with exactly half that constant times the tube radius squared.

If the tube is around the single regular-fiber minimizer, its fixed-radius complement can approach a different point of the minimizing sphere as Q approaches -I; the action excess then tends to zero. A uniform treatment requires a suitable neighborhood of the whole limiting sphere and control of the remaining angular variable. The final exponential absorption is valid if the missing uniform numerator, denominator, and gap estimates are supplied.

### P1 — Endpoint gauge invariance does not bound the nearby angular transition

Source: `docs/derivations/w6-synchronized-m10-domination.md:221-222`.

At Q=-I the minimizing sphere is one gauge orbit. For Q different from -I, only its stabilizer acts within the fixed-Q fiber. The full sphere is not a gauge orbit in that fiber. The two soft magnetic eigenvalues are

`8*cos(theta/4)-4*sqrt(2) = sqrt(2)*(pi-theta) + O((pi-theta)^2)`.

SymPy independently confirmed the expansion, including the second-order coefficient -sqrt(2)/8. A7 proves exact endpoint invariance, while A6 retains the nonconstant angular term in nearby fibers. Neither seven positive magnetic normal directions nor a positive potential budget bounds the true normal/angular score variance uniformly in both g and pi-theta. The claimed O(g^-2) estimate across this transition remains to be proved.

### P1 — The new tests report a stronger result than they check

Sources: `scripts/verify_m10_amplitude_and_complement.py:101-135`, `scripts/check_antipodal_score_bound.py:114-132`, and `src/workhouse/invariants/w6_synchronized_m10.py`.

`verify_agmon_gap` multiplies a supplied positive magnetic constant by a selected radius; it never computes an Agmon action or proves a conditional gap. `verify_global_domination_bound` samples only the potential floor and its endpoint value; it never evaluates or bounds K_g, a score derivative, or the normalized conditional law. `check_gauge_score_invariance` returns literal True values and zero, with its valid analytic explanation only in comments. The formal amplitude calculation omits the remainder entirely.

Consequently successful tests do not supply T1 certification of full-fiber M10, amplitude derivative estimates, or complement suppression. Preserve the algebraic checks with accurately scoped names and retain the analytic hypotheses until they are proved. A valid analytic proof need not have a complete Lean formalization, but these checks do not close its missing steps.

## Verification and provenance

Used `C:/WORKHOUSE/REPO/.venv/Scripts/python.exe` with explicit `PYTHONPATH=C:/WORKHOUSE/worktrees/m10-score-domination-20260911/src`; confirmed `workhouse.__file__` resolves to that submitted source. No environment installation occurred.

- `python -m pytest tests/test_m10_synchronized_score.py tests/test_graph.py -q -p no:cacheprovider`: exit 0; all 41 tests passed.
- Independent SymPy checks: differentiated-remainder example and soft-mode expansion, as above.
- Full `workhouse verify --json`: exit 0; 600/600 checks passed, including all eight new M10 checks. Raw output: `.graph-state/2026-09-11-m10-independent-review/verify.json`, SHA-256 `ffda901af2b6d5de995df8c2f45dad42d85befc9f5a61a73b88ee9116143d694`. The command executes checks without cache reuse. This confirms the software results within the scopes of those checks, not the missing analytic implications.
- Full pytest suite and Lean build were not rerun.
- The initial `python -m workhouse` briefing invocation failed because the package has no `__main__`. Corrected to `python -c "from workhouse.cli import main; main()"`; startup and both retained briefings then succeeded.

The generic M10 target remains `open` in the submitted `ledger/derivation_statements.yaml:4915`, while the new specialized record claims `proven`. No closure of the generic target is registered by these changes. This is separate from the mathematical objections above.

## Ownership and handoff

Only this review record, its ignored `.graph-state` evidence directory, and the outer navigation task record are owned by this review. No mathematical source, ledger, generated scientific view, branch history, or remote publication was changed.

M11–M15 become applicable after actual M10 is proved for S13. The surviving ingredients reduce that task to parameter-differentiated actual-ground control, conditionally normalized complement estimates, and a uniform treatment of the antipodal angular transition. Source-energy jets, interacting-volume estimates, and continuum transport remain separate successors.
