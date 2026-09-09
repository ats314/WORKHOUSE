"""The Feshbach resolvent comparison: what an interacting inverse image costs.

A recurring shape in the uniformity gaps (G17, G22, G23) is a bound on a
bilinear form with one FREE and one INTERACTING inverse image in its slots,

    (A_g - A_0)[A_0^-1 w, A_g^-1 w],

where the Gaussian half is under control and the interacting half is not. The
usual attack -- second resolvent identity, then Neumann iteration -- needs an
absolute operator bound on ``A_0^-1 (A_g - A_0)`` uniform in the volume, and
that is where such arguments stall.

The mixed form is removable. The first check here is an exact identity: the
interacting inverse image cancels out of the pairing entirely, leaving a
difference of two quadratic forms of the SAME vector. The rest of the module
follows that through to an explicit constant, and then records what the
constant costs -- because the reduction is not free, and the price is exactly
the hypothesis the gaps above are about.

Tiers, because the difference is the whole point here: the collapse identity and
the sandwich are T1, decided in exact rationals with no tolerance. The constant,
the void witness and the volume-stability comparison are **T2** -- they rest on
floating eigenvalues and power iteration, because a relative form bound is a
spectral quantity and not a rational one. Do not quote the T2 rows as exact.

Nothing here is specific to this corpus's geometry: A_0 and A_g are any two
symmetric invertible forms on the Feshbach complement. That generality is the
point -- the identity is available wherever the shape appears -- and it is also
the limit: this module proves nothing about Yang-Mills, and the closing check
says so with a witness rather than a caveat.
"""

from __future__ import annotations

import sympy as sp

from ._core import _suite

feshbach = _suite("the Feshbach resolvent comparison")

_SEC = "G17; G22; G23"

# Deterministic data. No RNG: a check whose witness changes between runs cannot
# be argued with, and the identity is exact, so one fixed family settles it.
_CASES = ((3, 1, "1/10"), (4, 2, "-1/7"), (5, 3, "3/100"), (6, 4, "-1/50"))


def _forms(n: int, seed: int, gval: str, scale: int = 1):
    """A_0 symmetric positive definite, V symmetric, A_g = A_0 + g V, source w."""
    b = sp.Matrix(n, n, lambda i, j: sp.Rational((i * 7 + j * 3 + seed) % 5 - 2))
    a0 = b * b.T + (n + 3) * sp.eye(n)
    v = sp.Matrix(n, n, lambda i, j: sp.Rational(((i + 2) * (j + 3) + seed) % 7 - 3))
    v = scale * (v + v.T) / 2
    g = sp.Rational(gval)
    w = sp.Matrix(n, 1, lambda i, j: sp.Rational((i * 5 + seed) % 9 - 4))
    return a0, v, g, a0 + g * v, w


def _kappa(a0, v) -> float:
    """The relative form bound: least k with -k A_0 <= V <= k A_0."""
    inv = a0.cholesky().inv()
    return max(abs(sp.N(e)) for e in (inv * v * inv.T).eigenvals())


@feshbach.check(
    "the interacting inverse image cancels: (A_g - A_0)[R_0 w, R_g w] = <(R_0 - R_g)w, w>", _SEC
)
def _():
    # Two lines, and the reason the rest of the module exists.
    #   A_g[R_0 w, R_g w] = (R_0 w)^T A_g A_g^-1 w = <R_0 w, w>
    #   A_0[R_0 w, R_g w] = (A_0 R_0 w)^T R_g w    = <w, R_g w>   (A_0 symmetric)
    # Subtract. The mixed pairing of a free against an interacting inverse image
    # is a difference of two quadratic forms of the SAME vector, so no absolute
    # bound on the interacting resolvent is needed to control it -- only a
    # comparison of the two forms. Exact, not numerical: the residual is 0.
    residuals = []
    for n, seed, gval in _CASES:
        a0, v, g, ag, w = _forms(n, seed, gval)
        u0, ug = a0.inv() * w, ag.inv() * w
        lhs = (u0.T * (g * v) * ug)[0]
        rhs = (u0.T * w)[0] - (ug.T * w)[0]
        residuals.append(sp.simplify(lhs - rhs))
    ok = all(r == 0 for r in residuals)
    return ok, (
        f"exact over {len(_CASES)} form pairs at n = 3, 4, 5, 6 with rational g: the residual "
        f"(A_g - A_0)[R_0 w, R_g w] - <(R_0 - R_g)w, w> is {set(map(str, residuals))}, "
        "identically zero and not merely small. Requires only that A_0 be symmetric and both "
        "forms invertible on the complement"
    )


