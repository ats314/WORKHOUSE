"""Finite exact controls for the analytic background and charged-vacuum estimates.

These checks do not formalize the differential-domain or parabolic arguments.
"""

from itertools import product

from sympy import Matrix, Rational, diff, expand, eye, integrate, kronecker_product, symbols, zeros

from ._core import _suite

background = _suite("Wilson background continuation: magnetic comparison and charged covariance")
CITE = "WILSON_BACKGROUND; G19; G23"


@background.check(
    "Adjoint Casimir and gauge-star residual have exact positive constants", CITE + " SC5-SC9"
)
def _charged_casimir():
    generators = [
        Matrix([[0, 0, 0], [0, 0, -2], [0, 2, 0]]),
        Matrix([[0, 0, 2], [0, 0, 0], [-2, 0, 0]]),
        Matrix([[0, -2, 0], [2, 0, 0], [0, 0, 0]]),
    ]
    casimir = -sum((a * a for a in generators), zeros(3))
    residual = eye(6) - Matrix.ones(6) / 6
    pairs = zeros(6)
    for i in range(6):
        for j in range(i + 1, 6):
            v = zeros(6, 1)
            v[i], v[j] = 1, -1
            pairs += v * v.T / 6
    singlet = Matrix([1, 0, 0, 0, 1, 0, 0, 0, 1])
    return (
        casimir == 8 * eye(3)
        and residual == pairs == residual.T
        and residual * residual == residual
        and all(
            (kronecker_product(a, eye(3)) + kronecker_product(eye(3), a)) * singlet == zeros(9, 1)
            for a in generators
        ),
        "Casimir(adj)=8; I-J/6 is the sum of 15 positive pair squares and an orthogonal "
        "projection. Same-tail adjoint tensor adjoint has an explicit singlet. "
        "The analytic Markov and gauge-covariance arguments are stated separately.",
    )


def _quaternion_fields(q):
    a, b, c, d = q
    return [(-b, a, -d, c), (-c, d, a, -b), (-d, -c, b, a)]


@background.check(
    "SU2 parabolic derivative identities retain the signed product cancellation",
    CITE + " SC1-SC4 SC16",
)
def _parabolic_ward():
    x, y = symbols("x0:4", real=True), symbols("y0:4", real=True)
    tau, epsilon = symbols("tau epsilon", real=True)
    fields = [(x, v) for v in _quaternion_fields(x)] + [(y, v) for v in _quaternion_fields(y)]

    def act(i, f):
        q, v = fields[i]
        return expand(sum(vj * diff(f, qj) for qj, vj in zip(q, v, strict=True)))

    def lap(f):
        return expand(sum(act(i, act(i, f)) for i in range(6)))

    def gamma(f, h):
        return expand(sum(act(i, f) * act(i, h) for i in range(6)))

    u = tau * x[0] * y[0]
    potential = expand(epsilon * (lap(u) + gamma(u, u)) - diff(u, tau))

    def k(f):
        return expand(-epsilon * (lap(f) + 2 * gamma(u, f)))

    px, py = act(0, u), act(4, u)
    h = act(4, px)
    q = expand(h + px * py)
    first = expand(diff(px, tau) + k(px) + act(0, potential))
    second = expand(diff(h, tau) + k(h) + act(4, act(0, potential)) - 2 * epsilon * gamma(px, py))
    raw = expand(
        diff(q, tau)
        + k(q)
        + act(4, act(0, potential))
        + px * act(4, potential)
        + py * act(0, potential)
    )
    return first == second == raw == 0, (
        "Exact left-multiplication quaternion fields on two SU2 factors give both parabolic "
        "Ward identities and Q=H+F tensor F cancellation. This kinematic fixture "
        "is not asserted to be a gauge-invariant Wilson vacuum."
    )


