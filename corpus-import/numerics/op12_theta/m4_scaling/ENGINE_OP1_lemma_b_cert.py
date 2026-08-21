#!/usr/bin/env python3
"""
ENGINE_OP1_lemma_b_cert.py - certified proof engine for LEMMA B (M5 / Tier-2 C-form pin)
==============================================================================
THEOREM (Lemma B; proof in programs/op1_defect_sparsity/LEM_OP1_lemma_b_proof_2026-06-12.md):
    For all mu2 in (0, 15/28]:
        g(mu2) := Y_inf(mu2) - (A/2) ln(3/mu2)  <=  G_BOUND  <  1/28,
    where  Y_inf(mu2) = (3/4) int_0^inf t e^{-mu2 t} q(t)^4 dt,
           q(t) = e^{-2t} I_0(2t),   A = 3/(32 pi^2) = (3/2) c,   c = 1/(16 pi^2).
    Hence C_inf(x) = g(mu2(x)) < 1/28 for ALL x >= 0 on the AF diagonal
    (mu2(x) = 3/(beta(x) e^{2x}) <= mu2(0) = 15/28 exactly), and -- via the
    triple-verified C-form envelope reduction (m5_audit G-M1; F030 Q4/Q5) --
    conditional on Lemma A only:
        T_C <= Tbar(1/28) = 0.124806 < 1/8  =>  N*_C >= 8, T_full < 9/64, N* >= 7
    uniformly on the diagonal.

PROOF SKELETON BEING CERTIFIED (every inequality hard-gated):
  MASTER BOUND (note SS2; T0 = 2):  for all mu2 in (0, M2MAX], M2MAX = 15/28:
      g(mu2) <= (3/4) H(T0) + (A/2) [ R+(T0) + M2MAX*T0 - gamma_E - ln(3*T0) ]
    with H(T0) = int_0^T0 t q^4 dt,  R+(T0) = int_T0^inf (r^4-1)^+ / t dt,
    r(t) = sqrt(4 pi t) q(t).
    Derivation: e^{-mu2 t} <= 1 on the head (cost ZERO); exact extraction
    c E1(mu2 T0) on the tail; (3/4) c = A/2; E1(z) <= -gamma_E - ln z + z
    (Lemma E, elementary); the +-(A/2) ln mu2 terms cancel EXACTLY -- the
    only surviving mu2 dependence is +(A/2) mu2 T0 <= (A/2) M2MAX T0.
  H(2):  certified rational upper Riemann sum, 256 cells, using q decreasing
         (q' = -(2/pi) int (1-cos th) e^{-2t(1-cos th)} dth < 0) and rational
         series brackets  q+(a) = I0_upper(a) * expneg_upper(2a).
  R+(2): [2,4] certified rational cell sum -- only pi^2 enters (r^4 = 16 pi^2
         t^2 q^4, no square roots);  ln(b/a) <= (b-a)/a.
         [4,inf) via the BESSEL UPPER BOUND (note SS3, fully elementary):
             r(t) <= 1 + 1/(16 t) + C2/t^2   for t >= 4,   C2 = 2311/10000,
         from q = (2/pi) int_0^1 e^{-4 t u^2} (1-u^2)^{-1/2} du with the
         Taylor-with-remainder split at b = 4/5 (kappa = (3/8)(5/3)^5 =
         3125/648, 3 kappa/64 = 9375/41472) plus the wrap term
         2 sqrt(pi t) e^{-(64/25) t}  <=  (C2 - 9375/41472)/t^2  on [4,inf)
         (single rational check at t = 4 + log-derivative monotonicity).
         Then r^4 - 1 <= 4 delta(t) (1+delta(4))^3, int_4^inf delta/t dt
         = 1/64 + C2/32 in closed form.
  CONSTANTS: ln 6 = 4 atanh(1/3) + 2 atanh(1/5), rational series brackets.
         pi and gamma_E: CITED intervals (the only non-self-contained
         constants), cross-checked vs mpmath at high precision (LB5).

GATES (all hard asserts):
  LB0 exact structure: mu2(0) == 15/28; A = (3/2)c; diagonal identity
      A x + (A/2) ln beta == (A/2)(ln(1/mu2) + ln 3); Lemma E on a z-grid.
  LB1 bracket validity: q(a) <= q+(a) on all anchors (sampled vs mpmath,
      dps 60) and q+ relative width <= 1e-15; q decreasing on anchors.
  LB2 Bessel upper bound validity: r(t) <= 1 + 1/(16t) + C2/t^2 on a dense
      mpmath grid t in [4, 2e4]; rational wrap-check at t = 4; kappa algebra.
  LB3 H certificate: H_cert >= H_true (mpmath quad) and H_cert - H_true <= 2e-3.
  LB4 R+ certificate: R_cert >= numeric int_2^600 (r^4-1)+/t; excess <= 0.2.
  LB5 constants: cited pi/gamma intervals contain mp.pi/mp.euler; ln6 bracket
      contains mp.log(6), width < 1e-12.
  LB6 ASSEMBLY (pure rational): X_up < 0; G_BOUND = (3/4)H_cert + A2_LO*X_up
      < 1/28 STRICT, margin >= 1/100.  [the certified inequality]
  LB7 consistency with deposited data: float g(mu2(x)) reproduces 4 reference
      C_inf rows (F030 Q2-verified, from ENGINE_OP1_m4_cover_domination_audit.py) <= 2e-9.
  LB8 end-to-end: float g(mu2) <= G_BOUND on a 10-point mu2 grid spanning
      (0, 15/28]; min slack recorded (expected ~ G_BOUND - C_infinity).
  LB9 bookkeeping: runtime, json written.

Run:  python3 ENGINE_OP1_lemma_b_cert.py [cert|float|all]     (default: all; 'cert' is the
      pure-rational certificate LB0-LB6, 'float' the mpmath blocks LB1/2/3/4/5/7/8)
Output: LEM_OP1_lemma_b_cert.json (merged across parts).  Dependency: mpmath only.
Grounds: derived + machine-certified (exact rational arithmetic in the
certified chain; mpmath only in validity/consistency cross-checks).
"""
import json, math, os, sys, time
from fractions import Fraction as F

