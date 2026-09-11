# Recovered earlier proofs and their exact application boundaries

11 September 2026. These arguments originate in the author's earlier WORKHOUSE
files. This integration exposes their statements, assumptions, evidence and
successors in the theory graph. Original bytes are preserved in the
[source package](../../runs/earlier_proof_recovery_2026-09-11/README.md).
The accompanying paper record is
[Earlier proof recovery](../../paper/research_notes/EARLIER_PROOF_RECOVERY_20260911.md).

A valid analytic theorem is registered as proven with analytic evidence; its
whole-statement machine tier remains T3 unless separately formalized. The
native exact controls support only the calculations they actually execute.

## E1. Cubic quotient regularity trichotomy

Put a_i=4 sin²(k_i/2), q=sum_i a_i, e2=sum_(i<j) a_i a_j, e3=a_1 a_2 a_3,
and extend Delta=Aq+Be2+4C e2/q+D e3/q by Delta(0)=0 near Gamma.
For real A,B,C,D the extension has the following exact regularity:
C nonzero implies C^{1,1} but not C²; C=0,D nonzero implies C^{3,1} but not
C⁴; C=D=0 is analytic. Here C^{r,1} means r derivatives with locally
Lipschitz r-th derivative.

Proof. Write k=t n, |n|=1. Then a_i=t² n_i²-t⁴ n_i⁴/12+O(t⁶), uniformly
with angular derivatives. The leading nonanalytic term for C nonzero is
4C t² sum_(i<j)n_i² n_j². A smooth angular homogeneous function of degree 2
is C^{1,1}; if it were C² its degree-two term would be a quadratic form.
Sign and permutation invariance would make that form proportional to |k|²,
but the axis and diagonal angular values are 0 and 1/3. This is impossible.
When C=0, the leading D term is D k_1² k_2² k_3²/|k|², of degree 4,
so it is C^{3,1}. A putative quartic polynomial is even and vanishes on all
three coordinate planes, hence divisible by k_1² k_2² k_3² of degree 6.
It cannot equal the nonzero degree-four term. Higher-order remainders cannot
cancel either leading obstruction. Removing both quotients leaves an analytic
trigonometric polynomial.

Origin: singular-geometry note, Theorem 1, lines 75-104. The archived radial
expansion is replayed exactly; the differentiability proof is analytic.

## E2. Equal-ray recovery and an independent holdout

For equal nonzero a on one, two, or three coordinate entries, respectively,
E1=Aa, E2=2(A+C)a+Ba², E3=(3A+4C)a+(3B+D/3)a². Divide by a and let b2,b3
be intercepts and m2,m3 slopes of R2,R3. Then

    A=R1, B=m2, C=b2/2-A, D=3m3-9m2, b3=2b2-R1.       (E2)

Proof. Substitute (a,0,0),(a,a,0),(a,a,a) into the defining dispersion.
The displayed equations are the inverse linear system. Two distinct nonzero
a values determine each affine function. The last intercept identity is not
needed for the reconstruction and supplies a held-out consistency test.
This statement is specific to the four displayed shapes; additional shapes
require additional measurements. Origin: singular-geometry note, lines 133-199.

## E3. No uniformly localized finite translation frame

Assume a periodic rank-one Bloch fiber for k nonzero whose projector is
P(k)=w(k)w(k)* / q(k), with w analytic and leading term J k, J a fixed
orthogonal signed permutation. Its directional limits at Gamma are
J n n^T J^T and depend on n. No finite collection of exponentially localized
translation generators can span that fiber with a uniform positive lower
frame bound as k approaches Gamma.

Proof. Exponential localization makes each Bloch generator analytic.
If S(k) is the sum of its rank-one outer products, the spanning and frame
hypotheses give S(k)=s(k)P(k) for k nonzero with s(k)>=c>0. S is continuous,
and tr S=s, so S/tr S extends P continuously through Gamma. Two different
axis limits contradict this. The compact cube generator has S=qP; on the
nonzero periodic momentum grid its floor is 4 sin²(pi/L), which tends to zero
like L^{-2}. This proves the obstruction and the finite-volume conditioning
law, not an obstruction to finite-volume spanning itself.

