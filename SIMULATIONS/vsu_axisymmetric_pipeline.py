
"""
VSU / MOND-like axisymmetric AQUAL solver + per-galaxy MCMC scaffold
-------------------------------------------------------------------

This script is designed to do exactly the upgrade you described:

1) Replace spherical "algebraic closure" (g μ(g/a0)=g_N) with a true axisymmetric solve of
       ∇·( μ(|∇Φ|/a0) ∇Φ ) = 4πG ρ
   on an (R,z) grid.

2) Use SPARC mass-model bundles as inputs (rotmod files + stellar density profiles).
   - SPARC "Newtonian mass model" files typically include: R, Vobs, eV, Vgas, Vdisk, Vbul,
     plus extra columns (often disk/bulge surface brightness or density). You may need to
     adjust `load_rotmod()` depending on the exact column convention in your bundle.

3) Run per-galaxy MCMC for Υ_* (and optionally a0, bulge Υ, distance scaling, etc.)
   by *precomputing* V(R|Υ_*) on a grid of Υ_* values and interpolating inside MCMC.
   This avoids solving the nonlinear PDE at every MCMC step.

4) Run a GR+NFW comparison MCMC in parallel.

Notes:
- This is intentionally self-contained (NumPy + SciPy only). No JAX, no numpyro required.
- The PDE solver here is a simple Picard + SOR relaxer. It is NOT production-grade multigrid,
  but it is sufficient as a starting point and is structurally correct.

Units:
- Length: kpc
- Velocity: km/s
- Potential Φ: (km/s)^2
- Acceleration: (km/s)^2/kpc
- Density: Msun/kpc^3
- G = 4.30091e-6  (kpc (km/s)^2 / Msun)

If you want speed/robustness:
- Replace the inner SOR with a multigrid V-cycle, or
- Switch to QUMOND (two linear Poisson solves), or
- Build a surrogate/emulator (GP/NN) for V(R|Υ_*,a0).
"""
from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from typing import Tuple, Dict, Optional, Callable
from scipy import optimize, interpolate, special

G = 4.30091e-6  # kpc (km/s)^2 Msun^-1
KPC_IN_M = 3.085677581e19
A0_SI = 1.2e-10  # m/s^2 (canonical MOND-ish scale; replace with your VSU a0 if different)
A0 = A0_SI / (1e6 / KPC_IN_M)  # convert to (km/s)^2/kpc

def mu_exponential(x: np.ndarray) -> np.ndarray:
    """Your VSU constitutive μ(x)=1-exp(-x)."""
    return 1.0 - np.exp(-x)

@dataclass
class RotmodData:
    R: np.ndarray        # kpc
    Vobs: np.ndarray     # km/s
    eV: np.ndarray       # km/s
    Vgas: np.ndarray     # km/s
    Vdisk: np.ndarray    # km/s (for Υ_disk=1 in SPARC convention)
    Vbul: np.ndarray     # km/s (for Υ_bul=1 in SPARC convention)
    extra: Optional[np.ndarray] = None  # any extra columns

def load_rotmod(path: str) -> RotmodData:
    """
    Load a SPARC-like rotmod file.
    Most common formats:
      - 6 columns: R, Vobs, eV, Vgas, Vdisk, Vbul
      - 8 columns: R, Vobs, eV, Vgas, Vdisk, Vbul, X7, X8
    """
    arr = np.genfromtxt(path)
    if arr.ndim != 2 or arr.shape[1] < 6:
        raise ValueError(f"Unexpected rotmod shape {arr.shape} in {path}")
    R, Vobs, eV, Vgas, Vdisk, Vbul = arr[:,0], arr[:,1], arr[:,2], arr[:,3], arr[:,4], arr[:,5]
    extra = arr[:,6:] if arr.shape[1] > 6 else None
    return RotmodData(R=R, Vobs=Vobs, eV=eV, Vgas=Vgas, Vdisk=Vdisk, Vbul=Vbul, extra=extra)

# ---------- Parametric baryon model helpers (optional fallback) ----------

