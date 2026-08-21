#!/usr/bin/env python3
"""
ENGINE_OP1_s_chessboard_rate.py — quantitative engine for the (S) chessboard/large-deviation route
=======================================================================================
Companion to NOTE_FLUX_s_chessboard_route_2026-06-12.md (June 12, 2026, lead math agent pass).

Computes, with hard gates:
  A. Plaquette-animal growth: exact counts a_n of connected (link-sharing) plaquette
     animals of size n containing a fixed root in Z^4, gated against the proved
     bound a_n <= e * (e*Delta)^(n-1), Delta = 20.  [Lemma A of the note]
  B. Exact SU(3) one-plaquette quantities by Weyl-measure quadrature:
     z(beta) = E_Haar e^{-beta*phi}, phi(U) = 1 - (1/3)Re tr U in [0, 3/2];
     Haar tail h(delta) = P_Haar(phi >= delta); <phi>_beta; exact one-plaquette
     conditional tail r1(beta, delta) = -log P_1pl(phi >= delta).
     Gates: Haar normalization, E tr U = 0, E |tr U|^2 = 1 (machine precision).
  C. Two-tier Peierls rates for P(Gamma in D_delta) <= exp(-r |Gamma|):
       Tier-R (rigorous-modulo-cited-package): r_R = beta*(delta - 1)
       Tier-S (sharp target, modulo the E-bound): r_S = beta*(delta - Ebar(beta)),
         Ebar reported as the exact one-plaquette <phi>_beta (proxy, labeled).
     Thresholds vs the rooted-capacity requirement r > log(mu_bar) (+ weights).
  D. MC gates vs deposited ensembles results_L*_b*.json:
     measured mean rhoP_d{delta} must satisfy rhoP <= exp(-r_R(beta,delta))
     whenever delta > 1 (the bound is vacuous for delta <= 1) — falsifiable check
     of the Tier-R inequality at |Gamma| = 1.

All gates are asserts. Output: CERT_OP1_s_chessboard_rate.json.
"""
import json, math, glob, re, sys, itertools
import numpy as np

DELTA_DEG = 20                      # plaquette adjacency degree in Z^4 (4 links x 5 others)
MU_BAR = math.e * DELTA_DEG         # Lemma A growth base, log = 1 + log 20 = 3.9957
GAMMA = 2.0 * 33.0 / (48.0 * math.pi**2)
BETA0 = 5.6

# ---------------------------------------------------------------- A. animals
def plaq_links(p):
    (x, mu, nu) = p
    xm = tuple(x[i] + (1 if i == mu else 0) for i in range(4))
    xn = tuple(x[i] + (1 if i == nu else 0) for i in range(4))
    return frozenset({(x, mu), (xm, nu), (xn, mu), (x, nu)})

def plaq_neighbors(p):
    """all plaquettes sharing a link with p (in infinite Z^4; exact, no wraps)."""
    nbrs = set()
    for (y, rho) in plaq_links(p):
        # plaquettes containing link (y, rho): orientations (rho, sig) at y and y - e_sig
        for sig in range(4):
            if sig == rho:
                continue
            a, b = min(rho, sig), max(rho, sig)
            nbrs.add((y, a, b))
            ym = tuple(y[i] - (1 if i == sig else 0) for i in range(4))
            nbrs.add((ym, a, b))
    p0 = (p[0], p[1], p[2])
    nbrs.discard(p0)
    return nbrs

def count_animals(n_max=4):
    root = ((0, 0, 0, 0), 0, 1)
    counts = {1: 1}
    frontier = {frozenset({root})}
    for n in range(2, n_max + 1):
        new = set()
        for S in frontier:
            cand = set()
            for p in S:
                cand |= plaq_neighbors(p)
            cand -= S
            for q in cand:
                new.add(S | {q})
        counts[n] = len(new)
        frontier = new
    return counts

