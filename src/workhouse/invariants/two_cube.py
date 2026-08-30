"""The two-cube charge-odd second-order closure (runs/two_cube_codd_o2_2026-08-29).

The 2026-08-29 delivery is the first genuinely multi-cube operator result in
the corpus: the connected adjacent-hopping coefficient re-derived on an actual
face-sharing two-cube (3,2,2) SU(3) Hilbert space (1,590,462 states at B=6),
with the left-cube, right-cube and shared-face contributions subtracted at the
operator level, target-blind. It recovers -1/12 at B=4 and +5/612 at B=6 --
the registry's own t_3 -- and exposes the sign-reversal mechanism channel by
channel.

Scope discipline, stated once for the whole suite: everything here is SECOND
order in u. None of it adjudicates C2 (the fourth-order off-axis C_shp), and
the delivery's own theorem note says so explicitly ("No cubic off-axis, rooted
fourth-order scalar, pentagonal, continuum, or infinite-volume claim is
changed"). What it does do for C2 is indirect: it retires the one-cube-only
objection to the second-order channel mechanism, and it demonstrates the
target-blind operator-level machinery a fourth-order adjudication (G3) would
need. The generators could not be re-run here (they need pyclebsch and three
sealed NPZ inputs that did not travel), so these checks verify the delivered
certificate's arithmetic against geometry rebuilt locally -- the same posture
as the one-cube B=6 audit next door in bridge.py.
"""

from __future__ import annotations

import json
from fractions import Fraction

from .. import constants as K
from ._core import ROOT, _suite

two_cube = _suite("two-cube charge-odd second-order closure (B=4 and B=6)")

_RUN = ROOT / "runs" / "two_cube_codd_o2_2026-08-29"

# The eleven oriented plaquettes of the (3,2,2) prism, in the frozen order of
# the delivery's Section 1: base vertex and ordered plane axes (1,2,3)=(x,y,z).
_FACES = (
    ((0, 0, 0), (1, 2)),
    ((0, 0, 0), (1, 3)),
    ((0, 0, 0), (2, 3)),
    ((0, 0, 1), (1, 2)),
    ((0, 1, 0), (1, 3)),
    ((1, 0, 0), (1, 2)),
    ((1, 0, 0), (1, 3)),
    ((1, 0, 0), (2, 3)),
    ((1, 0, 1), (1, 2)),
    ((1, 1, 0), (1, 3)),
    ((2, 0, 0), (2, 3)),
)
_I_L = (0, 1, 2, 3, 4, 7)
_I_R = (5, 6, 7, 8, 9, 10)
_I_F = (7,)


def _gram_conn() -> list[list[int]]:
    # G = B_row B_row^T rebuilt here from oriented cell boundaries -- the
    # delivery's own incidence array is not taken on trust. A face at base
    # vertex x in plane (a,b) has oriented boundary
    #   +(x,a) +(x+e_a,b) -(x+e_b,a) -(x,b),
    # the same convention bridge.py uses for the single cube.
    def step(x, a):
        y = list(x)
        y[a - 1] += 1
        return tuple(y)

    links: dict[tuple, int] = {}
    rows = []
    for x, (a, b) in _FACES:
        chain: dict[tuple, int] = {}
        for link, sign in (
            ((x, a), 1),
            ((step(x, a), b), 1),
            ((step(x, b), a), -1),
            ((x, b), -1),
        ):
            links.setdefault(link, len(links))
            chain[link] = chain.get(link, 0) + sign
        rows.append(chain)
    gram = [[sum(ri.get(link, 0) * rj.get(link, 0) for link in ri) for rj in rows] for ri in rows]
    # Moebius-fold the sources. A source cube's own face Gram is the target
    # Gram restricted to its faces (a face's boundary chain does not depend
    # on the ambient complex), so the lift-and-subtract collapses to index
    # arithmetic: an entry survives iff it is NOT inside L, R, or recovered
    # by the shared face F.
    conn = [[0] * 11 for _ in range(11)]
    for i in range(11):
        for j in range(11):
            weight = 1 - (
                (i in _I_L and j in _I_L) + (i in _I_R and j in _I_R) - (i in _I_F and j in _I_F)
            )
            conn[i][j] = gram[i][j] * weight
    return conn


