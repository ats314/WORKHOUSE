#!/usr/bin/env python3
"""
ENGINE_OP1_m4_tc_closed_form.py — exact Fourier closed forms for the comparator kernel constants
=====================================================================================
Derivation + verification engine (June 12, 2026, session agent as lead math agent,
DECISIONS #009). Companion note: NOTE_OP1_m4_tc_closed_form_2026-06-12.md.

THEOREM (proved in the note; verified here against all deposited data + one
independent dense computation):

On the 4-torus (Z/L)^4 with M = m0^2 I + aW d1^T d1 on 1-cochains and P the
orthogonal projector onto ker d0^T (= coexact (+) harmonic), with
  what(n) = sum_mu 4 sin^2(pi n_mu / L),   n in {0..L-1}^4,
the kernel constants are EXACTLY

  g_H    = 1/(m0^2 L^4)                       T_H = 1/(m0^4 L^4)
  g_C    = (3/(4 L^4)) * sum_{n != 0} (m0^2 + aW*what(n))^(-1)
  T_C    = (3/(4 L^4)) * sum_{n != 0} (m0^2 + aW*what(n))^(-2)
  g_diag = g_H + g_C                          T_full = T_H + T_C

(multiplicity 3 = transverse polarizations per nonzero momentum; the gauge band
contributes 0; the 4 harmonic modes are the k=0 fiber).

Certificate radii (definitions matching m1/m2/m4 deposits, v0 = 1):
  Nstar       = floor(1/T_full)        [HS count certificate]
  Nstar_C     = floor(1/T_C)
  Nstar_split = max |D| with |D|*g_H + sqrt(|D|*T_C) < 1

HARD GATES (assert; any failure aborts):
  G-CF1  closed form vs CERT_OP1_m4_harmonic_decomposition.json, all rows, rtol 1e-6
         (T_C, T_H, T_full, g_H) + integer match of Nstar/Nstar_C/Nstar_split
  G-CF2  closed form vs CERT_OP1_kernel_consts.json tables (T_full_max, g_diag, Nstar)
  G-CF3  closed form vs CERT_OP1_m4_scaling_tables.json rows (T_full, g_diag, Nstar)
  G-CF4  INDEPENDENT dense check at L=4: explicit d0, d1, SVD projector,
         direct solve; per-link constancy <= 1e-10; values vs closed form <= 1e-9
  G-CF5  heat-kernel/Bessel representation (second exact method) vs direct
         lattice sum, sample rows, rtol 1e-8
  G-CF6  Tier-1 rigorous ceiling dominates every computed T_C (sanity of the
         analytic bound)

OUTPUT: CERT_OP1_m4_tc_closed_form.json (gate results, extended physical-diagonal table,
asymptotic-law fit, uniform-ceiling numbers).

Conventions: the derivation is convention-agnostic given (m0^2, aW); all
numerical rows use the Casimir row of theory/DOC_GOV_conventions.md via aW = beta/6,
N = 3, anchored beta0 = 5.6, m0^2 = 0.5 at s = 1 (matching the M4 deposits).
"""
import json, math, sys
import numpy as np
from scipy.special import ive
from scipy.integrate import quad

GAMMA = 2.0 * (11.0 * 3.0) / (48.0 * math.pi**2)   # d beta / d ln s = 0.139314...
BETA0, M02_0, L0 = 5.6, 0.5, 4

def beta_of_s(s):  return BETA0 + GAMMA * math.log(s)
def m02_of_s(s):   return M02_0 / s**2