# ------------------------------------------- B. SU(3) Weyl-measure quadrature
def weyl_quantities(betas, deltas, N=1200):
    th = (np.arange(N) + 0.5) * (2 * np.pi / N) - np.pi
    T1, T2 = np.meshgrid(th, th, indexing="ij")
    T3 = -T1 - T2
    # |Delta|^2 = prod_{i<j} 4 sin^2((th_i - th_j)/2)
    D2 = (4 * np.sin((T1 - T2) / 2) ** 2
          * 4 * np.sin((T1 - T3) / 2) ** 2
          * 4 * np.sin((T2 - T3) / 2) ** 2)
    w = D2 / (6.0 * (2 * np.pi) ** 2) * (2 * np.pi / N) ** 2   # Haar weight per cell
    retr = np.cos(T1) + np.cos(T2) + np.cos(T3)
    imtr = np.sin(T1) + np.sin(T2) + np.sin(T3)
    phi = 1.0 - retr / 3.0
    norm = float(np.sum(w))
    m_re = float(np.sum(w * retr))
    m_abs2 = float(np.sum(w * (retr ** 2 + imtr ** 2)))
    # hard gates: Haar normalization and first two moments of tr U
    assert abs(norm - 1.0) <= 1e-9, f"G-S1 FAIL Haar norm {norm}"
    assert abs(m_re) <= 1e-9, f"G-S2 FAIL E Re tr {m_re}"
    assert abs(m_abs2 - 1.0) <= 1e-8, f"G-S2 FAIL E|tr|^2 {m_abs2}"
    out = {"gate_norm": norm, "gate_EReTr": m_re, "gate_EabsTr2": m_abs2,
           "phi_max_grid": float(phi.max())}
    rows = []
    for b in betas:
        ew = w * np.exp(-b * phi)
        z = float(np.sum(ew))
        Ephi = float(np.sum(ew * phi)) / z
        row = {"beta": b, "z": z, "f1": -math.log(z), "Ephi_1pl": Ephi, "tails": {}}
        for d in deltas:
            mask = phi >= d
            haar_tail = float(np.sum(w[mask]))
            p1 = float(np.sum(ew[mask])) / z
            row["tails"][f"{d:.2f}"] = {"haar": haar_tail, "p1": p1,
                                        "r1": (-math.log(p1) if p1 > 0 else float("inf"))}
        rows.append(row)
    out["rows"] = rows
    return out

# ------------------------------------------------------------- C. rate tables
def rate_tables(weyl, deltas):
    tab = []
    for row in weyl["rows"]:
        b, Ephi = row["beta"], row["Ephi_1pl"]
        for d in deltas:
            rR = b * (d - 1.0)
            rS = b * (d - Ephi)
            r1 = row["tails"][f"{d:.2f}"]["r1"]
            tab.append(dict(beta=b, delta=d, r_R=rR, r_S_proxy=rS, r1_exact_1pl=r1,
                            clears_logmu_R=rR > math.log(MU_BAR),
                            clears_logmu_S=rS > math.log(MU_BAR)))
    # thresholds beta_c(delta) per tier vs log(mu_bar)
    thr = []
    for d in deltas:
        if d > 1.0:
            bcR = math.log(MU_BAR) / (d - 1.0)
        else:
            bcR = float("inf")
        thr.append(dict(delta=d, beta_c_tierR=bcR,
                        lns_to_reach=(bcR - BETA0) / GAMMA if bcR > BETA0 else 0.0))
    return tab, thr

