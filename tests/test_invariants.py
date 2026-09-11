"""Every registered invariant runs as its own test case."""

import pytest

from workhouse.invariants import SUITES

CASES = [(s.name, name, tier) for s in SUITES for name, _sec, tier, _fn in s.checks]


@pytest.fixture(scope="session")
def verdicts():
    """Every suite's results, computed once per pytest session.

    The suites run through the same per-check cache the collectors use
    (``check_cache.CheckCache``), so within one session each check executes
    once however many tests want its verdict: ``test_certified`` renders
    CERTIFIED.md from the same cache, and whichever runs first pays for the
    computation. Before this fixture each parametrised case called its check
    body directly, past the cache, so CI computed every check twice -- about
    six of the fourteen minutes the check job took on 2026-09-10.

    A cached verdict is keyed on every input a check can read (see
    ``check_cache``), so a hit means nothing changed since the check last
    ran. ``WORKHOUSE_NO_CACHE=1`` makes every check execute, and a fresh CI
    container has nothing to hit.
    """
    from workhouse.check_cache import CheckCache

    cache = CheckCache()
    return {(s.name, r.name): r for s in SUITES for r in s.run(cache=cache)}


@pytest.mark.parametrize(
    ("suite", "name", "tier"),
    CASES,
    ids=[f"{s}::{n}" for s, n, _t in CASES],
)
def test_invariant(suite, name, tier, verdicts):
    # A check returns (passed, detail) or, since 2026-09-01, (passed, detail,
    # yields). The suite runner normalises the third element with
    # ``_exact_yields``, so a yielded float without the _NUM suffix fails here
    # too: the runner records it as a failed result with the reason in detail.
    result = verdicts[(suite, name)]
    assert result.passed, f"[{suite}] T{tier} {name}: {result.detail}"


def test_every_suite_has_checks():
    empty = [s.name for s in SUITES if not s.checks]
    assert not empty, f"suites with no checks: {empty}"


def test_every_check_declares_a_tier_it_can_support():
    """T2 means the verdict rests on a float; T1 means it does not.

    Declared, not inferred -- but a T1 check that compares against a `*_NUM`
    constant or a stated tolerance is mislabelled, and that mislabelling is how
    a numerical agreement quietly starts being quoted as an exact one.
    """
    import inspect
    import re

    numeric = re.compile(r"_NUM\b|TOLERANCE|\d+e-\d+|isclose")
    wrong = []
    for suite in SUITES:
        for name, _sec, tier, fn in suite.checks:
            body = inspect.getsource(fn)
            if tier == 1 and numeric.search(body):
                wrong.append(f"{suite.name}::{name}")
    assert not wrong, f"checks resting on floats but declared T1: {wrong}"


def test_every_suite_module_is_registered():
    """A suite module absent from `_MODULES` would never register its suite.

    The single-file version could not have this bug: defining a suite ran it.
    After the split, registration is import, and import is the `_MODULES`
    tuple in `invariants/__init__.py` -- so a new module added to the
    directory and forgotten there would drop its whole suite from `verify`,
    from `FRONTIER.md` and from the catalogue, with every remaining check
    still green. Coverage shrinking silently is the one thing this repository
    must never do, so the directory and the tuple are compared.
    """
    import pathlib

    from workhouse import invariants

    directory = pathlib.Path(invariants.__file__).parent
    on_disk = {p.stem for p in directory.glob("*.py") if not p.stem.startswith(("_", "test_"))}
    listed = set(invariants._MODULES)
    assert on_disk == listed, (
        f"suite modules on disk but not in _MODULES: {sorted(on_disk - listed)}; "
        f"listed but missing: {sorted(listed - on_disk)}"
    )


def test_every_check_reports_a_source_that_exists(monkeypatch):
    """`verify`, the catalogue and CERTIFIED.md all print a check's location.

    That location used to be a hard-coded `invariants.py` plus a line number,
    which the package split silently falsified in six places at once. It is
    now derived from the code object, and this pins that it resolves.
    """
    import pathlib

    from workhouse.invariants._core import Suite, source_path

    def reject_execution(*_args, **_kwargs):
        pytest.fail("Source metadata inspection must not rerun mathematical checks")

    monkeypatch.setattr(Suite, "run", reject_execution)
    root = pathlib.Path(__file__).resolve().parents[1]
    for suite in SUITES:
        for name, _sec, _tier, fn in suite.checks:
            source = source_path(fn)
            path, _, line = source.rpartition(":")
            assert (root / path).is_file(), f"{suite.name}::{name} -> {source}"
            assert int(line) > 0
            assert int(line) == fn.__code__.co_firstlineno
            assert path.startswith("src/workhouse/invariants/"), source


def test_suite_run_reports_source_metadata():
    from workhouse.invariants._core import Suite

    suite = Suite("source metadata probe")

    @suite.check("probe")
    def probe():
        return True, "cheap source metadata check"

    (result,) = suite.run()
    assert result.passed
    assert result.line == probe.__code__.co_firstlineno
    assert result.source == f"tests/test_invariants.py:{probe.__code__.co_firstlineno}"
