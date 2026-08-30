from __future__ import annotations

import json

from sympy import (
    Rational,
    cancel,
    diff,
    expand,
    limit,
    oo,
    simplify,
    symbols,
)

from .. import constants as K
from .. import even_sector as EVEN
from ._core import ROOT, _suite

# ==========================================================================
# The charge-even sector had five checks naming it and no check body reading
# its registered constants: LEAK_2, LEAK_2_EVEN, LEAK_3_EVEN and the
# lambda = -4 cubic were registered and inert. The C-odd side, meanwhile,
# has a closed-form spectrum, a Lean theorem and two dozen checks. That
# asymmetry is not physics -- both sectors are spectra of the same incidence
# matrix -- so it is an artifact of where the verification effort went, and it
# is the largest coherent T3 hole after C2 itself.
#
# What the corpus supplies for the C-even sector is a range and an expansion:
# `lambda in [-4, 12]`, argued from positivity below and 12-regularity above
# and reported by a dense zone scan, plus `lambda = 12 - (4/3)|k|^2` near
# Gamma. On this side the only C-even geometry ever checked was two
# hand-written matrices. This suite supplies the closed form
# `mu(mu - p)^2 = 4 a_1 a_2 a_3`, and then uses it: the band edges, the
# multiplicity structure at the floor, the Gamma curvature, and the two orders
# of the band ledger all follow from that one cubic.
even_band = _suite("the charge-even band, exactly")


@even_band.check(
    "the plaquette graph is 12-regular and two faces share at most one link",
    "MASTER paper eq. (30) / UNIFIED §0.1",
)
def _():
    # The `12 leak` in the assembly is a COUNT, and THIS repository had never
    # counted it: every band value in both sectors carries twelve leakages on
    # the manuscript's say-so. The corpus does count it -- the band certificate
    # gates "every plaquette has exactly 12 shared-link neighbors" on one
    # lattice -- so what is new here is only that the number is now derived
    # inside the verification layer, from the same boundary formula torus.py
    # uses, at two extents, because a wrong count would be invisible at one.
    reports = {ell: EVEN.plaquette_degrees(ell) for ell in (3, 4)}
    ok = all(
        diag == {4} and off <= {0, 1} and degrees == {12} for diag, off, degrees in reports.values()
    )
    return ok, (
        "|d2|^T|d2| on L = 3 and L = 4: every face carries exactly 4 boundary links, "
        "every pair of distinct faces shares 0 or 1 of them, and every face has exactly "
        "12 edge-sharing neighbours — so 'twelve neighbours, one leakage each' is a "
        "count here too, not a citation, and it is the count the upper band edge "
        "lambda <= 12 rests on"
    )


@even_band.check(
    "the two Bloch incidence symbols, and the determinant asymmetry between them",
    "PAPER Thm. (incidence factorization; Gauss law)",
)
def _():
    z1, z2, z3 = EVEN.Z
    a = EVEN.a_symbols()
    unsigned, signed = EVEN.bloch_incidence(False), EVEN.bloch_incidence(True)
    determinants = (
        cancel(unsigned.det() + 2 * (1 + z1) * (1 + z2) * (1 + z3)) == 0
        and cancel(signed.det()) == 0
    )
    # Each face feeds four boundary links lying in two directions, two links
    # each, so every row of either symbol has exactly two nonzero entries --
    # and so does every column. That is the whole content of ||N||^2 <= 16.
    shape = EVEN.matrix_norm_bound() == (2, 2)
    # The Bloch Gram diagonal is a_i + a_j at orbital (i,j), NOT 4: the
    # in-plane same-orbital neighbours carry phases. Traces are the invariant
    # statement, and they are complementary.
    diagonals = all(
        cancel(EVEN.gram(False)[o, o] - (a[i - 1] + a[j - 1])) == 0
        and cancel(EVEN.gram(True)[o, o] - (8 - a[i - 1] - a[j - 1])) == 0
        for o, (i, j) in enumerate(EVEN.FACE_PAIRS)
    )
    traces = (
        cancel(sum(EVEN.gram(False)[o, o] for o in range(3)) - 2 * EVEN.p_symbol()) == 0
        and cancel(sum(EVEN.gram(True)[o, o] for o in range(3)) - 2 * EVEN.q_symbol()) == 0
    )
    return determinants and shape and diagonals and traces, (
        "read straight off d2[x;i,j] = +[x+e_i;j] - [x;j] - [x+e_j;i] + [x;i]: "
        "det B == 0 identically (a whole flat C-odd band), while "
        "det N = -2 v_1 v_2 v_3 vanishes only where some k_j = pi. Two nonzero entries "
        "per row and per column in both symbols; Gram diagonal a_i + a_j at orbital "
        "(i,j) unsigned and 8 - a_i - a_j signed, so the traces are 2p and 2q and sum "
        "to 24 at every k — the trace form of p + q = 12"
    )


