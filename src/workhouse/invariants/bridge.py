from __future__ import annotations

import json

from sympy import (
    Rational,
    simplify,
    sqrt,
    symbols,
)

from .. import constants as K
from .. import payloads as P
from ._core import ROOT, _suite

# ==========================================================================
bridge = _suite("finite-rank truncation bridge (published SU(3) truncations)")


@bridge.check(
    "the published dimension-ratio matrix element is this registry's weight formula",
    "R2; Ciavarella-Burbano-Bauer arXiv:2503.11888v5 Eq. (D1); notes UPLOADS_2026-08-28e",
)
def _():
    # The all-ranks suite already derives the four shared-link channel
    # weights, A_N, B_N and t_N = B_N - A_N, exactly and at symbolic N. None
    # of that is re-derived here, and the bridge documents do not add to it.
    #
    # What they add is PROVENANCE. The repository's weight formula
    # w_rho = -(d_rho/N^2)/(C_F + C_rho/2) takes its numerator from the
    # corpus's own appendix. Ciavarella, Burbano and Bauer publish a
    # finite-rank plaquette matrix element |M_rho| = sqrt(dim rho / (dim A
    # dim R)), and for two fundamental factors dim A = dim R = N, so
    # |M_rho|^2 = d_rho/N^2 -- the same numerator, from a source that was
    # written without knowledge of this program.
    #
    # This check is that specialization and nothing more: the published
    # general form, evaluated at the fundamental-times-fundamental case,
    # equals the numerator the registry uses, identically in N. It buys a
    # citation, not a new number. The physics premise -- that this is the
    # right matrix element to feed the second-order resolvent, and that the
    # four channels exhaust the shared-link routes in the charge-odd
    # one-plaquette sector -- is argued in prose in the imported documents
    # and stays T3.
    n, d = symbols("n d", positive=True)

    # the published form, with both factors fundamental
    published = sqrt(d / (n * n)) ** 2
    registry = d / n**2

    same = simplify(published - registry) == 0
    # and the all-rank law the two together produce, against hopping()
    law = 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))
    agrees = all(simplify(law.subs(n, r) - K.hopping(r)) == 0 for r in (3, 4, 5, 7, 12))

    return same and agrees, (
        f"|M_rho|^2 = dim rho/(dim A dim R) with dim A = dim R = N is {registry}, identically the "
        "numerator the all-ranks suite already uses, so the published finite-rank matrix element "
        "and this registry's channel weights are the same statement. The closed law it yields, "
        "2N(N^2-4)/((N^2-1)(2N^2-1)(4N^2-9)), reproduces hopping(N) at N = 3, 4, 5, 7, 12. This "
        "is external provenance for a chain already checked here, not a new derivation, and it "
        "does not check the premise that four channels exhaust the sector"
    )


@bridge.check(
    "FINDING: the T1 link cutoff reverses the sign of t_3, and 14/153 is what it omits",
    "R2; notes UPLOADS_2026-08-28e §5; runs/cbb_finite_n_bridge_2026-08-28",
)
def _():
    # The registry carries t_3 = 5/612 and the four channel weights. It did
    # not carry what happens when a truncation keeps only some of them, and
    # that turns out to be the sharpest thing in these documents.
    #
    # The p+q <= 1 link cutoff -- T1 = {1, 3, 3bar} in the published
    # nomenclature, the truncation used for the published one-cube exact
    # diagonalization -- retains the singlet and the 3bar routes and drops
    # the 8 and the 6. Its projected second-order hopping is
    #
    #     t_3^T1 = w_3bar - w_1 = -1/6 + 1/12 = -1/12,
    #
    # against the channel-complete +5/612. Opposite in sign and 10.2 times
    # larger in magnitude. The omitted channels are not a correction to this;
    # they reverse it, and the exact completion is w_6 - w_8 = 14/153.
    #
    # One trap worth naming, because `workhouse search -1/12` walks straight
    # into it: -1/12 is ALSO the singlet weight w_1. The two are different
    # quantities that happen to coincide, and the cutoff value is a
    # difference of two weights, not a weight.
    #
    # The consequence recorded in the documents is that a counterterm added
    # to a published T1 Hamiltonian must be 14/153, never 5/612, since T1
    # already carries the singlet and 3bar routes. Nothing here promotes a
    # value: t_3 = 5/612 is the registry's, and the rest is arithmetic about
    # what a truncation drops.
    weights = {
        "1": -Rational(1, 12),
        "8": -Rational(16, 51),
        "3bar": -Rational(1, 6),
        "6": -Rational(2, 9),
    }
    t3 = K.hopping(3)
    cutoff = weights["3bar"] - weights["1"]
    completion = weights["6"] - weights["8"]

    closes = cutoff + completion == t3
    reversed_sign = cutoff * t3 < 0
    collision = cutoff == weights["1"]
    ratio = abs(cutoff / t3)

    return (closes and reversed_sign and collision and completion == Rational(14, 153)), (
        f"the p+q<=1 cutoff keeps the singlet and 3bar and drops the 8 and 6, giving "
        f"t_3^T1 = w_3bar - w_1 = {cutoff}, opposite in sign to the channel-complete {t3} and "
        f"{float(ratio):.1f}x larger in magnitude; the omitted pair completes it exactly, "
        f"w_6 - w_8 = {completion}, and {cutoff} + {completion} = {t3}. So a counterterm for a "
        "published T1 Hamiltonian is 14/153, not 5/612, which would double-count the two routes "
        f"T1 already has. Note the collision: {cutoff} is also the singlet weight w_1 itself "
        "-- a coincidence of value between a weight and a difference of weights"
    )


