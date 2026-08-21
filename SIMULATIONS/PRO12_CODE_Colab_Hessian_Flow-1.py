"""PRO12 — Horizontal projector + Wilson/Haar action + Hessian-vector products + flow/blocking.

This script is designed to be copied into Google Colab (A100-friendly).
It provides a concrete computational skeleton for the three hard steps:

1) Derive/diagnose PBH/Riccati structure from an actual flow map (finite-diff Hessian evolution)
2) Test positivity of the source term R(t) on the horizontal (physical) sector
3) Quantify off-diagonal mixing under coarse-graining (commutators / Schur complements)

It starts with the cheap benchmark:
- linearized (abelianized) Wilson action + quadratic Haar mass term
with an FFT-based horizontal projector.

Then it climbs to:
- nonlinear SU(2)/SU(3) Wilson action using U=exp(X)
- exact Haar Jacobian potential V_Haar(X) = -log det(∫_0^1 exp(-s ad_X) ds)
- autodiff Hessian–vector products (HVP)
- covariant horizontal projector via Faddeev–Popov solve (conjugate gradient)

NOTE
- Everything is written in torch.float64 / torch.complex128 on purpose.
- On an A100 this is still fast for small lattices (L=2..4).

Run:
  python PRO12_CODE_Colab_Hessian_Flow.py --demo haar
  python PRO12_CODE_Colab_Hessian_Flow.py --demo linear
  python PRO12_CODE_Colab_Hessian_Flow.py --demo su3 --L 2 --D 4 --beta 2.0

"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Callable, Tuple, Optional

import numpy as np
import torch

# ---------- precision defaults ----------

torch.set_default_dtype(torch.float64)


def get_device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ---------- lattice ----------

@dataclass(frozen=True)
class Lattice:
    L: int
    D: int
    device: torch.device

    coords: torch.Tensor      # (n_sites, D) int64
    fwd: torch.Tensor         # (n_sites, D) int64
    bwd: torch.Tensor         # (n_sites, D) int64

    @property
    def n_sites(self) -> int:
        return self.L ** self.D

    def reshape_sites(self, x: torch.Tensor, extra_dims: Tuple[int, ...] = ()) -> torch.Tensor:
        return x.reshape((self.L,) * self.D + extra_dims)


def make_lattice(L: int, D: int, device: torch.device) -> Lattice:
    n_sites = L ** D
    coords = torch.zeros((n_sites, D), dtype=torch.int64, device=device)
    for idx in range(n_sites):
        x = idx
        for mu in range(D):
            coords[idx, mu] = x % L
            x //= L

    powers = torch.tensor([L ** mu for mu in range(D)], dtype=torch.int64, device=device)

    def idx_from_coords(c: torch.Tensor) -> torch.Tensor:
        # c: (...,D)
        return torch.sum(c * powers, dim=-1)

    fwd = torch.empty((n_sites, D), dtype=torch.int64, device=device)
    bwd = torch.empty((n_sites, D), dtype=torch.int64, device=device)

    for mu in range(D):
        c_f = coords.clone()
        c_f[:, mu] = (c_f[:, mu] + 1) % L
        fwd[:, mu] = idx_from_coords(c_f)

        c_b = coords.clone()
        c_b[:, mu] = (c_b[:, mu] - 1) % L
        bwd[:, mu] = idx_from_coords(c_b)

    return Lattice(L=L, D=D, device=device, coords=coords, fwd=fwd, bwd=bwd)


# ---------- Lie algebra bases (anti-Hermitian, Tr(Ta Tb)=-1/2 δab) ----------

def su2_basis(device: torch.device) -> torch.Tensor:
    sigma1 = torch.tensor([[0, 1], [1, 0]], dtype=torch.complex128, device=device)
    sigma2 = torch.tensor([[0, -1j], [1j, 0]], dtype=torch.complex128, device=device)
    sigma3 = torch.tensor([[1, 0], [0, -1]], dtype=torch.complex128, device=device)
    T = torch.stack([1j * sigma1 / 2, 1j * sigma2 / 2, 1j * sigma3 / 2], dim=0)
    return T  # (3,2,2)


def su3_basis(device: torch.device) -> torch.Tensor:
    i = torch.tensor(1j, dtype=torch.complex128, device=device)
    lam = []
    lam.append(torch.tensor([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=torch.complex128, device=device))
    lam.append(torch.tensor([[0, -i, 0], [i, 0, 0], [0, 0, 0]], dtype=torch.complex128, device=device))
    lam.append(torch.tensor([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=torch.complex128, device=device))
    lam.append(torch.tensor([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=torch.complex128, device=device))
    lam.append(torch.tensor([[0, 0, -i], [0, 0, 0], [i, 0, 0]], dtype=torch.complex128, device=device))
    lam.append(torch.tensor([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=torch.complex128, device=device))
    lam.append(torch.tensor([[0, 0, 0], [0, 0, -i], [0, i, 0]], dtype=torch.complex128, device=device))
    lam.append((1 / math.sqrt(3)) * torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=torch.complex128, device=device))
    lam = torch.stack(lam, dim=0)  # (8,3,3)
    T = 1j * (lam / 2)             # anti-Hermitian
    return T


def coords_to_X(x: torch.Tensor, basis_T: torch.Tensor) -> torch.Tensor:
    """x: (...,m) real -> X: (...,N,N) complex anti-Hermitian."""
    return torch.einsum("...a,aij->...ij", x.to(torch.complex128), basis_T)


def expm_from_coords(x: torch.Tensor, basis_T: torch.Tensor) -> torch.Tensor:
    """Batch group exponential U = exp(X(x))."""
    X = coords_to_X(x, basis_T)
    return torch.matrix_exp(X)


# ---------- Haar Jacobian potential V_Haar(x) = -log det(∫_0^1 exp(-s ad_X) ds) ----------

def gauss_legendre_01(n: int, device: torch.device) -> Tuple[torch.Tensor, torch.Tensor]:
    """Gauss–Legendre nodes/weights on [0,1]."""
    x, w = np.polynomial.legendre.leggauss(n)
    s = 0.5 * (x + 1.0)
    ww = 0.5 * w
    return (
        torch.tensor(s, dtype=torch.float64, device=device),
        torch.tensor(ww, dtype=torch.float64, device=device),
    )


def ad_matrix_from_X(X: torch.Tensor, basis_T: torch.Tensor) -> torch.Tensor:
    """Compute the adjoint-representation matrix of ad_X in the chosen orthonormal basis.

    Inputs
      X: (...,N,N) complex anti-Hermitian
      basis_T: (m,N,N) complex anti-Hermitian, orthonormal with Tr(Ta Tb)=-1/2 δ

    Returns
      A: (...,m,m) real with A_{ab} = coefficients of [X,T_b] in basis.
    """
    # comm_b = [X, T_b]
    Xb = X.unsqueeze(-3)                 # (...,1,N,N)
    Tb = basis_T.unsqueeze(0)            # (1,m,N,N)
    comm = Xb @ Tb - Tb @ Xb             # (...,m,N,N)

    # coefficients c_ab = -2 Re Tr(T_a comm_b)
    comm_t = comm.transpose(-1, -2)      # (...,m,N,N) with indices (...,b,i,j)=comm(...,b,j,i)
    tr = torch.einsum("aij,...bij->...ab", basis_T, comm_t)
    coeff = -2.0 * torch.real(tr)        # (...,a,b)
    return coeff


def haar_potential(x: torch.Tensor, basis_T: torch.Tensor, quad_n: int = 8) -> torch.Tensor:
    """Exact Haar Jacobian potential per sample.

    x: (...,m) real
    returns V: (...) real, where V = -log det(∫_0^1 exp(-s ad_X) ds).

    Autodiff-friendly (uses only matrix_exp + slogdet).
    """
    device = x.device
    s_nodes, w_nodes = gauss_legendre_01(quad_n, device)

    X = coords_to_X(x, basis_T)                    # (...,N,N)
    A = ad_matrix_from_X(X, basis_T)               # (...,m,m) real

    F = None
    for s, w in zip(s_nodes, w_nodes):
        M = torch.matrix_exp((-s) * A)
        F = w * M if F is None else (F + w * M)

    sign, logabsdet = torch.linalg.slogdet(F)
    # sign should be positive in the small coordinate balls relevant for SAFE-region work
    # (if it flips sign, your coordinate chart is too large and you should shrink R0)
    return -logabsdet


# ---------- Wilson action ----------

def wilson_action(U: torch.Tensor, lat: Lattice, beta: float) -> torch.Tensor:
    """Standard Wilson plaquette action.

    U: (n_sites, D, N, N) complex unitary

    S = beta * Σ_{x,mu<nu} (1 - (1/N) Re Tr U_{mu,nu}(x)).
    """
    N = U.shape[-1]
    S = torch.tensor(0.0, dtype=torch.float64, device=U.device)

    for mu in range(lat.D):
        for nu in range(mu + 1, lat.D):
            U1 = U[:, mu]
            U2 = U[lat.fwd[:, mu], nu]
            U3 = U[lat.fwd[:, nu], mu].conj().transpose(-1, -2)
            U4 = U[:, nu].conj().transpose(-1, -2)
            Up = U1 @ U2 @ U3 @ U4
            tr = torch.real(torch.einsum("...ii->...", Up))
            S = S + torch.sum(1.0 - tr / N)

    return beta * S


# ---------- linearized (abelianized) Wilson + Haar-mass benchmark ----------

def curl_F(A: torch.Tensor, lat: Lattice) -> torch.Tensor:
    """Discrete curl F_{mu,nu}(x) for a 1-form A.

    A: (n_sites, D, m) real
    Returns: (n_plaq_types, n_sites, m)
    """
    Fs = []
    for mu in range(lat.D):
        for nu in range(mu + 1, lat.D):
            Axmu = A[:, mu]
            Axnu = A[:, nu]
            Axmu_nu = A[lat.fwd[:, mu], nu]
            Axnu_mu = A[lat.fwd[:, nu], mu]
            F = Axmu + Axmu_nu - Axnu_mu - Axnu
            Fs.append(F)
    return torch.stack(Fs, dim=0)


def linear_action(A: torch.Tensor, lat: Lattice, beta: float, kappa_mass: float) -> torch.Tensor:
    """Quadratic benchmark: (beta/2)||curl A||^2 + (kappa/2)||A||^2."""
    F = curl_F(A, lat)
    S1 = 0.5 * beta * torch.sum(F * F)
    S2 = 0.5 * kappa_mass * torch.sum(A * A)
    return S1 + S2


# ---------- linear horizontal projector (FFT Poisson solve) ----------

def divergence(V: torch.Tensor, lat: Lattice) -> torch.Tensor:
    # V: (n_sites,D,m)
    div = 0.0
    for mu in range(lat.D):
        div = div + (V[:, mu] - V[lat.bwd[:, mu], mu])
    return div


def grad_phi(phi: torch.Tensor, lat: Lattice) -> torch.Tensor:
    # phi: (n_sites,m)
    grads = []
    for mu in range(lat.D):
        grads.append(phi - phi[lat.fwd[:, mu]])
    return torch.stack(grads, dim=1)


def poisson_solve(div: torch.Tensor, lat: Lattice) -> torch.Tensor:
    """Solve Laplacian(phi)=div with periodic BC and zero-mean gauge fix."""
    m = div.shape[-1]
    div_grid = div.reshape((lat.L,) * lat.D + (m,))
    div_hat = torch.fft.fftn(div_grid, dim=tuple(range(lat.D)))

    grids = torch.meshgrid(*[torch.arange(lat.L, device=div.device) for _ in range(lat.D)], indexing="ij")
    lam = torch.zeros((lat.L,) * lat.D, dtype=torch.float64, device=div.device)
    for mu in range(lat.D):
        n = grids[mu].to(torch.float64)
        lam = lam + 2.0 * (1.0 - torch.cos(2 * math.pi * n / lat.L))
    lam = lam.unsqueeze(-1)

    invlam = torch.zeros_like(lam)
    mask = lam > 1e-12
    invlam[mask] = 1.0 / lam[mask]

    phi_hat = div_hat * invlam
    phi_grid = torch.fft.ifftn(phi_hat, dim=tuple(range(lat.D))).real
    return phi_grid.reshape(lat.n_sites, m)


def project_horizontal_linear(V: torch.Tensor, lat: Lattice) -> torch.Tensor:
    div = divergence(V, lat)
    phi = poisson_solve(div, lat)
    return V - grad_phi(phi, lat)


# ---------- covariant horizontal projector (FP solve via CG) ----------

def adjoint_rep(U: torch.Tensor, basis_T: torch.Tensor) -> torch.Tensor:
    """Adjoint representation matrix Ad_U in the chosen basis.

    U: (...,N,N) complex unitary
    Returns: (...,m,m) real matrix such that
      coords( U (sum v_a T_a) U^{-1} ) = Ad_U · v
    """
    m = basis_T.shape[0]
    # Build conjugated basis elements
    # Tb':= U Tb U^{-1}
    Uinv = U.conj().transpose(-1, -2)
    Tb = basis_T.unsqueeze(0)                                # (1,m,N,N)
    conj = U.unsqueeze(-3) @ Tb @ Uinv.unsqueeze(-3)         # (...,m,N,N)

    # coefficients: v'_a = -2 Re Tr(T_a conj_b)
    conj_t = conj.transpose(-1, -2)
    tr = torch.einsum("aij,...bij->...ab", basis_T, conj_t)
    Ad = -2.0 * torch.real(tr)
    return Ad


def D_apply(phi: torch.Tensor, AdU: torch.Tensor, lat: Lattice) -> torch.Tensor:
    """Covariant forward difference (site field -> link field).

    phi: (n_sites,m)
    AdU: (n_sites,D,m,m)
    Returns: (n_sites,D,m) with (D phi)_{x,mu} = phi_x - Ad_{U_{x,mu}} phi_{x+mu}.
    """
    m = phi.shape[-1]
    out = torch.empty((lat.n_sites, lat.D, m), dtype=torch.float64, device=phi.device)
    for mu in range(lat.D):
        phi_fwd = phi[lat.fwd[:, mu]]
        transported = torch.einsum("xab,xb->xa", AdU[:, mu], phi_fwd)
        out[:, mu] = phi - transported
    return out


def D_adj_apply(W: torch.Tensor, AdU: torch.Tensor, lat: Lattice) -> torch.Tensor:
    """Adjoint covariant divergence (link field -> site field).

    W: (n_sites,D,m)
    AdU: (n_sites,D,m,m)
    Returns: (n_sites,m) with (D^* W)_x = Σ_mu (W_{x,mu} - Ad_{U_{x-mu,mu}}^{-1} W_{x-mu,mu}).

    With orthonormal basis, Ad_{U^{-1}} = Ad_U^T.
    """
    m = W.shape[-1]
    out = torch.zeros((lat.n_sites, m), dtype=torch.float64, device=W.device)
    for mu in range(lat.D):
        out = out + W[:, mu]
        W_bwd = W[lat.bwd[:, mu], mu]
        Ad_bwd = AdU[lat.bwd[:, mu], mu]
        transported = torch.einsum("xba,xb->xa", Ad_bwd, W_bwd)  # Ad^T via swapped indices in einsum
        out = out - transported
    return out


def fp_apply(phi: torch.Tensor, AdU: torch.Tensor, lat: Lattice) -> torch.Tensor:
    return D_adj_apply(D_apply(phi, AdU, lat), AdU, lat)


def cg_solve(
    A: Callable[[torch.Tensor], torch.Tensor],
    b: torch.Tensor,
    x0: Optional[torch.Tensor] = None,
    tol: float = 1e-10,
    maxiter: int = 200,
    enforce_mean_zero: bool = True,
) -> torch.Tensor:
    """Conjugate gradient on a symmetric positive semidefinite operator.

    For the FP operator on periodic lattices, enforce_mean_zero removes the global gauge zero-mode.
    """
    x = torch.zeros_like(b) if x0 is None else x0.clone()

    if enforce_mean_zero:
        x = x - x.mean(dim=0, keepdim=True)
        b = b - b.mean(dim=0, keepdim=True)

    r = b - A(x)
    if enforce_mean_zero:
        r = r - r.mean(dim=0, keepdim=True)

    p = r.clone()
    rs_old = torch.sum(r * r)

    for _ in range(maxiter):
        Ap = A(p)
        alpha = rs_old / (torch.sum(p * Ap) + 1e-30)
        x = x + alpha * p
        r = r - alpha * Ap
        if enforce_mean_zero:
            x = x - x.mean(dim=0, keepdim=True)
            r = r - r.mean(dim=0, keepdim=True)
        rs_new = torch.sum(r * r)
        if torch.sqrt(rs_new) < tol:
            break
        p = r + (rs_new / (rs_old + 1e-30)) * p
        rs_old = rs_new
    return x


def project_horizontal_covariant(W: torch.Tensor, AdU: torch.Tensor, lat: Lattice, tol: float = 1e-10, maxiter: int = 200) -> torch.Tensor:
    """Horizontal projection: P = I - D (D^* D)^{-1} D^*."""
    b = D_adj_apply(W, AdU, lat)
    A = lambda phi: fp_apply(phi, AdU, lat)
    phi = cg_solve(A, b, tol=tol, maxiter=maxiter, enforce_mean_zero=True)
    return W - D_apply(phi, AdU, lat)


# ---------- autodiff Hessian–vector products ----------

def hvp(action_fn: Callable[[torch.Tensor], torch.Tensor], x: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
    """Hessian-vector product H(x)·v without materializing the Hessian."""
    y = action_fn(x)
    (g,) = torch.autograd.grad(y, x, create_graph=True)
    gv = torch.dot(g, v)
    (hv,) = torch.autograd.grad(gv, x)
    return hv


# ---------- Lanczos (Ritz) for extremal eigenvalues of a symmetric operator ----------

def lanczos_tridiag(
    op: Callable[[torch.Tensor], torch.Tensor],
    n: int,
    m_steps: int,
    device: torch.device,
    reorthogonalize: bool = True,
) -> torch.Tensor:
    q = torch.randn(n, device=device, dtype=torch.float64)
    q = q / torch.linalg.norm(q)

    q_prev = torch.zeros_like(q)
    beta_prev = torch.tensor(0.0, device=device, dtype=torch.float64)

    alphas = []
    betas = []
    Q = []

    for _ in range(m_steps):
        z = op(q)
        alpha = torch.dot(q, z)
        z = z - alpha * q - beta_prev * q_prev

        if reorthogonalize:
            for qi in Q:
                z = z - torch.dot(qi, z) * qi

        beta = torch.linalg.norm(z)
        alphas.append(alpha)
        betas.append(beta)
        Q.append(q)

        if beta < 1e-12:
            break

        q_prev = q
        q = z / beta
        beta_prev = beta

    k = len(alphas)
    T = torch.zeros((k, k), device=device, dtype=torch.float64)
    for i in range(k):
        T[i, i] = alphas[i]
        if i + 1 < k:
            T[i, i + 1] = betas[i]
            T[i + 1, i] = betas[i]
    return T


def lanczos_extremal_eigs(op: Callable[[torch.Tensor], torch.Tensor], n: int, m_steps: int, device: torch.device) -> Tuple[float, float]:
    T = lanczos_tridiag(op, n, m_steps=m_steps, device=device, reorthogonalize=True)
    eigs = torch.linalg.eigvalsh(T).cpu().numpy()
    return float(eigs[0]), float(eigs[-1])


# ---------- blocking (optional) ----------

def reunitarize(U: torch.Tensor) -> torch.Tensor:
    """Project a batch of matrices to SU(N) using polar decomposition + det normalization."""
    # U: (...,N,N) complex
    UdagU = U.conj().transpose(-1, -2) @ U
    # Hermitian positive definite; compute inverse square root
    evals, evecs = torch.linalg.eigh(UdagU)
    inv_sqrt = evecs @ torch.diag_embed(evals.clamp_min(1e-30).rsqrt()) @ evecs.conj().transpose(-1, -2)
    Up = U @ inv_sqrt

    # det normalize to SU(N)
    det = torch.linalg.det(Up)
    N = Up.shape[-1]
    det_phase = det ** (-1.0 / N)
    Up = Up * det_phase.unsqueeze(-1).unsqueeze(-1)
    return Up


def block_2x(U: torch.Tensor, lat: Lattice) -> Tuple[torch.Tensor, Lattice]:
    """2x decimation blocking map on a periodic lattice.

    Coarse lattice has L' = L/2 (requires even L).

    Coarse link is product of two fine links in the same direction.
    """
    assert lat.L % 2 == 0, "Need even L for 2x blocking"
    Lc = lat.L // 2
    coarse_lat = make_lattice(Lc, lat.D, U.device)

    # Map coarse site X to fine site x = 2X
    # Build fine indices for each coarse site
    Xcoords = coarse_lat.coords
    xcoords = (2 * Xcoords) % lat.L
    # convert xcoords to fine site indices (lex ordering)
    powers = torch.tensor([lat.L ** mu for mu in range(lat.D)], dtype=torch.int64, device=U.device)
    fine_site = torch.sum(xcoords * powers, dim=-1)

    n_sites_c = coarse_lat.n_sites
    D = lat.D

    N = U.shape[-1]
    Uc = torch.empty((n_sites_c, D, N, N), dtype=torch.complex128, device=U.device)

    for mu in range(D):
        x = fine_site
        x_fwd = lat.fwd[x, mu]
        Uc[:, mu] = U[x, mu] @ U[x_fwd, mu]

    Uc = reunitarize(Uc)
    return Uc, coarse_lat


# ---------- demos ----------

def demo_haar_constants() -> None:
    device = get_device()
    print(f"Device: {device}")

    # SU(2)
    T2 = su2_basis(device)
    x2 = (torch.randn(3, device=device) * 0.05).requires_grad_(True)

    def V2(z):
        return haar_potential(z, T2, quad_n=8)

    H2 = torch.autograd.functional.hessian(V2, x2)
    e2 = torch.linalg.eigvalsh(H2).detach().cpu().numpy()
    print("SU(2): Haar Hessian eig min/max ~", float(e2.min()), float(e2.max()))

    # SU(3)
    T3 = su3_basis(device)
    x3 = (torch.randn(8, device=device) * 0.05).requires_grad_(True)

    def V3(z):
        return haar_potential(z, T3, quad_n=8)

    H3 = torch.autograd.functional.hessian(V3, x3)
    e3 = torch.linalg.eigvalsh(H3).detach().cpu().numpy()
    print("SU(3): Haar Hessian eig min/max ~", float(e3.min()), float(e3.max()))


def demo_linear(L: int, D: int, m: int, beta: float, kappa: float, m_steps: int) -> None:
    device = get_device()
    lat = make_lattice(L, D, device)

    # random base point (doesn't matter; linear action has constant Hessian)
    A0 = (0.01 * torch.randn((lat.n_sites, lat.D, m), device=device)).requires_grad_(True)

    def action_flat(x_flat: torch.Tensor) -> torch.Tensor:
        A = x_flat.reshape(lat.n_sites, lat.D, m)
        return linear_action(A, lat, beta=beta, kappa_mass=kappa)

    x0 = A0.reshape(-1)
    n = x0.numel()
    gamma = 10.0 * max(1.0, kappa)

    def op(v: torch.Tensor) -> torch.Tensor:
        V = v.reshape(lat.n_sites, lat.D, m)
        PV = project_horizontal_linear(V, lat)
        hv = hvp(action_flat, x0, PV.reshape(-1)).reshape(lat.n_sites, lat.D, m)
        Phv = project_horizontal_linear(hv, lat)
        Kv = V - PV
        return (Phv + gamma * Kv).reshape(-1)

    lam_min, lam_max = lanczos_extremal_eigs(op, n=n, m_steps=m_steps, device=device)
    print(f"Linear demo: L={L} D={D} m={m} beta={beta} kappa={kappa}")
    print("  smallest eigen (horizontal, kernel-lifted):", lam_min)
    print("  largest  eigen:", lam_max)


def demo_suN(
    group: str,
    L: int,
    D: int,
    beta: float,
    use_haar: bool,
    project: str,
    m_steps: int,
) -> None:
    device = get_device()
    lat = make_lattice(L, D, device)

    if group.lower() == "su2":
        basis = su2_basis(device)
    elif group.lower() == "su3":
        basis = su3_basis(device)
    else:
        raise ValueError("group must be su2 or su3")

    m = basis.shape[0]
    N = basis.shape[-1]

    # start near identity in exponential coords
    x0 = (0.05 * torch.randn((lat.n_sites, lat.D, m), device=device)).requires_grad_(True)
    x_flat = x0.reshape(-1)

    def action_flat(z: torch.Tensor) -> torch.Tensor:
        x = z.reshape(lat.n_sites, lat.D, m)
        U = expm_from_coords(x, basis).reshape(lat.n_sites, lat.D, N, N)
        S = wilson_action(U, lat, beta=beta)
        if use_haar:
            V = haar_potential(x.reshape(-1, m), basis, quad_n=8)
            S = S + torch.sum(V)
        return S

    # build projector
    if project == "linear":
        proj = lambda V: project_horizontal_linear(V.reshape(lat.n_sites, lat.D, m), lat).reshape(-1)
        print("Projector: linear (FFT) — only correct near identity")
        AdU = None
    elif project == "covariant":
        with torch.no_grad():
            U = expm_from_coords(x0, basis).reshape(lat.n_sites, lat.D, N, N)
        AdU = adjoint_rep(U.reshape(-1, N, N), basis).reshape(lat.n_sites, lat.D, m, m)

        def proj(Vflat: torch.Tensor) -> torch.Tensor:
            W = Vflat.reshape(lat.n_sites, lat.D, m)
            Ph = project_horizontal_covariant(W, AdU, lat, tol=1e-10, maxiter=200)
            return Ph.reshape(-1)

        print("Projector: covariant (FP solve via CG)")
    else:
        raise ValueError("project must be 'linear' or 'covariant'")

    n = x_flat.numel()
    gamma = 10.0

    def op(v: torch.Tensor) -> torch.Tensor:
        Pv = proj(v)
        hv = hvp(action_flat, x_flat, Pv)
        Phv = proj(hv)
        Kv = v - Pv
        return Phv + gamma * Kv

    lam_min, lam_max = lanczos_extremal_eigs(op, n=n, m_steps=m_steps, device=device)
    print(f"Nonlinear demo: {group.upper()} L={L} D={D} beta={beta} use_haar={use_haar}")
    print("  smallest eigen (horizontal, kernel-lifted):", lam_min)
    print("  largest  eigen:", lam_max)


# ---------- CLI ----------

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", type=str, required=True, choices=["haar", "linear", "su2", "su3"], help="Which demo to run")
    parser.add_argument("--L", type=int, default=2)
    parser.add_argument("--D", type=int, default=4)
    parser.add_argument("--beta", type=float, default=2.0)
    parser.add_argument("--kappa", type=float, default=0.25, help="Quadratic Haar mass used in linear demo")
    parser.add_argument("--m_steps", type=int, default=60, help="Lanczos steps")
    parser.add_argument("--project", type=str, default="covariant", choices=["linear", "covariant"], help="Projector for su2/su3 demo")
    parser.add_argument("--no_haar", action="store_true", help="Disable exact Haar potential in su2/su3 demo")

    args = parser.parse_args()

    if args.demo == "haar":
        demo_haar_constants()
    elif args.demo == "linear":
        # dim(𝔤): SU(2)=3, SU(3)=8
        demo_linear(L=args.L, D=args.D, m=3, beta=args.beta, kappa=args.kappa, m_steps=args.m_steps)
    elif args.demo == "su2":
        demo_suN(group="su2", L=args.L, D=args.D, beta=args.beta, use_haar=(not args.no_haar), project=args.project, m_steps=args.m_steps)
    elif args.demo == "su3":
        demo_suN(group="su3", L=args.L, D=args.D, beta=args.beta, use_haar=(not args.no_haar), project=args.project, m_steps=args.m_steps)
    else:
        raise RuntimeError("unreachable")


if __name__ == "__main__":
    main()

# ---------- PBH/Riccati diagnostics (finite-difference) ----------

def flow_step_coords(x: torch.Tensor, action_fn: Callable[[torch.Tensor], torch.Tensor], dt: float) -> torch.Tensor:
    """One explicit Euler step for the coordinate gradient flow: x' = x - dt * ∇S(x).

    This is not *exactly* Wilson flow on the group manifold, but it is an honest gradient-flow scheme
    for the coordinate action you give it. It is good enough to test whether a Riccati-type
    curvature evolution inequality is plausible in the intended regime (small charts / SAFE region).
    """
    y = action_fn(x)
    (g,) = torch.autograd.grad(y, x)
    with torch.no_grad():
        x_next = x - dt * g
    return x_next.detach().requires_grad_(True)


def pbh_source_quadratic_form(
    action_fn: Callable[[torch.Tensor], torch.Tensor],
    x: torch.Tensor,
    proj: Callable[[torch.Tensor], torch.Tensor],
    dt: float,
    n_samples: int = 32,
    seed: int = 0,
) -> Tuple[float, float, float]:
    """Estimate vᵀ R v on random horizontal vectors, where

      R := (d/dt)H + 2 H^2

    using finite differences on HVPs:
      dH·v ≈ (H(x_next)·v - H(x)·v) / dt

    Returns (min, mean, max) over sampled vectors.

    If these are mostly ≥ 0, that's evidence (not proof) that the source term is positive
    on the tested sector at the tested configuration.
    """
    torch.manual_seed(seed)
    device = x.device
    n = x.numel()

    # Base Hessian action on vectors
    def H(v: torch.Tensor, x_here: torch.Tensor) -> torch.Tensor:
        v_h = proj(v)
        return proj(hvp(action_fn, x_here, v_h))

    # One flow step to approximate time derivative
    x_next = flow_step_coords(x, action_fn, dt=dt)

    vals = []
    for _ in range(n_samples):
        v = torch.randn(n, device=device)
        v = proj(v)
        v = v / (torch.linalg.norm(v) + 1e-30)

        Hv = H(v, x)
        Hv_next = H(v, x_next)

        dH_v = (Hv_next - Hv) / dt
        H2_v = H(Hv, x)  # H^2 v
        R_v = dH_v + 2.0 * H2_v

        q = torch.dot(v, R_v).item()
        vals.append(q)

    vals = np.array(vals, dtype=float)
    return float(vals.min()), float(vals.mean()), float(vals.max())


# ---------- off-diagonal mixing diagnostics ----------

def make_spatial_projector_links(lat: Lattice, radius: float) -> torch.Tensor:
    """Return a boolean mask selecting links whose *base site* is within 'radius' (ℓ2) of the origin.

    For commutator tests we only need a crude local-vs-nonlocal split.
    """
    coords = lat.coords.to(torch.float64)
    r = torch.linalg.norm(coords, dim=1)
    mask_sites = r <= radius
    # broadcast to links: (n_sites,D)
    mask_links = mask_sites[:, None].expand(-1, lat.D)
    return mask_links


def commutator_norm_estimate(
    H_op: Callable[[torch.Tensor], torch.Tensor],
    P_mask: torch.Tensor,
    n: int,
    n_iter: int = 25,
    seed: int = 0,
) -> float:
    """Estimate ||[H,P]|| by power iteration on the commutator.

    P is implemented as pointwise mask multiplication in the link basis.
    """
    torch.manual_seed(seed)
    device = P_mask.device

    # Flatten mask to vector length n
    P_flat = P_mask.reshape(-1).to(torch.float64)

    def P(v: torch.Tensor) -> torch.Tensor:
        return P_flat * v

    def comm(v: torch.Tensor) -> torch.Tensor:
        return H_op(P(v)) - P(H_op(v))

    v = torch.randn(n, device=device)
    v = v / (torch.linalg.norm(v) + 1e-30)

    for _ in range(n_iter):
        w = comm(v)
        nw = torch.linalg.norm(w) + 1e-30
        v = w / nw

    # Rayleigh-ish estimate
    return float(torch.linalg.norm(comm(v)).item())
