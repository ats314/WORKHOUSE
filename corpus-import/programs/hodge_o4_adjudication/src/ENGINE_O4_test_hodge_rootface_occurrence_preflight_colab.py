from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import tempfile
import unittest
from collections import Counter
from collections.abc import Mapping
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "ENGINE_O4_hodge_rootface_occurrence_preflight_colab.py"
NOTEBOOK = ROOT / "NB_O4_hodge_rootface_occurrence_preflight_colab.ipynb"
AUTHORITY = ROOT / "sources" / "hodge_v10a24c_RootedFullT1_DualColdOracle_O4_A100(1).py"
AUTHORITY_SHA256 = "935A3A5BA680D1373A5842486B10231D83232D8CB3393BBC250351BC51A68C8B"


def definitions(tree: ast.AST):
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.ClassDef))
    }


def assignment(tree: ast.Module, name: str) -> ast.AST:
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                return node.value
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id == name:
                return node.value
    raise KeyError(name)


def normalized_definition(node: ast.FunctionDef | ast.ClassDef) -> str:
    reparsed = ast.parse(ast.unparse(node)).body[0]
    if (
        reparsed.body
        and isinstance(reparsed.body[0], ast.Expr)
        and isinstance(reparsed.body[0].value, ast.Constant)
        and isinstance(reparsed.body[0].value.value, str)
    ):
        reparsed.body = reparsed.body[1:]
    return ast.dump(reparsed, include_attributes=False)


def exec_definitions(nodes: list[ast.AST], namespace: dict[str, Any]) -> dict[str, Any]:
    future = ast.ImportFrom(
        module="__future__", names=[ast.alias(name="annotations")], level=0,
    )
    module = ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[]))
    exec(compile(module, "<artifact-test-slice>", "exec"), namespace)
    return namespace


class FakeNDArray:
    pass


class FakeGeneric:
    def item(self):
        return self


class FakeNP:
    ndarray = FakeNDArray
    generic = FakeGeneric

    @staticmethod
    def all(value):
        return all(value)

    @staticmethod
    def isfinite(value):
        return value


class RootOccurrenceArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.text)
        cls.defs = definitions(cls.tree)
        cls.authority_text = AUTHORITY.read_text(encoding="utf-8")
        cls.authority_tree = ast.parse(cls.authority_text)
        cls.authority_defs = definitions(cls.authority_tree)

    def test_01_python_and_notebook_parse_without_gpu_request(self):
        compile(self.text, str(ARTIFACT), "exec")
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        self.assertEqual(notebook["nbformat"], 4)
        self.assertEqual(len(notebook["cells"]), 2)
        ast.parse("".join(notebook["cells"][1]["source"]))
        self.assertNotIn("gpuType", json.dumps(notebook))
        self.assertNotIn("accelerator", json.dumps(notebook).lower())

    def test_02_authority_hash_and_locator_are_exact(self):
        actual = hashlib.sha256(AUTHORITY.read_bytes()).hexdigest().upper()
        self.assertEqual(actual, AUTHORITY_SHA256)
        locator = ast.literal_eval(assignment(self.tree, "SOURCE_LOCATORS"))
        self.assertEqual(locator["authority_sha256"], AUTHORITY_SHA256)
        self.assertEqual(locator["ordered_3x3_endpoint_dispatch"], "6670-6684")
        self.assertEqual(locator["D_samepol_shortcut_crosspol_fallback"], "5658-5774")
        self.assertEqual(locator["oneface_character_certificate"], "3235-3253,5330-5358")

    def test_03_unmodified_core_definitions_are_exact_source_copies(self):
        copied = (
            "shift", "build_cubic_complex", "lx_canon", "LXState",
            "lx_trace_state", "lx_tensor_product", "lx_classes",
            "lx_merge_classes", "lx_swap_rows", "lx_opposite_reconnect",
            "lx_remove_pair", "lx_simplify_unitarity", "lx_pinv",
            "lx_pcompose", "lx_pcycles", "lx_wg_fixed",
            "lx_combine_bra_ket", "ordered_loop_steps", "face_steps_generic",
            "_joint_canon_states", "_rep_sig_from_flux", "_Hlink_action",
            "_vec_Hlink", "_project_link", "_v9_flux_key_state",
            "_v10_endpoint_patterns", "_v10a2_install_q2_haar",
            "_v10a2_energy_dyn", "_v10a2_fuse", "_v10a2_sig_dyn",
            "_v10a2_sig_conj", "_v10a2_sig_canon", "_v10a2_sig_E",
            "su3_c2_pq", "su3_fuse_fundamental", "su3_fuse_antifundamental",
            "_v10a11_oneface_axial_character",
            "_v10a3_sig_vec_add", "_v10a3_compress_state",
            "_v10a3_candidate_faces_vec", "_v10a3_project_action_dyn",
            "_v10a3_face_state", "_v10a3_face_pvec",
            "_v10a3_physical_blocks", "_v10a3_p0_catalog",
            "_v10a4_fs_model", "_v10a3_translate_state",
            "_v10a3_translate_sig", "_v17_translate_face",
            "_v17_translate_support", "_v17_add_state", "_v17_aggregate",
        )
        self.assertGreaterEqual(len(copied), 45)
        for name in copied:
            with self.subTest(name=name):
                self.assertEqual(
                    normalized_definition(self.authority_defs[name]),
                    normalized_definition(self.defs[name]),
                )

    def test_04_guarded_math_derivatives_contain_finite_firewalls(self):
        guarded = (
            "_v10a3_prune", "_v10a3_add_vec", "_v10a3_vec_inner",
            "_v10a3_vec_norm", "_v10a3_reduced_resolvent",
            "_v17_apply_W_labeled",
        )
        for name in guarded:
            with self.subTest(name=name):
                source = ast.unparse(self.defs[name])
                self.assertIn("ensure_finite", source)
        rss_source = ast.unparse(self.defs["process_rss_gib"])
        self.assertIn("RAM ceiling cannot be enforced", rss_source)
        self.assertIn("raise PreflightFailure", rss_source)
        inner_source = ast.unparse(self.defs["_v10a3_vec_inner"])
        self.assertIn("flux_key=k", inner_source)
        self.assertIn("bra_coefficient=float(ca)", inner_source)
        self.assertIn("ket_coefficient=float(cb)", inner_source)

    def test_05_tensor_and_global_constants_match_authority(self):
        for name in ("_FAST_T11", "_FAST_T22", "_FAST_EPS", "_FAST_T30",
                     "_V9_C41", "_V10A2_IMAP"):
            with self.subTest(name=name):
                self.assertEqual(
                    ast.dump(assignment(self.tree, name), include_attributes=False),
                    ast.dump(assignment(self.authority_tree, name), include_attributes=False),
                )
        self.assertEqual(ast.literal_eval(assignment(self.tree, "N")), 3)
        self.assertEqual(ast.literal_eval(assignment(self.tree, "L")), 5)
        self.assertEqual(
            ast.literal_eval(assignment(self.tree, "T1_POLS")),
            ((1, 2), (0, 2), (0, 1)),
        )

    def test_06_required_moments_are_full_and_exact(self):
        moments = ast.literal_eval(assignment(self.tree, "MOMENTS"))
        self.assertEqual(moments, (
            ("e1", "P0", "W1", "PP", True, False),
            ("K2/e2", "W1", "R1", "P1 + 1P", False, False),
            ("sigma3", "R1", "W2", "11", True, False),
            ("N", "R1", "R1", "P1 + 1P", False, False),
            ("C1", "R1", "R2", "11", False, False),
            ("J", "R1", "R12", "P1 + 1P", False, False),
            ("D", "W2", "R2", "11·11 + 12·21", False, True),
        ))
        self.assertFalse(moments[-1][4])
        matrix = ast.literal_eval(assignment(self.tree, "NONVACUITY_MATRIX"))
        self.assertEqual(set(matrix), {row[0] for row in moments})
        self.assertEqual(matrix["e1"], (
            (True, False, False), (False, True, False), (False, False, True),
        ))
        self.assertEqual(matrix["sigma3"], ((False,) * 3,) * 3)
        for moment in ("K2/e2", "N", "C1", "J", "D"):
            self.assertEqual(matrix[moment], ((True,) * 3,) * 3)

    def test_07_required_gate_manifest_is_fixed_unique_and_complete(self):
        gates = ast.literal_eval(assignment(self.tree, "REQUIRED_GATES"))
        self.assertEqual(len(gates), 23)
        self.assertEqual(len(set(gates)), 23)
        require = next(node for node in self.defs["GateBook"].body
                       if isinstance(node, ast.FunctionDef) and node.name == "require")
        finalize = next(node for node in self.defs["GateBook"].body
                        if isinstance(node, ast.FunctionDef) and node.name == "finalize")
        self.assertIn("REQUIRED_GATES[ordinal]", ast.unparse(require))
        self.assertIn("names != REQUIRED_GATES", ast.unparse(finalize))

    def test_08_full_t1_dispatch_is_all_63_ordered_units(self):
        driver = ast.unparse(self.defs["run_root_preflight"])
        self.assertIn("for ket_index in range(3)", driver)
        self.assertIn("for bra_index in range(3)", driver)
        self.assertIn("len(set(actual_units)) == 63", driver)
        self.assertLess(
            driver.index("for ket_index in range(3)"),
            driver.index("for bra_index in range(3)"),
        )
        polarizations = ((1, 2), (0, 2), (0, 1))
        faces = [((x, y, z), a, b)
                 for x in range(5) for y in range(5) for z in range(5)
                 for a, b in ((0, 1), (0, 2), (1, 2))]
        anchors = tuple(next(i for i, (v, a, b) in enumerate(faces)
                             if v == (0, 0, 0) and (a, b) == pol)
                        for pol in polarizations)
        self.assertEqual(anchors, (2, 1, 0))

    def test_09_each_left_physical_block_scans_exactly_125_translations(self):
        function = self.defs["census_unit"]
        vertex_loops = [
            node for node in ast.walk(function)
            if isinstance(node, ast.For)
            and isinstance(node.iter, ast.Call)
            and isinstance(node.iter.func, ast.Name)
            and node.iter.func.id == "enumerate"
            and isinstance(node.iter.args[0], ast.Name)
            and node.iter.args[0].id == "verts"
        ]
        self.assertEqual(len(vertex_loops), 1)
        source = ast.unparse(function)
        self.assertIn("scan_counts.append(scans_for_block)", source)
        self.assertIn("scans_for_block != len(verts)", source)
        self.assertIn("expected_translation_signature_tests", source)
        self.assertTrue({
            "_v10a3_translate_sig", "_v10a3_translate_state", "_v17_translate_support",
        }.issubset({
            node.func.id for node in ast.walk(function)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        }))

    def test_10_D_fallback_and_full_provenance_are_explicit(self):
        source = ast.unparse(self.defs["census_unit"])
        self.assertIn("d_special and len(left_support) == 1", source)
        self.assertIn("len(right_support) == 1", source)
        self.assertIn("if same_polarization", source)
        self.assertIn("samepol_oneface_skips += 1", source)
        self.assertIn("crosspol_oneface_fallback_matches += 1", source)
        self.assertIn("crosspol_oneface_fallback_candidate_blocks += 1", source)
        self.assertIn("crosspol_fallback_candidates.append", source)
        self.assertIn("cross-polarization general fallback", source)
        self.assertIn("_v10a11_oneface_axial_character", source)
        self.assertIn("same-polarization one-face matches escaped local displacement", source)
        self.assertIn("registered_analytic_contributions", source)
        self.assertLess(
            source.index("audit.inspect("),
            source.index("crosspol_oneface_fallback_matches += 1"),
        )
        inspect = ast.unparse(next(node for node in self.defs["OccurrenceAudit"].body
                                   if isinstance(node, ast.FunctionDef) and node.name == "inspect"))
        for field in ("dv", "bra_polarization_index", "ket_polarization_index",
                      "source_history_depth", "target_history_depth", "resolver_context",
                      "operator_between_endpoints", "resolver_phase",
                      "p0_projector_face", "p0_projector_geometry", "route"):
            with self.subTest(field=field):
                self.assertIn(field, inspect)
        self.assertNotIn("source_layer", inspect)
        self.assertIn("representative_key in self.representatives", inspect)
        self.assertIn("continue", inspect)

    def test_11_each_root_has_only_two_guarded_magnetic_calls(self):
        driver = self.defs["run_root_preflight"]
        calls = [
            node for node in ast.walk(driver)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "schedule"
            and node.func.attr == "apply"
        ]
        self.assertEqual(len(calls), 2)
        keywords = [{kw.arg: ast.literal_eval(kw.value) for kw in call.keywords} for call in calls]
        self.assertEqual([row["source_stage"] for row in keywords], ["P0", "R1"])
        self.assertEqual([row["target_stage"] for row in keywords], ["W1", "W2"])
        self.assertEqual([row["source_history_depth"] for row in keywords], [0, 1])
        self.assertEqual(
            [row["direct_blocks"] for row in keywords],
            [("PP", "1P"), ("P1", "11", "21")],
        )

    def test_12_guard_inspects_before_raw_contractor_with_poison_callback(self):
        namespace = {
            "Callable": Any,
            "LXState": object,
            "OccurrenceAudit": object,
            "ensure_finite": lambda name, value: (
                (_ for _ in ()).throw(RuntimeError(name))
                if isinstance(value, float) and not math.isfinite(value) else value
            ),
        }
        exec_definitions([self.defs["GuardedHaar"]], namespace)
        calls = {"raw": 0}

        class PoisonAudit:
            def inspect(self, _a, _b):
                raise RuntimeError("audit poison")

        def raw(_a, _b):
            calls["raw"] += 1
            return 1.0

        guard = namespace["GuardedHaar"](raw, PoisonAudit())
        with self.assertRaisesRegex(RuntimeError, "audit poison"):
            guard(object(), object())
        self.assertEqual(calls["raw"], 0)

        class PassAudit:
            def inspect(self, _a, _b):
                return None

        nan_guard = namespace["GuardedHaar"](lambda _a, _b: math.nan, PassAudit())
        with self.assertRaises(RuntimeError):
            nan_guard(object(), object())

    def test_13_invalid_schedule_never_calls_poison_engine(self):
        class ScheduleViolation(RuntimeError):
            pass

        class FakeAudit:
            root_faces = (2, 1, 0)
            action_log = []

            def record_action(self, **_kwargs):
                raise AssertionError("record_action must not run")

        namespace = {
            "Callable": Any,
            "Any": Any,
            "Sequence": list,
            "_v17_apply_W_labeled": lambda *_args: None,
            "ScheduleViolation": ScheduleViolation,
            "canonical_json": lambda value: json.dumps(value),
            "REQUESTED_ORDER": 4,
            "T1_POLS": ((1, 2), (0, 2), (0, 1)),
            "ALLOWED_BLOCKS": ("PP", "P1", "1P", "11", "12", "21"),
            "OccurrenceAudit": object,
            "ensure_finite": lambda _name, value: value,
        }
        exec_definitions([self.defs["MagneticSchedule"]], namespace)
        calls = {"engine": 0}

        def poison_engine(_state, _label):
            calls["engine"] += 1
            raise AssertionError("engine poison")

        schedule = namespace["MagneticSchedule"](FakeAudit(), 0, engine=poison_engine)
        with self.assertRaises(ScheduleViolation):
            schedule.apply({}, source_stage="Q2", target_stage="Q3",
                           source_history_depth=2, direct_blocks=("22",))
        self.assertEqual(calls["engine"], 0)

    def test_14_nan_mutations_fail_in_helpers_gates_prune_and_norm(self):
        class PreflightFailure(RuntimeError):
            pass

        retained = {
            "Any": Any,
            "Mapping": Mapping,
            "Fraction": Fraction,
            "np": FakeNP,
            "math": math,
            "PreflightFailure": PreflightFailure,
            "LXState": type("LXState", (), {}),
            "json": json,
            "V10A3_COEFF_TOL": 2e-13,
            "V10A3_NORM_TOL": 2e-10,
            "_v10a3_vec_inner": lambda _v, _w, _haar: math.nan,
        }
        exec_definitions([
            self.defs["ensure_finite"], self.defs["json_safe"],
            self.defs["canonical_json"], self.defs["_v10a3_prune"],
            self.defs["_v10a3_vec_norm"], self.defs["finite_max"],
        ], retained)
        with self.assertRaises(PreflightFailure):
            retained["ensure_finite"]("mutation", math.nan)
        with self.assertRaises(PreflightFailure):
            retained["canonical_json"]({"bad": math.inf})
        with self.assertRaises(PreflightFailure):
            retained["_v10a3_prune"]({object(): math.nan})
        with self.assertRaises(PreflightFailure):
            retained["_v10a3_vec_norm"]({}, None)
        with self.assertRaises(PreflightFailure):
            retained["finite_max"]("mutation.max", [1.0, math.nan])

        gate_namespace = {
            "Any": Any,
            "REQUIRED_GATES": ("g",),
            "PreflightFailure": PreflightFailure,
            "ensure_finite": retained["ensure_finite"],
            "json_safe": lambda value: value,
            "dataclass": lambda cls: cls,
        }
        exec_definitions([self.defs["GateBook"]], gate_namespace)
        gatebook = gate_namespace["GateBook"]()
        with self.assertRaises(PreflightFailure):
            gatebook.require("g", True, math.nan)

    def test_15_atomic_envelope_overwrites_stale_pass_and_rejects_nan(self):
        class PreflightFailure(RuntimeError):
            pass

        def ensure(name, value):
            if isinstance(value, float) and not math.isfinite(value):
                raise PreflightFailure(name)
            if isinstance(value, Mapping):
                for child in value.values():
                    ensure(name, child)
            if isinstance(value, (list, tuple)):
                for child in value:
                    ensure(name, child)
            return value

        namespace = {
            "Path": Path,
            "Mapping": Mapping,
            "Any": Any,
            "os": os,
            "json": json,
            "PreflightFailure": PreflightFailure,
            "ensure_finite": ensure,
            "json_safe": lambda value: value,
        }
        exec_definitions([
            self.defs["_serialized_json_bytes"], self.defs["atomic_write_json"],
        ], namespace)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "certificate.json"
            write = namespace["atomic_write_json"]
            self.assertGreater(write(path, {"status": "PASS"}), 0)
            write(path, {"status": "RUNNING"})
            write(path, {"status": "FAIL", "error": "poison"})
            self.assertEqual(json.loads(path.read_text())["status"], "FAIL")
            with self.assertRaises(PreflightFailure):
                write(path, {"status": "PASS", "bad": math.nan})
            self.assertEqual(json.loads(path.read_text())["status"], "FAIL")
            with self.assertRaises(PreflightFailure):
                write(path, {"status": "PASS", "blob": "x" * 100}, max_bytes=10)
            self.assertEqual(json.loads(path.read_text())["status"], "FAIL")

    def test_16_checkpoint_binding_and_order_fail_closed(self):
        class PreflightFailure(RuntimeError):
            pass

        def ensure(name, value):
            if isinstance(value, float) and not math.isfinite(value):
                raise PreflightFailure(name)
            if isinstance(value, Mapping):
                for child in value.values():
                    ensure(name, child)
            if isinstance(value, (list, tuple)):
                for child in value:
                    ensure(name, child)
            return value

        namespace = {
            "Path": Path,
            "Mapping": Mapping,
            "Any": Any,
            "os": os,
            "json": json,
            "PreflightFailure": PreflightFailure,
            "ensure_finite": ensure,
            "json_safe": lambda value: value,
            "canonical_json": lambda value: json.dumps(value, sort_keys=True, separators=(",", ":")),
            "sha256_text": lambda value: hashlib.sha256(value.encode()).hexdigest().upper(),
            "CHECKPOINT_SCHEMA": "hodge-full-t1-occurrence-checkpoint/v2",
            "UNIT_AUDIT_SCHEMA": "hodge-occurrence-unit/v2",
            "T1_POLS": ((1, 2), (0, 2), (0, 1)),
            "NONVACUITY_MATRIX": ast.literal_eval(
                assignment(self.tree, "NONVACUITY_MATRIX")
            ),
            "verts": tuple(range(125)),
            "math": math,
            "Counter": Counter,
        }
        exec_definitions([
            self.defs["_strict_json_load"], self.defs["_serialized_json_bytes"],
            self.defs["atomic_write_json"], self.defs["_parse_counts"],
            self.defs["_validate_representatives"],
            self.defs["_nonvacuity_expected"], self.defs["_substantive_unit_stats"],
            self.defs["_valid_same_d_route"], self.defs["_valid_cross_d_route"],
            self.defs["CheckpointStore"],
        ], namespace)
        Store = namespace["CheckpointStore"]
        def stats(unit, bra, ket):
            return {
                "unit": unit, "moment": "N",
                "bra_polarization_index": bra,
                "bra_polarization": list(namespace["T1_POLS"][bra]),
                "ket_polarization_index": ket,
                "ket_polarization": list(namespace["T1_POLS"][ket]),
                "same_polarization": bra == ket,
                "d_special_routing": False,
                "block_origin": "P1 + 1P",
                "operator_between_endpoints": False,
                "left_blocks": 1,
                "left_block_scan_counts": [125],
                "translation_signature_tests": 125,
                "expected_translation_signature_tests": 125,
                "matched_h0_support_blocks": 1,
                "raw_pair_upper": 1,
                "matched_flux_groups": 1,
                "state_pair_tests": 1,
                "local_occurrences": 1,
                "samepol_oneface_analytic_skips": 0,
                "samepol_oneface_skip_displacements": {},
                "samepol_oneface_skip_candidates": [],
                "analytic_oneface_route_certificate": None,
                "crosspol_oneface_fallback_candidate_blocks": 0,
                "crosspol_oneface_fallback_matches": 0,
                "crosspol_oneface_fallback_displacements": {},
                "crosspol_oneface_fallback_candidates": [],
                "crosspol_oneface_audited_pair_displacements": {},
            }
        def audit(unit):
            return {
                "schema": namespace["UNIT_AUDIT_SCHEMA"], "consumer": unit,
                "pair_tests": 1, "all_occurrences": {"1,1": 1},
                "center_neutral_occurrences": {"1,1": 1},
                "representatives": {
                    "1,1": {"consumer": unit, "occurrence": [1, 1]},
                },
            }
        def expected(bra, ket):
            return {
                "moment": "N", "bra_polarization_index": bra,
                "ket_polarization_index": ket,
                "same_polarization": bra == ket, "d_special_routing": False,
                "block_origin": "P1 + 1P", "operator_between_endpoints": False,
            }
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "checkpoint.json"
            store = Store(path, {"script": "A", "config": "B"}, resume=False)
            store.put("N:bra0->ket0", stats("N:bra0->ket0", 0, 0), audit("N:bra0->ket0"))
            store.put("N:bra1->ket0", stats("N:bra1->ket0", 1, 0), audit("N:bra1->ket0"))
            resumed = Store(path, {"script": "A", "config": "B"}, resume=True)
            self.assertEqual(
                resumed.completed_units(),
                ("N:bra0->ket0", "N:bra1->ket0"),
            )
            resumed.get("N:bra1->ket0", expected=expected(1, 0))
            with self.assertRaises(PreflightFailure):
                Store(path, {"script": "changed", "config": "B"}, resume=True)

            # Even a recomputed valid record/chain digest cannot hide a
            # cross-field mutation.
            document = json.loads(path.read_text())
            record = document["units"]["N:bra1->ket0"]
            record["stats"]["local_occurrences"] = 2
            record["record_sha256"] = Store._record_digest(record)
            document["chain_head_sha256"] = record["record_sha256"]
            path.write_text(json.dumps(document))
            mutated = Store(path, {"script": "A", "config": "B"}, resume=True)
            with self.assertRaises(PreflightFailure):
                mutated.get("N:bra1->ket0", expected=expected(1, 0))

            document = json.loads(path.read_text())
            record = document["units"]["N:bra1->ket0"]
            record["stats"]["local_occurrences"] = 1
            record["audit"]["representatives"] = {}
            record["record_sha256"] = Store._record_digest(record)
            document["chain_head_sha256"] = record["record_sha256"]
            path.write_text(json.dumps(document))
            missing_rep = Store(path, {"script": "A", "config": "B"}, resume=True)
            with self.assertRaises(PreflightFailure):
                missing_rep.get("N:bra1->ket0", expected=expected(1, 0))

            path.write_text('{"schema":"hodge-full-t1-occurrence-checkpoint/v2",'
                            '"binding":{},"unit_order":[],"units":{},"bad":NaN}')
            with self.assertRaises(PreflightFailure):
                Store(path, {}, resume=True)
            path.write_text('{"schema":"hodge-full-t1-occurrence-checkpoint/v2",'
                            '"binding":{},"binding":{},"unit_order":[],"units":{},'
                            '"chain_head_sha256":null}')
            with self.assertRaises(PreflightFailure):
                Store(path, {}, resume=True)

        merge_source = ast.unparse(next(
            node for node in self.defs["OccurrenceAudit"].body
            if isinstance(node, ast.FunctionDef) and node.name == "merge_unit"
        ))
        self.assertIn("pair_increment=pair_tests", merge_source)
        checkpoint_source = ast.unparse(self.defs["CheckpointStore"])
        self.assertIn("previous_record_sha256", checkpoint_source)
        self.assertIn("record_sha256", checkpoint_source)
        driver_source = ast.unparse(self.defs["run_root_preflight"])
        self.assertIn("checkpoint_prefix != expected_units[:len(checkpoint_prefix)]", driver_source)

    def test_17_notebook_is_bound_to_exact_script_hash(self):
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        code = "".join(notebook["cells"][1]["source"])
        notebook_tree = ast.parse(code)
        expected_assignment = next(
            node for node in notebook_tree.body
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "EXPECTED_SCRIPT_SHA256"
                    for target in node.targets)
        )
        expected = ast.literal_eval(expected_assignment.value)
        actual = hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper()
        self.assertEqual(expected, actual)
        notebook_gates = ast.literal_eval(assignment(notebook_tree, "EXPECTED_GATE_NAMES"))
        artifact_gates = ast.literal_eval(assignment(self.tree, "REQUIRED_GATES"))
        self.assertEqual(notebook_gates, artifact_gates)
        self.assertEqual(len(notebook_gates), 23)
        self.assertIn("file_sha256(script)", code)
        self.assertIn("--notebook-expected-script-sha", code)
        self.assertIn("--checkpoint", code)
        self.assertNotIn("--resume", code)
        self.assertIn("parse_constant=reject_constant", code)
        self.assertIn("object_pairs_hook=reject_duplicate_keys", code)
        self.assertIn("assert_finite(result)", code)
        self.assertIn("certificate_identity_material", code)
        self.assertIn("recomputed_certificate_id = value_sha256(identity)", code)
        self.assertIn("EXPECTED_GATE_NAMES", code)
        self.assertIn("gate_names == EXPECTED_GATE_NAMES", code)
        self.assertIn("checkpoint_doc.get('chain_head_sha256') == previous", code)
        self.assertIn("execution.get('resume_requested') is False", code)
        self.assertIn("result.get('promotable_pass') is True", code)
        self.assertIn("result.get(flag) is False", code)
        self.assertIn("actual_certificate_bytes", code)
        self.assertIn("exist_ok=False", code)
        self.assertIn("drive.mount", code)
        self.assertNotIn("sources/", code)

    def test_18_bootstrap_running_and_caught_failure_are_atomic(self):
        bootstrap_write = self.text.index("_bootstrap_atomic_write(_BOOTSTRAP_PATH, _bootstrap)")
        numerical_import = self.text.index("import numpy as np")
        self.assertLess(bootstrap_write, numerical_import)
        main_source = ast.unparse(self.defs["main"])
        self.assertIn("atomic_write_json(destination, running)", main_source)
        self.assertIn("except BaseException as exc", main_source)
        self.assertIn("atomic_write_json(destination, failure)", main_source)
        self.assertNotIn("wall_clock_guard", main_source)
        self.assertIn("final payload after serialization", main_source)
        self.assertIn("final payload after atomic write", main_source)
        self.assertIn("max_bytes=limits.max_payload_bytes", main_source)
        self.assertNotIn("import signal", self.text)

    def test_19_prohibited_engines_outputs_and_accelerator_requests_are_absent(self):
        lowered = self.text.lower()
        prohibited = (
            "gelfand", "factor52", "hamer", "local_shift", "unblind",
            "m4_oracle", "v23c_fit_cluster",
        )
        self.assertEqual([token for token in prohibited if token in lowered], [])
        self.assertNotIn("cupy", lowered)
        self.assertNotIn("cuda", lowered)
        allowed = ast.literal_eval(assignment(self.tree, "ALLOWED_BLOCKS"))
        forbidden = ast.literal_eval(assignment(self.tree, "FORBIDDEN_BLOCKS"))
        self.assertEqual(allowed, ("PP", "P1", "1P", "11", "12", "21"))
        self.assertEqual(forbidden, ("P2", "2P", "22"))
        policy = ast.unparse(self.defs["_static_scope_policy_report"])
        self.assertIn("not a proof of semantic absence", policy)
        self.assertNotIn("final_coefficient_or_shape_output_present", policy)

    def test_20_certificate_identity_excludes_nonstructural_runtime_floats(self):
        source = ast.unparse(self.defs["run_root_preflight"])
        identity_section = source[source.index("structural_identity ="):source.index("certificate_id =")]
        self.assertNotIn("operational_report", identity_section)
        self.assertNotIn("haar_certificate", identity_section)
        self.assertNotIn("representatives", identity_section)
        self.assertIn("environment_sha256", source)
        self.assertIn("authority_runtime_status", source)
        self.assertNotIn("checkpoint_integrity", identity_section)
        self.assertNotIn("checkpoint_chain_head", identity_section)
        self.assertNotIn("checkpoint_file_sha", identity_section)
        self.assertIn("checkpoint_structure", identity_section)
        self.assertIn("certificate_identity_material", source)
        self.assertIn("environment_fingerprint_bound", source)
        self.assertIn("exact_environment_attestation", source)
        self.assertIn("checkpoint_integrity_external_only", source)
        self.assertIn("portable_across_nonstructural_checkpoint_float_changes", source)
        self.assertIn("portable_identity_raw_float_policy", source)
        self.assertNotIn("exact_environment_bound", source)
        self.assertIn("_portable_certificate_id(structural_identity)", source)
        portable_source = ast.unparse(self.defs["_portable_certificate_id"])
        self.assertIn("contains a raw float", portable_source)
        self.assertIn("forbidden_checkpoint_keys", portable_source)

    def test_21_D_routes_are_nonvacuous_and_negative_error_fails(self):
        driver = ast.unparse(self.defs["run_root_preflight"])
        self.assertIn("len(cross_d) == 6", driver)
        self.assertIn("len(same_d) == 3", driver)
        self.assertIn("_valid_cross_d_route(stats) for stats in cross_d", driver)
        self.assertIn("_valid_same_d_route(stats) for stats in same_d", driver)

        namespace = {"Mapping": Mapping, "Any": Any, "math": math}
        exec_definitions([
            self.defs["_substantive_unit_stats"], self.defs["_valid_same_d_route"],
            self.defs["_valid_cross_d_route"],
        ], namespace)
        stats = {
            "unit": "D:bra0->ket0", "moment": "D",
            "d_special_routing": True, "operator_between_endpoints": False,
            "same_polarization": True,
            "matched_h0_support_blocks": 1,
            "samepol_oneface_analytic_skips": 1,
            "samepol_oneface_skip_displacements": {"0,0,0": 1},
            "samepol_oneface_skip_candidates": [{
                "unit": "D:bra0->ket0", "moment": "D",
                "dv": [0, 0, 0], "expected_local_dv": [0, 0, 0],
                "route": "accepted same-polarization analytic one-face certificate",
            }],
            "crosspol_oneface_fallback_candidate_blocks": 0,
            "crosspol_oneface_fallback_matches": 0,
            "crosspol_oneface_fallback_candidates": [],
            "crosspol_oneface_fallback_displacements": {},
            "crosspol_oneface_audited_pair_displacements": {},
            "analytic_oneface_route_certificate": {
                "derived_value": -13.0 / 896.0,
                "candidate_matches": 1,
                "registered_analytic_contributions": 1,
                "expected_exact_fraction": "-13/896",
                "absolute_error": -1.0,
                "local_displacement": [0, 0, 0],
            },
        }
        self.assertFalse(namespace["_valid_same_d_route"](stats))
        stats["analytic_oneface_route_certificate"]["absolute_error"] = 0.0
        self.assertTrue(namespace["_valid_same_d_route"](stats))
        stats["analytic_oneface_route_certificate"]["derived_value"] = 12.0
        self.assertFalse(namespace["_valid_same_d_route"](stats))

        cross = {
            "unit": "D:bra1->ket0", "moment": "D",
            "bra_polarization_index": 1, "ket_polarization_index": 0,
            "d_special_routing": True, "operator_between_endpoints": False,
            "same_polarization": False,
            "samepol_oneface_analytic_skips": 0,
            "samepol_oneface_skip_candidates": [],
            "samepol_oneface_skip_displacements": {},
            "analytic_oneface_route_certificate": None,
            "crosspol_oneface_fallback_candidate_blocks": 1,
            "crosspol_oneface_fallback_matches": 1,
            "crosspol_oneface_fallback_candidates": [{
                "unit": "D:bra1->ket0", "moment": "D",
                "bra_polarization_index": 1, "ket_polarization_index": 0,
                "dv": [1, 0, 0], "route": "cross-polarization general fallback",
            }],
            "crosspol_oneface_fallback_displacements": {"1,0,0": 1},
            "crosspol_oneface_audited_pair_displacements": {"1,0,0": 1},
            "matched_h0_support_blocks": 1, "matched_flux_groups": 1,
            "state_pair_tests": 1, "local_occurrences": 1,
        }
        self.assertTrue(namespace["_valid_cross_d_route"](cross))
        cross["crosspol_oneface_fallback_matches"] = 2
        cross["crosspol_oneface_audited_pair_displacements"]["1,0,0"] = 2
        self.assertFalse(namespace["_valid_cross_d_route"](cross))

    def test_22_fresh_only_promotion_and_checkpoint_hashes_are_explicit(self):
        source = ast.unparse(self.defs["run_root_preflight"])
        self.assertIn("terminal_status = 'DIAGNOSTIC_RESUME' if resume else 'PASS'", source)
        self.assertIn("resumed_units", source)
        self.assertIn("fresh_units", source)
        self.assertIn("checkpoint_chain_head", source)
        self.assertIn("checkpoint_file_sha", source)
        self.assertIn("unkeyed integrity checksums; not authenticity signatures", source)
        self.assertIn("tuple(resumed_units + fresh_units) == expected_units", source)

    def test_23_required_work_cannot_pass_vacuously(self):
        namespace = {
            "Mapping": Mapping, "Any": Any,
            "NONVACUITY_MATRIX": ast.literal_eval(
                assignment(self.tree, "NONVACUITY_MATRIX")
            ),
        }
        exec_definitions([
            self.defs["_nonvacuity_expected"], self.defs["_substantive_unit_stats"],
        ], namespace)
        empty = {
            "matched_h0_support_blocks": 0, "matched_flux_groups": 0,
            "state_pair_tests": 0, "local_occurrences": 0,
        }
        full = {key: 1 for key in empty}
        self.assertTrue(namespace["_nonvacuity_expected"]("N", 0, 0))
        self.assertFalse(namespace["_substantive_unit_stats"](empty))
        self.assertTrue(namespace["_substantive_unit_stats"](full))
        self.assertFalse(namespace["_nonvacuity_expected"]("e1", 1, 0))
        self.assertFalse(namespace["_nonvacuity_expected"]("sigma3", 2, 2))

    def test_24_checkpoint_float_mutation_changes_integrity_not_certificate_id(self):
        source = ast.unparse(self.defs["run_root_preflight"])
        identity_section = source[source.index("structural_identity ="):source.index("certificate_id =")]
        self.assertIn("checkpoint_structure", identity_section)
        self.assertNotIn("checkpoint_integrity", identity_section)
        self.assertNotIn("checkpoint_chain_head", identity_section)
        self.assertNotIn("checkpoint_file_sha", identity_section)

        namespace = {
            "Any": Any, "Mapping": Mapping, "Fraction": Fraction,
            "LXState": type("LXState", (), {}), "np": FakeNP,
            "math": math, "json": json, "hashlib": hashlib,
            "PreflightFailure": RuntimeError,
        }
        exec_definitions([
            self.defs["ensure_finite"], self.defs["json_safe"],
            self.defs["canonical_json"], self.defs["sha256_text"],
            self.defs["_portable_certificate_id"],
        ], namespace)
        canonical_json = namespace["canonical_json"]
        sha256_text = namespace["sha256_text"]
        portable_certificate_id = namespace["_portable_certificate_id"]

        def checkpoint(raw_float):
            record_body = {
                "previous_record_sha256": None,
                "unit": "N:bra0->ket0",
                "stats": {
                    "state_pair_tests": 1,
                    "nonstructural_residual_diagnostic": raw_float,
                },
                "audit": {"all_occurrences": {"1,1": 1}},
            }
            record_hash = sha256_text(canonical_json(record_body))
            return {
                "schema": "hodge-full-t1-occurrence-checkpoint/v2",
                "binding": {"script_sha256": "A" * 64},
                "unit_order": ["N:bra0->ket0"],
                "units": {
                    "N:bra0->ket0": {
                        **record_body,
                        "record_sha256": record_hash,
                    },
                },
                "chain_head_sha256": record_hash,
            }

        identity = {
            "schema": "hodge-o4-full-t1-occurrence-preflight/v4",
            "binding": {"script_sha256": "A" * 64},
            "execution": {
                "mode": "FRESH", "resumed_units": [],
                "fresh_units": ["N:bra0->ket0"],
            },
            "checkpoint_structure": {
                "schema": "hodge-full-t1-occurrence-checkpoint/v2",
                "unit_order": ["N:bra0->ket0"],
            },
            "moment_stats": {
                "N": {"N:bra0->ket0": {"state_pair_tests": 1}},
            },
        }
        checkpoint_a = checkpoint(1.0e-12)
        checkpoint_b = checkpoint(9.0e-4)
        integrity_a = sha256_text(canonical_json(checkpoint_a))
        integrity_b = sha256_text(canonical_json(checkpoint_b))
        certificate_a = portable_certificate_id(identity)
        certificate_b = portable_certificate_id(identity)

        self.assertNotEqual(
            checkpoint_a["chain_head_sha256"], checkpoint_b["chain_head_sha256"]
        )
        self.assertNotEqual(integrity_a, integrity_b)
        self.assertEqual(certificate_a, certificate_b)
        with self.assertRaises(RuntimeError):
            portable_certificate_id({**identity, "raw_diagnostic": 1.0e-12})
        with self.assertRaises(RuntimeError):
            portable_certificate_id({
                **identity,
                "checkpoint_integrity": {"file_sha256": integrity_a},
            })


if __name__ == "__main__":
    unittest.main()
