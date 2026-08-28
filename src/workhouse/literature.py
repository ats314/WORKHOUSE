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

The citation web (schema v2) follows the repository's one design pattern:
judgement lives in curated YAML (each paper's ``cites`` list, populated from
primary sources -- INSPIRE reference lists or a pinned PDF's bibliography),
the join is derived (``in_degree`` and ``holes`` are computed at call time,
never stored), and validation is mechanical (every cited id must resolve to
an indexed paper or a declared stub; an orphan stub is rejected as
decoration). Two relevance signals are kept apart because they mean different
things: ``inspire_citations`` is a *global* weight recorded with its
``as_of`` date, and the in-web citation in-degree is a *local* weight -- a
paper heavily cited by the indexed papers is load-bearing for THIS program
whatever the field thinks of it. A citation edge is bibliography, not
endorsement; nothing here can promote a claim.
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
    stubs: list[dict[str, Any]]
    wanted: list[dict[str, Any]]

    @property
    def ids(self) -> set[str]:
        return {p["id"] for p in self.papers}

    @property
    def stub_ids(self) -> set[str]:
        return {s["id"] for s in self.stubs}

    @property
    def node_ids(self) -> set[str]:
        """Everything a ``cites`` entry may resolve to."""
        return self.ids | self.stub_ids

    def entry(self, node_id: str) -> dict[str, Any] | None:
        """The paper or stub record for one id."""
        for record in self.papers + self.stubs:
            if record["id"] == node_id:
                return record
        return None

    def edges(self) -> list[tuple[dict[str, Any], dict[str, Any]]]:
        return [(p, e) for p in self.papers for e in p.get("bears_on", [])]

    def bearing_on(self, target: str) -> list[tuple[dict[str, Any], dict[str, Any]]]:
        """Every (paper, edge) pair that names this claim."""
        return [(p, e) for p, e in self.edges() if e["target"] == target]

    @property
    def targets(self) -> set[str]:
        return {e["target"] for _p, e in self.edges()}

    def cites(self) -> list[tuple[str, str]]:
        """Every curated (citing paper id, cited id) pair. Stubs cite nothing:
        a stub is a node the web points at, not a curated bibliography."""
        return [(p["id"], c) for p in self.papers for c in p.get("cites", [])]

    def in_degree(self) -> dict[str, int]:
        """In-web citation count per node, computed at call time, never stored.

        The LOCAL relevance weight: how many of the indexed papers cite this
        one. Distinct citing papers, not occurrences -- repetition is not
        independence here either. Every node appears, zeros included, so a
        ranking over this dict cannot silently drop the unreferenced.
        """
        counts = dict.fromkeys(self.node_ids, 0)
        for _src, dst in set(self.cites()):
            if dst in counts:
                counts[dst] += 1
        return counts

    def obtained(self, node_id: str) -> bool:
        """Whether the copy read is identifiable: pinned by digest or stored.

        Stubs are never obtained -- they carry no reading at all.
        """
        record = self.entry(node_id)
        if record is None or node_id in self.stub_ids:
            return False
        return bool(record.get("source_sha256")) or bool(record.get("fulltext"))


def load(path: Path | None = None) -> Literature:
    data = yaml.safe_load((path or INDEX).read_text(encoding="utf-8"))
    return Literature(
        papers=data.get("papers", []),
        stubs=data.get("stubs", []),
        wanted=data.get("wanted", []),
    )


def _known_targets() -> set[str]:
    """Everything an entry is allowed to point at.

    Ledger ids, unifying-candidate ids, and the names of registered constants.
    A constant is a legitimate target: "this paper publishes the number
    HAMER_A4_NUM holds" is the sharpest kind of edge there is.
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

    # Storing a paper is republishing it, so a file in fulltext/ with no index
    # entry has bypassed the licence gate entirely. Glob the directory itself:
    # every stored file must be some paper's declared fulltext.
    fulltext_dir = LITERATURE_DIR / "fulltext"
    if fulltext_dir.is_dir():
        declared = {str(p.get("fulltext", "")) for p in lit.papers}
        for stored in sorted(fulltext_dir.iterdir()):
            rel = str(stored.relative_to(LITERATURE_DIR))
            if stored.is_file() and rel not in declared:
                problems.append(f"orphan stored file with no licence record: {rel}")

    in_degree = lit.in_degree()

    seen: set[str] = set()
    for paper in lit.papers:
        pid = paper["id"]
        if pid in seen:
            problems.append(f"{pid}: duplicate id")
        seen.add(pid)

        if not paper.get("doi") and not paper.get("arxiv"):
            problems.append(f"{pid}: no DOI and no arXiv id — the citation is unpinnable")

        problems += _check_inspire_fields(paper)

        # The citation web: curated, but only over resolvable endpoints. A
        # cites entry pointing at nothing is the same failure mode as a
        # bears_on edge whose target does not resolve.
        cited = paper.get("cites", [])
        for target in cited:
            if target == pid:
                problems.append(f"{pid}: cites itself")
            elif target not in lit.node_ids:
                problems.append(f"{pid} cites unknown id {target!r} — index it or declare a stub")
        duplicate_cites = {c for c in cited if cited.count(c) > 1}
        if duplicate_cites:
            problems.append(f"{pid}: duplicate cites entries {sorted(duplicate_cites)}")

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

    # Stubs: nodes the web cites without indexing. A stub nothing cites is
    # decoration; a stub with a bears_on list is an evidence entry trying to
    # dodge the evidence rules; a stub without an identifier is unpinnable.
    for stub in lit.stubs:
        sid = stub["id"]
        if sid in seen:
            problems.append(f"{sid}: stub id collides with a paper id")
        if sid in {s2["id"] for s2 in lit.stubs} and [s["id"] for s in lit.stubs].count(sid) > 1:
            problems.append(f"{sid}: duplicate stub id")
        for field in ("title", "venue", "note"):
            if not str(stub.get(field, "")).strip():
                problems.append(f"{sid}: stub has no {field} — say what it is and why it is here")
        if not stub.get("doi") and not stub.get("arxiv") and not stub.get("inspire_recid"):
            problems.append(f"{sid}: stub has no DOI, arXiv id, or INSPIRE recid — unpinnable")
        if stub.get("bears_on"):
            problems.append(
                f"{sid}: a stub cannot bear on a claim — promote it to a full entry instead"
            )
        if stub.get("cites"):
            problems.append(f"{sid}: a stub cites nothing — a curated bibliography needs an entry")
        if in_degree.get(sid, 0) == 0:
            problems.append(f"{sid}: stub that no indexed paper cites — decoration, remove it")
        problems += _check_inspire_fields(stub)

    for want in lit.wanted:
        if not str(want.get("would_settle", "")).strip():
            problems.append(f"wanted {want.get('what')!r}: does not say what it would settle")

    return problems


def _check_inspire_fields(record: dict[str, Any]) -> list[str]:
    """The global-weight fields: recorded observations, so both halves bind.

    A count without its retrieval date reads as current forever, which is the
    generated-file staleness bug in miniature.
    """
    problems: list[str] = []
    rid = record["id"]
    recid = record.get("inspire_recid")
    if recid is not None and not (isinstance(recid, int) and recid > 0):
        problems.append(f"{rid}: inspire_recid must be a positive integer, got {recid!r}")
    citations = record.get("inspire_citations")
    if citations is not None:
        if not isinstance(citations, dict):
            problems.append(f"{rid}: inspire_citations must be a mapping {{count, as_of}}")
        else:
            count = citations.get("count")
            if not (isinstance(count, int) and count >= 0):
                problems.append(f"{rid}: inspire_citations.count must be an integer >= 0")
            if not str(citations.get("as_of", "")).strip():
                problems.append(
                    f"{rid}: inspire_citations without as_of — an undated count reads as current"
                )
    return problems


@dataclass(frozen=True)
class Hole:
    """One structural hole in the citation web. A lead, never a claim.

    ``kind`` is one of two computed absences:

    * ``disconnected-pair`` — two papers bear on the same claim with no
      citation path between them at all (undirected: shared cited sources
      count, which is bibliographic coupling).
    * ``missed-source`` — a paper bears on a claim without citing, in either
      direction, the most in-web-cited paper bearing on that claim.

    Either way it means one of two things worth checking: a connection the
    literature missed (where "what should they have been using" lives), or a
    sign the bears_on curation conflates two distinct threads. ``lead`` says
    what checking it would take. Nothing here promotes anything.
    """

    kind: str
    target: str
    pair: tuple[str, str]
    lead: str


def _adjacency(lit: Literature) -> dict[str, set[str]]:
    """The cites graph, undirected. Citation direction is temporal accident;
    for connectivity questions the link is what matters."""
    adj: dict[str, set[str]] = {n: set() for n in lit.node_ids}
    for src, dst in lit.cites():
        if dst in adj:
            adj[src].add(dst)
            adj[dst].add(src)
    return adj


def _connected(adj: dict[str, set[str]], a: str, b: str) -> bool:
    seen = {a}
    stack = [a]
    while stack:
        node = stack.pop()
        if node == b:
            return True
        for other in adj.get(node, ()):
            if other not in seen:
                seen.add(other)
                stack.append(other)
    return False


def _components(adj: dict[str, set[str]]) -> list[list[str]]:
    """Connected components, largest first, isolated nodes last."""
    seen: set[str] = set()
    out: list[list[str]] = []
    for start in sorted(adj):
        if start in seen:
            continue
        component = []
        stack = [start]
        seen.add(start)
        while stack:
            node = stack.pop()
            component.append(node)
            for other in adj[node]:
                if other not in seen:
                    seen.add(other)
                    stack.append(other)
        out.append(sorted(component))
    out.sort(key=lambda c: (-len(c), c[0]))
    return out


def holes(lit: Literature | None = None) -> list[Hole]:
    """The missing-link report, computed from bears_on and cites at call time.

    ``confusable`` edges are excluded from "bears on": that relation exists to
    say a paper is NOT a source for the claim, so its absence of citation
    links is the expected state, not a hole. A ``missed-source`` hole is
    skipped when the paper predates the most-cited source — a 1984 paper
    cannot cite 1989, and reporting that it does not would erode the report.
    """
    lit = lit or load()
    adj = _adjacency(lit)
    in_degree = lit.in_degree()
    year = {r["id"]: int(r.get("year", 0)) for r in lit.papers + lit.stubs}
    recid = {r["id"]: r.get("inspire_recid") for r in lit.papers + lit.stubs}

    bearing: dict[str, set[str]] = {}
    for paper, edge in lit.edges():
        if edge["relation"] != "confusable":
            bearing.setdefault(edge["target"], set()).add(paper["id"])

    out: list[Hole] = []
    for target in sorted(bearing):
        pids = sorted(bearing[target])
        disconnected: set[frozenset[str]] = set()
        for i, a in enumerate(pids):
            for b in pids[i + 1 :]:
                if not _connected(adj, a, b):
                    disconnected.add(frozenset((a, b)))
                    early, late = sorted((a, b), key=lambda p: year.get(p, 0))
                    out.append(
                        Hole(
                            "disconnected-pair",
                            target,
                            (a, b),
                            f"no citation path at all between {a} and {b}, which "
                            f"both bear on {target}. Check: read {late}'s full "
                            f"reference list (INSPIRE recid {recid.get(late)}) for "
                            f"{early} or a shared ancestor. A genuine absence is "
                            "either a link the literature missed or a sign the "
                            f"bears_on curation conflates two threads under {target}.",
                        )
                    )
        ranked = sorted(pids, key=lambda p: (-in_degree.get(p, 0), p))
        top = ranked[0] if ranked and in_degree.get(ranked[0], 0) > 0 else None
        if top is None:
            continue
        for pid in pids:
            if pid == top or top in adj.get(pid, set()):
                continue
            if frozenset((pid, top)) in disconnected:
                continue  # already reported as the stronger absence
            if year.get(pid, 0) < year.get(top, 0):
                continue  # cannot cite what did not exist yet
            out.append(
                Hole(
                    "missed-source",
                    target,
                    (pid, top),
                    f"{pid} bears on {target} without citing {top}, the most "
                    f"in-web-cited paper for that claim ({in_degree[top]} in-web "
                    f"citations). Check: {pid}'s full reference list (INSPIRE "
                    f"recid {recid.get(pid)}) — an independent route to {target} "
                    "is worth recording; a conflated thread is worth fixing.",
                )
            )
    return out


def relevance(lit: Literature | None = None) -> list[dict[str, Any]]:
    """Every node ranked by the two weights, local first.

    Local (in-web in-degree) outranks global (INSPIRE count) deliberately: a
    paper every indexed paper leans on is load-bearing for THIS program even
    if the field ignores it, and MP_1999's 1233 global citations do not make
    it more central to this web than KS_1975's seven in-web ones.
    """
    lit = lit or load()
    in_degree = lit.in_degree()
    rows = []
    for record in lit.papers + lit.stubs:
        rid = record["id"]
        citations = record.get("inspire_citations") or {}
        rows.append(
            {
                "id": rid,
                "in_web": in_degree.get(rid, 0),
                "inspire": citations.get("count"),
                "as_of": str(citations.get("as_of", "")),
                "stub": rid in lit.stub_ids,
                "obtained": lit.obtained(rid),
                "year": record.get("year"),
            }
        )
    rows.sort(key=lambda r: (-r["in_web"], -(r["inspire"] or 0), r["id"]))
    return rows


def acquisition_targets(lit: Literature | None = None) -> list[dict[str, Any]]:
    """Unobtained nodes that the web itself says matter, most cited first.

    The payoff of computing relevance: the next paper worth obtaining falls
    out of the data instead of being remembered. Only nodes some indexed
    paper cites qualify — an unobtained leaf is not a target, it is a note.
    """
    lit = lit or load()
    return [r for r in relevance(lit) if not r["obtained"] and r["in_web"] > 0]


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

    in_degree = lit.in_degree()

    w("\033[1mLiterature evidence map\033[0m")
    for paper in lit.papers:
        ident = paper.get("arxiv") or paper.get("doi")
        w(f"\n  \033[1m{paper['id']}\033[0m  {paper['title']}")
        w(f"    {', '.join(paper['authors'])} · {paper['venue']} ({paper['year']}) · {ident}")
        w(f"    {_weights_line(paper, in_degree)}")
        for edge in paper.get("bears_on", []):
            w(f"      → {edge['target']:<12} {edge['relation']:<20} {edge['status']}")
        cited = paper.get("cites", [])
        if cited:
            w(f"      \033[2mcites: {', '.join(cited)}\033[0m")
        for question in paper.get("open_questions", []):
            w(f"        ? {question}")
        for answered in paper.get("answered_questions", []):
            w(f"        \033[2m✓ {answered['q']}\033[0m")

    if lit.stubs:
        w("\n\033[1mStubs\033[0m — cited by the web, not indexed; they can promote nothing")
        for stub in lit.stubs:
            w(f"\n  {stub['id']}  {stub['title']}")
            w(f"    {stub['venue']} ({stub['year']}) · {_weights_line(stub, in_degree)}")

    w("\n\033[1mLoad-bearing in this web\033[0m — in-web citations first, INSPIRE second")
    for row in relevance(lit):
        if row["in_web"] == 0:
            continue
        mark = "stub" if row["stub"] else ("pinned" if row["obtained"] else "UNOBTAINED")
        inspire = f"INSPIRE {row['inspire']}" if row["inspire"] is not None else "INSPIRE —"
        w(f"  {row['in_web']:>2} in-web · {inspire:<14} {row['id']:<22} {mark}")
    targets = acquisition_targets(lit)
    if targets:
        top = targets[0]
        w(
            f"\n\033[33mNext acquisition target: {top['id']} — {top['in_web']} in-web "
            "citations and nobody here has read or pinned it.\033[0m"
        )

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


def _weights_line(record: dict[str, Any], in_degree: dict[str, int]) -> str:
    """Both relevance signals on one line, labelled so they cannot be confused."""
    citations = record.get("inspire_citations") or {}
    count = citations.get("count")
    as_of = str(citations.get("as_of", ""))
    inspire = f"INSPIRE {count} (as of {as_of})" if count is not None else "INSPIRE not recorded"
    return f"cited in-web by {in_degree.get(record['id'], 0)} · {inspire}"


def format_holes(lit: Literature | None = None) -> str:
    """``workhouse lit --holes``: the missing-link report.

    Every hole is a research lead with what checking it would take. An empty
    report is a real result too — it means every pair of papers bearing on a
    common claim is already citation-connected — so the component structure is
    printed either way, and a hole is never promoted to anything.
    """
    lit = lit or load()
    out: list[str] = []
    w = out.append
    found = holes(lit)
    w("\033[1mMissing-link report\033[0m — computed from bears_on × cites, never stored")
    if not found:
        w("\n  No structural holes: every pair of papers bearing on a common claim")
        w("  is citation-connected, and nothing skips its claim's most-cited source.")
    for hole in found:
        w(f"\n  \033[33m{hole.kind}\033[0m on \033[1m{hole.target}\033[0m: {' ↔ '.join(hole.pair)}")
        w(f"    {hole.lead}")
    w("\n\033[1mCitation components\033[0m — islands are where future holes will open")
    for component in _components(_adjacency(lit)):
        w(f"  [{len(component)}] {', '.join(component)}")
    w("")
    w("A hole is a lead, never a claim: checking one can add a citation edge or")
    w("fix a bears_on conflation, and nothing here auto-promotes either way.")
    return "\n".join(out)
