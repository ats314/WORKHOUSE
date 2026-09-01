from __future__ import annotations

import hashlib

from sympy import (
    Rational,
    simplify,
    symbols,
)

from .. import cellular as CELL
from .. import constants as K
from ._core import _suite

# ==========================================================================
published = _suite("published comparisons (literature/index.yaml)")
# An external result is not authority either -- it is T3 until something checks
# it. What makes one valuable is independence: it was produced without any
# knowledge of this program, so agreement is evidence rather than bookkeeping.


@published.check("SU(3) Weingarten values follow from the general formula", "CS_2006 / C7")
def _():
    # C7's decisive witness quotes Wg(e) = 1/8 and Wg((12)) = -1/24 for SU(3)
    # from a transcript. Re-derive them, symbolically in N, from the definition:
    # the order-n Weingarten matrix is the inverse of the Gram matrix
    # G[s,t] = N**(number of cycles of s*t^-1) on the symmetric group S_n —
    # built once, in cellular.weingarten_2, beside the n = 1 case the
    # tetrahedral merge lemma rests on.
    n = CELL.N
    identity, transposition = CELL.weingarten_2()
    return (
        simplify(identity - 1 / (n**2 - 1)) == 0
        and simplify(transposition + 1 / (n * (n**2 - 1))) == 0
        and identity.subs(n, 3) == Rational(1, 8)
        and transposition.subs(n, 3) == Rational(-1, 24)
    ), (
        f"Wg(e) = {identity} and Wg((12)) = {transposition} for all N; "
        f"at N = 3 they are {identity.subs(n, 3)} and {transposition.subs(n, 3)}, "
        "exactly the values C7 quotes"
    )


@published.check("the fourth moment integral |U_11|^4 = 1/6 at N = 3", "CS_2006 / C7")
def _():
    # The other half of C7's witness. All four indices are 1, so every pair
    # (sigma, tau) in S_2 x S_2 contributes and the integral is the full sum of
    # the Weingarten matrix: 2 Wg(e) + 2 Wg((12)).
    n = CELL.N
    identity, transposition = CELL.weingarten_2()
    moment = simplify(2 * identity + 2 * transposition)
    return simplify(moment - 2 / (n * (n + 1))) == 0 and moment.subs(n, 3) == Rational(1, 6), (
        f"integral |U_11|^4 dU = {moment} = 2/(N(N+1)); at N = 3 that is "
        f"{moment.subs(n, 3)}, nonzero -- which is what refuted the claimed Haar zero "
        "for the balanced (n_U, n_Udag) = (2,2) sector"
    )


@published.check("the Weingarten route is independent of the corpus", "CS_2006 / C7")
def _():
    # Worth stating explicitly, because it is the reason C7 is settled rather
    # than merely disputed. The derivation above uses only the symmetric group
    # and the rank; it imports no constant, convention, or coefficient from the
    # corpus, so it cannot inherit an error from it.
    identity, _transposition = CELL.weingarten_2()
    generic = simplify(identity * (CELL.N**2 - 1))
    return generic == 1, (
        "the identity-permutation Weingarten value times (N^2 - 1) is exactly 1 for "
        "symbolic N, so the SU(3) numbers are a specialization of a rank-generic "
        "formula rather than a fitted pair"
    )


