import sys, cProfile, pstats, io
sys.path.insert(0, "/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src")
import DATA_SU3_Exact_MarkedCluster_m4_Colab as M

def plaquette(links, orient=(1, 1, -1, -1)):
    return M.trace_state(tuple(zip(links, orient, strict=True)))
P1 = plaquette((0, 1, 2, 3))
w = M.tensor_product(M.tensor_product(P1, P1), P1)

M._HAAR_CACHE.clear()
pr = cProfile.Profile(); pr.enable()
M.haar_inner(w, w)
pr.disable()
s = io.StringIO()
pstats.Stats(pr, stream=s).sort_stats("tottime").print_stats(16)
print("\n".join(s.getvalue().splitlines()[:28]))