@even_band.check(
    "the C-even characteristic polynomial is mu(mu - p)^2 = 4 a_1 a_2 a_3",
    "PAPER Thm. (the C-even band) states the range; the closed form is derived here",
)
def _():
    a = EVEN.a_symbols()
    even_ok = cancel(expand(EVEN.gram_charpoly(False) - EVEN.even_cubic(EVEN.MU, *a))) == 0
    odd_target = EVEN.odd_cubic(EVEN.MU, EVEN.q_symbol())
    odd_ok = cancel(expand(EVEN.gram_charpoly(True) - odd_target)) == 0
    return even_ok and odd_ok, (
        "with a_m = 2 + 2 cos k_m and p = sum a_m, the unsigned Gram matrix has "
        "charpoly mu^3 - 2p mu^2 + p^2 mu - 4 a_1 a_2 a_3 and lambda = mu - 4, exactly "
        "at every k — the C-even counterpart of the C-odd closed form, which the same "
        "computation returns as mu(mu - q)^2. Scoped claim of novelty: no closed form "
        "for this sector appears in the one-plaquette program or the flat-band papers, "
        "which record the range, the Gamma expansion and a dense zone scan"
    )


@even_band.check("p + q = 12: one zone function runs both sectors", "MASTER paper eq. (24)")
def _():
    return cancel(expand(EVEN.p_symbol() + EVEN.q_symbol())) == 12, (
        "the C-even sector's p = 4 sum cos^2(k_m/2) and the C-odd sector's "
        "q = 4 sum sin^2(k_m/2) are not two variables: p = 12 - q pointwise, so the "
        "already-checked values q = 0, 4, 8, 12 at Gamma, X, M, R are p = 12, 8, 4, 0 "
        "and the two sectors' band structures are two readings of one function"
    )


@even_band.check(
    "the C-even range [-4, 12] is exact; the top only at Gamma, the floor on three planes",
    "PAPER Thm. (incidence factorization) / ENGINE_FLUX_glueball_band_certificate_v2.py",
)
def _():
    # RETRACTED, and kept because the failure is instructive. An earlier draft
    # of this check was a FINDING asserting that the corpus argues the UPPER
    # edge nowhere -- that PAPER's theorem says "Hence lambda(k) in [-4, 12]"
    # straight after exhibiting A + 4I = N N^dagger, which gives the lower
    # edge only, and that the corpus's evidence for the top is a dense zone
    # scan. The first half is true and is checked below. The second half was
    # false, and searching the corpus for the MECHANISM rather than for the
    # value found it in two places within a minute: the band certificate gates
    # "every plaquette has exactly 12 shared-link neighbors" outright, and the
    # results note states the implication in prose -- "the C-even spectrum is
    # bounded above by 12 (12-regular graph)". A negative about a 950-file
    # corpus asserted after reading two files is exactly the failure mode
    # AGENTS.md names, and this repository is not entitled to it.
    #
    # What stands is not a finding but a proof. Both edges follow from the
    # cubic, with no scan and no appeal to regularity:
    #
    #   mu < 0  =>  mu (mu - p)^2 < 0 <= 4abc, so f(mu) < 0: no root below 0.
    #   mu > 16 =>  f'(mu) = (3mu - p)(mu - p) > 0 there, since p <= 12; and
    #               f(16) = 16(16 - p)^2 - 4abc >= 16*16 - 4*64 = 0.
    #
    # Equality at the top forces p = 12 and abc = 64, hence a = b = c = 4,
    # hence k = 0: the top is attained at Gamma and nowhere else. Equality at
    # the bottom is f(0) = 0, i.e. abc = 0, i.e. SOME k_j = pi -- the whole of
    # three planes, not one point. It is a triple root only when p = 0 too,
    # which is R alone.
    #
    # An earlier name for this check said "each edge is attained at one point
    # only". That is true at the top and false at the bottom: the predicate it
    # ran (all three eigenvalues equal -4) is the TRIPLE-root condition, not
    # attainment, and among the four high-symmetry momenta X and M attain the
    # floor too. The name asserted more than the arithmetic under it, and it
    # contradicted the sibling check next door, which had the planes right.
    paper = (
        ROOT / "corpus-import" / "papers" / "flat_band" / "PAPER_FLUX_glueball_flat_band_v1_1.tex"
    ).read_text(encoding="utf-8")
    theorem = paper[paper.index("Incidence factorization") :]
    proof = theorem[theorem.index("begin{proof}") : theorem.index("end{proof}")]
    asserts_range = "\\lambda(k)\\in[-4,12]" in theorem.replace(" ", "")
    # the proof body argues the two determinants and stops; the regularity
    # clause that carries the upper edge lives in the sister documents
    proof_argues_determinants_only = "determinant" in proof and not any(
        word in proof for word in ("regular", "degree", "Gershgorin", "norm", "bounded")
    )
    one_plaquette = ROOT / "corpus-import" / "programs" / "one_plaquette"
    certificate = (one_plaquette / "ENGINE_FLUX_glueball_band_certificate_v2.py").read_text(
        encoding="utf-8"
    )
    note = (one_plaquette / "NOTE_FLUX_glueball_band_results_v2.md").read_text(encoding="utf-8")
    corpus_support = (
        "every plaquette has exactly 12 shared-link neighbors" in certificate
        and "C-even lambda in [-4, 12], extrema attained" in certificate
        and "bounded above by 12 (12-regular graph)" in note
    )

    mu = EVEN.MU
    a, b, c = symbols("a b c", nonnegative=True)
    f = EVEN.even_cubic(mu, a, b, c)
    derivative = expand(diff(f, mu) - (3 * mu - (a + b + c)) * (mu - (a + b + c)))
    at_top = expand(f.subs(mu, 16) - (16 * (16 - (a + b + c)) ** 2 - 4 * a * b * c))
    at_bottom = expand(f.subs(mu, 0) + 4 * a * b * c)
    edges = {name: EVEN.even_lambdas(k) for name, k in EVEN.HIGH_SYMMETRY.items()}
    attains_top = [n for n, spec in edges.items() if max(spec) == 12]
    attains_floor = sorted(n for n, spec in edges.items() if min(spec) == -4)
    triple_floor = [n for n, spec in edges.items() if set(spec) == {-4}]
    ok = (
        asserts_range
        and proof_argues_determinants_only
        and corpus_support
        and derivative == 0
        and at_top == 0
        and at_bottom == 0
        and attains_top == ["Gamma"]
        and attains_floor == ["M", "R", "X"]
        and triple_floor == ["R"]
    )
    return ok, (
        "f(mu) < 0 for mu < 0 since f(0) = -4abc <= 0 and mu(mu - p)^2 < 0 there; and "
        "f'(mu) = (3mu - p)(mu - p) > 0 above p with f(16) = 16(16 - p)^2 - 4abc >= 0 "
        "because p <= 12 and abc <= 64 — so lambda in [-4, 12] exactly. The top needs "
        "a = b = c = 4 and is attained at Gamma alone; the floor needs only abc = 0 and "
        "is attained on the whole of the three planes k_j = pi — among the high-symmetry "
        f"momenta at {attains_floor}, triple at {triple_floor} where p = 0 as well. The "
        "corpus reaches the same range by a different route it does argue — the "
        "certificate gates the 12-neighbour count and the results note draws the bound "
        "from it — and reports the edges 'attained' from a dense scan; the cubic gives "
        "the attainment SETS, which a scan cannot. PAPER's theorem still states the "
        "range as a consequence of the factorization alone, and that factorization "
        "carries the lower edge only"
    )


