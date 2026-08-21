#!/usr/bin/env python3
"""
Exact symbolic verifier for the Laurent–Koszul cage-annihilator factorization theorem.

This script verifies the algebraic identities used by the theorem note.
It does NOT regenerate the microscopic SU(4) exceptional kernel.  The SU(4)
all-zone residual is a provenance input from the accepted exact certificate.

Dependencies: sympy only.
"""

import sympy as sp

PASS = []
FAIL = []

def gate(name, expr, detail=""):
    ok = bool(expr)
    (PASS if ok else FAIL).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))

z0, z1, z2 = sp.symbols("z0 z1 z2", nonzero=True)
v0, v1, v2 = z0 - 1, z1 - 1, z2 - 1

psi = sp.Matrix([v2, -v1, v0])

S = sp.Matrix([
    [ v1,  v2,   0],
    [-v0,   0,  v2],
    [  0, -v0, -v1],
])

u0, u1, u2 = 1-z0, 1-z1, 1-z2
Ntilde = sp.Matrix([
    [u1, -u0,   0],
    [u2,    0, -u0],
    [ 0,   u2, -u1],
])

print("="*78)
print("LAURENT–KOSZUL CAGE-ANNIHILATOR FACTORIZATION — EXACT SYMBOLIC GATES")
print("="*78)

gate("K1  S psi = 0 exactly",
     all(sp.expand(x) == 0 for x in S*psi))

gate("K2  S = -Ntilde^T in the build convention",
     S == -Ntilde.T)

# Generic row combination of the three syzygies.
a, b, c = sp.symbols("a b c")
row = sp.Matrix([[v1*a - v0*b, v2*a - v0*c, v2*b - v1*c]])
gate("K3  generic Koszul row annihilates psi",
     sp.expand((row*psi)[0]) == 0)

# Generic 3x3 coefficient matrix gives a generic matrix in the right ideal.
cs = sp.symbols("c00:03 c10:13 c20:23")
C = sp.Matrix(3, 3, cs)
R = C*S
gate("K4  every matrix C S annihilates psi",
     all(sp.expand(x) == 0 for x in R*psi))

# Rank check away from Gamma: the syzygy module has the expected 2D fiber.
sample = {z0: sp.Rational(2), z1: sp.Rational(3), z2: sp.Rational(5)}
gate("K5  S has rank 2 away from Gamma",
     S.subs(sample).rank() == 2,
     f"rank={S.subs(sample).rank()}")

# Gamma specialization.
gamma = {z0: 1, z1: 1, z2: 1}
gate("K6  S vanishes at Gamma",
     S.subs(gamma) == sp.zeros(3))

# Constructive row proof sanity check with nontrivial polynomial multipliers.
aa = 2 + z0 - z1*z2
bb = z1 + z0*z2
cc = 1 - z2 + z0*z1
r1 = sp.expand(v1*aa - v0*bb)
r2 = sp.expand(v2*aa - v0*cc)
r3 = sp.expand(v2*bb - v1*cc)
gate("K7  constructive row formula satisfies the syzygy",
     sp.expand(r1*v2 - r2*v1 + r3*v0) == 0)

# Exact SU(4) scalar from certificate, retained only as a provenance/value gate.
dq4 = sp.Rational(-304746539168, 160249753125)
gate("K8  SU(4) certified exceptional shift is exact nonzero rational",
     dq4 != 0,
     str(dq4))

print("-"*78)
print("PROVENANCE INPUT (not regenerated here):")
print("  Exact SU(4) certificate:")
print("  [H_exc,4(z) - delta_q4 I] psi(z) = 0 componentwise as Laurent polynomials.")
print("  Therefore Theorem KAF implies existence of C4(z) with")
print("  H_exc,4(z)-delta_q4 I = C4(z) S(z) = -C4(z) Ntilde(z)^T.")
print("-"*78)
print(f"RESULT: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    print("FAILED:", ", ".join(FAIL))
    raise SystemExit(1)
print("CAGE-ANNIHILATOR FACTORIZATION ALGEBRA: PASS")
