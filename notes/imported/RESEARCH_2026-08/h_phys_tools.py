#!/usr/bin/env python3
"""
Tools to define and compute the "physical" Hessian H_phys used in the SAFE scans.

Core idea (as in the draft):
    H_phys(x) := Π_phys(x)^T [∇^2 V_tot(x)] Π_phys(x)

where Π_phys is an orthonormal basis matrix for the horizontal (gauge-orthogonal)
subspace H_U inside T_U(G^E), optionally followed by a Schur-complement elimination
(marginalization) if you reduce a multi-link cluster to an effective single-link
potential.

This file is intentionally modular:
- You supply the cluster graph (vertices + oriented edges).
- You supply V_tot(x) (scalar potential) and/or H_total(x) (Hessian).
- We supply Π_phys construction and the projection / Schur complement steps.

Conventions:
- G = SU(3)
- Lie algebra basis T_a is anti-Hermitian with <A,B> = -2 Re Tr(A B) (orthonormal).
- Link coordinates are x ∈ R^(8*|E|), flattened as [edge0(8), edge1(8), ...].
- Edge orientation is (tail -> head).

This matches the vertical tangent formula in the draft:
    (X^#(U))_{x,μ} = X_x - Ad_{U_{x,μ}}(X_{x+μ})
so the discrete covariant "gradient" D0(U) is:
    (D0(U) φ)_e = φ_tail(e) - Ad_{U_e}(φ_head(e))

Then horizontals are:
    H_U = ker(D0(U)^T)  (for the product metric / orthonormal basis)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

import torch

DTYPE_R = torch.float64
DTYPE_C = torch.complex128


# ----------------------------
# su(3) basis and inner product
# ----------------------------

def gell_mann() -> List[torch.Tensor]:
    """Standard Gell-Mann matrices λ_a (Hermitian, Tr(λ_a λ_b)=2 δ_ab)."""
    lam: List[torch.Tensor] = []
    lam.append(torch.tensor([[0,1,0],[1,0,0],[0,0,0]], dtype=DTYPE_C))                      # λ1
    lam.append(torch.tensor([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=DTYPE_C))                   # λ2
    lam.append(torch.tensor([[1,0,0],[0,-1,0],[0,0,0]], dtype=DTYPE_C))                     # λ3
    lam.append(torch.tensor([[0,0,1],[0,0,0],[1,0,0]], dtype=DTYPE_C))                      # λ4
    lam.append(torch.tensor([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=DTYPE_C))                   # λ5
    lam.append(torch.tensor([[0,0,0],[0,0,1],[0,1,0]], dtype=DTYPE_C))                      # λ6
    lam.append(torch.tensor([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=DTYPE_C))                   # λ7
    lam.append(torch.tensor([[1/3**0.5,0,0],[0,1/3**0.5,0],[0,0,-2/3**0.5]], dtype=DTYPE_C))# λ8
    return lam


def su3_basis() -> List[torch.Tensor]:
    """
    Anti-Hermitian orthonormal basis T_a = (i/2) λ_a w.r.t <A,B> = -2 Re Tr(A B).
    """
    lam = gell_mann()
    return [0.5j * L for L in lam]


def inner(A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
    """<A,B> := -2 Re Tr(A B)."""
    return (-2.0 * torch.real(torch.trace(A @ B)))


def su3_from_coords(x8: torch.Tensor, T: Sequence[torch.Tensor]) -> torch.Tensor:
    """X = sum_a x_a T_a."""
    assert x8.shape == (8,)
    X = torch.zeros((3,3), dtype=DTYPE_C, device=x8.device)
    for a in range(8):
        X = X + x8[a].to(DTYPE_R) * T[a]
    return X


def su3_exp_from_coords(x8: torch.Tensor, T: Sequence[torch.Tensor]) -> torch.Tensor:
    """U = exp(X) with X in su(3)."""
    X = su3_from_coords(x8, T)
    return torch.matrix_exp(X)


def adjoint_matrix(U: torch.Tensor, T: Sequence[torch.Tensor]) -> torch.Tensor:
    """
    Return Ad_U in the chosen orthonormal basis:
        (Ad_U)_{a b} = <T_a, U T_b U^{-1}>.
    Shape (8,8), real.
    """
    Uinv = torch.linalg.inv(U)
    A = torch.zeros((8,8), dtype=DTYPE_R, device=U.device)
    for b in range(8):
        Tb = T[b]
        Y = U @ Tb @ Uinv
        for a in range(8):
            A[a,b] = inner(T[a], Y).to(DTYPE_R)
    return A


# ----------------------------
# Cluster geometry
# ----------------------------

@dataclass(frozen=True)
class OrientedEdge:
    """One oriented edge (tail -> head) with integer vertex labels."""
    tail: int
    head: int


@dataclass(frozen=True)
class Cluster:
    """A cluster graph for local scans / block computations."""
    n_vertices: int
    edges: Tuple[OrientedEdge, ...]

    @property
    def n_edges(self) -> int:
        return len(self.edges)

    @property
    def dim_links(self) -> int:
        return 8 * self.n_edges

    @property
    def dim_gauge(self) -> int:
        return 8 * self.n_vertices


def split_link_coords(x: torch.Tensor, cluster: Cluster) -> List[torch.Tensor]:
    """Split flattened link coordinate vector into a list of 8-vectors (one per edge)."""
    assert x.ndim == 1 and x.shape[0] == cluster.dim_links
    return [x[8*i:8*(i+1)] for i in range(cluster.n_edges)]


def cluster_U_from_x(x: torch.Tensor, cluster: Cluster, T: Sequence[torch.Tensor]) -> List[torch.Tensor]:
    """Compute U_e = exp(X_e) for every edge e in the cluster."""
    xs = split_link_coords(x, cluster)
    return [su3_exp_from_coords(xe, T) for xe in xs]


# ----------------------------
# Gauge vertical operator and Π_phys
# ----------------------------

def vertical_operator_D0(
    U_edges: Sequence[torch.Tensor],
    cluster: Cluster,
    T: Sequence[torch.Tensor],
) -> torch.Tensor:
    """
    Build D0(U): su(3)^{V} -> su(3)^{E} as a real matrix of shape (8|E|, 8|V|).

    For edge e = (tail -> head), block row is:
        [ ... I_8 at tail ...  -Ad_{U_e} at head ... ].
    """
    assert len(U_edges) == cluster.n_edges
    D0 = torch.zeros((cluster.dim_links, cluster.dim_gauge), dtype=DTYPE_R, device=U_edges[0].device)

    I8 = torch.eye(8, dtype=DTYPE_R, device=U_edges[0].device)

    for i, e in enumerate(cluster.edges):
        Ad = adjoint_matrix(U_edges[i], T)  # (8,8)
        r0, r1 = 8*i, 8*(i+1)
        # tail block
        c_tail0, c_tail1 = 8*e.tail, 8*(e.tail+1)
        D0[r0:r1, c_tail0:c_tail1] = I8
        # head block
        c_head0, c_head1 = 8*e.head, 8*(e.head+1)
        D0[r0:r1, c_head0:c_head1] = -Ad
    return D0


def nullspace_basis(M: torch.Tensor, tol: float = 1e-12) -> torch.Tensor:
    """
    Orthonormal basis for ker(M) using SVD.
    Returns Q with shape (n, k) where columns span ker(M).
    """
    # M: (m,n)
    U, S, Vh = torch.linalg.svd(M, full_matrices=True)
    if S.numel() == 0:
        # zero matrix
        n = M.shape[1]
        return torch.eye(n, dtype=M.dtype, device=M.device)
    # rank = # singular values > tol
    rank = int(torch.sum(S > tol).item())
    V = Vh.transpose(-2, -1)
    Q = V[:, rank:]  # (n, n-rank)
    return Q


def physical_projector_Pi(
    x_links: torch.Tensor,
    cluster: Cluster,
    tol: float = 1e-10,
) -> torch.Tensor:
    """
    Compute Π_phys(x) as an orthonormal basis matrix for the horizontal subspace:
        Π_phys(x) columns span ker(D0(U(x))^T).
    """
    T = su3_basis()
    U_edges = cluster_U_from_x(x_links, cluster, T)
    D0 = vertical_operator_D0(U_edges, cluster, T)              # (8E, 8V)
    Q = nullspace_basis(D0.T, tol=tol)                          # (8E, dim_hor)
    return Q


def project_hessian(H: torch.Tensor, Pi: torch.Tensor) -> torch.Tensor:
    """Return Π^T H Π."""
    return Pi.T @ H @ Pi


# ----------------------------
# Schur complement (optional)
# ----------------------------

def schur_complement(
    H: torch.Tensor,
    keep: Sequence[int],
    drop: Sequence[int],
    rcond: float = 1e-12,
) -> torch.Tensor:
    """
    Quadratic marginalization / elimination of variables via the Schur complement.

    Given a symmetric Hessian H with variables ordered as (keep, drop),
        H = [[A, B],
             [B^T, C]],
    return H_eff = A - B C^+ B^T.

    C^+ is the Moore–Penrose pseudoinverse (with rcond cutoff) so this survives
    gauge / harmonic near-null modes.

    NOTE: if you *can* gauge-fix to make C invertible on the eliminated sector,
    use an inverse instead of pinv for sharper numerics.
    """
    keep = list(keep)
    drop = list(drop)
    idx = keep + drop
    Hs = H[idx][:, idx]
    nK = len(keep)
    A = Hs[:nK, :nK]
    B = Hs[:nK, nK:]
    C = Hs[nK:, nK:]
    Cpinv = torch.linalg.pinv(C, rcond=rcond)
    Heff = A - B @ Cpinv @ B.T
    # symmetrize to kill numerical noise
    Heff = 0.5 * (Heff + Heff.T)
    return Heff