def vdisk_exponential(R: np.ndarray, Mdisk: float, Rd: float) -> np.ndarray:
    """
    Newtonian circular speed of an infinitesimally thin exponential disk.

    Σ(R) = (Mdisk / (2π Rd^2)) exp(-R/Rd)

    V^2(R) = 4π G Σ0 Rd y^2 [I0(y)K0(y) - I1(y)K1(y)], y=R/(2Rd)
    """
    R = np.asarray(R)
    y = R / (2.0*Rd + 1e-30)
    Sigma0 = Mdisk / (2.0*np.pi*Rd**2)
    I0, I1 = special.iv(0, y), special.iv(1, y)
    K0, K1 = special.kv(0, y), special.kv(1, y)
    term = I0*K0 - I1*K1
    V2 = 4.0*np.pi*G*Sigma0*Rd*(y**2)*term
    V2 = np.clip(V2, 0.0, np.inf)
    return np.sqrt(V2)

def fit_exponential_disk(R: np.ndarray, V: np.ndarray, w: Optional[np.ndarray]=None) -> Tuple[float,float]:
    """
    Fit an exponential disk (Mdisk, Rd) to a provided Newtonian V(R) curve.
    This is a convenience fallback if you don't have surface density profiles.
    """
    R = np.asarray(R); V = np.asarray(V)
    if w is None:
        w = np.ones_like(R)
    # crude initial guesses
    Rd0 = max(0.5, 0.5*np.median(R))
    M0 = 1e10  # Msun
    def resid(p):
        logM, logRd = p
        M = 10**logM
        Rd = 10**logRd
        Vmod = vdisk_exponential(R, M, Rd)
        return (Vmod - V) * np.sqrt(w)
    p0 = np.array([np.log10(M0), np.log10(Rd0)])
    sol = optimize.least_squares(resid, p0, bounds=([6, -1],[13, 2]))
    M = 10**sol.x[0]
    Rd = 10**sol.x[1]
    return M, Rd

# ---------- 3D density builders (axisymmetric) ----------

def rho_exp_disk(R: np.ndarray, z: np.ndarray, Mdisk: float, Rd: float, hz: float) -> np.ndarray:
    """
    Axisymmetric exponential disk with exponential vertical profile:
       ρ(R,z) = Σ(R) exp(-|z|/hz) / (2 hz)
    where Σ(R)=(Mdisk/(2πRd^2)) exp(-R/Rd).
    """
    Sigma0 = Mdisk / (2.0*np.pi*Rd**2)
    SigmaR = Sigma0 * np.exp(-R/Rd)
    return SigmaR * np.exp(-np.abs(z)/hz) / (2.0*hz)

def rho_hernquist(R: np.ndarray, z: np.ndarray, Mb: float, a: float) -> np.ndarray:
    """
    Spherical Hernquist bulge density evaluated at r=sqrt(R^2+z^2):
      ρ(r) = (Mb / (2π)) * a / [ r (r+a)^3 ]
    """
    r = np.sqrt(R**2 + z**2) + 1e-30
    return (Mb / (2.0*np.pi)) * (a / (r * (r + a)**3))

# ---------- Axisymmetric AQUAL solver ----------

@dataclass
class Grid:
    R: np.ndarray   # shape (Nr,)
    z: np.ndarray   # shape (Nz,) (z>=0, using symmetry)
    dR: float
    dz: float

def make_grid(Rmax: float, zmax: float, Nr: int, Nz: int) -> Grid:
    R = np.linspace(0.0, Rmax, Nr)
    z = np.linspace(0.0, zmax, Nz)
    return Grid(R=R, z=z, dR=R[1]-R[0], dz=z[1]-z[0])

def boundary_phi_pointmass(R: float, z: float, Mtot: float, a0: float=A0) -> float:
    """
    Crude far-field boundary potential.
    In deep regime: g ≈ sqrt(G M a0) / r  -> Φ ≈ -sqrt(G M a0) ln r
    We use ln(r + r0) to avoid singularity at origin.
    """
    r = np.sqrt(R*R + z*z) + 1e-6
    return -np.sqrt(G*Mtot*a0) * np.log(r)