@feshbach.check("the variational sandwich puts the free optimizer on one side", _SEC)
def _():
    # With A > 0, <A^-1 w, w> = sup_u (2<u,w> - A[u,u]), attained at u = A^-1 w.
    # Evaluating each supremum at the OTHER problem's optimizer sandwiches the
    # difference between the interaction form on the two optimizers:
    #     g V[u_g, u_g] <= <(R_0 - R_g)w, w> <= g V[u_0, u_0]     (g > 0)
    # The upper side involves only u_0 -- the Gaussian object. That is the half
    # a free-field estimate already controls, obtained with no information about
    # the interacting problem at all.
    held = []
    for n, seed, gval in _CASES:
        a0, v, g, ag, w = _forms(n, seed, gval)
        u0, ug = a0.inv() * w, ag.inv() * w
        # every entry is rational, so the sandwich is decided exactly -- no tolerance
        mid = sp.nsimplify((u0.T * w)[0] - (ug.T * w)[0])
        lo, hi = sorted([sp.Rational(g * (u0.T * v * u0)[0]), sp.Rational(g * (ug.T * v * ug)[0])])
        held.append(bool(lo <= mid <= hi))
    return all(held), (
        f"the sandwich g V[u_g,u_g] <= <(R_0 - R_g)w,w> <= g V[u_0,u_0] holds in all "
        f"{len(held)} cases. One side is the interaction form on the free optimizer alone, so "
        "a Gaussian estimate closes it; the other still names u_g and is what the next check "
        "trades for a relative form bound"
    )


@feshbach.check(
    "a relative form bound gives the explicit constant C = kappa/(1-|g|kappa)^2 <R_0 w,w>", _SEC
)
def _():
    # If |V[u,u]| <= kappa A_0[u,u] with |g| kappa < 1, then A_g >= (1-|g|kappa) A_0,
    # hence R_g <= R_0/(1-|g|kappa) in the form sense, and the remaining slot closes:
    #   V[u_g,u_g] <= kappa A_0[u_g,u_g] <= kappa/(1-|g|kappa) <R_g w,w>
    #                                    <= kappa/(1-|g|kappa)^2 <R_0 w,w>.
    # So the whole quantity is O(|g|) with a constant built from Gaussian data and
    # kappa alone. NOTE what this is: a RELATIVE (KLMN-type) bound, not an
    # absolute operator bound on R_g. That is the entire saving, and the entire
    # remaining exposure -- see the closing check.
    rows = []
    for n, seed, gval in _CASES:
        a0, v, g, ag, w = _forms(n, seed, gval)
        u0, ug = a0.inv() * w, ag.inv() * w
        mid = abs(sp.N((u0.T * w)[0] - (ug.T * w)[0]))
        k = _kappa(a0, v)
        gabs = abs(sp.N(g))
        bound = gabs * k / (1 - gabs * k) ** 2 * sp.N((u0.T * w)[0])
        rows.append((n, k, float(mid), float(bound), bool(mid <= bound)))
    return all(r[4] for r in rows), (
        "the predicted bound holds in every case: "
        + "; ".join(f"n={n} kappa={k:.3f} |value|={m:.4g} <= {b:.4g}" for n, k, m, b, _ in rows)
        + ". The constant uses only <R_0 w, w> and kappa -- no quantity evaluated on the "
        "interacting problem"
    )


@feshbach.check(
    "FINDING: the reduction buys a relative form bound, not the estimate -- void at |g| kappa >= 1",
    _SEC,
    tier=2,
)
def _():
    # What this module does NOT do, recorded as a witness instead of a caveat.
    # Scaling V alone drives kappa up at fixed g, and the constant degrades like
    # (1 - |g| kappa)^-2 before going through infinity. Past |g| kappa = 1 the
    # form A_g is no longer positive on the complement and the whole variational
    # route is void -- not loose, void.
    #
    # This is the shape of the large-field problem, which is why the identity
    # above is a reduction and not a solution: for a lattice gauge interaction
    # the relative form bound with a volume-uniform kappa is exactly what fails
    # on the rough set, and G22 is the registered statement of that failure.
    # Anyone reading the first three checks as an infinite-volume estimate should
    # read this one: the checks are exact linear algebra, and the physics is in
    # whether kappa exists uniformly, which nothing here establishes.
    g = sp.Rational(1, 100)
    row = []
    for scale in (1, 4, 16, 64, 256):
        a0, v, _g, _ag, _w = _forms(4, 2, "1/100", scale=scale)
        k = _kappa(a0, v)
        row.append((scale, k, float(1 - abs(sp.N(g)) * k)))
    grows = all(row[i][1] < row[i + 1][1] for i in range(len(row) - 1))
    degrades = all(row[i][2] > row[i + 1][2] for i in range(len(row) - 1))
    survives = row[0][2] > 0 and row[-1][2] > 0
    return grows and degrades and survives, (
        "kappa scales linearly with the interaction while the margin 1 - |g| kappa collapses: "
        + ", ".join(f"scale {s}: kappa={k:.2f}, margin={m:.4f}" for s, k, m in row)
        + f". The constant grows as margin^-2 ({row[0][1] / row[0][2] ** 2:.3f} to "
        f"{row[-1][1] / row[-1][2] ** 2:.1f} across this family) and the bound is void once "
        "|g| kappa >= 1, where A_g loses positivity. So the identity moves the difficulty from "
        "an absolute bound on the interacting resolvent to a volume-uniform relative form bound, "
        "and does not supply the latter. G22 is where that debt is registered"
    )


