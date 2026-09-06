"""Exact finite endpoint counts and local source-gradient certificates.

The moment-only API requires an externally justified bound on the entire
omitted transfer. The finite-transfer API checks that bound directly. Neither
API promotes finite matrix evidence to an infinite Wilson theorem.
"""

from __future__ import annotations

import copy
import sys
from functools import lru_cache

import sympy as sp

from . import (
    _covariant_path_models,
    _endpoint_models,
    _fourier_alias_models,
    _local_gradient_models,
    _localized_score_models,
)


def _require(condition, label):
    if not condition:
        raise ValueError(label)


def _rational(value, label):
    value = sp.sympify(value)
    _require(value.is_Rational is True, label + " must be exact rational")
    return value


def _matrix(value, label, *, symmetric=False):
    value = sp.Matrix(value)
    _require(value.rows > 0 and value.cols > 0, label + " must be nonempty")
    _require(all(x.is_Rational is True for x in value), label + " must be exact rational")
    if symmetric:
        _require(value.rows == value.cols and value == value.T, label + " must be symmetric")
    return value


def _encode(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def _inertia(matrix):
    return _endpoint_models.inertia(matrix)


def _psd(matrix, label):
    result = _inertia(matrix)
    _require(result[1] == 0, label + " must be positive semidefinite")
    return result


def two_lag_count_certificate(first_moment, second_moment, discarded_cap, threshold):
    """Finite strict-index bounds conditional on a WHOLE omitted-space cap.

    For exact normalized moments A and A2 of a positive contraction T,
    V=A2-A^2=R*R. If its full omitted block D<=d and z>d, the actual
    positive index of T-z lies between those of A-z and A-z+V/(z-d).
    Moment positivity cannot establish D<=d; this API labels it external.
    """
    a = _matrix(first_moment, "first moment", symmetric=True)
    a2 = _matrix(second_moment, "second moment", symmetric=True)
    _require(a.shape == a2.shape, "moment dimensions must agree")
    d = _rational(discarded_cap, "discarded cap")
    z = _rational(threshold, "threshold")
    _require(0 <= d < z <= 1, "require 0 <= discarded cap < threshold <= 1")
    eye = sp.eye(a.rows)
    _psd(a, "first moment")
    _psd(eye - a, "first moment contraction slack")
    v = a2 - a**2
    variance = _psd(v, "two-lag leakage")
    _psd(a - a2, "positive contraction moment slack")
    lower = _inertia(a - z * eye)
    upper = _inertia(a - z * eye + v / (z - d))
    _require(lower[0] <= upper[0], "Loewner index monotonicity")
    return {
        "schema": "two-lag-strict-count-rational/v1",
        "first_moment": _encode(a),
        "second_moment": _encode(a2),
        "discarded_cap": str(d),
        "threshold": str(z),
        "leakage": _encode(v),
        "leakage_inertia": variance,
        "lower_inertia": lower,
        "upper_inertia": upper,
        "lower_count": lower[0],
        "upper_count": upper[0],
        "count_determined_if_full_cap_holds": lower[0] == upper[0],
        "full_omitted_cap_is_external_hypothesis": True,
        "scope": "Finite exact moments; the entire omitted-space cap is an explicit input premise.",
    }


def replay_two_lag_count(first_moment, second_moment, discarded_cap, threshold, report):
    expected = two_lag_count_certificate(first_moment, second_moment, discarded_cap, threshold)
    _require(report == expected, "two-lag certificate differs from exact recomputation")
    return expected


def finite_endpoint_certificate(transfer, source, discarded_cap, threshold):
    """Check a full finite transfer, normalized sources, exact vacuum and tail.

    This additionally checks every omitted direction and the exact full
    Schur count; it does not discard high retained sources.
    """
    t = _matrix(transfer, "transfer", symmetric=True)
    j = _matrix(source, "source")
    _require(j.rows == t.rows and j.cols <= j.rows, "source dimensions")
    _require(j.T * j == sp.eye(j.cols), "source must be an isometry")
    eye = sp.eye(t.rows)
    _psd(t, "transfer")
    _psd(eye - t, "transfer contraction slack")
    q = eye - j * j.T
    for vacuum in (eye - t).nullspace():
        _require(q * vacuum == sp.zeros(t.rows, 1), "entire exact vacuum must be retained")
    d = _rational(discarded_cap, "discarded cap")
    z = _rational(threshold, "threshold")
    _require(0 <= d < z <= 1, "require 0 <= discarded cap < threshold <= 1")
    tail = _psd(d * q - q * t * q, "entire omitted-transfer cap")
    a = j.T * t * j
    moments = two_lag_count_certificate(a, j.T * t**2 * j, d, z)
    r = q * t * j
    schur = a - z * sp.eye(j.cols) + r.T * (z * eye - q * t * q).inv() * r
    full_count = _inertia(t - z * eye)[0]
    schur_count = _inertia(schur)[0]
    _require(full_count == schur_count, "exact full Schur inertia")
    _require(
        moments["lower_count"] <= full_count <= moments["upper_count"], "complete count bounds"
    )
    return {
        "schema": "finite-endpoint-full-tail-rational/v1",
        "transfer": _encode(t),
        "source": _encode(j),
        "discarded_cap": str(d),
        "threshold": str(z),
        "entire_exact_vacuum_retained": True,
        "omitted_cap_slack_inertia": tail,
        "two_lag": moments,
        "full_count": full_count,
        "exact_schur_count": schur_count,
        "scope": "Entire finite matrix and all source directions; no infinite-Q certificate.",
    }


def replay_finite_endpoint(transfer, source, discarded_cap, threshold, report):
    expected = finite_endpoint_certificate(transfer, source, discarded_cap, threshold)
    _require(report == expected, "finite endpoint certificate differs from exact recomputation")
    return expected


def local_gradient_certificate(local_full, local_bad, copies):
    """Verify the complete radial/pair tensor form for rational SO(3) data.

    The five local basis vectors are a vacuum, a radial scalar and three
    centered adjoint colors. The full form is diag(0,a,b,b,b). Local bad
    entries may mix radial/color directions. Profiles are not normalized
    silently: their complete Gram and all form cross terms are returned.
    """
    full = _matrix(local_full, "local full form", symmetric=True)
    bad = _matrix(local_bad, "local bad form", symmetric=True)
    _require(full.shape == bad.shape == (5, 5), "five-state vacuum/radial/adjoint model required")
    _require(
        isinstance(copies, int) and not isinstance(copies, bool) and copies > 0,
        "positive integer copies",
    )
    a, b = full[1, 1], full[2, 2]
    _require(
        a > 0 and b > 0 and full == sp.diag(0, a, b, b, b), "centered isotropic local full form"
    )
    _require(bad[:, 0] == sp.zeros(5, 1), "local bad form must annihilate constants")
    _psd(bad, "local bad form")
    _psd(full - bad, "bad form bounded by full form")
    epsilon = max(bad[1, 1] / a, sum(bad[i, i] for i in range(2, 5)) / (3 * b))
    models = _local_gradient_models
    labels, basis = models.profiles(copies)
    gram = models.matrix_on(basis, models.dot)
    f = models.matrix_on(basis, lambda x, y: models.form_entry(x, y, full))
    v = models.matrix_on(basis, lambda x, y: models.form_entry(x, y, bad))
    _require(
        all(v[i, j] == 0 for i in range(v.rows) for j in range(v.cols) if i != j),
        "centered support cancellation",
    )
    slack = _psd(epsilon * f - v, "complete profile relative bound")
    return {
        "schema": "local-gradient-profile-rational/v1",
        "local_full": _encode(full),
        "local_bad": _encode(bad),
        "copies": copies,
        "labels": labels,
        "profile_Gram": _encode(gram),
        "complete_full_form": _encode(f),
        "complete_bad_form": _encode(v),
        "relative_cap": str(epsilon),
        "relative_slack_inertia": slack,
        "scope": "Finite centered SO(3) profiles; no Wilson derivative or interacting-copy bound.",
    }


def replay_local_gradient(local_full, local_bad, copies, report):
    expected = local_gradient_certificate(local_full, local_bad, copies)
    _require(report == expected, "gradient certificate differs from exact recomputation")
    return expected


def su2_score_contraction(coordinate, gradient):
    """Exact SU(2) leading score Gram with the actual normalized coefficient."""
    q = _matrix(coordinate, "coordinate")
    v = _matrix(gradient, "gradient")
    _require(q.shape == v.shape == (3, 1), "three-component columns required")
    ad = _localized_score_models.cross_matrix(q)
    angular = (v.T * ad.T * ad * v)[0]
    _require(angular == q.cross(v).dot(q.cross(v)), "Lie score Gram identity")
    return {
        "schema": "su2-leading-score-rational/v1",
        "coordinate": _encode(q),
        "gradient": _encode(v),
        "angular_squared": str(angular),
        "conditional_score_contraction": str(sp.simplify(49 * angular / (72 * sp.sqrt(5)))),
        "centralizer_cancellation": angular == 0,
        "scope": "Leading SU(2) Lie/Gaussian coefficient; no Wilson-ground remainder estimate.",
    }


def _qmatrix(value, label, *, hermitian=False):
    matrix = sp.Matrix(value)
    _require(matrix.rows > 0 and matrix.cols > 0, label + " must be nonempty")
    _require(
        all(all(part.is_Rational is True for part in x.as_real_imag()) for x in matrix),
        label + " must have exact Q(i) entries",
    )
    if hermitian:
        _require(matrix == matrix.conjugate().T, label + " must be Hermitian")
    return matrix


def covariant_source_floor_certificate(stiffness, coulomb, source, floor):
    """Verify a FULL finite Q(i) tangent source inequality and its zero modes.

    The supplied source columns are physical cotangents in ran(P_C). This
    checks K>=kappa(P_C-P_S) on the entire supplied space, not only its
    Q_S compression. The regulated Gaussian consequence is analytic; no
    unregulated Gaussian vacuum or nonlinear comparison is inferred.
    """
    k = _qmatrix(stiffness, "stiffness", hermitian=True)
    pc = _qmatrix(coulomb, "Coulomb projection", hermitian=True)
    b = _qmatrix(source, "source")
    value = _rational(floor, "floor")
    _require(value > 0, "floor must be positive")
    _require(k.shape == pc.shape and b.rows == k.rows, "compatible tangent dimensions")
    _require(pc * pc == pc, "Coulomb matrix must be a projection")
    _require(pc * k * pc == k, "stiffness must act on the Coulomb subspace")
    _require(pc * b == b, "source must be transverse")
    _require(b.rank() == b.cols, "source columns must be independent")

    def adjoint(m):
        return m.conjugate().T

    gram = adjoint(b) * b
    ps = (b * gram.inv() * adjoint(b)).applyfunc(sp.simplify)
    _require(ps * ps == ps and pc * ps == ps, "physical source projection")
    for zero_mode in k.nullspace():
        _require(
            (pc - ps) * zero_mode == sp.zeros(k.rows, 1),
            "every physical zero mode must be retained",
        )
    positive = _covariant_path_models.psd_pivots(k)
    slack = _covariant_path_models.psd_pivots(k - value * (pc - ps))
    return {
        "schema": "covariant-source-full-floor-Qi/v1",
        "stiffness": _encode(k),
        "coulomb": _encode(pc),
        "source": _encode(b),
        "floor": str(value),
        "source_Gram": _encode(gram),
        "source_projection": _encode(ps),
        "stiffness_PSD_pivots": positive,
        "full_floor_PSD_pivots": slack,
        "physical_zero_modes_retained": True,
        "unregulated_vacuum_asserted": False,
        "scope": "Full finite Q(i) matrices; Gaussian domains and nonlinear Wilson are analytic.",
    }


def replay_covariant_source_floor(stiffness, coulomb, source, floor, report):
    expected = covariant_source_floor_certificate(stiffness, coulomb, source, floor)
    _require(report == expected, "source-floor certificate differs from exact recomputation")
    return expected


@lru_cache(maxsize=1)
def _exact_controls():
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    return {
        "endpoint": _endpoint_models.controls(),
        "localized_score": _localized_score_models.controls(),
        "local_gradient": _local_gradient_models.controls(),
        "covariant_path": _covariant_path_models.controls(),
        "fourier_alias": _fourier_alias_models.controls(),
    }


def exact_endpoint_window_controls():
    return copy.deepcopy(_exact_controls())


def replay_endpoint_window_controls(report):
    expected = exact_endpoint_window_controls()
    _require(report == expected, "complete exact model payload differs")
    return expected
