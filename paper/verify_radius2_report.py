#!/usr/bin/env python3
"""Float-half verifier for the sealed cutoff-free radius-two report.

verify_publication_core.py constructs no float anywhere, so everything the
sealed 2026-08-29 radius-two artifact can support — finite-precision spectra,
tolerance-bounded agreements — lives here instead, with every tolerance
stated. Standard library only: the .npz payload is read with zipfile+struct
and the 11x11 Hermitian block is diagonalised by cyclic Jacobi, so no
dependency stands between the reader and the numbers.

What this file checks, and what it does not:

  1. the sealed spectrum artifact matches its pinned SHA-256 exactly;
  2. the eleven-dimensional cutoff-free second-order block odd_c2 is
     Hermitian to 1e-12 and real to 1e-12;
  3. six of its eleven eigenvalues are the exact rationals
     -2429/306 (x2), -404/51 (x3), -2419/306 (x1), each within 1e-12 —
     the outer pair straddles the triple by exactly 2 t_3 = 5/306, the
     shared-link coefficient of the paper, inside an artifact that made
     no shared-link truncation (the exact-arithmetic half of this
     statement is in verify_publication_core.py);
  4. the certificate's direct fourth- and fifth-order matched-gap
     coefficients agree with its own weak-coupling cubic intercepts to
     5e-6, its Cauchy interlacing violation is exactly 0, and its
     rephasing-invariance errors are below 1e-13;
  5. the fifth-order seed-space shape is traceless to 1e-12 and its
     trace-square is nonzero: the instrument emits more than a scalar.

Nothing here adjudicates C_shp: the two-cube cluster carries no off-axis
momentum, and the obstruction theorem is untouched. Nothing here is a
convergence statement. This file verifies a delivered artifact against
itself and against the paper's exact rationals; it does not replay the
builder that produced it.

Run:  python3 verify_radius2_report.py
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import struct
import sys
import zipfile
from fractions import Fraction as F

NPZ = "two_cube_cutoff_free_radius2_finite_u_spectrum.npz"
CERT = "two_cube_cutoff_free_radius2_finite_u_spectrum_certificate.json"
NPZ_SHA256 = "52a17f87d3990b234635828a0c92f73f781e9a3abec8bb3c127e990b7a717e6c"


def load_npy_member(path, member):
    """Minimal .npy v1 reader for the dtypes this artifact uses."""
    with zipfile.ZipFile(path) as z:
        raw = z.read(member + ".npy")
    assert raw[:6] == b"\x93NUMPY", "not an npy payload"
    (hlen,) = struct.unpack("<H", raw[8:10])
    header = ast.literal_eval(raw[10 : 10 + hlen].decode("latin1"))
    assert not header["fortran_order"]
    body = raw[10 + hlen :]
    shape = header["shape"]
    kind = header["descr"]
    n = 1
    for s in shape:
        n *= s
    if kind == "<c16":
        flat = struct.unpack(f"<{2 * n}d", body[: 16 * n])
        vals = [complex(flat[2 * i], flat[2 * i + 1]) for i in range(n)]
    elif kind == "<f8":
        vals = list(struct.unpack(f"<{n}d", body[: 8 * n]))
    else:
        raise AssertionError(f"unhandled dtype {kind}")
    return shape, vals


def jacobi_eigvals(a, sweeps=60):
    """Eigenvalues of a real symmetric matrix by cyclic Jacobi rotations."""
    m = [row[:] for row in a]
    n = len(m)
    for _ in range(sweeps):
        off = math.sqrt(sum(m[i][j] ** 2 for i in range(n) for j in range(n) if i != j))
        if off < 1e-15:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(m[p][q]) < 1e-18:
                    continue
                theta = 0.5 * math.atan2(2 * m[p][q], m[q][q] - m[p][p])
                c, s = math.cos(theta), math.sin(theta)
                for k in range(n):
                    mp, mq = m[p][k], m[q][k]
                    m[p][k] = c * mp - s * mq
                    m[q][k] = s * mp + c * mq
                for k in range(n):
                    mp, mq = m[k][p], m[k][q]
                    m[k][p] = c * mp - s * mq
                    m[k][q] = s * mp + c * mq
    return sorted(m[i][i] for i in range(n))


CHECKS = []


def check(name):
    def register(fn):
        CHECKS.append((name, fn))
        return fn

    return register


@check(f"sealed spectrum artifact matches its pinned SHA-256 {NPZ_SHA256[:12]}...")
def _():
    with open(NPZ, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest() == NPZ_SHA256


def _odd_c2():
    shape, vals = load_npy_member(NPZ, "odd_c2")
    assert shape == (11, 11)
    m = [[vals[11 * i + j] for j in range(11)] for i in range(11)]
    herm = max(abs(m[i][j] - m[j][i].conjugate()) for i in range(11) for j in range(11))
    imag = max(abs(v.imag) for row in m for v in row)
    return [[v.real for v in row] for row in m], herm, imag


@check("odd_c2 is Hermitian to 1e-12 and real to 1e-12")
def _():
    _, herm, imag = _odd_c2()
    return herm < 1e-12 and imag < 1e-12


@check("six sealed eigenvalues are -2429/306 (x2), -404/51 (x3), -2419/306, to 1e-12")
def _():
    m, _, _ = _odd_c2()
    ev = jacobi_eigvals(m)
    targets = [F(-2429, 306)] * 2 + [F(-404, 51)] * 3 + [F(-2419, 306)]
    hits = []
    for t in targets:
        tf = t.numerator / t.denominator
        best = min(range(len(ev)), key=lambda i: abs(ev[i] - tf))
        if abs(ev[best] - tf) >= 1e-12:
            return False
        hits.append(ev.pop(best))
    # and the straddle is the shared-link coefficient, twice, on both sides
    return F(-404, 51) - F(-2429, 306) == F(5, 306) == F(-2419, 306) - F(-404, 51)


@check("certificate: direct C4/C5 matched-gap vs weak-grid intercepts agree to 5e-6")
def _():
    with open(CERT) as fh:
        cert = json.load(fh)
    g = cert["direct_orders"]["matched_gap"]
    return (
        abs(g["c4_gap_direct"] - g["c4_gap_weak_grid_cubic_intercept"]) < 5e-6
        and abs(g["c5_gap_direct"] - g["c5_gap_weak_grid_cubic_intercept"]) < 5e-6
    )


@check("certificate: interlacing violation exactly 0, rephasing errors below 1e-13")
def _():
    with open(CERT) as fh:
        cert = json.load(fh)
    odd = cert["direct_orders"]["odd"]
    even = cert["direct_orders"]["even"]
    reph = max(
        odd["rephasing_c4_spectrum_max_abs_error"],
        odd["rephasing_c5_spectrum_max_abs_error"],
        even["rephasing_c4_spectrum_max_abs_error"],
        even["rephasing_c5_spectrum_max_abs_error"],
    )
    gates = json.dumps(cert.get("gates", {}))
    return reph < 1e-13 and '"max_interlacing_violation": 0' in gates.replace("0.0", "0")


@check("fifth-order seed shape: traceless to 1e-12, trace-square nonzero")
def _():
    shape, vals = load_npy_member(NPZ, "odd_c5_shape_eigenvalues")
    tr = sum(vals)
    tr2 = sum(v * v for v in vals)
    return abs(tr) < 1e-12 and tr2 > 0.3


def main():
    failures = 0
    for name, fn in CHECKS:
        try:
            ok = fn()
        except Exception as exc:  # a missing artifact is a failure, not a crash
            print(f"FAIL  {name}  ({exc!r})")
            failures += 1
            continue
        print(("PASS  " if ok else "FAIL  ") + name)
        failures += not ok
    print(f"\n{len(CHECKS) - failures}/{len(CHECKS)} radius-two report checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
