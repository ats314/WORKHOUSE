# An actual true-ground obstruction to global scaled vertical coercivity

9 September 2026. Analytic derivation for the actual SU(2) two-square
bouquet. This graph has eight distinct electric edges; the squares share
only their base vertex. It is not the seven-edge adjacent-square strip,
and it is not an interacting lattice of coupled blocks.

## Result and implication

For the actual quantum ground of this Wilson graph, with the literal
retained observable U=U1 U2 and the physical simultaneous-conjugation
constraint, let D_g be the vertical part of the ground-transformed
Dirichlet form, scaled by g^2, where g=u^(-1/4). Then

    inf spec(D_g on physical conditional-mean-zero functions)
       <= (3a/16) g^2 = (3/4) g^2                  (a=4).       (A)

Consequently no positive g-independent vertical floor can hold on this
whole source complement. In contrast, the full scaled quantum complement
F_g satisfies, for all sufficiently small g,

    F_g >= sqrt(a)/2 = 1                            (a=4).       (B)

Thus a full fast quantum inverse can remain controlled while the proposed
global vertical Poincare surrogate loses its scaled gap. The implication
from local fast tangent positivity to that global conditional surrogate
is false without a restriction or an additional nonlocal input.

This is not a counterexample to W6, to the full interacting fast floor,
or specifically to the coupled cubic-lattice target. It excludes a general
conversion principle using only the stated local tangent data. The new
analytic input below is a log-concavity lemma for the actual rotor ground.

## 1. Actual Hamiltonian, ground and conditional form

Use the conventions of
`G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md`:

    h_u = -(a/2) Delta + 2u v,
    v(K)=2-ReTr K=2(1-x),
    K=x I+i v_vec.sigma,    x^2+|v_vec|^2=1,
    Delta_class=(1/4)[(1-x^2) d_xx-3x d_x].

The physical bouquet has a=4. Its two-loop Hamiltonian is
H_u=h_u,1+h_u,2. The unique positive normalized one-loop ground is the
class function omega_u(K)=w_u(x), and the true full ground is exactly
Omega_u(U1,U2)=omega_u(U1)omega_u(U2). This factorization is actual quantum
separability on this graph, not a replacement by a classical Gibbs law.

In global coordinates U=U1 U2, K=U1, the true conditional density is

    rho_U(K)=omega_u(K)^2 omega_u(K^-1 U)^2 / mu_u(U),
    mu_u(U)=integral omega_u(K)^2 omega_u(K^-1 U)^2 dK.

The exact electric cometric has coarse block 2a I, mixed block a I and
vertical Schur block S=(a/2)I. Therefore its vertical form is

    d_g[f] = g^2 (a/4) integral |grad_K f(U,K)|^2 dnu(U,K).    (1)

Here nu is the true ground probability and grad_K uses the stated
SU(2) Lie metric. The associated nonnegative operator acts on
Q={f:E(f|U)=0}. The physical subspace consists of simultaneously
conjugation-invariant functions; all test functions below lie there.
Explicitly Q_phys=ker E[.|U] intersect H_phys. Conditional expectation
of an invariant function is a class function of U, so this is the literal
physical source complement.

## 2. New lemma: log w_u(x) is concave on [-1,1]

Let v_t=e^(-t h_u)1. Positivity and compact elliptic regularity imply
v_t>0 and smoothness as a radial function of x, including the endpoints.
Set c=a/8, h=log v_t, r=h_x and q=h_xx. The exact radial heat equation is

    h_t=c[(1-x^2)(h_xx+h_x^2)-3x h_x]-4u(1-x).

Differentiating twice yields

    q_t=c[(1-x^2)q_xx + (2(1-x^2)r-7x)q_x
           +(2(1-x^2)q-8xr-8)q - 2r^2].                 (2)

On any finite time interval all the displayed coefficients are bounded.
Regarding its realized q-dependent zeroth-order coefficient as a bounded
coefficient, this is a scalar linear parabolic inequality for q, with a
nonpositive forcing. The initial datum is q(0,x)=0. The elementary maximum
principle applies on the closed interval even at the degenerate endpoints:
the diffusion coefficient vanishes there and the drift is -7 at x=1 and
+7 at x=-1, directed inward. At a positive boundary maximum the drift
term is nonpositive. Multiplication by e^(-Mt), with M larger than the
bounded zeroth-order coefficient, gives the usual strict-maximum
contradiction, including at the endpoints. Hence q<=0.

The normalized positive heat solution converges to omega_u in C^infinity
on the group, by its compact elliptic spectral expansion and positivity
of its ground component. Smooth radial endpoint coordinates give the
corresponding x-derivative convergence. Passing to the limit proves

    (log w_u)''(x)<=0,          -1<=x<=1.                       (3)

This is a statement about the exact true quantum ground for every u>=0.
No forbidden-region asymptotics or identification with e^(-action) enters.

## 3. Uniform central radial moment

At U=-I, the conditional law is rotationally invariant. In quaternion
scalar coordinate x it has density

    Z^-1 sqrt(1-x^2) w_u(x)^2 w_u(-x)^2 dx,

