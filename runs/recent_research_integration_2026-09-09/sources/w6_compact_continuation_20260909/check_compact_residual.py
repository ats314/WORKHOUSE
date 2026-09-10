"""Exact controls of compact-reference graph/resolvent identities.

This is a finite-dimensional independent algebra control of the analytic
proof, including a reference source that does not reduce the reference
operator. It does not claim to certify the analytic quantifiers by tests.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def mv(a, x):
    return [sum(u * v for u, v in zip(row, x)) for row in a]


def dot(x, y):
    return sum(u * v for u, v in zip(x, y))


def inv(a):
    n = len(a)
    b = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        i = next(i for i in range(j, n) if b[i][j])
        b[i], b[j] = b[j], b[i]
        pivot = b[j][j]
        b[j] = [x / pivot for x in b[j]]
        for i in range(n):
            if i != j:
                scale = b[i][j]
                b[i] = [u - scale * v for u, v in zip(b[i], b[j])]
    return [row[n:] for row in b]


def block(a):
    return [row[1:] for row in a[1:]]


def quad(a, x):
    return dot(x, mv(a, x))


def schur(a):
    coupling = [row[0] for row in a[1:]]
    return a[0][0] - dot(coupling, mv(inv(block(a)), coupling))


checks = []


def check(name, truth):
    assert truth, name
    checks.append(name)


# A decoupled zero vacuum is implicit. The retained complement is e_0,
# and the actual baseline retained-fast coupling is nonzero.
hs = mat([[5, 1, 2], [1, 6, 1], [2, 1, 7]])
d = mat([[2, -1, 1], [-1, 1, -1], [1, -1, -2]])
fs = block(hs)
rs = inv(fs)
coupling = [F(1), F(2)]
j = [F(1)] + [-x for x in mv(rs, coupling)]
ts = mv(d, j)[1:]
us = mv(rs, ts)
bs = hs[0][0]
M1 = F(2)

check("baseline_source_nonreducing", coupling != [0, 0])
check("reference_gap_gershgorin_at_least_two", all(
    hs[i][i] - sum(abs(hs[i][j]) for j in range(3) if i != j) >= 2
    for i in range(3)))
check("perturbation_operator_bound_four", max(sum(abs(x) for x in row) for row in d) <= 4)
check("full_graph_fast_cross_cancels", mv(hs, j)[1:] == [0, 0])
check("graph_energy_exact_schur", quad(hs, j) == schur(hs))
check("graph_energy_at_most_actual_source_energy", quad(hs, j) <= bs)
check("first_force_is_nonzero", any(ts))
check("first_force_dual_bound", dot(ts, us) <= M1**2 * bs)

records = []
for delta in [F(-1, 4), F(-1, 8), F(-1, 16), F(1, 16), F(1, 8), F(1, 4)]:
    ht = [[hs[i][j_] + delta * d[i][j_] for j_ in range(3)] for i in range(3)]
    ft = block(ht)
    rt = inv(ft)
    ut = mv(rt, ts)
    residual = [delta * x for x in ts]
    residual_energy = dot(residual, mv(rt, residual))
    selected = dot(ts, [u - v for u, v in zip(ut, us)])
    signed = delta * dot(us, mv(block(d), ut))
    rho = [delta * x for x in mv(block(d), us)]
    rho_energy = dot(rho, mv(rt, rho))
    eps = M1 * abs(delta)
    direct = delta * quad(d, j)
    schur_difference = schur(ht) - schur(hs)
    remainder = schur_difference - direct + delta**2 * dot(ts, us)
    label = str(delta)
    check(label + ":signed_resolvent_identity", selected == -signed)
    check(label + ":complete_square_completion", schur_difference == direct - residual_energy)
    check(label + ":full_residual_dual_bound", residual_energy <= eps**2 * bs / (1 - eps))
    check(label + ":interacting_inverse_energy", quad(fs, ut) <= M1**2 * bs / (1 - eps)**2)
    check(label + ":selected_W6_bound", abs(signed) <= M1**3 * abs(delta) * bs / (1 - eps))
    check(label + ":selected_residual_dual_bound", rho_energy <= M1**2 * eps**2 * bs / (1 - eps))
    check(label + ":cubic_schur_remainder", abs(remainder) <= abs(delta)**3 * M1**3 * bs / (1 - eps))
    records.append({"delta": label, "complete_residual_dual_energy": str(residual_energy),
                    "selected_inverse_difference": str(selected),
                    "complete_schur_remainder": str(remainder)})

result = {"status": "passed", "checks": len(checks), "check_names": checks,
          "reference_graph": [str(x) for x in j], "force": [str(x) for x in ts],
          "records": records,
          "scope": "Exact rational finite algebra control; analytic theorem is in compact_residual.md."}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": len(checks), "output": str(out)}))