def _cert() -> dict:
    return json.loads(
        (_RUN / "two_cube_b6_codd_o2_connected_kernel_certificate.json").read_text(encoding="utf-8")
    )


def _spectrum(kmat: list[list[Fraction]]) -> dict[Fraction, int]:
    # The connected geometry is four disjoint 2x2 cross-cell pair blocks plus
    # three isolated directions, so the exact spectrum is closed-form: the
    # pairs give diag +- offdiag, the isolated faces give their diagonal.
    # This structure is asserted, not assumed: any off-diagonal entry outside
    # the four pairs fails the check that calls this.
    pairs = ((0, 5), (1, 6), (3, 8), (4, 9))
    spec: dict[Fraction, int] = {}
    for i, j in pairs:
        for ev in (kmat[i][i] + kmat[i][j], kmat[i][i] - kmat[i][j]):
            spec[ev] = spec.get(ev, 0) + 1
    for i in (2, 7, 10):
        spec[kmat[i][i]] = spec.get(kmat[i][i], 0) + 1
    return spec


@two_cube.check(
    "the connected two-cube geometry has exactly four cross-cell pairs, each -1",
    "R2; runs/two_cube_codd_o2_2026-08-29 §1",
)
def _():
    # The whole result hangs on G_conn: the Moebius fold of the incidence
    # Gram must leave exactly the four cross-cell adjacent pairs
    # (0,5),(1,6),(3,8),(4,9), each with signed entry -1, and nothing else
    # off the diagonal. Rebuilt from oriented boundaries, not read.
    conn = _gram_conn()
    off = {(i, j): conn[i][j] for i in range(11) for j in range(11) if i != j and conn[i][j] != 0}
    want = {}
    for i, j in ((0, 5), (1, 6), (3, 8), (4, 9)):
        want[(i, j)] = -1
        want[(j, i)] = -1
    return (off == want), (
        f"G_conn rebuilt from oriented cell boundaries has off-diagonal support {sorted(off)} "
        f"with entries {sorted(set(off.values())) if off else []}; the delivery's four "
        "cross-cell pairs (0,5),(1,6),(3,8),(4,9) at -1 are exactly reproduced, so the "
        "connected geometry is four disjoint 2x2 blocks plus three isolated directions"
    )


@two_cube.check(
    "the B=6 six-channel census sums to the registry's own t_3 = 5/612",
    "R2; runs/two_cube_codd_o2_2026-08-29 §7",
)
def _():
    # The six shared-link channel coefficients are read from the certificate
    # and summed exactly. Three gates: (1) the sum is 5/612; (2) that equals
    # the registry constant T_MINUS_2 -- the two-cube connected adjacent
    # coefficient IS the all-rank hopping t_3 the corpus already carries at
    # T0 (LEAN:hopping_three) from one-cube data, now recovered on a genuine
    # face-sharing two-cube space; (3) the mechanism split: the three
    # channels visible at B=4 sum to -51/612 and the restored 6, bar6, 8
    # channels to +56/612, which is the sign reversal.
    chans = _cert()["graph"]["channel_coefficients"]
    c = {k.split(":")[1]: Fraction(v["rational"]) for k, v in chans.items()}
    total = sum(c.values())
    legacy = c["1"] + c["3"] + c["bar3"]
    restored = c["6"] + c["bar6"] + c["8"]
    t3 = Fraction(int(K.T_MINUS_2.p), int(K.T_MINUS_2.q))
    ok = (
        set(c) == {"1", "3", "bar3", "6", "bar6", "8"}
        and total == Fraction(5, 612) == t3
        and legacy == Fraction(-51, 612)
        and restored == Fraction(56, 612)
    )
    return ok, (
        f"1/12 - 1/12 - 1/12 - 1/9 - 1/9 + 16/51 = {total} = registry t_3; legacy channels "
        f"{legacy}, restored 6+bar6+8 channels {restored}: the adjoint route (+16/51) overcomes "
        "both sextets and the legacy sum, which is the operator-level sign-reversal mechanism. "
        "Second order only -- this bears on t_N, not on the fourth-order C2"
    )


