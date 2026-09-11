"""Adversarial controls for the hypotheses in the kernel closure attempt."""

from sympy import Matrix, Rational

from workhouse.invariants.os_kernel_gap import os_kernel


def test_all_scoped_kernel_controls():
    results = os_kernel.run()
    assert len(results) == 5
    assert all(result.passed for result in results), results


def test_kernel_limit_needs_its_own_semigroup_compatibility():
    """Converging Gram matrices alone do not fix a chosen limiting shift."""
    injection = Matrix.eye(2)
    cutoff_transfer = Matrix.diag(1, Rational(1, 2))
    proposed_shift = Matrix.eye(2)
    defect = injection * proposed_shift - cutoff_transfer * injection
    assert defect == Matrix.diag(0, Rational(1, 2))
    assert defect[:, 1].dot(defect[:, 1]) == Rational(1, 4)


def test_source_norm_cannot_be_silently_allowed_to_diverge():
    """Tiny vector error need not give a tiny full-correlator error."""
    for n in (2, 10, 100):
        target = Matrix([n])
        probe = target - Matrix([Rational(1, n)])
        difference = target.dot(target) - probe.dot(probe)
        assert difference == 2 - Rational(1, n * n)
        assert difference > 1


def test_positive_equal_time_variance_can_be_os_null():
    """Independent halves with reflection swap have an OS-null centered source."""
    samples = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    euclidean_variance = sum(Rational(y * y, 4) for _, y in samples)
    reflected_norm = sum(Rational(x * y, 4) for x, y in samples)
    assert euclidean_variance == 1
    assert reflected_norm == 0


def test_one_observed_sector_is_not_the_full_history_space():
    transfer = Matrix.diag(1, Rational(15, 16), Rational(1, 4))
    observed = Matrix([0, 0, 1])
    dark = Matrix([0, 1, 0])
    for step in (1, 4, 10):
        assert (observed.T * transfer**step * observed)[0] == Rational(1, 4) ** step
        assert (dark.T * transfer**step * dark)[0] > Rational(1, 4) ** step


def test_instantaneous_loss_direction_is_not_positive_time_divisible():
    positive_time_shift = Matrix.diag(1, 0)
    disappearing = Matrix([0, 1])
    assert positive_time_shift.rank() == 1
    assert positive_time_shift.row_join(disappearing).rank() == 2
    assert positive_time_shift * disappearing == Matrix.zeros(2, 1)
