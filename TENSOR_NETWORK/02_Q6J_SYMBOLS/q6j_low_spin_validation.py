# q6j_low_spin_validation.py
# Self-contained low-spin validation suite for the U_q(su2) (quantum) 6j symbol.
#
# Goal: make the q–6j kernel indisputably correct on low spins *before* scaling.
#
# What this script does:
#   1) θ=0: compares the Racah-formula implementation to SymPy's wigner_6j (independent reference).
#   2) θ>0: compares a log-space "kernel" implementation to an independent high-precision direct-product implementation.
#   3) Checks tetrahedral symmetries (generated from the standard allowed symmetry operations).
#   4) Checks the (quantum) orthogonality relation (unitarity of the recoupling transform).
#
# Run (in Colab or local):
#   python q6j_low_spin_validation.py
#
# Notes:
# - Spins are represented as integers A=2j to avoid float parity bugs.
# - For root-of-unity test angles θ = π/(k+2) with k large enough, quantum integers [n]_q are positive for small n,
#   so everything stays real and branch-cut drama is minimized.

import math
import cmath
from functools import lru_cache
from itertools import product, permutations
import random

# ---------- Optional deps ----------
try:
    import mpmath as mp
except Exception as e:
    raise RuntimeError("mpmath is required. In Colab: pip install mpmath") from e

try:
    import sympy as sp
    from sympy import Rational
    from sympy.physics.wigner import wigner_6j
except Exception as e:
    raise RuntimeError("sympy is required for the θ=0 independent reference check. In Colab: pip install sympy") from e


# -------------------------
# Basic admissibility logic
# -------------------------
def tri_admissible(A: int, B: int, C: int) -> bool:
    """Triangle admissibility for SU(2) with spins encoded as A=2j.

    Conditions:
      |A-B| <= C <= A+B
      A+B+C even  (i.e. j1+j2+j3 is integer)
    """
    return (abs(A - B) <= C <= (A + B)) and ((A + B + C) % 2 == 0)


def sixj_admissible(A: int, B: int, C: int, D: int, E: int, F: int) -> bool:
    """Admissibility of {A B C; D E F} in 2j-encoding."""
    return (tri_admissible(A, B, C) and
            tri_admissible(A, E, F) and
            tri_admissible(D, B, F) and
            tri_admissible(D, E, C))


# -------------------------
# Quantum integers / factorials
# -------------------------
def _theta_key(theta: float) -> float:
    # Stabilize caching keys for floats.
    return float(f"{theta:.16e}")


@lru_cache(maxsize=None)
def qint(n: int, theta_key: float) -> float:
    """Quantum integer [n]_q for q = exp(iθ), using the sin ratio.

    For θ→0, [n]_q → n.
    """
    theta = theta_key
    if abs(theta) < 1e-16:
        return float(n)
    s = math.sin(theta)
    if abs(s) < 1e-30:
        # extremely close to 0: fallback to classical
        return float(n)
    return math.sin(n * theta) / s


@lru_cache(maxsize=None)
def qfact(n: int, theta_key: float) -> float:
    """Quantum factorial [n]_q! = Π_{m=1..n} [m]_q."""
    if n < 0:
        return 0.0
    if n == 0:
        return 1.0
    prod = 1.0
    for m in range(1, n + 1):
        prod *= qint(m, theta_key)
    return prod


@lru_cache(maxsize=None)
def log_qfact(n: int, theta_key: float) -> complex:
    """Complex log of [n]_q! (needed for the log-space kernel)."""
    if n < 0:
        return complex(-math.inf, 0.0)
    if n == 0:
        return 0.0 + 0.0j
    s = 0.0 + 0.0j
    for m in range(1, n + 1):
        v = qint(m, theta_key)
        if abs(v) < 1e-30:
            return complex(-math.inf, 0.0)
        s += cmath.log(v)  # handles v<0 by adding iπ
    return s


def _delta_args(A: int, B: int, C: int):
    """Return integer factorial arguments used in Δ(A,B,C) in 2j encoding."""
    x1 = (A + B - C) // 2
    x2 = (A - B + C) // 2
    x3 = (-A + B + C) // 2
    x4 = (A + B + C) // 2 + 1
    return x1, x2, x3, x4


def qdelta_direct(A: int, B: int, C: int, theta_key: float) -> complex:
    """Δ_q(A,B,C) computed directly (not log-space)."""
    if not tri_admissible(A, B, C):
        return 0.0 + 0.0j
    x1, x2, x3, x4 = _delta_args(A, B, C)
    val = qfact(x1, theta_key) * qfact(x2, theta_key) * qfact(x3, theta_key) / qfact(x4, theta_key)
    return cmath.sqrt(val)


