"""Exact periodic 3D link-Hodge and Coulomb-projected box controls.

Finite integer/rational matrices check the analytic all-box-count harmonic
bound. They do not prove a nonlinear Wilson gap or an OS block identity.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import sympy as s

sys.dont_write_bytecode = True


def complex_matrices(n: int):
    if n < 3:
        raise ValueError("Use n>=3; no short-period orientation alias is admitted")
    sites = list(itertools.product(range(n), repeat=3))
    index = {site: j for j, site in enumerate(sites)}
    count = n ** 3
    differences = []
    for direction in range(3):
        delta = s.zeros(count)
        for site, row in index.items():
            neighbor = list(site)
            neighbor[direction] = (neighbor[direction] + 1) % n
            delta[row, index[tuple(neighbor)]] += 1
            delta[row, row] -= 1
        differences.append(delta)
    a, b, c = differences
    zero = s.zeros(count)
    d0 = a.col_join(b).col_join(c)
    d1 = (-b).row_join(a).row_join(zero)
    d1 = d1.col_join((-c).row_join(zero).row_join(a))
    d1 = d1.col_join(zero.row_join(-c).row_join(b))
    d2 = c.row_join(-b).row_join(a)
    laplace = sum((delta.T * delta for delta in differences), s.zeros(count))
    return sites, differences, d0, d1, d2, laplace


def box_data(n, side, sites):
    if side < 2 or n % side:
        raise ValueError("Boxes must have integer side>=2 dividing the period")
    boxes = list(itertools.product(range(n // side), repeat=3))
    column = {box: j for j, box in enumerate(boxes)}
    site_index = {site: j for j, site in enumerate(sites)}
    indicator = s.zeros(n ** 3, len(boxes))
    neumann = s.zeros(n ** 3)
    for site, row in site_index.items():
        indicator[row, column[tuple(x // side for x in site)]] = 1
        for direction in range(3):
            if site[direction] % side == side - 1:
                continue
            neighbor = list(site)
            neighbor[direction] += 1
            other = site_index[tuple(neighbor)]
            neumann[row, row] += 1
            neumann[other, other] += 1
            neumann[row, other] -= 1
            neumann[other, row] -= 1
    return indicator, neumann


def periodic_green(n, sites):
    # At n=3 or 4, all Fourier cosines and squared frequencies are rational.
    cosines = ([s.Integer(1), -s.Rational(1, 2), -s.Rational(1, 2)] if n == 3
               else [s.Integer(1), s.Integer(0), -s.Integer(1), s.Integer(0)])
    if n not in (3, 4):
        raise ValueError("The exact small-cell Green control is only for n=3,4")
    eigenvalues = {k: 2 * sum(1 - cosines[t] for t in k) for k in sites}
    kernel = {
        x: sum(cosines[sum(a * b for a, b in zip(k, x, strict=True)) % n] / eigenvalues[k]
               for k in sites if k != (0, 0, 0)) / n ** 3
        for x in sites
    }
    return s.Matrix(len(sites), len(sites), lambda i, j:
                    kernel[tuple((a - b) % n for a, b in zip(sites[i], sites[j], strict=True))])


def controls():
    rows = []
    for n, side in [(3, 3), (4, 2)]:
        sites, differences, d0, d1, d2, laplace = complex_matrices(n)
        count = n ** 3
        assert d1 * d0 == s.zeros(3 * count, count)
        assert d2 * d1 == s.zeros(count, 3 * count)
        hodge = d1.T * d1 + d0 * d0.T
        assert hodge == s.diag(laplace, laplace, laplace)
        green = periodic_green(n, sites)
        assert green == green.T
        assert laplace * green == s.eye(count) - s.ones(count) / count
        assert green * s.ones(count, 1) == s.zeros(count, 1)
        # These identities certify the pseudoinverse and the factored Coulomb
        # projector, without a large dense rational projection matrix.

        def coulomb_apply(matrix, d0=d0, green=green):
            return matrix - d0 * (green * (d0.T * matrix))

        harmonic = s.diag(s.ones(count, 1), s.ones(count, 1), s.ones(count, 1))
        assert d0.T * harmonic == s.zeros(count, 3)
        assert d1 * harmonic == s.zeros(3 * count, 3)
        assert coulomb_apply(harmonic) == harmonic

        indicator, neumann = box_data(n, side, sites)
        volume, boxes = side ** 3, indicator.cols
        assert indicator.T * indicator == volume * s.eye(boxes)
        scalar_mean = indicator * indicator.T / volume
        assert scalar_mean * scalar_mean == scalar_mean
        # Exact positive boundary/interface decomposition of the scalar form.
        interface = laplace - neumann
        edge_sum = s.zeros(count)
        site_index = {site: j for j, site in enumerate(sites)}
        for site, row in site_index.items():
            for direction in range(3):
                if site[direction] % side != side - 1:
                    continue
                neighbor = list(site)
                neighbor[direction] = (neighbor[direction] + 1) % n
                other = site_index[tuple(neighbor)]
                vector = s.zeros(count, 1)
                vector[row], vector[other] = 1, -1
                edge_sum += vector * vector.T
        assert interface == edge_sum
        path = s.zeros(side)
        for j in range(side - 1):
            path[j, j] += 1
            path[j + 1, j + 1] += 1
            path[j, j + 1] -= 1
            path[j + 1, j] -= 1
        kappa = 4 * s.sin(s.pi / (2 * side)) ** 2
        centered = s.eye(side) - s.ones(side) / side
        assert all(value >= 0 for value in (path - kappa * centered).eigenvals())
        assert s.simplify(kappa - 4 / s.Integer(side) ** 2) >= 0

        raw_box = s.diag(indicator, indicator, indicator)
        selected_box = raw_box[:, :1]
        projected = coulomb_apply(selected_box)
        assert d0.T * projected == s.zeros(count, 1)
        assert d1 * projected == d1 * selected_box
        assert coulomb_apply(projected) == projected
        assert (projected.T * projected)[0] <= volume
        assert raw_box * (raw_box.T * harmonic) / volume == harmonic
        # Test the exact contraction used to compare the retained distance.
        coarse_test = coulomb_apply(s.Matrix([j * j + 1 for j in range(3 * count)]))
        mean_test = raw_box * (raw_box.T * coarse_test) / volume
        candidate = coulomb_apply(mean_test)
        actual_difference = coarse_test - candidate
        raw_difference = coarse_test - mean_test
        assert (actual_difference.T * actual_difference)[0] <= (
            raw_difference.T * raw_difference
        )[0]
        # A_j depends only on a different basepoint coordinate. This is exactly
        # transverse; its period-L pattern also has zero mean in every box.
        pattern = [1, -1, 0] if side == 3 else [1, -1]
        vector = s.zeros(3 * count, 1)
        for j, site in enumerate(sites):
            vector[j] = pattern[site[1] % side]
        assert d0.T * vector == s.zeros(count, 1)
        assert raw_box.T * vector == s.zeros(3 * boxes, 1)
        assert coulomb_apply(vector) == vector
        kinetic = d1.T * d1
        norm = (vector.T * vector)[0]
        energy = (vector.T * kinetic * vector)[0]
        assert norm > 0 and energy >= kappa * norm
        curl_energy = (coarse_test.T * kinetic * coarse_test)[0]
        gradient_energy = (coarse_test.T * hodge * coarse_test)[0]
        assert curl_energy == gradient_energy
        assert curl_energy >= kappa * (raw_difference.T * raw_difference)[0]
        outside_support = [j for j in range(3 * count) if raw_box[j, 0] == 0]
        tail_count = sum(projected[j, 0] != 0 for j in outside_support)
        if boxes > 1:
            assert tail_count > 0
        rows.append({"period": n, "box_side": side, "box_count": boxes,
                     "link_count": 3 * count, "transverse_dimension": 2 * count + 1,
                     "retained_rank_upper_bound": 3 * boxes,
                     "fast_rank_lower_bound": 2 * count + 1 - 3 * boxes,
                     "harmonic_cochain_directions_retained": 3,
                     "kappa": str(kappa), "fast_test_rayleigh": str(s.cancel(energy / norm)),
                     "projected_box_tail_nonzero_entries": int(tail_count)})
    try:
        complex_matrices(2)
    except ValueError:
        rejected_short_period = True
    else:
        raise AssertionError("Short-period alias convention was silently accepted")
    return {"scope": __doc__, "periodic_controls": rows,
            "d1_d0_and_d2_d1_zero": True, "exact_componentwise_Hodge": True,
            "positive_interface_decomposition": True,
            "short_period_requires_separate_convention": rejected_short_period}


if __name__ == "__main__":
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled")
    target = Path(__file__).with_suffix(".json")
    if target.exists():
        raise FileExistsError("Existing evidence is preserved")
    result = controls()
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, indent=2))