@bridge.check(
    "the certificate's finite-volume fingerprints, and 29 = L^3 + 2 is the Lean cycle count",
    "R2; notes UPLOADS_2026-08-28e §6-7; runs/cbb_finite_n_bridge_2026-08-28",
)
def _():
    # The two spectral fingerprints are the documents' concrete predictions,
    # and both are pure topology times one registered number, so they are
    # checkable here without re-running anything: the incidence spectrum of
    # the cubical complex, scaled by t_3.
    #
    # This check reads the PINNED certificate rather than recomputing the
    # boundary matrices, because the certificate is the artifact the run
    # record pins and a check that re-derives its own expectation tests
    # nothing. The recomputation is the certificate's job and it is
    # reproduced in runs/cbb_finite_n_bridge_2026-08-28.
    #
    # The detail worth having in the registry is the last line. The periodic
    # 3^3 torus has 29 zero modes, and 29 = 3^3 + 2 is exactly the cycle
    # count this repository already proves in Lean as dim_Z_2:
    # (L^3 - 1) + 3 = L^3 + 2, cube boundaries plus the harmonic triplet. So
    # the bridge's most discriminating multiplicity is a T0 statement here,
    # arrived at independently, and the zero modes are not an artifact of the
    # truncation but the homology of the three-torus.

    certificate = json.loads(
        (
            ROOT
            / "runs"
            / "cbb_finite_n_bridge_2026-08-28"
            / "su3_finite_n_bridge_certificate.json"
        ).read_text(encoding="utf-8")
    )
    t3 = K.hopping(3)

    cube = {
        int(k): v for k, v in certificate["open_cube"]["BBdagger_eigenvalue_multiplicities"].items()
    }
    torus = {
        int(k): v
        for k, v in certificate["periodic_L3"]["BBdagger_eigenvalue_multiplicities"].items()
    }

    cube_ok = cube == {0: 1, 4: 3, 6: 2}
    torus_ok = torus == {0: 29, 3: 12, 6: 24, 9: 16}
    exhausts = sum(torus.values()) == 3 * 3**3

    scaled_cube = {Rational(lam) * t3: m for lam, m in cube.items()}
    scaled_torus = {Rational(lam) * t3: m for lam, m in torus.items()}
    cube_pred = scaled_cube == {Rational(0): 1, Rational(5, 153): 3, Rational(5, 102): 2}
    torus_pred = scaled_torus == {
        Rational(0): 29,
        Rational(5, 204): 12,
        Rational(5, 102): 24,
        Rational(5, 68): 16,
    }
    cycles = torus[0] == 3**3 + 2

    return (cube_ok and torus_ok and exhausts and cube_pred and torus_pred and cycles), (
        f"the pinned certificate's incidence spectra are {cube} on one open cube and {torus} on "
        f"the periodic 3^3 torus, the latter exhausting all 3L^3 = {3 * 3**3} face modes. Scaling "
        f"by the registry's t_3 = {t3} gives the predicted charge-odd shells "
        "{0, (5/153)^3, (5/102)^2} and {0^29, (5/204)^12, (5/102)^24, (5/68)^16}. The 29 zero "
        f"modes are {3**3} + 2 = L^3 + 2, which this repository proves in Lean as dim_Z_2 -- so "
        "the most discriminating multiplicity in the fingerprint is the homology of the "
        "three-torus, not a feature of the truncation"
    )


