"""Exact finite controls for harmonic boundary and physical scale comparisons.

Reusable acceptance uses only exact arithmetic. The original research controls
are independently preserved in the run, not imported by this module. These
finite identities do not machine-certify the all-size, closed-form, Fock-density,
or nonlinear Wilson theorems; their proofs and hypotheses remain separate.
"""

from __future__ import annotations

import copy
from functools import lru_cache
from itertools import combinations

import sympy as s


def require(statement, message):
    if not statement:
        raise ValueError(message)


def positive_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def exact_symmetric(matrix, name):
    matrix = s.Matrix(matrix)
    require(matrix.rows > 0 and matrix.rows == matrix.cols, f"{name} must be nonempty square")
    require(matrix == matrix.T, f"{name} must be real symmetric")
    require(all(x.is_Rational for x in matrix), f"{name} must have exact rational entries")
    return matrix


def require_psd(matrix):
    """All principal minors: an exact finite real-symmetric PSD criterion."""
    matrix = exact_symmetric(matrix, "PSD matrix")
    for size in range(1, matrix.rows + 1):
        for indices in combinations(range(matrix.rows), size):
            require(
                matrix.extract(indices, indices).det() >= 0, "Matrix is not positive semidefinite"
            )


def rational_interval_replay(polynomial, interval, index):
    """Verify a simple positive real root's position by exact Sturm counts.

    The zero-based index counts all preceding real roots. Endpoints must be
    rational nonroots, so count_roots' closed-interval convention is harmless.
    """
    poly = s.Poly(polynomial)
    require(len(poly.gens) == 1 and poly.degree() > 0, "A univariate polynomial is required")
    require(all(value.is_Rational for value in poly.all_coeffs()), "Polynomial must be rational")
    require(
        not isinstance(index, bool) and isinstance(index, int) and index >= 0, "Invalid root index"
    )
    require(
        isinstance(interval, (list, tuple)) and len(interval) == 2, "Need two interval endpoints"
    )
    lo, hi = map(s.sympify, interval)
    require(
        lo.is_Rational and hi.is_Rational and 0 < lo < hi,
        "Ordered positive rational endpoints required",
    )
    require(poly.eval(lo) != 0 and poly.eval(hi) != 0, "Interval endpoint is a root")
    require(poly.count_roots(-s.oo, lo) == index, "Wrong root index")
    require(poly.count_roots(lo, hi) == 1, "Interval must contain exactly one root")
    require(poly.gcd(poly.diff()).count_roots(lo, hi) == 0, "Root must be simple")
    return lo, hi


def gaussian_schur_blocks(fast, coupling, static, floor):
    """Construct the full rational positive block and its induced graph norm."""
    fast = exact_symmetric(fast, "Fast block")
    static = exact_symmetric(static, "Static Schur block")
    coupling = s.Matrix(coupling)
    require(coupling.shape == (static.rows, fast.rows), "Coupling dimensions do not match")
    require(all(x.is_Rational for x in coupling), "Coupling must be rational")
    floor = s.sympify(floor)
    require(floor.is_Rational and floor > 0, "Fast floor must be positive rational")
    require_psd(fast - floor * s.eye(fast.rows))
    require_psd(static)
    require(static.det() > 0, "Gaussian static block must be strictly positive")
    u = fast.inv() * coupling.T
    metric = s.eye(static.rows) + u.T * u
    retained = static + coupling * u
    full = retained.row_join(coupling).col_join(coupling.T.row_join(fast))
    graph = s.eye(static.rows).col_join(-u)
    require(graph.T * graph == metric and graph.T * full * graph == static, "Graph identities fail")
    return full, metric, retained, graph


def replay_gaussian_enclosures(fast, coupling, static, floor, certificates):
    """Replay finite sorted-eigenvalue comparisons without an eigensolver."""
    full, metric, _, _ = gaussian_schur_blocks(fast, coupling, static, floor)
    static, floor = s.Matrix(static), s.Rational(floor)
    z = s.Symbol("z")
    full_poly = full.charpoly(z).as_poly()
    coarse_poly = s.Poly((static - z * metric).det(), z)
    require(len(certificates) == static.rows, "Incomplete retained spectrum")
    for index, entry in enumerate(certificates):
        require(entry["j"] == index + 1, "Certificate indices must be consecutive")
        lo, hi = rational_interval_replay(full_poly, entry["lambda_interval"], index)
        mlo, mhi = rational_interval_replay(coarse_poly, entry["mu_interval"], index)
        lower, upper = floor * mhi / (floor + mhi), mlo
        require(lower < lo <= hi < upper, "Schur eigenvalue comparison failed")
        require(
            s.Rational(entry["strict_lower_control"]) == lower, "Incorrect lower comparison margin"
        )
        require(
            s.Rational(entry["strict_upper_control"]) == upper, "Incorrect upper comparison margin"
        )
    return True


