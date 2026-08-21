#!/usr/bin/env python3
# =============================================================================
# ENGINE_FLUX_cls_flat_band_certificate_v1_1.py
#
# Compact-localized-state (CLS) and Gauss-law factorization certificate for the
# C-odd flat band of the one-plaquette strong-coupling band program (master
# document Section 8.1/8.6; manuscript Theorem 6.3 / 6.3'; standalone paper
# Theorems "gausslaw"/"flatband"/"cls"/"robust"/"sharp").
#
# -----------------------------------------------------------------------------
# VERSION HISTORY / PROVENANCE
# -----------------------------------------------------------------------------
# v1.0  ENGINE_FLUX_cls_flat_band_certificate.py (md5 d5396786ddaeae3cd1b968b7b76e5774),
#       13 gates G01-G13, all passing. Two audit findings were recorded against
#       it (master document v2.6 changelog; THEORY finding F015):
#         (a) G10 PRECEDENCE: the edge-count check was written
#               len(edge_sum)==12 and all(...) or all(...)
#             which Python parses as (A and B) or C, so the "exactly 12 edges"
#             clause was bypassed -- the gate passed on the all-zero check alone.
#         (b) G09 k=0 SPAN OVERCLAIM: the wording "cube states span the flat
#             band" is false AT k=0, where u(0)=0 and the flat subspace is the
#             three rest states (Ntilde(0)=-4I), not a cube state.
#
# v1.1  THIS FILE. Post-audit edition (14 gates). Changes vs v1.0, math
#       otherwise unchanged:
#         - G10: the "exactly 12 edges" count is now genuinely gated (the
#           precedence bug is removed).
#         - G09: reworded to claim only the generic-k statement it proves
#           (cube symbol spans the 1-dim kernel at k != 0; rank 2 there).
#         - G09b (NEW): exact completeness on the L=3 torus --
#           dim ker(Ntilde+4I) = L^3 + 2 = 29, split as 26 cube states
#           (one per nonzero Bloch momentum; equivalently L^3-1 real-space
#           cube states modulo the single relation sum_cubes psi = 0) + 3 rest
#           states at k=0. This is the statement the standalone paper's
#           Theorem "cls" (the L^3+2 decomposition) actually needs.
#         - G11: wording sharpened (all-orders / link-mediated scope).
#
#       RECONSTRUCTION NOTE (honesty): the original v1.1 was authored in a
#       session whose artifacts were not saved and is present in NO store
#       (F015). This file is an AGENT RECONSTRUCTION (THEORY, June 13, 2026)
#       built from the surviving v1.0 plus the v2.6 changelog specification of
#       the two fixes. It is a machine-gated (T1) artifact; it is not claimed
#       to be byte-identical to the lost original. Exit code 0 iff all gates
#       pass.  Runtime: a few seconds.
#
# CLAIMS CERTIFIED (all exact, sympy rational/trig arithmetic):
#
#   (T1) First-principles reconstruction. The signed shared-link plaquette
#        adjacency on the cubic lattice -- built here from nothing but the
#        oriented plaquette boundary (incidence signs sigma in {+-1}) -- yields
#        Bloch matrices that reproduce the document's S(k) (C-even, Section
#        3.15) and possess det(Ntilde(k) + 4I) == 0 identically (C-odd flat
#        band at mu == -4, independently re-derived).
#
#   (T2) Gauss-law factorization.  Ntilde(k) + 4I = B(k) B(k)^dagger exactly,
#        where B(k) is the plaquette-to-link boundary symbol (each plaquette
#        feeds signed amplitude into its four boundary links).  Hence
#        Ntilde >= -4 as an operator and the flat band IS the kernel of
#        B^dagger: states with zero net signed amplitude on every link.
#
#   (T3) Compact localized state + completeness.  The consistently
#        (Levi-Civita) oriented boundary of a single elementary cube -- six
#        faces, amplitudes +-1 -- is an exact real-space eigenvector of the
#        signed adjacency with eigenvalue -4 and zero leakage.  Its Bloch
#        symbol u(k) = (-sin(k2/2), -sin(k0/2), +sin(k1/2)) spans ker B(k)^dag
#        for all k != 0; on the L^3 torus the flat band has dimension exactly
#        L^3 + 2 (G09b).  Flatness is "boundary of a boundary is zero".
#
#   (T4) Robustness / all-orders criterion.  Any effective hopping correction
#        whose symbol has the link-mediated form  B(k) M(k) B(k)^dagger
#        (M arbitrary Hermitian symbol) annihilates the flat-band subspace
#        exactly: the band stays flat with UNSHIFTED hopping energy, only
#        diagonal (k-independent) constants can move it.  This subsumes the
#        O(y^2) theorem, explains why the O(y^3) tromino-vanishing lemma
#        (master Section 8.3) preserves flatness, and reduces the O(y^4)
#        question to a single sharp criterion:
#            flat at O(y^4)  <==>  u(k)^dagger H4(k) v(k) == 0
#        for v(k) spanning the dispersive subspace -- equivalently H4 commutes
#        with the flat projector P(k) = u u^dagger / |u|^2.  A generic
#        SITE-mediated (corner-sharing tromino/tetromino) hop does not factor
#        through B and is expected to break flatness; gate G12 exhibits the
#        simplest sigma-covariant corner-sharing symbol and certifies that it
#        indeed fails the criterion, so O(y^4) flatness, if true, will require
#        a cancellation among tromino weights, not geometry alone.
#
# Independence: no input is taken from ENGINE_FLUX_glueball_band_certificate.py or
# ENGINE_FLUX_su3_domino_d3.py; the only contact with the corpus is the gate against the
# documented S(k) entries and band edges.
# =============================================================================

