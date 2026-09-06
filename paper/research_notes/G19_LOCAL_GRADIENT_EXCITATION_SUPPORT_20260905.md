# Local gradient-energy leakage without a copy-count loss

5 September 2026. Analytic research continuation. The mathematical object here is
the sum of bad-region **local gradient energies**, not the probability of at
least one bad coarse coordinate. The latter has a concrete counterexample.

Inputs are the actual literal-source and common-Gauss constructions in
[G19_WILSON_LITERAL_VACUUM_COARSE_SOURCES_20260905.md](G19_WILSON_LITERAL_VACUUM_COARSE_SOURCES_20260905.md),
[G19_WILSON_COMMON_GAUSS_LITERAL_FAST_FLOOR_20260905.md](G19_WILSON_COMMON_GAUSS_LITERAL_FAST_FLOOR_20260905.md), and the selected-window
score obligations in [G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md](G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md),
Section 5. The originating derivation is preserved unchanged.

## 1. Abstract local form and exact support

Let (X_i,mu_i) be probability spaces. On L2(mu_i), let a_i be a nonnegative
closed gradient form with 1 in its domain and a_i[1]=0. For example,

    a_i(f,g)=(1/2) integral grad(f)^* C_i grad(g) dmu_i.

Let b_i be the local bad-region form obtained by inserting 1_(B_i), or more
generally any nonnegative form on the same domain satisfying 0<=b_i<=a_i.
Cauchy-Schwarz for the positive form gives a_i(1,f)=b_i(1,f)=0. In the
probability product, define

    a_M=sum_i a_i tensor I_(other factors),
    b_M=sum_i b_i tensor I_(other factors).                (1)

The local differential coefficients and the indicator B_i depend only on
coordinate i. This locality is an essential premise.

Decompose each factor as C1 plus H_i^0, where H_i^0 consists of mean-zero
functions. For S a finite subset of factors, take tensor products with
mean-zero entries exactly in S and constants elsewhere. If f_S and g_T are
finite such products and S is different from T, then

    a_M(f_S,g_T)=b_M(f_S,g_T)=0.                           (2)

Indeed a contribution from i vanishes if i is absent from either support,
because the local form kills constants. If i belongs to both, a coordinate
j in the symmetric difference of S and T remains outside i, and its ordinary
L2 inner product is between a mean-zero function and 1. That factor is zero.
The argument allows arbitrary superpositions within each support; extend by
polarization and form closure. It does not assume that multiplication by
1_(B_i) preserves mean-zero functions.

Consequently, if b_i<=epsilon a_i on each chosen local mean-zero profile
space E_i, then

    b_M<=epsilon a_M                                      (3)

on the tensor/direct-sum space built from those profiles, uniformly in M.
This follows by tensoring the compressed local form inequalities with the
positive spectator Gram matrices and summing. There is no factor equal to
the number of excited coordinates or to M in this relative bound. A bound
by the L2 norm rather than by a_i would have a different excitation-count
bookkeeping. Equation (3) also holds in a common compact-group invariant
subspace by restriction.

## 2. Exact common-Gauss low-window matrix

For identical factors choose real profiles R,A_1,...,A_d satisfying

    <1,R>=<1,A_a>=0,
    ||R||=1,  <A_a,A_b>=delta_ab,  <R,A_a>=0.             (4)

Here R is invariant and the A_a form an orthonormal real irreducible adjoint
multiplet. The profiles are in the local form domain. Let

    R_i=R on i, constants on the other factors,
    S_ij=d^-1/2 sum_a A_a on i tensor A_a on j, i<j.       (5)

Together with 1 these are an orthonormal invariant family. Write

    e_R=a[R],             e_R,B=b[R],
    e_A=(1/d)sum_a a[A_a], e_A,B=(1/d)sum_a b[A_a].        (6)

For the complete profile span

    f=c_0+sum_i x_i R_i+sum_(i<j) y_ij S_ij,

one has the exact identities

    a_M[f]=e_R sum_i |x_i|^2+2 e_A sum_(i<j)|y_ij|^2,
    b_M[f]=e_R,B sum_i |x_i|^2
                 +2 e_A,B sum_(i<j)|y_ij|^2.             (7)

Equation (2) removes radial-radial, radial-pair, disjoint-pair and overlapping-
pair off-diagonal entries. Within a pair, the spectator A inner product is
delta_ab, so the remaining local matrix is its trace divided by d. Thus (7)
does not even require b to be invariant or diagonal on the adjoint space.
Local radial-adjoint or adjoint-adjoint off-diagonal entries may be nonzero;
they are accounted for and cancel in (7). The full local form usually is
equivariant in the intended Wilson application, but this extra fact is not
needed for the displayed calculation.

