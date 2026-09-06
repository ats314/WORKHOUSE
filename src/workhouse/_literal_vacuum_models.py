"""Exact finite controls for literal true-vacuum sources and tensor leakage.

These certify finite matrix/sequence identities, not the Wilson harmonic
limit, elliptic domain facts, or an interacting infinite-volume theorem.
"""

from __future__ import annotations

import itertools

import sympy as sp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def psd_certificate(matrix):
    """Rational semidefinite elimination, keeping zero-pivot conditions."""
    current = sp.Matrix(matrix)
    require(current == current.T, "symmetric rational matrix")
    require(all(entry.is_Rational for entry in current), "exact rational entries")
    pivots = []
    for index in range(current.rows):
        pivot = current[index, index]
        require(pivot >= 0, "nonnegative Schur pivot")
        pivots.append(str(pivot))
        if pivot == 0:
            require(
                all(current[index, j] == 0 for j in range(index + 1, current.cols)),
                "a zero PSD pivot has no remaining off-diagonal row",
            )
            continue
        for row in range(index + 1, current.rows):
            for column in range(row, current.cols):
                value = current[row, column] - current[row, index] * current[index, column] / pivot
                current[row, column] = current[column, row] = value
    return pivots


def literal_weighted_graph():
    # Positive normalized nonproduct vacuum on two coarse by two fiber points.
    omega = sp.Matrix([144, 96, 72, 83]) / 205
    require(
        (omega.T * omega)[0] == 1 and all(entry > 0 for entry in omega),
        "strictly positive normalized vacuum",
    )
    laplace = sp.zeros(4)
    edges = ((0, 1, 2), (1, 2, 3), (2, 3, 5), (3, 0, 7), (0, 2, 1))
    for first, second, conductance in edges:
        difference = sp.eye(4)[:, first] - sp.eye(4)[:, second]
        laplace += conductance * difference * difference.T
    inverse_vacuum = sp.diag(*(1 / item for item in omega))
    hamiltonian = inverse_vacuum * laplace * inverse_vacuum
    require(hamiltonian * omega == sp.zeros(4, 1), "true zero vacuum")
    require(laplace.rank() == 3, "connected graph gives a unique vacuum")
    psd_certificate(hamiltonian)
    coarse = sp.Matrix([[1, 0], [1, 0], [0, 1], [0, 1]])
    source = sp.diag(*omega) * coarse
    marginal = sp.diag(sum(omega[j] ** 2 for j in (0, 1)), sum(omega[j] ** 2 for j in (2, 3)))
    require(source.T * source == marginal, "actual weighted source isometry")
    projection = source * marginal.inv() * source.T
    require(
        projection == projection.T and projection**2 == projection,
        "closed literal range projection",
    )
    require(projection * omega == omega, "literal projection contains the true vacuum")
    compressed = source.T * hamiltonian * source
    require(
        compressed == coarse.T * laplace * coarse == sp.Matrix([[11, -11], [-11, 11]]),
        "exact true-vacuum weighted coarse form",
    )
    a, b = sp.symbols("a b", real=True)
    test = sp.Matrix([a, b])
    require(
        sp.expand((test.T * compressed * test)[0] - 11 * (a - b) ** 2) == 0,
        "symbolic ground-state transform",
    )
    raw_projection = 2 * source * source.T
    require(
        raw_projection**2 != raw_projection,
        "raw uniform marginal cannot replace the quantum marginal",
    )
    shifted = hamiltonian + 13 * sp.eye(4)
    require(
        source.T * (shifted - 13 * sp.eye(4)) * source == compressed,
        "full vacuum energy subtraction",
    )
    require(
        (omega.T * shifted * omega)[0] == 13,
        "omitting the true vacuum shift leaves nonzero vacuum energy",
    )
    return {
        "marginal": [str(marginal[i, i]) for i in range(2)],
        "coarse_conductance": "11",
        "unique_true_vacuum": True,
        "vacuum_in_literal_range_exact": True,
        "source_Gram_equals_marginal": True,
        "raw_uniform_projection_not_idempotent": True,
        "omitted_vacuum_shift": "13",
    }


