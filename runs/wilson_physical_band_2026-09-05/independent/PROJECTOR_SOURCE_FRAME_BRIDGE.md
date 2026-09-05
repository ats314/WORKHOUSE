# Close spectral projections and complete projected source frames

5 September 2026. Independent abstract consequence for the actual Wilson
continuation. This note does not establish the Wilson operator limit or its
literal-source synthesis estimate; those are the two application inputs.

## 1. A projection estimate valid in infinite dimension

Let H be a Hilbert space, P0 an orthogonal projection, Q0=I-P0, and

    D = c P0 + D_Q,   D_Q=Q0 D Q0 <= (c-g) Q0,   g>0.

Here D and G are bounded self-adjoint operators and ||G-D||<=epsilon<g/2.
Positivity is useful for the eventual transfer interpretation but is not
needed for this lemma. Work inside the physical odd Hilbert space, so that
no vacuum eigenvalue above the free plaquette shell is present.

The self-adjoint resolvent Neumann bound puts the spectrum of G inside

    (-infinity,c-g+epsilon] union [c-epsilon,c+epsilon].

Let P=1_(c-g/2,infinity)(G), Q=I-P. The same P is the Riesz projection
around c of radius g/2. Then

    delta=||P-P0|| <= epsilon/(g-epsilon) < 1.                 (1)

Proof without a finite-rank assumption: put E=G-D, G_P=G restricted to
Ran P and G_Q=G restricted to Ran Q. For X=Q0 P and Y=Q P0,

    D_Q X - X G_P = -Q0 E P,
    G_Q Y - Y c = Q E P0.

Since sup spectrum(D_Q)<=c-g and inf spectrum(G_P)>=c-epsilon,

    X = integral_0^infinity exp(t(D_Q-(c-g)))
                 Q0 E P exp(-t(G_P-(c-g))) dt.

The integral converges in operator norm and has norm at most
epsilon/(g-epsilon). It solves the Sylvester equation; uniqueness follows
by applying the same exponentially decaying conjugation to a homogeneous
solution. Similarly

    Y = -integral_0^infinity exp(t(G_Q-c)) Q E P0 dt

has that bound. Finally ||P-P0||=max(||Q0P||,||QP0||), proving (1).
This also establishes the needed bound on both defect spaces; no dimension
comparison is hidden in the argument.

The simpler circular-contour bound is
2epsilon/(g-2epsilon). Equation (1) uses the one-sided free complement and
is stronger. In particular epsilon<=g/10 gives delta<=1/9.

## 2. Direct rotation and the onto unperturbed projected synthesis

For arbitrary orthogonal P,P0 with delta<1, define

    K=P-P0,
    R=P P0+(I-P)(I-P0),
    S=(I-K^2)^(1/2),
    U=R S^(-1).

Exact multiplication gives

    R*R=RR*=I-K^2,
    R P0=P R,
    [S,P]=[S,P0]=0.

Thus U is a unitary, U P0=P U, and it maps Ran P0 onto Ran P. This is a
direct rotation, not merely an isometric embedding. It also obeys

    U+U*=2S,
    ||U-I||=sqrt(2(1-sqrt(1-delta^2))) <= sqrt(2) delta.       (2)

Let E be a coefficient Hilbert space and J0:E->H an isometry onto Ran P0.
Then A0=P J0 has the exact factorization

    A0=U S J0.

Consequently A0 is a bounded bijection E->Ran P, with

    A0^(-1)=J0* S^(-1) U* restricted to Ran P,
    sqrt(1-delta^2)||f|| <= ||A0f|| <= ||f||.                 (3)

This proves surjectivity in infinite dimension. The lower bound alone
would not prove it.

## 3. Perturbed sources: completeness by a Neumann inverse

Suppose the actual source synthesis J:E->H is bounded and

    ||J-J0|| <= eta < sqrt(1-delta^2).                       (4)

The norm in (4) is the norm of the entire synthesis operator, not a bound
on each source column separately. Set A=PJ. On the coefficient space,

    A = A0 (I+B),
    B=A0^(-1) P(J-J0),
    ||B|| <= eta/sqrt(1-delta^2) < 1.

