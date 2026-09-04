"""The corner cluster from a third implementation, and the historical pipeline's own ledger.

Closes the last untried route on G3 (ADR 0024). Two instruments, neither of
which existed before 2026-09-04:

* ``workhouse.loopcalc`` -- a Wilson-loop calculus written from scratch,
  sharing no primitive with the pinned engine (Fierz ``H0`` by port
  rewiring, Weingarten by Gram pseudoinverse, the resolvent by per-link irrep
  projectors). It reproduces every registered second- and fourth-order
  constant the two earlier implementations agree on, then the corner
  cumulant, then the cube completion -- each in seconds.
* ``workhouse.stage3i`` -- the historical Y4 pipeline's Stage-3I word
  ledger, pinned in the corpus and read by nothing until now, reassembled
  by Stage 3J's own rule into the 189 records and regrouped by the set of
  plaquettes each word touches: the historical kernel's cluster cumulants,
  in its own basis.

What they establish, said plainly: the historical kernel and the cluster
assembly agree, to the digit, on every cluster of the rotation record --
pair, fourteen chains, two fans, two corners -- and differ in one term, the
adjacent-face cube completion, where the historical ledger holds 8 of the 24
insertion orderings. And the run that assembled the rotation element read
it in the conjugate orientation of the (0,2) face; in the kernel's own
basis the assembled ``C_shp`` is the historical value plus ``25/1024``.
Nothing here promotes a side of C2 in the ledger; the decision that follows
is recorded in ADR 0024 and left to the maintainer.
"""

from __future__ import annotations

import json
from fractions import Fraction

from sympy import Rational, simplify

from .. import cellular as CELL
from .. import constants as K
from .. import kernel_orbits as KO
from .. import loopcalc as LC
from .. import stage3i as S3
from ..payloads import kernel_records
from ._core import ROOT, _suite

third = _suite("the third implementation and the historical ledger (G3, C2)")

_RUN = "runs/g3_corner_third_implementation_2026-09-04"
_PAIR_RUN = "runs/g3_shared_link_pair_2026-09-02"
_CITE = "C2; G3; G14; " + _RUN + "; " + _PAIR_RUN + "; ADR 0024; ADR 0021"

_P = ((0, 1), (0, 0, 0))
_Q20 = ((2, 0), (0, 0, 0))
_Q02 = ((0, 2), (0, 0, 0))
_CORNER_X = ((1, 2), (1, 0, 0))
_OTHERS_PERP = [((0, 1), (0, 0, 1)), ((0, 2), (0, 1, 0)), ((1, 2), (0, 0, 0)), ((1, 2), (1, 0, 0))]
_OTHERS_NORM = [((0, 2), (0, 0, 0)), ((0, 2), (0, 1, 0)), ((1, 2), (0, 0, 0)), ((1, 2), (1, 0, 0))]

_CORNER_ODD = Fraction(-2580244782961, 398756546697600)
_CORNER_EVEN = Fraction(-56022878647, 4153714028100)
_SINGLE = Fraction(-385, 1997568)
_FAN = Fraction(135671797, 105250609440)
_CUBE_ADJ = Fraction(-53, 768)
_CUBE_HIST = Fraction(-31, 1536)

_CORNER_THIRD = (
    "the corner cluster's cumulant from a third implementation, independent of the engine "
    "in every primitive"
)
_LEDGER_REASSEMBLES = (
    "the historical pipeline's own word ledger, pinned in the corpus, reassembles to the 189 "
    "records"
)
_CUBE_THIRD = (
    "the cube completion from the third engine: -5/48 between opposite faces, -53/768 between "
    "adjacent ones"
)
_CUBE_MULTILOOP = (
    "the adjacent-face cube completion is -106/(N(N^2-1)^3): the primitive -88 plus ten multi-loop "
    "histories at -18"
)
_LEDGER_FINDING = (
    "FINDING: the historical rotation record holds every cluster the assembly has, to the digit, "
    "except 16 of the 24 cube orderings"
)
_BASIS_FINDING = (
    "FINDING: the run's rotation element is in the conjugate basis; in the kernel's own basis "
    "rho = -RHO_CLUSTER and rho_historical - rho = 25/512, the cube term alone"
)