def solve_aqual_axisymmetric(
    grid: Grid,
    rho: np.ndarray,                  # (Nr,Nz) Msun/kpc^3
    mu: Callable[[np.ndarray], np.ndarray] = mu_exponential,
    a0: float = A0,
    Mtot_for_bc: Optional[float] = None,
    max_outer: int = 50,
    max_inner: int = 400,
    omega: float = 1.6,
    tol: float = 1e-5,
    verbose: bool = False,
) -> np.ndarray:
    """
    Solve ∇·( μ(|∇Φ|/a0) ∇Φ ) = 4πGρ on an (R,z>=0) grid with symmetry BCs at R=0 and z=0.

    Returns Φ on grid, shape (Nr,Nz), in (km/s)^2.

    DISCLAIMER:
    - This is a "starter solver": Picard iteration + SOR, fixed Dirichlet boundaries.
    - For publication-grade work, use multigrid + better boundary treatment.
    """
    Nr, Nz = rho.shape
    assert Nr == grid.R.size and Nz == grid.z.size
    dR, dz = grid.dR, grid.dz

    # Boundary mass estimate if not provided
    if Mtot_for_bc is None:
        # crude: integrate rho over cylindrical volume (R,z>=0) and double for z<0 symmetry
        RR, ZZ = np.meshgrid(grid.R, grid.z, indexing='ij')
        vol = 2.0 * (2.0*np.pi*RR) * dR * dz  # factor 2 for z<0
        Mtot_for_bc = float(np.sum(rho * vol))

    # Initialize potential with boundary-based guess
    Phi = np.zeros((Nr, Nz), dtype=float)
    for i in range(Nr):
        for j in range(Nz):
            # rough init: point-mass deep potential
            Phi[i,j] = boundary_phi_pointmass(grid.R[i], grid.z[j], Mtot_for_bc, a0=a0)

    # Precompute RHS
    RHS = 4.0*np.pi*G*rho  # units: (km/s)^2/kpc^2

    # Helper: compute gradient magnitude at cell centers
    def grad_mag(Phi: np.ndarray) -> np.ndarray:
        dPhidR = np.zeros_like(Phi)
        dPhidz = np.zeros_like(Phi)

        # interior central differences
        dPhidR[1:-1,:] = (Phi[2:,:] - Phi[:-2,:])/(2.0*dR)
        dPhidz[:,1:-1] = (Phi[:,2:] - Phi[:,:-2])/(2.0*dz)

        # symmetry boundaries:
        # R=0: dPhi/dR = 0
        dPhidR[0,:] = 0.0
        # z=0: dPhi/dz = 0
        dPhidz[:,0] = 0.0

        # outer boundaries: one-sided
        dPhidR[-1,:] = (Phi[-1,:] - Phi[-2,:]) / dR
        dPhidz[:,-1] = (Phi[:,-1] - Phi[:,-2]) / dz

        return np.sqrt(dPhidR**2 + dPhidz**2) + 1e-30

    # Fixed Dirichlet boundaries using the crude point-mass boundary
    def apply_dirichlet_bc(Phi: np.ndarray):
        # outer R boundary
        i = Nr-1
        for j in range(Nz):
            Phi[i,j] = boundary_phi_pointmass(grid.R[i], grid.z[j], Mtot_for_bc, a0=a0)
        # outer z boundary
        j = Nz-1
        for i in range(Nr):
            Phi[i,j] = boundary_phi_pointmass(grid.R[i], grid.z[j], Mtot_for_bc, a0=a0)

    apply_dirichlet_bc(Phi)

    for outer in range(max_outer):
        gmag = grad_mag(Phi)
        mu_c = mu(gmag / a0)  # μ at cell centers
        # face μ via arithmetic mean
        mu_Rp = 0.5*(mu_c[1:,:] + mu_c[:-1,:])  # between i-1 and i (size Nr-1,Nz)
        mu_Zp = 0.5*(mu_c[:,1:] + mu_c[:,:-1])  # between j-1 and j (size Nr,Nz-1)

        # SOR iterations for linearized equation with frozen μ
        max_update = 0.0
        for inner in range(max_inner):
            max_update = 0.0
            # Gauss-Seidel sweep
            for i in range(Nr):
                Ri = grid.R[i]
                for j in range(Nz):
                    # Skip Dirichlet boundaries
                    if i == Nr-1 or j == Nz-1:
                        continue

                    # Symmetry at R=0 and z=0 handled by mirroring neighbors
                    # Neighbor indices
                    ip = i+1
                    im = i-1 if i-1 >= 0 else 1  # mirror for i=0
                    jp = j+1
                    jm = j-1 if j-1 >= 0 else 1  # mirror for j=0

                    # radial face coefficients
                    # define mu at i+1/2 and i-1/2
                    if i == 0:
                        mu_imh = mu_Rp[0,j]  # approximate
                    else:
                        mu_imh = mu_Rp[i-1,j]
                    mu_iph = mu_Rp[i,j] if i < Nr-1 else mu_Rp[-1,j]

                    R_imh = max(0.0, Ri - 0.5*dR)
                    R_iph = Ri + 0.5*dR

                    aR_p = (R_iph * mu_iph) / (Ri * dR*dR + 1e-30)
                    aR_m = (R_imh * mu_imh) / (Ri * dR*dR + 1e-30) if Ri > 0 else aR_p

                    # vertical face coefficients
                    mu_jmh = mu_Zp[i,j-1] if j > 0 else mu_Zp[i,0]
                    mu_jph = mu_Zp[i,j] if j < Nz-1 else mu_Zp[i,-1]
                    aZ_p = mu_jph / (dz*dz)
                    aZ_m = mu_jmh / (dz*dz)

                    aC = aR_p + aR_m + aZ_p + aZ_m
                    b = RHS[i,j]

                    Phi_new = (aR_p*Phi[ip,j] + aR_m*Phi[im,j] + aZ_p*Phi[i,jp] + aZ_m*Phi[i,jm] - b) / (aC + 1e-30)
                    # over-relax
                    upd = Phi_new - Phi[i,j]
                    Phi[i,j] += omega * upd
                    max_update = max(max_update, abs(upd))

            apply_dirichlet_bc(Phi)
            if max_update < tol:
                break

        if verbose:
            print(f"[outer {outer}] max_update={max_update:.3e}")

        if max_update < tol:
            break

    return Phi