@two_cube.check(
    "the B=6 six-channel census IS the Weingarten four-channel ledger, channel by channel",
    "R2; runs/two_cube_codd_o2_2026-08-29 §7.3; MASTER paper Thm. (census)",
)
def _():
    # That the six census coefficients SUM to 5/612 is weak evidence, and the
    # check above says so: six rationals reach one target in many ways, and a
    # fitted set would pass it. The statement worth making is the
    # correspondence itself -- each link-resolved coefficient is one of the
    # four Weingarten fusion weights, with two features that carry the content:
    #
    #   * the mixed family enters NEGATED, because t_N = B_N - A_N, which is
    #     the same relative sign the incidence orientation carries;
    #   * each like-family fusion weight splits EVENLY between an irrep and its
    #     conjugate -- the two orientations of the shared link weighted equally.
    #
    # The factor of two is the content, and it is not a fudge. The Weingarten
    # ledger is indexed by the FUSION channel of the shared link; the two-cube
    # certificate is indexed by the irrep the link actually CARRIES in the
    # ranked intermediate state, which distinguishes rho from bar-rho. For
    # SU(3) the like family splits as Lambda^2 F = 3bar and Sym^2 F = 6, and
    # the census finds the two orientations of each carrying exactly half the
    # fusion weight apiece.
    #
    # The weights come from K.channel_weight, i.e. from the dimension/Casimir
    # table and the order-two Weingarten values. Nothing about the two-cube
    # build enters them, so this compares two independently constructed objects
    # at six places rather than one number at one.
    #
    # Scope: N = 3, second order. The all-rank even split is a CONJECTURE whose
    # falsifier is one rank at which the split is uneven; nothing here promotes
    # it, and nothing here touches the fourth order or C2.
    def w(rho) -> Fraction:
        value = K.channel_weight(rho, 3)
        return Fraction(int(value.p), int(value.q))

    c = {
        k.split(":")[1]: Fraction(v["rational"])
        for k, v in _cert()["graph"]["channel_coefficients"].items()
    }
    predicted = {
        "1": -w("1"),
        "8": -w("Adj"),
        "3": w("Lambda2") / 2,
        "bar3": w("Lambda2") / 2,
        "6": w("Sym2") / 2,
        "bar6": w("Sym2") / 2,
    }
    # The cutoff corollary, on the same two objects: what a truncation keeping
    # only the singlet and Lambda^2 F routes projects the hopping to, and what
    # it omits. Both sides are computed twice -- from the census and from the
    # weights -- and neither is 5/612, which would double-count.
    legacy = c["1"] + c["3"] + c["bar3"]
    restored = c["6"] + c["bar6"] + c["8"]
    cutoff_ok = (
        legacy == w("Lambda2") - w("1") == Fraction(-1, 12)
        and restored == w("Sym2") - w("Adj") == Fraction(14, 153)
        and legacy + restored == Fraction(int(K.T_MINUS_2.p), int(K.T_MINUS_2.q))
    )
    # Rigidity: the labelled correspondence has no slack. Of all 6! ways to
    # attach the six census values to the six predicted slots, only the ones
    # that respect the correspondence work -- the degeneracy is exactly the
    # 2 x 2 from the two conjugate pairs, never more.
    from itertools import permutations

    slots = ("1", "8", "3", "bar3", "6", "bar6")
    matching = sum(
        1
        for perm in permutations(slots)
        if all(c[perm[i]] == predicted[slots[i]] for i in range(6))
    )
    return (c == predicted and cutoff_ok and matching == 4), (
        f"c_1 = -w_1 = {c['1']}, c_8 = -w_Adj = {c['8']}, "
        f"c_3 = c_bar3 = w_Lam/2 = {c['3']}, c_6 = c_bar6 = w_Sym/2 = {c['6']} -- six "
        "reconstructed coefficients landing on four predicted weights, with the two "
        "coincidences the correspondence requires and no others "
        f"({matching} of 720 labellings survive, exactly the 2x2 conjugate degeneracy). "
        f"The B=4 half sums to {legacy} = w_Lam - w_1 and the restored half to {restored} "
        "= w_Sym - w_Adj: the cutoff's projected hopping and the counterterm that completes "
        "it. The six delivered numbers remain rational reconstructions of finite-precision "
        "contractions; what is exact here is the identity they satisfy"
    )


