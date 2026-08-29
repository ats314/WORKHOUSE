"""The registry must stay internally consistent and honestly labelled."""

from sympy import Rational

from workhouse import constants as K


def test_registry_vocabularies_are_closed():
    for c in K.REGISTRY:
        assert c.status in K.STATUSES
        assert c.evidence in K.EVIDENCE
        assert c.source, f"{c.name} has no provenance"


def test_disputed_entries_record_both_sides():
    disputed = {c.name for c in K.REGISTRY if c.status == "disputed"}
    # C_shp is the one genuinely open pair; neither side may appear alone.
    assert "C_shp (historical)" in disputed and "C_shp (v10a.26)" in disputed


def test_the_anchor_pair_is_recorded_but_not_disputed():
    """C1 dissolved: these are differently anchored coordinates, not rivals."""
    names = {c.name: c for c in K.REGISTRY}
    assert "q_band^(4)" in names and "m_Gamma^(4)" in names
    assert names["q_band^(4)"].status != "disputed"
    assert names["m_Gamma^(4)"].status != "disputed"
    # The old collision name must not come back.
    assert not any(c.name.startswith("m_Gamma_4") for c in K.REGISTRY)


def test_scalar_shift_leaves_the_centered_operator_alone():
    """The whole reason C1 is not a dispute."""
    from sympy import Matrix, Symbol, eye, simplify, symbols, zeros

    h = Matrix(3, 3, symbols("h1:10"))
    dg, q = Symbol("dg"), Symbol("q")
    assert simplify((h + dg * eye(3)) - (q + dg) * eye(3) - (h - q * eye(3))) == zeros(3, 3)


def test_phi_c_vanishes_at_gamma_so_gamma_data_cannot_fix_delta_c():
    from sympy import Rational, limit, pi, symbols

    t, n1, n2, n3 = symbols("t n1 n2 n3", positive=True)
    assert limit(K.phi_c((t * n1, t * n2, t * n3)), t, 0) == 0
    assert K.phi_c((pi, 0, 0)) == 0  # axial cuts agree exactly
    assert K.phi_c((pi, pi, 0)) == 8  # M splits by 8*Delta_C
    assert K.phi_c((pi, pi, pi)) == 16  # R splits by 16*Delta_C
    assert K.phi_c((pi, pi / 2, 0)) == Rational(16, 3)


def test_exact_values_stay_exact_for_integer_ranks():
    assert K.hopping(3) == Rational(5, 612)
    assert K.hopping(2) == 0
    assert K.alpha_pen(3) == Rational(5, 12)
    assert K.alpha_pen(5) == Rational(1, 108)
    assert isinstance(K.dim_z2(4), type(Rational(66)))


def test_float_only_values_are_named_num():
    """A float masquerading as exact is the failure mode this guards against."""
    floats = {
        "M_GAMMA_4_NUM",
        "C_SHP_NEW_NUM",
        "A_SHP_3_NUM",
        "B_SHP_3_NUM",
        "D_SHP_3_NUM",
        "ALPHA_PEN_3_NUM",
        "RAW_FOLDED_AXIAL_GAMMA_NUM",
        "RUN15_APPLIED_SHIFT_NUM",
        "HAMER_A4_NUM",
        "W4_HISTORICAL_NUM",
        "W4_NEW_NUM",
        "DELTA_GAMMA_NUM",
        "DELTA_GAMMA_AS_PRINTED_NUM",
        "DELTA_C_NUM",
        "M_SPLIT_RECORDED_NUM",
        "R_SPLIT_RECORDED_NUM",
        "BETA_PEN_NEW_NUM",
        "SEALED_CORE_TOLERANCE",
        "HAMER_TOLERANCE",
    }
    for name in dir(K):
        if not name.isupper():
            continue
        value = getattr(K, name)
        if isinstance(value, float):
            assert name in floats, f"{name} is a bare float but not declared as one"


def test_q4_cross_derives_from_beta_pen():
    assert K.Q4_CROSS == K.BETA_PEN_3 / 4


def test_shared_values_are_declared_coincidences_not_accidental_aliases():
    """Two names on one rational must be deliberate, and say why.

    The join keys of this corpus are exact rationals, not concepts, so a value
    carried under two near-identical names is not a cosmetic wart: `workhouse
    search` returns two "different" constants and a reader can cite them as
    independent corroboration of each other. That is the same failure the
    check-id truncation collision had, one layer down.

    Distinct quantities may of course coincide -- a hopping and a leakage in
    the same sector are different objects, and recording both is the point.
    The rule is only that the coincidence be DECLARED, with a reason, in
    K.DECLARED_COINCIDENCES.

    This test exists because the registry had five undeclared aliases and did
    not know it: T_3_EVEN, D3_ODD, D3_EVEN, E_VAC3_DOMINO and D_3_TOP
    duplicated constants the block above them already carried, nothing read
    any of them, and a note review's bears_on pointed at three of the dead
    names. The registry's own prose miscounted the labels on -6335/249696 as
    a result.
    """
    import collections

    by_value = collections.defaultdict(list)
    for name in dir(K):
        if not name.isupper() or name.startswith("_"):
            continue
        value = getattr(K, name)
        # Genuine fractions only. Integer entries in this registry are counts
        # and dimensions -- two censuses landing on the same integer is not a
        # claim about anything, so requiring a declaration there would be noise.
        if isinstance(value, Rational) and value.q != 1:
            by_value[str(value)].append(name)

    shared = {v: sorted(n) for v, n in by_value.items() if len(n) > 1}
    undeclared = {v: n for v, n in shared.items() if v not in K.DECLARED_COINCIDENCES}
    assert not undeclared, (
        "constants sharing a value with no declared reason -- either the same "
        f"quantity registered twice (delete one), or not (declare it): {undeclared}"
    )

    for value, (names, reason) in K.DECLARED_COINCIDENCES.items():
        actual = sorted(names)
        assert value in shared, f"{value} is declared a coincidence but no longer shared"
        assert shared[value] == actual, (
            f"{value}: declared {actual}, registry now carries {shared[value]}"
        )
        assert len(reason.split()) >= 8, f"{value}: reason is too thin to be a reason"
