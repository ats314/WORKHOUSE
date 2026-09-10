import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import g19_rough_gauge_coercivity as g19


def test_g19_bochner_identity():
    assert g19.verify_bochner_identity_symbolic() is True


def test_g19_scale_hierarchy():
    results = g19.verify_scale_hierarchy([2, 3, 4, 8])
    for r in results:
        assert r["ratio_gt_one"] is True
        assert r["rho_pos"] is True
        assert r["kappa_pos"] is True


def test_g19_full_suite():
    assert g19.run_checks() is True
