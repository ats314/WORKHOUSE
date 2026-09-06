# Independent review of the first Wilson ground and source correction

6 September 2026. Outputs-only independent review of
`CUBIC_GROUND_TRANSFER.md`. The fixed-complex finite-cell proof is an
established input. No canonical source or sealed evidence was changed.

## Accepted mathematical statement

The strengthened first-order statement is valid under the draft's finite
connected complex, unique flat orbit, positive Hessian, fixed compact simple
group, representation and metric hypotheses. It identifies the entire
ground forcing, rather than merely its diagonal expectation. It supplies
no growing-volume remainder estimate.

The critical point is the actual first jet, not invariance alone. In a
tree quotient every original-link vector field comes from differentiating
products, inverses and conjugations. Its constant jet is color diagonal;
dexp, Ad and BCH give one Lie bracket in its linear jet. Real whitening
changes only spatial indices. Squaring the vector fields gives linear
second-order coefficients with one structure tensor. Differentiating those
coefficients identifies two colors of that tensor, giving zero. Product
Haar density begins at degree two, and its flattening supplies no first-order
term. This explicitly excludes a symmetric cubic color tensor even in a
group that admits such an invariant.

The face-word calculation also uses its actual ordered, signed occurrences.
The BCH expansion through degree two and
`Re Tr(XYZ)=Tr(X[Y,Z])/2` for anti-Hermitian matrices give the displayed
magnetic cubic. A repeated edge is not silently replaced by an independent
coordinate. Its first correction has precisely the same bracket color
structure as the electric correction.

On the color-diagonal Gaussian, the second derivatives produce a cubic
product of linear Gaussian gradients and a linear contraction. The latter
vanishes by repeated colors in the structure tensor. Commutativity of the
coordinate variables allows spatial antisymmetrization without changing
the remaining cubic. Thus `H1 Phi0=P_D Phi0` with `D in exterior^3 E*`.
This is stronger than projected parity cancellation and is established by
the actual differential operator calculation.

Every Gaussian trace of this cubic vanishes for an arbitrary positive
spatial covariance tensored with the color identity. Ground conjugation
therefore acts only by the three-slot frequency sum. Its eigenvalues are
`omega_i+omega_j+omega_k` with distinct spatial indices, and the stated
inverse is positive and well-defined. This gives the unique orthogonal
first ground corrector. For fewer than three spatial cycle coordinates,
the entire forcing and corrector vanish. It does not imply that H1
annihilates other states or that all higher odd orders vanish.

## Conditional and moving-source correction

For a fixed linear source, its conditional Gaussian covariance remains
color diagonal even when the spatial source does not reduce Omega.
Expanding the cubic about the actual conditional mean kills odd fast
moments and kills every even pair contraction by the color tensor. This
proves `E[P_C|y]=P_C(m(y))` using the actual inverse-frequency marginal,
including coupled aliases. The conditional wavefunction can still have
a nonzero first-order correction with mean zero.

An earlier wording risk was identified and repaired during review: the
first derivative of the law of a *nonlinear* source cannot be obtained
from its linear tangent alone. For `y_g=W*x+gY1(x)+...`, differentiation
against test functions gives the additional transport term
`-div(mu0 E[Y1|y])/mu0`. The current section 4 includes it explicitly.

The chosen local group-retracted chart has a bracket-valued quadratic
Y1. To verify this without assuming a polar chart for every group, expand
the nearest group point as `exp(gA+g²D)`. At order two its minimizing
condition is `D=Proj_Lie(B-A²/2)`. Squares and anticommutators are Hermitian
and orthogonal to the anti-Hermitian Lie tangent; the remaining bracket
terms lie in that tangent. Tree quotient and logarithm operations add
only BCH brackets. Conditional pair contractions again vanish. The
divergence of `Y1(m(y))` repeats an output color in the alternating tensor
and is zero. The remaining transport density is exactly
`2 <G^-1 y,Y1(m(y))>`. Its sign and normalization are correct because
the true marginal density is proportional to `exp(-y*G^-1 y)`.

This establishes the repaired formula for the specified finite local
submersive chart. It does not identify that chart's sigma algebra with
the sigma algebra of the whole matrix-valued average: additional matrix
directions can first appear at quadratic order. The draft retains this
distinction. A small total conditional Fisher bound is not inferred.

## Exact-control scope

The current checker was read independently. Its direct signed SU(2)
matrix-word expansions, including repeated occurrences, do not use the
predicted BCH cubic to manufacture the left-hand side. Non-diagonal
positive spatial Omega checks the determinant drift and its inverse;
non-diagonal spatial Gaussian covariance checks zero color-preserving
contraction. The broken-color, moving-source, frequency-sum and rank
controls test the corresponding finite algebra.

A symmetric polynomial test by itself need not be an invariant Lie
polynomial. It must not be reported as an SU(3) d-tensor test. In
particular actual invariant d is color-traceless; excluding it from the
Wilson first jet requires the argument above. The proposed separate
`Tr(diag(1,1,-2)^3)=-6` comparison correctly illustrates that invariance
alone would allow a symmetric one-spatial-copy cubic, while its
anti-Hermitian real Wilson trace vanishes.

These calculations support finite algebraic steps. Completeness of the
first-jet classification, all-group scope, analytic localized ground
asymptotics and nonlinear chart domains remain explicit analytic proof
steps. The checker correctly does not call their finite examples a
machine proof of those full statements.

## Final snapshot

The final repaired source and complete finite payload were independently
replayed with numerical proposal imports blocked. Three deliberate
corruptions (rank, moving-source coefficient and proof hash), optimized
execution and overwrite were rejected. All original bytes remained
unchanged. Evidence and the reproducible audit helper are
`CUBIC_INDEPENDENT_REPLAY_VALIDATION.json` and
`validate_cubic_independently.py`.

Final SHA256:

- Proof: `2f66774649f6b4d3e07fe273530cd3f37e24f5d2b3349943c2242623bb1c76db`.
- Checker: `48445f73f9cd0e0c2e3b63b76ebf1bcd109848cc02a8e572c2967b232414297f`.
- Frozen report: `f6f2da13e049b38ddeefbe00a39e2de474893bf8d6bbbe902fa1e819a84b1105`.

The complete final mathematical chain is accepted with the stated
finite-complex and chosen-source-chart scope.
