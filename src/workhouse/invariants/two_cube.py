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


@two_cube.check(
    "the retention rule is C2(rho) + 2 C2(3) <= B, and both retentions it decides are equalities",
    "MASTER edition §5.1; runs/two_cube_codd_o2_2026-08-29 §6.4",
)
def _():
    # The cutoff comparison is a WEAK inequality, and that is not a
    # convenience: both retentions this section turns on are decided by an
    # equality. Lambda^2 F = bar3 has budget exactly 4 and sits exactly on
    # the B = 4 cutoff; the sextet has budget exactly 6 and sits exactly on
    # the B = 6 one. Under a strict rule B = 4 would reach {1} alone and
    # B = 6 would lose the sextet, contradicting both delivered censuses --
    # so the DELIVERIES fix the convention, which is exactly why the budget
    # arithmetic is not an independent confirmation of either census. That
    # last clause is the point of the check: it bounds what the budgets prove.
    c2 = {
        "1": Fraction(0),
        "3": Fraction(4, 3),
        "bar3": Fraction(4, 3),
        "6": Fraction(10, 3),
        "bar6": Fraction(10, 3),
        "8": Fraction(3),
    }
    budget = {rho: c2[rho] + 2 * c2["3"] for rho in c2}
    weak = {b: {rho for rho, v in budget.items() if v <= b} for b in (4, 6)}
    strict = {b: {rho for rho, v in budget.items() if v < b} for b in (4, 6)}
    delivered = {4: {"1", "3", "bar3"}, 6: {"1", "3", "bar3", "6", "bar6", "8"}}
    ok = (
        weak == delivered
        and budget["bar3"] == 4
        and budget["6"] == 6
        and strict[4] == {"1"}
        and strict[6] == {"1", "3", "bar3", "8"}
        and strict != delivered
    )
    return ok, (
        f"budgets C2(rho) + 2 C2(3) = { {k: str(v) for k, v in budget.items()} }; the weak rule "
        f"reproduces both delivered censuses exactly, while the strict rule would give "
        f"{sorted(strict[4])} at B = 4 and drop the sextets at B = 6. Both retentions the "
        "section uses sit ON the cutoff (bar3 at 4, the sextet at 6), so the convention is "
        "fixed by the deliveries and the budget arithmetic corroborates rather than confirms"
    )


@two_cube.check(
    "connected first order vanishes by inclusion-exclusion, not by cancellation of numbers",
    "MASTER edition §5; runs/two_cube_codd_o2_2026-08-29 §5",
)
def _():
    # On the shell P V P = I_11, so first order is nonzero but scalar. Its
    # connected fold vanishes identically -- and by COUNTING, not by
    # arithmetic cancellation: each of the eleven faces is covered exactly
    # once by {L, R} once the shared face is restored by F, so the Moebius
    # weight applied to the identity is 1 - 1 = 0 on every index. That
    # distinction is what makes second order the leading connected term
    # rather than a correction to a first-order one, so it is worth
    # separating from the numerical fold.
    weights = {}
    for i in range(11):
        weights[i] = (i in _I_L) + (i in _I_R) - (i in _I_F)
    covered_once = set(weights.values()) == {1}
    fold_of_identity = [1 - weights[i] for i in range(11)]
    # and the same on the off-diagonal: the identity has none, so the fold is
    # exactly the diagonal statement above
    ok = covered_once and all(v == 0 for v in fold_of_identity)
    return ok, (
        f"Moebius weight (i in L) + (i in R) - (i in F) is {sorted(set(weights.values()))} on "
        "every one of the eleven faces -- the shared face 7 is in both cells and restored once "
        "by F, the other ten in exactly one -- so folding the identity gives 1 - 1 = 0 index by "
        "index. First order is scalar on the shell and its connected part vanishes by cover "
        "counting; second order is therefore the leading connected term"
    )


