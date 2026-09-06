# The first Wilson vacuum correction is a spatial exterior three-form

6 September 2026. Analytic derivation independently reviewed. This continues the
actual finite-cell Wilson expansion and the local-path Gaussian baseline.
It does not assert convergence of an interacting infinite-volume expansion.

## Inputs and precise target

The existing [G19_WILSON_FINITE_CELL_GAP_AND_BOUNDARY_FORM_20260905.md](G19_WILSON_FINITE_CELL_GAP_AND_BOUNDARY_FORM_20260905.md)
sections 3 and 5 constructs the exact gauge-tree quotient, its Haar measure,
the original-link electric metric, and the fixed-complex expansion

    g^2 H(g^-4) = H0 + g H1 + O(g^2),  g=u^-1/4.

The remainder is on fixed polynomial Gaussian vectors with a local cutoff.
Its prior parity argument proves PH1P=0 on the ground and first physical
cluster, and provides finite Hermite correctors. The proposed strengthening
here identifies the entire ground forcing, its frequency denominators and
its actual Gaussian conditional mean. It does not repeat that parity proof.

Use the same finite connected complex with a unique flat gauge orbit,
H^1=0, positive face weights and fixed compact connected simple group,
bi-invariant metric and faithful unitary representation. Its transverse
cycle space E has dimension r. Let Omega>0 be the oscillator frequency
matrix on E. On E tensor Lie(G),

    Phi0(x) = const exp[-(1/2) sum_a <x^a,Omega x^a>],
    e0 = dim(G) Tr(Omega)/2.

All constants in the analytic remainders retain their fixed-complex scope.

## 1. First jets contain one bracket, not a symmetric cubic color tensor

Choose based non-tree holonomies and their exponential coordinates, then
apply the real linear whitening map from the prior finite-cell proof.
The derivative induced by any original edge is obtained by differentiating
finite products, inverses and conjugations of those holonomies. The
constant coordinate jet is color diagonal. Every term in its first jet
is a real scalar spatial coefficient times one Lie bracket: this follows
from exp differential I+(1/2)ad_y+O(y^2), Ad_exp(y)=I+ad_y+O(y^2),
and BCH(y,z)=y+z+[y,z]/2+O(3). All real spatial linear changes preserve it.

Consequently, after rescaling, every term in the first electric correction
with two derivatives is a linear coordinate times one structure tensor
f_abc=<T_a,[T_b,T_c]>. Differentiating its coefficient can only contract two
indices of f; that contraction is zero. Product Haar density and its square
root start at even order two in these exponential coordinates, so flattening
Haar introduces no term of order g. There is no constant invariant vector
to supply another first-derivative term.

For a face with signed logarithms z_1,...,z_p in its actual ordered word,

    F1 = sum_j z_j,
    F2 = (1/2) sum_{j<k} [z_j,z_k],
    v_rho(product_j exp(g z_j))
      = (b_rho/2) g^2 |F1|^2 + b_rho g^3 <F1,F2> + O(g^4).

This uses the vanishing odd term for a single exponential character;
it keeps the BCH term. Repeated edges retain their signed occurrences.
Equivalently for anti-Hermitian matrices,
Re Tr(XYZ)=Tr(X[Y,Z])/2. Thus the first magnetic correction also has exactly
one alternating structure tensor. A symmetric invariant tensor available
for some groups cannot be inferred here from invariance alone; the actual
first jets exclude it.

Acting on Phi0, the two derivatives give
(Omega x)_j^b (Omega x)_k^c - Omega_jk delta_bc.
The delta term contracts f to zero. Hence there is a real alternating
spatial trilinear coefficient D in exterior^3 E* such that

    H1 Phi0 = P_D(x) Phi0,
    P_D(x) = sum_ijk,abc D_ijk f_abc x_i^a x_j^b x_k^c.       (1)

Our convention includes all ordered triples in this displayed sum.
Antisymmetrizing an arbitrary spatial coefficient does not change P_D,
because the coordinate variables commute and f is alternating. This
justifies exterior^3 E*, not merely a statement about odd degree.

## 2. Full first ground corrector and the rank-two cancellation

Color-diagonal Gaussian contraction kills every trace of P_D. In particular
Delta P_D=0, and P_D is pure Gaussian Wick degree three for every positive
spatial covariance tensored with the color identity. Ground conjugation gives

    Phi0^-1 (H0-e0) (P Phi0) = -(1/2)Delta P +(Omega x).grad P.

On these cubics the first term vanishes. The second applies Omega in each
of the three spatial slots. On exterior^3 E*, set

    L3 = Omega^(1)+Omega^(2)+Omega^(3).

Its spectrum consists of omega_i+omega_j+omega_k for distinct i,j,k,
and every eigenvalue is at least 3 omega_min. The unique orthogonal ground
corrector from the existing finite-cell theorem is therefore

    Phi1 = P_C Phi0,   C = -L3^-1 D.                       (2)

For r<3, exterior^3 E*=0 and H1Phi0=Phi1=0 exactly, for all the fixed simple
groups covered by the prior theorem. This supplies a structural reason for
the two-cycle vacuum cancellation; it does not say H1 vanishes on every
state. For r>=3, (1) can be nonzero, and no even-power vacuum expansion is
asserted without computing D. The already available actual ground-state
localization turns (2), with its cutoff, into the first derivative in the
fixed-complex asymptotic ground expansion. No volume-uniform remainder is
being supplied by the finite denominator formula.

## 3. Exact conditional mean: no first-order fast tadpole

