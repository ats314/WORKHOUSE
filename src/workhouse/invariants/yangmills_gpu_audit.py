"""Exact, narrowly scoped audits of the archived numerical operators."""

import ast
from pathlib import Path
from types import SimpleNamespace

from sympy import I, Matrix, Rational, eye, kronecker_product, simplify, sqrt, symbols, zeros

from ._core import _suite

audit = _suite("Yang-Mills GPU archive: exact operator identification audit")
CITE = "YM_GPU_AUDIT; G19; G23"
RUN = Path(__file__).resolve().parents[3] / "runs/gpu_yangmills_millennium_resolutions_2026-09-09"


class _ExactFloats(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, float):
            return ast.copy_location(
                ast.Call(
                    func=ast.Name(id="Rational", ctx=ast.Load()),
                    args=[ast.Constant(str(node.value))],
                    keywords=[],
                ),
                node,
            )
        return node


@audit.check(
    "Scalar fast model has an exact all-source bound distinct from its delta-source sample",
    CITE + " GA1 GA4",
)
def _scalar_resolvent():
    lam, g = symbols("lam g", nonnegative=True)
    d = 2 - lam / 4
    a = Rational(9, 4) + lam
    constant_ratio = 2 / (Rational(9, 4) * (Rational(9, 4) + Rational(1, 5)))
    return (
        simplify(a + g * d - ((1 - g / 4) * lam + Rational(9, 4) + 2 * g)) == 0
        and constant_ratio == Rational(160, 441) > Rational(53, 1000)
        and 2 / Rational(9, 4) ** 2 == Rational(32, 81),
        "Exact Fourier multiplier and constant-source witness for the inserted-mass scalar model. "
        "The spectral range and analytic monotonicity give norm <=32g/81. "
        "This does not identify the actual Wilson selected inverse or its source norm.",
    )


@audit.check(
    "Archived domino builder equals two independent rotors with increased kinetic coefficient",
    CITE + " GA5",
)
def _source_domino():
    tree = ast.parse((RUN / "phase2_wr26_dirichlet_gap.py").read_text(encoding="utf-8"))
    names = {"build_su2_single_rotor_hamiltonian", "build_su2_two_plaquette_domino"}
    selected = [
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names
    ]
    module = ast.fix_missing_locations(
        _ExactFloats().visit(ast.Module(body=selected, type_ignores=[]))
    )
    fake = SimpleNamespace(zeros=lambda shape, **kwargs: zeros(*shape), float64=None, device=object)
    scope = {"torch": fake, "Rational": Rational}
    exec(compile(module, str(RUN / "phase2_wr26_dirichlet_gap.py"), "exec"), scope)
    eps, v = symbols("epsilon v", positive=True)
    one = scope["build_su2_single_rotor_hamiltonian"](1, Rational(5, 4) * eps, v, None)
    two = scope["build_su2_two_plaquette_domino"](1, eps, v, None)
    return (
        two == kronecker_product(one, eye(3)) + kronecker_product(eye(3), one),
        "Archived builder executed with float literals rationalized, at j_max=1 and symbolic "
        "epsilon,v. Its displayed coefficient formula proves the factorization for every cutoff; "
        "this finite source equality is the machine control, not a coupled Wilson spectrum.",
    )


@audit.check(
    "Shared SU2 derivative produces a nonzero physical channel outside product characters",
    CITE + " GA6",
)
def _shared_cross():
    pauli = [Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]
    a, b = symbols("a0:4", real=True), symbols("b0:4", real=True)
    u = a[0] * eye(2) + I * sum((a[j + 1] * pauli[j] for j in range(3)), zeros(2))
    v = b[0] * eye(2) + I * sum((b[j + 1] * pauli[j] for j in range(3)), zeros(2))
    cross = sum((I * p / 2 * u).trace() * (v * I * p / 2).trace() for p in pauli)
    fierz = -(u * v).trace() / 2 + u.trace() * v.trace() / 4
    dot = sum(a[j] * b[j] for j in range(1, 4))
    return (
        simplify(cross - fierz) == 0
        and simplify(cross - dot) == 0
        and 3 * Rational(1, 4) ** 2 == Rational(3, 16) > 0,
        "Exact Pauli/Fierz derivative identity. Independent Haar quaternion coordinates have "
        "second moments delta_ij/4, giving squared norm 3/16; separate axis averages vanish. "
        "The omitted channel is invariant under joint, but not separate, conjugations.",
    )