# ------------------------------------------------------------ D. ensemble gate
def ensemble_gate(weyl_rows):
    files = sorted(glob.glob("/mnt/project/results_L*_b*.json"))
    recs, gate_checks = [], 0
    for fn in files:
        m = re.search(r"results_L(\d+)_b(\d+)_(\d+)\.json", fn)
        L, beta = int(m.group(1)), float(f"{m.group(2)}.{m.group(3)}")
        cfgs = json.load(open(fn))["cfg"]
        keys = [k for k in cfgs[0] if k.startswith("rhoP_d")]
        rec = {"L": L, "beta": beta, "n_cfg": len(cfgs),
               "plaq_mean": float(np.mean([c["plaq"] for c in cfgs])),
               "Ephi_meas": 1.0 - float(np.mean([c["plaq"] for c in cfgs]))}
        for k in keys:
            d = float(k.split("_d")[1])
            rho = float(np.mean([c[k] for c in cfgs]))
            rec[f"rhoP_{d}"] = rho
            if d > 1.0:   # Tier-R is vacuous for delta <= 1
                bound = math.exp(-beta * (d - 1.0))
                assert rho <= bound, \
                    f"G-S3 FAIL L={L} beta={beta} d={d}: rhoP {rho} > {bound}"
                gate_checks += 1
                rec[f"tierR_bound_{d}"] = bound
        recs.append(rec)
    return recs, gate_checks

# ----------------------------------------------------------------------- main
if __name__ == "__main__":
    out = {"meta": dict(engine="ENGINE_OP1_s_chessboard_rate.py", date="2026-06-12",
                        Delta=DELTA_DEG, mu_bar=MU_BAR, log_mu_bar=math.log(MU_BAR),
                        phi_convention="phi = 1 - (1/3) Re tr U in [0, 1.5]; P ~ exp(-beta sum phi)")}
    # A
    counts = count_animals(4)
    for n, a in counts.items():
        if n >= 2:
            assert a <= math.e * (math.e * DELTA_DEG) ** (n - 1), f"G-S4 FAIL n={n}"
    out["animals"] = {"counts": counts,
                      "bound_e_eDelta": {n: math.e * (math.e * DELTA_DEG) ** (n - 1)
                                         for n in counts},
                      "growth_estimates": {n: counts[n] ** (1.0 / (n - 1))
                                           for n in counts if n >= 2}}
    print("ANIMALS:", counts, "-> per-step growth",
          {n: round(v, 2) for n, v in out["animals"]["growth_estimates"].items()})
    # B
    betas = [5.6, 6.0, 6.4, 6.8, 7.2, 8.0, 10.0, 12.0, 16.0, 20.0]
    deltas = [0.7, 0.9, 1.1, 1.2, 1.3, 1.4, 1.45]
    weyl = weyl_quantities(betas, deltas)
    out["weyl"] = weyl
    print(f"WEYL gates: norm-1={weyl['gate_norm']-1:.2e}  EReTr={weyl['gate_EReTr']:.2e} "
          f" E|tr|^2-1={weyl['gate_EabsTr2']-1:.2e}  phi_max={weyl['phi_max_grid']:.6f}")
    for r in weyl["rows"][:5]:
        print(f"  beta={r['beta']:5.2f} z={r['z']:.6e} f1={r['f1']:.4f} <phi>1pl={r['Ephi_1pl']:.4f} "
              f"r1(1.1)={r['tails']['1.10']['r1']:.3f} r1(1.3)={r['tails']['1.30']['r1']:.3f}")
    # C
    tab, thr = rate_tables(weyl, deltas)
    out["rates"], out["thresholds"] = tab, thr
    print("THRESHOLDS (Tier-R, vs log mu_bar = %.4f):" % math.log(MU_BAR))
    for t in thr:
        print(f"  delta={t['delta']:.2f}  beta_c={t['beta_c_tierR']:8.2f}  ln s to reach={t['lns_to_reach']:8.1f}")
    # D
    recs, ngate = ensemble_gate(weyl["rows"])
    out["ensembles"] = recs
    print(f"ENSEMBLE GATE: {ngate} Tier-R single-plaquette checks passed over {len(recs)} ensembles")
    for r in recs:
        keys = sorted(k for k in r if k.startswith("rhoP_"))
        print(f"  L={r['L']} beta={r['beta']:.1f} <phi>_meas={r['Ephi_meas']:.4f} " +
              " ".join(f"{k}={r[k]:.3e}" for k in keys))
    json.dump(out, open("/home/claude/CERT_OP1_s_chessboard_rate.json", "w"), indent=1)
    print("WROTE /home/claude/CERT_OP1_s_chessboard_rate.json")
    print("ALL GATES PASS")
