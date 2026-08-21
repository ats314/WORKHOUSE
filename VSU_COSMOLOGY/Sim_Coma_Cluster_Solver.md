---
title: "Coma Cluster Solver"
subtitle: "Declining T(r) + scalar self-energy (code + reproduced runs)"
status: "Simulation extracted from chat logs; code consolidated and tested"
---

# Coma Cluster Solver: Declining \(T(r)\) + Scalar Self-Energy
## One-shot hydrostatic ODE integration with VSU constitutive law

### What this is
This is a compact, runnable implementation of the “declining \(T(r)\) + scalar self-energy” Coma cluster experiment from the project chat logs. It integrates a hydrostatic equilibrium ODE system in dimensionless variables and reports the gas mass \(M_g\), scalar self-energy mass \(M_\phi\), and their ratio at \(R_{500}\).

### What it is *not*
This is **not** a full X-ray forward model, not a lensing likelihood, and not a calibrated cluster pipeline. It’s a controlled toy-to-semi-phenomenological solver designed to test *regime control* and *mass partitioning* under the chosen \(\mu\)-function.

---

# 1. Dimensionless formulation

Choose physical constants \(G, a_0, k_B\) and a mean molecular weight \(\mu_{\rm gas}\).

Given a central temperature \(T_0\), define scales
\[
r_0=\frac{k_B T_0}{\mu_{\rm gas}m_p a_0},
\qquad
M_0=\frac{a_0 r_0^2}{G},
\qquad
\rho_0=\frac{a_0}{4\pi G r_0}.
\]

Define dimensionless radius \(x=r/r_0\) and dimensionless gas density \(y(x)=\rho_g(r)/\rho_0\).

Let the total enclosed dimensionless mass be
\[
m_{\rm tot}(x)=m_g(x)+m_\phi(x),
\]
where
\[
m_g'(x)=x^2 y(x),
\qquad
m_\phi'(x)=x^2 y_\phi(x).
\]

---

# 2. The constitutive closure and scalar self-energy density

Define the “effective” dimensionless acceleration \(\hat g = g/a_0\).
The solver uses the algebraic closure
\[
\hat g
=
\frac{m_{\rm tot}(x)/x^2}{1-e^{-\sqrt{m_{\rm tot}(x)}/x}},
\]
which is a stable implementation of the \(\mu\)-law
\(\mu(s)=1-e^{-s}\) with \(s=\sqrt{\hat g}\) in the quasilinear elliptic regime.

Let
\[
Y=\hat g^2,\qquad
\mu(Y)=1-e^{-Y^{1/4}},
\]
and define
\[
F(Y)=\int_0^Y \mu(\sqrt{s})\,ds
\]
(using a small-\(Y\) series for numerical stability).

Then the scalar self-energy density proxy is implemented as
\[
y_\phi(Y)=\frac12\left(2Y\,\mu(Y)-F(Y)\right).
\]

---

# 3. Hydrostatic equilibrium with a declining temperature profile

