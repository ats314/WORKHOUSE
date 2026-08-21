"""Cheap tests for the bounded exact SU(3) marked-cluster Phase-1 scaffold."""

from __future__ import annotations

import unittest
import hashlib
from fractions import Fraction
from pathlib import Path

import Hodge_SU3_Exact_MarkedCluster_m4_Colab as h


class ExactStateCoreTests(unittest.TestCase):
    def test_fraction_boundary_rejects_float(self) -> None:
        with self.assertRaises(TypeError):
            h.as_fraction(0.5)

    def test_free_unitarity(self) -> None:
        state = h.trace_state(((0, 1), (0, -1)))
        factor, reduced = h.simplify_unitarity(state)
        self.assertEqual(factor, Fraction(3))
        self.assertEqual(reduced, h.EMPTY_STATE)

    def test_one_face_h0_and_gram(self) -> None:
        face = h.trace_state(((0, 1), (1, 1), (2, -1), (3, -1)))
        self.assertEqual(h.h0_action(face), {face: Fraction(8, 3)})
        self.assertEqual(h.haar_inner(face, face), Fraction(1))


class ExactHaarRouterTests(unittest.TestCase):
    def test_router_recognizes_exact_nine_family_allowlist(self) -> None:
        for counts in h.CONSTRUCTION_MANIFEST["haar_allowlist"]:
            with self.subTest(counts=counts):
                self.assertEqual(h.DEFAULT_HAAR_ROUTER.classify(*counts).value, counts)

    def test_triality_mismatch_is_exact_zero(self) -> None:
        self.assertIsNone(h.DEFAULT_HAAR_ROUTER.classify(2, 0))
        partition = tuple(range(4))
        self.assertEqual(h.contract_link_partition(partition, (0, 1), ()), {})

    def test_unknown_zero_triality_family_fails_closed(self) -> None:
        with self.assertRaises(h.UnsupportedHaarFamily):
            h.DEFAULT_HAAR_ROUTER.classify(4, 4)

    def test_poison_families_hard_fail(self) -> None:
        for counts in ((2, 5), (5, 2)):
            with self.subTest(counts=counts):
                with self.assertRaises(h.ForbiddenHaarFamily):
                    h.DEFAULT_HAAR_ROUTER.classify(*counts)

    def test_pure_six_exact_projector_and_endpoint_adapter(self) -> None:
        gates = h.pure_six_exact_gates()
        self.assertEqual(gates["partition_count"], 10)
        self.assertEqual(gates["gram_rank"], 5)
        self.assertTrue(gates["tight_frame"])
        self.assertTrue(gates["mp_GGpG"])
        self.assertTrue(gates["mp_pGpGp"])
        self.assertTrue(gates["projector_symmetric"])
        self.assertTrue(gates["projector_idempotent"])
        self.assertEqual(gates["projector_trace"], 5)
        self.assertEqual(gates["delta_branch_count"], 456)
        self.assertEqual(gates["dsu_term_count"], 456)
        for u, ubar in ((tuple(range(6)), ()), ((), tuple(range(6)))):
            result = h.contract_link_partition(tuple(range(12)), u, ubar)
            self.assertTrue(result)
            self.assertTrue(all(isinstance(value, Fraction) for value in result.values()))

    def test_poison_fails_with_provenance_before_contractor(self) -> None:
        calls = []
        request = h.HaarRouteRequest(
            2, 5, "W2", "Q1", "Q2", "source-state", "target-state",
            "link-17", "h0-key", "flux-key", "unit-control",
        )
        with self.assertRaises(h.ForbiddenHaarFamily) as caught:
            h.DEFAULT_HAAR_ROUTER.route(
                request,
                lambda _family: calls.append("called"),
            )
        self.assertEqual(calls, [])
        self.assertEqual(set(caught.exception.provenance), {
            "operation", "source_layer", "target_layer", "source_state",
            "target_state", "link", "h0_key", "flux_key", "configuration",
        })

    def test_balanced_projectors_are_exact(self) -> None:
        for degree in (1, 2, 3):
            permutations, inverse = h.balanced_weingarten(degree)
            gram = h.fraction_matrix([[
                h.N ** h.permutation_cycles(
                    h.permutation_compose(h.permutation_inverse(left), right)
                )
                for right in permutations
            ] for left in permutations])
            with self.subTest(degree=degree):
                self.assertEqual(
                    h.fraction_matrix_multiply(gram, inverse),
                    h.fraction_identity(len(permutations)),
                )

    def test_determinant_projector_anchor(self) -> None:
        cubic_trace = h.trace_state(((0, 1), (0, 1), (0, 1)))
        self.assertEqual(h.haar_inner(h.EMPTY_STATE, cubic_trace), Fraction(1))

    def test_every_exact_ready_family_reaches_fraction_contractor(self) -> None:
        for n_u, n_ubar in (
            (1, 1), (2, 2), (3, 3), (3, 0), (0, 3), (4, 1), (1, 4),
            (6, 0), (0, 6)
        ):
            total = n_u + n_ubar
            result = h.contract_link_partition(
                tuple(range(2 * total)),
                tuple(range(n_u)),
                tuple(range(n_u, total)),
            )
            with self.subTest(counts=(n_u, n_ubar)):
                self.assertTrue(result)
                self.assertTrue(all(isinstance(value, Fraction) for value in result.values()))

    def test_mixed_projector_exact_identities(self) -> None:
        gram = h.fraction_matrix(h.MIXED_41_GRAM)
        inverse = h.fraction_matrix(h.MIXED_41_PSEUDOINVERSE)
        self.assertEqual(h.fraction_matrix_rank(gram), 3)
        gram_inverse = h.fraction_matrix_multiply(gram, inverse)
        inverse_gram = h.fraction_matrix_multiply(inverse, gram)
        self.assertEqual(h.fraction_matrix_multiply(gram_inverse, gram), gram)
        self.assertEqual(h.fraction_matrix_multiply(inverse_gram, inverse), inverse)
        self.assertEqual(sum(gram_inverse[index][index] for index in range(4)), 3)