T_START = time.time()
MODE = sys.argv[1] if len(sys.argv) > 1 else "all"
OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LEM_OP1_lemma_b_cert.json")

# ---------------------------------------------------------------- cited constants
PI_LO  = F(31415926535897932, 10**16)
PI_HI  = F(31415926535897933, 10**16)
GAM_LO = F(5772156649015328, 10**16)
GAM_HI = F(5772156649015329, 10**16)
PI2_HI = PI_HI * PI_HI
SQRTPI_HI = F(17724539, 10**7)          # (asserted below: SQRTPI_HI^2 >= PI_HI)

# ---------------------------------------------------------------- proof parameters
T0     = F(2)
M2MAX  = F(15, 28)
C2     = F(2311, 10000)
KAPPA  = F(3, 8) * F(5, 3)**5           # = 3125/648
K3_64  = 3 * KAPPA / 64                 # = 9375/41472
N_H    = 256                            # H-grid cells on [0, 2]
N_R    = 32                             # R-grid cells on [2, 4]

# ---------------------------------------------------------------- rational series
def expneg_upper(x, n=60):
    """rational upper bound on e^{-x}, x >= 0 rational: e^{-x} <= 1/S_n(x)."""
    s, term = F(1), F(1)
    for k in range(1, n + 1):
        term = term * x / k
        s += term
    return F(1) / s

def i0_upper(t, K=28):
    """rational upper bound on I_0(2t): sum_k t^{2k}/(k!)^2 + geometric tail."""
    t2 = t * t
    s, term = F(1), F(1)
    for k in range(1, K + 1):
        term = term * t2 / (k * k)
        s += term
    ratio = t2 / ((K + 1) * (K + 1))
    assert ratio < 1, "i0_upper: K too small for this t"
    nxt = term * t2 / ((K + 1) * (K + 1))
    return s + nxt / (1 - ratio)

def q_upper(a):
    """certified rational upper bound on q(a) = e^{-2a} I0(2a), a rational >= 0."""
    if a == 0:
        return F(1)
    return i0_upper(a) * expneg_upper(2 * a)

