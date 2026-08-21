#!/usr/bin/env python3
"""
Exact/global O(y^4) band-edge certificate for the SU(3) T1^{+-} branch.

Notebook-safe, no manual edits. It:
  1. finds/extracts DATA_Y4_full_real_space_h4_kernel.json.gz;
  2. binds orientation indices to meta['basis_planes'] (never a hard-coded reordered basis);
  3. constructs the projected fourth-order numerator exactly as a Laurent polynomial;
  4. proves the exact Gamma value and computes all high-symmetry values from the kernel;
  5. reduces the global min/max claims to two real trigonometric-polynomial inequalities;
  6. derives rigorous local Taylor certificates at Gamma (and R for the upper edge);
  7. uses interval branch-and-bound on the remaining Brillouin zone;
  8. writes JSON/Markdown certificate artifacts.

The key identity is
    c4(k) = N(k)/D(k),
where D(k)=||psi(k)||^2 >= 0 and psi is the cube-boundary flat vector. Therefore
    c4(k) >= cG  <=>  Qmin(k)=N(k)-cG*D(k) >= 0,
    c4(k) <= cR  <=>  Qmax(k)=cR*D(k)-N(k) >= 0.
Both Q's are finite exact trigonometric polynomials, avoiding division near Gamma.
"""

from __future__ import annotations

import gzip
import hashlib
import itertools
import json
import math
import os
import sys
import time
import zipfile
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
from mpmath import iv
import sympy as sp

# ------------------------------- configuration -------------------------------
IV_DPS = 45
MAX_BOXES_PER_CLAIM = 750_000
MAX_DEPTH = 34
INITIAL_SPLITS = 4
REPORT_EVERY = 25_000
OUTDIR = Path("/content/Y4_GLOBAL_BAND_CERT") if Path("/content").exists() else Path("/mnt/data/Y4_GLOBAL_BAND_CERT_FINAL")
OUTDIR.mkdir(parents=True, exist_ok=True)

mp.mp.dps = IV_DPS
iv.dps = IV_DPS

ZERO = (0, 0, 0)
KNOWN_GAMMA = F(-20721577909065127111, 7250590288602460800)
KNOWN_X = F(-17700498622147435111, 7250590288602460800)
KNOWN_M = F(-4367164159624988707, 1812647572150615200)
KNOWN_R = F(-3447362930970494909, 1450118057720492160)


def gate(name: str, cond: bool, detail: str = "") -> None:
    print(f"{'PASS' if cond else 'FAIL':4s} {name:48s} {detail}")
    if not cond:
        raise AssertionError(f"{name}: {detail}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def find_kernel() -> Path:
    fn = "DATA_Y4_full_real_space_h4_kernel.json.gz"
    explicit = os.environ.get("Y4_KERNEL")
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit))
    for a in sys.argv[1:]:
        if a.endswith((".json.gz", ".gz")):
            candidates.append(Path(a))
    candidates += [
        Path("/content") / fn,
        Path.cwd() / fn,
        Path("/mnt/data") / fn,
        Path("/content/Y4_FINAL_ARCHIVE_2026-06-13/certificates") / fn,
    ]

    # Extract likely Colab archives automatically.
    archives = [
        Path("/content/Y4_FINAL_ARCHIVE_2026-06-13.zip"),
        Path("/content/Y4_FINAL_ARCHIVE_2026-06-13"),
    ]
    for z in archives:
        if z.is_file() and z.suffix.lower() == ".zip":
            target = Path("/content/Y4_FINAL_ARCHIVE_2026-06-13")
            if not target.exists():
                print("Extracting", z)
                with zipfile.ZipFile(z) as zh:
                    zh.extractall("/content")

    for root in [Path("/content"), Path("/mnt/data"), Path.cwd()]:
        if root.exists():
            candidates.extend(root.glob(f"**/{fn}"))
    seen = set()
    for p in candidates:
        try:
            p = p.resolve()
        except Exception:
            pass
        if str(p) in seen:
            continue
        seen.add(str(p))
        if p.is_file():
            return p
    raise FileNotFoundError(
        f"Could not find {fn}. The uploaded notebook contains recovery code but not the 189 records. "
        "Place the kernel or Y4_FINAL_ARCHIVE_2026-06-13.zip in /content and rerun this one block."
    )


