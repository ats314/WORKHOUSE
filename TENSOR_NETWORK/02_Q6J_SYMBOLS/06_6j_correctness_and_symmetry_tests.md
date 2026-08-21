# Locking Down the Wigner $6j$: Correctness, Symmetry, and a Unit-Test Suite

This note is a *practical* “trust contract” for the Wigner $6j$ symbol implementation used throughout the project.

If the $6j$ is wrong (or cached under an invalid symmetry), the rest of the tensor-network physics becomes a haunted house: everything looks like a pattern, and none of it is.

---

## 1. What “correct” means for an SU(2) Wigner $6j$

We use the Wigner $6j$ in the standard convention
\[
\left\{ \begin{matrix}
j_1 & j_2 & j_3 \\
j_4 & j_5 & j_6
\end{matrix}\right\}.
\]

### 1.1 Selection rules (must be enforced *before* calling any special function)

The $6j$ is nonzero only if **four** SU(2) triangles are admissible:

\[
(j_1,j_2,j_3),\quad (j_1,j_5,j_6),\quad (j_4,j_2,j_6),\quad (j_4,j_5,j_3).
\]

Each triangle must satisfy:

1. **Triangle inequalities**
\[
|a-b|\le c \le a+b.
\]

2. **Parity (half-integer) constraint**
\[
a+b+c \in \mathbb{Z}.
\]

If you skip the parity check, you will generate *invalid* tuples and (correctly) trigger SymPy’s
“j values must be integer or half integer” failures.

---

## 2. The real symmetry group (and the symmetry that is *not* real)

### 2.1 Tetrahedral symmetry: 24 exact symmetries

The Wigner $6j$ has a **24-element** symmetry group (the tetrahedral group). A clean way to generate it:

- Treat the symbol as three **columns**
\[
(j_1,j_4),\ (j_2,j_5),\ (j_3,j_6).
\]
- You may:
  - permute the **columns** arbitrarily (6 permutations),
  - swap **top↔bottom** in an **even number** of columns (4 choices: swap none, or swap any 2 columns).

Total: \(6\times 4=24\) symmetries.

### 2.2 The tempting-but-wrong “full row swap” test

A project unit test asserted that
\[
\left\{\!\begin{matrix}1&1&1\\ \tfrac12&\tfrac12&\tfrac12\end{matrix}\!\right\}
\stackrel{?}{=}
\left\{\!\begin{matrix}\tfrac12&\tfrac12&\tfrac12\\ 1&1&1\end{matrix}\!\right\},
\]
and declared the kernel “FAILED” when they differed.

But the *second* symbol violates the parity condition because
\[
\tfrac12+\tfrac12+\tfrac12 = \tfrac32\notin\mathbb{Z}.
\]
So it is not even an admissible SU(2) coupling, and the mismatch is expected.

**Conclusion:** do **not** use “swap whole top and bottom rows” as a symmetry test.  
Use the tetrahedral 24 symmetries instead.

---

## 3. A reference implementation: Racah formula in integer arithmetic

A robust way to avoid floating-point parity bugs is to represent spins by integers
\[
A_i \equiv 2j_i\in\mathbb{Z}.
\]

Then all factorial arguments in the Racah formula become ordinary integers.

### 3.1 Racah formula (classical)

Define the triangle factor
\[
\Delta(a,b,c) \equiv 
\sqrt{\frac{(a+b-c)!\,(a-b+c)!\,(-a+b+c)!}{(a+b+c+1)!}}.
\]

Then
\[
\left\{ \begin{matrix}
j_1 & j_2 & j_3 \\
j_4 & j_5 & j_6
\end{matrix}\right\}
=
\Delta(1,2,3)\Delta(1,5,6)\Delta(4,2,6)\Delta(4,5,3)
\sum_{z=z_{\min}}^{z_{\max}}
(-1)^z\frac{(z+1)!}{\prod_{i=1}^{4}(z-x_i)!\,\prod_{i=5}^{7}(y_i-z)!},
\]
with
\[
\begin{aligned}
x_1&=j_1+j_2+j_3,& x_2&=j_1+j_5+j_6,& x_3&=j_4+j_2+j_6,& x_4&=j_4+j_5+j_3,\\
y_5&=j_1+j_2+j_4+j_5,& y_6&=j_2+j_3+j_5+j_6,& y_7&=j_3+j_1+j_6+j_4,\\
z_{\min}&=\max(x_1,x_2,x_3,x_4),& z_{\max}&=\min(y_5,y_6,y_7).
\end{aligned}
\]

### 3.2 Minimal Python reference (numerically stable for small/moderate spins)

