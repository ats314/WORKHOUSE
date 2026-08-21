# Bianchi constraints as Maxwell–Calladine self-stress
*(Project extraction: “Bianchi constraint functions as a Maxwell–Calladine–type” + corrections + a concrete cube computation)*

## 0. Executive idea
On a lattice, the **linearized Bianchi identity** is the statement that the “boundary of a boundary is zero”:
\[
d_2\,d_1 = 0.
\]
That is formally the same algebraic structure behind **rigidity theory**:

- degrees of freedom (edges / links),
- compatibility constraints (faces / plaquettes),
- and redundancies among constraints (cubes / 3-cells).

In Maxwell–Calladine language, redundancies generate **self-stresses**. Here the “self-stress” is exactly the Bianchi identity: it ties together the face constraints so that certain stress patterns are compatible with *zero displacement*, and that structure can produce **spectral stiffness** in the Hessian-like operators built from $d_1$.

This document packages that into a clean chain‑complex statement, and fixes one notational glitch in the project draft: the natural “Bianchi self‑stress” space is $\operatorname{im}(C^\top)$, not $\ker(C^\top)$.

---

## 1. The chain complex

Let $\mathfrak g$ be a Lie algebra of dimension $d$. Work in a single oriented cube cell complex.

Define real vector spaces
\[
V_E \cong \mathbb R^{|E|d},\qquad V_F \cong \mathbb R^{|F|d},\qquad V_C \cong \mathbb R^{|C|d}
\]
for edge/link variables, face/plaquette strains, and cube “closure” variables.

Let
\[
D:V_E\to V_F,\qquad C:V_F\to V_C
\]
be the **linearized plaquette map** and the **linearized Bianchi map**, with the defining property
\[
C D = 0.
\tag{1.1}
\]

---

## 2. Energetics and the stiffness operator

Let $H:V_F\to V_F$ be symmetric positive semidefinite (face energetics). Define the quadratic energy
\[
\mathcal Q(X)=\frac12\langle DX,\ H\,DX\rangle
\]
and the induced “stiffness” operator on edge space
\[
K := D^\top H D.
\tag{2.1}
\]

### Lemma 2.1 (Basic facts)
1. $K\succeq 0$.
2. $\ker K = \ker D$ provided $H$ is positive definite on $\operatorname{im}(D)$.

A stronger, Bianchi-aware condition is natural:

> **(H–Bianchi)**
> \[
> H\ \text{is positive definite on}\ \ker C.
> \tag{2.2}
> \]

Since $\operatorname{im}(D)\subset \ker C$ by (1.1), (H–Bianchi) implies the condition above.

---

## 3. “Rigidity from redundancy” (spectral bound)
Assume (H–Bianchi). Then on $(\ker D)^\perp$,
\[
\lambda_{\min}\!\left(K\big|_{(\ker D)^\perp}\right)
\ \ge\
\lambda_{\min}\!\left(H\big|_{\ker C}\right)\,
\sigma_{\min}\!\left(D|_{(\ker D)^\perp}\right)^2
\ >\ 0.
\tag{3.1}
\]

This is the cleanest quantitative statement: **as long as face energetics are stiff on Bianchi‑closed strains and $D$ has a uniform singular value bound on non-mechanisms, you get a spectral gap in $K$.**

---

## 4. Maxwell–Calladine index in the chain‑complex setting

In classic rigidity, the index relates:
- mechanisms $m = \dim \ker D$ (edge motions that create no strain),
- self-stresses $s = \dim \ker D^\top$ (face stress patterns that produce zero net force).

In the presence of a second boundary map $C$ with $CD=0$, there is a canonical subspace of self-stresses:
\[
\operatorname{im}(C^\top)\subseteq \ker(D^\top).
\tag{4.1}
\]

So a natural “Bianchi self-stress count” is
\[
s_{\text{Bianchi}} := \dim \operatorname{im}(C^\top) = \operatorname{rank}(C).
\tag{4.2}
\]

A corresponding index identity at the linear algebra level is
\[
m - s_{\text{Bianchi}}
=
\dim V_E - \operatorname{rank}(D) - \operatorname{rank}(C).
\tag{4.3}
\]
This matches the cube computation below.

*(Note: the project draft wrote $\dim\ker(C^\top)$ in one place; that’s not the right object for “redundancy/self-stress” in this complex.)*

---

## 5. Concrete cube computation (d = 1)
Below is an explicit incidence-matrix realization for a single cube with:

- 12 oriented edges (positive coordinate direction)
- 6 oriented faces (boundary orientation induced by the cube orientation)
- 1 cube

