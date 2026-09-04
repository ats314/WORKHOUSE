"""The fourth-order shape coefficient from the cluster assembly at every rank N = 4..70,
against the corpus's all-rank beta_N.

    python beta_from_assembly.py > console.log

At N >= 5 the pair cluster is the plain Hermitian fourth order on the two-face
cluster (workhouse.loopcalc.pair_element): the first-order vertex vanishes and
so does every determinant family. It cancels between the coplanar and the
perpendicular pair (see PAIR_NOTE below), so beta never contains it; at N = 4,
where it is infeasible in this form, it is left out. With the dressings, the corner,
the two-hop weight (runs/rank_sweep_cumulants_2026-09-04) and the adjacent-face
cube completion -106/(N(N^2-1)^3), all in the kernel's (0,2) basis:

    pi(N)  = pair_cop + 18 d_cop + 2 s_cop
    rho(N) = pair_perp + 14 d_perp + 2 s_perp + 2 corner + K_adj     (pair_cop + pair_perp = 0)
    C(N)   = -alpha_N/8 - u(N) - (rho + pi)/2,   alpha_N = 640/(N(N^2-1)^3)
    beta(N) = 8 A_N + 16 C(N),                    A_N = alpha_N/4

compared with the corpus's beta_N = P17(N^2)/(N R20(N^2)) (GLUEBALL v3.1,
transcribed in workhouse.channel_ledger). Nothing here reads a kernel.
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

from workhouse import loopcalc as L  # noqa: E402
from workhouse.channel_ledger import beta_formula  # noqa: E402

REC = ROOT / "runs" / "rank_sweep_cumulants_2026-09-04" / "certificate.json"
rec = json.loads(REC.read_text(encoding="utf-8"))["ranks"]

P = ((0, 1), (0, 0, 0))
Q_COP = ((0, 1), (1, 0, 0))
Q_PERP = ((0, 2), (0, 0, 0))
Q_NORM = ((0, 1), (0, 0, 1))
X_SINGLE_COP = ((0, 1), (2, 0, 0))
X_FAN_COP = ((1, 2), (1, 0, 0))

# N = 4: the pair element in the PVP = 0 form must integrate the (4,0) determinant
# family on every link that carries four parallel fluxes, and at N = 4 that is
# about fifteen thousand inner products at well over four seconds each -- not a
# computation for this record (two attempts were stopped after 23 CPU-minutes
# each with no inner product complete). It is also not needed: the coplanar and
# perpendicular two-face clusters are one abstract graph up to conjugating Q, so
# their pair elements agree entry by entry under Q <-> Q-bar (checked at N = 5,
# all four entries) and their C-odd blocks are exact negatives at every rank --
# pair_cop + pair_perp = 0 identically, and (rho + pi)/2 never contains the pair
# cluster. At N = 4 the nine other cumulants are computed and the pair entries
# are recorded as null.
PAIR_NOTE = (
    "pair clusters not computed at N = 4 (the (4,0)-family PVP = 0 pair element is infeasible); "
    "they cancel identically in rho + pi, so beta does not depend on them"
)

ONLY = [int(a) for a in sys.argv[1:]]  # e.g. `python beta_from_assembly.py 4` updates one rank
CERT = HERE / "certificate.json"
if ONLY and CERT.exists():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
else:
    cert = {"schema": "beta_n_from_assembly/v1", "basis": "(0,2) x-then-z, the kernel's", "ranks": {}}
T0 = time.time()
for n in ONLY or list(range(5, 71)) + [4]:
    L.set_rank(n)
    t0 = time.time()
    if n >= 5:
        pair_cop = L.block_odd(L.pair_element([P, Q_COP]))
        pair_perp = L.block_odd(L.pair_element([P, Q_PERP]))
        pair_norm = L.block_odd(L.pair_element([P, Q_NORM]))
        assert pair_cop + pair_perp == 0
    else:
        pair_cop = pair_perp = pair_norm = None
    d_cop = L.block_odd(L.cumulant([P, X_SINGLE_COP, Q_COP], 1))
    s_cop = L.block_odd(L.cumulant([P, X_FAN_COP, Q_COP], 1))
    r = rec[str(n)]
    u, d_perp, s_perp, corner = (F(r[k]) for k in ("u_odd", "single_odd", "fan_odd", "corner_odd"))
    den = n * (n * n - 1) ** 3
    k_adj = F(-106, den)
    pi = (pair_cop or 0) + 18 * d_cop + 2 * s_cop
    rho = (pair_perp or 0) + 14 * d_perp + 2 * s_perp + 2 * corner + k_adj
    c = F(-80, den) - u - (rho + pi) / 2
    beta_asm = 8 * F(160, den) + 16 * c
    beta_corpus = beta_formula(n)
    row = {
        "pair_coplanar": None if pair_cop is None else str(pair_cop),
        "pair_perpendicular": None if pair_perp is None else str(pair_perp),
        "pair_normal": None if pair_norm is None else str(pair_norm),
        "single_coplanar": str(d_cop),
        "fan_coplanar": str(s_cop),
        "pi": str(pi),
        "rho": str(rho),
        "C_shp": str(c),
        "beta_assembled": str(beta_asm),
        "beta_corpus": str(beta_corpus),
        "equal": beta_asm == beta_corpus,
        "seconds": round(time.time() - t0, 1),
    }
    if n < 5:
        row["note"] = PAIR_NOTE
    cert["ranks"][str(n)] = row
    print(
        f"[{time.time() - T0:7.1f}s] N={n}: beta_assembled = {beta_asm} ; corpus = {beta_corpus} ; "
        f"equal = {row['equal']} ; pair_normal = {pair_norm} ({row['seconds']}s)",
        flush=True,
    )
    (HERE / "certificate.json").write_text(json.dumps(cert, indent=1) + "\n", encoding="utf-8", newline="\n")
L.set_rank(3)
cert["seconds"] = round(time.time() - T0, 1) + cert.get("seconds", 0)
(HERE / "certificate.json").write_text(json.dumps(cert, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote certificate.json")