```python
import math

def sixj_racah(j1,j2,j3,j4,j5,j6):
    # Represent spins as integers A=2j to enforce parity exactly
    def to2j(x): return int(round(2*x))
    a,b,c,d,e,f = map(to2j,[j1,j2,j3,j4,j5,j6])

    def tri_ok(A,B,C):
        return (A+B>=C) and (A+C>=B) and (B+C>=A) and ((A+B+C)%2==0)

    if not (tri_ok(a,b,c) and tri_ok(a,e,f) and tri_ok(d,b,f) and tri_ok(d,e,c)):
        return 0.0

    def logfact(n): return -math.inf if n<0 else math.lgamma(n+1)

    def log_delta(A,B,C):
        n1=(A+B-C)//2
        n2=(A-B+C)//2
        n3=(-A+B+C)//2
        n4=(A+B+C)//2 + 1
        return 0.5*(logfact(n1)+logfact(n2)+logfact(n3)-logfact(n4))

    log_pre = log_delta(a,b,c)+log_delta(a,e,f)+log_delta(d,b,f)+log_delta(d,e,c)

    k1=(a+b+c)//2
    k2=(a+e+f)//2
    k3=(d+b+f)//2
    k4=(d+e+c)//2
    k5=(a+b+d+e)//2
    k6=(b+c+e+f)//2
    k7=(c+a+f+d)//2

    zmin=max(k1,k2,k3,k4)
    zmax=min(k5,k6,k7)
    if zmin>zmax:
        return 0.0

    s=0.0
    for z in range(zmin, zmax+1):
        sign = -1 if (z%2) else 1
        log_num = logfact(z+1)
        log_den = (logfact(z-k1)+logfact(z-k2)+logfact(z-k3)+logfact(z-k4)
                   +logfact(k5-z)+logfact(k6-z)+logfact(k7-z))
        s += sign*math.exp(log_num-log_den)

    return math.exp(log_pre)*s
```

---

## 4. A *correct* symmetry test generator (24 symmetries)

```python
import itertools

def symm24(j1,j2,j3,j4,j5,j6):
    cols=[(j1,j4),(j2,j5),(j3,j6)]
    perms=list(itertools.permutations([0,1,2]))
    swap_masks=[(),(0,1),(0,2),(1,2)]  # swap top/bottom in an even number of columns
    out=[]
    for p in perms:
        perm_cols=[cols[i] for i in p]
        for mask in swap_masks:
            new=[]
            for idx,(top,bot) in enumerate(perm_cols):
                new.append((bot,top) if idx in mask else (top,bot))
            (t1,b1),(t2,b2),(t3,b3)=new
            out.append((t1,t2,t3,b1,b2,b3))
    # unique tuples
    uniq=[]
    seen=set()
    for tup in out:
        if tup not in seen:
            uniq.append(tup); seen.add(tup)
    return uniq
```

Then, the unit test is:

```python
base = sixj_racah(j1,j2,j3,j4,j5,j6)
for tup in symm24(j1,j2,j3,j4,j5,j6):
    assert abs(sixj_racah(*tup) - base) < 1e-12
```

---

## 5. Two extra “physics-grade” tests (optional but very comforting)

### 5.1 Known-value checks

- \(\left\{\begin{matrix}0&0&0\\0&0&0\end{matrix}\right\}=1\)
- \(\left\{\begin{matrix}\tfrac12&\tfrac12&1\\ \tfrac12&\tfrac12&1\end{matrix}\right\}= \tfrac16\)
- \(\left\{\begin{matrix}1&1&0\\ 1&1&1\end{matrix}\right\}= -\tfrac13\)

### 5.2 Orthogonality relation

A standard orthogonality identity is
\[
\sum_{j_3} (2j_3+1)
\left\{ \begin{matrix} j_1 & j_2 & j_3\\ j_4 & j_5 & j_6 \end{matrix}\right\}
\left\{ \begin{matrix} j_1 & j_2 & j_3\\ j_4 & j_5 & j_6' \end{matrix}\right\}
=
\frac{\delta_{j_6 j_6'}}{2j_6+1}.
\]

This is a great “integration test” because it catches subtle off-by-one errors in the Racah sum bounds.

---

## 6. Caching: what symmetry reduction is actually safe?

If you canonicalize cache keys by **sorting** the top row, bottom row, or both, you will generally break correctness, because those are *not* symmetries in general.

**Safe canonical key:** enumerate the 24 symmetry-related tuples and choose the lexicographically smallest one as the canonical representative.

That’s slower per lookup, but for small `j_max` it’s usually worth it, and you can memoize the canonicalization itself.

---

## 7. What to do next

1. Fix / replace any unit tests that assume a non-symmetry (like full row swap).
2. Add the 24-symmetry test (it’s cheap).
3. Add the orthogonality test (it’s a medium-cost “integration test”).
4. Only then: trust any $\theta$-dependent model built on top of the $6j$ kernel.

