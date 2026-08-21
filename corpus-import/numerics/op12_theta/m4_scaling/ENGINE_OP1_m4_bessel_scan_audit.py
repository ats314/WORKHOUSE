#!/usr/bin/env python3
"""
ENGINE_OP1_m4_bessel_scan_audit.py - gated, resumable audit of M5_1 (HEAT-KERNEL/BESSEL
FINITE CERTIFICATE + TAIL PIN TEST)
============================================================================
Audits `_M5_1_-_HEAT_KERNEL_BESSEL_FINITE_CERTIFICATE_+_TAIL_PIN_TEST.ipynb`
(md5 664e657c): full integer scan L = 4..4096 of
    Y_L = alpha_W^2 T_C  (exact Bessel/heat-kernel quadrature, notebook's
    algorithm and tolerances reproduced verbatim),  B_L = Y_L - A ln(L/4).

Resumable: state in CERT_OP1_m4_bessel_scan_state.json (deadline-aware, idempotent;
op12_runner pattern).  Run repeatedly until "ALL GATES PASS".

Gates (hard asserts, applied at completion):
  PB1  18 probe rows reproduce the notebook printout (Y, B_L, T_C; rtol 5e-10).
  PB2  Dense closed-form cross-check at L in {4,8,16,32,64,128,256}:
       fresh |Y_dense - Y_bessel| rel <= 5e-12, and both match the notebook's
       printed pairs (rtol 1e-11).
  PB3  B_L strictly increasing over the whole integer scan.
  PB4  max B_L attained at L = 4096, equals notebook value (rtol 1e-9), and
       uniform margin to BCRIT = 57/1210 is >= 0.0286.
  PB5  finite_pass (B_L < BCRIT) and tc_pass (T_C < 1/8) over the full scan.
  PB6  D-law tie-in (F028 concordance + finite-D ridge): with
       D_L := Y_L - A x - (A/2) ln alpha(L),
       (a) D_L < D_infty(F028) for every scanned L - the infinite-lattice
           constant is a strict UPPER ENVELOPE (cover-domination direction);
           on the AF diagonal mu^2 L^2 = 48/beta stays O(1), so D_L does NOT
           converge to D_infty: it peaks and then drifts down;
       (b) the finite-D ridge is at L = 47, D_ridge = 0.018288870942
           (concordant with M5.3's own "finite corrected peak" x = ln(47/4));
       (c) probe-level shape: strictly rising L = 4..64, strictly falling
           L = 64..4096;
       (d) finite-scan headroom D_crit/D_ridge >= 2.44 (sharper than the
           F028 envelope headroom 2.10).
  PB7  Ceiling reduction rows reproduce (closed form x* = beta0/gamma - 2B/A;
       Tbar rtol 1e-9; floors >= 8 on non-boundary rows).  Boundary row at
       BCRIT reported only (float artifact, F028 species).

Output: AUDIT_OP1_m4_bessel_scan.json (gates + decimated table + extrema).
Dependencies: numpy, scipy.
"""
import json, math, os, sys, time
import numpy as np
from scipy.special import ive
from scipy.integrate import quad

BETA0 = 5.6
GAMMA = 11.0 / (8.0 * math.pi**2)
A_LOG = 3.0 / (32.0 * math.pi**2)
B_CRIT = 57.0 / 1210.0
L_MIN, L_MAX = 4, 4096
RTOL, ATOL, BESSEL_REL_CUTOFF = 2e-11, 2e-13, 1e-16
DEADLINE_S = float(os.environ.get("M4SCAN_DEADLINE", "30"))

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "CERT_OP1_m4_bessel_scan_state.json")
OUT = os.path.join(HERE, "AUDIT_OP1_m4_bessel_scan.json")