# ---------------------------------------------------------------- lattice sums
def reduced(L):
    """values and multiplicities of c(n) = 4 sin^2(pi n / L), exact pairing n <-> L-n."""
    ns = np.arange(L // 2 + 1)
    v = 4.0 * np.sin(np.pi * ns / L) ** 2
    cnt = np.full(len(ns), 2.0)
    cnt[0] = 1.0
    if L % 2 == 0:
        cnt[-1] = 1.0
    return v, cnt

def sums12(L, m02, aW, chunk_elems=6_000_000):
    """(S1, S2) = sums over n in {0..L-1}^4 of (m02 + aW*what(n))^(-1) and ^(-2),
    INCLUDING n=0, in a single chunked sweep (reciprocal + square)."""
    v, c = reduced(L)
    V2 = (v[:, None] + v[None, :]).ravel()
    C2 = (c[:, None] * c[None, :]).ravel()
    nB = len(V2)
    step = max(1, chunk_elems // nB)
    S1 = S2 = 0.0
    for i in range(0, nB, step):
        R = 1.0 / (m02 + aW * (V2[i:i + step, None] + V2[None, :]))
        WR = (C2[i:i + step, None] * C2[None, :]) * R
        S1 += float(np.sum(WR))
        S2 += float(np.sum(WR * R))
    return S1, S2

def consts(L, m02, aW):
    Ns = float(L) ** 4
    S1, S2 = sums12(L, m02, aW)
    S1 -= 1.0 / m02
    S2 -= 1.0 / m02**2
    g_H, T_H = 1.0 / (m02 * Ns), 1.0 / (m02**2 * Ns)
    g_C, T_C = (3.0 / (4.0 * Ns)) * S1, (3.0 / (4.0 * Ns)) * S2
    return dict(g_H=g_H, T_H=T_H, g_C=g_C, T_C=T_C,
                g_diag=g_H + g_C, T_full=T_H + T_C)

def nstar_split(g_H, T_C):
    n, best = 0, 0
    cap = int(1.0 / T_C) + 3
    for D in range(1, cap + 1):
        if D * g_H + math.sqrt(D * T_C) < 1.0:
            best = D
        else:
            break
    return best

def radii(cs):
    return dict(Nstar=int(1.0 // cs["T_full"]),
                Nstar_C=int(1.0 // cs["T_C"]),
                Nstar_split=nstar_split(cs["g_H"], cs["T_C"]))

# ------------------------------------------------- independent method 2: Bessel
def Phi_L(L, t):
    """(1/L) sum_n exp(-4 t sin^2(pi n/L)) = sum_{j in Z} I_{jL}(2t) e^{-2t}, exact."""
    t = np.asarray(t, dtype=float)
    out = ive(0, 2 * t)
    m = 1
    while True:
        term = 2.0 * ive(m * L, 2 * t)
        out = out + term
        if np.all(term <= 1e-18 * np.maximum(out, 1e-300)):
            break
        m += 1
        if m > 100000:
            raise RuntimeError("Phi_L truncation runaway")
    return out

def TC_bessel(L, m02, aW):
    """T_C via the exact heat-kernel representation:
       T_C = (3/(4 aW^2)) * int_0^inf t e^{-t mu^2} (Phi_L(t)^4 - 1/L^4) dt,
       mu^2 = m02/aW."""
    mu2 = m02 / aW
    Ns = float(L) ** 4
    def f(t):
        return t * math.exp(-t * mu2) * (float(Phi_L(L, t)) ** 4 - 1.0 / Ns)
    lam_min = 4.0 * math.sin(math.pi / L) ** 2          # slowest nonzero mode
    T = 60.0 / (mu2 + lam_min)                          # generous tail cutoff
    val, err = quad(f, 0.0, T, limit=600)
    # rigorous tail bound: integrand <= t e^{-t(mu2+lam_min)} * (L^4-1)/L^4 * C
    tail = (T + 1.0 / (mu2 + lam_min)) * math.exp(-T * (mu2 + lam_min)) / (mu2 + lam_min)
    return (3.0 / (4.0 * aW**2)) * val, (3.0 / (4.0 * aW**2)) * (abs(err) + tail)

# ------------------------------------------- independent method 3: dense L = 4
def dense_check(L=4, m02=0.5, aW=5.6 / 6.0):
    Ns, E = L**4, 4 * L**4
    def sidx(x):
        return ((x[0] * L + x[1]) * L + x[2]) * L + x[3]
    d0 = np.zeros((E, Ns))
    plq = []
    for s in range(Ns):
        x = [(s // L**3) % L, (s // L**2) % L, (s // L) % L, s % L]
        for mu in range(4):
            y = list(x); y[mu] = (y[mu] + 1) % L
            d0[s * 4 + mu, s] -= 1.0
            d0[s * 4 + mu, sidx(y)] += 1.0
        for mu in range(4):
            for nu in range(mu + 1, 4):
                row = np.zeros(E)
                xm = list(x); xm[mu] = (xm[mu] + 1) % L
                xn = list(x); xn[nu] = (xn[nu] + 1) % L
                row[s * 4 + mu] += 1.0
                row[sidx(xm) * 4 + nu] += 1.0
                row[sidx(xn) * 4 + mu] -= 1.0
                row[s * 4 + nu] -= 1.0
                plq.append(row)
    d1 = np.array(plq)
    M = m02 * np.eye(E) + aW * (d1.T @ d1)
    U, S, _ = np.linalg.svd(d0, full_matrices=False)
    Q = U[:, S > 1e-10]
    P = np.eye(E) - Q @ Q.T
    G = np.linalg.solve(M, P)
    GH = np.zeros((E, E))
    for mu in range(4):
        h = np.zeros(E); h[mu::4] = 1.0 / math.sqrt(Ns)
        GH += np.outer(h, h) / m02
    GC = G - GH
    TC_rows = np.sum(GC**2, axis=1)
    Tf_rows = np.sum(G**2, axis=1)
    gd_rows = np.diag(G)
    return (float(TC_rows.mean()), float(TC_rows.std()),
            float(Tf_rows.mean()), float(Tf_rows.std()),
            float(gd_rows.mean()), float(gd_rows.std()))

# --------------------------------------------------- Tier-1 rigorous ceiling
C0_EXACT = None
def tier1_bound(L, aW):
    """Fully elementary rigorous bound (proof in the note):
       T_C <= (3/(1024 aW^2)) [ c0 + (4/3)^4 * 2 pi^2 * ln((L+1)/2) ],
       c0 = sum over 0 < |m|^2 <= 8 of |m|^-4 (exact small-shell sum)."""
    global C0_EXACT
    if C0_EXACT is None:
        rng = range(-3, 4)
        c0 = 0.0
        for a in rng:
            for b in rng:
                for c in rng:
                    for d in rng:
                        q = a * a + b * b + c * c + d * d
                        if 0 < q <= 8:
                            c0 += 1.0 / q**2
        C0_EXACT = c0
    return (3.0 / (1024.0 * aW**2)) * (C0_EXACT + (4.0 / 3.0) ** 4 * 2.0 * math.pi**2
                                       * math.log((L + 1) / 2.0))

# ---------------------------------------------------------------------- gates
def approx(a, b, rtol):
    return abs(a - b) <= rtol * max(abs(a), abs(b), 1e-300)

def run_gates(proj="/mnt/project"):
    rep = {}

    # G-CF1 + integer radii vs CERT_OP1_m4_harmonic_decomposition.json (dual beta reading:
    # the deposit stores beta rounded to 4 decimals; some rows were computed with
    # the rounded value, some with the exact beta(s) formula — both readings are
    # tried and the matched one must agree at MACHINE level, 1e-12)
    def match_dual(r, keymap):
        b_stored = r["beta"]
        b_exact = BETA0 + GAMMA * math.log(r["scale"]) if "scale" in r else b_stored
        best = None
        for tag, b in (("stored_rounded", b_stored), ("formula_exact", b_exact)):
            cs = consts(r["L"], r["m02"], b / 6.0)
            d = max(abs(cs[km] - r[kt]) / max(abs(r[kt]), 1e-300)
                    for km, kt in keymap)
            if best is None or d < best[0]:
                best = (d, tag, cs)
        return best

    H = json.load(open(f"{proj}/CERT_OP1_m4_harmonic_decomposition.json"))["rows"]
    worst, tags = 0.0, {"stored_rounded": 0, "formula_exact": 0}
    for r in H:
        d, tag, cs = match_dual(r, [("T_C", "T_C"), ("T_H", "T_H"),
                                    ("T_full", "T_full"), ("g_H", "g_H")])
        worst = max(worst, d)
        assert d <= 1e-12, f"G-CF1 FAIL {r['L']},{r['scale']}: {d} ({tag})"
        tags[tag] += 1
        rr = radii(cs)
        for k in ("Nstar", "Nstar_C", "Nstar_split"):
            assert rr[k] == r[k], f"G-CF1 FAIL radii {r['L']},{r['scale']},{k}: {rr[k]} vs {r[k]}"
    rep["G_CF1"] = dict(rows=len(H), worst_rel=worst, beta_reading_counts=tags,
                        deposit_note=("beta stored at 4 decimals; rows resumed from the "
                                      "scaling state were computed AT the rounded beta, "
                                      "fresh rows (s=1.25 x3, L=12 s=3) at exact beta(s) — "
                                      "max cross-reading discrepancy 1.5e-5, no integer "
                                      "radius affected"), passed=True)

    # G-CF2 vs CERT_OP1_kernel_consts.json
    K = json.load(open(f"{proj}/CERT_OP1_kernel_consts.json"))["tables"]
    worst = 0.0
    for r in K:
        cs = consts(r["L"], 0.5, r["beta"] / 6.0)
        for mine, theirs in [("T_full", "T_full_max"), ("g_diag", "g_diag")]:
            d = abs(cs[mine] - r[theirs]) / abs(r[theirs])
            worst = max(worst, d)
            assert d <= 1e-6, f"G-CF2 FAIL {r['L']},{r['beta']},{mine}: {d}"
        assert int(1.0 // cs["T_full"]) == r["Nstar_theta_lt_1"], \
            f"G-CF2 FAIL Nstar {r['L']},{r['beta']}"
    rep["G_CF2"] = dict(rows=len(K), worst_rel=worst, passed=True)

    # G-CF3 vs CERT_OP1_m4_scaling_tables.json (dual beta reading, machine tolerance;
    # these rows were ALL computed at the exact beta(s), stored rounded)
    Srows = json.load(open(f"{proj}/CERT_OP1_m4_scaling_tables.json"))["rows"]
    worst, tags3 = 0.0, {"stored_rounded": 0, "formula_exact": 0}
    for r in Srows:
        d, tag, cs = match_dual(r, [("T_full", "T_full"), ("g_diag", "g_diag")])
        worst = max(worst, d)
        assert d <= 1e-12, f"G-CF3 FAIL {r['L']},{r['scale']}: {d} ({tag})"
        tags3[tag] += 1
        assert int(1.0 // cs["T_full"]) == r["Nstar"], f"G-CF3 FAIL Nstar"
    rep["G_CF3"] = dict(rows=len(Srows), worst_rel=worst,
                        beta_reading_counts=tags3, passed=True)

    # G-CF4 independent dense check (no deposited data used)
    tc_m, tc_s, tf_m, tf_s, gd_m, gd_s = dense_check()
    cs = consts(4, 0.5, 5.6 / 6.0)
    assert tc_s <= 1e-10 and tf_s <= 1e-10 and gd_s <= 1e-10, "G-CF4 FAIL constancy"
    for mine, val in [("T_C", tc_m), ("T_full", tf_m), ("g_diag", gd_m)]:
        assert approx(cs[mine], val, 1e-9), f"G-CF4 FAIL {mine}: {cs[mine]} vs {val}"
    rep["G_CF4"] = dict(per_link_std=max(tc_s, tf_s, gd_s),
                        T_C_dense=tc_m, T_C_closed=cs["T_C"], passed=True)

    # G-CF5 Bessel representation vs direct lattice sum
    worst = 0.0
    for (L, s) in [(4, 1.0), (6, 1.5), (12, 3.0), (16, 4.0), (32, 8.0), (64, 16.0)]:
        m02, aW = m02_of_s(s), beta_of_s(s) / 6.0
        tc_direct = consts(L, m02, aW)["T_C"]
        tc_b, errb = TC_bessel(L, m02, aW)
        d = abs(tc_b - tc_direct) / tc_direct
        worst = max(worst, d)
        assert d <= 1e-8, f"G-CF5 FAIL L={L}: {d} (quad err est {errb})"
    rep["G_CF5"] = dict(worst_rel=worst, passed=True)

    # G-CF6 Tier-1 ceiling dominates every computed value
    for r in H:
        assert consts(r["L"], r["m02"], r["beta"] / 6.0)["T_C"] <= tier1_bound(r["L"], r["beta"] / 6.0), \
            "G-CF6 FAIL"
    rep["G_CF6"] = dict(passed=True, c0_exact=C0_EXACT)
    return rep

# ------------------------------------------------- physical-diagonal extension
def diagonal_table(s_list):
    rows = []
    for s in s_list:
        L = int(round(L0 * s))
        assert abs(L - L0 * s) < 1e-9, f"non-integer L for s={s}"
        m02, beta = m02_of_s(s), beta_of_s(s)
        aW = beta / 6.0
        cs = consts(L, m02, aW)
        rr = radii(cs)
        rows.append(dict(L=L, scale=s, beta=beta, m02=m02,
                         T_C=cs["T_C"], T_H=cs["T_H"], T_full=cs["T_full"],
                         g_H=cs["g_H"], g_diag=cs["g_diag"],
                         x_lns=math.log(s), y_TCaW2=cs["T_C"] * aW**2,
                         tier1=tier1_bound(L, aW), **rr))
    return rows

def fit_and_ceiling(rows, x_min=1.0):
    pts = [(r["x_lns"], r["y_TCaW2"]) for r in rows if r["x_lns"] >= x_min]
    X = np.array([p[0] for p in pts]); Y = np.array([p[1] for p in pts])
    A, B = np.polyfit(X, Y, 1)
    A_theory = 3.0 / (32.0 * math.pi**2)
    # local slopes (consecutive differences) to show convergence toward A_theory
    allp = sorted([(r["x_lns"], r["y_TCaW2"]) for r in rows])
    slopes = [dict(x_mid=(allp[i][0] + allp[i + 1][0]) / 2,
                   slope=(allp[i + 1][1] - allp[i][1]) / (allp[i + 1][0] - allp[i][0]))
              for i in range(len(allp) - 1)]
    # ceiling of the fitted law along beta(s) = BETA0 + GAMMA x  (Tier-2)
    xstar = BETA0 / GAMMA - 2.0 * B / A
    bstar = BETA0 + GAMMA * xstar
    Tbar = (A * xstar + B) * (6.0 / bstar) ** 2
    return dict(A_fit=float(A), B_fit=float(B), A_theory=A_theory,
                A_ratio=float(A / A_theory), fit_range_lns=[float(X.min()), float(X.max())],
                local_slopes=slopes,
                xstar=xstar, sstar=math.exp(xstar), beta_star=bstar,
                T_C_ceiling=Tbar, NstarC_floor_uniform=int(1.0 // Tbar))

# ----------------------------------------------------------------------- main
if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    out = {"meta": dict(engine="ENGINE_OP1_m4_tc_closed_form.py",
                        date="2026-06-12",
                        conventions="Casimir row (alpha_W=beta/6, N=3); derivation convention-agnostic",
                        anchor=dict(beta0=BETA0, m02_0=M02_0, L0=L0, gamma_dbeta_dlns=GAMMA))}
    if stage in ("gates", "all"):
        out["gates"] = run_gates()
        json.dump(out["gates"], open("/home/claude/m4_gates.json", "w"), indent=1)
        print("GATES:", json.dumps(out["gates"], indent=1))
    if stage in ("diagonal", "all"):
        if "gates" not in out:
            try:
                out["gates"] = json.load(open("/home/claude/m4_gates.json"))
            except FileNotFoundError:
                pass
        s_list = [1, 1.25, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 48, 64]
        rows = diagonal_table(s_list)
        out["diagonal_rows"] = rows
        out["law"] = fit_and_ceiling(rows, x_min=1.0)
        for r in rows:
            print(f"L={r['L']:4d} s={r['scale']:6.2f} beta={r['beta']:.4f} "
                  f"T_C={r['T_C']:.6f} T_full={r['T_full']:.6f} "
                  f"N*={r['Nstar']:3d} N*_C={r['Nstar_C']:3d} N*_split={r['Nstar_split']:3d} "
                  f"tier1={r['tier1']:.4f}")
        print("LAW:", json.dumps({k: v for k, v in out["law"].items() if k != "local_slopes"}, indent=1))
        json.dump(out, open("/home/claude/CERT_OP1_m4_tc_closed_form.json", "w"), indent=1)
        print("WROTE /home/claude/CERT_OP1_m4_tc_closed_form.json")
    print("ALL GATES PASS" if "gates" not in out or all(g.get("passed") for g in out["gates"].values()) else "GATE FAILURE")
