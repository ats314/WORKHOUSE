# Earlier proof recovery: registered results and retained sources

11 September 2026. The author's earlier WORKHOUSE arguments are registered with
exact hypotheses, dependencies and source locators in the [complete derivation](../../docs/derivations/earlier-proof-recovery.md).
The [evidence package](../../runs/earlier_proof_recovery_2026-09-11/README.md) preserves the original bytes and replay receipts.

## E1. Cubic quotient regularity trichotomy

`RESULT:EARLIER_CUBIC_QUOTIENT_REGULARITY`

The cubic four-shape dispersion has the exact regularity trichotomy C nonzero: C^{1,1} not C^2; C=0,D nonzero: C^{3,1} not C^4; C=D=0: analytic.

Hypotheses: Real A,B,C,D; a_i=4 sin^2(k_i/2), q=sum a_i, e2=sum a_i a_j, e3=product a_i; Delta=Aq+Be2+4C e2/q+D e3/q extended by zero at Gamma.

Scope: Local differentiability at the cubic Gamma point for the specified four-shape formula.

Evidence: analytic; status: proven.

## E2. Equal-ray recovery and an independent holdout

`RESULT:EARLIER_EQUAL_RAY_IDENTIFICATION`

Equal-ray data recover A=R1, B=m2, C=b2/2-A and D=3m3-9m2, with independent holdout b3=2b2-R1.

Hypotheses: The dispersion consists of exactly the four shapes in E1; two distinct nonzero a values determine each affine divided ray.

Scope: Exact finite linear identification in the displayed basis; extra shapes require more data.

Evidence: analytic; status: proven.

## E3. No uniformly localized finite translation frame

`RESULT:EARLIER_LOCALIZED_FRAME_OBSTRUCTION`

A rank-one Bloch fiber with direction-dependent projector limits at Gamma has no finite exponentially localized translation frame with a uniform lower bound; its compact cube frame floor is 4 sin^2(pi/L).

Hypotheses: Analytic rank-one generators with S=sP; a positive frame floor approaching Gamma; P=w w*/q with leading w=Jk and q=|k|^2+O(|k|^4). For the explicit floor, q=sum_i 4 sin^2(k_i/2) on the nonzero periodic momentum grid.

Scope: Infinite-volume uniform localization obstruction and exact finite-volume frame conditioning; no dipolar remainder estimate.

Evidence: analytic; status: proven.

## E4. Sharp joint rank-volume scaling

`RESULT:EARLIER_JOINT_RANK_VOLUME_SCALING`

For N,L>=3 the rescaled second-order carrier gap G=4N^3 t_N L^2 sin^2(pi/L) increases in both variables, has sharp floor 405/68, strict ceiling pi^2 and joint limit pi^2; t_N decreases for real N>=3.

Hypotheses: Integer N,L>=3; u nonzero; t_N=2N(N^2-4)/[(N^2-1)(2N^2-1)(4N^2-9)]; Delta2=4t_N u^2 sin^2(pi/L).

Scope: Second-order coefficient and finite-volume scaling only; L=2 is excluded by an exact countercontrol.

Evidence: analytic; status: proven.

## E5a. Bounded support at a fixed order

`RESULT:EARLIER_FINITE_ORDER_SUPPORT`

At fixed order r a connected interaction history rooted in a finite support reaches only a finite union in its r-step support neighborhood.

Hypotheses: Bounded-support insertions; locally finite interaction support graph; finite root; at most r insertions.

Scope: Finite support combinatorics; not finite local Hilbert dimension.

Evidence: analytic; status: proven.

## E5b. Gram-null decoupling

`RESULT:EARLIER_GRAM_NULL_OPERATOR_QUOTIENT`

For G=C*C and B=C*AC, ker G=ker C is killed by B; G^+B is the physical Gram-quotient coordinate action, and C G^+B=AC on an invariant physical span.

Hypotheses: C maps a finite coefficient space onto its physical span; A is defined there, and the last intertwining conclusion assumes A-invariance.

Scope: Exact finite-dimensional physical quotient, with domains and invariance explicit.

Evidence: analytic; status: proven.

## E5c. Exact merging of decorated histories

`RESULT:EARLIER_DECORATED_HISTORY_MERGING`

Histories with identical complete continuation data can be merged by summing amplitudes without changing the fixed-order expansion.

Hypotheses: Finite reachable quotient states and known exact edge amplitudes; identical remaining state, support union, order, energy-resolvent data and fold ancestry.

Scope: Decorated dynamic programming; matching an endpoint alone is insufficient.

Evidence: analytic; status: proven.

## E5d. Finite-order nested-quotient spectral reduction

`RESULT:EARLIER_NESTED_QUOTIENT_REDUCTION`

The complete finite energy-decorated quotient history graph determines the connected effective operator through order r exactly, including direct/folded words, ordered support-union convolution and rooted subtraction.