def atanh_brackets(x, n=40):
    """rational lower/upper for atanh(x), 0 < x < 1: positive series + geom tail."""
    s, p = F(0), x
    for k in range(0, n + 1):
        s += p / (2 * k + 1)
        p = p * x * x
    tail = p / ((2 * n + 3) * (1 - x * x))
    return s, s + tail

# ---------------------------------------------------------------- certified pieces
def build_H_cert():
    h = T0 / N_H
    total = F(0)
    anchors = []
    for i in range(N_H):
        a, b = i * h, (i + 1) * h
        qa = q_upper(a)
        total += qa**4 * (b * b - a * a) / 2
        if i % 16 == 0:
            anchors.append((a, qa))
    return total, anchors

def build_R24_cert():
    h = F(2) / N_R
    total = F(0)
    anchors = []
    for i in range(N_R):
        a, b = 2 + i * h, 2 + (i + 1) * h
        qa = q_upper(a)
        r4_up = 16 * PI2_HI * b * b * qa**4          # >= r(t)^4 on [a,b]
        excess = r4_up - 1
        if excess > 0:
            total += excess * h / a                   # ln(b/a) <= (b-a)/a
        if i % 4 == 0:
            anchors.append((a, qa))
    return total, anchors

def build_R4inf_cert():
    delta4 = F(1, 64) + C2 / 16
    factor = 4 * (1 + delta4)**3
    integral = F(1, 64) + C2 / 32
    return factor * integral, delta4

def wrap_check_rational():
    """certify 2 sqrt(pi t) e^{-(64/25)t} <= (C2 - 3k/64)/t^2 at t=4; +monotone."""
    dC = C2 - K3_64
    assert dC > 0, "wrap budget non-positive"
    assert SQRTPI_HI**2 >= PI_HI, "sqrt-pi upper invalid"
    lhs_up = 4 * SQRTPI_HI * expneg_upper(F(256, 25), n=80)   # 2*sqrt(4pi)*e^{-10.24}
    rhs_lo = dC / 16
    assert lhs_up <= rhs_lo, f"wrap check fails at t=4: {float(lhs_up)} vs {float(rhs_lo)}"
    # log-derivative of t^{5/2} e^{-(64/25)t} is 5/(2t) - 64/25 < 0 for t >= 4:
    assert 5 * 25 < 2 * 64 * 4, "monotonicity precondition"
    return float(lhs_up), float(rhs_lo)

# ================================================================ certificate part
out = {}
if os.path.exists(OUT_PATH):
    try:
        out = json.load(open(OUT_PATH))
    except Exception:
        out = {}
out.setdefault("meta", {})
out["meta"].update(dict(engine="ENGINE_OP1_lemma_b_cert.py", date="2026-06-12",
                        statement="g(mu2) <= G_BOUND < 1/28 for mu2 in (0, 15/28]",
                        mode_last=MODE))

