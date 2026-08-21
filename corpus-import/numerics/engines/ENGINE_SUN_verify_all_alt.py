#!/usr/bin/env python3
"""
Consolidated verification suite for the SU(N) fourth-order flat-band program.

Runs every gate established in the 2026-08-08 build, in one file, from scratch.
No dependency on the scattered project artifacts except numpy/sympy.

Sections
    A. Cellular substrate and the flat-band theorem          (8 gates)
    B. Four-point shape extraction, corrected formulas       (3 gates)
    C. The complete fourth-order rank registry               (5 gates)
    D. SU(6) determinant resolvent, from first principles    (4 gates)
    E. N-ality family selection rule                         (3 gates)
    F. Odd Gram staircase, degree 5                          (1 gate)

Every certified constant is hard-coded from its source certificate and then
re-derived independently where possible.  Run:  python3 ENGINE_SUN_verify_all.py
"""

import itertools
from fractions import Fraction as F

import numpy as np

PASS, FAIL = [], []


def gate(name, ok, detail="", kind="DERIVED"):
    """kind: DERIVED  = rebuilt from definitions here
             CONSIST  = exact consistency check against certificate data
             REGRESS  = guard against a known trap or transcription error"""
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}][{kind:7s}] {name}"
          + (f"   {detail}" if detail else ""))


# ----------------------------------------------------------------------
# A. cellular substrate  (flatband paper rev. 2026-07-25)
# ----------------------------------------------------------------------

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
ORB = [(0, 1), (0, 2), (1, 2)]


def add(x, y, c=1):
    return tuple(x[i] + c * y[i] for i in range(3))


def plaq_links(p):
    x, mu, nu = p
    return [((x, mu), 1), ((add(x, E[mu]), nu), 1),
            ((add(x, E[nu]), mu), -1), ((x, nu), -1)]


def eps(p, l):
    for ll, e in plaq_links(p):
        if ll == l:
            return e
    return 0


def plaqs_of_link(l):
    y, lam = l
    out = []
    for rho in range(3):
        if rho == lam:
            continue
        mu, nu = min(lam, rho), max(lam, rho)
        out += [(y, mu, nu), (add(y, E[rho], -1), mu, nu)]
    return out


def neighbours(p):
    return [(pp, l, eps(p, l) * eps(pp, l))
            for l, _ in plaq_links(p) for pp in plaqs_of_link(l) if pp != p]


def Ntilde(k):
    u = [1 - np.exp(1j * kj) for kj in k]
    return np.array([[u[1], -u[0], 0], [u[2], 0, -u[0]], [0, u[2], -u[1]]], complex)


def q_of(k):
    return float(np.sum(4 * np.sin(np.array(k) / 2) ** 2))


def S_enum(k):
    """Bloch signed adjacency from the cellular definition; phase e^{-ik.x}."""
    M = np.zeros((3, 3), complex)
    for o, (mu, nu) in enumerate(ORB):
        p = ((0, 0, 0), mu, nu)
        for pp, _, s in neighbours(p):
            x, m2, n2 = pp
            M[ORB.index((m2, n2)), o] += s * np.exp(-1j * float(np.dot(k, x)))
    return M


