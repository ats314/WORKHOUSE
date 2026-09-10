"""Exact controls for SC17 spatial closure; analytic proof scopes remain explicit."""

from itertools import product

from sympy import (
    I,
    Integer,
    Matrix,
    Rational,
    cos,
    diff,
    expand,
    eye,
    limit,
    pi,
    series,
    simplify,
    sin,
    sqrt,
    symbols,
    zeros,
)

from ._core import _suite

sc17 = _suite("Wilson SC17: endpoint reanchoring and connected spatial decay")
CITE = "WILSON_SC17; G19; G23"


@sc17.check(
    "A plaquette mixed Hessian has unit matrix operator norm", CITE + " Endpoint reanchoring"
)
def _plaquette_operator_norm():
    q0, q1, q2, q3 = symbols("q0:4", real=True)
    v = Matrix([q1, q2, q3])
    cross = Matrix([[0, -q3, q2], [q3, 0, -q1], [-q2, q1, 0]])
    mixed = -q0 * eye(3) + cross
    norm2 = q0**2 + (v.T * v)[0]
    defect = mixed * mixed.T - norm2 * eye(3) + v * v.T
    return defect.applyfunc(expand) == zeros(3), (
        "The actual cyclic quaternion mixed matrix, up to orthogonal rotations, "
        "obeys M M^T=|q|^2 I-qvec qvec^T. For a unit plaquette quaternion its "
        "operator norm is at most one, with no Frobenius dimension factor."
    )


@sc17.check(
    "Opposite endpoint derivatives rotate the entire raw diagonal Hessian",
    CITE + " Endpoint reanchoring",
)
def _endpoint_reanchoring():
    q = symbols("q0:4", real=True)
    a, b, c, d = q
    left = Matrix([[-b, a, -d, c], [-c, d, a, -b], [-d, -c, b, a]])
    right = Matrix([[-b, a, d, -c], [-c, -d, a, b], [-d, c, -b, a]])
    norm2 = sum(z**2 for z in q)
    rotation = right * left.T

    def act(frame, i, f):
        return expand(sum(frame[i, j] * diff(f, q[j]) for j in range(4)))

    function = a * b + c**2 + a * c * d
    raw = Matrix(3, 3, lambda i, j: act(left, i, act(left, j, function)))
    mixed = Matrix(3, 3, lambda i, j: act(right, i, act(left, j, function)))
    commute = all(
        expand(act(left, i, right[j, z]) - act(right, j, left[i, z])) == 0
        for i in range(3)
        for j in range(3)
        for z in range(4)
    )
    return (
        commute
        and (rotation * rotation.T - norm2**2 * eye(3)).applyfunc(expand) == zeros(3)
        and (norm2 * mixed - rotation * raw).applyfunc(expand) == zeros(3),
        "Left-multiplication and right-multiplication fields commute. On |q|=1, "
        "YXf=O XXf with O orthogonal, including the diagonal frame derivatives; "
        "the coefficient is outside the indicated differentiation.",
    )


@sc17.check("Each Wilson link has twelve signed mixed-potential neighbors", CITE + " H1")
def _mixed_neighbor_count():
    valid = True
    for side in (3, 4):
        vertices = list(product(range(side), repeat=3))
        rows = {(v, i): {} for v in vertices for i in range(3)}

        def step(v, i, side=side):
            w = list(v)
            w[i] = (w[i] + 1) % side
            return tuple(w)

        for v in vertices:
            for i in range(3):
                for j in range(i + 1, 3):
                    face = [(v, i), (step(v, i), j), (step(v, j), i), (v, j)]
                    signs = (1, 1, -1, -1)
                    for ei, e in enumerate(face):
                        for fi, f in enumerate(face):
                            if e != f:
                                rows[e][f] = rows[e].get(f, 0) + signs[ei] * signs[fi]
        valid &= all(len(row) == 12 and set(map(abs, row.values())) == {1} for row in rows.values())
    return valid, (
        "At the identity the original plaquette words give twelve distinct off-diagonal "
        "blocks +/-k I per link, on side-three and side-four periodic cubes. Their "
        "weighted source row is exactly 12lambda q."
    )


