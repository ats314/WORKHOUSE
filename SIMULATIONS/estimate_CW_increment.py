#!/usr/bin/env python3
# Estimate the Wilson Hessian increment constant C_W using HVPs + power iteration.
#
# IMPORTANT: You must estimate ||H(A)-H(0)||, not ||H(A)||, otherwise you'll see ~1/r^2 blowup.

import numpy as np
import jax
import jax.numpy as jnp

# --- Utilities ---

def hvp_of_action(action_fn, theta, v):
    g = jax.grad(action_fn)
    return jax.jvp(g, (theta,), (v,))[1]

def opnorm_power_iteration(hvp_M, key, dim, n_iter=40):
    v = jax.random.normal(key, (dim,), dtype=jnp.float32)
    v = v / (jnp.linalg.norm(v) + 1e-12)
    for _ in range(n_iter):
        w = hvp_M(v)
        nw = jnp.linalg.norm(w) + 1e-12
        v = w / nw
    w = hvp_M(v)
    return jnp.abs(jnp.vdot(v, w))

# --- Example theta sampler ---
def theta_sampler_gaussian(key, dim, r):
    # Sample theta then clip to enforce ||theta||_inf <= r
    theta = jax.random.normal(key, (dim,), dtype=jnp.float32)
    theta = theta / (jnp.max(jnp.abs(theta)) + 1e-12)
    return r * theta

# --- Main estimator ---
def estimate_CW(action_fn, beta, r, key, dim, n_samples=16, n_iter=40):
    theta0 = jnp.zeros((dim,), dtype=jnp.float32)
    def hvp0(v): return hvp_of_action(action_fn, theta0, v)

    cws = []
    k = key
    for _ in range(n_samples):
        k, kA, kPI = jax.random.split(k, 3)
        theta = theta_sampler_gaussian(kA, dim, r)
        def hvpA(v): return hvp_of_action(action_fn, theta, v)
        def hvpM(v): return hvpA(v) - hvp0(v)

        opn = opnorm_power_iteration(hvpM, kPI, dim, n_iter=n_iter)
        cws.append(opn / (beta * (r**2)))
    return float(jnp.max(jnp.array(cws))), cws

