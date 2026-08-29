"""
Each check answers one question: *does this printed number follow from the
definition the corpus gives for it?* A check that fails is not automatically a
physics error — it is usually a transcription slip, a normalization erratum, or
a presentation difference. It is always worth knowing about.

Checks never adjudicate the fourth-order dispute. They verify the arithmetic
each side reports, and the exact size of the disagreement between them.

One module per subject, assembled here. This file fixes the order the
suites register in, which is the order ``workhouse verify`` and
``FRONTIER.md`` print them; importing a suite module has the side effect
of registering its suite, so the import list below is not decoration.
"""

from __future__ import annotations

import importlib

from ._core import SUITES, Result, Suite, source_path

#: Suite modules, in the order their suites must register.
#:
#: Walked by ``import_module`` rather than written as a block of import
#: statements because an import block is sorted alphabetically by the
#: formatter, which would silently reorder every suite in
#: ``workhouse verify`` and in ``FRONTIER.md``. The order here is the
#: order the single-file version defined them in.
_MODULES = (
    "rank_law",
    "su3",
    "charge_even",
    "fourth_order",
    "homology",
    "adjudication",
    "uniformity",
    "tier",
    "pentagonal",
    "string_tension",
    "published",
    "restored",
    "coupling",
    "tetrahedral",
    "notes_program",
    "channels",
    "manuscript",
    "bridge",
    "identification",
    "dual_engine",
    "two_cube",
)

for _name in _MODULES:
    importlib.import_module(f"{__name__}.{_name}")


def run_all() -> list[Result]:
    """Run every suite and return a flat list of results."""
    return [r for s in SUITES for r in s.run()]


__all__ = ["SUITES", "Result", "Suite", "_MODULES", "run_all", "source_path"]
