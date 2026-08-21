# CODE_02 — SPARC global-fit driver with Hankel kernel switch (screen vs anti)

Generated: 2026-01-01 01:41:14 UTC

## Purpose

Implements a SPARC/Rotmod pipeline that:

1. Loads SPARC rotation-curve component files (gas/disk/bulge contributions).
2. Constructs a baryonic acceleration proxy
   \[
   g_b(r)=\frac{v_\text{gas}^2+v_\text{disk}^2+v_\text{bul}^2}{r}.
   \]
3. Applies an order-1 Hankel transform, multiplies by a selectable kernel in the Hankel channel, and inverts back to obtain a modified acceleration profile.
4. Performs a **single global** fit parameter search over \(\mu\) (bounded scalar minimization).
5. For each galaxy, solves a **per-galaxy amplitude** \(A\) by weighted least squares (clamped).

Kernel options implemented in the code:

- `KERNEL="screen"`:
  \[
  M(k)=\frac{k^2}{k^2+\mu^2}
  \]
- `KERNEL="anti"`:
  \[
  M(k)=\frac{k^2+\mu^2}{k^2}
  \]
  (IR pole handled by the finite \(k_\min\) of the grid).

## Notes on execution

- The script is written to download SPARC Rotmod_LTG from Zenodo (`records/16284118`). Running it requires network access.
- This environment does not have network access; therefore the script is included verbatim but was **not executed here**.

## Dependencies

- `numpy`
- `scipy` (`scipy.special`, `scipy.optimize`)
- Standard library (`urllib`, `zipfile`, `os`, `re`, `shutil`)

## Code

