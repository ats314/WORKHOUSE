"""The two 189-record fourth-order kernels, compared record by record.

Pure-stdlib reimplementation of the v10a.26 transcript's 4-point Bloch
shape fit (no numpy: CI does not carry it), applied to the pinned
historical certificate (exact rationals) and the pinned cold record dump
(runs/g3_kernel_record_dump_2026-08-28/). One investigation, one module —
the same shape as tier_collapse.py and near_gamma.py.

Everything here is float arithmetic over recorded artifacts, so nothing
in this module can exceed T2, and nothing in it prefers either kernel.
"""

from __future__ import annotations

import cmath
import json
import math
import statistics
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HIST_CERT = (
    ROOT
    / "corpus-import"
    / "programs"
    / "one_plaquette"
    / "y4_o3_flatband_verification"
    / "y4_full_real_space_H4_kernel.json"
    / "CERT_Y4_full_real_space_h4_kernel.json"
)
COLD_DUMP = ROOT / "runs" / "g3_kernel_record_dump_2026-08-28" / "g3_kernel_records.json"

PLANES = [(0, 1), (0, 2), (1, 2)]
_PI = {p: i for i, p in enumerate(PLANES)}
_THETA = 2.0 * math.pi / 5.0
FIT_POINTS = [
    (_THETA, 0.0, 0.0),
    (_THETA, _THETA, 0.0),
    (2 * _THETA, _THETA, 0.0),
    (_THETA, _THETA, _THETA),
]

Key = tuple[tuple[int, int, int], tuple[int, int], tuple[int, int]]


def load_historical() -> dict[Key, float]:
    kernel = json.loads(HIST_CERT.read_text(encoding="utf-8"))["kernel"]
    return {
        (tuple(r["displacement"]), tuple(r["input_plane"]), tuple(r["output_plane"])): float(
            Fraction(r["weight"])
        )
        for r in kernel
    }


def load_cold() -> dict[Key, float]:
    records = json.loads(COLD_DUMP.read_text(encoding="utf-8"))["records"]

    def centered(v):
        return tuple((x + 2) % 5 - 2 for x in v)

    return {
        (centered(r["displacement"]), tuple(r["anchor_pol"]), tuple(r["row_pol"])): r["re"]
        for r in records
    }


def _boundary_symbol(k) -> list[list[complex]]:
    n = [[0j] * 3 for _ in range(3)]
    for col, (a, b) in enumerate(PLANES):
        n[a][col] += 1 - cmath.exp(-1j * k[b])
        n[b][col] -= 1 - cmath.exp(-1j * k[a])
    return n


def _flat_vector(k) -> list[complex]:
    """Unit right-null vector of the boundary symbol, by adjugate row cross."""
    n = _boundary_symbol(k)

    def cross(a, b):
        return [
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        ]

    # v with N v = 0: rows dot v (no conjugation) vanish, so any cross
    # product of two independent rows works — take the best-conditioned
    # pair; at fit points where N has a zero column the cross products can
    # all degenerate, and the null vector is that coordinate axis.
    best, best_norm = None, 0.0
    for a, b in ((0, 1), (0, 2), (1, 2)):
        v = cross(n[a], n[b])
        norm = math.sqrt(sum(abs(x) ** 2 for x in v))
        if norm > best_norm:
            best, best_norm = v, norm
    if best_norm < 1e-12:
        col = min(range(3), key=lambda j: sum(abs(n[i][j]) for i in range(3)))
        best = [1.0 + 0j if j == col else 0j for j in range(3)]
        best_norm = 1.0
    return [x / best_norm for x in best]


def _bloch(kernel: dict[Key, float], k) -> list[list[complex]]:
    m = [[0j] * 3 for _ in range(3)]
    for (d, ip, op), w in kernel.items():
        m[_PI[op]][_PI[ip]] += w * cmath.exp(-1j * (k[0] * d[0] + k[1] * d[1] + k[2] * d[2]))
    return m