and the axis of v_vec is independent and uniform on S^2. By (3),
s(x)=log w_u(x)+log w_u(-x) is even and concave. Thus exp(2s(x)) is
nonincreasing as a function of |x|. Under the unweighted Haar scalar law
sqrt(1-x^2) dx, x^2 is increasing in |x|. The elementary opposite-monotone
covariance inequality therefore gives

    E_c[x^2] <= E_Haar[x^2] = 1/4,
    m_u := E_c[|v_vec|^2] >= 3/4.                            (4)

For completeness, the covariance inequality follows by taking two
independent scalar samples X,Y and averaging
(X^2-Y^2)(exp(2s(X))-exp(2s(Y)))<=0. Positivity of the normalizing integral
then gives (4).

## 4. Exact angular test and physical localization

For any unit n in R^3, let h_n(K)=n.v_vec(K). The SU(2) metric has

    |grad_K h_n|^2=(1-h_n^2)/4.

At the central conditional law, E_c[h_n]=0 and E_c[h_n^2]=m_u/3. Its
vertical Rayleigh quotient is therefore exactly

    g^2 (a/16)(3/m_u-1) <= g^2(3a/16).                    (5)

A fixed n is not itself a physical observable. The following construction
repairs that without adding loops or an external color direction. Define

    W(U)=v_vec(U),
    M(U)=E_rhoU[ W(U).v_vec(K) ],
    f(U,K)=chi(U)[ W(U).v_vec(K)-M(U) ],                  (6)

where chi is a smooth conjugation-invariant function supported in a small
punctured neighborhood of -I. Equation (6) is smooth, physically invariant
and exactly conditionally centered. It has nonzero norm when chi is
nonzero on an open set sufficiently close to the center.

Although W(-I)=0, for U near and different from -I the conditional
Rayleigh quotient of the bracket in (6) equals that of

    n(U).v_vec(K) - E_rhoU[n(U).v_vec(K)],
    n(U)=W(U)/|W(U)|.

For each fixed finite u, omega_u, the strictly positive marginal mu_u,
and the conditional density are smooth. The variance and energy in this
last quotient tend to their central values as U tends to -I. The limit is
uniform in the approach direction because the central law is isotropic
and the family is conjugation covariant. The denominator tends to
m_u/3>=1/4, so division is justified. Thus the conditional quotient is at
most the right side of (5) plus any prescribed epsilon throughout a
sufficiently small punctured neighborhood.

Vertical differentiation does not hit chi or M. Integrating the fiber
inequality against chi^2 times the positive marginal proves the same
bound for (6). Taking the infimum and then epsilon to zero proves (A).

This is not a measure-zero argument: for every finite u the tests use
open sets of positive Haar and true-marginal measure. Their supports may
shrink with u. Such dependence is permitted when testing a purported
uniform Poincare inequality over all physical Q functions. No uniform
lower bound on their probabilities is required.

## 5. Why the actual full complement keeps its scaled floor

The compact-rotor theorem in
`G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md`, section 1, applies to
kappa=a/2 and lambda=2u. It gives the unrestricted one-loop gap

    gap(h_u) >= (1/2)sqrt(a u)

at sufficiently large u. Tensor addition gives the same lower floor for
H_u-2e_u above its unique vacuum. The literal source space includes that
vacuum exactly: it consists of Omega_u times functions of U. Therefore
its literal complement is orthogonal to the vacuum, both before and
after imposing physical conjugation invariance. Restriction of the full
closed form gives

    g^2 Q(H_u-2e_u)Q >= (1/2)sqrt(a),

which proves (B). This uses a full Hamiltonian spectral estimate, not the
conditional rotor ground or a false uniform conditional gap.

The horizontal kinetic square supplies the energy that excludes the
localized tests (6) from a low full quantum window. This explains why the
vertical obstruction does not refute the actual full inverse bound.

## 6. Consequence for the requested coupled continuation

The graph-path proposal G4 requires D_g>=lambda I with lambda independent
of g and volume, if its G5 constant is to stay uniform. The stated local
fast tangent control cannot supply that unrestricted vertical statement:
the actual model above has the usual positive identity fast tangent and
yet violates the global conclusion. The issue is conditioning near a
central retained holonomy far outside the identity harmonic chart.

There are two defensible remaining routes:

1. Prove the full quantum Q-form floor directly, including interfaces,
   and estimate the residual in its inverse norm. The additive bouquet
   demonstrates that such a floor is compatible with the obstruction.
2. Prove a conditional floor on an explicitly restricted good retained
   set, and control the bad-set contribution in the actual complete
   transported residual's energy norm. Small marginal probability alone
   cannot control arbitrary normalized sources or gradients there.

Neither interface control nor the required source leakage estimate is
proved by this note. The result makes the proposed global conversion
target more precise: its unrestricted version is too strong, even for
an exact true-ground Wilson example, while the needed selected full
inverse route survives.

## Evidence scope

Equations (2), (4), (5) and (6) are analytic identities/inequalities with
the stated maximum-principle and domain arguments. A separate symbolic
check can verify the differentiations and moment constants; it would
not constitute a Lean proof of the operator result. All cited project
notes reside under
`C:/WORKHOUSE/WORKHOUSE-flat-holonomy-20260907/paper/research_notes/`.
No existing graph node or proof status was edited.
