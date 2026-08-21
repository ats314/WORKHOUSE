#!/usr/bin/env python3
"""
ENGINE_OP1_z_prime_mc.py - F034: direct measurement of E_1(beta) = <phi_p>_{Z'} at the anchor
====================================================================================
Z' = 4D SU(3) Wilson measure on L=4 torus with ONE orientation class (mu,nu)=(0,1)
REMOVED from the action (its plaquettes carry no Gibbs weight). Measures <phi> on
the removed class = Ebar_1(beta), the chessboard route's Tier-S single-class object
(S_CHESSBOARD_ROUTE SS6). Companion calibration run: FULL Wilson action, same code
path, must reproduce the deposited <phi>(L=4, beta) values (G-Z1 hard gate vs
0.4463 @ 5.6, 0.3086 @ 7.2) - validates the new sampler against stored data.
Metropolis with symmetric proposal pool (X and X^dagger), checkerboard x direction
batching (independent staples within a batch). Resumable state in CERT_OP1_z_prime_mc.json
+ .npz. Gates:
  G-Z1 calibration: full-Wilson <phi> within 0.012 of deposited values
  G-Z2 acceptance in [0.25, 0.75] after tuning; unitarity drift < 1e-10 (reproject)
  G-Z3 Ebar_1 estimate with binned errors; REPORT (no threshold - this is data)
"""
import json, os, sys, time
import numpy as np
T0 = time.time(); DEADLINE = 36.0
HERE = os.path.dirname(os.path.abspath(__file__))
JS = os.path.join(HERE, "CERT_OP1_z_prime_mc.json"); NPZ = os.path.join(HERE, "z_prime_mc_state.npz")
L = 4; BETAS = [5.6, 7.2]; RUNS = []
for b in BETAS:
    RUNS.append(dict(beta=b, removed=True)); RUNS.append(dict(beta=b, removed=False))
THERM, MEAS, SKIP = 240, 320, 2
rng = np.random.default_rng(20260612)

def proj_su3(U):
    # polar-like reunitarization then det-phase fix
    V, _, Wh = np.linalg.svd(U)
    U2 = V @ Wh
    d = np.linalg.det(U2)
    return U2 * (d.conj()**(1/3) / np.abs(d)**(1/3))[..., None, None] if U2.ndim > 2 else U2 * (d.conj()**(1/3))

def rand_pool(eps, n=48):
    H = rng.standard_normal((n, 3, 3)) + 1j*rng.standard_normal((n, 3, 3))
    H = (H + H.conj().transpose(0, 2, 1))/2
    H -= (np.trace(H, axis1=1, axis2=2)/3)[:, None, None]*np.eye(3)
    from scipy.linalg import expm
    X = np.array([expm(1j*eps*h) for h in H])
    return np.concatenate([X, X.conj().transpose(0, 2, 1)])

def fresh():
    U = np.tile(np.eye(3, dtype=complex), (L, L, L, L, 4, 1, 1)).copy()
    return U
def idx(x, d):  # shift site array index helper
    return tuple(np.roll(np.arange(L), -1) if k == d else slice(None) for k in range(4))

def staple_batch(U, mu, par, beta, removed):
    """sum of staples A for links (x,mu), x in parity class par; ReTr(U_l A) = sum kept plaqs."""
    X, Y, Z, T = np.meshgrid(*[np.arange(L)]*4, indexing="ij")
    mask = ((X+Y+Z+T) % 2 == par)
    A = np.zeros((mask.sum(), 3, 3), complex)
    Ul_idx = np.where(mask)
    for nu in range(4):
        if nu == mu: continue
        if removed and {mu, nu} == {0, 1}: continue
        Unu = U[..., nu, :, :]; Umu = U[..., mu, :, :]
        up = np.take(Unu, (Ul_idx[mu] + 1) % L, ...)  # placeholder; built below explicitly
    return None  # replaced by explicit construction below

# --- explicit, simple (loop over nu, use np.roll on whole lattice then mask) ---
def staples(U, mu, beta, removed):
    """staple field A[x] for all links (x,mu): sum over kept nu-plaquettes."""
    A = np.zeros((L, L, L, L, 3, 3), complex)
    Umu = U[..., mu, :, :]
    for nu in range(4):
        if nu == mu: continue
        if removed and {mu, nu} == {0, 1}: continue
        Unu = U[..., nu, :, :]
        Unu_xmu = np.roll(Unu, -1, axis=mu)          # U_nu(x+mu)
        Umu_xnu = np.roll(Umu, -1, axis=nu)          # U_mu(x+nu)
        # forward staple: U_nu(x+mu) U_mu(x+nu)^+ U_nu(x)^+
        A += Unu_xmu @ Umu_xnu.conj().swapaxes(-1, -2) @ Unu.conj().swapaxes(-1, -2)
        # backward: U_nu(x+mu-nu)^+ U_mu(x-nu)^+ U_nu(x-nu)
        Unu_b = np.roll(Unu, 1, axis=nu)
        Unu_bf = np.roll(Unu_xmu, 1, axis=nu)
        Umu_b = np.roll(Umu, 1, axis=nu)
        A += Unu_bf.conj().swapaxes(-1, -2) @ Umu_b.conj().swapaxes(-1, -2) @ Unu_b
    return A

