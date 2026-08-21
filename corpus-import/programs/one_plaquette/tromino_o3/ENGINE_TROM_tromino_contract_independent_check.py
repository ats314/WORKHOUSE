#!/usr/bin/env python3
# =====================================================================
# ENGINE_TROM_tromino_contract_independent_check.py
#
# Independent review certificate for the uploaded O(y^3) tromino suite:
#   ENGINE_TROM_tromino_o3_su3_weight_cards.py        (geometry contract)
#   ENGINE_TROM_tromino_weight_constraint_certificate.py (nullspace certificate)
#   ENGINE_FLUX_su3_haar_tromino_primitives.py        (exact Haar engine)
#
# Part A re-derives the geometry contract SYMBOLICALLY:
#   B_backtrack(k) = 12 I
#   B_samelink(k)  = 2 S(k)
#   B_corner(k)    = -2 S_perp(k)
#   B_path+ + B_path- + B_corner = S(k)^2 - 12 I - 2 S(k)
# so equal lifter weights act as the constant 12 on the flat line
# (S w = -4 w  =>  16 - 12 + 8 = 12), and the corner class alone provably
# lifts (exact flat-line values 0 at X vs 16 at R).
#
# Part B settles the PHYSICAL O(y^3) question:
#   GATE: every two-hop path on three distinct plaquettes leaves the middle
#         plaquette with >= 2 links private to it (bare links).
#   GATE: using the uploaded Haar engine, ALL 32 five-trace O(y^3) numerators
#         vanish exactly on each lifter card  =>  W(path+)=W(path-)=W(corner)=0.
#   GATE: an O(y^4)-type tromino numerator (middle insertion pair chi chibar)
#         is NONZERO  =>  trominoes first activate at O(y^4).
#   GATE: coplanar vs perpendicular s=-1 dominoes give identical five-trace
#         O(y^3) NN numerator tables (abstract-domino isomorphism support),
#         and the nonzero entries require the (4,1)/(1,4) epsilon moment that
#         the primitive layer correctly hard-fails on (next-layer TODO).
# =====================================================================

import itertools, json, sys
from collections import Counter, defaultdict
from fractions import Fraction as F

import numpy as np
import sympy as sp

sys.path.insert(0, "/home/claude/review")
from ENGINE_FLUX_su3_haar_tromino_primitives import integrate_product, UnsupportedMoment

ORIENT = [(0, 1), (0, 2), (1, 2)]
L = 6
PASS = []
def gate(name, cond):
    PASS.append((name, bool(cond)))
    print(f"  GATE {'PASS' if cond else 'FAIL'} :: {name}")
    if not cond:
        raise SystemExit(f"GATE FAILED: {name}")

def shift(x, d, n=1):
    z = list(x); z[d] = (z[d] + n) % L; return tuple(z)

def boundary(x, o):
    mu, nu = ORIENT[o]
    x = tuple(x)
    return [((x, mu), +1), ((shift(x, mu), nu), +1),
            ((shift(x, nu), mu), -1), ((x, nu), -1)]

