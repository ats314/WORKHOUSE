"""Helpers read by more than one suite.

``_bridge_towers`` is used by the SU(3) series suite and by the coupling
erratum suite. It lives here rather than in either, because a suite module
importing another suite module would reorder ``SUITES``: registration
order is import order, and it is what ``workhouse verify`` and
``FRONTIER.md`` print. ``MASTER_EDITION`` and its reader are here for the
same reason: three suites quote exact values out of the pinned archive.
"""

from __future__ import annotations

import re
import zipfile

from sympy import Rational, expand, symbols

from .. import constants as K
from ._core import ROOT


def _bridge_towers():
    u, x = symbols("u x")
    minus = Rational(2, 3) + x / 6 + K.TOWER_B2_MINUS * x**2 + K.TOWER_B3_MINUS * x**3
    plus = Rational(2, 3) - x / 6 + K.TOWER_B2_PLUS * x**2 + K.TOWER_B3_PLUS * x**3
    return u, expand(4 * minus.subs(x, 3 * u / 2)), expand(4 * plus.subs(x, 3 * u / 2))


#: The 2026-08-28 unified master edition, pinned verbatim in the notes archive.
#: Two checks below quote exact values out of it; without the bytes in the tree
#: those checks would verify a transcription against itself, which a review bot
#: caught on PR #38 and was right about.
MASTER_EDITION = (
    ROOT
    / "notes"
    / "imported"
    / "UPLOADS_2026-08-28c"
    / "NESTED_QUOTIENT_GAUGE_SPECTRAL_THEORY_COMPLETE_UNIFIED_MASTER_CLOSED_20260828.docx"
)


def _master_edition_text() -> str:
    """The pinned edition's document text, digits preserved.

    A .docx is a zip of XML, so the text is extracted the same way every time
    and the check reads the same bytes the register pinned. Tags are stripped
    rather than parsed: these checks look for exact digit strings, and a
    numerator split across XML runs would otherwise be invisible.
    """

    with zipfile.ZipFile(MASTER_EDITION) as archive:
        xml = archive.read("word/document.xml").decode("utf-8", "replace")
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", xml))
