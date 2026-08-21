#!/usr/bin/env python3
"""
Exact theorem-assembly audit for the fourth-order SU(N) one-flux mobility result.

Purpose
-------
This script does NOT pretend to regenerate the microscopic SU(3)/SU(4)/SU(5)/SU(6)
Haar-resolvent certificates.  It verifies the algebra needed to assemble a rank-complete
theorem once those exact certificate facts are accepted, and it explicitly distinguishes
re-derived gates from certificate inputs.

The target old-pencil mobility coefficient is

    alpha_N = 640 / [ N (N^2 - 1)^3 ] .

Run:
    python3 ENGINE_FLUX_verify_theorem_assembly.py
"""

from fractions import Fraction as F
from pathlib import Path
import re

PASS = []
FAIL = []
INFO = []


def gate(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


def info(name, detail):
    INFO.append(name)
    print(f"[INFO] {name} :: {detail}")


def alpha(N):
    return F(640, N * (N*N - 1)**3)


# -----------------------------------------------------------------------------
# 1. Exact finite-rank arithmetic closure
# -----------------------------------------------------------------------------

CERT_ALPHA = {
    3: F(5, 12),
    4: F(32, 675),
    5: F(1, 108),
    6: F(64, 25725),
}

print("=" * 78)
print("UNIVERSAL FOURTH-ORDER MOBILITY THEOREM — ASSEMBLY AUDIT")
print("=" * 78)
print("\nA. LOW-RANK MOBILITY IDENTITY")
for N, a_cert in CERT_ALPHA.items():
    gate(f"A{N}: alpha_{N} matches universal rational function",
         a_cert == alpha(N),
         f"{a_cert} = 640/[{N}({N}^2-1)^3]")


# -----------------------------------------------------------------------------
# 2. SU(5): exact six-factor determinant parity obstruction
# -----------------------------------------------------------------------------

print("\nB. SU(5) SIX-FACTOR TERMINAL DETERMINANT OBSTRUCTION")
# A determinant terminal family at a six-factor word must satisfy p+q = 6 and
# |p-q| = N.  Since p+q and p-q have the same parity, odd N cannot occur at
# exactly six factors.  Enumerate explicitly as a hard gate.

def terminal_pairs(N, total=6):
    return [(p, total-p) for p in range(total+1) if abs(p-(total-p)) == N]

p5 = terminal_pairs(5)
gate("B1: no SU(5) determinant family at exactly six factors", p5 == [], str(p5))
gate("B2: parity proof", (6 - 5) % 2 == 1,
     "p=(6+5)/2 would be half-integral; equivalently p+q even but p-q odd")

# For comparison, the allowed even-rank terminal families are recovered exactly.
gate("B3: SU(4) six-factor terminal families", terminal_pairs(4) == [(1, 5), (5, 1)], str(terminal_pairs(4)))
gate("B4: SU(6) six-factor terminal families", terminal_pairs(6) == [(0, 6), (6, 0)], str(terminal_pairs(6)))


# -----------------------------------------------------------------------------
# 3. SU(6): determinant resolvent re-derived exactly
# -----------------------------------------------------------------------------

print("\nC. SU(6) DETERMINANT RESOLVENT")
N = 6
C2 = lambda k: F(k * (N-k) * (N+1), 2*N)
cas = [C2(k) for k in (2, 3, 4)]
gate("C1: antisymmetric-power Casimirs", cas == [F(14,3), F(21,4), F(14,3)], str(cas))
link4 = [4*x for x in cas]
gate("C2: four-link Casimir sums", link4 == [F(56,3), F(21), F(56,3)], str(link4))
E0 = F(1,2) * 4 * F(N*N-1, 2*N)
dens = [E0 - F(1,2)*x for x in link4]
gate("C3: three electric denominators", dens == [F(-7,2), F(-14,3), F(-7,2)], str(dens))
Fdet = 1
for d in dens:
    Fdet /= d
gate("C4: determinant resolvent factor", Fdet == F(-6,343), str(Fdet))
gate("C5: C-odd determinant shift", -Fdet == F(6,343), str(-Fdet))

# Same-plaquette support is a structural certificate fact from STATUS_fourth_order_build.md.
# We verify that the supplied status record actually contains that fact; the geometric
# implication (no displacement -> k-independent diagonal scalar after cubic completion)
# is then an exact Fourier statement.
status_path = Path('/mnt/data/STATUS_fourth_order_build.md')
status = status_path.read_text(encoding='utf-8') if status_path.exists() else ''
same_plaq = 'root + four insertions + output all on the SAME plaquette' in status
gate("C6: supplied build records SU(6) same-plaquette exceptional word", same_plaq)
if same_plaq:
    info("C7: exact geometric implication",
         "same input/output plaquette gives displacement r=0; cubic completion makes the orientation coefficient common, hence H_exc,6(k)=delta_q6 I_3 and cannot alter mobility")


# -----------------------------------------------------------------------------
# 4. SU(4): consume the exact all-zone certificate statement as provenance input
# -----------------------------------------------------------------------------

print("\nD. SU(4) ALL-ZONE EXCEPTIONAL IDENTITY")
# The full SU(4) JSON is in the project library rather than /mnt/data in this turn.
# The current status document contains the certified Delta q_4 and the rank value.
dq4 = F(-304746539168, 160249753125)
gate("D1: SU(4) exceptional shift is nonzero", dq4 != 0, str(dq4))
info("D2: required exact certificate fact",
     "CERT_SU4_hybrid_certificate_v2.json: H_exc,4(k) psi(k) = delta_q4 psi(k) identically, with delta_A=delta_B=0 and exact Laurent residual (0,0,0).")


# -----------------------------------------------------------------------------
# 5. Stable-rank theorem + exhaustive rank partition
# -----------------------------------------------------------------------------

print("\nE. CASE-COMPLETE THEOREM ASSEMBLY")
# N>=3 partitions into {3,4,5,6} union {N>=7}.
gate("E1: exceptional finite set is exhausted", set(CERT_ALPHA) == {3,4,5,6})
info("E2: stable theorem input",
     "For every integer N>=7, the accepted stable-rank exact computer-assisted theorem gives alpha_N = 640/[N(N^2-1)^3].")

gate("E3: universal formula is nonzero and positive for N=3..100",
     all(alpha(n) > 0 for n in range(3,101)))


# -----------------------------------------------------------------------------
# 6. Provenance diagnostics
# -----------------------------------------------------------------------------

print("\nF. PROVENANCE STATUS")
log_path = Path('/mnt/data/VERIFY_ALL_run.log')
log = log_path.read_text(encoding='utf-8') if log_path.exists() else ''
gate("F1: consolidated suite reports 24 passed, 0 failed", '24 passed, 0 failed' in log)

# Explicitly refuse to overstate cold reproducibility.
info("F2: theorem status",
     "Case-complete exact theorem relative to accepted microscopic certificates; NOT yet a single-file cold derivation of all microscopic Haar-resolvent data.")
info("F3: remaining publication-grade provenance task",
     "Bundle/cold-rerun the SU(5), SU(6), and stable-rank microscopic certificates, and retain the SU(4) all-zone Laurent residual certificate with its source hashes.")

print("\n" + "=" * 78)
print(f"RESULT: {len(PASS)} passed, {len(FAIL)} failed, {len(INFO)} provenance/info notes")
if FAIL:
    print("FAILED:", ', '.join(FAIL))
    raise SystemExit(1)
print("THEOREM ASSEMBLY: PASS")
print("=" * 78)
