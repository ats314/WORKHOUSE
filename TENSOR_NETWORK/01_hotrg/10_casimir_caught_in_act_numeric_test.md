---
title: "Catching the Casimir in the act: a concrete (a,b,c,d) numerical match-test"
date: "2025-12-29"
---

## What this is

This note implements the “tight next step”:

1. pick **one concrete admissible boundary** spin quadruple \((a,b,c,d)\);
2. build the **recoupling matrix** \(\Lambda\) *literally* from the \(U_q(\mathfrak{su}(2))\) **quantum \(6j\)** (the \(F\)-move);
3. build a **bulk generator** \(Q_{\mathrm{Cas}}\) from the **explicit q–Racah/Casimir spectrum** \(\lambda_n\) (diagonal in the \(e\)-channel);
4. form the compressed kernel
   \[
   K_{\mathrm{Cas}}(t) \;=\; \Lambda^\top e^{tQ_{\mathrm{Cas}}}\Lambda;
   \]
5. compare it to your current kernel
   \[
   K_{\mathrm{cur}}(t) \;=\; \Lambda^\top e^{tQ_{\mathrm{cur}}}\Lambda
   \]
   (or whatever you are currently calling the bulk piece), allowing only a **simple affine rescale** \(Q_{\mathrm{cur}}\approx s\,Q_{\mathrm{Cas}} + b\,I\).

If this works (small residual after fitting \(s,b\)), you’ve essentially shown that your toy “bulk” is *really* an intermediate Casimir representation on the fusion space.

---

## 1. Boundary fusion channels

Work in doubled-spin integers \(A=2a\), etc., to avoid half-integer bookkeeping.

For fixed \((a,b,c,d)\) (half-integers), define:

- \(e\)-channel admissible set \(\mathcal E\): triangles \((a,b,e)\) and \((e,c,d)\),
- \(f\)-channel admissible set \(\mathcal F\): triangles \((b,c,f)\) and \((f,a,d)\).

Multiplicity-free fusion implies \(|\mathcal E|=|\mathcal F|\), so \(\Lambda\) is square.

---

## 2. The honest \(\Lambda\) from the quantum \(6j\)

With quantum dimension \(\dim_q(j)=[2j+1]_q\), define
\[
\boxed{
\Lambda_{e f}
=
\sqrt{\dim_q(e)\,\dim_q(f)}\;
\left\{\begin{matrix}
a & b & e\\
c & d & f
\end{matrix}\right\}_q
}
\]
(up to an optional gauge/phase convention).

In standard normalizations \(\Lambda\) is orthogonal/unitary:
\[
\Lambda^\top \Lambda = I.
\]

---

## 3. The “Casimir” spectrum to build \(Q_{\mathrm{Cas}}\)

For the \(U_q(\mathfrak{su}(2))\) intermediate Casimir in the \((ab)\to e\) channel, a convenient shifted eigenvalue family is (see the project’s matching note for context)
\[
\boxed{
\lambda_e
=
[e-a+b]_q\,[e+a-b+1]_q
}
\qquad
\text{(with }e\in\mathcal E\text{)}.
\]

This is the same information as the q–Racah formula
\(\lambda_n=[n]_q[n+\alpha+\beta+1]_q\) after using \(\alpha+\beta=2(a-b)\) and \(n=e-a+b\).

To make the ground mode exactly \(0\) on the **actual** fusion range \(\mathcal E\), shift by the minimum:
\[
\lambda^{(\mathrm{shift})}_e := \lambda_e - \min_{e\in\mathcal E}\lambda_e.
\]

Then take
\[
\boxed{
Q_{\mathrm{Cas}} := -\kappa\,\mathrm{diag}\big(\lambda^{(\mathrm{shift})}_e\big)
}
\]
where \(\kappa>0\) is just a time-scale choice.

---

## 4. What you should see if “bulk = Casimir” is true

If the bulk really is the Racah/Casimir representation on the fusion space, then (after fitting \(\kappa\) and perhaps an overall shift \(b\))

- the eigenvalues of \(Q_{\mathrm{cur}}\) are affine functions of \(-\lambda_e\), and
- the compressed kernels match:
  \[
  K_{\mathrm{cur}}(t)\approx e^{bt}\,K_{\mathrm{Cas}}(\kappa t)
  \]
  to small error, for a range of \(t\).

---

## 5. Drop-in Python: compute \(\Lambda\), \(Q_{\mathrm{Cas}}\), and run the match-test

This code is deliberately “notebook-friendly” and self-contained.

It uses the standard Racah-sum formula for the quantum \(6j\) in doubled-spin integers.

