"""What displacements does the perpendicular cube OPERATOR carry, as opposed to
its carrier projection? The projection inherits psi's own displacement content,
so the two are not the same measurement."""
import sys
sys.path.insert(0, "/home/user/WORKHOUSE/src")
from collections import Counter

PLANES = [(1, 2), (1, 3), (2, 3)]
CUBE = [((0,0,0),(1,2),-1), ((0,0,1),(1,2),+1),
        ((0,0,0),(1,3),+1), ((0,1,0),(1,3),-1),
        ((0,0,0),(2,3),-1), ((1,0,0),(2,3),+1)]

def records(pairs):
    """Distinct (input plane, output plane, displacement) records."""
    out = {}
    for (xa, Pa, ea), (xb, Pb, eb) in pairs:
        delta = tuple(xb[i] - xa[i] for i in range(3))
        out[(Pa, Pb, delta)] = out.get((Pa, Pb, delta), 0) + ea * eb
    return out

cross = [(f, g) for f in CUBE for g in CUBE if f[1] != g[1]]
same  = [(f, g) for f in CUBE for g in CUBE if f is not g and f[1] == g[1]]

for label, pairs in (("PERPENDICULAR", cross), ("NORMAL", same)):
    rec = records(pairs)
    shells = Counter(tuple(sorted(abs(c) for c in d)) for (_, _, d) in rec)
    print(f"{label}: {len(rec)} distinct (plane_in, plane_out, displacement) records")
    for shell, n in sorted(shells.items()):
        print(f"    shell {shell}: {n} records")
    print(f"    max |component| = {max(max(abs(c) for c in d) for (_,_,d) in rec)}")
    print()

print("the ledger's own block census, for comparison:")
for name, n in (("on-site (0,0,0)", 3), ("NORMAL (0,0,1)", 6), ("IN-PLANE (0,0,1)", 12),
                ("IN-PLANE (0,0,2)", 12), ("IN-PLANE (0,1,1)", 12), ("MIXED (0,1,1)", 24),
                ("ROTATION (all)", 120)):
    print(f"    {name:20s} {n:3d}")
print(f"    {'total':20s} {3+6+12+12+12+24+120:3d}")