def inverse_fast_budget(initial_gap, fast_floors):
    """Finite exact conditional recursion; it does not assert Wilson premises."""
    values = [s.sympify(initial_gap), *(s.sympify(x) for x in fast_floors)]
    require(
        all(x.is_Rational and x > 0 for x in values), "Positive rational energy bounds required"
    )
    inverse = 1 / values[0]
    gaps = [values[0]]
    for fast in values[1:]:
        inverse += 1 / fast
        gaps.append(1 / inverse)
    return gaps


def rectangle_complex(nx: int, ny: int):
    positive_integer(nx, "nx")
    positive_integer(ny, "ny")
    vertices = [(x, y) for y in range(ny + 1) for x in range(nx + 1)]
    edges = [((x, y), (x + 1, y)) for y in range(ny + 1) for x in range(nx)]
    edges += [((x, y), (x, y + 1)) for y in range(ny) for x in range(nx + 1)]
    vertex_index, edge_index = (
        {v: i for i, v in enumerate(vertices)},
        {e: i for i, e in enumerate(edges)},
    )
    faces = [(x, y) for y in range(ny) for x in range(nx)]
    gradient = s.zeros(len(edges), len(vertices))
    for i, (a, b) in enumerate(edges):
        gradient[i, vertex_index[a]], gradient[i, vertex_index[b]] = -1, 1
    curl = s.zeros(len(faces), len(edges))
    for i, (x, y) in enumerate(faces):
        for edge, sign in (
            (((x, y), (x + 1, y)), 1),
            (((x + 1, y), (x + 1, y + 1)), 1),
            (((x, y + 1), (x + 1, y + 1)), -1),
            (((x, y), (x, y + 1)), -1),
        ):
            curl[i, edge_index[edge]] = sign
    return vertices, edges, faces, gradient, curl


def face_dirichlet_matrix(nx: int, ny: int) -> s.Matrix:
    positive_integer(nx, "nx")
    positive_integer(ny, "ny")
    faces = [(x, y) for y in range(ny) for x in range(nx)]
    return s.Matrix(
        [
            [4 if a == b else -int(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1) for b in faces]
            for a in faces
        ]
    )


def incidence_controls() -> list[dict]:
    rows = []
    for nx, ny in ((1, 1), (2, 1), (4, 1), (2, 2), (3, 2), (4, 3)):
        vertices, edges, faces, gradient, curl = rectangle_complex(nx, ny)
        assert curl * gradient == s.zeros(len(faces), len(vertices))
        assert gradient.rank() == len(vertices) - 1
        assert curl.rank() == len(faces) == len(edges) - len(vertices) + 1
        k = curl * curl.T
        assert k == face_dirichlet_matrix(nx, ny)
        # Minimal Euclidean link lift has exactly the inverse face metric.
        lift = curl.T * k.inv()
        assert curl * lift == s.eye(len(faces))
        assert lift.T * lift == k.inv()
        if (nx, ny) == (2, 1):
            assert k.charpoly().as_expr() == s.Symbol("lambda") ** 2 - 8 * s.Symbol("lambda") + 15
        rows.append(
            {
                "faces": [nx, ny],
                "vertices": len(vertices),
                "edges": len(edges),
                "rank_curl": curl.rank(),
            }
        )
    return rows