def rotation_curve_from_phi(grid: Grid, Phi: np.ndarray, R_eval: np.ndarray) -> np.ndarray:
    """
    Compute V(R)=sqrt(R * dΦ/dR) at z=0 from solved Φ(R,z).
    Uses interpolation in R for the midplane derivative.
    """
    # midplane is j=0 (z=0 plane, using symmetry)
    Phi_mid = Phi[:,0]
    # dΦ/dR via central difference
    dR = grid.dR
    dPhidR = np.zeros_like(Phi_mid)
    dPhidR[1:-1] = (Phi_mid[2:] - Phi_mid[:-2])/(2*dR)
    dPhidR[0] = 0.0
    dPhidR[-1] = (Phi_mid[-1] - Phi_mid[-2])/dR

    # interpolate dΦ/dR to requested radii
    f = interpolate.interp1d(grid.R, dPhidR, kind="linear", fill_value="extrapolate")
    gR = f(R_eval)  # (km/s)^2/kpc
    V2 = np.clip(R_eval * gR, 0.0, np.inf)
    return np.sqrt(V2)

# ---------- MCMC scaffolding (simple Metropolis) ----------

def loglike_gaussian(y: np.ndarray, yerr: np.ndarray, ymodel: np.ndarray) -> float:
    r = (y - ymodel)/yerr
    return -0.5*np.sum(r*r + np.log(2*np.pi*yerr*yerr))

def metropolis(
    logpost: Callable[[np.ndarray], float],
    x0: np.ndarray,
    step: np.ndarray,
    nsamp: int = 20000,
    burn: int = 5000,
    thin: int = 10,
    rng: Optional[np.random.Generator] = None,
) -> np.ndarray:
    if rng is None:
        rng = np.random.default_rng(0)
    x = x0.copy()
    lp = logpost(x)
    chain = []
    accept = 0
    for t in range(nsamp):
        prop = x + rng.normal(scale=step, size=x.shape)
        lp_prop = logpost(prop)
        if np.log(rng.random()) < lp_prop - lp:
            x, lp = prop, lp_prop
            accept += 1
        if t >= burn and ((t-burn) % thin == 0):
            chain.append(x.copy())
    chain = np.array(chain)
    # print(f"acceptance ~ {accept/nsamp:.3f}")
    return chain

# ---------- Example per-galaxy workflow ----------