PROBE_REF = {
    4:    (0.016409733262, 0.016409733262, 0.018837704000),
    5:    (0.018929513065, 0.016809903495, 0.021491037164),
    6:    (0.020959788397, 0.017108331708, 0.023582815295),
    8:    (0.024072902796, 0.017488794098, 0.026705736195),
    12:   (0.028277464892, 0.017841899506, 0.030757138402),
    16:   (0.031164850936, 0.017996633541, 0.033430311864),
    32:   (0.037943192191, 0.018190866098, 0.039377659840),
    64:   (0.044609778729, 0.018273343939, 0.044814680037),
    128:  (0.051240485166, 0.018319941678, 0.049854425192),
    256:  (0.057859881863, 0.018355229678, 0.054549051850),
    512:  (0.064475441604, 0.018386680722, 0.058929847452),
    1024: (0.071089368343, 0.018416498764, 0.063020615427),
    1536: (0.074957793430, 0.018433467162, 0.065287385067),
    2048: (0.077702310355, 0.018445332078, 0.066841838758),
    2560: (0.079831030602, 0.018454442755, 0.068017731009),
    3072: (0.081570264075, 0.018461829110, 0.068959602747),
    3584: (0.083040725621, 0.018468034780, 0.069742928699),
    4096: (0.084314468686, 0.018473381712, 0.070411987445),
}
MAXROW_REF = {"L": 4096, "Y": 0.084314468686484, "B_L": 0.018473381712093798,
              "margin": 0.028634056304435128, "T_C": 0.07041198744457938}
DENSE_REF = {4: (0.016409733262306, 0.016409733262306),
             8: (0.024072902795728, 0.024072902795739),
             16: (0.031164850936144, 0.031164850936149),
             32: (0.037943192190738, 0.037943192190743),
             64: (0.044609778728667, 0.044609778728672),
             128: (0.051240485165503, 0.051240485165508),
             256: (0.057859881862506, 0.057859881862511)}
CEIL_REF = [(0.018473381712, 36.306608, 0.115149144732, 8),
            (0.020, 35.985176, 0.115634993148, 8),
            (0.025, 34.932418, 0.117255356109, 8),
            (0.030, 33.879660, 0.118921775899, 8),
            (0.040, 31.774145, 0.122400870406, 8)]

def beta_of_L(L): return BETA0 + GAMMA * math.log(L / 4.0)
def mu2_of_L(L): return 48.0 / (beta_of_L(L) * L * L)

def Phi_L_bessel(L, t):
    out = float(ive(0, 2.0 * t)); j = 1
    while True:
        term = 2.0 * float(ive(j * L, 2.0 * t))
        out_new = out + term
        if term <= BESSEL_REL_CUTOFF * max(abs(out_new), 1e-300):
            return out_new
        out = out_new; j += 1
        if j > 200000: raise RuntimeError(f"image sum runaway L={L} t={t}")

def Y_bessel(L):
    mu2 = mu2_of_L(L); Ns_inv = 1.0 / float(L)**4
    lam_min = 4.0 * math.sin(math.pi / L)**2
    T_cut = 80.0 / (mu2 + lam_min)
    def integrand(t):
        p = Phi_L_bessel(L, t)
        diff = p**4 - Ns_inv
        if diff < 0 and abs(diff) < 1e-18: diff = 0.0
        return t * math.exp(-mu2 * t) * diff
    val, err = quad(integrand, 0.0, T_cut, epsabs=ATOL, epsrel=RTOL, limit=400)
    kappa = mu2 + lam_min
    tail = (T_cut + 1.0 / kappa) * math.exp(-kappa * T_cut) / kappa
    return 0.75 * (val + abs(err) + tail)

