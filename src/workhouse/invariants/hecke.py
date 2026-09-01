"""The Hecke cover correspondence note (2026-08-31) — one transcription guard.

`corpus-import/programs/hecke_cover_correspondence/` holds a result note the
maintainer generated externally, describing a target-blind generator that
maps lines in P^2(F_p) with Q=0 to sublattices of Z^3 and reads off Hecke
eigenvalues lambda_p of a claimed level-2 eta/Eisenstein newform, then a
post-hoc verifier that is reported to agree at all ten computed primes.

None of the five Python/JSON artifacts the note names reached this
repository -- only the prose did. So this module checks the one thing it
CAN check without them: that the printed target-blind table is internally
consistent, i.e. that the note did not make a transcription slip copying
A_p = p^4 * lambda_p from its own generator's output. This is deliberately
not a re-derivation of lambda_p, of the lattice construction, or of the
boxed infrared transformation -- those remain T3 (record-backed) until the
missing engine and verifier land here with their own SHA-256 digests. See
the note's own "What this repository has actually checked" section.
"""

from __future__ import annotations

from sympy import Rational

from ._core import _suite

# ==========================================================================
hecke = _suite("Hecke cover correspondence table")

#: (p, lambda_p, A_p) exactly as printed in the note's target-blind table.
_TABLE = (
    (3, Rational(-52, 27), -156),
    (5, Rational(174, 125), 870),
    (7, Rational(-136, 343), -952),
    (11, Rational(-56148, 14641), -56148),
    (13, Rational(178094, 28561), 178094),
    (17, Rational(-247662, 83521), -247662),
    (19, Rational(315380, 130321), 315380),
    (23, Rational(204504, 279841), 204504),
    (29, Rational(-3840450, 707281), -3840450),
    (31, Rational(-1309408, 923521), -1309408),
)


@hecke.check(
    "the geometric A_p column is p^4 times the printed lambda_p",
    "U6; corpus-import/programs/hecke_cover_correspondence/"
    "NOTE_FLUX_hecke_cover_correspondence_2026-08-31.md, target-blind prime table",
)
def _():
    # The note defines A_p := p^4 * lambda_p and then prints both columns.
    # That is a one-line arithmetic identity, exactly checkable in
    # sympy.Rational without the missing generator: it catches a copy-paste
    # slip in the table, nothing more. It does NOT confirm lambda_p is a
    # genuine Hecke eigenvalue, that the lattice L_ell is constructed as
    # described, or that the post-hoc verifier's agreement is real -- all of
    # that is record-backed only (the generator and verifier are absent from
    # this repository) and stays T3.
    mismatches = {p: (p**4 * lam, a_p) for p, lam, a_p in _TABLE if p**4 * lam != a_p}
    return not mismatches, (
        f"{len(_TABLE)} primes checked (3..31), A_p = p^4 lambda_p exactly for every one; "
        f"{len(mismatches)} mismatched" + (f": {mismatches}" if mismatches else "") + ". "
        "This confirms the table was transcribed without an arithmetic slip; it is not a "
        "re-derivation of lambda_p, the lattice construction, or the boxed infrared "
        "transformation, all of which remain T3 pending the missing generator and verifier"
    )