# ------------------------------- exact polynomials ----------------------------
Poly = dict[tuple[int, int, int], F]


def pclean(p: Poly) -> Poly:
    return {e: c for e, c in p.items() if c}


def padd(a: Poly, b: Poly, scale: F = F(1)) -> Poly:
    out = defaultdict(F)
    out.update(a)
    for e, c in b.items():
        out[e] += scale * c
    return pclean(dict(out))


def pscale(a: Poly, s: F) -> Poly:
    return pclean({e: s * c for e, c in a.items()})


def pmul(a: Poly, b: Poly) -> Poly:
    out = defaultdict(F)
    for ea, ca in a.items():
        for eb, cb in b.items():
            out[(ea[0] + eb[0], ea[1] + eb[1], ea[2] + eb[2])] += ca * cb
    return pclean(dict(out))


def pconj_torus(a: Poly) -> Poly:
    return {(-e[0], -e[1], -e[2]): c for e, c in a.items()}


def peval_sign(a: Poly, signs: tuple[int, int, int]) -> F:
    total = F(0)
    for e, c in a.items():
        phase = 1
        for i in range(3):
            if signs[i] == -1 and (e[i] & 1):
                phase = -phase
        total += c * phase
    return total


def exact_matrix_at_sign(H: list[list[Poly]], signs: tuple[int, int, int]) -> list[list[F]]:
    return [[peval_sign(H[i][j], signs) for j in range(3)] for i in range(3)]


def canonical_pair(e: tuple[int, int, int]) -> bool:
    ne = (-e[0], -e[1], -e[2])
    return e > ne


def cosine_terms(q: Poly) -> tuple[F, list[tuple[tuple[int, int, int], F]]]:
    # q(k)=const + sum A_r cos(r.k), requiring q_r=q_-r exactly.
    inversion_ok = all(q.get((-e[0], -e[1], -e[2]), F(0)) == c for e, c in q.items())
    gate("Laurent coefficient inversion symmetry", inversion_ok, f"terms={len(q)}")
    const = q.get(ZERO, F(0))
    terms = []
    for e, c in sorted(q.items()):
        if e != ZERO and canonical_pair(e):
            terms.append((e, 2 * c))
    return const, terms


def trig_eval_exact_at_parity(const: F, terms, parity: tuple[int, int, int]) -> F:
    out = const
    for r, a in terms:
        out += a * ((-1) ** sum(r[i] * parity[i] for i in range(3)))
    return out


def frac_sp(x: F) -> sp.Rational:
    return sp.Rational(x.numerator, x.denominator)


def frac_iv(x: F):
    return iv.mpf(x.numerator) / iv.mpf(x.denominator)


def frac_mp(x: F):
    return mp.mpf(x.numerator) / mp.mpf(x.denominator)


# ------------------------------- load kernel ----------------------------------
KPATH = find_kernel()
print("Using kernel:", KPATH)
with gzip.open(KPATH, "rt", encoding="utf-8") as f:
    payload = json.load(f)
records = payload["kernel"]
meta = payload.get("meta", {})
gate("kernel record count", len(records) == 189, str(len(records)))

basis_raw = meta.get("basis_planes")
gate("metadata basis_planes exists", isinstance(basis_raw, list) and len(basis_raw) == 3, repr(basis_raw))
basis = [tuple(int(x) for x in p) for p in basis_raw]
gate("canonical kernel basis order", basis == [(0, 1), (0, 2), (1, 2)], repr(basis))
plane_to_index = {frozenset(p): i for i, p in enumerate(basis)}