@even_band.check(
    "the C-even band touches its floor exactly on the three planes k_j = pi",
    "PAPER Rmk. (an exactly immobile excitation)",
)
def _():
    # The sharp form of "no C-even flat band". mu = 0 is a root iff abc = 0,
    # and abc = 0 iff some k_j = pi; the root is simple unless p = 0 too,
    # which happens only at R, where it is triple. So the C-even kernel is
    # measure zero (three planes) and the C-odd kernel is a whole band --
    # PAPER's asymmetry, now with the multiplicity attached.
    a, b, c = symbols("a b c", nonnegative=True)
    mu = EVEN.MU
    constant_term = EVEN.even_cubic(mu, a, b, c).subs(mu, 0)
    # on a plane: one a_m vanishes, the cubic degenerates to mu(mu - p)^2
    on_plane = expand(EVEN.even_cubic(mu, 0, b, c) - mu * (mu - (b + c)) ** 2)
    # driven by (a_1, a_2, a_3) rather than by k, so every root stays rational:
    # a_m = 0 is the plane k_m = pi, and a_m = 3, 1 are the L = 6 momenta
    # k_m = pi/3, 2pi/3.
    multiplicities = {
        label: sum(1 for lam in EVEN.lambdas_from_abc(*abc) if lam == -4)
        for label, abc in (
            ("generic", (3, 1, 3)),
            ("one face", (0, 3, 1)),
            ("two faces", (0, 0, 3)),
            ("R", (0, 0, 0)),
        )
    }
    ok = (
        constant_term == -4 * a * b * c
        and on_plane == 0
        and multiplicities == {"generic": 0, "one face": 1, "two faces": 1, "R": 3}
    )
    return ok, (
        "f(0) = -4 a_1 a_2 a_3, so lambda = -4 occurs exactly where some k_j = pi; "
        "there the cubic degenerates to mu(mu - p)^2, giving a SIMPLE root unless "
        f"p = 0 as well, which is only the corner. Multiplicities {multiplicities}: the "
        "C-even kernel is three measure-zero planes against the C-odd kernel's whole "
        "band — and a flat C-even branch would need f(mu_0) == 0 identically, which "
        "the constant term already forbids"
    )


