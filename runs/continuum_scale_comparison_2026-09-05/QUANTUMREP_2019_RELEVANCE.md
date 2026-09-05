# Attached coupled-oscillator paper: useful mechanism and checked corrections

Read 5 September 2026 from the user-supplied file
`C:/WORKHOUSE/quantumrep-01-00009.pdf`, nine pages. Bibliography:
Urzua, Ramos-Prieto, Fernandez-Guasti, Moya-Cessa, *Solution to the
Time-Dependent Coupled Harmonic Oscillators Hamiltonian with Arbitrary
Interactions*, Quantum Reports 1 (2019), 82-90,
DOI 10.3390/quantum1010009. The original is CC BY 4.0. No source bytes changed.
Source SHA256:
`907d88f5b4e3142c337e26ad8315d3393f51fba4c0423028d5f24d40da2cf210`.

## What can be used directly

For H(t)=(p*p+q*K(t)q)/2 with a real symmetric K(t), every solution
u''+K(t)u=0 gives the exact invariant G_u=u*p-u'*q:

    partial_t G_u + i[H,G_u] = -(u''+Ku)*q = 0.

This is the paper's equations (1)-(8), written as one matrix identity.
With a full symplectic fundamental solution, it provides all canonical
linear invariants and a metaplectic description of the quadratic
propagator. It is useful for checking moving normal-mode frames and their
derivative terms. Arbitrary prescribed time dependence still requires
solving the classical matrix differential equation; it does not give a
scale-uniform Yang-Mills estimate by itself. A renormalization scale is
also not automatically the real-time variable of this Schrodinger problem.

## Specific corrections before importing displayed transformations

Pages 6-7 were rendered and inspected, so these are present in the PDF
and are not text-extraction artifacts.

1. Equations (26) and (28) give, at theta=pi/4,
   x-y -> -sqrt(2)y. The potential -eta u_x u_y (x-y)^2/2
   therefore becomes -eta u_x u_y y^2. In equations (29)-(30),
   lambda must consequently be -eta u_x u_y, rather than the printed
   +eta u_x u_y/sqrt(2), if those preceding conventions are retained.
   The kinetic coefficients in (30) agree with direct rotation.
2. For the unitary rotation R=exp[i theta(x p_y-y p_x)], its action on
   a function is f(x cos(theta)-y sin(theta),x sin(theta)+y cos(theta)).
   Equation (33) inserts an extra cos(theta)^(-2) in the first argument.
   That map has determinant sec(theta)^2 and changes the L2 norm by
   |cos(theta)|. It cannot be that unitary rotation. Removing the extra
   denominator repairs the action and makes a radial Gaussian invariant.
3. The displacement just before (31) is printed as
   exp(i alpha p_y) exp(beta y). For real beta the second factor is not
   unitary. A real momentum displacement requires an imaginary exponent;
   its sign and the derivative terms must be rederived consistently.

These corrections do not invalidate the directly verified matrix
invariant. They mean that the later displayed chain cannot be copied
unchanged into a verifier. The source's global transformations also need
coordinate patches at zeros of the chosen u_x or u_y in equation (19).

## Why a conserved invariant needs a separate uniform bound

For a positive oscillator frequency omega, evolution for a quarter period
has the exact classical matrix R_omega=[[0,1/omega],[-omega,0]].
Switching frequencies 1 then 2 for their quarter periods gives
R_2 R_1=diag(-1/2,-2). The Hamiltonian is positive at each time, but one
canonical amplitude doubles every cycle. Thus existence of an invariant
does not bound its comparison with instantaneous energy uniformly in time.

The constructive use in WORKHOUSE is to retain the full symplectic
transport and prove that comparison bound where a changing scale/frame
requires it. The current static boundary Schur calculation avoids this
transport issue; any later changing-frame argument can use the exact
invariant and switched-frequency example as independent controls.