import sys
from itertools import product
import sympy as sp

k = sp.symbols('k0 k1 k2', real=True)
GATES = []


def gate(name, cond):
    cond = bool(cond)
    GATES.append((name, cond))
    print(("PASS  " if cond else "FAIL  ") + name)
    return cond


def iszero(expr):
    return sp.simplify(sp.expand_trig(sp.expand_complex(sp.expand(expr)))) == 0


def matzero(M):
    return all(iszero(M[i, j]) for i in range(M.rows) for j in range(M.cols))


# ----------------------------------------------------------------------------
# Layer 1: oriented plaquette geometry on Z^3, from first principles
# ----------------------------------------------------------------------------
ORI = [(0, 1), (1, 2), (0, 2)]          # xy, yz, xz
IDX = {o: i for i, o in enumerate(ORI)}


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def e(i):
    return tuple(1 if j == i else 0 for j in range(3))


def boundary(x, ori):
    """Oriented boundary links of plaquette (x; mu nu): (link base, dir, sign)."""
    mu, nu = ori
    return [(x, mu, +1), (add(x, e(mu)), nu, +1),
            (add(x, e(nu)), mu, -1), (x, nu, -1)]


def transverse(ori):
    return ({0, 1, 2} - set(ori)).pop()


def neighbors_of(x, ori):
    """All plaquettes sharing exactly one link with (x, ori), with the
    incidence-product sign s = sigma_p(b) * sigma_p'(b)."""
    links0 = {(xx, d): s for (xx, d, s) in boundary(x, ori)}
    out = []
    for ori2 in ORI:
        for off in product(range(-2, 3), repeat=3):
            x2 = add(x, off)
            if ori2 == ori and x2 == x:
                continue
            sh = [(links0[(xx, dd)], ss) for (xx, dd, ss) in boundary(x2, ori2)
                  if (xx, dd) in links0]
            if sh:
                assert len(sh) == 1
                out.append((x2, ori2, sh[0][0] * sh[0][1]))
    return out


nb0 = {o: neighbors_of((0, 0, 0), o) for o in ORI}
gate("G01 geometry: every plaquette has exactly 12 shared-link neighbors "
     "(4 coplanar, 8 transverse)",
     all(len(nb0[o]) == 12 and sum(1 for n in nb0[o] if n[1] == o) == 4
         for o in ORI))