def Y_dense_sum(L, chunk_elems=4_000_000):
    mu2 = mu2_of_L(L)
    ns = np.arange(L // 2 + 1)
    vals = 4.0 * np.sin(np.pi * ns / L)**2
    mult = np.full(len(vals), 2.0); mult[0] = 1.0
    if L % 2 == 0: mult[-1] = 1.0
    V2 = (vals[:, None] + vals[None, :]).ravel()
    C2 = (mult[:, None] * mult[None, :]).ravel()
    nB = len(V2); step = max(1, chunk_elems // nB); S2 = 0.0
    for i in range(0, nB, step):
        R = 1.0 / (mu2 + (V2[i:i + step, None] + V2[None, :]))
        W = C2[i:i + step, None] * C2[None, :]
        S2 += float(np.sum(W * R * R))
    S2 -= 1.0 / (mu2 * mu2)
    return 3.0 * S2 / (4.0 * float(L)**4)

def ceiling_from_B(B):
    x_star = max(BETA0 / GAMMA - 2.0 * B / A_LOG, 0.0)
    beta_star = BETA0 + GAMMA * x_star
    return x_star, 36.0 * (A_LOG * x_star + B) / (beta_star * beta_star)

def load_state():
    if os.path.exists(STATE): return json.load(open(STATE))
    return {"next_L": L_MIN, "rows": []}

def save_state(st):
    tmp = STATE + ".tmp"
    json.dump(st, open(tmp, "w")); os.replace(tmp, STATE)

if __name__ == "__main__":
    t0 = time.time()
    st = load_state()
    if st["next_L"] <= L_MAX:
        L = st["next_L"]
        while L <= L_MAX:
            Y = Y_bessel(L)
            x = math.log(L / 4.0)
            st["rows"].append([L, Y, Y - A_LOG * x])
            L += 1
            if time.time() - t0 > DEADLINE_S:
                st["next_L"] = L; save_state(st)
                print(f"RESUME at L={L} ({len(st['rows'])} rows done, "
                      f"{time.time()-t0:.1f}s)"); sys.exit(3)
        st["next_L"] = L; save_state(st)
    rows = st["rows"]
    assert len(rows) == L_MAX - L_MIN + 1, f"row count {len(rows)}"
    print(f"scan complete: {len(rows)} rows")

    worst1 = 0.0
    for L, (Yr, Br, Tr) in PROBE_REF.items():
        Lq, Y, B = rows[L - L_MIN]
        assert Lq == L
        b = beta_of_L(L); T_C = 36.0 * Y / (b * b)
        for got, ref in ((Y, Yr), (B, Br), (T_C, Tr)):
            rel = abs(got - ref) / max(abs(ref), 1e-300)
            worst1 = max(worst1, rel)
            assert rel <= 5e-10, f"PB1 FAIL L={L}: {got} vs {ref}"
    print(f"PB1 PASS  18 probe rows reproduce (worst rel {worst1:.2e})")

    worst2 = 0.0
    for L, (Ydr, Ybr) in DENSE_REF.items():
        Yd = Y_dense_sum(L); Yb = rows[L - L_MIN][1]
        rel_fresh = abs(Yd - Yb) / abs(Yd)
        assert rel_fresh <= 5e-12, f"PB2 FAIL fresh L={L}: {rel_fresh}"
        for got, ref in ((Yd, Ydr), (Yb, Ybr)):
            rel = abs(got - ref) / abs(ref); worst2 = max(worst2, rel)
            assert rel <= 1e-11, f"PB2 FAIL vs notebook L={L}: {got} vs {ref}"
    print(f"PB2 PASS  dense cross-checks at 7 L values (worst rel {worst2:.2e})")

    Bs = [r[2] for r in rows]
    mono_viol = sum(1 for i in range(1, len(Bs)) if Bs[i] <= Bs[i - 1])
    assert mono_viol == 0, f"PB3 FAIL: {mono_viol} non-increasing steps"
    print("PB3 PASS  B_L strictly increasing over the full integer scan")

    imax = max(range(len(rows)), key=lambda i: rows[i][2])
    Lm, Ym, Bm = rows[imax]
    margin = B_CRIT - Bm
    assert Lm == MAXROW_REF["L"], f"PB4 FAIL argmax L={Lm}"
    assert abs(Bm - MAXROW_REF["B_L"]) / MAXROW_REF["B_L"] <= 1e-9, f"PB4 FAIL Bmax {Bm}"
    assert margin >= 0.0286, f"PB4 FAIL margin {margin}"
    print(f"PB4 PASS  max B_L = {Bm:.15f} at L={Lm}; margin to 57/1210 = {margin:.12f}")

    assert all(r[2] < B_CRIT for r in rows), "PB5 FAIL B_L >= BCRIT somewhere"
    bad_tc = [r for r in rows
              if 36.0 * r[1] / beta_of_L(r[0])**2 >= 0.125]
    assert not bad_tc, f"PB5 FAIL T_C >= 1/8 at L={bad_tc[0][0]}"
    print("PB5 PASS  finite certificate: B_L < 57/1210 and T_C < 1/8 for all L in [4, 4096]")

    refjson = None
    for c in (os.path.join(HERE, "AUDIT_OP1_m4_ceiling_pin.json"),
              "/sessions/beautiful-charming-knuth/mnt/THEORY/numerics/op12_theta/m4_scaling/AUDIT_OP1_m4_ceiling_pin.json",
              "/tmp/AUDIT_OP1_m4_ceiling_pin.json"):
        if os.path.exists(c): refjson = c; break
    assert refjson, "PB6: F028 refs not found"
    refs = json.load(open(refjson))
    D_INFTY, D_CRIT = refs["D_infty"], refs["D_crit_3par"]
    Ds = []
    for L, Y, B in rows:
        alpha = beta_of_L(L) / 6.0
        Ds.append(B - 0.5 * A_LOG * math.log(alpha))
    assert all(d < D_INFTY for d in Ds), "PB6 FAIL D_L >= D_infty somewhere"
    imaxD = max(range(len(Ds)), key=lambda i: Ds[i])
    L_ridge, D_ridge = imaxD + L_MIN, Ds[imaxD]
    assert L_ridge == 47, f"PB6 FAIL ridge at L={L_ridge}, expected 47"
    assert abs(D_ridge - 0.018288870941571) <= 1e-9 * D_ridge + 1e-12, \
        f"PB6 FAIL D_ridge {D_ridge}"
    probes = sorted(PROBE_REF)
    Dp = {p: Ds[p - L_MIN] for p in probes}
    inc = [p for p in probes if p <= 64]
    assert all(Dp[a] < Dp[b] for a, b in zip(inc, inc[1:])), "PB6 FAIL rise to ridge"
    dec = [p for p in probes if p >= 64]
    assert all(Dp[a] > Dp[b] for a, b in zip(dec, dec[1:])), "PB6 FAIL decay past ridge"
    headroom_fin = D_CRIT / D_ridge
    assert headroom_fin >= 2.44, f"PB6 FAIL finite headroom {headroom_fin}"
    print(f"PB6 PASS  D_L < D_infty everywhere (strict envelope); finite-D ridge at "
          f"L={L_ridge}, D_ridge = {D_ridge:.15f}; probe shape rise/fall OK; "
          f"finite headroom D_crit/D_ridge = {headroom_fin:.4f} "
          f"(envelope headroom {D_CRIT / D_INFTY:.4f})")

    for B, xref, tref, fref in CEIL_REF:
        xs, tb = ceiling_from_B(B)
        assert abs(xs - xref) <= 1e-5, f"PB7 FAIL x* at B={B}"
        assert abs(tb - tref) / tref <= 1e-9, f"PB7 FAIL Tbar at B={B}"
        fl = int(1.0 // tb)
        assert fl == fref >= 8, f"PB7 FAIL floor at B={B}: {fl}"
    xs_b, tb_b = ceiling_from_B(B_CRIT)
    print(f"PB7 PASS  ceiling rows reproduce; boundary Tbar(BCRIT) = {tb_b:.17f} "
          f"(floor_float = {int(1.0 // tb_b)}; boundary artifact, report-only)")

    dec_rows = [r for r in rows if r[0] <= 256 or r[0] % 8 == 0 or r[0] in PROBE_REF]
    out = {"meta": {"engine": "ENGINE_OP1_m4_bessel_scan_audit.py", "date": "2026-06-12",
                    "audits": "_M5_1 HEAT_KERNEL_BESSEL_FINITE_CERTIFICATE_+_TAIL_PIN_TEST.ipynb (md5 664e657c)",
                    "gates": "PB1..PB7 hard asserts", "scan": [L_MIN, L_MAX],
                    "f028_refs": refjson},
           "summary": {"B_max": Bm, "argmax_L": Lm, "margin_to_BCRIT": margin,
                       "BCRIT": B_CRIT, "D_4096_alpha_form": Ds[-1],
                       "D_infty_F028": D_INFTY, "D_crit_3par_F028": D_CRIT,
                       "D_ridge": D_ridge, "L_ridge": L_ridge,
                       "headroom_finite": headroom_fin,
                       "headroom_envelope": D_CRIT / D_INFTY,
                       "note_D_shape": "D_L NOT monotone: rises to ridge at L=47 then drifts down; on the AF diagonal mu^2 L^2 = 48/beta stays O(1) so D_L never approaches D_infty - D_infty is a strict upper envelope (Lemma-A direction), not a limit",
                       "boundary_Tbar_at_BCRIT": tb_b},
           "rows_decimated_L_Y_B": dec_rows}
    json.dump(out, open(OUT, "w"), indent=1)
    print(f"WROTE {os.path.basename(OUT)}")
    print("ALL GATES PASS (PB1-PB7)")