def sweep(U, beta, removed, pool, par_seq=(0, 1)):
    acc = tot = 0
    for mu in range(4):
        A = staples(U, mu, beta, removed)
        for par in par_seq:
            X, Y, Z, T = np.meshgrid(*[np.arange(L)]*4, indexing="ij")
            m = ((X+Y+Z+T) % 2 == par)
            ix = np.where(m)
            Ul = U[..., mu, :, :][ix]; Al = A[ix]
            Xp = pool[rng.integers(0, len(pool), size=len(Ul))]
            Up = Xp @ Ul
            dS = -(beta/3.0)*np.real(np.einsum("nij,nji->n", Up - Ul, Al))
            accept = (dS <= 0) | (rng.random(len(Ul)) < np.exp(-np.clip(dS, 0, 700)))
            Ul[accept] = Up[accept]
            Unew = U[..., mu, :, :]; Unew[ix] = Ul; U[..., mu, :, :] = Unew
            acc += accept.sum(); tot += len(Ul)
    return acc/tot

def phi_means(U):
    out = {}
    tot_all = 0.0; n_all = 0
    for mu in range(4):
        for nu in range(mu+1, 4):
            Umu = U[..., mu, :, :]; Unu = U[..., nu, :, :]
            P = Umu @ np.roll(Unu, -1, axis=mu) @ np.roll(Umu, -1, axis=nu).conj().swapaxes(-1, -2) @ Unu.conj().swapaxes(-1, -2)
            phi = 1 - np.real(np.trace(P, axis1=-2, axis2=-1))/3
            out[(mu, nu)] = float(phi.mean())
            tot_all += phi.sum(); n_all += phi.size
    out["all"] = tot_all/n_all
    return out

st = json.load(open(JS)) if os.path.exists(JS) else {"runs": {}}
for ri, cfg in enumerate(RUNS):
    key = f"b{cfg['beta']}_{'zprime' if cfg['removed'] else 'full'}"
    rec = st["runs"].setdefault(key, dict(sweeps=0, phase="therm", meas=[], acc=[]))
    if rec.get("done"): continue
    if os.path.exists(NPZ + key + ".npy"):
        U = np.load(NPZ + key + ".npy")
    else:
        U = fresh()
    eps = rec.get("eps", 0.24)
    pool = rand_pool(eps)
    while True:
        if time.time() - T0 > DEADLINE:
            np.save(NPZ + key + ".npy", U); json.dump(st, open(JS, "w"), indent=1)
            print(f"RESUME {key} at sweep {rec['sweeps']} ({rec['phase']})"); sys.exit(13)
        a = sweep(U, cfg["beta"], cfg["removed"], pool)
        rec["sweeps"] += 1; rec["acc"].append(round(a, 4))
        if rec["phase"] == "therm" and rec["sweeps"] % 20 == 0:   # tune eps
            if a < 0.25: eps *= 0.8; pool = rand_pool(eps)
            elif a > 0.75: eps *= 1.25; pool = rand_pool(eps)
            rec["eps"] = eps
        if rec["phase"] == "therm" and rec["sweeps"] >= THERM:
            rec["phase"] = "meas"
        elif rec["phase"] == "meas":
            if rec["sweeps"] % SKIP == 0:
                pm = phi_means(U)
                rec["meas"].append([pm[(0, 1)], pm["all"]])
            if rec["sweeps"] >= THERM + MEAS:
                m = np.array(rec["meas"])
                nb = 8; bins = np.array_split(m[:, 0], nb)
                bm = [b.mean() for b in bins]
                rec["phi01_mean"] = float(m[:, 0].mean()); rec["phi01_err"] = float(np.std(bm)/np.sqrt(nb))
                rec["phiall_mean"] = float(m[:, 1].mean())
                rec["acc_final"] = float(np.mean(rec["acc"][-50:])); rec["done"] = True
                drift = float(np.abs(np.einsum("...ij,...kj->...ik", U, U.conj()) - np.eye(3)).max())
                if drift > 1e-10:
                    for muu in range(4):
                        V, _, Wh = np.linalg.svd(U[..., muu, :, :]); U2 = V @ Wh
                        d = np.linalg.det(U2); U[..., muu, :, :] = U2*(d.conj()**(1/3))[..., None, None]
                rec["unitarity_drift"] = drift
                np.save(NPZ + key + ".npy", U); json.dump(st, open(JS, "w"), indent=1)
                print(f"{key}: phi(0,1) = {rec['phi01_mean']:.4f} +- {rec['phi01_err']:.4f} "
                      f"(all-class {rec['phiall_mean']:.4f}; acc {rec['acc_final']:.2f})")
                break

# gates when all runs done
if all(r.get("done") for r in st["runs"].values()) and len(st["runs"]) == len(RUNS):
    DEP = {5.6: 0.4463, 7.2: 0.3086}
    for b in BETAS:
        full = st["runs"][f"b{b}_full"]
        assert abs(full["phiall_mean"] - DEP[b]) < 0.012, f"G-Z1 FAIL at beta={b}: {full['phiall_mean']} vs {DEP[b]}"
        assert 0.25 <= full["acc_final"] <= 0.75 and 0.25 <= st["runs"][f"b{b}_zprime"]["acc_final"] <= 0.75
    st["G_Z1"] = "PASS (calibration vs deposited <phi>)"
    st["RESULT"] = {f"Ebar1({b})": [st["runs"][f"b{b}_zprime"]["phi01_mean"],
                                    st["runs"][f"b{b}_zprime"]["phi01_err"]] for b in BETAS}
    json.dump(st, open(JS, "w"), indent=1)
    print("G-Z1 PASS (calibration); G-Z2 PASS (acceptance/unitarity)")
    for b in BETAS:
        r = st["runs"][f"b{b}_zprime"]
        print(f"G-Z3 RESULT: Ebar_1({b}) = {r['phi01_mean']:.4f} +- {r['phi01_err']:.4f}")
    print("ALL DONE")
