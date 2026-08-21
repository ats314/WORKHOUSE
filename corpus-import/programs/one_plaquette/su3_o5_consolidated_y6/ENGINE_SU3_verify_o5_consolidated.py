#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent

EXPECTED_HASHES = {
    "sources/AUDIT_SU3_glueball_string_normalization_2026-06-14.md": "e5a1d1240025d29d2f1bf9ae6afef07a60cdef5988003b07ebaa07098506344d",
    "sources/CERT_STRING_su3_tension_o4_certificate_normalized_v2.json": "e8ed0889df2a512d10b35c994ba32cf053dd9bcbb3f272a930cfec034ee68d5a",
    "sources/THM_STRING_su3_tension_o4_theorem_normalized_v2.md": "272a791f7c2cdfca49514a2a783bf85d0768e9cf8412b57d7d3cbdeac75b3eed",
    "sources/CERT_Y5_su3_fifth_order_certificate.json": "ce92a0aa66172346e6afc86d284e8e44eb38675faa96fda0fabfeb7514f8d89e",
    "sources/THM_Y5_su3_fifth_order_theorem.md": "7a1ab7acb533f2bf5221d76fb7ce4dc66487064e098d1258994f2367de5837b4",
}

MASS = [
    F(8, 3),
    F(1),
    F(11, 306),
    -F(109151, 249696),
    -F(20721577909065127111, 7250590288602460800),
    -F(866236750503342026253096691057, 1169668083793811403447133488000),
]

SIGMA = [
    F(2, 3),
    F(0),
    -F(22, 153),
    -F(61, 408),
    -F(737327120374220449, 7250590288602460800),
    -F(137767222189182735950309, 2009803206414863779920000),
    -F(
        13130661661034190772935959348816444649800714410750015999,
        168641444007491247688836385300053017225944999004544000000,
    ),
]

EXPECTED_RATIO = [
    F(4, 3),
    F(1, 2),
    F(11, 68),
    -F(7559, 499392),
    -F(15752822901180179, 12642703205932800),
    -F(
        10670728893034386567182468628311,
        46786723351752456137885339520000,
    ),
]


def fstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def poly_mul(a, b, order):
    out = [F(0)] * (order + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= order:
                out[i + j] += x * y
    return out


def inverse_sqrt_one_plus(t, order):
    # Sum_{k>=0} binom(-1/2,k) t^k.
    out = [F(0)] * (order + 1)
    power = [F(1)] + [F(0)] * order
    coeff = F(1)
    for k in range(order + 1):
        for i in range(order + 1):
            out[i] += coeff * power[i]
        power = poly_mul(power, t, order)
        coeff *= F(-1, 2) - k
        coeff /= k + 1
    return out


def ratio_inside_sqrt6(mass, sigma, order):
    s0 = sigma[0]
    t = [F(0)] * (order + 1)
    for i in range(1, min(len(sigma), order + 1)):
        t[i] = sigma[i] / s0
    inv = inverse_sqrt_one_plus(t, order)
    # m/sqrt(sigma) = sqrt(6) * [m/2] * (1+t)^(-1/2).
    half_mass = [F(0)] * (order + 1)
    for i in range(min(len(mass), order + 1)):
        half_mass[i] = mass[i] / 2
    return poly_mul(half_mass, inv, order)


def gate(name, condition, detail=""):
    print(("PASS" if condition else "FAIL"), name, detail)
    if not condition:
        raise AssertionError(name)


def main():
    for rel, expected in EXPECTED_HASHES.items():
        p = ROOT / rel
        gate(f"source hash {rel}", p.exists() and sha256(p) == expected, expected)

    y5 = json.loads((ROOT / "sources/CERT_Y5_su3_fifth_order_certificate.json").read_text())
    norm = json.loads((ROOT / "sources/CERT_STRING_su3_tension_o4_certificate_normalized_v2.json").read_text())
    fold = json.loads((ROOT / "CERT_Y6_folded_descloizeaux_preflight_certificate.json").read_text())
    local = json.loads((ROOT / "CERT_Y6_local_fusion_path_preflight_certificate.json").read_text())
    cert = json.loads((ROOT / "CERT_SU3_o5_consolidated_certificate.json").read_text())

    gate("Y5 source certificate PASS", y5["status"] == "PASS")
    gate("normalization source certificate PASS", norm["gates"]["all_passed"] is True)
    gate("preferred variable u", norm["meta"]["preferred_variable"] == "u=beta_lat/6=1/g^4")
    gate("m5 exact", F(y5["coefficients"]["q5"]) == MASS[5], y5["coefficients"]["q5"])
    gate("sigma5 target exact", F(norm["string_tension"]["historical_targets"]["sigma5"]) == SIGMA[5])
    gate("sigma6 target exact", F(norm["string_tension"]["historical_targets"]["sigma6"]) == SIGMA[6])

    ratio = ratio_inside_sqrt6(MASS, SIGMA, 5)
    gate("ratio coefficients through O(u^5)", ratio == EXPECTED_RATIO, str([fstr(x) for x in ratio]))
    gate("consolidated c5", F(cert["ratio"]["inside_sqrt6_coefficients"]["c5"]) == EXPECTED_RATIO[5])
    gate("folded O(u^6) preflight PASS", fold["status"] == "PASS" and all(fold["gates"].values()))
    gate("local O(u^6) fusion-path preflight PASS", local["status"] == "PASS" and all(local["gates"].values()))
    sectors = {tuple(x["canonical_nfund_nantifund"]) for x in local["sectors"]}
    gate("double-determinant local sectors present", {(0, 6), (1, 7)} <= sectors, str(sorted(sectors)))
    gate("m6 remains unresolved", cert["research_boundary"]["m6_status"] == "unknown")

    print("ALL CONSOLIDATED O5 + Y6 PREFLIGHT GATES PASS")


if __name__ == "__main__":
    main()
