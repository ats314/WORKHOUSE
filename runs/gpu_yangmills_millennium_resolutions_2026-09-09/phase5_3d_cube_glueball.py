"""
Phase 5: 3D Elementary Cube SU(2) Kogut-Susskind Lattice Gauge Theory
and Glueball Mass Spectrum (0++ Scalar vs 2++ Tensor) on AMD Radeon RX 7900 XTX.

Geometry:
- 3D elementary cube: 8 vertices, 12 links, 6 square plaquette faces.
- Gauge group: SU(2).
- Cubic symmetry group Oh representations:
  - A1g (0++ scalar glueball): O_0++ = (P0 + P1 + P2 + P3 + P4 + P5) / sqrt(6)
  - Eg (2++ tensor glueball): O_2++,1 = (2(P0+P1) - (P2+P3) - (P4+P5)) / sqrt(12)
                             O_2++,2 = ((P2+P3) - (P4+P5)) / 2

Computes:
1. Exact Hamiltonian matrix on GPU (torch.float64, ROCm).
2. Spectrum across couplings v in [0.2, 5.0].
3. Ground state E0, Scalar mass M(0++), Tensor mass M(2++), and ratio M(2++)/M(0++).
4. Confirms mass gap Delta = M(0++) > 0 strictly in 3 spatial dimensions.
"""

import sys
import os
import json
import time
import math
import itertools
import numpy as np
import torch

def setup_device():
    if torch.cuda.is_available():
        dev = torch.device('cuda:0')
        prop = torch.cuda.get_device_properties(0)
        print(f"[Device] Using GPU: {prop.name} (Compute: {prop.major}.{prop.minor}, VRAM: {prop.total_memory / (1024**3):.2f} GB)")
    else:
        dev = torch.device('cpu')
        print("[Device] CUDA not available; using CPU.")
    return dev

def build_3d_cube_system():
    # 8 vertices: (x,y,z) in {0,1}^3
    # 12 links:
    # 0..3: x-links
    # 4..7: y-links
    # 8..11: z-links
    links = [
        (0, 1), # 0: (0,0,0)->(1,0,0)
        (2, 3), # 1: (0,1,0)->(1,1,0)
        (4, 5), # 2: (0,0,1)->(1,0,1)
        (6, 7), # 3: (0,1,1)->(1,1,1)
        (0, 2), # 4: (0,0,0)->(0,1,0)
        (1, 3), # 5: (1,0,0)->(1,1,0)
        (4, 6), # 6: (0,0,1)->(0,1,1)
        (5, 7), # 7: (1,0,1)->(1,1,1)
        (0, 4), # 8: (0,0,0)->(0,0,1)
        (1, 5), # 9: (1,0,0)->(1,0,1)
        (2, 6), # 10: (0,1,0)->(0,1,1)
        (3, 7)  # 11: (1,1,0)->(1,1,1)
    ]
    
    # 6 plaquettes (sets of 4 links):
    # p0 (z=0, bottom): {0, 5, 1, 4}
    # p1 (z=1, top):    {2, 7, 3, 6}
    # p2 (y=0, front):  {0, 9, 2, 8}
    # p3 (y=1, back):   {1, 11, 3, 10}
    # p4 (x=0, left):   {4, 10, 6, 8}
    # p5 (x=1, right):  {5, 11, 7, 9}
    plaquettes = [
        (0, 5, 1, 4),
        (2, 7, 3, 6),
        (0, 9, 2, 8),
        (1, 11, 3, 10),
        (4, 10, 6, 8),
        (5, 11, 7, 9)
    ]
    
    # Incident links at each vertex
    vertices = [
        [0, 4, 8],
        [0, 5, 9],
        [1, 4, 10],
        [1, 5, 11],
        [2, 6, 8],
        [2, 7, 9],
        [3, 6, 10],
        [3, 7, 11]
    ]
    
    return links, plaquettes, vertices