class CanonicalScheduleTests(unittest.TestCase):
    def make_schedule(self):
        calls: list[str] = []
        schedule = h.CanonicalFourthOrderSchedule(
            lambda value: calls.append("W(P)") or value + 1,
            lambda value: calls.append("R1") or value + 1,
            lambda value: calls.append("W(Q1)") or value + 1,
            lambda value: calls.append("R2") or value + 1,
        )
        return schedule, calls

    def test_only_canonical_path_runs(self) -> None:
        schedule, calls = self.make_schedule()
        result = schedule.run(h.P(0))
        self.assertEqual(result, h.R2(4))
        self.assertEqual(
            schedule.trace,
            ("P->W1", "W1->R1(Q1)", "R1(Q1)->W2", "W2->R2(Q2)"),
        )
        self.assertEqual(calls, ["W(P)", "R1", "W(Q1)", "R2"])

    def test_w_q2_is_rejected_before_backend_call(self) -> None:
        schedule, calls = self.make_schedule()
        q2 = schedule.run(h.P(0))
        before = tuple(calls)
        with self.assertRaises(h.WOnQ2Forbidden):
            schedule.apply_w(q2)
        self.assertEqual(tuple(calls), before)

    def test_out_of_order_stage_is_poisoned(self) -> None:
        schedule, calls = self.make_schedule()
        with self.assertRaises(h.IllegalScheduleTransition):
            schedule.first_resolvent(h.W2(0))
        with self.assertRaises(h.IllegalScheduleTransition):
            schedule.second_resolvent(h.W1(0))
        self.assertEqual(calls, [])


class RootedIncidenceTests(unittest.TestCase):
    def test_literal_mobius_recursion_and_union_convolution(self) -> None:
        adjacency = {0: {1}, 1: {0, 2}, 2: {1}}
        connected = lambda support: h.connected_in_adjacency(support, adjacency)
        minimal = {
            frozenset({0}): Fraction(1, 2),
            frozenset({0, 1}): Fraction(1, 3),
            frozenset({0, 1, 2}): Fraction(-1, 7),
        }
        result = h.rooted_incidence_transform(minimal, 0, connected)
        self.assertEqual(dict(result.omega), minimal)
        self.assertEqual(
            dict(h.rooted_union_convolution(
                {frozenset({0}): Fraction(2, 3)},
                {frozenset({0, 1}): Fraction(3, 5)},
            )),
            {frozenset({0, 1}): Fraction(2, 5)},
        )


class ConstructionSealTests(unittest.TestCase):
    def test_manifest_is_honestly_blocked(self) -> None:
        self.assertEqual(h.CONSTRUCTION_MANIFEST["status"], "PHASE1_BLOCKED_NOT_M4")
        self.assertFalse(h.CONSTRUCTION_MANIFEST["construction_seal"])

    def test_production_refuses_to_emit_coefficient(self) -> None:
        with self.assertRaises(h.ProductionNotReady):
            h.run_production_m4()

    def test_hamer_is_separate_and_disabled(self) -> None:
        with self.assertRaises(h.HamerDiagnosticDisabled):
            h.terminal_hamer_diagnostic(Fraction(0), Fraction(0), enabled=True)

    def test_restored_package_byte_hashes_unchanged(self) -> None:
        root = Path(__file__).resolve().parent
        for name, expected in h.RESTORED_PACKAGE_SHA256.items():
            with self.subTest(name=name):
                actual = hashlib.sha256((root / name).read_bytes()).hexdigest().upper()
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
