# Source tilts, reflected pushforwards and finite-range inverse transport

11 September 2026. Targeted continuation of the historical-archive review.
Verbatim sources and hashes are in [the source package](../../runs/archive_derivations_2026-09-11/README.md).
The author's PMBSF interface, Appendix H and Appendix G supply the original arguments.
S1-S2 make differentiation explicit; S4 repairs normalized domination;
S6 supplies a conservative proved animal count. S9 and S14 are negative controls.
All conclusions retain their stated hypotheses and operator scope.

## S1. Inhomogeneous source tilting is a partition ratio

Let mu_beta=Z(beta)^-1 exp[-sum_p beta_p V_p] nu, with finite reference
measure nu, finitely many plaquettes and bounded real V_p. For any real t,

    E_beta exp(sum t_p V_p)=Z(beta-t)/Z(beta).                 (S1)

Combine exponentials inside the integral. This identity neither bounds
the ratio uniformly nor requires beta-t to be positive in this bounded setting.

## S2. Source response is covariance and log partition is convex

Set F(t)=log E_beta exp(sum t_p V_p) and let mu_t be the normalized tilt.
Boundedness justifies differentiating under the integral:

    partial_p F=E_t V_p,
    partial_p partial_q F=Cov_t(V_p,V_q),
    d/ds E_(t+s v) O|_(s=0)=Cov_t(O,sum v_p V_p).             (S2)

For real v, v^T Hess F v=Var_t(sum v_p V_p)>=0. Thus F is convex.
Uniform decay of mixed derivatives remains a separate estimate.

## S3. Pointwise envelopes do not order normalized tilts

Let disjoint A,B have probabilities q and 1/2, 0<q<1/2. Set X=1_A,
Y=1_(A union B), so X<=Y. With w=1+sX, v=1+sY and s=1/q,

    E_w X=q(1+s)/(1+sq)=(1+q)/2,
    E_v X=q(1+s)/(1+s(q+1/2)).                              (S3)

As q tends to zero these tend to 1/2 and zero, respectively. At q=1/100
they are 101/200 and 101/5200. Hence a cap-envelope tilted bound cannot
be transferred just from X<=Y. This is the normalization defect in the
August 22 H3 source audit, not a refutation of all possible LCI estimates.

## S4. Bounded log likelihood ratios transfer tilted estimates

For positive integrable weights v,w assume 0<a<=w/v<=b<infinity a.e.
The normalized measures satisfy

    dmu_w/dmu_v=(w/v)/E_v(w/v),
    a/b<=dmu_w/dmu_v<=b/a.                                  (S4)

Therefore E_w X<=(b/a)E_v X for any nonnegative measurable X.
An essential oscillation bound osc(log(w/v))<=d yields the factor exp(d).
An LCI transfer must bound this normalization cost or prove the smooth-source
estimate directly. This supplies a valid replacement hypothesis for S3.

## S5. Free energy implies conditional rooted-capacity summability

For a connected plaquette animal Gamma of size n assume V_p>=0 and
Theta(Gamma,U)<=gamma n. Let X_Gamma=product_(p in Gamma)1_{V_p>=delta},
delta>0. For t>0,s>=0, on X_Gamma=1 the sum of V_p is at least delta n,
so

    X_Gamma exp(s Theta)<=exp(-t delta n+s gamma n) exp(t sum_Gamma V_p).

If E exp(t sum_Gamma V_p)<=K^n uniformly, then

    E[X_Gamma exp(s Theta)]<=q0^n, q0=K exp(-t delta+s gamma). (S5)

With at most mu^(n-1) rooted animals of size n, writing q=exp(a)q0 gives

    sum_(Gamma containing root) exp(a n) E[X_Gamma exp(s Theta)]
       <=q/(1-mu q), provided mu q<1.                       (S5b)

This proves an implication under free-energy, capacity and counting inputs.
It does not prove PMBSF smooth-source LCI or far-source stability.

## S6. A conservative rooted-animal count

On a graph of maximum degree Delta>=1 with fixed neighbor orderings,
choose a deterministic rooted spanning tree for each connected n-vertex
set containing the root. Its depth-first traversal has length 2(n-1),
with at most Delta choices per step, and determines its visited set.
The chosen traversal map is injective. Thus

    number of rooted n-vertex animals<=Delta^[2(n-1)].       (S6)

For shared-link plaquette adjacency, r distinct links per plaquette and
at most nu plaquettes per link give degree <=r(nu-1). Hence a valid
mu in S5 is [r(nu-1)]^2: 400 for r=4,nu=6. This is not claimed optimal;
7 needs its own geometric definition and proof. An isolated root has
only its singleton animal and is treated separately.

## S7. Reflection-positive deterministic pushforward

Let (Omega_f,mu_f,Theta_f,A_f+) be reflection positive, pi a measurable
map to (Omega_c,Theta_c,A_c+), pi Theta_f=Theta_c pi, and assume every
F in A_c+ has pullback F composed with pi in A_f+. For mu_c=pi_*mu_f,
with theta F=conjugate(F composed with Theta),

    E_c[(theta_c F)F]
      =E_f[(theta_f(F composed with pi))(F composed with pi)]>=0. (S7)

This is the original Appendix H.3, including its essential positive-time
pullback condition. It proves permanence, not existence of an RG map.