def qdelta_log(A: int, B: int, C: int, theta_key: float) -> complex:
    """log Δ_q(A,B,C)"""
    if not tri_admissible(A, B, C):
        return complex(-math.inf, 0.0)
    x1, x2, x3, x4 = _delta_args(A, B, C)
    l1 = log_qfact(x1, theta_key)
    l2 = log_qfact(x2, theta_key)
    l3 = log_qfact(x3, theta_key)
    l4 = log_qfact(x4, theta_key)
    if (math.isinf(l1.real) or math.isinf(l2.real) or math.isinf(l3.real) or math.isinf(l4.real)):
        return complex(-math.inf, 0.0)
    return 0.5 * (l1 + l2 + l3 - l4)


# -------------------------
# q–6j symbol: two independent implementations
# -------------------------
def q6j_kernel_log(A: int, B: int, C: int, D: int, E: int, F: int, theta: float) -> complex:
    """Log-space "kernel" implementation (mirrors the structure in CLEANRUN.pdf)."""
    if not sixj_admissible(A, B, C, D, E, F):
        return 0.0 + 0.0j

    tk = _theta_key(theta)

    # Prefactor: product of 4 deltas (in log)
    log_pref = (
        qdelta_log(A, B, C, tk) +
        qdelta_log(A, E, F, tk) +
        qdelta_log(D, B, F, tk) +
        qdelta_log(D, E, C, tk)
    )

    if math.isinf(log_pref.real):
        return 0.0 + 0.0j

    # Define the integer sums used in Racah formula
    t1 = (A + B + C) // 2
    t2 = (A + E + F) // 2
    t3 = (D + B + F) // 2
    t4 = (D + E + C) // 2

    u1 = (A + B + D + E) // 2
    u2 = (B + C + E + F) // 2
    u3 = (C + A + F + D) // 2

    k_min = max(t1, t2, t3, t4)
    k_max = min(u1, u2, u3)

    s = 0.0 + 0.0j
    for k in range(k_min, k_max + 1):
        log_num = cmath.log((-1) ** k) + log_qfact(k + 1, tk)
        den_args = [
            k - t1, k - t2, k - t3, k - t4,
            u1 - k, u2 - k, u3 - k
        ]
        log_den = 0.0 + 0.0j
        for a in den_args:
            log_den += log_qfact(a, tk)
        term = cmath.exp(log_pref + log_num - log_den)
        s += term
    return s


# ---- High-precision direct reference (independent numeric route) ----
mp.mp.dps = 80


def qint_mp(n: int, theta: float) -> mp.mpf:
    if abs(theta) < 1e-30:
        return mp.mpf(n)
    return mp.sin(n * theta) / mp.sin(theta)


@lru_cache(maxsize=None)
def qfact_mp(n: int, theta_key: float) -> mp.mpf:
    theta = float(theta_key)
    if n < 0:
        return mp.mpf("0")
    if n == 0:
        return mp.mpf("1")
    prod = mp.mpf("1")
    for m in range(1, n + 1):
        prod *= qint_mp(m, theta)
    return prod


def qdelta_mp(A: int, B: int, C: int, theta: float) -> mp.mpf:
    if not tri_admissible(A, B, C):
        return mp.mpf("0")
    x1, x2, x3, x4 = _delta_args(A, B, C)
    tk = _theta_key(theta)
    val = qfact_mp(x1, tk) * qfact_mp(x2, tk) * qfact_mp(x3, tk) / qfact_mp(x4, tk)
    return mp.sqrt(val)


def q6j_reference_mp(A: int, B: int, C: int, D: int, E: int, F: int, theta: float) -> mp.mpf:
    """Independent (high precision) reference via direct products, no complex logs."""
    if not sixj_admissible(A, B, C, D, E, F):
        return mp.mpf("0")

    # Prefactor (product of deltas)
    pref = (
        qdelta_mp(A, B, C, theta) *
        qdelta_mp(A, E, F, theta) *
        qdelta_mp(D, B, F, theta) *
        qdelta_mp(D, E, C, theta)
    )

    t1 = (A + B + C) // 2
    t2 = (A + E + F) // 2
    t3 = (D + B + F) // 2
    t4 = (D + E + C) // 2

    u1 = (A + B + D + E) // 2
    u2 = (B + C + E + F) // 2
    u3 = (C + A + F + D) // 2

    k_min = max(t1, t2, t3, t4)
    k_max = min(u1, u2, u3)

    tk = _theta_key(theta)

    s = mp.mpf("0")
    for k in range(k_min, k_max + 1):
        num = ((-1) ** k) * qfact_mp(k + 1, tk)
        den = (
            qfact_mp(k - t1, tk) * qfact_mp(k - t2, tk) *
            qfact_mp(k - t3, tk) * qfact_mp(k - t4, tk) *
            qfact_mp(u1 - k, tk) * qfact_mp(u2 - k, tk) * qfact_mp(u3 - k, tk)
        )
        s += num / den

    return pref * s


