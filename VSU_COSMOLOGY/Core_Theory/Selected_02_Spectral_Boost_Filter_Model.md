# Spectral Boost Filter Model (Hankel / QDHT) — Definition, Asymptotics, and Global $\mu$ Fits

This document extracts the *spectral* (Fourier/Bessel) version of “vacuum stiffness”: instead of an acceleration-space interpolation $g(g_{\rm bar})$, one modifies the **response** of the gravitational field in radial wavenumber $k$.

The project implements this using Hankel transforms (order 1) for axisymmetric disks.

---

## 1. Core idea: modify the Poisson response in $k$-space

For an axisymmetric thin disk, one can represent the Newtonian radial field as a Hankel integral

\[
g_N(r) \;=\; 2\pi G \int_0^\infty dk\; J_1(kr)\,\widehat{\Sigma}(k),
\]

with inverse

\[
\widehat{\Sigma}(k)\;=\;\frac{1}{2\pi G}\int_0^\infty dr\; r\, g_N(r)\,J_1(kr).
\]

The spectral-boost model applies a multiplicative modifier $M(k)$:

\[
\widehat{g}_{\mu}(k)\;=\;M(k;\mu)\,\widehat{g}_{N}(k),
\qquad
g_\mu(r)=\int_0^\infty dk\; J_1(kr)\,\widehat{g}_\mu(k).
\]

This is a **linear** modification (in $g$), but **nonlocal** in real space.

---

## 2. The “sharpened boost” transfer function (the project’s $n=4$ choice)

A specific family used in the project is:

\[
M(k;\mu,n)=\left(1+\left(\frac{\mu}{k}\right)^n\right)^{1/n}.
\]

The “sharpened boost” run uses $n=4$:

\[
M(k;\mu)=\left(1+\left(\frac{\mu}{k}\right)^4\right)^{1/4}.
\]

### 2.1 Asymptotics

- UV / small scales ($k\gg \mu$):  
  \[
  M(k)\to 1,
  \]
  recovering Newtonian gravity.

- IR / large scales ($k\ll \mu$):  
  \[
  M(k)\sim \frac{\mu}{k}.
  \]

That IR behavior is the whole magic trick: multiplying by $1/k$ in $k$-space corresponds to a slower falloff in real space (heuristically: pushing you from a $1/r^2$-type scaling toward a $1/r$-type scaling in the far field).

---

## 3. What the global-$\mu$ SPARC fits actually reported

Two global fits appear in the archive. They are not the same problem (they enforce different constraints), and they land on radically different $\mu$.

### 3.1 Global $\mu$ (no “fixed mass constraint”)

Printed result:

- Uses 143 galaxies.
- Best-fit:
  \[
  \mu_* = 1.67038\;{\rm kpc}^{-1},
  \qquad
  \ell_*=\mu_*^{-1}\approx 0.60\;{\rm kpc}.
  \]

### 3.2 Global $\mu$ with “Fixed Mass Constraint”

Printed result:

\[
\mu_* = 1.00634\times 10^{-4}\;{\rm kpc}^{-1},
\qquad
\ell_* \approx 9.94\times 10^3\;{\rm kpc}.
\]

That scale is cosmologically huge, and the per-galaxy diagnostics show the fit struggling (several galaxies saturating the allowed baryonic scaling, enormous $\chi^2/{\rm dof}$ for some cases).

**Interpretation (engineering view):** this model family has a degeneracy between (i) per-galaxy amplitude freedom ($A_{\rm gal}$) and (ii) where you put the “turn-on” scale $\ell=1/\mu$. If the amplitude can soak up mismatch, the optimizer can push $\mu$ to extremes.

---

## 4. Minimal “reference implementation” for the spectral boost

The archive uses a quasi-discrete Hankel transform (QDHT) pipeline. The core steps are:

1. Build $g_N(r)$ from SPARC components.
2. Hankel transform to $\widehat{g}_N(k)$.
3. Multiply by $M(k;\mu)$.
4. Inverse Hankel transform to $g_\mu(r)$.
5. Predict $V(r)=\sqrt{r\,g_\mu(r)}$ and compute $\chi^2$.

Pseudocode:

```python
# given arrays r, gN(r)
k, gN_hat = hankel1_forward(r, gN)

M = (1.0 + (mu / np.maximum(k, kmin))**4)**0.25
gmu_hat = gN_hat * M

gmu = hankel1_inverse(k, gmu_hat, r)
Vmu = np.sqrt(r * gmu)
```

---

## 5. Why this is interesting (and how it could become a *theory*)

This spectral model is *not* just “another MOND curve fit.” It is:

