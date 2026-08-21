#!/usr/bin/env python3
"""
ENGINE_FLUX_lci_typicality_diagnostic.py

Local Cap-Intersection (LCI) typicality diagnostic for SU(2) Wilson on the
exact-HB Stage B ensemble.

Following NOTE_PMBSF_lci_tosj_reduction_lemmaq_2026_05_26.md sections 4 and 9.7, this
script measures, for each (target plaquette p, incident link e of p) and each
non-empty subset A of the 5 other plaquettes through e,

    chi_0(A; p, e) = u_A . n_p  -  a,
    u_A = argmax_{u in S^3, u.n_r <= a for r in A} m_e . u.

The local-good event is

    G^LCI = { min_{A non-empty} chi_0(A) >= chi_0^* }

for a target margin chi_0^*. This is the geometric statement used to derive
Lemma Q via the LCI -> TOS+J chain in the project master document.

QUATERNION / GEOMETRY CONVENTION (project's)
    Each SU(2) link is a unit quaternion U = (q0, q1, q2, q3) in S^3 c R^4
    with (1/2) Re Tr(U) = q0.

    For each plaquette p containing link e, there is a unit quaternion n_p
    (a 4-vector with ||n_p||=1) such that

        (1/2) Re Tr(U_p) = U_e . n_p

    in the R^4 dot product. Concretely, for e = (x, mu):
      - positively-oriented plaquette in (mu, +nu) plane:
          n_p = qconj( U(x+mu,nu) U(x+nu,mu)^c U(x,nu)^c )
      - negatively-oriented plaquette in (mu, -nu) plane:
          n_p =        U(x-nu,nu)^c U(x-nu,mu) U(x-nu+mu,nu)
    where ^c is quaternion conjugation = SU(2) inverse.

    The conditional heat-bath law of U_e given U_{e^c} is
        P(u | rest) propto exp(beta * u . H_e),
        H_e = sum_{p containing e} n_p   (4-vector, not unit),
        m_e = H_e / ||H_e||,  kappa_e = beta * ||H_e||.

CAP DEFINITION
    C_r = { u in S^3 : u . n_r <= a },  a = 1 - (t - eta),
    where t is the "high plaquette" threshold on the defect 1 - (1/2) Re Tr(U_p),
    and eta is the ramp width. Defaults: t = 1.0104245908659366, eta = 0.005.

INPUTS
    --configs PATH
        Numpy .npy file shape (N_cfg, L, L, L, L, 4, 4) of pre-thermalized
        SU(2) Wilson configurations. The last two axes are
        (direction mu in 0..3, quaternion component q_a in 0..3).
        Periodic boundary conditions assumed.
    --test
        Self-contained: thermalize a tiny L=4 lattice in pure NumPy, then run.

OUTPUTS (in --out-dir, default 'results/lci')
    lci_rows.csv         Per-(config, block, p, e) measurements.
    lci_summary.json     Aggregate stats (LCI-good fractions, margin quantiles).
    lci_log.txt          Parameters and timings.

USAGE
    # Production, with cached configs:
    python ENGINE_FLUX_lci_typicality_diagnostic.py --configs configs.npy \
        --beta 3.5 --block-side 10 --core-margin 3 \
        --blocks-per-config 8 --t 1.0104245908659366 --eta 0.005 \
        --subset-mode key --out-dir results/lci

    # Exhaustive 31-subset enumeration on a smaller sample:
    python ENGINE_FLUX_lci_typicality_diagnostic.py --configs configs.npy \
        --subset-mode full --blocks-per-config 2 --max-links-per-block 200 \
        --out-dir results/lci_full

    # Self-test on tiny lattice (no external configs needed):
    python ENGINE_FLUX_lci_typicality_diagnostic.py --test
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import time
from dataclasses import dataclass, asdict, fields
from itertools import combinations
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

import numpy as np


# =============================================================================
# Quaternion arithmetic (4-vector representation of SU(2))
# =============================================================================
# U = q0 * I + i * (q1*sigma_1 + q2*sigma_2 + q3*sigma_3),    q.q = 1.
# (1/2) Re Tr(U) = q0.  Scal(q*r) = q . qconj(r)  (R^4 dot product).

def qmul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Hamilton product a * b. Broadcasts; last axis must have length 4."""
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0,
    ], axis=-1)


def qconj(a: np.ndarray) -> np.ndarray:
    """Quaternion conjugate = SU(2) inverse for unit quaternions."""
    out = np.asarray(a, dtype=float).copy()
    out[..., 1:] *= -1
    return out


def qmul3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return qmul(qmul(a, b), c)


def qrand(n: int, rng: np.random.Generator) -> np.ndarray:
    """n uniform unit quaternions, shape (n, 4)."""
    v = rng.standard_normal((n, 4))
    return v / np.linalg.norm(v, axis=-1, keepdims=True)


# =============================================================================
# Lattice geometry (4D periodic torus)
# =============================================================================
D = 4  # spacetime dimensions


def shift(x: Tuple[int, ...], mu: int, sign: int, L: int) -> Tuple[int, ...]:
    """Periodic-BC shift of site x in direction mu by sign units."""
    y = list(x)
    y[mu] = (y[mu] + sign) % L
    return tuple(y)


