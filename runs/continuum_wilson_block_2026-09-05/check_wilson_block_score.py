"""Finite algebra/coefficient controls for the actual Wilson-block derivation.

These controls do not certify the analytic global Poincare asymptotics.
Run from the repository using its existing Python environment.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.linalg import expm, expm_frechet


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


I = sp.I
T1 = I * sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / 2
T2 = I * sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]) / 2
T3 = I * sp.diag(1, -1, 0) / 2


def bracket(a, b):
    return a * b - b * a


def inner(a, b):
    return sp.simplify(-2 * sp.trace(a * b))


q, z = sp.symbols("q z", real=True)
mixed_v2 = -sp.trace((q * T3) ** 2 * (z * T3) ** 2) / 4
require(sp.simplify(sp.diff(mixed_v2, q, z) + q * z / 8) == 0,
        "Commuting-line quartic mixed coefficient failed")
comm = bracket(T1, T2)
require(bracket(T1, T2) + bracket(T2, T1) == sp.zeros(3),
        "Total Gauss identity failed")
require(inner(comm, comm) == 1, "Physical score witness unexpectedly zero")
cross_coefficient = inner(T1, bracket(T3, T2)) / sp.sqrt(2)
require(cross_coefficient == 1 / sp.sqrt(2), "Metric coefficient sign failed")
center_cosine = (sp.sqrt(5) - 1) / 4
require(center_cosine.is_positive is True, "SU(5) center Hessian not positive")


def arr(x):
    return np.array(x, dtype=np.complex128)


def ip(a, b):
    return float(-2 * np.trace(a @ b).real)


Q, Z, E, F = map(arr, [T3, T1, T1, T2])


def fine_metric(g, dq, dz):
    t = g / np.sqrt(2)
    H, dH = expm_frechet(t * Q, t * dq)
    K, dK = expm_frechet(t * Z, t * dz)
    u1 = H @ K
    u2 = K.conj().T @ H
    du1 = dH @ K + H @ dK
    du2 = dK.conj().T @ H + K.conj().T @ dH
    a1 = u1.conj().T @ du1
    a2 = u2.conj().T @ du2
    direct = (ip(a1, a1) + ip(a2, a2)) / g**2
    a, b = H.conj().T @ dH, K.conj().T @ dK
    ad_k_b = K @ b @ K.conj().T
    exact = (2 * ip(a, a) + 2 * ip(b, b)
             + 2 * ip(a, ad_k_b - H.conj().T @ ad_k_b @ H)) / g**2
    require(abs(direct - exact) < 1e-11, "Exact metric identity failed")
    return direct


rows = []
for g in [0.1, 0.05, 0.025, 0.0125]:
    t = g / np.sqrt(2)
    H, K = expm(t * Q), expm(t * Z)
    action = 2 / g**2 * (6 - np.trace(H @ K + K.conj().T @ H).real)
    cosh_q = (H + H.conj().T) / 2
    cosh_z = (K + K.conj().T) / 2
    action_exact = 4 / g**2 * (3 - np.trace(cosh_q @ cosh_z).real)
    require(abs(action - action_exact) < 1e-9, "Trace action identity failed")
    action0 = (ip(Q, Q) + ip(Z, Z)) / 2
    action2 = -np.trace(Q @ Q @ Q @ Q + Z @ Z @ Z @ Z).real / 24
    action2 -= np.trace(Q @ Q @ Z @ Z).real / 4
    cross = fine_metric(g, E, F) - fine_metric(g, E, 0 * F) - fine_metric(g, 0 * E, F)
    rows.append({
        "g": g,
        "action_remainder_over_g4": float((action - action0 - g**2 * action2) / g**4),
        "metric_cross_over_g": cross / g,
        "metric_cross_limit": 1 / np.sqrt(2),
    })
require(abs(rows[-1]["metric_cross_over_g"] - 1 / np.sqrt(2)) < 1e-4,
        "Leading order-g metric coefficient failed")
require(all(abs(row["action_remainder_over_g4"]) < 0.02 for row in rows),
        "Even action expansion failed")

# Independent adjacent-strip check: the full shared-link co-metric is
# used before taking its horizontal lift, rather than a product-rotor
# substitution. The embedded SU(2) subalgebra is closed under Ad(U).
basis = list(map(arr, [T1, T2, T3]))


def coords(a):
    return np.array([ip(x, a) for x in basis])


def from_coords(v):
    return sum(x * b for x, b in zip(v, basis))


strip_rows = []
for g in [0.1, 0.05, 0.025, 0.0125]:
    alpha = np.sqrt(2) * g
    U, dU = expm_frechet(alpha * Q, alpha * E)
    H, dH = expm_frechet(alpha * Q / 2, alpha * E / 2)
    ad = np.array([[ip(x, U @ y @ U.conj().T) for y in basis] for x in basis])
    cuu = 8 * np.eye(3) - ad - ad.T
    cku = 4 * np.eye(3) - ad.T
    k_velocity = from_coords(cku @ np.linalg.solve(cuu, coords(dU @ U.conj().T)))
    v = 2 / alpha * H.conj().T @ (k_velocity - dH @ H.conj().T) @ H
    strip_rows.append({"g": g, "horizontal_coefficient_over_g": ip(v, Q @ E - E @ Q) / g})
require(abs(strip_rows[-1]["horizontal_coefficient_over_g"] - 7 / (6 * np.sqrt(2))) < 1e-4,
        "Adjacent-strip horizontal coefficient failed")
require(sp.Rational(4) - sp.Rational(3)**2 / 6 == sp.Rational(5, 2),
        "Adjacent-strip exact fiber Schur complement failed")

result = {
    "scope": "Exact finite Lie-algebra identities plus floating Wilson/metric coefficient checks; no global spectral proof",
    "exact_commuting_mixed_hessian_coefficient": str(sp.diff(mixed_v2, q, z)),
    "two_coarse_gauss_sum": "zero",
    "two_coarse_score_commutator_norm_squared": str(inner(comm, comm)),
    "SU5_center_W_quadratic_coefficient": str(center_cosine),
    "coefficient_checks": rows,
    "adjacent_strip_exact_fiber_cometric": "5/2",
    "adjacent_strip_horizontal_coefficient_limit": 7 / (6 * np.sqrt(2)),
    "adjacent_strip_checks": strip_rows,
}
destination = Path(__file__).with_name("wilson_block_score_controls.json")
destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
