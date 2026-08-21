# SPARC Global Fits and the Kill-Switch Diagnostic

This document extracts the *computationally checkable* content from the SPARC (Rotmod\_LTG) runs in the project archive. It is deliberately minimal: **models, equations, code, and the printed outcomes**.

---

## 1. Data model and observable

For each galaxy, SPARC provides (at radii $r_i$):

- observed rotation curve $V_{\rm obs}(r_i)$ with uncertainties $\sigma_i$,
- baryonic component velocities $(V_{\rm gas},V_{\rm disk},V_{\rm bul})$.

The baryonic Newtonian acceleration proxy is computed from the mass model components:

\[
g_{\rm bar}(r) \;=\;\frac{V_{\rm gas}^2(r)+V_{\rm disk}^2(r)+V_{\rm bul}^2(r)}{r}.
\]

The observed acceleration is:

\[
g_{\rm obs}(r)\;=\;\frac{V_{\rm obs}^2(r)}{r}.
\]

Predicted velocity from any model producing $g_{\rm pred}(r)$:

\[
V_{\rm pred}(r)\;=\;\sqrt{r\,g_{\rm pred}(r)}.
\]

The fit metric used in the run is a global pointwise chi-square:

\[
\chi^2 \;=\;\sum_i \left(\frac{V_{\rm obs}(r_i)-V_{\rm pred}(r_i)}{\sigma_i}\right)^2,
\qquad
\chi^2/{\rm dof} \approx \chi^2/(N_{\rm pts}-N_{\rm par}).
\]

---

## 2. Models compared in the run

### Model A: Baryons-only

\[
g_{\rm pred}(r)=g_{\rm bar}(r).
\]

### Model B: MOND “simple” interpolation (single $a_0$)

Let $x=g_{\rm bar}/a_0$. The “simple” $\nu$ used in the run is:

\[
\nu_{\rm simple}(x)=\tfrac12\left(1+\sqrt{1+\frac{4}{x}}\right),
\qquad
g_{\rm pred}(r)=\nu_{\rm simple}(x)\,g_{\rm bar}(r).
\]

### Model C: MOND / RAR exponential transition (single $a_0$)

The exponential RAR form used in the run:

\[
g_{\rm pred}(r)=\frac{g_{\rm bar}(r)}{1-\exp\!\left(-\sqrt{g_{\rm bar}(r)/a_0}\right)}.
\]

### Model D: Finite-range response kernel (single $L$)

A Yukawa/Helmholtz-like “response kernel” with a range parameter $L$ (implemented numerically in the project code). The run reports only best-fit $L$ and $\chi^2/{\rm dof}$.

### Model E: Kernel TRANSPORT variant (single $L$)

A transport-flavored kernel variant (implementation code provided later in the archive). The run reports best-fit $L$ and $\chi^2/{\rm dof}$.

---

## 3. Printed global outcomes (verbatim numbers from the run)

### 3.1 Global summary

| Model | Best parameter | $\chi^2/{\rm dof}$ |
|---|---:|---:|
| A baryons-only | — | 620.69 |
| B MOND simple | $a_0=3742.11\;({\rm km/s})^2/{\rm kpc}$ | 57.097 |
| C MOND/RAR exp | $a_0=4072.53\;({\rm km/s})^2/{\rm kpc}$ | 58.1651 |
| D finite-range kernel | $L=13.8753\;{\rm kpc}$ | 380.595 |
| E kernel TRANSPORT | $L=40.0447\;{\rm kpc}$ | 234.478 |

**Immediate take-away:** in *this* run configuration (global fixed $M/L$), the MOND-like algebraic transforms outperform the kernel attempts by a lot, and baryons-only is catastrophically bad.

### 3.2 Stratified diagnostics (mass-bin stress test)

The run additionally stratifies galaxies by an estimated $V_{\rm flat}$ bin (dwarfs/mid/big), and reports:

- mean $\chi^2/{\rm dof}$ per bin,
- mean “outer residual” sign bias,
- “per-bin refits” (whether a single global parameter is stable across bins).

