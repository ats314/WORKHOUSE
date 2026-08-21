#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

def gate(name: str, condition: bool, detail: str = "") -> None:
    print(("PASS" if condition else "FAIL"), name, detail, flush=True)
    if not condition:
        raise RuntimeError(f"{name}: {detail}")

def load(name: str):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

support = load("support_scan_raw.json")
local = load("local_coefficients_raw.json")
sigma4_payload = load("sigma4_raw.json")

raw = {
    0: F(2, 3),
    1: F(0),
    2: F(local["sigma2"]),
    3: F(local["sigma3"]),
    4: F(sigma4_payload["sigma4"]),
}
expected_raw = {
    0: F(2, 3),
    1: F(0),
    2: -F(22, 153),
    3: F(61, 408),
    4: -F(737327120374220449, 7250590288602460800),
}
for n in range(5):
    gate(f"raw reduced coefficient n={n}", raw[n] == expected_raw[n], str(raw[n]))

t = {
    0: F(4, 3),
    1: F(0),
    2: -F(11, 153),
    3: -F(61, 1632),
    4: -F(737327120374220449, 58004722308819686400),
    5: -F(137767222189182735950309, 32156851302637820478720000),
    6: -F(
        13130661661034190772935959348816444649800714410750015999,
        5396526208239719926042764329601696551230239968145408000000,
    ),
}

physical_from_raw = {n: raw[n] * F((-1) ** n, 4**n) for n in range(5)}
physical = {n: t[n] / (2 ** (n + 1)) for n in range(7)}

for n in range(5):
    gate(
        f"project contraction agrees with KPS at n={n}",
        physical_from_raw[n] == physical[n],
        f"{physical_from_raw[n]} vs {physical[n]}",
    )

order4 = support["order4"]
gate("support count", order4["primitive_supports"] == 182440)
gate("fourth-order admissible assignments", order4["triality_assignments"] == 636)
gate("no triality-only fourth-order assignments", order4["triality_only_assignments"] == 0)
gate("support JSON canonicalized", "walltime_seconds" not in order4)

mass = {
    0: F(8, 3),
    1: F(1),
    2: F(11, 306),
    3: -F(109151, 249696),
    4: -F(20721577909065127111, 7250590288602460800),
}

# Compute Q(y)=(sigma/(2/3))^(-1/2) recursively from Q^2*S=1.
# This avoids a very expensive symbolic square-root expansion of the huge
# sixth-order rational coefficient.
S = [sp.Rational(physical.get(n, F(0)).numerator, physical.get(n, F(0)).denominator) /
     sp.Rational(2, 3) for n in range(7)]
Q = [sp.Integer(1)]
for n in range(1, 7):
    qn = sp.symbols(f"q{n}")
    trial = Q + [qn]
    coeff = sp.Integer(0)
    for i in range(n + 1):
        for j in range(n + 1 - i):
            k = n - i - j
            if i < len(trial) and j < len(trial) and k < len(S):
                coeff += trial[i] * trial[j] * S[k]
    Q.append(sp.simplify(sp.solve(sp.Eq(coeff, 0), qn)[0]))

mass_sym = [
    sp.Rational(mass[n].numerator, mass[n].denominator) if n in mass
    else (sp.symbols("m5") if n == 5 else sp.symbols("m6"))
    for n in range(7)
]
# m/sqrt(sigma)=sqrt(6)*sum b_n y^n.
b = []
for n in range(7):
    b.append(sp.simplify(sum(mass_sym[i] * Q[n-i] for i in range(n+1)) / 2))

expected_ratio = [
    sp.Rational(4, 3),
    sp.Rational(1, 2),
    sp.Rational(11, 408),
    -sp.Rational(850411, 3995136),
    -sp.Rational(2649605075224534084759, 1856151113882229964800),
]
gate(
    "corrected ratio coefficients through O(y^4)",
    b[:5] == expected_ratio,
    str(b[:5]),
)

