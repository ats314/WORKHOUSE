"""Every registered invariant runs as its own test case."""

import pytest

from workhouse.invariants import SUITES

CASES = [(s.name, name, tier, fn) for s in SUITES for name, _sec, tier, fn in s.checks]


@pytest.mark.parametrize(
    ("suite", "name", "tier", "fn"),
    CASES,
    ids=[f"{s}::{n}" for s, n, _t, _f in CASES],
)
def test_invariant(suite, name, tier, fn):
    passed, detail = fn()
    assert passed, f"[{suite}] T{tier} {name}: {detail}"


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


def test_every_check_reports_a_source_that_exists():
    """`verify`, the catalogue and CERTIFIED.md all print a check's location.

    That location used to be a hard-coded `invariants.py` plus a line number,
    which the package split silently falsified in six places at once. It is
    now derived from the code object, and this pins that it resolves.
    """
    import pathlib

    root = pathlib.Path(__file__).resolve().parents[1]
    for suite in SUITES:
        for name, _sec, _tier, _fn in suite.checks:
            result = next(r for r in suite.run({name}) if r.name == name)
            path, _, line = result.source.rpartition(":")
            assert (root / path).is_file(), f"{suite.name}::{name} -> {result.source}"
            assert int(line) > 0
            assert path.startswith("src/workhouse/invariants/"), result.source
