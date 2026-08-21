#!/usr/bin/env python3
"""
A100-worthy SU(2) 4D lattice stress test.

Two modes:

1) --mode hunt
   Massive parallel counterexample hunt for:
     Bavg >= eps  AND  alignment_score >= align_min  AND  force_norm small

2) --mode sgld
   Stochastic quantization (manifold SGLD / Langevin on SU(2)) to get
   empirical distributions of (Bavg, force_norm, alignment_score).

Notes
-----
- SU(2) links stored as unit quaternions q=(a,b,c,d) in R^4.
- Plaquette defect uses 1 - a (since Tr(U)=2a in the fundamental rep).
- Force = right-trivialized Riemannian gradient of Wilson action.
"""

import argparse
import math
import time
from dataclasses import dataclass
from typing import Tuple, List

import numpy as np
import torch


# -----------------------------
# SU(2) quaternion ops
# -----------------------------
def su2_normalize(q: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    return q / (q.pow(2).sum(dim=-1, keepdim=True).clamp_min(eps).sqrt())


def su2_mul(q1: torch.Tensor, q2: torch.Tensor) -> torch.Tensor:
    a1, b1, c1, d1 = q1.unbind(-1)
    a2, b2, c2, d2 = q2.unbind(-1)
    return torch.stack(
        [
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
        ],
        dim=-1,
    )


def su2_inv(q: torch.Tensor) -> torch.Tensor:
    # For unit quaternions, inverse = conjugate
    a, b, c, d = q.unbind(-1)
    return torch.stack([a, -b, -c, -d], dim=-1)


def su2_exp(v: torch.Tensor) -> torch.Tensor:
    """
    Exponential map su(2) ~ R^3 -> SU(2) ~ S^3 in quaternion coords.
    v shape (...,3) returns (...,4).
    """
    theta = v.pow(2).sum(dim=-1, keepdim=True).sqrt()
    a = torch.cos(theta)
    s_over_theta = torch.where(
        theta > 1e-8,
        torch.sin(theta) / theta,
        1 - theta.pow(2) / 6
    )
    vec = s_over_theta * v
    return torch.cat([a, vec], dim=-1)


# -----------------------------
# Lattice plaquettes + action
# -----------------------------
def plaquettes(U: torch.Tensor) -> torch.Tensor:
    """
    Compute oriented plaquettes for all mu<nu.

    U shape: (B, L, L, L, L, d, 4) with d=4
    Returns: plaqs shape (B, 6, L, L, L, L, 4)
    """
    d = U.shape[-2]
    assert d == 4, "This script is set up for d=4."
    pairs = [(mu, nu) for mu in range(d) for nu in range(mu + 1, d)]

    plaqs = []
    for mu, nu in pairs:
        U_mu = U[..., mu, :]  # (B, lattice..., 4)
        U_nu = U[..., nu, :]
        # x + e_mu
        U_nu_x_plus_mu = torch.roll(U_nu, shifts=-1, dims=1 + mu)
        # x + e_nu
        U_mu_x_plus_nu = torch.roll(U_mu, shifts=-1, dims=1 + nu)

        # U_mu(x) U_nu(x+mu) U_mu(x+nu)^{-1} U_nu(x)^{-1}
        p = su2_mul(
            su2_mul(su2_mul(U_mu, U_nu_x_plus_mu), su2_inv(U_mu_x_plus_nu)),
            su2_inv(U_nu),
        )
        plaqs.append(p)

    return torch.stack(plaqs, dim=1)


def wilson_action_and_B(U: torch.Tensor, beta: float) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Wilson action S = beta * sum_p (1 - a_p), where plaquette quaternion is (a,v).
    Returns:
      S_per_chain: (B,)
      Bavg_per_chain: (B,) average plaquette defect
    """
    plaqs = plaquettes(U)  # (B,6,L^4,4)
    defect = 1.0 - plaqs[..., 0]  # (B,6,L^4)
    S = beta * defect.sum(dim=tuple(range(1, defect.ndim)))
    Bavg = defect.mean(dim=tuple(range(1, defect.ndim)))
    return S, Bavg


# -----------------------------
# Force: tangent projection + right trivialization
# -----------------------------
def tangent_project(U: torch.Tensor, G: torch.Tensor) -> torch.Tensor:
    # Project ambient R^4 gradient onto tangent of S^3 at U
    dot = (G * U).sum(dim=-1, keepdim=True)
    return G - dot * U


def right_trivialize(U: torch.Tensor, T: torch.Tensor) -> torch.Tensor:
    # T is tangent at U, return v in R^3 such that T = U * (0,v).
    # v = imag( U^{-1} * T ).
    W = su2_mul(su2_inv(U), T)
    return W[..., 1:]


@torch.no_grad()
def cartan_alignment_score(U: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    """
    Cheap "are links mostly in one U(1)?" score:
    - take imaginary parts v in R^3 for all links
    - form weighted covariance C = (sum v v^T) / (sum |v|^2)
    - if perfectly colinear => eigenvalues ~ (1,0,0)
    score = 1 - lambda_max, so score ~ 0 means Cartan-aligned
    """
    v = U[..., 1:]  # (B, ..., d, 3)
    B = v.shape[0]
    v_flat = v.reshape(B, -1, 3)
    num = torch.einsum("bni,bnj->bij", v_flat, v_flat)
    denom = v_flat.pow(2).sum(dim=(1, 2)).view(B, 1, 1).clamp_min(eps)
    C = num / denom
    evals = torch.linalg.eigvalsh(C)  # (B,3) ascending
    lam_max = evals[:, -1]
    return (1.0 - lam_max).contiguous()


def compute_force_norm_and_B(U: torch.Tensor, beta: float) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Returns:
      force_norm: (B,)  sqrt(sum_links |v_link|^2)
      Bavg:       (B,)
      v:          (B, L,L,L,L,d,3) right-trivialized gradient field (detached)
    """
    Ureq = U.detach().clone().requires_grad_(True)
    S, Bavg = wilson_action_and_B(Ureq, beta)
    G = torch.autograd.grad(S.sum(), Ureq, create_graph=False)[0]
    G_tan = tangent_project(Ureq, G)
    v = right_trivialize(Ureq, G_tan)  # (B, ..., d, 3)

    v2 = v.pow(2).sum(dim=-1)  # (B, ..., d)
    f2 = v2.sum(dim=tuple(range(1, v2.ndim)))  # (B,)
    force_norm = f2.sqrt()
    return force_norm.detach(), Bavg.detach(), v.detach()


def random_config(
    batch: int,
    L: int,
    d: int,
    mode: str,
    sigma: float,
    device: torch.device,
    dtype: torch.dtype,
) -> torch.Tensor:
    """
    mode:
      - 'haar'         : Haar-ish by normalizing N(0,1)^4
      - 'exp_gaussian' : near-identity by exp(sigma * N(0,1)^3)
    """
    if mode == "haar":
        q = torch.randn(batch, *([L] * d), d, 4, device=device, dtype=dtype)
        return su2_normalize(q)
    if mode == "exp_gaussian":
        v = sigma * torch.randn(batch, *([L] * d), d, 3, device=device, dtype=dtype)
        q = su2_exp(v)
        return su2_normalize(q)
    raise ValueError(f"Unknown init mode: {mode}")


# -----------------------------
# SGLD / Langevin step on SU(2)
# -----------------------------
def sgld_step(U: torch.Tensor, beta: float, dt: float) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    One stochastic quantization step:
      v = grad S right-trivialized
      U <- U * exp( -dt*v + sqrt(2dt)*noise )

    Returns:
      U_new, force_norm, Bavg, align_score
    """
    force_norm, Bavg, v = compute_force_norm_and_B(U, beta)
    noise = torch.randn_like(v)
    delta = (-dt) * v + math.sqrt(2.0 * dt) * noise
    dq = su2_exp(delta)
    U_new = su2_mul(U, dq)
    U_new = su2_normalize(U_new)

    align = cartan_alignment_score(U_new)
    return U_new.detach(), force_norm, Bavg, align


# -----------------------------
# Main experiments
# -----------------------------
@dataclass
class BestHit:
    force: float = float("inf")
    Bavg: float = float("nan")
    align: float = float("nan")
    batch_idx: int = -1
    chain_idx: int = -1


def run_hunt(args) -> None:
    device = torch.device(args.device)
    dtype = torch.float32 if args.dtype == "float32" else torch.float64

    print("\n=== COUNTEREXAMPLE HUNT ===")
    print(f"device={device} dtype={dtype} L={args.L} batch={args.batch} init={args.init} sigma={args.sigma}")
    print(f"Target filter: Bavg >= {args.eps} AND align_score >= {args.align_min} (i.e. NOT Cartan-ish)")
    print(f"Scanning {args.num_batches} fresh batches...")

    best = BestHit()
    t0 = time.time()

    for bi in range(args.num_batches):
        U = random_config(
            batch=args.batch, L=args.L, d=4,
            mode=args.init, sigma=args.sigma,
            device=device, dtype=dtype
        )

        force_norm, Bavg, _v = compute_force_norm_and_B(U, beta=args.beta)
        align = cartan_alignment_score(U)

        mask = (Bavg >= args.eps) & (align >= args.align_min)
        if mask.any():
            f_masked = force_norm.clone()
            f_masked[~mask] = float("inf")
            fmin, idx = torch.min(f_masked, dim=0)
            fmin_val = float(fmin.item())

            if fmin_val < best.force:
                best.force = fmin_val
                best.Bavg = float(Bavg[idx].item())
                best.align = float(align[idx].item())
                best.batch_idx = bi
                best.chain_idx = int(idx.item())

        if (bi + 1) % args.report_every == 0:
            elapsed = time.time() - t0
            print(
                f"[{bi+1:6d}/{args.num_batches}] "
                f"best_force={best.force:.6e} best_B={best.Bavg:.6f} best_align={best.align:.6f} "
                f"(batch={best.batch_idx}, chain={best.chain_idx}) "
                f"elapsed={elapsed:.1f}s"
            )

    print("\n=== HUNT DONE ===")
    print(f"BEST HIT: force={best.force:.6e} | Bavg={best.Bavg:.6f} | align={best.align:.6f} "
          f"(batch={best.batch_idx}, chain={best.chain_idx})")
    print("Interpretation:")
    print("- If best_force keeps dropping toward ~0 while align stays non-tiny, that's a serious red flag.")
    print("- If best_force bottoms out well above 0 (and only Cartan-ish align scores get tiny), that's evidence for 'rough ⇒ force bounded below'.")


def run_sgld(args) -> None:
    device = torch.device(args.device)
    dtype = torch.float32 if args.dtype == "float32" else torch.float64

    print("\n=== SGLD / STOCHASTIC QUANTIZATION ===")
    print(f"device={device} dtype={dtype} L={args.L} batch={args.batch} beta={args.beta} dt={args.dt}")
    print(f"Recording after burnin={args.burnin}, thinning every {args.thin} steps for {args.steps} steps total.")
    print(f"K^c proxy: Bavg > eps with eps={args.eps} (typicality proxy).")

    U = random_config(
        batch=args.batch, L=args.L, d=4,
        mode=args.init, sigma=args.sigma,
        device=device, dtype=dtype
    )

    Bs: List[np.ndarray] = []
    Fs: List[np.ndarray] = []
    As: List[np.ndarray] = []

    t0 = time.time()
    for t in range(args.steps):
        U, force_norm, Bavg, align = sgld_step(U, beta=args.beta, dt=args.dt)

        if t >= args.burnin and ((t - args.burnin) % args.thin == 0):
            Bs.append(Bavg.cpu().numpy())
            Fs.append(force_norm.cpu().numpy())
            As.append(align.cpu().numpy())

        if (t + 1) % args.report_every == 0:
            elapsed = time.time() - t0
            print(
                f"[{t+1:6d}/{args.steps}] "
                f"Bavg_mean={float(Bavg.mean()):.6f} Bavg_std={float(Bavg.std()):.6f} "
                f"force_mean={float(force_norm.mean()):.6f} "
                f"align_mean={float(align.mean()):.6f} "
                f"elapsed={elapsed:.1f}s"
            )

    B = np.concatenate(Bs, axis=0) if Bs else np.zeros((0,), dtype=np.float64)
    F = np.concatenate(Fs, axis=0) if Fs else np.zeros((0,), dtype=np.float64)
    A = np.concatenate(As, axis=0) if As else np.zeros((0,), dtype=np.float64)

    if B.size > 0:
        tail = float(np.mean(B > args.eps))
        cond = (B > args.eps) & (A > args.align_min)
        if np.any(cond):
            fmin = float(np.min(F[cond]))
        else:
            fmin = float("nan")
    else:
        tail, fmin = float("nan"), float("nan")

    print("\n=== SGLD DONE ===")
    print(f"Empirical tail P(Bavg > eps): {tail:.6e}")
    print(f"Min force among (Bavg>eps AND align>align_min): {fmin}")

    if args.out:
        np.savez(args.out, B=B, F=F, A=A, args=vars(args))
        print(f"Saved stats to: {args.out}")

    print("\nInterpretation:")
    print("- tail ≈ mu(K^c) proxy for a K defined by Bavg<=eps. (This is what appears in the localization error term.)")
    print("- If fmin is tiny for non-Cartan align, that suggests a real obstruction to coercivity-on-K^c.")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["hunt", "sgld"], default="hunt")

    p.add_argument("--L", type=int, default=16)
    p.add_argument("--batch", type=int, default=32)
    p.add_argument("--beta", type=float, default=8.0)

    p.add_argument("--init", choices=["haar", "exp_gaussian"], default="exp_gaussian")
    p.add_argument("--sigma", type=float, default=0.35)

    p.add_argument("--eps", type=float, default=0.08, help="roughness threshold for Bavg")
    p.add_argument("--align_min", type=float, default=0.15, help="exclude Cartan-ish if align_score < align_min")

    # Dynamically set default device based on CUDA availability
    default_device = "cuda" if torch.cuda.is_available() else "cpu"
    p.add_argument("--device", type=str, default=default_device)

    p.add_argument("--dtype", choices=["float32", "float64"], default="float32")

    p.add_argument("--num_batches", type=int, default=2000, help="hunt mode: number of fresh batches")

    p.add_argument("--dt", type=float, default=1e-4, help="sgld mode: step size")
    p.add_argument("--steps", type=int, default=2000, help="sgld mode: total steps")
    p.add_argument("--burnin", type=int, default=500, help="sgld mode: burn-in")
    p.add_argument("--thin", type=int, default=10, help="sgld mode: thinning")
    p.add_argument("--out", type=str, default="su2_a100_sgld_stats.npz")

    p.add_argument("--report_every", type=int, default=50)

    # parse_known_args avoids crashes in notebook-like environments
    args, unknown = p.parse_known_args()

    if args.device.startswith("cuda") and torch.cuda.is_available():
        # Prefer the new API when available, fall back to legacy flags
        try:
            torch.backends.cuda.matmul.fp32_precision = "tf32"
        except Exception:
            try:
                torch.backends.cuda.matmul.allow_tf32 = True
            except Exception:
                pass
        try:
            torch.backends.cudnn.conv.fp32_precision = "tf32"
        except Exception:
            try:
                torch.backends.cudnn.allow_tf32 = True
            except Exception:
                pass

    if args.mode == "hunt":
        run_hunt(args)
    else:
        run_sgld(args)


if __name__ == "__main__":
    main()
