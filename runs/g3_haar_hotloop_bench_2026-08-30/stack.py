"""Both accelerations at once, against the pinned engine's own answer."""
import sys, time
from fractions import Fraction
sys.path.insert(0, "/home/user/WORKHOUSE/src/workhouse/_haarcore")
sys.path.insert(0, "/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src")
import flint, _haarcore
import DATA_SU3_Exact_MarkedCluster_m4_Colab as M

def plaq(l, o=(1, 1, -1, -1)): return M.trace_state(tuple(zip(l, o, strict=True)))
def word(*ps):
    s = ps[0]
    for p in ps[1:]: s = M.tensor_product(s, p)
    return s
P1, P2, P3 = plaq((0,1,2,3)), plaq((3,4,5,6)), plaq((6,7,8,9))
Q1 = plaq((20,21,22,23))
CASES = [("deg2 x4  (P1^2)", word(P1,P1)),
         ("deg2 x2L (P1,P2,P3)", word(P1,P2,P3)),
         ("deg3 x4  (P1^3)", word(P1,P1,P1)),
         ("deg3 x8  (P1^3,Q1^3)", word(P1,P1,P1,Q1,Q1,Q1))]

PY_MERGE, PY_FRAC, PY_WG = M.merge_classes, M.Fraction, M.balanced_weingarten

def _wg_fmpq(degree, _cache={}):
    # The engine builds its Weingarten inverse-Gram in Fraction at import time,
    # so swapping the arithmetic type means converting the tables too. That is
    # the point at which a hot-loop swap stops being a drop-in.
    if degree not in _cache:
        perms, inv = PY_WG(degree)
        _cache[degree] = (perms, tuple(tuple(flint.fmpq(x.numerator, x.denominator)
                                             for x in row) for row in inv))
    return _cache[degree]

def run(w, merge, frac):
    M.merge_classes, M.Fraction = merge, frac
    M.balanced_weingarten = _wg_fmpq if frac is flint.fmpq else PY_WG
    M._HAAR_CACHE.clear()
    t0 = time.time(); v = M.haar_inner(w, w); return time.time() - t0, v

print(f"{'case':24s} {'baseline':>10s} {'+C':>9s} {'+C+flint':>10s} {'total':>8s}  exact?")
for name, w in CASES:
    t_c, v_c = run(w, _haarcore.merge_classes, PY_FRAC)
    t_cf, v_cf = run(w, _haarcore.merge_classes, flint.fmpq)
    if t_c > 120:
        print(f"{name:24s} {'(skipped)':>10s} {t_c:8.2f}s {t_cf:9.2f}s {t_c/t_cf:7.1f}x  {Fraction(int(v_cf.p),int(v_cf.q)) == v_c}")
        continue
    t_b, v_b = run(w, PY_MERGE, PY_FRAC)
    ok = v_b == v_c and Fraction(int(v_cf.p), int(v_cf.q)) == v_b
    print(f"{name:24s} {t_b:9.3f}s {t_c:8.3f}s {t_cf:9.3f}s {t_b/max(t_cf,1e-9):7.1f}x  {ok} (value {v_b})")
M.merge_classes, M.Fraction, M.balanced_weingarten = PY_MERGE, PY_FRAC, PY_WG