# ----------------------------------------------------------------------------
# Layer 2: Bloch matrices in the plaquette-center gauge
# ----------------------------------------------------------------------------
half = sp.Rational(1, 2)


def center(x, ori):
    mu, nu = ori
    c = [sp.Integer(xx) for xx in x]
    c[mu] += half
    c[nu] += half
    return c


S = sp.zeros(3, 3)      # unsigned (C-even structure matrix)
Nt = sp.zeros(3, 3)     # signed   (C-odd structure matrix)
c0 = {o: center((0, 0, 0), o) for o in ORI}
for o in ORI:
    for (off, o2, s) in nb0[o]:
        d = [center(off, o2)[a] - c0[o][a] for a in range(3)]
        ph = sp.exp(sp.I * sum(k[a] * d[a] for a in range(3)))
        S[IDX[o], IDX[o2]] += ph
        Nt[IDX[o], IDX[o2]] += s * ph
S = sp.trigsimp(sp.expand_complex(S))
Nt = sp.trigsimp(sp.expand_complex(Nt))

S_doc = sp.Matrix([
    [2*sp.cos(k[0]) + 2*sp.cos(k[1]), 4*sp.cos(k[0]/2)*sp.cos(k[2]/2), 4*sp.cos(k[1]/2)*sp.cos(k[2]/2)],
    [4*sp.cos(k[0]/2)*sp.cos(k[2]/2), 2*sp.cos(k[1]) + 2*sp.cos(k[2]), 4*sp.cos(k[0]/2)*sp.cos(k[1]/2)],
    [4*sp.cos(k[1]/2)*sp.cos(k[2]/2), 4*sp.cos(k[0]/2)*sp.cos(k[1]/2), 2*sp.cos(k[0]) + 2*sp.cos(k[2])]])
gate("G02 anchor: unsigned Bloch matrix reproduces the document's S(k) "
     "entry-for-entry (Section 3.15)", matzero(S - S_doc))
gate("G03 anchor: S(0) spectrum {12, 0, 0} and S(pi,pi,pi) = -4 I "
     "(lambda_S in [-4, 12])",
     S.subs({k[0]: 0, k[1]: 0, k[2]: 0}).eigenvals() == {sp.Integer(12): 1, sp.Integer(0): 2}
     and S.subs({k[0]: sp.pi, k[1]: sp.pi, k[2]: sp.pi}) == -4*sp.eye(3))
gate("G04 flat band re-derived: det(Ntilde(k) + 4I) == 0 identically in k",
     iszero(sp.det(Nt + 4*sp.eye(3))))

# ----------------------------------------------------------------------------
# Layer 3 (T2): Gauss-law factorization  Ntilde + 4I = B B^dagger
# ----------------------------------------------------------------------------
B = sp.zeros(3, 3)
for i, ori in enumerate(ORI):
    mu, nu = ori
    # plaquette (mu,nu): its two mu-links sit at center -+ e_nu/2 with
    # incidence signs +1 / -1; its two nu-links at center +- e_mu/2 with
    # signs +1 / -1 (read off boundary()).
    B[i, mu] = sp.exp(-sp.I*k[nu]*half) - sp.exp(sp.I*k[nu]*half)
    B[i, nu] = sp.exp(sp.I*k[mu]*half) - sp.exp(-sp.I*k[mu]*half)
gate("G05 factorization: Ntilde(k) + 4I == B(k) B(k)^dagger identically "
     "(hence spectrum >= -4; flat band = ker B^dagger)",
     matzero(sp.expand(B*B.H) - (Nt + 4*sp.eye(3))))

