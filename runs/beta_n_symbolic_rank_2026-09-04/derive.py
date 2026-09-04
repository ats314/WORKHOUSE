"""Every cumulant of the beta_N assembly over Q(N): the closed forms derived, the degree bound proved.

    python derive.py > console.log

The third engine (workhouse.loopcalc) run over the rational function field Q(N)
(workhouse.symbolic_rank): the second-order hops, the two-hop weight u, the
single-contact and fan dressings of the coplanar and the perpendicular pair,
the corner dressing, and both cube completions, each returned as ONE rational
function of N in both C-parity sectors. Then:

* every closed form is specialised at every rank of the two pinned per-rank
  records (runs/rank_sweep_cumulants_2026-09-04, N = 3..70, and
  runs/beta_n_from_assembly_2026-09-04, N = 4..70) and compared exactly;
* the audit behind the specialisation argument of symbolic_rank's docstring is
  recorded: every eigencomponent verified, the largest Weingarten family, the
  largest link flux met, and every resolvent denominator E0 - E with its
  rational roots -- the integer roots >= 4 are where the argument does NOT
  reach and the agreement is a checked fact instead;
* the assembly beta = -16u - 8(rho + pi), with rho and pi as in ADR 0027, is
  compared with the corpus's P17(N^2)/(N R20(N^2)) as rational functions, and
  the coplanar dressings with the perpendicular ones.

Writes closed_forms.json and certificate.json. Nothing here reads a kernel.
"""

from __future__ import annotations

import json
import sys
import time
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sympy import Symbol, cancel, factor  # noqa: E402

from workhouse import loopcalc as L  # noqa: E402
from workhouse import symbolic_rank as SR  # noqa: E402
from workhouse.channel_ledger import P17, R20, _z  # noqa: E402

SWEEP = ROOT / "runs" / "rank_sweep_cumulants_2026-09-04" / "certificate.json"
ASSEMBLY = ROOT / "runs" / "beta_n_from_assembly_2026-09-04" / "certificate.json"
sweep = json.loads(SWEEP.read_text(encoding="utf-8"))["ranks"]
assembly = json.loads(ASSEMBLY.read_text(encoding="utf-8"))["ranks"]
# the record's pi and rho carry the pair cluster, which cancels in their sum (ADR 0027)
for row in assembly.values():
    row["rho_plus_pi"] = str(F(row["rho"]) + F(row["pi"]))

P = ((0, 1), (0, 0, 0))
Q_COP = ((0, 1), (1, 0, 0))
Q_PERP = ((0, 2), (0, 0, 0))
Q_NORMAL = ((0, 1), (0, 0, 1))
X_SINGLE_COP = ((0, 1), (2, 0, 0))
X_FAN_COP = ((1, 2), (1, 0, 0))
X_SINGLE_PERP = ((0, 1), (1, 0, 0))
X_FAN_PERP = ((0, 1), (0, -1, 0))
X_CORNER = ((1, 2), (1, 0, 0))
OTHERS_ADJACENT = [((0, 1), (0, 0, 1)), ((0, 2), (0, 1, 0)), ((1, 2), (0, 0, 0)), ((1, 2), (1, 0, 0))]
OTHERS_OPPOSITE = [((0, 2), (0, 0, 0)), ((0, 2), (0, 1, 0)), ((1, 2), (0, 0, 0)), ((1, 2), (1, 0, 0))]

#: quantity -> (pinned record, key) for the specialisation check
PINNED = {
    "hop_odd": ("sweep", "hop_odd"),
    "hop_even": ("sweep", "hop_even"),
    "hop_perp_odd": ("sweep", "hop_perp_odd"),
    "u_odd": ("sweep", "u_odd"),
    "u_even": ("sweep", "u_even"),
    "single_perp_odd": ("sweep", "single_odd"),
    "single_perp_even": ("sweep", "single_even"),
    "fan_perp_odd": ("sweep", "fan_odd"),
    "fan_perp_even": ("sweep", "fan_even"),
    "corner_odd": ("sweep", "corner_odd"),
    "corner_even": ("sweep", "corner_even"),
    "single_cop_odd": ("assembly", "single_coplanar"),
    "fan_cop_odd": ("assembly", "fan_coplanar"),
    "rho_plus_pi": ("assembly", "rho_plus_pi"),
    "C_shp": ("assembly", "C_shp"),
    "beta_assembled": ("assembly", "beta_assembled"),
}

N = Symbol("N")
T0 = time.time()
forms: dict[str, SR.RF] = {}


def record(name: str, rf: SR.RF, cluster: str = "") -> None:
    forms[name] = rf
    print(f"[{time.time() - T0:7.1f}s] {name}: degrees {rf.degrees()}  {factor(rf.to_sympy())}", flush=True)


def specialise(name: str, rf: SR.RF) -> dict:
    which, key = PINNED[name]
    rows = sweep if which == "sweep" else assembly
    checked, bad = [], []
    for n_str, row in rows.items():
        if row.get(key) is None:
            continue
        n = int(n_str)
        checked.append(n)
        if rf.at(n) != F(row[key]):
            bad.append(n)
    return {
        "record": SWEEP.parent.name if which == "sweep" else ASSEMBLY.parent.name,
        "key": key,
        "ranks_checked": f"{min(checked)}..{max(checked)} ({len(checked)} ranks)",
        "ranks_disagreeing": bad,
    }