def plaquette_normal(U: np.ndarray, x: Tuple[int, ...], mu: int, nu: int,
                     sign_nu: int, L: int) -> np.ndarray:
    """
    Returns n_p (unit-quaternion 4-vector) for the plaquette in the (mu, nu)
    plane on the +sign_nu side of link e = (x, mu), such that
        (1/2) Re Tr(U_p) = U_e . n_p   in R^4 dot product.

    sign_nu = +1: plaquette P_{x, mu nu}; e appears as first link, n_p = conj(V_+)
                  with V_+ = U(x+mu,nu) U(x+nu,mu)^c U(x,nu)^c.
    sign_nu = -1: plaquette P_{x-nu, mu nu}; e appears as third link as inverse,
                  cyclic + Tr(U_e^c W) = Tr(U_e W^c) identity gives
                  n_p = U(x-nu,nu)^c U(x-nu,mu) U(x-nu+mu,nu).
    """
    if sign_nu == +1:
        x_pm = shift(x, mu, +1, L)
        x_pn = shift(x, nu, +1, L)
        V_plus = qmul3(U[x_pm + (nu,)],
                       qconj(U[x_pn + (mu,)]),
                       qconj(U[x + (nu,)]))
        return qconj(V_plus)
    else:
        x_mn = shift(x, nu, -1, L)
        x_mnpm = shift(x_mn, mu, +1, L)
        return qmul3(qconj(U[x_mn + (nu,)]),
                     U[x_mn + (mu,)],
                     U[x_mnpm + (nu,)])


def link_normals(U: np.ndarray, x: Tuple[int, ...], mu: int, L: int
                 ) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
    """
    Compute n_p for all 6 plaquettes containing link e = (x, mu).
    Returns:
      normals: (6, 4) array of n_p
      ids:     list of (nu, sign_nu), one per row
    """
    normals = np.empty((6, 4))
    ids: List[Tuple[int, int]] = []
    idx = 0
    for nu in range(D):
        if nu == mu:
            continue
        for sign_nu in (+1, -1):
            normals[idx] = plaquette_normal(U, x, mu, nu, sign_nu, L)
            ids.append((nu, sign_nu))
            idx += 1
    return normals, ids


def plaquette_value_re_tr_half(U: np.ndarray, x: Tuple[int, ...],
                               mu: int, nu: int, L: int) -> float:
    """(1/2) Re Tr(U_p) for the standard plaquette P_{x, mu nu}, mu < nu."""
    x_pm = shift(x, mu, +1, L)
    x_pn = shift(x, nu, +1, L)
    U_p = qmul3(U[x + (mu,)],
                U[x_pm + (nu,)],
                qmul(qconj(U[x_pn + (mu,)]), qconj(U[x + (nu,)])))
    return float(U_p[0])


def all_plaquettes_mean_defect(U: np.ndarray, x0: Tuple[int, ...],
                               side: int, L: int) -> float:
    """
    Mean of  1 - (1/2) Re Tr(U_p)  over all D*(D-1)/2 oriented planes and all
    sites x with x_d in [x0_d, x0_d + side) for each d (with periodic wrap).
    """
    total = 0.0
    count = 0
    for d0 in range(side):
        for d1 in range(side):
            for d2 in range(side):
                for d3 in range(side):
                    x = ((x0[0] + d0) % L, (x0[1] + d1) % L,
                         (x0[2] + d2) % L, (x0[3] + d3) % L)
                    for mu in range(D):
                        for nu in range(mu + 1, D):
                            total += 1.0 - plaquette_value_re_tr_half(U, x, mu, nu, L)
                            count += 1
    return total / max(count, 1)


# =============================================================================
# Cap-intersection optimizer
# =============================================================================
# Goal:   max u.m  subject to  u.u = 1  and  u.n_r <= a  for r in A.
# Method: enumerate active sets A_act subset A.  For each A_act, find the
#         unique critical point with u.n_r = a for r in A_act and u.u = 1,
#         maximising u.m on that constrained subsphere.  Discard candidates
#         that violate u.n_r <= a for r in A \ A_act.  Take max over feasible.

def constrained_max_on_sphere(m: np.ndarray, N: np.ndarray, a: float,
                              tol: float = 1e-12
                              ) -> Tuple[Optional[np.ndarray], float]:
    """
    Solve:  max u.m  s.t.  u.u = 1  AND  N @ u = a * 1_k  (k equality constraints).

    N: (k, 4) array of constraint normals (need not be lin. indep. but
       redundant rows are detected via Gram singularity and rejected).
    Returns (u, value) on success, (None, -inf) if infeasible.

    Closed form:
        u0 = N^T (N N^T)^-1 (a 1_k)    (min-norm point in the affine subspace)
        if ||u0||^2 > 1: subspace doesn't reach S^3, infeasible.
        m_perp = m - N^T (N N^T)^-1 (N m)   (projection of m onto null(N))
        u* = u0 + sqrt(1 - ||u0||^2) * m_perp / ||m_perp||
    """
    if N.size == 0 or N.shape[0] == 0:
        nm = float(np.linalg.norm(m))
        if nm < tol:
            return np.array([1.0, 0.0, 0.0, 0.0]), 0.0
        u = m / nm
        return u, float(u @ m)

    # Gram matrix of constraint normals
    G = N @ N.T  # (k, k)
    try:
        # Use solve rather than inv for numerical robustness on small systems
        Ginv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return None, -np.inf

    k = N.shape[0]
    b = a * np.ones(k)
    lam = Ginv @ b
    u0 = N.T @ lam
    s = float(u0 @ u0)
    if s > 1.0 - tol:
        return None, -np.inf  # affine subspace too far from origin

    m_perp = m - N.T @ (Ginv @ (N @ m))
    mp = float(np.linalg.norm(m_perp))

    if mp < tol:
        # u.m is constant on the intersection sphere.  Pick any feasible u.
        for j in range(4):
            ej = np.zeros(4)
            ej[j] = 1.0
            ep = ej - N.T @ (Ginv @ (N @ ej))
            ne = float(np.linalg.norm(ep))
            if ne > tol:
                u = u0 + math.sqrt(max(0.0, 1.0 - s)) * (ep / ne)
                return u, float(u @ m)
        return None, -np.inf

    u = u0 + math.sqrt(max(0.0, 1.0 - s)) * (m_perp / mp)
    return u, float(u @ m)