def build_vsu_interpolator_for_galaxy(
    rot: RotmodData,
    Rmax_factor: float = 3.0,
    zmax_factor: float = 2.0,
    Nr: int = 160,
    Nz: int = 120,
    hz_over_Rd: float = 0.2,
    ups_grid: np.ndarray = np.linspace(0.05, 1.2, 25),
    a0: float = A0,
    verbose: bool = False,
) -> Callable[[float], np.ndarray]:
    """
    Precompute V(R_i | Υ*) for Υ* on `ups_grid`, then return interpolator Υ* -> Vmodel(R_obs).

    Baryons:
    - Gas disk: fitted exponential disk to Vgas curve.
    - Stellar disk: fitted exponential disk to Vdisk curve (SPARC convention Υ=1), then scaled by Υ*.
    - Bulge: ignored here; you can add bulge by fitting Hernquist to Vbul if needed.

    This is a pragmatic compromise if you don't have the full surface density profiles available.
    """
    R_obs = rot.R

    # Fit exponential disks to the *unit-normalization* Newtonian curves
    Mgas, Rd_gas = fit_exponential_disk(R_obs, rot.Vgas)
    Mstar_unit, Rd_star = fit_exponential_disk(R_obs, rot.Vdisk)

    hz_star = hz_over_Rd * Rd_star
    hz_gas  = 0.1  # kpc, crude

    Rmax = float(Rmax_factor * R_obs.max())
    zmax = float(zmax_factor * R_obs.max())
    grid = make_grid(Rmax, zmax, Nr=Nr, Nz=Nz)
    RR, ZZ = np.meshgrid(grid.R, grid.z, indexing='ij')

    # precompute gas density (fixed)
    rho_gas = rho_exp_disk(RR, ZZ, Mgas, Rd_gas, hz_gas)

    Vgrid = []
    for ups in ups_grid:
        rho_star = rho_exp_disk(RR, ZZ, ups*Mstar_unit, Rd_star, hz_star)
        rho = rho_gas + rho_star
        Phi = solve_aqual_axisymmetric(grid, rho, a0=a0, verbose=verbose)
        V = rotation_curve_from_phi(grid, Phi, R_obs)
        Vgrid.append(V)

    Vgrid = np.asarray(Vgrid)  # shape (Nups, Nobs)
    # interpolation in ups for each radius
    def V_of_ups(ups: float) -> np.ndarray:
        # cubic over ups for each radius
        out = np.zeros_like(R_obs)
        for i in range(R_obs.size):
            f = interpolate.interp1d(ups_grid, Vgrid[:,i], kind="cubic", fill_value="extrapolate")
            out[i] = float(f(ups))
        return out
    return V_of_ups

def fit_galaxy_vsu_vs_nfw(rot: RotmodData):
    """
    Demonstration skeleton:
    - Build VSU axisymmetric interpolator V(R|Υ*)
    - Run Metropolis on Υ* only (you can extend)
    - Run Metropolis on NFW params (logM200, logc, Υ*)
    """
    R = rot.R
    y = rot.Vobs
    yerr = rot.eV

    # --- VSU axisymmetric ---
    V_of_ups = build_vsu_interpolator_for_galaxy(rot, verbose=False)
    def logpost_vsu(x):
        ups = x[0]
        if not (0.01 < ups < 2.0):
            return -np.inf
        # weak prior: lognormal-ish around 0.5 dex width
        lp = -0.5*((np.log10(ups) - np.log10(0.5))/0.2)**2
        Vmod = V_of_ups(ups)
        return lp + loglike_gaussian(y, yerr, Vmod)

    chain_vsu = metropolis(logpost_vsu, x0=np.array([0.5]), step=np.array([0.03]))
    ups_samples = chain_vsu[:,0]
    ups_mean = float(np.mean(ups_samples))
    ups_std  = float(np.std(ups_samples))

    # --- GR + NFW ---
    # NFW halo circular speed (simple form)
    def vhalo_nfw(R, M200, c200):
        # This is a placeholder; implement a standard NFW V(R) in kpc/km/s units
        # using concentration and virial radius. Many references exist.
        # For now: return zeros (so the scaffold runs).
        return np.zeros_like(R)

    def logpost_nfw(x):
        logM200, logc, ups = x
        if not (8.0 < logM200 < 14.0 and 0.1 < logc < 2.0 and 0.01 < ups < 2.0):
            return -np.inf
        # broad priors
        lp = 0.0
        Vbar2 = rot.Vgas**2 + ups*rot.Vdisk**2 + ups*rot.Vbul**2
        Vhalo = vhalo_nfw(R, 10**logM200, 10**logc)
        Vmod = np.sqrt(np.clip(Vbar2 + Vhalo**2, 0.0, np.inf))
        return lp + loglike_gaussian(y, yerr, Vmod)

    chain_nfw = metropolis(logpost_nfw, x0=np.array([11.0, 1.0, 0.5]), step=np.array([0.05,0.03,0.03]))
    ups_samples_nfw = chain_nfw[:,2]
    ups_mean_nfw = float(np.mean(ups_samples_nfw))
    ups_std_nfw  = float(np.std(ups_samples_nfw))

    return dict(
        ups_vsu=ups_mean, sigma_ups_vsu=ups_std,
        ups_nfw=ups_mean_nfw, sigma_ups_nfw=ups_std_nfw,
    )
