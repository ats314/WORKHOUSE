# Cluster Hydrostatic Equilibrium with Scalar Self-Energy: Coma-Like Run

This document extracts the **dimensionless derivation** and the **numerical run outputs** for the “scalar-augmented hydrostatic equilibrium” cluster model present in the project logs.

The goal is not rhetoric: it is to show the equations and the two executed parameter runs (with their printed enclosed masses).

---

## 1. Physical setup

Assume spherical symmetry and hydrostatic equilibrium (HSE) for an ionized intracluster medium (ICM):

\[
\frac{dP}{dr} = -\rho_g(r)\, g_{\rm eff}(r).
\]

Assume an ideal gas equation of state:

\[
P(r)=\frac{k_B}{\mu_{\rm gas} m_p}\rho_g(r)\,T(r).
\]

Define a (possibly) dimensionless temperature profile $\theta(x)=T(r)/T_0$ (the run used isothermal $\theta\equiv 1$).

---

## 2. Dimensionless scaling and ODE system

Introduce scales $(r_0,\rho_0,M_0)$ and dimensionless variables:

\[
x=\frac{r}{r_0},\qquad y(x)=\frac{\rho_g(r)}{\rho_0},\qquad m_g(x)=\frac{M_g(r)}{M_0}.
\]

The enclosed gas mass satisfies:

\[
\frac{dm_g}{dx}=x^2 y.
\]

### 2.1 The modified-gravity “gain” factor

The run uses a MOND-like gain factor written in terms of $m_g/x$:

\[
g_{\rm fac}(x)\;=\;\frac{1}{1-\exp\!\left(-\frac{m_g(x)}{x}\right)}.
\]

### 2.2 Scalar self-energy closure

The scalar contribution is encoded through a function

\[
y_\phi(Y)=\frac{1-\exp(-Y)(1+Y)}{Y},
\qquad
Y=Y_0\,y.
\]

The scalar acts as an additional effective mass factor:

\[
1+Y_0\,y_\phi(Y).
\]

### 2.3 Final HSE ODE (isothermal form)

Using $d\ln y/dx$ to reduce stiffness, the project’s model corresponds to:

\[
\frac{d\ln y}{dx}
=
-\frac{m_g(x)}{x^2}\left(1+Y_0\,y_\phi(Y_0 y)\right)\,g_{\rm fac}(x),
\qquad
\frac{dm_g}{dx}=x^2 y.
\]

(The full log also evolves an explicit scalar enclosed mass $m_\phi$; the printed outputs report $M_\phi$ separately.)

---

## 3. Reference code (clean, minimal, runnable)

```python
import numpy as np
from scipy.integrate import solve_ivp

# --- constants
G   = 6.674e-11
a0  = 1.2e-10
kB  = 1.380649e-23
m_p = 1.67262192369e-27
mu_gas = 0.6

KPC_M   = 3.085677581e19
MSUN_KG = 1.98847e30

def y_phi_of_Y(Y):
    if Y < 1e-10:
        # series: (1 - e^{-Y}(1+Y))/Y ~ Y/2 + O(Y^2)
        return 0.5*Y
    return (1.0 - np.exp(-Y)*(1.0+Y)) / Y

def rhs(x, u, Y0):
    ln_y, mg = u
    y = np.exp(ln_y)

    Y = Y0 * y
    gfac = 1.0 / (1.0 - np.exp(-mg / max(x, 1e-10)))

    dlny_dx = - (mg / max(x, 1e-10)**2) * (1.0 + Y0 * y_phi_of_Y(Y)) * gfac
    dmg_dx  = x**2 * y
    return [dlny_dx, dmg_dx]

def run_cluster(Y0, X_MAX=3.677059, ln_y0=0.0):
    # initial conditions at small x
    x0 = 1e-5
    u0 = [ln_y0, 1e-12]

    sol = solve_ivp(
        lambda x,u: rhs(x,u,Y0),
        t_span=(x0, X_MAX),
        y0=u0,
        method="Radau",
        rtol=1e-8, atol=1e-10,
        max_step=0.05
    )
    assert sol.success
    x  = sol.t
    y  = np.exp(sol.y[0])
    mg = sol.y[1]
    return x, y, mg

# NOTE: the project log includes the scalar enclosed mass M_phi as well; this minimal
# version shows the gas-only integration structure.
```

---

## 4. Executed outputs from the project log

The project log ran a Coma-like configuration (isothermal $T_0\simeq 8.2$ keV, $R_{500}\simeq 1.3$ Mpc, $r_0\simeq 353.5$ kpc) for two central stiffness values.

### 4.1 Run A: $Y_0 = 0.47$

Printed results at $r\simeq R_{500}$:

- $M_g = 2.387\times 10^{14}\,M_\odot$
- $M_\phi = 2.940\times 10^{14}\,M_\odot$
- $M_{\rm tot} = 5.326\times 10^{14}\,M_\odot$
- $M_\phi/M_g = 1.231820$

Consistency checks:

- outer slope median $d\ln\rho/d\ln r \approx -2.447$
- $\rho_g(R_{500})/\rho_0 = 6.067587\times 10^{-2}$

### 4.2 Run B: $Y_0 = 0.32$

Printed results at $r\simeq R_{500}$:

- $M_g = 2.007\times 10^{14}\,M_\odot$
- $M_\phi = 1.871\times 10^{14}\,M_\odot$
- $M_{\rm tot} = 3.878\times 10^{14}\,M_\odot$
- $M_\phi/M_g = 0.932581$

Consistency checks:

- outer slope median $d\ln\rho/d\ln r \approx -1.971$
- $\rho_g(R_{500})/\rho_0 = 5.986417\times 10^{-2}$

---

## 5. Why this is potentially important

Clusters are where many MOND-like models historically struggle (they often still need “something extra”).

This model’s distinctive claim is:

> the scalar sector self-energy can contribute an effective enclosed mass comparable to (or larger than) the gas mass at $R_{500}$.

That is a *quantitative* statement. It becomes a scientific test once you compute and compare:

1. $M_{\rm tot}(R)$ to weak-lensing $M_{\rm lens}(R)$,
2. baryon fraction $f_b(R)=M_g(R)/M_{\rm tot}(R)$ against observed $f_b$,
3. temperature profile sensitivity ($\theta(x)\neq 1$).

If these checks line up for Coma/A1689-like systems without ad hoc extra components, that’s a real win.