@two_cube.check(
    "the B=6 connected kernel is (5/612) G_conn + diag, with the certified spectrum",
    "R2; runs/two_cube_codd_o2_2026-08-29 §7.4",
)
def _():
    # Assemble K_conn from the certificate's connected diagonal plus
    # (5/612) x the locally rebuilt G_conn off-diagonal, and verify its
    # exact spectrum {0, (-15/4)^2, (-34/9)^4, (-129/34)^4} against the
    # certificate's own connected_spectrum, multiplicities included.
    cert = _cert()
    conn = _gram_conn()
    diag = [Fraction(x) for x in cert["graph"]["connected_diagonal"]]
    coeff = Fraction(cert["graph"]["channel_exact_sum"])
    kmat = [[diag[i] if i == j else coeff * conn[i][j] for j in range(11)] for i in range(11)]
    spec = _spectrum(kmat)
    want = {Fraction(rec["value"]): rec["multiplicity"] for rec in cert["connected_spectrum"]}
    closed = {
        Fraction(0): 1,
        Fraction(-15, 4): 2,
        Fraction(-34, 9): 4,
        Fraction(-129, 34): 4,
    }
    return (spec == want == closed and coeff == Fraction(5, 612)), (
        f"exact spectrum {sorted(spec.items())} equals the certificate's connected_spectrum and "
        "the closed form {0, (-15/4)^2, (-34/9)^4, (-129/34)^4}; the pair blocks give "
        "-2317/612 -+ 5/612 = -34/9 and -129/34, the isolated faces -2295/612 = -15/4, and the "
        "shared-face direction exactly 0"
    )


@two_cube.check(
    "the B=4 comparator on the same geometry gives -1/12 with the reversed spectrum",
    "R2; runs/two_cube_codd_o2_2026-08-29, B4 note §4",
)
def _():
    # The sealed B=4 two-cube result: K_conn = -(1/12) G_conn + D_B4 with
    # D_B4 = diag(-7/4 x8 pattern, -15/4 on faces 2 and 10, 0 on the shared
    # face). Same assembly, same closed-form spectrum machinery; it must
    # give {0, (-15/4)^2, (-11/6)^4, (-5/3)^4} -- the truncated branch,
    # opposite ordering to B=6, on the identical two-cube geometry.
    conn = _gram_conn()
    d = [Fraction(-7, 4)] * 11
    d[2] = d[10] = Fraction(-15, 4)
    d[7] = Fraction(0)
    coeff = Fraction(-1, 12)
    # The B4 note's displayed decomposition puts the whole diagonal in
    # D_conn, with the coefficient acting off-diagonal only (its D entries
    # -7/4 etc. already absorb the Gram diagonal). Follow that convention.
    kmat = [[d[i] if i == j else coeff * conn[i][j] for j in range(11)] for i in range(11)]
    spec = _spectrum(kmat)
    want = {
        Fraction(0): 1,
        Fraction(-15, 4): 2,
        Fraction(-11, 6): 4,
        Fraction(-5, 3): 4,
    }
    return (spec == want), (
        f"-(1/12) G_conn + D_B4 has exact spectrum {sorted(spec.items())} = "
        "{0, (-15/4)^2, (-11/6)^4, (-5/3)^4}: cross-cell entries +1/12, the truncated-branch "
        "ordering, on the same rebuilt two-cube geometry that gives +5/612 at B=6"
    )


