"""A second engine for the T1 layer: the exact values recomputed in FLINT.

T1 means "re-derived symbolically from stated definitions, exactly" -- and,
until ``src/workhouse/cross_check.py`` existed, it also quietly meant "by
sympy". These four checks are the witness that it no longer does. ADR 0016
states what the agreement covers (the arithmetic) and what it does not (the
derivation: a wrong formula would be computed identically wrong by both).
"""

from __future__ import annotations

from .. import constants as K
from ._core import _suite

# ==========================================================================
dual_engine = _suite("dual-engine witness for the T1 layer (ADR 0010, R2, R14)")


@dual_engine.check(
    "the all-rank laws agree between sympy and flint, as rational functions",
    "MASTER_THEORY §4.3 / R2 / src/workhouse/cross_check.py",
)
def _():
    # T1 said "re-derived symbolically from stated definitions, exactly". It
    # also said, silently, "by sympy". Here the same ten laws are rebuilt in
    # python-flint -- typed out from the printed closed forms, reading no
    # sympy expression -- and compared as rational functions over Q: two
    # polynomials pairs are equal exactly when their normal forms are, and
    # flint's exact gcd supplies the normal form.
    #
    # What this witnesses is the ARITHMETIC. A bug in Rational, cancel,
    # together or simplify would be caught. A wrong formula in constants.py
    # would not: both engines would compute the same wrong thing and agree.
    # That is the difference between a witness and a proof, and it is why this
    # suite is named for a witness.
    from .. import cross_check as X

    laws = X.rational_laws()
    bad = [w.name for w in laws if not w.holds()]
    return not bad, (
        f"{len(laws) - len(bad)}/{len(laws)} all-rank laws rebuilt independently in "
        f"flint and equal to sympy's as rational functions over Q: "
        + ", ".join(w.name.split(",")[0] for w in laws)
        + f". {bad or 'no disagreement'}"
    )


@dual_engine.check(
    "the monotonicity cubic is an exact factor of d/dN (N**3 t_N) in flint too",
    "MASTER_THEORY §4.3 / src/workhouse/cross_check.py",
)
def _():
    # The one witness that reaches sympy's `diff` as well as its cancel.
    # flint differentiates its own construction by the quotient rule, divides
    # the numerator by the corpus's printed cubic, and the division has to come
    # out exact with a positive multiple of N**3 left over -- which is the
    # statement that the cubic alone controls the sign, and hence that
    # N**3 t_N increases monotonically to 1/4.
    from .. import cross_check as X

    rows = X.derivative_law()
    bad = [w.name for w in rows if not w.holds()]
    return not bad, (
        "flint's quotient rule on its own construction of N**3 t_N leaves a numerator "
        "divisible by 2x**3 + 62x**2 - 151x + 72 at x = N**2 with remainder zero and a "
        f"positive multiple of N**3 as quotient, and that cubic is the registry's "
        f"MONOTONICITY_CUBIC. {bad or 'both rows hold'}"
    )


@dual_engine.check(
    "every registry value with a stated formula recomputes bit for bit in fmpq",
    "C2 / C13 / R14 / src/workhouse/cross_check.py",
)
def _():
    # Transcribed constants that the corpus ALSO gives a formula for: the
    # formula is recomputed in flint's fmpq and compared to the stored
    # sympy.Rational numerator and denominator exactly. A constant the corpus
    # states only as a literal has nothing to witness and is deliberately
    # absent -- there is no second derivation to disagree with.
    #
    # C_shp (historical) is among them, and this promotes nothing: it re-derives
    # the historical side from its own stated formula and says nothing whatever
    # about the v10a.26 side. C2 stays open.
    from .. import cross_check as X

    rows = X.registered_rationals()
    bad = [w.name for w in rows if not w.holds()]
    return not bad, (
        f"{len(rows) - len(bad)}/{len(rows)} registry values recomputed in flint's fmpq "
        f"and equal bit for bit, including C_shp (historical) from "
        f"(beta_pen - 2 alpha_3)/16 and d_3 from 7/32 + 12 leak_3 - 4 b_3. "
        f"{bad or 'no disagreement'}. Neither side of C2 is preferred here"
    )


@dual_engine.check(
    "the witness can fail: a planted error is caught, a planted identity is not",
    "src/workhouse/cross_check.py",
)
def _():
    # The check that makes the other three mean something. A comparison that
    # cannot fail proves nothing about the thing compared, so the engine is
    # shown rejecting a deliberately wrong construction -- t_N with one
    # coefficient moved -- and accepting a deliberately obscured correct one.
    # Without this row, "27/27 agree" would be indistinguishable from a
    # comparison that returns True unconditionally.
    from .. import cross_check as X

    n = X.Rat.of(X.GEN)
    correct = 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))
    wrong = 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 8))
    obscured = (2 * n**3 - 8 * n) / ((n**2 - 1) * (8 * n**4 - 22 * n**2 + 9))
    sympy_side = X.from_sympy(K.hopping(), K.N)
    caught = sympy_side != wrong
    kept = sympy_side == correct == obscured
    # ... and a rational-function comparison must not be fooled by agreeing at
    # a handful of points, which is the failure mode point-sampling has.
    agree_at = [p for p in range(5, 12) if correct.at(p) == wrong.at(p)]
    return caught and kept and not agree_at, (
        f"a one-coefficient error in t_N's denominator (4N**2-9 -> 4N**2-8) is rejected: "
        f"{caught}; the same law written over an expanded denominator is accepted: "
        f"{kept}; and the wrong law agrees with the right one at {len(agree_at)} of the "
        "7 integer points 5..11, so the comparison is structural and not a sample"
    )
