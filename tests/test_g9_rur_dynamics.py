import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import g9_sixth_order_rur_census as g9


def test_carrier_defect_is_computed_with_correct_normalization():
    sym = g9.carrier_symbol_rur()
    assert sym["sigma_r"] == "-2*e2"
    assert sym["sigma_u"] == "q**2"
    assert sym["defect_rur"] == "0"
    assert sym["is_rur_carrier_projected"] is True


def test_walk_counts_do_not_claim_physical_coefficients():
    four = g9.geometric_census_length_4_paths()
    six = g9.geometric_census_length_6_cube_boundaries()
    assert four["closed"] == 90
    assert four["planar_nonretracing"] == 24
    assert four["nonplanar_nonretracing"] == 0
    assert six["nonplanar_nonretracing"] == 192
    assert "B_shp_4" not in four
    assert "activates_order_6" not in six
    with pytest.raises(NotImplementedError, match="Haar"):
        g9.compute_sixth_order_b_shp_amplitude()


def test_report_retains_unresolved_physical_support():
    result = g9.report()
    assert result["combination"]["direct_h6_supplied"] is False
    assert len(result["hermitian_h6_shifted_electric_words"]) == 18
    assert result["one_face_rooted_gap"][6] == "-2055143/35123200"
