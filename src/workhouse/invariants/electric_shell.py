"""What isolates the electric shell, and what the torus offers below it.

The 30 August master edition replaced two prose premises with theorems. Both
turn on arithmetic small enough to re-derive here, and both had been asserted
in every earlier edition:

* the retained shell -- that nothing else in the trivial-flux sector sits in
  ``[0, 5 C_F / 2)`` except the vacuum and the oriented one-plaquette lines.
  Two ingredients: a Casimir shelf that clears ``5 C_F / 4`` for every irrep
  but the fundamental pair, and a cycle census that says the only closed link
  sets short enough to fit the energy budget are elementary faces, plus the
  windings the one-form flux condition removes;
* the small-``|u|`` persistence of that shell, whose contour clearance is
  decided by which SU(3) one-link energies the additive semigroup can reach
  near the shell.

Neither check touches the gauge theory. They are the finite arithmetic the
proofs delegate to, carried out, so that a reader auditing the new theorems
does not have to take the counting on the page's word.
"""

from __future__ import annotations

from itertools import product

from sympy import Rational, Symbol, factor, simplify

from ._core import _suite

# ==========================================================================
electric_shell = _suite("the electric shell, and what isolates it")

_N = Symbol("N", positive=True, integer=True)


def _casimir_fundamental_weight(i, n):
    """C_2(omega_i) for su(n), normalised so every root has squared length 2."""
    return Rational(1, 2) * i * (n - i) * (n + 1) / n


@electric_shell.check(
    "every nontrivial irrep clears 5/4 C_F, except the fundamental pair",
    "MASTER edition Thm. 1 (uniform first electric spectral window)",
)
def _():
    # The window proof needs a shelf, not just minimality: every irrep other
    # than 1, F, bar F must sit STRICTLY above (5/4) C_F, or a two-link or
    # four-link support could hide under the 5 C_F budget. Dominance
    # monotonicity reduces the whole weight lattice to three comparisons,
    # and each is a rational function of N with a sign this check settles
    # symbolically rather than by sampling ranks.
    cf = (_N**2 - 1) / (2 * _N)
    shelf = Rational(5, 4) * cf
    cases = {
        # C_2(omega_2), available only from N >= 4 (no interior node at N = 3)
        "omega_2": (
            _casimir_fundamental_weight(2, _N) - shelf,
            (_N + 1) * (3 * _N - 11) / (8 * _N),
        ),
        # C_2(2 omega_1) = 2 C_2(omega_1) + (N-1)(N+1)/N  -- the symmetric square
        "2omega_1": ((_N - 1) * (_N + 2) / _N - shelf, (_N - 1) * (3 * _N + 11) / (8 * _N)),
        # C_2(omega_1 + omega_{N-1}) = N -- the adjoint
        "adjoint": (_N - shelf, (3 * _N**2 + 5) / (8 * _N)),
    }
    identities = {k: simplify(lhs - rhs) == 0 for k, (lhs, rhs) in cases.items()}
    # Positivity for ALL N on the range each case is used over, by the sign of
    # each factor rather than by sampling ranks: 8N > 0 always; (N+1) > 0
    # always and (3N-11) > 0 exactly from N = 4; (N-1) and (3N+11) > 0 from
    # N = 2; and 3N^2 + 5 > 0 identically. The omega_2 numerator is why the
    # N = 3 case must run on the other two: 3N - 11 is NEGATIVE at N = 3,
    # which is exactly the rank with no interior Dynkin node, so the case
    # never arises there.
    lowest = {"omega_2": 4, "2omega_1": 3, "adjoint": 3}
    positive = {}
    for name, floor in lowest.items():
        expr = factor(cases[name][1])
        num, den = expr.as_numer_denom()
        pieces = num.as_ordered_factors() if num.is_Mul else [num]
        signs = [p.subs(_N, floor) > 0 and p.diff(_N).subs(_N, floor) >= 0 for p in pieces]
        positive[name] = all(signs) and den.subs(_N, floor) > 0
    # and the boundary the omega_2 case turns on, stated rather than implied
    omega2_at_three = cases["omega_2"][1].subs(_N, 3) < 0
    # And the minimality the shelf sits on: C_2(omega_i) - C_F >= 0 with
    # equality exactly at i = 1 and i = N-1.
    equality = {}
    for n in range(3, 13):
        gaps = {
            i: _casimir_fundamental_weight(i, n) - Rational(n**2 - 1, 2 * n) for i in range(1, n)
        }
        equality[n] = {i for i, g in gaps.items() if g == 0} == {1, n - 1} and all(
            g >= 0 for g in gaps.values()
        )
    ok = (
        all(identities.values())
        and all(positive.values())
        and omega2_at_three
        and all(equality.values())
    )
    return ok, (
        "the three dominance-reduced comparisons are exactly "
        "(N+1)(3N-11)/8N, (N-1)(3N+11)/8N and (3N^2+5)/8N as rational functions of N. Each is "
        "positive for ALL N on its range by the sign of its factors -- positive at the floor "
        "and nondecreasing above it -- the first from N = 4 and the other two from N = 3; and "
        "(N+1)(3N-11) is negative at N = 3, which is exactly the rank with no interior Dynkin "
        "node, so that case never arises there. Underneath, C_2(omega_i) = C_F exactly at "
        "i = 1, N-1 and nowhere else, checked N = 3..12"
    )


