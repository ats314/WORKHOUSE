# ym_hotrg_jacobian.py
#
# Scaffold for the HOTRG Jacobian. For now, this uses JAX autodiff to obtain
# a Jacobian-vector product (JVP) and vector-Jacobian product (VJP) for the
# HOTRG merge step defined in ym_hotrg.py.
#
# This is NOT the full manual SVD-perturbation implementation we discussed.
# It is explicitly marked as such. You can later replace the autodiff logic
# with a hand-coded SVD derivative while keeping the same API.

from __future__ import annotations
from typing import Callable, Tuple
import jax
import jax.numpy as jnp

jax.config.update("jax_enable_x64", True)

from ym_hotrg import hotrg_merge_vertical


def hotrg_merge_vjp_fun(T_up: jax.Array, T_down: jax.Array, chi: int):
    """
    Return:
        f(T_up, T_down) = T_coarse
    and a function vjp(g) that gives (grad_T_up, grad_T_down).
    """
    def f(Tu, Td):
        return hotrg_merge_vertical(Tu, Td, chi)

    y, vjp = jax.vjp(f, T_up, T_down)
    return y, vjp


def hotrg_jacobian_apply_vjp(T_up: jax.Array,
                             T_down: jax.Array,
                             chi: int,
                             g: jax.Array) -> Tuple[jax.Array, jax.Array]:
    """
    Apply J^T to a "gradient" tensor g, returning contributions to
    dS/dT_up and dS/dT_down, interpreted as vector-Jacobian product.

    This is effectively:
        (dS/dT_up, dS/dT_down) = J^T g

    where J is the Jacobian of the HOTRG merge.
    """
    _, vjp = hotrg_merge_vjp_fun(T_up, T_down, chi)
    grad_T_up, grad_T_down = vjp(g)
    return grad_T_up, grad_T_down


def hotrg_jvp(T_up: jax.Array,
              T_down: jax.Array,
              chi: int,
              dT_up: jax.Array,
              dT_down: jax.Array) -> jax.Array:
    """
    Jacobian-vector product: compute J · v where v = (dT_up, dT_down),
    using JAX's jvp on the HOTRG merge.

    This is again using autodiff for now, *not* a hand-derived SVD perturbation.
    """
    def f(Tu, Td):
        return hotrg_merge_vertical(Tu, Td, chi)

    y, dy = jax.jvp(f, (T_up, T_down), (dT_up, dT_down))
    return dy
