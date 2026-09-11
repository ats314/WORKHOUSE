"""G9 sixth-order exact controls, with explicit formal/physical boundaries."""

from __future__ import annotations

import itertools

import sympy as sp

from .. import kernel_orbits as KO
from ..sixth_order import (
    E2,
    E3,
    Q,
    add,
    adjoint,
    as_laurent,
    carrier_word,
    evaluate_words,
    folded_series,
    h4_support,
    mixing_terms,
    mul,
    single_plaquette_series,
)
from ._core import _suite

sixth = _suite("G9 sixth-order folds and combined carrier shapes")
_CITE = "G9_SIXTH_ORDER_COMBINED; G9; G14"


@sixth.check("G9 generates all 18 Hermitian sixth-order folded words", _CITE)
def formal_support():
    series = folded_series()
    h = series["hermitian"]

    def a(m):
        return {tuple("PV" + "DV" * (m - 1) + "P"): sp.Rational(1)}

    def b(m):
        word = next(iter(a(m)))
        return {
            word[:i] + ("D",) + word[i:]: sp.Rational(1)
            for i, letter in enumerate(word)
            if letter == "D"
        }

    def anti(x, y):
        return add((1, mul(x, y)), (1, mul(y, x)))

    c2 = {tuple("PVDDDVP"): sp.Rational(1)}
    compact = add(
        (1, a(6)),
        (-sp.Rational(1, 2), anti(a(4), b(2))),
        (-sp.Rational(1, 2), anti(a(3), b(3))),
        (-sp.Rational(1, 2), anti(a(2), b(4))),
        (sp.Rational(1, 2), anti(mul(a(2), a(2)), c2)),
        (sp.Rational(3, 8), anti(a(2), mul(b(2), b(2)))),
        (sp.Rational(1, 4), mul(mul(b(2), a(2)), b(2))),
    )
    ok = compact == h[6] and all(adjoint(x) == x for x in h)
    ok = ok and len(h[6]) == 18 and all(w.count("V") == 6 for w in h[6])
    ok = ok and h[4] == {
        tuple("PVDVDVDVP"): sp.Rational(1),
        tuple("PVDVPVDDVP"): sp.Rational(-1, 2),
        tuple("PVDDVPVDVP"): sp.Rational(-1, 2),
    }
    return ok, (
        "Bloch recursion plus canonical metric: H2..H6 have 1,1,3,7,18 words; PVP=0 "
        "for shifted V; odd orders retained. Physical Haar amplitudes are not "
        "assigned."
    )


@sixth.check("G9 folded series satisfies exact invariant-subspace and metric equations", _CITE)
def matrix_recursion():
    # Independent matrix residual for a two-dimensional retained space and
    # three electric levels; noncommuting retained coefficients and odd terms.
    p = sp.diag(1, 1, 0, 0, 0)
    h0 = sp.diag(0, 0, 2, 3, 5)
    v = sp.Matrix(
        [[0, 0, 1, 2, -1], [0, 0, 3, -1, 2], [1, 3, 2, 1, -2], [2, -1, 1, -1, 3], [-1, 2, -2, 3, 1]]
    )
    matrices = {
        "P": p,
        "D": sp.diag(0, 0, -sp.Rational(1, 2), -sp.Rational(1, 3), -sp.Rational(1, 5)),
        "V": v,
    }
    series = folded_series()
    y = [evaluate_words(x, matrices) for x in series["wave"]]
    h = [evaluate_words(x, matrices) for x in series["hermitian"]]
    residuals = []
    for n in range(7):
        rhs = sum((y[j] * h[n - j] for j in range(n + 1)), sp.zeros(5))
        residuals.append(h0 * y[n] + (v * y[n - 1] if n else sp.zeros(5)) - rhs)
        gram = sum((y[j].T * y[n - j] for j in range(n + 1)), sp.zeros(5))
        residuals.append(gram - (p if n == 0 else sp.zeros(5)))
    return all(x == sp.zeros(5) for x in residuals), (
        "All coefficients through degree 6 vanish in H(g)Y-YH_eff and Y*Y-P over Q; "
        "finite matrix regression of the formal recurrence, not Wilson dynamics."
    )


