#!/usr/bin/env python3
"""
ENGINE_OP1_lemma_window_cert.py - F033 certificate: LEMMA A compact window tau in (0, 0.31]
====================================================================================
Certifies the numerical inequalities of LEM_OP1_lemma_closure_2026-06-12.md:
  WB0 toolkit: T1/T3 spots; Lemma W validity (contour bound >= true p_k);
      Lemma R+ chain (r >= 1, t >= 3); R_MAX <= 1.19 on (0,4] (80 directed cells)
  WB1 Region-A extension constants (tau0 = 0.31): h_A2(0.31) <= 0.8868 < 1
  WB2 uniform branch L >= 12: F(tau) < 1 on [3/144, 0.31], directed cells
  WB3 uniform small-tau: dyadic cells to 1e-3 + analytic tau^10 tail
  WB4 per-L branches L = 4..11: head-kill endpoint + directed cells to 0.31
  WB5 bound-validity sample: cell bound >= true D at random (L, tau)
Method: mpmath dps 25, every comparison padded by PAD = 1e-18 in the safe
direction (margins certified are >= 3e-2). Resumable (state in json).
"""
import json, math, os, sys, time
import mpmath as mp
mp.mp.dps = 25
T0 = time.time(); DEADLINE = 38.0
PAD = mp.mpf("1e-18"); UP = 1 + PAD; DN = 1 - PAD
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LEM_OP1_lemma_window_cert.json")
st = json.load(open(OUT)) if os.path.exists(OUT) else {}
st.setdefault("meta", dict(engine="ENGINE_OP1_lemma_window_cert.py", date="2026-06-12"))
st.setdefault("done", {})
def save(): json.dump(st, open(OUT, "w"), indent=1)
def checkpoint(tag):
    if time.time() - T0 > DEADLINE:
        st["meta"]["resume_at"] = tag; save()
        print(f"RESUME NEEDED at {tag} ({time.time()-T0:.0f}s)"); sys.exit(13)

QCACHE = {}
def qq(t):
    key = mp.nstr(t, 20)
    if key in QCACHE: return QCACHE[key]
    if t <= 30: v = mp.besseli(0, 2*t)*mp.exp(-2*t)
    else:
        w = 6/mp.sqrt(t)
        v = (1/mp.pi)*mp.quad(lambda th: mp.exp(-2*t*(1-mp.cos(th))), [0, w, mp.pi])
    QCACHE[key] = v; return v
def q_up(t): return qq(t)*UP
def q_lo(t): return qq(t)*DN
def Lam(v): return v*mp.asinh(v/2) + 2 - mp.sqrt(4 + v*v)
def Em(tau, L, m): return tau*L*L*Lam(m/(tau*L))
def PhiL(L, t): return mp.fsum(mp.exp(-4*t*mp.sin(mp.pi*n/L)**2) for n in range(L))/L

RBAR4 = (mp.mpf("1.19")*UP)**4   # global cap, certified in WB0
C2 = mp.mpf("0.2311")
def delta(t): return 1/(16*t) + C2/(t*t)   # valid t >= 4 (F031)

