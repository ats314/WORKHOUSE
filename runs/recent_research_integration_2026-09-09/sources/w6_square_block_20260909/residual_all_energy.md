# All-retained-energy control of the complete first residual coefficient

9 September 2026. This is the next operator calculation after the sharp
first-force synthesis bound. It uses the actual twelve-edge square,
the source-compatible K in `source.md`, and the complete W_1 there.

## Statement

Write q=qt, u=qb-qt/2, s=rt, v=rb-rt/2, using the top/bottom variables
in `source.md`. These are independent Gaussian three-vectors, with
covariances sqrt(2), 1/2, 2, sqrt(6)/4 times the identity. Let

    a=|q|^2, T=q.(u cross s),
    delta=sqrt(2)(sqrt(2)-4)/7,
    b[phi]=8 E[a |phi'(a)|^2].

The actual first force is t_1 phi=delta T phi'(a). Let

    u_0=F_0^(-1)t_1 phi,
    rho_1=Q_0 W_1 u_0.

Then, for every radial source of finite Gaussian energy, the polynomial
core construction extends continuously and satisfies

    ||rho_1||^2 <= K_res b[phi],
    <rho_1,F_0^(-1)rho_1> <= (K_res/2) b[phi],           (R1)

where

    c_A=(9-4sqrt(2))/49,
    c_B=-211/98+sqrt(6)/4+134sqrt(2)/49,
    K_res=delta^2/8 [c_B/(4+sqrt(2))^2+15c_A/16]
         =0.0048897755570330521477... .                  (R2)

In particular the simple exact bounds are

    ||rho_1||^2 <= b[phi]/128,
    <rho_1,F_0^(-1)rho_1> <= b[phi]/256.                 (R3)

This is an all-source estimate for the first coefficient of the full
transported residual. The horizontal inverse is used before taking its
norm. No link derivative estimate of an unsmoothed residual is assumed.

## Complete radial action and exact fast moments

Put A=(2sqrt(2)-1)/7, B=(sqrt(2)-4)/14,
C=(4-sqrt(2))/7, D=sqrt(2)/4. The compact complete W_1, independently
verified in `source.md`, gives

    W_1[T psi(a)]=U psi(a)+2A V psi'(a),                 (R4)

before projection, where

    U=A[2s^2-(sqrt(2)/4)(a s^2-(q.s)^2)
           -(u^2 s^2-(u.s)^2)]
      +B[2a-(a u^2-(q.u)^2)-(a s^2-(q.s)^2)/4]
      +C[-2q.u+((q.u)s^2-(q.s)(u.s))/4]
      +D(sqrt(6)/3)[2(q.u)(v.s)-(q.s)(v.u)-(u.s)(v.q)],

    V=a s^2-(q.s)^2-T^2.

There is no psi'' term. The exact conditional means are

    E[U|q]=A(6-sqrt(2)a),  E[V|q]=2a.

Let U_c and V_c denote these centered profiles. Direct Gaussian Wick
evaluation, using the true Gaussian covariances above, gives

    E[U_c^2|q]=c_A a^2
        +(346+49sqrt(6)-328sqrt(2))a/196+84c_A,
    E[U_c V_c|q]=28A a+2f a^2,  f=(sqrt(2)-4)/7,
    E[V_c^2|q]=20a^2.                                  (R5)

These formulas are exact polynomials. The checker evaluates them after
rotating q to one coordinate axis, justified by simultaneous rotational
invariance, and integrates every fast monomial by its exact Gaussian
moment. It uses no numerical quadrature.

## Keep the full horizontal denominator

The radial inverse on this selected angular-one sector is

    u_0=delta T psi(a),
    [-8a d_a^2+(2sqrt(2)a-20)d_a+(sqrt(2)+4)]psi=phi'.

Equivalently define the vector-valued radial functions

    F(q)=q psi(|q|^2), G(q)=q phi'(|q|^2),
    L_q=-2 Delta_q+sqrt(2) q.gradient_q.

Then exactly

    F=(L_q+4)^(-1)G,  ||G||^2=b[phi]/8.                 (R6)

The number 4 is the sum of the two fast oscillator energies of u and s.
The radial vector subspace has L_q spectrum bounded below by sqrt(2).
The Gaussian form of L_q is 2||gradient F||^2, so spectral calculus gives

    ||F||^2 <= ||G||^2/(4+sqrt(2))^2,
    ||gradient F||^2
      <= (1/2) sup_(lambda>=sqrt(2)) lambda/(lambda+4)^2 ||G||^2
      <= ||G||^2/32.                                   (R7)

## Exact norm identity and closure

The radial a distribution is proportional to
a^(1/2) exp[-a/(2sqrt(2))] da. For core functions, integration by parts
gives

    Re E[a^k conjugate(psi) psi']
      =E[(a^k/(4sqrt(2))-(2k+1)a^(k-1)/4)|psi|^2].

Apply this to the cross term from (R5). The constant contribution cancels
exactly, and the a^2 term has a negative sign. The complete result is

    ||rho_1||^2=delta^2 E[
       c_B a |psi|^2-c_A a^2 |psi|^2
       +80c_A a^2 |psi'|^2].                            (R8)

For F=q psi(a), its gradient has transverse eigenvalue psi twice and
radial eigenvalue psi+2a psi'. Completing the square yields pointwise

    ||gradient F||_Frobenius^2
      =3|psi+2a psi'/3|^2+(8/3)a^2|psi'|^2,
    a^2|psi'|^2 <= (3/8)||gradient F||_Frobenius^2.       (R9)

Since c_A,c_B>0, discard the negative term in (R8), apply (R9), then
(R6)-(R7). This proves the first estimate (R1). In the physical Q space
at least one fast oscillator is excited: a fast-vacuum physical function
depends radially only on q and belongs to P. Every fast frequency is at
least 2. Consequently F_0>=2 on physical Q, proving the inverse bound.

For a purely rational certificate of the coarser constants, use

    7/5<sqrt(2)<10/7, 12/5<sqrt(6)<5/2.

They imply delta^2<1/3, 0<c_A<1/14, 0<c_B<5/2 and
4+sqrt(2)>5. Hence

    K_res < (1/24)[1/10+15/224]
          =187/26880 < 1/128.

Polynomials in a are dense in the retained Gaussian form domain. On
that core every identity above is finite and integration by parts has
vanishing boundary terms. The bounds then extend the map
phi -> Q_0 W_1 F_0^(-1)t_1 phi uniquely and continuously to the full
radial energy domain. This establishes the all-energy statement without
assuming a pointwise derivative bound for arbitrary source functions.

The first diagonal defect also vanishes on this selected family:
<u_0,W_1u_0>=0. Under simultaneous X_i -> -X_i, u_0 is odd and W_1u_0
is even, while the Gaussian measure is even.

## Uniform real spectral shifts

The same proof applies to u_0=(F_0-z)^(-1)t_1 phi uniformly for
0<=z<=z_*<2. Replace F in (R6) by (L_q+4-z)^(-1)G. Then

    ||F||^2 <= ||G||^2/(4+sqrt(2)-z_*)^2,
    ||gradient F||^2 <= ||G||^2/[8(4-z_*)].

Consequently

    ||Q W_1(F_0-z)^(-1)t_1 phi||^2 <= K_res(z_*) b[phi],

    K_res(z_*)=delta^2/8 [c_B/(4+sqrt(2)-z_*)^2
                         +15c_A/(4(4-z_*))].

Its inverse energy in F_0-z is bounded by K_res(z_*)/(2-z_*) times
b[phi]. This supplies a common constant on every such compact shift
interval; it does not require keeping z fixed at zero.

## Verification record

`residual_radial_moments.py` verifies the conditional means and every
coefficient of (R5)-(R8). The arbitrary-source extension is the analytic
spectral and form argument (R6)-(R9). These are coefficient-level results
for this fixed square; the notation rho_1 identifies precisely the
operator coefficient estimated, rather than a finite-g remainder.

`verify_residual_original_operator.py` supplies two independent exact
checks: it applies the original based-X operator H_1+[H_0,K] to T and
T*a before changing coordinates, then compares every resulting
coefficient with U and 2A V in (R4). Both checks pass. The moment checker
contains ten further exact controls, including the integrated norm
identity, the complex radial gradient square, and the resolvent gradient
maximum.
