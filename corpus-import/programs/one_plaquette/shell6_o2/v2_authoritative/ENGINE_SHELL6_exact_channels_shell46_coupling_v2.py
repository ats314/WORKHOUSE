#!/usr/bin/env python3
"""
Exact shell-six channel extraction and shell-four/shell-six T1^{+-} coupling.

Inputs:
  CERT_SHELL6_o2_matrix_v2.json
  shell6_o2_full_intermediate_v2.py
  ENGINE_SHELL6_o2_full_intermediate_v1.py
  ENGINE_FLUX_su3_moments_ext.py

Outputs:
  CERT_SHELL6_o2_exact_channel_certificate_v2.json
  CERT_SHELL6_shell46_t1_coupling_certificate_v1.json
  THM_SHELL6_shell46_theorem_v2.md
  DATA_SHELL6_shell46_t1_o2_diagnostic_scan.csv

All coefficients use u = beta_lat/6 = 1/g^4.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
MATRIX_PATH = HERE / "CERT_SHELL6_o2_matrix_v2.json"
ENGINE_PATH = HERE / "shell6_o2_full_intermediate_v2.py"

if not MATRIX_PATH.exists():
    raise FileNotFoundError(MATRIX_PATH)
if not ENGINE_PATH.exists():
    raise FileNotFoundError(ENGINE_PATH)

spec = importlib.util.spec_from_file_location("shell6_engine", ENGINE_PATH)
engine = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(engine)


def gate(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s} {name} {detail}")
    if not condition:
        raise RuntimeError(f"{name}: {detail}")


def enumerate_simple_shapes(length: int):
    found = set()

    def dfs(sequence, position, visited):
        if len(sequence) == length:
            if (
                position == (0, 0, 0)
                and (sequence[-1] ^ 1) != sequence[0]
            ):
                found.add(engine.canon_step_cycle(tuple(sequence)))
            return

        for direction in range(6):
            if sequence and (sequence[-1] ^ 1) == direction:
                continue
            next_position = tuple(
                position[k] + engine.DIRS[direction][k]
                for k in range(3)
            )
            if next_position == (0, 0, 0):
                if len(sequence) + 1 != length:
                    continue
            elif next_position in visited:
                continue
            dfs(
                sequence + [direction],
                next_position,
                visited | {next_position},
            )

    dfs([], (0, 0, 0), {(0, 0, 0)})
    return sorted(found)


def permutation_representations(shapes):
    index = {shape: i for i, shape in enumerate(shapes)}
    group = engine.signed_permutation_group()
    representations = []

    for matrix in group:
        representation = sp.zeros(len(shapes))
        for column, shape in enumerate(shapes):
            transformed = engine.transform_shape(shape, matrix)
            representation[index[transformed], column] = 1
        representations.append(representation)

    return group, representations


def reversal_matrix(shapes):
    index = {shape: i for i, shape in enumerate(shapes)}
    matrix = sp.zeros(len(shapes))
    for column, shape in enumerate(shapes):
        matrix[index[engine.reverse_shape(shape)], column] = 1
    return matrix


def channel_projector(shapes, irrep: str, parity: str):
    group, representations = permutation_representations(shapes)
    projector = sp.zeros(len(shapes))

    for matrix, representation in zip(group, representations):
        projector += (
            engine.irrep_character(irrep, parity, matrix)
            * representation
        )

    projector *= sp.Rational(
        engine.IRREP_DIMENSIONS[irrep],
        48,
    )
    odd = (sp.eye(len(shapes)) - reversal_matrix(shapes)) / 2
    result = odd * projector

    gate(
        f"{irrep}{parity}- projector idempotent",
        result * result == result,
    )
    return result


def action_in_basis(operator: sp.Matrix, basis: sp.Matrix):
    rank = basis.cols
    _rref, pivot_rows = basis.T.rref()
    rows = list(pivot_rows)
    gate("basis has full column rank", len(rows) == rank)
    square = basis.extract(rows, range(rank))
    gate("pivot-row submatrix invertible", square.det() != 0)
    return sp.simplify(
        square.inv()
        * (operator * basis).extract(rows, range(rank))
    )


def exact_channel_data(shapes, h1, h2):
    data = {}

    for irrep, parity, channel in (
        ("A1", "-", "0--"),
        ("A2", "+", "3+-"),
        ("E", "-", "2--(E)"),
        ("T1", "+", "1+-"),
        ("T2", "+", "2+-"),
        ("T2", "-", "2--(T2)"),
    ):
        projector = channel_projector(shapes, irrep, parity)
        columns = projector.columnspace()
        gate(f"{irrep}{parity}- nonempty", bool(columns))
        basis = sp.Matrix.hstack(*columns)

        block1 = action_in_basis(h1, basis)
        block2 = action_in_basis(h2, basis)

        row = {
            "channel": channel,
            "irrep": f"{irrep}{parity}-",
            "rank": basis.cols,
            "multiplicity": (
                basis.cols // engine.IRREP_DIMENSIONS[irrep]
            ),
            "H1_characteristic_polynomial": str(
                sp.factor(block1.charpoly().as_expr())
            ),
            "H2_characteristic_polynomial": str(
                sp.factor(block2.charpoly().as_expr())
            ),
        }

        if irrep == "T1":
            a = 2 * sp.sqrt(2) / 3
            p_zero = sp.eye(basis.cols) - sp.Rational(9, 8) * block1**2
            p_minus = sp.Rational(1, 2) * (
                sp.Rational(9, 8) * block1**2 - block1 / a
            )
            p_plus = sp.Rational(1, 2) * (
                sp.Rational(9, 8) * block1**2 + block1 / a
            )

            branches = []
            for label, first_order, spectral_projector in (
                ("lower", -a, p_minus),
                ("middle", sp.Integer(0), p_zero),
                ("upper", a, p_plus),
            ):
                rank = sp.trace(spectral_projector)
                gate(f"T1 {label} rank", rank == 3, str(rank))
                second_order = sp.simplify(
                    sp.trace(spectral_projector * block2) / 3
                )
                residual = (
                    spectral_projector
                    * block2
                    * spectral_projector
                    - second_order * spectral_projector
                ).applyfunc(sp.simplify)
                gate(
                    f"T1 {label} H2 scalar on irrep row space",
                    residual == sp.zeros(*residual.shape),
                )
                branches.append(
                    {
                        "branch": label,
                        "first_order": str(first_order),
                        "second_order_connected": str(second_order),
                        "second_order_decimal": float(
                            sp.N(second_order, 17)
                        ),
                    }
                )
            row["branches"] = branches
        else:
            row["H1_eigenvalues"] = {
                str(value): multiplicity
                for value, multiplicity in block1.eigenvals().items()
            }
            row["H2_eigenvalues"] = {
                str(value): multiplicity
                for value, multiplicity in block2.eigenvals().items()
            }

        data[f"{irrep}{parity}-"] = row

    return data


def build_shell46_cross_matrix(shell4_shapes, shell6_shapes):
    shell6_index = {
        engine.canonical_edges_translation(
            engine.word_to_edges(
                engine.steps_to_word((0, 0, 0), shape)[0]
            )
        ): index
        for index, shape in enumerate(shell6_shapes)
    }
    shell4_index = {
        engine.canonical_edges_translation(
            engine.word_to_edges(
                engine.steps_to_word((0, 0, 0), shape)[0]
            )
        ): index
        for index, shape in enumerate(shell4_shapes)
    }

    cross_64 = [
        [sp.Integer(0) for _ in shell4_shapes]
        for _ in shell6_shapes
    ]

    for column, shape in enumerate(shell4_shapes):
        word, endpoint = engine.steps_to_word((0, 0, 0), shape)
        gate("shell-four word closes", endpoint == (0, 0, 0))
        links = {link for link, _power in word}

        for plaquette in engine.touching(links):
            expression = engine.canon_expr((word, plaquette))
            for edges, amplitude in engine.project_shell(
                expression, 6
            ).items():
                key = engine.canonical_edges_translation(edges)
                if key in shell6_index:
                    cross_64[shell6_index[key]][column] -= sp.Rational(
                        amplitude.numerator,
                        amplitude.denominator,
                    )

    cross_46 = [
        [sp.Integer(0) for _ in shell6_shapes]
        for _ in shell4_shapes
    ]
    for column, shape in enumerate(shell6_shapes):
        word, endpoint = engine.steps_to_word((0, 0, 0), shape)
        gate("shell-six word closes", endpoint == (0, 0, 0))
        links = {link for link, _power in word}

        for plaquette in engine.touching(links):
            expression = engine.canon_expr((word, plaquette))
            for edges, amplitude in engine.project_shell(
                expression, 4
            ).items():
                key = engine.canonical_edges_translation(edges)
                if key in shell4_index:
                    cross_46[shell4_index[key]][column] -= sp.Rational(
                        amplitude.numerator,
                        amplitude.denominator,
                    )

    c64 = sp.Matrix(cross_64)
    c46 = sp.Matrix(cross_46)
    gate("shell-four/shell-six Hermitian cross-check", c46 == c64.T)
    gate("cross matrix has 60 nonzero entries", len([
        value for value in c64 if value != 0
    ]) == 60)
    gate(
        "cross entries are -1/3 or -2/3",
        set(value for value in c64 if value != 0)
        == {sp.Rational(-1, 3), sp.Rational(-2, 3)},
    )
    return c64


def coupling_data(shell4_shapes, shell6_shapes, h1, h2, c64):
    p4 = channel_projector(shell4_shapes, "T1", "+")
    p6 = channel_projector(shell6_shapes, "T1", "+")

    gate("shell-four T1+- rank", p4.rank() == 3, str(p4.rank()))
    gate("shell-six T1+- rank", p6.rank() == 9, str(p6.rank()))
    projected_cross = p6 * c64 * p4
    gate("projected T1+- cross block rank", projected_cross.rank() == 3, str(projected_cross.rank()))

    total_kernel = p4 * c64.T * p6 * c64 * p4
    total_g2 = sp.simplify(sp.trace(total_kernel) / 3)
    total_residual = (total_kernel - total_g2 * p4).applyfunc(sp.simplify)
    gate(
        "total coupling is scalar on shell-four T1",
        total_residual == sp.zeros(*total_residual.shape),
    )
    gate("total g^2", total_g2 == sp.Rational(16, 9), str(total_g2))

    a = 2 * sp.sqrt(2) / 3
    p6_zero = p6 * (
        sp.eye(len(shell6_shapes))
        - sp.Rational(9, 8) * h1**2
    )
    p6_minus = p6 * sp.Rational(1, 2) * (
        sp.Rational(9, 8) * h1**2 - h1 / a
    )
    p6_plus = p6 * sp.Rational(1, 2) * (
        sp.Rational(9, 8) * h1**2 + h1 / a
    )

    coupling_branches = []
    expected_g2 = {
        "lower": sp.Rational(4, 9),
        "middle": sp.Rational(8, 9),
        "upper": sp.Rational(4, 9),
    }

    shell6_projectors = {
        "lower": p6_minus,
        "middle": p6_zero,
        "upper": p6_plus,
    }

    for label, projector in shell6_projectors.items():
        kernel = p4 * c64.T * projector * c64 * p4
        g2 = sp.simplify(sp.trace(kernel) / 3)
        coupling_residual = (kernel - g2 * p4).applyfunc(sp.simplify)
        gate(
            f"{label} coupling scalar",
            coupling_residual == sp.zeros(*coupling_residual.shape),
        )
        gate(
            f"{label} coupling strength",
            g2 == expected_g2[label],
            str(g2),
        )
        coupling_branches.append(
            {
                "branch": label,
                "g_squared": str(g2),
                "g_positive_convention": str(sp.sqrt(g2)),
            }
        )

    # Folded shell-six H2 coefficients.
    t1_projector = p6
    t1_basis = sp.Matrix.hstack(*t1_projector.columnspace())
    t1_h1 = action_in_basis(h1, t1_basis)
    t1_h2 = action_in_basis(h2, t1_basis)

    local_a = 2 * sp.sqrt(2) / 3
    local_projectors = {
        "lower": sp.Rational(1, 2) * (
            sp.Rational(9, 8) * t1_h1**2 - t1_h1 / local_a
        ),
        "middle": (
            sp.eye(t1_basis.cols)
            - sp.Rational(9, 8) * t1_h1**2
        ),
        "upper": sp.Rational(1, 2) * (
            sp.Rational(9, 8) * t1_h1**2 + t1_h1 / local_a
        ),
    }
    first_orders = {
        "lower": -local_a,
        "middle": sp.Integer(0),
        "upper": local_a,
    }

    folded_mu = {}
    unfolded_mu = {}
    for item in coupling_branches:
        label = item["branch"]
        projector = local_projectors[label]
        folded = sp.simplify(sp.trace(projector * t1_h2) / 3)
        g2 = sp.sympify(item["g_squared"])
        unfolded = sp.simplify(
            folded - sp.Rational(3, 4) * g2
        )
        folded_mu[label] = folded
        unfolded_mu[label] = unfolded
        item["first_order"] = str(first_orders[label])
        item["folded_shell6_H2"] = str(folded)
        item["unfolded_shell6_H2"] = str(unfolded)

    shell4_folded_m2 = sp.Rational(11, 306)
    shell4_virtual_shell6 = (
        -sp.Rational(3, 4) * total_g2
    )
    shell4_unfolded_m2 = sp.simplify(
        shell4_folded_m2 - shell4_virtual_shell6
    )
    gate(
        "shell-four virtual shell-six contribution",
        shell4_virtual_shell6 == -sp.Rational(4, 3),
    )
    gate(
        "shell-four unfolded m2",
        shell4_unfolded_m2 == sp.Rational(419, 306),
        str(shell4_unfolded_m2),
    )

    return {
        "cross_matrix_shape": [c64.rows, c64.cols],
        "cross_matrix_nonzero_entries": 60,
        "cross_matrix_values": ["-1/3", "-2/3"],
        "total_g_squared": str(total_g2),
        "branches": coupling_branches,
        "shell4": {
            "folded_m2": str(shell4_folded_m2),
            "virtual_shell6_contribution": str(
                shell4_virtual_shell6
            ),
            "unfolded_m2": str(shell4_unfolded_m2),
        },
        "normal_form": {
            "basis": [
                "shell4",
                "shell6_lower",
                "shell6_middle",
                "shell6_upper",
            ],
            "H0_diagonal": ["8/3", "4", "4", "4"],
            "H1_diagonal": [
                "1",
                str(first_orders["lower"]),
                "0",
                str(first_orders["upper"]),
            ],
            "H1_shell4_couplings_positive_phase": [
                "2/3",
                "2*sqrt(2)/3",
                "2/3",
            ],
            "H2_unfolded_diagonal": [
                str(shell4_unfolded_m2),
                str(unfolded_mu["lower"]),
                str(unfolded_mu["middle"]),
                str(unfolded_mu["upper"]),
            ],
            "scope": (
                "Des-Cloizeaux normal form through O(u^2). "
                "Cross-shell O(u^2) matrix elements are not included."
            ),
        },
    }


def diagnostic_scan(coupling, output_path: Path):
    sqrt2 = math.sqrt(2.0)

    alpha4 = 419.0 / 306.0
    mu_lower = float(
        sp.N(sp.sympify(
            coupling["branches"][0]["unfolded_shell6_H2"]
        ), 17)
    )
    mu_middle = float(
        sp.N(sp.sympify(
            coupling["branches"][1]["unfolded_shell6_H2"]
        ), 17)
    )
    mu_upper = float(
        sp.N(sp.sympify(
            coupling["branches"][2]["unfolded_shell6_H2"]
        ), 17)
    )

    first = np.array([-2 * sqrt2 / 3, 0.0, 2 * sqrt2 / 3])
    second = np.array([mu_lower, mu_middle, mu_upper])
    couplings = np.array([2 / 3, 2 * sqrt2 / 3, 2 / 3])

    rows = []
    for u in np.linspace(0.0, 0.40, 401):
        matrix = np.zeros((4, 4), dtype=float)
        matrix[0, 0] = 8 / 3 + u + alpha4 * u * u
        matrix[1:, 1:] = np.diag(
            4.0 + first * u + second * u * u
        )
        matrix[0, 1:] = couplings * u
        matrix[1:, 0] = couplings * u

        eigenvalues, eigenvectors = np.linalg.eigh(matrix)
        rows.append(
            {
                "u": u,
                "lowest_energy_O2_normal_form": eigenvalues[0],
                "second_energy_O2_normal_form": eigenvalues[1],
                "gap": eigenvalues[1] - eigenvalues[0],
                "lowest_shell4_weight": eigenvectors[0, 0] ** 2,
                "lowest_shell6_lower_weight": eigenvectors[1, 0] ** 2,
                "lowest_shell6_middle_weight": eigenvectors[2, 0] ** 2,
                "lowest_shell6_upper_weight": eigenvectors[3, 0] ** 2,
            }
        )

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    closest = min(
        rows,
        key=lambda row: abs(row["lowest_shell4_weight"] - 0.5),
    )
    return {
        "scan_range": "0 <= u <= 0.40",
        "shell4_weight_half_nearest_u": closest["u"],
        "shell4_weight_at_that_point": closest[
            "lowest_shell4_weight"
        ],
        "warning": (
            "This scan is a truncated O(u^2) diagnostic, not a continuum "
            "extrapolation or controlled finite-coupling prediction."
        ),
    }


def main():
    payload = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))
    shell6_shapes = [
        tuple(shape) for shape in payload["shell_shapes"]
    ]
    h1 = sp.Matrix([
        [sp.Rational(value) for value in row]
        for row in payload["H1"]
    ])
    h2 = sp.Matrix([
        [sp.Rational(value) for value in row]
        for row in payload["H2_connected"]
    ])

    gate("shell-six matrix dimension", h1.shape == (44, 44))
    gate("shell-six H2 dimension", h2.shape == (44, 44))
    gate("shell-six H1 symmetric", h1 == h1.T)
    gate("shell-six H2 symmetric", h2 == h2.T)

    channels = exact_channel_data(shell6_shapes, h1, h2)

    channel_certificate = {
        "meta": {
            "version": "2026-06-14-shell6-exact-channels-v2",
            "variable": "u=beta_lat/6=1/g^4",
            "common_disconnected_scalar_omitted": True,
        },
        "channels": channels,
        "ordering": {
            "first_order": (
                "The lower T1+- branch is the unique shell-six branch "
                "with negative O(u) coefficient."
            ),
            "first_order_flat_exotic_lowest_at_Ou2": "T2+- lower branch",
            "three_plus_minus_below_zero_minus": True,
            "E_3+-_minus_E_0--_coefficient": str(
                -sp.Rational(1107923, 959310)
            ),
        },
    }

    shell4_shapes = enumerate_simple_shapes(4)
    gate("shell-four oriented basis size", len(shell4_shapes) == 6)
    c64 = build_shell46_cross_matrix(
        shell4_shapes,
        shell6_shapes,
    )
    coupling = coupling_data(
        shell4_shapes,
        shell6_shapes,
        h1,
        h2,
        c64,
    )

    scan_path = HERE / "DATA_SHELL6_shell46_t1_o2_diagnostic_scan.csv"
    scan = diagnostic_scan(coupling, scan_path)
    coupling["diagnostic_scan"] = scan

    channel_path = (
        HERE / "CERT_SHELL6_o2_exact_channel_certificate_v2.json"
    )
    channel_path.write_text(
        json.dumps(
            channel_certificate,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    coupling_path = (
        HERE / "CERT_SHELL6_shell46_t1_coupling_certificate_v1.json"
    )
    coupling_path.write_text(
        json.dumps(coupling, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    theorem = r"""# Exact shell-six O(u²) spectrum and shell-four/shell-six coupling

