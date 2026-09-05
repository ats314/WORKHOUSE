#!/usr/bin/env python3
"""Independent checks for the WORKHOUSE weighted-remainder bridge.

This verifies algebra, estimates on samples, and a non-polynomial toy symbol.
It does NOT rerun WORKHOUSE, construct microscopic SU(3) matrix elements,
or certify the upstream G18 hypotheses. The general result is proved in
RELATIVE_GAP_BRIDGE.md. Requires Python >=3.10 and NumPy.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np

REPO_COMMIT = "31255abac3829cb0cc1ce7c36c1852db8cdafbea"
T = Fraction(5, 612)


def bloch(k: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
    """Paper's (12,13,23) convention; expm1 avoids small-k cancellation."""
    d = np.expm1(1j * np.asarray(k, dtype=float))
    w = np.array([d[2].conjugate(), -d[1].conjugate(), d[0].conjugate()])
    q = float(np.vdot(w, w).real)
    up = np.outer(w, w.conjugate())
    down = q * np.eye(3) - up
    return q, up, down


def schur_weighted_norm(kernel: dict[tuple[int, int, int], np.ndarray], mu: float) -> float:
    """Exactly the row/column weighted l1 expression (evaluated in floats)."""
    if mu <= 0:
        raise ValueError("mu must be positive")
    total = np.zeros((3, 3))
    for x, value in kernel.items():
        total += math.exp(mu * sum(abs(v) for v in x)) * np.abs(value)
    return float(max(total.sum(axis=0).max(), total.sum(axis=1).max()))


def centered_even_symbol(k: np.ndarray, terms: list[tuple[np.ndarray, np.ndarray]]) -> np.ndarray:
    # Stable evaluation of cos(theta)-1 even for theta very near zero.
    return sum((-2 * math.sin(float(k @ x) / 2) ** 2 * a for x, a in terms),
               np.zeros((3, 3)))


