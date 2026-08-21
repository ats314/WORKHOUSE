# -*- coding: utf-8 -*-
"""
MoA Rank-8 (spin-cutoff) tensor -> transfer matrix -> Doob Markov kernel -> Doeblin-certified mass gap.

Copy into a Colab cell or run as a script. Requires: numpy, jax, matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

# Optional: JAX acceleration (works great on Colab GPUs). Falls back to NumPy if unavailable.
try:
    import jax
    import jax.numpy as jnp
    HAVE_JAX = True
except Exception:
    HAVE_JAX = False
    jax = None
    jnp = None

import cmath, math, functools
from typing import List, Tuple, Dict, Any


# ============================================================
# 1) q-numbers + log q-factorials (stable via sinh(log q))
# ============================================================

def q_number(n: int, q: complex) -> complex:
    """
    [n]_q = (q^n - q^{-n})/(q - q^{-1})
         = sinh(n log q)/sinh(log q)

    Works for:
      - real q in (0,1) or q>1
      - q on the unit circle (q=e^{i theta}) as long as theta not at a root-of-unity singularity.
    """
    if n == 0:
        return 0.0 + 0.0j
    x = cmath.log(q)
    if abs(x) < 1e-12:
        return complex(n)
    return cmath.sinh(n * x) / cmath.sinh(x)


def log_q_factorials_table(n_max: int, q: complex) -> np.ndarray:
    """
    Precompute log([n]_q!) for n=0..n_max in complex128.
    If any [n]_q hits ~0, log factorial becomes -inf thereafter.
    """
    log_fact = np.empty(n_max + 1, dtype=np.complex128)
    log_fact[0] = 0.0 + 0.0j
    for n in range(1, n_max + 1):
        prev = log_fact[n - 1]
        val = q_number(n, q)

        if (not np.isfinite(prev.real)) or abs(val) < 1e-300 or (not np.isfinite(val.real)) or (not np.isfinite(val.imag)):
            log_fact[n] = -np.inf + 0.0j
        else:
            log_fact[n] = prev + cmath.log(val)
    return log_fact


# ============================================================
# 2) Quantum 6j symbol (q-Racah) using doubled spins J=2j
# ============================================================

def tri_ok(J1: int, J2: int, J3: int) -> bool:
    """Triangle + parity in doubled-spin integers."""
    return (abs(J1 - J2) <= J3 <= (J1 + J2)) and ((J1 + J2 + J3) % 2 == 0)


def q_delta_log(Ja: int, Jb: int, Jc: int, log_fact: np.ndarray) -> complex:
    """
    log( Δ_q(Ja,Jb,Jc) ) where Δ_q(a,b,c) = sqrt( [a+b-c]! [a-b+c]! [-a+b+c]! / [a+b+c+1]! )
    in doubled-spin units.
    """
    if not tri_ok(Ja, Jb, Jc):
        return -np.inf + 0.0j

    a = (Ja + Jb - Jc) // 2
    b = (Ja - Jb + Jc) // 2
    c = (-Ja + Jb + Jc) // 2
    d = (Ja + Jb + Jc) // 2 + 1

    if min(a, b, c, d) < 0:
        return -np.inf + 0.0j

    lf = (log_fact[a], log_fact[b], log_fact[c], log_fact[d])
    if any(not np.isfinite(z.real) for z in lf):
        return -np.inf + 0.0j

    return 0.5 * (log_fact[a] + log_fact[b] + log_fact[c] - log_fact[d])


def quantum_6j(J1: int, J2: int, J3: int, J4: int, J5: int, J6: int, q: complex, log_fact: np.ndarray) -> complex:
    """
    Quantum 6j symbol {j1 j2 j3; j4 j5 j6}_q in doubled-spin units.

    Formula structure matches the MoA session's log-domain implementation:
      - triangle checks on the 4 faces
      - product of Δ_q prefactors
      - Racah sum over z with (-1)^z factor
    """
    # Triangle conditions (4 faces)
    if not (tri_ok(J1, J2, J3) and tri_ok(J1, J5, J6) and tri_ok(J4, J2, J6) and tri_ok(J4, J5, J3)):
        return 0.0 + 0.0j

    log_pref = (
        q_delta_log(J1, J2, J3, log_fact)
        + q_delta_log(J1, J5, J6, log_fact)
        + q_delta_log(J4, J2, J6, log_fact)
        + q_delta_log(J4, J5, J3, log_fact)
    )
    if not np.isfinite(log_pref.real):
        return 0.0 + 0.0j

    # z-range (integer)
    s1 = (J1 + J2 + J3) // 2
    s2 = (J1 + J5 + J6) // 2
    s3 = (J4 + J2 + J6) // 2
    s4 = (J4 + J5 + J3) // 2

    t1 = (J1 + J2 + J4 + J5) // 2
    t2 = (J2 + J3 + J5 + J6) // 2
    t3 = (J3 + J1 + J6 + J4) // 2

    z_min = max(s1, s2, s3, s4)
    z_max = min(t1, t2, t3)
    if z_min > z_max:
        return 0.0 + 0.0j

    sum_val = 0.0 + 0.0j
    for z in range(z_min, z_max + 1):
        # log((-1)^z) = i*pi*z (mod 2)
        log_sign = 0.0j if (z % 2 == 0) else 1j * math.pi
        log_num = log_fact[z + 1] + log_sign

        den_args = [z - s1, z - s2, z - s3, z - s4, t1 - z, t2 - z, t3 - z]
        if any(a < 0 for a in den_args):
            continue
        if any(not np.isfinite(log_fact[a].real) for a in den_args):
            continue

        log_den = sum(log_fact[a] for a in den_args)
        sum_val += cmath.exp(log_pref + log_num - log_den)

    return sum_val


# ============================================================
# 3) MoA-style rank-8 tensor -> flattened transfer matrix M
#    (factorized build: avoids explicit d^8 loops)
# ============================================================

def spin_basis(j_max: float) -> Tuple[List[float], List[int]]:
    """
    Spins allowed: j = 0, 1/2, 1, ..., j_max
    Represented by doubled integers J = 2j = 0,1,2,...,2*j_max
    """
    J_max = int(round(2 * j_max))
    J_vals = list(range(0, J_max + 1))
    j_vals = [J / 2.0 for J in J_vals]
    return j_vals, J_vals


def weight_spin(j: float, beta: float, energy_scale: float) -> float:
    """Character-expansion-ish weight: (2j+1)*exp(-beta*j(j+1)*energy_scale)."""
    return (2 * j + 1.0) * math.exp(-beta * j * (j + 1.0) * energy_scale)


def build_transfer_matrix_M(
    j_max: float,
    q: complex,
    beta: float = 0.5,
    energy_scale: float = 0.1,
    threshold_6j: float = 1e-15,
    normalize: bool = True,
    verbose: bool = True,
) -> Dict[str, Any]:
    """
    Build the MoA rank-8 vertex tensor in the specific coupling pattern:
        T_{xp,xm,yp,ym,zp,zm,tp,tm} = sum_{j_int} w(all spins)* 6j(x,y; j_int)*6j(z,t; j_int)
    and then flatten it to M of shape (d^4, d^4) with rows=(xp,xm,yp,ym), cols=(zp,zm,tp,tm).

    Uses factorization:
        M[r,c] = w_row[r]*w_col[c] * sum_k w_int[k] * U[r,k] * V[c,k]
        where U[r,k]=6j(xp,xm,k, yp,ym,k), V[c,k]=6j(zp,zm,k, tp,tm,k)
    """
    j_vals, J_vals = spin_basis(j_max)
    d = len(j_vals)
    n = d**4

    # Conservative factorial cutoff
    n_max = int(8 * j_max + 10)
    log_fact = log_q_factorials_table(n_max, q)

    # Internal weights (k dimension)
    w_int = np.array([weight_spin(j, beta, energy_scale) for j in j_vals], dtype=np.float64)

    # Enumerate 4-index "boundary states"
    states4 = np.array(list(np.ndindex((d,) * 4)), dtype=np.int32)  # (n,4)

    # Boundary weights factorize by index
    w_row = np.ones(n, dtype=np.float64)
    for ax in range(4):
        w_row *= np.array([weight_spin(j_vals[i], beta, energy_scale) for i in states4[:, ax]], dtype=np.float64)
    w_col = w_row.copy()

    # Cache 6j values
    @functools.lru_cache(None)
    def s6j(J1, J2, J3, J4, J5, J6):
        return quantum_6j(J1, J2, J3, J4, J5, J6, q, log_fact)

    # Build U and V (n*d entries each)
    U = np.zeros((n, d), dtype=np.complex128)
    V = np.zeros((n, d), dtype=np.complex128)

    for r in range(n):
        ixp, ixm, iyp, iym = map(int, states4[r])
        Jxp, Jxm, Jyp, Jym = J_vals[ixp], J_vals[ixm], J_vals[iyp], J_vals[iym]
        for k in range(d):
            Jint = J_vals[k]
            val = s6j(Jxp, Jxm, Jint, Jyp, Jym, Jint)
            U[r, k] = val if abs(val) > threshold_6j else 0.0 + 0.0j

    for c in range(n):
        izp, izm, itp, itm = map(int, states4[c])
        Jzp, Jzm, Jtp, Jtm = J_vals[izp], J_vals[izm], J_vals[itp], J_vals[itm]
        for k in range(d):
            Jint = J_vals[k]
            val = s6j(Jzp, Jzm, Jint, Jtp, Jtm, Jint)
            V[c, k] = val if abs(val) > threshold_6j else 0.0 + 0.0j

    # Big matmul: S = (U * w_int) @ V^T
    if HAVE_JAX:
        Uj = jnp.array(U)
        Vj = jnp.array(V)
        wintj = jnp.array(w_int)
        wrowj = jnp.array(w_row)
        wcolj = jnp.array(w_col)

        S = (Uj * wintj[None, :]) @ Vj.T
        M = (wrowj[:, None] * wcolj[None, :]) * S
        M = np.array(M)  # back to numpy for graph ops
    else:
        S = (U * w_int[None, :]) @ V.T
        M = (w_row[:, None] * w_col[None, :]) * S


    if normalize:
        m = float(np.max(np.abs(M)))
        if m > 0:
            M = M / m

    nnz = int((np.abs(M) > 1e-15).sum())
    if verbose:
        print("=== Building MoA-style transfer matrix from rank-8 tensor ===")
        print(f"j_max={j_max}  => d={d}, n=d^4={n}")
        print(f"q={q}")
        print(f"M shape={M.shape}, nonzero(|M|>1e-15)={nnz} / {n*n}")

    return dict(
        M=M,
        d=d,
        n=n,
        states4=states4,
        j_vals=j_vals,
        J_vals=J_vals,
        w_int=w_int,
    )


# ============================================================
# 4) Turn transfer matrix into a nonnegative kernel K (entrywise)
# ============================================================

def nonnegative_kernel_from_M(M: np.ndarray, mode: str = "abs2", reg_eps: float = 0.0) -> np.ndarray:
    """
    mode:
      - "abs2": K_ij = |M_ij|^2   (double-layer weight; usually the least offensive positivity hack)
      - "abs" : K_ij = |M_ij|
    reg_eps:
      - if >0, replaces exact zeros by reg_eps (NOT recommended for physics; use SCC restriction instead)
    """
    if mode == "abs2":
        K = np.abs(M) ** 2
    elif mode == "abs":
        K = np.abs(M)
    else:
        raise ValueError("mode must be 'abs2' or 'abs'")

    if reg_eps > 0:
        K = np.where(K > 0, K, reg_eps)

    return K.astype(np.float64)


# ============================================================
# 5) Strongly connected components, dominant PF block
# ============================================================

def tarjan_scc(neighbors: List[List[int]]) -> List[List[int]]:
    """Tarjan SCC in O(V+E)."""
    import sys
    sys.setrecursionlimit(1000000)

    n = len(neighbors)
    index = 0
    stack = []
    onstack = [False] * n
    idx = [-1] * n
    low = [0] * n
    comps = []

    def strongconnect(v: int):
        nonlocal index
        idx[v] = index
        low[v] = index
        index += 1
        stack.append(v)
        onstack[v] = True

        for w in neighbors[v]:
            if idx[w] == -1:
                strongconnect(w)
                low[v] = min(low[v], low[w])
            elif onstack[w]:
                low[v] = min(low[v], idx[w])

        if low[v] == idx[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack[w] = False
                comp.append(w)
                if w == v:
                    break
            comps.append(comp)

    for v in range(n):
        if idx[v] == -1:
            strongconnect(v)

    return comps


def pf_spectral_radius_power(K: np.ndarray, n_iter: int = 200) -> float:
    """Cheap spectral radius estimate for nonnegative irreducible-ish blocks."""
    n = K.shape[0]
    v = np.ones(n, dtype=np.float64)
    lam = 0.0
    for _ in range(n_iter):
        w = K @ v
        lam_new = float(np.max(w))
        if lam_new <= 0:
            return 0.0
        v = w / lam_new
        lam = lam_new
    return lam


def dominant_pf_block(K: np.ndarray, verbose: bool = True) -> Dict[str, Any]:
    """
    Decompose support graph into SCCs; pick SCC block with maximal PF spectral radius.
    """
    n = K.shape[0]
    neighbors = [list(np.flatnonzero(K[i] > 0)) for i in range(n)]
    comps = tarjan_scc(neighbors)

    best_comp = None
    best_lam = -1.0

    for comp in comps:
        sub = K[np.ix_(comp, comp)]
        lam = pf_spectral_radius_power(sub, n_iter=150)
        if lam > best_lam:
            best_lam = lam
            best_comp = comp

    block = sorted(best_comp)
    if verbose:
        print("\n=== SCC / PF dominant sector ===")
        print(f"#SCCs = {len(comps)}")
        print(f"Dominant SCC size = {len(block)}")
        print(f"Estimated PF lambda (block) ≈ {best_lam:.12e}")

    return dict(block=block, comps=comps, lam_est=best_lam)


# ============================================================
# 6) Doob transform (PF -> Markov), mass gap, minorization bound
# ============================================================

def pf_eigenpair_power(K: np.ndarray, n_iter: int = 600, tol: float = 1e-12) -> Tuple[float, np.ndarray]:
    """
    PF eigenpair for nonnegative irreducible K using max-normalized power iteration.
    Returns (lambda_pf, v_pf) with v_pf L1-normalized.
    """
    n = K.shape[0]
    v = np.ones(n, dtype=np.float64)
    lam = 0.0

    for _ in range(n_iter):
        w = K @ v
        lam_new = float(np.max(w))
        if lam_new <= 0:
            return 0.0, v / np.linalg.norm(v, 1)
        v_new = w / lam_new
        if np.linalg.norm(v_new - v) <= tol * np.linalg.norm(v):
            lam = lam_new
            v = v_new
            break
        lam = lam_new
        v = v_new

    v = v / np.linalg.norm(v, 1)
    return lam, v


def doob_transform(K: np.ndarray) -> Tuple[float, np.ndarray, np.ndarray]:
    """
    Doob transform of a nonnegative matrix K:
        P_ij = K_ij * v_j / (lambda * v_i)
    where (lambda, v) is the PF eigenpair of K.
    """
    lam, v = pf_eigenpair_power(K)
    if lam <= 0:
        raise ValueError("PF eigenvalue nonpositive; K likely all zeros?")
    P = (K * v[None, :]) / (lam * v[:, None])
    return lam, v, P


def markov_spectrum_mass(P: np.ndarray) -> Dict[str, Any]:
    """
    For a Markov kernel P, eigenvalues satisfy |λ|<=1, λ1=1.
    Mass gap proxy: m = -log(|λ2|)
    """
    evals = np.linalg.eigvals(P)
    mags = np.sort(np.abs(evals))[::-1]
    lam2 = float(mags[1]) if len(mags) > 1 else 0.0
    mass = float(-math.log(max(lam2, 1e-300))) if lam2 > 0 else float("inf")
    return dict(evals=evals, mags=mags, lam2=lam2, mass=mass)


def minorization_epsilon(Pk: np.ndarray) -> float:
    """ε_k = sum_j min_i (P^k)_{ij}."""
    return float(Pk.min(axis=0).sum())


def best_minorization_bound(P: np.ndarray, k_max: int = 64) -> Dict[str, Any]:
    """
    Scan k=1..k_max for best Doeblin/minorization lower bound on mass:
      m >= -(1/k) log(1-ε_k)
    """
    n = P.shape[0]
    Pk = np.eye(n, dtype=np.float64)
    best = dict(k=None, eps=0.0, mass_bound=0.0)

    for k in range(1, k_max + 1):
        Pk = Pk @ P
        eps = minorization_epsilon(Pk)
        if eps <= 0:
            continue
        mass_bound = -(1.0 / k) * math.log(max(1.0 - eps, 1e-300))
        if mass_bound > best["mass_bound"]:
            best = dict(k=k, eps=eps, mass_bound=mass_bound)

    return best


# Fast eps_k curve in JAX (optional but nice)

# Fast eps_k curve in JAX (optional). If JAX is not available, we use a NumPy fallback.
if HAVE_JAX:
    @functools.partial(jax.jit, static_argnames=("k_max",))
    def eps_curve_jax(P: "jnp.ndarray", k_max: int = 64):
        n = P.shape[0]
        Pk0 = jnp.eye(n, dtype=P.dtype)

        def step(Pk, _):
            Pk = Pk @ P
            eps = jnp.sum(jnp.min(Pk, axis=0))
            return Pk, eps

        _, eps_seq = jax.lax.scan(step, Pk0, xs=jnp.arange(k_max))
        return eps_seq
else:
    def eps_curve_jax(P, k_max: int = 64):
        # NumPy fallback: returns np.ndarray of eps_k
        P = np.array(P, dtype=np.float64)
        n = P.shape[0]
        Pk = np.eye(n, dtype=np.float64)
        eps = np.zeros(k_max, dtype=np.float64)
        for k in range(1, k_max + 1):
            Pk = Pk @ P
            eps[k-1] = minorization_epsilon(Pk)
        return eps



def analyze_rank8_transfer_gap(
    j_max: float = 1.0,
    q: complex = 0.95,
    beta: float = 0.5,
    energy_scale: float = 0.1,
    kernel_mode: str = "abs2",
    reg_eps: float = 0.0,
    k_max: int = 64,
    verbose: bool = True,
    make_plots: bool = True,
) -> Dict[str, Any]:
    """
    End-to-end:
      1) build M (flattened transfer matrix) from MoA rank-8 tensor logic
      2) build entrywise nonnegative kernel K (default: |M|^2)
      3) find SCC dominant PF sector, restrict to it
      4) Doob transform => Markov kernel P
      5) compute mass m = -log|λ2(P)|
      6) Doeblin/minorization certified lower bound
    """
    built = build_transfer_matrix_M(
        j_max=j_max, q=q, beta=beta, energy_scale=energy_scale, verbose=verbose
    )
    M = built["M"]
    states4 = built["states4"]
    j_vals = built["j_vals"]

    K = nonnegative_kernel_from_M(M, mode=kernel_mode, reg_eps=reg_eps)
    nnzK = int((K > 0).sum())
    if verbose:
        print("\n=== Nonnegative kernel K from M ===")
        print(f"mode={kernel_mode}, reg_eps={reg_eps:.1e}")
        print(f"K: min={K.min():.3e}, max={K.max():.3e}, density={(K>0).mean():.6f} ({nnzK}/{K.size})")

    # SCC dominant block
    dom = dominant_pf_block(K, verbose=verbose)
    block = dom["block"]

    Kb = K[np.ix_(block, block)]
    lam_pf, v_pf, P = doob_transform(Kb)

    # Sanity: row sums
    row_err = float(np.max(np.abs(P.sum(axis=1) - 1.0)))

    spec = markov_spectrum_mass(P)
    bound = best_minorization_bound(P, k_max=k_max)

    if verbose:
        print("\n=== Doob/Markov + mass gap ===")
        print(f"Block size={len(block)} (out of n={K.shape[0]})")
        print(f"PF lambda(K_block) ≈ {lam_pf:.12e}")
        print(f"Row-sum max error ≈ {row_err:.3e}")
        print(f"|lambda2(P)| ≈ {spec['lam2']:.12e}")
        print(f"Mass gap m = -log|λ2| ≈ {spec['mass']:.12e}")
        if bound["k"] is None:
            print(f"Minorization: no eps_k>0 found up to k_max={k_max}.")
        else:
            print(f"Minorization best: k={bound['k']}, eps_k={bound['eps']:.12e}, m_bound={bound['mass_bound']:.12e}")

        # Decode which boundary states live in the dominant block
        print("\nDominant block boundary states (indices -> spins):")
        for idx in block:
            tup = states4[idx].tolist()
            spins = [j_vals[i] for i in tup]
            print(f"  state {idx:3d}: idx={tup}   j={spins}")

    out = dict(
        built=built,
        K=K,
        dom=dom,
        block=block,
        K_block=Kb,
        pf_lambda=lam_pf,
        pf_vec=v_pf,
        P=P,
        row_sum_err=row_err,
        spec=spec,
        bound=bound,
    )

    if make_plots:
        # eps_k curve and certified m_k curve (computed in JAX for speed/stability)
        Pj = jnp.array(P, dtype=jnp.float64)
        eps_seq = np.array(eps_curve_jax(Pj, k_max=k_max))
        ks = np.arange(1, k_max + 1, dtype=np.float64)
        m_lb = -(1.0 / ks) * np.log(np.maximum(1.0 - eps_seq, 1e-300))

        plt.figure()
        plt.plot(ks, m_lb)
        plt.xlabel("k (power in P^k)")
        plt.ylabel(r"certified lower bound  $m_k = -(1/k)\log(1-\epsilon_k)$")
        plt.title("Doeblin/minorization certified mass lower bound vs k")
        plt.grid(True)
        plt.show()

        plt.figure()
        plt.plot(ks, eps_seq)
        plt.xlabel("k (power in P^k)")
        plt.ylabel(r"$\epsilon_k = \sum_j \min_i (P^k)_{ij}$")
        plt.title("Doeblin epsilon_k vs k")
        plt.grid(True)
        plt.ylim(-0.05, 1.05)
        plt.show()

        out["eps_seq"] = eps_seq
        out["m_lb_seq"] = m_lb

    return out


# ============================================================
# 7) Run (edit params here)
# ============================================================

if __name__ == "__main__":
    results = analyze_rank8_transfer_gap(
        j_max=1.0,
        q=0.95,          # try 0.85..0.99 (real) or q=np.exp(1j*theta) (complex)
        beta=0.5,
        energy_scale=0.1,
        kernel_mode="abs2",   # "abs2" is recommended
        reg_eps=0.0,          # IMPORTANT: keep 0; use SCC restriction instead of filling zeros
        k_max=64,
        verbose=True,
        make_plots=True,
    )
