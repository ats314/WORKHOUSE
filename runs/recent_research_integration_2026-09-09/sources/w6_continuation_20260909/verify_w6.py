"""Exact algebra controls for the W6 continuation, not a Wilson uniformity proof."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []


def record(name, condition, detail):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(dict(name=name, passed=True, detail=detail))


def zero(matrix):
    return all(s.simplify(x) == 0 for x in matrix)


# Noncommuting rational matrices, two simultaneous retained sources.
A0 = s.Matrix([[3, 1, 0], [1, 4, 1], [0, 1, 5]])
D = s.Matrix([[1, 2, -1], [2, -1, 1], [-1, 1, 2]]) / 7
Ag = A0 + D
T = s.Matrix([[1, 2], [-1, 1], [2, -1]])
U = A0.inv() * T
rho = D * U
variation = T.T * (Ag.inv() - A0.inv()) * T
certificate = -U.T * D * U + rho.T * Ag.inv() * rho
record("noncommuting residual identity", zero(variation-certificate),
       "Exact 2 by 2 selected operator equality for positive noncommuting 3 by 3 fast forms.")
record("signed pairing identity", zero(variation + U.T * D * Ag.inv() * T),
       "Checks the sign and full matrix polarization, not just one diagonal entry.")
record("positive fast forms", A0.is_positive_definite and Ag.is_positive_definite,
       "SymPy exact principal-minor criterion; [A0,D] is nonzero.")
assert not zero(A0*D-D*A0)

# The lower-reference certificate uses only a known lower operator.
L = s.eye(3)
kappa = s.Rational(1, 2)
upper = (1/kappa) * rho.T * L.inv() * rho
lower = rho.T * Ag.inv() * rho
record("lower-reference residual enclosure",
       (Ag-kappa*L).is_positive_definite and (upper-lower).is_positive_definite,
       "Ag >= kappa L implies rho*Ag^-1 rho <= kappa^-1 rho*L^-1 rho on this exact control.")

g, M = s.symbols("g M", positive=True)
c = M*g**2/(2*(1+M*g**2))
A = s.Matrix([[1, c], [c, 1]])
t = s.Matrix([1, 0])
delta = s.factor((t.T*(A.inv()-s.eye(2))*t)[0])
record("uniform-floor counterexample formula",
       s.simplify(delta-c**2/(1-c**2)) == 0
       and (t.T*(A-s.eye(2))*t)[0] == 0,
       "A0=I, Ag has floor >=1/2 and zero Gaussian diagonal defect, but selected variation=c^2/(1-c^2).")
n = s.symbols("n", positive=True, integer=True)
record("nonuniform analytic family",
       s.simplify(delta.subs({g:1/n, M:n**2})-s.Rational(1,15)) == 0,
       "For g=1/n and M=n^2, delta=1/15, so delta/g=n/15 is unbounded. This is an abstract counterexample, not Wilson.")

# The old cell and vacuum controls are independently recomputed.
gc, rank, mode = s.Rational(1,4), 1, 1024
record("recorded compact spectral-growth witness",
       gc**2*mode*(mode+2)/2-4/gc**2 == 32768
       and (1+gc)*4*(mode+rank) == 5125,
       "Reproduces the exact numerical witness in W2-W3; the min-max quantifiers remain analytic.")
record("recorded vacuum-subtraction reversal",
       1/(s.Integer(2)-100*s.Rational(1,20)**2) == s.Rational(4,7),
       "Positive bare perturbation can increase the vacuum-subtracted selected inverse above 1/2.")

# Integrated Wilson radial phase volume at the top of its potential.
r = s.symbols("r", real=True)
v = s.Function("v")(r)
radial = v/s.sin(r/2)
conjugated = s.sin(r/2)*(s.diff(radial,r,2)+s.cot(r/2)*s.diff(radial,r))
record("four-link radial unitary conjugacy",
       s.trigsimp(conjugated-s.diff(v,r,2)-v/4) == 0,
       "Exact differential identity gives Hg=-2g^2 d_r^2+4g^-2(1-cos(r/2))-g^2/2 with the physical Dirichlet realization specified analytically.")
primitive = 8*s.sqrt(2)*s.sin(r/4)
assert s.simplify(s.diff(primitive,r)-2*s.sqrt(2)*s.cos(r/4)) == 0
phase_integral = primitive.subs(r,2*s.pi)-primitive.subs(r,0)
record("radial phase-volume coefficient",
       s.simplify(phase_integral/(s.pi*s.sqrt(2))-8/s.pi) == 0,
       "The integral gives 8/pi. This checks a constant only; the spectral counting proof is analytic.")

inputs = [
    Path("C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-selected-inverse-wall.md"),
    Path("C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-spatial-schur-excess.md"),
    Path("C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/research/spatial-continuum-passage-2026-09-08.md"),
    Path("C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md"),
    Path("C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md"),
    Path("C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md"),
    Path("C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md"),
    Path("C:/Users/Alex/.codex/codex-remote-attachments/01a082e4-6acd-7fb3-9b51-19444da9ee6b/7CB6AE9F-52F3-4247-B1C0-B94760FF97DD/1-yangmills.pdf"),
]
report = dict(
    scope="Exact finite algebra controls only. Conditional form and limit lemmas are analytic; W6 for coupled Wilson remains open. No new Lean theorem is claimed.",
    checks=checks,
    input_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
    artifact_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.iterdir()
                     if p.suffix in (".md", ".py")},
)
(ROOT/"verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(f"{len(checks)}/{len(checks)} exact controls passed; report: {ROOT/'verification.json'}")