def solve_cap_intersection_max(m: np.ndarray, n_list: Sequence[np.ndarray],
                               a: float, ineq_tol: float = 1e-9
                               ) -> Tuple[Optional[np.ndarray], float, Tuple[int, ...]]:
    """
    max u.m  s.t.  u in S^3,  u.n_r <= a  for r in n_list.
    Active-set enumeration.  Returns (u, value, active_set_idx_tuple).
    """
    n_arr = np.asarray(n_list, dtype=float)
    A_size = len(n_arr)

    best_u: Optional[np.ndarray] = None
    best_val = -np.inf
    best_act: Tuple[int, ...] = ()

    for active_mask in range(1 << A_size):
        active_idx = tuple(i for i in range(A_size) if (active_mask >> i) & 1)
        if active_idx:
            N_act = n_arr[list(active_idx)]
        else:
            N_act = np.zeros((0, 4))

        u, val = constrained_max_on_sphere(m, N_act, a)
        if u is None:
            continue

        # Check inactive inequality constraints
        feasible = True
        for j in range(A_size):
            if j in active_idx:
                continue
            if float(n_arr[j] @ u) > a + ineq_tol:
                feasible = False
                break
        if not feasible:
            continue

        if val > best_val:
            best_val = val
            best_u = u
            best_act = active_idx

    return best_u, best_val, best_act


# =============================================================================
# LCI margin per (p, e)
# =============================================================================

def lci_margin_full(m_e: np.ndarray, n_p: np.ndarray,
                    n_neighbors: Sequence[np.ndarray], a: float
                    ) -> Tuple[float, int, Tuple[int, ...], float]:
    """
    Compute  min_{A non-empty, A subset of neighbors}  ( u_A . n_p  -  a ).

    Returns (min_chi0, worst_size, worst_idx, m_dot_u_at_worst).
    """
    A_size = len(n_neighbors)
    best_min = np.inf
    best_size = -1
    best_idx: Tuple[int, ...] = ()
    best_m_dot_u = float("nan")

    for k in range(1, A_size + 1):
        for subset in combinations(range(A_size), k):
            sub_n = [n_neighbors[i] for i in subset]
            u_A, m_dot_u, _ = solve_cap_intersection_max(m_e, sub_n, a)
            if u_A is None:
                continue
            chi0 = float(u_A @ n_p) - a
            if chi0 < best_min:
                best_min = chi0
                best_size = k
                best_idx = subset
                best_m_dot_u = m_dot_u

    return best_min, best_size, best_idx, best_m_dot_u


def lci_margin_key_subsets(m_e: np.ndarray, n_p: np.ndarray,
                           n_neighbors: Sequence[np.ndarray], a: float
                           ) -> Tuple[float, int, Tuple[int, ...], float,
                                       List[float], float]:
    """
    Cheaper diagnostic: compute chi_0 for the 5 singletons and for the full
    5-element subset only.  Return min over these 6, plus the singleton
    margins and the full-subset margin.

    Returns (min_chi0_key, worst_size, worst_idx, m_dot_u_at_worst,
             singleton_chi0_list, full_chi0).
    """
    A_size = len(n_neighbors)
    singleton_chi0: List[float] = []
    best_min = np.inf
    best_size = -1
    best_idx: Tuple[int, ...] = ()
    best_m_dot_u = float("nan")

    # Singletons
    for i in range(A_size):
        u_A, m_dot_u, _ = solve_cap_intersection_max(m_e, [n_neighbors[i]], a)
        if u_A is None:
            singleton_chi0.append(float("nan"))
            continue
        chi0 = float(u_A @ n_p) - a
        singleton_chi0.append(chi0)
        if chi0 < best_min:
            best_min = chi0
            best_size = 1
            best_idx = (i,)
            best_m_dot_u = m_dot_u

    # Full set
    u_full, m_dot_u_full, _ = solve_cap_intersection_max(m_e, list(n_neighbors), a)
    if u_full is not None:
        full_chi0 = float(u_full @ n_p) - a
        if full_chi0 < best_min:
            best_min = full_chi0
            best_size = A_size
            best_idx = tuple(range(A_size))
            best_m_dot_u = m_dot_u_full
    else:
        full_chi0 = float("nan")

    return best_min, best_size, best_idx, best_m_dot_u, singleton_chi0, full_chi0


# =============================================================================
# SU(2) Wilson heat-bath sampler (used only for --test mode)
# =============================================================================