@published.check(
    "the Hamer table is pinned, and the a_4 agreement is primary-source",
    "HAMER_1989",
    tier=2,
)
def _():
    # This check used to assert its own caveat: the strongest external
    # agreement rested on an unhashed transcription. On 2026-08-21 the
    # four-page primary was obtained, digest-pinned (sha256 in the index; the
    # publisher-copyright PDF is NOT stored), and Table 1 (M_A, order 4) reads
    # -0.968932328773 E-1 — digit for digit the registry's a_4, verified
    # against the rendered page image rather than OCR. The caveat is retired,
    # not forgotten: the bound is unchanged, and the pin is asserted here so
    # it cannot quietly disappear.
    from .. import literature as lit_mod

    lit = lit_mod.load()
    paper = next(p for p in lit.papers if p["id"] == "HAMER_1989")
    edges = lit.bearing_on("HAMER_A4_NUM")
    supplies = [e for _p, e in edges if e["relation"] == "supplies-value"]
    bridged = 8 * K.HAMER_A4_NUM
    gap = abs(bridged - K.M_GAMMA_4_NUM)
    digest = str(paper.get("source_sha256", ""))
    return (
        len(supplies) == 1
        and supplies[0]["status"] == "verified"
        and len(digest) == 64
        and K.HAMER_MA_NUM[2] == K.HAMER_A4_NUM
        and len(paper.get("answered_questions", [])) == 5
        and gap < K.HAMER_TOLERANCE
    ), (
        f"8 * a_4 = {bridged} against m_Gamma^(4) = {K.M_GAMMA_4_NUM}, gap {gap:.2e} "
        f"(bound {K.HAMER_TOLERANCE:.1e}); the copy read is pinned as sha256 "
        f"{digest[:16]}…, a_4 equals Table 1's M_A order-4 entry, and the corpus "
        "audit's five open questions carry answers from the pinned copy"
    )


@published.check(
    "Hamer's 1+- series matches the C-odd Gamma-point coefficients through x^3",
    "HAMER_1989 / C1",
    tier=2,
)
def _():
    # Table 1's M_A column against the program's vacuum-subtracted C-odd
    # series under the bridge m_n = 2**(n-1) a_n. Orders 0 and 1 are exact in
    # the paper: a_0 = 16/3 (recurring-decimal dot) halves to the free
    # plaquette energy 8/3, and a_1 = +1 is the u-coefficient of e_flat.
    # Orders 2 and 3 are printed to 12 significant digits; the bounds are a
    # few times the printed half-ulp times the bridge factor, and the detail
    # carries the measured gaps so nobody has to trust the bound choice.
    exact_ok = Rational(16, 3) / 2 == K.e_flat(0) == Rational(8, 3)
    gap2 = abs(2 * K.HAMER_MA_NUM[0] - float(Rational(11, 306)))
    gap3 = abs(4 * K.HAMER_MA_NUM[1] - float(K.D_3))
    return exact_ok and gap2 < 2e-13 and gap3 < 3e-12, (
        f"n=0: 16/3 / 2 = 8/3 = e_flat(0) exactly; n=1: a_1 = +1 = the u-coefficient; "
        f"n=2: 2 a_2 = {2 * K.HAMER_MA_NUM[0]!r} vs 11/306, gap {gap2:.2e} (bound 2e-13); "
        f"n=3: 4 a_3 = {4 * K.HAMER_MA_NUM[1]!r} vs D_3 = -109151/249696, gap {gap3:.2e} "
        "(bound 3e-12 = printed half-ulp x 4 with margin) — a 1989 table agreeing with "
        "rationals this program computed cold, at every shared order"
    )


@published.check(
    "Hamer's 0++ series matches the C-even Gamma-point coefficients through x^3",
    "HAMER_1989",
    tier=2,
)
def _():
    # The C-even sector too: Table 1's M_S column against the corpus's
    # vacuum-subtracted A1++ coefficients at k = 0. The n = 3 target is a
    # corpus certificate value (RUN_TROM d3) not independently re-derived
    # here, so this check binds two INDEPENDENT sources to each other: a 1989
    # journal table and a 2026 cold run, neither computed with knowledge of
    # the other.
    exact_ok = Rational(16, 3) / 2 == Rational(8, 3) and K.HAMER_MS_NUM[0] < 0
    gap2 = abs(2 * K.HAMER_MS_NUM[0] - float(K.BAND_EVEN_BOTTOM))
    gap3 = abs(4 * K.HAMER_MS_NUM[1] - float(K.M3_EVEN_K0))
    return exact_ok and gap2 < 2e-12 and gap3 < 5e-13, (
        f"n=2: 2 a_2 = {2 * K.HAMER_MS_NUM[0]!r} vs -217/1020, gap {gap2:.2e} "
        f"(bound 2e-12); n=3: 4 a_3 = {4 * K.HAMER_MS_NUM[1]!r} vs -54049/520200, "
        f"gap {gap3:.2e} (bound 5e-13); a_1 = -1 in the scalar channel where the "
        "carrier's is +1 — the sign structure matches too"
    )