Origin: singular-geometry note, lines 203-265. Its additional dipolar principal
term is consistent with differentiating the Coulomb kernel; the printed
O(|x|^{-4}) remainder remains a separate unverified extension (E18).

## E4. Sharp joint rank-volume scaling

For integers N,L>=3 and u nonzero, put

    t_N=2N(N²-4)/[(N²-1)(2N²-1)(4N²-9)],
    Delta2=4 t_N u² sin²(pi/L),
    G(N,L)=N³ L² Delta2/u².

Then G increases strictly in N and L, 405/68<=G<pi², equality on the left
occurs only at (3,3), and G tends to pi² as both variables tend to infinity.
In addition, t_N decreases strictly for real N>=3.

Proof. The numerator of -t_N'/2 is
24N^8-190N^6+329N^4-97N²-36. Substituting N²=9+y gives
24y⁴+674y³+6863y²+29639y+44694>0. The numerator of (N³t_N)'/(4N³)
becomes 2y³+116y²+1451y+5193>0, with positive common denominators.
The existing quarter-deficit identity gives 0<N³t_N<1/4 and limit 1/4.
For h(L)=L sin(pi/L), h'=sin x-x cos x with x=pi/L; this is positive since
its x derivative is x sin x>0 and its value at zero is zero. Also h(L)<pi
and h tends to pi. Thus G=4(N³t_N)h² has the stated monotonicity and limit.
At N=L=3 its exact value is 405/68. The L>=3 condition matters:
G(3,2)=60/17 does not meet the claimed lower endpoint.

Origin: singular-geometry note, lines 269-354. N³t_N monotonicity and the
quarter-deficit were already checked in rank_law.py; the new statement is the
joint scaling law, not a second registration of those ingredients.

## E5a. Bounded support at a fixed order

Let V be a sum of bounded-support interactions on a locally finite support
graph, with a finite root and fixed order r. A connected history containing
at most r insertions reaches only a finite union of supports within a finite
r-step neighborhood of the root.

Proof. Each insertion extends a connected support union through one of
finitely many adjacent interaction supports. Induct on insertion number.
The conclusion requires the stated locality and finite branching; it does
not assert finite-dimensional local Hilbert spaces by itself.
Origin: finite-order full derivation, lines 240-250.

## E5b. Gram-null decoupling

Let C map a finite coefficient space onto its physical span and G=C*C.
Then ker G=ker C. If B=C*AC is an overlap matrix of a physical operator A,
B kills ker G. The coordinate action on the Gram quotient is G^+ B;
it is not generally B. If the physical span is A-invariant,
C G^+ B=A C.

Proof. z*Gz=||Cz||² proves the kernel identity. Bz=C*A(Cz)=0 for Cz=0.
C G^+ C* is the orthogonal projection onto ran C, so the last assertion
follows from invariance. Resolvents must act on the corresponding physical
quotient with their actual domains; none is supplied by an overlap matrix alone.
Origin: finite-order full derivation, lines 252-295.

## E5c. Exact merging of decorated histories

At a fixed order with finitely many reachable quotient states and known edge
amplitudes, histories with the same complete remaining state, support-union,
order and energy-resolvent/fold data can be merged by summing their amplitudes.

Proof. Their future continuations have identical factors by the equality of
all retained data; distributing each continuation across the sum reproduces
the original history sum. Repeat finitely. Matching an endpoint or support
alone does not suffice when denominators or fold ancestry differ.
Origin: finite-order full derivation, lines 297-328.

## E5d. Finite-order nested-quotient spectral reduction

Under E5a, a finite retained space, a finite reachable Wilson/Gram quotient,
nonresonant eliminated-space resolvents, complete direct and folded words,
disconnected-vacuum removal, complete ordered support-union convolution,
a complete finite rooted inclusion poset, and a fixed canonical Hermitian
normalization, the energy-decorated finite quotient history graph determines
the connected effective operator through order r exactly.