def _certificate() -> dict:
    return json.loads((ROOT / _RUN / "certificate.json").read_text(encoding="utf-8"))


def _pair_certificate() -> dict:
    return json.loads(
        (ROOT / _PAIR_RUN / "shared_link_pair_certificate.json").read_text(encoding="utf-8")
    )


def _rat(x) -> Fraction:
    return Fraction(x.p, x.q)


@third.check(
    "the third engine reproduces the second-order constants and u = X_QUANTUM on three chain types",
    _CITE + "; ADR 0020",
)
def _():
    # The validation ladder every implementation here has had to climb, run
    # live: the four second-order constants from the primitives, then the
    # two-hop weight on the coplanar, bent and zigzag chains with the
    # incidence signs of THM_FLUX Prop. 2, then the C-even chain amplitude.
    single = LC.Cluster([_P])
    pair = LC.Cluster([_P, ((0, 1), (1, 0, 0))])
    perp = LC.Cluster([_P, _Q02])
    h2s, _ = single.second_order()
    h2, _ = pair.second_order()
    h2p, _ = perp.second_order()
    second = (
        LC.codd(h2, 0, 1),
        LC.codd(h2p, 0, 1),
        LC.ceven(h2, 0, 1),
        LC.codd(h2, 0, 0) - LC.codd(h2s, 0, 0) + Fraction(3, 4),
    )
    chains = {
        "coplanar-coplanar": ([_P, ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0))], 1),
        "coplanar-perpendicular": ([_P, ((0, 1), (1, 0, 0)), ((1, 2), (2, 0, 0))], -1),
        "perpendicular-perpendicular": ([_P, _Q02, ((0, 1), (0, 0, 1))], -1),
    }
    u = _rat(K.X_QUANTUM)
    got = {}
    for name, (faces, sign) in chains.items():
        w = LC.cumulant(faces, 1)
        got[name] = (LC.block_odd(w), LC.block_even(w), sign)
    ok = second == (
        Fraction(-5, 612),
        Fraction(5, 612),
        Fraction(-11, 306),
        Fraction(-11, 306),
    ) and all(
        odd == sign * u and even == Fraction(948253471, 40327601932800)
        for odd, even, sign in got.values()
    )
    return ok, (
        f"second order from the primitives: coplanar hop {second[0]}, perpendicular hop "
        f"{second[1]} "
        f"(the (0,2) traversal), C-even hop {second[2]}, leakage {second[3]}; chain amplitudes "
        + ", ".join(f"{n}: {o} (= {s:+d} u)" for n, (o, _e, s) in got.items())
        + f", C-even {Fraction(948253471, 40327601932800)} on all three. Third engine, no engine "
        "primitive, seconds"
    )


@third.check(_CORNER_THIRD, _CITE)
def _():
    # The route as the ledger wrote it: W(P,Q,X) - W(P,Q) on the P <- Q block
    # for P = xy(0), Q = zx(0) in the run's (2,0) traversal, X = yz(1,0,0),
    # "without reusing chain_amplitude.py, chain_cluster.py or
    # haar_epsilon.py". Fierz H0 by port rewiring, Weingarten by Gram
    # pseudoinverse, the resolvent by per-link projectors; the E0 components
    # the resolvent drops were verified to lie in the plaquette span
    # (runs/.../console.log of the scratch verification is summarised in the
    # run README). Same four W entries as the run, to the digit.
    w = LC.cumulant([_P, _CORNER_X, _Q20], 1)
    cert = _pair_certificate()["pairs"]["perpendicular"]["dressings"]["((1, 2), (1, 0, 0))"]
    stage = json.loads(
        (ROOT / _PAIR_RUN / "pair_route_perpendicular_all.json").read_text(encoding="utf-8")
    )
    run_w = {k: Fraction(v) for k, v in stage["dressings"]["((1, 2), (1, 0, 0))"]["W"].items()}
    ok = (
        LC.block_odd(w) == _CORNER_ODD == Fraction(cert["codd"])
        and LC.block_even(w) == _CORNER_EVEN == Fraction(cert["ceven"])
        and {str(k): v for k, v in w.items()} == run_w
    )
    return (
        ok,
        (
            f"corner face (1,2) at (1,0,0) with the perpendicular pair: third implementation C-odd "
            f"{LC.block_odd(w)}, C-even {LC.block_even(w)}, all four orientation entries "
            f"{ {str(k): str(v) for k, v in w.items()} } identical to the run's. Three "
            "implementations now, the third sharing no primitive with the first two"
        ),
        {"PAIR_CORNER_DRESSING_EVEN": _CORNER_EVEN},
    )


