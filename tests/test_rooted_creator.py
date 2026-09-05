"""Exact finite-binary controls; these samples do not prove an all-input theorem."""

from fractions import Fraction

import pytest

from workhouse.rooted_creator import (
    BALL_RADIUS,
    FACES,
    KAPPA,
    composed_map,
    family,
    flip,
    flow_tangent_controls,
    magnetic_map,
    magnetic_vector,
    rooted_norm,
    sample_controls,
    sample_families,
    star,
    star_exp,
    star_log,
    theorem_constants,
)


def test_disjoint_star_is_nilpotent_and_is_not_the_pauli_flip_product():
    creator = family(2, ((1, Fraction(1)),))
    assert star(creator, creator) == family(2)
    assert flip(creator, 1) == family(2, ((0, Fraction(1)),))
    assert star(creator, family(2, ((2, Fraction(1)),))) == family(2, ((3, Fraction(1)),))


@pytest.mark.parametrize("name", tuple(sample_families()))
def test_exact_creation_log_exp_inversion_and_independent_operator_tangent(name):
    creator = sample_families()[name]
    vector = star_exp(creator)
    assert star_log(vector) == creator
    assert star_exp(star_log(vector)) == vector
    assert all(flow_tangent_controls(creator).values())


def test_mixed_magnetic_products_and_scalar_normalization_are_retained():
    zero = sample_families()["zero"]
    transformed, normalizer = magnetic_map(zero, FACES, KAPPA)
    assert normalizer == 1 + KAPPA**3
    assert transformed == family(6, ((mask, (KAPPA + KAPPA**2) / (1 + KAPPA**3)) for mask in FACES))
    magnetic = magnetic_vector(star_exp(zero), FACES, KAPPA)
    with pytest.raises(ValueError, match="vacuum coefficient one"):
        star_log(magnetic)


def test_exact_constants_and_rational_upper_bound_place_model_inside_proved_domain():
    constants = theorem_constants()
    assert tuple(constants[key] for key in ("A", "B", "C", "L")) == (
        Fraction(16900, 9),
        Fraction(33280, 9),
        Fraction(6500),
        Fraction(619360, 9),
    )
    assert constants["u_star"] == Fraction(9, 9_909_760)
    assert constants["u_upper"] == Fraction(1, 99_999_999)
    assert 0 < constants["u_upper"] < constants["u_star"]
    assert all(value > 0 for key, value in constants.items() if key.endswith("margin"))
    # log(2)>=1/2 follows by integrating 1/t>=1/2 on [1,2].
    # This proves both the kinetic gap gamma=1/2 and mu>=gamma*tau0/2.
    assert constants["gamma"] * constants["tau0"] / 2 <= Fraction(1, 2)


def test_six_link_samples_have_exact_selfmap_and_pairwise_half_lipschitz_controls():
    controls = sample_controls()
    assert controls.input_norms == (0, Fraction(1, 128), Fraction(1, 128))
    assert controls.passed
    assert all(value < BALL_RADIUS for value in controls.output_norms)
    assert all(value < Fraction(1, 2) for value in controls.pair_ratios)


def test_zero_coupling_gives_zero_composed_map_for_every_fixed_sample():
    for creator in sample_families().values():
        assert rooted_norm(composed_map(creator, kappa=Fraction(0))) == 0


def test_invalid_vacuum_and_kinetic_domains_fail_closed():
    with pytest.raises(ValueError, match="vacuum coefficient zero"):
        star_exp(family(2, ((0, Fraction(1)),)))
    with pytest.raises(ValueError, match="strictly between"):
        composed_map(sample_families()["zero"], kinetic_ratio=Fraction(1))
    with pytest.raises(ValueError, match="normalization vanished"):
        magnetic_map(family(1, ((1, Fraction(-1)),)), (1,), Fraction(1))


def test_float_inputs_cannot_silently_convert_the_exact_oracle_to_a_numeric_check():
    with pytest.raises(TypeError, match="must be exact"):
        magnetic_map(sample_families()["zero"], FACES, 0.1)
    with pytest.raises(TypeError, match="must be exact"):
        star((Fraction(0), 0.1), family(1))