def tensor_leakage_control():
    a, b, high = sp.Integer(4), sp.Integer(7), sp.Integer(11)
    c, s = sp.Rational(3, 5), sp.Rational(4, 5)
    retained = sp.diag(1, 0, 0, 0)
    vector = sp.Matrix([0, c, s, 0])
    retained += vector * vector.T
    floor = b - (b - a) * s**2
    require(floor == sp.Rational(127, 25), "refined floor keeps first-level energy")
    require(
        retained**2 == retained and retained[:, 0] == sp.eye(4)[:, 0], "retained vacuum is exact"
    )
    rows = []
    for count in (1, 2, 3):
        dimension = 4**count
        total_projection = sp.kronecker_product(*(retained for _ in range(count)))
        complement = sp.eye(dimension) - total_projection
        indices = [4**j for j in range(count)]
        low_indices = [0, *indices]
        gram = complement.extract(low_indices, low_indices)
        require(
            gram == sp.diag(0, *(s**2 for _ in indices)),
            "orthogonal one-excitation leakage has no copy-count factor",
        )
        energies = [
            sum((0, a, b, high)[j] for j in state)
            for state in itertools.product(range(4), repeat=count)
        ]
        remainder = [
            energy - (0 if index == 0 else a if index in indices else b)
            for index, energy in enumerate(energies)
        ]
        require(all(value >= 0 for value in remainder), "complete additive low spectral sector")
        psd = None
        if count <= 2:
            compressed = complement * sp.diag(*energies) * complement
            psd = psd_certificate(compressed - floor * complement)
            wrong = compressed - b * complement
            try:
                psd_certificate(wrong)
            except AssertionError:
                pass
            else:
                raise AssertionError("Omitting leakage must reject the false floor b")
        trial = complement[:, indices[0]]
        rayleigh = (trial.T * sp.diag(*energies) * trial)[0] / (trial.T * trial)[0]
        require(rayleigh == floor, "one-excitation trial attains the refined floor")
        rows.append(
            {
                "copies": count,
                "dimension": dimension,
                "low_rank": count + 1,
                "leakage_squared": str(s**2),
                "compressed_floor": str(floor),
                "literal_low_frame_squared": str(1 - s**2),
                "complete_spectral_remainder_nonnegative": True,
                "full_compression_PSD_pivots": psd,
                "floor_attained": True,
            }
        )
    g = sp.symbols("g", positive=True)
    sine = 2 * g**2 / (1 + g**4)
    require(sp.limit(b - (b - a) * sine**2, g, 0) == b, "scalar small-leakage limit")
    return {
        "models": rows,
        "first_gap": str(a),
        "second_gap": str(b),
        "two_first_gaps_above_second": bool(2 * a >= b),
        "no_vacuum_overlap_product_loss": True,
        "small_leakage_floor_limit": str(b),
        "scope": "Exact one-, two- and three-copy controls; all-copy conclusion is analytic.",
    }


def cutoff_negative_control():
    n = sp.symbols("n", positive=True)
    cosine, sine = (n**2 - 1) / (n**2 + 1), 2 * n / (n**2 + 1)
    require(sp.cancel(cosine**2 + sine**2 - 1) == 0, "normalized sequence")
    norm_error = sp.cancel((cosine - 1) ** 2 + sine**2)
    multiplied_error = sp.cancel(n**2 * sine**2)
    require(sp.limit(norm_error, n, sp.oo) == 0, "L2 vacuum convergence")
    require(
        sp.limit(multiplied_error, n, sp.oo) == 4,
        "unbounded multiplication does not preserve that convergence",
    )
    return {
        "Hilbert_space": "l2(N_0)",
        "vacuum_n": "c_n e_0+s_n e_n",
        "multiplier": "p e_k=k e_k",
        "vacuum_limit": "e_0",
        "norm_error_squared": str(norm_error),
        "norm_error_limit": "0",
        "multiplied_error_squared": str(multiplied_error),
        "multiplied_error_limit": "4",
        "fixed_cutoff_then_limit": "For n>R, p_R(c_n e_0+s_n e_n)=0=p_R e_0.",
    }


def controls():
    if not __debug__:
        raise RuntimeError("Optimized Python is rejected for exact verification")
    return {
        "literal_weighted_graph": literal_weighted_graph(),
        "tensor_leakage": tensor_leakage_control(),
        "unbounded_multiplier_counterexample": cutoff_negative_control(),
    }


# Derived from immutable original under next_nonlinear/:
# next_literal/check_literal_vacuum_projection.py
# Original SHA256: d252b19e5b8c7ab9bb27bbcd83ce66122612d10160b98bf49d4a31bfdf64775f