@sixth.check("G9 Hodge word reduction agrees with spatial Laurent operators", _CITE)
def spatial_words():
    from .hodge_feshbach import _ops, _psi, _sigma

    ident, _, up, s, r = _ops()
    gens = {"S": s, "U": up, "R": r}
    words = [""] + ["".join(w) for n in range(1, 4) for w in itertools.product("SUR", repeat=n)]
    ok = all(as_laurent(carrier_word(w)) == _sigma(w, gens, ident, _psi()) for w in words)
    return ok, (
        "All 40 words of length 0..3 agree coefficientwise over "
        "Q[z1^+-1,z2^+-1,z3^+-1]; sigma(R)=-2e2, sigma(U)=q^2, RR=q e2+3e3, "
        "RUR=4e2^2. Not a dynamical support enumeration."
    )


@sixth.check("G9 all 25 H4 mixing pairs reduce to RR minus projected RUR", _CITE)
def complete_mixing():
    terms = mixing_terms()
    kappa = sp.Rational(h4_support()["R"]) ** 2 / sp.Rational(5, 612)
    expected = -kappa * (Q**2 * E2 + 3 * Q * E3 - 4 * E2**2)
    ok = len(terms) == 25 and [w for w, c in terms.items() if c] == [("R", "R")]
    ok = ok and sp.expand(sum(terms.values()) - expected) == 0
    # Full 189-record kernel, independent of the 25-pair carrier reduction.
    from .anisotropy_variance import _kernel

    _, records = _kernel()
    mean = KO.bloch(records.items())
    square = KO.bloch(KO.compose(records, records).items())
    residual = KO._add(KO._mul(KO.E1, square), KO._mul(mean, mean), -1)
    ok = ok and as_laurent(-sp.Rational(5, 612) * expected) == residual
    return (
        ok,
        (
            f"q^3 lambda6_mix=-kappa*(q^2 e2+3q e3-4e2^2), kappa={kappa}; all Hodge-only "
            f"and cross terms cancel. H3 preserves the carrier; H5 cannot enter this "
            f"mixing at order six."
        ),
    )


@sixth.check("G9 local direct H6 cannot cancel the induced cubic-denominator shape", _CITE)
def noncancellation():
    # q^3 lambda6=q^2 sigma(H6)-kappa*(q^2 e2+3q e3-4e2^2).
    # Formal quotient plus an independent witness in the Laurent ring:
    # z=(-1,-1,5+2sqrt(6)) gives a=(4,4,-8), q=0, e2=-48.
    kappa = sp.Rational(h4_support()["R"]) ** 2 / sp.Rational(5, 612)
    numerator = sp.expand(sum(mixing_terms().values()))
    z = [-sp.S.One, -sp.S.One, 5 + 2 * sp.sqrt(6)]
    a = [sp.simplify(2 - x - 1 / x) for x in z]
    q = sum(a)
    e2 = a[0] * a[1] + a[0] * a[2] + a[1] * a[2]
    ok = q == 0 and e2 == -48 and kappa > 0
    ok = ok and numerator.subs(Q, 0) == 4 * kappa * E2**2
    ok = ok and sp.rem(numerator, Q**2, Q) == 4 * kappa * E2**2 - 3 * kappa * Q * E3
    return ok, (
        "Modulo q the combined numerator is 4*kappa*e2^2, independently of every "
        "Laurent-polynomial H6. Laurent q=0 witness has e2=-48, so divisibility "
        "fails. This proves noncancellation under local-shell and H3-decoupling "
        "hypotheses, not a physical direct RUR coefficient or a Gamma pole."
    )


@sixth.check("G9 one-face SU3 sixth-order rooted coefficient from exact character dynamics", _CITE)
def one_face():
    odd = single_plaquette_series()["energies"]
    vacuum = single_plaquette_series(odd=False)["energies"]
    value = odd[6] - vacuum[6]
    ok = (
        odd[1:4] == [1, sp.Rational(-1, 4), sp.Rational(-1, 16)]
        and vacuum[2] == sp.Rational(-3, 4)
        and odd[6] == sp.Rational(407, 702464)
        and vacuum[6] == sp.Rational(6051, 102400)
        and value == sp.Rational(-2055143, 35123200)
    )
    return (
        ok,
        (
            f"One plaquette H0=2C2, V=-(chi3+chi3bar): Eodd6={odd[6]}, Evac6={vacuum[6]}, "
            f"rooted difference={value}. Exact generated representation support and all "
            f"normalization folds; spatially on-site only, no global m6 or "
            f"multi-plaquette shape claim."
        ),
        {"G9_ONE_FACE_ROOTED_SIXTH": value},
    )