if MODE in ("cert", "all"):
    # ---- LB0 exact structure
    assert F(48) / (F(28, 5) * 16) == F(15, 28)
    assert K3_64 == F(9375, 41472)
    assert KAPPA == F(3125, 648)
    out["LB0"] = dict(mu2_x0="15/28", kappa="3125/648", k3_64="9375/41472", passed=True)
    print("LB0 PASS: mu2(0)=15/28 exact; kappa algebra exact")

    # ---- LB6 ingredients (pure rational)
    H_cert, H_anchors = build_H_cert()
    R24, R_anchors = build_R24_cert()
    R4inf, delta4 = build_R4inf_cert()
    wrap_lhs, wrap_rhs = wrap_check_rational()
    R_cert = R24 + R4inf

    at3_lo, at3_hi = atanh_brackets(F(1, 3))
    at5_lo, at5_hi = atanh_brackets(F(1, 5))
    LN6_LO = 4 * at3_lo + 2 * at5_lo
    LN6_HI = 4 * at3_hi + 2 * at5_hi

    X_up = R_cert + M2MAX * T0 - GAM_LO - LN6_LO
    assert X_up < 0, f"X_up not negative: {float(X_up)}"
    A2_LO = F(3, 64) / PI2_HI
    G_BOUND = F(3, 4) * H_cert + A2_LO * X_up
    margin = F(1, 28) - G_BOUND
    assert G_BOUND < F(1, 28), "LB6 FAIL: G_BOUND >= 1/28"
    assert margin >= F(1, 100), f"LB6 FAIL: margin {float(margin)} < 1/100"

    out["LB6"] = dict(
        H_cert=float(H_cert), R24_cert=float(R24), R4inf_cert=float(R4inf),
        R_cert=float(R_cert), delta4=float(delta4),
        wrap_lhs_up=wrap_lhs, wrap_rhs_lo=wrap_rhs,
        ln6_bracket=[float(LN6_LO), float(LN6_HI)],
        X_up=float(X_up), A2_LO=float(A2_LO),
        G_BOUND=float(G_BOUND), threshold=float(F(1, 28)), margin=float(margin),
        margin_ratio=float(F(1, 28) / G_BOUND),
        n_cells_H=N_H, n_cells_R=N_R, T0=float(T0), C2=float(C2), passed=True)
    # exact rationals (decimal strings, 24 digits) for the record
    def dec(fr, nd=24):
        sign = "-" if fr < 0 else ""
        fr = abs(fr); ip = fr.numerator // fr.denominator
        rem = fr - ip
        digs = (rem * 10**nd).numerator // (rem * 10**nd).denominator
        return f"{sign}{ip}.{str(digs).zfill(nd)}"
    out["LB6"]["G_BOUND_dec"] = dec(G_BOUND)
    out["LB6"]["margin_dec"] = dec(margin)
    print(f"LB6 PASS: G_BOUND = {float(G_BOUND):.12f} < 1/28 = {1/28:.12f}; "
          f"margin = {float(margin):.12f} (ratio {float(F(1,28)/G_BOUND):.4f})")
    print(f"   pieces: (3/4)H = {0.75*float(H_cert):.12f}  H_cert = {float(H_cert):.12f}")
    print(f"           R+ = {float(R_cert):.6f} (= {float(R24):.6f} on [2,4] + {float(R4inf):.6f} on [4,inf))")
    print(f"           X_up = {float(X_up):.9f}  (A/2)X_up = {float(A2_LO*X_up):.12f}")

    out["meta"]["anchors_H"] = [[str(a), str(q)] for a, q in H_anchors[:4]]
    out["meta"]["runtime_cert_s"] = round(time.time() - T_START, 3)
    json.dump(out, open(OUT_PATH, "w"), indent=1)
    print(f"certificate part done in {time.time()-T_START:.1f}s")