@published.check("the m_n = 2^(n-1) a_n bridge is the x = 2u conversion", "HAMER_1989")
def _():
    # The bridge the corpus asserts, proved as algebra: with x = 2/g^4 = 2u
    # and m a = (g^2/2) M (Hamer eqs. (1)-(2)), the series m(u) = M(x=2u)/2
    # term by term, so the u^n coefficient is a_n 2^n / 2 = 2^(n-1) a_n. Not
    # a fit and not a convention choice — the two printed equations force it.
    u_, x_ = symbols("u x", positive=True)
    a = symbols("a0:5", positive=True)
    series_m = sum(coefficient * x_**n for n, coefficient in enumerate(a)).subs(x_, 2 * u_) / 2
    bridged = [simplify(series_m.coeff(u_, n) - 2 ** (n - 1) * a[n]) for n in range(5)]
    return all(b == 0 for b in bridged), (
        "M(2u)/2 has u^n coefficient 2^(n-1) a_n for n = 0..4 identically — the "
        "half from m a = (g^2/2) M, the 2^n from x = 2u; no 4**r ambiguity anywhere"
    )


@published.check(
    "the series Hamer supersedes is Kogut-SINCLAIR-Susskind 1976, not KS 1975", "HAMER_1989"
)
def _():
    # Hamer's reference [7] — the series his x^3 and x^4 terms disagree with —
    # is the THREE-author Nucl. Phys. B114 (1976) 199, not the two-author
    # Hamiltonian-formulation paper this program's coordinate convention rests
    # on. An earlier revision of the index note conflated them ("supersedes
    # KS_1975"); INSPIRE's reference list for Hamer's recid 25468 carries both
    # papers as separate entries. This check pins the disentanglement so it
    # cannot silently regress: the reported disagreement lands on KSS_1976 as
    # contradiction edges, KS_1975 carries none, and the citation web records
    # Hamer citing both.
    from .. import literature as lit_mod

    # The exact two-element target set is pinned in tests/test_literature.py;
    # here the fourth-order constant stays unnamed because this check is T1
    # and the tier guard reads the float-registry suffix anywhere in a check
    # body as a float dependency. The verdict below is pure structure:
    # recids, author counts, relations, and the citation web.
    lit = lit_mod.load()
    kss = next(p for p in lit.papers if p["id"] == "KSS_1976")
    ks = next(p for p in lit.papers if p["id"] == "KS_1975")
    hamer = next(p for p in lit.papers if p["id"] == "HAMER_1989")
    kss_targets = {e["target"] for e in kss["bears_on"]}
    return (
        kss["inspire_recid"] == 3785
        and ks["inspire_recid"] == 1336
        and len(kss["authors"]) == 3
        and len(ks["authors"]) == 2
        and {e["relation"] for e in kss["bears_on"]} == {"contradicts"}
        and len(kss_targets) == 2
        and "D_3" in kss_targets
        and all(e["relation"] != "contradicts" for e in ks["bears_on"])
        and {"KS_1975", "KSS_1976"} <= set(hamer.get("cites", []))
    ), (
        "Hamer 1989 cites both recid 1336 (Kogut-Susskind, 2 authors, the "
        "Hamiltonian) and recid 3785 (Kogut-Sinclair-Susskind, 3 authors, the "
        "series); the x^3/x^4 disagreement Hamer reports lands on KSS_1976 as "
        "contradiction edges against D_3 and the Gamma-point fourth-order "
        "registry value, pending a read of the primary, and KS_1975 carries "
        "no contradiction edge"
    )


