# True-vacuum marginal, intrinsic score and weighted Schur comparison

5 September 2026. New analytic derivation. This connects the actual Hamiltonian
ground-state transform to the literal equal-time coarse-source projection. It
does not replace the true quantum ground measure by the Wilson Gibbs measure.
The uniform score hypotheses in Sections 3-4 are criteria, not established
all-volume Wilson estimates.

## 1. Geometric and domain assumptions

Let the full configuration space be a compact smooth product base/fiber, with
fixed Haar reference measures, or a Riemannian submersion admitting the same
integration identities. Let

    H = - (1/2) div(C grad) + V

be uniformly elliptic and have a strictly positive smooth normalized ground
Omega of energy E. The formulas also hold for closed forms with the indicated
smooth cores and justified approximation. Compactness here avoids boundary
terms; a Dirichlet truncation needs its own boundary argument.

The horizontal/vertical completion of the kinetic form is

    Gamma(F,G) = (D F)* A(U) D G + (grad_K F)* S grad_K G,
    D_a = partial_a + b_a(U,K).grad_K,
    A = C_uu,  S = C_kk - C_ku A^-1 C_uk.

Assume A depends only on the coarse variable U. The actual Wilson two-face
metrics have precisely this property. Derivatives can be invariant Haar
vector fields; conditional differentiation below uses the fixed fiber measure.
All identities extend to a compact gauge-invariant subspace when the data and
projection are equivariant. No independent Gauss constraint is imposed silently.

Set nu = Omega^2 dU dK, mu(U) = integral Omega(U,K)^2 dK and
rho_U(K) = Omega(U,K)^2/mu(U). Ground-state multiplication gives the exact form

    h[F,G] := <Omega F, (H-E) Omega G>
             = (1/2) integral Gamma(F,G) dnu.                 (1)

The literal coarse-source space is {f(U) Omega}; in L2(nu), its projection P
is conditional expectation over rho_U. Let Q=1-P. In particular P1=1 and
Q1=0 exactly. This is an equal-time source range, not an asserted full-history
reducing range. At every fixed parameter value, positivity and compactness make
P preserve H1 and the restricted Q form closed and densely defined.

## 2. The exact centered intrinsic score

Define the vector score with components

    s_a = partial_a log rho_U + div_K(rho_U b_a)/rho_U.       (2)

The divergence is relative to fiber Haar measure. The second term includes
both b_a.grad_K log rho_U and div_K b_a. Thus the connection term is retained,
including in charts where it does not vanish. Normalization and fiber
integration by parts give

    E_U s_a = 0,
    E_U D_a g = -E_U(g s_a),       whenever E_U g=0.          (3)

Indeed differentiating E_U g=0 gives E_U partial_a g =
-E_U(g partial_a log rho_U), and integrating the b_a derivative gives the
second term of (2). No conditional Poincare estimate enters this identity.

For a coarse f and a conditional mean-zero g, (1) therefore gives

    a[f] := h[f] = (1/2) integral (grad f)* A grad f dmu,
    h[f,g] = -(1/2) integral (grad f)* A E_U(g s) dmu.       (4)

This removes every derivative of g from the cross form. The scalar terms of
the original potential have already canceled against the *full* ground-state
energy in (1); they cannot be independently dropped before that transform.

## 3. Weighted score criterion for the actual Schur correction

Let F denote the self-adjoint operator of h restricted to Q. Assume its
actual full form satisfies

    h[g] >= integral w(U) |g|^2 dnu,   g in D(h) intersect Q,
    w(U) >= f0 > 0.                                           (5)

The weight can include a coarse barrier. It is not an assumed uniform gap of
the conditional fiber Hamiltonian. Define the conditional Fisher matrix
I(U)=E_U(s s*) and suppose

    A(U)^(1/2) I(U) A(U)^(1/2) <= 2 eta w(U) I,
    0 <= eta < 1.                                            (6)

For any vector xi, conditional Cauchy-Schwarz yields

    |xi* A^(1/2) E_U(g s)|^2
       <= E_U |g|^2 . xi* A^(1/2) I(U) A^(1/2) xi.

Taking the supremum over unit xi gives a bound without a coarse-dimension
factor. Applying it to (4), then applying Cauchy-Schwarz in U, proves

    |h[f,g]|^2 <= eta a[f] integral w(U)|g|^2 dnu
               <= eta a[f] h[g].                            (7)

For the Riesz lift U_S defined by h[f,g]=<F^(1/2) U_S f,
F^(1/2)g>, this implies

    ||F^(1/2) U_S f||^2 <= eta a[f],
    ||U_S f||^2 <= (eta/f0) a[f],
    (1-eta) a[f] <= k0[f] := a[f]-||F^(1/2)U_S f||^2
                              <= a[f].                      (8)

