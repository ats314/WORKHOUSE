"""Exact algebra behind Simon's confinement mechanism at finite dimension.

Source: SIMON_1983_DISCRETE, sections 2 and 7, pp. 211-212, 216-217.
Derivation: docs/derivations/yangmills-simon-flat-directions.md.

These T1 checks verify factorization, normalization, derivative and allocation
identities. Integration by parts, form closure, compactness and spectral
theorems are stated separately in the derivation; they are not formalized by
these polynomial checks. No check establishes the G22 force conjecture or G23.
"""

from __future__ import annotations

from sympy import Matrix, Rational, diff, exp, expand, eye, simplify, sqrt, symbols, zeros

from ._core import _suite

ym_flat_directions = _suite("Yang-Mills flat directions: exact finite-dimensional algebra")

_SOURCE = "YM_FLAT_DIRECTIONS; SIMON_1983_DISCRETE sections 2, 7; G22, G23"
_OSC = "YM flat directions: oscillator square completion fixes the zero-point constant"
_SCALAR = "YM flat directions: Simon's scalar split retains half the Laplacian"
_SLICE = "YM flat directions: SU(2) slice has two transverse modes"
_JACOBIAN = "YM flat directions: commutator Jacobian is coercive while the force vanishes"
_VALLEY = "YM flat directions: commuting-valley Hessian is a Gram projector"
_ASSEMBLY = "YM flat directions: balanced slice aggregation retains half the kinetic energy"
_HARDY = "YM flat directions: three-dimensional Hardy completion has coefficient 1/4"
_RADIAL = "YM flat directions: radial lower-bound minimum has cube 27/32"
_SCALING = "YM flat directions: quartic coupling dilation scales energies as g^(2/3)"


def _pair_data():
    x = Matrix(symbols("x0:3", real=True))
    y = Matrix(symbols("y0:3", real=True))
    cross = x.cross(y)
    return x, y, cross, expand(cross.dot(cross))


@ym_flat_directions.check(_OSC, _SOURCE)
def oscillator_factorization():
    # A=sqrt(kinetic coefficient), B=sqrt(quadratic-potential coefficient).
    # For compactly supported real u, the total derivative integrates to zero.
    a, b = symbols("A B", positive=True)
    q, u, du = symbols("q u du", real=True)
    completed = (a * du + b * q * u) ** 2 - a * b * (u**2 + 2 * q * u * du)
    original = a**2 * du**2 + b**2 * q**2 * u**2 - a * b * u**2
    gaussian = exp(-b * q**2 / (2 * a))
    eigen_residual = simplify(
        -(a**2) * diff(gaussian, q, 2) + b**2 * q**2 * gaussian - a * b * gaussian
    )
    return (
        expand(completed - original) == 0 and eigen_residual == 0,
        (
            "A^2|u'|^2+B^2 q^2|u|^2-AB|u|^2 = "
            "|Au'+Bqu|^2-AB(q|u|^2)' exactly; Gaussian exp(-Bq^2/(2A)) "
            "has eigenvalue AB. With A=1, B=|omega| the slice bottom is |omega|. "
            "Integration and the operator domain are analytic inputs, not checked here."
        ),
        {"YM_OSCILLATOR_ZERO_POINT_FACTOR": 1},
    )


@ym_flat_directions.check(_SCALAR, _SOURCE, rests_on=(_OSC,))
def scalar_split():
    tx, ty, potential, xabs, yabs = symbols("T_x T_y V abs_x abs_y", nonnegative=True)
    h = tx + ty + potential
    split = (tx + potential) / 2 + (ty + potential) / 2 + (tx + ty) / 2
    residual = (h - (tx + ty + xabs + yabs) / 2) - (
        (tx + potential - yabs) / 2 + (ty + potential - xabs) / 2
    )
    return (
        expand(h - split) == 0 and expand(residual) == 0,
        (
            "For H=-Delta+x^2 y^2, H-(T+|x|+|y|)/2 is exactly one half "
            "the sum of the two nonnegative oscillator slice remainders. "
            "This reconstructs Simon equation (5), p.212, with kinetic coefficient 1/2."
        ),
        {"YM_SIMON_RETAINED_KINETIC": Rational(1, 2)},
    )


