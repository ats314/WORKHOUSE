"""Second-order validation of the block machinery, then a cost probe for the fourth order."""
import time
from fractions import Fraction as F
import cluster_pt as P
M = P.M

def second_order(cluster):
    e0 = cluster.e0; mw = cluster.words; m = len(mw)
    t0 = time.time()
    vs = [cluster.apply_V(d) for d in cluster.model]
    r = [P.resolvent(v, e0, mw) for v in vs]
    t1 = time.time()
    H2 = [[P.inner(vs[i], r[j]) for j in range(m)] for i in range(m)]
    t2 = time.time()
    print(f"    blocks={len(P._BLOCKS)} sizes={[b.n for b in P._BLOCKS.values()]} resolvent {t1-t0:.1f}s inner {t2-t1:.1f}s", flush=True)
    return H2, vs, r

single = P.Cluster([((0, 1), (0, 0, 0))])
H2s, _, _ = second_order(single)
print("single: C-odd diag", P.codd(H2s, 0, 0), " C-even diag", P.ceven(H2s, 0, 0), flush=True)
pair = P.Cluster([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))])
H2, vs, r = second_order(pair)
print("pair: C-odd hop", P.codd(H2, 0, 1), " (t_3 = 5/612 =", F(5, 612), ") C-even hop", P.ceven(H2, 0, 1), flush=True)
print("pair: C-odd connected diag (leakage per neighbour)", P.codd(H2, 0, 0) - P.codd(H2s, 0, 0), " (-11/306 =", F(-11, 306), ")", flush=True)
# perpendicular pair sharing a link: P in plane (0,1) at origin, Q in plane (0,2) at origin (shares the x-link at origin)
perp = P.Cluster([((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0))])
H2p, _, _ = second_order(perp)
print("perp pair: C-odd hop", P.codd(H2p, 0, 1), " C-even hop", P.ceven(H2p, 0, 1), flush=True)
# cost probe: words of V r_P on the pair, their degrees and one inner product each
vr = pair.apply_V(r[0])
print("V r_P words:", len(vr), flush=True)
from collections import Counter
for w in list(vr)[:40]:
    deg = Counter()
    for l, is_u in w.occ: deg[l] += 1
    mx = max(deg.values())
    t0 = time.time(); v = M.haar_inner(w, w); dt = time.time() - t0
    print(f"    occ={len(w.occ)} maxdeg={mx} <w|w> in {dt:.3f}s", flush=True)