@even_band.check(
    "the Bloch cubic IS the finite L = 3 and L = 4 plaquette spectrum, exactly",
    "UNIFIED §0.1; the corpus checks the analogous statement numerically",
)
def _():
    # Two constructions that share nothing but the boundary formula: the
    # symbolic cubic above, and an integer plaquette adjacency built on the
    # torus. Comparing characteristic polynomials over Z settles completeness
    # of the Bloch decomposition -- every finite eigenvalue is a cubic root at
    # an allowed momentum, with multiplicity -- where an eigenvalue-list
    # comparison would need a tolerance.
    matches = {ell: EVEN.finite_charpoly(ell) == EVEN.bloch_charpoly(ell) for ell in (3, 4)}
    sizes = {ell: 3 * ell**3 for ell in matches}
    return all(matches.values()), (
        f"char poly of the {sizes[3]}x{sizes[3]} and {sizes[4]}x{sizes[4]} unsigned "
        "plaquette adjacencies equals the product of mu^3 - 2p mu^2 + p^2 mu - 4abc "
        "over all L^3 momenta, coefficient for coefficient in Z — so the closed form "
        "is complete, not merely consistent at sampled k"
    )


@even_band.check(
    "the C-even spectra at the four high-symmetry momenta",
    "MASTER paper §4.5 / PAPER Thm. (the C-even band)",
)
def _():
    spectra = {name: EVEN.even_lambdas(k) for name, k in EVEN.HIGH_SYMMETRY.items()}
    expected = {
        "Gamma": [0, 0, 12],
        "X": [-4, 4, 4],
        "M": [-4, 0, 0],
        "R": [-4, -4, -4],
    }
    return spectra == expected, (
        "Gamma {12, 0, 0} (A1++ and the E++ doublet), X {4, 4, -4}, M {0, 0, -4}, "
        "R {-4, -4, -4} — the existing check writes out Gamma and R by hand; these are "
        "roots of the one cubic, and X and M come free. Only Gamma and R are degenerate "
        "the way the sector's two band edges require"
    )


@even_band.check(
    "one assembly formula gives every C-even value at both orders",
    "ENGINE_FLUX_su3_domino_d3.py / MASTER paper eq. (30)",
)
def _():
    # constants.band_assembly existed and no check read it; the band ledger
    # check next door carries its own inline copy of the same dictionaries.
    # This reads the registry's own function, and reaches the two C-even
    # entries that copy never covered: the lambda = -4 cubic and the E++ level
    # PAPER derives from the certified band form.
    bottom, top = K.BAND_LAMBDA["even"]
    targets = [
        (K.band_assembly("even", 2, bottom), K.BAND_EVEN_BOTTOM),
        (K.band_assembly("even", 2, 0), K.D_PLUS_2),
        (K.band_assembly("even", 2, top), K.BAND_EVEN_TOP),
        (K.band_assembly("even", 3, bottom), K.M3_EVEN_K0),
        (K.band_assembly("even", 3, 0), K.M3_EVEN_EPP),
        (K.band_assembly("even", 3, top), K.M3_EVEN_BANDTOP),
    ]
    collapsed = all(
        K.band_assembly("even", r, lam) == K.band_tower("even", r) + (12 + lam) * hop
        for r, hop in ((2, K.T_PLUS_2), (3, K.T3_EVEN))
        for lam in (bottom, 0, top)
    )
    ok = all(got == want for got, want in targets) and collapsed
    return ok, (
        "E_+(lambda, r) = tower + 12 leak_{r,+} + lambda t_{r,+} reproduces all six "
        f"C-even levels: order 2 {K.BAND_EVEN_BOTTOM}, {K.D_PLUS_2}, {K.BAND_EVEN_TOP}; "
        f"order 3 {K.M3_EVEN_K0}, {K.M3_EVEN_EPP}, {K.M3_EVEN_BANDTOP}. Because "
        "leak_{r,+} = t_{r,+} the whole C-even sector collapses to "
        "tower_r + (12 + lambda) t_{r,+} — a one-parameter family, which is why the "
        "engine's regression gates read 101/200 + 24 T3e and 101/200 + 8 T3e"
    )


