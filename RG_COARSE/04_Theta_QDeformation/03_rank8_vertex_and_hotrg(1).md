# Rank-8 hypercubic vertex tensors and simplified HOTRG coarse graining

This document extracts the *4D tensor-network construction* used throughout the project:
1) how the rank-8 vertex tensor is assembled from spin weights and \(6j\) couplings, and  
2) how it is coarse-grained using a simplified HOTRG-like SVD step.

**Source files:** `CLEANRUN.pdf`, `CLEAN S4.pdf`, `NEWFOURIER.pdf`, `su2_4d_complete_standalone_FIXED.ipynb - Colab.pdf`.

---

## 1. Geometry: why rank-8?

A 4D hypercubic lattice vertex has 8 incident links (two directions along each of the 4 axes: \(\pm \hat x,\pm \hat y,\pm \hat z,\pm \hat t\)). In a spin-network representation where each link is labeled by an SU(2) irrep \(j\), the local tensor at a vertex naturally carries 8 representation indices:

\[
T_{j_1 j_2 j_3 j_4 j_5 j_6 j_7 j_8}.
\]

The project enumerates these indices using a finite spin cutoff
\[
j \in \{0,\tfrac12,1,\ldots,j_{\max}\},
\qquad D=\#\text{spins} = 2 j_{\max}+1.
\]

---

## 2. A minimal (but nontrivial) rank-8 vertex ansatz used in the project

The construction used in the project is a simplified “fusion-tree” amplitude with **one internal channel** \(k\), coupling the eight external spins through two \(6j\) symbols.

A representative schematic form is:
\[
T(\{j_a\})
=
\left(\prod_{a=1}^8 w(j_a)\right)\;
\sum_{k} w(k)\;
\left\{\begin{matrix}
j_1 & j_2 & k\\
j_3 & j_4 & k
\end{matrix}\right\}_{(\cdot)}
\left\{\begin{matrix}
j_5 & j_6 & k\\
j_7 & j_8 & k
\end{matrix}\right\}_{(\cdot)}.
\]

Where:
- \(w(j)\) is a local weight (in the project, a simple Boltzmann-like factor),
- the braces are either classical \(6j\) symbols or \(q\)-deformed ones.

### 2.1 The spin weight used

The project often uses an SU(2)-Casimir-like factor
\[
w(j) \propto (2j+1)\,\exp\!\big(-\beta\,j(j+1)\big),
\]
both for external spins and internal channel \(k\).

This is not the exact Wilson-action character coefficient (which involves Bessel functions), but it is a reasonable “toy YM-like” weight for developing the tensor machinery.

---

## 3. Code skeleton (from the project, reorganized)

The `CLEANRUN.pdf` notebook implements a brute-force vertex builder for small \(j_{\max}\). The essential structure is:

```python
import numpy as np, cmath

def build_rank8_vertex(spins, beta, sixj, q=None):
    # spins: [0, 0.5, ..., j_max]
    # sixj:  callable(j1,j2,j3,j4,j5,j6[,q]) -> complex

    D = len(spins)
    T = np.zeros((D,)*8, dtype=np.complex128)

    def w(j):
        return (2*j+1) * np.exp(-beta*j*(j+1))

    for idx in np.ndindex((D,)*8):
        js = [spins[i] for i in idx]
        w_prod = np.prod([w(j) for j in js])

        term_sum = 0.0 + 0j
        for k in spins:
            wk = w(k)
            if q is None:
                s1 = sixj(js[0],js[1],k, js[2],js[3],k)
                s2 = sixj(js[4],js[5],k, js[6],js[7],k)
            else:
                s1 = sixj(js[0],js[1],k, js[2],js[3],k, q)
                s2 = sixj(js[4],js[5],k, js[6],js[7],k, q)
            term_sum += wk * s1 * s2

        T[idx] = w_prod * term_sum

    # normalization for numerical stability
    norm = np.max(np.abs(T))
    log_norm = cmath.log(norm) if norm > 1e-18 else (-np.inf + 0j)
    if norm > 1e-18:
        T /= norm
    return T, log_norm
```

---

## 4. Simplified HOTRG coarse graining used in the project

A full HOTRG implementation for 4D rank-8 tensors typically:
- contracts tensors along a chosen direction,
- builds isometries from higher-order SVDs,
- truncates bonds direction-by-direction.

The project uses a deliberately simplified surrogate:
- reshape the rank-8 tensor into a matrix \(M\) of size \(D^4\times D^4\),
- do an SVD,
- keep the top \(K\) singular values,
- reshape back to rank-8.

### 4.1 Mathematical picture

Let \(T\) have indices \((a_1,a_2,a_3,a_4)\) and \((b_1,b_2,b_3,b_4)\), each \(a_i,b_i\in\{1,\dots,D\). Flatten:
\[
M_{A,B} = T_{a_1a_2a_3a_4 b_1b_2b_3b_4},
\qquad A\equiv(a_1,a_2,a_3,a_4),\; B\equiv(b_1,b_2,b_3,b_4).
\]

Compute
\[
M = U\,S\,V^\dagger,
\]
truncate \(S\to S_K\) by keeping only the top \(K\) singular values, then
\[
M_{\text{new}} = U_K\,S_K\,V^\dagger_K,
\]
and reshape \(M_{\text{new}}\) back to \(T_{\text{new}}\).

### 4.2 Code skeleton (“RealityWeaver”, from `CLEANRUN.pdf`)

```python
import numpy as np, cmath

class RealityWeaver:
    def __init__(self):
        self.coherence_budget = 0.0j  # accumulated log-normalizations

    def weave_step(self, T: np.ndarray, bond_dim: int) -> np.ndarray:
        D = T.shape[0]
        M = T.reshape(D**4, D**4)

        U, S, Vh = np.linalg.svd(M, full_matrices=False)
        K = min(bond_dim, S.size)

        # accumulate norm-ish contributions
        norm_contribution = np.sum(S[:K])
        if norm_contribution > 1e-18:
            self.coherence_budget += cmath.log(norm_contribution)

        M_new = U[:, :K] @ np.diag(S[:K]) @ Vh[:K, :]
        T_new = M_new.reshape((D,)*8)

        step_norm = np.max(np.abs(T_new))
        if step_norm > 1e-18:
            T_new /= step_norm
            self.coherence_budget += cmath.log(step_norm)

        return T_new
```

---

## 5. How free energy is extracted (and why volume factors matter)

The project computes a log-partition-function estimate from:
- an initial normalization from the vertex builder, plus
- the accumulated \(\log\) normalizations across HOTRG steps, plus
- a final trace/sum of the coarse-grained tensor.

Because each coarse-graining step (conceptually) rescales the effective volume by \(2^4=16\), the code sometimes multiplies accumulated logs by 16 per step.

**Important:** the precise volume factors depend on the exact contraction scheme. If the coarse graining is only a surrogate (as here), the volume scaling is heuristic and should be validated by comparing against exactly solvable limits.

---

## 6. What to improve next (to make this “publishable physics”)

1. Replace the toy weight \(w(j)\) with the correct character-expansion coefficient for the Wilson action (involves modified Bessel functions).
2. Replace the single-channel internal sum with a true 4D vertex amplitude (multiple internal spins; effectively a \(15j\)-like structure).
3. Implement direction-by-direction HOTRG with proper isometries.
4. Validate convergence vs bond dimension \(\chi\) and spin cutoff \(j_{\max}\).
5. Run symmetry and normalization checks at each step to avoid artifacts.

This document is intentionally faithful to what the project currently does, while being explicit about where the “physics fidelity” needs upgrades.
