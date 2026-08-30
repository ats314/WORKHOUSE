"""Closed lattice boxes tiled by UNIT squares, so face pairs can be classified
geometrically (normal, displacement) rather than combinatorially."""
import sys
sys.path.insert(0, "/home/user/WORKHOUSE/src")
from workhouse import cellular as CELL

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
def add(u, v): return tuple(a + b for a, b in zip(u, v))

def unit_faces_of_box(L):
    """Outward-oriented unit squares tiling the surface of the box [0,L1]x[0,L2]x[0,L3].

    Returns [(vertex_cycle, normal_axis, outward_sign, base_corner), ...].
    """
    faces = []
    for n in range(3):
        i, j = (n + 1) % 3, (n + 2) % 3          # e_i x e_j = e_n
        for side, lo in ((+1, L[n]), (-1, 0)):
            for u in range(L[i]):
                for v in range(L[j]):
                    base = [0, 0, 0]
                    base[n], base[i], base[j] = lo, u, v
                    base = tuple(base)
                    cyc = (base, add(base, E[i]), add(add(base, E[i]), E[j]), add(base, E[j]))
                    if side < 0:                  # inward normal -> reverse
                        cyc = (cyc[0], cyc[3], cyc[2], cyc[1])
                    faces.append((cyc, n, side, base))
    return faces

def cell_from_box(name, L):
    faces = unit_faces_of_box(L)
    return CELL.Cell(name, tuple(f[0] for f in faces)), faces

for name, L in (("unit cube", (1, 1, 1)), ("1x2x1 box", (1, 2, 1)), ("1x1x2 box", (1, 1, 2))):
    try:
        cell, meta = cell_from_box(name, L)
    except ValueError as exc:
        print(f"{name:12s} INVALID: {exc}")
        continue
    r = len(cell.faces) - 2
    coplanar = [
        (a, b)
        for a in range(len(meta)) for b in range(a + 1, len(meta))
        if meta[a][1] == meta[b][1] and meta[a][2] == meta[b][2]        # same normal AND same side
        and len({frozenset(e) for e in CELL._face_edges(cell.faces[a])}
                & {frozenset(e) for e in CELL._face_edges(cell.faces[b])}) == 1
    ]
    print(f"{name:12s} VALID closed cell: {len(cell.faces):2d} unit faces, r = {r}, "
          f"coplanar edge-sharing pairs: {len(coplanar)}")
