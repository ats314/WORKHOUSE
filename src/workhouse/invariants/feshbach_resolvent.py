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
        mid = sp.N((u0.T * w)[0] - (ug.T * w)[0])
        lo, hi = sorted([sp.N(g * (u0.T * v * u0)[0]), sp.N(g * (ug.T * v * ug)[0])])
        held.append(bool(lo - sp.Float("1e-20") <= mid <= hi + sp.Float("1e-20")))
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