The convergent operator-norm Neumann series for (I+B)^(-1) proves A is a
bounded bijection onto the complete spectral range Ran P. In particular

    (sqrt(1-delta^2)-eta)^2 I <= J*P J <= (1+eta)^2 I,        (5)
    ||A^(-1)|| <= 1/(sqrt(1-delta^2)-eta).

Its polar normalization W=A(A*A)^(-1/2) is a unitary E->Ran P. If P,J0,J
intertwine translations, so do the inverse, Gram normalization and W.
With E=ell^2(Z^3) tensor C^3 this identifies the complete band as a
three-component translation representation. Exponential decay of the
orthonormalized band kernel needs a weighted kernel estimate in addition
to the plain operator-norm statement here.

Convenient exact sufficient constants are

    epsilon<=g/10,   delta<=1/9,   eta<=1/8.

Since sqrt(1-delta^2)>=1-delta^2>=80/81,

    ||Af|| >= (559/648)||f|| > (3/4)||f||,
    A*A >= (559/648)^2 I > (9/16) I,
    ||A^(-1)|| <= 648/559 < 6/5.                            (6)

No finite-volume rank argument, source-by-source extrapolation, or
infinite-dimensional compactness is needed in (1)-(6).

## 4. Counterexamples defining the precise premises

1. The unilateral shift L on ell^2(N), L e_n=e_(n+1), obeys L*L=I and
   LL*=I-|e0><e0|. A perfect Gram lower bound does not imply totality.
   Taking P=P0=I and J=L meets the Gram assertion but not the small
   synthesis-perturbation hypothesis. In fact ||L-I||=2.

2. On C^N, let v=(1,...,1)/sqrt(N) and J=I-|v><v|. Every column of
   J-I has norm 1/sqrt(N), yet ||J-I||=1 and Jv=0. Thus arbitrarily small
   uniform column errors do not produce a small synthesis operator.
   A Schur/overlap or Gram-kernel estimate must handle the entire family.

3. Let U_N cyclically permute e0,...,eN by U_N e_k=e_(k+1) for k<N and
   U_N eN=e0, and fix all later basis vectors. Each U_N is unitary, but
   U_N converges strongly to the unilateral shift. Completeness can be
   lost in a strong limit of individually onto maps. Their adjoints do
   not converge strongly on e0. A common norm-near reference or controlled
   inverse avoids this failure.

The exact controls in `check_projector_source_frame.py` verify rational
rotated finite bands, direct rotation, Gram certificates, and finite
witnesses of these examples. The infinite-dimensional statements above
are operator arguments, not consequences of finite matrix sampling.

## 5. Provenance audit of the existing G18 source results

`paper/research_notes/G18_FIXED_SPACING_CARRIER_BRIDGE_INSERT.tex`, theorem
`g18-fixed-spacing-band`, already establishes its fixed-spacing Hamiltonian
band and literal Wilson-source frame. Its proof first imports coefficient
to GNS totality from `G18_CMP1_CLOSE_PROJECTION_GNS_TRANSPORT_20260830.tex`.
It then combines totality with the canonical Gram lower bound to obtain
an onto map T_c. The literal-source step correctly uses that onto property:

    T_D=T_c(T_c*T_c)^(-1)T_c*T_D=T_c E,
    T_W=T_c(I+E).

There is no false lower-bound-implies-onto step in that proof. Its stated
normalization c_W=i sqrt(2), source difference norm 3sqrt(2)+1 and physical
coefficients belong to its source/rank convention. They must be reconciled
with the rank and source normalization of any new all-rank application.
The closing remark explicitly excludes identification of its Hamiltonian
semigroup with the isotropic Wilson-action transfer matrix.

`G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md`, Theorem 2, proves an actual
Wilson finite-volume literal-source basis. It explicitly has a volume
dependent coupling domain, estimates synthesis error by a sqrt(P) column
bound, and uses equality of finite ranks P to obtain onto. That is correct
there, but neither the domain nor the dimension argument can be reused
for the thermodynamic synthesis theorem.

The new weighted-activity theorem supplies a volume-uniform actual Wilson
operator bound. To apply this bridge, the remaining arguments must place
its limit and the actual transported literal sources on one specified
physical Hilbert space, establish the free complement bound there, and
prove (4) uniformly for the complete synthesis operator. Once those
inputs hold, (1)-(6) complete the Riesz-range and source-frame step.
