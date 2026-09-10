import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import g17_alpha_dependent_kp_check as g17


def test_g17_coordination_numbers_and_formulas():
    assert g17.compute_plaquette_coordination(3) == {"dim": 3, "D_edge": 12, "D_vertex": 32}
    assert g17.compute_plaquette_coordination(4) == {"dim": 4, "D_edge": 20, "D_vertex": 72}
    for d in [2, 3, 4, 5]:
        c = g17.compute_plaquette_coordination(d)
        assert c["D_edge"] == 4 * (2 * d - 3)
        assert c["D_vertex"] == 8 * ((d - 1) ** 2)


def test_g17_alpha_dependent_certificate_suite():
    assert g17.run_checks() is True