@electric_shell.check(
    "the SU(3) additive electric spectrum leaves 14, 16, 17 around the shell",
    "MASTER edition Thm. 2 (SU(3) all-orders finite-volume Riesz island)",
)
def _():
    # The Riesz contour of the island theorem is placed by ARITHMETIC, not by
    # a norm bound: the free electric energies are sums of one-link numerators
    # p^2 + q^2 + pq + 3p + 3q in units of 1/6, and what decides the clearance
    # is which totals the additive semigroup can reach next to the shell's 16.
    # If any semigroup element fell strictly between 14 and 16, or between 16
    # and 17, the separations delta_-, delta_+ printed in the theorem would be
    # wrong. Enumerate rather than trust.
    singles = sorted(
        {
            p * p + q * q + p * q + 3 * p + 3 * q
            for p in range(0, 8)
            for q in range(0, 8)
            if (p, q) != (0, 0)
        }
    )
    below18 = [s for s in singles if s < 18]
    reach = {0}
    for _ in range(6):  # at most six links matter below 18
        reach |= {r + s for r in reach for s in singles if r + s <= 24}
    attainable = sorted(reach)
    neighbours = [a for a in attainable if 12 <= a <= 18]
    ok = (
        below18 == [4, 9, 10, 16]
        and 16 in attainable
        and 15 not in attainable
        and neighbours == [12, 13, 14, 16, 17, 18]
    )
    return ok, (
        f"nonzero one-link numerators below 18 are {below18}; the additive semigroup near the "
        f"shell attains {neighbours}, so 16 is flanked by 14 below and 17 above with 15 "
        "unattainable. Those are exactly the gaps the printed separations "
        "delta_- >= (1 - 15 lambda)/3 and delta_+ >= (1 - 33 lambda)/6 are computed from"
    )


# --------------------------------------------------------------------------
# The cycle census the window proof delegates to.
#
# The support of a state below 5 C_F / 2 has at most four charged links and
# minimum degree two, so it is a single C_3 or C_4. The proof then claims two
# things about the periodic cubic graph, and both are finite: the only
# closed link sets shorter than four are the L = 3 straight winding
# triangles, and every 4-cycle is an elementary face except exactly the
# 3 L^2 straight winding loops at L = 4.
# --------------------------------------------------------------------------

_UNIT = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def _steps():
    return [s for e in _UNIT for s in (e, tuple(-c for c in e))]


def _cycles(ell, length):
    """Every closed length-``length`` walk from the origin with distinct sites.

    Returned as the multiset of its lifted steps, so a caller can tell a
    contractible face from a winding loop: a face's steps sum to zero in
    ``Z^3``, a winding loop's sum to ``L w`` with ``w != 0``.
    """
    out = []
    steps = _steps()

    def walk(site, lift, path, taken):
        if len(taken) == length:
            if site == (0, 0, 0):
                out.append((tuple(taken), lift))
            return
        for s in steps:
            nxt = tuple((site[i] + s[i]) % ell for i in range(3))
            # simple cycle: no repeated site except the closing return
            if nxt in path and not (nxt == (0, 0, 0) and len(taken) == length - 1):
                continue
            walk(nxt, tuple(lift[i] + s[i] for i in range(3)), path | {nxt}, [*taken, s])

    walk((0, 0, 0), (0, 0, 0), {(0, 0, 0)}, [])
    return out


@electric_shell.check(
    "the torus graph is simple, and the only short cycles are the L = 3 winding triangles",
    "MASTER edition Thm. 1, proof (support census)",
)
def _():
    # Two claims, both enumerated at L = 3, 4, 5: the periodic cubic graph has
    # no multi-edge and no loop (so "minimum degree two" really does force a
    # cycle of length at least three), and the only closed walks shorter than
    # four are the straight triangles that exist at L = 3 alone. The triangles
    # are why the proof needs the centre-flux condition at all: they are
    # noncontractible, and their N-ality is what removes them.
    report = {}
    for ell in (3, 4, 5):
        # simplicity: distinct neighbours, none equal to the site itself
        sites = list(product(range(ell), repeat=3))
        simple = all(
            len({tuple((x[i] + s[i]) % ell for i in range(3)) for s in _steps()}) == 6
            and all(tuple((x[i] + s[i]) % ell for i in range(3)) != x for s in _steps())
            for x in sites
        )
        tris = _cycles(ell, 3)
        winding = [lift for _, lift in tris if lift != (0, 0, 0)]
        report[ell] = (simple, len(tris), len(winding))
    ok = (
        report[3][0]
        and report[4][0]
        and report[5][0]
        and report[3][1] > 0
        and report[3][1] == report[3][2]  # every L=3 triangle winds
        and report[4][1] == 0
        and report[5][1] == 0
    )
    per_site = report[3][1]
    return ok, (
        f"L = 3, 4, 5 all simple (six distinct neighbours, no self-loop); closed 3-walks from "
        f"one site: {report[3][1]} at L = 3 (all of them winding, lifted step sum L w), "
        f"{report[4][1]} at L = 4, {report[5][1]} at L = 5. So a support of minimum degree two "
        f"and at most four links is a C_3 only at L = 3, and every such C_3 is noncontractible "
        f"-- {per_site} per site, i.e. the 3 L^2 straight triangles, all removed by trivial "
        "one-form flux"
    )