Key printed facts:

- **Baryons-only** has strong **positive outer residual bias** (almost all outer points under-predicted).  
- **MOND simple / MOND-RAR** flips to mostly **negative** outer residual bias.  
- **Per-bin refits** prefer significantly different $a_0$ for dwarfs vs big galaxies.

These are exactly the kinds of diagnostics that should gate theory iteration.

---

## 4. The Kill-Switch checklist

The project introduces a pragmatic “kill-switch reading”:

1. Compare $\chi^2/{\rm dof}$ across models.  
2. Outer residual sign fraction should be near $0.5$ if there is no systematic bias.  
3. Per-bin refits should not demand radically different “universal” parameters.

This is a good practice: it prevents a model from hiding behind a global best-fit while failing systematically in a physically meaningful regime split.

---

## 5. Code fragment used for the MOND/RAR exponential prediction (from project archive)

```python
import numpy as np

def v_pred_mond_rar(cache, a0):
    # gbar in (km/s)^2/kpc, a0 in same units
    gbar = cache.gbar
    x = np.sqrt(np.maximum(gbar / a0, 0.0))
    nu_inv = 1.0 - np.exp(-x)
    nu = 1.0 / np.maximum(nu_inv, 1e-12)
    g = nu * gbar
    v = np.sqrt(np.maximum(cache.r_kpc * g, 0.0))
    return v
```

---

## 6. What this *does* and *does not* establish

- It **does** establish that a purely baryonic Newtonian model fails badly on SPARC under this setup.
- It **does** establish that algebraic MOND/RAR transforms dramatically improve the global fit in the same setup.
- It **does not** (yet) establish cosmological consistency, lensing consistency, or the existence of a Lagrangian completion.
- It **does not** validate any claimed “unification” (e.g., $a_0 \leftrightarrow H_0$) without separate, independent tests.

---

## Appendix A. Unit conversion reminder

The run’s best-fit $a_0$ is in SPARC-friendly units:

\[
a_0^{\rm (SI)} \;=\; a_0^{\rm (km^2/s^2/kpc)}\times\frac{10^6}{1\,{\rm kpc}}\approx a_0^{\rm (km^2/s^2/kpc)} \times 3.24078\times 10^{-14}\;\rm m/s^2.
\]

So $a_0\simeq 3700\;({\rm km/s})^2/{\rm kpc}$ corresponds to $\sim 1.2\times 10^{-10}\rm\,m/s^2$.


## Appendix B. Full global-fit script (as captured in GALAXYRUN.ipynb cell 3)