```python
#!/usr/bin/env python3
# sparc_rigidity_HANKEL_KERNEL_SWITCH.py
#
# ONE global fit parameter: mu.
# Optional kernel choice:
#   KERNEL="screen" -> k^2/(k^2+mu^2)   (your current; provably suppresses outer curves)
#   KERNEL="anti"   -> (k^2+mu^2)/k^2   (IR-enhanced; capable of flat outer curves)

import os, zipfile, shutil, re
import numpy as np
from scipy.special import j1
from scipy.optimize import minimize_scalar

ZENODO_REC = "16284118"
BASE = f"https://zenodo.org/records/{{ZENODO_REC}}/files"
URL_ROTMOD = f"{{BASE}}/Rotmod_LTG.zip?download=1"

WORKDIR = "SPARC_WORK"
Z1 = os.path.join(WORKDIR, "Rotmod_LTG.zip")
ROTMOD_DIR = os.path.join(WORKDIR, "Rotmod_LTG")

# ---- knobs (NOT fit params) ----
NK = 512
KMAX_FACTOR = 6.0
KMAX_ABS = 400.0        # hard cap, prevents pathological dr_min explosions
KMIN_FACTOR = 0.5       # kmin ≈ KMIN_FACTOR / r_max  (important for anti kernel)
USE_TAPER = True
KC_FACTOR = 1.0         # kc = KC_FACTOR * π/dr_eff
TAPER_P = 4.0

SIGMA_FLOOR = 5.0       # km/s modeling/systematic floor
A_CLAMP = (0.05, 50.0)  # widen if using anti kernel
MU_BOUNDS = (1e-3, 2.0)

KERNEL = "anti"         # "screen" or "anti"

def download(url, out_path, chunk=1 << 20):
    import urllib.request
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with urllib.request.urlopen(url) as r, open(out_path, "wb") as f:
        while True:
            b = r.read(chunk)
            if not b:
                break
            f.write(b)

def unzip(zip_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(out_dir)

def read_table(path):
    rows = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            parts = re.split(r"[,\s]+", s)
            try:
                vals = [float(x) for x in parts if x != ""]
            except Exception:
                continue
            if len(vals) >= 3:
                rows.append(vals)
    if not rows:
        return None
    w = min(len(r) for r in rows)
    return np.array([r[:w] for r in rows], dtype=np.float64)

def stem(path):
    return os.path.splitext(os.path.basename(path))[0].strip()

def load_rotmod_components(path):
    a = read_table(path)
    if a is None or a.shape[1] < 5:
        raise RuntimeError("rotmod missing components")
    r = a[:, 0]
    vobs = a[:, 1]
    dv = np.maximum(a[:, 2], 1e-3)
    vgas = a[:, 3]
    vdisk = a[:, 4]
    vbul = a[:, 5] if a.shape[1] >= 6 else np.zeros_like(r)

    m = (
        np.isfinite(r) & np.isfinite(vobs) & np.isfinite(dv) &
        np.isfinite(vgas) & np.isfinite(vdisk) & np.isfinite(vbul) &
        (r > 0)
    )
    r, vobs, dv, vgas, vdisk, vbul = r[m], vobs[m], dv[m], vgas[m], vdisk[m], vbul[m]
    if r.size < 8:
        raise RuntimeError("too few points")

    idx = np.argsort(r)
    r, vobs, dv, vgas, vdisk, vbul = r[idx], vobs[idx], dv[idx], vgas[idx], vdisk[idx], vbul[idx]
    keep = np.ones_like(r, dtype=bool)
    keep[1:] = r[1:] > r[:-1]
    r, vobs, dv, vgas, vdisk, vbul = r[keep], vobs[keep], dv[keep], vgas[keep], vdisk[keep], vbul[keep]
    if r.size < 8:
        raise RuntimeError("too few points after dedupe")
    return r, vobs, dv, vgas, vdisk, vbul

def build_k_grid(r):
    dr = np.diff(r)
    dr_pos = dr[dr > 0]
    dr_eff = float(np.quantile(dr_pos, 0.25))  # robust vs tiny dr_min
    rmax = float(np.max(r))

    kmin = max(1e-4, KMIN_FACTOR / max(rmax, 1e-6))
    kmax = KMAX_FACTOR * np.pi / max(dr_eff, 1e-6)
    kmax = min(kmax, KMAX_ABS)

    k = np.logspace(np.log10(kmin), np.log10(kmax), NK).astype(np.float64)
    wk = np.gradient(k)

    if USE_TAPER:
        kc = KC_FACTOR * np.pi / max(dr_eff, 1e-6)
        W = np.exp(- (k / kc) ** TAPER_P)
    else:
        W = np.ones_like(k)

    return k, wk, W

# Hankel-1 pair:
#   F(k) = ∫ dr r f(r) J1(kr)
#   f(r) = ∫ dk k F(k) J1(kr)
def hankel1_forward(f_r, r, k, wr):
    J = j1(np.outer(k, r))
    return (J * (r * f_r * wr)[None, :]).sum(axis=1)

def hankel1_inverse(F_k, k, wk, r):
    J = j1(np.outer(k, r))
    return ((k * F_k * wk)[:, None] * J).sum(axis=0)

def kernel_M(k, mu):
    k2 = k * k
    mu2 = mu * mu
    if KERNEL == "screen":
        return k2 / (k2 + mu2)
    elif KERNEL == "anti":
        return (k2 + mu2) / np.maximum(k2, 1e-30)  # IR pole regularized by kmin anyway
    else:
        raise ValueError("KERNEL must be 'screen' or 'anti'")

def predict_gmu_from_gb(r, gb, mu, k, wk, W):
    wr = np.gradient(r)
    Gb = hankel1_forward(gb, r, k, wr)
    M = kernel_M(k, mu)
    gmu = hankel1_inverse(Gb * M * W, k, wk, r)
    # No hard positivity clamp here; let the fit reveal if ringing is killing you.
    return gmu

def best_A_weighted(vobs, vmu, dv):
    dv_eff = np.sqrt(dv * dv + SIGMA_FLOOR * SIGMA_FLOOR)
    w = 1.0 / np.maximum(dv_eff * dv_eff, 1e-12)
    num = float(np.sum(w * vmu * vobs))
    den = float(np.sum(w * vmu * vmu))
    if den <= 0 or not np.isfinite(den):
        return A_CLAMP[0]
    s = num / den
    s = float(np.clip(s, np.sqrt(A_CLAMP[0]), np.sqrt(A_CLAMP[1])))
    return s * s

def chi2_global(mu, dataset, cache):
    total = 0.0
    for name, r, vobs, dv, gb in dataset:
        k, wk, W = cache[name]["k"], cache[name]["wk"], cache[name]["W"]
        gmu = predict_gmu_from_gb(r, gb, mu, k, wk, W)
        v2 = np.maximum(r * gmu, 0.0)
        vmu = np.sqrt(v2)
        A = best_A_weighted(vobs, vmu, dv)
        vpred = np.sqrt(np.maximum(A * v2, 0.0))
        dv_eff = np.sqrt(dv * dv + SIGMA_FLOOR * SIGMA_FLOOR)
        total += float(np.sum(((vobs - vpred) / dv_eff) ** 2))
    return total

def main():
    os.makedirs(WORKDIR, exist_ok=True)
    if not os.path.exists(Z1):
        print(f"[download] {{URL_ROTMOD}}", flush=True)
        download(URL_ROTMOD, Z1)

    if os.path.exists(ROTMOD_DIR):
        shutil.rmtree(ROTMOD_DIR)
    unzip(Z1, ROTMOD_DIR)

    rc_files = []
    for root, _, fns in os.walk(ROTMOD_DIR):
        for fn in fns:
            if fn.lower().endswith((".dat", ".txt", ".csv", ".mrt")) and "rotmod" in fn.lower():
                rc_files.append(os.path.join(root, fn))
    rc_files.sort()
    print(f"FOUND {{len(rc_files)}} RC FILES", flush=True)

    dataset = []
    skipped = 0
    for f in rc_files:
        try:
            r, vobs, dv, vgas, vdisk, vbul = load_rotmod_components(f)
            gb = (vgas * vgas + vdisk * vdisk + vbul * vbul) / r
            dataset.append((stem(f), r, vobs, dv, gb))
        except Exception:
            skipped += 1

    print(f"USING {{len(dataset)}} GALAXIES", flush=True)
    print(f"SKIPPED {{skipped}}", flush=True)
    if len(dataset) < 20:
        print("Too few galaxies. Abort.", flush=True)
        return

    cache = {{}}
    for name, r, vobs, dv, gb in dataset:
        k, wk, W = build_k_grid(r)
        cache[name] = {{"k": k, "wk": wk, "W": W}}

    res = minimize_scalar(
        lambda mu: chi2_global(mu, dataset, cache),
        bounds=MU_BOUNDS,
        method="bounded",
        options=dict(xatol=1e-6, maxiter=300)
    )
    mu_star = float(res.x)
    print("\n=== GLOBAL FIT ===", flush=True)
    print(f"KERNEL = {{KERNEL}}", flush=True)
    print(f"mu* = {{mu_star:.6g}}  [kpc^-1]   ell = {{1.0/mu_star:.6g}} kpc", flush=True)

    chi2dofs, rmses, As = [], [], []

    print("\n=== PER-GALAXY @ mu* ===", flush=True)
    for name, r, vobs, dv, gb in dataset:
        k, wk, W = cache[name]["k"], cache[name]["wk"], cache[name]["W"]
        gmu = predict_gmu_from_gb(r, gb, mu_star, k, wk, W)
        v2 = np.maximum(r * gmu, 0.0)
        vmu = np.sqrt(v2)
        A = best_A_weighted(vobs, vmu, dv)
        vpred = np.sqrt(np.maximum(A * v2, 0.0))

        dv_eff = np.sqrt(dv * dv + SIGMA_FLOOR * SIGMA_FLOOR)
        c2 = float(np.sum(((vobs - vpred) / dv_eff) ** 2))
        dof = max(1, int(r.size - 1))
        rms = float(np.sqrt(np.mean((vobs - vpred) ** 2)))

        chi2dofs.append(c2 / dof)
        rmses.append(rms)
        As.append(A)

        print(f"{{name:18s}}  chi2/dof={{c2/dof:10.3f}}  rms={{rms:7.2f}} km/s  A={{A:7.3f}}", flush=True)

    chi2dofs = np.array(chi2dofs)
    rmses = np.array(rmses)
    As = np.array(As)

    print("\n=== SUMMARY ===", flush=True)
    print(f"median chi2/dof = {{np.median(chi2dofs):.6g}}", flush=True)
    print(f"p90 chi2/dof    = {{np.quantile(chi2dofs,0.90):.6g}}", flush=True)
    print(f"median rms      = {{np.median(rmses):.6g}} km/s", flush=True)
    print(f"p90 rms         = {{np.quantile(rmses,0.90):.6g}} km/s", flush=True)
    print(f"A median        = {{np.median(As):.6g}}", flush=True)
    print(f"A p90           = {{np.quantile(As,0.90):.6g}}", flush=True)

if __name__ == "__main__":
    main()
```
