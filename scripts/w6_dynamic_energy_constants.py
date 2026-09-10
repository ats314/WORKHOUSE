"""
Compute exact symbolic and numerical values for W6 residual bound constants
a and c from the G19 dynamic fiber covariance and Lie-cubic energy estimates.

References:
- paper/research_notes/G19_DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY_20260906.md
- runs/recent_research_integration_2026-09-09/sources/w6_continuation_20260909/W6_PATH_FORWARD.md
"""

from __future__ import annotations

import json
import math
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class W6Constants:
    L: int
    dim_G: int
    C_A: int
    beta_G: float
    M0: float
    v: float
    c_spec: float
    a_spec: float
    sigma_bar: float
    term1_m4: float
    term2_m2: float
    term3_m0: float
    bracket_sum: float
    K_F: float
    C_B: float
    C_L: float
    a_const: float
    c_const: float
    kappa: float
    g0: float
    w6_bound_factor: float


def compute_w6_constants(
    L: int = 2,
    dim_G: int = 3,
    C_A: int = 2,
    beta_G: float = 1.0,
    M0: float = 0.5,
    v: float = 1.0,
    A: float = 6.0,
    a_star: float = 12.0,
    S_bar: float = 4.1887902047863905,  # 4 * pi / 3
    C_B: float = 1.0,
    C_L: float = 1.0,
    kappa: float = 0.5,
    g0: float = 0.1,
) -> W6Constants:
    """
    Compute explicit values for:
      |d[u,u]| <= a |g| b[p]
      ||rho_p||_{ell^*} <= c |g| b[p]^(1/2)
    and the resulting W6 factor (a + kappa^(-1) * c^2 * g0).
    """
    sqrt_33 = math.sqrt(33.0)
    c_spec = 1.0 / (sqrt_33 * L)
    a_spec = c_spec / 2.0
    sigma_bar = sqrt_33 * L / 2.0

    # Three terms inside the bracket of Eq. (16) in G19 note:
    # 1. 9 * beta_G^2 * M0^4 / (a_spec * v^2) = 18 * sqrt(33) * L * beta_G^2 * M0^4 / v^2
    term1 = 18.0 * sqrt_33 * L * (beta_G**2) * (M0**4) / (v**2)

    # 2. 18 * C_A * M0^2 * sigma_bar / ((a_spec + c_spec) * v^3) = 198 * C_A * L^2 * M0^2 / v^3
    term2 = 198.0 * C_A * (L**2) * (M0**2) / (v**3)

    # 3. 6 * C_A * dim_G * sigma_bar^2 / ((a_spec + 2 * c_spec) * v^4)
    #    = (99 * sqrt(33) / 5) * C_A * dim_G * L^3 / v^4
    term3 = (99.0 * sqrt_33 / 5.0) * C_A * dim_G * (L**3) / (v**4)

    bracket = term1 + term2 + term3
    K_F = A * a_star * S_bar * bracket

    # From W6_PATH_FORWARD.md Section 3:
    # ||rho_p||_{ell^*} <= c |g| b[p]^(1/2) with c = sqrt(C_B * C_L * K_F)
    # |d[u,u]| <= a |g| b[p] with a = C_B * K_F
    a_const = C_B * K_F
    c_const = math.sqrt(C_B * C_L * K_F)

    # Variational W6 bound factor from (R4):
    # |<t, (A_g^(-1) - A_0^(-1)) t>| <= (a + kappa^(-1) * c^2 * g0) |g| b[p]
    w6_bound_factor = a_const + (1.0 / kappa) * (c_const**2) * g0

    return W6Constants(
        L=L,
        dim_G=dim_G,
        C_A=C_A,
        beta_G=beta_G,
        M0=M0,
        v=v,
        c_spec=c_spec,
        a_spec=a_spec,
        sigma_bar=sigma_bar,
        term1_m4=term1,
        term2_m2=term2,
        term3_m0=term3,
        bracket_sum=bracket,
        K_F=K_F,
        C_B=C_B,
        C_L=C_L,
        a_const=a_const,
        c_const=c_const,
        kappa=kappa,
        g0=g0,
        w6_bound_factor=w6_bound_factor,
    )


def main() -> int:
    print("================================================================================")
    print("W6 Variational Residual & Diagonal Constants (G19 Dynamic Fiber Energy)")
    print("================================================================================")

    results = {}
    for L_val in [2, 3, 4, 8]:
        res = compute_w6_constants(L=L_val)
        results[f"L_{L_val}"] = asdict(res)
        print(f"\n--- Block scale L = {L_val} (SU(2), v = 1.0, M0 = 0.5) ---")
        print(f"  c_spec               = {res.c_spec:.6e}")
        print(f"  term 1 (M0^4)        = {res.term1_m4:.6f}")
        print(f"  term 2 (M0^2)        = {res.term2_m2:.6f}")
        print(f"  term 3 (M0^0)        = {res.term3_m0:.6f}")
        print(f"  bracket sum          = {res.bracket_sum:.6f}")
        print(f"  K_F (Schur bound)    = {res.K_F:.6e}")
        print(f"  Constant a (diag)    = {res.a_const:.6e}")
        print(f"  Constant c (resid)   = {res.c_const:.6e}")
        print(f"  W6 factor (a+c^2*g0/k)= {res.w6_bound_factor:.6e}")

    out_path = Path(__file__).resolve().parent / "w6_dynamic_energy_constants.json"
    out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\n[OK] Results written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
