# Attached coupled-oscillator paper: useful mechanism and checked corrections

Read 5 September 2026 from the user-supplied file
[the preserved original PDF](../../literature/fulltext/quantumrep-01-00009.pdf), nine pages. Bibliography:
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

## Consistent unitary displacement and its retained dispersion

For real beta, exp(beta y) in the printed displacement is not unitary.
There is a useful more explicit repair. Put

```text
D=exp(i alpha p_y) exp(i beta y),  phi_D=D phi_theta,
```

where alpha,beta are real functions of t and p_x, mutually commuting and
commuting with y,p_y. This can be read fiberwise at fixed p_x. Then

```text
D y D*=y+alpha,             D p_y D*=p_y-beta,
i D' D*=-alpha' p_y-beta' y-alpha beta'.
```

For H_theta=(p_x^2+p_y^2)/(2mu)+p_x p_y/(2nu)+lambda y^2, cancellation
of the linear terms gives exactly the paper's equations (32):

```text
alpha'+beta/mu-p_x/(2nu)=0,     beta'-2lambda alpha=0.
```

But the remaining term in the corrected equation (31) is

```text
p_x^2/(2mu)-beta p_x/(2nu)+lambda alpha^2
    +beta^2/(2mu)-alpha beta'.
```

The last sign is minus, while the rendered equation prints plus. Since
alpha and beta may depend on p_x, this discrepancy can change the
retained dispersion; it is not necessarily an overall scalar phase.
The assessment's instruction to rederive the derivative terms is thus
necessary, and the formulas above supply one consistent repair.


## A concrete invariant/energy comparison criterion

The paper's mechanism suggests a usable benchmark more explicit than
simply requesting a bounded moving frame. Let K(t)>0 be absolutely
continuous and define

```text
kappa(t)=||K(t)^(-1/2) K'(t) K(t)^(-1/2)||,
A(t)=integral_0^t kappa(s) ds.
```

For a classical solution q''+Kq=0, its positive instantaneous energy
E=(|q'|^2+q.Kq)/2 satisfies

```text
E'=q.K'q/2,       |E'|<=kappa E,
exp(-A(t)) E(0)<=E(t)<=exp(A(t)) E(0).                  (1)
```

The same inequalities hold for the quantum energy quadratic forms under
the corresponding propagator, on finite-energy states. They concern the
positive total quadratic Hamiltonian, not a separately claimed vacuum-
subtracted spectral gap.

Equivalently, if Phi is the classical fundamental matrix and
W(t)=diag(K(t),I), the positive invariant coefficient matrix is

```text
I(t)=Phi(t)^(-T) W(0) Phi(t)^(-1),
exp(-A(t)) I(t)<=W(t)<=exp(A(t)) I(t).                  (2)
```

A finite total relative variation A(infinity) is therefore one explicit
sufficient condition for uniform invariant/energy equivalence. It is
dimension-independent in form and requires no diagonalization or
noncrossing hypothesis. A full fundamental matrix also avoids artificial
singularities when one particular scalar solution u_x or u_y vanishes in
the paper's logarithmic coordinate chart. This does not remove genuine
growth such as the switching example; its repeated jumps have an
unbounded accumulated relative-variation budget.

For the current scale analysis, (1)-(2) are a concrete test of a proposed
changing quadratic frame and its omitted derivative terms. Applying them
to a scale trajectory still requires an actual transport construction and
a finite variation/error budget for that construction. Renormalization
scale cannot silently be substituted for physical Schrodinger time.
The current exact static Schur-memory and Gaussian OS-observability
theorems do not need such a substitution.


## Evidence and provenance

The original PDF digest above was independently checked. Rendered pages 1,
6 and 7 confirm the bibliographic and displayed-equation readings. The
original assessment and independent review are preserved separately in
[runs/continuum_scale_comparison_2026-09-05](../../runs/continuum_scale_comparison_2026-09-05/README.md),
alongside the exact algebra controls. They establish their stated quadratic
identities; no source from this paper is a premise of an unproved Wilson
nonlinear scale estimate. The primary paper's linear invariant is retained
as a useful method rather than discarded because later printed formulas
need correction.