H: list[list[Poly]] = [[{} for _ in range(3)] for __ in range(3)]
raw_sparse: dict[tuple[int, int, tuple[int, int, int]], F] = {}
for rec in records:
    a = plane_to_index[frozenset(int(x) for x in rec["input_plane"])]
    b = plane_to_index[frozenset(int(x) for x in rec["output_plane"])]
    r = tuple(int(x) for x in rec["displacement"])
    w = F(str(rec["weight"]))
    # H row=output, column=input, matching the verified ENGINE_Y4_band_structure.py.
    H[b][a][r] = H[b][a].get(r, F(0)) + w
    raw_sparse[(b, a, r)] = raw_sparse.get((b, a, r), F(0)) + w

herm = all(raw_sparse.get((a, b, (-r[0], -r[1], -r[2])), F(0)) == w
           for (b, a, r), w in raw_sparse.items())
gate("exact real-space Hermiticity", herm)

# Exact H4(Gamma).
HG = exact_matrix_at_sign(H, (1, 1, 1))
gate("H4(Gamma) off-diagonal zero", all(HG[i][j] == 0 for i in range(3) for j in range(3) if i != j))
gate("H4(Gamma) scalar", HG[0][0] == HG[1][1] == HG[2][2])
cG = HG[0][0]
gate("Gamma coefficient anchor", cG == KNOWN_GAMMA, str(cG))

# Flat cube-boundary vector in metadata order [xy,xz,yz].
zx = {(1, 0, 0): F(1)}
zy = {(0, 1, 0): F(1)}
zz = {(0, 0, 1): F(1)}
one = {ZERO: F(1)}
psi = [padd(zz, one, F(-1)), padd(one, zy, F(-1)), padd(zx, one, F(-1))]
barpsi = [pconj_torus(p) for p in psi]

N: Poly = {}
for i in range(3):
    for j in range(3):
        N = padd(N, pmul(pmul(barpsi[i], H[i][j]), psi[j]))
D: Poly = {}
for i in range(3):
    D = padd(D, pmul(barpsi[i], psi[i]))

# High-symmetry coefficients are computed, not inserted.
def c_at_sign(signs):
    den = peval_sign(D, signs)
    gate("nonzero projected denominator", den != 0, f"signs={signs}")
    return peval_sign(N, signs) / den

cX = c_at_sign((-1, 1, 1))
cM = c_at_sign((-1, -1, 1))
cR = c_at_sign((-1, -1, -1))
gate("X coefficient anchor", cX == KNOWN_X, str(cX))
gate("M coefficient anchor", cM == KNOWN_M, str(cM))
gate("R coefficient anchor", cR == KNOWN_R, str(cR))

QMIN = padd(N, pscale(D, cG), F(-1))
QMAX = padd(pscale(D, cR), N, F(-1))
min_const, min_terms = cosine_terms(QMIN)
max_const, max_terms = cosine_terms(QMAX)
print(f"Exact Laurent terms: N={len(N)}, D={len(D)}, Qmin={len(QMIN)}, Qmax={len(QMAX)}")
print(f"Cosine terms: Qmin={len(min_terms)}, Qmax={len(max_terms)}")

gate("Qmin(Gamma)=0", trig_eval_exact_at_parity(min_const, min_terms, (0, 0, 0)) == 0)
gate("Qmax(Gamma)=0", trig_eval_exact_at_parity(max_const, max_terms, (0, 0, 0)) == 0)
gate("Qmax(R)=0", trig_eval_exact_at_parity(max_const, max_terms, (1, 1, 1)) == 0)

# Reflection and permutation checks determine the rigorous search domain.
def transform_exp(e, perm=(0, 1, 2), flips=(1, 1, 1)):
    x = (e[perm[0]], e[perm[1]], e[perm[2]])
    return tuple(flips[i] * x[i] for i in range(3))


def invariant_under(q: Poly, perm=(0, 1, 2), flips=(1, 1, 1)):
    return all(q.get(transform_exp(e, perm, flips), F(0)) == c for e, c in q.items())

all_reflections = all(invariant_under(QMIN, flips=f) and invariant_under(QMAX, flips=f)
                      for f in itertools.product((-1, 1), repeat=3))
all_permutations = all(invariant_under(QMIN, perm=p) and invariant_under(QMAX, perm=p)
                       for p in itertools.permutations(range(3)))
