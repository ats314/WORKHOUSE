"""The odd orders of the band are determinant families: the third order at N = 3..7 and over Q(N).

Runs the third engine's des Cloizeaux operator through third order
(``workhouse.invariants.odd_order.effective``) on the single plaquette and on
the coplanar and perpendicular shared-link pairs at N = 3, 4, 6, 7; at N = 5,
where the five-word determinant families of the one-plaquette histories are
too expensive for the word engine, the pair hops and X-touched leakages
(``pair_third_cheap``, which never meets them) and the towers and vacuum from
the one-plaquette character engine (``towers``). Also: the character engine at
N = 3..11 through seventh order, the third-order pair hops over Q(N), the
closed form of the first odd-order vertex for odd N, the centre-parity link
set on finite blocks, and the theorem's criterion tabulated. Writes
certificate.json next to itself. Every number is an exact rational.
"""

from __future__ import annotations

import json
import sys
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from workhouse import loopcalc as LC  # noqa: E402
from workhouse import symbolic_rank as SR  # noqa: E402
from workhouse.invariants import odd_order as OO  # noqa: E402

HERE = Path(__file__).resolve().parent


def s(x):
    return str(Fraction(x)) if not hasattr(x, "to_sympy") else str(x.to_sympy())


def show(title, row):
    print(f"{title}:", flush=True)
    for k, v in row.items():
        print(f"  {k} = {v}", flush=True)


def main() -> None:
    cert = {"ranks": {}, "characters": {}, "timing_s": {}}
    for n in (3, 4, 6, 7):
        t = time.time()
        LC.set_rank(n)
        row = OO.band_numbers(n)
        LC.set_rank(3)
        cert["ranks"][str(n)] = {k: s(v) for k, v in row.items()}
        cert["timing_s"][str(n)] = round(time.time() - t, 1)
        show(f"N = {n}, loopcalc ({cert['timing_s'][str(n)]} s)", row)
    t = time.time()
    LC.set_rank(5)
    row = {}
    for pair in ("coplanar", "perpendicular"):
        cheap = OO.pair_third_cheap(OO._CLUSTERS[pair])
        for k, v in cheap.items():
            row[k.replace("3_", f"3_{pair}_", 1)] = v
    LC.set_rank(3)
    for k, v in OO.towers(5, 3).items():
        row[k] = v
    cert["ranks"]["5"] = {k: s(v) for k, v in row.items()}
    cert["ranks"]["5"]["method"] = (
        "hops and X-touched leakages by loopcalc (pair_third_cheap); towers and vacuum by the "
        "character engine (towers), the five-word determinant families being too expensive for "
        "the word engine"
    )
    cert["timing_s"]["5"] = round(time.time() - t, 1)
    show(f"N = 5, cheap loopcalc + characters ({cert['timing_s']['5']} s)", row)
    t = time.time()
    for n in range(3, 12):
        cert["characters"][str(n)] = {k: s(v) for k, v in OO.towers(n, 7).items()}
    cert["timing_s"]["characters"] = round(time.time() - t, 1)
    print("characters N = 3..11 through order 7:", flush=True)
    for n, row in cert["characters"].items():
        print(f"  N = {n}: " + ", ".join(f"{k} = {v}" for k, v in row.items()), flush=True)
    t = time.time()
    with SR.Symbolic() as S:
        hops = {}
        for pair in ("coplanar", "perpendicular"):
            cl = LC.Cluster(OO._CLUSTERS[pair])
            for a in (2, 3):
                ket = cl.V(cl.R(cl.V(cl.R(cl.V({cl.words[a]: LC.F(1)})))))
                for b in (0, 1):
                    hops[f"{pair}[{b},{a}]"] = s(LC.inner(cl.words[b], ket))
    cert["symbolic_third_order_hops"] = hops
    cert["symbolic_stats"] = {
        "components_verified": S.stats["components_verified"],
        "max_weingarten_n": S.stats["max_weingarten_n"],
        "max_charge": S.stats["max_charge"],
        "energies": sorted(str(e.to_sympy()) for e in S.stats["energies"]),
    }
    cert["timing_s"]["symbolic"] = round(time.time() - t, 1)
    print("symbolic:", hops, cert["symbolic_stats"], flush=True)
    cert["first_odd_vertex"] = {str(n): s(OO.first_odd_vertex(n)) for n in (3, 5, 7, 9, 11, 13)}
    cert["parity_links"] = {str(b): list(OO.parity_links(b)) for b in (2, 3, 4, 5, 6)}
    cert["criterion"] = {
        f"N={n}": [m for m in range(1, 16) if OO.odd_order_survives(n, m) and m % 2 == 1]
        for n in range(3, 14)
    }
    print("first odd vertex:", cert["first_odd_vertex"], flush=True)
    print("parity links:", cert["parity_links"], flush=True)
    print("odd orders left open by the theorem:", cert["criterion"], flush=True)
    (HERE / "certificate.json").write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