Let y=W*x be any color-independent linear source with injective W and true
Gaussian vacuum marginal. Define

    C0=Omega^-1, G=W*C0W,
    m(y)=C0 W G^-1 y,
    Cf=C0-C0 W G^-1 W*C0.

The actual coordinate covariance is C0/2; conditionally it is Cf/2, tensor
the color identity. Write x=m+z. Every term in E[P_C(m+z)|y] containing one
or three z vanishes by Gaussian parity. Every term with two z contracts
two colors of f and also vanishes. Therefore

    E[P_C(x)|y] = P_C(m(y)).                               (3)

This holds for the entire linear tangent source of the actual local-path
map, including all its Fourier aliases and nonzero slow/fast coupling. It
does not assume those coordinates reduce Omega. Likewise
E[P_D(x)|y]=P_D(m(y)). The nonlinear observable's moving coordinate needs
the additional term below; it cannot be inferred from its tangent alone.

At the formal first derivative of a normalized quantum ground density,
Phi_g=Phi0(1+g P_C+O(g^2)), equations (2)-(3) give

    d(mu_g/mu0)/dg at 0 = 2 P_C(m(y)),
    d(phi_cond,g/phi_cond,0)/dg at 0
      = P_C(x)-P_C(m(y)).                                 (4)

Equation (4) concerns the fixed linear source. It is a coefficient identity.
Upgrading it to a uniform derivative
bound on true interacting marginals requires a remainder estimate, and on
growing lattices requires the summable fast-covariance and nonlinear control
currently being developed. It does not make the full conditional Fisher
small: the nonreducing Gaussian score remains its leading baseline.

## 4. Keep the first nonlinear change of source coordinates

Suppose the chosen coarse chart has the expansion
y_g(x)=W*x+g Y1(x)+O(g^2). Testing its pushforward against a smooth compactly
supported function and differentiating gives

    d(mu_g/mu0)/dg at 0
      = 2 E[P_C|y] - div_y(mu0 E[Y1|y])/mu0.                (5)

This is an additional first-order term, even when the ground derivative
is known. Here mu0 has density proportional to exp[-y*G^-1 y].

For a fixed finite local group chart of the path average, Y1 contains
one Lie bracket. Indeed M=I+g A+g^2 B+O(g^3), and the local nearest-group
projection has logarithm g A+g^2 proj_Lie(B-A^2/2)+O(g^3).
Every path product contributes its half-square, which is Hermitian, plus
one anti-Hermitian bracket; projection against the Lie algebra kills the
Hermitian terms and retains the bracket. A coarse tree quotient, its BCH
logarithms and real spatial changes again preserve this property.
Thus each component has the form

    (Y1)_i^a(x) = sum_jk,bc E_ijk f_abc x_j^b x_k^c.

For the color-independent conditional Gaussian,
E[Y1|y]=Y1(m(y)). Its divergence in y is zero: differentiating either
factor repeats the output color a in f. Consequently (5) becomes

    d(mu_g/mu0)/dg at 0
      = 2 P_C(m(y)) + 2 <G^-1 y,Y1(m(y))>.                 (6)

Both terms are cubic. This incorporates the first moving-source correction
and still has no linear Gaussian contraction. The chosen finite local chart
must be submersive on the transverse variables under consideration. No
volume-uniform quotient-chart radius is asserted. The entire sigma algebra
of the original matrix-valued observation may contain additional directions
visible first at order g^2; it is not identified with this chosen chart or
with its tangent sigma algebra. Global nonlinear source identification
therefore remains a separate obligation.

## Consequence and next calculation

The first nonlinear source-law calculation can keep its exact quadratic
memory and push forward the ground Lie cubic together with the specified
chart's bracket correction. Fast pair contractions do
not generate a linear source counterterm at this order. The first
contributions from fast pair contractions occur at order g^2, where two
cubic insertions, the quartic
Wilson term, the electric metric and the Haar/quotient contributions must
be combined. None can be discarded when testing a gauge-forbidden mass
term or deriving a running coupling. This is a concrete input to that
interacting calculation, not an all-orders construction or a mass gap.

## Canonical provenance and reproduction

The [original derivation](../../runs/gaussian_path_nonlinear_input_2026-09-06/CUBIC_GROUND_TRANSFER.md) is preserved
with SHA256 `2f66774649f6b4d3e07fe273530cd3f37e24f5d2b3349943c2242623bb1c76db`. This copy changes only stage metadata and links,
normalizes line endings and appends this separate provenance record.
The [sealed run](../../runs/gaussian_path_nonlinear_input_2026-09-06/README.md) contains the original controls
and independent reviews; their finite algebraic scope does not certify the
full analytic theorem by itself.

- [check_cubic_ground_transfer.py](../../runs/gaussian_path_nonlinear_input_2026-09-06/check_cubic_ground_transfer.py)
- [cubic_ground_controls_frozen.json](../../runs/gaussian_path_nonlinear_input_2026-09-06/cubic_ground_controls_frozen.json)
- [INDEPENDENT_CUBIC_GROUND_REVIEW.md](../../runs/gaussian_path_nonlinear_input_2026-09-06/INDEPENDENT_CUBIC_GROUND_REVIEW.md)
- [CUBIC_INDEPENDENT_REPLAY_VALIDATION.json](../../runs/gaussian_path_nonlinear_input_2026-09-06/CUBIC_INDEPENDENT_REPLAY_VALIDATION.json)

The [conditional covariance continuation](G19_CONDITIONAL_QUANTUM_PATH_COVARIANCE_20260906.md) now supplies fixed-scale harmonic summability. A connected second-moment/fast-energy continuation remains an unverified research draft; no such result is promoted here.
