#!/usr/bin/env python3
"""Compare the two 189-record fourth-order kernels, record by record.

Inputs: the historical kernel (exact rationals, pinned corpus certificate)
and the cold v10a.26 kernel (the record dump g3_kernel_record_dump.py
produces — floats, diagnostic). Both are run through ONE shape extractor,
the transcript's own 4-point Bloch fit, reimplemented standalone here.

The comparison is structural, not a verdict: it reports the record classes
where one global scale explains both kernels, the classes where it cannot,
and the ΔC attribution per class via hybrid kernels (historical kernel with
one class swapped to the cold values at a time). Neither side is promoted.

Usage:
    python3 scripts/g3_block_comparison.py /path/to/g3_kernel_records.json
"""

from __future__ import annotations

import cmath
import collections
import json
import math
import statistics
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
HIST = (
    ROOT
    / "corpus-import"
    / "programs"
    / "one_plaquette"
    / "y4_o3_flatband_verification"
    / "y4_full_real_space_H4_kernel.json"
    / "CERT_Y4_full_real_space_h4_kernel.json"
)
PLANES = [(0, 1), (0, 2), (1, 2)]
PI = {p: i for i, p in enumerate(PLANES)}
THETA = 2.0 * math.pi / 5.0
FIT = [(THETA, 0, 0), (THETA, THETA, 0), (2 * THETA, THETA, 0), (THETA, THETA, THETA)]


def centered(v):
    return tuple((x + 2) % 5 - 2 for x in v)


def load_hist():
    kernel = json.loads(Path(HIST).read_text())["kernel"]
    return {
        (tuple(r["displacement"]), tuple(r["input_plane"]), tuple(r["output_plane"])): float(
            Fraction(r["weight"])
        )
        for r in kernel
    }


def load_cold(path):
    records = json.loads(Path(path).read_text())["records"]
    return {
        (centered(r["displacement"]), tuple(r["anchor_pol"]), tuple(r["row_pol"])): r["re"]
        for r in records
    }


def boundary_symbol(k):
    """3x3 symbol of B2 at the origin face, planes in PLANES order."""
    n = np.zeros((3, 3), dtype=complex)
    for col, (a, b) in enumerate(PLANES):
        # face in plane (a,b): boundary links in directions a and b
        n[a, col] += 1 - cmath.exp(-1j * k[b])
        n[b, col] -= 1 - cmath.exp(-1j * k[a])
    return n


def flat_vector(k):
    n = boundary_symbol(np.asarray(k, dtype=float))
    _, _, vh = np.linalg.svd(n)
    v = vh[-1].conj()
    return v / np.linalg.norm(v)


def bloch(kernel, k):
    m = np.zeros((3, 3), dtype=complex)
    for (d, ip, op), w in kernel.items():
        m[PI[op], PI[ip]] += w * cmath.exp(-1j * (k[0] * d[0] + k[1] * d[1] + k[2] * d[2]))
    return m


def shape_row(k):
    aa = np.asarray([4.0 * math.sin(float(x) / 2.0) ** 2 for x in k])
    q = float(np.sum(aa))
    e2 = float(aa[0] * aa[1] + aa[0] * aa[2] + aa[1] * aa[2])
    e3 = float(np.prod(aa))
    return np.asarray([q, e2, 4.0 * e2 / q, e3 / q], dtype=float)


def extract_shape(kernel):
    hg = bloch(kernel, (0.0, 0.0, 0.0))
    eps_g = float(np.trace(hg).real / 3.0)
    vals = []
    for k in FIT:
        h = bloch(kernel, k)
        v = flat_vector(k)
        vals.append(float(np.real(np.vdot(v, h @ v))))
    m = np.vstack([shape_row(k) for k in FIT])
    coef = np.linalg.solve(m, np.asarray(vals) - eps_g)
    return {"rest": eps_g, "A": coef[0], "B": coef[1], "C": coef[2], "D": coef[3]}


def dclass(d):
    n = tuple(sorted(abs(x) for x in d))
    return {
        (0, 0, 0): "onsite",
        (0, 0, 1): "nn",
        (0, 1, 1): "diag2",
        (0, 0, 2): "axial2",
        (1, 1, 1): "cube",
        (0, 1, 2): "knight",
    }.get(n, str(n))


def record_class(key):
    d, ip, op = key
    return (dclass(d), "same" if ip == op else "cross")


def main() -> int:
    cold_path = sys.argv[1] if len(sys.argv) > 1 else "g3_kernel_records.json"
    hist = load_hist()
    cold = load_cold(cold_path)
    assert set(hist) == set(cold), "support mismatch"
    print(f"support: identical, {len(hist)} records\n")

    # global scale from the modal ratio class
    ratios = [cold[k] / hist[k] for k in hist if abs(hist[k]) > 1e-15]
    mode = statistics.mode(round(r, 6) for r in ratios)
    s_vals = [r for r in ratios if abs(r - mode) < 1e-3]
    s = statistics.median(s_vals)
    print(
        f"global scale s = {s!r}  explains {len(s_vals)}/{len(ratios)} records "
        f"(spread {max(s_vals) - min(s_vals):.2e})\n"
    )

    divergent = collections.defaultdict(list)
    for k in hist:
        if abs(hist[k]) < 1e-15:
            continue
        if abs(cold[k] / (s * hist[k]) - 1) > 1e-6:
            divergent[record_class(k)].append(k)

    print("divergent classes (cold != s * hist):")
    for cls, keys in sorted(divergent.items()):
        vals_h = sorted({round(hist[k], 10) for k in keys})
        vals_c = sorted({round(cold[k], 10) for k in keys})
        print(f"  {cls}: {len(keys)} records; hist values {vals_h}; cold values {vals_c}")

    hist_s = {k: s * w for k, w in hist.items()}
    for name, kern in (("hist", hist), ("s*hist", hist_s), ("cold", cold)):
        sh = extract_shape(kern)
        print(f"\n{name:8s}: A={sh['A']:+.12f} B={sh['B']:+.2e} C={sh['C']:+.12f} D={sh['D']:+.2e}")

    # ΔC attribution: swap one divergent class at a time into s*hist
    print("\nΔC attribution (swap one divergent class of s*hist to cold values):")
    c_base = extract_shape(hist_s)["C"]
    c_cold = extract_shape(cold)["C"]
    total = 0.0
    for cls, keys in sorted(divergent.items()):
        hybrid = dict(hist_s)
        for k in keys:
            hybrid[k] = cold[k]
        dc = extract_shape(hybrid)["C"] - c_base
        total += dc
        print(f"  {cls}: ΔC = {dc:+.12f}")
    print(f"  sum of class swaps  = {total:+.12f}")
    print(f"  actual C_cold - C_s*hist = {c_cold - c_base:+.12f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
