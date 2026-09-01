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

import flint
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


# --------------------------------------------------------------------------
# Publication edition rev. 5 (2026-08-30) states the window theorem, its
# retained-shell corollary and the process-completeness lemma under three
# labels of its own. Each names a finite computation the proof delegates to,
# and none of the three was registered: the shelf and the cycle census above
# are the INGREDIENTS, and what follows is the assembly the theorem performs
# on them -- the support bound, the centre-neutral Casimir bound, the two
# winding energies, the state count, and the centre-charge classification of
# every second-order intermediate.
# --------------------------------------------------------------------------


def _casimir(labels, n):
    """C_2 of the su(n) dominant weight with Dynkin labels ``labels``.

    Roots normalised to squared length 2, so ``(omega_i, omega_j) = min(i,j) - ij/n``
    and ``(omega_i, rho) = i(n-i)/2``; then ``C_2 = ((l, l) + 2(l, rho))/2``.
    """
    m = len(labels)
    assert m == n - 1
    gram = [[Rational(min(i, j)) - Rational(i * j, n) for j in range(1, n)] for i in range(1, n)]
    norm = sum(labels[i] * labels[j] * gram[i][j] for i in range(m) for j in range(m))
    rho = sum(labels[i] * Rational((i + 1) * (n - i - 1), 2) for i in range(m))
    return Rational(1, 2) * (norm + 2 * rho)