If e_R,e_A>0, the optimal relative constant on this profile span, for M>=2,
is

    epsilon=max{e_R,B/e_R, e_A,B/e_A}.                    (8)

For M=1 omit the adjoint-pair ratio. Neither d nor the number M(M-1)/2 of
pair singlets multiplies (8). Arbitrary complex superpositions are included.

The countable result uses the constant-vacuum incomplete tensor product,
equivalently the cylinder-function completion of the probability product.
On this low span finite energy is the weighted l2 condition in (7). Finite
coefficient truncations converge in the a_M form norm. Since 0<=b_M<=a_M,
both formulas and (8) extend to the countable closure. No unbounded tensor
operator is defined merely by a formal matrix identity.

## 3. The actual projected Wilson profiles

For one actual strip, let J_u f=f(U)Omega_u with the true full vacuum and
its exact marginal mu_u. Let r_u be the normalized first physical radial
state and e_(u,a) the real orthonormal complete slow-adjoint frame used in
the common-Gauss theorem. Then

    rbar_u=J_u^* r_u,
    abar_(u,a)=J_u^* e_(u,a),
    ||rbar_u||^2=p_r=1-d_r^2,
    <abar_(u,a),abar_(u,b)>=p_A delta_ab,
    p_A=1-d_A^2.                                        (9)

Exact vacuum inclusion makes these profiles mean-zero. Equivariance gives
the stated orthogonality and scalar adjoint Gram. For sufficiently large u,
p_r,p_A>0. Set R=rbar_u/sqrt(p_r), A_a=abar_(u,a)/sqrt(p_A).
The profiles are smooth at every fixed u: the true ground and eigenfunctions
are smooth on the compact space and the exact marginal is strictly positive.
They are consequently in the true marginal gradient form domain, without
assuming a uniform positive lower bound on the marginal.

For M additive copies, the coarse profiles obtained by applying J_M^* to
the complete physical fine window below t_u are exactly the span (5), up to
the nonzero scalar normalizations sqrt(p_r) and p_A. Therefore (7)--(8) apply
to that whole actual source space, uniformly in finite/countable copy count.

This statement transports a LOCAL gradient-leakage estimate. It does not
prove that e_R,B/e_R or e_A,B/e_A tends to zero. Existing L2 source leakage
d_r,d_A does not by itself bound these derivative ratios. It also does not
identify this source space with a spectral window of the marginal operator.
Those are distinct possible next inputs.

## 4. Why an any-bad criterion fails

Assume identical factors with p=mu(B) in (0,1). Let f=R_1 depend only on
coordinate 1 and let r=b[R]/a[R]. Insert into the TOTAL gradient energy the
indicator that at least one of the M coordinates is bad. Independence gives

    a_(any bad)[R_1]/a_M[R_1]
      =1-(1-r)(1-p)^(M-1) -> 1.                         (10)

In contrast, the ratio for the local sum in (1) is exactly r for every M.
Even r=0 does not repair (10): bad vacuum coordinates which the source does
not differentiate account for the entire loss. Small one-block bad-region
probability cannot be union-bounded into a useful global good-event theorem.

This example is compatible with a globally invariant source R_1. It is not
removed by the common Gauss constraint. A theorem using (7) must keep the
indicator B_i attached to the derivative in the same coordinate i.

## 5. Componentwise product-score consequence

For the true product vacuum and local metric/connection, the conditional
density factorizes, rho_M=product_i rho_i. Its score covariance is block
diagonal: cross factors have zero covariance because each local intrinsic
score has conditional mean zero. The coarse cometric is likewise a direct
sum. Let F_M be the actual full-Q restricted form for the product literal
projection, restricted to the common invariant space if desired.

Suppose the full form established by the inverse-energy theorem supplies
F_M>=f0 Q_M with a constant independent of M. Assume, locally,

    C^(1/2) I C^(1/2)<=2 eta_G f0 I on G,
    C^(1/2) I C^(1/2)<=2 C_B f0 I on B.                 (11)

The actual Schur cross vector is T_M f=-(1/2)sum_i s_i^* C_i grad_i f.
It is conditionally mean-zero. Orthogonality of the centered local scores
gives its squared norm as the sum of the diagonal local quadratic terms,
even when f is an arbitrary function of all coarse coordinates. Thus

    ||F_M^-1/2 T_M f||^2
      <= eta_G a_M[f]+(C_B-eta_G)b_M[f].                 (12)

For C_B>=eta_G, (8) yields the coefficient

    eta_G+(C_B-eta_G)epsilon                             (13)

