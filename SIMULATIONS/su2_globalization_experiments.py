"""
SU(2) lattice gauge toy sampler (projected Langevin on unit quaternions)
---------------------------------------------------------------------

Purpose: empirical "globalization hints" experiments

1) Estimate how likely different candidate "core sets" A are as volume grows:
   - average plaquette action density small
   - max plaquette angle small (very strict)
   - (optional) scaled L2 distance of links from identity

2) Collect diagnostics that relate to Lyapunov-style drift heuristics:
   - action S
   - (approx) ||grad S||^2 on the constrained manifold

This is *not* a production-grade lattice gauge code.
It's meant as a quick exploratory tool you can run on Colab GPU.

On large lattices you will want an SU(2) heatbath / HMC implementation with staples
(and ideally in CUDA/C++).
"""

from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Dict, Tuple, List, Optional

import torch


# ----------------------------
# Quaternion SU(2) utilities
# ----------------------------

def qnormalize(q: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """Normalize unit quaternions; q shape (...,4)."""
    norm = torch.linalg.norm(q, dim=-1, keepdim=True).clamp_min(eps)
    return q / norm

def qconj(q: torch.Tensor) -> torch.Tensor:
    """Quaternion conjugate (a,b,c,d)->(a,-b,-c,-d)."""
    qc = q.clone()
    qc[..., 1:] = -qc[..., 1:]
    return qc

def qmul(q: torch.Tensor, r: torch.Tensor) -> torch.Tensor:
    """Hamilton product; q,r shape (...,4)."""
    a, b, c, d = q.unbind(-1)
    e, f, g, h = r.unbind(-1)
    return torch.stack(
        [
            a * e - b * f - c * g - d * h,
            a * f + b * e + c * h - d * g,
            a * g - b * h + c * e + d * f,
            a * h + b * g - c * f + d * e,
        ],
        dim=-1,
    )

def su2_random(shape: Tuple[int, ...], device: torch.device) -> torch.Tensor:
    """Haar-ish random SU(2) by normalizing Gaussian quaternions."""
    q = torch.randn(*shape, 4, device=device)
    return qnormalize(q)

def su2_angle(q: torch.Tensor) -> torch.Tensor:
    """Geodesic-like angle theta in [0,pi], with scalar part cos(theta)."""
    a = q[..., 0].clamp(-1.0, 1.0)
    return torch.arccos(a)


# ----------------------------
# Lattice ops
# ----------------------------

def plaquette_quaternion(U: torch.Tensor, mu: int, nu: int) -> torch.Tensor:
    """
    Oriented plaquette at each site for directions (mu,nu).
    U shape: (L,L,L,L, ndim, 4) for 4D; periodic BC.
    """
    U_mu = U[..., mu, :]
    U_nu = U[..., nu, :]

    # Shifted links
    U_mu_shift_nu = torch.roll(U_mu, shifts=-1, dims=nu)  # U(x+nu, mu)
    U_nu_shift_mu = torch.roll(U_nu, shifts=-1, dims=mu)  # U(x+mu, nu)

    # P = U(x,mu) U(x+mu,nu) U(x+nu,mu)^{-1} U(x,nu)^{-1}
    P = qmul(qmul(qmul(U_mu, U_nu_shift_mu), qconj(U_mu_shift_nu)), qconj(U_nu))
    return qnormalize(P)

def wilson_action(U: torch.Tensor, beta: float) -> torch.Tensor:
    """
    Wilson action for SU(2):
      S = beta * sum_{plaquettes} (1 - (1/2) Re Tr P)
        = beta * sum_{plaquettes} (1 - p0)
    where p0 is the scalar part of the plaquette quaternion.
    """
    ndim = U.shape[-2]
    S = torch.zeros((), device=U.device, dtype=U.dtype)
    for mu in range(ndim):
        for nu in range(mu + 1, ndim):
            P = plaquette_quaternion(U, mu, nu)
            S = S + beta * (1.0 - P[..., 0]).sum()
    return S

def plaquette_stats(U: torch.Tensor) -> Dict[str, float]:
    """
    Return mean and max of plaquette angle and plaquette scalar part.
    """
    ndim = U.shape[-2]
    p0_list = []
    ang_list = []
    for mu in range(ndim):
        for nu in range(mu + 1, ndim):
            P = plaquette_quaternion(U, mu, nu)
            p0_list.append(P[..., 0].reshape(-1))
            ang_list.append(su2_angle(P).reshape(-1))

    p0 = torch.cat(p0_list, dim=0)
    ang = torch.cat(ang_list, dim=0)
    # action density per plaquette is (1 - p0)
    return {
        "plaq_p0_mean": float(p0.mean().detach().cpu()),
        "plaq_p0_min": float(p0.min().detach().cpu()),
        "plaq_angle_mean": float(ang.mean().detach().cpu()),
        "plaq_angle_max": float(ang.max().detach().cpu()),
        "plaq_action_density_mean": float((1.0 - p0).mean().detach().cpu()),
        "n_plaquettes": int(p0.numel()),
    }


# ----------------------------
# Projected Langevin step on S^3 constraint (toy)
# ----------------------------

def projected_langevin_step(U: torch.Tensor, beta: float, eps: float) -> Tuple[torch.Tensor, float]:
    """
    One Euler–Maruyama step:
      U <- normalize( U - eps * grad_tan S + sqrt(2 eps) * noise_tan )

    NOTE: This is only an *approximation* to the true left-invariant Yang–Mills Langevin.
    It's enough for exploration, not for precision physics.
    """
    U = U.detach().requires_grad_(True)
    S = wilson_action(U, beta)
    S.backward()

    grad = U.grad
    # Tangent projection at each quaternion: g_tan = g - (g·U) U
    inner = (grad * U).sum(dim=-1, keepdim=True)
    grad_tan = grad - inner * U

    xi = torch.randn_like(U)
    inner_xi = (xi * U).sum(dim=-1, keepdim=True)
    xi_tan = xi - inner_xi * U

    U_new = U - eps * grad_tan + math.sqrt(2.0 * eps) * xi_tan
    U_new = qnormalize(U_new)
    return U_new.detach(), float(S.detach().cpu())


def gradnorm_sq(U: torch.Tensor, beta: float) -> float:
    """Approximate ||grad S||^2 on the constrained manifold (ambient projection)."""
    U = U.detach().requires_grad_(True)
    S = wilson_action(U, beta)
    S.backward()
    grad = U.grad
    grad_tan = grad - (grad * U).sum(dim=-1, keepdim=True) * U
    return float((grad_tan ** 2).sum().detach().cpu())


# ----------------------------
# Experiment harness
# ----------------------------

@dataclass
class RunConfig:
    L: int = 4
    beta: float = 3.0
    eps: float = 2e-4
    steps: int = 10_000
    burn: int = 2_000
    thin: int = 50
    seed: int = 0
    device: str = "cuda"  # "cuda" or "cpu"

@dataclass
class CoreThresholds:
    # A "core set" defined by plaquette action density mean <= thr
    mean_plaq_action_density: float = 0.35
    # A very strict core defined by max plaquette angle <= thr (radians)
    max_plaq_angle: float = 0.9

def run_experiment(cfg: RunConfig, thr: CoreThresholds) -> Dict[str, float]:
    torch.manual_seed(cfg.seed)
    device = torch.device(cfg.device if (cfg.device == "cpu" or torch.cuda.is_available()) else "cpu")

    ndim = 4
    U = su2_random((cfg.L, cfg.L, cfg.L, cfg.L, ndim), device=device)

    n_samples = 0
    core_mean_density_hits = 0
    core_max_angle_hits = 0

    action_vals: List[float] = []
    plaq_density_vals: List[float] = []
    plaq_angle_max_vals: List[float] = []
    gradnorm_vals: List[float] = []

    for t in range(cfg.steps):
        U, S = projected_langevin_step(U, beta=cfg.beta, eps=cfg.eps)

        if t >= cfg.burn and (t - cfg.burn) % cfg.thin == 0:
            stats = plaquette_stats(U)
            g2 = gradnorm_sq(U, cfg.beta)

            n_samples += 1
            action_vals.append(S)
            plaq_density_vals.append(stats["plaq_action_density_mean"])
            plaq_angle_max_vals.append(stats["plaq_angle_max"])
            gradnorm_vals.append(g2)

            if stats["plaq_action_density_mean"] <= thr.mean_plaq_action_density:
                core_mean_density_hits += 1
            if stats["plaq_angle_max"] <= thr.max_plaq_angle:
                core_max_angle_hits += 1

    # summarize
    def mean(xs: List[float]) -> float:
        return float(sum(xs) / max(1, len(xs)))

    def std(xs: List[float]) -> float:
        m = mean(xs)
        return float(math.sqrt(sum((x - m) ** 2 for x in xs) / max(1, len(xs) - 1)))

    out = {
        "L": cfg.L,
        "beta": cfg.beta,
        "eps": cfg.eps,
        "n_samples": n_samples,

        "action_mean": mean(action_vals),
        "action_std": std(action_vals),

        "plaq_action_density_mean": mean(plaq_density_vals),
        "plaq_action_density_std": std(plaq_density_vals),

        "plaq_angle_max_mean": mean(plaq_angle_max_vals),
        "plaq_angle_max_std": std(plaq_angle_max_vals),

        "gradnorm_sq_mean": mean(gradnorm_vals),
        "gradnorm_sq_std": std(gradnorm_vals),

        # empirical core probabilities
        "P_core_mean_density": core_mean_density_hits / max(1, n_samples),
        "P_core_max_angle": core_max_angle_hits / max(1, n_samples),
    }
    return out


if __name__ == "__main__":
    cfg = RunConfig(L=2, beta=3.0, eps=2e-4, steps=6000, burn=2000, thin=100, device="cpu")
    thr = CoreThresholds(mean_plaq_action_density=0.35, max_plaq_angle=0.9)
    out = run_experiment(cfg, thr)
    for k, v in out.items():
        print(f"{k:>24s} : {v}")
