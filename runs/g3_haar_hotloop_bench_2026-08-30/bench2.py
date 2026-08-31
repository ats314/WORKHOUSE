"""Benchmark the exact Haar contraction on BALANCED states (nonzero integrals)."""
import sys, time, cProfile, pstats, io
sys.path.insert(0, "/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src")
import DATA_SU3_Exact_MarkedCluster_m4_Colab as M


def plaquette(links, orient=(1, 1, -1, -1)):
    return M.trace_state(tuple(zip(links, orient, strict=True)))


def word(*plaqs):
    s = plaqs[0]
    for p in plaqs[1:]:
        s = M.tensor_product(s, p)
    return s


P1 = plaquette((0, 1, 2, 3))
P2 = plaquette((3, 4, 5, 6))    # shares link 3 with P1
P3 = plaquette((6, 7, 8, 9))    # shares link 6 with P2

# <w|w>: the bra conjugates, so every link is balanced. Repeating a face
# raises that link's Haar degree, which is what drives the cost: degree d
# contributes d!^2 (sigma, tau) terms per link.
CASES = [
    ("deg1 x4 links   (P1)",          word(P1)),
    ("deg2 on 1 link  (P1,P2)",       word(P1, P2)),
    ("deg2 on 2 links (P1,P2,P3)",    word(P1, P2, P3)),
    ("deg2 x4 links   (P1,P1)",       word(P1, P1)),
    ("deg3 x4 links   (P1,P1,P1)",    word(P1, P1, P1)),
    ("deg3 + deg2     (P1,P1,P1,P2)", word(P1, P1, P1, P2)),
]

results = []
for name, w in CASES:
    M._HAAR_CACHE.clear()
    occ, part = M.combine_bra_ket(w, w)
    t0 = time.time()
    val = M.haar_inner(w, w)
    dt = time.time() - t0
    print(f"{name:32s} occ={len(occ):3d} part={len(part):3d}  {dt:9.3f}s  value={val}")
    results.append((name, w, dt))
    if dt > 120:
        break

# profile the largest case that took measurable time
name, w, dt = max(results, key=lambda r: r[2])
M._HAAR_CACHE.clear()
pr = cProfile.Profile(); pr.enable()
M.haar_inner(w, w)
pr.disable()
s = io.StringIO()
pstats.Stats(pr, stream=s).sort_stats("tottime").print_stats(14)
print(f"\n=== profile: {name} ({dt:.2f}s) ===")
print("\n".join(s.getvalue().splitlines()[:26]))