Hypotheses: E5a locality and fixed order; finite retained space and finite reachable Wilson/Gram quotient. Nonresonant eliminated resolvents; complete direct and folded words; disconnected-vacuum removal. Complete ordered support-union convolution before rooted Mobius subtraction on a complete finite inclusion poset; fixed canonical Hermitian normalization.

Scope: Conditional finite-order reconstruction; no unrestricted G13 classification or momentum-shape absorption into a scalar shift.

Evidence: analytic; status: proven.

## E6a. Symmetry and residual control for a reduced shell

`RESULT:EARLIER_SHELL_SYMMETRY_RITZ_CONTROL`

Commuting finite Hermitian shell operators reduce to multiplicity-space matrices; every normalized lifted Ritz vector satisfies dist(lambda,Spec(E-uM))<=||(E-uM-lambda)v||.

Hypotheses: Finite Hermitian E,M commute with a finite unitary group action; real u,lambda; residual is evaluated in the full retained physical space.

Scope: Analytic isotypic reduction and full-space residual theorem; no uniform branch identification.

Evidence: analytic; status: proven.

## E6b. Retained B6 numerical campaign

`RESULT:EARLIER_B6_RETAINED_KRYLOV_CAMPAIGN`

The retained SU(3) B6 certificate reports radial dimensions 67,155,133 and maximum full-space Ritz residual 8.775675697349887e-14 on 201 g-values in [1,2], with crossing g=1.3039546641713.

Hypotheses: Historical source K6(u)=E-uM, source coupling conversion and branch choices; level-eight 511-column word spaces; relative SVD cutoff 1e-10. The certificate is retained and hash-verified; the B6 eigensolver was not rerun in this integration.

Scope: Historical finite-campaign numerical evidence only, with 355 representative coordinates and 798 including multiplicities.

Evidence: numerical; status: conditional.

## E7. Isolated positive matrix atom persists

`RESULT:EARLIER_ISOLATED_POSITIVE_MATRIX_ATOM`

Normalized positive matrix measures with locally uniform Laplace convergence through zero, a collapsing interval of uniformly positive matrix mass and a fixed empty annulus retain an isolated full-rank atom at the limiting positive energy.

Hypotheses: Finite d-by-d positive matrix measures on [0,infinity) of total mass I; locally uniform Laplace-transform convergence including zero. Closed intervals I_n converge to {M}, M>0; nu_n(I_n)>=z_*I for z_*>0; no mass at 0<dist(E,I_n)<Delta_* outside I_n. The scalar-residue conclusion additionally assumes covariance under one irreducible source representation.

Scope: Source-visible spectral pole theorem; no actual-source construction, unseen-sector gap or exact triplet stability.

Evidence: analytic; status: proven.

## E8. Conditional spectral floor and defect contraction

`RESULT:EARLIER_CONDITIONAL_SPECTRAL_FLOOR`

Conditional averaging raises the smallest eigenvalue relative to its conditional mean and contracts the positive spectral-floor defect: (c-lambda_min(E[H|G]))_+<=E[(c-lambda_min(H))_+|G].

Hypotheses: Integrable random symmetric matrices on one fixed finite-dimensional space; a sigma-algebra G and real c.

Scope: Finite matrix conditional Jensen statement; a marginalized Hessian can have an additional covariance subtraction.

Evidence: analytic; status: proven.

## E9. Six disjoint staple coordinates in four dimensions

`RESULT:EARLIER_D4_DISJOINT_STAPLE_COORDINATES`

Each of the six staples incident to a fixed D=4 link has a distinct selected link coordinate affecting only that staple within the star.

Hypotheses: Periodic nondegenerate cubic lattice with L>=3; for nu!=mu use (x+e_mu,nu) and (x+e_mu-e_nu,nu).

Scope: Exact incidence theorem; no statistical independence or force-rank conclusion.

Evidence: analytic; status: proven.

## E10. Positive-sector phase isolation

`RESULT:EARLIER_POSITIVE_SECTOR_PHASE_ISOLATION`

Nonnegative local weights with additive integer charge give nonnegative Laurent sector coefficients preserved by tensor multiplication and summation, with theta dependence evaluated last at z=exp(i theta).

Hypotheses: Finite configuration/charge sums, or absolute convergence justifying all expansions and evaluation; nonnegative local weights.

Scope: Sector-polynomial algebra; no general positive non-Abelian representation or efficient sign-problem solution.

Evidence: analytic; status: proven.

## E11. Convex VSU action on a bounded domain

`RESULT:EARLIER_VSU_BOUNDED_DOMAIN_WELLPOSEDNESS`

The VSU primitive F(s)=s-2+2(sqrt(s)+1)exp(-sqrt(s)) yields a strictly convex, quadratically coercive gradient energy and a unique weak Dirichlet solution on bounded Lipschitz domains.