@sc17.check("The SC17 weighted row has a strict rational invariant barrier", CITE + " H1-H2")
def _weighted_barrier():
    lam, q, row = Rational(1, 640), Rational(17, 16), Rational(1, 64)
    diagonal = 3 * lam + 27 * lam**2
    source = 12 * lam * q
    slack = (Rational(4, 3) - Rational(4, 200)) * row - 2 * row**2 - source
    broad_lam, broad_q, broad_row = Rational(1, 73), Rational(1025, 1024), Rational(2, 7)
    broad_diagonal = 3 * broad_lam + 27 * broad_lam**2
    broad_slack = (
        (Rational(4, 3) - 4 * broad_diagonal) * broad_row
        - 2 * broad_row**2
        - 12 * broad_lam * broad_q
    )
    return (
        diagonal == Rational(1947, 409600) < Rational(1, 200)
        and source == Rational(51, 2560)
        and slack == Rational(17, 153600) > 0
        and broad_diagonal == Rational(246, 5329)
        and broad_slack == Rational(77375, 200540928) > 0,
        "At lambda=1/73, q=1025/1024 and Sbar=2/7, the connected Volterra "
        "majorant has slack 77375/200540928. The sharper lambda=1/640, "
        "q=17/16, Sbar=1/64 budget has slack 17/153600. Charged Markov "
        "Duhamel estimate supply the analytic first-crossing argument.",
    )


@sc17.check(
    "True curvature and conditional scores give the sharpened SC17 gap budget",
    CITE + " Curvature and single-link angles",
)
def _curvature_angle_gap():
    rho = 2 * (1 - Rational(1, 200) - Rational(1, 64))
    kappa = 2 * Rational(1, 64) / rho
    cat = 1 / (1 - kappa)
    gap_floor = 3 * (1 - kappa) * (1 - Rational(33, 1120))
    broad_rho = 2 * (1 - Rational(246, 5329) - Rational(2, 7))
    broad_kappa = 2 * Rational(2, 7) / broad_rho
    return (
        rho == Rational(1567, 800)
        and kappa == Rational(25, 1567)
        and cat == Rational(1567, 1542) < Rational(51, 50)
        and gap_floor - Rational(57, 20) == Rational(13299, 877520) > 0
        and broad_rho == Rational(49846, 37303)
        and broad_rho - Rational(4, 3) == Rational(326, 111909) > 0
        and broad_kappa == Rational(10658, 24923)
        and 1 / (1 - broad_kappa) == Rational(24923, 14265) < Rational(7, 4),
        "At lambda<=1/73: rho=49846/37303>4/3, angle row<=10658/24923, "
        "C_AT<=24923/14265<7/4. At lambda<=1/640: rho=1567/800, "
        "link-angle row<=25/1567, C_AT<=1567/1542<51/50. "
        "Using pi<22/7 and exp(-x)>1-x gives gap>57epsilon/20. The true "
        "conditional curvature/score-to-angle proofs are analytical, not formalized here.",
    )


@sc17.check(
    "The bare SC17 norm bootstrap has an exact large-coupling obstruction", CITE + " Exact wall"
)
def _majorant_wall():
    s = symbols("s", real=True)
    variable_lam = symbols("lambda", real=True)
    lam = Rational(1, 64)
    mu = Rational(4, 3) - 4 * (3 * lam + 27 * lam**2)
    discr = mu**2 - 96 * lam
    square = expand(
        Rational(4, 3) * s - 2 * s**2 - (Rational(2, 9) - 2 * (s - Rational(1, 3)) ** 2)
    )
    general_mu = Rational(4, 3) - 12 * variable_lam - 108 * variable_lam**2
    threshold_polynomial = (
        6561 * variable_lam**4
        + 1458 * variable_lam**3
        - 81 * variable_lam**2
        - 72 * variable_lam
        + 1
    )
    sharper_wall = (Rational(4, 3) - 4 * Rational(3, 64)) ** 2 - Rational(96, 72)
    return (
        square == 0
        and mu == Rational(3439, 3072)
        and discr == -Rational(2329055, 9437184)
        and sharper_wall == -Rational(47, 2304)
        and expand(9 * (general_mu**2 - 96 * variable_lam) - 16 * threshold_polynomial) == 0
    ), (
        "At lambda=1/72 the scalar discriminant is -47/2304 even at q=1. "
        "The first threshold solves 6561lambda^4+1458lambda^3-81lambda^2-72lambda+1=0. "
        "The older lambda=1/64 obstruction is also retained exactly. "
        "Even a zero diagonal loss permits source at most 2/9, requiring lambda<1/(54q). "
        "This falsifies extension of this norm bootstrap, not the actual Wilson gap."
    )