@electric_shell.check(
    "below 5 C_F/2 the trivial-flux electric spectrum is exactly 0 and 2 C_F",
    "PUBLICATION rev5 Thm. 1 (uniform first electric spectral window)",
    rests_on=(
        "every nontrivial irrep clears 5/4 C_F, except the fundamental pair",
        "the torus graph is simple, and the only short cycles are the L = 3 winding triangles",
        "every 4-cycle is an elementary face, except exactly the 3L^2 straight winding loops at L = 4",  # noqa: E501
    ),
)
def _():
    # The theorem's proof is a chain of finite facts, and this check walks the
    # chain rather than trusting the page. (1) Every nontrivial irrep costs at
    # least C_F on its link, so a state below 5 C_F/2 has at most four charged
    # links -- an integer bound from a rational inequality. (2) A charged
    # support of minimum degree two on at most four links is a C_3 or a C_4;
    # the sibling checks enumerate those on the torus: the L = 3 winding
    # triangles, the elementary faces, and the L = 4 straight winding loops.
    # (3) A winding loop transports ONE irrep, whose N-ality must vanish in the
    # trivial one-form sector; a nonzero root-lattice weight has C_2 >= N, and
    # both winding energies then clear 5 C_F/2 for every N >= 3. (4) A face
    # transports one irrep at energy 2 C_2(R) < 5 C_F/2, which the shelf
    # confines to F or bar F. What is left is the vacuum and the faces, at
    # exactly 0 and 2 C_F, with nothing else below 5 C_F/2 -- so the shell's
    # external margin is at least C_F/2, uniformly in L and N.
    cf = (_N**2 - 1) / (2 * _N)
    # (1) |S| C_F <= sum_e C_2(R_e) = 2E < 5 C_F  =>  |S| <= 4, as an integer
    support_bound = max(s for s in range(0, 12) if s * 1 < 5) == 4
    # (3) the centre-neutral Casimir bound, by enumeration of dominant weights
    # in a box. C_2 is increasing in every Dynkin label, so the minimum over
    # the whole root lattice is found inside the box; equality at the adjoint.
    neutral = {}
    for n in range(3, 8):
        box = product(range(0, 4), repeat=n - 1)
        rows = []
        for lab in box:
            if not any(lab):
                continue
            n_ality = sum((i + 1) * lab[i] for i in range(n - 1)) % n
            if n_ality == 0:
                rows.append((_casimir(lab, n), lab))
        floor = min(rows)
        adjoint = tuple([1] + [0] * (n - 3) + [1])
        neutral[n] = (
            floor[0] == n
            and floor[1] == adjoint
            and all(c > n for c, lab in rows if lab != adjoint)
            # and the (lambda, rho) >= N - 1 step the proof states on the way
            and all(
                sum(lab[i] * Rational((i + 1) * (n - i - 1), 2) for i in range(n - 1)) >= n - 1
                for _c, lab in rows
            )
        )
    # sanity: the Casimir formula reproduces the fundamental-weight values
    formula_ok = all(
        _casimir(tuple(1 if j == i else 0 for j in range(1, n)), n)
        == _casimir_fundamental_weight(i, n)
        for n in range(3, 8)
        for i in range(1, n)
    )
    # the two winding energies against the window, as rational functions of N
    triangle = simplify(Rational(3, 2) * _N - Rational(5, 2) * cf - (_N**2 + 5) / (4 * _N)) == 0
    line = simplify(2 * _N - Rational(5, 2) * cf - (3 * _N**2 + 5) / (4 * _N)) == 0
    # (4) a face below the window carries F or bar F only: the shelf, re-read
    # from the same enumeration, so this check does not merely cite its sibling
    fundamental_only = {}
    for n in range(3, 8):
        cfn = Rational(n**2 - 1, 2 * n)
        under = [
            lab
            for lab in product(range(0, 3), repeat=n - 1)
            if any(lab) and 2 * _casimir(lab, n) < Rational(5, 2) * cfn
        ]
        fund = {
            tuple(1 if j == 1 else 0 for j in range(1, n)),
            tuple(1 if j == n - 1 else 0 for j in range(1, n)),
        }
        fundamental_only[n] = set(under) == fund
    # the window and the margin
    face_energy = simplify(2 * cf - 4 * (cf / 2)) == 0
    margin = simplify((Rational(5, 2) * cf - 2 * cf) - cf / 2) == 0
    vacuum_margin = simplify(2 * cf - cf / 2 - Rational(3, 2) * cf) == 0
    ok = (
        support_bound
        and formula_ok
        and all(neutral.values())
        and triangle
        and line
        and all(fundamental_only.values())
        and face_energy
        and margin
        and vacuum_margin
    )
    return ok, (
        "a state below 5 C_F/2 charges at most 4 links (|S| C_F <= 2E < 5 C_F); the sibling "
        "cycle census makes such a support a C_3 (L = 3, winding) or a C_4 (a face, or at L = 4 "
        "a straight winding loop). A winding loop carries one centre-neutral irrep, and over "
        "the dominant weights of su(3..7) the centre-neutral floor is C_2 = N, attained only at "
        "the adjoint, with (lambda, rho) >= N - 1 throughout; so the triangle costs "
        "3N/2 - 5C_F/2 = (N^2+5)/4N > 0 and the line 2N - 5C_F/2 = (3N^2+5)/4N > 0 above the "
        "window. A face below it carries F or bar F alone (the only weights with "
        "2 C_2 < 5 C_F/2 at N = 3..7), at exactly 4 (C_F/2) = 2 C_F. Hence "
        "spec cap [0, 5C_F/2) = {0, 2C_F}, the shell sits C_F/2 below the window and 2 C_F "
        "above the vacuum, and the external margin is >= C_F/2 uniformly in L and N"
    )