Hypotheses: a0,G>0; mu(x)=1-exp(-x); bounded Lipschitz Omega in R^3; rho in L^(6/5)(Omega); phi in W_0^(1,2)(Omega).

Scope: Bounded-domain variational theorem for the specified constitutive model; whole-space and far-field limits remain separate.

Evidence: analytic; status: proven.

## E12. Determinant reduction with the missing parity restored

`RESULT:EARLIER_DETERMINANT_PARITY_REPAIR`

When w_r=0, det[x,u,w]=sgn(r,p,q)[x_r(u_p w_q-u_q w_p)-u_r(x_p w_q-x_q w_p)]; the parity factor is indispensable.

Hypotheses: Three-dimensional columns x,u,w; (r,p,q) is a permutation of (0,1,2); w_r=0.

Scope: Corrected exact determinant identity with all six row orders checked; original source preserved unchanged.

Evidence: analytic; status: proven.

## E13. A moving adjoint force has two derivative terms

`RESULT:EARLIER_MOVING_ADJOINT_FORCE_DERIVATIVE`

The moving adjoint force obeys d(Ad_g X)/dt=[g′g^-1,Ad_g X]+Ad_g X′; the selected staple can have a nonzero own-force derivative.

Hypotheses: Differentiable matrix-group path g and Lie-algebra path X; full product rule.

Scope: Exact derivative correction; the historical transversality/tube estimate requires a separate repaired proof.

Evidence: analytic; status: proven.

## E14. Equal-coupling SU(3) faces on a sphere have nonnegative covariance

`RESULT:EARLIER_SPHERE_EQUAL_COUPLING_COVARIANCE`

Two distinct equal-coupling SU(3) Wilson faces on a finite genus-zero cellulation have nonnegative normalized-trace covariance, equal to a variance of representation scores.

Hypotheses: Finite oriented cellulation of S^2 with normalized edge Haar measure and face weights exp(b_f ReTr(U_f)/3), all b_f>=0. The two distinct faces have identical coupling; zero-coupling endpoints are taken by continuity.

Scope: Genus-zero same-coupling covariance only; no cross-class or higher-dimensional plaquette closure.

Evidence: analytic; status: proven.

## E15. Exact SU(3) boundaries of the covariance argument

`RESULT:EARLIER_SU3_POSITIVITY_BOUNDARIES`

At SU(3) Haar measure Cov(ReTr(U)/3,ReTr(U^2)/3)=-1/18 and the balanced-degree-two crossed Weingarten coefficient is -1/24 (the direct coefficient is 1/8).

Hypotheses: Normalized Haar SU(3); the second observable is the twice-wound trace, not a second elementary plaquette.

Scope: Exact countercontrols to generic loop or coefficientwise positivity; no refutation of fully summed elementary-plaquette covariance.

Evidence: analytic; status: proven.

## E16. Reflection-adapted deterministic blocking preserves positivity

`RESULT:EARLIER_REFLECTION_ADAPTED_BLOCKING`

Reflection-adapted centered odd blocks and compatible deterministic Balaban-form path averages preserve reflection positivity on the coarse gauge-invariant positive-time algebra.

Hypotheses: Reflection-positive fine measure; reflection-permuted centered blocks with odd L and reflection/orientation-compatible path families. Conjugation-compatible logarithm on a reflection-invariant full-measure regular domain; positive coarse bonds have both endpoint blocks wholly in the fine positive half.

Scope: Specified deterministic raw blocking geometry; extra field partitions, stochastic kernels and multistep effective actions need their own hypotheses.

Evidence: analytic; status: proven.

## E17. Literal corner paths fail the required reflection identity

`RESULT:EARLIER_CORNER_BLOCKING_REFLECTION_DEFECT`

The literal lower-corner ordered-path L=3 blocking has gauge-invariant reflected coarse-plaquette trace defect (4/81)epsilon^4+O(epsilon^5), so that convention fails the required reflection identity.

Hypotheses: SU(2) periodic 12-by-12 lattice; source coordinate-order (0,1) trees; reflection (x,t)->(x,2-t); only exp(i epsilon sigma_x),exp(i epsilon sigma_y) at the two specified origin links. Analytic log/exp near identity; compare the coarse plaquette based at (9,9) using the retained source instrument.

Scope: Exact local failure of this intertwining convention; not a proof that every blocked measure violates reflection positivity.

Evidence: analytic; status: proven.

## Remaining application obligations

The four open E18 extensions remain explicit graph statements. E12 and E13 also
retain the rejected historical formulas as falsified statements, with corrections.
The existing SU(2) affine Casimir check and G19 stochastic-blocking counterexample
are linked as prior results. No continuum mass-gap closure, B6 numerical rerun
or whole-statement Lean formalization is asserted by this recovery.