## Convention

\[
u=\frac{\beta_{\rm lat}}6=\frac1{g^4},
\qquad
H=H_0-uW.
\]

A common disconnected vacuum scalar is omitted from the shell-six second-order
matrix. It cancels in channel differences and does not affect ordering.

## Shell-six C-odd spectrum

The first-order-flat exotic channels split at second order as follows:

\[
\begin{aligned}
0^{--}\;(A_1^{--}):\quad&
-\frac{6117632}{479655}u^2,\\
3^{+-}\;(A_2^{+-}):\quad&
-\frac{21281}{1530}u^2,\\
2^{--}\;(E^{--}):\quad&
-\frac{6597287}{479655}u^2,\\
2^{--}\;(T_2^{--}):\quad&
-\frac{6277517}{479655}u^2.
\end{aligned}
\]

The two \(T_2^{+-}\) multiplicity branches have coefficients

\[
-\frac{27013849}{1918620}
\pm\frac{\sqrt{59782141}}{9180}.
\]

The lower one is the lowest among the channels that remain flat at first
order.

The shell-six \(T_1^{+-}\) branches are

\[
\begin{aligned}
E_{6,-}(u)
&=
4-\frac{2\sqrt2}{3}u
+\left(
-\frac{13029053}{959310}-\frac{\sqrt2}{2}
\right)u^2+O(u^3),\\
E_{6,0}(u)
&=
4-\frac{52959}{3553}u^2+O(u^3),\\
E_{6,+}(u)
&=
4+\frac{2\sqrt2}{3}u
+\left(
-\frac{13029053}{959310}+\frac{\sqrt2}{2}
\right)u^2+O(u^3).
\end{aligned}
\]