@bridge.check(
    "FINDING: the bridge documents match the obtained paper, except one equation number",
    "R2; arXiv:2503.11888v5 Eqs. (1), (D1), Fig. 6, App. C; notes UPLOADS_2026-08-28e",
)
def _():
    # The paper was registered not-yet-obtained, with the note that obtaining
    # it is what would move the edge to verified. It has been obtained
    # (arXiv:2503.11888v5, dated 17 Feb 2026,
    # sha256 55f47cd77126e296d8dbd91d1a18ca2b66a80afa9dd20bc78c56c88a56113c5c)
    # and read. Everything the bridge documents rest on checks out:
    #
    #   Eq. (1)   H = (g^2/2) sum_l E_l^2 - (1/2g^2) sum_p (Box_p + Box_p^dag)
    #             -- so u = 1/(2 g^4) after dividing by g^2, as claimed.
    #   Eq. (D1)  <...|Box|...> = sqrt(dim(B)/(dim(A) dim(R))), with B in
    #             R (x) A. With both factors fundamental this is d_rho/N^2,
    #             the numerator this registry already uses.
    #   Fig. 6    derives the three nontrivial (1,2,2) amplitudes FROM (D1):
    #             sqrt(1 - 1/N^2), sqrt((1+1/N)/2), sqrt((1-1/N)/2).
    #   App. C    tabulates every dimension and Casimir the weights need,
    #             INCLUDING the adjoint row (1,0,...,0,1) -> N^2-1, N.
    #
    # One transcription error, and it is worth recording rather than
    # silently repairing: FINITE_N_SU3_TRUNCATION_CAPABILITY_RESULT section 4
    # cites "Appendix D, Eq. (265)". The paper's main text numbering stops at
    # (25) and the equation is labelled (D1). The companion document
    # CBB_FINITE_N_SU3_TN_BBDAGGER_BRIDGE has it right. So the two imported
    # documents disagree with each other, and the one that is wrong is wrong
    # about a pointer, not about the physics.
    #
    # This check asserts the Appendix C closed forms as read from the paper
    # against the values the pinned certificate actually used. It does not
    # read the PDF: the paper is not stored here, because its redistribution
    # licence was not established, so the transcription is curated in
    # literature/index.yaml and its consequences are checked here.
    from sympy import Integer

    n = symbols("n", positive=True)

    # Appendix C, general-N column, transcribed from the obtained paper
    paper = {
        "1": (Integer(1), Integer(0)),
        "8": (n**2 - 1, n),
        "3bar": (n * (n - 1) / 2, (n**2 - n - 2) / n),
        "6": (n * (n + 1) / 2, (n**2 + n - 2) / n),
    }
    c_f = (n**2 - 1) / (2 * n)

    # what runs/cbb_finite_n_bridge_2026-08-28 actually used, at N = 3
    certificate = {
        "1": (1, Rational(0), -Rational(1, 12)),
        "8": (8, Rational(3), -Rational(16, 51)),
        "3bar": (3, Rational(4, 3), -Rational(1, 6)),
        "6": (6, Rational(10, 3), -Rational(2, 9)),
    }

    agree = []
    for rho, (dim_form, cas_form) in paper.items():
        dim3, cas3, weight = certificate[rho]
        agree.append(simplify(dim_form.subs(n, 3) - dim3) == 0)
        agree.append(simplify(cas_form.subs(n, 3) - cas3) == 0)
        # and the weight the paper's own inputs force
        forced = -(dim_form / n**2) / (c_f + cas_form / 2)
        agree.append(simplify(forced.subs(n, 3) - weight) == 0)

    return all(agree), (
        "the obtained paper's Eq. (1) fixes u = 1/(2g^4), its Eq. (D1) gives "
        "|M|^2 = dim(B)/(dim(A)dim(R)) = d_rho/N^2 for two fundamental factors, its Fig. 6 "
        "derives the three nontrivial (1,2,2) amplitudes from (D1), and its Appendix C tabulates "
        "all four dimensions and Casimirs INCLUDING the adjoint row (1,0,...,0,1) -> (N^2-1, N). "
        "Feeding those closed forms through the registry's weight formula reproduces every "
        "channel weight the pinned certificate used, at N = 3. The one error found: "
        "FINITE_N_SU3_TRUNCATION_CAPABILITY_RESULT section 4 cites 'Eq. (265)'; the paper "
        "numbers its main text to (25) and labels this equation (D1), which its companion "
        "document gets right. A wrong pointer, not wrong physics"
    )


