"""Check the su(N) Killing form normalization and the resulting Ricci constant.

Pure Python (no numpy in the REPO venv). Facts under test:

  (1) B(X,Y) = tr(ad_X ad_Y) = 2N tr(XY) on su(N).
  (2) For a bi-invariant metric on a compact group,
        Ric(X,X) = (1/4) sum_a |[X, e_a]|^2  =  -(1/4) B(X,X)
      for a g-orthonormal basis {e_a}. This is the identity the Lean file
      quotes; both sides are computed independently here.
  (3) Hence with g(X,Y) = -tr(XY) = Tr(X^dag Y), Ric = (N/2) g, i.e. kappa = N/2.
      The value N/4 belongs to g = 2 Tr(X^dag Y) instead.
"""

import itertools


def mat(n):
    return [[0j] * n for _ in range(n)]


def mul(a, b):
    n = len(a)
    c = mat(n)
    for i in range(n):
        ai = a[i]
        for k in range(n):
            if ai[k] == 0:
                continue
            aik, bk = ai[k], b[k]
            for j in range(n):
                c[i][j] += aik * bk[j]
    return c


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def scale(a, s):
    return [[a[i][j] * s for j in range(len(a))] for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def bracket(x, y):
    return sub(mul(x, y), mul(y, x))


def hs(a, b):
    """Real inner product g(A,B) = Tr(A^dag B) on anti-Hermitian matrices."""
    n = len(a)
    return sum(a[k][i].conjugate() * b[k][i] for i in range(n) for k in range(n)).real


def su_basis(n):
    out = []
    for i, j in itertools.combinations(range(n), 2):
        a = mat(n)
        a[i][j], a[j][i] = 1j, 1j
        out.append(a)
        b = mat(n)
        b[i][j], b[j][i] = 1 + 0j, -1 + 0j
        out.append(b)
    for k in range(1, n):
        d = mat(n)
        for m in range(k):
            d[m][m] = 1j
        d[k][k] = -1j * k
        out.append(d)
    return out


def gram_schmidt(basis):
    onb = []
    for v in basis:
        w = [row[:] for row in v]
        for e in onb:
            c = hs(e, w)
            w = sub(w, scale(e, c))
        nrm = hs(w, w) ** 0.5
        if nrm > 1e-9:
            onb.append(scale(w, 1.0 / nrm))
    return onb


print(f"{'N':>3} {'dim':>4} {'B(X,X)/tr(XX)':>15} {'expect 2N':>10} "
      f"{'Ric=-B/4?':>11} {'kappa':>9} {'expect N/2':>11}")
for n in range(2, 7):
    onb = gram_schmidt(su_basis(n))
    assert len(onb) == n * n - 1, (n, len(onb))

    x = onb[0]                                   # unit vector: g(X,X) = 1

    # ad_X in the orthonormal basis, then B(X,X) = tr(ad_X^2)
    m = [[hs(onb[a], bracket(x, onb[b])) for b in range(len(onb))]
         for a in range(len(onb))]
    b_xx = sum(m[a][b] * m[b][a] for a in range(len(m)) for b in range(len(m)))

    tr_xx = trace(mul(x, x)).real
    ratio = b_xx / tr_xx

    ric = 0.25 * sum(hs(bracket(x, e), bracket(x, e)) for e in onb)
    agree = abs(ric - (-0.25 * b_xx)) < 1e-8
    kappa = ric / hs(x, x)

    print(f"{n:>3} {len(onb):>4} {ratio:>15.6f} {2*n:>10} "
          f"{str(agree):>11} {kappa:>9.6f} {n/2:>11.1f}")

print()
print("g(X,Y) = Tr(X^dag Y) = -tr(XY) = -(1/(2N)) B(X,Y)  =>  Ric = (N/2) g")
print("g(X,Y) = 2 Tr(X^dag Y)                             =>  Ric = (N/4) g")
print()
print("SU(2) cross-check by an independent route: g = Tr(X^dag Y) makes SU(2)")
print("the round 3-sphere of radius sqrt(2), where Ric = (2/r^2) g = 1 * g,")
print("and N/2 = 1 for N = 2.")