Proof. E5a limits possible connected supports. The assumed finite reachable
quotient makes each support's physical state space finite, and E5b removes
only null coordinate directions. Nonresonance supplies every required
resolvent. Expanding every direct and folded word gives a finite weighted
history sum; E5c merges only histories with identical continuation data.
Perform the ordered support-union convolution before rooted Möbius subtraction.
Complete poset data removes the disconnected proper-support contributions,
and the stipulated Hermitian normalization fixes the operator representative.
Every step preserves the original expansion under these hypotheses.

The root-scalar readout and the operator shape quotient have different
codomains. A scalar shift is one momentum-independent multiple of identity;
it cannot absorb a nonconstant carrier shape. The graph determines amplitudes
from its decorated exact data, not from support topology alone.
Origin: finite-order full derivation, hypotheses 178-237 and theorem 447-547.
The unrestricted shortest-physical-history classification in G13 is not
supplied by these finite-order hypotheses.

## E6a. Symmetry and residual control for a reduced shell

If finite Hermitian E and M commute with a finite unitary group action, their
isotypic blocks have the form I_(d_lambda) tensor E_lambda and
I_(d_lambda) tensor M_lambda. A reduced word space inside a multiplicity
space may be used for Ritz approximation even when it is not invariant.
For a normalized lifted Ritz vector v and real lambda,

    dist(lambda, Spec(E-uM)) <= ||(E-uM-lambda)v||.       (E6a)

Proof. The isotypic form follows from Schur's lemma and the multiplicity-space
commutant. Expand v in an orthonormal eigenbasis of the full retained
Hermitian operator: the squared residual is the weighted average of
(e_j-lambda)² and bounds their minimum. Residuals must be computed after
lifting to the full retained space. This theorem supplies neither a selected
branch identification nor an all-u error bound without further estimates.
Origin: B6 shell reduction note, lines 1-115, and the finite-order full
source's B6 application.

## E6b. Retained B6 numerical campaign

The saved SU(3) open-cube B6 campaign uses K6(u)=E-uM and 511 word columns at
level eight per carrier. At relative SVD cutoff 10^{-10}, radial dimensions
are 67,155,133: 355 representative coordinates and 798 with cubic
multiplicities, compared with 1,916 odd and 3,864 physical coordinates.
The retained 201-point g-grid on [1,2] reports maximum full-space Ritz residual
8.775675697349887e-14 and crossing g=1.3039546641713.

These are historical numerical outputs with the original certificate retained
and hashed. This integration does not rerun the B6 eigensolver. Their use
requires the exact source operator, coupling conversion, cutoff and branch
selection of that campaign. E6a explains the meaning of a correct residual;
it does not certify that every archived floating-point entry was recomputed.

## E7. Isolated positive matrix atom persists

Let nu_n be positive d-by-d matrix measures on [0,infinity) with total mass I.
Assume their Laplace transforms converge locally uniformly for s>=0 including
zero. Let closed intervals I_n converge in Hausdorff distance to {M}, M>0,
with nu_n(I_n)>=z_*I for fixed z_*>0. Assume also that nu_n vanishes wherever
0<dist(E,I_n)<Delta_* for fixed Delta_*>0 outside I_n.
Then the limiting matrix measure exists, nu({M})>=z_*I, and it vanishes on
(M-Delta_*,M+Delta_*) minus {M}, intersected with [0,infinity).
For a single irreducible source representation, covariance makes the atom
z I with z>=z_*.

Proof. For each vector v, v*nu_n v is positive with fixed finite mass.
Laplace convergence and continuity at zero give tightness and weak convergence.
Polarization recovers the matrix limit. For each epsilon>0, eventually
I_n lies in the closed epsilon-neighborhood F of M, and
v*nu_n(F)v>=z_*||v||². The closed-set Portmanteau bound gives the same
lower bound for nu(F); continuity from above gives the atom. Every open
interval compactly contained in the punctured annulus has eventually zero
measure, hence zero limiting measure by the open-set inequality. A countable
cover finishes. Schur's lemma gives the scalar matrix in the irreducible case.

