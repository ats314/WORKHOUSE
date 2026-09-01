"""The cubic group on plaquette records, the machinery behind G3's sign test."""

from __future__ import annotations

from workhouse import kernel_orbits as KO
from workhouse.payloads import kernel_records


def test_cubic_group_is_the_48_signed_permutations():
    group = KO.cubic_group()
    assert len(group) == 48 and len(set(group)) == 48


def test_the_orientation_character_at_the_identity_is_psi_sign():
    # PSI_SIGN is the parity of (i, j, n(P)) -- the cube boundary d_3. The
    # character of the inversion is +1 on every plane, so k -> -k is a
    # symmetry with no orientation change, which is why every orbit's carrier
    # projection is even.
    identity = ((0, 1, 2), (1, 1, 1))
    inversion = ((0, 1, 2), (-1, -1, -1))
    for plane in KO.PLANES:
        assert KO.act_plane(identity, plane) == (plane, 1)
        assert KO.act_plane(inversion, plane) == (plane, 1)
    # a single reflection reverses the two planes that contain the axis
    reflect_z = ((0, 1, 2), (1, 1, -1))
    assert {p: KO.act_plane(reflect_z, p)[1] for p in KO.PLANES} == {
        (0, 1): 1,
        (0, 2): -1,
        (1, 2): -1,
    }


def test_transform_record_is_a_bijection_on_the_kernel():
    recs = kernel_records()
    keys = {key for key, _ in recs}
    for g in KO.cubic_group():
        images = {KO.transform_record(g, key)[0] for key in keys}
        assert None not in images, "a rotated centre displacement must stay a legal base offset"
        assert images == keys, "the cubic group permutes the 189 records"


def test_regauging_fixes_same_plane_records_and_signs_cross_plane_ones():
    recs = kernel_records()
    g = ((0, 1, 2), (1, -1, 1))  # reverse the orientation of plane (0, 2)
    for (ip, op, d), w in KO.regauge(recs, g):
        original = dict(recs)[(ip, op, d)]
        flipped = ((0, 2) in (ip, op)) and ip != op
        assert w == (-original if flipped else original)