```python
#!/usr/bin/env python3
from __future__ import annotations

import io, math, zipfile, argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple, Optional

import numpy as np

# ============================
# CONFIG (GLOBAL, NO PER-GALAXY)
# ============================
UPSILON_DISK  = 0.5
UPSILON_BULGE = 0.5

# SPARC (Zenodo record you used)
ZENODO_REC = "16284118"
URL_ROTMOD_ZIP = f"https://zenodo.org/records/{ZENODO_REC}/files/Rotmod_LTG.zip?download=1"
URL_TABLE_MRT  = f"https://zenodo.org/records/{ZENODO_REC}/files/SPARC_Lelli2016c.mrt?download=1"

# ============================
# DATA STRUCTURES
# ============================
@dataclass
class GalaxyParams:
    name: str
    Q: int

@dataclass
class Rotmod:
    r_kpc: np.ndarray
    vobs: np.ndarray
    ev: np.ndarray
    vgas: np.ndarray
    vdisk: np.ndarray
    vbul: np.ndarray

@dataclass
class GalaxyCache:
    key: str
    Vflat: float
    r_obs: np.ndarray
    v_obs: np.ndarray
    ev_obs: np.ndarray
    gbar_obs: np.ndarray          # at observed radii
    # kernel cache (for the finite-range response model)
    r_u: np.ndarray
    Dmat: np.ndarray
    w: np.ndarray
    gbar_w: np.ndarray

# ============================
# UTIL
# ============================
def norm_name(s: str) -> str:
    return "".join(ch for ch in s.upper() if ch.isalnum())

def _download(url: str, out_path: Path, chunk: int = 1 << 20) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and out_path.stat().st_size > 0:
        return
    try:
        import requests  # type: ignore
        with requests.get(url, stream=True, timeout=240, headers={"User-Agent": "sparc-fit/1.0"}) as r:
            r.raise_for_status()
            with open(out_path, "wb") as f:
                for b in r.iter_content(chunk_size=chunk):
                    if b:
                        f.write(b)
        return
    except Exception:
        import urllib.request
        req = urllib.request.Request(url, headers={"User-Agent": "sparc-fit/1.0"})
        with urllib.request.urlopen(req, timeout=240) as r:
            head = r.read(256)
            with open(out_path, "wb") as f:
                f.write(head)
                while True:
                    b = r.read(chunk)
                    if not b:
                        break
                    f.write(b)

def fetch_sparc(cache_dir: Path) -> Tuple[Path, Path]:
    rotzip = cache_dir / "Rotmod_LTG.zip"
    table  = cache_dir / "SPARC_Lelli2016c.mrt"
    _download(URL_ROTMOD_ZIP, rotzip)
    _download(URL_TABLE_MRT, table)
    return rotzip, table

def _safe_int(tok: str, default: int = 0) -> int:
    tok = tok.strip()
    if not tok or tok in {".", "..", "..."}:
        return default
    try:
        return int(tok)
    except Exception:
        return default

def parse_sparc_table_minQ(table_path: Path) -> Dict[str, GalaxyParams]:
    raw = table_path.read_text(errors="replace")
    if "<html" in raw[:512].lower():
        raise RuntimeError("SPARC table is HTML (bad download). Delete cache and rerun.")
    out: Dict[str, GalaxyParams] = {}
    for line in raw.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        low = s.lower()
        if low.startswith(("byte-by-byte", "bytes", "name", "----", "====", "col.")):
            continue
        parts = s.split()
        if len(parts) < 19:
            continue
        name = parts[0]
        Q = _safe_int(parts[18], default=9)
        out[name] = GalaxyParams(name=name, Q=Q)
    if not out:
        raise RuntimeError("Failed to parse SPARC table.")
    return out

def _parse_rotmod_one(raw_bytes: bytes) -> Optional[Rotmod]:
    txt = raw_bytes.decode("utf-8", errors="replace").splitlines()
    data_lines = []
    for L in txt:
        s = L.strip()
        if not s or s.startswith("#"):
            continue
        data_lines.append(s)
    if not data_lines:
        return None

    arr = np.loadtxt(io.StringIO("\n".join(data_lines)))
    if arr.ndim == 1:
        arr = arr[None, :]
    if arr.shape[1] < 3:
        return None

    r = arr[:, 0].astype(float)
    vobs = arr[:, 1].astype(float)
    ev = arr[:, 2].astype(float)

    vgas = np.zeros_like(vobs)
    vdisk = np.zeros_like(vobs)
    vbul = np.zeros_like(vobs)

    # common SPARC layout: r, Vobs, eV, Vgas, Vdisk, Vbul, ...
    if arr.shape[1] >= 6:
        vgas = arr[:, 3].astype(float)
        vdisk = arr[:, 4].astype(float)
        vbul = arr[:, 5].astype(float)
    elif arr.shape[1] == 5:
        vgas = arr[:, 3].astype(float)
        vdisk = arr[:, 4].astype(float)
    elif arr.shape[1] == 4:
        vgas = arr[:, 3].astype(float)

    m = np.isfinite(r) & np.isfinite(vobs) & np.isfinite(ev) & (r > 0) & (ev > 0)
    m &= np.isfinite(vgas) & np.isfinite(vdisk) & np.isfinite(vbul)
    if int(m.sum()) < 6:
        return None

    return Rotmod(r_kpc=r[m], vobs=vobs[m], ev=ev[m], vgas=vgas[m], vdisk=vdisk[m], vbul=vbul[m])

def load_rotmod_zip(rotzip: Path) -> Dict[str, Rotmod]:
    out: Dict[str, Rotmod] = {}
    with zipfile.ZipFile(rotzip, "r") as z:
        for fn in z.namelist():
            if not fn.lower().endswith("_rotmod.dat"):
                continue
            name = Path(fn).name.replace("_rotmod.dat", "")
            rm = _parse_rotmod_one(z.read(fn))
            if rm is not None:
                out[name] = rm
    return out

# ============================
# PREPROCESSING PIPELINE
# ============================
def baryon_v2(rm: Rotmod) -> np.ndarray:
    # treat negatives safely
    vgas2  = np.maximum(rm.vgas, 0.0)**2
    vdisk2 = np.maximum(rm.vdisk, 0.0)**2
    vbul2  = np.maximum(rm.vbul, 0.0)**2
    return vgas2 + UPSILON_DISK * vdisk2 + UPSILON_BULGE * vbul2

def gbar_from_rotmod(rm: Rotmod) -> np.ndarray:
    v2 = baryon_v2(rm)
    return v2 / rm.r_kpc  # (km/s)^2/kpc

def Vflat_from_vobs(vobs: np.ndarray) -> float:
    # robust proxy: 90th percentile of observed speeds
    return float(np.percentile(vobs, 90.0))

def _uniform_grid(r: np.ndarray, n: int = 128, rmax_mult: float = 1.2) -> np.ndarray:
    r = np.asarray(r, float)
    rmax = float(r.max()) * float(rmax_mult)
    rmin = max(float(np.min(r[r > 0])), 1e-3)
    return np.linspace(rmin, rmax, n)

def _trap_weights(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, float)
    dx = np.diff(x)
    w = np.empty_like(x)
    w[0] = 0.5 * dx[0]
    w[-1] = 0.5 * dx[-1]
    w[1:-1] = 0.5 * (dx[:-1] + dx[1:])
    return w

def build_cache(key: str, Vflat: float, rm: Rotmod, ngrid: int = 128) -> GalaxyCache:
    r_obs = rm.r_kpc
    v_obs = rm.vobs
    ev_obs = rm.ev
    gbar_obs = gbar_from_rotmod(rm)

    r_u = _uniform_grid(r_obs, n=ngrid, rmax_mult=1.2)
    w = _trap_weights(r_u)
    gbar_u = np.interp(r_u, r_obs, gbar_obs)
    gbar_w = gbar_u * w
    Dmat = np.abs(r_u[:, None] - r_u[None, :]).astype(np.float64)

    return GalaxyCache(
        key=key,
        Vflat=Vflat,
        r_obs=r_obs,
        v_obs=v_obs,
        ev_obs=ev_obs,
        gbar_obs=gbar_obs,
        r_u=r_u,
        Dmat=Dmat,
        w=w,
        gbar_w=gbar_w,
    )

# ============================
# MODELS
# ============================

# (A) Pure baryons (Newtonian) using SPARC components
def v_pred_baryons(c: GalaxyCache) -> np.ndarray:
    v2 = c.gbar_obs * c.r_obs
    return np.sqrt(np.maximum(v2, 0.0))

# (B) MOND “simple” interpolation (one global a0 in same units: (km/s)^2/kpc)
def v_pred_mond_simple(c: GalaxyCache, a0: float) -> np.ndarray:
    gbar = np.maximum(c.gbar_obs, 0.0)
    gobs = 0.5 * (gbar + np.sqrt(gbar*gbar + 4.0*a0*gbar))
    v2 = c.r_obs * gobs
    return np.sqrt(np.maximum(v2, 0.0))

# (C) MOND/RAR exponential form (one global a0)
def v_pred_mond_rar(c: GalaxyCache, a0: float) -> np.ndarray:
    gbar = np.maximum(c.gbar_obs, 0.0)
    x = np.sqrt(np.maximum(gbar / max(a0, 1e-300), 0.0))
    denom = 1.0 - np.exp(-x)
    denom = np.maximum(denom, 1e-300)
    gobs = gbar / denom
    v2 = c.r_obs * gobs
    return np.sqrt(np.maximum(v2, 0.0))

# (D) Finite-range response kernel on acceleration (one global L = mu_inv)
# g_eff(r) = (K * gbar)(r) / (K * 1)(r), K=exp(-|r-r'|/L)
def v_pred_kernel_response(c: GalaxyCache, L: float) -> np.ndarray:
    L = max(float(L), 1e-6)
    K = np.exp(-c.Dmat / L)
    num = K @ c.gbar_w
    den = K @ c.w
    g_eff_u = num / np.maximum(den, 1e-300)
    v2_u = c.r_u * g_eff_u
    v_u = np.sqrt(np.maximum(v2_u, 0.0))
    return np.interp(c.r_obs, c.r_u, v_u)

# ============================
# FITTING (1D GRID SEARCH, GLOBAL)
# ============================
def chi2_dof_for_pred(caches: List[GalaxyCache], pred_fn) -> float:
    chi2 = 0.0
    dof = 0
    for c in caches:
        vmod = pred_fn(c)
        res = (c.v_obs - vmod) / c.ev_obs
        chi2 += float(np.sum(res*res))
        dof += int(res.size)
    return chi2 / max(dof, 1)

def fit_1d(caches: List[GalaxyCache], grid: np.ndarray, make_pred) -> Tuple[float, float]:
    vals = np.array([chi2_dof_for_pred(caches, lambda c, x=x: make_pred(c, x)) for x in grid], dtype=float)
    j = int(np.argmin(vals))
    return float(grid[j]), float(vals[j])

# ============================
# DIAGNOSTICS / KILL-SWITCH
# ============================
def stratified_report(caches: List[GalaxyCache], pred_fn, label: str) -> None:
    Vflat = np.array([c.Vflat for c in caches], float)
    chi2d = np.zeros(len(caches), float)
    outer = np.zeros(len(caches), float)

    for i, c in enumerate(caches):
        vmod = pred_fn(c)
        res = c.v_obs - vmod
        chi2d[i] = float(np.mean((res / c.ev_obs) ** 2))
        order = np.argsort(c.r_obs)
        k0 = int(0.7 * len(order))
        outer[i] = float(np.mean(res[order][k0:])) if k0 < len(order) else float("nan")

    print(f"\n=== {label}: stratified diagnostics ===")
    for lbl, m in [
        ("dwarfs (Vflat<80)", Vflat < 80),
        ("mid (80<=Vflat<150)", (Vflat >= 80) & (Vflat < 150)),
        ("big (Vflat>=150)", Vflat >= 150),
    ]:
        n = int(np.sum(m))
        if n == 0:
            continue
        sub = chi2d[m]
        subo = outer[m]
        print(f"{lbl:18s}: N={n:3d}  mean chi2/dof={sub.mean():.3f}  median={np.median(sub):.3f}  mean outer resid={np.nanmean(subo):+.3f} km/s")

    frac_outer_pos = float(np.mean(outer > 0.0))
    print(f"Outer residual sign: fraction positive = {frac_outer_pos:.3f}  (0.5 ~ no systematic bias)")

def per_bin_refit(caches: List[GalaxyCache], grid: np.ndarray, make_pred, label: str) -> None:
    Vflat = np.array([c.Vflat for c in caches], float)
    print(f"\n=== {label}: per-bin refits ===")
    for lbl, m in [("dwarfs", Vflat < 80), ("big", Vflat >= 150)]:
        sub = [caches[i] for i in range(len(caches)) if m[i]]
        if len(sub) < 10:
            continue
        xbest, chi = fit_1d(sub, grid, make_pred)
        print(f"{lbl:6s}: best={xbest:.6g}  chi2/dof={chi:.3f}")

# ============================
# MAIN
# ============================
def main(argv: Optional[List[str]] = None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", type=str, default="sparc_cache")
    ap.add_argument("--quality_max", type=int, default=3)
    ap.add_argument("--min_points", type=int, default=8)
    ap.add_argument("--ngrid", type=int, default=128)
    args, _unknown = ap.parse_known_args(args=argv)

    cache_dir = Path(args.cache)
    rotzip, table = fetch_sparc(cache_dir)

    params_raw = parse_sparc_table_minQ(table)
    rot_raw = load_rotmod_zip(rotzip)

    params = {norm_name(k): v for k, v in params_raw.items()}
    rot = {norm_name(k): v for k, v in rot_raw.items()}

    common = sorted(set(params.keys()) & set(rot.keys()))
    chosen = []
    for k in common:
        if params[k].Q > args.quality_max:
            continue
        if rot[k].r_kpc.size < args.min_points:
            continue
        chosen.append(k)
    if not chosen:
        chosen = [k for k in common if rot[k].r_kpc.size >= 6]

    caches = []
    for k in chosen:
        rm = rot[k]
        Vflat = Vflat_from_vobs(rm.vobs)
        caches.append(build_cache(k, Vflat, rm, ngrid=int(args.ngrid)))

    print(f"Loaded: params={len(params_raw)}  rotmod={len(rot_raw)}  overlap={len(common)}  using={len(caches)}")
    print(f"Global M/L: UPSILON_DISK={UPSILON_DISK}  UPSILON_BULGE={UPSILON_BULGE}")

    # --- Baseline baryons-only
    chi_bary = chi2_dof_for_pred(caches, v_pred_baryons)
    print("\n=== MODEL A: baryons-only (SPARC components) ===")
    print(f"chi2/dof = {chi_bary:.6g}")
    stratified_report(caches, v_pred_baryons, "Baryons-only")

    # --- MOND fits (one global a0 in (km/s)^2/kpc)
    # Use broad grid; includes typical a0 ~ 3700 in these units.
    a0_grid = np.geomspace(50.0, 40000.0, 80)

    a0_s, chi_s = fit_1d(caches, a0_grid, lambda c, a0: v_pred_mond_simple(c, a0))
    print("\n=== MODEL B: MOND simple (1 param a0) ===")
    print(f"a0_best = {a0_s:.6g}  (units: (km/s)^2/kpc)")
    print(f"chi2/dof = {chi_s:.6g}")
    stratified_report(caches, lambda c: v_pred_mond_simple(c, a0_s), "MOND simple")
    per_bin_refit(caches, a0_grid, lambda c, a0: v_pred_mond_simple(c, a0), "MOND simple")

    a0_r, chi_r = fit_1d(caches, a0_grid, lambda c, a0: v_pred_mond_rar(c, a0))
    print("\n=== MODEL C: MOND/RAR exp (1 param a0) ===")
    print(f"a0_best = {a0_r:.6g}  (units: (km/s)^2/kpc)")
    print(f"chi2/dof = {chi_r:.6g}")
    stratified_report(caches, lambda c: v_pred_mond_rar(c, a0_r), "MOND/RAR exp")
    per_bin_refit(caches, a0_grid, lambda c, a0: v_pred_mond_rar(c, a0), "MOND/RAR exp")

    # --- Finite-range response kernel (one global L in kpc)
    L_grid = np.geomspace(0.2, 300.0, 70)

    L_best, chi_k = fit_1d(caches, L_grid, lambda c, L: v_pred_kernel_response(c, L))
    print("\n=== MODEL D: finite-range response kernel (1 param L=mu_inv) ===")
    print(f"L_best = {L_best:.6g} kpc")
    print(f"chi2/dof = {chi_k:.6g}")
    stratified_report(caches, lambda c: v_pred_kernel_response(c, L_best), "Kernel response")
    per_bin_refit(caches, L_grid, lambda c, L: v_pred_kernel_response(c, L), "Kernel response")

    print("\nKILL-SWITCH reading:")
    print("  - Compare chi2/dof across models.")
    print("  - Check outer residual sign near 0.5 and small outer bias.")
    print("  - Check per-bin refits: dwarfs vs big must not demand different global parameters.")

# Run in Colab/Jupyter safely
main(argv=[])
```