```python
import numpy as np, math
import scipy.linalg as la
from functools import lru_cache

# ----------------------------
# q arithmetic (code convention)
# [x]_q = (q^x - q^{-x})/(q - q^{-1})
# ----------------------------
def make_qnum(q: float):
    def qnum(x: float) -> float:
        return (q**x - q**(-x)) / (q - q**(-1))
    return qnum

def make_log_qfact(q: float):
    qnum = make_qnum(q)

    @lru_cache(None)
    def log_qfact(n: int) -> float:
        if n < 0:
            raise ValueError("factorial argument < 0")
        acc = 0.0
        for k in range(1, n+1):
            acc += math.log(float(qnum(k)))
        return acc

    return log_qfact

# ----------------------------
# SU(2) triangle admissibility in doubled spins
# ----------------------------
def tri_ok(A,B,C):
    return ((A+B+C) % 2 == 0) and (A+B >= C) and (A+C >= B) and (B+C >= A)

# ----------------------------
# quantum 6j in doubled spins (real q in (0,1) works fine)
# Convention: {j1 j2 j3; j4 j5 j6}_q with the 4 triangle checks
# ----------------------------
def sixj_q_doubled(j1,j2,j3,j4,j5,j6, q: float) -> float:
    log_qfact = make_log_qfact(q)

    tris = [(j1,j2,j3),(j1,j5,j6),(j4,j2,j6),(j4,j5,j3)]
    if not all(tri_ok(*t) for t in tris):
        return 0.0

    def delta_log(a,b,c):
        x1 = (a+b-c)//2
        x2 = (a-b+c)//2
        x3 = (-a+b+c)//2
        x4 = (a+b+c)//2 + 1
        return 0.5*(log_qfact(x1)+log_qfact(x2)+log_qfact(x3)-log_qfact(x4))

    log_pref = sum(delta_log(*t) for t in tris)

    t1 = (j1+j2+j3)//2
    t2 = (j1+j5+j6)//2
    t3 = (j4+j2+j6)//2
    t4 = (j4+j5+j3)//2
    zmin = max(t1,t2,t3,t4)

    u1 = (j1+j2+j4+j5)//2
    u2 = (j1+j3+j4+j6)//2
    u3 = (j2+j3+j5+j6)//2
    zmax = min(u1,u2,u3)

    total = 0.0
    for z in range(zmin, zmax+1):
        den_args = [z-t1, z-t2, z-t3, z-t4, u1-z, u2-z, u3-z]
        if any(a < 0 for a in den_args):
            continue
        log_term = log_qfact(z+1) - sum(log_qfact(a) for a in den_args)
        total += ((-1)**z) * math.exp(log_term)

    return math.exp(log_pref) * total

# ----------------------------
# channel sets (doubled spins)
# ----------------------------
def allowed_channel_doubled(jx,jy,jz,jw):
    # e: (jx,jy,e) and (e,jz,jw) both admissible
    out=[]
    emin = max(abs(jx-jy), abs(jw-jz))
    emax = min(jx+jy, jw+jz)
    for e in range(emin, emax+1, 2):
        if tri_ok(jx,jy,e) and tri_ok(e,jz,jw):
            out.append(e)
    return out

def build_Lambda(a2,b2,c2,d2, q):
    E = allowed_channel_doubled(a2,b2,c2,d2)   # e channel
    F = allowed_channel_doubled(b2,c2,a2,d2)   # f channel

    qnum = make_qnum(q)

    Lam = np.zeros((len(E),len(F)), dtype=float)
    for i,e2 in enumerate(E):
        qdime = float(qnum(e2+1))
        for j,f2 in enumerate(F):
            qdimf = float(qnum(f2+1))
            six = sixj_q_doubled(a2,b2,e2,c2,d2,f2,q)
            Lam[i,j] = math.sqrt(qdime*qdimf)*six

    return Lam, E, F

# ----------------------------
# Casimir/q-Racah eigenvalues on the e-channel
# λ_e = [e-a+b]_q [e+a-b+1]_q
# ----------------------------
def casimir_lambdas(E_doubled, a2, b2, q):
    qnum = make_qnum(q)
    a = a2/2.0
    b = b2/2.0
    lam=[]
    for e2 in E_doubled:
        e = e2/2.0
        n = e - a + b
        lam.append(float(qnum(n) * qnum(n + 2*(a-b) + 1)))
    lam = np.array(lam)
    lam = lam - lam.min()  # shift ground to 0 on the actual admissible set
    return lam

# ----------------------------
# YOUR current toy bulk generator (optional)
# copy-pasted from the notebook PDF for convenience
# ----------------------------
def q_racah_jacobi_matrix(N, q, alpha, beta, gamma, delta):
    A = np.zeros(N+1); B = np.zeros(N+1); C = np.zeros(N+1)
    for n in range(0, N+1):
        if n < N:
            numA = ((1 - alpha * q**(n+1)) *
                    (1 - beta * delta * q**(n+1)) *
                    (1 - gamma * q**(n+1)) *
                    (1 - delta * q**(n+1)))
            denA = ((1 - delta * q**(2*n+1)) *
                    (1 - delta * q**(2*n+2)))
            A[n] = math.sqrt(max(numA/denA, 0.0))
        if n > 0:
            numC = ((1 - q**n) *
                    (1 - beta * q**n) *
                    (1 - gamma * q**n) *
                    (1 - alpha * delta * q**n))
            denC = ((1 - delta * q**(2*n)) *
                    (1 - delta * q**(2*n+1)))
            C[n] = math.sqrt(max(numC/denC, 0.0))
        B[n] = -(A[n]**2 + C[n]**2)

    H = np.zeros((N+1, N+1))
    for n in range(N+1):
        H[n,n] = -B[n]
        if n < N:
            H[n,n+1] = -A[n]; H[n+1,n] = -A[n]
        if n > 0:
            H[n,n-1] = -C[n]; H[n-1,n] = -C[n]
    return H

def doob_transform(H):
    evals, evecs = np.linalg.eigh(H)
    idx = np.argsort(evals)
    evals = evals[idx]; evecs = evecs[:,idx]
    psi0 = np.abs(evecs[:,0]); psi0 = psi0/psi0.sum()
    Q = np.zeros_like(H)
    Np1 = H.shape[0]
    for i in range(Np1):
        for j in range(Np1):
            if i==j: continue
            if H[i,j] != 0.0:
                Q[i,j] = -H[i,j]*psi0[j]/psi0[i]
    for i in range(Np1):
        Q[i,i] = -Q[i,:].sum()
    return Q

# ----------------------------
# the actual match test
# ----------------------------
def match_test_one_boundary(a,b,c,d, q=0.95, t=1.0):
    # doubled spins
    a2,b2,c2,d2 = int(round(2*a)), int(round(2*b)), int(round(2*c)), int(round(2*d))

    Lam, E, F = build_Lambda(a2,b2,c2,d2,q)
    assert Lam.shape[0] == Lam.shape[1], "need |E|=|F| for square fusion space"

    # orthogonality sanity check
    orth_err = np.max(np.abs(Lam.T@Lam - np.eye(Lam.shape[1])))
    print("E(doubled)=",E,"F(doubled)=",F)
    print("max|Lam^T Lam - I| =", orth_err)

    # Casimir generator (diagonal in e)
    lam = casimir_lambdas(E, a2, b2, q)
    Qcas = np.diag(-lam)

    # CURRENT toy generator on same dimension (optional; choose any params you like)
    N = Lam.shape[0]-1
    H = q_racah_jacobi_matrix(N, q, alpha=q, beta=1.0, gamma=q, delta=1.0)
    Qcur = doob_transform(H)

    # Fit a single scale s so that spectra align best in least squares
    eig_cur = np.sort(np.real_if_close(np.linalg.eigvals(Qcur)))
    eig_cas = np.sort(np.real_if_close(np.linalg.eigvals(Qcas)))
    # drop the last entry (the ~0 eigenvalue)
    s = (eig_cur[:-1] @ eig_cas[:-1]) / (eig_cas[:-1] @ eig_cas[:-1])
    print("best-fit spectral scale s ≈", s)

    # Compressed kernels
    Kcur = Lam.T @ la.expm(t*Qcur) @ Lam
    Kcas = Lam.T @ np.diag(np.exp(t*s*np.diag(Qcas))) @ Lam

    rel_err = np.linalg.norm(Kcur-Kcas)/np.linalg.norm(Kcur)
    print("relative Frobenius error ||Kcur-Kcas||/||Kcur|| =", rel_err)

    return dict(Lam=Lam, E=E, F=F, Qcas=Qcas, Qcur=Qcur, s=s, Kcas=Kcas, Kcur=Kcur, rel_err=rel_err)

# Example run (symmetric boundary gives a clean square space)
out = match_test_one_boundary(a=2,b=2,c=2,d=2, q=0.95, t=1.0)
```