Origin: carrier-to-particle dossier, lines 607-730, d=3 and separated-time
Gram-normalized carrier sources. This proves a source-visible pole. A true
sector gap excluding dark states, rank stability, physical clock and source
identifications are additional application inputs (E18).

## E8. Conditional spectral floor and defect contraction

For an integrable random symmetric d-by-d matrix H and a sigma-algebra G,

    lambda_min(E[H|G]) >= E[lambda_min(H)|G] a.e.
    (c-lambda_min(E[H|G]))_+ <= E[(c-lambda_min(H))_+|G]. (E8)

Proof. For every rational unit-vector approximation v,
v*Hv>=lambda_min(H)||v||²; conditional expectation preserves this inequality.
Use a countable dense set to choose one common probability-one event and then
continuity and the Rayleigh infimum. For the second inequality use the first,
the decreasing map x->(c-x)_+, and conditional Jensen for that convex map.
Matrices must act on the same fixed finite space. A Hessian of a marginalized
potential can have a covariance subtraction, so E8 does not identify that
Hessian with E[H|G]. Origin: conditional spectral floor note, lines 14-82.

## E9. Six disjoint staple coordinates in four dimensions

On the nondegenerate periodic D=4 cubic lattice, L>=3, fix a link (x,mu).
For each nu different from mu choose the links (x+e_mu,nu) and
(x+e_mu-e_nu,nu) in the forward/backward nu staples. These six links are
distinct, each is in its own staple, and no selected link is in another of
the six staples incident to the fixed link.

Proof. Compare link directions and basepoints. Different nu give different
link directions; the two choices for one nu differ by e_nu. Among the other
staples, links parallel to mu have the wrong direction, and links at x or
x-e_nu have basepoints differing by e_mu. L>=3 prevents identifications
that would collapse the displayed star. Thus each chosen coordinate changes
only its selected staple inside that star. Statistical conditional independence
requires a separate interaction factorization.
Origin: LYAPUNOV_09 appendix, lines 51-180.

## E10. Positive-sector phase isolation

For a finite configuration sum with nonnegative local weights and additive
integer charge Q=sum q_c, define Z_Q by restricting to charge Q. Then
P(z)=sum_Q Z_Q z^Q has nonnegative Laurent coefficients and
Z(theta)=P(exp(i theta)). A tensor contraction built from those local
polynomials preserves coefficient nonnegativity under multiplication and
summation. The statement extends when absolute convergence justifies these
operations and evaluation.

Proof. Expand the products and collect equal total charges; each coefficient
is a sum of nonnegative products. Phase evaluation can be performed last.
This algebra does not prove a positive local representation for a general
non-Abelian character network, nor remove cancellations in the final Fourier
sum or establish an efficient contraction algorithm.
Origin: LATTICE_QCD_phase_isolation_principle.md, lines 28-114.

## E11. Convex VSU action on a bounded domain