certificate = {
    "meta": {
        "version": "2026-06-14-su3-string-physical-o6-v2",
        "status": "PASS",
        "scope": (
            "Project-native raw contractions through n=4; physical normalization "
            "through n=4; KPS historical denominator extension through n=6; "
            "mass numerator certified only through n=4."
        ),
    },
    "normalization": {
        "project_magnetic_vertex": "-y/4 per oriented character insertion",
        "raw_to_physical_rule": "sigma_n = (-1/4)^n sigma_n_reduced",
        "KPS_variable": "x=2/g^4",
        "project_variable": "y=2x",
        "dimensionless_tension": "sigma(y)=W(y/2)/2",
        "KPS_coefficient_rule": "sigma_n=t_n/2^(n+1)",
    },
    "raw_reduced_coefficients": {
        f"sigma{n}_reduced": str(raw[n]) for n in range(5)
    },
    "physical_string_tension_coefficients": {
        f"sigma{n}": str(physical[n]) for n in range(7)
    },
    "mass_coefficients_through_o4": {
        f"m{n}": str(mass[n]) for n in range(5)
    },
    "ratio": {
        "convention": "m/sqrt(sigma)=sqrt(6)*sum b_n y^n",
        "coefficients_through_o4": {
            f"b{n}": str(b[n]) for n in range(5)
        },
        "r5_with_unknown_mass": str(sp.sqrt(6) * b[5]),
        "r6_with_unknown_mass": str(sp.sqrt(6) * b[6]),
    },
    "support_census": support,
    "raw_length_checks": {
        "local": local["rows"],
        "fourth_order": [
            {k: v for k, v in row.items() if k != "ledger"}
            for row in sigma4_payload["rows"]
        ],
    },
    "source_hashes": {
        "support_scan_raw": sha256(RESULTS / "support_scan_raw.json"),
        "local_coefficients_raw": sha256(RESULTS / "local_coefficients_raw.json"),
        "sigma4_raw": sha256(RESULTS / "sigma4_raw.json"),
    },
    "gates": {
        "all_passed": True,
        "project_raw_matches_KPS_orders_0_to_4": True,
        "KPS_denominator_known_through_order_6": True,
        "mass_m5_m6_known": False,
    },
}
cert_path = RESULTS / "CERT_STRING_su3_tension_physical_o6_certificate.json"
cert_path.write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)

theorem = """# Corrected SU(3) fundamental string tension through sixth order

**Status:** PASS  
**Project-native contraction:** through $O(y^4)$  
**Historical KPS extension:** $O(y^5)$ and $O(y^6)$  
**Mass numerator:** certified only through $O(y^4)$

The paper Hamiltonian has nonconstant magnetic vertex

\[
V_y=-\frac y4\sum_p(\chi_p+\bar\chi_p).
\]

Consequently the unit-vertex reduced contraction at order $n$ must be
multiplied by $(-1/4)^n$.

The physical same-normalization string tension is

\[
\begin{aligned}
\sigma(y)=\;&\frac23
-\frac{11}{1224}y^2
-\frac{61}{26112}y^3\\
&-\frac{737327120374220449}{1856151113882229964800}y^4\\
&-\frac{137767222189182735950309}{2058038483368820510638080000}y^5\\
&-\frac{13130661661034190772935959348816444649800714410750015999}
{690755354654684150533473834189017158557470715922612224000000}y^6
+O(y^7).
\end{aligned}
\]

The corrected dimensionless ratio through fourth order is

\[
\frac{m_{1^{+-}}}{\sqrt{\sigma}}
=
\sqrt6\left[
\frac43+\frac12y+\frac{11}{408}y^2
-\frac{850411}{3995136}y^3
-\frac{2649605075224534084759}{1856151113882229964800}y^4
\right]+O(y^5).
\]

The denominator is known through sixth order, but $m_5$ and $m_6$ are not
contained in the audited historical inputs and are not inferred here.
"""
theorem += f"\nCertificate SHA-256: `{sha256(cert_path)}`\n"
(RESULTS / "THM_STRING_su3_tension_physical_o6_theorem.md").write_text(
    theorem, encoding="utf-8"
)

print("ALL PHYSICAL STRING-TENSION V2 GATES PASS", flush=True)
print("CERTIFICATE", cert_path, flush=True)