These are form statements on the coarse form domain. They do not by themselves
make U_S bounded on coarse L2. The separate fixed-block integration-by-parts
argument can supply that additional domain hypothesis for the full normalized
Schur theorem. The gap estimate below uses (7) directly and does not require
that additional boundedness.

## 4. Full-gap consequence and a constant-score variant

Assume the actual marginal Dirichlet form satisfies

    a[f] >= alpha ||f||^2,  integral f dmu=0,  alpha>0.       (9)

If psi=f+g is orthogonal to 1, then f is marginal mean-zero and g is
conditional mean-zero. For x=sqrt(a[f]), y=sqrt(h[g]), equation (7) gives

    h[psi] >= x^2+y^2-2 sqrt(eta) x y,
    ||psi||^2 <= x^2/alpha+y^2/f0.

The smallest generalized eigenvalue is

    Delta >= (alpha+f0-sqrt((alpha-f0)^2+4 eta alpha f0))/2. (10)

This is positive for eta<1. It compares the actual quantum Hamiltonian gap
to its actual ground marginal, with the full complement and the intrinsic
score in the same kinetic metric. It is not a reconstruction theorem.

If only F>=f0 and the constant bound

    A^(1/2) I(U) A^(1/2) <= beta I

are available, take w=f0 and eta=beta/(2f0); (10) becomes

    Delta >= (alpha+f0-sqrt((alpha-f0)^2+2 alpha beta))/2,
    beta < 2f0.                                             (11)

The two-by-two optimization is sharp for abstract forms satisfying just the
three scalar bounds; it is not asserted sharp for every diffusion geometry.
At eta=0 it gives min(alpha,f0). Dropping the score without establishing its
vanishing would give this same expression unjustifiably.

## 5. The precise Wilson target exposed by this identity

**Later resolution, 5 September 2026.** The displayed global sublinear
Fisher candidate in this section is retained as the proposal at this stage.
The [exact central SU(2) true-ground identity](G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md)
disproves it for the actual two-square bouquet, on open coarse neighborhoods
at sufficiently large u. Sections 1–4 of this note remain valid. The
successor gives an energy-localized integral/resolvent criterion, retaining
the high-retained-space obligation before any full-gap conclusion.


The actual block complement and true-vacuum source construction supply the
right operator and projection for (5). To obtain a useful uniform estimate,
one must prove (6) for the *true joint quantum ground state*, including its
horizontal connection, in the same metric and after true vacuum subtraction.
Earlier bounds for the intrinsic conditional fiber ground or the classical
Wilson Gibbs conditional measure are distinct inputs and do not supply it.

A potentially useful sufficient pair, stated conditionally, is

    F >= c0 sqrt(u) + c1 u v(U) on Q,
    A^(1/2) I(U) A^(1/2) <= C0 + C1 sqrt(u) v(U),

with positive constants uniform in the desired block geometry. Their ratio
is bounded by

    2 eta <= max(C0/c0, C1/c1)/sqrt(u).

This follows by comparing numerator and denominator term by term. It would
make the Schur loss O(u^-1/2)=O(g^2), while retaining a global coarse barrier.
Neither displayed Wilson estimate is inferred merely from this algebra.
The actual all-group conditional score, interacting interfaces, uniform
constants and the coarse marginal's scale trajectory must still be proved.

The established global vertical barrier, actual full-block fast floor,
ground-bundle geometry and exact literal-vacuum marginal now identify separate
pieces of this criterion. The unresolved step is specific: control the true
ground marginal's intrinsic score against the *vacuum-subtracted full Q form*.
This formulation avoids the false uniform raw conditional-gap premise at
central coarse holonomies and makes the needed cancellation measurable.

## Provenance and claim boundaries

Inputs: the actual seven-link metric in
G19_WILSON_BLOCK_SCORE_AND_FIBER_OBSTRUCTION_20260905.md; the closed-form Schur
construction in G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md; the actual nonlinear
block complement in G19_WILSON_ACTUAL_BLOCK_FAST_COMPLEMENT_20260905.md; and
the separately derived literal true-vacuum projection. Equations (1)-(11)
are the analytic derivation here. Section 5 is a precise conditional target.
No literature novelty claim or full Lean formalization is made.

The accepted original derivation, independent audits and finite controls
are preserved in the [sealed evidence run](../../runs/literal_quantum_sources_2026-09-05/README.md).
The run's native checks retain their finite scope; the operator, domain
and limiting statements above are analytic proofs.