@even_band.check(
    "FINDING: the certificate key 'bandmin' holds the band MAXIMUM, at both orders",
    "RUN_TROM_d3_results.json vs PAPER, the §6 patch, and the arithmetic",
)
def _():
    # A label, not a number -- and this repository imported the label. The
    # engine writes the lambda = -4 endpoint under the key
    # "m3_even_bandmin (lambda=-4)"; three corpus documents call the same
    # quantity the band top, and t_{r,+} < 0 settles it, since E_+ decreases
    # in lambda and lambda runs over [-4, 12]. Recorded rather than quietly
    # fixed: the certificate keys are the join to the corpus and they still
    # say "bandmin".

    certificate = json.loads(
        (
            ROOT / "corpus-import" / "numerics" / "certificates" / "RUN_TROM_d3_results.json"
        ).read_text(encoding="utf-8")
    )
    key_order2 = "m2_even_bandmin_corrected"
    key_order3 = "m3_even_bandmin (lambda=-4)"
    from_key = {
        key_order2: Rational(certificate["order2"][key_order2]),
        key_order3: Rational(certificate["order3"][key_order3]),
    }
    paper = (
        ROOT / "corpus-import" / "papers" / "flat_band" / "PAPER_FLUX_glueball_flat_band_v1_1.tex"
    ).read_text(encoding="utf-8")
    patch = (
        ROOT
        / "corpus-import"
        / "programs"
        / "one_plaquette"
        / "PAPER_FLUX_manuscript_section6_patch.tex"
    ).read_text(encoding="utf-8")
    prose_says_top = (
        "band top $\\tfrac{1109}{3060}$" in paper
        and "C-even band-top cubic & $471353/1560600$" in patch
        and "at the band top ($\\lambda=-4$) the cubic coefficient is" in patch
    )
    edges_ordered = (
        K.T_PLUS_2 < 0
        and K.T3_EVEN < 0
        and K.BAND_EVEN_TOP > K.BAND_EVEN_BOTTOM
        and K.M3_EVEN_BANDTOP > K.M3_EVEN_K0
    )
    labels_agree = (
        from_key[key_order2] == K.BAND_EVEN_TOP and from_key[key_order3] == K.M3_EVEN_BANDTOP
    )
    return prose_says_top and edges_ordered and labels_agree, (
        f"the certificate stores {from_key[key_order2]} under '{key_order2}' and "
        f"{from_key[key_order3]} under '{key_order3}'; both are the lambda = -4 endpoint, "
        "and both exceed the lambda = 12 endpoint because t_{r,+} < 0 at r = 2 and 3. "
        "PAPER calls it 'band top', the manuscript patch tabulates it as 'C-even "
        "band-top cubic', and the certificate v2 compares the order-2 key against its "
        "own even_top. One key name against three documents and the arithmetic: the "
        "registry now reads M3_EVEN_BANDTOP, and BAND_EVEN_TOP no longer contradicts "
        "its own order-3 twin"
    )


@even_band.check(
    "the C-even Gamma point pins t_+, exactly where no C-odd Gamma datum can",
    "MASTER paper Rmk. 12 / PAPER Thm. (the C-even band)",
)
def _():
    # The counterpart of the FINDING next door. The C-odd sector is blind at
    # Gamma because the signed adjacency there is -4I: one level, so no
    # splitting to measure, and q(0) = 0 kills the hopping term outright. The
    # unsigned adjacency at Gamma is {12, 0, 0}: TWO levels, and their
    # separation is 12 t_+ at every order. So a rest-frame measurement is not
    # blind to the hopping in general -- it is blind to the C-ODD hopping, and
    # a rest-frame A1++/E++ splitting would pin the C-even one directly.
    splitting = {
        2: K.band_assembly("even", 2, 12) - K.band_assembly("even", 2, 0),
        3: K.band_assembly("even", 3, 12) - K.band_assembly("even", 3, 0),
    }
    hops = {2: K.T_PLUS_2, 3: K.T3_EVEN}
    exact = all(splitting[r] == 12 * hops[r] for r in (2, 3))
    gamma_even = EVEN.even_lambdas(EVEN.HIGH_SYMMETRY["Gamma"])
    gamma_odd = EVEN.odd_lambdas(EVEN.HIGH_SYMMETRY["Gamma"])
    structure = len(set(gamma_even)) == 2 and set(gamma_odd) == {-4}
    # the C-odd blindness, restated in the same variables: q(0) = 0
    blind = EVEN.q_symbol().subs(dict.fromkeys(EVEN.Z, 1)) == 0
    return exact and structure and blind, (
        f"A1++ minus E++ = 12 t_+ exactly: {splitting[2]} at order 2 and {splitting[3]} "
        "at order 3. The mechanism is the two incidence spectra at Gamma — unsigned "
        "{12, 0, 0} has two distinct levels, signed {-4, -4, -4} has one — so the "
        "rest-frame blindness that the C-odd FINDING records does not extend to the "
        "C-even sector. Hamer's 0++ series constrains the A1++ level alone; the E++ "
        "doublet is the second datum that would separate leak_+ from t_+"
    )


