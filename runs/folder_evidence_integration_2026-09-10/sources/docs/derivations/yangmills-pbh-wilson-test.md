# Testing the proposed PBH replacement on the actual Wilson quotient

8 September 2026. The proposal is evaluated as a new route, retaining the
existing W6 route and the established ground-state curvature results.
Some displayed equations were absent from the supplied quotation. The
normalizations below are explicit and define the version tested here.

## PBH-1. The actual measure and horizontal form

On a finite connected lattice use the compact link space Q=SU(2)^E with
the product bi-invariant electric metric, and the vertex gauge group K.
The quotient is stratified. Its principal stratum M_reg is a smooth
Riemannian quotient; it is not legitimate to treat every orbit as regular.
Let s(U)=sum_p(1-Re Tr U_p/2) and let beta>0 be its coefficient:

    d mu_beta = Z_beta^-1 exp(-beta s(U)) d vol_Q(U).

On M_reg, coarea gives the pushed-forward measure

    d nu_beta = Z_beta^-1 exp(-beta s(x)) v(x) d vol_M(x),
    W_beta = beta s - log v.                              (PBH-1)

Here v is the orbit-volume density, up to an irrelevant constant on this
stratum. Omitting v changes the Wilson measure. The gauge action and metric
are beta-independent. A positive overall rescaling of the kinetic metric
does not change the sign of the tensor tested below.

With left-trivialized variations, (d_U xi)_e=xi_s-Ad_(U_e)xi_t. Thus
V_U=im d_U and H_U=ker d_U*. On a fixed-rank regular chart,

    P_H=I-d_U(d_U* d_U)^dagger d_U*.

For a smooth gauge-invariant s and horizontal X,Y, the horizontal Hessian
is the ambient covariant Hessian restricted to these vectors, since the
vertical part of the submersion connection pairs to zero with grad s:

    Hess_M s(X,Y)=Hess_Q s(X^H,Y^H).                       (PBH-2)

This is a covariant Hessian, not an ordinary ambient coordinate Hessian.
At an orbit-type change, the fixed-rank formula cannot be differentiated
as if its rank remained constant.

The correct Wilson Bakry-Emery tensor on the regular stratum is

    Ric_nu = Ric_M - Hess_M log v + beta Hess_M s.          (PBH-3)

For L=c(Delta_M-grad W_beta . grad), c>0, the conventions are

    Gamma(f)=c |grad f|^2,
    Gamma_2(f)=c^2[|Hess f|^2+Ric_nu(grad f,grad f)].

A valid global tensor floor Ric_nu>=kappa metric, with the required closed
operator and boundary/domain hypotheses, gives gap(-L)>=c kappa. The
standard LSI reads Ent_nu(f^2)<=2/kappa int|grad f|^2 dnu.
For the quotation's Gamma=|grad f|^2/2, c=1/2 and the diffusion gap bound is
kappa/2. Identification with physical time is an additional statement.

## PBH-2. Explicit regular-point counterexample

Take one actual four-link plaquette, with all four vertex gauge actions.
Its quotient coordinate is the holonomy angle theta in [0,pi], where
Re Tr U=2 cos theta. The open interval is the principal stratum.

In the electric normalization -sum_e Delta_e/2, each link SU(2) metric
has radial line element 4 d theta_e^2. Minimizing
4 sum_(e=1)^4 dot theta_e^2 subject to sum_e dot theta_e=dot theta gives
the quotient line element d theta^2. The original four-link Laplacian on
class functions is therefore

    D=partial_theta^2+2 cot(theta) partial_theta.

This agrees with the existing character check: -D/2 has eigenvalue
n(n+2)/2 on the spin-n/2 character.

Product Haar pushes forward to sin^2(theta) d theta, so the exact Wilson
quotient measure and potential are

    d nu_beta = Z^-1 exp[-beta(1-cos theta)] sin^2(theta) d theta,
    W_beta = beta(1-cos theta)-2 log sin theta.

The one-dimensional quotient Ricci tensor is zero. Including the complete
Haar/orbit contribution gives

    Ric_nu(theta)=W_beta''(theta)
                =beta cos theta+2 csc^2(theta).            (PBH-4)

At the regular point theta=2pi/3,

    Ric_nu=8/3-beta/2.

For example beta=8 gives exactly -4/3. Thus the proposed globally positive
curvature bound fails at a smooth physical orbit, away from singular
endpoints, even before taking any limit. If the proposal instead omits
the Haar/orbit density, its curvature there is -beta/2 and fails more
directly, but that would also be a different measure.

