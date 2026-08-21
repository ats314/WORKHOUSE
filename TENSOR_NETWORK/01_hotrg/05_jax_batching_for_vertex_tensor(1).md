# Fast tensor generation: JAX log-space \(6j\) + batching patterns

This document extracts the most practically useful *computational physics* contribution in the project: how to make the insane combinatorics of \(6j\) symbols and rank-8 tensors tractable with JAX.

**Source files:** `NEWFOURIER.pdf`, `BATCH J3.pdf`, `BATCH J4 WORKING.pdf`, `EFFICIENT CODE RUNS.pdf`, `GTP5.1 ATTEMPT.pdf`, plus the “Untitled76 … FLATTENED VMAP GENERATOR” notebook.

---

## 1. The problem

Even at modest \(j_{\max}\), the 4D vertex tensor has \(D^8\) elements, and many of those elements require summing internal channels and evaluating multiple \(6j\) symbols.

Naively:
- computing a single \(6j\) uses a Racah sum over \(z\),
- computing a vertex element uses internal sums over \(k\),
- computing the full tensor is \(D^8\) vertex elements.

So the project leans heavily on:
- **log-space arithmetic** (to avoid overflow/underflow),
- **vectorization (`vmap`)**,
- **JIT compilation**,
- and **batching**.

---

## 2. Stable classical \(6j\) in log space (JAX-friendly)

A good classical baseline is to compute factorials via \(\Gamma\)-functions:
\[
\log(n!) = \log\Gamma(n+1),
\]
which supports half-integers cleanly.

### 2.1 Log factorial helper

```python
import jax, jax.numpy as jnp
from jax.scipy.special import gammaln

def log_factorial(x):
    # x can be integer or half-integer >=0
    return gammaln(x + 1.0)
```

### 2.2 Racah sum structure in JAX

The notebooks implement a fixed-range loop over \(z\) with masking:
- pick an upper bound `Z_MAX` (e.g. 40–80),
- build a `z_vals = jnp.arange(Z_MAX)`,
- mask out invalid z that violate the factorial arguments.

This avoids Python loops inside `jit`.

---

## 3. Caching: you never want to recompute the same \(6j\)

For fixed \(j_{\max}\), the number of distinct \(6j\) values is far smaller than the number of times you need them inside tensor construction.

The project uses **canonicalization** of the 6 arguments:
- sort within columns,
- sort columns,
- possibly apply row swaps,

to map a \(6j\) to a unique key, then store it in a cache.

This is especially useful in non-JAX Python runs.

---

## 4. The rank-8 tensor: flatten + vmap + batch

### 4.1 The key trick

Instead of 8 nested Python loops over indices, do:

1. enumerate *all* index tuples, shape \((N,8)\) where \(N=D^8\),
2. `vmap` a `compute_vertex_element(indices)` function,
3. reshape result back to \((D,D,D,D,D,D,D,D)\).

### 4.2 But \(D^8\) is enormous, so batch it

Even for \(D=5\), \(D^8=390625\). For \(D=9\), \(D^8 \approx 43\) million (nope).

So the project implements batching like:

```python
def generate_tensor_batched(all_indices, batch_size, compute_fn):
    out = []
    n = all_indices.shape[0]
    for i in range(0, n, batch_size):
        batch = all_indices[i:i+batch_size]
        out.append(compute_fn(batch))   # compute_fn is vmapped+jitted
    return jnp.concatenate(out, axis=0)
```

### 4.3 A canonical pattern

```python
import itertools
import jax, jax.numpy as jnp

def all_index_tuples(D):
    # Beware: materializing this is only OK for small D.
    return jnp.array(list(itertools.product(range(D), repeat=8)), dtype=jnp.int32)

@jax.jit
def compute_batch(batch_idx):
    # batch_idx: (B, 8)
    # return: (B,) complex or float
    return jax.vmap(compute_vertex_element)(batch_idx)

# then:
idx = all_index_tuples(D)
vals = generate_tensor_batched(idx, batch_size=4096, compute_fn=compute_batch)
T = vals.reshape((D,)*8)
```

This is essentially what the “FLATTENED VMAP GENERATOR” notebook demonstrates.

---

## 5. A practical recommendation hierarchy

If you only have time for one engineering upgrade, do this:

1. **Correctness first:** validate the classical \(6j\) against SymPy for random small spins.
2. **Then performance:**
   - move \(6j\) to JAX with `jit`,
   - batch your tensor element evaluation,
   - avoid Python loops over tensor indices.

Only after the classical pipeline is solid should you attempt \(q\)-deformed \(6j\) in JAX, because:
- \(q\)-factorials at \(q=e^{i\theta}\) can have zeros and complex phases,
- phase tracking + log-space needs extra care.

---

## 6. Where this becomes “new physics enabled by new compute”

If the \(q=e^{i\theta}\) deformation idea is physically meaningful, then the bottleneck is not “theory”, it’s *making the calculation feasible* beyond tiny cutoffs.

The JAX batching pipeline is the part that scales to:
- larger \(j_{\max}\),
- larger bond dimensions \(\chi\),
- finer \(\theta\)-grids,

which is exactly what you need to test whether the \(\theta\to q\) hypothesis survives beyond toy sizes.