@two_cube.check(
    "the connected diagonal is orbit-constant, and only the transporting orbit moves",
    "MASTER edition §5.2; runs/two_cube_codd_o2_2026-08-29 §7.4",
)
def _():
    # D is treated as an eleven-number remainder in both deliveries. It is
    # not eleven numbers: the open prism has a symmetry group of order 16
    # (cell exchange, two transverse reflections, the y <-> z swap) whose
    # orbits on the faces are 8 + 2 + 1, and D is constant on them. The
    # eight-element orbit is exactly the support of the four cross-cell
    # pairs, and it is the ONLY orbit whose value differs between the two
    # truncations -- so the whole B = 4 -> B = 6 difference is confined to
    # the faces that carry connected transport. That is the architecture
    # measured rather than assumed.
    sides = tuple(i for i in range(11) if i not in (2, 7, 10))
    caps, shared = (2, 10), (7,)
    d6 = [Fraction(x) for x in _cert()["graph"]["connected_diagonal"]]
    d4 = [
        Fraction(-15, 4) if i in caps else Fraction(0) if i in shared else Fraction(-7, 4)
        for i in range(11)
    ]
    transporting = {i for pair in ((0, 5), (1, 6), (3, 8), (4, 9)) for i in pair}
    orbits = {"sides": sides, "caps": caps, "shared": shared}
    const = {
        name: (len({d6[i] for i in idx}) == 1 and len({d4[i] for i in idx}) == 1)
        for name, idx in orbits.items()
    }
    moved = {name: d6[idx[0]] != d4[idx[0]] for name, idx in orbits.items()}
    ok = (
        all(const.values())
        and set(sides) == transporting
        and moved == {"sides": True, "caps": False, "shared": False}
        and d6[0] == Fraction(-2317, 612)
        and d4[0] == Fraction(-7, 4)
        and d6[2] == d4[2] == Fraction(-15, 4)
        and d6[7] == d4[7] == 0
    )
    return ok, (
        f"orbits 8 + 2 + 1: D is constant on each at both truncations {const}. The eight side "
        f"faces are exactly the support of the four cross-cell pairs, and only their value moves "
        f"({d4[0]} -> {d6[0]}); the end caps stay -15/4 and the shared face 0 at both B = 4 and "
        "B = 6. With the four cross-cell blocks carrying the whole off-diagonal change, the "
        "entire B=4 -> B=6 difference lives on the faces that carry connected transport -- and "
        "where the faces form a SINGLE orbit (closed cube, periodic torus) the same argument "
        "forces D scalar, so the prism's three orbits are its boundary, not a defect"
    )


@two_cube.check(
    "the B=6 six-channel census IS the Weingarten four-channel ledger, channel by channel",
    "MASTER edition Reported result (the census is the Weingarten ledger)",
)
def _():
    # The registered sum check is weak evidence on its own: six rationals
    # reach one target in many ways and a fitted set would pass it. The
    # stronger statement is the correspondence itself -- c_1 = -w_1,
    # c_8 = -w_Adj, and each like-family weight split EVENLY between an
    # irrep and its conjugate, c_3 = c_bar3 = w_{Lambda^2 F}/2 and
    # c_6 = c_bar6 = w_{Sym^2 F}/2. Four predicted numbers, six delivered
    # ones, and the two coincidences the correspondence requires. Still
    # conditional on the delivery's rational reconstructions, which is why
    # the paper labels it reported and not proved.
    chans = _cert()["graph"]["channel_coefficients"]
    c = {k.split(":")[1]: Fraction(v["rational"]) for k, v in chans.items()}

    def _w(channel):
        # the registry's own resolvent weight, so this is a JOIN against
        # constants.py and not a second local derivation of the same number
        r = K.channel_weight(channel, 3)
        return Fraction(int(r.p), int(r.q))

    w = {"1": _w("1"), "8": _w("Adj"), "3": _w("Lambda2"), "6": _w("Sym2")}
    ok = (
        c["1"] == -w["1"]
        and c["8"] == -w["8"]
        and c["3"] == c["bar3"] == w["3"] / 2
        and c["6"] == c["bar6"] == w["6"] / 2
        and w["1"] == Fraction(-1, 12)
        and w["8"] == Fraction(-16, 51)
        and w["3"] == Fraction(-1, 6)
        and w["6"] == Fraction(-2, 9)
    )
    return ok, (
        f"Weingarten weights at N = 3 from d_rho/N^2 over C_F + C_rho/2: w_1 = {w['1']}, "
        f"w_Adj = {w['8']}, w_Lambda2 = {w['3']}, w_Sym2 = {w['6']}. The delivered census "
        f"matches channel by channel: c_1 = {c['1']} = -w_1, c_8 = {c['8']} = -w_Adj, "
        f"c_3 = c_bar3 = {c['3']} = w_Lambda2/2, c_6 = c_bar6 = {c['6']} = w_Sym2/2 -- six "
        "reconstructed rationals landing on four predicted ones with the two conjugate "
        "coincidences the correspondence requires, which is stronger than the one-sum test and "
        "still conditional on the reconstruction"
    )


