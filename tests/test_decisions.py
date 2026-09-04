"""The ADR numbers are the one identifier here that git cannot protect.

Every other generated or curated artifact in this repository has a test that
fails when two sources disagree. The decision records do not, because their
identity is a number and their filename is `NNNN-a-slug.md`: two branches that
both claim 0022 produce two *different* filenames, so git merges them cleanly
and reports no conflict. The corruption is silent by construction.

It has already happened once. Commit 36c6678 reads "Renumber the ADR to 0014:
PR #35 claimed 0013 concurrently" -- which is why 0013 is vacant on main to this
day. At the time this file was written the open queue held three more instances:
#48 adds a second 0015 and 0016, and #80 and #81 both add a 0022 and a 0023.
None of them conflict.

The rule this replaces is "remember to check the queue before you pick a
number", which is a rule about a person's attention, and the queue is 22 PRs
deep precisely because that attention is the scarce resource. So it is checked
here instead. Whichever PR lands second goes red, and the fix is a rename.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = ROOT / "docs" / "decisions"
NAME = re.compile(r"^(\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")


def _records() -> list[Path]:
    return sorted(p for p in DECISIONS.glob("*.md") if p.name != "README.md")


def test_no_two_decisions_claim_the_same_number():
    """Two ADRs numbered 0022 are one citation that resolves to two documents."""
    seen: dict[str, list[str]] = {}
    for path in _records():
        seen.setdefault(path.name[:4], []).append(path.name)
    clashes = {num: names for num, names in seen.items() if len(names) > 1}
    assert not clashes, "two decision records claim the same number: " + "; ".join(
        f"{num} -> {', '.join(sorted(names))}" for num, names in sorted(clashes.items())
    )


def test_every_decision_filename_is_shaped_like_one():
    """A name the glob cannot parse is a record the duplicate check cannot see.

    `NNNN-lower-case-slug.md`. Enforced so that the guard above never passes
    because a record slipped out of its own namespace.
    """
    malformed = [p.name for p in _records() if not NAME.match(p.name)]
    assert not malformed, f"decision records that do not match NNNN-slug.md: {malformed}"
