#!/usr/bin/env python3
"""
SPECTRAL UNIT TEST (A100-friendly, physics-correct normalization)

Model: real vector field A_mu(x) with Langevin dynamics
  dA = -((m^2 + alpha p̂^2)A + lambda A^3) dt + sqrt(2) dW

This is NOT gauge theory. It is a spectral sanity sandbox.

What it does:
  - For lambda=0: verifies measured G(k)=<|A(k)|^2> matches 1/(m^2+alpha p̂^2)
  - For lambda>0: fits low-momentum inverse propagator to m_R^2 + Z p̂^2

Key: uses FFT norm="ortho" to remove volume scaling artifacts.
"""

import math
import time
import torch
import torch.fft as fft


def radial_bin(xvals: torch.Tensor, yvals: torch.Tensor, nbins: int = 80):
    """Bin y by x, return (x_mid, y_mean)."""
    x = xvals.flatten()
    y = yvals.flatten()
    x_max = float(x.max().item())
    bins = torch.linspace(0.0, x_max, nbins + 1, device=x.device, dtype=x.dtype)
    idx = torch.bucketize(x, bins) - 1
    idx = torch.clamp(idx, 0, nbins - 1)
    y_sum = torch.zeros(nbins, device=x.device, dtype=y.dtype)
    y_cnt = torch.zeros(nbins, device=x.device, dtype=y.dtype)
    y_sum.scatter_add_(0, idx, y)
    y_cnt.scatter_add_(0, idx, torch.ones_like(y))
    y_mean = y_sum / y_cnt.clamp_min(1.0)
    x_mid = 0.5 * (bins[:-1] + bins[1:])
    return x_mid, y_mean


def fit_low_p2(ph2: torch.Tensor, Gk: torch.Tensor, p2_max: float = 1.5):
    """Fit inv(G) = m_R^2 + Z p̂^2 on low p̂^2 region."""
    invG = 1.0 / Gk
    mask = (ph2 <= p2_max).flatten()
    x = ph2.flatten()[mask].double()
    y = invG.flatten()[mask].double()
    X = torch.stack([torch.ones_like(x), x], dim=1)
    beta_hat = torch.linalg.lstsq(X, y).solution
    mR2 = float(beta_hat[0].item())
    Z = float(beta_hat[1].item())
    return mR2, Z


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float32

    L = 64
    d = 4
    m2 = 0.3
    alpha = 1.0

    dt = 0.01
    steps = 1200
    burn = 300
    thin = 10

    batch = 4
    lambda_list = [0.0, 0.5, 1.0]

    print(f"device={device} L={L} d={d} batch={batch} dtype={dtype}")
    print(f"m2={m2} alpha={alpha} dt={dt} steps={steps} burn={burn} thin={thin}")

    # Build lattice momentum symbol p̂^2 (4D)
    k1 = 2.0 * math.pi * fft.fftfreq(L, d=1.0, device=device, dtype=dtype)
    grid = torch.meshgrid([k1] * d, indexing="ij")
    phat2 = sum((2.0 * torch.sin(ki / 2.0)) ** 2 for ki in grid)  # p̂^2
    Mdiag = (m2 + alpha * phat2).to(dtype=dtype)  # (L,L,L,L)

    # Exact free propagator target
    G_free_exact = (1.0 / Mdiag).to(dtype=dtype)

    for lam in lambda_list:
        print(f"\n=== lambda={lam} ===")
        A = 0.05 * torch.randn((batch, d, L, L, L, L), device=device, dtype=dtype)

        Gk_acc = torch.zeros((L, L, L, L), device=device, dtype=torch.float64)
        meas = 0

        torch.cuda.synchronize() if device == "cuda" else None
        t0 = time.time()

        for t in range(steps):
            Ahat = fft.fftn(A, dim=(2, 3, 4, 5), norm="ortho")

            # linear force via spectral multiplier
            Force_lin_hat = Ahat * Mdiag.unsqueeze(0).unsqueeze(0)
            Force_lin = fft.ifftn(Force_lin_hat, dim=(2, 3, 4, 5), norm="ortho").real

            Force_int = lam * (A ** 3)

            noise = torch.randn_like(A)
            A = A - dt * (Force_lin + Force_int) + math.sqrt(2.0 * dt) * noise

            if t >= burn and (t - burn) % thin == 0:
                Ahat2 = fft.fftn(A, dim=(2, 3, 4, 5), norm="ortho")
                power = torch.sum(torch.abs(Ahat2) ** 2, dim=1)  # (batch,L,L,L,L)
                Gk_acc += power.double().mean(dim=0)
                meas += 1

        torch.cuda.synchronize() if device == "cuda" else None
        print(f"measures={meas} elapsed={time.time() - t0:.2f}s")

        Gk = (Gk_acc / max(meas, 1)).to(dtype=dtype)

        if lam == 0.0:
            rel = torch.abs(Gk - G_free_exact) / torch.abs(G_free_exact)
            rel_med = float(torch.median(rel).item())
            rel_95 = float(torch.quantile(rel.flatten(), 0.95).item())
            rel_max = float(torch.max(rel).item())
            print(f"FREE CHECK: median rel.err={rel_med:.3e} | 95%={rel_95:.3e} | max={rel_max:.3e}")

        mR2, Z = fit_low_p2(phat2, Gk, p2_max=1.5)
        print(f"LOW-k FIT: m_R^2≈{mR2:.6f} | Z≈{Z:.6f}")

        xmid, ymean = radial_bin(phat2, 1.0 / Gk, nbins=60)
        first = [(float(xmid[i].item()), float(ymean[i].item())) for i in range(6)]
        print("BINS (p̂^2, <G^{-1}>):", first)


if __name__ == "__main__":
    main()