def _chain(n: int, mass: float):
    """A_0 = sum over links of (u_i - u_j)^2 + mass; V = sum of signed local link terms.

    A one-dimensional caricature of a local kinetic form with a near-zero mode.
    It models one thing only: how the two candidate hypotheses behave as the
    volume grows.
    """
    a0 = [[0.0] * n for _ in range(n)]
    v = [[0.0] * n for _ in range(n)]
    for i in range(n - 1):
        c = 0.5 * (-1) ** i
        for a, sa in ((i, 1), (i + 1, -1)):
            for b, sb in ((i, 1), (i + 1, -1)):
                a0[a][b] += sa * sb
                v[a][b] += c * sa * sb
    for i in range(n):
        a0[i][i] += mass
    return a0, v


def _spectral(a0, v, n: int):
    """(kappa, ||R_0 V||) by Cholesky plus power iteration, in floats."""
    import math
    import random

    ell = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(ell[i][k] * ell[j][k] for k in range(j))
            ell[i][j] = math.sqrt(a0[i][i] - s) if i == j else (a0[i][j] - s) / ell[j][j]

    def fwd(b):
        y = [0.0] * n
        for i in range(n):
            y[i] = (b[i] - sum(ell[i][k] * y[k] for k in range(i))) / ell[i][i]
        return y

    def back(b):
        x = [0.0] * n
        for i in reversed(range(n)):
            x[i] = (b[i] - sum(ell[k][i] * x[k] for k in range(i + 1, n))) / ell[i][i]
        return x

    def mul(m, u):
        return [sum(m[i][j] * u[j] for j in range(n)) for i in range(n)]

    def power(op):
        random.seed(0)
        u = [random.random() for _ in range(n)]
        lam = 0.0
        for _ in range(4000):
            w = op(u)
            s = math.sqrt(sum(x * x for x in w))
            if s < 1e-300:
                return 0.0
            u = [x / s for x in w]
            lam = s
        return lam

    kappa = power(lambda x: fwd(mul(v, back(x))))
    resolvent_norm = math.sqrt(power(lambda x: mul(v, back(fwd(back(fwd(mul(v, x))))))))
    return kappa, resolvent_norm


@feshbach.check(
    "the relative bound is volume-stable where the Neumann quantity is not", _SEC, tier=2
)
def _():
    # The reason the reduction is a path and not just a restatement, and the
    # answer to "what does moving the difficulty buy".
    #
    # Neumann iteration on the second resolvent identity needs ||R_0 V||
    # bounded uniformly in the volume. That quantity ACCUMULATES: on a local
    # form with a near-zero mode it grows linearly in the size of the system,
    # because R_0 carries the growing inverse gap. The relative bound kappa
    # does not accumulate. It is a max over local terms rather than a sum:
    # if V = sum_x V_x and A_0 = sum_x A_{0,x} with V_x <= kappa A_{0,x} as
    # forms, summing gives V <= kappa A_0 with the SAME kappa at any volume.
    #
    # Scope, and it matters: this is a one-dimensional caricature of a local
    # kinetic form, not a gauge interaction. It demonstrates the mechanism --
    # relative bounds are stable under volume growth, absolute ones are not --
    # and nothing about SU(N). Whether the gauge interaction admits such a
    # local decomposition on the rough set is G22 and is untouched here.
    rows = []
    for n in (4, 8, 16, 32, 64):
        a0, v = _chain(n, 1e-6)
        rows.append((n, *_spectral(a0, v, n)))
    kappas = [k for _n, k, _r in rows]
    norms = [r for _n, _k, r in rows]
    flat = max(kappas) - min(kappas) < 1e-3
    grows = all(norms[i] < norms[i + 1] for i in range(len(norms) - 1)) and norms[-1] > 8 * norms[0]
    return flat and grows, (
        "across n = 4..64 with a near-zero mode: kappa is "
        + ", ".join(f"{k:.6f}" for k in kappas)
        + f" (spread {max(kappas) - min(kappas):.2e}, volume-independent) while ||R_0 V|| is "
        + ", ".join(f"{r:.1f}" for r in norms)
        + f" (a factor {norms[-1] / norms[0]:.1f} across the same range, growing linearly). "
        "The quantity Neumann iteration needs diverges with the volume; the quantity the "
        "collapse identity needs does not, because a relative bound is a max over local terms "
        "and not a sum. One dimension, kinetic interaction: the mechanism, not a gauge statement"
    )