# -------------------------
# Independent θ=0 reference via SymPy
# -------------------------
def sympy_6j(A: int, B: int, C: int, D: int, E: int, F: int) -> complex:
    """Independent reference: SymPy's wigner_6j (classical)."""
    a = Rational(A, 2)
    b = Rational(B, 2)
    c = Rational(C, 2)
    d = Rational(D, 2)
    e = Rational(E, 2)
    f = Rational(F, 2)
    # SymPy raises on non-admissible tuples; we treat them as 0 by convention.
    try:
        val = wigner_6j(a, b, c, d, e, f)
        return complex(val.evalf(50))
    except Exception:
        return 0.0 + 0.0j


# -------------------------
# Symmetry orbit generation (24 tetrahedral symmetries)
# -------------------------
def permute_columns(tup, perm):
    """Permute columns of the 2x3 array.
    Columns are pairs: (A,D), (B,E), (C,F).
    """
    A, B, C, D, E, F = tup
    cols = [(A, D), (B, E), (C, F)]
    cols_p = [cols[i] for i in perm]
    A2, D2 = cols_p[0]
    B2, E2 = cols_p[1]
    C2, F2 = cols_p[2]
    return (A2, B2, C2, D2, E2, F2)


def swap_rows_in_two_columns(tup, which):
    """Swap upper/lower entries in exactly TWO columns (a known symmetry operation)."""
    A, B, C, D, E, F = tup
    cols = [(A, D), (B, E), (C, F)]
    i, j = which
    cols[i] = (cols[i][1], cols[i][0])
    cols[j] = (cols[j][1], cols[j][0])
    (A2, D2), (B2, E2), (C2, F2) = cols
    return (A2, B2, C2, D2, E2, F2)


def symmetry_orbit(tup):
    """Generate the full symmetry orbit under:
       - all column permutations
       - swap-rows in any TWO columns
    """
    ops = []
    perms = list(permutations([0, 1, 2]))
    for p in perms:
        ops.append(lambda x, p=p: permute_columns(x, p))
    for which in [(0, 1), (0, 2), (1, 2)]:
        ops.append(lambda x, which=which: swap_rows_in_two_columns(x, which))

    seen = set()
    frontier = [tup]
    while frontier:
        x = frontier.pop()
        if x in seen:
            continue
        seen.add(x)
        for op in ops:
            y = op(x)
            if y not in seen:
                frontier.append(y)
    return seen


# -------------------------
# Test suite
# -------------------------
def enumerate_admissible(Jmax: float):
    twoJ = int(round(2 * Jmax))
    twos = range(0, twoJ + 1)
    out = []
    for A, B, C, D, E, F in product(twos, repeat=6):
        if sixj_admissible(A, B, C, D, E, F):
            out.append((A, B, C, D, E, F))
    return out


def qdim(A: int, theta: float) -> float:
    """Quantum dimension d_j = [2j+1]_q = [A+1]_q."""
    return qint(A + 1, _theta_key(theta))


def allowed_intermediate_twoj(A: int, B: int, C: int, D: int):
    """X allowed such that (A,B,X) and (C,D,X) are admissible."""
    # brute force over a reasonable small range (low-spin tests)
    max_two = A + B  # worst-case
    xs = []
    for X in range(0, max_two + 1):
        if tri_admissible(A, B, X) and tri_admissible(C, D, X):
            xs.append(X)
    return xs


def test_theta0_vs_sympy(Jmax=2.0, tol=1e-12):
    tuples = enumerate_admissible(Jmax)
    worst = 0.0
    worst_t = None
    for t in tuples:
        A, B, C, D, E, F = t
        v_kernel = q6j_kernel_log(A, B, C, D, E, F, theta=0.0)
        v_sym = sympy_6j(A, B, C, D, E, F)
        err = abs(v_kernel - v_sym)
        if err > worst:
            worst = err
            worst_t = t
        if err > tol:
            raise AssertionError(f"θ=0 mismatch > tol for {t}: kernel={v_kernel}, sympy={v_sym}, err={err}")
    print(f"[PASS] θ=0 matches SymPy for all admissible 6j up to Jmax={Jmax}. Worst err={worst:.3e} at {worst_t}")


