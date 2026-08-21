"""Every check citation must resolve to something a cold agent can open.

CLAUDE.md's first instruction when a check fails is "re-read the corpus
section the check cites" — which requires the cite to name a findable
document. `ledger/documents.yaml` is the legend for the alias vocabulary the
`section` strings use; this test makes an unlegended NEW alias a build
failure, keeps every legend path real, and keeps the standing vocabulary
closed. An alias may be explicitly `unresolved` — a recorded unknown beats a
plausible wrong mapping — but it must say so.
"""

import re
from pathlib import Path

import yaml

from workhouse.invariants import SUITES

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "ledger" / "documents.yaml"
STANDINGS = {"current", "superseded", "quarantined", "corpus", "repo"}

ALIASES = yaml.safe_load(SOURCE.read_text())["aliases"]

#: Tokens that make a citation resolvable WITHOUT the alias table: ledger ids,
#: ADR references, literature ids, and repository paths.
LEDGER_ID = re.compile(r"\b[CGRU]\d+\b")
ADR = re.compile(r"\bADR\b")
LIT_ID = re.compile(r"\b[A-Z]{2,}_\d{4}\b")  # CS_2006, KRS_2023, HAMER_1989 ...
PATHISH = re.compile(r"[\w./-]+\.(?:py|md|yaml|json|txt|tex|csv)\b")


def test_legend_is_sound():
    seen = set()
    for entry in ALIASES:
        alias = entry["alias"]
        assert alias not in seen, f"duplicate alias {alias!r}"
        seen.add(alias)
        if entry.get("unresolved"):
            assert entry.get("note"), f"{alias}: unresolved alias needs a note saying what is known"
            assert "path" not in entry, f"{alias}: unresolved but carries a path — pick one"
            continue
        path = entry["path"]
        assert (ROOT / path).is_file(), f"{alias}: {path} does not exist"
        assert entry["standing"] in STANDINGS, f"{alias}: unknown standing {entry['standing']!r}"
        if entry["standing"] == "superseded":
            assert "superseded" in path, f"{alias}: superseded standing but not in superseded/"


def test_every_check_citation_resolves():
    """Each section string must carry at least one resolvable token."""
    known = {e["alias"] for e in ALIASES}
    orphans = []
    for suite in SUITES:
        for name, section, _tier, _fn in suite.checks:
            blob = f"{section} | {suite.name}"
            resolvable = (
                any(alias in blob for alias in known)
                or LEDGER_ID.search(blob)
                or ADR.search(blob)
                or LIT_ID.search(blob)
                or PATHISH.search(blob)
            )
            if not resolvable:
                orphans.append(f"{suite.name} :: {name} :: {section!r}")
    assert not orphans, "citations no cold agent can resolve:\n  " + "\n  ".join(orphans)
