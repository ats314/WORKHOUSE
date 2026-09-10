# Adjacent SU(2) strip: complete second-order force and inverse energy

This is an exact local weak-field coefficient computation for the genuine
seven-edge two-square strip. The shared electric edge is retained. It uses
the physical simultaneous-conjugation sector and the literal scalar coarse
observation specified below. The calculation is at a fixed block; no
volume-uniform remainder is inferred from the finite polynomial identities.

## 1. Operator and chart

Use T_a=i sigma_a/2 and the original-link electric normalization H_E=-1/2
sum_e Delta_e. For based face holonomies U1,U2, the strip operator is

    H = -2(Delta_1+Delta_2) + sum_a L_1,a R_2,a
        +4 g^-4(2-x_1-x_2),

where U_j=x_j I+i v_j.sigma. The last term is 2u times the sum of the
fundamental Wilson potentials 2-ReTr U_j, with u=g^-4. The shared edge,
whose derivative is L_1-R_2, is responsible for the cross term.

Choose chord coordinates v_1=gX/2, v_2=gY/2, x_1=sqrt(1-g²|X|²/4), and
similarly for x_2. The density relative to dX dY is proportional to
1/(x_1 x_2). Its square-root conjugation is included in all operators.
Write R_X,a=(e_a cross X).grad_X. The flattened scaled generators are

    D_L,a = partial_a -(g/2) R_X,a
               -(g²/8)(|X|² partial_a+X_a)+O(g³),
    D_R,a = partial_a +(g/2) R_X,a
               -(g²/8)(|X|² partial_a+X_a)+O(g³).

Indeed their exact even part is x_1 partial_a +(partial_a x_1)/2.
Thus this computation includes the metric and Haar terms together.
The corresponding logarithmic coordinate is

    X_log=X+(g²/24)|X|²X+O(g⁴).

The physical sector consists of functions of |X|²,|Y|²,X.Y. Every
order-g term is a scalar triple product with vectors in span(X,Y), so
H1 annihilates the physical invariant core. Equivalently simultaneous
inversion of an SU(2) pair fixes its simultaneous-conjugation orbit.
The scalar source below also has no order-g term. Hence W1=t1=0 for
this specified physical one-block source.

## 2. Complete second jet

Put E_X=X.grad_X, E_Y=Y.grad_Y and C=grad_X.grad_Y. Direct multiplication
of the generators, including D1*D1, gives

    H2_el = (E_X²+E_Y²)/2 +3(E_X+E_Y)/2+3/2
            -[(|X|²+|Y|²)C+X.grad_Y+Y.grad_X]/8
            -(R_X.R_Y)/4,
    H2_mag = (|X|⁴+|Y|⁴)/32.

Introduce s=(X+Y)/sqrt(2), t=(X-Y)/sqrt(2), and a=|s|²,
b=|t|², c=s.t. Then

    H0=-(3/2)Delta_s-(5/2)Delta_t+(a+b)/2,
    Omega0=normalization*exp[-a/(2 sqrt(3))-b/(2 sqrt(5))],
    e0=3(sqrt(3)+sqrt(5))/2.

Its ground conjugation L0=Omega0^-1(H0-e0)Omega0 acts on invariant
polynomials by

    L0 f = -(3/2)(6 f_a+4a f_aa+4c f_ac+b f_cc)
           -(5/2)(6 f_b+4b f_bb+4c f_bc+a f_cc)
           +sqrt(3)(2a f_a+c f_c)+sqrt(5)(2b f_b+c f_c).

The complete forcing P2=Omega0^-1 H2 Omega0 is

    P2 = 5(a²+b²)/64 +(9/160+sqrt(15)/40)ab
         +(13/80+sqrt(15)/24)c²
         -(29sqrt(3)/48+9sqrt(5)/80)a
         -(sqrt(3)/16+39sqrt(5)/80)b+3/2.

The normalized ground correction Omega_g=Omega0(1+g²p2+...) is

    p2 = (411sqrt(3)-597sqrt(5))/5120
         +(3/64+29sqrt(15)/1280)a
         +(49/320-81sqrt(15)/6400)b
         -5sqrt(3)a²/768
         +(-11sqrt(3)+3sqrt(5))ab/640
         -sqrt(5)b²/256
         +(-9sqrt(5)-11sqrt(3))c²/960,

    e2 = -39/32-9sqrt(15)/640.