### What to do next if the error is not small

If the kernel mismatch is not tiny, that’s informative (not a failure):

- it means your current toy \(Q_{\mathrm{cur}}\) parameters are *not* yet the representation-theoretic ones,
- or you need to compare in the **correct inner product** (insert \(\Pi\) weights / use the symmetric conjugate),
- or you should compare \(H\)-level objects (Casimir Hamiltonian vs Jacobi Hamiltonian) before Doob transforming.

In practice, the fastest route is:

1. **Construct the tridiagonal operator in the \(f\)-basis directly**
   \[
   L_f := \Lambda^\top Q_{\mathrm{Cas}} \Lambda
   \]
   and treat *that* as the “bulk q-Racah Jacobi matrix” for this boundary.
2. If you still want the four-parameter Jacobi family, fit \((\alpha,\beta,\gamma,\delta)\) to match \(L_f\) (tridiagonal coefficients are an easy least-squares target).
3. Only then Doob-transform, and only then compare semigroups.

That way the Doob chain inherits the right spectral content.

---

## 6. Output you should archive when this works

For the winning boundary configuration and fitted \((s,b)\), save:

- \(E,F\) channel sets,
- the orthogonality error \(\|\Lambda^\top\Lambda-I\|\),
- the affine fit \(Q_{\mathrm{cur}}\approx s Q_{\mathrm{Cas}} + bI\) residual,
- the kernel mismatch \(\|K_{\mathrm{cur}}(t)-e^{bt}K_{\mathrm{Cas}}(st)\|/\|K_{\mathrm{cur}}(t)\|\) vs \(t\),
- the extracted tridiagonal \(L_f=\Lambda^\top Q_{\mathrm{Cas}}\Lambda\) (this is your “non-placeholder” bulk operator in the boundary channel basis).

That bundle is essentially your “Casimir caught on camera” evidence.