uniformly on the complete coarse profile space in Section 3. The looser
eta_G+C_B epsilon is always available with nonnegative coefficients.
No all-good product event is used. Local rates eta_G=O(u^-1/2), bounded C_B
and epsilon=O(u^-1/2) would therefore transfer with no volume loss. More
generally only the product C_B epsilon has to have the desired rate.

Equation (11) remains a local true-ground score premise. The center theorem
does not establish it, and the common-Gauss fine spectral gap does not by
itself provide the marginal high-energy control needed for a full Schur-gap
deduction. Equation (13) is a selected-source form estimate.

## 6. Cutoff sources can make the local bad energy exactly zero

An alternative to proving derivative tails for the projected profiles (9)
is to choose the bounded cutoff coarse profiles already used in the actual
source construction. In a small conjugation-invariant logarithm chart,
take an invariant cutoff chi supported inside G. A radial profile has the
form chi(U) times a rescaled invariant quadratic, minus its true marginal
mean. An adjoint profile is chi(U) times the rescaled adjoint logarithm.
Its true marginal mean is zero by equivariance. Centering the radial
profile adds a constant, so it does not change its gradient support.

After normalization, these profiles obey (4) and every gradient is supported
inside G. Hence e_R,B=e_A,B=0 and b_M[f]=0 exactly for their complete common-
Gauss source span, regardless of the probability of any bad coordinate.

This can be made compatible with the established entire fine-window frame.
First choose a fixed, sufficiently large cutoff radius in the rescaled
harmonic coarse variable; its truncated radial and adjoint oscillator
overlaps are nonzero and arbitrarily close to the full overlaps as that
radius increases. Keep that finite radius fixed and then take u large.
The bounded-cutoff local convergence argument in the common-Gauss source
proof preserves the nonzero actual radial overlap and the scalar adjoint
overlap. The supports shrink into any fixed near-identity chart, and the
tensor excitation-support calculation gives a uniform onto frame for the
same complete fine window. An explicit shrinking good region can instead
be used if it contains the chosen rescaled cutoff support.

For clarity, let those normalized local overlaps be z_r and z_A. Exact
support and equivariance give whole fine-window BB* weights

    1, |z_r|^2, |z_A|^4.                                (14)

They are positive independently of M. This concerns an explicitly chosen
coarse source space with onto projected fine image. It is not a declaration
that all marginal low-energy functions have compact gradient support.
For (12) on this cutoff space one needs the true-ground score estimate only
on the gradient support; no finite global C_B is required for that step.
The remaining high-retained-space issue is unchanged.

## 7. Consequence and exact controls

The volume transfer is settled for additive common-Gauss low source spaces:
local derivative leakage, including the possible local radial/adjoint cross
entries, does not acquire a combinatorial factor. The next mathematical
obligation is genuinely local: prove the actual score contraction on the
chosen gradient support, or bound the two local derivative ratios in (8).
Extending beyond additive blocks requires new estimates for the interacting
marginal, source geometry and cross-coordinate covariance.

The companion exact control evaluates tensor form matrices directly for
several copy counts using a local bad form with nonzero radial/adjoint and
adjoint/adjoint entries. It tests the complete radial/pair superposition
matrix, a non-centered-profile negative, and the any-bad formula. Those
finite identities check the algebra; the countable domain and actual Wilson
profile identifications are the analytic arguments above.

## Canonical source provenance and reproduction

This is the canonical copy of the independently reviewed 5 September
derivation [LOCAL_GRADIENT_EXCITATION_SUPPORT.md](../../runs/wilson_endpoint_local_score_2026-09-05/LOCAL_GRADIENT_EXCITATION_SUPPORT.md),
whose original SHA256 is `e955622980220d74e1a70144fcc6a9921c6b9831bf81204555e72c589b65a140`. The original proof bytes are
preserved; this copy adjusts only stage metadata and relative links,
then appends this explicitly separate provenance and follow-up record.

The [reproduction run](../../runs/wilson_endpoint_local_score_2026-09-05/README.md) preserves the analytic
sources and the precisely scoped finite controls:

- [check_local_gradient_tensorization.py](../../runs/wilson_endpoint_local_score_2026-09-05/check_local_gradient_tensorization.py)
- [local_gradient_tensorization_controls_final.json](../../runs/wilson_endpoint_local_score_2026-09-05/local_gradient_tensorization_controls_final.json)

The [actual localized true-ground score theorem](G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md)
subsequently proves the local additive score premise left as a target
in Section 7. Its selected-source scope remains distinct from the
[complete endpoint comparison](G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md),
which controls the full high retained spectrum. Ambient interacting
ground/source and scale comparisons remain open.
