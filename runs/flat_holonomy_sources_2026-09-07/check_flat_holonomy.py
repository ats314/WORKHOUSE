"""Exact finite controls for flat-background path sources; not the all-size proof.

Uses Q(i) throughout. Direct differentiated path words and Fourier/Hodge
matrices are built separately. No floating eigenvalues or tolerance decisions.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

from sympy.polys.domains import QQ_I


Q = QQ_I
ZERO, ONE, II = Q.zero, Q.one, Q(0, 1)
BITS = list(itertools.product(range(2), repeat=3))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def conj(z):
    return Q(z.x, -z.y)


def zeros(n, m=None):
    return [[ZERO for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    a = zeros(n)
    for i in range(n):
        a[i][i] = ONE
    return a


def star(a):
    return [[conj(a[i][j]) for i in range(len(a))] for j in range(len(a[0]))]


def mul(a, b):
    c = zeros(len(a), len(b[0]))
    for i, row in enumerate(a):
        for k, value in enumerate(row):
            if value:
                for j, other in enumerate(b[k]):
                    if other:
                        c[i][j] += value * other
    return c


def sub(a, b, factor=ONE):
    return [[v - factor * b[i][j] for j, v in enumerate(row)] for i, row in enumerate(a)]


def inv(a):
    n = len(a)
    rows = [row[:] + ident for row, ident in zip(a, eye(n))]
    for k in range(n):
        pivot = next((i for i in range(k, n) if rows[i][k]), None)
        require(pivot is not None, "singular inverse")
        rows[k], rows[pivot] = rows[pivot], rows[k]
        scale = rows[k][k]
        rows[k] = [z / scale for z in rows[k]]
        for i in range(n):
            if i != k and rows[i][k]:
                factor = rows[i][k]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[k])]
    return [row[n:] for row in rows]


def psd(a):
    """Exact Hermitian elimination, including the zero-pivot row condition."""
    require(a == star(a), "non-Hermitian form")
    a = [row[:] for row in a]
    positive, null = 0, 0
    pivots = []
    for k in range(len(a)):
        p = a[k][k]
        require(not p.y and p.x >= 0, f"negative/nonreal pivot {k}")
        pivots.append(str(p.x))
        if not p:
            require(all(not v for v in a[k][k + 1 :]), "zero pivot with nonzero row")
            null += 1
            continue
        positive += 1
        for i in range(k + 1, len(a)):
            for j in range(i, len(a)):
                a[i][j] -= a[i][k] * a[k][j] / p
                a[j][i] = conj(a[i][j])
    return {
        "positive": positive,
        "zero": null,
        "exact_pivot_digest": hashlib.sha256("\n".join(pivots).encode()).hexdigest(),
    }


def transverse_basis(d):
    """A full basis of ker d*, without a norm or rank tolerance."""
    pivot = next((i for i in range(3) if d[i]), None)
    if pivot is None:
        return eye(3)
    basis = zeros(3, 2)
    for col, j in enumerate(i for i in range(3) if i != pivot):
        basis[j][col] = ONE
        basis[pivot][col] = -conj(d[j]) / conj(d[pivot])
    return basis


def projection(w):
    return mul(mul(w, inv(mul(star(w), w))), star(w))


def product(values):
    answer = ONE
    for value in values:
        answer *= value
    return answer


def word_tangent(steps, transports, frequency):
    """Direct delta(word) word^-1 on a fine plane wave, at root zero.

    Position is on the universal cover. The fourth-root plane wave makes
    wrapping an exact periodic equality; transport phases retain windings.
    """
    position = [0, 0, 0]
    prefix = ONE
    out = [ZERO, ZERO, ZERO]
    for axis, sign in steps:
        if sign < 0:
            position[axis] -= 1
            prefix /= transports[axis]
        plane = II ** (sum(frequency[j] * position[j] for j in range(3)) % 4)
        out[axis] += sign * prefix * plane
        if sign > 0:
            position[axis] += 1
            prefix *= transports[axis]
    return out


def direct_symbol(transports, frequency):
    actual = zeros(3)
    phi = [ZERO, ZERO, ZERO]
    for offset in BITS:
        anchor = [(j, 1) for j in range(3) for _ in range(offset[j])]
        anchor_value = word_tangent(anchor, transports, frequency)
        for j in range(3):
            phi[j] += anchor_value[j] / 16
        for axis in range(3):
            steps = anchor + [(axis, 1), (axis, 1)] + [(j, -sign) for j, sign in reversed(anchor)]
            value = word_tangent(steps, transports, frequency)
            for j in range(3):
                # Average 1/8, Fourier factor 1/sqrt(8), then scale by sqrt(2).
                actual[axis][j] += value[j] / 16
    return actual, phi


def block(transports, coarse):
    dcoarse = [transports[j] ** 2 * (-ONE) ** coarse[j] - ONE for j in range(3)]
    basis = transverse_basis(dcoarse)
    physical_rank = len(basis[0])
    pc, stiffness = zeros(24), zeros(24)
    source = zeros(24, physical_rank)
    tangent = zeros(3, 24)
    direct_checks = 0
    for alias_index, alias in enumerate(BITS):
        frequency = [coarse[j] + 2 * alias[j] for j in range(3)]
        phases = [transports[j] * II ** frequency[j] for j in range(3)]
        d = [z - ONE for z in phases]
        q = sum((conj(z) * z for z in d), ZERO)
        require(not q.y and q.x >= 0, "invalid curl symbol")
        local_pc = (
            eye(3)
            if not q
            else [[Q(int(i == j)) - d[i] * conj(d[j]) / q for j in range(3)] for i in range(3)]
        )
        averages = [(ONE + z) / 2 for z in phases]
        common = product(averages)
        r = [common * averages[j] for j in range(3)]
        actual, phi = direct_symbol(transports, frequency)
        expected = [
            [Q(int(i == j)) * r[i] - dcoarse[i] * phi[j] for j in range(3)] for i in range(3)
        ]
        require(actual == expected, "actual anchored word differs from R-dc Phi")
        require(
            sum((phi[j] * d[j] for j in range(3)), ZERO) == (common - ONE) / 2,
            "transported anchor telescope",
        )
        for i in range(3):
            require(averages[i] * d[i] == dcoarse[i] / 2, "phase-sensitive cochain identity")
            require(
                sum((actual[i][j] * d[j] for j in range(3)), ZERO) == dcoarse[i] / 2,
                "actual tangent does not restrict gauge parameters",
            )
            for j in range(3):
                pc[3 * alias_index + i][3 * alias_index + j] = local_pc[i][j]
                stiffness[3 * alias_index + i][3 * alias_index + j] = q * local_pc[i][j]
                tangent[i][3 * alias_index + j] = actual[i][j]
            for col in range(physical_rank):
                source[3 * alias_index + i][col] = conj(r[i]) * basis[i][col]
        # Independent full Hodge expansion, not the scalar-times-projector formula.
        curl = [
            [-d[1], d[0], ZERO],
            [-d[2], ZERO, d[0]],
            [ZERO, -d[2], d[1]],
        ]
        curl_square = mul(star(curl), curl)
        require(
            curl_square == [[q * local_pc[i][j] for j in range(3)] for i in range(3)],
            "covariant Hodge identity",
        )
        direct_checks += 1
    require(mul(star(tangent), basis) == source, "physical anchor cancellation")
    ps = projection(source)
    require(mul(pc, ps) == ps and mul(ps, ps) == ps, "physical source projection")
    defect = sub(stiffness, sub(pc, ps), ONE / 132)
    inertia = psd(defect)
    source_gram = psd(mul(star(source), source))
    full_gram = psd(mul(tangent, star(tangent)))
    # T_hat=sqrt(2)T, so the exact boundary-edge lower bound is I/2.
    boundary_floor = psd(sub(mul(tangent, star(tangent)), eye(3), ONE / 2))
    require(source_gram["positive"] == physical_rank, "physical source rank")
    require(full_gram["positive"] == 3, "redundant actual tangent loses rank")
    record = {
        "coarse_pi_units": list(coarse),
        "direct_word_aliases_checked": direct_checks,
        "physical_source_rank": physical_rank,
        "physical_floor_inertia": inertia,
        "redundant_scaled_gram_inertia": full_gram,
        "redundant_boundary_floor_inertia": boundary_floor,
    }
    return record, ps, tangent, stiffness, pc


def expect_rejected(action, message):
    try:
        action()
    except ValueError:
        return True
    raise ValueError(message)


def boundary_geometry(n, length, transports):
    """Real-space boundary-column proof, including wrapped one-box geometry."""
    sites = list(itertools.product(range(n), repeat=3))
    roots = list(itertools.product(range(0, n, length), repeat=3))
    outputs = [(v, i) for v in roots for i in range(3)]
    rows = {}
    max_word = 0
    for v, axis in outputs:
        row = {}
        for offset in itertools.product(range(length), repeat=3):
            anchor = [(j, 1) for j in range(3) for _ in range(offset[j])]
            steps = anchor + [(axis, 1)] * length + [(j, -s) for j, s in reversed(anchor)]
            max_word = max(max_word, len(steps))
            pos, prefix = list(v), ONE
            for j, sign in steps:
                if sign < 0:
                    pos[j] -= 1
                    prefix /= transports[j]
                edge = (tuple(x % n for x in pos), j)
                row[edge] = row.get(edge, ZERO) + sign * prefix / length**3
                if sign > 0:
                    pos[j] += 1
                    prefix *= transports[j]
        rows[v, axis] = row
    count = 0
    output_counts = {output: 0 for output in outputs}
    for x in sites:
        for j in range(3):
            if x[j] % length != length - 1:
                continue
            v = tuple(length * (xk // length) for xk in x)
            expected = product(transports[k] ** (x[k] - v[k]) for k in range(3)) / length**2
            for output in outputs:
                require(
                    rows[output].get((x, j), ZERO) == (expected if output == (v, j) else ZERO),
                    "boundary edge has wrong transport, multiplicity or output",
                )
            output_counts[v, j] += 1
            count += 1
    require(set(output_counts.values()) == {length**2}, "boundary right inverse is incomplete")
    require(max_word == 7 * length - 6, "path length bound changed")
    return {
        "n": n,
        "L": length,
        "coarse_outputs_per_complex_color": len(outputs),
        "boundary_edges_checked": count,
        "boundary_edges_per_output": length**2,
        "boundary_gram_diagonal": str(Q(1) / length**2),
        "max_word_length": max_word,
        "single_coarse_box": n == length,
    }


def controls():
    require(__debug__, "optimized Python is not accepted")
    cases = {
        "identity": (ONE, ONE, ONE),
        "noncentral_one_axis": (Q(3, 4) / 5, ONE, ONE),
        "noncentral_two_axes": (Q(3, 4) / 5, Q(5, 12) / 13, ONE),
        "central_shifted_zero": (-ONE, ONE, ONE),
    }
    reports, saved = [], {}
    for name, transports in cases.items():
        rows = []
        for coarse in BITS:
            record, ps, tangent, stiffness, pc = block(transports, coarse)
            rows.append(record)
            if coarse == (0, 0, 0):
                saved[name] = ps, tangent, stiffness, pc
        charged_rank = sum(row["physical_source_rank"] for row in rows)
        expected = 17 if name in {"identity", "central_shifted_zero"} else 16
        require(charged_rank == expected, "complete charged physical source rank")
        reports.append(
            {
                "name": name,
                "adjoint_link_phases": [str(z) for z in transports],
                "adjoint_winding_phases": [str(z**4) for z in transports],
                "charged_source_rank": charged_rank,
                "real_su2_physical_source_rank": 17 + 2 * charged_rank,
                "real_su2_redundant_source_rank": 72,
                "blocks": rows,
            }
        )
    # Constant charged direction 1: harmonic at identity, gauge at noncentral U.
    unit = zeros(24, 1)
    unit[0][0] = ONE
    p0 = saved["identity"][0]
    pt = saved["noncentral_one_axis"][0]
    require(mul(p0, unit) == unit and mul(pt, unit) == zeros(24, 1), "rank-jump witness")
    transport = cases["noncentral_one_axis"][0]
    gauge_parameter = ONE / (transport - ONE)
    require((transport - ONE) * gauge_parameter == ONE, "witness is not a gauge gradient")

    # The covariantly constant charged direction 2 now lives at free momentum pi.
    # Free alias (pi,0,0) is (r1,r2,r3)=(1,0,0), index 4 in product order.
    shifted = zeros(24, 1)
    shifted[3 * BITS.index((1, 0, 0)) + 1][0] = ONE
    correct, tangent_shifted, stiffness, pc = saved["central_shifted_zero"]
    require(mul(stiffness, shifted) == zeros(24, 1), "shifted mode is not a zero mode")
    require(mul(pc, shifted) == shifted, "shifted mode is not physical")
    require(mul(correct, shifted) == shifted, "actual map loses the shifted harmonic")
    require(mul(p0, shifted) == zeros(24, 1), "frozen identity source negative is absent")
    require(
        mul(saved["identity"][1], shifted) == zeros(3, 1), "identity full tangent sees negative"
    )
    require(mul(tangent_shifted, shifted) != zeros(3, 1), "transported full tangent misses mode")
    frozen_source_rejected = expect_rejected(
        lambda: psd(sub(stiffness, sub(pc, p0), ONE / 132)),
        "frozen identity source passed the full form test",
    )
    phase = Q(3, 4) / 5
    wrong_phase_rejected = expect_rejected(
        lambda: require(
            ((ONE + ONE) / 2) * (phase - ONE) == (phase**2 - ONE) / 2, "dropped transport phase"
        ),
        "omitting transport phase was not rejected",
    )
    false_constant_rejected = expect_rejected(
        lambda: psd(sub(saved["identity"][2], sub(saved["identity"][3], p0), Q(100))),
        "false large fast constant accepted",
    )
    return {
        "scope": "Exact n=4,L=2 Q(i) controls; all-size and smooth-family theorems are analytic.",
        "normalization": "Symbols of T,R,Phi,E are scaled by sqrt(2); source projections are unchanged.",
        "physical_full_form_constant": "1/132",
        "backgrounds": reports,
        "independent_real_space_boundary_controls": [
            boundary_geometry(4, 2, cases["noncentral_two_axes"]),
            boundary_geometry(3, 3, cases["noncentral_two_axes"]),
            boundary_geometry(4, 4, cases["central_shifted_zero"]),
        ],
        "projection_jump": {
            "identity_rank": 51,
            "noncentral_rank": 49,
            "fixed_unit_witness_P0": "A",
            "fixed_unit_witness_Pt": "0",
            "operator_norm_difference": "1",
            "gauge_parameter_charged": str(gauge_parameter),
        },
        "negative_controls": {
            "frozen_identity_source_rejected": frozen_source_rejected,
            "transport_phase_omission_rejected": wrong_phase_rejected,
            "false_constant_100_rejected": false_constant_rejected,
        },
        "pi_constant_integer_margin": 33 * 3072 * 7**10 - 22**10,
    }


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def check_manifest(directory):
    manifest = directory / "SHA256SUMS"
    require(manifest.is_file(), "missing manifest")
    recorded = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, name = line.split(maxsplit=1)
        require(
            name not in recorded and not Path(name).is_absolute() and ".." not in Path(name).parts,
            "unsafe or duplicate manifest entry",
        )
        recorded[name] = digest
    actual = {p.relative_to(directory).as_posix() for p in directory.rglob("*") if p.is_file()}
    require(set(recorded) == actual - {"SHA256SUMS"}, "manifest coverage differs")
    for name, digest in recorded.items():
        require(
            hashlib.sha256((directory / name).read_bytes()).hexdigest() == digest,
            f"changed pinned input: {name}",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output", type=Path)
    group.add_argument("--replay", type=Path)
    args = parser.parse_args()
    require(__debug__, "optimized Python is not accepted")
    if args.replay:
        check_manifest(Path(__file__).resolve().parent)
    actual = controls()
    if args.output:
        with args.output.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(actual, handle, indent=2, sort_keys=True)
            handle.write("\n")
        print("Wrote exact finite controls:", args.output)
    else:
        expected = json.loads(
            args.replay.read_text(encoding="utf-8"), object_pairs_hook=unique_object
        )
        require(actual == expected, "replayed mathematical report differs")
        print(
            "PASS: 32 complete exact Fourier blocks, direct path words, ranks, jump and negative controls"
        )


if __name__ == "__main__":
    main()