@ym_flat_directions.check(_SLICE, _SOURCE, rests_on=(_OSC,))
def transverse_slice():
    x, y, _, potential = _pair_data()
    r2 = x.dot(x)
    transverse = r2 * eye(3) - x * x.T
    lam = symbols("lambda", real=True)
    characteristic = expand((lam * eye(3) - transverse).det() - lam * (lam - r2) ** 2)
    residual = simplify(transverse * transverse - r2 * transverse)
    return (
        (
            expand(potential - (y.T * transverse * y)[0]) == 0
            and characteristic == 0
            and residual == zeros(3)
            and simplify(transverse.trace() - 2 * r2) == 0
        ),
        (
            "|x cross y|^2 = y^T(|x|^2 I-xx^T)y, and M^2=|x|^2 M; "
            "det(lambda I-M)=lambda(lambda-|x|^2)^2. The two transverse "
            "oscillators contribute 2 sqrt(c)|x| for -Delta_y+c|x cross y|^2. "
            "The longitudinal free mode contributes spectral infimum zero."
        ),
        {"YM_SU2_TRANSVERSE_MULTIPLICITY": 2},
    )


@ym_flat_directions.check(_JACOBIAN, _SOURCE)
def jacobian_and_force():
    x, y, cross, potential = _pair_data()
    coordinates = [*x, *y]
    jacobian = cross.jacobian(coordinates)
    jacobian_norm = expand(sum(entry**2 for entry in jacobian))
    residual = expand(jacobian_norm - 2 * (x.dot(x) + y.dot(y)))
    a, b = symbols("a b", real=True)
    valley = dict(zip(coordinates, [0, 0, a, 0, 0, b], strict=True))
    zero_force = all(diff(potential, z).subs(valley) == 0 for z in coordinates)
    n, total_r2 = symbols("n total_r2", positive=True)
    pair_counted_jacobian = 2 * n * total_r2  # each matrix occurs in n=m-1 pairs
    return (
        (
            residual == 0
            and potential.subs(valley) == 0
            and zero_force
            and simplify(jacobian_norm.subs(valley) - 2 * (a**2 + b**2)) == 0
            and pair_counted_jacobian.is_positive
        ),
        (
            "For one SU(2) pair, ||D(x cross y)||_F^2=2(|x|^2+|y|^2). "
            "Summing pairs gives 2(m-1) sum_i |A_i|^2. Yet at x=a e3, y=b e3, "
            "V=0 and grad V=0. Simon's derivative condition concerns DQ, "
            "not grad(sum Q^2); it cannot establish the G22 force lower bound."
        ),
        {"YM_SU2_PAIR_JACOBIAN_FACTOR": 2},
    )


@ym_flat_directions.check(_VALLEY, _SOURCE, rests_on=(_JACOBIAN, _SLICE))
def commuting_valley_hessian():
    # Three matrices are the physical zero-momentum spatial example. The
    # arbitrary-m identity follows by the pair-sum expansion in the document.
    a = Matrix(symbols("a0:3", real=True))
    u = Matrix(symbols("u0:3", real=True))
    v = Matrix(symbols("v0:3", real=True))
    r2 = a.dot(a)
    projector = r2 * eye(3) - a * a.T
    pair_sum = sum(
        (a[i] * u[j] - a[j] * u[i]) ** 2 + (a[i] * v[j] - a[j] * v[i]) ** 2
        for i in range(3)
        for j in range(i + 1, 3)
    )
    gram = r2 * (u.dot(u) + v.dot(v)) - a.dot(u) ** 2 - a.dot(v) ** 2
    hessian = Matrix([[diff(pair_sum, z, w) for w in [*u, *v]] for z in [*u, *v]])
    expected = Matrix.diag(2 * projector, 2 * projector)
    lam = symbols("lambda", real=True)
    return (
        (
            expand(pair_sum - gram) == 0
            and simplify(hessian - expected) == zeros(6)
            and simplify(projector * a) == zeros(3, 1)
            and simplify(projector * projector - r2 * projector) == zeros(3)
            and expand((lam * eye(3) - projector).det() - lam * (lam - r2) ** 2) == 0
        ),
        (
            "For three commuting backgrounds A_i=a_i e3, the quadratic transverse "
            "potential is R^2(||u||^2+||v||^2)-(a.u)^2-(a.v)^2. Its Hessian is "
            "2 diag(R^2 I-aa^T,R^2 I-aa^T): four eigenvalues 2R^2 and two "
            "collective-rotation zero modes when R>0. General m has 2(m-1) "
            "normal modes, derived by the same pair identity in the note."
        ),
        {"YM_SU2_THREE_MATRIX_NORMAL_MODES": 4},
    )


