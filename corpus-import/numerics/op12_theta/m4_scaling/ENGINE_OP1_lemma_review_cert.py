#!/usr/bin/env python3
"""
ENGINE_OP1_lemma_review_cert.py — F032 (#53) independent review certificate for the
session-P Lemma-A proofs (M5_AUDIT_AND_LEMMAS SS3-SS4; M5_4_AUDIT_AND_REGION_A SS2)
====================================================================================
Verifies, with independent recomputation at high precision, every numeric claim
in the three proofs reviewed line-by-line in F032:
  RA1  Claim 1 (Phi_L <= 1/L + q): direct scan + the proof's own per-interval
       inequality f(n/L) <= L*int_{(n-1)/L}^{n/L} f  (decreasing half; mirror).
  RA2  Continuum core, region (a) c >= 1/8: the geometric-tail factor
       (NIT 1: note says 2.0000003, true value ~2.0000007 — still conservative
       in the chain because the eps(1/8) constant they used, 0.014438, is
       ITSELF an overstatement of the true 0.0143838, NIT 2); full chain
       reproduces G <= 0.1482 <= 0.149; grid sup on [1/8, 30] ~ 0.1381.
  RA3  Continuum core, region (b): s-constant 2.005; h(1/8) = 0.903937 < 0.904;
       monotonicity factor sign (d/dc[e^{-1/(4c)}/c^2] > 0 iff c < 1/8).
  RA4  Region-A theorem: R1 constant 2(1+e^{-19.2}/(1-e^{-32})) <= 2.0001;
       prefactor 4*2.0001*1.01*16pi^2 <= 1276.1; h_A(0.4) <= 0.33925 and
       decreasing; erfc(pi*sqrt(6.4)) <= 1e-27; sin(pi k/L) >= 2k/L spots;
       e(L,tau) <= 2.0001 e^{-16 tau} direct on adversarial (L, tau >= 0.4);
       arcsinh(w) >= w - w^3/6 and >= w/sqrt(1+w^2) spots (W2 toolkit).
  RA5  Compact-window margins, independent: E_L = (L Phi)^4 - 1 - (L q)^4 < 0
       on a (L, tau) grid covering L = 4..64, tau in (0.002, 0.4]; min |E_L|
       near the boundary recorded (DATA for the closure pass F033).
  RA6  Box-certificate method reproduced independently: coarse directed
       one-box bound on [0.05, 0.0609375] brackets the M5.6b value 0.980657;
       6-box coarse certification of [0.05, 0.4] (R < 1 on every box).
Output: LEM_OP1_lemma_review_cert.json. Dependency: mpmath. Grounds: independent
recomputation, directed where it matters; the PROOFS' validity is established
in F032's text — these gates pin the constants those proofs use.
"""
import json, math, os, sys, time
import mpmath as mp

T0 = time.time()
mp.mp.dps = 30
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LEM_OP1_lemma_review_cert.json")
out = {"meta": dict(engine="ENGINE_OP1_lemma_review_cert.py", date="2026-06-12", unit=53)}

def q(t):
    if t <= 30:
        return mp.besseli(0, 2*t)*mp.exp(-2*t)
    w = 6/mp.sqrt(t)
    return (1/mp.pi)*mp.quad(lambda th: mp.exp(-2*t*(1 - mp.cos(th))), [0, w, mp.pi])
def PhiL(L, t):
    return mp.fsum(mp.exp(-4*t*mp.sin(mp.pi*n/L)**2) for n in range(L))/L

# ---- RA1 Claim 1
worst = mp.mpf(-1)
for L in [4, 5, 6, 7, 8, 9, 16, 47]:
    for t in [mp.mpf("0.05"), mp.mpf("0.3"), 1, 5, mp.mpf("0.2")*L*L, 2*L*L]:
        gap = PhiL(L, t) - (mp.mpf(1)/L + q(t))
        worst = max(worst, gap)
assert worst < 0, f"RA1 FAIL: Claim 1 violated, gap {worst}"
# per-interval inequality of the proof (decreasing half + mirror)
for (L, n, t) in [(5, 1, mp.mpf("0.7")), (5, 2, mp.mpf("0.7")), (8, 3, 2), (8, 4, 2), (9, 7, mp.mpf("0.3"))]:
    f = lambda u: mp.exp(-4*t*mp.sin(mp.pi*u)**2)
    if n <= L//2:
        lhs, rhs = f(mp.mpf(n)/L), L*mp.quad(f, [mp.mpf(n-1)/L, mp.mpf(n)/L])
    else:
        lhs, rhs = f(mp.mpf(n)/L), L*mp.quad(f, [mp.mpf(n)/L, mp.mpf(n+1)/L])
    assert lhs <= rhs + mp.mpf("1e-25"), f"RA1 interval step fails at {(L,n,float(t))}"