This negative point really defeats the pointwise Gamma_2 criterion: choose
a smooth invariant test function with nonzero first derivative and zero
second derivative near theta=2pi/3, supported inside the regular interval.
Then its Hessian-square term vanishes at that point. For c=1/2 the ratio
Gamma_2/Gamma equals Ric_nu/2 there.

O'Neill's horizontal formula for orthonormal X,Y is

    K_M(X,Y)=K_Q(X^H,Y^H)+3|A_X Y|^2.

Its added term is nonnegative, not automatically strictly positive. It is
an integrability tensor of horizontal lifts, not the sectional curvature
of the gauge fibers and not the plaquette action. In this example the
horizontal space is one-dimensional: A_X X=0 and there are no horizontal
two-planes, yet 1-cos(2pi/3)=3/2>0. A universal strictly positive lower
bound inferred from non-Abelian field strength does not follow.

## PBH-3. The obstruction is not confined to a one-plaquette lattice

The following argument applies to a fixed finite connected SU(2) lattice
with at least two independent cycles and nonconstant Wilson action s;
in particular it applies to ordinary finite cubic lattices of sufficient
size. All statements here are finite-dimensional analytic arguments.

There exists a regular orbit and a horizontal direction with Hess_M s<0.
To prove this, choose a principal U_0 with grad_Q s(U_0) nonzero. Such a
point exists: principal points form a dense open set, and otherwise the
smooth function s would have zero gradient everywhere and be constant.
Let gamma be the complete product-metric geodesic starting in this
gradient direction. Since the gauge fundamental vector fields are Killing,
their inner products with dot gamma are conserved. They are zero at time
zero, so gamma remains horizontal. The function h(t)=s(gamma(t)) is bounded,
whereas h'(0)>0. Hence h'' is negative somewhere for t>0; otherwise h'
would remain at least h'(0) and h would be unbounded.

We can select such a negative point to be principal. For SU(2), tree
trivialization identifies stabilizers with common centralizers of loop
holonomies. Two noncommuting loop holonomies have common centralizer
{+I,-I}. Consequently, maximal infinitesimal gauge-orbit rank is exactly
the principal stratum for a graph with at least two cycles. Along gamma,

    det(d_gamma(t)* d_gamma(t))

is real analytic and positive at t=0. Its zeros are isolated, because it
is not identically zero. The open interval where h''<0 therefore contains
a principal point t_*. Projecting its horizontal tangent and using PBH-2
gives a unit X_* with Hess_M s(X_*,X_*)=-a_*<0.

At this fixed regular point the beta-independent geometric quantity

    k_*=(Ric_M-Hess_M log v)(X_*,X_*)

is finite. The exact weighted curvature there is k_*-beta a_*. It is
negative for all sufficiently large beta. Therefore:

**On each such fixed finite SU(2) Wilson lattice with the stated metric,
global nonnegative Bakry-Emery curvature on all regular configurations
cannot persist to arbitrarily large beta.**                        (PBH-5)

No uniform-in-volume estimate or continuum limit was used in this proof.
It disproves the proposed all-configuration pointwise curvature premise
along the weak bare-coupling end of this regularization. It does not
disprove a Poincare/LSI inequality obtainable by a different argument,
an integrated/localized curvature method, or a mass gap. It also does
not cover a different effective metric/weight unless that new construction
and its relation to the Wilson theory are supplied.

## PBH-4. Classical Wilson weight is not the quantum ground-state weight

There is a separate exact identification test on the same plaquette. Let

    H=-c D+k(1-cos theta),       c>0,
    psi_beta=constant exp[-beta(1-cos theta)/2].

The trial measure psi_beta^2 times Haar is precisely the classical
Wilson measure above. Direct differentiation gives

    (H psi_beta)/psi_beta
      =k(1-cos theta)+(3c beta/2)cos theta
                       -(c beta^2/4)sin^2 theta.           (PBH-6)

As a polynomial in z=cos theta, this has z^2 coefficient c beta^2/4>0.
It is not constant for any beta>0, regardless of how k is tuned.
Therefore this classical Wilson weight is not the exact ground-state
weight of this physical Wilson Hamiltonian. Its sampling generator cannot
be identified with the ground-transformed Hamiltonian by dropping the
nonconstant residual.

The existing [ground-state curvature derivation](yangmills-weighted-curvature.md),
GST-1 through GST-6, already supplies the correct alternative:

    psi^-1 H psi=-c L_psi+R,      R=(H psi)/psi,
    gap(H)>=c kappa-[E_(psi^2) R-inf R],

