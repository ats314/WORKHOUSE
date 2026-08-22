#!/usr/bin/env python3
# Sanity-check: exponential decay of the inverse massive Maxwell operator on a 2D periodic lattice.
#
# This is NOT part of the manuscript's proofs; it is a numerical illustration of the deterministic
# Green-kernel decay statements (Combes–Thomas / Davies bounds) for operators of the form
#   M = m^2 I + alpha d1^* d1
# acting on link 1-cochains.

import math
from collections import defaultdict, deque
import numpy as np
import matplotlib.pyplot as plt


def build_d1(L: int):
    'Exterior derivative d1: C^1 -> C^2 for a 2D periodic LxL lattice (Z_L^2).'
    d = 2
    edge_index = {}
    idx = 0
    for x in range(L):
        for y in range(L):
            for mu in range(d):
                edge_index[(x, y, mu)] = idx
                idx += 1
    nE = idx

    plaquettes = [(x, y) for x in range(L) for y in range(L)]
    nP = len(plaquettes)

    d1 = np.zeros((nP, nE), dtype=int)

    for p_idx, (x, y) in enumerate(plaquettes):
        # Oriented boundary of plaquette with basepoint (x,y), directions (0,1)
        d1[p_idx, edge_index[(x, y, 0)]] = 1
        d1[p_idx, edge_index[((x + 1) % L, y, 1)]] = 1
        d1[p_idx, edge_index[(x, (y + 1) % L, 0)]] = -1
        d1[p_idx, edge_index[(x, y, 1)]] = -1

    return d1, edge_index


def inverse_decay_data(L: int, m2: float = 1.0, alpha: float = 1.0):
    d1, edge_index = build_d1(L)
    nP, nE = d1.shape

    K = (d1.T @ d1).astype(float)  # d1^* d1 on edges (with standard inner product)
    M = m2 * np.eye(nE) + alpha * K
    G = np.linalg.inv(M)

    # Choose a reference edge e0=(0,0,0)
    i0 = edge_index[(0, 0, 0)]

    # Build adjacency graph from nonzero off-diagonal entries of K (finite-range couplings)
    adj = [set() for _ in range(nE)]
    for i in range(nE):
        nz = np.nonzero(K[i])[0]
        for j in nz:
            if j != i:
                adj[i].add(j)

    # Graph distances dist_E from i0
    dist = [-1] * nE
    dist[i0] = 0
    q = deque([i0])
    while q:
        i = q.popleft()
        for j in adj[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                q.append(j)

    max_by = defaultdict(float)
    mean_by = defaultdict(float)
    count_by = defaultdict(int)

    for j in range(nE):
        r = dist[j]
        v = abs(G[i0, j])
        if v > max_by[r]:
            max_by[r] = v
        mean_by[r] += v
        count_by[r] += 1

    for r in list(mean_by.keys()):
        mean_by[r] /= count_by[r]

    # A crude Combes–Thomas style lower bound for the decay exponent
    off_row_sums = np.sum(np.abs(alpha * K), axis=1) - np.abs(np.diag(alpha * K))
    nu = float(np.max(off_row_sums))
    eta_bound = math.log(1.0 + m2 / nu)

    # Fit an empirical exponential rate from dist=1..min(10,maxdist)
    maxdist = max(max_by.keys())
    fit_max = min(10, maxdist)
    xs = np.array([r for r in range(1, fit_max + 1)], dtype=float)
    ys = np.array([math.log(max_by[int(r)]) for r in xs], dtype=float)
    slope, intercept = np.polyfit(xs, ys, 1)

    return max_by, mean_by, count_by, eta_bound, nu, slope, intercept


def main():
    L = 12
    m2 = 1.0
    alpha = 1.0

    max_by, mean_by, count_by, eta_bound, nu, slope, intercept = inverse_decay_data(L, m2=m2, alpha=alpha)

    print(f"L={L}, m^2={m2}, alpha={alpha}")
    print(f"nu (max off-diagonal row sum of alpha*d1^*d1) = {nu:.6f}")
    print(f"Combes–Thomas-style exponent lower bound: eta >= log(1+m/nu) = {eta_bound:.6f}")
    print(f"Empirical fit (log max|G| ~ a + b*dist) over dist=1..10: b = {slope:.6f}")

    print("\n dist | max_abs | mean_abs | count")
    print("----------------------------------")
    for r in sorted(max_by.keys()):
        print(f"{r:5d} | {max_by[r]:.3e} | {mean_by[r]:.3e} | {count_by[r]:5d}")

    # Plot
    dists = np.array(sorted(max_by.keys()))
    vals = np.array([max_by[int(r)] for r in dists])
    plt.figure()
    plt.plot(dists, np.log(vals), marker="o")
    plt.xlabel("graph distance dist_E(e0,e)")
    plt.ylabel("log max |(M^{-1})_{e0,e}|")
    plt.title(f"Exponential decay of inverse massive Maxwell operator (2D, L={L})")
    plt.savefig("maxwell_inverse_decay_L12_d2.png", dpi=200, bbox_inches="tight")


if __name__ == "__main__":
    main()