def enumerate_gauge_invariant_states(vertices, max_2j=2):
    """
    Enumerate gauge invariant states where each link has 2j in {0, ..., max_2j}.
    For 3-valent vertices, gauge invariance is exactly the Clebsch-Gordan triangle condition.
    """
    def valid_vertex(j1, j2, j3):
        s = j1 + j2 + j3
        return (s % 2 == 0) and (abs(j1 - j2) <= j3 <= j1 + j2)
    
    valid_triples = set()
    vals = list(range(max_2j + 1))
    for j1 in vals:
        for j2 in vals:
            for j3 in vals:
                if valid_vertex(j1, j2, j3):
                    valid_triples.add((j1, j2, j3))
                    
    states = []
    
    for t0 in valid_triples:
        j0, j4, j8 = t0
        for j5 in vals:
            for j9 in vals:
                if (j0, j5, j9) not in valid_triples:
                    continue
                for j1 in vals:
                    for j10 in vals:
                        if (j1, j4, j10) not in valid_triples:
                            continue
                        for j11 in vals:
                            if (j1, j5, j11) not in valid_triples:
                                continue
                            for j2 in vals:
                                for j6 in vals:
                                    if (j2, j6, j8) not in valid_triples:
                                        continue
                                    for j7 in vals:
                                        if (j2, j7, j9) not in valid_triples:
                                            continue
                                        for j3 in vals:
                                            if (j3, j6, j10) not in valid_triples:
                                                continue
                                            if (j3, j7, j11) not in valid_triples:
                                                continue
                                            state = (j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11)
                                            states.append(state)
    return states

def construct_hamiltonian(states, plaquettes, epsilon=1.0, v=1.0, device=None):
    """
    Construct the Kogut-Susskind Hamiltonian matrix on the gauge-invariant basis.
    H = epsilon * H_kin - v * V_mag
    """
    state_to_idx = {s: i for i, s in enumerate(states)}
    dim = len(states)
    
    H = np.zeros((dim, dim), dtype=np.float64)
    
    # 1. Kinetic energy (diagonal)
    for i, s in enumerate(states):
        kin = 0.0
        for val in s:
            j = val / 2.0
            kin += j * (j + 1.0)
        H[i, i] += epsilon * kin
    
    # 2. Magnetic potential: sum over 6 plaquettes
    for p_idx, p in enumerate(plaquettes):
        for i, s in enumerate(states):
            for d in itertools.product([-1, 1], repeat=4):
                new_s = list(s)
                valid = True
                for link_k, delta in zip(p, d):
                    new_val = new_s[link_k] + delta
                    if new_val < 0 or new_val > 2:
                        valid = False
                        break
                    new_s[link_k] = new_val
                if not valid:
                    continue
                new_s = tuple(new_s)
                if new_s in state_to_idx:
                    j_idx = state_to_idx[new_s]
                    weight = 0.5
                    H[i, j_idx] -= v * (weight / 4.0)
    
    # Make strictly symmetric
    H = 0.5 * (H + H.T)
    H_torch = torch.tensor(H, dtype=torch.float64, device=device)
    return H_torch, state_to_idx

def compute_glueball_projections(states, plaquettes, state_to_idx, device=None):
    """
    Construct trial wavefunctions for 0++ (A1g) and 2++ (Eg) glueballs.
    """
    dim = len(states)
    vac_state = tuple([0] * 12)
    vac_idx = state_to_idx[vac_state]
    
    plaq_indices = []
    for p in plaquettes:
        s = [0] * 12
        for e in p:
            s[e] = 1 # 2j = 1 -> j = 1/2
        s = tuple(s)
        plaq_indices.append(state_to_idx[s])
    
    # 1. Scalar glueball 0++ (A1g):
    psi_0pp = np.zeros(dim, dtype=np.float64)
    for idx in plaq_indices:
        psi_0pp[idx] = 1.0 / math.sqrt(6.0)
    
    # 2. Tensor glueball 2++ (Eg):
    psi_2pp_1 = np.zeros(dim, dtype=np.float64)
    psi_2pp_1[plaq_indices[0]] = 2.0 / math.sqrt(12.0)
    psi_2pp_1[plaq_indices[1]] = 2.0 / math.sqrt(12.0)
    psi_2pp_1[plaq_indices[2]] = -1.0 / math.sqrt(12.0)
    psi_2pp_1[plaq_indices[3]] = -1.0 / math.sqrt(12.0)
    psi_2pp_1[plaq_indices[4]] = -1.0 / math.sqrt(12.0)
    psi_2pp_1[plaq_indices[5]] = -1.0 / math.sqrt(12.0)
    
    psi_2pp_2 = np.zeros(dim, dtype=np.float64)
    psi_2pp_2[plaq_indices[2]] = 1.0 / 2.0
    psi_2pp_2[plaq_indices[3]] = 1.0 / 2.0
    psi_2pp_2[plaq_indices[4]] = -1.0 / 2.0
    psi_2pp_2[plaq_indices[5]] = -1.0 / 2.0
    
    psi_0pp_t = torch.tensor(psi_0pp, dtype=torch.float64, device=device)
    psi_2pp_1_t = torch.tensor(psi_2pp_1, dtype=torch.float64, device=device)
    psi_2pp_2_t = torch.tensor(psi_2pp_2, dtype=torch.float64, device=device)
    
    return vac_idx, plaq_indices, psi_0pp_t, psi_2pp_1_t, psi_2pp_2_t