## S8. Projective and weak limits preserve the stated OS forms

Assume a directed compatible reflected system, reflection-positive
finite-level measures, compatible positive-time pullbacks, and an existing
projective-limit measure with these marginals. Each cylinder observable
has precisely its finite-level OS form. A finite linear combination pulls
to a common level by directedness, so the cylinder algebra is RP.
This is Appendix H.6 with the common-level step made explicit.

For other limit constructions, convergence of every required OS product
expectation suffices, since a limit of nonnegative numbers is nonnegative.
Weak convergence supplies this for bounded continuous OS products;
unbounded products need uniform integrability or another convergence
argument. Neither existence nor nontriviality follows from permanence.

## S9. Reflection equivariance alone has a counterexample

Let independent fair signs x,y have reflection Theta(x,y)=(y,x) and
positive algebra f(x). Their law is RP because
E[conjugate(f(y))f(x)]=|E f(x)|^2. The map pi(x,y)=(x-y,y-x) commutes
with reflection. But for the first coarse coordinate F(x',y')=x',

    E[(theta F)F]=E[(y-x)(x-y)]=-2.                        (S9)

Its pullback mixes the two half spaces, locating exactly the missing
premise in the later synthesis's assertion.

## S10. Block Schur bound with row and column control

For K on a finite direct sum of Hilbert fibers with bounded blocks,
assume sup_x sum_y||K_xy||<=R0 and sup_y sum_x||K_xy||<=C0. Then

    ||K||<=sqrt(R0 C0).                                    (S10)

Put k_xy=||K_xy||. Bound |<g,Kf>| by sum_xy k_xy|g_x||f_y| and apply
weighted Cauchy-Schwarz to obtain
[sum_xy k_xy|g_x|^2]^(1/2)[sum_xy k_xy|f_y|^2]^(1/2).
Self-adjointness gives equal row/column bounds, but is not required for
K. This is Appendix G.2 and applies to the non-self-adjoint perturbation below.

## S11. Finite-range inverse transport with an explicit exponent

On a finite graph let A=A*>=a0 I, a0>0, have range R>=1 and
B=sup_x sum_(y!=x)||A_xy||. For B>0 set eta=log(1+a0/(2B))/R.
Fix y0, let phi(x)=dist(x,y0) and W_t=diag(exp(t phi)).
K_t=W_t A W_t^-1-A has row and column sums <=B(exp(tR)-1), since
A is self-adjoint and phi is 1-Lipschitz. S10 gives ||K_eta||<=a0/2.
The Neumann inverse gives ||(A+K_eta)^-1||<=2/a0. Undoing conjugation,

    ||(A^-1)_xy||<=(2/a0)exp[-eta dist(x,y)].               (S11)

For B=0 the inverse is diagonal. This reconstructs Appendix G.3 for
bounded blocks without assuming K_t self-adjoint. Unbounded fibers need
an additional common-domain argument.

## S12. Massive Maxwell row sums from incidence counting

Let C have r distinct signed unit entries per plaquette row and at most
nu incidences per link column. For M=m^2 I+alpha C*C, m^2>0,alpha>=0,
the floor is m^2 and the shared-plaquette graph range is one. Summing
entrywise absolute values over other links, using the triangle inequality
before summing the incident plaquettes, gives

    sup_e sum_(e'!=e)||M_ee'||<=alpha(r-1)nu.               (S12)

Each incident plaquette contributes r-1. This works even for multiple
shared plaquettes; individual combined entries need not be <=1.
For square plaquettes in four dimensions the upper bound is 18alpha.
S11 then gives eta=log(1+m^2/[2alpha(r-1)nu]) when the denominator is
positive. This is a deterministic inverse estimate, not a covariance identity.

## S13. Cochain horizontals reduce the massive Maxwell operator

For finite cochain differentials with d1 d0=0 let H=ker d0* and
M=m^2 I+alpha d1*d1, m^2>0,alpha>=0. Then d0* M f=m^2 d0* f.
Thus H is invariant and, by self-adjointness, reducing. The inverse of
M restricted to H is M^-1 restricted to H. This is Appendix G.6.
It does not identify its ambient zero-extension with the full M^-1.

## S14. Restriction need not preserve an ambient local kernel

Take the n-cycle cochain complex with d0 cyclic edge-vertex incidence
and d1=0. Then H=ker d0* is the constant edge vectors. For M=I, the
full inverse is diagonal, while the inverse on H extended by zero is
P_H=11^T/n, with every off-diagonal entry 1/n. At cycle distance
floor(n/2), no volume-independent C,eta>0 can bound this by
C exp[-eta floor(n/2)] for every n.

Thus Appendix G.7's ambient pointwise-kernel conclusion does not follow
from G.6 alone. S13 remains valid. Localized horizontal source pairings
can still use the full inverse when localization is proved. This is a
cochain-complex counterexample to the inference, not a claim that every
Wilson source family fails.

## Consequences and remaining Wilson obligations

S1-S6 supply precise normalization and rooted-summability interfaces;
S7-S9 recover usable RP permanence with its support condition; S10-S14
separate local full inverses from projected inverse kernels. Existing B6,
sigma5 and G3/C2 results are linked rather than duplicated. Actual Wilson
source-tilted stability, physical time, compatible continuum kernels,
nontriviality and weak-coupling rate remain required for G17/G19/G23.
