# Current BC2 repair: bounded source/ghost/quantum-defect audit

9 September 2026. Read-only review of the current
`docs/derivations/yangmills-continuum-balaban-multiscale-proof.md`.
SHA256 at inspection:
`0e0f561f2e6b106d5f03ecbd32f1ca31f85f7f3abcb8fb830d759bc5c8eaf68a`.
Line numbers below refer to that version. The review is limited to current
Lemma 3.2, the source equations immediately following it, Section 5, and
the presence of an actual SC17 quantum-defect bound.

## Accepted repairs

1. The cellwise adjoint average has the correct transformation law.
   Equations (3.2), (3.4), lines 93 and 99, now average the fluctuation z
   relative to a transforming background B. Given the stated endpoint
   transporter convention, the cancellation at lines 103-108 is exact:

       Q_(B^g)(z^g)(x_Delta)
         =g(x_Delta) Q_B(z)(x_Delta) g(x_Delta)^(-1).

   The old inhomogeneous connection-average counterexample does not refute
   this repaired cellwise equation. It proves a valid source-geometric
   premise for background-relative adjoint variables.

2. The rescaling in (5.8), lines 203-204, has corrected the sign of the
   coupling exponent. Under the NEW domain condition

       z=g zeta, ||zeta||_infty<=g^(-kappa')/a,

   one indeed obtains a||z||_infty<=g^(1-kappa'), which tends to zero for
   kappa'<1. This is accepted algebra. It is conditional on the operator
   estimate preceding it and on using that actual rescaled domain.

3. The arithmetic absorption in (5.13), lines 224-226, is valid conditional
   on (5.11) and the stated curvature norm estimate: alpha_0>=8delta implies

       alpha_0/2-2delta>=alpha_0/4.

   The chosen alpha_0>=8delta+1 certainly satisfies this scalar implication.
   The earlier objection that the displayed absorption drops an adverse
   g^(-kappa) factor does not apply to this repaired conditional calculation.

## Exact remaining source premise

The cellwise identity does not yet establish the continuous source/fiber
used later. Equation (3.3), line 95, is an ordinary scalar-kernel interpolation
of vectors sitting in different gauge fibers. The last sentence of line 109,
"Convolution with the partition-of-unity kernel ... preserves this covariance,"
does not follow for position-dependent gauge transformations.

Exact two-cell check: at a point where both weights are 1/2, let the two
coarse adjoint vectors both equal T. Set g_1=I and choose g_2 in SU(2) with
Ad(g_2)T=-T. The original interpolation equals T, while the transformed
interpolation equals zero. No group conjugation maps a nonzero T to zero.
This is a failure of the plain interpolation step, not of repaired (3.4).
It can be repaired by transporting both adjoint outputs to the evaluation
fiber, or by retaining their separate endpoint-covariant coarse variables.

The subsequent variational functional still contains Q_k B in (3.7), line
117, and its Euler-Lagrange equation contains Q_k* (Q_k B-A_coarse) in
(3.9), line 125. These expressions are not identified with the repaired
operator Q_B acting on a homogeneous fluctuation. If their replacement
depends on B, its derivative and second derivative contribute to the
variational equation and the Hessian. Those contributions are not displayed
in (3.9) or (3.11), lines 125 and 133. Thus the valid cellwise equivariance
does not yet discharge the actual nonlinear source-fiber/induced-metric
premise used by SC17 or the existing source matching theorem.

## Exact remaining ghost premise in (5.8)

The first inequality of line 204 is

    ||(-Delta_B)^(-1) D_B ad(z)||_(L2->L2)
       <= C_0 a ||z||_infty.                              (A1)

No fast ghost projection, zero-mode restriction with uniform floor, or
mass term is specified for this inverse. The document does require
D_B.mu z_mu=0 in (5.2), line 189, and describes z as high-frequency in
line 88. An explicit equation Q_B z=0 was not located. The following
countertest nevertheless satisfies both divergence zero and block average
zero, so it does not rely on a forbidden constant fluctuation.

At B=0 on a periodic box of side R that is a multiple of the coarse block
side h=L a, put K=2pi/h, q=2pi/R and choose noncommuting Lie vectors Z,T:

    z_2(x)=Z cos(K x_1), z_mu(x)=0 for mu!=2,
    f(x)=exp(-iK x_1+iq x_2) T.

Then div z=partial_2 z_2=0 and the actual average of z over every h-block
vanishes. The ghost input f also has zero block average in x_1. Direct
multiplication gives

    D_mu ad(z_mu) f
      =(iq/2)[exp(iq x_2)+exp(-2iK x_1+iq x_2)] [Z,T].

The low output mode after (-Delta)^(-1) has coefficient i/(2q)[Z,T].
Orthogonality of the two output Fourier modes therefore gives the exact
lower bound

    ||(-Delta)^(-1) D_mu ad(z_mu)f||/||f||
       >= R ||[Z,T]||/(4pi ||T||).

This violates (A1) with volume-independent C_0 as R/a tends to infinity,
even for the high-frequency, divergence-free, zero-average z just displayed.
Multiplying Z by the repaired small factor g^(1-kappa') does not remove
the R/a growth. Complex ghost test functions are legitimate in the
complexified L2 norm; z itself is a real Lie-algebra-valued cosine.
For the literal R^4 statement, separated-frequency Schwartz wave packets
give the same infrared scaling, with a divergence-free polarization.

An ACTUAL output fast projection that removes the generated q mode, together
with a proved bound for its compressed inverse, would change this test.
The displayed operator in (5.8) contains no such projection. Merely requiring
z or the incoming ghost to be fast does not prevent high-high multiplication
from producing the low output mode. This is the precise domain issue.

Consequently the rescaling algebra is repaired, but the input inverse
estimate still needs a specified actual fast ghost domain and a uniform
bound there. The one-form operator with Q*Q in (5.3) is not the ghost
inverse appearing in (5.8).

There is also a separate exact determinant algebra issue at line 202.
Equation (5.6) is det(A-B), A=-Delta_B. Its finite-dimensional factor is
det(A) det(I-A^(-1)B). Equation (5.7) instead writes det(A)/det(I+A^(-1)B).
For a scalar perturbation t these are 1-t and 1/(1+t), whose difference is
t^2/(1+t). They agree only to first order, not as an exact determinant
identity. This issue is independent of the repaired coupling exponent.

The rescaled small-field domain also differs from the existing definition:
line 147, equation (4.1), bounds the unscaled z by g^(-kappa')/a. Lines
203-204 instead assume z=g zeta and ||zeta||<=g^(-kappa')/a, which gives
the smaller bound ||z||<=g^(1-kappa')/a. These domains need to be made
consistent in the actual field partition; rescaling the symbol does not
change which configurations satisfy the old bound.

## Exact remaining resolvent premise after stiffness repair

The spectral arithmetic (5.13) is valid under (5.11). However the weighted
identity (5.17), line 235, omits the conjugation of the nonlocal averaging
mass term Q_B*Q_B from (5.3). In general

    exp(w) Q_B*Q_B exp(-w) != Q_B*Q_B.

For an exact two-point averaging control, take

    P=(1/2)[[1,1],[1,1]], W=diag(2,1), v=(1,-1).

Then v*Pv=0 but v*WPW^(-1)v=-1/4, or -1/8 after division by ||v||^2.
The real quadratic correction is nonzero and adverse. This finite algebra
does not refute every possible Combes-Thomas estimate; it proves that the
equality asserted in (5.17) is missing the actual averaging commutator.
That term must be bounded, using its finite support/scale and stiffness,
before (5.18) follows with a chosen decay exponent.

There is likewise no general right to increase alpha_0 without changing
the Poincare coefficient in (5.11): on vectors in ker Q the left side's
averaging term vanishes. The constant must respect the actual fast
Poincare floor and block side. The document's BF4-BF6 citation at line 212
also invokes a bound proved for link-coordinate radius delta near a flat
background; a curvature bound ||F(B)||<=delta/a^2 is a different hypothesis
until a compatible background chart is constructed.

## Exact relation to SC17 R5/R12 and current conclusion

The needed conditional quantum defect is

    D_b = Hess_B[V_B+(H_out Omega)/Omega]-2epsilon A^2,
    ||D_b||_(s,infty)<=delta_R,
    2 beta_s(A)^2 delta_R/epsilon<1,                      (A2)

or the equivalent full projected Riccati source including cross, moving-
projection, kinetic-coordinate, and cutoff terms. A reference angle margin
and compatibility with the literal physical source fibers are also needed.

The current Section 5 supplies no expression or estimate for
Hess_B[(H_out Omega)/Omega]. Equation (5.1), line 185, names a classical
interaction remainder V_int(B,z). It does not identify that remainder with
the normalized physical-ground-law quantity in (A2). The nearby Section 6
continuation was checked only for such an input: (6.1), line 253, defines a
gauge-fixed Euclidean integral; line 293 states orders of Wick/Feynman
graphs, but supplies no bound for the actual normalized ground score,
outside-pressure Hessian, or the complete signed quantum remainder in (A2).
The targeted search found no formula for H_out, W_B, conditional ground
pressure, or a source-fiber Schur defect in this document.

Therefore the corrected cellwise adjoint law and coupling-power algebra
are accepted and should replace the stale BC2 objections to those exact
lines. They do not yet discharge SC17's remaining large-lambda quantum
defect: the first operator estimate in (5.8), the actual weighted Q*Q
commutator in (5.17), the nonlinear source-fiber identification, and finally
the concrete inequality (A2) remain unproved in this submission.

Exact SymPy controls executed in this audit: the averaging conjugation
quadratic values 0 and -1/4; the normalized correction -1/8; the determinant
difference t^2/(t+1); and the two-cell adjoint interpolation reducing T to 0.
These check the stated finite algebra, not the unproved operator estimates.