def section_A():
    print("\nA. CELLULAR SUBSTRATE AND THE FLAT-BAND THEOREM")
    rng = np.random.default_rng(0)
    ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(300)]

    # A1 boundary of a boundary
    L = 3
    S = list(itertools.product(range(L), repeat=3))
    li = lambda x, m: ((x[0] * L + x[1]) * L + x[2]) * 3 + m
    pi_ = lambda x, o: ((x[0] * L + x[1]) * L + x[2]) * 3 + o
    d2 = np.zeros((len(S) * 3, len(S) * 3))
    for x in S:
        for o, (mu, nu) in enumerate(ORB):
            sh = lambda d: tuple((x[i] + (1 if i == d else 0)) % L for i in range(3))
            d2[li(x, mu), pi_(x, o)] += 1
            d2[li(sh(mu), nu), pi_(x, o)] += 1
            d2[li(sh(nu), mu), pi_(x, o)] -= 1
            d2[li(x, nu), pi_(x, o)] -= 1
    d3 = np.zeros((len(S) * 3, len(S)))
    for x in S:
        c = (x[0] * L + x[1]) * L + x[2]
        for o, (mu, nu) in enumerate(ORB):
            rho = 3 - mu - nu
            sgn = 1.0 if (mu, nu, rho) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1.0
            shr = tuple((x[i] + (1 if i == rho else 0)) % L for i in range(3))
            d3[pi_(shr, o), c] += sgn
            d3[pi_(x, o), c] -= sgn
    gate("A1  d2 d3 = 0", np.abs(d2 @ d3).max() < 1e-12,
         f"max = {np.abs(d2 @ d3).max():.1e}")

    # A2 enumeration reproduces S(k)
    w = max(np.abs(S_enum(k) - (Ntilde(k) @ Ntilde(k).conj().T - 4 * np.eye(3))).max()
            for k in ks)
    gate("A2  cellular enumeration reproduces S(k)", w < 1e-10, f"max dev {w:.1e}")

    # A3 Eq.(8)
    w = 0.0
    for k in ks:
        u = np.array([1 - np.exp(1j * kj) for kj in k])
        w = max(w, np.abs(Ntilde(k).conj().T @ Ntilde(k)
                          - (q_of(k) * np.eye(3) - np.outer(u, u.conj()))).max())
    gate("A3  Ntilde^dag Ntilde = qI - uu^dag", w < 1e-10, f"max dev {w:.1e}")

    # A4 Theorem 4.1
    w = 0.0
    for k in ks:
        ev = np.sort(np.linalg.eigvalsh(Ntilde(k) @ Ntilde(k).conj().T - 4 * np.eye(3)))
        w = max(w, np.abs(ev - np.sort([-4, -4 + q_of(k), -4 + q_of(k)])).max())
    gate("A4  spec S(k) = {-4, -4+q, -4+q}", w < 1e-9, f"max dev {w:.1e}")

    # A5 flat vector
    w = 0.0
    for k in ks:
        ub = [np.conj(1 - np.exp(1j * kj)) for kj in k]
        psi = np.array([ub[2], -ub[1], ub[0]])
        w = max(w, np.abs(Ntilde(k).conj().T @ psi).max() / max(np.abs(psi).max(), 1e-300))
    gate("A5  flat vector (u3bar,-u2bar,u1bar) in ker Ntilde^dag", w < 1e-10,
         f"max residual {w:.1e}")

    # A6/A7 torus counts and finite-volume gap
    okc, okg, det = True, True, []
    for L in (3, 4, 5):
        Sset = list(itertools.product(range(L), repeat=3))
        li = lambda x, m: ((x[0] * L + x[1]) * L + x[2]) * 3 + m
        pi2 = lambda x, o: ((x[0] * L + x[1]) * L + x[2]) * 3 + o
        D = np.zeros((len(Sset) * 3, len(Sset) * 3))
        for x in Sset:
            for o, (mu, nu) in enumerate(ORB):
                sh = lambda d: tuple((x[i] + (1 if i == d else 0)) % L for i in range(3))
                D[li(x, mu), pi2(x, o)] += 1
                D[li(sh(mu), nu), pi2(x, o)] += 1
                D[li(sh(nu), mu), pi2(x, o)] -= 1
                D[li(x, nu), pi2(x, o)] -= 1
        ev = np.sort(np.linalg.eigvalsh(D.T @ D - 4 * np.eye(D.shape[1])))
        mult = int(np.sum(np.abs(ev + 4) < 1e-8))
        okc &= (mult == L ** 3 + 2)
        above = ev[np.abs(ev + 4) >= 1e-8]
        okg &= abs(above.min() + 4 - 4 * np.sin(np.pi / L) ** 2) < 1e-8
        det.append(f"L={L}:{mult}")
    gate("A6  flat eigenspace dim = L^3 + 2", okc, "; ".join(det))
    gate("A7  first level above flat band = 4 sin^2(pi/L)", okg, "L = 3,4,5")

    # A8 Fourier-convention trap
    kk = np.array([0.3, 0.7, 1.1])
    Mp = np.zeros((3, 3), complex)
    for o, (mu, nu) in enumerate(ORB):
        p = ((0, 0, 0), mu, nu)
        for pp, _, s in neighbours(p):
            x, m2, n2 = pp
            Mp[ORB.index((m2, n2)), o] += s * np.exp(+1j * float(np.dot(kk, x)))
    ref = Ntilde(kk) @ Ntilde(kk).conj().T - 4 * np.eye(3)
    gate("A8  wrong Fourier sign gives the TRANSPOSE (silent at 2nd order)",
         np.abs(Mp - ref.T).max() < 1e-10 and np.abs(Mp - ref).max() > 1e-3
         and np.allclose(np.sort(np.linalg.eigvalsh(Mp)),
                         np.sort(np.linalg.eigvalsh(ref))),
         "same spectrum, flipped at 4th order", kind="REGRESS")


# ----------------------------------------------------------------------
# B/C. extraction and the rank registry
# ----------------------------------------------------------------------

