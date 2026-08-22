#!/usr/bin/env python3
"""
G20 groundwork: first execution of the imported H_phys operator.

This harness contains NO physics of its own. It:
  1. imports, UNMODIFIED, the two byte-verified files from
     /home/user/WORKHOUSE/notes/imported/RESEARCH_2026-08/:
       - h_phys_tools.py        (Pi_phys, projection; sha256 4d98701...)
       - safe_scan_tracked_v2.py (V_Haar, hessian, sampling; sha256 4fd92d8...)
  2. declares the cluster, following the archive's own repro plan
     (07_safe_scan_repro_v2.md section 3, step 1: "one plaquette or two
     plaquettes sharing a link");
  3. sets V_tot(x) = sum_e V_Haar(x_e) -- the "Haar-only in physical
     subspace" quantity of the draft's radius table (07_safe_scan_repro_v2.md
     section 2.1), in the pinned convention: T_a = (i/2) lambda_a orthonormal
     under <A,B> = -2 Re Tr(AB), metric_scale = 1.0 (the code normalization in
     which the machine-checked V_Haar Hessian at the identity is exactly I/4);
  4. computes H_phys(x) = Pi_phys(x)^T [grad^2 V_tot(x)] Pi_phys(x) exactly as
     H_phys_spec.md section 4 pins it, and scans lambda_min over the SAFE ball
     with the imported script's own sampling scheme (random unit directions on
     spheres of radius r, radii 0..0.05, n_dir, seed as in its defaults).

No Wilson term is added: no imported document states a Wilson coupling, so
"Haar + S_W" cannot be run without improvising physics (see report).
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

IMPORT_DIR = Path("/home/user/WORKHOUSE/notes/imported/RESEARCH_2026-08")
sys.dont_write_bytecode = True  # repo is read-only: never drop __pycache__
sys.path.insert(0, str(IMPORT_DIR))

import torch  # noqa: E402

torch.set_num_threads(1)
torch.set_num_interop_threads(1)

import h_phys_tools as HT  # noqa: E402  (imported, unmodified)
import safe_scan_tracked_v2 as SS  # noqa: E402  (imported, unmodified)

DTYPE_R = torch.float64


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Declared clusters (07_safe_scan_repro_v2.md section 3 step 1)
# ---------------------------------------------------------------------------
E = HT.OrientedEdge

CLUSTERS = {
    # one plaquette: the 4-cycle v0->v1->v2->v3->v0
    "plaquette_1x1": HT.Cluster(
        n_vertices=4,
        edges=(E(0, 1), E(1, 2), E(2, 3), E(3, 0)),
    ),
    # two plaquettes sharing the link (1->2):
    # square A: 0->1->2->3->0 ; square B: 1->4->5->2 (closes through edge 1->2)
    "two_plaquettes_shared_link": HT.Cluster(
        n_vertices=6,
        edges=(E(0, 1), E(1, 2), E(2, 3), E(3, 0), E(1, 4), E(4, 5), E(5, 2)),
    ),
}


def v_tot(x: torch.Tensor, cluster: HT.Cluster, data: SS.SU3AdjointData,
          series_order: int) -> torch.Tensor:
    """V_tot(x) = sum over links of the imported single-link V_Haar.

    metric_scale = 1.0 (pinned convention): x enters haar_potential unscaled.
    """
    total = x.new_zeros(())
    for i in range(cluster.n_edges):
        total = total + SS.haar_potential(x[8 * i: 8 * (i + 1)], data,
                                          series_order=series_order)
    return total


def scan_cluster(name: str, cluster: HT.Cluster, radii, n_dir: int, seed: int,
                 series_order: int, sampling: str) -> dict:
    data = SS.precompute_structure_constants()
    rng = torch.Generator().manual_seed(seed)
    d = cluster.dim_links

    # --- identity-point certificate first --------------------------------
    x0 = torch.zeros(d, dtype=DTYPE_R)
    Pi0 = HT.physical_projector_Pi(x0, cluster)
    H0 = SS.hessian_of_scalar(lambda z: v_tot(z, cluster, data, series_order), x0)
    Hp0 = HT.project_hessian(H0, Pi0)
    m0 = Pi0.shape[1]
    dev0 = float(torch.max(torch.abs(Hp0 - 0.25 * torch.eye(m0, dtype=DTYPE_R))))
    lam0 = SS.min_eigval(Hp0)

    rows = []
    global_min = float("inf")
    global_arg = None
    t_start = time.time()
    for r in radii:
        min_r = float("inf")
        min_r_full = float("inf")
        dims = set()
        for _ in range(n_dir):
            if sampling == "total_radius":
                n = SS.random_unit(d, rng)
                x = (r * n).to(DTYPE_R)
            elif sampling == "per_link_radius":
                parts = [SS.random_unit(8, rng) * r for _ in range(cluster.n_edges)]
                x = torch.cat(parts).to(DTYPE_R)
            else:
                raise ValueError(sampling)
            H = SS.hessian_of_scalar(
                lambda z: v_tot(z, cluster, data, series_order), x)
            Pi = HT.physical_projector_Pi(x, cluster)
            dims.add(Pi.shape[1])
            Hp = HT.project_hessian(H, Pi)
            lam = SS.min_eigval(Hp)
            min_r_full = min(min_r_full, SS.min_eigval(H))
            min_r = min(min_r, lam)
            if lam < global_min:
                global_min = lam
                global_arg = (r, x.detach().cpu().numpy().copy())
        rows.append({
            "r": float(r),
            "lambda_min_phys": min_r,
            "lambda_min_total_unprojected": min_r_full,
            "dim_horizontal": sorted(dims),
        })
    elapsed = time.time() - t_start

    out = {
        "cluster": name,
        "n_vertices": cluster.n_vertices,
        "n_edges": cluster.n_edges,
        "dim_links": d,
        "sampling": sampling,
        "n_dir": n_dir,
        "seed": seed,
        "series_order": series_order,
        "metric_scale": 1.0,
        "identity_point": {
            "dim_horizontal": m0,
            "lambda_min_phys_at_0": lam0,
            "max_abs_dev_from_quarter_identity": dev0,
        },
        "rows": rows,
        "global_min_lambda_phys": global_min,
        "global_min_at_radius": None if global_arg is None else float(global_arg[0]),
        "elapsed_s": elapsed,
    }
    if global_arg is not None:
        out["global_min_direction"] = [float(v) for v in global_arg[1]]
    return out


def main() -> None:
    radii = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05]  # imported scan defaults
    n_dir, seed, series_order = 64, 42, 20        # imported scan defaults

    prov = {
        "imported_files": {
            "h_phys_tools.py": sha256(IMPORT_DIR / "h_phys_tools.py"),
            "safe_scan_tracked_v2.py": sha256(IMPORT_DIR / "safe_scan_tracked_v2.py"),
            "H_phys_spec.md": sha256(IMPORT_DIR / "H_phys_spec.md"),
            "07_safe_scan_repro_v2.md": sha256(IMPORT_DIR / "07_safe_scan_repro_v2.md"),
        },
        "torch": torch.__version__,
        "python": sys.version,
        "torch_num_threads": torch.get_num_threads(),
        "argv": sys.argv,
    }
    print("PROVENANCE:", json.dumps(prov, indent=2))

    results = []
    for name, cluster in CLUSTERS.items():
        for sampling in ("total_radius", "per_link_radius"):
            print(f"\n=== cluster={name} sampling={sampling} ===", flush=True)
            res = scan_cluster(name, cluster, radii, n_dir, seed,
                               series_order, sampling)
            results.append(res)
            ip = res["identity_point"]
            print(f"dim_horizontal at identity: {ip['dim_horizontal']} "
                  f"(expected 8*(nE-nV+1) = {8 * (cluster.n_edges - cluster.n_vertices + 1)})")
            print(f"H_phys(0): lambda_min = {ip['lambda_min_phys_at_0']:.15f}, "
                  f"max|H_phys(0) - I/4| = {ip['max_abs_dev_from_quarter_identity']:.3e}")
            for row in res["rows"]:
                print(f"  r={row['r']:.2f}  lambda_min_phys={row['lambda_min_phys']:.9f}"
                      f"  (unprojected lambda_min_tot={row['lambda_min_total_unprojected']:.9f})"
                      f"  dim_hor={row['dim_horizontal']}")
            print(f"GLOBAL MIN lambda_min_phys = {res['global_min_lambda_phys']:.12f} "
                  f"at r = {res['global_min_at_radius']}  [{res['elapsed_s']:.1f}s]")

    out_path = Path(__file__).parent / "h_phys_first_run_results.json"
    out_path.write_text(json.dumps({"provenance": prov, "results": results}, indent=2))
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    main()
