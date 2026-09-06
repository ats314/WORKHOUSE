"""Exact controls for literal sources, common Gauss and Gaussian complements.

The private model modules preserve independently authored derivations.
Generic certificates below check finite rational inputs and replay all values.
They do not certify the analytic Wilson limits or infinite Fock statements.
"""

from __future__ import annotations

import copy
from functools import lru_cache

import sympy as sp

from . import (
    _central_score_models,
    _common_gauss_models,
    _gaussian_literal_models,
    _ground_score_models,
    _literal_inverse_models,
    _literal_vacuum_models,
)


def _require(condition, label):
    if not condition:
        raise ValueError(label)


def _rational(value, label):
    result = sp.sympify(value)
    _require(result.is_Rational is True, label + " must be exact rational")
    return result


def _matrix(value, label, *, square=False):
    result = sp.Matrix(value)
    _require(result.rows > 0 and result.cols > 0, label + " must be nonempty")
    _require(all(entry.is_Rational is True for entry in result), label + " must be exact rational")
    if square:
        _require(result.rows == result.cols and result == result.T, label + " must be symmetric")
    return result


def _encode(matrix):
    return [[str(entry) for entry in row] for row in matrix.tolist()]


def _psd(matrix):
    try:
        return _gaussian_literal_models.psd_pivots(matrix)
    except AssertionError as error:
        raise ValueError(str(error)) from error


def _positive(matrix, label):
    pivots = _psd(matrix)
    _require(all(sp.Rational(pivot) > 0 for pivot in pivots), label + " must be positive definite")
    return pivots


def _projection(columns):
    _require(columns.rank() == columns.cols, "source columns must be independent")
    return columns * (columns.T * columns).inv() * columns.T


def literal_projection_certificate(omega, coarse, hamiltonian, vacuum_energy=0):
    """Verify a positive true ground and its actual weighted literal range.

    `coarse` gives arbitrary independent real observable columns, with the
    constant observable in their span. It need not be a partition matrix.
    """
    omega = _matrix(omega, "vacuum")
    coarse = _matrix(coarse, "coarse observations")
    hamiltonian = _matrix(hamiltonian, "Hamiltonian", square=True)
    energy = _rational(vacuum_energy, "vacuum energy")
    dimension = hamiltonian.rows
    _require(omega.shape == (dimension, 1) and coarse.rows == dimension, "compatible dimensions")
    _require(all(entry > 0 for entry in omega), "strictly positive vacuum")
    _require((omega.T * omega)[0] == 1, "normalized vacuum")
    shifted = hamiltonian - energy * sp.eye(dimension)
    _require(shifted * omega == sp.zeros(dimension, 1), "actual vacuum energy subtraction")
    pivots = _psd(shifted)
    source = sp.diag(*omega) * coarse
    projection = _projection(source)
    _require(projection * omega == omega, "literal range must contain the exact vacuum")
    gram = source.T * source
    compressed = source.T * shifted * source
    return {
        "schema": "literal-projection-rational/v1",
        "omega": _encode(omega),
        "coarse": _encode(coarse),
        "hamiltonian": _encode(hamiltonian),
        "vacuum_energy": str(energy),
        "vacuum_subtracted_PSD_pivots": pivots,
        "source_Gram": _encode(gram),
        "literal_projection": _encode(projection),
        "compressed_form": _encode(compressed),
        "compressed_PSD_pivots": _psd(compressed),
        "vacuum_in_range_exact": True,
    }


def replay_literal_projection(omega, coarse, hamiltonian, vacuum_energy, certificate):
    expected = literal_projection_certificate(omega, coarse, hamiltonian, vacuum_energy)
    _require(certificate == expected, "literal certificate differs from exact recomputation")
    return expected


def gaussian_source_certificate(root_omega, source, floor):
    """Check the finite inverse-frequency bridge with both square roots rational.

    T=root_omega>0, Omega=T^2, K=T^4. The full K boundary inequality is
    checked, rather than only its compression to discarded coordinates.
    Commuting, noncommuting and fully retained sources are all admissible.
    """
    root = _matrix(root_omega, "frequency square root", square=True)
    source = _matrix(source, "source columns")
    floor = _rational(floor, "frequency floor")
    _require(source.rows == root.rows, "compatible source dimensions")
    _require(floor > 0, "strictly positive frequency floor")
    positive_pivots = _positive(root, "frequency square root")
    omega = root**2
    stiffness = omega**2
    coordinate_projection = _projection(source)
    source_projection = _projection(root.inv() * source)
    coordinate_q = sp.eye(root.rows) - coordinate_projection
    source_q = sp.eye(root.rows) - source_projection
    _require(
        coordinate_q * root.inv() * source_q == root.inv() * source_q,
        "inverse-frequency source orthogonality",
    )
    return {
        "schema": "gaussian-source-rational/v1",
        "root_omega": _encode(root),
        "source": _encode(source),
        "floor": str(floor),
        "strict_positive_pivots": positive_pivots,
        "P_S": _encode(coordinate_projection),
        "P_R": _encode(source_projection),
        "full_boundary_PSD_pivots": _psd(stiffness - floor**2 * coordinate_q),
        "square_root_PSD_pivots": _psd(omega - floor * coordinate_q),
        "compressed_inverse_PSD_pivots": _psd(source_q / floor - source_q * omega.inv() * source_q),
        "full_frequency_PSD_pivots": _psd(omega - floor * source_q),
        "source_commutes_with_frequency": bool(
            source_projection * omega == omega * source_projection
        ),
    }