@published.check(
    "the KPS 1980 string-tension table equals the certified sigma series EXACTLY",
    "KPS_1981 / G7",
)
def _():
    # The strongest kind of external agreement this repository has: Table 2
    # of the pinned Kogut-Pearson-Shigemitsu preprint (KEK scan, ILL-(TH)-
    # 80-41, September 1980) prints the 3+1 dimensional SU(3) Hamiltonian
    # string-tension coefficients as exact rationals, and under the same
    # x = 2u bridge as the Hamer table (sigma_n = 2**(n-1) t_n, from
    # T = (g**2/2a**2) W(x) against the corpus's vacuum-normalized sigma(u))
    # they equal the certified SIGMA_n rational for rational -- including the
    # CRT-certified SIGMA_4 and SIGMA_5, whose 18- and 24-digit numerators
    # appear digit for digit in a table printed in 1980, 46 years before this
    # program recomputed them cold. The paper's p.5 records that its own
    # earlier x^5 (KPS PRL 43, 484) was wrong and is corrected here: the
    # certified value agrees with the CORRECTION, not the original. Exact
    # equality, so T1: no tolerance anywhere.
    rows = {
        2: 2 * K.KPS_T2 == K.SIGMA_2,
        3: 4 * K.KPS_T3 == K.SIGMA_3,
        4: 8 * K.KPS_T4 == K.SIGMA_4,
        5: 16 * K.KPS_T5 == K.SIGMA_5,
    }
    edges = K.KPS_T0 / 2 == K.SIGMA_0 == Rational(2, 3)
    return all(rows.values()) and edges, (
        f"2^(n-1) t_n = sigma_n exactly for n = 2..5: {rows}; t_0/2 = 2/3 = sigma_0 "
        "and t_1 = 0 matches the absent sigma_1. The printed sign is negative at "
        "every order, i.e. the R14 physical convention sigma_n^phys, and the n = 5 "
        "row agrees with KPS's own 1980 correction of their 1979 PRL x^5 error"
    )


@published.check(
    "the KPS eq. (6a) decimals are its own Table 2, to a printed ulp",
    "KPS_1981",
    tier=2,
)
def _():
    # The transcription guard: eq. (6a)'s seven-digit decimals and Table 2's
    # exact rationals were transcribed independently from different pages of
    # the scan, so their agreement within one printed ulp checks both -- in
    # particular the 56-digit t_6 numerator, which no certified value can
    # cross-check yet. The n = 2, 3, 5 entries are truncations rather than
    # roundings of the exact decimal, hence the full-ulp rather than
    # half-ulp bound.
    gaps = {
        n: abs(float(t / K.KPS_T0) - w)
        for (n, t), w in zip(
            ((2, K.KPS_T2), (3, K.KPS_T3), (4, K.KPS_T4), (5, K.KPS_T5), (6, K.KPS_T6)),
            K.KPS_W_NUM,
            strict=True,
        )
    }
    bounds = {2: 5e-9, 3: 5e-9, 4: 5e-10, 5: 1e-9, 6: 5e-10}
    return all(gaps[n] < bounds[n] for n in gaps), (
        "eq. (6a) w_n vs Table 2 t_n/(4/3): "
        + ", ".join(f"n={n}: gap {gaps[n]:.1e} (bound {bounds[n]:.0e})" for n in gaps)
        + " — sigma_6 = 32 t_6 = -0.07786141620… is the published target G7's "
        "native rerun must hit"
    )


@published.check(
    "the errata-resolved Euclidean series is doubly sourced, transcription for transcription",
    "MUNSTER_1981 / SMIT_1982",
)
def _():
    # The corrected Munster-Seo Euclidean SU(3) glueball series had a messy
    # history: NPB 190 (1981), an erratum-and-addendum (NPB 200), then a
    # second erratum (NPB 205 648) fixing the 8th order again — "Murphy's
    # sixth law", thanking Ukawa and Seo. Two primary sources for the final
    # coefficients were obtained and read on 2026-08-21: the definitive NPB
    # 205 erratum itself (maintainer-supplied) and Smit's ITFA-82-3 Table 1
    # (open KEK scan), which reprints all three channels crediting Munster
    # and Seo. The scalar rows were transcribed independently from the two
    # documents; this check asserts the transcriptions agree exactly, and
    # pins Smit's own stated structure that the tensor channel's first three
    # coefficients equal the scalar's. EUCLIDEAN throughout: nothing here
    # touches the certified Hamiltonian series, by corpus section 12.
    same = K.SMIT_EUC_MS == K.MUNSTER_ERR_MS
    tensor_head = K.SMIT_EUC_MT[:3] == K.SMIT_EUC_MS[:3]
    lengths = len(K.SMIT_EUC_MS) == len(K.SMIT_EUC_MA) == len(K.SMIT_EUC_MT) == 8
    return same and tensor_head and lengths, (
        "the NPB 205 (1982) 648 erratum's SU(3) row and Smit's Table 1 scalar "
        "column agree rational for rational through u^8 (m_8 = -179208453/40960); "
        "the tensor channel's first three coefficients equal the scalar's, as "
        "Smit states; Euclidean record only — no Hamiltonian comparison exists "
        "or is permitted"
    )