@two_cube.check(
    "every shared-link channel is separately proportional to the geometry, on all 56 pairs",
    "MASTER edition §5; runs/two_cube_codd_o2_2026-08-29 §7",
    tier=2,
)
def _():
    # The paper's central architecture -- colour separates from geometry --
    # measured rather than assumed. The delivery resolves the connected
    # operator into six link-irrep matrices, and EACH ONE is a scalar
    # multiple of the same incidence Gram: the ratio (channel matrix entry) /
    # (G_conn entry) is constant across all 56 adjacent ordered pairs, to a
    # residual the certificate records per channel. If colour and geometry
    # did not separate, six matrices would be six different shapes summing to
    # one; instead they are six numbers times one shape. T2: the residuals
    # are floats from the delivery's own reconstruction.
    chans = _cert()["graph"]["channel_coefficients"]
    counts = {k.split(":")[1]: v["nonzero_ratio_count"] for k, v in chans.items()}
    resid = {k.split(":")[1]: v["max_abs_residual_on_nonzero"] for k, v in chans.items()}
    worst = max(resid.values())
    ok = (
        set(counts) == {"1", "3", "bar3", "6", "bar6", "8"}
        and all(n == 56 for n in counts.values())
        and worst < 2.2e-15
    )
    pairs = sorted(set(counts.values()))
    return ok, (
        f"all six channels report a constant channel-to-geometry ratio on {pairs} "
        f"nonzero adjacent ordered pairs each, worst residual {worst:.2e} < 2.2e-15. Colour and "
        "geometry separate channel by channel, not merely in the sum -- six numbers times one "
        "incidence Gram, which is what the shared-link factorisation claims and what a fitted "
        "ledger would not reproduce"
    )


@two_cube.check(
    "the one-cube shell is A1 + T1 + E, and its flat level is the S^2 fundamental class",
    "MASTER edition §5.3 (one-cube shell)",
)
def _():
    # Both deliveries ASSERT the cubic labels and neither builds the symmetry
    # matrices. They are integer linear algebra and take no delivered input,
    # so they are derived here. The six faces of a cube are a closed surface:
    # ker d_2 is one-dimensional, spanned by the sum of all six -- the
    # fundamental class, b_2(S^2) = 1, which is the torus theorem on a
    # complex with no three-cells. G = d_2^T d_2 then has spectrum
    # {0, 4, 4, 4, 6, 6}, the antisymmetric combinations b_{+i} - b_{-i}
    # carrying the defining representation and the symmetric ones the
    # permutation representation of the three unordered axes. With the
    # charge-odd inversion P b_{+i} = -b_{-i} the shell is
    # A_1^{--} + T_1^{+-} + E^{--}, and alpha I + t G has levels alpha,
    # alpha + 4t, alpha + 6t. The A_1 level sits AT the scalar for every t:
    # no truncation, no channel, no disputed coefficient can move it.
    #
    # Faces in the order (+x, -x, +y, -y, +z, -z), outward oriented; edges
    # are the twelve cube edges, each shared by exactly two faces with
    # opposite induced orientation.
    axes = ((0, 1), (2, 3), (4, 5))
    edges = []
    for a in range(3):
        for b in range(3):
            if a == b:
                continue
            for i in axes[a]:
                for j in axes[b]:
                    if (j, i) not in [(x, y) for x, y in edges]:
                        edges.append((i, j))
    edges = sorted({tuple(sorted(e)) for e in edges})
    d2 = [[0] * 6 for _ in edges]
    for r, (i, j) in enumerate(edges):
        d2[r][i], d2[r][j] = 1, -1
    gram = [
        [sum(d2[r][i] * d2[r][j] for r in range(len(edges))) for j in range(6)] for i in range(6)
    ]
    # exact spectrum by the symmetry-adapted basis, not by a solver
    anti = [[1 if k == i else -1 if k == j else 0 for k in range(6)] for i, j in axes]
    symm = [[1 if k in (i, j) else 0 for k in range(6)] for i, j in axes]

    def _apply(vec):
        return [sum(gram[i][j] * vec[j] for j in range(6)) for i in range(6)]

    def _eig(vec):
        img = _apply(vec)
        nz = next(i for i, v in enumerate(vec) if v != 0)
        lam = Fraction(img[nz], vec[nz])
        return lam if all(Fraction(img[i]) == lam * vec[i] for i in range(6)) else None

    anti_eigs = {_eig(v) for v in anti}
    total = [1] * 6
    flat = _eig(total)
    # the symmetric sector splits as A_1 (the total) + E; take two E vectors
    e_vecs = [
        [a - b for a, b in zip(symm[0], symm[1], strict=True)],
        [a - b for a, b in zip(symm[1], symm[2], strict=True)],
    ]
    e_eigs = {_eig(v) for v in e_vecs}
    ok = (
        len(edges) == 12
        and anti_eigs == {Fraction(4)}
        and flat == Fraction(0)
        and e_eigs == {Fraction(6)}
    )
    return ok, (
        f"G = d_2^T d_2 on the closed cube surface, built from {len(edges)} oriented edges: the "
        "three antisymmetric combinations b_{+i} - b_{-i} carry the defining representation with "
        f"eigenvalue {anti_eigs.pop()}, the two symmetric traceless ones give {e_eigs.pop()}, and "
        "the sum of all six faces -- the S^2 fundamental class -- has eigenvalue 0. So the shell "
        "is A_1^{--} + T_1^{+-} + E^{--} with G-spectrum {0, 4, 4, 4, 6, 6} and alpha I + t G has "
        "levels alpha, alpha + 4t, alpha + 6t: the A_1 level sits at the scalar for EVERY t, "
        "which is why no truncation or disputed coefficient anywhere can move it"
    )