@sc17.check(
    "The actual two-alias fast conditional precision retains its cubic cusp",
    CITE + " Gaussian reference",
)
def _actual_fast_cusp():
    t = symbols("t", real=True)
    c, s = cos(t / 4), sin(t / 4)
    w, v = Matrix([c, I * s]), Matrix([I * s, c])
    precision = (v.conjugate().T * Matrix.diag(2 * s, 2 * c) * v)[0]
    actual = series(precision, t, 0, 5).removeO().expand()
    inverse = series(1 / precision, t, 0, 5).removeO().expand()
    return (
        simplify((w.conjugate().T * v)[0]) == 0
        and simplify((v.conjugate().T * v)[0]) == 1
        and actual == 2 - Rational(3, 16) * t**2 + Rational(1, 32) * t**3 + Rational(7, 1024) * t**4
        and inverse
        == Rational(1, 2)
        + Rational(3, 64) * t**2
        - Rational(1, 128) * t**3
        + Rational(11, 4096) * t**4,
        "The analytic fast vector for the actual ell=2 path-source aliases gives "
        "2(cos(t/4)^3+|sin(t/4)|^3). One-sided cubic coefficients 1/32 and -1/128 "
        "in its inverse certify third-derivative jumps 3/8 and -3/32.",
    )


@sc17.check(
    "A scalar Gaussian square-root precision has the exact critical angle row",
    CITE + " Gaussian reference",
)
def _gaussian_angle_row():
    m, r = symbols("m r", positive=True)
    p = Matrix.ones(3) / 3
    precision = m * p + r * (eye(3) - p)
    a = precision[0, 0]
    off = -precision[0, 1]
    conditional_covariance = precision[:2, :2].inv()
    signed_correlation = simplify(conditional_covariance[0, 1] / conditional_covariance[0, 0])
    return (
        simplify(signed_correlation - off / a) == 0
        and simplify(2 * off / a - (1 - m / a)) == 0
        and (precision * precision - m**2 * p - r**2 * (eye(3) - p)).applyfunc(simplify)
        == zeros(3),
        "For r>m>0 this positive square-root precision has c_ij=(r-m)/(m+2r), "
        "and its row is 1-m/M_ii, approaching one as m vanishes. It is a scalar "
        "Gaussian reference check, not an identification with compact Wilson conditionals.",
    )


@sc17.check(
    "The massless square-root reference has angle row exactly one in the limit",
    CITE + " Gaussian reference",
)
def _massless_reference_row():
    """The lattice form of the three-site instance: the row is 1-m/M(e,e) exactly."""
    m = symbols("m", positive=True)
    side = 3
    sites = [(a, b) for a in range(side) for b in range(side)]

    # -Delta on the 3x3 periodic lattice has symbol sum_i 4 sin^2(pi k_i/3), i.e. 3 per
    # nonzero component, so every eigenvalue of L+m^2 is m^2, 3+m^2 or 6+m^2 exactly.
    def eigenvalue(k):
        return sum(Integer(0) if component == 0 else Integer(3) for component in k)

    row = {}
    for x in sites:
        row[x] = simplify(
            sum(
                sqrt(eigenvalue(k) + m**2) * cos(2 * pi * sum(k[i] * x[i] for i in range(2)) / side)
                for k in sites
            )
            / side**2
        )
    diagonal = row[(0, 0)]
    off = [row[x] for x in sites if x != (0, 0)]
    kappa = simplify(sum(-value for value in off) / diagonal)
    return (
        simplify(diagonal + sum(off) - m) == 0
        and all(value.subs(m, Rational(1, 10)) < 0 for value in off)
        and simplify(kappa - (1 - m / diagonal)) == 0
        and simplify(limit(kappa, m, 0)) == 1,
        "(L+m^2)1=m^2 1 gives sqrt(L+m^2)1=m 1, so the row sums are m; the off-diagonal "
        "entries are negative, hence sum|M(e,f)|=M(e,e)-m and the conditional maximal "
        "correlation row is exactly 1-m/M(e,e), which tends to one as m vanishes. Here "
        "M(e,e)=(m+4sqrt(m^2+3)+4sqrt(m^2+6))/9 and kappa=0.5404178 at m=1. This is the "
        "uniform lattice form of the three-site scalar instance; it is a statement about "
        "a Gaussian reference, not about compact Wilson conditionals.",
    )