gate("independent momentum-reflection symmetry", all_reflections)
gate("coordinate-permutation symmetry", all_permutations)

# ------------------------------- basis-correct numerical reconnaissance -------
def peval_numeric(poly: Poly, k):
    out = 0.0j
    for e, c in poly.items():
        phase = e[0] * k[0] + e[1] * k[1] + e[2] * k[2]
        out += float(c) * complex(math.cos(phase), math.sin(phase))
    return out


def peval_mp(poly: Poly, k):
    out = mp.mpc(0)
    kk = tuple(mp.mpf(str(v)) for v in k)
    for e, c in poly.items():
        phase = sum(mp.mpf(e[i]) * kk[i] for i in range(3))
        out += frac_mp(c) * mp.e**(1j * phase)
    return out


def c_numeric(k):
    den = peval_numeric(D, k).real
    if abs(den) < 1e-20:
        return float(cG)
    # N and D both vanish at Gamma.  Direct double-precision division is
    # ill-conditioned there, so switch to 80-digit evaluation before taking
    # the quotient.  This avoids false sub-Gamma minima from cancellation.
    if abs(den) < 1e-5:
        den_mp = peval_mp(D, k).real
        if abs(den_mp) < mp.mpf('1e-60'):
            return float(cG)
        val_mp = peval_mp(N, k) / den_mp
        if abs(val_mp.imag) > mp.mpf('1e-35'):
            raise AssertionError(f"projected coefficient not real at k={k}: {val_mp}")
        return float(val_mp.real)
    val = peval_numeric(N, k) / den
    if abs(val.imag) > 2e-9:
        raise AssertionError(f"projected coefficient not real at k={k}: {val}")
    return float(val.real)

SCAN_G = 33
scan_min = (float(cG), (0.0, 0.0, 0.0))
scan_max = (-float("inf"), None)
for i, j, l in itertools.product(range(SCAN_G), repeat=3):
    k = (math.pi * i / (SCAN_G - 1), math.pi * j / (SCAN_G - 1), math.pi * l / (SCAN_G - 1))
    v = c_numeric(k)
    if v < scan_min[0]:
        scan_min = (v, k)
    if v > scan_max[0]:
        scan_max = (v, k)

refined_min, refined_max = scan_min, scan_max
try:
    from scipy.optimize import minimize
    bnds = [(0.0, math.pi)] * 3
    rmin = minimize(lambda q: c_numeric(q), scan_min[1], method="Nelder-Mead",
                    options={"maxiter": 3000, "xatol": 1e-12, "fatol": 1e-13})
    rmax = minimize(lambda q: -c_numeric(q), scan_max[1], method="Nelder-Mead",
                    options={"maxiter": 3000, "xatol": 1e-12, "fatol": 1e-13})
    refined_min = (float(rmin.fun), tuple(float(v) for v in rmin.x))
    refined_max = (-float(rmax.fun), tuple(float(v) for v in rmax.x))
except Exception as exc:
    print("SciPy refinement unavailable:", repr(exc))

print("\nBASIS-CORRECT NUMERICAL RECONNAISSANCE")
print("scan/refined minimum:", refined_min)
print("scan/refined maximum:", refined_max)
print("Gamma candidate:", float(cG), "R candidate:", float(cR))
MIN_CANDIDATE_SURVIVES = refined_min[0] >= float(cG) - 2e-9
MAX_CANDIDATE_SURVIVES = refined_max[0] <= float(cR) + 2e-9
gate("numerical scan does not falsify Gamma minimum", MIN_CANDIDATE_SURVIVES, repr(refined_min))
if not MAX_CANDIDATE_SURVIVES:
    print("FAIL numerical scan falsifies R as global maximum:", refined_max)
else:
    print("PASS numerical scan does not falsify R maximum", refined_max)

# ------------------------------- exact Taylor data ----------------------------
x, y, z = sp.symbols("x y z", real=True)
vars3 = (x, y, z)