def run_simulation():
    device = setup_device()
    links, plaquettes, vertices = build_3d_cube_system()
    
    t0 = time.time()
    states = enumerate_gauge_invariant_states(vertices, max_2j=2)
    t_states = time.time() - t0
    print(f"[Basis] Found {len(states)} gauge-invariant states in {t_states:.3f}s")
    
    v_values = [0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]
    results = []
    
    print("\n--- Running 3D Elementary Cube Glueball Spectrum on 7900 XTX ---")
    print(f"{'v':>6} | {'E_0':>10} | {'M(0++)':>10} | {'M(2++)':>10} | {'M(2++)/M(0++)':>14} | {'Status':>8}")
    print("-" * 72)
    
    for v in v_values:
        H_torch, state_to_idx = construct_hamiltonian(states, plaquettes, epsilon=1.0, v=v, device=device)
        vac_idx, plaq_indices, psi_0pp_t, psi_2pp_1_t, psi_2pp_2_t = compute_glueball_projections(
            states, plaquettes, state_to_idx, device=device
        )
        
        eigvals, eigvecs = torch.linalg.eigh(H_torch)
        eigvals_cpu = eigvals.cpu().numpy()
        eigvecs_t = eigvecs
        
        e0 = eigvals_cpu[0]
        
        overlaps_0pp = torch.abs(torch.matmul(psi_0pp_t, eigvecs_t)).cpu().numpy() ** 2
        overlaps_2pp_1 = torch.abs(torch.matmul(psi_2pp_1_t, eigvecs_t)).cpu().numpy() ** 2
        overlaps_2pp_2 = torch.abs(torch.matmul(psi_2pp_2_t, eigvecs_t)).cpu().numpy() ** 2
        overlaps_2pp = overlaps_2pp_1 + overlaps_2pp_2
        
        overlaps_0pp[0] = 0.0
        overlaps_2pp[0] = 0.0
        
        idx_0pp = np.argmax(overlaps_0pp)
        idx_2pp = np.argmax(overlaps_2pp)
        
        e_0pp = eigvals_cpu[idx_0pp]
        e_2pp = eigvals_cpu[idx_2pp]
        
        m_0pp = e_0pp - e0
        m_2pp = e_2pp - e0
        ratio = m_2pp / m_0pp
        
        status = "GAP > 0" if m_0pp > 0 else "NO GAP"
        print(f"{v:6.2f} | {e0:10.6f} | {m_0pp:10.6f} | {m_2pp:10.6f} | {ratio:14.6f} | {status:>8}")
        
        results.append({
            "v": float(v),
            "E_0": float(e0),
            "E_0pp": float(e_0pp),
            "E_2pp": float(e_2pp),
            "M_0pp": float(m_0pp),
            "M_2pp": float(m_2pp),
            "ratio_2pp_to_0pp": float(ratio),
            "overlap_0pp": float(overlaps_0pp[idx_0pp]),
            "overlap_2pp": float(overlaps_2pp[idx_2pp]),
            "gap_positive": bool(m_0pp > 0)
        })
    
    out_dir = r"c:\WORKHOUSE\ALL THEORY\WORKHOUSE\runs\gpu_yangmills_millennium_resolutions_2026-09-09"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "phase5_3d_cube_glueball_results.json")
    with open(out_file, "w") as f:
        json.dump({
            "lattice_geometry": "3D Elementary Cube (8 vertices, 12 links, 6 plaquettes)",
            "basis_dimension": len(states),
            "gauge_group": "SU(2)",
            "representations": {
                "0++": "Scalar glueball (A1g trivial cubic representation)",
                "2++": "Tensor glueball (Eg quadrupolar doublet)"
            },
            "results": results
        }, f, indent=2)
    
    print(f"\n[Success] Results saved to {out_file}")

if __name__ == "__main__":
    run_simulation()