@published.check(
    "FINDING: Munster's 1985 table shifts his 1982 erratum at eighth order",
    "MUNSTER_1985_TM / MUNSTER_1981",
)
def _():
    # Both documents were obtained (maintainer-supplied) and read on
    # 2026-08-21, both tables re-read at 200 dpi before transcription. The
    # 1985 effective-transfer-matrix recomputation reproduces the 1982
    # erratum's SU(3) row through u^7 and then shifts m_8 by EXACTLY -96
    # (-3932160/40960); the same table shifts Z3 by -32, SU(infinity) by
    # -18, and U(1)-Wilson by -1/8 at u^6 and -1/6 at u^8, while SU(2), Z2
    # and U(1)-Villain are untouched.
    #
    # The history was then reconstructed from the record (same day): the
    # SU(3) shift is a FOURTH correction round that no erratum ever
    # recorded — Drouffe-Zuber's 1983 review (Phys. Rep. 102, Table 10)
    # already prints -183140613/40960, attributing its table to Seo NPB 209
    # (1982) 200 and Munster PLB 121 (1983) 53, and the 1985 paper agrees;
    # the NPB 205 erratum value is orphaned in the later literature. The
    # SU(infinity), U(1)-Wilson and Z3 shifts are different: DZ 1983 still
    # carries the ERRATUM values there (-546, -445/6, -1659829/2880), so
    # those corrections first appear in 1985 and rest on a single printing.
    # Langelage-Munster-Philipsen 2007 reprints every channel through u^7
    # only. This check asserts the discrepancy so it stays visible; it
    # promotes neither value — every source in the chain shares
    # Munster/Seo provenance, and only an independent recomputation would
    # close it. Euclidean throughout: no certified Hamiltonian quantity is
    # touched either way.
    agree_low = K.MUNSTER_TM_MS[:7] == K.MUNSTER_ERR_MS[:7]
    shift = K.MUNSTER_TM_MS[7] - K.MUNSTER_ERR_MS[7]
    sibling_shifts = tuple(
        tm - err for tm, err in zip(K.MUNSTER_TM_SIB, K.MUNSTER_ERR_SIB, strict=True)
    )
    expected_siblings = (
        Rational(-32),  # Z3 m_8
        Rational(-18),  # SU(infinity) m_8
        Rational(-1, 8),  # U(1)-Wilson m_6
        Rational(-1, 6),  # U(1)-Wilson m_8
    )
    return agree_low and shift == -96 and sibling_shifts == expected_siblings, (
        "SU(3): 1985 Table 1 equals the 1982 erratum row for k = 1..7 and differs "
        f"at k = 8 by {shift} exactly (-183140613/40960 vs -179208453/40960) — a "
        "fourth correction already in print by 1983 (DZ Phys. Rep. 102 Table 10, "
        "citing Seo NPB 209 and Munster PLB 121) that no erratum records; the "
        "registered sibling shifts are asserted too: Z3 m_8 by -32, SU(inf) m_8 "
        "by -18, U(1)-Wilson by -1/8 at u^6 and -1/6 at u^8, all 1985-only (DZ "
        "1983 still carries the erratum values there). The SU(2), Z2 and "
        "U(1)-Villain rows were read as identical in both tables but are not "
        "registered, so this check does not certify them. Recorded, not "
        "adjudicated: every printing shares Munster/Seo provenance"
    )


