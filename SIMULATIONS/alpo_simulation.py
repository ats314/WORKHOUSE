"""
ALPO / direction-dependent stiffness oscillator simulation (energy-accounted).

Model:
    m x¨ + c_tot x˙ + k(v) x = - m a_ext(t)
    x is the relative displacement of the proof mass w.r.t. a vibrating base.
    a_ext(t) comes from x_ext(t)=A sin(ωt), so a_ext(t) = -A ω^2 sin(ωt).

Direction-dependent stiffness:
    k(v) = k_soft + (k_stiff-k_soft) * 0.5*(1 - tanh(v/v0))

Energy accounting:
    E(t) = 1/2 m v^2 + 1/2 k(t) x^2
    dE/dt = P_base + P_k - c_tot v^2
    P_base = -m a_ext(t) v
    P_k    = 1/2 (dk/dt) x^2     (computed numerically)

Harvested power is modeled as electrical damping:
    P_load = c_load v^2
Mechanical loss:
    P_mech = c_mech v^2

In steady state: <P_base> + <P_k> ≈ <P_load> + <P_mech>
So if <P_k> > 0, the stiffness modulation is injecting energy (parametric drive)
and must be provided by some mechanism; it is not "free".
"""

from __future__ import annotations
import math
import numpy as np
import pandas as pd


def simulate_alpo(
    m: float = 1.0,
    A: float = 0.01,
    f: float = 5.0,
    k_soft: float = 1000.0,
    k_stiff: float = 5000.0,
    v0: float = 0.01,
    c_mech: float = 1.0,
    c_load: float = 0.0,
    n_periods: int = 200,
    steps_per_period: int = 800,
    transient_periods: int = 100,
) -> dict:
    omega = 2.0 * math.pi * f
    T = 1.0 / f
    dt = T / steps_per_period
    n_steps = int(n_periods * steps_per_period)
    trans_steps = int(transient_periods * steps_per_period)

    c_tot = c_mech + c_load

    # state
    x = 0.0
    v = 0.0

    def a_ext(t: float) -> float:
        return -A * omega * omega * math.sin(omega * t)

    def k_of_v(v: float) -> float:
        s = 0.5 * (1.0 - math.tanh(v / v0))
        return k_soft + (k_stiff - k_soft) * s

    def deriv(t: float, x: float, v: float):
        k = k_of_v(v)
        a = (-c_tot * v - k * x - m * a_ext(t)) / m
        return v, a

    # running averages over analysis window
    sum_P_load = 0.0
    sum_P_mech = 0.0
    sum_P_base = 0.0
    sum_P_k = 0.0
    sum_dE = 0.0

    k_prev = k_of_v(v)
    E_prev = 0.5 * m * v * v + 0.5 * k_prev * x * x

    t = 0.0
    for i in range(n_steps):
        # RK4 step
        k1x, k1v = deriv(t, x, v)
        k2x, k2v = deriv(t + 0.5 * dt, x + 0.5 * dt * k1x, v + 0.5 * dt * k1v)
        k3x, k3v = deriv(t + 0.5 * dt, x + 0.5 * dt * k2x, v + 0.5 * dt * k2v)
        k4x, k4v = deriv(t + dt, x + dt * k3x, v + dt * k3v)

        x_new = x + (dt / 6.0) * (k1x + 2.0 * k2x + 2.0 * k3x + k4x)
        v_new = v + (dt / 6.0) * (k1v + 2.0 * k2v + 2.0 * k3v + k4v)
        t_new = t + dt

        k_now = k_of_v(v_new)
        E_now = 0.5 * m * v_new * v_new + 0.5 * k_now * x_new * x_new

        if i >= trans_steps:
            P_load = c_load * v_new * v_new
            P_mech = c_mech * v_new * v_new
            P_base = -m * a_ext(t_new) * v_new
            P_k = 0.5 * (k_now - k_prev) / dt * x_new * x_new
            dE = (E_now - E_prev) / dt

            sum_P_load += P_load
            sum_P_mech += P_mech
            sum_P_base += P_base
            sum_P_k += P_k
            sum_dE += dE

        # update
        x, v, t = x_new, v_new, t_new
        k_prev, E_prev = k_now, E_now

    n_an = n_steps - trans_steps
    out = {
        "P_load_W": sum_P_load / n_an,
        "P_mech_W": sum_P_mech / n_an,
        "P_base_W": sum_P_base / n_an,
        "P_k_W": sum_P_k / n_an,
        "dE_dt_W": sum_dE / n_an,
    }
    out["balance_error_W"] = (out["P_base_W"] + out["P_k_W"]) - (out["P_load_W"] + out["P_mech_W"] + out["dE_dt_W"])
    out["P_in_total_W"] = out["P_base_W"] + out["P_k_W"]
    out["P_diss_total_W"] = out["P_load_W"] + out["P_mech_W"]
    return out


def sweep_loads(loads, **kwargs) -> pd.DataFrame:
    rows = []
    for cL in loads:
        r = simulate_alpo(c_load=float(cL), **kwargs)
        r["c_load"] = float(cL)
        r["eta_load_over_total_in"] = r["P_load_W"] / r["P_in_total_W"] if r["P_in_total_W"] > 0 else float("nan")
        r["eta_load_over_base_only"] = r["P_load_W"] / r["P_base_W"] if r["P_base_W"] > 0 else float("nan")
        rows.append(r)
    df = pd.DataFrame(rows).set_index("c_load").sort_index()
    return df


if __name__ == "__main__":
    loads = np.linspace(0.0, 20.0, 21)
    df = sweep_loads(loads)
    df.to_csv("alpo_results.csv")
    print(df)