@third.check(
    "the third engine reproduces every dressing class of the three shared-link pairs, and the "
    "far gate",
    _CITE,
    rests_on=(_CORNER_THIRD,),
)
def _():
    # The pinned run certificate holds all 58 three-cluster cumulants (18 for
    # the perpendicular pair, 20 each for the coplanar and stacked pairs) in
    # the kernel's (0,2) basis; the two non-corner classes of the
    # perpendicular pair are recomputed live here. Against the 2026-09-02
    # certificate the C-even values are identical and every C-odd value of
    # the perpendicular pair is the negative, which is the (0,2)-vs-(2,0)
    # traversal of Q and nothing else; the coplanar pair's agree sign included.
    cert = _certificate()
    old = _pair_certificate()["pairs"]
    live = {
        "single": LC.block_odd(LC.cumulant([_P, ((0, 1), (1, 0, 0)), _Q02], 1)),
        "fan": LC.block_odd(LC.cumulant([_P, ((0, 1), (0, -1, 0)), _Q02], 1)),
    }
    perp_new = {
        k: (Fraction(v["codd"]), Fraction(v["ceven"]))
        for k, v in cert["pairs"]["perpendicular"]["dressings"].items()
    }
    perp_old = {
        k: (Fraction(v["codd"]), Fraction(v["ceven"]))
        for k, v in old["perpendicular"]["dressings"].items()
    }
    cop_new = {
        k: (Fraction(v["codd"]), Fraction(v["ceven"]))
        for k, v in cert["pairs"]["coplanar"]["dressings"].items()
    }
    cop_old = {
        k: (Fraction(v["codd"]), Fraction(v["ceven"]))
        for k, v in old["coplanar"]["dressings"].items()
    }
    norm_new = {k: Fraction(v["codd"]) for k, v in cert["pairs"]["normal"]["dressings"].items()}
    u = _rat(K.X_QUANTUM)
    classes = sorted(v[0] for v in perp_new.values())
    ok = (
        live["single"] == -_SINGLE
        and live["fan"] == -_FAN
        and set(perp_new) == set(perp_old)
        and all(perp_new[k] == (-perp_old[k][0], perp_old[k][1]) for k in perp_new)
        and set(cop_new) == set(cop_old)
        and all(cop_new[k] == cop_old[k] for k in cop_new)
        and classes.count(-_SINGLE) == 14
        and classes.count(-_FAN) == 2
        and classes.count(-_CORNER_ODD) == 2
        and sorted(norm_new.values()) == [-u] * 4 + [Fraction(0)] * 16
        and all(
            cert["pairs"][p]["far_X_gate_all_zero"] for p in ("coplanar", "normal", "perpendicular")
        )
    )
    return ok, (
        f"perpendicular pair in the (0,2) basis: 14 single contacts at {-_SINGLE}, 2 fans at "
        f"{-_FAN}, "
        f"2 corners at {-_CORNER_ODD}; every C-odd value the negative of the (2,0) run's and every "
        "C-even value identical; coplanar pair identical in both sectors; stacked pair 16 "
        "zeros and 4 "
        f"side chains at {-u}; a plaquette five sites away gives exactly zero on all three pairs. "
        "58 cumulants, none reading either kernel or the engine"
    )


