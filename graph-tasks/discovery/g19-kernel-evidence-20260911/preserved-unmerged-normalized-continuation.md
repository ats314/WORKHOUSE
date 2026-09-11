# G19: verified operator algebra and normalized continuum comparison

Date: 2026-09-10 (verification and integration continued on 2026-09-11 UTC).
Source: the user's two pasted derivations, their read-only review, and the exact
Python calculations in task 01a08e08-5ced-7110-a2da-89b86120044d.
The original [dimension-five note](G19_DIMENSION_FIVE_IRRELEVANCE_LEMMA_20260910.md)
is retained unchanged. This is a corrected successor, not a new certificate for
the interacting continuum construction. Exact checks are in
[src/workhouse/invariants/g19_verified_continuation.py](../../src/workhouse/invariants/g19_verified_continuation.py).

## D1. Local polynomial selection and operator identities

Work in four Euclidean dimensions with SU(N), N >= 2, D = partial + [A,.],
[D] = [A] = 1 and [F] = 2. Operators are homogeneous bulk local polynomials
in curvature and its covariant derivatives with constant invariant
coefficients, without matter, spurions, boundaries or inverse derivatives.

A monomial with m derivatives and n curvatures has dimension and spacetime
tensor rank d = m + 2n. Since -I4 belongs to SO(4) and H4, an invariant
contraction tensor obeys C = (-1)^d C. Odd d therefore gives C = 0.
No dimension-two scalar survives: the linear SU(N) color trace vanishes and
delta(mu,nu) F(mu,nu) = 0. Apart from the identity, dimension four is the first
allowed scalar sector. Full H4 includes orientation-reversing reflections:
individual axis sign flips force a quadratic curvature contraction to pair
the same unordered index pair, and coordinate permutations fix equal weights.
Thus the parity-even dimension-four sector is the kinetic term.

The correct transformation is F[A^I](x) = +F[A](-x). The density
epsilon(mu,nu,rho,sigma) Tr(F(mu,nu)F(rho,sigma)) transforms with det(R);
inversion preserves it, while an orientation-reversing reflection changes its
sign. This is a transformation law, not evenness of every fixed field.

For antisymmetric spacetime matrices A, B, C,
Tr(ABC) = Tr((ABC)^T) = -Tr(CBA). Thus the symmetric color d_abc contraction
of F^a(mu,nu)F^b(nu,rho)F^c(rho,mu) is zero. An SU(2) epsilon_abc witness
using the three embedded rotation generators has value 6. Four curvatures
have dimension eight, not six.

For commuting coordinates x,
\[
\sum_{i<j}x_ix_j(x_i-x_j)^2
=(\sum_i x_i)(\sum_i x_i^3)-(\sum_i x_i^2)^2. \tag{D1.1}
\]
On the nonnegative simplex the summands are nonnegative; equality holds
exactly when all positive coordinates are equal. Every nonempty uniform
support is a zero. Dimensionless direction ratios give dimensionless variance.

## D2. Full Bianchi-compatible anisotropy projection

Use a positive invariant color inner product and T(abc) = D_a F_bc.
It is antisymmetric in b,c and obeys T(abc)+T(bca)+T(cab)=0.
There are 24 antisymmetric components per color and four independent Bianchi
constraints, leaving twenty independent components.

Set
\[
 I_1=\sum_{abc}\langle T_{abc},T_{abc}\rangle,\quad
 I_2=\sum_c\langle\sum_aT_{aac},\sum_bT_{bbc}\rangle,\quad
 H=\sum_{ac}\langle T_{aac},T_{aac}\rangle.
\]
Bianchi and antisymmetry give
J = sum(abc) <T_abc,T_bac> = I1/2.
For normalized Haar averaging on SO(4),
\[
 \sum_{\mu=1}^4\int R_{\mu a}R_{\mu b}R_{\mu d}R_{\mu e}\,dR
 =(\delta_{ab}\delta_{de}+\delta_{ad}\delta_{be}
   +\delta_{ae}\delta_{bd})/6.
\]
Indeed a unit vector on S3 has fourth moments E(v1^4)=1/8 and
E(v1^2 v2^2)=1/24; summing four frame rows gives the displayed tensor.
Contraction yields
\[
 \operatorname{Av}H=(I_2+I_1+J)/6=I_1/4+I_2/6,\qquad
 H_{\rm aniso}=H-I_1/4-I_2/6. \tag{D2.1}
\]
The rotational average of H_aniso is zero. H-I1/4 still contains the
isotropic term I2/6. These are operator structures; minimal basis claims
require an explicit convention on total derivatives and equations of motion.