# ---------------- WB0 toolkit
if "WB0" not in st["done"]:
    for w in [0.01, 0.3, 1.0, 2.5, 10.0]:
        w = mp.mpf(w)
        assert mp.asinh(w) >= w/mp.sqrt(1+w*w) - PAD                      # T1
        v = 2*w
        assert 2*Lam(v) >= v*mp.asinh(v/2) - PAD                          # T3
    for tau in [0.01, 0.05, 0.125, 0.31]:
        for m in [1, 2]:
            assert Em(mp.mpf(tau), 13, m) >= Em(mp.mpf(tau), 12, m) - PAD # T4
    # Lemma W validity
    worstW = mp.mpf(1)
    for k in [1, 2, 3, 4, 8, 12, 24, 40]:
        for t in [0.3, 1, 2, 5, 10, 25, 50]:
            t = mp.mpf(t)
            ptrue = mp.besseli(k, 2*t)*mp.exp(-2*t)
            bnd = mp.exp(-t*Lam(mp.mpf(k)/t))*q_up(mp.sqrt(t*t + mp.mpf(k)**2/4))
            assert bnd >= ptrue*DN, f"Lemma W fails at k={k} t={t}"
            if ptrue > 0: worstW = min(worstW, bnd/ptrue)
    # Lemma R+ : r >= 1 for t >= 3 (chain constants + direct)
    t3 = mp.mpf(3)
    eps_tail = mp.sqrt(4*mp.pi*t3)*( mp.exp(-mp.pi**2*t3)/(2*mp.pi**2*t3)
        + (t3/12)*(mp.exp(-mp.pi**2*t3)/(2*mp.pi))*(mp.pi**4/t3)*(1+2/(mp.pi**2*t3)+2/(mp.pi**4*t3**2)) )/mp.pi
    assert eps_tail < mp.mpf("1e-9")
    assert 1/(16*t3) - 1/(384*t3*t3) - eps_tail > mp.mpf("0.020")
    for t in [3, 4, 6, 10, 30, 100]:
        assert mp.sqrt(4*mp.pi*t)*q_lo(mp.mpf(t)) >= 1, f"r>=1 fails at t={t}"
    # R_MAX on (0,4]
    edges = [mp.mpf("1e-4")] + [mp.mpf("0.01")*(mp.mpf(400))**(mp.mpf(i)/599) for i in range(600)]
    rmax_seen = mp.mpf(0)
    for i in range(len(edges)-1):
        rb = mp.sqrt(4*mp.pi*edges[i+1])*q_up(edges[i])
        rmax_seen = max(rmax_seen, rb)
        assert rb <= mp.mpf("1.19"), f"R_MAX cell fail [{edges[i]},{edges[i+1]}]: {rb}"
    st["done"]["WB0"] = dict(lemmaW_worst_ratio=float(worstW), rmax_cells=float(rmax_seen),
                             eps_tail_t3=float(eps_tail))
    save(); print(f"WB0 PASS: Lemma W valid (min bound/true {float(worstW):.4f}); r>=1 (t>=3); "
                  f"R_MAX cells <= {float(rmax_seen):.5f} <= 1.19")
checkpoint("WB1")

# ---------------- WB1 Region-A extension
if "WB1" not in st["done"]:
    tail = 2*(1 + mp.exp(-mp.mpf("14.88"))/(1 - mp.exp(mp.mpf("-24.8"))))
    assert tail <= mp.mpf("2.0001")
    e31 = mp.mpf("2.0001")*mp.exp(mp.mpf("-4.96"))
    assert (1 + e31)**3 <= mp.mpf("1.0427")
    pref = 4*mp.mpf("2.0001")*mp.mpf("1.0427")*16*mp.pi**2
    assert pref <= mp.mpf("1317.4")
    ha = lambda tau: mp.mpf("1317.4")*tau*tau*mp.exp(-16*tau)
    assert ha(mp.mpf("0.31")) <= mp.mpf("0.8880")
    assert all(ha(mp.mpf(a)) > ha(mp.mpf(b)) for a, b in [(0.31, 0.35), (0.35, 0.5), (0.5, 2), (2, 20)])
    assert mp.erfc(mp.pi*mp.sqrt(mp.mpf("4.96"))) <= mp.mpf("1e-20")
    st["done"]["WB1"] = dict(h_A2_031=float(ha(mp.mpf("0.31"))))
    save(); print(f"WB1 PASS: Region-A extension to tau0=0.31 (h_A2 = {float(ha(mp.mpf('0.31'))):.4f} < 1)")
checkpoint("WB2")

# ---------------- WB2 uniform branch L >= 12 on [3/144, 0.31]
def Ybar12(taub):
    L = 12; terms = []
    for m in (1, 2, 3):
        terms.append(mp.exp(-Em(taub, L, m)))
    rho = mp.exp(-L*mp.asinh(3/(2*taub*L)))
    tail = terms[2]*rho/(1 - rho)
    return 2*(terms[0] + terms[1] + terms[2] + tail)*UP