with SR.Symbolic() as S:
    pair = L.Cluster([P, Q_COP])
    perp = L.Cluster([P, Q_PERP])
    h2, _v2 = pair.second_order()
    h2p, _v2p = perp.second_order()
    record("hop_odd", L.codd(h2, 0, 1), "coplanar pair")
    record("hop_even", L.ceven(h2, 0, 1), "coplanar pair")
    record("hop_perp_odd", L.codd(h2p, 0, 1), "perpendicular pair")
    for name, faces in (
        ("u", [P, Q_COP, ((0, 1), (2, 0, 0))]),
        ("single_perp", [P, X_SINGLE_PERP, Q_PERP]),
        ("fan_perp", [P, X_FAN_PERP, Q_PERP]),
        ("corner", [P, X_CORNER, Q_PERP]),
        ("single_cop", [P, X_SINGLE_COP, Q_COP]),
        ("fan_cop", [P, X_FAN_COP, Q_COP]),
    ):
        t = time.time()
        w = L.cumulant(faces, 1)
        print(f"   cumulant {name}: {time.time() - t:.1f}s", flush=True)
        record(name + "_odd", L.block_odd(w))
        record(name + "_even", L.block_even(w))
    t = time.time()
    adj = L.cube_completion(P, Q_PERP, OTHERS_ADJACENT)
    opp = L.cube_completion(P, Q_NORMAL, OTHERS_OPPOSITE)
    print(f"   cube completions: {time.time() - t:.1f}s", flush=True)
    record("cube_adjacent_odd", L.block_odd(adj))
    record("cube_adjacent_even", L.block_even(adj))
    record("cube_opposite_odd", L.block_odd(opp))
    record("cube_opposite_even", L.block_even(opp))
    denominators = S.resolvent_denominators()
    audit = {k: v for k, v in S.stats.items() if k in ("components_verified", "max_weingarten_n", "max_charge")}
    audit["link_irreps_met"] = sorted(SR.ENERGY_NAME.get(e, str(e.to_sympy())) for e in S.stats["link_energies"])
    audit["distinct_intermediate_energies"] = len(S.stats["energies"])
    audit.update(denominators)
L.set_rank(3)

# the assembly of ADR 0027, pair cluster cancelling
u, d_cop, s_cop = forms["u_odd"], forms["single_cop_odd"], forms["fan_cop_odd"]
d_perp, s_perp, corner = forms["single_perp_odd"], forms["fan_perp_odd"], forms["corner_odd"]
k_adj, k_opp = forms["cube_adjacent_odd"], forms["cube_opposite_odd"]
alpha = -4 * k_opp
pi = 18 * d_cop + 2 * s_cop
rho = 14 * d_perp + 2 * s_perp + 2 * corner + k_adj
c_shp = -alpha / 8 - u - (rho + pi) / 2
beta = 8 * (alpha / 4) + 16 * c_shp
record("pi", pi)
record("rho", rho)
record("rho_plus_pi", rho + pi)
record("C_shp", c_shp)
record("beta_assembled", beta)
three = -16 * u + 32 * d_perp - 16 * corner - 8 * k_adj
corpus = P17.as_expr().subs(_z, N**2) / (N * R20.as_expr().subs(_z, N**2))
identities = {
    "single_cop_plus_single_perp": str((d_cop + d_perp).to_sympy()),
    "fan_cop_plus_fan_perp": str((s_cop + s_perp).to_sympy()),
    "beta_minus_three_cumulant_form": str((beta - three).to_sympy()),
    "beta_minus_corpus": str(cancel(beta.to_sympy() - corpus)),
    "alpha_N": str(factor(alpha.to_sympy())),
    "beta_at_3": str(beta.at(3)),
    "beta_at_4": str(beta.at(4)),
}
print("identities:", json.dumps(identities, indent=1), flush=True)

closed = {"schema": "beta_n_symbolic_rank/v1", "field": "Q(N)", "basis": "(0,2) x-then-z, the kernel's", "forms": {}}
for name, rf in forms.items():
    closed["forms"][name] = {
        "factored": str(factor(rf.to_sympy())),
        "degrees_in_N": list(rf.degrees()),
        **rf.coefficient_lists(),
    }
closed["identities"] = identities
(HERE / "closed_forms.json").write_text(json.dumps(closed, indent=1) + "\n", encoding="utf-8", newline="\n")

cert = {
    "schema": "beta_n_symbolic_rank/v1",
    "specialisation": {name: specialise(name, forms[name]) for name in PINNED},
    "audit": audit,
    "seconds": round(time.time() - T0, 1),
}
(HERE / "certificate.json").write_text(json.dumps(cert, indent=1) + "\n", encoding="utf-8", newline="\n")
print("specialisation:", json.dumps(cert["specialisation"], indent=1), flush=True)
print("audit:", json.dumps({k: v for k, v in audit.items() if k != "denominators"}, indent=1), flush=True)
print("wrote closed_forms.json and certificate.json in", cert["seconds"], "s")