def run() -> dict:
    checks: list[dict] = []

    def record(name: str, passed: bool, details: dict | None = None) -> None:
        entry = {"name": name, "passed": bool(passed), **(details or {})}
        checks.append(entry)
        if not passed:
            raise AssertionError(json.dumps(entry, indent=2))

    # Exact arithmetic: constants resulting from the scalar inequalities.
    # (1/2)*(4/(e^2 mu^2))*(pi^2/4) = pi^2/(2 e^2 mu^2).
    record("rational_prefactor_in_weighted_centering_bound",
           Fraction(1, 2) * 4 * Fraction(1, 4) == Fraction(1, 2))
    # Tail bound M/rho^3 * 1/(1-|u|/rho) <= 2 M/rho^3 on half the disc.
    record("Cauchy_half_disc_geometric_factor", 1 / (1 - Fraction(1, 2)) == 2)
    # u <= t/(4K) gives a relative gap >= t/2.
    record("gap_threshold_algebra", 1 - 2 * Fraction(1, 4) == Fraction(1, 2))
    # Projection bound eta/(a-2eta) at eta/a=1/4 is <=1/2.
    record("projector_threshold_algebra",
           Fraction(1, 4) / (1 - 2 * Fraction(1, 4)) == Fraction(1, 2))

    # Phase-dependent inversion: d/dk[J(sI)J^-1] contributes [J',sI]=0.
    phase_generator = np.diag(np.array([1, -2, 3], dtype=np.int64))
    scalar = 7 * np.eye(3, dtype=np.int64)
    record("inversion_phase_commutator_with_Gamma_scalar_vanishes",
           np.array_equal(phase_generator @ scalar - scalar @ phase_generator,
                          np.zeros((3, 3), dtype=np.int64)))

    rng = np.random.default_rng(20260904)
    random_k = rng.uniform(-math.pi, math.pi, size=(1000, 3))
    grid_k = []
    for L in (3, 4, 5, 8):
        for j in product(range(L), repeat=3):
            k = 2 * math.pi * np.asarray(j, dtype=float) / L
            grid_k.append((k + math.pi) % (2 * math.pi) - math.pi)
    directions = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 1, 2]], dtype=float)
    directions /= np.linalg.norm(directions, axis=1)[:, None]
    near_k = [scale * n for scale in (1e-2, 1e-4, 1e-6, 1e-8) for n in directions]
    points = np.vstack([random_k, grid_k, near_k])
    nonzero = [k for k in points if np.linalg.norm(k) > 1e-15]

    identity_error = 0.0
    jordan_violation = 0.0
    for k in nonzero:
        q, up, down = bloch(k)
        d = np.expm1(1j * k)
        B = np.array([[d[1], -d[0], 0], [d[2], 0, -d[0]], [0, d[2], -d[1]]])
        identity_error = max(identity_error, float(np.linalg.norm(B @ B.conj().T - down)),
                             float(np.linalg.norm(up @ down)))
        jordan_violation = max(jordan_violation, float(k @ k - math.pi**2 / 4 * q))
    record("Bloch_Hodge_identities_sampled", identity_error < 2e-12,
           {"max_absolute_error": identity_error, "nonzero_momenta": len(nonzero)})
    record("Jordan_momentum_bound_sampled", jordan_violation < 2e-12,
           {"max_violation": jordan_violation})

    # A generic matrix-valued, even Fourier kernel with exact zero first moment.
    terms = []
    kernel: dict[tuple[int, int, int], np.ndarray] = {(0, 0, 0): np.zeros((3, 3))}
    for coords in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (2, -1, 1)]:
        a = rng.integers(-3, 4, size=(3, 3)).astype(float)
        a = (a + a.T) / 2
        x = np.array(coords)
        terms.append((x, a))
        kernel[coords] = a / 2
        kernel[tuple(-x)] = a / 2
        kernel[(0, 0, 0)] -= a
    first_moment = [sum((x[j] * a for x, a in kernel.items()), np.zeros((3, 3))) for j in range(3)]
    record("test_kernel_first_moment_exactly_zero", all(np.array_equal(m, np.zeros((3, 3))) for m in first_moment))
    mu = 0.7
    norm = schur_weighted_norm(kernel, mu)
    gamma_mu = math.pi**2 / (2 * math.e**2 * mu**2)
    max_fraction = 0.0
    for k in nonzero:
        q, _, _ = bloch(k)
        max_fraction = max(max_fraction, float(np.linalg.norm(centered_even_symbol(k, terms), 2) / (gamma_mu * norm * q)))
    record("weighted_q_bound_on_generic_even_kernel", max_fraction <= 1 + 1e-12,
           {"largest_observed_fraction_of_bound": max_fraction, "weighted_norm": norm})

    # Exact, NON-POLYNOMIAL toy family, not a microscopic gauge Hamiltonian:
    # h-E_Gamma I = t u^2 L_down + [u^3/(1-u)] c diag(a3,a2,a1).
    # Its remainder has a known convergent infinite series and zero gradient.
    mu, c, umax = 1.0, 0.0005, 0.1
    a_norm = 2 * c * (1 + math.exp(mu))
    cubic_majorant = a_norm / (1 - umax)
    K = math.pi**2 / (2 * math.e**2 * mu**2) * cubic_majorant
    record("toy_interval_inside_relative_gap_domain", umax < float(T) / (4 * K),
           {"u_max": umax, "K": K, "t_over_4K": float(T) / (4 * K)})
    min_gap_ratio, max_projector_fraction = float("inf"), 0.0
    toy_count = 0
    for u in (0.02, 0.05, 0.1):
        for k in nonzero:
            q, up, down = bloch(k)
            aa = 4 * np.sin(k / 2) ** 2
            tail = u**3 / (1 - u) * c * np.diag(aa[::-1])
            h = float(T) * u**2 * down + tail
            eig, vec = np.linalg.eigh(h)
            bound = q * u**2 * (float(T) - 2 * K * u)
            min_gap_ratio = min(min_gap_ratio, float((eig[1] - eig[0]) / bound))
            P = np.outer(vec[:, 0], vec[:, 0].conjugate())
            P0 = up / q
            p_bound = K * u / (float(T) - 2 * K * u)
            max_projector_fraction = max(max_projector_fraction, float(np.linalg.norm(P - P0, 2) / p_bound))
            toy_count += 1
    record("exact_nonpolynomial_toy_gap_and_projector_bounds",
           min_gap_ratio >= 1 - 1e-9 and max_projector_fraction <= 1 + 1e-9,
           {"evaluations": toy_count, "minimum_gap_over_lower_bound": min_gap_ratio,
            "maximum_projector_error_over_bound": max_projector_fraction})

    # Hostile control: remove the zero-gradient condition. sin(k_x)/q(k)
    # diverges as k_x ->0; mere analyticity and locality cannot give O(q).
    scales = [1e-2, 1e-4, 1e-6]
    linear_ratios = [abs(math.sin(s)) / (4 * math.sin(s/2)**2) for s in scales]
    record("negative_control_nonzero_gradient_defeats_q_bound",
           linear_ratios[1] > 90 * linear_ratios[0] and linear_ratios[2] > 90 * linear_ratios[1],
           {"momenta": scales, "linear_tail_over_q": linear_ratios})

    return {
        "status": "PASS", "checks_passed": len(checks), "checks": checks,
        "repo_commit_read": REPO_COMMIT,
        "scope": "Independent algebra and sampled regressions for the derived bridge; toy spectrum only.",
        "not_verified": ["WORKHOUSE full test suite", "microscopic SU(3) contractions",
                         "G18 construction and cited cluster majorants", "continuum or Wilson transfer matching"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("relative_gap_checks.json"))
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