def replay_gaussian_source(root_omega, source, floor, certificate):
    expected = gaussian_source_certificate(root_omega, source, floor)
    _require(certificate == expected, "Gaussian certificate differs from exact recomputation")
    return expected


def fisher_cap_certificate(metric, fisher, beta):
    """Verify A>0, I>=0 and I<=beta A^-1 without assuming commutation."""
    metric = _matrix(metric, "coarse metric", square=True)
    fisher = _matrix(fisher, "conditional Fisher covariance", square=True)
    beta = _rational(beta, "Fisher cap")
    _require(metric.shape == fisher.shape, "compatible covariance dimensions")
    _require(beta >= 0, "nonnegative Fisher cap")
    metric_pivots = _positive(metric, "coarse metric")
    covariance_pivots = _psd(fisher)
    slack = beta * metric.inv() - fisher
    return {
        "schema": "fisher-cap-rational/v1",
        "metric": _encode(metric),
        "fisher": _encode(fisher),
        "beta": str(beta),
        "metric_pivots": metric_pivots,
        "covariance_pivots": covariance_pivots,
        "congruence_slack": _encode(slack),
        "slack_PSD_pivots": _psd(slack),
        "commuting": bool(metric * fisher == fisher * metric),
    }


def replay_fisher_cap(metric, fisher, beta, certificate):
    expected = fisher_cap_certificate(metric, fisher, beta)
    _require(certificate == expected, "Fisher certificate differs from exact recomputation")
    return expected


def literal_full_domination_certificate(hamiltonian, retained, vacuum_projection, floor):
    """Check inverse-energy control of the full form, beyond QHQ compression.

    The supplied Hamiltonian is already vacuum-subtracted. The entire exact
    kernel must be supplied and retained. Its inverse on the kernel's
    orthogonal complement is computed by the rational rank-one shift (or
    the same projection shift for a higher-dimensional kernel).
    """
    hamiltonian = _matrix(hamiltonian, "Hamiltonian", square=True)
    retained = _matrix(retained, "retained projection", square=True)
    vacuum = _matrix(vacuum_projection, "vacuum projection", square=True)
    floor = _rational(floor, "full form floor")
    _require(
        hamiltonian.shape == retained.shape == vacuum.shape, "compatible projection dimensions"
    )
    _require(floor > 0, "strictly positive full form floor")
    _require(retained**2 == retained and vacuum**2 == vacuum, "orthogonal projections")
    _require(vacuum.rank() > 0, "nonempty exact vacuum space")
    _require(hamiltonian * vacuum == sp.zeros(hamiltonian.rows), "vacuum is annihilated")
    _require(hamiltonian.rank() + vacuum.rank() == hamiltonian.rows, "complete vacuum kernel")
    _require(retained * vacuum == vacuum, "entire vacuum retained exactly")
    _psd(hamiltonian)
    inverse = (hamiltonian + vacuum).inv() - vacuum
    discarded = sp.eye(hamiltonian.rows) - retained
    return {
        "schema": "literal-full-domination-rational/v1",
        "hamiltonian": _encode(hamiltonian),
        "retained": _encode(retained),
        "vacuum_projection": _encode(vacuum),
        "floor": str(floor),
        "reduced_inverse": _encode(inverse),
        "inverse_cap_PSD_pivots": _psd(discarded / floor - discarded * inverse * discarded),
        "full_domination_PSD_pivots": _psd(hamiltonian - floor * discarded),
    }


def replay_literal_full_domination(hamiltonian, retained, vacuum_projection, floor, certificate):
    expected = literal_full_domination_certificate(hamiltonian, retained, vacuum_projection, floor)
    _require(
        certificate == expected, "full domination certificate differs from exact recomputation"
    )
    return expected


@lru_cache(maxsize=1)
def _cached_controls():
    if not __debug__:
        raise RuntimeError("Exact acceptance rejects optimized Python")
    return {
        "literal": _literal_vacuum_models.controls(),
        "common_gauss": _common_gauss_models.controls(),
        "score": _ground_score_models.controls(),
        "gaussian": _gaussian_literal_models.controls(),
        "central_score": _central_score_models.controls(),
        "literal_inverse": _literal_inverse_models.controls(),
    }


def exact_literal_coarse_controls():
    """Return an isolated copy of all six original mathematical payloads."""
    return copy.deepcopy(_cached_controls())


def replay_literal_coarse_controls(payload):
    expected = exact_literal_coarse_controls()
    _require(payload == expected, "control payload differs from exact recomputation")
    return expected