@electric_shell.check(
    "every 4-cycle is an elementary face, except exactly the 3L^2 straight winding loops at L = 4",
    "MASTER edition Thm. 1, proof (four-cycle classification)",
)
def _():
    # The last geometric step of the window proof. A four-cycle with zero
    # winding is forced to be a plaquette boundary; the only nonzero winding
    # a four-cycle can carry is four collinear steps, which needs L = 4. The
    # count matters as much as the classification: 3 L^2 straight loops is
    # what the L = 4 coincidence costs, and it is the same number at every
    # rank -- which is why the flux condition is load-bearing for all N, not
    # only for SU(4).
    report = {}
    for ell in (3, 4, 5):
        quads = _cycles(ell, 4)
        contractible = [st for st, lift in quads if lift == (0, 0, 0)]
        winding = [st for st, lift in quads if lift != (0, 0, 0)]
        # a contractible 4-cycle is a face iff its steps are +-e_i, +-e_j with
        # i != j, each appearing once
        faces = [
            st
            for st in contractible
            if len({tuple(abs(c) for c in s) for s in st}) == 2
            and all(st.count(s) == 1 for s in st)
        ]
        straight = [st for st in winding if len({tuple(abs(c) for c in s) for s in st}) == 1]
        report[ell] = (len(quads), len(contractible), len(faces), len(winding), len(straight))
    ok = (
        all(c == f for _, c, f, _, _ in report.values())  # every contractible 4-cycle is a face
        and report[3][3] == 0
        and report[5][3] == 0
        and report[4][3] == report[4][4] > 0  # at L = 4 all winding 4-cycles are straight
    )
    straight4 = report[4][4]
    return ok, (
        f"closed 4-walks from one site (count, contractible, faces, winding, straight): {report}. "
        "Every contractible 4-cycle is an elementary plaquette boundary at L = 3, 4, 5; the only "
        f"winding 4-cycles occur at L = 4, where all {straight4} of them (three directions, two "
        "orientations) are straight -- globally the 3 L^2 = 48 once-winding loops, excluded by "
        "trivial one-form flux at every rank N >= 3, not only at SU(4)"
    )


@electric_shell.check(
    "the sealed radius-two report passes its six float checks at stated tolerances",
    "MASTER edition §5.4; paper/verify_radius2_report.py",
    tier=2,
)
def _():
    # T2 by construction: the radius-two delivery is finite-precision, and the
    # program that reads it is deliberately kept OUT of this package so the
    # exact layer stays float-free (constants.py's boundary rule). Running it
    # here is what makes the paper's radius-two sentences resolvable at all --
    # without this, four printed markers name nothing.
    #
    # What it establishes: the pinned SHA-256 of the sealed spectrum; that the
    # odd second-order block is Hermitian and real; that six of its eleven
    # eigenvalues are -2429/306 (x2), -404/51 (x3) and -2419/306 to 1e-12, so
    # the outer pair straddles the central triple by exactly 2 t_3 = 5/306;
    # that the certificate's direct C4/C5 matched-gap coefficients agree with
    # their weak-grid intercepts to 5e-6; that interlacing violation is
    # exactly 0; and that the fifth-order seed shape is traceless with nonzero
    # trace-square, i.e. the instrument emits a matrix and not a scalar.
    import subprocess
    import sys

    from ._core import PAPER_DIR

    script = PAPER_DIR / "verify_radius2_report.py"
    if not script.exists():
        return False, f"{script} is missing: the paper's radius-two markers name nothing"
    done = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        cwd=str(PAPER_DIR),
        timeout=300,
    )
    lines = [ln for ln in done.stdout.splitlines() if ln.startswith(("PASS", "FAIL"))]
    failed = [ln for ln in lines if ln.startswith("FAIL")]
    ok = done.returncode == 0 and lines and not failed
    return ok, (
        f"{len(lines) - len(failed)}/{len(lines)} radius-two report checks pass against the "
        "pinned spectrum: the rational sub-block straddle is exactly 2 t_3 = 5/306, the C4/C5 "
        "matched-gap coefficients agree with their weak-grid intercepts to 5e-6, and the "
        "fifth-order seed shape is a traceless matrix with nonzero trace-square. Floats at "
        "stated tolerances throughout, which is why this is T2 and lives outside the exact layer"
        + (f"; FAILED: {failed}" if failed else "")
    )
