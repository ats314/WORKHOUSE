"""Exact finite controls for the Gaussian boundary comparison research draft."""

import json
from itertools import combinations
from pathlib import Path

import sympy as s

if not __debug__:
    raise RuntimeError("Assertions must remain enabled")


def psd(a):
    assert a == a.T
    for size in range(1, a.rows + 1):
        for ix in combinations(range(a.rows), size):
            assert a.extract(ix, ix).det() >= 0


def root_intervals(poly, expected):
    roots = s.Poly(poly, z).intervals(eps=s.Rational(1, 10**9))
    assert len(roots) == expected
    assert all(mult == 1 and lo > 0 for (lo, hi), mult in roots)
    return [interval for interval, _ in roots]


z = s.symbols("z")
f = s.Integer(3)
F = s.Matrix([[7, 2], [2, 5]])
D = s.Matrix([[2, -1], [1, 3]])
K0 = s.Matrix([[2, 1], [1, 4]])
M = s.eye(2) + D * F**-2 * D.T
C = K0 + D * F.inv() * D.T
V = C.row_join(D).col_join(D.T.row_join(F))
psd(F - f * s.eye(2))
assert F.det() > 0 and K0.det() > 0 and K0[0, 0] > 0
assert K0 * M != M * K0  # This control does not diagonalize both by fiat.
X = s.eye(2).col_join(-F.inv() * D.T)
assert X.T * V * X == K0
assert X.T * X == M

exact = C + z * s.eye(2) - D * (F + z * s.eye(2)).inv() * D.T
remainder = D * F**-2 * (F + z * s.eye(2)).inv() * D.T
assert (exact - K0 - z * M + z**2 * remainder).applyfunc(s.factor) == s.zeros(2)
for x in (s.Rational(1, 3), s.Integer(2), s.Integer(5)):
    rx = remainder.subs(z, x)
    psd(rx)
    psd((M - s.eye(2)) / (f + x) - rx)
    kx = exact.subs(z, x)
    psd(K0 + x * M - kx)
    psd(kx - K0 - x * s.eye(2) - x * f / (f + x) * (M - s.eye(2)))

for x in (s.Rational(1, 4), s.Integer(1), s.Rational(5, 2)):
    sx = C - x * s.eye(2) - D * (F - x * s.eye(2)).inv() * D.T
    psd(sx - K0 + x * f / (f - x) * M)
    psd(K0 - x * M - sx)

lam_intervals = root_intervals(V.charpoly(z).as_expr(), 4)
mu_intervals = root_intervals((K0 - z * M).det(), 2)
certificates = []
for j, ((llo, lhi), (mlo, mhi)) in enumerate(zip(lam_intervals, mu_intervals)):
    # The theorem endpoints use the unknown exact roots; monotone rational
    # bounds here certify the stronger finite inequalities independently.
    lower = f * mhi / (f + mhi)
    upper = mlo
    assert lower < llo <= lhi < upper
    certificates.append(
        {
            "j": j + 1,
            "lambda_interval": [str(llo), str(lhi)],
            "mu_interval": [str(mlo), str(mhi)],
            "strict_lower_control": str(lower),
            "strict_upper_control": str(upper),
        }
    )

result = {
    "scope": "Exact matrix identities, Loewner controls and rational Sturm root isolation for one noncommuting finite example; the dimension-independent theorem is analytic.",
    "F": str(F),
    "D": str(D),
    "K0": str(K0),
    "M": str(M),
    "f": str(f),
    "certificates": certificates,
    "passed": True,
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
