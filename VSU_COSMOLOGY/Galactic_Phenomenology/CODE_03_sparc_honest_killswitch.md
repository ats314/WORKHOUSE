# CODE_03 — “Honest kill-switch” stress test (QDHT + spectral kernel, outlier reporting)

Generated: 2026-01-01 01:41:14 UTC

## Purpose

Implements an analysis driver that:

1. Loads SPARC Rotmod files from a local directory (`SPARC_WORK/Rotmod_LTG`).
2. Builds the baryonic acceleration proxy \(g_b\) from the component velocities.
3. Applies a **quasi-discrete Hankel transform** (QDHT) using Bessel zeros (order 0/1).
4. Applies a spectral multiplier
   \[
   M(k)=1+\left(\frac{\mu}{k}\right)^2,
   \]
   with a **global switch** for \(\mu\) based on the maximum baryonic acceleration in the galaxy.
5. Fits a per-galaxy amplitude \(A\) (log-space bounded minimization) and reports outliers by \(A\) and \(\chi^2/\mathrm{dof}\).
6. Produces an RAR comparison plot and saves it to disk.

## Notes on execution

- This script expects SPARC Rotmod files already present in `SPARC_WORK/Rotmod_LTG`.
- This environment does not contain the SPARC dataset; therefore the script is included verbatim but was **not executed here**.

## Dependencies

- `numpy`
- `scipy` (`scipy.special`, `scipy.optimize`, `scipy.interpolate`)
- `matplotlib`
- `dataclasses` (standard library, Python 3.7+)
- `pathlib` (standard library)

## Code