@two_cube.check(
    "connected first order vanishes by inclusion-exclusion, not by cancellation of numbers",
    "R2; runs/two_cube_codd_o2_2026-08-29 §3",
)
def _():
    # The delivery reports two first-order facts: PVP = I_11 on the shell, and
    # its Moebius fold is exactly zero. The first is the build's; the second
    # needs no build at all, and saying so is the point.
    #
    # If PVP is the identity then every source fold is the identity on its own
    # faces, so the Moebius transform reduces to the same index arithmetic the
    # geometry fold uses: entry (i,i) carries weight
    #     1 - [i in L] - [i in R] + [i in F],
    # and the eleven faces are covered exactly once by L or R, except the
    # shared face which is in both and restored by F. Every weight is zero, so
    # M[I_11] = 0 identically -- inclusion-exclusion on a cover, not eleven
    # numbers that happen to cancel. First order is a scalar shift of the whole
    # shell and carries no connected transport, which is why second order is
    # the leading connected term rather than a correction to a first-order one.
    fold = [
        [
            (1 if i == j else 0)
            * (
                1
                - (
                    (i in _I_L and j in _I_L)
                    + (i in _I_R and j in _I_R)
                    - (i in _I_F and j in _I_F)
                )
            )
            for j in range(11)
        ]
        for i in range(11)
    ]
    cover = [(i in _I_L) + (i in _I_R) - (i in _I_F) for i in range(11)]
    cert = _cert()["fold"]
    return (
        all(all(v == 0 for v in row) for row in fold)
        and cover == [1] * 11
        and cert["PVP"] == "I_11"
        and cert["connected_PVP"] == "0"
    ), (
        "each of the eleven faces is covered exactly once by {L, R} once the shared face is "
        f"restored by F ({cover}), so the Moebius weight of every diagonal entry of the identity "
        "is 1 - 1 = 0 and M[I_11] = 0 identically -- no arithmetic on amplitudes enters. The "
        f"delivery's own gates record PVP = {cert['PVP']} and connected PVP = "
        f"{cert['connected_PVP']}; what is re-derived here is that the SECOND of those follows "
        "from the first by counting alone. First order is a uniform shift of all eleven branches "
        "and creates no branch ambiguity"
    )