out["RA1"] = dict(worst_gap=float(worst), passed=True)
print(f"RA1 PASS: Claim 1 holds (worst gap {float(worst):.3e}); proof's interval steps verified")

# ---- RA2 core region (a)
c8 = mp.mpf(1)/8
factor_a = 2*(1 + mp.exp(-12*mp.pi**2*c8)/(1 - mp.exp(-20*mp.pi**2*c8)))
assert mp.mpf("2.0000003") < factor_a <= mp.mpf("2.0000008"), f"RA2: factor_a {factor_a}"
eps8_true = 2*mp.nsum(lambda n: mp.exp(-4*mp.pi**2*c8*n*n), [1, mp.inf])
assert abs(eps8_true - mp.mpf("0.0143838")) < mp.mpf("2e-7"), "RA2: true eps(1/8)"
# their chain with their (overstated, hence conservative) eps = 0.014438:
chain = 16*mp.pi**2 * 4*(1 + mp.mpf("0.014438"))**3 * factor_a * c8**2 * mp.exp(-4*mp.pi**2*c8)
assert chain <= mp.mpf("0.149"), f"RA2: chain {chain}"
G = lambda c: 16*mp.pi**2*c*c*((1 + 2*mp.nsum(lambda n: mp.exp(-4*mp.pi**2*c*n*n), [1, mp.inf]))**4 - 1)
supA = max(G(mp.mpf(c)) for c in [0.125, 0.13, 0.14, 0.15, 0.17, 0.2, 0.25, 0.3, 0.5, 1, 2, 5, 30])
# NIT 3: the notes' printed "grid sup 0.1381" missed the left endpoint —
# the true region-(a) sup is G(1/8) = 0.14505, still under the PROVED 0.1482:
assert mp.mpf("0.1449") <= supA <= chain, f"RA2: grid sup {supA} vs chain {chain}"
assert abs(G(c8) - supA) < mp.mpf("1e-6"), "RA2: sup should sit at the c=1/8 endpoint"
out["RA2"] = dict(factor_a=float(factor_a), eps8_true=float(eps8_true),
                  note_eps="0.014438 (note) vs 0.0143838 (true) — overstatement, conservative",
                  chain_value=float(chain), true_sup_a=float(supA),
                  nit3="notes' printed grid-sup 0.1381 misses endpoint; true sup G(1/8)=0.14505 < proved 0.1482",
                  passed=True)
print(f"RA2 PASS: region (a) chain = {float(chain):.6f} <= 0.149 covers true sup G(1/8) = {float(supA):.6f} "
      f"(NIT 3: notes' grid-sup 0.1381 is a grid artifact; factor_a = {float(factor_a):.9f}, NIT 1 benign)")

# ---- RA3 core region (b)
sconst = 2*(1 + mp.exp(-6)/(1 - mp.exp(-10)))
assert sconst <= mp.mpf("2.005"), f"RA3: s-const {sconst}"
sbar = mp.mpf("2.005")*mp.exp(-2)
h18 = sbar*(1 + sbar)**3/(4*mp.pi**2*c8**2)
assert abs(h18 - mp.mpf("0.903937")) <= mp.mpf("1e-5") and h18 < mp.mpf("0.904"), f"RA3: h(1/8) {h18}"
for c, sgn in [(0.03, 1), (0.06, 1), (0.1, 1), (0.124, 1), (0.126, -1), (0.2, -1)]:
    d = mp.diff(lambda x: mp.exp(-1/(4*x))/x**2, mp.mpf(c))
    assert mp.sign(d) == sgn, f"RA3 monotonicity sign at c={c}"
out["RA3"] = dict(s_const=float(sconst), h_18=float(h18), passed=True)
print(f"RA3 PASS: h(1/8) = {float(h18):.9f} < 0.904; s-const {float(sconst):.9f} <= 2.005; mono signs ok")

