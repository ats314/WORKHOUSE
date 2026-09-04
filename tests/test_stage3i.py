"""The pinned Stage-3I word ledger reassembles to the pinned 189-record kernel."""

from fractions import Fraction as F

from workhouse import stage3i as S
from workhouse.payloads import kernel_records, stage3i_hashes


def test_fixture_hash_is_the_kernels_stage3i_input():
    assert S.STAGE3I_SHA in stage3i_hashes()
    assert len(S.load_words()) == 4221


def test_reassembly_reproduces_the_pinned_kernel():
    full = S.build_full_kernel(S.build_root_kernel(S.load_words()))
    assert full == dict(kernel_records())


def test_cluster_classes_of_the_rotation_record():
    classes = S.cluster_classes(S.ROTATION_OUTPUT)
    assert classes["corner(three faces at a vertex)"]["supports"] == 2
    assert set(classes["corner(three faces at a vertex)"]["values"]) == {
        F(2580244782961, 398756546697600)
    }
    assert classes["cube(six faces once each)"]["sum"] == F(-31, 1536)
    assert len(S.cube_words(S.ROTATION_OUTPUT)) == 8