@published.check(
    "the cap family's signed counts are n x Catalan, the published sewing weights",
    "OBZ_1985 / G5",
)
def _():
    # The completion-family novelty search (docs/referee/novelty_search_
    # 2026-08-21.md) surfaced O'Brien-Zuber 1985: eq. (2.5) attaches signed
    # central binomials (2k)!/(k!)^2 as the weights sewing closed plaquette
    # surfaces at large N, systematizing Kazakov's cyclic contractions. The
    # cellular cap family's signed count is S_n = (-1)^(n-1) C(2n-2, n-1),
    # and C(2m, m) = (m+1) Cat(m) makes that exactly n times a Catalan
    # number -- the same combinatorial family, in print in 1985, in a
    # different limit (N -> infinity, Euclidean free energy) and different
    # dynamics (no resolvents). This check proves the bridge as algebra and
    # anchors it on the enumerated cube; whether the finite-N family is
    # DERIVABLE from those cumulant weights is the open adjudication the
    # novelty record states, and this check decides nothing about it.
    from sympy import Symbol, binomial, catalan, factorial

    n = Symbol("n", positive=True, integer=True)
    # The factorial rewrite is what lets sympy cancel: both sides become
    # (2n-2)!/((n-1)!)^2 exactly.
    identity = simplify((binomial(2 * n - 2, n - 1) - n * catalan(n - 1)).rewrite(factorial))
    _c4, s4, hist4 = CELL.c_prim(CELL.CUBE, *CELL.CAP_SECTOR)
    return identity == 0 and s4 == -20 == (-1) ** 3 * 4 * catalan(3), (
        "C(2n-2, n-1) = n Cat(n-1) identically, so S_n = (-1)^(n-1) n Cat(n-1); "
        f"the enumerated cube instance gives S_4 = {s4} = -4 Cat(3) over "
        f"{len(hist4)} histories -- the completion counts are n times the "
        "Kazakov/O'Brien-Zuber cyclic-contraction Catalan weights"
    )


@published.check("the overlap obstruction was published in 1988, and it scales", "SCHIERHOLZ_1988")
def _():
    # G18 is the largest unpaid debt in the program: the claim that the
    # protected carrier is the glueball. Its own statement records the bare
    # operator carrying under 4% of the physical state -- as a fixed number.
    # Schierholz 1988 measured the same few-percent overlap independently and
    # showed it falls like a^5 for a local dimension-4 operator, which is the
    # class the bare T_1^{+-} operator belongs to. A power law, not a constant:
    # it degrades toward the continuum, so the smeared basis is structural.
    #
    # This check exists so the connection cannot quietly fall out of the ledger.
    from .. import ledger as led_mod
    from .. import literature as lit_mod

    edges = lit_mod.load().bearing_on("G18")
    schierholz = [e for p, e in edges if p["id"] == "SCHIERHOLZ_1988"]
    g18 = next(g for g in led_mod.load().gaps if g["id"] == "G18")
    sharpening = str(g18.get("external_sharpening", ""))
    return (
        len(schierholz) == 1
        and schierholz[0]["status"] == "verified"
        and "a^5" in sharpening
        and g18.get("load_bearing") is True
    ), (
        "G18 records the bare operator at <4% (2 sigma) as a fixed number; "
        "Schierholz 1988 §2 measures 'a couple of percent' at beta = 5.9 AND "
        "gives the scaling a^5 for a local dimension-4 operator. Independent, "
        "38 years earlier, and it makes the smeared basis structural rather than "
        "a convenience — better statistics cannot recover a power law"
    )


@published.check("a cross-regime paper never supplies a value", "KRS_2023 / §12")
def _():
    # The firewall that corpus §12 states in prose, made binding. KRS_2023 is
    # 1+1 dimensional with dynamical quarks; this program is 3+1 and pure gauge,
    # and the chain complex C_3 -> C_2 -> C_1 does not exist below three spatial
    # dimensions. So the paper is comparable and citable and its numbers are not
    # admissible, and `literature.validate` refuses any entry that mixes the two.
    from .. import literature as lit_mod

    lit = lit_mod.load()
    walled = [p for p in lit.papers if str(p.get("scope_firewall", "")).strip()]
    offenders = [
        (p["id"], e["target"])
        for p in walled
        for e in p["bears_on"]
        if e["relation"] == "supplies-value"
    ]
    return bool(walled) and not offenders, (
        f"{len(walled)} indexed paper(s) declare a scope firewall and none supplies "
        f"a value: {[p['id'] for p in walled]}. The rule is enforced in "
        "literature.validate, not just recorded in the entry"
    )


