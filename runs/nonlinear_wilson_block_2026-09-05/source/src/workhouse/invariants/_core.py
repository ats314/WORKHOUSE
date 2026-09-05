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
    #: Exact values this check establishes, ``NAME -> "p/q"`` (or a symbolic
    #: string), returned by the check as an optional third element. A yielded
    #: value becomes a catalogue constant that ``workhouse search`` can reach
    #: by value, with a ``yields`` edge from the check. Floats are refused
    #: unless the name carries the ``_NUM`` suffix -- the registry's own
    #: exact/float boundary, enforced at the point a number is born.
    yields: dict[str, str] = field(default_factory=dict)
    #: Registered check names this check's verdict rests on, declared by the
    #: author at registration. Rendered as ``rests_on`` edges in the graph.
    rests_on: tuple[str, ...] = ()


@dataclass
class Suite:
    """A named group of checks."""

    name: str
    checks: list[tuple[str, str, int, Callable[[], tuple[bool, str]]]] = field(default_factory=list)

    def check(
        self,
        name: str,
        section: str = "",
        tier: int = 1,
        rests_on: tuple[str, ...] | list[str] = (),
    ):
        """Register a check.

        ``tier`` is the verification tier the check establishes, and it is
        declared rather than inferred because the difference is the whole point:
        T1 is exact re-derivation, T2 is float agreement within a tolerance. A
        check that compares against a ``*_NUM`` constant or a stated tolerance
        is T2 however exact its inputs look.

        ``rests_on`` names the registered checks whose results this one takes
        as inputs -- the sibling census a proof delegates to, the closed form
        an assembly substitutes into. It is declared, never inferred, and the
        graph turns it into ``rests_on`` edges between checks; until it
        existed the graph had 265 check nodes and not one edge between them,
        so nothing could answer "which checks fall if this one is refuted".
        Names must resolve to exactly one registered check; the graph
        validator and a test hold that.
        """
        if tier not in (1, 2):
            raise ValueError(f"{name}: a check establishes T1 or T2, not T{tier}")
        rests = tuple(rests_on)
        if name in rests:
            raise ValueError(f"{name}: a check cannot rest on itself")

        def register(fn):
            fn.rests_on = rests
            self.checks.append((name, section, tier, fn))
            return fn

        return register

    def run(self, names: set[str] | None = None, cache=None) -> list[Result]:
        """Run the checks, or just the named subset.

        ``names`` exists so ``verify --only`` can keep its promise of one
        claim in about a second — filtering after a full run cannot.

        ``cache`` is a ``check_cache.CheckCache`` or ``None``. With one, a
        check whose inputs are unchanged since its last run returns its
        recorded result instead of running; the collectors pass one, and
        ``workhouse verify`` never does, because "re-derive it now" is that
        command's whole promise.
        """
        import inspect

        out = []
        for name, section, tier, fn in self.checks:
            if names is not None and name not in names:
                continue
            key = None
            if cache is not None and cache.on:
                try:
                    source = inspect.getsource(fn)
                except OSError:  # pragma: no cover
                    source = ""
                key = cache.key(self.name, name, source)
                hit = cache.get(key)
                if hit is not None:
                    hit["rests_on"] = tuple(hit.get("rests_on", ()))
                    out.append(Result(**hit))
                    continue
            yields: dict[str, str] = {}
            try:
                outcome = fn()
                if len(outcome) == 3:
                    passed, detail, raw = outcome
                    yields = _exact_yields(name, raw)
                else:
                    passed, detail = outcome
            except Exception as exc:  # a broken check is a failure
                passed, detail = False, f"raised {type(exc).__name__}: {exc}"
            # Plain Python types only: a sympy BooleanTrue passes every `if`
            # but is not a bool, and a cached result must serialise as JSON.
            result = Result(
                name,
                bool(passed),
                str(detail),
                section,
                tier,
                fn.__code__.co_firstlineno,
                source_path(fn),
                yields,
                getattr(fn, "rests_on", ()),
            )
            out.append(result)
            if key is not None:
                cache.put(key, result)
        return out


def _exact_yields(check_name: str, raw: dict) -> dict[str, str]:
    """Normalise a check's yielded values, refusing a float that reads as exact.

    The registry's rule is that exact values are rationals and floats carry a
    ``_NUM`` suffix, and a value born inside a check is the easiest place for
    that boundary to be crossed unnoticed. So the rule is applied here, at
    birth: a ``float`` under a name without ``_NUM`` raises, and the check
    that yielded it fails with the reason in its detail line.
    """
    from fractions import Fraction

    out: dict[str, str] = {}
    for name, value in raw.items():
        if not (isinstance(name, str) and name.isupper() and name.replace("_", "").isalnum()):
            raise ValueError(f"{check_name}: yielded name {name!r} is not an UPPER_CASE identifier")
        if isinstance(value, float):
            if not name.endswith("_NUM"):
                raise ValueError(
                    f"{check_name}: yielded {name} is a float; a float carries the _NUM suffix"
                )
            out[name] = repr(value)
        elif isinstance(value, bool):
            raise ValueError(f"{check_name}: yielded {name} is a bool, not a value")
        elif isinstance(value, int):
            out[name] = str(value)
        elif isinstance(value, Fraction):
            out[name] = f"{value.numerator}/{value.denominator}"
        elif hasattr(value, "p") and hasattr(value, "q"):  # sympy Rational / Integer
            out[name] = f"{value.p}/{value.q}" if value.q != 1 else str(value.p)
        elif getattr(value, "free_symbols", None):
            out[name] = str(value)  # symbolic in N or L, exact as an expression
        else:
            raise ValueError(f"{check_name}: yielded {name} has unsupported type {type(value)}")
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
