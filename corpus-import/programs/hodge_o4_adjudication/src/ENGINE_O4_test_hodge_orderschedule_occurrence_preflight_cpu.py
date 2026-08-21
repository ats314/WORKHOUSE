import json
import tempfile
import unittest
from pathlib import Path

import Hodge_O4_OrderSchedule_Occurrence_Preflight_CPU as preflight


class O4PreflightTests(unittest.TestCase):
    def test_closed_walk_boundary(self):
        o4 = preflight.enumerate_closed_layer_walks(4)
        self.assertEqual(len(o4), 9)
        self.assertEqual(preflight.walk_blocks(o4), preflight.O4_BLOCKS)
        self.assertFalse(any((2, 2) in tuple(zip(w, w[1:])) for w in o4))
        self.assertEqual(preflight.first_closed_order_with_block((2, 2)), 5)
        self.assertIn((0, 1, 2, 2, 1, 0), preflight.enumerate_closed_layer_walks(5))

    def test_exact_one_face_sensitivity(self):
        result = preflight.exact_one_face_w22_sensitivity()
        self.assertTrue(result["o4_equal"])
        self.assertEqual(result["full"][4], preflight.Fraction(-13, 896))
        self.assertEqual(result["o5_difference"], preflight.Fraction(-5, 7168))

    def test_poison_q2_access_is_never_reached(self):
        gates = preflight.GateBook()
        report = preflight.poison_access_regression(gates)
        self.assertEqual(report["applied_source_layers"], [0, 1])
        self.assertTrue(report["w22_exactly_zero"])

    def test_negative_controls_include_provenance(self):
        gates = preflight.GateBook()
        result = preflight.negative_provenance_regression(gates)
        self.assertIn("source-LXState", result["occurrence_error"])
        self.assertIn("first_closed_order", result["schedule_error"])

    def test_executed_v10a2_fixture(self):
        gates = preflight.GateBook()
        result = preflight.audit_executed_v10a2(preflight.default_v10a2_path(), gates)
        self.assertEqual(result["new_q2"], 52608)
        self.assertEqual(result["unique_canonical_networks"], 4524)
        self.assertEqual({tuple(x) for x in result["patterns"]}, preflight.APPROVED_CENTER_NEUTRAL_PATTERNS)

    def test_source_policy(self):
        gates = preflight.GateBook()
        result = preflight.self_policy_audit(gates)
        self.assertEqual(result["prohibited_symbols_present"], [])
        self.assertEqual(result["prohibited_imports_present"], [])

    def test_deterministic_quick_certificate(self):
        args = preflight.parse_args([])
        first = preflight.run(args)
        second = preflight.run(args)
        self.assertEqual(first["certificate_id"], second["certificate_id"])
        self.assertEqual(first, second)

    def test_atomic_json_output_shape(self):
        args = preflight.parse_args([])
        payload = preflight.run(args)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "certificate.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            loaded = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(loaded["status"], "PASS")
        self.assertIn("certificate_id", loaded)


if __name__ == "__main__":
    unittest.main(verbosity=2)
