#!/usr/bin/env python3
# =====================================================================
# ENGINE_FLUX_glueball_band_certificate.py
#
# O(y^2) single-plaquette glueball BAND STRUCTURE for the SU(3)
# Kogut-Susskind Hamiltonian in d=3 spatial dimensions, both charge
# sectors, from the exact per-neighbor constants of the paper:
#
# v2 (SS8.2 correction applied): hopping t+ = -481/612 + 3/4 = -11/306 per
# shared-link neighbor (vacuum-route-inclusive); the original header below is
# retained for provenance.
#   C-even: hopping t+ = -481/612 per shared-link neighbor (orientation
#           independent); diagonal per-neighbor (self-energy + vacuum
#           subtraction) = -481/612 + 3/4 = -22/612.
#   C-odd:  hopping t-(s) = (5/612) * s, s = +1 same / -1 opposite
#           relative shared-link orientation; same diagonal.
#
# Within-plaquette restricted pieces (Bridge Theorem):
#   4*Delta+(3y/2) = 8/3 - y + (13/20) y^2 + O(y^3)
#   4*Delta-(3y/2) = 8/3 + y + (1/2)  y^2 + O(y^3)
#
# Effective one-excitation Hamiltonians at O(y^2), units of y^2:
#   E+(k) = 13/20 - 22/51 - (481/612) * lambda(k),  lambda in spec A(k)
#   E-(k) = 1/2   - 22/51 + (5/612)   * mu(k),      mu     in spec S(k)
# where A(k)/S(k) are the unsigned/signed 3x3 Bloch matrices of the
# plaquette shared-link adjacency (orbitals = orientations xy,xz,yz).
#
# This closes the paper's open problem (Theorem 6.3, signed band
# minimization). All structural claims are gated.
# =====================================================================

import itertools
import numpy as np
import sympy as sp
from fractions import Fraction as F

np.set_printoptions(precision=6, suppress=True)

PASS = []
def gate(name, cond):
    PASS.append((name, bool(cond)))
    print(f"  GATE {'PASS' if cond else 'FAIL'} :: {name}")
    if not cond:
        raise SystemExit(f"GATE FAILED: {name}")

# ---------------------------------------------------------------------
# 1. Cubical complex: plaquettes, oriented boundaries, signed incidence
# ---------------------------------------------------------------------
ORIENT = [(0, 1), (0, 2), (1, 2)]   # orbitals a=xy(01), b=xz(02), c=yz(12)
ONAME = {0: "a(01)", 1: "b(02)", 2: "c(12)"}

def boundary(x, o, L):
    """Oriented boundary of plaquette (x; mu<nu): list of ((site,dir), sign)."""
    mu, nu = ORIENT[o]
    x = tuple(x)
    def shift(y, d):
        z = list(y); z[d] = (z[d] + 1) % L; return tuple(z)
    return [((x, mu), +1),
            ((shift(x, mu), nu), +1),
            ((shift(x, nu), mu), -1),
            ((x, nu), -1)]

def build_complex(L):
    plaqs = [(x, o) for x in itertools.product(range(L), repeat=3) for o in range(3)]
    pidx = {p: i for i, p in enumerate(plaqs)}
    link_inc = {}                       # link -> list of (plaq_index, sign)
    for p in plaqs:
        for (ln, sg) in boundary(p[0], p[1], L):
            link_inc.setdefault(ln, []).append((pidx[p], sg))
    return plaqs, pidx, link_inc

L = 4
plaqs, pidx, link_inc = build_complex(L)
NP = len(plaqs)

print("=" * 78)
print("STEP 1: complex sanity")
print("=" * 78)
ok = all(len(v) == 4 and sorted(s for _, s in v) == [-1, -1, 1, 1]
         for v in link_inc.values())
gate("every link lies in exactly 4 plaquettes with signs (+,+,-,-)", ok)

# Neighbor map with relative orientation s = sigma_p * sigma_q
nbrs = {i: {} for i in range(NP)}      # i -> {j: (s, shared_link)}
for ln, inc in link_inc.items():
    for (i, si), (j, sj) in itertools.combinations(inc, 2):
        for (u, su), (v, sv) in [((i, si), (j, sj)), ((j, sj), (i, si))]:
            if v in nbrs[u]:
                gate("two plaquettes share at most one link", False)
            nbrs[u][v] = (su * sv, ln)
gate("every plaquette has exactly 12 shared-link neighbors",
     all(len(nbrs[i]) == 12 for i in range(NP)))