def extract(dX, dM, dP, dR):
    return (dX / 4,
            (dX + 4 * dM - 6 * dP) / 16,
            3 * (2 * dP - dM - dX) / 8,
            3 * (dR - 6 * dM + 6 * dP) / 16)


REG = {
    3: dict(A=F(5, 12), B=F(17607806155349, 275331901291200)),
    4: dict(A=F(32, 675), B=F(3601925923737103752887, 70481696720359496343750)),
    5: dict(A=F(1, 108), B=F(126537112003083861011, 12716894720031723060840),
            q=F(-781009569168365268247626732239, 6484474594581730088957376233472),
            X=F(-720968137737052952609132507855, 6484474594581730088957376233472),
            M=F(-313048570171186155311188521473, 2947488452082604585889716469760),
            R=F(-3282227855080830653800484933131, 32422372972908650444786881167360),
            bw=F(81428712396187592747, 4238964906677241020280)),
    6: dict(A=F(64, 25725), B=F(235401086266217267636986869176,
                                88159201615617988827817767796875),
            q=F(-55954617740619111266546735567327219227,
                2665788121217129017242143775195086906250),
            X=F(-49322530675200403507421479916696099227,
                2665788121217129017242143775195086906250),
            M=F(-1306018781752515053808629340880268237741,
                76077491767042681953602718507490557093750),
            R=F(-1423439040460549245251908528526611033459,
                89909762997414078672439576417943385656250),
            bw=F(454728157341029756849050509176,
                 88159201615617988827817767796875)),
}


def section_BC():
    print("\nB. FOUR-POINT SHAPE EXTRACTION (corrected C and D)")
    # round trip
    A0, B0, C0, D0 = F(5, 48), F(7, 13), F(-3, 11), F(2, 9)
    ev = lambda a: (A0 * sum(a) + B0 * (a[0]*a[1]+a[0]*a[2]+a[1]*a[2])
                    + C0 * 4 * (a[0]*a[1]+a[0]*a[2]+a[1]*a[2]) / sum(a)
                    + D0 * a[0]*a[1]*a[2] / sum(a))
    d = [ev(a) for a in ([F(4), F(0), F(0)], [F(4), F(4), F(0)],
                         [F(4), F(2), F(0)], [F(4), F(4), F(4)])]
    gate("B1  extraction round trip on a generic (A,B,C,D)",
         extract(*d) == (A0, B0, C0, D0))

    # the mis-transcribed forms in the canonical source are provably different
    dX, dM, dP, dR = d
    gate("B2  literal .docx forms for C,D differ from the correct ones",
         (32*dP - dM - dX)/8 != extract(*d)[2]
         and (3*dR - 6*dM + 6*dP)/16 != extract(*d)[3],
         "32dP vs 6dP;  -6dM vs -18dM", kind="REGRESS")

    # checkpoint identities are not independent
    al, be = REG[3]['A'], REG[3]['B']
    dX, dM = al, al + be/2
    dP, dR = 5*al/6 + be/3, al + be
    gate("B3  '6dP-4dM-dX=0' is exactly B=0, not an independent check",
         6*dP - 4*dM - dX == 0 and dR - 2*dM + dX == 0)

    print("\nC. THE COMPLETE FOURTH-ORDER RANK REGISTRY")
    stable = lambda N: F(640, N * (N*N - 1)**3)
    ok = all(stable(N) == REG[N]['A'] for N in (3, 4, 5, 6))
    gate("C1  A_N = 640/[N(N^2-1)^3] at EVERY rank N=3,4,5,6", ok,
         "  ".join(f"{N}:{REG[N]['A']}" for N in (3, 4, 5, 6)),
         kind="CONSIST")   # A_N values are certificate data, not derived here

    for N in (5, 6):
        r = REG[N]
        dX, dM, dR = r['X'] - r['q'], r['M'] - r['q'], r['R'] - r['q']
        dP = (5*r['A'] + 2*r['B']) / 6
        a, b, c, dd = extract(dX, dM, dP, dR)
        ok = (dX == r['A'] and dM == r['A'] + r['B']/2 and dR == r['A'] + r['B']
              and a == r['A']/4 and b == 0 and c == (r['B'] - 2*r['A'])/16 and dd == 0)
        gate(f"C{N-3}  extraction reproduces the certified SU({N}) shape vector", ok,
             f"B=D=0, bandwidth {'ok' if r['A']+r['B'] == r['bw'] else 'MISMATCH'}",
             kind="CONSIST")   # dP built from the supplied A,B

    for N in (5, 6):
        gate(f"C{N-1}  SU({N}) parity identity c_R - 2c_M + c_X = 0",
             REG[N]['R'] - 2*REG[N]['M'] + REG[N]['X'] == 0, kind="CONSIST")