@bridge.check(
    "the discrete index theorem gives 0 on the signed face-edge operator, bounding nothing",
    "R2; G14; arXiv:2607.22831v1 (Hazra) §6 Eq. for ind_a(D)",
    tier=2,
)
def _():
    # A published face-graph flat-band framework arrived alongside the CBB
    # paper: an infinite family of Hamiltonians H = t B^T B supported on the
    # FACES of an arbitrary graph, with the null space proved extensive by a
    # discrete Atiyah-Singer index theorem,
    #
    #     dim ker(B^T B) - dim ker(B B^T) = |F| - |V|,   hence  >= |F| - |V|.
    #
    # The shape is this repository's face operator, and the temptation is to
    # call it the same mechanism. It is not, and the difference is exactly
    # checkable, so it is recorded here before it becomes an analogy.
    #
    # Hazra's B is the UNORIENTED face-vertex incidence -- his own footnote
    # says so, B_vf = 1 if vertex v lies on the face's cycle. On the cubic
    # lattice |V| = L^3 and |F| = 3L^3, so his bound is 2L^3 flat bands, and
    # it is forced by rank-nullity alone: more faces than vertices.
    #
    # This repository's B is the SIGNED face-edge boundary d_2, where
    # |F| = |E| = 3L^3. So the index is ZERO, the theorem gives no lower
    # bound at all, and the L^3 + 2 zero modes are not a rank-nullity
    # artifact -- they are the cycle space of the three-torus, which the T0
    # layer proves as dim_Z_2. This check verifies both halves: index 0, and
    # both kernels equal to L^3 + 2, at three volumes.
    #
    # So the honest relation is agreement of FORM with a different mechanism:
    # extensive degeneracy from counting there, from homology here. Recorded
    # as a distinction rather than a unifying candidate, which would need a
    # falsifier and does not have one.
    from .. import torus

    rows = []
    for ell in (2, 3, 4):
        d2 = torus.d2_matrix(ell)
        rank = d2.rank()
        faces, edges = d2.ncols(), d2.nrows()
        ker_face, ker_edge = faces - rank, edges - rank
        rows.append((ell, faces, edges, ker_face, ker_edge, ell**3 + 2))

    index_zero = all(kf - ke == 0 and f == e for _, f, e, kf, ke, _ in rows)
    homology = all(kf == cyc and ke == cyc for _, _, _, kf, ke, cyc in rows)
    hazra_bound = {ell: 3 * ell**3 - ell**3 for ell, *_ in rows}

    return index_zero and homology, (
        "on the signed face-edge boundary d_2 the index dim ker(B^T B) - dim ker(B B^T) is 0 at "
        f"L = 2, 3, 4 because |F| = |E| = 3L^3, and both kernels equal L^3 + 2 = "
        f"{[r[5] for r in rows]} -- the cycle space the T0 layer proves as dim_Z_2. The published "
        "face-graph theorem bounds dim ker(B^T B) >= |F| - |V| for the UNORIENTED face-vertex "
        f"incidence, which on this lattice is {hazra_bound}, a different operator with a "
        "different count. Same form, different mechanism: rank-nullity counting there, homology "
        "here, and the index bounds nothing on the operator this repository uses. A distinction, "
        "not a unifying candidate -- there is no falsifier for an identification of the two"
    )