@even_band.check(
    "the C-even curvature is (4/3)|t_+| at both orders, and isotropic",
    "PAPER Thm. (the C-even band); §6 patch curvature 22/459",
)
def _():
    # PAPER states "lambda(k) = 12 - (4/3)|k|^2 + O(k^4) isotropically, hence
    # curvature +22/459" and derives the third-order correction 6335/187272
    # from the certified band form. Both are consequences of the cubic, and
    # the isotropy is a conclusion here rather than an assumption: the three
    # directional derivatives are computed separately and come back equal.
    directional = EVEN.gamma_curvature_coefficients()
    isotropic = set(directional) == {Rational(-4, 3)}
    curvatures = {
        2: Rational(4, 3) * abs(K.T_PLUS_2),
        3: Rational(4, 3) * abs(K.T3_EVEN),
    }
    ok = (
        isotropic
        and curvatures[2] == K.CEVEN_CURVATURE_2
        and curvatures[3] == K.CEVEN_CURVATURE_3
        and Rational(459, 44) == 1 / (2 * K.CEVEN_CURVATURE_2)
    )
    return ok, (
        f"d lambda/d(k_m^2) at Gamma = {directional} — equal in all three directions, so "
        "the A1++ branch is isotropic at leading order without assuming it — giving "
        f"lambda = 12 - (4/3)|k|^2 and curvature (4/3)|t_(r,+)|: {K.CEVEN_CURVATURE_2} at "
        f"order 2 and {K.CEVEN_CURVATURE_3} at order 3, hence the corpus's effective mass "
        "m* = 459/(44 u^2). The 4/3 is the cubic's Gamma expansion, not a normalization"
    )


@even_band.check(
    "the C-even bandwidth is 16|t_+| at every order; the C-odd manifold width is 12|t_-|",
    "PAPER Rmk. (an exactly immobile excitation)",
)
def _():
    # The order-2 statement is checked elsewhere from two hand-written
    # matrices. It is not a fact about order 2: the spans are properties of
    # the two incidence spectra, so the same 16 and 12 hold at every order the
    # ledger reaches. The order-3 C-even bandwidth below is not in the corpus.
    even_edges, odd_edges = K.BAND_LAMBDA["even"], K.BAND_LAMBDA["odd"]
    even_span = max(even_edges) - min(even_edges)
    odd_span = max(odd_edges) - min(odd_edges)
    widths = {
        2: K.band_assembly("even", 2, -4) - K.band_assembly("even", 2, 12),
        3: K.band_assembly("even", 3, -4) - K.band_assembly("even", 3, 12),
    }
    ok = (
        even_span == 16
        and odd_span == 12
        and widths[2] == K.BAND_EVEN_WIDTH
        and widths[2] == 16 * abs(K.T_PLUS_2)
        and widths[3] == 16 * abs(K.T3_EVEN)
        and 12 * K.T_MINUS_2 == K.BAND_ODD_WIDTH
        and Rational(15, 88) == K.BAND_ODD_WIDTH / K.BAND_EVEN_WIDTH
    )
    return ok, (
        f"C-even span 16 gives {widths[2]} at order 2 — the registered 88/153 — and "
        f"{widths[3]} at order 3, which appears nowhere in the pinned corpus; C-odd "
        "span 12 gives "
        f"{K.BAND_ODD_WIDTH}, and the manifold-width ratio 15/88 the corpus prints is "
        "the ratio of the two spans times the ratio of the two hops"
    )