Both L0 p2+P2-e2=0 and E_Omega0² p2=0 hold exactly. These equations
include the true vacuum subtraction through second order, not a
classical Gibbs replacement.

## 3. Actual source and complete transported force

Take the literal scalar source of U=U1 U2,

    a_g=4[1-(ReTr U)/2]/g²=a+g² c²/8+O(g⁴).

The Gaussian conditional projection P0 integrates out t at fixed s;
on the simultaneous-conjugation sector it is the projection onto
functions of a. It reduces H0. Let m2(a) be the second coefficient of
the true normalized source marginal. The literal isometry therefore has

    J2 phi=Omega0[(p2-m2(a)/2)phi(a)+(c²/8)phi'(a)].

The marginal term and every retained-only term drop out after Q0 because
P0 reduces H0. For the first nonconstant retained eigenfunction

    phi(a)=a-3sqrt(3)/2,       L0 phi=2sqrt(3) phi,

the complete transported force is

    t2(phi) = Q0[H2(Omega0 phi)+(H0-e0)J2 phi-J2(L0 phi)].

Its explicitly evaluated polynomial is

    t2(phi)/Omega0 = (sqrt(5)-sqrt(3))
        [-33a(b-3sqrt(5)/2)/160
          +9(c²-sqrt(5)a/2)/80].

This force is nonzero. It includes the shared electric derivative, the
Haar correction, the quantum ground correction, and the motion of the
literal observation. Leaving out either p2 or c²/8 changes its answer.

The same computation gives the complete operator on every smooth radial
source, not only the first eigenfunction:

    t2(phi)/Omega0 = (sqrt(5)-sqrt(3))
        [-33a(b-3sqrt(5)/2)/160
          +9(c²-sqrt(5)a/2)/80] phi'(a).

To verify the absence of a second derivative term, the coefficient of
phi'' in H2(Omega0 phi)/Omega0 is 3(a²+c²)/4. The transport of the
observation eta=c²/8 contributes -6eta phi''=-3c² phi''/4. The
remaining 3a² phi''/4 is retained-only and is annihilated by Q0. The
ground product rule contributes only to phi'; its contribution is
-6(2a partial_a p2+c partial_c p2)phi'. The marginal normalization
also contributes only retained terms after the complete operator
commutator. Thus the displayed first-derivative operator is exact at
order g² on the radial invariant core.

For an independent short reproduction, the required commutator is

    Omega0^-1[H2,a]Omega0
       =-sqrt(3)a²/4-3sqrt(5)ab/20+29a/8+3b/8
         -(sqrt(3)+sqrt(5))c²/4.

Subtract 6(2a partial_a p2+c partial_c p2), add
(L0-2sqrt(3))(c²/8), and apply Q0. This yields exactly the force above.

## 4. Full inverse, including retained energy

Let B=b-3sqrt(5)/2 and Ctilde=c²-sqrt(5)a/2. On this finite Hermite span,

    L0 B=2sqrt(5) B,
    L0(aB)=2(sqrt(3)+sqrt(5))aB-9B,
    L0 Ctilde=2(sqrt(3)+sqrt(5))Ctilde-3B.

The actual reference fast inverse A0^-1=Q0(H0-e0)^-1 Q0 at z=0 is

    A0^-1 t2(phi)/Omega0 = (4-sqrt(15))
         [-33aB/320+9Ctilde/160-243B/(640sqrt(5))].

The term sqrt(3) in these denominators is the retained horizontal
oscillator energy. It has not been discarded in favor of a vertical
derivative estimate. Exact independent Gaussian moments give

    ||t2(phi)||² = 21627(4-sqrt(15))/4096,

    <t2(phi), A0^-1 t2(phi)>
       =1095201sqrt(5)/204800-2187sqrt(3)/320
       =0.120249075623735...,

    <phi,L0 phi>=9sqrt(3),

    <t2(phi),A0^-1t2(phi)>/<phi,L0 phi>
       =40563sqrt(15)/204800-243/320.

These values establish the complete first nonzero transported force and
its full inverse energy on an actual adjacent Wilson block. They are
coefficient identities for this source and block, not an all-source
interacting inverse estimate.

## 5. Reproduction

Run `verify_residual.py` with SymPy and `SYMPY_GROUND_TYPES=python`.
The program checks the second jet forcing, ground equation and
normalization, literal scalar observation coefficient, transported force,
full inverse equation, and exact Gaussian inverse norm. The derivation
above explains the analytic coefficient identities; finite controls do
not supply a remainder or an infinite-volume estimate.
