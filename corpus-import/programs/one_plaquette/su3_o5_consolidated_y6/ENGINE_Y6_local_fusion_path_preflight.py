#!/usr/bin/env python3
"""Universal SU(3) local fusion-path census for six-insertion (8-event) links."""
from __future__ import annotations

import itertools
import json
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

EVENTS = (
    "ket",
    "insertion_1",
    "insertion_2",
    "insertion_3",
    "insertion_4",
    "insertion_5",
    "insertion_6",
    "bra",
)


@lru_cache(None)
def fuse_f(ir):
    p, q = ir
    out = [(p + 1, q)]
    if p > 0:
        out.append((p - 1, q + 1))
    if q > 0:
        out.append((p, q - 1))
    return tuple(out)


@lru_cache(None)
def fuse_a(ir):
    p, q = ir
    out = [(p, q + 1)]
    if q > 0:
        out.append((p + 1, q - 1))
    if p > 0:
        out.append((p - 1, q))
    return tuple(out)


def fuse(ir, token):
    if token == 0:
        return (ir,)
    return fuse_f(ir) if token == 1 else fuse_a(ir)


def dim(ir):
    p, q = ir
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def c2_num(ir):
    p, q = ir
    return p * p + q * q + p * q + 3 * p + 3 * q


@lru_cache(None)
def fusion_paths(signature):
    paths = [((0, 0),)]
    for token in signature:
        nxt = []
        for path in paths:
            for ir in fuse(path[-1], token):
                nxt.append(path + (ir,))
        paths = nxt
    return tuple(path for path in paths if path[-1] == (0, 0))


def canonical_sector(nf, na):
    return tuple(sorted((nf, na)))


def main():
    records = []
    sector_counts = Counter()
    sector_signature_counts = Counter()
    degree_hist = Counter()
    path_count_hist = Counter()
    max_path_count = 0
    max_irrep_dim = 1
    max_c2_num = 0
    feasible = 0

    representative_by_sector = {}
    for sig in itertools.product((-1, 0, 1), repeat=8):
        if not any(sig):
            continue
        paths = fusion_paths(sig)
        if not paths:
            continue
        feasible += 1
        nf = sig.count(1)
        na = sig.count(-1)
        degree = nf + na
        sector = canonical_sector(nf, na)
        count = len(paths)
        sector_signature_counts[sector] += 1
        sector_counts[(sector, count)] += 1
        degree_hist[degree] += 1
        path_count_hist[count] += 1
        max_path_count = max(max_path_count, count)
        for path in paths:
            max_irrep_dim = max(max_irrep_dim, *(dim(ir) for ir in path))
            max_c2_num = max(max_c2_num, *(c2_num(ir) for ir in path))
        representative_by_sector.setdefault(
            sector,
            {
                "signature": list(sig),
                "path_count": count,
                "first_path": [list(ir) for ir in paths[0]],
                "intermediate_E6": [c2_num(paths[0][i]) for i in range(2, 7)],
            },
        )
        records.append((sig, count, sector))

    sectors = []
    for sector in sorted(sector_signature_counts):
        nf, na = sector
        multiplicities = sorted(
            {
                count
                for (sec, count), occurrences in sector_counts.items()
                if sec == sector and occurrences
            }
        )
        determinant_number = abs(na - nf) // 3
        sectors.append(
            {
                "canonical_nfund_nantifund": [nf, na],
                "degree": nf + na,
                "triality_difference": na - nf,
                "determinant_number": determinant_number,
                "signature_count": sector_signature_counts[sector],
                "singlet_multiplicities": multiplicities,
                "representative": representative_by_sector[sector],
            }
        )

    expected_new = {(0, 6), (1, 7), (4, 4)}
    found = {tuple(x["canonical_nfund_nantifund"]) for x in sectors}
    gates = {
        "all_feasible_signatures_have_triality_zero": all(
            (sig.count(1) - sig.count(-1)) % 3 == 0 for sig, _, _ in records
        ),
        "balanced_degree_eight_sector_present": (4, 4) in found,
        "double_determinant_0_6_sector_present": (0, 6) in found,
        "double_determinant_1_7_sector_present": (1, 7) in found,
        "all_expected_new_sectors_present": expected_new <= found,
        "path_basis_nonempty_for_every_record": all(count > 0 for _, count, _ in records),
    }

    payload = {
        "status": "PASS" if all(gates.values()) else "FAIL",
        "events": list(EVENTS),
        "universal_signature_space": 3**8 - 1,
        "feasible_nonzero_signatures": feasible,
        "gates": gates,
        "degree_histogram": dict(sorted(degree_hist.items())),
        "path_count_histogram": dict(sorted(path_count_hist.items())),
        "max_singlet_path_count": max_path_count,
        "max_intermediate_irrep_dimension": max_irrep_dim,
        "max_intermediate_C2_num_over_3": max_c2_num,
        "sectors": sectors,
        "interpretation": (
            "The fusion-path carrier basis automatically includes balanced, single-determinant, "
            "and double-determinant sectors. Explicit normalized edge tensors and projector "
            "matrices remain to be constructed only for signatures realized by the sixth-order geometry."
        ),
    }
    out = Path(__file__).with_name("CERT_Y6_local_fusion_path_preflight_certificate.json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    for name, value in gates.items():
        print(("PASS" if value else "FAIL"), name)
    print("feasible signatures", feasible)
    print("sectors", [x["canonical_nfund_nantifund"] for x in sectors])
    print("max singlet paths", max_path_count)
    print("max irrep dimension", max_irrep_dim)
    print("CERTIFICATE", out)
    print("ALL Y6 LOCAL FUSION-PATH PREFLIGHT GATES PASS" if all(gates.values()) else "Y6 LOCAL PREFLIGHT FAILED")
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