@two_cube.check(
    "every shared-link channel is separately proportional to the geometry, on all 56 pairs",
    "R2; runs/two_cube_codd_o2_2026-08-29 §7.3",
    tier=2,
)
def _():
    # The strongest architectural statement the two-cube delivery supports,
    # and the one the sum test cannot reach. The paper's separation --
    #   colour dynamics -> a coefficient, cellular geometry -> B B^dagger
    # -- is normally read off the TOTAL operator. Here it holds channel by
    # channel: each of the six link-resolved matrices is separately
    # proportional to the same incidence Gram, on every one of its nonzero
    # off-diagonal entries.
    #
    # The 56 is rebuilt here rather than read: the eleven oriented plaquettes
    # of the prism have exactly 56 ordered adjacent pairs, each sharing one
    # link with signed overlap +-1, and the certificate reports a constant
    # ratio on exactly that many entries for every channel. So the geometry
    # does not merely survive the sum of the channels; it survives each of
    # them, which is what makes t_3 a coefficient rather than a fit.
    #
    # T2: the per-channel ratios are float residuals from the sealed build.
    # What is exact here is the 56 and the channel list.
    def step(x, a):
        y = list(x)
        y[a - 1] += 1
        return tuple(y)

    rows = []
    for x, (a, b) in _FACES:
        chain: dict[tuple, int] = {}
        for link, sign in (((x, a), 1), ((step(x, a), b), 1), ((step(x, b), a), -1), ((x, b), -1)):
            chain[link] = chain.get(link, 0) + sign
        rows.append(chain)
    gram = [[sum(ri.get(k, 0) * rj.get(k, 0) for k in ri) for rj in rows] for ri in rows]
    adjacent = [gram[i][j] for i in range(11) for j in range(11) if i != j and gram[i][j] != 0]

    chans = _cert()["graph"]["channel_coefficients"]
    counts = {k.split(":")[1]: v["nonzero_ratio_count"] for k, v in chans.items()}
    worst = max(v["max_abs_residual_on_nonzero"] for v in chans.values())
    return (
        len(adjacent) == 56
        and set(abs(v) for v in adjacent) == {1}
        and set(counts) == {"1", "3", "bar3", "6", "bar6", "8"}
        and set(counts.values()) == {56}
        and worst < 1e-14
    ), (
        f"the prism has {len(adjacent)} ordered adjacent face pairs, each sharing one link with "
        "signed overlap +-1, rebuilt here from oriented cell boundaries; the certificate reports "
        f"a constant channel-to-geometry ratio on all {sorted(set(counts.values()))[0]} of them "
        f"for every one of the six channels, worst residual {worst:.1e}. So the incidence "
        "factorisation is not a property of the summed operator only -- each colour channel "
        "carries the same geometry separately, which is the paper's separation of colour "
        "dynamics from cellular geometry, measured rather than assumed"
    )