@bridge.check(
    "FINDING: a full T1 = B = 4 cube Hamiltonian reproduces -1/12 and the reversed shell",
    "R2; runs/balaji_open_cube_b4_t1_2026-08-28; notes UPLOADS_2026-08-28g",
    tier=2,
)
def _():
    # The bridge documents named one test they had not done: diagonalise the
    # authors' complete one-cube Hamiltonian at small u and see whether the
    # 1+3+2 charge-odd shell comes out in the predicted order. For the T1
    # branch that test has now been done, from the authors' own published
    # ymcirc plaquette table rather than from the bridge's algebra, and it
    # passes.
    #
    # The sharpest form of the agreement is not the eigenvalues, it is the
    # MATRIX. The reconstruction's second-order gap matrix on the six
    # charge-odd single-face states equals
    #
    #     (37/12) I - (1/12) G,        G = B^T B the cube's face Gram,
    #
    # to 4.3e-11. So t_3^T1 = -1/12 is not fitted from a spectrum; it appears
    # directly as the off-diagonal element of a matrix built from published
    # data, and the identity coefficient 37/12 is the one the separate CBB
    # certificate derived. Two independently produced certificates agree, and
    # this one did not go through the second-order Schur algebra at all.
    #
    # Scope, and it is narrow. This confirms the TRUNCATED branch: the cutoff
    # that omits the 8 and 6 really does give the reversed ordering. It says
    # nothing about the channel-complete +5/612, which needs a B = 6 cube
    # carrying all four shared-link channels, and none has been run. It is
    # also not an independent-group replication -- the table and the cube
    # paper share an author and code lineage, and the open-cube assembly is
    # the reconstructor's, not the authors'.
    #
    # G is rebuilt here from oriented cell boundaries rather than read, so
    # the check does not take the certificate's own Gram on trust.
    from fractions import Fraction

    record = json.loads(
        (
            ROOT
            / "runs"
            / "balaji_open_cube_b4_t1_2026-08-28"
            / "balaji_open_cube_B4_T1_certificate.json"
        ).read_text(encoding="utf-8")
    )
    gap = record["perturbative_result"]["gap_second_order_matrix"]

    # G rebuilt from oriented cell boundaries, in the certificate's own face
    # order (xy@z=0, xy@z=1, xz@y=0, xz@y=1, yz@x=0, yz@x=1) -- so the
    # certificate's Gram is not taken on trust.
    edges, faces = [], []
    for a in range(3):
        for x0 in (0, 1):
            for x1 in (0, 1):
                x = [0, 0, 0]
                rest = [i for i in range(3) if i != a]
                x[rest[0]], x[rest[1]] = x0, x1
                edges.append((tuple(x), a))
    edge_id = {e: i for i, e in enumerate(edges)}
    for a in range(3):
        for b in range(a + 1, 3):
            c = next(i for i in range(3) if i not in (a, b))
            for side in (0, 1):
                x = [0, 0, 0]
                x[c] = side
                faces.append((tuple(x), a, b))

    def step(x, a):
        y = list(x)
        y[a] += 1
        return tuple(y)

    boundary = [[0] * len(faces) for _ in edges]
    for j, (x, a, b) in enumerate(faces):
        for e, sign in (((x, a), 1), ((step(x, a), b), 1), ((step(x, b), a), -1), ((x, b), -1)):
            boundary[edge_id[e]][j] += sign
    built = [
        [sum(boundary[e][i] * boundary[e][j] for e in range(len(edges))) for j in range(6)]
        for i in range(6)
    ]

    predicted = [
        [float(Fraction(37, 12)) * (i == j) - Fraction(1, 12) * built[i][j] for j in range(6)]
        for i in range(6)
    ]
    worst = max(abs(gap[i][j] - predicted[i][j]) for i in range(6) for j in range(6))

    groups = record["perturbative_result"]["gap_second_order_groups"]
    seen = sorted((round(g["value"], 9), g["multiplicity"]) for g in groups)
    want = sorted(
        [
            (round(float(Fraction(31, 12)), 9), 2),
            (round(float(Fraction(11, 4)), 9), 3),
            (round(float(Fraction(37, 12)), 9), 1),
        ]
    )

    return (worst < 1e-9 and seen == want and record["status"] == "PASS"), (
        f"the reconstructed second-order gap matrix equals (37/12)I - (1/12)G to {worst:.1e}, with "
        "G rebuilt here from oriented cell boundaries -- so t_3^T1 = -1/12 is the off-diagonal "
        f"element of a matrix assembled from the authors' published plaquette table. Its spectrum "
        f"{seen} is {want}: the T1 absolute coefficients the independent CBB certificate "
        "predicted, doublet lowest and the signed cube boundary highest, the REVERSE of the "
        "channel-complete ordering. This confirms the truncated branch only; the +5/612 branch "
        "needs a B = 6 cube nobody has run, and this is not an independent-group replication"
    )