def centered(x, y):
    return tuple(((y[i] - x[i] + L // 2) % L) - L // 2 for i in range(3))

plaqs = [(x, o) for x in itertools.product(range(L), repeat=3) for o in range(3)]
pidx = {p: i for i, p in enumerate(plaqs)}
link_inc = defaultdict(list)
for p in plaqs:
    for ln, sg in boundary(*p):
        link_inc[ln].append((pidx[p], sg))
nbrs = {i: {} for i in range(len(plaqs))}
for ln, inc in link_inc.items():
    for (i, si), (j, sj) in itertools.combinations(inc, 2):
        nbrs[i][j] = (si * sj, ln); nbrs[j][i] = (si * sj, ln)
bsets = [set(ln for ln, _ in boundary(*p)) for p in plaqs]
NP = len(plaqs)

print("=" * 78)
print("PART A: independent symbolic re-derivation of the geometry contract")
print("=" * 78)
gate("complex sanity: 4 plaquettes/link, 12 neighbors/plaquette",
     all(len(v) == 4 for v in link_inc.values()) and all(len(nbrs[i]) == 12 for i in nbrs))

# --- enumerate ordered two-hop paths into class-resolved Bloch tables -----
def classify(i, q, r):
    if r == i: return "backtrack"
    s1, s2 = nbrs[i][q][0], nbrs[q][r][0]
    com3 = bsets[i] & bsets[q] & bsets[r]
    if r in nbrs[i]:
        cyc = s1 * s2 * nbrs[r][i][0]
        return ("samelink" if len(com3) == 1 else "corner") + f"{cyc:+d}"
    if len(com3) == 1: return f"common_link{(s1*s2):+d}"
    return f"path{(s1*s2):+d}"

tables = defaultdict(Counter)   # cls -> {(oi,or,delta,sgnprod): count}
counts = Counter()
bond_mid = defaultdict(Counter) # (i,r) NN ordered pair -> {"samelink": n, "corner": n}
priv_links_min = {"path": 99, "corner": 99, "samelink": 99}
for i in range(NP):
    xi, oi = plaqs[i]
    for q in nbrs[i]:
        for r in nbrs[q]:
            cls = classify(i, q, r)
            counts[cls] += 1
            if r != i:
                covered = bsets[q] & (bsets[i] | bsets[r])
                priv = 4 - len(covered)
                key = "samelink" if cls.startswith("samelink") else ("corner" if cls.startswith("corner") else "path")
                priv_links_min[key] = min(priv_links_min[key], priv)
                if r in nbrs[i]:
                    bond_mid[(i, r)][key] += 1
            xr, orr = plaqs[r]
            tables[cls][(oi, orr, centered(xi, xr), nbrs[i][q][0] * nbrs[q][r][0])] += 1

per_src = {c: counts[c] // NP for c in counts}
print(f"  per-source class counts: {dict(sorted(per_src.items()))}")
gate("class counts per source = backtrack 12, path+ 52, path- 40, corner-1 16, samelink+1 24; "
     "no common-link or +1-corner or -1-samelink classes",
     per_src == {"backtrack": 12, "path+1": 52, "path-1": 40, "corner-1": 16, "samelink+1": 24})
gate("every ordered NN pair has exactly 2 same-link middles; perpendicular pairs "
     "have exactly 2 corner middles, coplanar pairs 0",
     all(v["samelink"] == 2 and v["corner"] in (0, 2) for v in bond_mid.values())
     and sorted(Counter(v["corner"] for v in bond_mid.values()).items()) == [(0, NP * 4), (2, NP * 8)])

# --- symbolic Bloch operators from the tables ------------------------------
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
kk = (k1, k2, k3)
def bloch_of(cls, signed_path=True):
    M = sp.zeros(3, 3)
    for (oi, orr, d, sgn), mult in tables[cls].items():
        assert mult % (L ** 3) == 0
        M[oi, orr] += (mult // L ** 3) * (sgn if signed_path else 1) * sp.exp(sp.I * sum(kk[m] * d[m] for m in range(3)))
    return sp.expand(M)

# S(k) rebuilt from first principles (single-hop table)
S = sp.zeros(3, 3)
for i in [pidx[((0, 0, 0), o)] for o in range(3)]:
    oi = plaqs[i][1]
    for j, (s, _) in nbrs[i].items():
        xj, oj = plaqs[j]
        S[oi, oj] += s * sp.exp(sp.I * sum(kk[m] * centered((0, 0, 0), xj)[m] for m in range(3)))
S = sp.expand(S)
D = sp.diag(S[0, 0], S[1, 1], S[2, 2])          # coplanar (orbital-diagonal) part
Z = sp.zeros(3, 3)
B_bt, B_sl, B_co = bloch_of("backtrack"), bloch_of("samelink+1"), bloch_of("corner-1")
B_pp, B_pm = bloch_of("path+1"), bloch_of("path-1")

gate("B_backtrack(k) == 12 I identically", sp.expand(B_bt - 12 * sp.eye(3)) == Z)
gate("B_samelink(k) == 2 S(k) identically  [protected: multiple of S]",
     sp.expand(B_sl - 2 * S) == Z)
gate("B_corner(k) == -2 S_perp(k) identically  [supported on perpendicular bonds only]",
     sp.expand(B_co + 2 * (S - D)) == Z)
gate("SUFFICIENCY: B_path+ + B_path- + B_corner == S(k)^2 - 12 I - 2 S(k) identically "
     "[equal lifter weights act as the constant 16-12+8 = 12 on the flat line]",
     sp.expand(B_pp + B_pm + B_co - (S * S - 12 * sp.eye(3) - 2 * S)) == Z)

# exact necessity: corner flat-line eigenvalue varies (0 at X, 16 at R)
u = [1 - sp.exp(sp.I * q) for q in kk]
w = sp.Matrix([sp.conjugate(u[2]), -sp.conjugate(u[1]), sp.conjugate(u[0])])
def flat_val(B, pt):
    sub = dict(zip(kk, pt))
    wv, Bv = w.subs(sub), B.subs(sub)
    return sp.nsimplify(sp.expand((wv.H * Bv * wv)[0] / (wv.H * wv)[0]))
vX, vR = flat_val(B_co, (sp.pi, 0, 0)), flat_val(B_co, (sp.pi, sp.pi, sp.pi))
print(f"  corner-class flat-line value: X(pi,0,0) -> {vX},  R(pi,pi,pi) -> {vR}")
gate("NECESSITY: corner class alone is non-constant on the flat line (0 at X vs 16 at R)",
     vX == 0 and vR == 16)

print("=" * 78)
print("PART B: the physical O(y^3) weights and the protection theorem")
print("=" * 78)
print(f"  minimum private (bare) links of the middle plaquette, by landing type: {priv_links_min}")
gate("BARE-LINK LEMMA: every 3-distinct-plaquette two-hop geometry leaves the middle "
     "plaquette >= 2 links touched by no other plaquette (paths/corner: 2, same-link: 3)",
     priv_links_min == {"path": 2, "corner": 2, "samelink": 3})

cards = {c["class"]: c for c in json.load(open("/home/claude/review/CERT_TROM_tromino_o3_su3_weight_cards.json"))["lifter_cards"]}
ROLES = ["initial", "middle", "final"]

# All 32 five-trace O(y^3) numerators per lifter card:
#   <0| trace(final)^bar-ish . trace(i) trace(q) trace(r) . trace(initial) |0>
print("\n  five-trace O(y^3) numerators (bra_r x ins_i x ins_q x ins_r x ket_i), all sign patterns:")
for cls, card in cards.items():
    P = {r: card["plaquettes"][r] for r in ROLES}
    vals = []
    for kinds in itertools.product(["chi", "chibar"], repeat=5):
        specs = [(P["final"], kinds[0]), (P["initial"], kinds[1]), (P["middle"], kinds[2]),
                 (P["final"], kinds[3]), (P["initial"], kinds[4])]
        val, diag = integrate_product(specs)
        vals.append(val)
    nz = sum(1 for v in vals if v != 0)
    print(f"    {cls:32s}: 32 patterns, nonzero = {nz}")
    gate(f"ALL 32 O(y^3) numerators vanish exactly on {cls}  [W = 0]", nz == 0)

# O(y^4) activation: middle plaquette dressed with a chi chibar pair.
card = cards["path_bent_or_straight_prod+1"]
P = {r: card["plaquettes"][r] for r in ROLES}
nz4 = 0
for kq1, kq2 in [("chi", "chibar"), ("chibar", "chi")]:
    for kb, ki1, kr, ki2 in itertools.product(["chi", "chibar"], repeat=4):
        specs = [(P["final"], kb), (P["initial"], ki1), (P["middle"], kq1),
                 (P["middle"], kq2), (P["final"], kr), (P["initial"], ki2)]
        try:
            val, _ = integrate_product(specs)
        except UnsupportedMoment:
            continue
        if val != 0:
            nz4 += 1
gate(f"O(y^4) ACTIVATION: six-trace tromino numerators with a chi-chibar pair on the middle "
     f"are NOT all zero ({nz4} nonzero patterns found)", nz4 > 0)

# Abstract-domino isomorphism support: coplanar vs perpendicular s=-1 pairs,
# identical five-trace NN numerator status tables. Classify each pattern by its
# full degree profile FIRST (any center-zero link => exact 0), because the
# engine's early return in sorted link order would otherwise flag
# mathematically-zero patterns inconsistently between the two embeddings.
from ENGINE_FLUX_su3_haar_tromino_primitives import trace_factors

def pattern_status(specs):
    by = defaultdict(lambda: [0, 0])
    nv = 0
    for plaq, kind in specs:
        fac, nv = trace_factors(plaq, kind, nv)
        for lk, sg, a, b in fac:
            by[lk][0 if sg == 1 else 1] += 1
    if any((p - q) % 3 for p, q in by.values()):
        return ("zero_by_center", "0")
    if any((p != q and (p, q) not in ((3, 0), (0, 3))) or (p == q and p > 3)
           for p, q in by.values()):
        return ("needs_eps_4_1_moment", None)
    val, _ = integrate_product(specs)
    return ("eval", str(val))

def plaq_dict(x, o):
    return {"boundary": [{"link": {"site": list(ln[0]), "dir": int(ln[1])}, "sign": int(sg)}
                         for ln, sg in boundary(x, o)]}
pairs = {
    "coplanar(s=-1)":      (plaq_dict((0, 0, 0), 0), plaq_dict((0, L - 1, 0), 0)),
    "perpendicular(s=-1)": (plaq_dict((0, 0, 0), 0), plaq_dict((0, 0, 0), 2)),
}
tabs = {}
for name, (Pi, Pr) in pairs.items():
    rows = []
    for kinds in itertools.product(["chi", "chibar"], repeat=5):
        specs = [(Pr, kinds[0]), (Pi, kinds[1]), (Pi, kinds[2]), (Pr, kinds[3]), (Pi, kinds[4])]
        rows.append(pattern_status(specs))
    tabs[name] = rows
ref = tabs["coplanar(s=-1)"]
n_eps = sum(1 for t, _ in ref if t.startswith("needs"))
n_zero = sum(1 for t, v in ref if v == "0")
n_nz = sum(1 for t, v in ref if t == "eval" and v not in (None, "0"))
print(f"\n  NN domino five-trace table: {n_zero} exact zeros, {n_nz} nonzero evaluable, "
      f"{n_eps} require the (4,1)/(1,4) epsilon moment")
gate("ABSTRACT-DOMINO: coplanar and perpendicular s=-1 pairs give IDENTICAL "
     "pattern-by-pattern five-trace status tables",
     tabs["coplanar(s=-1)"] == tabs["perpendicular(s=-1)"])
gate("the O(y^3) NN numerator content is PURELY epsilon-mediated: every pattern is "
     "an exact zero except those needing the (4,1)/(1,4) SU(3) moment "
     "(correctly hard-failed by the primitive layer; required input for the d3 layer)",
     n_eps > 0 and n_nz == 0)

# Orbit coarseness inside path classes (relevant only at O(y^4)).
deltas_pp = {(d, oi == orr) for (oi, orr, d, s) in tables["path+1"]}
has_straight = any(max(abs(c) for c in d) == 2 for d, _ in deltas_pp)
has_bent = any(max(abs(c) for c in d) == 1 for d, _ in deltas_pp)
gate("path+ lumps inequivalent geometries (straight |delta|=2 AND bent |delta|=1 entries) "
     "-> orbit-resolved cards needed before the O(y^4) program", has_straight and has_bent)

print("=" * 78)
print(f"ALL {len(PASS)} GATES PASSED")
print("=" * 78)
print("""
CONCLUSIONS:
  1. The uploaded geometry contract is exactly right as algebra: equal lifter
     weights <=> the two-hop layer assembles into a*I + b*S + c*S^2, which acts
     as a constant on the flat line; the corner class alone provably lifts.
  2. The physical O(y^3) answer is W(path+) = W(path-) = W(corner) = 0:
     three-distinct-plaquette processes die on the middle plaquette's bare
     links (>= 2 of them, exact gate) -- a single chi_q insertion deposits
     unremovable fundamental flux there.  The contract holds with margin.
  3. Trominoes first activate at O(y^4) (chi-chibar pair on the middle:
     nonzero numerators found).
  4. The surviving O(y^3) terms live on <= 2 plaquettes.  The NN numerator
     tables are embedding-blind (coplanar == perpendicular at fixed s), the
     epsilon channel enters through the (4,1)/(1,4) moment, and sigma-
     covariance forces the NN amplitude to be s * (universal constant).
     Hence O(y^3) C-odd H_eff = alpha*I + b*S: the flat band stays EXACTLY
     FLAT at O(y^3), rigidly shifted by (alpha - 4b) y^3.
""")