def partition_matrices(nx: int, ny: int, side: int):
    positive_integer(nx, "nx")
    positive_integer(ny, "ny")
    positive_integer(side, "side")
    if nx % side or ny % side:
        raise ValueError("The exact controls use equal square boxes")
    faces = [(x, y) for y in range(ny) for x in range(nx)]
    fi = {p: i for i, p in enumerate(faces)}
    boxes = [(x, y) for y in range(ny // side) for x in range(nx // side)]
    bi = {p: i for i, p in enumerate(boxes)}
    means = s.zeros(len(faces), len(boxes))
    neumann = s.zeros(len(faces))
    interface_vectors, boundary_vectors = [], []
    for face, i in fi.items():
        x, y = face
        box = (x // side, y // side)
        means[i, bi[box]] = s.Rational(1, side)
        for adjacent in ((x + 1, y), (x, y + 1)):
            if adjacent not in fi:
                continue
            vector = s.zeros(len(faces), 1)
            vector[i], vector[fi[adjacent]] = 1, -1
            if (adjacent[0] // side, adjacent[1] // side) == box:
                neumann += vector * vector.T
            else:
                interface_vectors.append(vector)
        missing = int(x == 0) + int(x == nx - 1) + int(y == 0) + int(y == ny - 1)
        for _ in range(missing):
            vector = s.zeros(len(faces), 1)
            vector[i] = 1
            boundary_vectors.append(vector)
    return means, neumann, interface_vectors, boundary_vectors


def gluing_controls() -> list[dict]:
    rows = []
    for nx, ny, side in ((4, 4, 2), (6, 4, 2), (6, 6, 3), (8, 4, 2)):
        means, neumann, interfaces, exterior = partition_matrices(nx, ny, side)
        k = face_dirichlet_matrix(nx, ny)
        assert means.T * means == s.eye(means.cols)
        assert neumann * means == s.zeros(k.rows, means.cols)
        assert k == neumann + sum((v * v.T for v in interfaces + exterior), s.zeros(k.rows))
        f = s.Rational(4, side * side)
        polynomial = k.charpoly().as_poly()
        assert polynomial.eval(f) != 0
        count = int(polynomial.count_roots(-s.oo, f))
        assert count <= means.cols
        rows.append(
            {
                "faces": [nx, ny],
                "box_side": side,
                "retained_dimension_bound": means.cols,
                "rational_fast_squared_frequency_floor": str(f),
                "exact_eigenvalue_count_below_floor": count,
                "retained_interface_squares": len(interfaces),
                "exterior_boundary_squares": len(exterior),
            }
        )
    return rows


def local_poincare_certificates() -> list[dict]:
    rows = []
    for side in (2, 3, 4):
        means, neumann, interfaces, exterior = partition_matrices(side, side, side)
        assert not interfaces
        q = s.eye(side * side) - means * means.T
        f = s.Rational(4, side * side)
        matrix = neumann - f * q
        lower, d = matrix.LDLdecomposition(hermitian=False)
        assert lower * d * lower.T == matrix
        assert all(value >= 0 for value in d.diagonal())
        assert matrix * means == s.zeros(side * side, 1)
        rows.append(
            {
                "box_side": side,
                "floor": str(f),
                "exact_LDL_diagonal": [str(x) for x in d.diagonal()],
            }
        )
    return rows


def low_mode_source_control() -> dict:
    k = face_dirichlet_matrix(4, 4)
    means, _, _, _ = partition_matrices(4, 4, 2)
    golden = (1 + s.sqrt(5)) / 2
    path_mode = s.Matrix([1, golden, golden, 1])
    mode = s.kronecker_product(path_mode, path_mode)
    eigenvalue = 3 - s.sqrt(5)
    assert (k * mode - eigenvalue * mode).applyfunc(s.simplify) == s.zeros(16, 1)
    ratio = s.simplify((mode.T * means * means.T * mode)[0] / mode.dot(mode))
    assert s.simplify(ratio - (9 + 4 * s.sqrt(5)) / 20) == 0
    exact_local_floor = s.Integer(2)
    lower = 1 - eigenvalue / exact_local_floor
    assert s.simplify(ratio - lower).is_positive is True
    # For a literal linear face coordinate the squared vacuum-source factor is sqrt(lambda)/2.
    face_source_frame = s.simplify(s.sqrt(eigenvalue) * ratio / 2)
    assert s.simplify(face_source_frame - s.sqrt(eigenvalue) * lower / 2).is_positive is True
    # Incorrect replacement by a Neumann outer boundary creates a zero mode.
    _, neumann_whole, _, _ = partition_matrices(4, 4, 4)
    assert neumann_whole * s.ones(16, 1) == s.zeros(16, 1)
    assert k * s.ones(16, 1) != s.zeros(16, 1)
    return {
        "lowest_squared_frequency": str(eigenvalue),
        "box_mean_frame_factor": str(ratio),
        "analytic_frame_lower": str(lower),
        "literal_face_source_frame_factor": str(face_source_frame),
        "wrong_outer_boundary_zero_mode_negative_control": True,
        "source_scope": (
            "Color-adjoint harmonic linear sources; "
            "physical singlets require centered quadratic pairs"
        ),
    }


def finite_cell_controls():
    rows = []
    for nx, ny in [(1, 1), (2, 1), (2, 2), (3, 3)]:
        d0, d1 = rectangle_complex(nx, ny)[3:]
        assert d1 * d0 == s.zeros(nx * ny, (nx + 1) * (ny + 1))
        assert d1.rank() == d1.rows == d1.cols - d0.rank()
        face = d1 * d1.T
        expected = s.zeros(nx * ny)
        for y in range(ny):
            for x in range(nx):
                f = y * nx + x
                expected[f, f] = 4
                for xx, yy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= xx < nx and 0 <= yy < ny:
                        expected[f, yy * nx + xx] = -1
        assert face == expected
        lam = s.symbols("lam")
        spectrum = [
            4 - 2 * s.cos(s.pi * j / (nx + 1)) - 2 * s.cos(s.pi * k / (ny + 1))
            for j in range(1, nx + 1)
            for k in range(1, ny + 1)
        ]
        assert s.simplify(face.charpoly(lam).as_expr() - s.prod(lam - e for e in spectrum)) == 0
        minimum = s.simplify(spectrum[0])
        rows.append(
            {
                "faces": [nx, ny],
                "transverse_dimension": d1.rows,
                "minimum_curl_squared": str(minimum),
                "SU_N_physical_gap_leading_coefficient": str(2 * s.sqrt(minimum)),
            }
        )

    d0, d1 = rectangle_complex(2, 2)[3:]
    rooted_gradient = d0[:, 1:]
    projector = (
        s.eye(d0.rows)
        - rooted_gradient * (rooted_gradient.T * rooted_gradient).inv() * rooted_gradient.T
    )
    assert projector == projector.T and projector * projector == projector
    assert d0.T * projector == s.zeros(d0.cols, d0.rows)
    assert d1 * projector == d1

    kinetic = d1.T * d1
    q = projector * s.Matrix([i * i + 1 for i in range(d1.cols)])
    eta0 = [s.Rational(3, 5) if i % 2 else s.Rational(4, 5) for i in range(d1.cols)]
    eta1 = [s.Rational(4, 5) if i % 2 else s.Rational(3, 5) for i in range(d1.cols)]
    etas = [eta0, eta1]
    assert all(sum(eta[i] ** 2 for eta in etas) == 1 for i in range(d1.cols))
    difference = (
        sum(((s.diag(*eta) * q).T * kinetic * (s.diag(*eta) * q))[0] for eta in etas)
        - (q.T * kinetic * q)[0]
    )
    delta = s.Matrix(d1.cols, d1.cols, lambda i, j: sum((eta[i] - eta[j]) ** 2 for eta in etas))
    identity = -s.Rational(1, 2) * sum(
        kinetic[i, j] * q[i] * q[j] * delta[i, j] for i in range(d1.cols) for j in range(d1.cols)
    )
    assert difference == identity
    bound = (
        max(sum(abs(kinetic[i, j]) * delta[i, j] for j in range(d1.cols)) for i in range(d1.cols))
        / 2
    )
    assert abs(difference) <= bound * (q.T * q)[0]
    gradient = d0 * s.Matrix([i * i for i in range(d0.cols)])
    assert (gradient.T * kinetic * gradient)[0] == 0
    localized_gradient_energy = sum(
        ((s.diag(*eta) * gradient).T * kinetic * (s.diag(*eta) * gradient))[0] for eta in etas
    )
    assert localized_gradient_energy > 0
    return {
        "scope": "Finite incidence, transverse metric and discrete IMS controls only",
        "rectangle_controls": rows,
        "transverse_projector_identities": True,
        "IMS_exact_difference": str(difference),
        "IMS_row_bound": str(bound),
        "localized_pure_gradient_negative_control": str(localized_gradient_energy),
        "first_physical_cluster_rank": "m*(m+1)/2 (analytic invariant-tensor proof)",
    }


def observability_controls() -> dict:
    rows = []
    omega = s.Matrix([[2, 1], [1, 2]])
    b = s.Matrix([[1, 0]])
    covariance = (2 * omega).inv()
    # h=log(2); the two eigenvalues of exp(-h Omega) are 1/2 and 1/8.
    transfer = s.Matrix(
        [[s.Rational(5, 16), -s.Rational(3, 16)], [-s.Rational(3, 16), s.Rational(5, 16)]]
    )
    require(omega * transfer == transfer * omega, "sampled transfer commutator")
    require(
        set(transfer.eigenvals()) == {s.Rational(1, 2), s.Rational(1, 8)},
        "sampled transfer eigenvalues",
    )
    krylov = b.T.row_join(omega * b.T)
    sampled = b.T.row_join(transfer * b.T)
    require(
        krylov.det() == 1 and sampled.det() == -s.Rational(3, 16),
        "continuous or sampled observability determinant",
    )
    cn = [(b * covariance * transfer**n * b.T)[0] for n in range(5)]
    require(
        all(
            cn[n]
            == s.Rational(1, 4) * s.Rational(1, 2) ** n + s.Rational(1, 12) * s.Rational(1, 8) ** n
            for n in range(5)
        ),
        "two-frequency covariance decomposition",
    )
    os_gram = s.Matrix([[cn[0], cn[1]], [cn[1], cn[2]]])
    require(os_gram.det() > 0, "two sampled histories fail to see both frequencies")
    rows.append(
        {
            "check": "one equal-time coordinate reconstructs two frequencies",
            "passed": True,
            "krylov_det": str(krylov.det()),
            "sampled_det": str(sampled.det()),
            "reflected_gram_det": str(os_gram.det()),
            "markov_covariance_defect": str(cn[0] * cn[2] - cn[1] ** 2),
        }
    )

    degenerate = 2 * s.eye(2)
    selected = s.Matrix([[1, -1]])
    require(b.T.row_join(degenerate * b.T).rank() == 1, "degenerate frequency rank obstruction")
    require(
        selected.T.row_join(omega * selected.T).rank() == 1,
        "exact eigenspace selection rank obstruction",
    )
    rows.append(
        {
            "check": "degenerate and exactly unobserved frequency controls",
            "passed": True,
            "ranks": [1, 1],
        }
    )

    # Original seven-link strip cycle Gram, with one shared edge of opposite sign.
    cycles = s.Matrix([[1, 1, 1, 1, 0, 0, 0], [-1, 0, 0, 0, 1, 1, 1]])
    c = cycles * cycles.T
    require(c == s.Matrix([[4, -1], [-1, 4]]), "seven-link cycle Gram")
    w1, w2, eps = s.symbols("w1 w2 eps", real=True)
    weights = s.diag(w1, w2)
    coarse = s.Matrix([1, 1])
    raw_det = s.factor(coarse.row_join(weights * c * coarse).det())
    require(s.expand(raw_det - 3 * (w2 - w1)) == 0, "weighted strip observability")
    a = s.Matrix([[3, s.sqrt(15) * eps], [s.sqrt(15) * eps, 5]])
    observed = s.Matrix([s.sqrt(3), 0])
    white_det = s.simplify(observed.row_join(a * observed).det())
    require(white_det == 3 * s.sqrt(15) * eps, "white-coordinate determinant")
    lam = s.symbols("lam")
    require(
        s.factor(a.charpoly(lam).as_expr()) == lam**2 - 8 * lam + 15 - 15 * eps**2,
        "weighted frequency polynomial",
    )
    high_lambda = 4 + s.sqrt(1 + 15 * eps**2)
    high_residue = 3 / (4 * s.sqrt(high_lambda)) * (1 - 1 / s.sqrt(1 + 15 * eps**2))
    residue_coefficient = s.simplify(s.limit(high_residue / eps**2, eps, 0))
    require(residue_coefficient == 9 * s.sqrt(5) / 8, "small observed high-frequency residue")
    require(
        s.simplify(2 * s.sqrt(5) - s.sqrt(3) - s.sqrt(5)).is_positive,
        "mixed physical singlet should precede the pure fiber singlet",
    )
    rows.append(
        {
            "check": "actual weighted seven-link strip",
            "passed": True,
            "raw_det": str(raw_det),
            "white_det": str(white_det),
            "frequency_polynomial": str(a.charpoly(lam).as_expr()),
            "high_residue_epsilon2_coefficient": str(residue_coefficient),
            "symmetric_complement_energy": "sqrt(3)+sqrt(5)",
            "intrinsic_fiber_class_energy": "2*sqrt(5)",
        }
    )

    # Frequencies 1,2 and h=log(2): the three quadratic rates are 2,3,4.
    nodes = [s.Rational(1, 4), s.Rational(1, 8), s.Rational(1, 16)]
    factors = [s.Integer(1), s.Integer(2), s.Integer(1)]
    quadratic = s.Matrix([[factors[j] * nodes[j] ** k for j in range(3)] for k in range(3)])
    require(quadratic.det() != 0, "quadratic singlet reconstruction")
    require(quadratic.inv() * quadratic == s.eye(3), "exact quadratic inverse")
    rows.append(
        {
            "check": "three regular times separate all quadratic singlets",
            "passed": True,
            "determinant": str(quadratic.det()),
            "inverse": [[str(v) for v in row] for row in quadratic.inv().tolist()],
        }
    )

    coords = s.symbols("x0:3 y0:3 z0:3")
    x, y, z = [s.Matrix(coords[j : j + 3]) for j in (0, 3, 6)]
    chirality = s.expand(x.row_join(y).row_join(z).det())
    vectors = [x, y, z]
    for axis in range(3):
        e = s.eye(3)[:, axis]
        rotation_derivative = sum(
            sum((e.cross(v))[k] * s.diff(chirality, v[k]) for k in range(3)) for v in vectors
        )
        require(s.expand(rotation_derivative) == 0, "chirality Gauss invariance")
    reflect = {v[0]: -v[0] for v in vectors}
    require(
        s.expand(chirality.subs(reflect, simultaneous=True) + chirality) == 0,
        "chirality reflection parity",
    )
    qform = s.expand((2 * x + 3 * y + 5 * z).dot(2 * x + 3 * y + 5 * z))
    require(
        s.expand(qform.subs(reflect, simultaneous=True) - qform) == 0,
        "radial observable reflection parity",
    )
    omega3 = s.diag(1, 2, 3)
    b3 = s.Matrix([2, 3, 5])
    observable3 = b3.row_join(omega3 * b3).row_join(omega3**2 * b3)
    require(
        observable3.det() != 0 and chirality != 0, "three-mode physical-algebra negative control"
    )
    rows.append(
        {
            "check": "one-particle observability does not imply arbitrary physical cyclicity",
            "passed": True,
            "three_mode_krylov_det": str(observable3.det()),
            "chirality": str(chirality),
            "simultaneous_rotation_derivatives": ["0", "0", "0"],
            "chirality_reflection_parity": -1,
            "radial_reflection_parity": 1,
        }
    )

    payload = {
        "passed": all(row["passed"] for row in rows),
        "exact_check_count": len(rows),
        "checks": rows,
        "scope": (
            "Finite exact controls only; the accompanying note proves "
            "the general OS/Fock statements."
        ),
    }
    return payload


def closed_form_controls():
    # Large cross term: static K0 without the graph norm gives a false gap.
    eigenvalue = 3 - 2 * s.sqrt(2)
    assert eigenvalue >= s.Rational(1, 6)
    assert eigenvalue <= s.Rational(1, 5)
    assert eigenvalue < s.Rational(1, 2)

    fine = s.diag(2, 5)
    lift = s.Matrix([[1, s.Rational(1, 2)], [-s.Rational(2, 3), s.Rational(3, 4)]])
    static = s.Matrix([[1, -1], [-1, 1]])
    mass = s.eye(2) + lift.T * lift
    assert mass * static != static * mass
    hamiltonian = (static + lift.T * fine * lift).row_join(lift.T * fine)
    hamiltonian = hamiltonian.col_join((fine * lift).row_join(fine))
    triangular = s.eye(4)
    triangular[2:, :2] = -lift
    assert triangular.T * hamiltonian * triangular == s.diag(static, fine)
    null = s.Matrix([1, 1]).col_join(-lift * s.Matrix([1, 1]))
    assert hamiltonian * null == s.zeros(4, 1)
    assert hamiltonian.rank() == 3

    shift_rows = []
    for z in [s.Rational(1, 3), s.Rational(1), s.Rational(3, 2)]:
        resolvent = (fine - z * s.eye(2)).inv()
        lifted = lift + z * resolvent * lift
        remainder = lift.T * resolvent * lift
        schur = static - z * mass - z * z * remainder
        transform = s.eye(4)
        transform[2:, :2] = -lifted
        assert transform.T * (hamiltonian - z * s.eye(4)) * transform == s.diag(
            schur, fine - z * s.eye(2)
        )
        assert positive_semidefinite((mass - s.eye(2)) / (2 - z) - remainder)
        assert positive_semidefinite(schur - (static - 2 * z / (2 - z) * mass))
        variable = s.symbols("t")
        full_negative = hamiltonian.charpoly(variable).as_poly().count_roots(-s.oo, z)
        schur_negative = schur.charpoly(variable).as_poly().count_roots(-s.oo, 0)
        assert full_negative == schur_negative
        shift_rows.append({"z": str(z), "negative_index": int(full_negative)})

    mu = s.trace(mass.inv() * static)
    lower = 2 * mu / (2 + mu)
    variable = s.symbols("t")
    nonzero_polynomial = s.Poly(
        s.cancel(hamiltonian.charpoly(variable).as_expr() / variable), variable
    )
    assert nonzero_polynomial.count_roots(0, lower) == 0
    assert nonzero_polynomial.count_roots(0, mu) >= 1

    # Rational actual low-window projector, independent of any eigenvector fit.
    rotation13 = s.Matrix(
        [
            [s.Rational(4, 5), 0, s.Rational(3, 5)],
            [0, 1, 0],
            [-s.Rational(3, 5), 0, s.Rational(4, 5)],
        ]
    )
    rotation23 = s.Matrix(
        [
            [1, 0, 0],
            [0, s.Rational(12, 13), s.Rational(5, 13)],
            [0, -s.Rational(5, 13), s.Rational(12, 13)],
        ]
    )
    rotation = rotation13 * rotation23
    assert rotation.T * rotation == s.eye(3)
    energy = s.Rational(1, 4)
    full = rotation * s.diag(0, energy, 5) * rotation.T
    window = rotation * s.diag(1, 1, 0) * rotation.T
    floor = full[2, 2]
    u = full[2:, :2] / floor
    graph = s.eye(2).col_join(-u)
    metric = s.eye(2) + u.T * u
    graph_projection = graph * metric.inv() * graph.T
    frame_lower = 1 - (energy / floor) ** 2
    assert energy < floor
    assert graph_projection * graph_projection == graph_projection
    assert positive_semidefinite(window * graph_projection * window - frame_lower * window)
    assert (window * graph).rank() == window.rank() == 2
    assert (full * window)[2:, :] == floor * (window[2:, :] + u * window[:2, :])

    inverse_gap = s.Rational(7)
    for j in range(8):
        fast = 3 * 2**j
        next_gap = fast / (1 + fast * inverse_gap)
        inverse_gap = s.cancel(1 / next_gap)
    expected_inverse = 7 + s.Rational(2, 3) * (1 - s.Rational(1, 2) ** 8)
    assert inverse_gap == expected_inverse

    assert (
        inverse_fast_budget(s.Rational(1, 7), [3 * 2**j for j in range(8)])[-1] == 1 / inverse_gap
    )
    assert graph_source_control(full, 2, window, energy, floor)["rank"] == 2

    return {
        "scope": "Finite rational closed-form, vacuum, gap and graph-frame controls only",
        "large_cross_term": {
            "actual_low_energy": str(eigenvalue),
            "mu": "1/5",
            "lower_bound": "1/6",
            "omitted_mass_false_bound": "1/2",
        },
        "noncommuting_shift_controls": shift_rows,
        "vacuum_graph_dimension": 1,
        "noncommuting_coarse_positive_energy": str(mu),
        "noncommuting_full_gap_bracket": [str(lower), str(mu)],
        "whole_window": {
            "rank": 2,
            "energy": str(energy),
            "fast_floor": str(floor),
            "frame_lower": str(frame_lower),
            "onto_rank": 2,
        },
        "eight_step_inverse_gap_budget": str(inverse_gap),
    }


def positive_semidefinite(matrix):
    require_psd(matrix)
    return True


def graph_source_control(hamiltonian, retained_dimension, window, energy, floor):
    """Validate an exact finite reducing low window and its entire graph frame."""
    hamiltonian = exact_symmetric(hamiltonian, "Hamiltonian")
    window = exact_symmetric(window, "Window")
    positive_integer(retained_dimension, "Retained dimension")
    require(retained_dimension < hamiltonian.rows, "A nonempty fast space is required")
    require(window.shape == hamiltonian.shape, "Window dimensions do not match")
    require(window * window == window, "Window must be an orthogonal projector")
    require(hamiltonian * window == window * hamiltonian, "Window must reduce the Hamiltonian")
    energy, floor = map(s.sympify, (energy, floor))
    require(
        energy.is_Rational and floor.is_Rational and 0 <= energy < floor,
        "Need exact rational 0 <= energy < fast floor",
    )
    require_psd(hamiltonian)
    require_psd(energy * window - hamiltonian * window)
    n = retained_dimension
    fast = hamiltonian[n:, n:]
    require_psd(fast - floor * s.eye(fast.rows))
    lift = fast.inv() * hamiltonian[n:, :n]
    graph = s.eye(n).col_join(-lift)
    metric = graph.T * graph
    projector = graph * metric.inv() * graph.T
    lower = 1 - (energy / floor) ** 2
    require(projector**2 == projector, "Graph projector fails")
    require_psd(window * projector * window - lower * window)
    require_psd(window - window * projector * window)
    require((window * graph).rank() == window.rank(), "Projected graph fails finite onto rank")
    require(
        (hamiltonian * window)[n:, :] == fast * (window[n:, :] + lift * window[:n, :]),
        "Graph residual row identity fails",
    )
    return {"rank": window.rank(), "frame_lower": str(lower), "graph_metric": str(metric)}


def gaussian_certificates():
    """A fresh copy of the original exact rational isolating intervals."""
    return copy.deepcopy(
        [
            {
                "j": 1,
                "lambda_interval": ["57192/58879", "72007/74131"],
                "mu_interval": ["15871/14680", "74651/69049"],
                "strict_lower_control": "223953/281798",
                "strict_upper_control": "15871/14680",
            },
            {
                "j": 2,
                "lambda_interval": ["407459/119113", "34608/10117"],
                "mu_interval": ["284305/74798", "71272/18751"],
                "strict_lower_control": "213816/127525",
                "strict_upper_control": "284305/74798",
            },
        ]
    )


def gaussian_memory_controls():
    fast = s.Matrix([[7, 2], [2, 5]])
    coupling = s.Matrix([[2, -1], [1, 3]])
    static = s.Matrix([[2, 1], [1, 4]])
    floor = s.Integer(3)
    _, metric, retained, _ = gaussian_schur_blocks(fast, coupling, static, floor)
    require(static * metric != metric * static, "Control must retain noncommuting coarse matrices")
    z = s.Symbol("z")
    exact = retained + z * s.eye(2) - coupling * (fast + z * s.eye(2)).inv() * coupling.T
    remainder = coupling * fast**-2 * (fast + z * s.eye(2)).inv() * coupling.T
    require(
        (exact - static - z * metric + z**2 * remainder).applyfunc(s.factor) == s.zeros(2),
        "Exact Gaussian memory identity fails",
    )
    for x in (s.Rational(1, 3), s.Integer(2), s.Integer(5)):
        rx = remainder.subs(z, x)
        require_psd(rx)
        require_psd((metric - s.eye(2)) / (floor + x) - rx)
        kernel = exact.subs(z, x)
        require_psd(static + x * metric - kernel)
        require_psd(kernel - static - x * s.eye(2) - x * floor / (floor + x) * (metric - s.eye(2)))
    for x in (s.Rational(1, 4), s.Integer(1), s.Rational(5, 2)):
        shifted = retained - x * s.eye(2) - coupling * (fast - x * s.eye(2)).inv() * coupling.T
        require_psd(shifted - static + x * floor / (floor - x) * metric)
        require_psd(static - x * metric - shifted)
    certificates = gaussian_certificates()
    replay_gaussian_enclosures(fast, coupling, static, floor, certificates)
    return {
        "scope": (
            "One noncommuting finite Gaussian control, exact identities "
            "and rational Sturm enclosures"
        ),
        "F": str(fast),
        "D": str(coupling),
        "K0": str(static),
        "M": str(metric),
        "f": str(floor),
        "certificates": certificates,
        "positive_frequency_samples": 3,
        "shifted_frequency_samples": 3,
        "passed": True,
    }


@lru_cache(maxsize=1)
def _cached_scale_controls():
    if not __debug__:
        raise RuntimeError("Exact controls require assertions enabled")
    return {
        "original_link_incidence": incidence_controls(),
        "retained_boundary_gluing": gluing_controls(),
        "local_rational_Poincare_LDL": local_poincare_certificates(),
        "spectral_frame_and_source_coordinates": low_mode_source_control(),
        "finite_cell": finite_cell_controls(),
        "gaussian_memory": gaussian_memory_controls(),
        "os_observability": observability_controls(),
        "closed_form_schur": closed_form_controls(),
        "numerical_eigensolver_used": False,
    }


def exact_scale_controls():
    """Recompute once, then return independent payloads for suite and sealing."""
    return copy.deepcopy(_cached_scale_controls())
