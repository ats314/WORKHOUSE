import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import g9_sixth_order_rur_census as g9


def test_g9_carrier_symbols():
    sym = g9.carrier_symbol_rur()
    assert sym["sigma_rur"] == "4*e_2**2"
    assert sym["contains_e3"] is False
    assert sym["is_rur_carrier_projected"] is True


def test_g9_fourth_order_selection_rule():
    c4 = g9.geometric_census_length_4_paths()
    assert c4["non_planar_non_retracing"] == 0
    assert c4["B_shp_4"] == 0
    assert c4["D_shp_4"] == 0


def test_g9_sixth_order_activation():
    c6 = g9.geometric_census_length_6_cube_boundaries()
    assert c6["activates_order_6"] is True
    assert c6["non_retracing_3d_6paths"] > 0


def test_g9_full_suite():
    assert g9.run_checks() is True
