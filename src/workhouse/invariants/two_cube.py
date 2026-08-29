"""The two-cube kernel: the first adjacent-hopping result not read off one cell.

Every other cube result in this repository lives on a single cube, where the
adjacent-face coefficient is inferred from one cell plus a graph ansatz. This
suite checks a release that does it on a genuine face-sharing two-cube prism —
8,361 states at B4, 1,590,462 at B6 — with the connected part obtained by
literal operator-level Moebius subtraction rather than a fitted scalar.

Nothing here re-executes the builder: it needs pyclebsch and NPZ artifacts that
did not travel with the documents. What is checked is the sealed bytes and the
arithmetic, which is where the interesting content turned out to be.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction

from sympy import Matrix, Rational, diag, zeros

from .. import constants as K
from .. import payloads as P
from ._core import ROOT, _suite

# ==========================================================================
two_cube = _suite("two-cube connected kernel (B4 and B6)")

_RELEASE = ROOT / "runs" / "two_cube_b4_b6_codd_o2_2026-08-29"

#: The four connected cross-cell pairs, from the release's geometry section.
#: G_conn has zero diagonal (each face's own cube subtracts it) and -1 here.
_PAIRS = ((0, 5), (1, 6), (3, 8), (4, 9))

#: The six shared-link channel coefficients recovered target-blind at B6.
_CHANNELS = {
    "1": Fraction(1, 12),
    "3": Fraction(-1, 12),
    "3bar": Fraction(-1, 12),
    "6": Fraction(-1, 9),
    "6bar": Fraction(-1, 9),
    "8": Fraction(16, 51),
}


def _g_conn():
    g = zeros(11)
    for a, b in _PAIRS:
        g[a, b] = g[b, a] = -1
    return g


@two_cube.check(
    "the two-cube six-channel census IS this registry's t_N = B_N - A_N",
    "R2; runs/two_cube_b4_b6_codd_o2_2026-08-29 §7; notes UPLOADS_2026-08-29a",
)
def _():
    # This is the result worth having from the release, and it is not the
    # fraction 5/612 -- the registry already carries that. It is that a
    # two-cube contraction, told nothing about the target, resolves channel by
    # channel into the rank law constants.py states abstractly.
    #
    # The all-ranks suite carries four weights with conjugates merged:
    # w_1 = -1/12, w_8 = -16/51, w_3bar = -1/6, w_6 = -2/9, with
    # A_N = w_1 + w_Adj the mixed-orientation family, B_N = w_Lambda2 + w_Sym2
    # the like-orientation family, and t_N = B_N - A_N.
    #
    # The two-cube release reports SIX coefficients, conjugates resolved and
    # the charge-odd projection already applied to each. They line up exactly:
    #
    #     3 + 3bar = -1/6  = w_3bar         1 = +1/12  = -w_1
    #     6 + 6bar = -2/9  = w_6            8 = +16/51 = -w_8
    #
    # so the like-orientation channels sum to B_3, the mixed-orientation ones
    # to MINUS A_3, and the census total is B_3 - A_3 = hopping(3). The minus
    # sign that the rank law writes as a subtraction between two families is,
    # on an actual two-cube Hilbert space, the sign the charge-odd projection
    # puts on the mixed-orientation channels. An abstract identity turns out
    # to be an operational one.
    #
    # Neither side of C2 is touched: this is second-order hopping, not C_shp.
    like = _CHANNELS["3"] + _CHANNELS["3bar"] + _CHANNELS["6"] + _CHANNELS["6bar"]
    mixed = _CHANNELS["1"] + _CHANNELS["8"]

    w_1, w_8 = Fraction(-1, 12), Fraction(-16, 51)
    w_3bar, w_6 = Fraction(-1, 6), Fraction(-2, 9)
    a3, b3 = w_1 + w_8, w_3bar + w_6

    conjugates_merge = (
        _CHANNELS["3"] + _CHANNELS["3bar"] == w_3bar
        and _CHANNELS["6"] + _CHANNELS["6bar"] == w_6
        and _CHANNELS["1"] == -w_1
        and _CHANNELS["8"] == -w_8
    )
    rank_law = like == b3 and mixed == -a3
    total = sum(_CHANNELS.values(), Fraction(0))

    return (
        conjugates_merge and rank_law and total == P.as_fraction(K.hopping(3)),
        f"the six target-blind two-cube channels resolve into the registry's four: "
        f"3 + 3bar = {like - _CHANNELS['6'] - _CHANNELS['6bar']} = w_3bar, "
        f"6 + 6bar = {_CHANNELS['6'] + _CHANNELS['6bar']} = w_6, 1 = {_CHANNELS['1']} = -w_1, "
        f"8 = {_CHANNELS['8']} = -w_8. So the like-orientation channels sum to B_3 = {b3} and "
        f"the mixed-orientation ones to -A_3 = {-a3}, making the census B_3 - A_3 = {total} = "
        "hopping(3). The subtraction the rank law writes between two families is the sign the "
        "charge-odd projection puts on the mixed channels -- an abstract identity shown to be "
        "an operational one on a real two-cube space. Second-order hopping; C2 untouched",
    )


@two_cube.check(
    "the connected kernel is t_3 G_conn plus a diagonal, at B6 and B4, with the stated spectra",
    "R2; runs/two_cube_b4_b6_codd_o2_2026-08-29 §6",
)
def _():
    # The release's central matrices, checked against a G_conn built here from
    # the geometry alone rather than read from the release. If the printed
    # kernel really is t_3 * G_conn + D, then subtracting the registry's own
    # hopping(3) times that geometry must leave something exactly diagonal --
    # and the leftover must be the document's D, to the integer.
    #
    # The B4 kernel is the same statement at the truncated coefficient, and
    # the two spectra are what make the sign reversal visible as an ordering:
    # at B6 the shared-face direction sits at zero and the pair blocks split
    # downward; at B4 the same geometry gives a different fourfold pair.
    b6_rows = [
        [-2317, 0, 0, 0, 0, -5, 0, 0, 0, 0, 0],
        [0, -2317, 0, 0, 0, 0, -5, 0, 0, 0, 0],
        [0, 0, -2295, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -2317, 0, 0, 0, 0, -5, 0, 0],
        [0, 0, 0, 0, -2317, 0, 0, 0, 0, -5, 0],
        [-5, 0, 0, 0, 0, -2317, 0, 0, 0, 0, 0],
        [0, -5, 0, 0, 0, 0, -2317, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -5, 0, 0, 0, 0, -2317, 0, 0],
        [0, 0, 0, 0, -5, 0, 0, 0, 0, -2317, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2295],
    ]
    g = _g_conn()
    t3 = P.as_fraction(K.hopping(3))

    k6 = Matrix(11, 11, lambda i, j: Rational(b6_rows[i][j], 612))
    residual = k6 - Rational(t3.numerator, t3.denominator) * g
    is_diagonal = all(residual[i, j] == 0 for i in range(11) for j in range(11) if i != j)
    d_b6 = [int(residual[i, i] * 612) for i in range(11)]
    stated_d = [-2317, -2317, -2295, -2317, -2317, -2317, -2317, 0, -2317, -2317, -2295]

    seven = [Rational(-7, 4)] * 2 + [Rational(-15, 4)] + [Rational(-7, 4)] * 4
    k4 = Rational(-1, 12) * g + diag(
        *(seven + [Rational(0)] + [Rational(-7, 4)] * 2 + [Rational(-15, 4)])
    )

    spec6 = k6.eigenvals()
    spec4 = k4.eigenvals()
    want6 = {Rational(0): 1, Rational(-15, 4): 2, Rational(-34, 9): 4, Rational(-129, 34): 4}
    want4 = {Rational(0): 1, Rational(-15, 4): 2, Rational(-11, 6): 4, Rational(-5, 3): 4}

    return (
        is_diagonal and d_b6 == stated_d and spec6 == want6 and spec4 == want4,
        f"subtracting hopping(3) = {t3} times a geometry-only G_conn from the printed B6 kernel "
        f"leaves an exactly diagonal residual, and that residual is the release's D_B6 to the "
        f"integer ({stated_d[0]}/612 on the bulk, 0 on the shared face). The spectra are "
        "{0, (-15/4)^2, (-34/9)^4, (-129/34)^4} at B6 and {0, (-15/4)^2, (-11/6)^4, (-5/3)^4} at "
        "B4, both exact. The B6 note prints the fourfold as -578/153, which is -34/9 unreduced, "
        "not a discrepancy",
    )


@two_cube.check(
    "FINDING: the two-cube restored channels reproduce the bridge's 14/153 completion",
    "R2; runs/two_cube_b4_b6_codd_o2_2026-08-29 §10; runs/cbb_finite_n_bridge_2026-08-28",
)
def _():
    # The bridge registered w_6 - w_8 = 14/153 as the exact completion the
    # p+q<=1 cutoff omits, derived from four merged channel weights on a
    # one-cube second-order Schur complement. That was recorded before any
    # two-cube calculation existed.
    #
    # The two-cube release reaches the same number from the other side: its
    # restored 6, 6bar and 8 channels, resolved separately on a 1,590,462-state
    # face-sharing Hilbert space, sum to 6 + 6bar + 8 = 14/153. The legacy
    # channels sum to -1/12, which is the B4 coefficient, and the two add to
    # 5/612.
    #
    # So the completion is not an artifact of merging conjugates or of the
    # one-cube Schur route. Two constructions that share no geometry agree on
    # which channels are missing and by how much.
    legacy = _CHANNELS["1"] + _CHANNELS["3"] + _CHANNELS["3bar"]
    restored = _CHANNELS["6"] + _CHANNELS["6bar"] + _CHANNELS["8"]
    bridge_completion = Fraction(-2, 9) - Fraction(-16, 51)  # w_6 - w_8, as registered

    return (
        legacy == Fraction(-1, 12)
        and restored == bridge_completion
        and legacy + restored == P.as_fraction(K.hopping(3)),
        f"the two-cube legacy channels 1, 3, 3bar sum to {legacy} = {legacy * 612}/612, the B4 "
        f"coefficient; the restored 6, 6bar, 8 sum to {restored} = {restored * 612}/612, which is "
        f"exactly the w_6 - w_8 = {bridge_completion} completion registered from the one-cube "
        f"bridge before any two-cube calculation existed. Together {legacy + restored}. Two "
        "constructions sharing no geometry agree on which channels are missing and by how much",
    )


@two_cube.check(
    "the pinned two-cube bytes are the sealed release bytes, manifest root included",
    "R2; runs/two_cube_b4_b6_codd_o2_2026-08-29; notes UPLOADS_2026-08-29a",
)
def _():
    # The release's own discipline is a detached manifest published last: it
    # seals every other byte and deliberately omits its own hash, so the root
    # has to be carried beside it or recomputed. This check does the
    # recomputation, and confirms the documents pinned here are the ones the
    # manifest describes rather than a later edit of them.
    manifest_path = _RELEASE / "two_cube_b6_codd_o2_connected_kernel_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    recorded = {record["name"]: record["sha256"] for record in manifest["files"]}

    checked = {}
    for name in (
        "two_cube_b6_codd_o2_connected_kernel_certificate.json",
        "TWO_CUBE_B6_CODD_O2_CONNECTED_KERNEL_2026-08-29.md",
        "TWO_CUBE_B4_CODD_O2_CONNECTED_KERNEL_2026-08-29.md",
    ):
        checked[name] = hashlib.sha256((_RELEASE / name).read_bytes()).hexdigest() == recorded[name]

    root = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    stated_root = "021558ce5bea60e43f757d76c1b8122f15f355c1e5174304f440cce5d98d422b"

    return (
        all(checked.values()) and root == stated_root and not manifest["self_hash_included"],
        f"all {len(checked)} pinned files hash to the value the detached manifest records for "
        f"them, and the manifest itself hashes to {root[:12]}..., the root the theorem document "
        "states. It declares self_hash_included false, which is why the root is recomputed here "
        "rather than read: a manifest that sealed its own hash could not be verified this way",
    )