Then $C$ is the “sum of oriented faces” map, and one checks $CD=0$.

### Python code
```python
import numpy as np
import numpy.linalg as la

# Edge list (12)
edges=[]
for y in [0,1]:
    for z in [0,1]:
        edges.append(((0,y,z),(1,y,z),'x'))
for x in [0,1]:
    for z in [0,1]:
        edges.append(((x,0,z),(x,1,z),'y'))
for x in [0,1]:
    for y in [0,1]:
        edges.append(((x,y,0),(x,y,1),'z'))
edge_index={e:i for i,e in enumerate(edges)}

def edge_var_and_sign(v_from, v_to):
    dx=v_to[0]-v_from[0]; dy=v_to[1]-v_from[1]; dz=v_to[2]-v_from[2]
    axis='x' if dx else ('y' if dy else 'z')
    if (v_from,v_to,axis) in edge_index: return edge_index[(v_from,v_to,axis)], +1
    if (v_to,v_from,axis) in edge_index: return edge_index[(v_to,v_from,axis)], -1
    raise KeyError

# Faces as vertex cycles, oriented as induced boundary orientation of the cube
faces = {
    'px+': [(1,0,0),(1,1,0),(1,1,1),(1,0,1),(1,0,0)],
    'px-': [(0,0,0),(0,0,1),(0,1,1),(0,1,0),(0,0,0)],
    'py+': [(0,1,0),(0,1,1),(1,1,1),(1,1,0),(0,1,0)],
    'py-': [(0,0,0),(1,0,0),(1,0,1),(0,0,1),(0,0,0)],
    'pz+': [(0,0,1),(1,0,1),(1,1,1),(0,1,1),(0,0,1)],
    'pz-': [(0,0,0),(0,1,0),(1,1,0),(1,0,0),(0,0,0)]
}
face_names=list(faces.keys())

D=np.zeros((6,12),dtype=int)
for fi,fname in enumerate(face_names):
    path=faces[fname]
    for a,b in zip(path[:-1],path[1:]):
        ei,sg=edge_var_and_sign(a,b)
        D[fi,ei]+=sg

# Cube boundary operator: sum of the 6 boundary faces (rank 1)
C=np.ones((1,6),dtype=int)

print("Check CD:", (C@D))
print("rank(D):", la.matrix_rank(D.astype(float)))
print("rank(C):", la.matrix_rank(C.astype(float)))

K=D.T@D
eig=la.eigvalsh(K)
pos=eig[eig>1e-8]
print("nonzero eigenvalues:", pos)
print("min positive eigenvalue:", pos.min())
```

### Numerical output (what you should see)
- $CD = 0$ exactly.
- $\operatorname{rank}(D)=5$, $\operatorname{rank}(C)=1$.
- $K=D^\top D$ has eigenvalues:
  \[
  \{0,\dots,0,4,4,4,6,6\}
  \]
  so the spectral gap on $(\ker D)^\perp$ is $4$.

The index check:
\[
m=\dim\ker D = 12-\operatorname{rank}(D)=7,\qquad
s_{\text{Bianchi}}=\operatorname{rank}(C)=1,
\]
so
\[
m-s_{\text{Bianchi}}=6
=
12-\operatorname{rank}(D)-\operatorname{rank}(C).
\]

---

## 6. How this connects back to lattice gauge theory
In the full lattice gauge setting:

- $D$ is the linearized map from link Lie-algebra variables to plaquette curvature variables,
- $C$ is the linearized Bianchi map (cube closure),
- gauge degrees of freedom appear as a subspace of $\ker D$ (and in the full complex via $d_0$).

The project’s larger geometric picture is: **Bianchi redundancy behaves like a self-stress that stabilizes (“stiffens”) the physical directions**, and that “stiffness” is exactly what functional-inequality machinery needs to manufacture a spectral gap.

---

## 7. Next directions (where this could become a real theory rather than a metaphor)

1. **Global assembly with boundary conditions.**  
   Prove a volume‑uniform lower bound on $\sigma_{\min}(D|_{(\ker D)^\perp})$ for a full lattice complex modulo gauge (a discrete Hodge estimate).

2. **Energetic generalization.**  
   Incorporate heterogenous stiffness/prestress à la generalized Maxwell–Calladine frameworks (e.g., susceptibility-based versions). This is the correct way to track “energetics” rather than pure counting.

3. **Bridge to curvature / Bakry–Émery.**  
   Interpret $K$ as a Hessian-like curvature operator for the Wilson action restricted to physical directions; then use it as a pointwise input to log-Sobolev/Poincaré machinery.

