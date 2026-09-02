"""Assemble the lattice fourth-order nearest-neighbour elements from the stage outputs.

Reads pair_route_<pair>_{gate,dressing,pair}.json, sums the cluster cumulants,
compares with the historical kernel's records, and writes one certificate.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent

X_QUANTUM = F(360421351, 40327601932800)
RECORDS = {
    "normal": ("(0,1)->(0,1) at (0,0,1): the normal orbit nu", F(-1050558388351, 10081900483200)),
    "coplanar": ("(0,1)->(0,1) at (1,0,0): the in-plane orbit pi", F(-20535103905179, 1264270320593280)),
    "perpendicular": ("(0,1)->(0,2) at (0,0,0): the rotation orbit rho", F(238714892212171339, 29002361154409843200)),
}
C_SHP_HISTORICAL = F(-211835444920651, 4405310420659200)
RHO_ORBIT = F(238714892212171339, 29002361154409843200)
PI_ORBIT = F(-20535103905179, 1264270320593280)


def load(name, stage):
    """A stage's output: its own file, or the combined file an `all` run writes."""
    try:
        with open(HERE / f"pair_route_{name}_{stage}.json") as fh:
            return json.load(fh)
    except FileNotFoundError:
        if stage in ("gate", "dressing", "pair", "cube"):
            with open(HERE / f"pair_route_{name}_all.json") as fh:
                d = json.load(fh)
            if stage != "cube" or "cubes" in d:
                return d
        raise


def main():
    out = {"schema": "workhouse/shared-link-pair/v1", "pairs": {}}
    lattice = {}
    for name in ("normal", "coplanar", "perpendicular"):
        try:
            gate = load(name, "gate")
        except FileNotFoundError:
            gate = None
        try:
            dressing = load(name, "dressing")
            pair = load(name, "pair")
        except FileNotFoundError:
            print(f"== {name}: not complete yet")
            continue
        label, record = RECORDS[name]
        codd_pair = F(pair["pair_cluster"]["codd"])
        ceven_pair = F(pair["pair_cluster"]["ceven"])
        dress = {x: (F(d["codd"]), F(d["ceven"])) for x, d in dressing["dressings"].items()}
        s_odd = sum((v[0] for v in dress.values()), F(0))
        s_even = sum((v[1] for v in dress.values()), F(0))
        try:
            cube = load(name, "cube")
            cube_odd = F(cube["cube_sum_codd"])
            cube_even = sum((F(c["ceven"]) for c in cube["cubes"]), F(0))
        except FileNotFoundError:
            cube_odd, cube_even = F(0), F(0)
        total = codd_pair + s_odd + cube_odd
        lattice[name] = total
        by_value = {}
        for x, (v, _e) in dress.items():
            by_value.setdefault(str(v), []).append(x)
        print(f"== {name}: {label}")
        print(f"   pair cluster C-odd        {codd_pair} = {float(codd_pair):+.9e}")
        for v, xs in sorted(by_value.items(), key=lambda kv: -len(kv[1])):
            print(f"   {len(xs):2d} dressings at {v:>32s} = {float(F(v)):+.9e}  ({', '.join(xs[:2])}{', ...' if len(xs) > 2 else ''})")
        print(f"   dressing sum              {s_odd} = {float(s_odd):+.9e}")
        print(f"   cube completion           {cube_odd} = {float(cube_odd):+.9e}")
        print(f"   lattice element, C-odd    {total} = {float(total):+.9e}")
        print(f"   record                    {record} = {float(record):+.9e}")
        print(f"   difference                {total - record}   {'EXACT' if total == record else 'DIFFERS'}")
        out["pairs"][name] = {
            "faces": pair["faces"],
            "record_label": label,
            "record": str(record),
            "pair_cluster_codd": str(codd_pair),
            "pair_cluster_ceven": str(ceven_pair),
            "dressings": {x: {"codd": str(v), "ceven": str(e)} for x, (v, e) in dress.items()},
            "dressing_sum_codd": str(s_odd),
            "dressing_sum_ceven": str(s_even),
            "cube_completion_codd": str(cube_odd),
            "lattice_codd": str(total),
            "lattice_ceven": str(ceven_pair + s_even + cube_even),
            "equals_record": total == record,
            "gate_far_X_all_zero": bool(gate and all(F(v) == 0 for v in gate["gate_far_X"].values())),
        }
        try:
            blind = load(name, "pair_epsblind")
            b_odd = F(blind["pair_cluster"]["codd"])
            out["pairs"][name]["pair_cluster_codd_eps_blind"] = str(b_odd)
            out["pairs"][name]["eps_sector_codd"] = str(codd_pair - b_odd)
            print(f"   eps-blind pair cluster    {b_odd} = {float(b_odd):+.9e};  eps-sector {codd_pair - b_odd}")
        except FileNotFoundError:
            pass
    eps = {n: F(d["eps_sector_codd"]) for n, d in out["pairs"].items() if "eps_sector_codd" in d}
    if len(eps) == 2:
        # U5's prediction concerns rho + pi~ under a "direct balanced contraction":
        # the epsilon-blind assembly. The dressings carry no epsilon sector
        # (epsblind_dressing check), so the whole shift is the two pair clusters'.
        delta = -(eps["perpendicular"] + eps["coplanar"])  # blind minus full
        print("== the epsilon sector of rho + pi~ (epsilon-blind minus full)")
        print(f"   rho: {-eps['perpendicular']}, pi: {-eps['coplanar']}, sum {delta} = {float(delta):.9e}")
        print(f"   U5 predicted Delta(rho + pi~) = -25/512 = {float(F(-25, 512)):.9e}  {'MATCH' if delta == F(-25, 512) else 'FALSIFIED'}")
        out["eps_sector_delta_rho_plus_pi_reduced"] = str(delta)
        out["U5_predicted_delta"] = "-25/512"
        out["U5_prediction_holds"] = delta == F(-25, 512)
    if "perpendicular" in lattice and "coplanar" in lattice:
        rho, pi = lattice["perpendicular"], lattice["coplanar"]
        c_shp = F(-5, 96) - X_QUANTUM - (rho + pi) / 2
        print("== C_shp = -5/96 - u - (rho + pi)/2 from the computed amplitudes")
        print(f"   rho = {rho}, pi = {pi}")
        print(f"   C_shp = {c_shp} = {float(c_shp):.15f}")
        print(f"   historical C_shp = {C_SHP_HISTORICAL} = {float(C_SHP_HISTORICAL):.15f}  {'EXACT' if c_shp == C_SHP_HISTORICAL else 'DIFFERS'}")
        out["C_shp_from_computed_amplitudes"] = str(c_shp)
        out["C_shp_equals_historical"] = c_shp == C_SHP_HISTORICAL
    with open(HERE / "shared_link_pair_certificate.json", "w") as fh:
        json.dump(out, fh, indent=1)
        fh.write("\n")
    print("certificate written: shared_link_pair_certificate.json")


if __name__ == "__main__":
    main(*sys.argv[1:])