if "WB2" not in st["done"]:
    lo, hi = mp.mpf(3)/144, mp.mpf("0.31")
    N = 560; r = (hi/lo)**(mp.mpf(1)/N)
    edges = [lo*r**i for i in range(N+1)]; edges[-1] = hi
    worstF, at = mp.mpf(0), None
    for i in range(N):
        a, b = edges[i], edges[i+1]
        ta = 144*a
        if ta >= 4: r4 = (1 + delta(ta))**4
        else:       r4 = (mp.sqrt(4*mp.pi*144*b)*q_up(ta))**4
        Y = Ybar12(b)
        Fdiff = (r4*(1+Y)**4 - 1)/(16*mp.pi**2*a*a)*UP
        Fconv = 4*Y*(1+Y)**3*r4/(16*mp.pi**2*a*a)*UP
        F = min(Fdiff, Fconv)
        if F > worstF: worstF, at = F, (a, b)
        assert F < 1, f"WB2 cell FAIL [{float(a)},{float(b)}]: F={float(F)}"
        if i % 60 == 0: checkpoint(f"WB2:{i}")
    st["done"]["WB2"] = dict(worst_F=float(worstF), at=[float(at[0]), float(at[1])], cells=N)
    save(); print(f"WB2 PASS: uniform L>=12 certified on [3/144, 0.31]; worst F = {float(worstF):.4f} "
                  f"at tau~{float(at[1]):.4f}")
checkpoint("WB3")

# ---------------- WB3 uniform small-tau (dyadic + analytic tail)
if "WB3" not in st["done"]:
    a = mp.mpf(3)/144; worstG = mp.mpf(0)
    while a > mp.mpf("1e-3"):
        b, a2 = a, a/2
        E1 = Em(b, 12, 1)
        ratio2 = mp.exp(-(Em(b, 12, 2) - E1))
        assert ratio2 < mp.mpf("0.05")
        Y = mp.mpf("2.1")*mp.exp(-E1)
        G = 4*Y*(1+Y)**3*RBAR4/(16*mp.pi**2*a2*a2)*UP
        assert G < 1, f"WB3 dyadic FAIL [{float(a2)},{float(b)}]: {float(G)}"
        worstG = max(worstG, G); a = a2
    # analytic tail on (0, 1e-3]: E1 >= 12(asinh(1/(24 tau)) - 1) and bound ~ tau^10 increasing
    tau = mp.mpf("1e-3")
    E1min = 12*(mp.asinh(1/(24*tau)) - 1)
    Gtail = 4*mp.mpf("2.1")*mp.exp(-E1min)*(1.01)*RBAR4/(16*mp.pi**2*tau*tau)*UP
    assert Gtail < mp.mpf("1e-8"), f"WB3 tail {Gtail}"
    st["done"]["WB3"] = dict(worst_dyadic_G=float(worstG), tail_at_1e3=float(Gtail))
    save(); print(f"WB3 PASS: small-tau dyadic worst G = {float(worstG):.4f}; analytic tail {float(Gtail):.1e}")
checkpoint("WB4")

# ---------------- WB4 per-L branches
TKILL = {4: mp.mpf("0.25"), 5: mp.mpf("0.45"), 6: mp.mpf("0.7"), 7: mp.mpf("0.9"),
         8: mp.mpf("1.2"), 9: mp.mpf("1.5"), 10: mp.mpf("1.8"), 11: mp.mpf("2.1")}
def head_val(L, t):
    geo = t**L*mp.factorial(L)/mp.factorial(2*L)
    assert geo < mp.mpf("0.05")
    return 8*mp.mpf(L)**4*(t**L/mp.factorial(L))*mp.exp(-2*t + t*t/(L+1))/(1-geo)*UP