```python
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from pathlib import Path
from scipy.optimize import minimize_scalar
from scipy.special import j0, j1, jn_zeros
from scipy.interpolate import interp1d

# ----- Units & Constants -----
A0_SIMPLE = 3742.11  # (km/s)^2/kpc
A0_RAR    = 4072.53  # (km/s)^2/kpc
A0_SPECTRAL = 3700.0 # From your calibration
MU_MAX = 0.30        # From your calibration

# ----- QDHT ENGINE (The Missing Physics) -----
class QDHT:
    def __init__(self, n_points, r_max):
        self.N = n_points
        self.R = r_max
        self.alpha = jn_zeros(0, self.N + 1)
        self.alpha_N = self.alpha[-1]
        self.roots = self.alpha[:-1]
        self.r = self.roots * self.R / self.alpha_N
        self.k = self.roots / self.R
        self.j1_vals = np.abs(j1(self.roots))
        root_prod = np.outer(self.roots, self.roots)
        kernel = j0(root_prod / self.alpha_N)
        norm = 2.0 / self.alpha_N
        inv_j1_outer = 1.0 / np.outer(self.j1_vals, self.j1_vals)
        self.T = norm * kernel * inv_j1_outer

    def forward(self, f_r):
        v_in = f_r * self.j1_vals
        v_out = self.T @ v_in
        return v_out / self.j1_vals

    def inverse(self, f_k):
        return self.forward(f_k) # Symmetric

def predict_v2_spectral_A1(r_kpc, gbar_km2s2_per_kpc):
    """
    Predicts velocity^2 using the Spectral Rigidity model (A=1).
    """
    # 1. Setup Grid
    max_r = np.max(r_kpc) if r_kpc.size > 0 else 10.0
    dht = QDHT(n_points=512, r_max=max_r * 4.0)

    # 2. Interpolate gbar onto DHT grid
    # Assume gbar -> 0 at boundaries
    interp = interp1d(r_kpc, gbar_km2s2_per_kpc, kind='linear', bounds_error=False, fill_value=0.0)
    gb_dht = interp(dht.r)

    # 3. Determine Stiffness (Global Switch)
    max_g = np.max(gbar_km2s2_per_kpc) if gbar_km2s2_per_kpc.size > 0 else 0
    if max_g > A0_SPECTRAL:
        mu = 0.0
    else:
        mu = MU_MAX * (1.0 - max_g / A0_SPECTRAL)
        if mu < 0: mu = 0.0

    # 4. Transform
    G_k = dht.forward(gb_dht)
    M_k = 1.0 + (mu / dht.k)**2
    G_k_filtered = G_k * M_k
    g_dht_filtered = dht.inverse(G_k_filtered)

    # 5. Map back to r_kpc
    back_interp = interp1d(dht.r, g_dht_filtered, kind='linear', bounds_error=False, fill_value=0.0)
    g_final = back_interp(r_kpc)

    return np.maximum(r_kpc * g_final, 0.0)

# ----- Baseline Models -----
def mond_simple_gobs(gbar, a0=A0_SIMPLE):
    gbar = np.maximum(gbar, 0.0)
    return 0.5 * (gbar + np.sqrt(gbar*gbar + 4.0*a0*gbar))

def mond_rar_exp_gobs(gbar, a0=A0_RAR):
    gbar = np.maximum(gbar, 0.0)
    x = np.sqrt(np.maximum(gbar / max(a0, 1e-300), 0.0))
    denom = np.maximum(1.0 - np.exp(-x), 1e-12)
    return gbar / denom

def fit_A_for_v2(vobs, ev, v2_model_A1, A_bounds=(1e-3, 1e2)):
    v2_model_A1 = np.maximum(v2_model_A1, 0.0)
    def chi2_of_logA(logA):
        A = np.exp(logA)
        vmod = np.sqrt(np.maximum(A * v2_model_A1, 0.0))
        res = (vobs - vmod) / np.maximum(ev, 1e-6)
        return float(np.sum(res*res))
    lo, hi = np.log(A_bounds[0]), np.log(A_bounds[1])
    out = minimize_scalar(chi2_of_logA, bounds=(lo, hi), method="bounded")
    return float(np.exp(out.x)), float(out.fun) / max(int(vobs.size) - 1, 1)

@dataclass
class Rotmod:
    name: str; r: np.ndarray; vobs: np.ndarray; ev: np.ndarray
    vgas: np.ndarray; vdisk: np.ndarray; vbul: np.ndarray

def load_rotmod(path: Path) -> Rotmod:
    data = np.loadtxt(path)
    r, vobs, ev, vgas, vdisk, vbul = data.T[:6]
    return Rotmod(path.stem, r, vobs, ev, vgas, vdisk, vbul)

def baryon_v2(rm: Rotmod, ups_disk=0.5, ups_bul=0.5):
    return np.maximum(rm.vgas, 0)**2 + ups_disk*np.maximum(rm.vdisk, 0)**2 + ups_bul*np.maximum(rm.vbul, 0)**2

def stress_test(rotmod_dir: str, out_dir="stress_plots", A_cut=(0.4, 2.5), chi2_cut=25.0, topN=20):
    rotmod_dir = Path(rotmod_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    rows, gbar_all, gobs_all, gpred_all = [], [], [], []

    files = list(rotmod_dir.glob("*_rotmod.dat"))
    print(f"Found {{len(files)}} galaxies. Processing...")

    for f in files:
        try:
            rm = load_rotmod(f)
            if len(rm.r) < 3: continue

            v2bar = baryon_v2(rm)
            gbar = v2bar / np.maximum(rm.r, 1e-6)
            gobs = np.maximum(rm.vobs, 0.0)**2 / np.maximum(rm.r, 1e-6)

            # --- RUN SPECTRAL MODEL ---
            v2spec_A1 = predict_v2_spectral_A1(rm.r, gbar)

            # Fit A
            A_best, chi2dof = fit_A_for_v2(rm.vobs, rm.ev, v2spec_A1, A_bounds=(1e-3, 1e2))
            v2pred = A_best * np.maximum(v2spec_A1, 0.0)
            rms = float(np.sqrt(np.mean((rm.vobs - np.sqrt(np.maximum(v2pred, 0.0)))**2)))

            rows.append((rm.name, A_best, chi2dof, rms, float(np.max(gbar))))
            gbar_all.append(gbar); gobs_all.append(gobs); gpred_all.append(v2pred / np.maximum(rm.r, 1e-6))
        except Exception as e:
            print(f"Skipping {{f.name}}: {{e}}")

    # Rank outliers
    rows.sort(key=lambda x: x[2], reverse=True)
    outliers = [r for r in rows if (r[1] < A_cut[0] or r[1] > A_cut[1] or r[2] > chi2_cut)]

    print(f"\nEvaluated {{len(rows)}} galaxies.")
    print(f"Found {{len(outliers)}} outliers.\n")
    print(f"{{'Name':22s}} {{'A':6s}} {{'Chi2/dof':8s}} {{'RMS':7s}} {{'Max_g':9s}}")
    for name, A_best, chi2dof, rms, gmax in outliers[:min(topN, len(outliers))]:
        print(f"{{name:22s}} {{A_best:6.3f}} {{chi2dof:8.2f}} {{rms:7.2f}} {{gmax:9.1f}}")

    # Plot RAR
    gbar_all = np.concatenate(gbar_all)
    gobs_all = np.concatenate(gobs_all)
    gpred_all = np.concatenate(gpred_all)
    gx = np.geomspace(max(np.min(gbar_all[gbar_all>0]), 1e-2), np.max(gbar_all), 400)

    plt.figure(figsize=(8,6))
    plt.scatter(gbar_all, gobs_all, s=4, alpha=0.25, color='gray', label="Observed")
    plt.scatter(gbar_all, gpred_all, s=4, alpha=0.25, color='blue', label="Spectral Prediction")
    plt.plot(gx, gx, 'k--', label="Newtonian")
    plt.plot(gx, mond_simple_gobs(gx, A0_SIMPLE), 'r-', label=f"MOND Simple (a0={{A0_SIMPLE:.0f}})")
    plt.plot(gx, mond_rar_exp_gobs(gx, A0_RAR), 'g-.', label=f"RAR Exp (a0={{A0_RAR:.0f}})")

    plt.xscale("log"); plt.yscale("log")
    plt.xlabel(r"$g_{{\rm bar}}$"); plt.ylabel(r"$g_{{\rm obs}}$")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "RAR_comparison.png", dpi=150)
    print(f"\nSaved plot to {{out_dir}}/RAR_comparison.png")

if __name__ == "__main__":
    # Ensure this path matches your folder structure
    stress_test("SPARC_WORK/Rotmod_LTG", out_dir="stress_plots")
```