In particular,

\[
E_{3^{+-}}-E_{0^{--}}
=
-\frac{1107923}{959310}u^2+O(u^3),
\]

so \(3^{+-}\) lies below \(0^{--}\) at second order.

## Exact shell-four/shell-six first-order coupling

The exact cross-shell matrix has 60 nonzero oriented entries, each
\(-1/3\) or \(-2/3\), and is Hermitian under the independently computed
reverse action.

After projection to \(T_1^{+-}\),

\[
g_-^2=\frac49,\qquad
g_0^2=\frac89,\qquad
g_+^2=\frac49,
\]

so

\[
g_{\rm total}^2=\frac{16}{9}.
\]

## Unfolded O(u²) normal form

The published shell-four coefficient

\[
m_2=\frac{11}{306}
\]

already contains virtual shell-six propagation. Explicitly,

\[
\Delta m_2^{(6)}
=
-\frac34g_{\rm total}^2
=
-\frac43.
\]

Therefore the shell-four diagonal used in an explicit coupled-shell
Hamiltonian is

\[
m_{2,\rm unfolded}
=
\frac{11}{306}+\frac43
=
\frac{419}{306}.
\]

Likewise, the shell-six folded second-order coefficients must have the
virtual shell-four terms \(3g_i^2/4\) removed. The resulting normal-form
diagonal is