@background.check(
    "Cubic incidence gives the uniform magnetic Hessian constant 64", CITE + " BF4-BF6"
)
def _magnetic_geometry():
    side = 3
    vertices = list(product(range(side), repeat=3))
    links = [(v, i) for v in vertices for i in range(3)]
    counts = dict.fromkeys(links, 0)

    def step(v, i):
        w = list(v)
        w[i] = (w[i] + 1) % side
        return tuple(w)

    valid = True
    for v in vertices:
        for i in range(3):
            for j in range(i + 1, 3):
                face = {(v, i), (step(v, i), j), (step(v, j), i), (v, j)}
                valid &= len(face) == 4
                for link in face:
                    counts[link] += 1
    return valid and set(counts.values()) == {4} and 64 * 33 == 2112, (
        "The side-three periodic cubic control has 81 links, four links per face and "
        "four faces per link; the analytic Frechet bound gives 4*4*4=64 and "
        "theta<=2112 ell^2 delta. Delta<=1/(4224 ell^2) gives theta<=1/2."
    )


@background.check("Signed fast resolvent pairing obeys its relative-form bound", CITE + " BF1-BF3")
def _signed_resolvent():
    a0 = Matrix([[4, 1], [1, 3]]) - eye(2) / 3
    v = Matrix([[Rational(1, 10), Rational(1, 5)], [Rational(1, 5), -Rational(1, 10)]])
    theta = Rational(1, 4)
    r0, rg = a0.inv(), (a0 + v).inv()
    w = Matrix([1, 2])
    pair = (w.T * r0 * v * rg * w)[0]
    rhs = (w.T * (r0 - rg) * w)[0]
    relative = all(m[0, 0] > 0 and m.det() > 0 for m in (theta * a0 - v, theta * a0 + v))
    return relative and pair == rhs and abs(pair) <= theta / (1 - theta) * (w.T * r0 * w)[0], (
        f"Noncommuting signed fast matrices at z=1/3 give pairing={pair}, exactly "
        "the resolvent difference; both relative-order matrices are positive. "
        "No true-Wilson quantum relative constant is inferred from this fixture."
    )


@background.check(
    "A fixed fast inverse does not prevent a vanishing retained Schur energy", CITE + " BC1"
)
def _retained_soft_mode():
    eta = symbols("eta", positive=True)
    h = Matrix([[1 + eta, 1], [1, 1]])
    v = Matrix([1, -1])
    schur = h[0, 0] - h[0, 1] * h[1, 0] / h[1, 1]
    rayleigh = (v.T * h * v)[0] / (v.T * v)[0]
    return schur == eta and rayleigh == eta / 2 and h.det() == eta, (
        "For H=0 direct_sum [[1+eta,1],[1,1]], the exact fast inverse is one "
        "while the retained Schur form is eta and an excited Rayleigh quotient "
        "is eta/2. Fast invertibility alone cannot supply the physical gap."
    )


@background.check(
    "All-coupling charged covariance constants preserve both cancellation terms",
    CITE + " SC10-SC14",
)
def _charged_constants():
    first = Rational(6, 8) * 4
    source = 2 * first * 4
    nearby = Rational(6, 8) * source + first**2
    distant = Rational(3, 8) * source + first**2
    return (first, source, nearby, distant, 2 * distant) == (3, 24, 27, 18, 36), (
        "Force<=4k, charged inverse<=3/(4epsilon), first derivative<=3lambda; "
        "source product<=24epsilon lambda^2. Adding the retained F tensor F "
        "term yields 27lambda^2 nearby and 18lambda^2 for disjoint tail stars. "
        "These constants contain no spatial distance decay."
    )


@background.check(
    "Barycenter connection averaging fails its claimed gauge equivariance", CITE + " BC2"
)
def _connection_average():
    x = symbols("x", real=True)
    h = x**2 * (2 - x) ** 2 * (x - Rational(1, 2)) ** 2 * (x - Rational(3, 2)) ** 2
    average = integrate(diff(h, x), (x, 0, 1))
    return h.subs(x, Rational(1, 2)) == h.subs(x, Rational(3, 2)) == 0 and average == Rational(
        1, 16
    ), (
        "Cartan gauge h has zero values at both cell barycenters but integral_0^1 h'=1/16. "
        "Thus the submitted Q(A) connection average cannot transform by an interpolation "
        "of barycenter gauge values; background averaging of homogeneous fluctuations survives."
    )