def taylor_data(const: F, terms, center_parity: tuple[int, int, int]):
    q0 = frac_sp(const)
    q2 = sp.Integer(0)
    q4 = sp.Integer(0)
    for r, a in terms:
        sgn = (-1) ** sum(r[i] * center_parity[i] for i in range(3))
        aa = frac_sp(a * sgn)
        lin = sum(sp.Integer(r[i]) * vars3[i] for i in range(3))
        q0 += aa
        q2 += -aa * lin**2 / 2
        q4 += aa * lin**4 / 24
    return sp.factor(q0), sp.Poly(sp.expand(q2), *vars3), sp.Poly(sp.expand(q4), *vars3)


def isotropic_quadratic_lambda(poly: sp.Poly) -> sp.Rational:
    expr = poly.as_expr()
    diag = [sp.expand(expr).coeff(v, 2).subs({w: 0 for w in vars3 if w != v}) for v in vars3]
    # More robust coefficient extraction.
    diag = [poly.coeff_monomial(v**2) for v in vars3]
    off = [poly.coeff_monomial(vars3[i] * vars3[j]) for i in range(3) for j in range(i + 1, 3)]
    gate("quadratic off-diagonal coefficients zero", all(v == 0 for v in off), repr(off))
    gate("quadratic isotropy", diag[0] == diag[1] == diag[2], repr(diag))
    gate("quadratic local positivity", diag[0] > 0, str(diag[0]))
    return sp.factor(diag[0])


def cubic_quartic_lambda(poly: sp.Poly) -> sp.Rational:
    allowed = {(4, 0, 0), (0, 4, 0), (0, 0, 4), (2, 2, 0), (2, 0, 2), (0, 2, 2)}
    bad = [(m, c) for m, c in poly.terms() if m not in allowed and c != 0]
    gate("quartic contains only cubic invariants", not bad, repr(bad[:8]))
    A = poly.coeff_monomial(x**4)
    Aall = [poly.coeff_monomial(v**4) for v in vars3]
    Ball = [poly.coeff_monomial(x**2 * y**2), poly.coeff_monomial(x**2 * z**2), poly.coeff_monomial(y**2 * z**2)]
    gate("quartic pure-axis coefficients equal", Aall[0] == Aall[1] == Aall[2], repr(Aall))
    gate("quartic mixed coefficients equal", Ball[0] == Ball[1] == Ball[2], repr(Ball))
    B = Ball[0]
    lam = sp.Min(A, (A + B) / 3)
    # Resolve exact Min.
    lam = A if A <= (A + B) / 3 else (A + B) / 3
    gate("quartic local positivity", lam > 0, f"A={A}, B={B}, lambda={lam}")
    return sp.factor(lam)