def sample_vmf_s3(mean_dir: np.ndarray, kappa: float,
                  rng: np.random.Generator) -> np.ndarray:
    """
    Sample a unit quaternion from vMF_4 on S^3 with mean_dir and concentration kappa.
    Uses Wood (1994) acceptance-rejection.  For p = 4 the marginal density of
    w = u.mean_dir is propto (1 - w^2)^{1/2} exp(kappa w) on [-1, 1].
    """
    p = 4
    if kappa < 1e-10:
        v = rng.standard_normal(p)
        return v / np.linalg.norm(v)

    # Wood envelope parameters
    b = (-2.0 * kappa + math.sqrt(4.0 * kappa * kappa + (p - 1) ** 2)) / (p - 1)
    x0 = (1.0 - b) / (1.0 + b)
    c = kappa * x0 + (p - 1) * math.log(1.0 - x0 * x0)

    # Rejection loop for w
    while True:
        z = float(rng.beta((p - 1) / 2.0, (p - 1) / 2.0))
        w = (1.0 - (1.0 + b) * z) / (1.0 - (1.0 - b) * z)
        log_u = math.log(float(rng.uniform()))
        if kappa * w + (p - 1) * math.log(1.0 - x0 * w) - c >= log_u:
            break

    # Uniform direction in 3-plane orthogonal to mean_dir
    v = rng.standard_normal(p)
    v = v - (v @ mean_dir) * mean_dir
    nv = float(np.linalg.norm(v))
    if nv < 1e-14:
        # Pick an arbitrary orthogonal direction
        for j in range(p):
            ej = np.zeros(p); ej[j] = 1.0
            v = ej - (ej @ mean_dir) * mean_dir
            nv = float(np.linalg.norm(v))
            if nv > 1e-14:
                break
    v = v / nv

    return float(w) * mean_dir + math.sqrt(max(0.0, 1.0 - w * w)) * v


def staple_sum_at_link(U: np.ndarray, x: Tuple[int, ...], mu: int, L: int
                       ) -> np.ndarray:
    """H_e = sum of n_p over the 6 plaquettes through link (x, mu)."""
    normals, _ = link_normals(U, x, mu, L)
    return normals.sum(axis=0)


def heatbath_update_link(U: np.ndarray, x: Tuple[int, ...], mu: int,
                         beta: float, L: int, rng: np.random.Generator) -> None:
    """One exact heat-bath update of link (x, mu) in place."""
    H = staple_sum_at_link(U, x, mu, L)
    h_norm = float(np.linalg.norm(H))
    if h_norm < 1e-14:
        U[x + (mu,)] = qrand(1, rng)[0]
        return
    mean_dir = H / h_norm
    kappa = beta * h_norm
    U[x + (mu,)] = sample_vmf_s3(mean_dir, kappa, rng)


def heatbath_sweep(U: np.ndarray, beta: float, L: int,
                   rng: np.random.Generator) -> None:
    """Full lexicographic heat-bath sweep over all links."""
    # Lexicographic order; for serious work, use checkerboard or random order.
    it = np.ndindex(*([L] * D))
    for x in it:
        for mu in range(D):
            heatbath_update_link(U, x, mu, beta, L, rng)


def thermalize(L: int, beta: float, n_sweeps: int,
               rng: np.random.Generator, log_every: int = 10) -> np.ndarray:
    """Cold start, n_sweeps of exact heat-bath.  Returns the final config."""
    U = np.zeros((L, L, L, L, D, 4))
    U[..., 0] = 1.0  # all identity
    print(f"[therm] cold start, L={L}, beta={beta}, sweeps={n_sweeps}")
    t0 = time.time()
    for s in range(n_sweeps):
        heatbath_sweep(U, beta, L, rng)
        if (s + 1) % log_every == 0 or s == n_sweeps - 1:
            # Quick mean-plaquette estimate
            mp = 0.0
            count = 0
            for x in np.ndindex(*([L] * D)):
                for mu in range(D):
                    for nu in range(mu + 1, D):
                        mp += plaquette_value_re_tr_half(U, x, mu, nu, L)
                        count += 1
            print(f"[therm] sweep {s+1}/{n_sweeps}  "
                  f"<(1/2) Re Tr U_p> = {mp/count:.6f}  "
                  f"elapsed = {time.time()-t0:.1f}s")
    return U


# =============================================================================
# Block / core geometry
# =============================================================================

@dataclass(frozen=True)
class Block:
    origin: Tuple[int, int, int, int]
    side: int
    core_margin: int

    @property
    def core_side(self) -> int:
        return self.side - 2 * self.core_margin


def pick_block(L: int, side: int, core_margin: int,
               rng: np.random.Generator) -> Block:
    """Pick a random block origin so the block fits inside the lattice."""
    if side > L:
        raise ValueError(f"block side {side} exceeds lattice size {L}")
    origin = tuple(int(rng.integers(0, L - side + 1)) for _ in range(D))  # type: ignore
    return Block(origin=origin, side=side, core_margin=core_margin)


def core_links(block: Block, L: int) -> Iterable[Tuple[Tuple[int, ...], int]]:
    """
    Yield (site, mu) for every link e = (x, mu) such that x lies in the core
    of the block AND all 6 plaquettes through e lie inside the block (so the
    LCI geometry is well-defined relative to the frozen exterior).

    The core has corner block.origin + (core_margin, ...) and side core_side.
    For e = (x, mu) to have all 6 plaquettes inside the block, x must satisfy
    block_min <= x_d AND x_d <= block_max - 1  for all d != mu (because the
    transverse plaquette needs sites x +/- e_nu inside the block), and
    block_min <= x_mu AND x_mu + 1 <= block_max - 1 along the link direction
    (so x + mu is also a valid site, and the second-nearest x + 2*mu is not
    required since plaquettes only extend one step in each direction).

    With core margin M and block side B, sites of the form
        x_d in [origin_d + M, origin_d + B - M - 1]
    are in the core.  All plaquettes through links rooted at such x stay
    inside the block as long as M >= 1.
    """
    b0 = block.origin
    M = block.core_margin
    B = block.side
    if M < 1:
        # Plaquettes extend 1 step transversely; need M >= 1 for safety.
        # We still proceed, but the user is warned.
        pass
    lo = [b0[d] + M for d in range(D)]
    hi = [b0[d] + B - M - 1 for d in range(D)]  # inclusive upper

    # Iterate over all core sites
    rng_d = [range(lo[d], hi[d] + 1) for d in range(D)]
    for x0 in rng_d[0]:
        for x1 in rng_d[1]:
            for x2 in rng_d[2]:
                for x3 in rng_d[3]:
                    x = ((x0 % L), (x1 % L), (x2 % L), (x3 % L))
                    for mu in range(D):
                        # Need x + mu to also be in [lo, hi] for all transverse,
                        # but since M >= 1 the plaquette neighbours x +/- nu are
                        # still inside the block.  We do not need them to be in
                        # the core, only in the block, for the LCI geometry.
                        yield x, mu