Let \(\theta(x)=T(x)/T_0\). Hydrostatic equilibrium gives an ODE for \(\ln y\):
\[
\frac{d\ln y}{dx}
=
-\left(\frac{\hat g}{\theta}+\frac{\theta'}{\theta}\right).
\]

The solver uses a smooth declining profile:
\[
\theta(x)=
\left(\frac{x}{x_t}\right)^{-a_T}
\left(1+\left(\frac{x}{x_t}\right)^{b_T}\right)^{-c_T/b_T},
\]
with \(x_t\) set as a fraction of \(X_{\max}=R_{500}/r_0\).

---

# 4. Colab-ready code (single file)

```python
import math, numpy as np
from scipy.integrate import solve_ivp

# Physical constants (SI)
G   = 6.674e-11
a0  = 1.2e-10
kB  = 1.380649e-23
m_p = 1.67262192369e-27
mu_gas = 0.6

KPC_M = 3.085677581e19
MSUN_KG = 1.98847e30

def coma_run(
    Y0_CENTRAL=0.23,
    T0_keV=8.2,
    R500_kpc=1300.0,
    # temperature profile controls
    c_T=0.8,
    b_T=2.0,
    a_T=0.0,
    x_t_factor=0.45,
    # numerics
    X0=1e-4,
    RTOL=5e-9,
    ATOL=5e-13,
    MAX_STEP=5e-4,
    LN_Y_FLOOR=-200.0,
):
    # --- scaling ---
    T0_K = T0_keV * 1.16045e7
    r0   = (kB * T0_K) / (mu_gas * m_p * a0)   # [m]
    M0   = (a0 * r0 * r0) / G                  # [kg]
    rho0 = a0 / (4.0 * math.pi * G * r0)       # [kg/m^3]
    X_MAX  = (R500_kpc * KPC_M) / r0
    x_t = x_t_factor * X_MAX

    # --- declining temperature profile ---
    def theta(x: float) -> float:
        if x <= 0.0:
            return 1.0
        z = x / x_t
        return (z ** (-a_T)) * ((1.0 + z**b_T) ** (-c_T / b_T))

    def dtheta_dx(x: float) -> float:
        if x <= 0.0:
            return 0.0
        z = x / x_t
        th = theta(x)
        term_a = -a_T / x if a_T != 0.0 else 0.0
        dln = term_a - (c_T / b_T) * ((b_T * z**(b_T - 1.0)) / (x_t * (1.0 + z**b_T)))
        return th * dln

    # --- scalar constitutive functions ---
    U_SERIES = 2e-3
    DENOM_FLOOR = 1e-14

    def U_from_Y(Y: float) -> float:
        if Y <= 0.0:
            return 0.0
        return math.exp(0.25 * math.log(Y))  # Y^(1/4)

    def mu_Y(Y: float) -> float:
        U = U_from_Y(Y)
        return -math.expm1(-U)               # 1 - exp(-U), stable

    def F_Y(Y: float) -> float:
        U = U_from_Y(Y)
        if U < U_SERIES:
            U2 = U*U
            U4 = U2*U2
            U5 = U4*U
            U6 = U5*U
            U7 = U6*U
            U8 = U7*U
            U9 = U8*U
            U10 = U9*U
            U11 = U10*U
            return 4.0 * (U5/5.0 - U6/6.0 + U7/14.0 - U8/48.0
                          + U9/216.0 - U10/1200.0 + U11/7920.0)
        return U**4 - 24.0 + 4.0*math.exp(-U)*(U**3 + 3.0*U**2 + 6.0*U + 6.0)

    def y_phi_from_Y(Y: float) -> float:
        mu = mu_Y(Y)
        F  = F_Y(Y)
        return 0.5 * (2.0*Y*mu - F)

    # --- ODE system: [ln y, m_g, m_phi] ---
    def rhs(x: float, u: np.ndarray) -> np.ndarray:
        ln_y, mg, mp = float(u[0]), float(u[1]), float(u[2])

        ln_y = max(ln_y, LN_Y_FLOOR)
        y = math.exp(ln_y)

        mg = max(mg, 0.0)
        mp = max(mp, 0.0)
        m_tot = mg + mp

        s = math.sqrt(max(m_tot, 0.0)) / x
        denom = -math.expm1(-s)
        if denom < DENOM_FLOOR:
            denom = max(s, DENOM_FLOOR)

        ghat = (m_tot / (x*x)) / denom
        Y = ghat * ghat
        yphi = y_phi_from_Y(Y)

        th = theta(x)
        dth = dtheta_dx(x)

        dlny_dx = -(ghat/th + dth/th)
        dmg_dx  = x*x*y
        dmp_dx  = x*x*yphi

        return np.array([dlny_dx, dmg_dx, dmp_dx], dtype=np.float64)

    # --- initial conditions ---
    y0 = float(Y0_CENTRAL)
    u0 = np.array([math.log(max(y0, 1e-300)), (X0**3)*y0/3.0, 0.0], dtype=np.float64)

    sol = solve_ivp(
        rhs, (X0, X_MAX), u0,
        method="Radau",
        rtol=RTOL, atol=ATOL,
        max_step=MAX_STEP
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    # --- unpack + compute physical outputs ---
    x = sol.t
    ln_y = sol.y[0]
    y = np.exp(np.maximum(ln_y, LN_Y_FLOOR))
    mg = sol.y[1]
    mp = sol.y[2]

    r_final_kpc = (x[-1] * r0) / KPC_M
    Mg_Msun   = mg[-1] * (M0 / MSUN_KG)
    Mphi_Msun = mp[-1] * (M0 / MSUN_KG)
    Mtot_Msun = (mg[-1] + mp[-1]) * (M0 / MSUN_KG)

    # diagnostics: median slope in the last 10% of radii
    slope = np.gradient(np.log(y + 1e-300), np.log(x + 1e-300))
    outer_slope = float(np.median(slope[int(0.9*len(slope)):]))

    return dict(
        T0_keV=T0_keV,
        r0_kpc=r0/KPC_M,
        R500_kpc=R500_kpc,
        X_MAX=X_MAX,
        rho0=rho0,
        M0_Msun=M0/MSUN_KG,
        Y0_CENTRAL=Y0_CENTRAL,
        theta_R500=theta(X_MAX),
        r_final_kpc=r_final_kpc,
        M_g_Msun=Mg_Msun,
        M_phi_Msun=Mphi_Msun,
        M_total_Msun=Mtot_Msun,
        Mphi_over_Mg=Mphi_Msun/Mg_Msun,
        outer_slope=outer_slope,
        rho_ratio_R500=y[-1]
    )
```

---

# 5. Reproduced runs (numbers)

Below are three runs reproduced from the project chat log, using the code above.

## Run A: \(Y_{0,\mathrm{central}}=0.23\), steeper decline (\(c_T=0.8\))
- \(\theta(R_{500}) \approx 0.490384\) (so \(T(R_{500})\approx 4.021\ {\rm keV}\))
- \(M_g(R_{500}) \approx 1.828\times 10^{14}\,M_\odot\)
- \(M_\phi(R_{500}) \approx 1.610\times 10^{14}\,M_\odot\)
- \(M_\phi/M_g \approx 0.880308\)

## Run B: \(Y_{0,\mathrm{central}}=0.23\), milder decline (\(c_T\approx 0.35\))
- \(\theta(R_{500}) \approx 0.732166\) (so \(T(R_{500})\approx 6.004\ {\rm keV}\))
- \(M_g(R_{500}) \approx 1.781\times 10^{14}\,M_\odot\)
- \(M_\phi(R_{500}) \approx 1.427\times 10^{14}\,M_\odot\)
- \(M_\phi/M_g \approx 0.801272\)

## Run C: \(Y_{0,\mathrm{central}}=0.18\), same milder decline (\(c_T\approx 0.35\))
- \(\theta(R_{500}) \approx 0.732166\)
- \(M_g(R_{500}) \approx 1.566\times 10^{14}\,M_\odot\)
- \(M_\phi(R_{500}) \approx 1.081\times 10^{14}\,M_\odot\)
- \(M_\phi/M_g \approx 0.690232\)

---

# 6. What this simulation is good for next

A practical next step is to wrap this ODE solver in a likelihood against:
- observed \(T(r)\) and gas density profiles for Coma (or a cluster sample),
- hydrostatic mass bias priors,
- weak-lensing mass calibration at \(R_{500}\).

You can then treat \((Y_{0,\rm central}, c_T, x_t)\) as nuisance parameters and ask whether the required \(M_\phi/M_g\) is consistent across systems.

---

# Dependencies in the project
Extracted from the project chat logs (Coma solver cell) and consistent with the VSU constitutive choices described in:
- `01.1_Action_and_Field_Equations.md`
- `05.1_Nonlinear_Screening_Mechanism.md`