def _shape_row(k) -> list[float]:
    aa = [4.0 * math.sin(x / 2.0) ** 2 for x in k]
    q = sum(aa)
    e2 = aa[0] * aa[1] + aa[0] * aa[2] + aa[1] * aa[2]
    e3 = aa[0] * aa[1] * aa[2]
    return [q, e2, 4.0 * e2 / q, e3 / q]


def _solve4(m: list[list[float]], d: list[float]) -> list[float]:
    a = [row[:] + [d[i]] for i, row in enumerate(m)]
    n = 4
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[piv] = a[piv], a[col]
        for r in range(n):
            if r != col:
                f = a[r][col] / a[col][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col], strict=True)]
    return [a[i][4] / a[i][i] for i in range(n)]


def extract_shape(kernel: dict[Key, float]) -> dict[str, float]:
    """The transcript's fit: A q + B e2 + C 4e2/q + D e3/q on the flat band."""
    hg = _bloch(kernel, (0.0, 0.0, 0.0))
    rest = sum(hg[i][i].real for i in range(3)) / 3.0
    vals = []
    for k in FIT_POINTS:
        h = _bloch(kernel, k)
        v = _flat_vector(k)
        hv = [sum(h[i][j] * v[j] for j in range(3)) for i in range(3)]
        vals.append(sum((v[i].conjugate() * hv[i]).real for i in range(3)))
    coef = _solve4([_shape_row(k) for k in FIT_POINTS], [x - rest for x in vals])
    return {"rest": rest, "A": coef[0], "B": coef[1], "C": coef[2], "D": coef[3]}


def record_class(key: Key) -> tuple[str, str]:
    d, ip, op = key
    n = tuple(sorted(abs(x) for x in d))
    names = {
        (0, 0, 0): "onsite",
        (0, 0, 1): "nn",
        (0, 1, 1): "diag2",
        (0, 0, 2): "axial2",
        (1, 1, 1): "cube",
        (0, 1, 2): "knight",
    }
    return (names.get(n, str(n)), "same" if ip == op else "cross")


def compare() -> dict:
    """The full structural comparison; every number a check needs."""
    hist = load_historical()
    cold = load_cold()
    ratios = {k: cold[k] / hist[k] for k in hist if abs(hist[k]) > 1e-15 and k in cold}
    mode = statistics.mode(round(r, 6) for r in ratios.values())
    bulk = [r for r in ratios.values() if abs(r - mode) < 1e-3]
    s = statistics.median(bulk)
    divergent: dict[tuple[str, str], list[Key]] = {}
    for k, r in ratios.items():
        if abs(r / s - 1) > 1e-6:
            divergent.setdefault(record_class(k), []).append(k)
    hist_s = {k: s * w for k, w in hist.items()}
    c_base = extract_shape(hist_s)["C"]
    swaps = {}
    for cls, keys in divergent.items():
        hybrid = dict(hist_s)
        for k in keys:
            hybrid[k] = cold[k]
        swaps[cls] = extract_shape(hybrid)["C"] - c_base
    # the divergent cross sector, resolved to its own structure: the 24
    # divergent cross records are ONE amplitude in each kernel (a single
    # cold/hist multiplier across all of them), and the other 96 cross
    # records ride the bulk scale exactly.
    big_x = Fraction(238714892212171339, 29002361154409843200)
    cross_ratios = set()
    small_cross_ratios = set()
    for k, r in ratios.items():
        d, ip, op = k
        if ip == op:
            continue
        if abs(abs(hist[k]) - float(big_x)) < 1e-15:
            cross_ratios.add(round(r, 9))
        else:
            small_cross_ratios.add(round(r / s, 9))
    return {
        "support_hist": set(hist),
        "support_cold": set(cold),
        "cross_ratios": cross_ratios,
        "small_cross_ratios": small_cross_ratios,
        "scale": s,
        "bulk_count": len(bulk),
        "bulk_spread": max(bulk) - min(bulk),
        "divergent": {cls: sorted(keys) for cls, keys in divergent.items()},
        "shape_hist": extract_shape(hist),
        "shape_cold": extract_shape(cold),
        "c_base": c_base,
        "swaps": swaps,
    }