@two_cube.check(
    "the connected diagonal is orbit-constant, and only the transporting orbit moves",
    "R2; runs/two_cube_codd_o2_2026-08-29 §4, §7.4; MASTER paper §6",
)
def _():
    # Neither delivery asks what SHAPE the connected diagonal has; both print
    # eleven numbers. They are not eleven numbers. The open (3,2,2) prism has a
    # symmetry group -- generated by the cell exchange x -> 2-x, the two
    # transverse reflections and the y<->z swap, order 16 -- and the diagonal
    # is constant on its orbits, in BOTH truncations.
    #
    # The orbits are 8 + 2 + 1: the eight side faces, the two end caps, the
    # shared face. And the eight-orbit is exactly the support of the four
    # cross-cell pairs -- the faces that carry connected transport at all. So
    # the truncation moves the diagonal on precisely those eight faces and
    # nowhere else: the end caps stay at -15/4 and the shared face at 0 in both
    # B=4 and B=6, while the side value goes -7/4 -> -2317/612.
    #
    # That is the sharp form of what the cutoff does. Together with the four
    # cross-cell blocks carrying the whole off-diagonal change, the entire
    # B=4 -> B=6 difference is confined to the transporting orbit.
    #
    # It also explains the shape of the closed-geometry results next door: on
    # the cube and on the torus the faces are a SINGLE orbit, so the same
    # statement forces the diagonal to be scalar and the operator to be
    # exactly alpha I + t G. The nonuniform D here is the open boundary, not a
    # failure of the incidence form.
    import itertools

    ext = (2, 1, 1)  # the prism's vertex box is 3 x 2 x 2, so 2 x 1 x 1 cells
    index = {f: i for i, f in enumerate(_FACES)}

    def image(perm, flips, face):
        x, (a, b) = face
        moved = [0, 0, 0]
        for i in range(3):
            v = x[i]
            if flips[i]:
                v = ext[i] - v - (1 if (i + 1) in (a, b) else 0)
            moved[perm[i]] = v
        return (tuple(moved), tuple(sorted((perm[a - 1] + 1, perm[b - 1] + 1))))

    symmetries = set()
    axis_perms = [
        p
        for p in itertools.permutations(range(3))
        if tuple(ext[p.index(i)] for i in range(3)) == ext
    ]
    for perm in axis_perms:
        for flips in itertools.product((0, 1), repeat=3):
            try:
                img = tuple(index[image(perm, flips, f)] for f in _FACES)
            except KeyError:
                continue
            if sorted(img) == list(range(11)):
                symmetries.add(img)

    def raw_gram():
        def step(x, a):
            y = list(x)
            y[a - 1] += 1
            return tuple(y)

        rows = []
        for x, (a, b) in _FACES:
            chain: dict[tuple, int] = {}
            for link, s in (((x, a), 1), ((step(x, a), b), 1), ((step(x, b), a), -1), ((x, b), -1)):
                chain[link] = chain.get(link, 0) + s
            rows.append(chain)
        return [[sum(ri.get(k, 0) * rj.get(k, 0) for k in ri) for rj in rows] for ri in rows]

    gram, conn = raw_gram(), _gram_conn()
    # a symmetry of the complex preserves both Grams up to the orientation sign
    preserves = all(
        abs(m[i][j]) == abs(m[img[i]][img[j]])
        for img in symmetries
        for m in (gram, conn)
        for i in range(11)
        for j in range(11)
    )

    parent = list(range(11))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for img in symmetries:
        for i, j in enumerate(img):
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[ri] = rj
    orbits: dict[int, list[int]] = {}
    for i in range(11):
        orbits.setdefault(find(i), []).append(i)
    orbit_sets = sorted((tuple(v) for v in orbits.values()), key=len, reverse=True)

    transporting = tuple(sorted({i for pair in ((0, 5), (1, 6), (3, 8), (4, 9)) for i in pair}))
    d_b6 = [Fraction(x) for x in _cert()["graph"]["connected_diagonal"]]
    d_b4 = [Fraction(-7, 4)] * 11
    d_b4[2] = d_b4[10] = Fraction(-15, 4)
    d_b4[7] = Fraction(0)
    constant = all(len({d[i] for i in o}) == 1 for d in (d_b6, d_b4) for o in orbit_sets)
    moved = tuple(sorted(o for o in orbit_sets if d_b6[o[0]] != d_b4[o[0]]))

    return (
        len(symmetries) == 16
        and preserves
        and [len(o) for o in orbit_sets] == [8, 2, 1]
        and orbit_sets[0] == transporting
        and constant
        and moved == (transporting,)
        and d_b6[2] == d_b4[2] == Fraction(-15, 4)
        and d_b6[7] == d_b4[7] == 0
    ), (
        f"the prism's {len(symmetries)} geometric symmetries, built here from the vertex box and "
        "checked to preserve both Grams up to orientation sign, have face orbits "
        f"{[len(o) for o in orbit_sets]} -- eight sides, two end caps, one shared face -- and the "
        "connected diagonal is constant on them in BOTH truncations "
        f"(B=6: {d_b6[0]}, {d_b6[2]}, {d_b6[7]}; B=4: {d_b4[0]}, {d_b4[2]}, {d_b4[7]}). The "
        "eight-orbit is exactly the support of the four cross-cell pairs, and it is the ONLY "
        "orbit whose value changes with the cutoff: the end caps stay at -15/4 and the shared "
        "face at 0. So the whole B=4 -> B=6 difference, diagonal and off-diagonal alike, lives on "
        "the faces that carry connected transport. Where the faces are a single orbit -- the "
        "closed cube, the periodic torus -- the same statement forces the diagonal to be scalar, "
        "which is why alpha I + t G is exact there and not here"
    )


