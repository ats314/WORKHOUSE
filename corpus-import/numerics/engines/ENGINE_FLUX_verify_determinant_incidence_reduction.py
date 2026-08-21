#!/usr/bin/env python3
"""
Exact/sanity verifier for the determinant-to-incidence reduction theorem.

The associativity statements are algebraic identities; this script verifies:
  1. the explicit Laurent incidence vector is annihilated at the endpoint;
  2. generic exact rational instances of the internal-resolvent identity;
  3. closure of the protected algebra under multiplication;
  4. a generic boundary-ideal term annihilates the cage vector symbolically.

It does NOT perform the missing word-by-word SU(4) endpoint provenance gate.
"""

import sympy as sp
from fractions import Fraction
import random

PASS = []
FAIL = []

def gate(name, ok, detail=""):
    ok = bool(ok)
    (PASS if ok else FAIL).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))

print("="*78)
print("DETERMINANT-TO-INCIDENCE REDUCTION — EXACT ALGEBRA")
print("="*78)

z0,z1,z2 = sp.symbols("z0 z1 z2", nonzero=True)
v0,v1,v2 = z0-1,z1-1,z2-1

# Current plaquette-to-link convention.
u0,u1,u2 = 1-z0,1-z1,1-z2
Ntilde = sp.Matrix([
    [u1,-u0,0],
    [u2,0,-u0],
    [0,u2,-u1],
])

psi = sp.Matrix([v2,-v1,v0])

# In the current convention psi is killed by Ntilde^T.
gate("D1  endpoint incidence kills cage vector",
     all(sp.expand(x)==0 for x in Ntilde.T*psi))

# Symbolic generic link-space matrix.
m = sp.symbols("m0:9")
M = sp.Matrix(3,3,m)
R = Ntilde*M*Ntilde.T
gate("D2  every two-sided incidence term annihilates psi",
     all(sp.expand(x)==0 for x in R*psi))

# Internal-resolvent identity with exact rational matrices.
rng = random.Random(20260808)
ok = True
for trial in range(25):
    def rm():
        return sp.Matrix(3,3,[sp.Rational(rng.randint(-7,7), rng.randint(1,7))
                              for _ in range(9)])
    J = rm()
    U = rm()
    G = rm()
    T = U*J
    left = T.T*G*T
    right = J.T*(U.T*G*U)*J
    ok &= (left == right)
gate("D3  internal-resolvent inheritance (25 exact rational trials)", ok)

# Closure identity for the protected algebra.
ok = True
for trial in range(25):
    def rm():
        return sp.Matrix(3,3,[sp.Rational(rng.randint(-5,5), rng.randint(1,5))
                              for _ in range(9)])
    J = rm()
    M1 = rm()
    M2 = rm()
    c = sp.Rational(rng.randint(-5,5), rng.randint(1,5))
    d = sp.Rational(rng.randint(-5,5), rng.randint(1,5))
    I = sp.eye(3)
    H1 = c*I + J.T*M1*J
    H2 = d*I + J.T*M2*J
    middle = c*M2 + d*M1 + M1*(J*J.T)*M2
    expected = c*d*I + J.T*middle*J
    ok &= (H1*H2 == expected)
gate("D4  protected algebra is multiplicatively closed (25 exact trials)", ok)

# Explicit scalar action on the cage vector.
q = sp.symbols("q")
H = q*sp.eye(3) + R
gate("D5  scalar + boundary ideal acts rigidly on cage",
     all(sp.expand(x)==0 for x in H*psi - q*psi))

print("-"*78)
print("PROVENANCE GATE NOT EXECUTED:")
print("  For each of the 76 SU(4) exceptional-bearing words, verify that")
print("  the determinant correction changes only an internal cut/channel and")
print("  leaves the two endpoint incidence maps unchanged.")
print("  The active local bundle does not contain the persistent endpoint-word payload.")
print("-"*78)
print(f"RESULT: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    print("FAILED:", ", ".join(FAIL))
    raise SystemExit(1)
print("STRUCTURAL REDUCTION: PASS")
print("MICROSCOPIC ENDPOINT-INHERITANCE GATE: OPEN")
