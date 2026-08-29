"""Suite plumbing: the registry every invariant module fills.

Split out of a single 6,300-line ``invariants.py`` on 2026-08-29. Nothing
here checks anything. It holds the ``Suite``/``Result`` pair, the
module-level ``SUITES`` list that ``__init__`` fills in a fixed order, and
the one path helper the split made necessary.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Result:
    """Outcome of one invariant check."""

    name: str
    passed: bool
    detail: str = ""
    section: str = ""
    #: T1 = re-derived exactly; T2 = float agreement within a stated tolerance.
    tier: int = 1
    #: Line of the check's body, so a reader can go argue with the source.
    line: int = 0
    #: ``src/workhouse/invariants/<module>.py:<line>``, derived from the
    #: code object. The split made a hard-coded filename wrong in six
    #: places at once, so it is no longer spelled anywhere.
    source: str = ""


@dataclass
class Suite:
    """A named group of checks."""

    name: str
    checks: list[tuple[str, str, int, Callable[[], tuple[bool, str]]]] = field(default_factory=list)

    def check(self, name: str, section: str = "", tier: int = 1):
        """Register a check.

        ``tier`` is the verification tier the check establishes, and it is
        declared rather than inferred because the difference is the whole point:
        T1 is exact re-derivation, T2 is float agreement within a tolerance. A
        check that compares against a ``*_NUM`` constant or a stated tolerance
        is T2 however exact its inputs look.
        """
        if tier not in (1, 2):
            raise ValueError(f"{name}: a check establishes T1 or T2, not T{tier}")

        def register(fn):
            self.checks.append((name, section, tier, fn))
            return fn

        return register

    def run(self, names: set[str] | None = None) -> list[Result]:
        """Run the checks, or just the named subset.

        ``names`` exists so ``verify --only`` can keep its promise of one
        claim in about a second — filtering after a full run cannot.
        """
        out = []
        for name, section, tier, fn in self.checks:
            if names is not None and name not in names:
                continue
            try:
                passed, detail = fn()
            except Exception as exc:  # a broken check is a failure
                passed, detail = False, f"raised {type(exc).__name__}: {exc}"
            out.append(
                Result(
                    name,
                    passed,
                    detail,
                    section,
                    tier,
                    fn.__code__.co_firstlineno,
                    source_path(fn),
                )
            )
        return out


SUITES: list[Suite] = []


def _suite(name: str) -> Suite:
    s = Suite(name)
    SUITES.append(s)
    return s


#: Repository root. ``invariants/_core.py`` sits three directories below it.
ROOT = Path(__file__).resolve().parents[3]
PAPER_DIR = ROOT / "paper"


def source_path(fn) -> str:
    """``src/workhouse/invariants/<module>.py:<line>`` for a check body.

    The split made the old hard-coded ``invariants.py`` string wrong in six
    places at once -- the CLI, the claim catalogue, CERTIFIED.md and three
    edge sources in the graph -- so the path is now derived from the code
    object rather than spelled anywhere.
    """
    path = Path(fn.__code__.co_filename).resolve()
    try:
        relative = path.relative_to(ROOT)
    except ValueError:  # pragma: no cover - only outside a source checkout
        relative = Path(path.name)
    return f"{relative.as_posix()}:{fn.__code__.co_firstlineno}"