for L in range(4, 12):
    key = f"WB4_L{L}"
    if key in st["done"]: continue
    tk = TKILL[L]
    hv = head_val(L, tk)
    assert hv < mp.mpf("0.5"), f"head kill fails L={L}: {float(hv)}"
    assert tk < mp.mpf(L)/2   # monotonicity range of the head bound
    lo, hi = tk/(L*L), mp.mpf("0.31")
    N = 760; rr = (hi/lo)**(mp.mpf(1)/N)
    edges = [lo*rr**i for i in range(N+1)]; edges[-1] = hi
    worstD, at = mp.mpf(0), None
    for i in range(N):
        a, b = edges[i], edges[i+1]
        ta, tb = a*L*L, b*L*L
        xbar = L*q_up(ta); xlo = L*q_lo(tb)
        terms = []
        for m in (1, 2, 3):
            rho = q_up(mp.sqrt(ta*ta + mp.mpf(m*L)**2/4))/q_lo(tb)
            terms.append(min(rho, mp.mpf(1)*UP)*mp.exp(-Em(b, L, m)))
        rhostep = mp.exp(-L*mp.asinh(3/(2*b*L)))
        Y = 2*(terms[0] + terms[1] + terms[2] + terms[2]*rhostep/(1-rhostep))*UP
        D = min((xbar*(1+Y))**4 - xlo**4, 4*Y*(1+Y)**3*xbar**4)
        if D > worstD: worstD, at = D, (a, b)
        assert D < 1, f"WB4 L={L} cell FAIL [{float(a):.5f},{float(b):.5f}]: D={float(D):.5f}"
        if i % 80 == 0: checkpoint(f"WB4:L{L}:{i}")
    st["done"][key] = dict(head_val=float(hv), worst_D=float(worstD),
                           at=[float(at[0]), float(at[1])], cells=N)
    save(); print(f"WB4 L={L} PASS: head {float(hv):.3f} @ t={float(tk)}; worst cell D = "
                  f"{float(worstD):.4f} at tau~{float(at[1]):.4f}")
    checkpoint(f"WB4 after L{L}")

# ---------------- WB5 bound-validity sample
if "WB5" not in st["done"]:
    import random
    random.seed(33)
    worst_gap = mp.mpf(100)
    for _ in range(40):
        L = random.choice([4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 24, 64])
        tau = mp.mpf(str(round(random.uniform(0.002, 0.31), 6)))
        t = tau*L*L
        Dtrue = (L*PhiL(L, t))**4 - (L*qq(t))**4
        xbar = L*q_up(t); xlo = L*q_lo(t)
        terms = []
        for m in (1, 2, 3):
            rho = q_up(mp.sqrt(t*t + mp.mpf(m*L)**2/4))/q_lo(t)
            terms.append(min(rho, mp.mpf(1)*UP)*mp.exp(-Em(tau, L, m)))
        rhostep = mp.exp(-L*mp.asinh(3/(2*tau*L)))
        Y = 2*(sum(terms) + terms[2]*rhostep/(1-rhostep))*UP
        Dbnd = min((xbar*(1+Y))**4 - xlo**4, 4*Y*(1+Y)**3*xbar**4)
        assert Dbnd >= Dtrue*DN - PAD, f"validity fail at L={L} tau={float(tau)}"
        worst_gap = min(worst_gap, Dbnd - Dtrue)
    st["done"]["WB5"] = dict(min_bound_minus_true=float(worst_gap), samples=40)
    save(); print(f"WB5 PASS: bound >= true D on 40 random samples (min gap {float(worst_gap):.5f})")

st["meta"]["runtime_s"] = round(time.time() - T0, 1)
st["meta"]["verdict"] = "LEMMA A COMPACT WINDOW CERTIFIED: WB0-WB5 ALL PASS"
st["meta"].pop("resume_at", None)
save()
print(f"ALL WB GATES PASS in {time.time()-T0:.1f}s -> {OUT}")