@third.check(_CUBE_THIRD, _CITE, rests_on=(_CORNER_THIRD,))
def _():
    # The direct term through the four other faces of the cube, with the full
    # H0 dynamics (adjoint components included -- no singlet shortcut), in the
    # third engine. Both traversals of the perpendicular face are computed:
    # the (2,0) one reproduces the run's raw W entries, the (0,2) one is the
    # kernel's basis, where the C-odd cube term is -53/768.
    normal = LC.cube_completion(_P, ((0, 1), (0, 0, 1)), _OTHERS_NORM)
    p20 = LC.cube_completion(_P, _Q20, _OTHERS_PERP)
    p02 = LC.cube_completion(_P, _Q02, _OTHERS_PERP)
    raw = json.loads(
        (ROOT / _PAIR_RUN / "pair_route_perpendicular_cube.json").read_text(encoding="utf-8")
    )
    run_w = {k: Fraction(v) for k, v in raw["cubes"][0]["W"].items()}
    ok = (
        LC.block_odd(normal) == _rat(K.CUBE_COMPLETION_4)
        and LC.block_even(normal) == _rat(K.CUBE_COMPLETION_4)
        and {str(k): v for k, v in p20.items()} == run_w
        and LC.block_odd(p20) == Fraction(53, 768)
        and LC.block_odd(p02) == _CUBE_ADJ == _rat(K.CUBE_COMPLETION_ADJACENT_4)
        and LC.block_even(p02) == _CUBE_ADJ
    )
    return (
        ok,
        (
            f"opposite faces: C-odd {LC.block_odd(normal)} = C-even, the agreed nu~; adjacent "
            "faces in "
            f"the run's (2,0) traversal: entries { {str(k): str(v) for k, v in p20.items()} } "
            "= the "
            f"run's, C-odd {LC.block_odd(p20)}; in the kernel's (0,2) basis C-odd "
            f"{LC.block_odd(p02)}, "
            f"C-even {LC.block_even(p02)}"
        ),
    )


@third.check(
    _CUBE_MULTILOOP,
    "C2; G3; G14; MOB §4; runs/g3_offaxis_channels_2026-08-30; " + _RUN + "; ADR 0024",
    rests_on=(
        "the perpendicular cube sector is a second fourth-order primitive channel, S_4 = -11",
        "the cube instance re-derives the sealed core, temporal classes included",
        _CUBE_THIRD,
    ),
)
def _():
    # Every link of a cube lies in exactly two faces, so once both are present
    # the link's adjoint component can never return to the target face: the
    # exact cube completion is the primitive law extended to histories whose
    # intermediates are products of disjoint simple loops, H0 additive over
    # the loops. That adds to the 14 single-loop orderings the 10 that begin
    # with a face disjoint from the current loop, eight at -2 and two at -1
    # in units of 1/(N(N^2-1)^3), and reproduces the full computation at
    # N = 3 exactly -- with only the n = 1 Haar moment, symbolic in N.
    opp, _rows = CELL.c_full(CELL.CUBE, 0, 1)
    adj, rows = CELL.c_full(CELL.CUBE, 0, 2)
    n = CELL.N
    single = [r for r in rows if all(k == 1 for k in r[2])]
    multi = [r for r in rows if not all(k == 1 for k in r[2])]
    unit = -1 / (n * (n**2 - 1) ** 3)
    multi_units = sorted(int(simplify(r[3] / unit)) for r in multi)
    ok = (
        simplify(opp - K.c_prim_printed(4)) == 0
        and simplify(adj + 106 / (n * (n**2 - 1) ** 3)) == 0
        and len(single) == 14
        and multi_units == [1, 1] + [2] * 8
        and simplify(sum(r[3] for r in single) + 88 / (n * (n**2 - 1) ** 3)) == 0
        and adj.subs(n, 3) == Rational(-53, 768)
        and simplify(adj / opp - Rational(53, 80)) == 0
    )
    return (
        ok,
        (
            f"opposite faces {opp} (24 single-loop orderings, the sealed core); adjacent faces "
            f"{adj}: "
            f"14 single-loop orderings summing to -88/(N(N^2-1)^3) and 10 multi-loop orderings at "
            f"{multi_units} units of -1/(N(N^2-1)^3), total -106; at N = 3 {adj.subs(n, 3)}, "
            "the run's "
            "cube term to the digit. Ratio adjacent/opposite = 53/80 at every rank. The Hodge "
            "form's "
            "single weight on L_up is therefore not the mechanism (ADR 0021), and this is the "
            "closed form "
            "G14 asked for"
        ),
        {"CUBE_COMPLETION_ADJACENT_N": adj},
    )


