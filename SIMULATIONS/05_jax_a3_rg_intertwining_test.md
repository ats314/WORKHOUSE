# GPU-Ready JAX Skeleton to Empirically Test (A3): RG Gradient Intertwining

## Goal
Empirically estimate (on your A100) the constant
\[
C_{\mathrm{RG}}^{\mathrm{emp}} \approx \sup_{U,v}\; R(U,v),\qquad
R(U,v) := \frac{\bigl|\nabla (F_v\circ \pi)(U)\bigr|^2}{\bigl(|\nabla F_v|^2\circ \pi\bigr)(U)},
\]
for a block-spin map \(\pi\) defined by **geodesic (Karcher) averaging on \(\mathrm{SU}(2)\)**, using linear test functions
\[
F_v(V) := \langle v,\log(V)\rangle,\qquad v\in\mathbb{R}^3,
\]
which are the right probes in the linearized regime.

This file is deliberately *just* a skeleton you can drop into one JAX notebook cell and run; it is written to be batchable.

---

## One-cell JAX code

```python
# ======= One-cell JAX script: RG intertwining test for SU(2) geodesic averaging =======
# Requirements:
#   pip install "jax[cuda12]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
#
# Notes:
#   - Represents SU(2) as unit quaternions q = (w, xyz) with w in R and xyz in R^3.
#   - Uses principal-branch log, valid when samples stay in a normal neighborhood.
#   - Karcher mean is computed by a standard fixed-point iteration:
#       q_{t+1} = q_t * exp( mean_i log(q_t^{-1} * q_i) )
#   - The test function is F_v(q) = <v, log(q)>, so |∇F_v|^2 = |v|^2 under Euclidean Lie-algebra metric.

import jax
import jax.numpy as jnp
from jax import jit, vmap, grad, random, lax

# -------------------------
# Quaternion utilities
# -------------------------
def q_normalize(q):
    return q / (jnp.linalg.norm(q, axis=-1, keepdims=True) + 1e-12)

def q_conj(q):
    return jnp.concatenate([q[..., :1], -q[..., 1:]], axis=-1)

def q_mul(a, b):
    aw, av = a[..., :1], a[..., 1:]
    bw, bv = b[..., :1], b[..., 1:]
    w = aw * bw - jnp.sum(av * bv, axis=-1, keepdims=True)
    v = aw * bv + bw * av + jnp.cross(av, bv)
    return jnp.concatenate([w, v], axis=-1)

# -------------------------
# SU(2) exp / log in exponential (Lie algebra) coordinates
# -------------------------
def su2_exp(x):
    # x: (...,3) Lie algebra coords; map to unit quaternion exp(x)
    r = jnp.linalg.norm(x, axis=-1, keepdims=True)
    half = 1.0  # convention knob; keep =1 for consistency
    rr = half * r
    w = jnp.cos(rr)
    s = jnp.sin(rr) / (r + 1e-12)
    v = s * x
    return q_normalize(jnp.concatenate([w, v], axis=-1))

def su2_log(q):
    # q: (...,4) unit quaternion -> x in R^3 (principal log, rr in [0,pi])
    q = q_normalize(q)
    w = jnp.clip(q[..., 0:1], -1.0, 1.0)
    v = q[..., 1:]
    vnorm = jnp.linalg.norm(v, axis=-1, keepdims=True)
    rr = jnp.arctan2(vnorm, w)
    x = rr * v / (vnorm + 1e-12)
    return x

# -------------------------
# Karcher (geodesic) mean on SU(2)
# -------------------------
def karcher_mean_quat(qs, num_iters=20, step=1.0):
    # qs: (...,N,4) batch of unit quaternions
    qs = q_normalize(qs)
    q0 = q_normalize(jnp.mean(qs, axis=-2))  # extrinsic init

    def body(q, _):
        dq = q_mul(q_conj(q)[..., None, :], qs)  # (...,N,4)
        logs = su2_log(dq)                       # (...,N,3)
        delta = jnp.mean(logs, axis=-2)          # (...,3)
        q_next = q_mul(q, su2_exp(step * delta))
        q_next = q_normalize(q_next)
        return q_next, None

    qT, _ = lax.scan(body, q0, xs=None, length=num_iters)
    return qT

# -------------------------
# Block map π and test functional F_v
# -------------------------
def block_map_pi(x_block, num_iters=20):
    # x_block: (...,N,3) Lie algebra coords for N fine links in one block
    qs = su2_exp(x_block)                        # (...,N,4)
    return karcher_mean_quat(qs, num_iters=num_iters, step=1.0)

def F_v_of_V(V, v):
    y = su2_log(V)
    return jnp.sum(y * v, axis=-1)

# -------------------------
# R(U,v) computation
# -------------------------
def R_ratio(x_block, v, num_iters=20):
    # x_block: (N,3) fine coords for one block
    # v: (3,)
    def scalar_fn(xflat):
        x = xflat.reshape(x_block.shape)
        V = block_map_pi(x, num_iters=num_iters)
        return F_v_of_V(V, v)

    g = grad(scalar_fn)(x_block.reshape(-1))
    g = g.reshape(x_block.shape)  # (N,3)

    num = jnp.sum(g * g)          # |∇(F∘π)|^2
    den = jnp.sum(v * v) + 1e-12  # |∇F|^2 at coarse, for linear F_v
    return num / den

R_ratio_batched = jit(vmap(R_ratio, in_axes=(0, 0, None)))

# -------------------------
# Sampling driver (batchable)
# -------------------------
@jit
def sample_small_field(key, batch_size, N=16, sigma=0.05):
    return sigma * random.normal(key, (batch_size, N, 3))

@jit
def sample_v(key, batch_size):
    v = random.normal(key, (batch_size, 3))
    return v / (jnp.linalg.norm(v, axis=-1, keepdims=True) + 1e-12)

def run_experiment(seed=0, batch_size=1024, N=16, sigma=0.05, num_iters=20):
    key = random.PRNGKey(seed)
    k1, k2 = random.split(key)
    x = sample_small_field(k1, batch_size, N=N, sigma=sigma)
    v = sample_v(k2, batch_size)

    R = R_ratio_batched(x, v, num_iters)  # (B,)
    return {
        "mean_R": float(jnp.mean(R)),
        "std_R": float(jnp.std(R)),
        "max_R": float(jnp.max(R)),
        "min_R": float(jnp.min(R)),
    }

# Example (uncomment when running interactively):
# stats = run_experiment(seed=0, batch_size=4096, N=16, sigma=0.05, num_iters=25)
# print(stats)
# Expectation in linearized regime: mean_R ~ 1/N ≈ 0.0625 and max_R not far above.
```

---

## Interpreting outputs (what to look for)
- In the **small-field** regime (e.g. `sigma=0.02–0.08`), you expect:
  - `mean_R` close to \(1/N = 1/16 \approx 0.0625\),
  - `max_R` not drifting upward as you increase batch size,
  - stability in `mean_R` as you vary `num_iters`.

- If `max_R` or `mean_R` climbs noticeably above \(0.1\) *even at very small sigma*, your Karcher iteration may be leaving the normal neighborhood or your log branch is misbehaving. Fix by reducing sigma or adding step damping / line search.

- To stress-test beyond small field, increase `sigma` and watch whether the ratio stays controlled; if it blows up, that’s a real warning that (A3) is only small-field unless you change \(\pi\) (e.g. switch to decimation).

---

## What this does *not* prove
- This is an *empirical de-risking harness*, not a proof.
- It checks exactly the kinematic inequality (A3) for the geodesic-mean \(\pi\), and tells you where it might fail (branch cuts / loss of convexity / large dispersion).

