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
    "the B=6 six-channel census IS the Weingarten four-channel ledger, channel by channel",
    "R2; runs/two_cube_codd_o2_2026-08-29 §7; FINAL paper Thm. 12",
)
def _():
    # The census check next door establishes that the six coefficients SUM to
    # t_3. Summing to the right number is weak evidence: six rationals have
    # many ways to reach 5/612, and a fitted set would pass it. The stronger
    # statement, and the one that makes the two-cube fold a re-derivation
    # rather than a coincidence, is that the six coefficients are the four
    # Weingarten channel weights individually:
    #
    #     c_1    = -w_1            c_8      = -w_Adj
    #     c_3    =  w_Lambda2 / 2  c_bar3   =  w_Lambda2 / 2
    #     c_6    =  w_Sym2 / 2     c_bar6   =  w_Sym2 / 2
    #
    # with w_rho = -(d_rho/N^2)/(C_F + C_rho/2) taken from the all-ranks
    # suite, where it is derived from the order-2 Weingarten values and
    # imports nothing from the corpus. The two sign conventions are not a
    # fudge: t_N = B_N - A_N, so the MIXED family (1, Adj) enters the hopping
    # negated and the LIKE family (Lambda2, Sym2) enters as it stands. That is
    # the same relative sign the incidence orientation carries.
    #
    # The factor of two is the content. The Weingarten ledger is indexed by
    # the FUSION channel of the shared link; the two-cube certificate is
    # indexed by the irrep the link actually carries in the ranked
    # intermediate state, which distinguishes rho from bar-rho. For SU(3) the
    # like family splits as Lambda2 F = 3bar and Sym2 F = 6, and the census
    # finds the two orientations of each carrying exactly half the fusion
    # weight apiece -- the equal split the isotropy of the two link
    # orientations predicts, measured on a 1,590,462-state space rather than
    # assumed.
    #
    # Scope: N = 3, second order. The all-rank statement -- that each like
    # family weight splits evenly between an irrep and its conjugate at every
    # rank -- is NOT established here; it is a conjecture whose falsifier is
    # one rank at which the split is uneven. Nothing here promotes it, and
    # nothing here touches the fourth order or C2.
    def w(channel: str) -> Fraction:
        v = K.channel_weight(channel, 3)
        return Fraction(int(v.p), int(v.q))

    predicted = {
        "1": -w("1"),
        "8": -w("Adj"),
        "3": w("Lambda2") / 2,
        "bar3": w("Lambda2") / 2,
        "6": w("Sym2") / 2,
        "bar6": w("Sym2") / 2,
    }
    chans = _cert()["graph"]["channel_coefficients"]
    measured = {k.split(":")[1]: Fraction(v["rational"]) for k, v in chans.items()}

    agree = measured == predicted
    # and the two truncations are the same truncation: B=4 keeps {1, 3, bar3},
    # the published p+q<=1 link cutoff keeps {1, 3bar}, and both land on the
    # same -1/12 because the two like-family halves reassemble.
    b4 = measured["1"] + measured["3"] + measured["bar3"]
    published_t1 = w("Lambda2") - w("1")
    same_cutoff = b4 == published_t1 == Fraction(-1, 12)
    omitted = measured["6"] + measured["bar6"] + measured["8"]
    same_completion = omitted == w("Sym2") - w("Adj") == Fraction(14, 153)

    return (agree and same_cutoff and same_completion), (
        f"all six certificate coefficients equal their Weingarten predictions {predicted}: the "
        "mixed family enters negated (t_N = B_N - A_N) and each like-family fusion weight splits "
        "evenly between the irrep and its conjugate. Two unrelated constructions therefore agree "
        f"channel by channel, not merely in the sum. The B=4 channel set sums to {b4}, exactly "
        f"the published p+q<=1 link cutoff's w_Lambda2 - w_1, and what B=4 omits is {omitted} = "
        "w_Sym2 - w_Adj = 14/153, exactly the published cutoff's completion -- so the operator-"
        "level sign reversal and the finite-rank truncation's are one statement. N = 3 and "
        "second order; the even split at every rank is a conjecture, falsified by one rank where "
        "it is uneven"
    )
