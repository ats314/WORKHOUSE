"""Published literature as an evidence map, not a bibliography.

An entry earns its place by naming a claim in this repository and saying what
relationship the paper has to it. Validation enforces that: a target that does
not resolve is an error, because a citation attached to nothing is decoration.

Two disciplines this module exists to keep:

* **A published paper is not authority either.** It is T3 until something
  checks it, exactly like a corpus document. What makes an external result
  valuable is independence -- it was produced without knowledge of this program
  -- not its being published.
* **A paper can be pinned without being stored.** ``source_sha256`` records
  the digest of the copy that was actually read, so the reading is
  identifiable and re-checkable by anyone holding the same file, while the
  file itself stays out of the repository.
* **Full text is stored only where the licence permits redistribution.** Most
  of the load-bearing literature here predates 2004 and carries the arXiv
  assumed-1991-2003 licence, which grants arXiv distribution rights and grants
  third parties nothing. ``validate`` refuses a ``fulltext`` path under any
  licence not on the redistributable list.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from . import constants as K
from . import ledger as ledger_mod

ROOT = Path(__file__).resolve().parents[2]
LITERATURE_DIR = ROOT / "literature"
INDEX = LITERATURE_DIR / "index.yaml"

RELATIONS = frozenset(
    {
        "supplies-value",
        "supplies-method",
        "corroborates",
        "contradicts",
        "supplies-comparison",
        "confusable",
    }
)

EDGE_STATUSES = frozenset({"verified", "transcription-unverified", "not-yet-obtained", "refuted"})

#: Licences under which storing the paper's text in this repository is lawful.
#: The arXiv "assumed-1991-2003" licence is deliberately absent: it is a licence
#: to arXiv, not to anyone else.
REDISTRIBUTABLE = frozenset(
    {"cc-by", "cc-by-sa", "cc-by-nc-sa", "cc0", "public-domain", "arxiv-cc-by-4.0"}
)

#: Licences that permit redistribution only of an UNMODIFIED copy. The
#: NoDerivatives clause is the whole difference: the file may be stored, but not
#: reformatted, excerpted into the repository, or shipped as extracted text. So
#: a fulltext under one of these must hash to the recorded ``source_sha256``,
#: which is checked rather than promised.
VERBATIM_ONLY = frozenset({"cc-by-nc-nd", "cc-by-nd"})

LEDGER_ID = re.compile(r"^[CGRU]\d+$")


@dataclass
class Literature:
    papers: list[dict[str, Any]]
    wanted: list[dict[str, Any]]

    @property
    def ids(self) -> set[str]:
        return {p["id"] for p in self.papers}

    def edges(self) -> list[tuple[dict[str, Any], dict[str, Any]]]:
        return [(p, e) for p in self.papers for e in p.get("bears_on", [])]

    def bearing_on(self, target: str) -> list[tuple[dict[str, Any], dict[str, Any]]]:
        """Every (paper, edge) pair that names this claim."""
        return [(p, e) for p, e in self.edges() if e["target"] == target]

    @property
    def targets(self) -> set[str]:
        return {e["target"] for _p, e in self.edges()}


def load(path: Path | None = None) -> Literature:
    data = yaml.safe_load((path or INDEX).read_text())
    return Literature(papers=data.get("papers", []), wanted=data.get("wanted", []))


def _known_targets() -> set[str]:
    """Everything an entry is allowed to point at.

    Ledger ids, unifying-candidate ids, and the names of registered constants.
    A constant is a legitimate target: "this paper publishes the number
    HAMER_A4 holds" is the sharpest kind of edge there is.
    """
    led = ledger_mod.load()
    ids = led.contradiction_ids | led.gap_ids | led.register_ids
    ids |= {u["id"] for u in led.unifying_candidates}
    ids |= {name for name in dir(K) if name.isupper()}
    return ids


def validate(lit: Literature | None = None) -> list[str]:
    lit = lit or load()
    problems: list[str] = []
    known = _known_targets()

    seen: set[str] = set()
    for paper in lit.papers:
        pid = paper["id"]
        if pid in seen:
            problems.append(f"{pid}: duplicate id")
        seen.add(pid)

        if not paper.get("doi") and not paper.get("arxiv"):
            problems.append(f"{pid}: no DOI and no arXiv id — the citation is unpinnable")

        digest = str(paper.get("source_sha256", ""))
        if digest and len(digest) != 64:
            problems.append(f"{pid}: source_sha256 is not a SHA-256 digest")

        licence = str(paper.get("licence", "")).lower()
        fulltext = paper.get("fulltext")
        if fulltext:
            path = LITERATURE_DIR / fulltext
            if licence not in REDISTRIBUTABLE | VERBATIM_ONLY:
                problems.append(
                    f"{pid}: stores fulltext under licence {licence!r}, which does not "
                    "permit redistribution"
                )
            elif not path.is_file():
                problems.append(f"{pid}: fulltext {fulltext} is missing")
            elif licence in VERBATIM_ONLY:
                # NoDerivatives: prove the stored bytes are the ones read.
                if not digest:
                    problems.append(
                        f"{pid}: {licence} permits only a verbatim copy, so "
                        "source_sha256 is required to show the file is unmodified"
                    )
                else:
                    actual = hashlib.sha256(path.read_bytes()).hexdigest()
                    if actual != digest:
                        problems.append(
                            f"{pid}: stored fulltext does not match source_sha256 "
                            f"({actual} != {digest}); {licence} forbids derivatives"
                        )

        # A scope firewall is only worth writing down if it binds. A paper from
        # a different regime -- other dimension, other field content -- may be
        # compared against or borrowed from methodologically, but its NUMBERS
        # must never enter. Corpus section 12 forbids exactly that crossing.
        firewall = str(paper.get("scope_firewall", "")).strip()
        edges = paper.get("bears_on", [])
        if firewall:
            supplying = [e["target"] for e in edges if e["relation"] == "supplies-value"]
            if supplying:
                problems.append(
                    f"{pid} declares a scope firewall but supplies values to "
                    f"{supplying}; a cross-regime number is exactly what the "
                    "firewall forbids"
                )
        if not edges:
            problems.append(f"{pid}: bears on nothing — a citation attached to no claim")
        for edge in edges:
            target = edge["target"]
            if target not in known:
                problems.append(f"{pid} bears on unknown target {target}")
            if edge["relation"] not in RELATIONS:
                problems.append(f"{pid}->{target}: unknown relation {edge['relation']!r}")
            if edge["status"] not in EDGE_STATUSES:
                problems.append(f"{pid}->{target}: unknown status {edge['status']!r}")
            if not str(edge.get("detail", "")).strip():
                problems.append(f"{pid}->{target}: no detail — say what the paper does here")

    for want in lit.wanted:
        if not str(want.get("would_settle", "")).strip():
            problems.append(f"wanted {want.get('what')!r}: does not say what it would settle")

    return problems


def format_index(lit: Literature | None = None, target: str | None = None) -> str:
    lit = lit or load()
    out: list[str] = []
    w = out.append

    if target:
        rows = lit.bearing_on(target)
        w(f"\033[1mPublished work bearing on {target}\033[0m")
        if not rows:
            w(
                "  nothing indexed. `workhouse lit` lists what is here; "
                "literature/index.yaml has a `wanted` list."
            )
            return "\n".join(out)
        for paper, edge in rows:
            w(f"\n  {paper['id']} — {paper['title']}")
            w(f"    {', '.join(paper['authors'])} · {paper['venue']} ({paper['year']})")
            w(f"    \033[1m{edge['relation']}\033[0m · {edge['status']}")
            w(f"    {' '.join(str(edge['detail']).split())}")
        return "\n".join(out)

    w("\033[1mLiterature evidence map\033[0m")
    for paper in lit.papers:
        ident = paper.get("arxiv") or paper.get("doi")
        w(f"\n  \033[1m{paper['id']}\033[0m  {paper['title']}")
        w(f"    {', '.join(paper['authors'])} · {paper['venue']} ({paper['year']}) · {ident}")
        for edge in paper.get("bears_on", []):
            w(f"      → {edge['target']:<12} {edge['relation']:<20} {edge['status']}")
        for question in paper.get("open_questions", []):
            w(f"        ? {question}")

    w("\n\033[1mWanted\033[0m — named because they would settle something")
    for want in lit.wanted:
        w(f"\n  {want['what']}")
        w(f"    {' '.join(str(want['would_settle']).split())}")

    unverified = [
        (p["id"], e["target"])
        for p, e in lit.edges()
        if e["status"] in ("transcription-unverified", "not-yet-obtained")
    ]
    w(
        f"\n\033[33m{len(unverified)} of {len(lit.edges())} edges rest on an unread or "
        f"unpinned source.\033[0m"
    )
    return "\n".join(out)
