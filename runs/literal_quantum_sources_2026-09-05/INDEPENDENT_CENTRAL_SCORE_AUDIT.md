# Independent exact central true-quantum score audit

5 September 2026. The central SU(2) identity is accepted. It is an exact
consequence of the actual Wilson ground equation and Haar integration by
parts, with no WKB or assumed exponential ground wavefunction.

## 1. Actual class equation and endpoint domain

For unit generators T_a=i sigma_a/2 and the metric -2 ReTr(XY), the positive
single-holonomy Hamiltonian is

    H=-(a/2)Delta+2u v,  v=2-2cos(theta),  a>0,
    Delta_class=(1/4)(partial_theta^2+2cot(theta)partial_theta).

The four-link Wilson square has a=4. Its ground omega is positive and smooth
on the compact connected group and is a class function by uniqueness.
Writing l=log omega gives the exact Riccati equation

    l''=32u(1-cos(theta))/a-8e/a-(l')^2-2cot(theta)l'.

At both central endpoints, a smooth class function is even in its local
radial coordinate. Since omega is strictly positive at each fixed u,
l'=O(theta) near zero and O(pi-theta) near pi. These fixed-u endpoint
facts justify the integration below; no uniform pointwise lower bound on
omega as u grows is needed.

At coarse product U=-I, the true joint vacuum is
omega(theta)omega(pi-theta). Conditional Haar measure has radial density

    p(theta)=Z^-1 sin(theta)^2 omega(theta)^2 omega(pi-theta)^2,

and an independent uniform conjugacy axis n on S^2. Set
A=l'(theta), B=l'(pi-theta), d=A-B and s=A+B. The second term B is evaluated
at pi-theta; its derivative with respect to theta has the opposite sign.
Direct substitution gives

    d'=64u/a-16e/a-A^2-B^2-2cot(theta)d,
    p'/p=2cot(theta)+2d.

The endpoint flux p d vanishes as the cube of the endpoint distance.
Integrating (p d)' and canceling the Haar drift yields

    E(A^2+B^2)=64u/a-16e/a+2E d^2,
    E s^2=128u/a-32e/a+3E d^2.                         (1)

Every factor in (1) is confirmed independently. Dropping the Haar factor
sin(theta)^2 would change the identity and is not permitted.

## 2. Actual horizontal connection and quantum conditional score

In global variables U=U1U2, K=U1, the product electric cometric is

    C_uu=2a I,  C_ku=a I,  C_kk=a I,
    b=C_ku C_uu^-1=I/2,  S=a I/2.

This follows directly from the velocity map
(E1,E2) -> (E1+Ad(K)E2,E1), and uses Ad(K) orthogonal. It is the actual
two-square bouquet metric. It is not the adjacent-strip kinetic metric.

For a unit coarse tangent E at U=-I, the horizontal motion has
dot U=EU and dot K=(E/2)K. Both holonomy class angles then have derivative
(E_axis.n)/4 in the displayed basis. Consequently

    D_E log(Omega_joint^2)=(s/2)(E_axis.n).

The marginal mu(U) is a smooth conjugation-invariant scalar. Its derivative
at the central U=-I is an invariant adjoint covector, hence zero. The fiber
translation b has zero Haar divergence. Thus the intrinsic conditional score
is exactly s n/2. Choosing the opposite Lie basis reverses its sign and
leaves its covariance unchanged. Uniform axis covariance E(nn*)=I/3 gives

    I_cond=E(score score*)=(E s^2/12)I,
    C_uu^(1/2) I_cond C_uu^(1/2)
      =[64u/3-16e/3+(a/2)E d^2]I.                      (2)

## 3. Precise failed hypothesis and surviving route

The established fixed-a compact-rotor variational estimate gives
e(u)=O(sqrt(u)). Since E d^2>=0, (2) is at least
(64u/3-O(sqrt(u)))I. At -I, v(U)=4. Therefore no fixed constants C0,C1 can
bound this matrix globally by [C0+C1 sqrt(u)v(U)]I at large u.

This is not merely a measure-zero counterexample. For each fixed finite u,
the true positive ground and marginal are smooth, so the score covariance
is continuous. Once the proposed inequality is violated strictly at -I,
it is violated on an open neighborhood with positive quantum marginal
measure. The neighborhood may shrink with u; that does not restore a
uniform pointwise or essential-supremum bound.

The generic intrinsic-score identity and its conditional Schur/gap theorem
remain valid. What fails is the particular proposed global O(g^2) Fisher
hypothesis, already in the additive actual quantum bouquet. This result
does not rule out an energy-localized or integrated score estimate that
retains the rarity and coarse energy cost of the central region. Nor does
it prove the all-scale Wilson comparison or identify an OS history range.

## 4. Independent exact control and its limits

`check_central_score_identity_independent.py` passed. SHA256:
`9a16953abb64750ec87039c44dfc868e70a0b1ff5e392b23a630084d885af0e3`.
Saved report `central_score_identity_independent.json`, SHA256:
`ad4d2e94802fa270d27fbc15f33b46185ecc3ceca215f225d8f9f6617de46f61`.

The control checks the Wilson Riccati algebra, all factors in (1)--(2),
the normalized fundamental Casimir 3/4, three exact rational quaternion
horizontal motions, the original cometric/Schur calculation, and exact
spherical axis moments.

An independent positive smooth trial omega=2+cos(theta) is checked with
its **reconstructed** potential V=e+(a/2)Delta omega/omega. It verifies the
general-potential identity

    E s^2=(16/a)E[V(theta)+V(pi-theta)-2e]+3E d^2.

Its exact values are E s^2=96/113, E d^2=4/113,
E[2cot(theta)d]=28/113 and E d'=-36/113; the endpoint fluxes vanish.
The missing-Haar-drift calculation is rejected. This trial is not treated
as a Wilson solution: multiplying its would-be Wilson eigen-equation by
2+cos(theta) gives a cosine-squared residual coefficient -4u, nonzero for
u>0. Its role is an independent algebra/domain-normalization control.

The actual Wilson large-u obstruction is analytic, using its real positive
ground equation and energy bound. The finite examples do not substitute a
trial wavefunction for that ground or certify the full spectral theorem.