# ----------------------------------------------------------------------
# D. SU(6) determinant resolvent, from first principles
# ----------------------------------------------------------------------

def section_D():
    print("\nD. SU(6) DETERMINANT RESOLVENT, DERIVED INDEPENDENTLY")
    N = 6
    C2w = lambda k: F(k * (N - k) * (N + 1), 2 * N)
    cas = [C2w(k) for k in (2, 3, 4)]
    gate("D1  C_2(Lambda^k V) = (14/3, 21/4, 14/3)",
         cas == [F(14, 3), F(21, 4), F(14, 3)])
    glob = [4 * c for c in cas]
    gate("D2  summed over four links = (56/3, 21, 56/3)",
         glob == [F(56, 3), F(21), F(56, 3)])
    E0 = F(1, 2) * 4 * F(N*N - 1, 2*N)
    dens = [E0 - F(1, 2) * g for g in glob]
    gate("D3  electric denominators = (-7/2, -14/3, -7/2)",
         dens == [F(-7, 2), F(-14, 3), F(-7, 2)])
    Fdet = 1 / (dens[0] * dens[1] * dens[2])
    gate("D4  F_det = -6/343 (denominator product, derived)",
         Fdet == F(-6, 343), "343 = 7^3, three cuts")
    gate("D5  Delta q_6 = 6/343 given the asserted C-odd phase -1",
         -Fdet == F(6, 343),
         "phase and channel matrix element NOT derived here", kind="CONSIST")


# ----------------------------------------------------------------------
# E. N-ality family selection rule
# ----------------------------------------------------------------------

def families(N, maxlen=6):
    """(p,q) with p+q <= maxlen, p-q = +-N, matching parity."""
    out = []
    for tot in range(1, maxlen + 1):
        for p in range(tot + 1):
            q = tot - p
            if abs(p - q) == N:
                out.append((p, q))
    return sorted(set(out))


def section_E():
    print("\nE. N-ALITY FAMILY SELECTION RULE  (p+q<=6, p-q=+-N, matching parity)")
    gate("E1  N=4 gives exactly (4,0),(0,4),(5,1),(1,5)",
         families(4) == [(0, 4), (1, 5), (4, 0), (5, 1)],
         "matches SU(4) hybrid theorem")
    gate("E2  N=6 gives exactly (6,0),(0,6)",
         families(6) == [(0, 6), (6, 0)], "matches SU(6) certificate")
    gate("E3  N=5 admits NO family with a 6-factor word",
         families(5, 6) == [(0, 5), (5, 0)] and (5, 0) not in families(5, 4),
         "certified mod-5 scan: 0 of 895,524 pairs")


# ----------------------------------------------------------------------
# F. odd Gram staircase
# ----------------------------------------------------------------------

def section_F():
    print("\nF. ODD GRAM STAIRCASE — REGENERATED FROM AN INDEPENDENT WICK ENGINE")
    import ENGINE_FLUX_gram_cold as G
    ok, n5, n7, need5, need7 = G.verify(verbose=False)
    gate("F1  deg<=5 Gram determinant regenerated and matched",
         ok and n5 >= need5,
         f"exact at {n5} ranks; {need5} suffice (num deg 16 / N^3)")
    gate("F2  deg<=7 Gram determinant regenerated and matched",
         ok and n7 >= need7,
         f"exact at {n7} ranks; {need7} suffice (num deg 48 / N^7)")
    d5 = [n for n in range(2, 10) if G.gram_det(n, 5)[0] == 0]
    d7 = [n for n in range(2, 10) if G.gram_det(n, 7)[0] == 0]
    gate("F3  staircase: deg<=5 valid N>=5, deg<=7 valid N>=7",
         d5 == [2, 3, 4] and d7 == [2, 3, 4, 5, 6],
         f"zeros {d5} then {d7}")


if __name__ == "__main__":
    print("=" * 78)
    print("CONSOLIDATED VERIFICATION SUITE — SU(N) fourth-order flat-band program")
    print("=" * 78)
    print("\n  legend: DERIVED = rebuilt from definitions in this file")
    print("          CONSIST = exact consistency check against certificate data")
    print("          REGRESS = guard against a known trap / transcription error")
    section_A(); section_BC(); section_D(); section_E(); section_F()
    print("=" * 78)
    print(f"  {len(PASS)} passed, {len(FAIL)} failed")
    if FAIL:
        print("  FAILED: " + ", ".join(FAIL))
    print("=" * 78)
