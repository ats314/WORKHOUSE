# Independent review of the coupled-oscillator paper's relevance

5 September 2026. Read-only review of
[QUANTUMREP_2019_RELEVANCE.md](QUANTUMREP_2019_RELEVANCE.md), the original
`C:/WORKHOUSE/quantumrep-01-00009.pdf`, its extracted text, and rendered
pages 1, 6 and 7. The original SHA256 independently matches
`907d88f5b4e3142c337e26ad8315d3393f51fba4c0423028d5f24d40da2cf210`.
The paper is Urzua et al., Quantum Reports 1 (2019), 82-90,
DOI 10.3390/quantum1010009. No source or canonical repository file was changed.

Verdict: the assessment is mathematically sound and constructive. The
linear invariant is a useful exact benchmark for coupled quadratic
transport. The displayed later transformations require the stated
repairs. Neither the paper nor the assessment establishes a nonlinear
Yang-Mills scale comparison.

## 1. Checks against the original equations

For real symmetric K(t), H=(p.p+q.Kq)/2, and G=u.p-u'.q, direct canonical
commutation gives

```text
partial_t G+i[H,G]=-(u''+Ku).q.
```

This verifies the mechanism of the paper's equations (1)-(8), including
the sign convention. Because H is quadratic and G is linear, there is no
higher quantization correction. An independent exact two-coordinate
polynomial calculation gives zero residual with symbolic entries of K.
A full symplectic basis of classical solutions supplies a complete set
of canonical invariants. A single G, or its product GG*, need not be
coercive on all modes when there is more than one oscillator; a complete
positive quadratic invariant requires a complete basis and suitable
positive weights. The assessment correctly calls for that full basis.

The rendered page 6 confirms that equations (26) and (28) give
R(x-y)R*=-sqrt(2)y at theta=pi/4. Therefore the transformed potential is
-eta u_x u_y y^2, so lambda=-eta u_x u_y. The printed lambda in (30) has
both a different sign and an extra factor 1/sqrt(2). The kinetic
coefficients in (30) agree with direct rotation.

The rendered page 7 confirms the extra cos(theta)^2 denominator in the
first argument of (33). The printed linear coordinate map has determinant
sec(theta)^2. Its pullback multiplies the L2 norm by |cos(theta)|, wherever
cos(theta)!=0, whereas the actual rotation has determinant 1 and preserves
the norm. The correction in the assessment is exact.

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

The positive-frequency switching example also checks exactly:

```text
R_omega=[[0,1/omega],[-omega,0]],
R_2 R_1=diag(-1/2,-2).
```

Repeated identical quarter-period cycles therefore have an exponentially
growing canonical direction although both instantaneous frequencies are
positive. It refutes an inference from existence of an invariant to a
uniform comparison with instantaneous energy. It does not refute the
invariant or the exact quadratic solution.

## 2. A concrete additional comparison criterion

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

## 3. Evidence boundary

The three values in `quantumrep_exact_controls.txt` were independently
recomputed: the rotated potential, the two-frequency switch, and both
rotation determinants agree exactly. The displacement coefficients and
central invariant were additionally checked by symbolic polynomial
algebra. The original rendered formulas agree with the extraction on
every issue discussed above. These are finite algebraic checks and direct
quadratic arguments, not a Wilson interaction estimate, an OS blocking
identification, or a continuum mass theorem.