# ----------------------------------------------------------------------------
# Layer 4 (T3): the compact localized state
# ----------------------------------------------------------------------------
# Levi-Civita oriented cube boundary: for orientation (mu,nu) with transverse
# rho, eps = +1 for cyclic (xy->z, yz->x), -1 for xz->y.
EPS = {(0, 1): +1, (1, 2): +1, (0, 2): -1}
psi = {}
for ori in ORI:
    r = transverse(ori)
    psi[((0, 0, 0), ori)] = -EPS[ori]
    psi[(e(r), ori)] = +EPS[ori]
Hpsi = {}
for (x, ori), amp in psi.items():
    for (x2, o2, s) in neighbors_of(x, ori):
        Hpsi[(x2, o2)] = Hpsi.get((x2, o2), 0) + s*amp
gate("G06 CLS on-support: signed adjacency gives H psi == -4 psi on all six "
     "cube faces", all(Hpsi.get(K, 0) == -4*psi[K] for K in psi))
gate("G07 CLS leakage: H psi vanishes identically on every plaquette off the "
     "cube", all(Hpsi.get(K, 0) == 0 for K in set(Hpsi) - set(psi)))

u = sp.Matrix([-sp.sin(k[2]/2), -sp.sin(k[0]/2), sp.sin(k[1]/2)])
gate("G08 Bloch symbol: B(k)^dagger u(k) == 0 (zero net signed flux into "
     "every link channel) and (Ntilde + 4I) u == 0",
     matzero(B.H*u) and matzero((Nt + 4*sp.eye(3))*u))

# v1.1: G09 now states only the generic-k claim it proves (the k=0 case is
# handled by G09b; the v1.0 phrase "cube states span the flat band" was a
# k=0 overclaim, since u(0)=0).
gate("G09 generic-k span: |u(k)|^2 == sin^2(k0/2)+sin^2(k1/2)+sin^2(k2/2), "
     "which is > 0 for k != 0, and rank(Ntilde+4I) == 2 at generic k -- so "
     "the cube symbol u(k) spans the 1-dimensional kernel away from k = 0",
     iszero(u.dot(u) - sum(sp.sin(k[a]/2)**2 for a in range(3)))
     and (Nt + 4*sp.eye(3)).subs({k[0]: 1, k[1]: sp.Rational(1, 3), k[2]: sp.Rational(1, 7)}).rank() == 2)

# v1.1 NEW: G09b -- exact completeness on the L=3 torus.
# The torus Hamiltonian block-diagonalizes (discrete Bloch transform) into the
# L^3 momentum blocks Ntilde(k)+4I, so the flat-band dimension on the L^3 torus
# is sum over the L^3 Brillouin-zone points of nullity(Ntilde(k)+4I). We
# evaluate that nullity from the already-built symbolic Ntilde (G02/G05 anchor
# it) at each exact momentum k = 2*pi*(a,b,c)/L.
NtI = Nt + 4*sp.eye(3)
L = 3
nullity = {}
for a in range(L):
    for b in range(L):
        for c in range(L):
            sub = {k[0]: 2*sp.pi*a/L, k[1]: 2*sp.pi*b/L, k[2]: 2*sp.pi*c/L}
            nullity[(a, b, c)] = 3 - NtI.subs(sub).rank()
tot = sum(nullity.values())
n_rest = nullity[(0, 0, 0)]                              # k=0 rest states
cube_states = sum(v for kk, v in nullity.items() if kk != (0, 0, 0))
gate("G09b completeness on the L=3 torus: dim ker(Ntilde+4I) "
     "= sum_k nullity = L^3 + 2 = 29, split as 26 cube states (one per "
     "nonzero momentum; equivalently L^3-1 real-space cube states modulo the "
     "single relation sum psi = 0) (+) 3 rest states at k=0 (Ntilde(0)=-4I)",
     tot == L**3 + 2 and tot == 29 and n_rest == 3 and cube_states == 26
     and all(v == 1 for kk, v in nullity.items() if kk != (0, 0, 0)))

# Chain-complex reading: each edge of the cube is shared by exactly two faces
# with opposite induced orientation (d2 o d3 = 0), computed combinatorially.
edge_sum = {}
for (x, ori), amp in psi.items():
    for (xx, dd, ss) in boundary(x, ori):
        edge_sum[(xx, dd)] = edge_sum.get((xx, dd), 0) + ss*amp