@bridge.check(
    "FINDING: the B = 6 cube flips the sign back to +5/612, closing the decisive test",
    "R2; runs/b6_open_cube_channel_complete_2026-08-28",
    tier=2,
)
def _():
    # The bridge named one test as remaining: diagonalise the authors'
    # complete one-cube Hamiltonian and see which ordering the charge-odd
    # 1+3+2 shell comes out in. Both branches are now done, and they
    # disagree with each other exactly as predicted:
    #
    #   B = 4 (T1, omits 6 and 8)   t = -1/12    doublet lowest
    #   B = 6 (channel-complete)    t = +5/612   cube boundary lowest
    #
    # This check reads the B = 6 certificate. Its gap operator is
    # (39/68) I + (5/612) G with G the cube face Gram -- so the registry's
    # own t_3 = 5/612 is the off-diagonal element, and the relative shell is
    # {0, (5/153)^3, (5/102)^2}, the exact inverse ordering of the B = 4 run
    # next door. The certificate's own channel census sums to it too:
    # 1/12 - 1/6 - 2/9 + 16/51 = 5/612 exactly.
    #
    # Scope, and the certificate is candid about it. Second order in u only,
    # and the global B = 6 basis was deliberately NOT enumerated -- through
    # second order only states reachable by one action of M matter. So this
    # is exact at O(u^2) in a reduced space, not a finite-coupling
    # diagonalisation, and it could not be re-run here because its generator
    # needs pyclebsch and an adapter that did not travel. What is checked is
    # arithmetic; the physics premise rests on the source audit.
    from fractions import Fraction

    record = json.loads(
        (
            ROOT
            / "runs"
            / "b6_open_cube_channel_complete_2026-08-28"
            / "b6_cube_reduced_certificate.json"
        ).read_text(encoding="utf-8")
    )
    gram = record["face_gram"]
    matrix = record["gap_second_order_matrix"]

    scalar, hop = Fraction(39, 68), P.as_fraction(K.hopping(3))
    worst = max(
        abs(matrix[i][j] - (float(scalar) * (i == j) + float(hop) * gram[i][j]))
        for i in range(6)
        for j in range(6)
    )
    shell = [hop * lam for lam in (0, 4, 6)]
    census = Fraction(1, 12) - Fraction(1, 6) - Fraction(2, 9) + Fraction(16, 51)
    cutoff_t1 = -Fraction(1, 12)

    return (
        worst < 1e-13
        and hop == Fraction(5, 612)
        and census == hop
        and shell == [Fraction(0), Fraction(5, 153), Fraction(5, 102)]
        and cutoff_t1 * hop < 0
        and record["pass"],
        f"the B = 6 gap operator is (39/68)I + ({hop})G to {worst:.1e}, so the registry's own "
        f"t_3 is its off-diagonal element and the relative shell is {[str(x) for x in shell]} "
        "with multiplicities 1, 3, 2 -- the signed cube boundary lowest, the exact inverse of the "
        f"B = 4 ordering where t = {cutoff_t1} put the doublet lowest. The certificate's channel "
        f"census 1/12 - 1/6 - 2/9 + 16/51 = {census} independently. Both branches of the bridge's "
        "remaining test now agree with it. Second order in a reduced space, not a finite-coupling "
        "diagonalisation, and audited for arithmetic rather than re-run",
    )


