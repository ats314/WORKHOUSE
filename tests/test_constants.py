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
    # Neither fourth-order kernel may appear without its rival.
    assert "q_3 (historical)" in disputed and "m_Gamma_4 (v10a.26)" in disputed
    assert "C_shp (historical)" in disputed and "C_shp (v10a.26)" in disputed


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
        "RAW_FOLDED_AXIAL_GAMMA",
        "RUN15_APPLIED_SHIFT",
        "HAMER_A4",
        "W4_HISTORICAL",
        "W4_NEW_NUM",
        "DELTA_GAMMA",
        "DELTA_C",
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