@third.check(_LEDGER_REASSEMBLES, "C2; G3; corpus manifest row A41F; ADR 0024; " + _RUN)
def _():
    # DATA_Y4_stagei_authority_fixture.xz.b85 decodes to the Stage-3I word
    # ledger whose gzip hash is the stage3i_input the kernel copies quote.
    # Stage 3J's rooted-stabilizer assembly, ported verbatim, turns its 4,221
    # words into the pinned 189 records exactly. ADR 0021 said this
    # repository did not hold the historical face-resolved ledger; it did.
    from ..payloads import stage3i_hashes

    words = S3.load_words()
    full = S3.build_full_kernel(S3.build_root_kernel(words))
    pinned = dict(kernel_records())
    ok = S3.STAGE3I_SHA in stage3i_hashes() and len(words) == 4221 and full == pinned
    return ok, (
        f"fixture gzip sha256 {S3.STAGE3I_SHA[:16]}... is a kernel copy's stage3i_input; "
        f"{len(words)} "
        f"ordered words; rooted reassembly gives {len(full)} records equal to the pinned "
        f"{len(pinned)} to the digit"
    )


@third.check(
    _LEDGER_FINDING,
    _CITE + "; corpus manifest row A41F",
    rests_on=(_LEDGER_REASSEMBLES, _CORNER_THIRD, _CUBE_THIRD, _CUBE_MULTILOOP),
)
def _():
    # Grouping the ledger's rooted images by the set of plaquettes they touch
    # gives the historical kernel's own connected cumulants. For the rotation
    # record (xy(0) -> xz(0), the (0,2) face) they are the assembly's: pair,
    # 14 chains, 2 fans, 2 corners, all to the digit in the (0,2) basis, C-odd
    # and C-even. The cube cluster holds 8 ordered words summing to -31/1536
    # where the full completion is -53/768; the 8 carry weights -8,-8,-4,-4,-2,
    # -2,-2,-1 in units of 1/1536 -- eight of the 24 histories' weights, each
    # right (the multi-loop model's -8 x 8, -4 x 6, -2 x 8, -1 x 2) --
    # and the 16 orderings it lacks sum to exactly -25/512.
    cert = _certificate()
    odd = S3.cluster_classes(S3.ROTATION_OUTPUT, "odd")
    even = S3.cluster_classes(S3.ROTATION_OUTPUT, "even")
    pair_old = -Fraction(_pair_certificate()["pairs"]["perpendicular"]["pair_cluster_codd"])
    weights = sorted(int(v * 1536) for _i, _ins, v in S3.cube_words(S3.ROTATION_OUTPUT))
    third_engine = {
        k: (Fraction(v["codd"]), Fraction(v["ceven"]))
        for k, v in cert["pairs"]["perpendicular"]["dressings"].items()
    }
    ok = (
        odd["pair(shared link)"]["sum"] == pair_old
        and set(odd["chain3(two shared links)"]["values"]) == {-_SINGLE}
        and odd["chain3(two shared links)"]["supports"] == 14
        and set(odd["fan(three on one link)"]["values"]) == {-_FAN}
        and set(odd["corner(three faces at a vertex)"]["values"]) == {-_CORNER_ODD}
        and set(even["corner(three faces at a vertex)"]["values"]) == {_CORNER_EVEN}
        and set(even["chain3(two shared links)"]["values"]) == {Fraction(-121, 249696)}
        and odd["cube(six faces once each)"]["sum"]
        == _CUBE_HIST
        == _rat(K.CUBE_COMPLETION_ADJACENT_HISTORICAL_4)
        and even["cube(six faces once each)"]["sum"] == _CUBE_HIST
        and weights == [-8, -8, -4, -4, -2, -2, -2, -1]
        and Fraction(-25, 512) == _CUBE_ADJ - _CUBE_HIST
        and {v[0] for v in third_engine.values()} == {-_SINGLE, -_FAN, -_CORNER_ODD}
    )
    return (
        ok,
        (
            f"historical rotation record by cluster, C-odd: pair "
            f"{odd['pair(shared link)']['sum']} (the "
            f"run's, sign flipped to the (0,2) basis), 14 chains at {-_SINGLE}, 2 fans at "
            f"{-_FAN}, 2 "
            f"corners at {-_CORNER_ODD}, cube {_CUBE_HIST} from 8 words with weights "
            f"{weights}/1536; "
            f"C-even corners {_CORNER_EVEN}, cube {_CUBE_HIST}. The third engine gives the same "
            "three "
            f"dressing classes. Cube: full {_CUBE_ADJ} against historical {_CUBE_HIST}, the "
            "difference "
            f"{_CUBE_ADJ - _CUBE_HIST} being the 16 missing orderings"
        ),
    )


