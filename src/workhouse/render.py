"""Output policy: whether to paint, and the one boundary that strips when not.

The colour decision lives here rather than in each renderer because every
``workhouse`` renderer builds a string and hands it to ``cli`` to print. Putting
the ANSI codes in the strings and stripping them at that single boundary keeps
one policy in one place; threading a ``color`` flag through ``navigator``,
``search``, ``frontier`` and the rest would put the same decision in a dozen
functions and let them disagree.

The default is the reported failure. An agent memo (notes/imported/
UPLOADS_2026-08-28i) found ``workhouse why C2`` emitting 41 escape sequences
into a pipe, where nothing can see them and every consumer has to strip them
itself. A terminal still gets colour; a pipe now gets text.

``NO_COLOR`` and ``FORCE_COLOR`` are honoured because they are the conventions
agents and CI already set (no-color.org: *any* value of ``NO_COLOR``, including
the empty string, disables colour).
"""

from __future__ import annotations

import json
import os
import re
import sys
from typing import Any, TextIO

#: SGR sequences only -- the colour and weight codes this repository emits.
#: Deliberately not a general ANSI eraser: it must never touch a claim's text.
ANSI = re.compile(r"\x1b\[[0-9;]*m")

#: Bumped only for a breaking change to a payload's shape. Consumers that pin
#: a major version keep working across additive fields.
SCHEMA = "workhouse/1"


def strip_ansi(text: str) -> str:
    return ANSI.sub("", text)


def should_color(stream: TextIO | None = None, override: bool | None = None) -> bool:
    """``--color``/``--no-color`` win, then the environment, then the terminal."""
    if override is not None:
        return override
    if "NO_COLOR" in os.environ:
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    stream = stream if stream is not None else sys.stdout
    try:
        return bool(stream.isatty())
    except (AttributeError, ValueError):
        # A closed or exotic stream is not a terminal.
        return False


class Out:
    """A ``print`` that knows the colour policy.

    Callable so the call sites read as ``out(...)`` rather than
    ``printer.write(...)``; the renderers are dense enough already.
    """

    def __init__(self, color: bool, stream: TextIO | None = None) -> None:
        self.color = color
        self.stream = stream if stream is not None else sys.stdout

    def __call__(self, text: str = "") -> None:
        print(text if self.color else strip_ansi(text), file=self.stream)


def dump(payload: dict[str, Any], stream: TextIO | None = None) -> None:
    """Emit one JSON document.

    ``sort_keys`` so a diff between two runs shows what changed rather than
    what moved, and ``ensure_ascii=False`` so the corpus's ``Γ`` and ``λ`` reach
    the consumer as themselves rather than as escapes.
    """
    stream = stream if stream is not None else sys.stdout
    json.dump(payload, stream, indent=2, sort_keys=True, ensure_ascii=False, default=str)
    stream.write("\n")