# ================================================================ float part
if MODE in ("float", "all"):
    import mpmath as mp
    mp.mp.dps = 22

    def qf(t):  return mp.besseli(0, 2 * t) * mp.exp(-2 * t)
    def rf(t):  return mp.sqrt(4 * mp.pi * t) * qf(t)

    C_F = 1 / (16 * mp.pi**2); A_F = 3 / (32 * mp.pi**2)

    def Yinf_f(mu2, T0f=24, T1f=40000):
        v0 = mp.quad(lambda t: t * mp.e**(-mu2 * t) * qf(t)**4, [0, F(1, 2), 3, 10, T0f])
        fr_ = lambda t: mp.e**(-mu2 * t) * (t * qf(t)**4 - C_F / t - C_F / (4 * t * t))
        vr = mp.quad(fr_, [T0f, 100, 1000, T1f])
        vlog = C_F * mp.e1(mu2 * T0f)
        vsq = (C_F / 4) * (mp.e**(-mu2 * T0f) / T0f - mu2 * mp.e1(mu2 * T0f))
        return 0.75 * (v0 + vr + vlog + vsq)

    def g_f(mu2):  return Yinf_f(mu2) - (A_F / 2) * mp.log(3 / mu2)

    def C_inf_f(x):
        beta = F(28, 5) + 11 / (8 * mp.pi**2) * x
        mu2 = 48 / (beta * (4 * mp.e**x)**2)
        return Yinf_f(mu2) - A_F * x - (A_F / 2) * mp.log(beta)

    # ---- LB0b: diagonal identity + Lemma E (float)
    for x in [0, mp.mpf("1.7"), mp.mpf("6.3")]:
        beta = F(28, 5) + 11 / (8 * mp.pi**2) * x
        mu2 = 48 / (beta * (4 * mp.e**x)**2)
        lhs = A_F * x + (A_F / 2) * mp.log(beta)
        rhs = (A_F / 2) * (mp.log(1 / mu2) + mp.log(3))
        assert abs(lhs - rhs) < mp.mpf("1e-24"), "diagonal identity fails"
    for z in ["1e-6", "1e-3", "0.05", "0.3", str(float(F(15, 14))), "3", "10"]:
        z = mp.mpf(z)
        v = mp.e1(z) + mp.euler + mp.log(z)
        assert -mp.mpf("1e-20") <= v <= z + mp.mpf("1e-20"), "Lemma E numeric check fails"
    out["LB0b"] = dict(passed=True)
    print("LB0b PASS: diagonal identity + Lemma E (0 <= E1+gamma+ln z <= z) verified")

    # ---- LB1 bracket validity (sampled anchors, dps 60)
    mp.mp.dps = 60
    worst_gap, worst_rel, prev_q = None, 0.0, None
    samples = sorted(set([F(i, 32) for i in range(0, 65, 4)] +
                         [2 + F(i, 16) for i in range(0, 33, 4)]))
    for a in samples:
        if a == 0:
            continue
        qa_true = mp.besseli(0, 2 * mp.mpf(a.numerator) / a.denominator) * \
                  mp.exp(-2 * mp.mpf(a.numerator) / a.denominator)
        qa_up = mp.mpf(q_upper(a).numerator) / mp.mpf(q_upper(a).denominator)
        gap = qa_up - qa_true
        assert gap >= -mp.mpf("1e-50"), f"q_upper INVALID at t={a}"
        rel = float(gap / qa_true)
        worst_rel = max(worst_rel, rel)
        if prev_q is not None:
            assert qa_true < prev_q, "q not decreasing?!"
        prev_q = qa_true
    assert worst_rel <= 1e-15, f"bracket too loose: {worst_rel}"
    mp.mp.dps = 22
    out["LB1"] = dict(worst_rel_width=worst_rel, n_samples=len(samples), passed=True)
    print(f"LB1 PASS: q+ brackets valid; worst relative width {worst_rel:.2e}")

    # ---- LB2 Bessel upper bound validity on [4, 2e4]
    min_slack, min_t = None, None
    tgrid = [mp.mpf(4) * mp.mpf(10)**(mp.mpf(i) / 135) for i in range(0, 500)]
    for t in tgrid:
        bound = 1 + 1 / (16 * t) + mp.mpf(C2.numerator) / C2.denominator / t**2
        slack = bound - rf(t)
        if min_slack is None or slack < min_slack:
            min_slack, min_t = slack, t
    assert min_slack > 0, f"LB2 FAIL: bound violated at t={min_t}"
    out["LB2"] = dict(min_slack=float(min_slack), at_t=float(min_t),
                      n_grid=len(tgrid), passed=True)
    print(f"LB2 PASS: r(t) <= 1 + 1/(16t) + {float(C2)}/t^2 on [4,2e4]; "
          f"min slack {float(min_slack):.3e} at t={float(min_t):.3f}")

    # ---- LB3 / LB4 certificate-vs-truth quality
    H_true = mp.quad(lambda t: t * qf(t)**4, [0, F(1, 8), F(1, 2), 1, 2])
    assert "LB6" in out, "run 'cert' part first (LB6 missing from json)"
    H_c = mp.mpf(out["LB6"]["H_cert"])
    assert H_c >= H_true, "H_cert below true value?!"
    assert H_c - H_true <= mp.mpf("2e-3"), f"H_cert too loose: {float(H_c - H_true)}"
    out["LB3"] = dict(H_true=float(H_true), H_cert=float(H_c),
                      excess=float(H_c - H_true), passed=True)
    print(f"LB3 PASS: H_true = {float(H_true):.9f}, H_cert = {float(H_c):.9f} "
          f"(excess {float(H_c - H_true):.2e})")

    Rnum = mp.quad(lambda t: max(rf(t)**4 - 1, mp.mpf(0)) / t, [2, 4, 20, 100, 600])
    R_c = mp.mpf(out["LB6"]["R_cert"])
    assert R_c >= Rnum, "R_cert below numeric truth?!"
    assert R_c - Rnum <= mp.mpf("0.2"), f"R_cert too loose: {float(R_c - Rnum)}"
    out["LB4"] = dict(R_numeric_2_600=float(Rnum), R_cert=float(R_c),
                      excess=float(R_c - Rnum), passed=True)
    print(f"LB4 PASS: R+ numeric [2,600] = {float(Rnum):.6f}, R_cert = {float(R_c):.6f}")

    # ---- LB5 cited constants  (dps 60: the ln6 series bracket is ~1e-41 wide,
    # so the comparison must run well below that conversion-rounding scale)
    mp.mp.dps = 60
    assert mp.mpf(PI_LO.numerator) / PI_LO.denominator < mp.pi < mp.mpf(PI_HI.numerator) / PI_HI.denominator
    assert mp.mpf(GAM_LO.numerator) / GAM_LO.denominator < mp.euler < mp.mpf(GAM_HI.numerator) / GAM_HI.denominator
    at3_lo, at3_hi = atanh_brackets(F(1, 3)); at5_lo, at5_hi = atanh_brackets(F(1, 5))
    l6lo = 4 * at3_lo + 2 * at5_lo; l6hi = 4 * at3_hi + 2 * at5_hi
    assert mp.mpf(l6lo.numerator) / l6lo.denominator < mp.log(6) < mp.mpf(l6hi.numerator) / l6hi.denominator
    assert float(l6hi - l6lo) < 1e-12
    mp.mp.dps = 22
    out["LB5"] = dict(ln6_width=float(l6hi - l6lo), passed=True)
    print("LB5 PASS: pi/gamma cited intervals + ln6 series bracket verified")

    # ---- LB7 consistency with F030-verified C_inf rows
    REF = [(0.0, 0.010666266672), (math.log(47 / 4), 0.012754714524),
           (10.0, 0.012792103131), (20.0, 0.012792103147)]
    worst = 0.0
    for x, ref in REF:
        v = float(C_inf_f(mp.mpf(x)))
        worst = max(worst, abs(v - ref))
        assert abs(v - ref) <= 2e-9, f"LB7 FAIL at x={x}: {v} vs {ref}"
    out["LB7"] = dict(worst_abs_dev=worst, rows=len(REF), passed=True)
    print(f"LB7 PASS: reproduces F030-verified C_inf rows (worst dev {worst:.2e})")

    # ---- LB8 end-to-end: g(mu2) <= G_BOUND on the range
    GB = mp.mpf(out["LB6"]["G_BOUND"])
    grid = [F(15, 28), F(2, 5), F(1, 4), F(3, 20), F(2, 25), F(1, 25),
            F(1, 50), F(1, 100), F(1, 250), F(1, 1000)]
    min_slack8, at8 = None, None
    gvals = []
    for m in grid:
        gv = g_f(mp.mpf(m.numerator) / m.denominator)
        gvals.append((float(m), float(gv)))
        slack = GB - gv
        assert slack > 0, f"LB8 FAIL: g({float(m)}) = {float(gv)} > G_BOUND"
        if min_slack8 is None or slack < min_slack8:
            min_slack8, at8 = slack, m
    out["LB8"] = dict(min_slack=float(min_slack8), at_mu2=float(at8),
                      g_values=gvals, passed=True)
    print(f"LB8 PASS: g(mu2) <= G_BOUND on 10-pt grid; min slack "
          f"{float(min_slack8):.6f} at mu2={float(at8)}")

    out["meta"]["runtime_total_s"] = round(time.time() - T_START, 3)
    json.dump(out, open(OUT_PATH, "w"), indent=1)
    print(f"ALL GATES PASS in {time.time()-T_START:.1f}s -> {OUT_PATH}")