@third.check(
    _BASIS_FINDING,
    _CITE + "; ADR 0018; ADR 0019; THM_FLUX Prop. 2",
    rests_on=(
        _LEDGER_FINDING,
        _CUBE_THIRD,
        "the 144 agreed records are u S_sq^2, the shared-link adjacency squared",
    ),
)
def _():
    # Which orientation of the (0,2) face the kernel's records use is a fact,
    # not a convention to choose: all 24 cross-plane records equal rho times
    # the x-then-z L_down incidence (+1 for xy(0) -> xz(0)), the second-order
    # perpendicular hop in that traversal is +5/612 = t_3 times the same +1,
    # and every C-odd component of the historical ledger is the negative of
    # the run's (2,0)-traversal value. So the run's element compares to the
    # record only after conjugating Q: rho_assembled = -RHO_CLUSTER. Then
    # rho_historical - rho_assembled = 25/512, entirely the cube term, and the
    # -25/512 the U5 prediction named is realised -- as the historical
    # kernel's shortfall on a cluster with no epsilon sector, not as the
    # epsilon sector (which the 2026-09-02 run measured at -55/6936).
    cert = _certificate()["rotation_element_kernel_basis"]
    recs = dict(kernel_records())
    rho_hist = _rat(K.RHO_ORBIT)
    ldown = KO.down_laplacian()
    cross = {k: v for k, v in recs.items() if abs(v) == rho_hist}
    rho_asm = Fraction(cert["rho_assembled"])
    rho_cluster = Fraction(_pair_certificate()["pairs"]["perpendicular"]["lattice_codd"])
    ok = (
        len(cross) == 24
        and all(v == rho_hist * ldown[k] for k, v in cross.items())
        and ldown[((0, 1), (0, 2), (0, 0, 0))] == 1
        and rho_asm == -rho_cluster == _rat(K.RHO_ASSEMBLED)
        and rho_hist - rho_asm == Fraction(25, 512)
        and Fraction(cert["cube_full"]) == _CUBE_ADJ
        and Fraction(cert["cube_historical"]) == _CUBE_HIST
        and cert["rho_historical_equals_non_cube_plus_historical_cube"] is True
        and Fraction(cert["rho_historical_minus_assembled"]) == Fraction(25, 512)
    )
    return (
        ok,
        (
            f"all 24 cross-plane records are RHO_ORBIT times the x-then-z L_down incidence, +1 on "
            f"xy(0) -> xz(0); in that basis the assembled element is {rho_asm} = -RHO_CLUSTER, the "
            f"historical {rho_hist}; non-cube part {cert['non_cube_part']} shared by both, cube "
            f"{cert['cube_full']} against {cert['cube_historical']}; difference "
            f"{cert['rho_historical_minus_assembled']} = 25/512 exactly. ADR 0021 compared "
            "+RHO_CLUSTER "
            "with the record and so recorded a third value that is not in the kernel's basis"
        ),
    )


