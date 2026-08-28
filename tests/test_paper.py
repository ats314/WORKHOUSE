"""The manuscript is pinned evidence, and its printed contract is checkable.

``paper/`` holds the manuscript that cites this repository by commit. Two
things are worth a test rather than a promise:

1. the artifacts are byte-pinned, exactly like ``runs/`` — a manuscript that
   can drift silently stops being the thing the checks refer to;
2. ``verify_core.py``, which §9 of the manuscript names as accompanying it,
   actually runs, actually passes, and does not disagree with the registry.

The third thing — that no fourth-order coefficient enters the manuscript — is
an invariant, not a test, because it is a statement about the corpus rather
than about the repository's plumbing. See the ``the flat-band manuscript``
suite.
"""

import hashlib
import subprocess
import sys
from pathlib import Path

from sympy import Rational

from workhouse import constants as K

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"


def test_paper_directory_is_fully_pinned():
    manifest = PAPER / "SHA256SUMS"
    assert manifest.exists(), "paper/SHA256SUMS is missing"
    recorded = {}
    for line in manifest.read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            digest, name = line.split(maxsplit=1)
            recorded[name.strip()] = digest
    on_disk = {p.name for p in PAPER.iterdir()} - {"SHA256SUMS", "README.md"}
    assert set(recorded) == on_disk, f"pinned {sorted(recorded)} != on disk {sorted(on_disk)}"
    for name, digest in recorded.items():
        actual = hashlib.sha256((PAPER / name).read_bytes()).hexdigest()
        assert actual == digest, f"paper/{name} changed: {actual}"


def test_verify_core_runs_and_passes():
    script = ROOT / "verify_core.py"
    assert script.exists(), "verify_core.py is what the manuscript's section 9 promises"
    done = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, timeout=120
    )
    assert done.returncode == 0, done.stdout + done.stderr
    assert "FAIL" not in done.stdout, done.stdout


def test_verify_core_ledger_agrees_with_the_registry():
    """The portable verifier is independent in implementation, not in values.

    It reimplements the algebra with nothing but ``fractions``, which is the
    point — a referee who installs nothing can still run it. But if its
    hard-coded ledger drifted from ``constants.py`` the two would certify
    different papers, so the values are joined here.
    """
    sys.path.insert(0, str(ROOT))
    import verify_core as VC

    assert VC.T3 == K.T_MINUS_2
    assert VC.B3 == K.B_3
    assert VC.LEAK3 == K.LEAK_3
    assert VC.D3 == K.D_3
    assert VC.E_FLAT_2 == K.BAND_ODD_FLAT
    assert VC.D_MINUS_2 == K.D_MINUS_2
    assert (Rational(8, 3), Rational(1), Rational(1, 2), Rational(7, 32)) == VC.TOWER
    assert VC.T_N.at(3) == K.hopping(3)
    for n in (3, 4, 5, 7, 11):
        assert VC.T_N.at(n) == K.hopping(n), n
        assert VC.A_N.at(n) == K.antiparallel_sum(n), n
        assert VC.B_N.at(n) == K.parallel_sum(n), n


def test_verify_core_is_standard_library_only():
    """A verifier with a dependency is not portable, whatever its docstring says."""
    body = (ROOT / "verify_core.py").read_text()
    forbidden = ("sympy", "numpy", "scipy", "flint", "workhouse", "yaml")
    hits = [name for name in forbidden if f"import {name}" in body]
    assert not hits, f"verify_core.py imports {hits}; it must run on a bare interpreter"