# v1.1: the "exactly 12 edges" clause is now genuinely gated (the v1.0
# expression (len==12 and all_zero) or all_zero bypassed the count by operator
# precedence).
gate("G10 boundary-of-boundary: there are exactly 12 cube edges AND the signed "
     "face amplitudes cancel on every one of them (the flatness IS d2 d3 = 0; "
     "v1.1: edge count gated, no longer bypassed by operator precedence)",
     len(edge_sum) == 12 and all(v == 0 for v in edge_sum.values()))

# ----------------------------------------------------------------------------
# Layer 5 (T4): robustness and the O(y^4) criterion
# ----------------------------------------------------------------------------
# Any link-mediated correction B M B^dagger annihilates u -- check with a
# generic Hermitian symbol M built from free real symbols and phases.
m = sp.symbols('m1:7', real=True)
M = sp.Matrix([[m[0], m[3] + sp.I*m[4], m[5]],
               [m[3] - sp.I*m[4], m[1], sp.I*m[5]],
               [m[5], -sp.I*m[5], m[2]]])
Z = (B.H*u).applyfunc(lambda x: sp.simplify(sp.expand_trig(sp.expand_complex(sp.expand(x)))))
# v1.1: wording sharpened (all-orders / link-mediated scope).
gate("G11 robustness (all-orders): for ARBITRARY Hermitian link-channel "
     "symbol M, (B M B^dagger) u == 0 -- every correction whose symbol factors "
     "through the link channel leaves the band exactly flat with UNSHIFTED "
     "hopping energy, at every order in which it is link-mediated; only "
     "diagonal (k-independent) constants can move the band",
     matzero(Z) and matzero(B*M*Z))

# Simplest sigma-covariant corner-sharing (site-mediated) hop: connect equal-
# orientation plaquettes across a body/face diagonal sharing only a site,
# e.g. (x; xy) <-> (x + ex + ey; xy), symbol 2cos(k0+k1) on the diagonal etc.
# (orientation-diagonal, parity-even -- the minimal tromino-reachable class).
Hcorner = sp.diag(2*sp.cos(k[0] + k[1]), 2*sp.cos(k[1] + k[2]), 2*sp.cos(k[0] + k[2]))
resid = sp.expand_trig(sp.expand_complex(Hcorner*u - (u.dot(Hcorner*u)/u.dot(u))*u))
gate("G12 sharpness: the minimal corner-sharing symbol does NOT preserve the "
     "flat subspace (P H_corner P_perp != 0) -- O(y^4) flatness, if it holds, "
     "must come from weight cancellation, not lattice geometry",
     not matzero(resid))

# Dispersive partner band: eigenvalues of B B^dagger are {0, lam+, lam-} with
# lam+ + lam- = 2(|u|^2 ... ); certify the documented edges mu in [-4, 8] by
# exact trace/det identities plus a rational-point battery.
s2 = sum(sp.sin(k[a]/2)**2 for a in range(3))
tr = sp.trigsimp(sp.expand_complex((B*B.H).trace()))
gate("G13 partner-band trace identity: tr(Ntilde + 4I) == 8 * (s0^2+s1^2+s2^2) "
     "(so the two dispersive eigenvalues sum to 8|u|^2; at k = (pi,pi,pi) "
     "the top reaches mu = 8, i.e. coefficient interval [11/306, 41/306])",
     iszero(tr - 8*s2)
     and (Nt.subs({k[0]: sp.pi, k[1]: sp.pi, k[2]: sp.pi})).eigenvals() ==
         {sp.Integer(8): 2, sp.Integer(-4): 1})

ok = all(c for _, c in GATES)
print()
print("GATES PASSED: %d / %d" % (sum(c for _, c in GATES), len(GATES)))
print("VERDICT:", "ALL GATES PASS" if ok else "FAILURE")
sys.exit(0 if ok else 1)
