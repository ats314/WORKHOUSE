#!/usr/bin/env python3
"""
Single-block A100 validation of the SU(3) O(y^4) real-space SOS theorem.

Default Colab use:
    %run /content/ENGINE_Y4_sos_a100_validation.py

The script:
  1. locates DATA_Y4_full_real_space_h4_kernel.json.gz, or uses the embedded
     exact 189-record regenerated kernel;
  2. reconstructs the exact 25-point SOS stencil in Fraction arithmetic;
  3. applies both the full plaquette-space kernel and the scalar SOS stencil;
  4. verifies C^dagger(H4-qI)C = Q on a periodic 3D lattice;
  5. FFT-verifies the exact symbol and generalized eigenvalue D/G;
  6. benchmarks the local 25-point stencil on the GPU.

No source editing is required.  Run on a Colab A100 runtime.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import io
import json
import math
import time
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

import torch

PLANES = ((0, 1), (0, 2), (1, 2))
A_EXACT = F(5, 12)
B_EXACT = F(17607806155349, 275331901291200)
Q_EXACT = F(-20721577909065127111, 7250590288602460800)
BANDWIDTH_EXACT = F(132329431693349, 275331901291200)
SEMANTIC_KERNEL_SHA256 = "48a422a517c7c1e70b84fd88a0773943f81ae3f9bfafadbe2304f8eb7d2e9b77"

# Exact Stage-3J output regenerated from the complete Stage 0->3J source chain.
EMBEDDED_KERNEL_GZ_B64 = (
    "H4sICAAAAAAC/3k0X2Z1bGxfcmVhbF9zcGFjZV9INF9rZXJuZWwuanNvbgDNXMFu00AQ/RefYzwza6/t3jggxBkuCKHISTYlkCZVHUBQ9d/ZpgeEqFE8u/OEVLWSm/hldt7Me9nZ5L74Eu4OYV9cfbgvNrvxdj+sw004nOKFUha0oI+LYne4/Xpaxn8dQrxMC47Xjl9Pf1/8HnbXn+JTC+epFnYNVzU5aT1x76QjKh4Wf8PwIv6k4gixdxGh976exKGIhIhHu2ylUBNByPXUcNtXLL6WNiJSc8abhINEhUhSzJAAOPdIBAQXSE9tDRfOcIio1IVUMjXUNJ3rukcsJuq4J6q7GNcklnIB2446X3PPkWuuc57bypEwtb10vufW9//AhIUH4iGWhhgWIjoFSJxA2oSVJowyYYQJ5oXm8EAwHuUPmHK2a1DGU9rZEwH5BsH4Bv2ynZVcAOGoWV2K61quu16EhVt2rq8kSqpEPeemrqnv6ize4Q/URFBGZI61mZuPw/hFVNM/ERVR2wJpibP8kaQ4CkBDBOkVSq4wajXLTXCa+l6cHgapLyeVzuXyy4myKIhw1DTAqC/n1XwGZA5FRAQPOaGurN5Lc1J3VdeVlfRlZLi+1yaCMiJzICJCeCh6gsyFIYjIT5SvGMyDWIWTx7VY4LD5uk2OTgxgANmZNnuCGdFcEE+ST1GTPBVVEMkjbe5m4xB+EbXlnGpsBVANjGiJUzstgpndGMAAyA6SK4xaTR4ukdxbIHM4YLDVMgfnwkMsunCyHi7JHhUiSTMthWAshSQeIJjTfPJvVQlmUGRDb9IXU/bDJXYRItIGqitgWSGqCiROIG3CShNGmTDC9B96ITY4XCLZpzQCCGeWa2CMa8g6MLncQDBG2VNnXbpFxOwIWEyDJPcmvLquyjxjJwsgOClYX1illbpz/hMYYj7sQsSG0EVJaPBGbiJF5Z+H4ezTE3mWAmwydULEM9EXDAJ6ti8waIzGtpvwEztTbLwLf4YVRPJQZERwkfS1NRsGwHjSV1a6lWXAnInR1UzqqspgoNlghgZgob7tpk+DbFT+4mhSTAsrYUpDNyEgkc+9pXPRusFEXpLUVrmKpZ2sSz6rxAtMdIIoLtLXlqHM596yMiYFqSsrx8eHGDIZsm5PpK6r9M/xsMGMCFBT+gZoJr8Mkl/GyC8nTj7naC4naq59hiZmRAyaEc3DuejrUbSrlvH7RPJH9ezhEsaMoOwWT12zmQ+XWEaISBuotLCVhSksRPMDiS1Ia4FSi1FaC6GNj7oJp6G4ui9Ww7gbn+4wxls87QI9mbfz/eJDx9NwHdxueX4F8b7VzeFUbYbTUC3HY3zu7jbsd4dQva+Xb9+9fP3Kval+1Mv18eZ2H05huT3uN2Gz/H68i7/Or2188Xk8Hl5c/yx+33z8NEjj49371q22vtvWdb+Of3y73q6Z+tg6u5a4bYah9ZvG90MdaNVsN23Xhhij8KqREFYS7/kt3I274+HxHRaJL8mX7MonoM/lNy4eHn4BM8eakjhPAAA="
)


def gate(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s} {name:58s} {detail}")
    if not condition:
        raise AssertionError(f"{name}: {detail}")


def recursive_find(filename: str) -> Path | None:
    preferred = [
        Path("/content") / filename,
        Path("/content/Y4_STAGE3J") / filename,
        Path.cwd() / filename,
        Path.cwd() / "Y4_STAGE3J" / filename,
        Path("/mnt/data") / filename,
        Path("/mnt/data/_sos_pipeline/Y4_STAGE3J") / filename,
    ]
    for path in preferred:
        if path.exists():
            return path
    for root in (Path("/content"), Path.cwd(), Path("/mnt/data")):
        if root.exists():
            for path in root.rglob(filename):
                return path
    return None


def load_kernel() -> tuple[dict, str]:
    path = recursive_find("DATA_Y4_full_real_space_h4_kernel.json.gz")
    if path is not None:
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            return json.load(handle), str(path)
    raw = gzip.decompress(base64.b64decode(EMBEDDED_KERNEL_GZ_B64))
    return json.loads(raw.decode("utf-8")), "embedded exact Stage-3J kernel"


def semantic_sha(records: list[dict]) -> str:
    canonical = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(canonical).hexdigest()


def exact_scalar_stencil(payload: dict) -> tuple[dict[tuple[int, int, int], F], F]:
    records = payload["kernel"]
    plane_index = {tuple(p): i for i, p in enumerate(payload["meta"]["basis_planes"])}

    # Laurent polynomials as exponent -> rational coefficient.
    zero = (0, 0, 0)
    psi = [
        {zero: F(-1), (0, 0, 1): F(1)},
        {zero: F(1), (0, 1, 0): F(-1)},
        {zero: F(-1), (1, 0, 0): F(1)},
    ]

    def adj(poly):
        return {tuple(-x for x in e): c for e, c in poly.items()}

    def mul(left, right):
        out = defaultdict(F)
        for e, c in left.items():
            for f, d in right.items():
                out[tuple(e[i] + f[i] for i in range(3))] += c * d
        return {e: c for e, c in out.items() if c}

    h0 = [[F(0) for _ in range(3)] for _ in range(3)]
    out = defaultdict(F)
    for record in records:
        a = plane_index[tuple(record["input_plane"])]
        b = plane_index[tuple(record["output_plane"])]
        r = tuple(int(x) for x in record["displacement"])
        w = F(record["weight"])
        h0[b][a] += w
        for e, c in mul(adj(psi[b]), psi[a]).items():
            out[tuple(e[i] + r[i] for i in range(3))] += w * c

    q = h0[0][0]
    for a in range(3):
        for e, c in mul(adj(psi[a]), psi[a]).items():
            out[e] -= q * c
    return {e: c for e, c in out.items() if c}, q


def expected_stencil() -> dict[tuple[int, int, int], F]:
    w0 = F(9, 2) * A_EXACT + 3 * B_EXACT
    w1 = -(A_EXACT + B_EXACT)
    w2 = A_EXACT / 4
    wd = B_EXACT / 4
    out = defaultdict(F)
    out[(0, 0, 0)] = w0
    for i in range(3):
        for s in (-1, 1):
            e = [0, 0, 0]
            e[i] = s
            out[tuple(e)] += w1
            e = [0, 0, 0]
            e[i] = 2 * s
            out[tuple(e)] += w2
    for i in range(3):
        for j in range(i + 1, 3):
            for si in (-1, 1):
                for sj in (-1, 1):
                    e = [0, 0, 0]
                    e[i] = si
                    e[j] = sj
                    out[tuple(e)] += wd
    return dict(out)


def roll_plus(field: torch.Tensor, displacement: tuple[int, int, int]) -> torch.Tensor:
    # Returns field[x+r], whose Fourier multiplier is exp(+ik.r).
    return torch.roll(field, shifts=tuple(-x for x in displacement), dims=(0, 1, 2))


def boundary(phi: torch.Tensor) -> list[torch.Tensor]:
    # C phi in basis planes (01,02,12), matching psi=(z2-1,1-z1,z0-1).
    return [
        roll_plus(phi, (0, 0, 1)) - phi,
        phi - roll_plus(phi, (0, 1, 0)),
        roll_plus(phi, (1, 0, 0)) - phi,
    ]


def boundary_adjoint(fields: list[torch.Tensor]) -> torch.Tensor:
    y01, y02, y12 = fields
    return (
        roll_plus(y01, (0, 0, -1)) - y01
        + y02 - roll_plus(y02, (0, -1, 0))
        + roll_plus(y12, (-1, 0, 0)) - y12
    )


def apply_full_h4(
    plaquettes: list[torch.Tensor],
    records: list[dict],
    plane_index: dict[tuple[int, int], int],
    dtype: torch.dtype,
) -> list[torch.Tensor]:
    out = [torch.zeros_like(plaquettes[0]) for _ in range(3)]
    for record in records:
        a = plane_index[tuple(record["input_plane"])]
        b = plane_index[tuple(record["output_plane"])]
        r = tuple(int(x) for x in record["displacement"])
        w = float(F(record["weight"]))
        out[b].add_(roll_plus(plaquettes[a], r), alpha=w)
    return out


def apply_metric(phi: torch.Tensor) -> torch.Tensor:
    out = torch.zeros_like(phi)
    for axis in range(3):
        e = [0, 0, 0]
        e[axis] = 1
        ep = tuple(e)
        em = tuple(-x for x in e)
        out += 2 * phi - roll_plus(phi, ep) - roll_plus(phi, em)
    return out


def apply_q_stencil(phi: torch.Tensor, weights: dict[str, float]) -> torch.Tensor:
    out = weights["w0"] * phi
    for axis in range(3):
        e = [0, 0, 0]
        e[axis] = 1
        ep = tuple(e)
        em = tuple(-x for x in e)
        e2p = tuple(2 * x for x in e)
        e2m = tuple(-2 * x for x in e)
        out = out + weights["w1"] * (roll_plus(phi, ep) + roll_plus(phi, em))
        out = out + weights["w2"] * (roll_plus(phi, e2p) + roll_plus(phi, e2m))
    for i in range(3):
        for j in range(i + 1, 3):
            for si in (-1, 1):
                for sj in (-1, 1):
                    e = [0, 0, 0]
                    e[i] = si
                    e[j] = sj
                    out = out + weights["wd"] * roll_plus(phi, tuple(e))
    return out


def sync(device: torch.device) -> None:
    if device.type == "cuda":
        torch.cuda.synchronize(device)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--L", type=int, default=128)
    parser.add_argument("--bench-iters", type=int, default=10)
    parser.add_argument("--allow-cpu", action="store_true")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("/content/Y4_SOS_A100") if Path("/content").exists() else Path("/mnt/data/Y4_SOS_A100"),
    )
    args, _unknown = parser.parse_known_args()

    cuda = torch.cuda.is_available()
    if not cuda and not args.allow_cpu:
        raise RuntimeError("CUDA runtime required. In Colab select an A100 GPU runtime and rerun this cell.")
    device = torch.device("cuda" if cuda else "cpu")
    dtype = torch.float64
    device_name = torch.cuda.get_device_name(0) if cuda else "CPU validation mode"

    print("=" * 104)
    print("SU(3) O(y^4) REAL-SPACE SOS — A100 VALIDATION")
    print("=" * 104)
    print("device :", device_name)
    print("torch  :", torch.__version__)
    print("L      :", args.L)
    print("dtype  :", dtype)
    print()

    payload, kernel_source = load_kernel()
    records = payload["kernel"]
    kernel_sha = semantic_sha(records)
    gate("kernel record count", len(records) == 189, str(len(records)))
    gate("semantic kernel SHA-256", kernel_sha == SEMANTIC_KERNEL_SHA256, kernel_sha)
    gate("basis planes", tuple(tuple(p) for p in payload["meta"]["basis_planes"]) == PLANES)
    print("kernel :", kernel_source)

    derived, q_exact = exact_scalar_stencil(payload)
    expected = expected_stencil()
    gate("exact contracted 25-point support", len(derived) == 25, str(len(derived)))
    gate("exact scalar stencil derivation", derived == expected)
    gate("exact q", q_exact == Q_EXACT, str(q_exact))

    w0 = float(expected[(0, 0, 0)])
    w1 = float(expected[(1, 0, 0)])
    w2 = float(expected[(2, 0, 0)])
    wd = float(expected[(1, 1, 0)])
    weights = {"w0": w0, "w1": w1, "w2": w2, "wd": wd}
    gate("exact row sum", sum(expected.values(), F(0)) == 0)

    torch.manual_seed(20260614)
    if cuda:
        torch.cuda.manual_seed_all(20260614)
        torch.cuda.reset_peak_memory_stats(device)

    phi = torch.randn((args.L, args.L, args.L), device=device, dtype=dtype)
    plane_index = {plane: i for i, plane in enumerate(PLANES)}

    # Full plaquette-kernel closure gate.
    Cphi = boundary(phi)
    H4C = apply_full_h4(Cphi, records, plane_index, dtype)
    q_float = float(q_exact)
    shifted = [H4C[i] - q_float * Cphi[i] for i in range(3)]
    lhs = boundary_adjoint(shifted)
    rhs = apply_q_stencil(phi, weights)
    sync(device)
    abs_err = float((lhs - rhs).abs().max().item())
    scale = float(rhs.abs().max().item())
    rel_err = abs_err / max(scale, 1e-300)
    tolerance = 2e-11 if device.type == "cuda" else 5e-12
    gate("full 189-record kernel -> 25-point SOS", rel_err < tolerance, f"abs={abs_err:.3e}, rel={rel_err:.3e}")

    # Metric identity C^dag C = sum_i L_i.
    metric_from_C = boundary_adjoint(Cphi)
    metric_stencil = apply_metric(phi)
    metric_err = float((metric_from_C - metric_stencil).abs().max().item())
    gate("cube-boundary Gram metric", metric_err < 5e-13, f"max={metric_err:.3e}")

    # FFT symbol gate using a lattice delta.
    delta = torch.zeros_like(phi)
    delta[0, 0, 0] = 1.0
    q_delta = apply_q_stencil(delta, weights)
    g_delta = apply_metric(delta)
    qhat = torch.fft.fftn(q_delta)
    ghat = torch.fft.fftn(g_delta)

    k = 2 * math.pi * torch.fft.fftfreq(args.L, d=1.0, device=device, dtype=dtype)
    X0 = (1 - torch.cos(k))[:, None, None]
    X1 = (1 - torch.cos(k))[None, :, None]
    X2 = (1 - torch.cos(k))[None, None, :]
    A = float(A_EXACT)
    B = float(B_EXACT)
    d_theory = A * (X0**2 + X1**2 + X2**2) + B * (X0 * X1 + X0 * X2 + X1 * X2)
    g_theory = 2 * (X0 + X1 + X2)

    qhat_err = float((qhat.real - d_theory).abs().max().item())
    qhat_imag = float(qhat.imag.abs().max().item())
    ghat_err = float((ghat.real - g_theory).abs().max().item())
    gate("FFT numerator symbol", qhat_err < 2e-12 and qhat_imag < 2e-12, f"real={qhat_err:.3e}, imag={qhat_imag:.3e}")
    gate("FFT Gram symbol", ghat_err < 2e-12, f"max={ghat_err:.3e}")

    mask = g_theory > 1e-10
    ratio_fft = qhat.real[mask] / ghat.real[mask]
    ratio_theory = d_theory[mask] / g_theory[mask]
    ratio_err = float((ratio_fft - ratio_theory).abs().max().item())
    gate("generalized eigenvalue D/G", ratio_err < 2e-12, f"max={ratio_err:.3e}")

    # Exact high-symmetry values on an even grid.
    gate("even lattice for parity points", args.L % 2 == 0, str(args.L))
    h = args.L // 2
    def ratio_at(index):
        return float((qhat.real[index] / ghat.real[index]).item())

    lam_X = ratio_at((h, 0, 0))
    lam_M = ratio_at((h, h, 0))
    lam_R = ratio_at((h, h, h))
    gate("X lift A", abs(lam_X - float(A_EXACT)) < 2e-13, f"{lam_X:.15g}")
    gate("M lift A+B/2", abs(lam_M - float(A_EXACT + B_EXACT / 2)) < 2e-13, f"{lam_M:.15g}")
    gate("R lift/bandwidth A+B", abs(lam_R - float(BANDWIDTH_EXACT)) < 2e-13, f"{lam_R:.15g}")

    # Benchmark the scalar local operator only; this is the production stencil.
    for _ in range(3):
        rhs = apply_q_stencil(phi, weights)
    sync(device)
    t0 = time.perf_counter()
    for _ in range(args.bench_iters):
        rhs = apply_q_stencil(rhs, weights)
    sync(device)
    elapsed = time.perf_counter() - t0
    sites = args.L**3 * args.bench_iters
    site_updates_per_second = sites / elapsed
    ns_per_site = elapsed * 1e9 / sites
    peak_memory = int(torch.cuda.max_memory_allocated(device)) if cuda else 0

    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary = {
        "status": "PASS",
        "device": device_name,
        "torch_version": torch.__version__,
        "lattice_L": args.L,
        "dtype": str(dtype),
        "kernel_source": kernel_source,
        "kernel_records": len(records),
        "semantic_kernel_sha256": kernel_sha,
        "exact_constants": {
            "q": str(Q_EXACT),
            "A": str(A_EXACT),
            "B": str(B_EXACT),
            "bandwidth": str(BANDWIDTH_EXACT),
        },
        "errors": {
            "full_kernel_vs_sos_abs": abs_err,
            "full_kernel_vs_sos_rel": rel_err,
            "gram_metric_abs": metric_err,
            "fft_numerator_abs": qhat_err,
            "fft_numerator_imag": qhat_imag,
            "fft_gram_abs": ghat_err,
            "generalized_ratio_abs": ratio_err,
        },
        "high_symmetry_lifts": {"X": lam_X, "M": lam_M, "R": lam_R},
        "benchmark": {
            "iterations": args.bench_iters,
            "elapsed_seconds": elapsed,
            "site_updates_per_second": site_updates_per_second,
            "nanoseconds_per_site": ns_per_site,
            "peak_cuda_bytes": peak_memory,
        },
    }
    summary_path = args.output_dir / "y4_sos_a100_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")

    print()
    print("=" * 104)
    print("ALL A100 SOS VALIDATION GATES PASS")
    print("=" * 104)
    print(f"stencil throughput : {site_updates_per_second:.3e} site-updates/s")
    print(f"time per site      : {ns_per_site:.3f} ns")
    if cuda:
        print(f"peak CUDA memory   : {peak_memory / 2**30:.3f} GiB")
    print("summary            :", summary_path)


if __name__ == "__main__":
    main()