def test_q_kernel_vs_reference(Jmax=2.0, theta=math.pi/22, tol=5e-13):
    tuples = enumerate_admissible(Jmax)
    worst = 0.0
    worst_t = None
    for t in tuples:
        A, B, C, D, E, F = t
        v_kernel = q6j_kernel_log(A, B, C, D, E, F, theta=theta)
        v_ref = q6j_reference_mp(A, B, C, D, E, F, theta=theta)
        v_ref_c = complex(v_ref)  # should be real for this theta
        err = abs(v_kernel - v_ref_c)
        if err > worst:
            worst = err
            worst_t = t
        if err > tol:
            raise AssertionError(f"q mismatch > tol for {t}: kernel={v_kernel}, ref={v_ref_c}, err={err}")
    print(f"[PASS] q–6j kernel matches independent MP reference at θ={theta:.6f} for all admissible 6j up to Jmax={Jmax}. Worst err={worst:.3e} at {worst_t}")


def test_symmetries(Jmax=2.0, theta=math.pi/22, samples=50, tol=5e-13):
    tuples = enumerate_admissible(Jmax)
    random.shuffle(tuples)
    tuples = tuples[:min(samples, len(tuples))]

    for t in tuples:
        v0 = q6j_kernel_log(*t, theta=theta)
        orb = symmetry_orbit(t)
        for t2 in orb:
            if not sixj_admissible(*t2):
                # Symmetry orbit should mostly stay admissible, but we skip if not.
                continue
            v2 = q6j_kernel_log(*t2, theta=theta)
            if abs(v0 - v2) > tol:
                raise AssertionError(f"Symmetry failed: {t} vs {t2} at θ={theta}: {v0} vs {v2}")
    print(f"[PASS] Symmetry orbit checks passed on {len(tuples)} random admissible 6j (Jmax={Jmax}, θ={theta:.6f}).")


def test_orthogonality(theta=math.pi/22, tol=5e-12):
    # A small deterministic set of cases is nicer than random for reproducibility.
    # We'll test a=b=c=d=1/2 in 2j encoding: A=B=C=D=1
    A = B = C = D = 1
    # allowed e values are intersection of (A,D,e) and (C,B,e)
    es = [E for E in range(0, A + D + 1) if tri_admissible(A, D, E) and tri_admissible(C, B, E)]
    xs = [X for X in range(0, A + B + 1) if tri_admissible(A, B, X) and tri_admissible(C, D, X)]

    # Build M_{E,E'} = sum_X dim(X) * 6j(A,B,X; C,D,E)*6j(A,B,X; C,D,E')
    for E in es:
        for Ep in es:
            s = 0.0 + 0.0j
            for X in xs:
                dimX = qdim(X, theta)
                s += dimX * q6j_kernel_log(A, B, X, C, D, E, theta=theta) * q6j_kernel_log(A, B, X, C, D, Ep, theta=theta)
            rhs = (1.0 / qdim(E, theta)) if (E == Ep) else 0.0
            if abs(s - rhs) > tol:
                raise AssertionError(f"Orthogonality failed at θ={theta}: E={E},Ep={Ep}, LHS={s}, RHS={rhs}")
    print(f"[PASS] Orthogonality check passed at θ={theta:.6f} (tested a=b=c=d=1/2 case).")


def main():
    print("============================================================")
    print(" Low-spin q–6j validation suite")
    print("============================================================")
    # Your original Stage-A symmetry test used {1 1 1; 1/2 1/2 1/2} == {1/2 1/2 1/2; 1 1 1}.
    # The second tuple is NOT admissible because (1/2+1/2+1/2) is not an integer.
    # So a robust test suite must *never* assume a symmetry that maps outside admissible space.

    # 1) Classical agreement
    test_theta0_vs_sympy(Jmax=2.0)

    # 2) q agreement vs independent high-precision reference
    theta = math.pi / 22  # root-of-unity style angle, very safe for low spins
    test_q_kernel_vs_reference(Jmax=2.0, theta=theta)

    # 3) Symmetry checks
    test_symmetries(Jmax=2.0, theta=theta, samples=60)

    # 4) Orthogonality
    test_orthogonality(theta=theta)

    print("\n✅ ALL LOW-SPIN VALIDATIONS PASSED.")
    print("Next step: only now is it worth optimizing / JAXing / scaling Jmax.")


if __name__ == "__main__":
    main()