@even_band.check(
    "both declared coincidences, checked: one is ell_N at all ranks, the other is bare",
    "ENGINE_FLUX_su3_domino_d3.py / MASTER paper Prop. 8",
)
def _():
    # constants.DECLARED_COINCIDENCES names two rationals this registry
    # deliberately carries under several names. A declaration is a statement
    # about intent, not about mathematics: it says the duplication is not an
    # accident, and nothing in it establishes that the values agree for a
    # reason. This check does what the declaration cannot.
    #
    # -11/306 is now explained. It is ell_3, the vacuum-route-inclusive
    # channel sum -481/612 + 3/4, which the engine also computes as the
    # second-order per-neighbour leakage in BOTH sectors -- and ell_N is an
    # all-rank closed form, so the three labels are one object at every rank,
    # not a numerical accident at N = 3.
    #
    # -6335/249696 is NOT explained, and this check does not pretend
    # otherwise: it verifies the equality and stops. The mechanism is
    # registered as the unifying candidate U4, with a falsifier, because
    # ADR 0005 is what happens when one is read off a coincidence here.
    ell_3 = K.antiparallel_sum(3) + K.parallel_sum(3) + 1 / K.casimir_fundamental(3)
    second_order = K.LEAK_2 == K.LEAK_2_EVEN == K.T_PLUS_2 == ell_3 == K.even_hopping(3)
    all_rank = simplify(
        K.even_hopping() - (K.antiparallel_sum() + K.parallel_sum() + 1 / K.casimir_fundamental())
    )
    third_order = K.LEAK_3_EVEN == K.T3_EVEN
    # the declarations and the values must not drift apart
    declared = {
        str(K.T_PLUS_2): ("LEAK_2", "LEAK_2_EVEN", "T_PLUS_2"),
        str(K.T3_EVEN): ("T3_EVEN", "LEAK_3_EVEN"),
    }
    matches_registry = {v: names for v, (names, _) in K.DECLARED_COINCIDENCES.items()} == declared
    distinct = K.T_MINUS_2 != K.LEAK_2 and K.LEAK_3 != K.B_3
    # CORRECTION, kept visible because the wrong version was printed. An
    # earlier detail line here -- and the manuscript, which copied it -- said
    # that at third order "the C-odd leakage separates from the C-odd hop".
    # It never joined it: leak_2- = -11/306 against t_2- = 5/612 at second
    # order already. What leak_2- coincides with is the C-EVEN hop, and that
    # is the pairing the third order breaks: leak_3- = -12331/249696 against
    # t_3+ = -6335/249696. Naming the wrong partner made a live coincidence
    # look like a live one between different objects, so the arithmetic is
    # asserted here rather than described.
    never_joined = K.LEAK_2 != K.T_MINUS_2 and K.LEAK_3 != K.B_3
    joined_then_parted = K.LEAK_2 == K.T_PLUS_2 and K.LEAK_3 != K.T3_EVEN
    ok = (
        second_order
        and all_rank == 0
        and third_order
        and matches_registry
        and distinct
        and never_joined
        and joined_then_parted
    )
    return ok, (
        f"leak_2- = leak_2+ = t_2+ = ell_3 = {K.T_PLUS_2} = -481/612 + 3/4, and "
        "ell_N = A_N + B_N + 1/C_F holds at symbolic N — so the first declared "
        "coincidence is one all-rank object under three names, derived rather than "
        f"observed. Only the C-odd hop stands apart ({K.T_MINUS_2}), because the vacuum "
        "route cannot reach it — and it stands apart at BOTH orders, so nothing about "
        "it 'separates' at the third. The pairing that does part is the C-odd leakage "
        f"against the C-EVEN hop: equal at r = 2 (both {K.T_PLUS_2}), unequal at r = 3 "
        f"({K.LEAK_3} against {K.T3_EVEN}). The second declared coincidence, "
        f"leak_3+ = t_3+ = {K.T3_EVEN}, survives that and is verified and unexplained, "
        "which is why it is U4 with a falsifier and not a mechanism"
    )


@even_band.check(
    "at N = 2 the C-odd hopping vanishes and the C-even one does not",
    "MASTER_THEORY §4.3; ledger/theorems.yaml (t_2 = 0)",
)
def _():
    # t_N carries the factor N^2 - 4 and vanishes at N = 2, which the corpus
    # reads as "SU(2) is excluded at the source". The C-even sector has no
    # such zero: ell_2 = -4/21. Scope, because this is a regime boundary and
    # the name of the check used to overrun it: this is a statement about the
    # two closed forms continued to N = 2, NOT about an SU(2) spectrum. SU(2)
    # representations are self-conjugate, so the charge-conjugation split that
    # defines the two sectors degenerates there and "the C-odd manifold at
    # N = 2" may name nothing. What the arithmetic does say is where the zero
    # lives: in the channel DIFFERENCE B_N - A_N, not in the incidence, which
    # is the same geometric object for both sectors at every rank.
    ratio = simplify(16 * (-K.even_hopping()) / (12 * K.hopping()))
    closed = simplify(ratio - 4 * (3 * K.N**2 - 5) / (3 * (K.N**2 - 4)))
    ok = (
        K.hopping(2) == 0
        and K.even_hopping(2) == Rational(-4, 21)
        and 16 * abs(K.even_hopping(2)) == Rational(64, 21)
        and closed == 0
        and limit(ratio, K.N, oo) == 4
        and ratio.subs(K.N, 3) == Rational(88, 15)
    )
    return ok, (
        f"t_2 = 0 while ell_2 = {K.even_hopping(2)}: continued to N = 2 the C-odd "
        "width is 0 and the C-even width is 64/21, so the N^2 - 4 zero that excludes "
        "SU(2) sits in the channel difference B_N - A_N and not in the incidence, "
        "which is rank-independent. The width ratio 16|ell_N|/(12 t_N) = "
        "4(3N^2 - 5)/(3(N^2 - 4)) is finite and > 1 at every rank N >= 3 — 88/15 at "
        "N = 3, decreasing monotonically to 4 — so the C-even band is the wider one "
        "always, and the flat-band program's asymmetry is a channel statement rather "
        "than a geometric one"
    )