@two_cube.check(
    "B=6 retains every adjacent shared-link channel; B=4 provably cannot",
    "R2; G3; runs/two_cube_codd_o2_2026-08-29 §6.4",
)
def _():
    # The channel-exhaustion argument is pure rational algebra and is
    # re-derived here. A shell state carries 3 or bar3 on the shared link;
    # one Wilson action tensors by 3 or bar3; the products
    # 3x3 = 6 + bar3, 3xbar3 = 1 + 8 (and conjugates) exhaust
    # {1, 3, bar3, 6, bar6, 8}. The intermediate-state budget on the
    # endpoint faces is C2(rho) + 2 C2(3): for the sextet 10/3 + 8/3 = 6
    # and for the adjoint 3 + 8/3 = 17/3 -- both inside B=6, both OUTSIDE
    # B=4. So B=6 closes the adjacent one-action channel list at this
    # order, and the B=4/B=6 disagreement is a theorem about the cutoff,
    # not a numerical accident.
    c2 = {
        "1": Fraction(0),
        "3": Fraction(4, 3),
        "bar3": Fraction(4, 3),
        "6": Fraction(10, 3),
        "bar6": Fraction(10, 3),
        "8": Fraction(3),
    }
    budgets = {rho: c2[rho] + 2 * c2["3"] for rho in c2}
    in_b6 = {rho for rho, b in budgets.items() if b <= 6}
    in_b4 = {rho for rho, b in budgets.items() if b <= 4}
    cert_irreps = set(_cert()["reachable_channel_census"]["labels"])
    ok = (
        in_b6 == {"1", "3", "bar3", "6", "bar6", "8"} == cert_irreps
        and in_b4 == {"1", "3", "bar3"}
        and budgets["6"] == 6
        and budgets["8"] == Fraction(17, 3)
    )
    return ok, (
        f"endpoint budgets C2(rho) + 2*C2(3): sextet {budgets['6']}, adjoint {budgets['8']} -- "
        "both <= 6 and both > 4, so B=6 retains all six adjacent channels (matching the "
        "certificate's reachable census) while B=4 can only ever see {1, 3, bar3}: the sign "
        "reversal is forced by the cutoff, exactly as the one-cube suite found"
    )


@two_cube.check(
    "the certificate's own gates pass, target-blind, with the wrong-sign control rejected",
    "R2; runs/two_cube_codd_o2_2026-08-29 heldout_validation",
    tier=2,
)
def _():
    # T2 by nature: these are the delivered run's own numerical gates, read
    # and re-thresholded here, not re-executed (the builder needs pyclebsch
    # and sealed NPZ inputs that did not travel). Gates: every required
    # gate flag true; target-blind flag set; rational-reconstruction
    # residuals below the declared 2.14e-14; the held-out remainder scales
    # cubically (slope ~2.90) while the deliberately wrong-sign control
    # scales quadratically (slope ~2.00) and is at least 324x worse.
    cert = _cert()
    hv = cert["heldout_validation"]
    resid = max(cert["numerical_exactness_boundary"]["max_abs_errors"].values())
    ok = (
        cert["all_required_gates_pass"]
        and hv["target_blind"]
        and all(cert["heldout_validation"]["integration_gates"].values())
        and resid < 2.14e-14
        and 2.8 < hv["heldout_small_u"]["correct_error_log_log_slope"] < 3.1
        and 1.9 < hv["heldout_small_u"]["wrong_sign_error_log_log_slope"] < 2.1
        and hv["heldout_small_u"]["minimum_wrong_to_correct_error_ratio"] > 300
    )
    return ok, (
        f"all required gates pass, target_blind=true, max reconstruction residual {resid:.2e} "
        f"< 2.14e-14; held-out remainder slope "
        f"{hv['heldout_small_u']['correct_error_log_log_slope']:.4f} (cubic) vs wrong-sign "
        f"control {hv['heldout_small_u']['wrong_sign_error_log_log_slope']:.4f} (quadratic), "
        f"ratio >= {hv['heldout_small_u']['minimum_wrong_to_correct_error_ratio']:.0f}. Read "
        "from the sealed certificate; the 1,590,462-state builder was not re-run here"
    )