@electric_shell.check(
    "the retained electric shell is exactly the trivial-flux charge-odd plaquette span",
    "PUBLICATION rev5 Thm. 1, eq. (retained-shell)",
    rests_on=(
        "below 5 C_F/2 the trivial-flux electric spectrum is exactly 0 and 2 C_F",
        "every 4-cycle is an elementary face, except exactly the 3L^2 straight winding loops at L = 4",  # noqa: E501
        "d_2 d_3 = 0 on the built complex",
    ),
)
def _():
    # The corollary is a count with two uniqueness inputs. Uniqueness: at each
    # degree-two vertex Schur's lemma makes the intertwiner unique, so a face
    # carries exactly two lines, chi_p |0> and its conjugate, exchanged by C;
    # for N >= 3 the fundamental is not self-conjugate (omega_1 = omega_{N-1}
    # only at N = 2), so the two are orthonormal by Peter-Weyl and the odd
    # combination is one line per face. The count: the cycle census gives the
    # faces as closed 4-walks, 24 per site (12 faces through a site, two
    # orientations each), and 24 L^3 / (4 sites x 2 orientations) = 3 L^3 is
    # the number of columns of the built d_2. At L = 4 the 3 L^2 straight
    # winding loops also sit at 2 C_F, and would add 6 L^2 = 96 states to the
    # shell -- with N-ality one, so trivial one-form flux removes every one of
    # them, at every rank and not only at SU(4).
    from .. import torus as TOR

    report = {}
    for ell in (3, 4, 5):
        quads = _cycles(ell, 4)
        face_walks = [
            st
            for st, lift in quads
            if lift == (0, 0, 0)
            and len({tuple(abs(c) for c in s) for s in st}) == 2
            and all(st.count(s) == 1 for s in st)
        ]
        straight = [st for st, lift in quads if lift != (0, 0, 0)]
        faces_from_census = Rational(len(face_walks) * ell**3, 8)
        columns = TOR.d2_matrix(ell).ncols()
        report[ell] = (
            len(face_walks),
            faces_from_census,
            columns,
            # global straight lines: 3 directions x L^2 lines, each in 2 orientations
            (len(straight) * ell**3) // 4,
        )
    counts_ok = all(
        walks == 24 and faces == cols == 3 * ell**3
        for ell, (walks, faces, cols, _) in report.items()
    )
    winding_states = {ell: r[3] for ell, r in report.items()}
    winding_ok = winding_states == {3: 0, 4: 6 * 16, 5: 0}
    # self-conjugacy of the fundamental happens at N = 2 alone
    self_conjugate = [n for n in range(2, 13) if n - 1 == 1]
    ok = counts_ok and winding_ok and self_conjugate == [2]
    return ok, (
        f"closed face-walks per site, faces, d_2 columns, oriented straight winding loops: "
        f"{ {ell: tuple(str(v) for v in r) for ell, r in report.items()} }. The 2 C_F eigenspace "
        "of the trivial-flux sector is two oriented lines per face -- 6 L^3 states, one odd "
        "combination each, so the charge-odd shell is 3 L^3-dimensional and equals the span "
        "of |p,->. The only other 2 C_F configurations are the 96 oriented once-winding "
        "fundamental lines at L = 4, all of N-ality one and all removed by trivial flux; "
        "F is self-conjugate at N = 2 only, which is where the odd line vanishes"
    )


def _sparse(vec_items, n):
    """Sorted ``((edge, coeff mod n), ...)`` with zero coefficients dropped."""
    return tuple(sorted((e, c % n) for e, c in vec_items.items() if c % n))