# Frustration structure: triangles
x0 = (0, 0, 0)
pa, pb, pc = pidx[(x0, 0)], pidx[(x0, 1)], pidx[(x0, 2)]
tri_corner = nbrs[pa][pb][0] * nbrs[pb][pc][0] * nbrs[pc][pa][0]
# same-link triangle: three of the four plaquettes around link ((0,0,0),0)
q1, q2, q3 = [i for i, _ in link_inc[((0, 0, 0), 0)][:3]]
tri_link = nbrs[q1][q2][0] * nbrs[q2][q3][0] * nbrs[q3][q1][0]
gate("corner triangle frustrated (sign product -1): signed graph is NOT "
     "gauge-equivalent to a uniform one", tri_corner == -1)
gate("same-link triangle unfrustrated (+1)", tri_link == +1)

# ---------------------------------------------------------------------
# 2. Translation-invariant neighbor table  ->  Bloch matrices
# ---------------------------------------------------------------------
print("=" * 78)
print("STEP 2: orbital-resolved neighbor table and Bloch matrices")
print("=" * 78)

def centered(d, L):
    return tuple(((c + L // 2) % L) - L // 2 for c in d)

tables = {}
for x in itertools.product(range(L), repeat=3):
    for o in range(3):
        i = pidx[(x, o)]
        tab = []
        for j, (s, _) in nbrs[i].items():
            (xj, oj) = plaqs[j]
            d = centered(tuple((xj[m] - x[m]) % L for m in range(3)), L)
            tab.append((o, oj, d, s))
        tab = tuple(sorted(tab))
        tables.setdefault(o, set()).add(tab)
gate("neighbor table is translation invariant (one table per orbital)",
     all(len(v) == 1 for v in tables.values()))
TAB = {o: sorted(next(iter(tables[o]))) for o in range(3)}
for o in range(3):
    print(f"  orbital {ONAME[o]}:")
    for (_, oj, d, s) in TAB[o]:
        print(f"    -> {ONAME[oj]:6s} at delta={d}  s={s:+d}")

k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
kk = (k1, k2, k3)

def bloch(signed):
    M = sp.zeros(3, 3)
    for o in range(3):
        for (_, oj, d, s) in TAB[o]:
            w = (s if signed else 1) * sp.exp(sp.I * sum(kk[m] * d[m] for m in range(3)))
            M[o, oj] += w
    return sp.simplify(M)

A = bloch(False)   # C-even
S = bloch(True)    # C-odd
print("\n  A(k) [C-even] ="); sp.pprint(sp.simplify(sp.expand_trig(A)))
print("\n  S(k) [C-odd]  ="); sp.pprint(sp.simplify(sp.expand_trig(S)))

gate("A(k), S(k) Hermitian", sp.simplify(A - A.H) == sp.zeros(3, 3)
     and sp.simplify(S - S.H) == sp.zeros(3, 3))
gate("A(0) = 4*J (A1 eigenvalue 12, E doublet 0)",
     sp.simplify(A.subs({k1: 0, k2: 0, k3: 0}) - 4 * sp.ones(3, 3)) == sp.zeros(3, 3))
gate("S(0) = -4*I  (triple degeneracy at k=0)",
     sp.simplify(S.subs({k1: 0, k2: 0, k3: 0}) + 4 * sp.eye(3)) == sp.zeros(3, 3))

# ---------------------------------------------------------------------
# 3. Bloch vs finite lattice (exact spectral match)
# ---------------------------------------------------------------------
print("=" * 78)
print("STEP 3: Bloch decomposition reproduces the finite-lattice spectra")
print("=" * 78)

def finite_matrix(signed):
    M = np.zeros((NP, NP))
    for i in range(NP):
        for j, (s, _) in nbrs[i].items():
            M[i, j] += (s if signed else 1)
    return M

Afin, Sfin = finite_matrix(False), finite_matrix(True)
gate("finite matrices symmetric", np.allclose(Afin, Afin.T) and np.allclose(Sfin, Sfin.T))

fA = sp.lambdify((k1, k2, k3), A, "numpy")
fS = sp.lambdify((k1, k2, k3), S, "numpy")
ks = [2 * np.pi * n / L for n in range(L)]
for tag, Msym, Mfin in [("A", fA, Afin), ("S", fS, Sfin)]:
    ev_bloch = np.sort(np.concatenate([
        np.linalg.eigvalsh(np.array(Msym(a, b, c), dtype=complex))
        for a in ks for b in ks for c in ks]))
    ev_fin = np.sort(np.linalg.eigvalsh(Mfin))
    gate(f"{tag}: union of Bloch spectra == finite L={L} spectrum "
         f"(max dev {np.max(np.abs(ev_bloch - ev_fin)):.2e})",
         np.allclose(ev_bloch, ev_fin, atol=1e-9))

# gauge invariance: random plaquette-orientation flips conjugate S by diag(+-1)
rng = np.random.default_rng(7)
D = np.diag(rng.choice([-1.0, 1.0], size=NP))
gate("C-odd spectrum gauge-invariant under random orientation flips",
     np.allclose(np.sort(np.linalg.eigvalsh(D @ Sfin @ D)),
                 np.sort(np.linalg.eigvalsh(Sfin)), atol=1e-9))

# ---------------------------------------------------------------------
# 4. Incidence factorization:  A+4I = N N^dag,  S+4I = Ntil Ntil^dag
# ---------------------------------------------------------------------
print("=" * 78)
print("STEP 4: incidence factorization and the exact C-odd flat band")
print("=" * 78)

def bloch_incidence(signed):
    """3x3 (orbital x link-direction) Bloch incidence from the boundary chains."""
    M = sp.zeros(3, 3)
    for o in range(3):
        for ((site, d), sg) in boundary((0, 0, 0), o, L):
            dlt = centered(site, L)
            w = (sg if signed else 1) * sp.exp(sp.I * sum(kk[m] * dlt[m] for m in range(3)))
            M[o, d] += w
    return sp.simplify(M)

Ninc = bloch_incidence(False)
Ntil = bloch_incidence(True)
print("  signed Bloch incidence Ntil(k) ="); sp.pprint(Ntil)

gate("A(k) + 4I == N(k) N(k)^dag (unsigned incidence) identically",
     sp.simplify(sp.expand(A + 4 * sp.eye(3) - Ninc * Ninc.H)) == sp.zeros(3, 3))
gate("S(k) + 4I == Ntil(k) Ntil(k)^dag (signed incidence) identically  "
     "[=> mu(k) >= -4 for all k]",
     sp.simplify(sp.expand(S + 4 * sp.eye(3) - Ntil * Ntil.H)) == sp.zeros(3, 3))

detN = sp.simplify(Ninc.det())
detNt = sp.simplify(Ntil.det())
v = [1 + sp.exp(sp.I * q) for q in kk]
gate("det N(k) = -2 (1+e^{ik1})(1+e^{ik2})(1+e^{ik3})  (no C-even flat band)",
     sp.simplify(detN + 2 * v[0] * v[1] * v[2]) == 0)
gate("det Ntil(k) == 0 identically  [=> EXACTLY FLAT C-ODD BAND mu(k) = -4]",
     detNt == 0)

u = [1 - sp.exp(sp.I * q) for q in kk]
w_flat = sp.Matrix([sp.conjugate(u[2]), -sp.conjugate(u[1]), sp.conjugate(u[0])])
ker_sym = sp.expand(Ntil.H * w_flat)
fSnum = sp.lambdify((k1, k2, k3), S, "numpy")
fwnum = sp.lambdify((k1, k2, k3), w_flat, "numpy")
rng2 = np.random.default_rng(3)
num_ok = True
for _ in range(25):
    ka, kb, kc = rng2.uniform(0.1, 2 * np.pi - 0.1, 3)
    Sm = np.array(fSnum(ka, kb, kc), dtype=complex)
    wv = np.array(fwnum(ka, kb, kc), dtype=complex).reshape(3)
    if np.linalg.norm(wv) > 1e-9:
        num_ok &= bool(np.allclose(Sm @ wv, -4.0 * wv, atol=1e-9))
gate("flat-band eigenvector: Ntil(k)^dag w == 0 identically with "
     "w = (conj u3, -conj u2, conj u1)  [=> (S+4I)w = 0 by the factorization "
     "gate]; numeric S w = -4 w at 25 random k",
     ker_sym == sp.zeros(3, 1) and num_ok)

# real-space compact localized states: boundary of the elementary 3-cell
print("  searching the elementary-cube 2-chain (d2 d3 = 0 mechanism)...")
e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
def addv(x, y): return tuple((a + b) % L for a, b in zip(x, y))
cube_faces = [((0, 0, 0), 0), (e[2], 0), ((0, 0, 0), 1), (e[1], 1),
              ((0, 0, 0), 2), (e[0], 2)]
sol = None
for signs in itertools.product([1, -1], repeat=6):
    acc = {}
    for (p, sg) in zip(cube_faces, signs):
        for (ln, s2) in boundary(p[0], p[1], L):
            acc[ln] = acc.get(ln, 0) + sg * s2
    if all(val == 0 for val in acc.values()):
        sol = signs
        break
gate("a +-1 signing of the 6 cube faces is link-free (closed 2-chain, ∂∂=0)",
     sol is not None)
vec = np.zeros(NP)
for (p, sg) in zip(cube_faces, sol):
    vec[pidx[p]] = sg
gate("the cube 2-chain is an exact finite-lattice eigenvector of S at -4",
     np.allclose(Sfin @ vec, -4.0 * vec, atol=1e-12))
mult = int(np.sum(np.abs(np.linalg.eigvalsh(Sfin) + 4.0) < 1e-9))
gate(f"flat-band multiplicity on L={L}: {mult} = L^3 + 2 "
     "(L^3 cube states + 2 dispersive branches touching at k=0)",
     mult == L ** 3 + 2)

# ---------------------------------------------------------------------
# 5. Band extrema and exact coefficients
# ---------------------------------------------------------------------
print("=" * 78)
print("STEP 5: band extrema, exact O(y^2) coefficients")
print("=" * 78)

# dense scan
grid = np.linspace(0, 2 * np.pi, 41)[:-1]
lam_all, mu_all, mu_max_pt = [], [], None
mu_max_val = -1e9
for a in grid:
    for b in grid:
        for c in grid:
            lam_all.append(np.linalg.eigvalsh(np.array(fA(a, b, c), dtype=complex)))
            evs = np.linalg.eigvalsh(np.array(fS(a, b, c), dtype=complex))
            mu_all.append(evs)
            if evs[-1] > mu_max_val:
                mu_max_val, mu_max_pt = evs[-1], (a, b, c)
lam_all, mu_all = np.array(lam_all), np.array(mu_all)
print(f"  C-even lambda range (scan): [{lam_all.min():.6f}, {lam_all.max():.6f}]")
print(f"  C-odd  mu     range (scan): [{mu_all.min():.6f}, {mu_all.max():.6f}]"
      f"   argmax ~ {tuple(round(x/np.pi,3) for x in mu_max_pt)} * pi")
gate("C-even lambda in [-4, 12], extrema attained (NN^dag >= 0; 12-regular)",
     abs(lam_all.max() - 12) < 1e-9 and abs(lam_all.min() + 4) < 1e-9)
gate("C-odd mu_min = -4 attained at every scanned k (flat band)",
     np.allclose(mu_all.min(axis=1), -4.0, atol=1e-9))

Spi = sp.Matrix(S.subs({k1: sp.pi, k2: sp.pi, k3: sp.pi}))
ev_pi = sorted(Spi.eigenvals().items(), key=lambda t: t[0])
print(f"  exact spec S(pi,pi,pi) = {[(sp.nsimplify(v), m) for v, m in ev_pi]}")
gate("C-odd mu_max = 8, attained at k=(pi,pi,pi) with multiplicity 2",
     ev_pi == [(-4, 1), (8, 2)] and abs(mu_all.max() - 8) < 1e-9)

# exact O(y^2) coefficients (units of y^2), Fractions throughout
diag = F(-481, 612) + F(3, 4)                 # per-neighbor self-energy + vacuum
even_within, odd_within = F(13, 20), F(1, 2)  # 9*c2(+/-) from the Bridge
tp_aswritten, tm = F(-481, 612), F(5, 612)   # manuscript Thm 6.2 hop (as written)
tp = tp_aswritten + F(3, 4)                   # SS8.2 vacuum-route-inclusive hop = -11/306 (v2 correction)

even_k0_A1 = even_within + 12 * diag + tp * 12
even_k0_E  = even_within + 12 * diag + tp * 0
even_top   = even_within + 12 * diag + tp * (-4)
odd_flat   = odd_within  + 12 * diag + tm * (-4)
odd_top    = odd_within  + 12 * diag + tm * 8

print(f"\n  C-even A1++ (k=0, lambda=12) coefficient : {even_k0_A1} = {float(even_k0_A1):+.6f}")
print(f"  C-even E++  (k=0, lambda=0)  coefficient : {even_k0_E} = {float(even_k0_E):+.6f}")
print(f"  C-even band top (lambda=-4)  coefficient : {even_top} = {float(even_top):+.6f}")
print(f"  C-odd  FLAT BAND (all k)     coefficient : {odd_flat} = {float(odd_flat):+.6f}")
print(f"  C-odd  band top (mu=8 at pi) coefficient : {odd_top} = {float(odd_top):+.6f}")

gate("v2: C-even k=0 A1++ == -217/1020 (SS8.2-corrected)",
     even_k0_A1 == F(-217, 1020))
gate("v2 provenance: as-written assembly reproduces the manuscript's -9397/1020",
     even_within + 12 * diag + tp_aswritten * 12 == F(-9397, 1020))
gate("v2: C-even band top (lambda=-4) == 1109/3060",
     even_top == F(1109, 3060))
gate("v2: E++ (lambda=0) == 223/1020, t-independent hence unchanged by the correction",
     even_k0_E == F(223, 1020)
     and even_within + 12 * diag + tp_aswritten * 0 == F(223, 1020))
gate("v2: C-even bandwidth 16|t+| == 88/153",
     tp * (-4) - tp * 12 == F(88, 153))
gate("v2: C-even curvature (11/306)*(4/3) == 22/459",
     (-tp) * F(4, 3) == F(22, 459))
gate("v2: corrected per-bond ratio |t-|/|t+| == 5/22 (supersedes Remark 6.4's 5/481; "
     "immobility statement survives via the exact flat band, not the ratio)",
     tm / (-tp) == F(5, 22))
import json as _json, os as _os
if _os.path.exists("RUN_TROM_d3_results.json"):
    _o2 = _json.load(open("RUN_TROM_d3_results.json"))["order2"]
    gate("v2 cross-check vs RUN_TROM_d3_results.json order-2 block (6 fields)",
         F(_o2["m2_even_k0_A1++_corrected"]) == even_k0_A1
         and F(_o2["m2_even_bandmin_corrected"]) == even_top
         and F(_o2["E++_k0_unchanged"]) == even_k0_E
         and F(_o2["m2_odd_flat"]) == odd_flat
         and F(_o2["corrected_Ceven_curvature_coeff"]) == (-tp) * F(4, 3)
         and F(_o2["corrected_Ceven_bandwidth_16|t|"]) == tp * (-4) - tp * 12)
else:
    print("  NOTE  RUN_TROM_d3_results.json not present in cwd; cross-check gate skipped (constants hard-pinned above)")
gate("C-odd flat-band coefficient = 11/306 (CLOSES Theorem 6.3's open "
     "interval [-3/102, 17/102])",
     odd_flat == F(11, 306) and F(-3, 102) <= odd_flat <= F(17, 102))
print(f"  bandwidths (units of y^2): C-even = {tp*(-4)-tp*12} = "
      f"{float(tp*(-4)-tp*12):.4f};  C-odd manifold = {tm*8-tm*(-4)} = "
      f"{float(tm*8-tm*(-4)):.4f};  C-odd lowest branch = 0 (exact)")

# ---------------------------------------------------------------------
# 6. Effective masses: exact k->0 expansions
# ---------------------------------------------------------------------
print("=" * 78)
print("STEP 6: exact small-k expansions")
print("=" * 78)
eps = sp.symbols("eps", positive=True)
q1s, q2s, q3s = sp.symbols("q1 q2 q3", real=True)
sub = {k1: eps * q1s, k2: eps * q2s, k3: eps * q3s}

# C-even A1 branch: second-order perturbation theory about k=0
evec = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
Aser = sp.Matrix([[sp.series(A[i, j].subs(sub), eps, 0, 3).removeO()
                   for j in range(3)] for i in range(3)])
A0 = Aser.subs(eps, 0)
A1m = sp.expand((Aser - A0).applyfunc(lambda z: z.coeff(eps, 1)))
A2m = sp.expand((Aser - A0).applyfunc(lambda z: z.coeff(eps, 2)))
P = sp.eye(3) - evec * evec.T
lam2 = sp.simplify((evec.T * A2m * evec)[0]
                   + (evec.T * A1m.H * P * A1m * evec)[0] / sp.Integer(12))
q2sum = q1s**2 + q2s**2 + q3s**2
gate("C-even A1 branch: lambda(k) = 12 - (4/3)|k|^2 + O(k^4) (isotropic)",
     sp.simplify(lam2 + sp.Rational(4, 3) * q2sum) == 0)

# C-odd: Ntil Ntil^dag = QQ^T eps^2 + O(eps^3), spec(QQ^T) = {0, |k|^2, |k|^2}
NtN = sp.expand((Ntil * Ntil.H).subs(sub).applyfunc(
    lambda z: sp.series(z, eps, 0, 3).removeO()))
Q2 = sp.simplify(NtN.applyfunc(lambda z: z.coeff(eps, 2)))
lamq = sp.symbols("lamq")
char = sp.factor(sp.expand((Q2 - lamq * sp.eye(3)).det()))
gate("C-odd dispersive branches: mu(k) = -4 + |k|^2 + O(k^3), doubly degen. "
     "(char poly = -lam (lam - |k|^2)^2)",
     sp.simplify(char + lamq * (lamq - q2sum) ** 2) == 0)
print(f"  => C-even A1++ curvature (v2, SS8.2 hop): (11/306)*(4/3) = {(F(11,306))*F(4,3)} y^2 |k|^2  [as-written: 481/459]")
print(f"  => C-odd dispersive curvature: 5/612 y^2 |k|^2 ; flat branch: 0")

# ---------------------------------------------------------------------
# 7. O_h quantum numbers at k=0 (Lambda^2 of the vector rep)
# ---------------------------------------------------------------------
print("=" * 78)
print("STEP 7: cubic-group content at k=0")
print("=" * 78)
def rot(axis, quarter):
    R = np.eye(3)
    c, s = round(np.cos(np.pi/2*quarter)), round(np.sin(np.pi/2*quarter))
    i, j = [m for m in range(3) if m != axis]
    R[i, i], R[i, j], R[j, i], R[j, j] = c, -s, s, c
    return R
def chi_even(R):  # 2-subsets of axes mapped to themselves (orientation ignored)
    return sum(1 for (m, n) in ORIENT
               if {np.argmax(np.abs(R[:, m])), np.argmax(np.abs(R[:, n]))} == {m, n})
def chi_odd(R):   # trace of Lambda^2 R
    return round((np.trace(R) ** 2 - np.trace(R @ R)) / 2)

C3 = np.array([[0., 0., 1.], [1., 0., 0.], [0., 1., 0.]])
C2p = np.array([[0., 1., 0.], [1., 0., 0.], [0., 0., -1.]])
classes = [np.eye(3), C3, rot(2, 2), rot(2, 1), C2p]   # E, C3, C2, C4, C2'
ce = [chi_even(R) for R in classes]
co = [chi_odd(R) for R in classes]
print(f"  characters (E,8C3,3C2,6C4,6C2'): C-even {ce}, C-odd {co}")
gate("C-even k=0 triplet = A1 (+) E   [0++ at lambda=12; E++ doublet at lambda=0]",
     ce == [3, 0, 3, 1, 1])
gate("C-odd  k=0 triplet = T1; inversion on 2-forms = +1  =>  T1^{+-} (1^{+-}-like), "
     "NO A1 (scalar) component in the C-odd one-plaquette sector",
     co == [3, 0, -1, 1, -1] and chi_odd(-np.eye(3)) == 3)

print("=" * 78)
print(f"ALL {len(PASS)} GATES PASSED")
print("=" * 78)
print("""
SUMMARY (exact, O(y^2)):
  m+(k)  = 8/3 - y + y^2 [ 223/1020 - (11/306) lambda(k) ],  lambda in [-4,12]
           A1++ bottom (k=0): 8/3 - y - (217/1020) y^2   [SS8.2-corrected, gate;
               as-written -9397/1020 retained as a provenance gate]
           E++ channel (k=0): 8/3 - y + (223/1020) y^2   [unchanged by correction]
           curvature at bottom: + (22/459) |k|^2 y^2     [corrected; as-written 481/459]
  m-(k)  = 8/3 + y + y^2 [ 7/102 + (5/612) mu(k) ],  mu in [-4, 8]
           LOWEST BRANCH EXACTLY FLAT: mu(k) = -4 for ALL k:
               m- = 8/3 + y + (11/306) y^2   for every k         [new: closes
               Theorem 6.3's open interval [-3/102, 17/102]]
           mechanism: S + 4I = (signed incidence)(signed incidence)^dag,
               det == 0 identically; flat band spanned by elementary-cube
               boundary 2-chains (∂2∂3 = 0)
           dispersive branches: -4 + |k|^2, doubly degenerate; top mu = 8
               at k=(pi,pi,pi)
  quantum numbers at rest: C-even A1++ (0++) and E++ ; C-odd triplet T1^{+-}
      (axial-vector-like) -- the C-odd one-plaquette sector contains NO scalar.
""")
