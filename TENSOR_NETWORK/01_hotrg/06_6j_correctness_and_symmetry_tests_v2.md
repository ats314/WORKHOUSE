# Locking Down the Wigner/Quantum \(6j\): 24 Tetrahedral Symmetries, Canonicalization, and an Orthogonality “Integration Test”

This note is the “trust contract” for any pipeline that builds a 4D SU(2) vertex out of \(6j\) symbols and then tries to infer \(\theta\)-physics from \(F(\theta)=-\log Z(\theta)\).

If the \(6j\) kernel is wrong, *everything* downstream becomes an interpretive Rorschach test.

---

## 1. The one symmetry that keeps biting people: the **full-row swap is not a \(6j\) symmetry**

For the Wigner \(6j\),
\[
\left\{\begin{matrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{matrix}\right\},
\]
it is **not** true in general that
\[
\left\{\begin{matrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{matrix}\right\}
=
\left\{\begin{matrix}
j_4 & j_5 & j_6\\
j_1 & j_2 & j_3
\end{matrix}\right\}.
\]

A concrete counterexample (classical SU(2), verified with SymPy):

- Original: \(\{2,1,2;1,2,1\}\) gives \(\approx 0.07453559925\)
- Full-row swap: \(\{1,2,1;2,1,2\}\) gives \(\approx 0.15275252317\)

So: **delete** any “unit test” that asserts equality under full-row swap.

---

## 2. What the *real* symmetry group is: the 24 tetrahedral symmetries

The Wigner \(6j\) (and the quantum \(6j_q\) computed from a \(q\)-Racah formula) is invariant under the **24 symmetries of the tetrahedron**.  
A clean way to generate them is:

1. Interpret the \(6\) labels as the **edges** of a tetrahedron.
2. Permute the **4 vertices** (\(4!=24\)).
3. Read off the induced permutation of edges.

### 2.1 Edge ↔ \(6j\) label mapping

Use the face-triple structure (the four triangle constraints):
\[
(j_1,j_2,j_3),\quad (j_1,j_5,j_6),\quad (j_4,j_2,j_6),\quad (j_4,j_5,j_3).
\]

Label tetrahedron vertices by which triple meets there:
- vertex 1: \((j_1,j_2,j_3)\)
- vertex 2: \((j_1,j_5,j_6)\)
- vertex 3: \((j_4,j_2,j_6)\)
- vertex 4: \((j_4,j_5,j_3)\)

Then each \(j_k\) is the edge connecting the two vertices whose triples contain it:
\[
\begin{aligned}
j_1 &\leftrightarrow (1,2), &
j_2 &\leftrightarrow (1,3), &
j_3 &\leftrightarrow (1,4),\\
j_4 &\leftrightarrow (3,4), &
j_5 &\leftrightarrow (2,4), &
j_6 &\leftrightarrow (2,3).
\end{aligned}
\]

This mapping reproduces the standard tetrahedral symmetry identities for the classical \(6j\).

---

## 3. Canonicalization rule (cache keys): **only** via the 24 symmetries

Two acceptable choices:

- **No canonical key**: cache only the exact tuple \((j_1,\dots,j_6)\). Simple, always safe.
- **Canonicalize by orbit enumeration**: compute the 24 symmetric tuples and choose one representative (lexicographically smallest is fine).

**Never** canonicalize by “sorting rows”, “sorting columns independently”, or anything that permutes top-row entries without carrying the bottom-row entries along.  
That collapses non-equivalent tetrahedra into the same cache key (a silent correctness killer).

---

## 4. Implementation skeleton (twice-spin integer arithmetic is your friend)

Parity bugs love floats. The most robust representation is:

- store spins as integers \(J=2j\) (so half-integers become odd integers)
- triangle parity becomes “sum is even”

### 4.1 Enumerate the 24 symmetry orbit

```python
import itertools

# Standard edge order for a 6j tuple (J1..J6):
EDGE_ORDER = [(1,2),(1,3),(1,4),(3,4),(2,4),(2,3)]

def tetrahedral_orbit(Js):
    # Js is a 6-tuple (J1..J6) with J=2j integers.
    #
    # Returns the list of distinct tuples in the 24-element tetrahedral orbit
    # (fewer if labels repeat).
    edges = {EDGE_ORDER[i]: Js[i] for i in range(6)}

    out = []
    for perm in itertools.permutations([1,2,3,4]):  # 24 vertex permutations
        p = {1:perm[0], 2:perm[1], 3:perm[2], 4:perm[3]}
        new_edges = {}
        for (a,b), val in edges.items():
            a2, b2 = p[a], p[b]
            if a2 > b2:
                a2, b2 = b2, a2
            new_edges[(a2,b2)] = val

        out.append(tuple(new_edges[e] for e in EDGE_ORDER))

    # unique (preserve order)
    uniq, seen = [], set()
    for t in out:
        if t not in seen:
            uniq.append(t); seen.add(t)
    return uniq

def canonical_key_24(Js):
    return min(tetrahedral_orbit(Js))
```

---

## 5. Replace the bogus symmetry unit test with a 24-symmetry test

### 5.1 Test: invariance under the tetrahedral orbit

```python
import random
import numpy as np

def triangle_ok(Ja,Jb,Jc):
    if abs(Ja-Jb) > Jc: return False
    if Ja+Jb < Jc: return False
    if (Ja+Jb+Jc) % 2 != 0: return False
    return True

def sixj_value(J1,J2,J3,J4,J5,J6, theta=0.0):
    # plug in your implementation here:
    return quantum_6j(J1,J2,J3,J4,J5,J6, theta)

def random_admissible_tuple(Jmax=6, tries=20000):
    for _ in range(tries):
        Js = [random.randint(0, Jmax) for _ in range(6)]
        J1,J2,J3,J4,J5,J6 = Js
        if triangle_ok(J1,J2,J3) and triangle_ok(J1,J5,J6) and triangle_ok(J4,J2,J6) and triangle_ok(J4,J5,J3):
            return tuple(Js)
    raise RuntimeError("could not find admissible 6j tuple")

def test_tetrahedral_symmetry(theta=0.37, ncases=200, rtol=1e-8, atol=1e-12):
    for _ in range(ncases):
        Js = random_admissible_tuple(Jmax=6)  # up to j=3
        v0 = sixj_value(*Js, theta=theta)
        for Js2 in tetrahedral_orbit(Js):
            v2 = sixj_value(*Js2, theta=theta)
            assert abs(v2 - v0) <= atol + rtol*abs(v0)
```

This catches:
- wrong “step size” in the Racah sum,
- wrong triangle/parity gating,
- bad canonicalization that collapses non-equivalent tuples.

### 5.2 Test: canonical key is orbit-invariant

```python
def test_canonical_key_is_orbit_invariant(ncases=200):
    for _ in range(ncases):
        Js = random_admissible_tuple(Jmax=6)
        key = canonical_key_24(Js)
        for Js2 in tetrahedral_orbit(Js):
            assert canonical_key_24(Js2) == key
```

---

## 6. Add the “integration-grade” orthogonality test (this one catches subtle parity/bound bugs)

There is a standard orthogonality identity:
\[
\sum_x (2x+1)
\left\{\begin{matrix}
a & b & x\\
c & d & e
\end{matrix}\right\}
\left\{\begin{matrix}
a & b & x\\
c & d & e'
\end{matrix}\right\}
=
\frac{\delta_{e,e'}}{2e+1}.
\]

In twice-spin units \(J=2j\), the weight is \((2x+1)=J_x+1\) and the RHS is \(\delta/(J_e+1)\).

```python
def allowed_intermediate(Ja,Jb,Jc,Jd):
    Jmin = max(abs(Ja-Jb), abs(Jc-Jd))
    Jmax = min(Ja+Jb, Jc+Jd)
    xs=[]
    for Jx in range(Jmin, Jmax+1):
        if triangle_ok(Ja,Jb,Jx) and triangle_ok(Jc,Jd,Jx):
            xs.append(Jx)
    return xs

def allowed_e_values(Ja,Jd,Jc,Jb):
    Jmin = max(abs(Ja-Jd), abs(Jc-Jb))
    Jmax = min(Ja+Jd, Jc+Jb)
    es=[]
    for Je in range(Jmin, Jmax+1):
        if triangle_ok(Ja,Jd,Je) and triangle_ok(Jc,Jb,Je):
            es.append(Je)
    return es

def test_orthogonality_sum_rule(ncases=100, theta=0.0, tol=1e-8):
    # Orthogonality is strictest/standard at theta=0 where q->1 and sixj is classical.
    for _ in range(ncases):
        Ja,Jb,Jc,Jd = [random.randint(0, 6) for _ in range(4)]
        xs = allowed_intermediate(Ja,Jb,Jc,Jd)
        if not xs:
            continue
        es = allowed_e_values(Ja,Jd,Jc,Jb)
        if not es:
            continue

        Je  = random.choice(es)
        Jep = random.choice(es)

        s = 0.0 + 0.0j
        for Jx in xs:
            w = (Jx + 1)
            s += w * sixj_value(Ja,Jb,Jx,Jc,Jd,Je,theta) * sixj_value(Ja,Jb,Jx,Jc,Jd,Jep,theta)

        target = (1.0/(Je+1)) if (Je == Jep) else 0.0
        assert abs(s - target) < tol
```

Why this test is “integration-grade”:
- it forces *many* admissible \(x\) values to contribute,
- it explodes if your Racah sum bounds are off by \(\pm 1\),
- it is hypersensitive to parity mistakes (using half-steps where you need integer steps, etc.).

---

## 7. Minimal acceptance checklist (before you interpret \(\theta\)-dependence)

1. ✅ tetrahedral (24) symmetry test passes at \(\theta=0\) and a generic \(\theta\neq 0\)
2. ✅ canonicalization key is orbit-invariant (or you turned canonicalization off)
3. ✅ orthogonality sum rule passes at \(\theta=0\)
4. ✅ (bonus) \(6j_q(\theta\to 0)\to 6j\) matches a trusted classical reference

Only after that should you start arguing about whether a \(\theta\)-trend is physics or an indexing mistake wearing a trench coat.