# =============================================================================
# Data row
# =============================================================================

@dataclass
class LCIRow:
    config_idx: int
    block_idx: int
    block_avg_defect: float
    site0: int
    site1: int
    site2: int
    site3: int
    link_mu: int
    target_idx: int   # 0..5 within the link's 6 plaquettes
    target_nu: int
    target_sign: int
    half_re_tr_target: float
    kappa_e: float
    m_dot_np: float
    min_chi0: float
    worst_A_size: int
    worst_A_mask: int
    m_dot_u_at_worst: float
    single_chi0_max: float   # max over 5 singletons
    single_chi0_min: float   # min over 5 singletons (a partial bound on min_chi0)
    full_chi0: float         # chi_0 for A = all 5 neighbors


# =============================================================================
# Driver: process one link
# =============================================================================

def process_link(U: np.ndarray, x: Tuple[int, ...], mu: int, L: int,
                 beta: float, a: float, block: Block, block_avg_def: float,
                 config_idx: int, block_idx: int, subset_mode: str,
                 ) -> List[LCIRow]:
    """
    For link (x, mu), compute the LCI diagnostics for each of the 6 target
    plaquettes through e.  Returns up to 6 LCIRow records.
    """
    normals, ids = link_normals(U, x, mu, L)        # (6, 4),  list of (nu, sign)
    H_e = normals.sum(axis=0)                       # 4-vector
    h_norm = float(np.linalg.norm(H_e))
    if h_norm < 1e-14:
        return []
    m_e = H_e / h_norm
    kappa_e = beta * h_norm

    rows: List[LCIRow] = []
    for t_idx in range(6):
        n_p = normals[t_idx]
        neighbor_idx = [i for i in range(6) if i != t_idx]
        n_neighbors = [normals[i] for i in neighbor_idx]
        half_re_tr_target = float(np.dot(U[x + (mu,)], n_p))  # = (1/2) Re Tr(U_p_target)

        # Always compute singletons + full (cheap)
        single = []
        for j in range(5):
            u_s, _, _ = solve_cap_intersection_max(m_e, [n_neighbors[j]], a)
            if u_s is None:
                single.append(float("nan"))
            else:
                single.append(float(u_s @ n_p) - a)
        u_full, m_dot_u_full, _ = solve_cap_intersection_max(m_e, n_neighbors, a)
        full_chi0 = float(u_full @ n_p) - a if u_full is not None else float("nan")

        if subset_mode == "full":
            min_chi0, worst_size, worst_idx_local, m_dot_u_worst = \
                lci_margin_full(m_e, n_p, n_neighbors, a)
        elif subset_mode == "key":
            # Use singletons + full as the candidate set
            candidates: List[Tuple[float, int, Tuple[int, ...], float]] = []
            for j, ch in enumerate(single):
                if not math.isnan(ch):
                    candidates.append((ch, 1, (j,), float("nan")))
            if not math.isnan(full_chi0):
                candidates.append((full_chi0, 5, (0, 1, 2, 3, 4), m_dot_u_full))
            if not candidates:
                min_chi0, worst_size, worst_idx_local, m_dot_u_worst = (
                    float("nan"), -1, (), float("nan"))
            else:
                candidates.sort(key=lambda c: c[0])
                min_chi0, worst_size, worst_idx_local, m_dot_u_worst = candidates[0]
        else:
            raise ValueError(f"unknown subset_mode {subset_mode!r}")

        # Translate local neighbor index to original (0..5) target index for the mask.
        # We dropped t_idx from {0..5} to form the 5 neighbours; map back.
        worst_mask = 0
        for i_local in worst_idx_local:
            worst_mask |= 1 << neighbor_idx[i_local]

        nu, sign_nu = ids[t_idx]
        single_clean = [c for c in single if not math.isnan(c)]
        rows.append(LCIRow(
            config_idx=config_idx,
            block_idx=block_idx,
            block_avg_defect=block_avg_def,
            site0=x[0], site1=x[1], site2=x[2], site3=x[3],
            link_mu=mu,
            target_idx=t_idx,
            target_nu=nu,
            target_sign=sign_nu,
            half_re_tr_target=half_re_tr_target,
            kappa_e=kappa_e,
            m_dot_np=float(m_e @ n_p),
            min_chi0=float(min_chi0),
            worst_A_size=int(worst_size),
            worst_A_mask=int(worst_mask),
            m_dot_u_at_worst=float(m_dot_u_worst),
            single_chi0_max=float(max(single_clean)) if single_clean else float("nan"),
            single_chi0_min=float(min(single_clean)) if single_clean else float("nan"),
            full_chi0=float(full_chi0),
        ))
    return rows


# =============================================================================
# Driver: full diagnostic loop
# =============================================================================