def exact_remainder_constant(terms, order: int) -> sp.Rational:
    # cos remainder after degree order-2: |t|^order/order!
    total = sp.Rational(0)
    for r, a in terms:
        r2 = sum(ri * ri for ri in r)
        total += abs(frac_sp(a)) * sp.Integer(r2) ** (order // 2) / sp.factorial(order)
    return sp.factor(total)

min_q0_G, min_q2_G, min_q4_G = taylor_data(min_const, min_terms, (0, 0, 0))
gate("Qmin Taylor constant at Gamma zero", min_q0_G == 0)
gate("Qmin quadratic term at Gamma zero", min_q2_G.as_expr() == 0, str(min_q2_G.as_expr()))
lam4_min_G = cubic_quartic_lambda(min_q4_G)
C6_min_G = exact_remainder_constant(min_terms, 6)
r2_min_G = sp.factor(lam4_min_G / (2 * C6_min_G))

max_q0_G, max_q2_G, max_q4_G = taylor_data(max_const, max_terms, (0, 0, 0))
gate("Qmax Taylor constant at Gamma zero", max_q0_G == 0)
lam2_max_G = isotropic_quadratic_lambda(max_q2_G)
C4_max_G = exact_remainder_constant(max_terms, 4)
r2_max_G = sp.factor(lam2_max_G / (2 * C4_max_G))

max_q0_R, max_q2_R, max_q4_R = taylor_data(max_const, max_terms, (1, 1, 1))
gate("Qmax Taylor constant at R zero", max_q0_R == 0)
lam2_max_R = isotropic_quadratic_lambda(max_q2_R)
C4_max_R = exact_remainder_constant(max_terms, 4)
r2_max_R = sp.factor(lam2_max_R / (2 * C4_max_R))

print("\nLOCAL EXACT CERTIFICATES")
print("Qmin @ Gamma quartic lambda =", lam4_min_G)
print("Qmin @ Gamma C6             =", C6_min_G)
print("Qmin proven for |k|^2 <=    =", r2_min_G, "~", sp.N(r2_min_G, 12))
print("Qmax @ Gamma quadratic lambda=", lam2_max_G)
print("Qmax @ Gamma C4             =", C4_max_G)
print("Qmax proven for |k|^2 <=    =", r2_max_G, "~", sp.N(r2_max_G, 12))
print("Qmax @ R quadratic lambda    =", lam2_max_R)
print("Qmax @ R C4                 =", C4_max_R)
print("Qmax proven for |k-R|^2 <=  =", r2_max_R, "~", sp.N(r2_max_R, 12))

# ------------------------------- interval proof -------------------------------
@dataclass(frozen=True)
class Box:
    lo: tuple[mp.mpf, mp.mpf, mp.mpf]
    hi: tuple[mp.mpf, mp.mpf, mp.mpf]
    depth: int = 0


def iv_lower(v):
    return v.a


def iv_upper(v):
    return v.b


def max_abs_iv(v):
    return max(abs(v.a), abs(v.b))


def interval_direct(const: F, terms, box: Box):
    total = frac_iv(const)
    for r, a in terms:
        plo = mp.mpf("0")
        phi = mp.mpf("0")
        for i, ri in enumerate(r):
            if ri >= 0:
                plo += ri * box.lo[i]
                phi += ri * box.hi[i]
            else:
                plo += ri * box.hi[i]
                phi += ri * box.lo[i]
        total += frac_iv(a) * iv.cos(iv.mpf([plo, phi]))
    return total.a


def interval_taylor_lower(const: F, terms, box: Box):
    center = tuple((box.lo[i] + box.hi[i]) / 2 for i in range(3))
    half = tuple((box.hi[i] - box.lo[i]) / 2 for i in range(3))
    value = frac_iv(const)
    grad = [iv.mpf(0), iv.mpf(0), iv.mpf(0)]
    rem = iv.mpf(0)
    for r, a in terms:
        theta = sum(r[i] * center[i] for i in range(3))
        aa = frac_iv(a)
        value += aa * iv.cos(iv.mpf(theta))
        st = iv.sin(iv.mpf(theta))
        for i in range(3):
            if r[i]:
                grad[i] += -aa * r[i] * st
        delta = sum(abs(r[i]) * half[i] for i in range(3))
        rem += abs(aa) * iv.mpf(delta) ** 2 / 2
    lower = value.a - rem.b
    for i in range(3):
        lower -= max_abs_iv(grad[i]) * half[i]
    return lower


def better_lower(a, b):
    return a if a >= b else b


def inside_local_gamma(box: Box, r2_exact: sp.Rational) -> bool:
    # Domain is [0,pi]^3 after reflection reduction.
    d2 = sum(box.hi[i] ** 2 for i in range(3))
    bound = mp.mpf(str(sp.N(r2_exact, IV_DPS - 5)))
    return d2 <= bound * mp.mpf("0.999999999999")


def inside_local_R(box: Box, r2_exact: sp.Rational) -> bool:
    pi = mp.pi
    d2 = sum((pi - box.lo[i]) ** 2 for i in range(3))
    bound = mp.mpf(str(sp.N(r2_exact, IV_DPS - 5)))
    return d2 <= bound * mp.mpf("0.999999999999")


def initial_boxes(n: int):
    pi = mp.pi
    edges = [pi * i / n for i in range(n + 1)]
    for i, j, k in itertools.product(range(n), repeat=3):
        yield Box((edges[i], edges[j], edges[k]), (edges[i + 1], edges[j + 1], edges[k + 1]), 0)


def certify_claim(name: str, const: F, terms, local_gamma_r2=None, local_R_r2=None):
    stack = list(initial_boxes(INITIAL_SPLITS))
    processed = 0
    interval_pass = 0
    local_pass = 0
    deepest = 0
    worst_lb = None
    unresolved = []
    t0 = time.time()

    while stack:
        box = stack.pop()
        processed += 1
        deepest = max(deepest, box.depth)
        if processed > MAX_BOXES_PER_CLAIM:
            unresolved.append(box)
            unresolved.extend(stack)
            break

        if local_gamma_r2 is not None and inside_local_gamma(box, local_gamma_r2):
            local_pass += 1
            continue
        if local_R_r2 is not None and inside_local_R(box, local_R_r2):
            local_pass += 1
            continue

        ld = interval_direct(const, terms, box)
        lt = interval_taylor_lower(const, terms, box)
        lb = better_lower(ld, lt)
        if worst_lb is None or lb < worst_lb:
            worst_lb = lb
        if lb >= 0:
            interval_pass += 1
            continue

        widths = [box.hi[i] - box.lo[i] for i in range(3)]
        axis = max(range(3), key=lambda i: widths[i])
        if box.depth >= MAX_DEPTH:
            unresolved.append(box)
            continue
        mid = (box.lo[axis] + box.hi[axis]) / 2
        lo1, hi1 = list(box.lo), list(box.hi)
        lo2, hi2 = list(box.lo), list(box.hi)
        hi1[axis] = mid
        lo2[axis] = mid
        stack.append(Box(tuple(lo2), tuple(hi2), box.depth + 1))
        stack.append(Box(tuple(lo1), tuple(hi1), box.depth + 1))

        if processed % REPORT_EVERY == 0:
            print(f"{name}: boxes={processed:,} pending={len(stack):,} local={local_pass:,} interval={interval_pass:,} depth={deepest}")

    elapsed = time.time() - t0
    result = {
        "name": name,
        "proved": len(unresolved) == 0,
        "processed_boxes": processed,
        "interval_pass_boxes": interval_pass,
        "local_taylor_pass_boxes": local_pass,
        "max_depth": deepest,
        "elapsed_seconds": elapsed,
        "unresolved_boxes": len(unresolved),
        "worst_interval_lower_seen": None if worst_lb is None else str(worst_lb),
    }
    print("\n", name, json.dumps(result, indent=2), sep="")
    if unresolved:
        sample = []
        for b in unresolved[:10]:
            sample.append({"lo": [str(v) for v in b.lo], "hi": [str(v) for v in b.hi], "depth": b.depth})
        result["unresolved_sample"] = sample
    return result


print("\n" + "=" * 100)
print("GLOBAL INTERVAL CERTIFICATION ON [0,pi]^3")
print("=" * 100)
min_result = certify_claim("GLOBAL MINIMUM AT GAMMA", min_const, min_terms, local_gamma_r2=r2_min_G)
if MAX_CANDIDATE_SURVIVES:
    max_result = certify_claim("GLOBAL MAXIMUM AT R", max_const, max_terms, local_gamma_r2=r2_max_G, local_R_r2=r2_max_R)
else:
    max_result = {
        "name": "GLOBAL MAXIMUM AT R",
        "proved": False,
        "falsified_by_basis_correct_numerical_scan": True,
        "refined_numerical_max": {"value": refined_max[0], "k": list(refined_max[1])},
        "message": "R is not the global maximum under the metadata-bound basis and cube-boundary projector."
    }

# ------------------------------- artifact output ------------------------------
bandwidth = cR - cG
result = {
    "title": "Global O(y^4) band-edge certificate for the SU(3) T1^{+-} branch",
    "kernel": str(KPATH),
    "kernel_sha256": sha256(KPATH),
    "kernel_records": len(records),
    "basis_planes": [list(p) for p in basis],
    "orientation_binding": "indices taken directly from meta.basis_planes",
    "basis_correct_numerical_reconnaissance": {
        "grid": SCAN_G,
        "refined_min": {"value": refined_min[0], "k": list(refined_min[1])},
        "refined_max": {"value": refined_max[0], "k": list(refined_max[1])},
        "Gamma_candidate_survives": MIN_CANDIDATE_SURVIVES,
        "R_candidate_survives": MAX_CANDIDATE_SURVIVES,
    },
    "exact": {
        "c4_Gamma": str(cG),
        "c4_X": str(cX),
        "c4_M": str(cM),
        "c4_R": str(cR),
        "candidate_bandwidth_R_minus_Gamma": str(bandwidth),
        "c4_Gamma_decimal": str(float(cG)),
        "c4_R_decimal": str(float(cR)),
        "candidate_bandwidth_decimal": str(float(bandwidth)),
    },
    "laurent_term_counts": {"N": len(N), "D": len(D), "Qmin": len(QMIN), "Qmax": len(QMAX)},
    "cosine_term_counts": {"Qmin": len(min_terms), "Qmax": len(max_terms)},
    "symmetry": {"independent_reflections": all_reflections, "coordinate_permutations": all_permutations},
    "local_certificates": {
        "Qmin_Gamma": {"quartic_lambda": str(lam4_min_G), "C6": str(C6_min_G), "radius_squared": str(r2_min_G), "quartic": str(min_q4_G.as_expr())},
        "Qmax_Gamma": {"quadratic_lambda": str(lam2_max_G), "C4": str(C4_max_G), "radius_squared": str(r2_max_G), "quadratic": str(max_q2_G.as_expr())},
        "Qmax_R": {"quadratic_lambda": str(lam2_max_R), "C4": str(C4_max_R), "radius_squared": str(r2_max_R), "quadratic": str(max_q2_R.as_expr())},
    },
    "global_minimum_certificate": min_result,
    "global_maximum_certificate": max_result,
    "overall_proved": bool(min_result["proved"] and max_result["proved"]),
}

json_path = OUTDIR / "CERT_Y4_global_band_edge_certificate.json"
md_path = OUTDIR / "CERT_Y4_global_band_edge_certificate.md"
json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

status = "PROVED" if result["overall_proved"] else "UNRESOLVED"
md = f"""# Global O(y^4) band-edge certificate — {status}

- Kernel: `{KPATH}`
- SHA-256: `{result['kernel_sha256']}`
- Records: **{len(records)}**
- Basis order: `{basis}` (bound directly from kernel metadata)

## Exact candidate edges

- Gamma: `c4 = {cG}` = {float(cG):.16g}
- X: `c4 = {cX}` = {float(cX):.16g}
- M: `c4 = {cM}` = {float(cM):.16g}
- R: `c4 = {cR}` = {float(cR):.16g}
- R-Gamma: `{bandwidth}` = {float(bandwidth):.16g}

## Proof reduction

The projected coefficient is `c4=N/D`, where `D=||psi||^2`. The code constructs the exact Laurent
polynomials and certifies the two division-free inequalities:

- `Qmin=N-c4(Gamma)D >= 0`,
- `Qmax=c4(R)D-N >= 0`.

Local zeros are handled by exact Taylor lower bounds; all remaining boxes are handled by interval
branch-and-bound on `[0,pi]^3`, justified by exact independent-reflection symmetry.

## Machine result

```json
{json.dumps({'minimum': min_result, 'maximum': max_result, 'overall_proved': result['overall_proved']}, indent=2)}
```

## Verdict

**{status}.**
"""
md_path.write_text(md, encoding="utf-8")

print("\n" + "=" * 100)
print("FINAL VERDICT:", status)
print("candidate exact bandwidth =", bandwidth, "=", float(bandwidth))
print("JSON:", json_path)
print("MD:  ", md_path)
if not result["overall_proved"]:
    print("The exact reduction and local certificates passed, but interval subdivision left unresolved boxes.")
    print("Do not label Gamma/R as globally exact edges until overall_proved=true.")