## D3. Engineering scaling and the missing norm realization

For refinement a_k=a0*3^(-k), a dimension-six term in physical coordinates is
c6(k) a0^2 9^(-k) integral O6. This identifies an engineering coefficient.
It is not an activity-norm bound. Under x=ay, A(x)=a^(-1) Atilde(y),
\[
 a^2\int_{\rm block} d^4x\,O_6(A)
 =\int_{\rm unit\ block}d^4y\,O_6(\widetilde A). \tag{D3.1}
\]
The explicit powers cancel in dimensionless block coordinates. A source
estimate ||G_k|| <= B 9^(-k) requires a specified RG map, norms, localization,
coefficient and remainder estimates. No overall one-loop g^2 is inferred
merely from the propagator: vertices and field normalization also matter.

## D4. A sufficient nonlinear recurrence theorem

Let x_k >= 0 and u_k >= 0 satisfy
\[
 x_{k+1}\le(1/9+C_1u_k)x_k+C_2x_k^2+B9^{-k}, \tag{D4.1}
\]
with nonnegative constants. Assume C1*u_k <= 1/72 for all k. Choose M>0 with
x0 <= M, B <= M/72 and C2*M <= 1/72. Then x_k <= M 6^(-k) for every k.

Proof: assuming x_k <= M 6^(-k), divide its upper bound by M 6^(-k):
\[
 x_{k+1}/(M6^{-k})
 \le 1/8+C_2M6^{-k}+(B/M)(2/3)^k
 \le 11/72 < 1/6. \tag{D4.2}
\]
The base case is x0 <= M, so induction closes. In particular
sum(k>=n) x_k <= (6/5)M6^(-n).
More generally x_k <= M rho^k follows for 1/9 <= rho < 1 when
x0 <= M and 1/8+C2*M+B/M <= rho.
This is a proved scalar implication. Realizing D4.1 in the Wilson norms is
an independent analytic obligation.

## D5. Normalized interpolation and the coupling denominator

At finite cutoff and volume, put adjacent theories on a common measure space,
including changes of variables and Jacobians. Assume positive partition
functions, integrability and dominated differentiability. Quotient
differentiation gives
\[
 \frac d{ds}\langle O_s\rangle_s
 =\langle\dot O_s\rangle_s-\operatorname{Cov}_s(O_s,\dot S_s). \tag{D5.1}
\]
Here Zdot/Z=-<Sdot>; this term centers the covariance exactly.

Write u_k=g_k^2>0 and, in the common representation,
Sdot = (1/(4u_(k+1))-1/(4u_k))*E_k + R_k.
The remainder includes transported activity, discretization and any remaining
measure-comparison terms. Exactly,
\[
 |\operatorname{Cov}(O,\dot S^{\rm marg})|
 =\frac{|u_{k+1}-u_k|}{4u_ku_{k+1}}|\operatorname{Cov}(O,E_k)|. \tag{D5.2}
\]
Consequently the uniform estimate
|Cov_s(O_s,E_k)| <= C_E u_k u_(k+1)
implies a marginal response <= (C_E/4)|u_(k+1)-u_k|.
Exponential spatial clustering alone does not supply these coupling factors
or the uniform ultraviolet/contact estimates.

## D6. Conditional normalized Cauchy comparison