def run_diagnostic(configs: np.ndarray, beta: float, t: float, eta: float,
                   block_side: int, core_margin: int, blocks_per_config: int,
                   subset_mode: str, out_dir: Path,
                   max_links_per_block: Optional[int],
                   rng: np.random.Generator) -> dict:
    """
    Run the LCI diagnostic on the given configurations.
    Writes lci_rows.csv, lci_summary.json, lci_log.txt to out_dir.
    Returns the summary dict.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    log_lines: List[str] = []
    def log(msg: str) -> None:
        print(msg)
        log_lines.append(msg)

    if configs.ndim != 7 or configs.shape[-1] != 4 or configs.shape[-2] != D:
        raise ValueError(
            f"configs must have shape (N, L, L, L, L, {D}, 4); got {configs.shape}"
        )
    N_cfg = configs.shape[0]
    L = configs.shape[1]
    a = 1.0 - (t - eta)

    log(f"[lci] N_cfg={N_cfg}  L={L}  beta={beta}")
    log(f"[lci] t={t}  eta={eta}  =>  a = 1 - (t - eta) = {a:.6f}")
    log(f"[lci] block_side={block_side}  core_margin={core_margin}  "
        f"core_side={block_side - 2*core_margin}")
    log(f"[lci] blocks_per_config={blocks_per_config}  subset_mode={subset_mode}")
    if max_links_per_block is not None:
        log(f"[lci] max_links_per_block={max_links_per_block} (sub-sampled)")

    csv_path = out_dir / "lci_rows.csv"
    csv_file = open(csv_path, "w", newline="")
    field_names = [f.name for f in fields(LCIRow)]
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()

    n_rows_written = 0
    t_start = time.time()
    all_min_chi0: List[float] = []
    all_full_chi0: List[float] = []
    all_kappa: List[float] = []
    all_block_def: List[float] = []
    worst_size_counter = {}
    block_summaries: List[dict] = []

    for c_idx in range(N_cfg):
        U = configs[c_idx]
        for b_idx in range(blocks_per_config):
            block = pick_block(L, block_side, core_margin, rng)
            bad = all_plaquettes_mean_defect(U, block.origin, block.side, L)

            link_iter = list(core_links(block, L))
            if max_links_per_block is not None and len(link_iter) > max_links_per_block:
                idxs = rng.choice(len(link_iter), size=max_links_per_block, replace=False)
                link_iter = [link_iter[i] for i in idxs]

            t_block = time.time()
            block_min_chi0: List[float] = []
            block_full_chi0: List[float] = []
            for x, mu in link_iter:
                rows = process_link(U, x, mu, L, beta, a, block, bad,
                                    c_idx, b_idx, subset_mode)
                for row in rows:
                    writer.writerow(asdict(row))
                    n_rows_written += 1
                    all_min_chi0.append(row.min_chi0)
                    all_full_chi0.append(row.full_chi0)
                    all_kappa.append(row.kappa_e)
                    block_min_chi0.append(row.min_chi0)
                    block_full_chi0.append(row.full_chi0)
                    worst_size_counter[row.worst_A_size] = \
                        worst_size_counter.get(row.worst_A_size, 0) + 1
            all_block_def.append(bad)
            block_summaries.append({
                "config_idx": c_idx,
                "block_idx": b_idx,
                "origin": list(block.origin),
                "n_links": len(link_iter),
                "n_rows": len(block_min_chi0),
                "block_avg_defect": bad,
                "min_chi0_median": float(np.median(block_min_chi0)) if block_min_chi0 else float("nan"),
                "min_chi0_min": float(np.min(block_min_chi0)) if block_min_chi0 else float("nan"),
                "frac_lci_good": float(np.mean([c > 0 for c in block_min_chi0])) if block_min_chi0 else float("nan"),
            })
            log(f"[lci] cfg {c_idx+1}/{N_cfg} block {b_idx+1}/{blocks_per_config}  "
                f"links={len(link_iter)}  rows={len(block_min_chi0)}  "
                f"defect={bad:.4f}  "
                f"frac_chi0>0={block_summaries[-1]['frac_lci_good']:.3f}  "
                f"min(min_chi0)={block_summaries[-1]['min_chi0_min']:.4f}  "
                f"({time.time()-t_block:.1f}s)")

    csv_file.close()
    elapsed = time.time() - t_start
    log(f"[lci] wrote {n_rows_written} rows to {csv_path} in {elapsed:.1f}s")

    # ----- Aggregate summary -----
    summary = _compute_summary(all_min_chi0, all_full_chi0, all_kappa,
                                all_block_def, worst_size_counter,
                                block_summaries, n_rows_written, a, beta, t, eta,
                                block_side, core_margin, subset_mode)

    with open(out_dir / "lci_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    log(f"[lci] wrote summary to {out_dir / 'lci_summary.json'}")

    log("\n[lci] ====== SUMMARY ======")
    for k, v in summary["overall"].items():
        log(f"  {k:30s} {v}")

    with open(out_dir / "lci_log.txt", "w") as f:
        f.write("\n".join(log_lines))

    return summary


def _compute_summary(min_chi0: List[float], full_chi0: List[float],
                     kappa: List[float], block_def: List[float],
                     worst_size: dict, block_summaries: List[dict],
                     n_rows: int, a: float, beta: float, t: float, eta: float,
                     block_side: int, core_margin: int, subset_mode: str) -> dict:
    arr = np.array(min_chi0, dtype=float)
    finite = arr[np.isfinite(arr)]
    full_arr = np.array(full_chi0, dtype=float)
    full_finite = full_arr[np.isfinite(full_arr)]
    kappa_arr = np.array(kappa, dtype=float)
    kappa_finite = kappa_arr[np.isfinite(kappa_arr)]

    def quantiles(x, qs):
        if x.size == 0:
            return {f"q{int(q*100):02d}": float("nan") for q in qs}
        return {f"q{int(q*100):02d}": float(np.quantile(x, q)) for q in qs}

    overall = {
        "n_rows": n_rows,
        "n_finite_min_chi0": int(finite.size),
        "a_threshold": a,
        "beta": beta,
        "t": t,
        "eta": eta,
        "block_side": block_side,
        "core_margin": core_margin,
        "subset_mode": subset_mode,
    }
    if finite.size > 0:
        overall.update({
            "frac_lci_good_chi0>0":       float(np.mean(finite > 0.0)),
            "frac_lci_good_chi0>0.01":    float(np.mean(finite > 0.01)),
            "frac_lci_good_chi0>0.05":    float(np.mean(finite > 0.05)),
            "frac_lci_good_chi0>0.10":    float(np.mean(finite > 0.10)),
            "min_chi0_min":    float(finite.min()),
            "min_chi0_max":    float(finite.max()),
            "min_chi0_mean":   float(finite.mean()),
            "min_chi0_median": float(np.median(finite)),
        })
        overall.update({"min_chi0_" + k: v
                        for k, v in quantiles(finite, [0.01, 0.05, 0.25, 0.75, 0.95]).items()})

    if full_finite.size > 0:
        overall.update({
            "full_chi0_min":    float(full_finite.min()),
            "full_chi0_median": float(np.median(full_finite)),
            "full_chi0_mean":   float(full_finite.mean()),
            "frac_full_chi0>0": float(np.mean(full_finite > 0.0)),
        })

    if kappa_finite.size > 0:
        overall["kappa_e_median"] = float(np.median(kappa_finite))
        overall["kappa_e_q05"]    = float(np.quantile(kappa_finite, 0.05))
        overall["kappa_e_q95"]    = float(np.quantile(kappa_finite, 0.95))

    if block_def:
        bd = np.array(block_def)
        overall["block_avg_defect_median"] = float(np.median(bd))
        overall["block_avg_defect_q05"]    = float(np.quantile(bd, 0.05))
        overall["block_avg_defect_q95"]    = float(np.quantile(bd, 0.95))

    return {
        "overall": overall,
        "worst_subset_size_distribution": {str(k): v for k, v in sorted(worst_size.items())},
        "blocks": block_summaries,
    }


# =============================================================================
# CLI
# =============================================================================

def _build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="LCI typicality diagnostic for SU(2) Wilson",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    src = p.add_mutually_exclusive_group(required=False)
    src.add_argument("--configs", type=str, default=None,
                     help="Path to .npy file of shape (N, L, L, L, L, 4, 4) of "
                          "thermalized SU(2) configs.")
    src.add_argument("--test", action="store_true",
                     help="Self-contained: thermalize a tiny L=4 lattice and run.")
    p.add_argument("--beta", type=float, default=3.5)
    p.add_argument("--t", type=float, default=1.0104245908659366,
                   help="High-plaquette threshold on 1 - (1/2) Re Tr(U_p).")
    p.add_argument("--eta", type=float, default=0.005,
                   help="Upper-envelope ramp width.")
    p.add_argument("--block-side", type=int, default=10)
    p.add_argument("--core-margin", type=int, default=3)
    p.add_argument("--blocks-per-config", type=int, default=8)
    p.add_argument("--subset-mode", type=str, choices=["full", "key"],
                   default="key",
                   help="full = enumerate all 31 non-empty subsets (slow, exact).  "
                        "key  = singletons + full 5-subset only (fast, lower bound on margin).")
    p.add_argument("--max-links-per-block", type=int, default=None,
                   help="If set, subsample core links per block (for fast scans).")
    p.add_argument("--out-dir", type=str, default="results/lci")
    p.add_argument("--seed", type=int, default=20260526)
    p.add_argument("--test-L", type=int, default=4,
                   help="Lattice size for --test mode (small for speed).")
    p.add_argument("--test-therm", type=int, default=80,
                   help="Thermalization sweeps for --test mode.")
    p.add_argument("--test-beta", type=float, default=2.0,
                   help="beta for --test mode (smaller for faster decorrelation).")
    p.add_argument("--test-n-cfg", type=int, default=2,
                   help="Number of configs to generate for --test mode.")
    p.add_argument("--test-decorr", type=int, default=8,
                   help="Sweeps between saved configs in --test mode.")
    return p


def _running_in_jupyter() -> bool:
    """True when imported inside an IPython/Jupyter kernel."""
    try:
        # IPython/Jupyter sets __IPYTHON__ in the builtins; getipython is the supported probe.
        from IPython import get_ipython  # type: ignore
        return get_ipython() is not None
    except Exception:
        return False


def _strip_jupyter_argv(argv: List[str]) -> List[str]:
    """Drop the '-f /path/to/kernel-*.json' pair that Jupyter injects."""
    out: List[str] = []
    skip_next = False
    for a in argv:
        if skip_next:
            skip_next = False
            continue
        if a == "-f":
            skip_next = True
            continue
        if a.endswith(".json") and "kernel-" in a:
            continue
        out.append(a)
    return out


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_argparser()
    if argv is None:
        argv = sys.argv[1:]
    # Tolerate Jupyter/Colab kernel-launcher args.
    if _running_in_jupyter() or any(a == "-f" or (a.endswith(".json") and "kernel-" in a) for a in argv):
        argv = _strip_jupyter_argv(argv)
    args, unknown = parser.parse_known_args(argv)
    if unknown:
        print(f"warning: ignoring unknown args: {unknown}", file=sys.stderr)

    if not args.configs and not args.test:
        print("ERROR: either --configs PATH or --test must be specified", file=sys.stderr)
        print("       (in a notebook, call run(test=True, ...) or run(configs=...) instead)",
              file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)

    if args.test:
        L = args.test_L
        beta = args.test_beta
        print(f"[main] --test mode: L={L} beta={beta} therm={args.test_therm} "
              f"n_cfg={args.test_n_cfg}")
        U = thermalize(L, beta, args.test_therm, rng, log_every=max(1, args.test_therm // 8))
        configs = np.empty((args.test_n_cfg, L, L, L, L, D, 4))
        configs[0] = U
        for i in range(1, args.test_n_cfg):
            for _ in range(args.test_decorr):
                heatbath_sweep(U, beta, L, rng)
            configs[i] = U.copy()
        # Use a smaller block on the tiny lattice
        block_side = min(args.block_side, L)
        core_margin = min(args.core_margin, max(0, (block_side - 2) // 2))
        print(f"[main] using block_side={block_side} core_margin={core_margin} for --test")
        run_diagnostic(configs, beta=beta, t=args.t, eta=args.eta,
                       block_side=block_side, core_margin=core_margin,
                       blocks_per_config=min(args.blocks_per_config, 4),
                       subset_mode=args.subset_mode, out_dir=out_dir,
                       max_links_per_block=args.max_links_per_block, rng=rng)
        return 0

    cfg_path = Path(args.configs)
    print(f"[main] loading configs from {cfg_path} ...")
    configs = np.load(cfg_path)
    print(f"[main] loaded shape {configs.shape}")
    run_diagnostic(configs, beta=args.beta, t=args.t, eta=args.eta,
                   block_side=args.block_side, core_margin=args.core_margin,
                   blocks_per_config=args.blocks_per_config,
                   subset_mode=args.subset_mode, out_dir=out_dir,
                   max_links_per_block=args.max_links_per_block, rng=rng)
    return 0


# -----------------------------------------------------------------------------
# Programmatic entry point (notebook-friendly)
# -----------------------------------------------------------------------------

def run(*,
        configs: "np.ndarray | str | Path | None" = None,
        test: bool = False,
        beta: float = 3.5,
        t: float = 1.0104245908659366,
        eta: float = 0.005,
        block_side: int = 10,
        core_margin: int = 3,
        blocks_per_config: int = 8,
        subset_mode: str = "key",
        max_links_per_block: Optional[int] = None,
        out_dir: "str | Path" = "results/lci",
        seed: int = 20260526,
        # --test-only knobs:
        test_L: int = 4,
        test_therm: int = 80,
        test_beta: float = 2.0,
        test_n_cfg: int = 2,
        test_decorr: int = 8) -> dict:
    """
    Programmatic entry point. Use from a Jupyter/Colab cell:

        import ENGINE_FLUX_lci_typicality_diagnostic as lci

        # Self-contained test (no external configs needed)
        summary = lci.run(test=True, test_L=4, test_therm=20,
                          block_side=4, core_margin=1,
                          blocks_per_config=2, subset_mode="key",
                          out_dir="/tmp/lci_test")

        # Production: pass a numpy array directly, or a path to a .npy file
        summary = lci.run(configs=cfg_array,
                          beta=3.5, block_side=10, core_margin=3,
                          blocks_per_config=64, subset_mode="key",
                          out_dir="results/lci_stageB_key")

    Returns the same summary dict that is also written to
    `<out_dir>/lci_summary.json`.
    """
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)

    if test:
        L = test_L
        _beta = test_beta
        print(f"[run ] test mode: L={L} beta={_beta} therm={test_therm} n_cfg={test_n_cfg}")
        U = thermalize(L, _beta, test_therm, rng, log_every=max(1, test_therm // 8))
        cfgs = np.empty((test_n_cfg, L, L, L, L, D, 4))
        cfgs[0] = U
        for i in range(1, test_n_cfg):
            for _ in range(test_decorr):
                heatbath_sweep(U, _beta, L, rng)
            cfgs[i] = U.copy()
        bs = min(block_side, L)
        cm = min(core_margin, max(0, (bs - 2) // 2))
        print(f"[run ] using block_side={bs} core_margin={cm} for test")
        return run_diagnostic(cfgs, beta=_beta, t=t, eta=eta,
                              block_side=bs, core_margin=cm,
                              blocks_per_config=min(blocks_per_config, 4),
                              subset_mode=subset_mode, out_dir=out_path,
                              max_links_per_block=max_links_per_block, rng=rng)

    if configs is None:
        raise ValueError("run(): pass configs=... (np.ndarray or path) or test=True")
    if isinstance(configs, (str, Path)):
        cfg_path = Path(configs)
        print(f"[run ] loading configs from {cfg_path} ...")
        cfgs = np.load(cfg_path)
    else:
        cfgs = np.asarray(configs)
    print(f"[run ] configs shape {cfgs.shape}")
    return run_diagnostic(cfgs, beta=beta, t=t, eta=eta,
                          block_side=block_side, core_margin=core_margin,
                          blocks_per_config=blocks_per_config,
                          subset_mode=subset_mode, out_dir=out_path,
                          max_links_per_block=max_links_per_block, rng=rng)


if __name__ == "__main__":
    sys.exit(main())
