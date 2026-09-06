"""Exact finite incidence and Q(i) Fourier controls for local path sources.

The all-size analytic theorem is separate from this finite n=4, L=2 model.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def adjoint(matrix: s.MatrixBase) -> s.MatrixBase:
    return matrix.conjugate().T


def reduced(value: s.Expr) -> s.Expr:
    return s.cancel(s.expand_complex(value))


def psd_pivots(matrix: s.MatrixBase) -> list[str]:
    current = s.Matrix(matrix).applyfunc(reduced)
    require(current == adjoint(current), "Hermitian matrix required")
    pivots = []
    for k in range(current.rows):
        pivot = reduced(current[k, k])
        require(pivot.is_real is True, "real pivot required")
        require(pivot >= 0, f"negative exact pivot at {k}: {pivot}")
        pivots.append(str(pivot))
        if pivot == 0:
            require(
                all(current[k, j] == 0 for j in range(k + 1, current.cols)),
                "zero pivot with nonzero row",
            )
            continue
        for i in range(k + 1, current.rows):
            for j in range(i, current.cols):
                entry = reduced(current[i, j] - current[i, k] * current[k, j] / pivot)
                current[i, j] = entry
                current[j, i] = s.conjugate(entry)
        for i in range(k + 1, current.rows):
            current[i, k] = current[k, i] = 0
    return pivots


def geometry_controls() -> dict:
    n, length = 4, 2
    m = n // length
    sites = list(itertools.product(range(n), repeat=3))
    coarse = list(itertools.product(range(m), repeat=3))
    site_index = {x: j for j, x in enumerate(sites)}
    coarse_index = {x: j for j, x in enumerate(coarse)}

    def shift(x, i, amount=1, period=n):
        out = list(x)
        out[i] = (out[i] + amount) % period
        return tuple(out)

    def edge(x, i):
        return 3 * site_index[x] + i

    def coarse_edge(y, i):
        return 3 * coarse_index[y] + i

    def point(y):
        return tuple(length * yj for yj in y)

    def anchor(v, offset):
        x = v
        path = []
        for i in range(3):
            for _ in range(offset[i]):
                path.append((edge(x, i), 1))
                x = shift(x, i)
        return path, x

    offsets = list(itertools.product(range(length), repeat=3))
    d0 = s.zeros(3 * n**3, n**3)
    dc = s.zeros(3 * m**3, m**3)
    for x in sites:
        for i in range(3):
            d0[edge(x, i), site_index[shift(x, i)]] += 1
            d0[edge(x, i), site_index[x]] -= 1
    for y in coarse:
        for i in range(3):
            dc[coarse_edge(y, i), coarse_index[shift(y, i, period=m)]] += 1
            dc[coarse_edge(y, i), coarse_index[y]] -= 1

    average = s.zeros(m**3, n**3)
    restriction = s.zeros(m**3, n**3)
    phi = s.zeros(m**3, 3 * n**3)
    r = s.zeros(3 * m**3, 3 * n**3)
    t_paths = s.zeros(3 * m**3, 3 * n**3)
    naive = s.zeros(3 * m**3, 3 * n**3)
    all_paths = {}
    weight = s.Rational(1, length**3)
    max_path = 0
    for y in coarse:
        v = point(y)
        restriction[coarse_index[y], site_index[v]] = 1
        for offset in offsets:
            first_anchor, x = anchor(v, offset)
            average[coarse_index[y], site_index[x]] += weight
            for e, sign in first_anchor:
                phi[coarse_index[y], e] += weight * sign
            for i in range(3):
                row = coarse_edge(y, i)
                naive[row, edge(x, i)] += weight
                long_path = []
                cursor = x
                for _ in range(length):
                    e = edge(cursor, i)
                    r[row, e] += weight
                    long_path.append((e, 1))
                    cursor = shift(cursor, i)
                next_v = shift(v, i, length)
                last_anchor, head = anchor(next_v, offset)
                require(cursor == head, "path endpoints")
                path = first_anchor + long_path + [(e, -sign) for e, sign in reversed(last_anchor)]
                all_paths.setdefault((y, i), []).append(path)
                max_path = max(max_path, len(path))
                boxes = {anchor(v, o)[1] for o in offsets} | {anchor(next_v, o)[1] for o in offsets}
                require(all(sites[e // 3] in boxes for e, _ in path), "two-cube support")
                for e, sign in path:
                    t_paths[row, e] += weight * sign

    require(r * d0 == dc * average, "averaged cochain square")
    require(phi * d0 == average - restriction, "anchor telescope")
    require(t_paths == r - dc * phi, "direct path tangent differs")
    require(t_paths * d0 == dc * restriction, "actual point-restriction square")
    coarse_transverse = s.Matrix.hstack(*dc.T.nullspace())
    source = r.T * coarse_transverse
    require(d0.T * source == s.zeros(n**3, source.cols), "source transverse")
    require(t_paths.T * coarse_transverse == source, "anchor cancellation")
    require(source.rank() == 2 * m**3 + 1, "coarse transverse rank")
    constant_controls = []
    for i in range(3):
        b = s.Matrix([int(j % 3 == i) for j in range(3 * m**3)])
        fine = r.T * b
        expected = s.Matrix([s.Rational(int(j % 3 == i), length**2) for j in range(3 * n**3)])
        require(fine == expected, "constant mode not retained")
        constant_controls.append(str(fine[edge((0, 0, 0), i)]))
    naive_defect = d0.T * naive.T * coarse_transverse
    require(naive_defect != s.zeros(*naive_defect.shape), "naive box negative missing")
    require(r * d0 != dc * restriction, "anchor-free actual-square negative missing")

    # Compare the actual real-space matrix with every fine plane wave, not
    # merely with a separately coded Fourier formula at selected momenta.
    rows = [
        [(j, r[row, j]) for j in range(r.cols) if r[row, j] != 0]
        for row in range(r.rows)
    ]
    plane_wave_checks = 0
    for frequency in itertools.product(range(n), repeat=3):
        plane = {
            x: s.I ** (sum(frequency[j] * x[j] for j in range(3)) % 4)
            for x in sites
        }
        aa = [(1 + s.I ** frequency[j]) / 2 for j in range(3)]
        for y in coarse:
            for i in range(3):
                row = coarse_edge(y, i)
                actual = sum(weight * plane[sites[e // 3]] for e, weight in rows[row])
                expected = length * s.prod(aa) * aa[i] * plane[point(y)]
                require(reduced(actual - expected) == 0, "real-space/Fourier symbol mismatch")
                plane_wave_checks += 1

    # Exact noncommuting SU(2) holonomies and independent gauge rotations.
    rot1 = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5)], [-s.Rational(4, 5), s.Rational(3, 5)]])
    rot2 = s.diag((3 + 4 * s.I) / 5, (3 - 4 * s.I) / 5)
    choices = [s.eye(2), rot1, rot2, rot1 * rot2]
    edges = {j: choices[(7 * j + 1) % 4] for j in range(3 * n**3)}
    gauges = {x: choices[(site_index[x] + sum(x)) % 4] for x in sites}

    def transformed(e):
        x, i = sites[e // 3], e % 3
        return gauges[x] * edges[e] * adjoint(gauges[shift(x, i)])

    def path_value(path, gauge=False):
        value = s.eye(2)
        for e, sign in path:
            factor = transformed(e) if gauge else edges[e]
            value = value * (factor if sign == 1 else adjoint(factor))
            value = value.applyfunc(reduced)
        return value

    covariances = []
    for y, i in [((0, 0, 0), 0), ((0, 1, 0), 2)]:
        matrix = sum((path_value(p) for p in all_paths[(y, i)]), s.zeros(2)) * weight
        gauged = sum((path_value(p, True) for p in all_paths[(y, i)]), s.zeros(2)) * weight
        v = point(y)
        expected = gauges[v] * matrix * adjoint(gauges[shift(v, i, length)])
        require((gauged - expected).applyfunc(reduced) == s.zeros(2), "exact gauge covariance")
        covariances.append(
            {
                "site": list(y),
                "direction": i,
                "matrix_is_unitary": (adjoint(matrix) * matrix).applyfunc(reduced) == s.eye(2),
            }
        )
    return {
        "period": n,
        "block_length": length,
        "fine_vertices": n**3,
        "fine_oriented_edges": 3 * n**3,
        "coarse_transverse_rank": source.cols,
        "four_exact_cochain_identities": True,
        "retained_constant_amplitudes": constant_controls,
        "max_path_length": max_path,
        "two_cube_support": True,
        "real_space_fourier_plane_wave_equalities": plane_wave_checks,
        "naive_box_transverse_defect_nonzero_entries": sum(v != 0 for v in naive_defect),
        "noncommuting_gauge_covariances": covariances,
    }


def fourier_controls() -> dict:
    blocks = []
    bad_matrix = None
    for coarse in itertools.product(range(2), repeat=3):
        d_coarse = s.Matrix([(-1) ** j - 1 for j in coarse])
        nc = s.Matrix.hstack(*d_coarse.T.nullspace())
        aliases = list(itertools.product(range(2), repeat=3))
        pc = s.zeros(24)
        stiffness = s.zeros(24)
        source = s.zeros(24, nc.cols)
        symbols = []
        for r_index, r in enumerate(aliases):
            phases = [s.I ** ((coarse[j] + 2 * r[j]) % 4) for j in range(3)]
            d = s.Matrix([v - 1 for v in phases])
            q = reduced((adjoint(d) * d)[0])
            local_pc = s.eye(3) if q == 0 else s.eye(3) - d * adjoint(d) / q
            aa = [(1 + v) / 2 for v in phases]
            total = s.prod(aa)
            row = s.diag(*[s.conjugate(2 * total * aa[j]) for j in range(3)]) * nc
            for i in range(3):
                for j in range(3):
                    pc[3 * r_index + i, 3 * r_index + j] = reduced(local_pc[i, j])
                    stiffness[3 * r_index + i, 3 * r_index + j] = reduced(q * local_pc[i, j])
                for j in range(nc.cols):
                    source[3 * r_index + i, j] = reduced(row[i, j])
            require(
                (adjoint(d) * row).applyfunc(reduced) == s.zeros(1, nc.cols),
                "alias source not transverse",
            )
            symbols.append(aa)
        require(source.rank() == nc.cols, "principal alias rank")
        gram = adjoint(source) * source
        ps = (source * gram.inv() * adjoint(source)).applyfunc(reduced)
        require(
            (pc * ps - ps).applyfunc(reduced) == s.zeros(24), "retained projector not transverse"
        )
        require(
            (ps * ps - ps).applyfunc(reduced) == s.zeros(24), "retained projector not idempotent"
        )
        defect = stiffness - s.Rational(1, 132) * (pc - ps)
        pivots = psd_pivots(defect)
        # Each one-dimensional alias distribution is exactly normalized.
        for j in range(3):
            values = [abs((1 + s.I ** ((coarse[j] + 2 * r) % 4)) / 2) ** 2 for r in range(2)]
            require(sum(values) == 1, "alias Parseval normalization")
        blocks.append(
            {
                "coarse_pi_units": list(coarse),
                "source_rank": nc.cols,
                "positive_pivots": sum(bool(s.sympify(p) > 0) for p in pivots),
                "zero_pivots": pivots.count("0"),
                "pivots": pivots,
            }
        )
        if coarse == (0, 0, 0):
            bad_matrix = stiffness - 100 * (pc - ps)
    require(bad_matrix is not None, "negative matrix not constructed")
    rejected = False
    try:
        psd_pivots(bad_matrix)
    except ValueError:
        rejected = True
    require(rejected, "false large fast constant not rejected")
    require(22**10 < 33 * 3072 * 7**10, "rational pi upper constant")
    return {
        "period": 4,
        "block_length": 2,
        "exact_field": "Q(i)",
        "full_form_constant": "1/132",
        "all_eight_alias_blocks": blocks,
        "false_constant_100_rejected": rejected,
        "pi_upper_integer_margin": 33 * 3072 * 7**10 - 22**10,
    }


def controls() -> dict:
    return {
        "scope": (
            "Finite exact n=4,L=2 incidence, actual SU2 gauge covariance, "
            "and all-mode Q(i) PSD; all-size theorem analytic."
        ),
        "geometry": geometry_controls(),
        "fourier": fourier_controls(),
    }


def main() -> None:
    if not __debug__:
        raise SystemExit("Refusing python -O for recorded exact evidence.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    require(not (args.output and args.replay), "choose output or replay")
    payload = controls()
    if args.replay:
        record = json.loads(args.replay.read_text(encoding="utf-8"))
        require(record["controls"] == payload, "finite payload differs")
        require(
            record["script_sha256"] == hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "script changed",
        )
        print(
            "PASS: exact incidence, noncommuting gauge and all eight full-form blocks replay."
        )
    elif args.output:
        record = {
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "controls": payload,
        }
        with args.output.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(record, stream, indent=2)
            stream.write("\n")
        print("PASS: finite incidence, noncommuting gauge and all eight full-form blocks recorded.")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