@audit.check(
    "Archived 2x2 shared kinetic expression is exactly a sum of separate Casimirs", CITE + " GA9"
)
def _four_rotors():
    tree = ast.parse(
        (RUN / "phase4_multiscale_schur_and_2x2_lattice.py").read_text(encoding="utf-8")
    )
    assignments = {}
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id in {"kin_self", "kin_shared"}
        ):
            assignments[node.targets[0].id] = node.value
    ns = symbols("n0:4", integer=True, nonnegative=True)
    eps = symbols("epsilon", positive=True)
    scope = dict(zip(["n0", "n1", "n2", "n3"], ns, strict=True), epsilon=eps, Rational=Rational)
    values = []
    for key in ("kin_self", "kin_shared"):
        expression = ast.fix_missing_locations(
            _ExactFloats().visit(ast.Expression(assignments[key]))
        )
        values.append(eval(compile(expression, "phase4_kinetic", "eval"), scope))
    return (
        simplify(sum(values) - Rational(3, 2) * eps * sum(n * (n + 2) for n in ns)) == 0
        and (2 * 3 + 1) ** 4 == 2401,
        "Source-derived symbolic equality for arbitrary four indices. Together with the four "
        "separate nearest-character hops in the source this is four independent h(3epsilon/2,v). "
        "The 2401-dimensional spectrum is not a shared-link cluster calculation.",
    )


@audit.check(
    "Scalar telescope recurrence is valid but a squared-time clock is not additive",
    CITE + " GA7 GA8",
)
def _telescope_clock():
    a, b, alpha, f, s, t = symbols("A B alpha f s t", positive=True)
    next_gap = alpha * a / (b + alpha * a / f)
    return (
        simplify(1 / next_gap - ((b / a) / alpha + 1 / f)) == 0
        and simplify((s + t) ** 2 - s**2 - t**2) == 2 * s * t,
        "Exact scalar recurrence behind SP21, conditional on its inputs. GA8 integral/product "
        "bounds separately prove the model's infinite limit. The nonzero clock cross term "
        "prevents t->t^2 from intertwining time-translation semigroups.",
    )


@audit.check(
    "Admissible cube basis has magnetic weights missing the shared-edge recoupling ratio",
    CITE + " GA10",
)
def _cube_recoupling():
    tree = ast.parse((RUN / "phase5_3d_cube_glueball.py").read_text(encoding="utf-8"))
    selected = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name in {"build_3d_cube_system", "enumerate_gauge_invariant_states"}
    ]
    scope = {}
    exec(compile(ast.Module(body=selected, type_ignores=[]), "phase5_geometry", "exec"), scope)
    _, plaquettes, vertices = scope["build_3d_cube_system"]()
    states = scope["enumerate_gauge_invariant_states"](vertices)
    first, adjacent = plaquettes[0], plaquettes[2]
    (shared,) = set(first) & set(adjacent)
    initial = tuple(int(e in first) for e in range(12))
    targets = []
    for shared_spin in (0, 2):
        target = [int(e in set(first) | set(adjacent)) for e in range(12)]
        target[shared] = shared_spin
        targets.append(tuple(target))
    weights = [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == "weight"
    ]
    constant = ast.fix_missing_locations(_ExactFloats().visit(ast.Expression(weights[0])))
    coded_weight = eval(compile(constant, "phase5_weight", "eval"), {"Rational": Rational}) / 4
    return (
        len(states) == len(set(states)) == 1013
        and initial in states
        and all(target in states for target in targets)
        and coded_weight == Rational(1, 8)
        and Rational(1, 4) + Rational(3, 4) == 1
        and sqrt(Rational(3, 4)) / sqrt(Rational(1, 4)) == sqrt(3) != 1,
        "Source-executed 1013-state triangle enumeration and two allowed shared-edge channels. "
        "GA10 Haar orthogonality gives their squared character-product coefficients 1/4,3/4, "
        "hence magnetic amplitude ratio sqrt(3). The source assigns equal v/8 weights, "
        "so a global convention change cannot make this the SU2 Wilson magnetic operator.",
    )