- linear in the field (so superposition is preserved),
- explicitly nonlocal (real-space kernel),
- naturally phrased as an operator deformation of Poisson:
  \[
  g = \mathcal{M}(\sqrt{-\nabla^2})\,g_N,
  \]
  which suggests an effective action with a nonlocal term or a scale-dependent $G_{\rm eff}(k)$.

If you want this to be publishable, the next derivation target is:

- write the equivalent **real-space kernel** $K_\mu(r,r')$,
- prove **positivity / stability** (no negative-energy or acausal modes) once embedded relativistically,
- show which choice of $M(k)$ reproduces the observed RAR without killing CMB/BAO.

---

## Appendix A. Printed excerpt (selected lines)

The run output includes:

- “FOUND 175 RC FILES”  
- “USING 143 GALAXIES”  
- “Optimizing mu (Global)...”  
- “mu* = 1.67038 kpc^-1 / Scale ~ 0.60 kpc”  
- and, under fixed-mass constraint, “mu* = 0.000100634 kpc^-1 / Scale ~ 9936.96 kpc”.

(See the archive outputs for the full per-galaxy table.)



## Appendix B. Global \mu fit with fixed mass constraint (as captured in GALAXYRUN.ipynb cell 20)

```python
#!/usr/bin/env python3
# sparc_rigidity_FIXED_MASS.py
#
# OBJECTIVE:
#   Fit the "Boost" model (M(k) = sqrt(1 + (mu/k)^2))
#   BUT constrain A_gal to [0.5, 2.0].
#   This prevents the model from "cheating" by suppressing baryon mass.
#
# EXPECTATION:
#   The solver should find a smaller mu (larger length scale),
#   pushing the boost transition further out to the galaxy edge.

import os, zipfile, shutil, re
import numpy as np
from scipy.special import j1
from scipy.optimize import minimize_scalar

ZENODO_REC = "16284118"
BASE = f"https://zenodo.org/records/{ZENODO_REC}/files"
URL_ROTMOD = f"{BASE}/Rotmod_LTG.zip?download=1"

WORKDIR = "SPARC_WORK"
Z1 = os.path.join(WORKDIR, "Rotmod_LTG.zip")
ROTMOD_DIR = os.path.join(WORKDIR, "Rotmod_LTG")

# ---- knobs ----
NK = 512
KMAX_FACTOR = 6.0
KMIN = 1e-4

# Spectral taper
USE_TAPER = True
KC_FACTOR = 1.0
TAPER_P = 4.0

TOP_Q = 0.30

# --- CRITICAL CHANGE: MASS CONSTRAINT ---
# We force the amplitude A to be physically realistic.
# 1.0 means perfect agreement with photometric mass.
# 0.5 - 2.0 allows for standard Mass-to-Light ratio uncertainty.
A_CLAMP = (0.5, 2.0)

MU_BOUNDS = (1e-4, 5.0)

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

    # Filter bad points
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

    # Deduplicate r
    keep = np.ones_like(r, dtype=bool)
    keep[1:] = r[1:] > r[:-1] + 1e-5
    r, vobs, dv, vgas, vdisk, vbul = r[keep], vobs[keep], dv[keep], vgas[keep], vdisk[keep], vbul[keep]

    if r.size < 8:
        raise RuntimeError("too few points after dedupe")
    return r, vobs, dv, vgas, vdisk, vbul

def build_k_grid(r):
    dr = np.diff(r)
    dr_min = float(np.min(dr[dr > 0]))
    kmax = KMAX_FACTOR * np.pi / max(dr_min, 1e-6)
    k = np.logspace(np.log10(KMIN), np.log10(kmax), NK).astype(np.float64)
    wk = np.gradient(k)
    if USE_TAPER:
        kc = KC_FACTOR * np.pi / max(dr_min, 1e-6)
        W = np.exp(- (k / kc) ** TAPER_P)
    else:
        W = np.ones_like(k)
    return k, wk, W

def compute_A_gal(vobs, v2_mu, gb):
    mask = v2_mu > 1e-12
    if not np.any(mask):
        return 1.0

    ratios = (vobs[mask] ** 2) / v2_mu[mask]

    # Use median of top-Q strongly predicted points to avoid noise
    n = ratios.size
    q = max(3, int(np.ceil(TOP_Q * n)))
    idx = np.argsort(v2_mu[mask])[-q:] # Points where force is strongest

    A = float(np.median(ratios[idx]))

    # --- CLAMPING ---
    return float(np.clip(A, *A_CLAMP))

def hankel1_forward(gb, r, k, wr):
    J = j1(np.outer(k, r))
    return (J * (r * gb * wr)[None, :]).sum(axis=1)

def hankel1_inverse(Gb, k, wk, r):
    J = j1(np.outer(k, r))
    return ((k * Gb * wk)[:, None] * J).sum(axis=0)

def predict_gmu_from_gb(r, gb, mu, k, wk, W):
    wr = np.gradient(r)
    Gb = hankel1_forward(gb, r, k, wr)

    # Low-Pass Boost
    M = np.sqrt(1.0 + (mu / k)**2)

    Gb_f = Gb * M * W
    gmu = hankel1_inverse(Gb_f, k, wk, r)
    return np.maximum(gmu, 0.0)

def chi2_global(mu, dataset, cache):
    total = 0.0
    for name, r, vobs, dv, gb in dataset:
        k, wk, W = cache[name]["k"], cache[name]["wk"], cache[name]["W"]
        gmu = predict_gmu_from_gb(r, gb, mu, k, wk, W)
        v2 = np.maximum(r * gmu, 0.0)

        # This will now return A clamped between 0.5 and 2.0
        A = compute_A_gal(vobs, v2, gb)

        vpred = np.sqrt(np.maximum(A * v2, 0.0))
        total += float(np.sum(((vobs - vpred) / dv) ** 2))
    return total

def main():
    os.makedirs(WORKDIR, exist_ok=True)
    if not os.path.exists(Z1):
        print(f"[download] {URL_ROTMOD}", flush=True)
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
    print(f"FOUND {len(rc_files)} RC FILES", flush=True)

    dataset = []
    skipped = 0
    for f in rc_files:
        try:
            r, vobs, dv, vgas, vdisk, vbul = load_rotmod_components(f)
            gb = (vgas * vgas + vdisk * vdisk + vbul * vbul) / r
            dataset.append((stem(f), r, vobs, dv, gb))
        except Exception:
            skipped += 1

    print(f"USING {len(dataset)} GALAXIES", flush=True)
    if len(dataset) < 20:
        print("Too few galaxies. Abort.", flush=True)
        return

    cache = {}
    for name, r, vobs, dv, gb in dataset:
        k, wk, W = build_k_grid(r)
        cache[name] = {"k": k, "wk": wk, "W": W}

    print("Optimizing mu (Global, Fixed Mass Constraint)...", flush=True)
    res = minimize_scalar(
        lambda mu: chi2_global(mu, dataset, cache),
        bounds=MU_BOUNDS,
        method="bounded",
        options=dict(xatol=1e-6, maxiter=300)
    )
    mu_star = float(res.x)
    print(f"\n=== GLOBAL FIT RESULT ===", flush=True)
    print(f"mu* = {mu_star:.6g} kpc^-1", flush=True)
    print(f"Scale ~ {1.0/mu_star:.2f} kpc", flush=True)

    chi2dofs, rmses, As = [], [], []

    print("\n=== PER-GALAXY PERFORMANCE ===", flush=True)
    print(f"{'Galaxy':18s} {'Chi2/dof':>10s} {'RMS':>10s} {'A_gal':>8s}")

    for name, r, vobs, dv, gb in dataset:
        k, wk, W = cache[name]["k"], cache[name]["wk"], cache[name]["W"]
        gmu = predict_gmu_from_gb(r, gb, mu_star, k, wk, W)
        v2 = np.maximum(r * gmu, 0.0)
        A = compute_A_gal(vobs, v2, gb)
        vpred = np.sqrt(np.maximum(A * v2, 0.0))

        c2 = float(np.sum(((vobs - vpred) / dv) ** 2))
        dof = max(1, int(r.size - 1))
        rms = float(np.sqrt(np.mean((vobs - vpred) ** 2)))

        chi2dofs.append(c2 / dof)
        rmses.append(rms)
        As.append(A)

        print(f"{name:18s} {c2/dof:10.3f} {rms:10.2f} {A:8.3f}", flush=True)

    chi2dofs = np.array(chi2dofs)
    rmses = np.array(rmses)
    As = np.array(As)

    print("\n=== STATS SUMMARY ===", flush=True)
    print(f"Median Chi2/dof : {np.median(chi2dofs):.4f}")
    print(f"Median RMS      : {np.median(rmses):.4f} km/s")
    print(f"Median A_gal    : {np.median(As):.4f}")
    print(f"StdDev A_gal    : {np.std(As):.4f}")

if __name__ == "__main__":
    main()
```


## Appendix C. Sharpened boost (n=4) global \mu fit (as captured in GALAXYRUN.ipynb cell 22)

```python
#!/usr/bin/env python3
# sparc_rigidity_SHARP_BOOST.py
#
# FIX: Implements a "Sharpened" transfer function (Power n=4).
#      M(k) = (1 + (mu/k)^4)^(1/4)
#
# RATIONALE:
#   The previous n=2 filter turned on too early, forcing the solver to either
#   shrink the mass (A=0.1) or turn off the boost (mu=0).
#   This n=4 filter "protects" the inner Newtonian disk while still
#   delivering the 1/k boost needed for flat rotation curves at the edge.

import os, zipfile, shutil, re
import numpy as np
from scipy.special import j1
from scipy.optimize import minimize_scalar

ZENODO_REC = "16284118"
BASE = f"https://zenodo.org/records/{ZENODO_REC}/files"
URL_ROTMOD = f"{BASE}/Rotmod_LTG.zip?download=1"

WORKDIR = "SPARC_WORK"
Z1 = os.path.join(WORKDIR, "Rotmod_LTG.zip")
ROTMOD_DIR = os.path.join(WORKDIR, "Rotmod_LTG")

# ---- knobs ----
NK = 512
KMAX_FACTOR = 6.0
KMIN = 1e-4

# Spectral taper
USE_TAPER = True
KC_FACTOR = 1.0
TAPER_P = 4.0

TOP_Q = 0.30

# CONSTRAINT: We expect A to be near 1.0 (Real Mass)
# We relax slightly to 0.4-3.0 to allow for M/L uncertainty,
# but prevent the A=0.09 cheating.
A_CLAMP = (0.4, 3.0)

MU_BOUNDS = (1e-4, 5.0)

def download(url, out_path, chunk=1 << 20):
    import urllib.request
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with urllib.request.urlopen(url) as r, open(out_path, "wb") as f:
        while True:
            b = r.read(chunk)
            if not b: break
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
            if not s or s.startswith("#"): continue
            parts = re.split(r"[,\s]+", s)
            try: vals = [float(x) for x in parts if x != ""]
            except: continue
            if len(vals) >= 3: rows.append(vals)
    if not rows: return None
    w = min(len(r) for r in rows)
    return np.array([r[:w] for r in rows], dtype=np.float64)

def stem(path):
    return os.path.splitext(os.path.basename(path))[0].strip()

def load_rotmod_components(path):
    a = read_table(path)
    if a is None or a.shape[1] < 5: raise RuntimeError("rotmod missing components")
    r = a[:, 0]; vobs = a[:, 1]; dv = np.maximum(a[:, 2], 1e-3)
    vgas = a[:, 3]; vdisk = a[:, 4]; vbul = a[:, 5] if a.shape[1] >= 6 else np.zeros_like(r)

    m = (np.isfinite(r) & np.isfinite(vobs) & (r > 0))
    r, vobs, dv, vgas, vdisk, vbul = r[m], vobs[m], dv[m], vgas[m], vdisk[m], vbul[m]
    if r.size < 8: raise RuntimeError("too few points")

    idx = np.argsort(r)
    r, vobs, dv, vgas, vdisk, vbul = r[idx], vobs[idx], dv[idx], vgas[idx], vdisk[idx], vbul[idx]
    keep = np.ones_like(r, dtype=bool)
    keep[1:] = r[1:] > r[:-1] + 1e-5
    r, vobs, dv, vgas, vdisk, vbul = r[keep], vobs[keep], dv[keep], vgas[keep], vdisk[keep], vbul[keep]
    if r.size < 8: raise RuntimeError("too few points after dedupe")
    return r, vobs, dv, vgas, vdisk, vbul

def build_k_grid(r):
    dr = np.diff(r)
    dr_min = float(np.min(dr[dr > 0]))
    kmax = KMAX_FACTOR * np.pi / max(dr_min, 1e-6)
    k = np.logspace(np.log10(KMIN), np.log10(kmax), NK).astype(np.float64)
    wk = np.gradient(k)
    W = np.exp(- (k / (KC_FACTOR * np.pi/dr_min)) ** TAPER_P) if USE_TAPER else np.ones_like(k)
    return k, wk, W

def compute_A_gal(vobs, v2_mu, gb):
    mask = v2_mu > 1e-12
    if not np.any(mask): return 1.0
    ratios = (vobs[mask] ** 2) / v2_mu[mask]
    n = ratios.size
    q = max(3, int(np.ceil(TOP_Q * n)))
    idx = np.argsort(v2_mu[mask])[-q:]
    A = float(np.median(ratios[idx]))
    return float(np.clip(A, *A_CLAMP))

def hankel1_forward(gb, r, k, wr):
    J = j1(np.outer(k, r))
    return (J * (r * gb * wr)[None, :]).sum(axis=1)

def hankel1_inverse(Gb, k, wk, r):
    J = j1(np.outer(k, r))
    return ((k * Gb * wk)[:, None] * J).sum(axis=0)

def predict_gmu_from_gb(r, gb, mu, k, wk, W):
    wr = np.gradient(r)
    Gb = hankel1_forward(gb, r, k, wr)

    # --- SHARPENED BOOST ---
    # n=4 Power Law
    # Asymptote at low k: mu/k (Flat Rotation)
    # Asymptote at high k: 1 (Newtonian)
    # Transition: Sharper than n=2
    M = (1.0 + (mu / k)**4)**0.25

    Gb_f = Gb * M * W
    gmu = hankel1_inverse(Gb_f, k, wk, r)
    return np.maximum(gmu, 0.0)

def chi2_global(mu, dataset, cache):
    total = 0.0
    for name, r, vobs, dv, gb in dataset:
        k, wk, W = cache[name]["k"], cache[name]["wk"], cache[name]["W"]
        gmu = predict_gmu_from_gb(r, gb, mu, k, wk, W)
        v2 = np.maximum(r * gmu, 0.0)
        A = compute_A_gal(vobs, v2, gb)
        vpred = np.sqrt(np.maximum(A * v2, 0.0))
        total += float(np.sum(((vobs - vpred) / dv) ** 2))
    return total

def main():
    os.makedirs(WORKDIR, exist_ok=True)
    if not os.path.exists(Z1):
        print(f"[download] {URL_ROTMOD}", flush=True)
        download(URL_ROTMOD, Z1)

    if os.path.exists(ROTMOD_DIR):
        shutil.rmtree(ROTMOD_DIR)
    unzip(Z1, ROTMOD_DIR)

    rc_files = []
    for root, _, fns in os.walk(ROTMOD_DIR):
        for fn in fns:
            if "rotmod" in fn.lower() and fn.endswith(".dat"):
                rc_files.append(os.path.join(root, fn))
    rc_files.sort()

    dataset = []
    for f in rc_files:
        try:
            r, vobs, dv, vgas, vdisk, vbul = load_rotmod_components(f)
            gb = (vgas * vgas + vdisk * vdisk + vbul * vbul) / r
            dataset.append((stem(f), r, vobs, dv, gb))
        except: pass

    print(f"USING {len(dataset)} GALAXIES", flush=True)
    if len(dataset) < 20: return

    cache = {}
    for name, r, vobs, dv, gb in dataset:
        k, wk, W = build_k_grid(r)
        cache[name] = {"k": k, "wk": wk, "W": W}

    print("Optimizing mu (Sharpened Boost n=4)...", flush=True)
    res = minimize_scalar(
        lambda mu: chi2_global(mu, dataset, cache),
        bounds=MU_BOUNDS,
        method="bounded",
        options=dict(xatol=1e-6, maxiter=300)
    )
    mu_star = float(res.x)
    print(f"\n=== GLOBAL FIT RESULT ===", flush=True)
    print(f"mu* = {mu_star:.6g} kpc^-1", flush=True)

    chi2dofs, rmses, As = [], [], []
    print("\n=== PER-GALAXY PERFORMANCE ===", flush=True)
    print(f"{'Galaxy':18s} {'Chi2/dof':>10s} {'RMS':>10s} {'A_gal':>8s}")

    for name, r, vobs, dv, gb in dataset:
        k, wk, W = cache[name]["k"], cache[name]["wk"], cache[name]["W"]
        gmu = predict_gmu_from_gb(r, gb, mu_star, k, wk, W)
        v2 = np.maximum(r * gmu, 0.0)
        A = compute_A_gal(vobs, v2, gb)
        vpred = np.sqrt(np.maximum(A * v2, 0.0))

        c2 = float(np.sum(((vobs - vpred) / dv) ** 2))
        dof = max(1, int(r.size - 1))
        rms = float(np.sqrt(np.mean((vobs - vpred) ** 2)))

        chi2dofs.append(c2 / dof)
        rmses.append(rms)
        As.append(A)

        print(f"{name:18s} {c2/dof:10.3f} {rms:10.2f} {A:8.3f}", flush=True)

    chi2dofs = np.array(chi2dofs)
    rmses = np.array(rmses)
    As = np.array(As)

    print("\n=== STATS SUMMARY ===", flush=True)
    print(f"Median Chi2/dof : {np.median(chi2dofs):.4f}")
    print(f"Median RMS      : {np.median(rmses):.4f} km/s")
    print(f"Median A_gal    : {np.median(As):.4f}")

if __name__ == "__main__":
    main()
```