@even_band.check(
    "Schur alone fixes both Gamma blocks: the C-odd triple is irreducible, the C-even one is not",
    "MASTER paper §6.3 (Where the rest frame is not blind); PAPER Prop. (C-even Gamma splitting)",
)
def _():
    # The paper argued the charge-odd rest-frame blindness from the incidence
    # ansatz -- "the hopping enters only through tau(u) q(k), and q(0) = 0" --
    # and Proposition (boundary-factorised rigidity) warns in its own remark
    # that the ansatz is not an unconditional all-orders statement. So as
    # argued, the FINDING inherited a conditionality it does not need. This
    # check removes it, using nothing but the point group.
    #
    # At Gamma the little group is the full cubic point group, so the 3x3
    # block of the effective Hamiltonian commutes with the point-group action
    # on the three plaquette orbitals -- at every order in u, and whether or
    # not the correction factors through links. Schur then decides both
    # sectors, and decides them DIFFERENTLY, which is the content:
    #
    #   C-odd: the state is the ORIENTED 2-cell e_i ^ e_j, so R acts by the
    #     second exterior power. For a proper rotation Lambda^2 R = R (the
    #     defining rep, T_1), which is irreducible -- commutant dimension 1 --
    #     so the Gamma block is a SCALAR at every order and no charge-odd
    #     rest-frame series can separate hopping from diagonal.
    #
    #   C-even: charge conjugation drops the orientation, so the state is the
    #     UNORIENTED plane and R acts by the permutation of the three axes,
    #     which is A_1 (+) E -- commutant dimension 2 -- so the Gamma block
    #     has exactly two levels and the charge-even rest frame CAN see the
    #     hopping.
    #
    # The two commutant dimensions ARE the two Gamma spectra the sectors
    # report, {-4,-4,-4} and {12,0,0}, and this check ties them together.
    import itertools

    from sympy import Matrix, eye, zeros

    def rotations():
        for perm in itertools.permutations(range(3)):
            for signs in itertools.product((1, -1), repeat=3):
                r = zeros(3, 3)
                for col, row in enumerate(perm):
                    r[row, col] = signs[col]
                if r.det() == 1:
                    yield r

    rots = list(rotations())
    pairs = list(EVEN.FACE_PAIRS)

    def odd_rep(r):
        # (R e_i) ^ (R e_j) expanded in the basis e_a ^ e_b, a < b: the 2x2 minor
        d = zeros(3, 3)
        for col, (i, j) in enumerate(pairs):
            for row, (a, b) in enumerate(pairs):
                d[row, col] = r[a - 1, i - 1] * r[b - 1, j - 1] - r[b - 1, i - 1] * r[a - 1, j - 1]
        return d

    def even_rep(r):
        # orientation dropped: the unordered plane {i,j} goes to {pi(i), pi(j)}
        return odd_rep(r).applyfunc(abs)

    def commutant_dim(reps):
        rows = []
        for d in reps:
            # vec(D X - X D) = (I (x) D - D^T (x) I) vec(X), column-major vec
            block = zeros(9, 9)
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        block[a * 3 + b, a * 3 + c] += d[b, c]
                        block[a * 3 + b, c * 3 + b] -= d[c, a]
            rows.append(block)
        stacked = Matrix.vstack(*rows)
        return len(stacked.nullspace())

    odd = [odd_rep(r) for r in rots]
    even = [even_rep(r) for r in rots]

    # The exterior square of a proper rotation IS the rotation, conjugated by
    # the Hodge duality e_1^e_2 -> e_3, e_1^e_3 -> -e_2, e_2^e_3 -> e_1. So
    # the C-odd rep is the DEFINING rep T_1, derived here rather than asserted
    # by character arithmetic.
    hodge = Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    exterior_square_is_defining = all(hodge * odd_rep(r) * hodge.inv() == r for r in rots)

    gamma = {s: EVEN.gram(s).subs({z: 1 for z in EVEN.Z}) for s in (True, False)}
    invariant = all(d * gamma[True] == gamma[True] * d for d in odd) and all(
        d * gamma[False] == gamma[False] * d for d in even
    )
    dims = (commutant_dim(odd), commutant_dim(even))
    spectra = (
        sorted((gamma[True] - 4 * eye(3)).eigenvals().keys()),
        sorted((gamma[False] - 4 * eye(3)).eigenvals().keys()),
    )
    levels = (len(spectra[0]), len(spectra[1]))
    ok = (
        len(rots) == 24
        and dims == (1, 2)
        and levels == dims
        and invariant
        and spectra == ([-4], [0, 12])
        and exterior_square_is_defining
    )
    return ok, (
        f"24 proper rotations, and the exterior square of each is the rotation itself "
        f"under Hodge duality, so the C-odd rep is the defining T_1. Its commutant has "
        f"dimension {dims[0]}; the C-even (unoriented, axis-permutation) rep has "
        f"{dims[1]}. Both commute with their sector's Gamma Gram block, and the commutant "
        f"dimensions are exactly the level counts: C-odd {spectra[0]} (one level, scalar) "
        f"against C-even {spectra[1]} (two levels). So the charge-odd rest-frame blindness "
        "is Schur's lemma on an irreducible T_1, not a consequence of the incidence "
        "ansatz -- it holds at every order and survives any correction that does not "
        "factor through links; and the charge-even sector is not blind for the same reason"
    )