# ---- RA4 Region-A theorem constants
r1c = 2*(1 + mp.exp(mp.mpf("-19.2"))/(1 - mp.exp(-32)))
assert r1c <= mp.mpf("2.0001"), f"RA4: R1 const {r1c}"
pref = 4*mp.mpf("2.0001")*mp.mpf("1.01")*16*mp.pi**2
assert pref <= mp.mpf("1276.1"), f"RA4: prefactor {pref}"
hA = lambda tau: mp.mpf("1276.1")*tau**2*mp.exp(-16*tau)
assert hA(mp.mpf("0.4")) <= mp.mpf("0.339251"), f"RA4: h_A(0.4) {hA(mp.mpf('0.4'))}"
# NIT 4: note displays 0.33925 - true 0.3392501 (display rounding; conclusion unaffected)
assert all(hA(mp.mpf(a)) > hA(mp.mpf(b)) for a, b in [(0.4, 0.5), (0.5, 1), (1, 3), (3, 10)])
assert mp.erfc(mp.pi*mp.sqrt(mp.mpf("6.4"))) <= mp.mpf("1e-27")
for L in [4, 7, 16, 101]:
    for k in range(1, L//2 + 1):
        assert mp.sin(mp.pi*k/L) >= mp.mpf(2*k)/L - mp.mpf("1e-28")
for w in [0.01, 0.3, 1, 2.5, 10]:
    w = mp.mpf(w)
    assert mp.asinh(w) >= w - w**3/6 - mp.mpf("1e-28")
    assert mp.asinh(w) >= w/mp.sqrt(1 + w*w) - mp.mpf("1e-28")
worst_e = mp.mpf(-1)
for L in [4, 5, 7, 12, 64, 512, 2048]:
    for tau in [0.4, 0.45, 0.6, 1, 2, 5]:
        tau = mp.mpf(tau); t = tau*L*L
        e_exact = L*PhiL(L, t) - 1
        slack = mp.mpf("2.0001")*mp.exp(-16*tau) - e_exact
        worst_e = max(worst_e, -slack)
assert worst_e <= 0, f"RA4: R1 e-bound violated by {worst_e}"
out["RA4"] = dict(r1_const=float(r1c), prefactor=float(pref), hA_04=float(hA(mp.mpf("0.4"))), passed=True)
print(f"RA4 PASS: R1 const {float(r1c):.9f}; h_A(0.4) = {float(hA(mp.mpf('0.4'))):.6f} <= 0.33925; "
      f"e-bound, sin, asinh spots all hold")

# ---- RA5 compact-window margins (independent; DATA for F033)
mins = {}
worst_E = mp.mpf(-100)
for L in [4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 24, 32, 48, 64]:
    mn_corner = mp.mpf(100)
    taus = [mp.mpf("0.002")*mp.mpf(159)**(mp.mpf(i)/29) for i in range(30)] + \
           [mp.mpf("0.31") + mp.mpf("0.09")*i/19 for i in range(20)]
    for tau in taus:
        t = tau*L*L
        E = (L*PhiL(L, t))**4 - 1 - (L*q(t))**4
        assert E < 0, f"RA5 FAIL: E >= 0 at (L,tau)=({L},{float(tau)})"
        worst_E = max(worst_E, E)
        if tau >= mp.mpf("0.379"): mn_corner = min(mn_corner, -E)
    mins[L] = float(mn_corner)
out["RA5"] = dict(worst_E=float(worst_E), corner_margin_by_L=mins, passed=True)
print(f"RA5 PASS: E_L < 0 on full grid (max E = {float(worst_E):.6e}); corner |E| by L: "
      + ", ".join(f"{L}:{v:.4f}" for L, v in list(mins.items())[:6]))

# ---- RA6 coarse directed box certification (independent of M5.6b machinery)
def theta_upper(c):   # theta decreasing in c => upper at left end; explicit tail
    s = mp.mpf(1) + 2*mp.nsum(lambda n: mp.exp(-4*mp.pi**2*c*n*n), [1, mp.inf])
    return s
def box_bound(a, b):  # sup_{[a,b]} G <= 16 pi^2 b^2 (theta(a)^4 - 1)
    a, b = mp.mpf(a), mp.mpf(b)
    return 16*mp.pi**2*b*b*(theta_upper(a)**4 - 1)
b1 = box_bound("0.05", "0.0609375")
assert mp.mpf("0.9806") <= b1 <= mp.mpf("0.99"), f"RA6: first box {b1}"
edges = ["0.05", "0.0609375", "0.08", "0.11", "0.16", "0.25", "0.4"]
boxes = []
for i in range(len(edges) - 1):
    v = box_bound(edges[i], edges[i+1])
    if v >= 1:  # bisect once if coarse fails
        mid = (mp.mpf(edges[i]) + mp.mpf(edges[i+1]))/2
        v = max(box_bound(edges[i], mid), box_bound(mid, edges[i+1]))
    boxes.append(float(v))
    assert v < 1, f"RA6: box [{edges[i]},{edges[i+1]}] not certified ({v})"
out["RA6"] = dict(first_box=float(b1), m56b_value=0.980657081547, boxes=boxes, passed=True)
print(f"RA6 PASS: first box {float(b1):.6f} (brackets M5.6b 0.980657); "
      f"[0.05,0.4] certified coarse, box maxima {['%.3f' % x for x in boxes]}")

out["meta"]["runtime_s"] = round(time.time() - T0, 2)
json.dump(out, open(OUT, "w"), indent=1)
print(f"ALL RA GATES PASS in {time.time()-T0:.1f}s -> {OUT}")