@bridge.check(
    "the one-cube shell is A1 + T1 + E, and its flat level is the S^2 fundamental class",
    "R2; runs/b6_open_cube_channel_complete_2026-08-28 §5; MASTER paper §3, §6",
    tier=1,
)
def _():
    # The two cube runs next door report a shell of multiplicities 1, 3, 2 and
    # ASSIGN it the cubic labels A_1^{--}, T_1^{+-}, E^{--}. The assignment is
    # asserted in both deliveries -- the B = 6 route's own gate 7 says the
    # symmetry matrices were never built -- and it is worth deriving, because
    # it turns the one-cube validation into the same statement as the torus
    # theorem rather than a numerical coincidence beside it.
    #
    # Everything below is exact integer linear algebra on the cube's own
    # oriented face complex. Three statements:
    #
    # 1. HOMOLOGY. The six faces of a cube are a closed surface. In the
    #    OUTWARD orientation ker d_2 is one-dimensional and generated by the
    #    sum of all six faces -- the fundamental class, b_2(S^2) = 1. This is
    #    the same mechanism as the torus carrier: there ker d_2 is
    #    im d_3 (+) H_2 of dimension L^3 + 2, here there are no three-cells
    #    and only the class survives.
    #
    # 2. REPRESENTATION CONTENT, by explicit intertwiner rather than by
    #    character arithmetic. Write b_{+i}, b_{-i} for the two outward faces
    #    normal to axis i. The 24 proper rotations permute the six outward
    #    faces; v_i = b_{+i} - b_{-i} transforms exactly as the coordinate
    #    e_i (the defining rep, which is T_1), and s_i = b_{+i} + b_{-i}
    #    transforms as the permutation rep on the three unordered axes, which
    #    is A_1 (+) E. With the charge-odd inversion P b_{+i} = -b_{-i}, the
    #    s-sector is parity ODD and the v-sector parity EVEN, giving
    #    A_1^{--} (+) E^{--} and T_1^{+-}.
    #
    # 3. THE SPECTRUM SPLITS ALONG THAT DECOMPOSITION. G = d_2^T d_2 commutes
    #    with all 24 permutations; on the v-sector it is 4I and on the
    #    s-sector 4I - 2(J - I), whose spectrum is {0, 6, 6}. So
    #    G-eigenvalue 4 IS T_1, 6 IS E and 0 IS A_1 -- and the A_1 level of
    #    alpha I + t G sits at alpha for EVERY t. The one-cube flat level is
    #    therefore protected by the same boundary factorisation that protects
    #    the torus carrier, and no truncation, no channel and no disputed
    #    coefficient can move it. What the truncation moves is the ORDER of
    #    the other two, alpha + 4t and alpha + 6t, which is why the reversal
    #    the two runs report is a statement about sign(t) alone.
    import itertools

    from sympy import Matrix, eye, ones, zeros

    # --- the cube's oriented face complex, outward-oriented -----------------
    # faces indexed by outward normal: 0,1 = -e1,+e1; 2,3 = -e2,+e2; 4,5 = -e3,+e3
    normals = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    axis_of = {i: i // 2 for i in range(6)}
    edges: dict[tuple, int] = {}
    boundary_rows = []
    for n in normals:
        c = next(k for k in range(3) if n[k] != 0)
        a, b = (k for k in range(3) if k != c)
        base = [0, 0, 0]
        base[c] = 1 if n[c] > 0 else 0
        # plane orientation (e_a, e_b) has normal +e_c for (a,b,c) an even
        # permutation; flip it when the outward normal points the other way
        # or the permutation is odd.
        parity = 1 if (a, b, c) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1
        sign = parity * (1 if n[c] > 0 else -1)

        def step(x, k):
            y = list(x)
            y[k] += 1
            return tuple(y)

        chain: dict[tuple, int] = {}
        x = tuple(base)
        for link, s in (((x, a), 1), ((step(x, a), b), 1), ((step(x, b), a), -1), ((x, b), -1)):
            edges.setdefault(link, len(edges))
            chain[link] = chain.get(link, 0) + sign * s
        boundary_rows.append(chain)
    d2 = zeros(len(edges), 6)
    for j, chain in enumerate(boundary_rows):
        for link, s in chain.items():
            d2[edges[link], j] += s
    gram = (d2.T * d2).applyfunc(int)

    kernel = d2.nullspace()
    fundamental_class = len(kernel) == 1 and kernel[0] == kernel[0][0] * ones(6, 1) != zeros(6, 1)

    # --- the 24 proper rotations, as permutations of the outward faces ------
    rotations = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            m = zeros(3, 3)
            for i, p in enumerate(perm):
                m[i, p] = signs[i]
            if m.det() == 1:
                rotations.append(m)
    index_of = {n: i for i, n in enumerate(normals)}
    permutations_ = []
    for r in rotations:
        image = []
        for n in normals:
            v = r * Matrix(n)
            image.append(index_of[(int(v[0]), int(v[1]), int(v[2]))])
        permutations_.append(image)
    commutes = True
    for image in permutations_:
        p_mat = zeros(6, 6)
        for i, j in enumerate(image):
            p_mat[j, i] = 1
        commutes &= p_mat * gram == gram * p_mat

    # --- the two sectors, and the intertwiners that name them ---------------
    s_vec = [
        Matrix([1 if axis_of[i] == m else 0 for i in range(6)]) for m in range(3)
    ]  # b_{+m} + b_{-m}
    v_vec = [
        Matrix([(1 if i % 2 else -1) if axis_of[i] == m else 0 for i in range(6)]) for m in range(3)
    ]  # b_{+m} - b_{-m}
    vector_rep = True
    axis_rep = True
    for r, image in zip(rotations, permutations_, strict=True):
        p_mat = zeros(6, 6)
        for i, j in enumerate(image):
            p_mat[j, i] = 1
        for m in range(3):
            # v transforms as the coordinate e_m: P v_m = sum_n R_{n m} v_n
            vector_rep &= p_mat * v_vec[m] == sum(
                (r[n, m] * v_vec[n] for n in range(3)), zeros(6, 1)
            )
            # s transforms as the permutation of unordered axes
            axis_rep &= any(p_mat * s_vec[m] == s_vec[n] for n in range(3))
    s_block = Matrix(3, 3, lambda i, j: (s_vec[i].T * gram * s_vec[j])[0] / 2)
    v_block = Matrix(3, 3, lambda i, j: (v_vec[i].T * gram * v_vec[j])[0] / 2)
    sectors_ok = v_block == 4 * eye(3) and s_block == 4 * eye(3) - 2 * (ones(3, 3) - eye(3))
    spectra_ok = (
        gram.eigenvals() == {0: 1, 4: 3, 6: 2}
        and s_block.eigenvals() == {0: 1, 6: 2}
        and v_block.eigenvals() == {4: 3}
    )

    # --- the consequence for the two truncations ---------------------------
    levels = {}
    for label, t in (("B=6", K.hopping(3)), ("B=4", -Rational(1, 12))):
        alpha = Rational(39, 68) if label == "B=6" else Rational(37, 12)
        levels[label] = [alpha + t * lam for lam in (0, 4, 6)]
    flat_fixed = levels["B=6"][0] == Rational(39, 68) and levels["B=4"][0] == Rational(37, 12)
    reversed_order = (levels["B=6"][0] < levels["B=6"][2]) and (levels["B=4"][0] > levels["B=4"][2])

    ok = (
        fundamental_class
        and commutes
        and vector_rep
        and axis_rep
        and sectors_ok
        and spectra_ok
        and flat_fixed
        and reversed_order
    )
    return ok, (
        "ker d_2 on the closed cube surface is one-dimensional and spanned by the sum of the six "
        "OUTWARD faces -- the fundamental class, b_2(S^2) = 1, the cube's analogue of the torus "
        "carrier. G commutes with all 24 proper rotations; b_+i - b_-i carries the defining "
        "(vector) rep, so it is T_1, and b_+i + b_-i the permutation rep of the three axes, "
        "A_1 + E. With the charge-odd inversion P b_+i = -b_-i the first sector is parity EVEN "
        "and the second parity ODD, so the shell is A_1^{--} (+) T_1^{+-} (+) E^{--} with G "
        f"eigenvalues {{0, 4, 6}} and multiplicities {{1, 3, 2}} -- derived, not assigned. Hence "
        f"alpha I + t G has levels alpha, alpha + 4t, alpha + 6t: the A_1 level is INDEPENDENT of "
        f"t, so no truncation and no channel can move it (the one-cube form of the carrier "
        f"rigidity), while the order of the other two follows sign(t) alone -- "
        f"{[str(x) for x in levels['B=6']]} at B=6 against {[str(x) for x in levels['B=4']]} at "
        "B=4, the reversal both runs report"
    )


@bridge.check(
    "the B = 6 scalar misses the bridge's by exactly the same-face sextet route",
    "R2; runs/b6_open_cube_channel_complete_2026-08-28; notes UPLOADS_2026-08-28e §5.1",
    tier=1,
)
def _():
    # The two calculations disagreed about the scalar, and the disagreement is
    # the most convincing thing in the bundle.
    #
    # The bridge predicted an open-cube scalar of 11/34. The B = 6 run reports
    # 39/68. Those differ by exactly 1/4, and 39/68 - 1/4 = 11/34.
    #
    # Neither side is wrong. The bridge's own section 5.1 names a local
    # SAME-FACE sextet route worth -1/4 and includes it; the B = 6 certificate
    # independently reports that the same-face sextet first enters at cutoff
    # 7, because a same-face sextet PAIR needs C2(6) + C2(6bar) = 20/3 of
    # vertex Casimir where the adjacent-face sextet needs only
    # C2(6) + 2 C2(3) = 6. So B = 6 is channel-complete for the adjacent-face
    # hopping t and NOT for the on-site scalar.
    #
    # Two calculations, neither told about the other, identified the same
    # missing route from opposite directions: one by including it, one by
    # being cut off just below it. That is a much stronger consistency
    # statement than the scalars agreeing would have been, and it is exact
    # rational arithmetic, so no float enters.
    from fractions import Fraction

    b6_scalar = Fraction(39, 68)
    bridge_scalar = Fraction(11, 34)
    sextet_route = Fraction(1, 4)

    return (
        b6_scalar - bridge_scalar == sextet_route and b6_scalar - sextet_route == bridge_scalar,
        f"the B = 6 open-cube scalar is {b6_scalar} and the bridge predicted {bridge_scalar}; "
        f"they differ by {b6_scalar - bridge_scalar}, exactly the local same-face sextet route "
        f"the bridge's section 5.1 carries as -1/4, and {b6_scalar} - 1/4 = {bridge_scalar}. The "
        "certificate reaches the same conclusion from the other side, reporting that the "
        "same-face sextet first enters at cutoff 7 while the adjacent-face sextet is already in "
        "at 6. So B = 6 is channel-complete for the hopping and not for the scalar, and the two "
        "calculations located the same missing route without being told about each other",
    )