For a0,G>0, let mu(x)=1-exp(-x) and
F(s)=s-2+2(sqrt(s)+1)exp(-sqrt(s)). Define
H(p)=a0² F(|p|²/a0²)/(8 pi G). Then
DH(p)=mu(|p|/a0)p/(4 pi G). For p nonzero its Hessian eigenvalues are
mu(x)/(4 pi G) transversely and [mu(x)+x mu'(x)]/(4 pi G) longitudinally.
They are positive. H is strictly convex, including through p=0, and
H(p)>=c|p|²-C for suitable positive c and finite C.

For a bounded Lipschitz Omega in R³ and rho in L^{6/5}(Omega),
J(phi)=integral H(grad phi)+integral rho phi has a unique minimizer in
W_0^{1,2}(Omega). It solves div(mu(|grad phi|/a0)grad phi)=4 pi G rho weakly.

Proof. Differentiate the displayed primitive; at zero use F(x²)~(2/3)x³.
Along every nonconstant line segment, positive second derivative away from
at most one zero point gives strict convexity. As x tends to infinity,
F(x²)/x² tends to one, giving quadratic coercivity up to a constant.
Sobolev and Poincare bound the source functional; Young's inequality gives
coercivity of J. The direct method in reflexive W_0^{1,2}, convex weak lower
semicontinuity, and strict convexity give existence and uniqueness. The first
variation, justified by the at-most-linear DH bound, gives the weak equation.

Origin: VSU_Convex_Poisson_WellPosedness.md, lines 43-243. This is a separate
constitutive-model result. The later whole-space limit and far-field claims
require additional normalization, estimates and boundary control (E18).

## E12. Determinant reduction with the missing parity restored

Let x,u,w be three-dimensional columns and w_r=0. Let (r,p,q) permute (0,1,2)
and let epsilon be its permutation sign. Then

    det[x,u,w] = epsilon *
      [x_r(u_p w_q-u_q w_p)-u_r(x_p w_q-x_q w_p)].       (E12)

Proof. Permute the rows to (r,p,q), expand along its first row, and undo the
row permutation. With p<q the sign is (-1)^r. The earlier formula omits
this sign: x=(0,1,0),u=(1,0,0),w=(0,0,1) gives -1, not +1.
This is a corrected exact identity; the original source remains unchanged.
Origin: 01_determinant_reduction_theorem.md, especially line 32.

## E13. A moving adjoint force has two derivative terms

For differentiable matrix-group g(t) and Lie-algebra X(t), with
Y=g' g^{-1},

    d/dt Ad_g X = [Y,Ad_g X] + Ad_g X'.                 (E13)

Proof. Differentiate gXg^{-1} and use (g^{-1})'=-g^{-1}g'g^{-1}.
In the standard SO(3) adjoint realization of SU(2), take g's rotation R_z(t)
and X(t)=(cos t,sin t,1). The omitted term at zero is (0,1,0), nonzero.
Disjointness of other staples does not make the selected staple's own force
constant. The printed LYAPUNOV_08 derivative at line 127 needs this term;
the rank/tube conclusion remains an open repair, not a refuted goal.

## E14. Equal-coupling SU(3) faces on a sphere have nonnegative covariance

On a finite oriented cellulation of S² with normalized edge Haar measure and
central Wilson face factors exp(b_f ReTr(U_f)/3), b_f>=0, two distinct faces
with equal coupling have nonnegative covariance of ReTr(U_f)/3.

Proof. Expand w_b=sum_R c_R(b)chi_R. The Taylor expansion of
exp[b(chi_3+chi_bar3)/6] and nonnegative tensor-product multiplicities give
c_R(b)>=0. Successive edge integrations and the Euler characteristic give
Z=sum_R d_R^{2-F} product_f c_R(b_f). For positive couplings set
pi_R=Z^{-1}d_R^{2-F}product_f c_R(b_f) and y_R(b)=c_R'(b)/c_R(b).
Differentiating at two distinct faces gives Cov_pi(y_R(b_p),y_R(b_q)).
At b_p=b_q this is Var_pi(y_R(b))>=0. Analyticity of compact-group integrals
and the nonnegative locally convergent coefficient series justify the
differentiations; zero couplings follow by continuity.

Origin: NOTE_G17_SU3_COVARIANCE_ATTACK_2026-08-30.md, section 1.
It settles equal-coupling pairs on a genus-zero surface, including within-class
pairs on a cube boundary. Unequal-coupling pairs and higher-dimensional
recoupling remain separate G17 inputs.

## E15. Exact SU(3) boundaries of the covariance argument

At Haar measure, A=ReTr U and B=ReTr U² have zero means and integral AB=-1/2;
after dividing both traces by three their covariance is -1/18.
Also Wg_3(e)=1/8 and Wg_3((12))=-1/24 at balanced degree two.

Proof. Tr U=chi_3 and Tr U²=chi_6-chi_bar3. Taking real parts and applying
character orthogonality leaves two terms -1/4. The balanced Weingarten
coefficients are 1/(N²-1) and -1/[N(N²-1)] at N=3. These facts obstruct a
generic all-loop positivity argument and a coefficientwise-positive lift;
they do not disprove elementary-plaquette covariance after the full sum.
Origin: the same G17 note, section 3.

## E16. Reflection-adapted deterministic blocking preserves positivity

Assume a reflection-positive fine Wilson measure. Choose centered blocks
with odd factor L, reflection permuting them, reflection- and
orientation-compatible path families, a conjugation-compatible logarithm on
a reflection-invariant full-measure regular domain, and positive coarse bonds
whose endpoint blocks lie wholly in the fine positive half. The Balaban-form
deterministic average with equal weights then preserves reflection positivity
on its coarse gauge-invariant positive-time algebra.

Proof. Reindex the equal-weight average by the reflection. Functorial path
holonomy, conjugation of log/exp and the paired orientations give
P theta=theta' P, or its gauge-equivalent version for gauge-invariant tests.
Locality in the two endpoint blocks gives one-sided pullback. For a coarse
test F, integral (Theta'F)F d(P_#mu)=integral (Theta(F o P))(F o P) dmu>=0.
This instantiates the already registered deterministic OS-history intertwiner
with the specified geometry. Additional gauge fixing, field partitions,
stochastic softening and multistep effective actions need their own checks.
Origin: NOTE_G19_balaban_blocking_reflection_positivity_2026-08-30.md, Lemma 3.1.

## E17. Literal corner paths fail the required reflection identity

For the source's lower-corner, coordinate-order (0,1) trees, SU(2) on the
periodic 12-by-12 lattice with L=3, reflection (x,t)->(x,2-t), and only
U((0,0),e0)=exp(i epsilon sigma_x), U((0,0),e1)=exp(i epsilon sigma_y)
nontrivial, the coarse plaquette rooted at (9,9) obeys

    tr P(rU)(boundary p)-tr (r_B P(U))(boundary p)
        = (4/81) epsilon^4 + O(epsilon^5).             (E17)

Proof. The retained exact Q(i) instrument implements the path holonomies,
logarithm and exponential through degree four. Its live replay gives zero
coefficients at degrees 0..3 and 4/81 at degree 4. Both sides are analytic
near identity, so the nonzero coefficient proves inequivalence on an open set.
Coarse gauge equivalence preserves each plaquette trace, hence cannot repair
this failure. SU(2) embeds into SU(N), N>=2; constant extension in extra
coordinates supplies the same local witness. This disproves the required
reflection identity for that convention, not reflection positivity of every
possible blocked measure by some other argument.

The same historical note's two-spin Markov counterexample is already in the
G19 route register: a one-point fine law sent equally to (+1,-1),(-1,+1)
is reflection equivariant and one-sided, but its coarse RP form on F=s_+
is -1. We retain its source and link the existing record rather than claim
this counterexample was absent. A factorization hypothesis is stronger than
mere Markov equivariance.

## E18. Explicit remaining application obligations

DIPOLAR_REMAINDER: establish the claimed O(|x|^{-4}) lattice-kernel remainder
with Fourier cutoff and derivative estimates; the frame obstruction E3 does
not require it.

PHYSICAL_CARRIER_REALIZATION: construct the actual cutoff sources, positive
residue floor, collapsing intervals, empty true-sector annulus, physical clock
and limiting measure required to apply E7. A source measure may miss dark
states. Norm-resolvent/projector identifications are additional requirements
for exactly one stable physical triplet.

STAPLE_TRANSVERSALITY_REPAIR: prove the rank and tube estimates using the full
E13 derivative; E9 alone establishes incidence and leaves this open.

VSU_WHOLE_SPACE: establish a compatible additive normalization, uniform local
estimates and the whole-space limit, then separately justify the asserted
far-field law. The bounded-domain theorem E11 does not supply these.

These open statements keep the historical extensions queryable. They do not
reopen results already proved under their explicit hypotheses above.