Assume D5 holds uniformly in cutoff, volume and interpolation parameter on a
common transported observable class, and
\[
 |\langle\dot O_s\rangle_s|\le A_O9^{-k},\quad
 |\operatorname{Cov}_s(O_s,E_k)|\le C_Eu_ku_{k+1},\quad
 |\operatorname{Cov}_s(O_s,R_k)|\le C_K(x_k+x_{k+1}),
\]
\[
 |u_{k+1}-u_k|\le D/(k+\kappa)^2,\qquad \kappa>0. \tag{D6.1}
\]
Suppose D4 gives x_k <= M rho^k, 1/9 <= rho < 1.
Integrating D5.1, set A=A_O+C_K M(1+rho), B_O=C_E D/4 to obtain
\[
 |\langle O\rangle_{k+1}-\langle O\rangle_k|
 \le A\rho^k+B_O/(k+\kappa)^2. \tag{D6.2}
\]
For m>n and n+kappa>1,
\[
 |\langle O\rangle_m-\langle O\rangle_n|
 \le A\rho^n/(1-\rho)+B_O/(n+\kappa-1). \tag{D6.3}
\]
The first sum is geometric. For the second, 1/t^2 <= 1/((t-1)t)
when t>1, and the latter telescopes. Both tails tend to zero; completeness of
C proves existence of the limiting expectation. The same estimate bounds its
error. The all-scale theorem is analytic; symbolic checks certify its algebra,
not D4.1 or D6.1 for the interacting model.

## D7. Conditional rotational and measure passage

For each R in SO(4), transport the rotated and unrotated theories to a common
space. Suppose the exact normalized comparison reads
\[
 \langle O_R\rangle_k-\langle O\rangle_k
 =\epsilon_{k,R}-\int_0^1\operatorname{Cov}_{k,s,R}(O,\Delta_R S_k)\,ds
\]
with |epsilon| <= A_R rho^k and sup_s |Cov| <= B_R rho^k.
Then the finite-scale defect is at most (A_R+B_R)rho^k. D6 applied to O
and O_R and the triangle inequality give <O_R>_infinity=<O>_infinity.
The full action difference and its inserted remainder must be controlled;
D2 alone does not prove these estimates.

Measure existence is separate: on a specified real nuclear test space,
pointwise convergent normalized positive-definite characteristic functionals
with equicontinuity at zero have a continuous normalized positive-definite
limit. Bochner-Minlos then constructs its probability measure on the
appropriate dual. The gauge-space identification and determining observable
class remain application hypotheses. No continuum mass gap is concluded.

## D8. Exact counterexamples to stronger intermediate claims

For r=1/9, q=1/8, B>0, x0=0,
\[
 x_{k+1}=qx_k+Br^k
 \quad\Longrightarrow\quad x_k=72B(8^{-k}-9^{-k}). \tag{D8.1}
\]
Substitution proves the recurrence and initial value. At k=6 the ratio to
72B9^(-k) equals 269297/262144>1. Hence that purported induction bound fails.

Even a running source has a resonant multiplier:
x_(k+1)=r*x_k+B*r^k/(k+1) gives x_k=9B H_k 9^(-k).
Since H_k is unbounded, no fixed M9^(-k) majorant follows; summability still
holds, for example H_k<=k and sum k9^(-k)<infinity.

For u_k=1/(alpha+beta*k), alpha,beta>0,
\[
 |u_{k+1}-u_k|/(4u_ku_{k+1})=\beta/4. \tag{D8.2}
\]
This refutes removal of the coupling denominator from a merely bounded
covariance estimate, not convergence of the actual theory.

## Handoff to the continuum obligation

Available inputs: local selection, full Bianchi projection, normalized
differentiation, a nonlinear scalar majorant and conditional Cauchy/rotation
passage. Remaining: actual subtracted RG norm/source bounds, uniform
normalized connected response, interscale observable and measure transport,
rotational defect control and the measure-extension hypotheses.
G19 and the original continuum Theorem 7.1 remain open at that application.