@ym_flat_directions.check(_ASSEMBLY, _SOURCE, rests_on=(_SLICE,))
def balanced_slice_aggregation():
    n, g = symbols("n g", positive=True)  # n=m-1
    kinetic, potential, radius_sum = symbols("T V R", nonnegative=True)
    sum_slices = n * kinetic + 2 * n * potential
    slice_floor = 2 * g * n * sqrt(n) * radius_sum
    comparison = kinetic / 2 + g * sqrt(n) * radius_sum
    residual = simplify(kinetic + potential - comparison - (sum_slices - slice_floor) / (2 * n))
    return (
        residual == 0,
        (
            "K_i=sum_(j!=i)[-Delta_j+(m-1)g^2|A_i cross A_j|^2]. "
            "Each kinetic term occurs m-1 times and each potential pair twice: "
            "sum K_i=(m-1)(T+2V). The slice floors sum to "
            "2g(m-1)^(3/2) sum|A_i|. Hence H>=T/2+g sqrt(m-1) sum|A_i| "
            "on the common form core, provided the oscillator slice inequalities hold."
        ),
        {"YM_MATRIX_RETAINED_KINETIC": Rational(1, 2)},
    )


@ym_flat_directions.check(_HARDY, _SOURCE)
def hardy_completion():
    x = Matrix(symbols("x0:3", real=True))
    r2 = x.dot(x)
    field = x / (2 * r2)
    divergence = sum(diff(field[j], x[j]) for j in range(3))
    field_norm = field.dot(field)
    return (
        (
            simplify(divergence - 1 / (2 * r2)) == 0
            and simplify(field_norm - 1 / (4 * r2)) == 0
            and simplify(field_norm - divergence + 1 / (4 * r2)) == 0
        ),
        (
            "For b(x)=x/(2|x|^2), div b=1/(2|x|^2) and |b|^2=1/(4|x|^2). "
            "Integration by parts gives ||grad u+bu||^2=||grad u||^2 "
            "-(1/4)||u/|x|||^2 on the punctured smooth core. The checked "
            "rational identities fix the Hardy coefficient; density is analytic."
        ),
        {"YM_HARDY_R3_COEFFICIENT": Rational(1, 4)},
    )


@ym_flat_directions.check(_RADIAL, _SOURCE, rests_on=(_HARDY, _ASSEMBLY))
def radial_minimum():
    z, s = symbols("z s", positive=True)
    # Put r=s*z and k=1/(4*s^3), so s=(4k)^(-1/3).
    k = 1 / (4 * s**3)
    radial = 1 / (8 * (s * z) ** 2) + k * s * z
    minimum = 3 / (8 * s**2)
    remainder = (z - 1) ** 2 * (2 * z + 1) / (8 * s**2 * z**2)
    return (
        (
            simplify(radial - minimum - remainder) == 0
            and simplify(minimum**3 / k**2 - Rational(27, 32)) == 0
            and simplify(radial.subs(z, 1) - minimum) == 0
        ),
        (
            "1/(8r^2)+kr has minimum 3(k^2/32)^(1/3); after r=s*z, "
            "k=1/(4s^3), its remainder is (z-1)^2(2z+1)/(8s^2z^2)>=0. "
            "Thus the analytic form argument yields E0(H_m(g)) >= "
            "3m[g^2(m-1)/32]^(1/3). This is ground energy before vacuum "
            "subtraction; no lower bound on E1-E0 is claimed by this check."
        ),
        {"YM_RADIAL_MINIMUM_CUBED_FACTOR": Rational(27, 32)},
    )


@ym_flat_directions.check(_SCALING, _SOURCE)
def quartic_coupling_scaling():
    x, y, _, potential = _pair_data()
    scale = symbols("s", positive=True)
    dilation = {z: z / scale for z in [*x, *y]}
    # g=s^3 gives g^2 V(A/s)=s^2 V(A), matching the kinetic scaling.
    scaled_potential = expand(scale**6 * potential.subs(dilation, simultaneous=True))
    return (
        expand(scaled_potential - scale**2 * potential) == 0,
        (
            "V(A/s)=s^-4 V(A); setting g=s^3 makes g^2 V(A/s)=s^2 V(A). "
            "The unitary spatial dilation scales -Delta by s^2 as well, so "
            "H_m(g) is unitarily equivalent to g^(2/3) H_m(1). Both E0 and "
            "any vacuum-subtracted gap have this scaling at fixed m; compactness "
            "at fixed g gives no positive lower bound uniform as g tends to zero."
        ),
        {"YM_QUARTIC_ENERGY_COUPLING_EXPONENT": Rational(2, 3)},
    )
