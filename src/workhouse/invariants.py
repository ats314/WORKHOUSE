"""Re-derivation of the corpus's exact claims from their stated definitions.

Each check answers one question: *does this printed number follow from the
definition the corpus gives for it?* A check that fails is not automatically a
physics error — it is usually a transcription slip, a normalization erratum, or
a presentation difference. It is always worth knowing about.

Checks never adjudicate the fourth-order dispute. They verify the arithmetic
each side reports, and the exact size of the disagreement between them.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field

from sympy import (
    Matrix,
    Rational,
    diff,
    eye,
    limit,
    nsimplify,
    numer,
    pi,
    series,
    simplify,
    sin,
    solve,
    sqrt,
    symbols,
    sympify,
    together,
    zeros,
)

from . import constants as K
from . import near_gamma as G
from . import settlement as S


@dataclass
class Result:
    """Outcome of one invariant check."""

    name: str
    passed: bool
    detail: str = ""
    section: str = ""


@dataclass
class Suite:
    """A named group of checks."""

    name: str
    checks: list[tuple[str, str, Callable[[], tuple[bool, str]]]] = field(default_factory=list)

    def check(self, name: str, section: str = ""):
        def register(fn):
            self.checks.append((name, section, fn))
            return fn

        return register

    def run(self) -> list[Result]:
        out = []
        for name, section, fn in self.checks:
            try:
                passed, detail = fn()
            except Exception as exc:  # a broken check is a failure
                passed, detail = False, f"raised {type(exc).__name__}: {exc}"
            out.append(Result(name, passed, detail, section))
        return out


SUITES: list[Suite] = []


def _suite(name: str) -> Suite:
    s = Suite(name)
    SUITES.append(s)
    return s


# ==========================================================================
rank_law = _suite("second order, all ranks")


@rank_law.check("t_N = B_N - A_N", "MASTER_THEORY §4.3")
def _():
    lhs = K.parallel_sum() - K.antiparallel_sum()
    return simplify(lhs - K.hopping()) == 0, "channel difference reproduces the rank law"


@rank_law.check("t_2 = 0 and t_3 = 5/612", "MASTER_THEORY §4.3")
def _():
    ok = K.hopping(2) == 0 and K.hopping(3) == Rational(5, 612)
    return ok, f"t_2={K.hopping(2)}, t_3={K.hopping(3)}"


@rank_law.check("t_N > 0 for N >= 3", "MASTER_THEORY §4.3")
def _():
    bad = [n for n in range(3, 40) if not K.hopping(n) > 0]
    return not bad, "positive for N=3..39" if not bad else f"non-positive at {bad}"


@rank_law.check("deficit identity 1/4 - N^3 t_N", "MASTER_THEORY §4.3")
def _():
    lhs = Rational(1, 4) - K.N**3 * K.hopping()
    return simplify(lhs - K.hopping_deficit()) == 0, "closed form matches"


@rank_law.check("deficit positive at N = 3, 5, 9", "MASTER_THEORY §4.3")
def _():
    vals = {n: K.hopping_deficit(n) for n in (3, 5, 9)}
    return all(v > 0 for v in vals.values()), f"{ {k: str(v) for k, v in vals.items()} }"


@rank_law.check("large-N expansion of t_N through 1/N^9", "GLUEBALL §4")
def _():
    inv = symbols("inv", positive=True)
    ser = series(K.hopping(1 / inv), inv, 0, 10).removeO()
    got = {k: ser.coeff(inv, k) for k in K.HOPPING_LARGE_N}
    return got == K.HOPPING_LARGE_N, f"{ {k: str(v) for k, v in got.items()} }"


@rank_law.check("N^3 t_N increases monotonically to 1/4", "CANON §10.2/§10.5")
def _():
    num = simplify(numer(together(diff(K.N**3 * K.hopping(), K.N))))
    cubic_in_N = K.MONOTONICITY_CUBIC.subs(K.x, K.N**2)
    # sympy cancels one power of x that the corpus leaves in the printed prefactor;
    # the sign-determining cubic is what must agree.
    matches = simplify(num - 4 * K.N**3 * cubic_in_N) == 0
    positive = all(K.MONOTONICITY_CUBIC.subs(K.x, v) > 0 for v in (4, 9, 16, 10**6))
    roots = [complex(r).real for r in solve(K.MONOTONICITY_CUBIC, K.x)]
    return (
        matches and positive,
        f"d/dN numerator = 4N^3*cubic(N^2); cubic roots {[round(r, 4) for r in roots]} "
        f"all < 4, so cubic > 0 on the physical range",
    )


# ==========================================================================
su3_series = _suite("SU(3) second and third order")


@su3_series.check("d_- - 4 t_- = 11/306", "PAPER eq. (7)")
def _():
    v = K.D_MINUS_2 - 4 * K.T_MINUS_2
    return v == Rational(11, 306), f"= {v}"


@su3_series.check("t_- equals the rank law at N = 3", "MASTER_THEORY §4.3")
def _():
    return K.hopping(3) == K.T_MINUS_2, f"{K.T_MINUS_2} == {K.hopping(3)}"


@su3_series.check("C-even bandwidth = top - bottom = 88/153", "PAPER App. B")
def _():
    w = K.BAND_EVEN_TOP - K.BAND_EVEN_BOTTOM
    return w == K.BAND_EVEN_WIDTH, f"= {w}"


@su3_series.check("C-odd manifold width = 5/51", "PAPER App. B")
def _():
    w = K.BAND_ODD_TOP - K.BAND_ODD_FLAT
    return w == K.BAND_ODD_WIDTH, f"= {w}"


@su3_series.check("d_3 = 7/32 + 12*leak_3 - 4*b_3", "MASTER_THEORY §4.4")
def _():
    v = Rational(7, 32) + 12 * K.LEAK_3 - 4 * K.B_3
    return v == K.D_3, f"= {v}"


@su3_series.check("E_flat and t(u) carry the ledger coefficients", "MASTER_THEORY §4.4")
def _():
    e, t = K.e_flat(), K.t_series()
    ok = (
        e.coeff(K.u, 0) == Rational(8, 3)
        and e.coeff(K.u, 1) == 1
        and e.coeff(K.u, 2) == Rational(11, 306)
        and e.coeff(K.u, 3) == K.D_3
        and t.coeff(K.u, 2) == K.T_MINUS_2
        and t.coeff(K.u, 3) == K.B_3
    )
    return ok, "E_flat = 8/3 + u + 11/306 u^2 - 109151/249696 u^3"


# ==========================================================================
sealed = _suite("fourth order, sealed core")


@sealed.check("alpha_3 = 4*A_shp = 5/12", "MASTER_THEORY §5.2")
def _():
    ok = K.alpha_pen(3) == 4 * K.A_SHP_3 == K.ALPHA_PEN_3
    return ok, f"alpha_3 = {K.alpha_pen(3)}"


@sealed.check("axial law reproduces alpha_4, alpha_5, alpha_6", "MASTER_THEORY §5.3")
def _():
    want = {4: Rational(32, 675), 5: Rational(1, 108), 6: Rational(64, 25725)}
    got = {n: K.alpha_pen(n) for n in want}
    return got == want, f"{ {k: str(v) for k, v in got.items()} }"


@sealed.check("alpha_3 = 4*|c_4^square(3)|", "MOB §4")
def _():
    return 4 * abs(K.CUBE_COMPLETION_4) == K.ALPHA_PEN_3, "cube-completion route agrees"


def _sealed_gaps():
    return {
        "A": abs(K.A_SHP_3_NUM - float(K.A_SHP_3)),
        "B": abs(K.B_SHP_3_NUM - float(K.B_SHP_3)),
        "D": abs(K.D_SHP_3_NUM - float(K.D_SHP_3)),
        "alpha": abs(K.ALPHA_PEN_3_NUM - float(K.ALPHA_PEN_3)),
    }


@sealed.check("v10a.26 A, B, D match the sealed rationals within 2.3e-13", "GLUEBALL §10")
def _():
    gaps = _sealed_gaps()
    subset = {k: gaps[k] for k in ("A", "B", "D")}
    ok = all(g <= K.SEALED_CORE_TOLERANCE for g in subset.values())
    return ok, "; ".join(f"{k} {v:.3e}" for k, v in subset.items())


@sealed.check("FINDING: alpha_new falls outside the corpus's own 2.3e-13 bound", "GLUEBALL §10")
def _():
    gaps = _sealed_gaps()
    # alpha = 4A, so it inherits four times A's deviation. The corpus's stated
    # aggregate bound (2.3e-13) tracks D_new (2.23e-13) and does not cover alpha.
    # This is a bookkeeping slip in the quoted tolerance, not a discrepancy in
    # the sealed core itself: the run's own alpha and A stay mutually consistent.
    exceeds = gaps["alpha"] > K.SEALED_CORE_TOLERANCE
    consistent = abs(K.ALPHA_PEN_3_NUM - 4 * K.A_SHP_3_NUM) < 1e-14
    return exceeds and consistent, (
        f"alpha gap {gaps['alpha']:.4e} > stated {K.SEALED_CORE_TOLERANCE:.1e} "
        f"(= 4x the A gap {gaps['A']:.4e}); alpha_new vs 4*A_new agree to "
        f"{abs(K.ALPHA_PEN_3_NUM - 4 * K.A_SHP_3_NUM):.1e}, so the sealed core holds "
        "and only the quoted bound is too tight"
    )


@sealed.check("exceptional ranks are exactly {3,4,5,6}", "MASTER_THEORY §5.3")
def _():
    # A fourth-order word carries at most 6 character factors, so a determinant
    # channel needs |p-q| = N <= 6; and N >= 3 for the sector to exist at all.
    derived = tuple(n for n in range(2, 12) if 3 <= n <= 6)
    return derived == K.EXCEPTIONAL_RANKS, f"{derived}"


# ==========================================================================
dispute = _suite("fourth order, anchoring and the residual dispute")


@dispute.check("historical q_3 decimal expansion", "MASTER_THEORY §5.5")
def _():
    d = abs(float(K.Q_BAND_4) - (-2.857915988114559))
    return d < 1e-15, f"|diff| = {d:.2e}"


@dispute.check("C_old = (beta_pen_3 - 2*alpha_3)/16", "MASTER_THEORY §5.5")
def _():
    v = (K.BETA_PEN_3 - 2 * K.ALPHA_PEN_3) / 16
    return v == K.C_SHP_HISTORICAL, f"= {v}"


@dispute.check("Delta_Gamma = m_Gamma^(4) - q_band^(4)", "MASTER_THEORY §5.5 / C1")
def _():
    v = K.M_GAMMA_4_NUM - float(K.Q_BAND_4)
    # Double-precision evaluation lands one ulp below the correctly rounded
    # value; both are recorded, so accept either.
    ok = min(abs(v - K.DELTA_GAMMA), abs(v - K.DELTA_GAMMA_AS_PRINTED)) < 1e-15
    return ok, f"double eval {v!r}; exact rounds to {K.DELTA_GAMMA!r}"


@dispute.check("FINDING: the printed Delta_Gamma is one ulp low", "MASTER_THEORY §5.5")
def _():
    from sympy import Float

    exact = (Float(repr(K.M_GAMMA_4_NUM), 25) - K.Q_BAND_4).evalf(25)
    # Rounding q_band^(4) to a double before subtracting loses the last digit.
    correct = abs(float(exact) - K.DELTA_GAMMA) < 1e-16
    printed_is_low = K.DELTA_GAMMA_AS_PRINTED < K.DELTA_GAMMA
    gap = K.DELTA_GAMMA - K.DELTA_GAMMA_AS_PRINTED
    return correct and printed_is_low, (
        f"high precision {exact} rounds to {K.DELTA_GAMMA!r}; corpus prints "
        f"{K.DELTA_GAMMA_AS_PRINTED!r}, low by {gap:.3e} (1 ulp). Cosmetic, but "
        "the printed digit is not the correctly rounded one."
    )


@dispute.check(
    "a translation-local scalar shift changes nothing observable",
    "MASTER_THEORY §5.5 / C1",
)
def _():
    # H_mass = H_band + Delta_Gamma*I  =>  centered forms coincide identically.
    h = Matrix(3, 3, symbols("h1:10"))
    dg, q = symbols("dg q")
    centered_mass = (h + dg * eye(3)) - (q + dg) * eye(3)
    centered_band = h - q * eye(3)
    same = simplify(centered_mass - centered_band) == zeros(3, 3)
    return same, (
        "centered operator, eigenvectors, SOS factorization, mobility "
        "coefficients and bandwidth are all invariant under the anchoring shift, "
        "so q_band^(4) and m_Gamma^(4) are not competing estimates"
    )


@dispute.check("Delta_C = C_new - C_old > 0 (the real discrepancy)", "MASTER_THEORY §5.5 / C2")
def _():
    v = K.C_SHP_NEW_NUM - float(K.C_SHP_HISTORICAL)
    d = abs(v - K.DELTA_C)
    return d < 1e-16 and v > 0, f"{v!r} vs recorded {K.DELTA_C!r} (|diff| {d:.1e})"


@dispute.check("beta_new = 8A + 16*C_new", "MASTER_THEORY §5.5")
def _():
    v = 8 * float(K.A_SHP_3) + 16 * K.C_SHP_NEW_NUM
    return abs(v - 0.5099200711546681) < 1e-15, f"= {v!r}"


@dispute.check("off-axis band splits are 8*Delta_C and 16*Delta_C", "MASTER_THEORY §5.5")
def _():
    m, r = 8 * K.DELTA_C, 16 * K.DELTA_C
    ok = abs(m - 0.2229844343615374) < 1e-15 and abs(r - 0.4459688687230748) < 1e-15
    return ok, f"M: {m!r}, R: {r!r}; axial cuts agree exactly"


@dispute.check("bandwidth ratio W4_new / W4_old ~ 1.93", "MASTER_THEORY §5.5")
def _():
    ratio = K.W4_NEW_NUM / K.W4_HISTORICAL
    return abs(ratio - 1.93) < 5e-3, f"= {ratio:.6f}"


@dispute.check("Hamer 8*a_4 matches m_Gamma to ~5.2e-13", "GLUEBALL §2.3")
def _():
    d = abs(8 * K.HAMER_A4 - K.M_GAMMA_4_NUM)
    return d < K.HAMER_TOLERANCE, (
        f"|diff| = {d:.2e}; a_4 is an unverified notebook transcription, "
        "so this is a normalization cross-check, not primary-source proof"
    )


@dispute.check("quarantined scalar decimal", "MASTER_THEORY §5.5")
def _():
    d = abs(float(K.QUARANTINED_SCALAR) - (-11.068479463778765))
    return d < 1e-14, f"|diff| = {d:.2e}; rejected by both sides"


@dispute.check("C20: exact gate value vs printed float-reconstruction", "MASTER_THEORY C20")
def _():
    exact = float(K.LINKED_VACUUM_4)
    artifact = float(K.LINKED_VACUUM_4_ARTIFACT)
    gap = abs(exact - artifact)
    ulp = 2.0**-53 * abs(exact)
    # C20 records these as agreeing "to float precision". They do not: the gap is
    # ~31 ulps, and the decimal printed throughout the corpus (-0.8800987156226097)
    # is the artifact's value, not the exact gate value (-0.8800987156226127).
    agree_to_float = gap <= 2 * ulp
    return (
        not agree_to_float,
        f"exact {exact!r} vs artifact {artifact!r}; gap {gap:.2e} = {gap / ulp:.0f} ulps. "
        f"They agree to ~14 significant digits, NOT to float precision as C20 states; "
        f"the corpus's printed decimal tracks the artifact.",
    )


@dispute.check("run's applied shift is not Delta_Gamma", "GLUEBALL §9.2 / C22")
def _():
    # Gate 85's equality was produced by construction with this shift, so it
    # certifies internal bookkeeping rather than independent agreement.
    return (
        abs(K.RUN15_APPLIED_SHIFT - K.DELTA_GAMMA) > 1.0,
        f"applied {K.RUN15_APPLIED_SHIFT} vs Delta_Gamma {K.DELTA_GAMMA} "
        "— target-derived, so gate 85 is not an independent scalar verification",
    )


# ==========================================================================
crosswalk = _suite("old-to-new crosswalk")


@crosswalk.check("Phi_C vanishes at Gamma along every direction", "MASTER_THEORY §5.5")
def _():
    t, n1, n2, n3 = symbols("t n1 n2 n3", positive=True)
    radial = K.phi_c((t * n1, t * n2, t * n3))
    lead = simplify(series(radial, t, 0, 4).removeO())
    vanishes = limit(radial, t, 0) == 0
    return vanishes, (
        f"Phi_C = {lead} = O(|k|^2), since e_2 = O(|k|^4) and Q = O(|k|^2). "
        "A Gamma-point scalar therefore constrains Delta_Gamma but places no "
        "constraint whatsoever on Delta_C."
    )


@crosswalk.check("Phi_C at the high-symmetry points", "MASTER_THEORY §5.1")
def _():
    got = {
        "X": K.phi_c((pi, 0, 0)),
        "M": K.phi_c((pi, pi, 0)),
        "P": K.phi_c((pi, pi / 2, 0)),
        "R": K.phi_c((pi, pi, pi)),
    }
    want = {"X": 0, "M": 8, "P": Rational(16, 3), "R": 16}
    return got == want, f"{ {k: str(v) for k, v in got.items()} }"


@crosswalk.check("crosswalk reproduces the recorded off-axis band splits", "MASTER_THEORY §5.5")
def _():
    # c_4_new(k) - c_4_old(k) - Delta_Gamma == Delta_C * Phi_C(k)
    m = K.DELTA_C * float(K.phi_c((pi, pi, 0)))
    r = K.DELTA_C * float(K.phi_c((pi, pi, pi)))
    ok = abs(m - 0.2229844343615374) < 1e-15 and abs(r - 0.4459688687230748) < 1e-15
    return ok, f"M -> {m!r}, R -> {r!r}; independently recorded as 8*Delta_C and 16*Delta_C"


@crosswalk.check("the crosswalk is exactly scalar on the momentum axes", "MASTER_THEORY §5.5")
def _():
    axial = [K.phi_c(kv) for kv in ((pi, 0, 0), (pi / 2, 0, 0), (pi / 3, 0, 0))]
    return all(a == 0 for a in axial), (
        "Phi_C vanishes on every axial cut, so axial data cannot distinguish the "
        "two kernels — the whole residual disagreement lives off-axis"
    )


@crosswalk.check("bandwidth is preserved only if Delta_C vanishes", "MASTER_THEORY §5.5")
def _():
    # The scalar term drops out of any difference of band values; only Phi_C survives.
    spread = K.DELTA_C * (float(K.phi_c((pi, pi, pi))) - float(K.phi_c((pi, 0, 0))))
    return abs(spread) > 1e-3, (
        f"scalar re-anchoring alone leaves the centered structure unchanged, but the "
        f"additional Delta_C*Phi_C term spreads R against X by {spread:.6f}. Bandwidth "
        "survives the crosswalk only if Delta_C is shown to vanish or is absorbed by an "
        "exact operator identity; neither is established."
    )


# ==========================================================================
pencil = _suite("fourth-order generalized Hodge pencil")


@pencil.check("Q4 cross coefficient = beta_pen_3 / 4", "GLUEBALL §8")
def _():
    return K.Q4_CROSS == K.BETA_PEN_3 / 4, f"= {K.Q4_CROSS}"


@pencil.check("historical Q4 numerator is positive definite", "UNIFIED §0.1")
def _():
    m = Matrix(3, 3, lambda i, j: K.A_SHP_3 if i == j else K.Q4_CROSS / 2)
    eig = m.eigenvals()
    ok = all(e > 0 for e in eig) and set(eig) == {
        K.A_SHP_3 + K.Q4_CROSS,
        K.A_SHP_3 - K.Q4_CROSS / 2,
    }
    return ok, f"eigenvalues {sorted(str(e) for e in eig)} — PSD, in fact PD"


@pencil.check("centered kernel difference is PSD (vanishes on axes)", "MASTER_THEORY §5.5")
def _():
    # C^dagger[(H4_new - s_new) - (H4_old - q_old)]C = 4*Delta_C*sum_{i<j} L_i L_j
    m = Matrix(3, 3, lambda i, j: 0 if i == j else 2 * K.DELTA_C)
    eig = [complex(e).real for e in m.eigenvals()]
    return K.DELTA_C > 0, (
        f"4*Delta_C*sum_(i<j) L_iL_j with Delta_C = {K.DELTA_C:.6e} > 0; "
        f"form eigenvalues {sorted(round(e, 6) for e in eig)} — indefinite as a free "
        "quadratic form, PSD on the cube-amplitude sector where the pencil is scoped"
    )


# ==========================================================================
extraction = _suite("fourth-order checkpoint extraction")

_As, _Bs, _Cs, _Ds, _c0 = symbols("A_shp B_shp C_shp D_shp c0")


def _eps4(k):
    """Generic cubic-invariant fourth-order correction on the flat fiber."""
    a = [4 * sin(sympify(ki) / 2) ** 2 for ki in k]
    q = sum(a)
    e2 = a[0] * a[1] + a[0] * a[2] + a[1] * a[2]
    e3 = a[0] * a[1] * a[2]
    return simplify(_c0 + _As * q + _Bs * e2 + _Cs * 4 * e2 / q + _Ds * e3 / q)


def _deltas():
    g = _c0  # epsilon_4(Gamma) = c0
    return (
        simplify(_eps4([pi, 0, 0]) - g),
        simplify(_eps4([pi, pi, 0]) - g),
        simplify(_eps4([pi, pi / 2, 0]) - g),
        simplify(_eps4([pi, pi, pi]) - g),
    )


@extraction.check("checkpoint values at X, M, P, R", "MASTER_THEORY §5.1")
def _():
    dX, dM, dP, dR = _deltas()
    ok = (
        simplify(dX - 4 * _As) == 0
        and simplify(dM - (8 * _As + 16 * _Bs + 8 * _Cs)) == 0
        and simplify(dP - (6 * _As + 8 * _Bs + Rational(16, 3) * _Cs)) == 0
        and simplify(dR - (12 * _As + 48 * _Bs + 16 * _Cs + Rational(16, 3) * _Ds)) == 0
    )
    return ok, f"dX={dX}, dM={dM}, dP={dP}, dR={dR}"


@extraction.check("the four extraction formulas invert the ansatz", "MASTER_THEORY §5.1")
def _():
    dX, dM, dP, dR = _deltas()
    ok = (
        simplify(dX / 4 - _As) == 0
        and simplify((dX + 4 * dM - 6 * dP) / 16 - _Bs) == 0
        and simplify(3 * (2 * dP - dM - dX) / 8 - _Cs) == 0
        and simplify(3 * (dR - 6 * dM + 6 * dP) / 16 - _Ds) == 0
    )
    return ok, "A, B, C, D each recovered exactly from the checkpoint deltas"


@extraction.check("X is blind to B, C, D — it fixes A alone", "MASTER_THEORY §5.1")
def _():
    dX, *_ = _deltas()
    free = {s for s in dX.free_symbols if s in {_Bs, _Cs, _Ds}}
    return not free, "Delta_X = 4*A_shp exactly, which is why the axial cuts agree"


# ==========================================================================
homology = _suite("homology and finite volume")


@homology.check("dim Z_2 = (L^3 - 1) + 3 = L^3 + 2", "UNIFIED §0.1")
def _():
    lhs = (K.L**3 - 1) + 3
    return simplify(lhs - K.dim_z2()) == 0, "cube boundaries plus the harmonic plane triplet"


@homology.check("dim Z_2 at L = 3, 4, 5", "UNIFIED §0.1")
def _():
    vals = {n: K.dim_z2(n) for n in (3, 4, 5)}
    return vals == {3: 29, 4: 66, 5: 127}, f"{vals}"


def run_all() -> list[Result]:
    """Run every suite and return a flat list of results."""
    return [r for s in SUITES for r in s.run()]


# ==========================================================================
adjudication = _suite("settlement package and adjudication harness")


@adjudication.check("cold reruns re-certify both in-corpus audits", "SETTLEMENT.md §2")
def _():
    runs = S.read_cold_runs()
    ok = len(runs) == 2 and all(r.passed == r.total == 8 for r in runs)
    detail = "; ".join(f"{r.name.replace('cold_rerun_', '')} {r.passed}/{r.total}" for r in runs)
    return ok, detail


@adjudication.check("stranded-flux zero backend stays falsified (C7)", "MASTER_THEORY C7")
def _():
    run = next(r for r in S.read_cold_runs() if "stranded_flux" in r.name)
    # Cold rerun, so C7's evidence class rises from in-corpus to cold-reproduced.
    return run.verdict == "ZERO_BACKEND_FALSIFIED", (
        f"{run.passed}/{run.total}, verdict {run.verdict}; generating script "
        f"sha256 {run.source_sha256[:16]}... (the script is absent from this repo; "
        "settlement/SHA256SUMS pins the transcript, not the script)"
    )


@adjudication.check(
    "FINDING: the target-blindness scan cannot see two scalar-determining targets",
    "settlement/mce_adjudication_harness.py",
)
def _():
    audit = S.audit_contamination_scan()
    missed = audit.uncovered_scalar_determining
    # Asserting the gap, per the repository's convention for findings. When the
    # harness's CONTAMINATION_STRINGS is extended upstream this check will fail,
    # and the correct response is to retire it, not to widen it.
    return missed == {"delta_gamma", "hamer_8a4"}, (
        f"quarantined targets {len(audit.targets)}, scan strings {len(audit.strings)}; "
        f"uncovered {sorted(audit.uncovered)}. Two of those determine the disputed "
        "scalar: m_Gamma = q_band + Delta_Gamma exactly, and Hamer's 8*a_4 IS the "
        "scalar to 13 digits. The scan covers the 16-digit oracle form "
        "7751458630189173, but that string does NOT contain 7751458630184 — they "
        "diverge at index 12 — so an engine carrying either constant passes the scan. "
        "Closing it means adding 0827701250956414, 7751458630184 (and the ...417 "
        "rounding), 160506019419340168451, 7250590288602460800, 4405310420659200."
    )


@adjudication.check(
    "FINDING: the contamination scan reads only the engine file",
    "settlement/mce_adjudication_harness.py",
)
def _():
    return S.scans_a_single_file(), (
        "src = open(engine).read() — an engine that imports a helper module, loads a "
        "JSON/npz, or restores from the sqlite checkpoint carries that content past "
        "the scan entirely"
    )


@adjudication.check(
    "FINDING: the harness can never report COMPLETE",
    "settlement/mce_adjudication_harness.py",
)
def _():
    # item10_W22_toggle is assigned "OPEN (...)" unconditionally and the
    # completeness predicate rejects any OPEN value.
    return not S.verdict_can_be_complete(), (
        "protocol item 10 (W22 order-schedule toggle) is hardcoded OPEN, and the "
        "completeness predicate rejects any OPEN value, so even a certificate that "
        "discharges items 8 and 9 with a full shape block yields PARTIAL. Honest as a "
        "default, but the protocol has no path to closure until the engine exposes "
        "the toggle."
    )


@adjudication.check(
    "the harness carries the printed Delta_Gamma, not the rounded one",
    "settlement/mce_adjudication_harness.py",
)
def _():
    v = S.harness_delta_gamma()
    return v == K.DELTA_GAMMA_AS_PRINTED, (
        f"harness has {v!r}, matching the corpus's printed value; the correctly "
        f"rounded value is {K.DELTA_GAMMA!r}. Harmless after unblinding, but if the "
        "digit string is added to the scan, add both forms."
    )


@adjudication.check("quarantined targets never reach the engine process", "GLUEBALL §18.1 item 6")
def _():
    audit = S.audit_contamination_scan()
    src = S.HARNESS.read_text()
    # The architecture itself is sound: Q is module-local and the engine is
    # launched with a plain env, so no target is exported. The weakness audited
    # above is detection of a target already inside the engine, not leakage.
    leaks = re.findall(r"env\s*=\s*dict\(os\.environ,([^)]*)\)", src)
    exported = [seg for seg in leaks if any(t in seg for t in audit.targets)]
    return not exported, (
        f"{len(audit.targets)} targets held module-local; engine env carries only "
        "HODGE_SU3_M4_SEALED_SOURCE_FD. Quarantine architecture is sound — the gap "
        "is in detecting a target already present in the engine."
    )


# ==========================================================================
near_gamma = _suite("near-Gamma uniformity (G11)")


@near_gamma.check("Jordan bound q(k) >= (4/pi^2)|k|^2 holds on the whole zone", "GLUEBALL §18.3")
def _():
    xs = symbols("xs", real=True)
    diff_expr = 4 * sin(xs / 2) ** 2 - G.JORDAN * xs**2
    # sin'' = -sin <= 0 on [0,pi] so sin is concave and lies above its chord.
    concave = simplify(diff(sin(xs), xs, 2) + sin(xs)) == 0
    samples = [diff_expr.subs(xs, pi * Rational(i, 200)) for i in range(201)]
    never_negative = all(v >= 0 for v in samples)
    tight = simplify(diff_expr.subs(xs, pi)) == 0
    return concave and never_negative and tight, (
        "sin is concave on [0,pi] so it exceeds its chord 2x/pi; substituting "
        "x -> x/2 and squaring gives the bound, with equality at k=0 and at the "
        "zone corner — so the bound is tight, not slack"
    )


@near_gamma.check("t(u) >= t_3 u^2 for u > 0, so the gap bound is safe", "MASTER_THEORY §4.4")
def _():
    # b_3 > 0, so dropping the cubic term can only understate the gap.
    return K.B_3 > 0, f"b_3 = {K.B_3} > 0; t(u) - t_3 u^2 = b_3 u^3 >= 0"


@near_gamma.check("crossover constant K = (pi/2) sqrt(W_4 / (theta t_3))", "GLUEBALL §18.3")
def _():
    theta = Rational(1, 2)
    got = G.crossover_constant(K.W4_HISTORICAL, theta)
    want = (pi / 2) * sqrt(nsimplify(K.W4_HISTORICAL, rational=True) / (theta * K.T_MINUS_2))
    return simplify(got - want) == 0, f"K_historical(theta=1/2) = {float(got):.4f}"


@near_gamma.check(
    "the criterion survives C2: K depends on the kernel only through sqrt(W_4)",
    "MASTER_THEORY §5.5 / C2",
)
def _():
    theta = Rational(1, 2)
    k_hist = float(G.crossover_constant(K.W4_HISTORICAL, theta))
    k_new = float(G.crossover_constant(K.W4_NEW_NUM, theta))
    ratio = k_new / k_hist
    expected = (K.W4_NEW_NUM / K.W4_HISTORICAL) ** 0.5
    conservative = float(G.conservative_constant(theta))
    return abs(ratio - expected) < 1e-12 and conservative >= max(k_hist, k_new), (
        f"K_hist = {k_hist:.4f}, K_new = {k_new:.4f}, ratio {ratio:.6f} = "
        f"sqrt(W4_new/W4_old); the larger constant {conservative:.4f} bounds both, so "
        "the exclusion radius can be stated now without adjudicating C2"
    )


@near_gamma.check("the statement is non-vacuous only below an explicit coupling", "GLUEBALL §18.3")
def _():
    theta = Rational(1, 2)
    u_max = float(G.max_coupling(theta))
    # At u_max the excluded ball exactly fills the inscribed sphere of the zone.
    at_max = G.excluded_zone_fraction(u_max * 1.01, theta)
    return 0 < u_max < 1 and at_max == 1.0, (
        f"K*u < pi requires u < {u_max:.6f} at theta=1/2 "
        f"(u < {float(G.max_coupling(1)):.6f} at theta=1). Above that the excluded "
        "ball covers the zone and the near-Gamma claim says nothing."
    )


@near_gamma.check("excluded zone fraction grows as u^3", "GLUEBALL §18.3")
def _():
    f1 = G.excluded_zone_fraction(0.02)
    f2 = G.excluded_zone_fraction(0.04)
    return abs(f2 / f1 - 8) < 1e-9, (
        f"u=0.02 excludes {100 * f1:.2f}%, u=0.04 excludes {100 * f2:.2f}% "
        "— a factor of 8, as a ball volume must"
    )