@third.check(
    "FINDING: C_shp from the assembled amplitudes in the kernel's basis is C_historical + 25/1024, "
    "the registered continuation-shifted value",
    _CITE + "; C10; ADR 0019",
    rests_on=(
        _BASIS_FINDING,
        "the shape coefficients are solved, not fitted: A = 5/48, B = D = 0 exactly",
        "C_shp = -5/96 - u - (rho + pi)/2, exactly",
        "RETRACTED: B_3 - beta_historical = 25/64 is a forbidden substitution, not an exact branch",
    ),
)
def _():
    # The assembled rho put into the 24 cross-plane records, in the kernel's
    # basis, and the shape ansatz solved over the whole zone exactly as for the
    # historical kernel: A, B, D unchanged, no residual, and C moves by
    # -(delta rho)/2 = +25/1024 to the value this registry already holds as
    # C_SHP_CONTINUATION_SHIFTED -- the number the all-rank beta_N formula
    # gives at N = 3, whose DERIVATION by continuation was retracted on
    # 2026-08-30 (the retraction stands: the route was forbidden; the number
    # it produced was right). The corpus's "determinant sectors shift C at
    # N = 3 by -25/1024" (C10) is this shortfall, on a cluster that has no
    # determinant sector.
    recs = dict(kernel_records())
    rho_hist = _rat(K.RHO_ORBIT)
    ldown = KO.down_laplacian()
    rho_asm = Fraction(_certificate()["rotation_element_kernel_basis"]["rho_assembled"])
    mod = dict(recs)
    for k, v in recs.items():
        if abs(v) == rho_hist:
            mod[k] = rho_asm * ldown[k]
    co, residual = KO.coefficients(tuple(mod.items()))
    c_hist = _rat(K.C_SHP_HISTORICAL)
    formula = Fraction(-5, 96) - _rat(K.X_QUANTUM) - (rho_asm + _rat(K.PI_ORBIT)) / 2
    ok = (
        not residual
        and co["A"] == Fraction(5, 48)
        and co["B"] == 0
        and co["D"] == 0
        and co["C"] == formula == c_hist + Fraction(25, 1024) == _rat(K.C_SHP_ASSEMBLED)
        and _rat(K.C_SHP_ASSEMBLED) == _rat(K.C_SHP_CONTINUATION_SHIFTED)
    )
    return (
        ok,
        (
            f"with rho_assembled = {rho_asm} in the kernel's basis: A = {co['A']}, B = {co['B']}, "
            f"D = {co['D']}, residual {residual or 'none'}, C = {co['C']} = "
            f"{float(co['C']):.12f} = "
            f"C_historical + 25/1024 = C_SHP_CONTINUATION_SHIFTED; historical "
            f"{float(c_hist):.12f}, "
            "cold -0.020213328886. The 2026-09-02 'third value' -0.0642696 was the same "
            "assembly read in the conjugate basis and is superseded"
        ),
    )


@third.check(
    "the all-rank beta_N formula at N = 3 is 8A + 16 C_shp_assembled exactly: the SU(3) "
    "exception in the shape channel was the cube shortfall",
    _CITE + "; C10; GLUEBALL v3.1 ~1511 (the forbidden substitution); corpus CLAUDE.md trap 2",
    rests_on=(
        "RETRACTED: B_3 - beta_historical = 25/64 is a forbidden substitution, not an exact branch",
        "FINDING: C_shp from the assembled amplitudes in the kernel's basis is C_historical + "
        "25/1024, the registered continuation-shifted value",
    ),
)
def _():
    # The corpus forbids substituting the compact all-rank beta_N formula at
    # N = 3 and prescribes a separate SU(3) value 25/64 below it, attributing
    # the gap to the determinant sector (trap 2 and trap 3 of the corpus
    # CLAUDE.md, C10). With the historical rho corrected by its own ledger,
    # beta = 8A + 16 C_shp at N = 3 IS the formula's value: the SU(3)
    # exception in the shape channel was the sixteen missing cube orderings.
    # The formula stays forbidden as a DERIVATION at N = 3 (its continuation
    # route has a third-order pole there); what this check records is that
    # the number it produces is the assembled one, exactly.
    from ..channel_ledger import beta_formula
    from ..payloads import kernel_constants

    a = _rat(K.A_SHP_3)
    c = _rat(K.C_SHP_ASSEMBLED)
    beta_hist = kernel_constants()["beta"]
    formula = beta_formula(3)
    ok = (
        8 * a + 16 * c == formula
        and formula - beta_hist == Fraction(25, 64)
        and beta_hist == _rat(K.BETA_PEN_3)
        and c - _rat(K.C_SHP_HISTORICAL) == Fraction(25, 1024)
    )
    return ok, (
        f"beta_N(3) = {formula} = 8 * {a} + 16 * {c} = 8A + 16 C_shp_assembled, against the "
        f"historical beta_3 = {beta_hist} (gap 25/64 = 16 * 25/1024). The formula is still not a "
        "derivation at N = 3; it is now the right number there, and nothing distinguishes N = 3 "
        "from N >= 4 in the fourth-order shape coefficient"
    )