under its explicit curvature, form-domain and min-max hypotheses.
For a true ground state R is constant; for a trial state its error remains.
This is a legitimate route without R_0, but no corresponding uniform
interacting Yang-Mills curvature/residual budget is derived by the proposal.
The gap of a chosen sampling diffusion also does not, by itself, establish
the formula physical mass=sqrt(curvature). One must identify physical
Euclidean-time correlations or the physical Hamiltonian and its clock.

## PBH-5. The stated gradient-flow shortcut also fails an exact test

Use the same quotient metric and flow the actual plaquette action
s(theta)=1-cos theta. Up to a positive change of flow time, its equation is

    dot theta=-sin theta,
    tan(theta(t)/2)=exp(-t) tan(theta(0)/2).

For y=tan(theta(0)/2), its differential is

    D Phi_t=exp(-t)(1+y^2)/(1+exp(-2t)y^2).

At theta(0)=2pi/3 and t=log 2 this equals 8/7>1. Thus Wilson gradient flow
is not globally contractive in the proposed orbit metric, already on a
regular orbit of a finite plaquette. Decrease of the action is not
contraction of distances between configurations.

Nor is positive flow time a deterministic bound on all lattice energy
densities as a tends to zero. Every all-center SU(2) link configuration is
a stationary point of Wilson flow: every plaquette is +I or -I, and the
derivative of its trace against a traceless tangent is zero. Choose a
negative plaquette. Its normalized local energy a^-4(1-Re Tr U_p/2)
remains 2/a^4 at every flow time. This is a counterexample to a pointwise
bound, not to a possible bound on expectations after probabilistic and
renormalization estimates.

The established perturbative gradient-flow result does not fill those
missing estimates: Luescher-Weisz, arXiv:1101.0963, proves finiteness to
all perturbative orders after the underlying four-dimensional theory has
been renormalized. It does not construct the underlying nonperturbative
continuum measure or prove the small-flow-time OPE limit needed here.

## PBH-6. What survives and the exact stopping point

The proposal correctly points to a possible method independent of the
selected-resolvent W6. W6 was an energy-relative Schur remainder criterion,
not merely a boundary-sensitivity estimate; its reference retained the
physical Gaussian gauge constraint and a specified fast floor. There is
no reason to strike that open route because another route was suggested.

For the classical Wilson PBH proposal, the first failed derivation is

    Ric_M-Hess log v+beta Hess s >= rho_0 metric, rho_0>0,

globally on regular configurations throughout the weak-coupling regime.
Equation (PBH-4) supplies the explicit -4/3 witness and theorem (PBH-5)
proves failure at large
beta on the stated finite SU(2) cubic lattices. O'Neill positivity cannot
repair the signed Wilson Hessian in that limit. Consequently the proposed
chain cannot invoke that Bakry-Emery premise to close continuum G19.

For comparison, [Shen-Zhu-Zhu](https://www.sfb1283.uni-bielefeld.de/preprints/sfb22100.pdf),
Assumption 1.1 and Theorems 1.2 and 1.4, establish infinite-volume uniqueness
and LSI in an explicit strong-coupling regime. Their SU(N) bound is
|beta_SZZ|<1/[16(d-1)] for action N beta_SZZ Re sum Tr U_p.
Our SU(2) beta equals 4 beta_SZZ; these conventions must not be mixed.
Their spatial clustering also uses locality and generator-derivative
commutator bounds. This is a constructive implementation of the surviving
idea in its proved regime, not the claimed weak-coupling continuum result.

The alternative true-ground/trial-weight curvature route remains G23:
construct the physical weight or prove a uniform residual budget, including
the singular-orbit domain and physical-time identification. No Yang-Mills
continuum proof follows from the present calculation.

The corresponding unmet requirement in the supplied Jaffe-Witten document
is on printed page 11, Section 6.5:

> One must then verify the existence of limits of appropriate expectations of gauge-invariant observables as the lattice spacing tends to zero and as the volume tends to infinity.

The original attachment and its SHA-256 are recorded in the preceding
[selected-inverse validation](../validation/wilson-selected-2026-09-08.json).
This quotation states the required limiting conclusion; it does not itself
assert or prove the curvature counterexample derived above.

## Evidence

The five native PBH checks verify the quotient metric/Haar curvature,
Gamma_2 normalization, exact Hamiltonian residual, noncontractive flow
Jacobian and stationary center configuration. Theorem (PBH-5) is an analytic
compactness/geodesic argument, not a finite computation or a Lean theorem.
Original proposal text and originating research documents are not altered.

Additional source: [Moncrief-Marini-Maitra, orbit-space curvature](https://arxiv.org/abs/1809.06318),
with the detailed ground-state conventions already pinned and analyzed in
the linked GST derivation. Gradient-flow source:
[Luescher-Weisz](https://arxiv.org/abs/1101.0963).