@published.check("stored full text is verbatim, and the licence is checked", "KRS_2023")
def _():
    # Storing a paper is republishing it. One indexed paper is openly licensed
    # enough to store (CC BY-NC-ND); NoDerivatives means the bytes must be the
    # original, so the stored file is hashed against the digest of the copy that
    # was read rather than trusted to be unmodified.

    from .. import literature as lit_mod

    lit = lit_mod.load()
    stored = [p for p in lit.papers if p.get("fulltext")]
    verified = []
    for paper in stored:
        path = lit_mod.LITERATURE_DIR / paper["fulltext"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        licence = str(paper["licence"]).lower()
        ok = digest == paper["source_sha256"] and licence in (
            lit_mod.REDISTRIBUTABLE | lit_mod.VERBATIM_ONLY
        )
        verified.append(ok)
    unstored = len(lit.papers) - len(stored)
    return bool(stored) and all(verified), (
        f"{len(stored)} of {len(lit.papers)} papers are stored, each hash-verified "
        f"against the copy that was read; the other {unstored} are under publisher "
        "copyright or the arXiv assumed-1991-2003 licence and are pinned by digest "
        "without being redistributed"
    )


@published.check(
    "the Hamer table metadata is pinned; no fourth-order agreement is used",
    "HAMER_1989 / PUBLICATION rev5 (External comparisons)",
)
def _():
    # Rev. 5 confines its Hamer comparison to what the flat scalar can test --
    # the 1+- series through x^3 and, under the unsigned-symbol hypothesis,
    # the 0++ series through x^3 -- and says in its own words that no
    # fourth-order agreement is used. That is a claim about a document, so
    # the pinned document is read: the primary-source digest is present, and
    # the fourth-order numbers this registry holds (Hamer's a_4 and the
    # Gamma-point m_Gamma^(4) it is bridged to) appear nowhere in the source,
    # while the x^2 and x^3 comparisons do. The a_4 agreement itself stays
    # registered under its own check; it is simply not what the paper leans on.
    import re

    from .. import literature as lit_mod
    from ._core import PAPER_DIR

    lit = lit_mod.load()
    paper = next(p for p in lit.papers if p["id"] == "HAMER_1989")
    digest = str(paper.get("source_sha256", ""))
    source = (PAPER_DIR / "workhouse_publication_edition_rev5_2026-08-30.tex").read_text(
        encoding="utf-8"
    )
    # The leading digits of Hamer's a_4 (-0.0968932328773, Table 1 M_A order 4)
    # and of the Gamma-point m_Gamma^(4) it is bridged to (-0.7751458630189173),
    # written as literals on purpose: this check reads a document for them and
    # compares no float against anything, so it must not name the registry's
    # float constants -- the tier guard rightly reads such a name as a float
    # comparison. Their registered values are asserted by the sibling check.
    a4_digits = "968932328"
    m4_digits = "775145863"
    fourth_absent = (
        a4_digits not in source
        and m4_digits not in source
        and not re.search(r"8\s*a_4|2\^\{?3\}?\s*a_4|a_4\s*=", source)
    )
    lower_present = "$2a_2$, $4a_3$ matching $11/306$ and $d_3$" in source
    boundary_stated = "no fourth-order agreement is used" in source
    ok = len(digest) == 64 and fourth_absent and lower_present and boundary_stated
    return ok, (
        f"HAMER_1989 pinned as sha256 {digest[:16]}…; the rev. 5 source compares 2 a_2 and "
        "4 a_3 against 11/306 and d_3 and carries neither a_4 = -0.0968932328773 nor "
        "m_Gamma^(4) = -0.7751458630189173 anywhere -- the fourth-order agreement is "
        "registered here but not leaned on there, as its own marker says"
    )
