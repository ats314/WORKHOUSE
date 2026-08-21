# ym_hotrg.py
#
# Basic HOTRG implementation for rank-4 tensors with bond dimension D.
# This file supports:
#   - contracting two neighboring tensors along one axis
#   - reshaping, SVD, truncation to D
#   - building a coarse-grained tensor T'
#
# This is a *numerical engine*; it does NOT know about SU(3) structure.
# We keep it generic so it can be used for various models.
#
# NOTE: The *manual Jacobian* for HOTRG is NOT implemented here.
#       A placeholder API is provided in ym_hotrg_jacobian.py.

from __future__ import annotations
from typing import Tuple
import jax
import jax.numpy as jnp

jax.config.update("jax_enable_x64", True)


def hotrg_merge_vertical(T_up: jax.Array, T_down: jax.Array, chi: int) -> jax.Array:
    """
    Merge two rank-4 tensors along the vertical (2nd index) direction:

        T_up(i, a, j, b),   T_down(k, a, l, c)

    Contract over 'a' to form a rank-6 tensor, then reshape and SVD-truncate
    back to a rank-4 tensor with bond dimension chi.

    Indices convention for T: (left, up, right, down)
    """
    # T_up:   (l,u,r,d)
    # T_down: (l,u,r,d)
    # contract u index: T_merge(l1, u, r1, d1 ; l2, u, r2, d2)
    Tm = jnp.tensordot(T_up, T_down, axes=((1,), (1,)))  # shape (l1,r1,d1, l2,r2,d2)
    l1,r1,d1,l2,r2,d2 = Tm.shape
    Tm = jnp.reshape(Tm, (l1*l2, r1*r2*d1*d2))

    # SVD truncation
    U, S, Vh = jnp.linalg.svd(Tm, full_matrices=False)
    U = U[:, :chi]
    S = S[:chi]
    Vh = Vh[:chi, :]

    M = U @ jnp.diag(jnp.sqrt(S))
    N = jnp.diag(jnp.sqrt(S)) @ Vh

    M = jnp.reshape(M, (l1, l2, chi))         # (l1,l2,chi)
    N = jnp.reshape(N, (chi, r1, r2, d1, d2)) # (chi,r1,r2,d1,d2)

    # assemble coarse tensor: (L, U, R, D) = (l1, chi, r1*r2, d1*d2)
    T_coarse = jnp.einsum("lLc, crRdd2 -> lURD", M, N, optimize=True)
    T_coarse = jnp.reshape(T_coarse, (l1, chi, r1*r2, d1*d2))
    return T_coarse


def hotrg_sweep(T: jax.Array, chi: int, n_steps: int) -> jax.Array:
    """
    Perform a very simple HOTRG sweep that repeatedly merges copies
    of the same tensor along one direction. This is NOT a full 2D HOTRG
    implementation on a finite lattice; instead, it is a toy RG flow
    on a homogeneous tensor network.

    T: rank-4 tensor (l,u,r,d) with all legs of size D.
    chi: truncation dimension.
    n_steps: number of RG iterations.
    """
    def step(T_cur, _):
        T_new = hotrg_merge_vertical(T_cur, T_cur, chi)
        return T_new, None

    T_final, _ = jax.lax.scan(step, T, None, length=n_steps)
    return T_final