\[
\begin{aligned}
\mu_-^{\rm unfolded}
&=
-\frac{13348823}{959310}-\frac{\sqrt2}{2},\\
\mu_0^{\rm unfolded}
&=
-\frac{165983}{10659},\\
\mu_+^{\rm unfolded}
&=
-\frac{13348823}{959310}+\frac{\sqrt2}{2}.
\end{aligned}
\]

In the positive-coupling phase convention, the coupled normal form through
second order is

\[
H_{\rm normal}(u)=
\begin{pmatrix}
\frac83+u+\frac{419}{306}u^2
&\frac23u&\frac{2\sqrt2}{3}u&\frac23u\\
\frac23u
&4-\frac{2\sqrt2}{3}u+\mu_-^{\rm unfolded}u^2&0&0\\
\frac{2\sqrt2}{3}u
&0&4+\mu_0^{\rm unfolded}u^2&0\\
\frac23u
&0&0&4+\frac{2\sqrt2}{3}u+\mu_+^{\rm unfolded}u^2
\end{pmatrix}
+O(u^3).
\]

This normal form exactly reproduces the folded shell-four and shell-six
second-order coefficients when either shell is perturbatively eliminated.
Cross-shell matrix elements at order \(u^2\) are not yet included.

The accompanying finite-\(u\) scan is diagnostic only. It is not a controlled
continuum extrapolation.
"""
    theorem_path = HERE / "THM_SHELL6_shell46_theorem_v2.md"
    theorem_path.write_text(theorem, encoding="utf-8")

    print("ALL EXACT CHANNEL AND COUPLING GATES PASS")
    print(channel_path)
    print(coupling_path)
    print(theorem_path)
    print(scan_path)


if __name__ == "__main__":
    main()