@electric_shell.check(
    "second-order off-diagonal processes are exactly the adjacent shared-link channels",
    "PUBLICATION rev5 Lemma (second-order process completeness)",
    rests_on=(
        "the retained electric shell is exactly the trivial-flux charge-odd plaquette span",
        "the plaquette graph is 12-regular and two faces share at most one link",
        "the shared-link weights are Weingarten, not an isotropy assumption",
        "each channel gap is C_F + C_R/2, and the weights sum to one",
    ),
)
def _():
    # The lemma's combinatorial core, enumerated. A term chi_p^eps chi_q^eta on
    # the p side can share an electric intermediate with chi_p'^eps' chi_r^eta'
    # on the p' side only if the two carry the same linkwise centre charge,
    # d(eps p + eta q) = d(eps' p' + eta' r) in C_1(Z_N). The proof reduces
    # every solution to two routes: the same-face route (q = p, eta = -eps and
    # likewise on the other side) and the exchange route (q = p', r = p, with
    # eta = eps', eta' = eps). Everything else is excluded by the small-support
    # two-cycle lemma, whose modular subtlety at N = 3, 4 (a coefficient +-3
    # or +-4 vanishing mod N) is exactly why the enumeration runs mod N rather
    # than over Z. It runs at L = 3 and L = 4, N = 3, 4, 5, with p fixed at
    # the origin in each of its three orientations -- translation covariance
    # is what makes that exhaustive -- and p', q, r over every face.
    #
    # The representation-theory half is not re-derived here: a link-disjoint
    # exchange pair is orthogonal by charge parity, and a shared-link pair has
    # exactly the four fusion channels, whose weights `the four channel
    # weights follow from dimension and Casimir` and Weingarten checks carry.
    # What this check settles is that no OTHER intermediate exists.
    from .. import torus as TOR

    report = {}
    for ell in (3, 4):
        d2 = TOR.d2_matrix(ell)
        nf, ne = d2.ncols(), d2.nrows()
        cols = [{r: int(d2[r, c]) for r in range(ne) if int(d2[r, c]) != 0} for c in range(nf)]

        def shares(a, b, cols=cols):
            return len(set(cols[a]) & set(cols[b]))

        for n in (3, 4, 5):
            single = {}
            for r in range(nf):
                for s in (1, -1):
                    key = _sparse({e: s * c for e, c in cols[r].items()}, n)
                    single.setdefault(key, []).append((r, s))
            zero = exchange_shared = exchange_disjoint = other = 0
            for p in range(3):
                for eps in (1, -1):
                    for q in range(nf):
                        for eta in (1, -1):
                            v = {}
                            for e, c in cols[p].items():
                                v[e] = v.get(e, 0) + eps * c
                            for e, c in cols[q].items():
                                v[e] = v.get(e, 0) + eta * c
                            for pp in range(nf):
                                if pp == p:
                                    continue
                                for eps2 in (1, -1):
                                    w = dict(v)
                                    for e, c in cols[pp].items():
                                        w[e] = w.get(e, 0) - eps2 * c
                                    for r, eta2 in single.get(_sparse(w, n), []):
                                        if q == p and eta == -eps and r == pp and eta2 == -eps2:
                                            zero += 1
                                        elif q == pp and r == p and eta == eps2 and eta2 == eps:
                                            if shares(p, pp) == 1:
                                                exchange_shared += 1
                                            else:
                                                exchange_disjoint += 1
                                        else:
                                            other += 1
            report[(ell, n)] = (zero, exchange_shared, exchange_disjoint, other)
    # per origin face and sign: one same-face route to every other face and
    # sign (2 (3L^3 - 1)), one exchange route per (p', eps'); twelve of the
    # exchange partners share a link, the rest are link-disjoint
    expected = {
        (ell, n): (
            3 * 2 * 2 * (3 * ell**3 - 1),
            3 * 2 * 2 * 12,
            3 * 2 * 2 * (3 * ell**3 - 1 - 12),
            0,
        )
        for (ell, n) in report
    }
    # sharpness of the small-support lemma at L = 2: a wrapping sheet is a
    # four-face cycle there, so the classification is NOT available at L = 2
    d2_two = TOR.d2_matrix(2)
    sheet = TOR.wrapping_sheet(2, (1, 2))
    image = d2_two * flint.fmpz_mat([[s] for s in sheet])
    sharp = sum(sheet) == 4 and all(int(image[r, 0]) == 0 for r in range(image.nrows()))
    ok = report == expected and sharp
    return ok, (
        "centre-charge matches d(eps p + eta q) = d(eps' p' + eta' r) mod N, p at the origin "
        "in three orientations, p', q, r over every face, signs free -- (same-face, exchange "
        f"sharing a link, exchange link-disjoint, anything else): {report}. No third kind of "
        "intermediate exists at L = 3, 4 for N = 3, 4, 5, the +-3 and +-4 modular escapes "
        "included; every exchange partner that shares a link is one of a face's 12 neighbours, "
        "and the shared link then carries exactly two fundamental factors, i.e. the four fusion "
        "channels. At L = 2 the lemma is sharp: the wrapping sheet is a four-face cycle"
    )
