"""Every relationship this repository records, as one generated edge list.

The entities already have machine-readable records — ``index/claims.jsonl``
plus the symbols in ``index/symbols.jsonl`` — but the relationships between
them were siloed in six formats: ledger edge fields, the symbol records'
``claims``/``code_names`` lists, free-text section strings on checks,
literature ``bears_on`` edges, ADR prose, and (until ``ledger/theorems.yaml``)
nothing at all for the Lean layer. This module reads each of those sources and
emits ``index/graph.jsonl``: one JSON record per edge,
``{src, dst, type, how, source}``.

Two rules keep the graph honest:

* **Edges are computed, never asserted.** A *curated* edge's ``type`` is the
  verbatim field name of the file it was read from (``blocks``, ``resolves``,
  ``bears_on``, ``formalizes``, ...); a *derived* edge names its extraction
  (``cites`` — an id parsed out of a check's registered name, section, or
  suite name; ``mentions`` — an id appearing in an ADR body; ``amends`` and
  ``retracts`` — from an ADR status paragraph). There are **no inferred
  edges**: where no source records a relationship, the graph stays silent.
  In particular, ``blocks`` keeps the ledger's own direction — ``C2 blocks
  G3`` names the gap whose completion would resolve C2 (see
  ``frontier._downstream``) — rather than a prettier paraphrase.
* **Both endpoints must resolve.** An edge is emitted only when ``src`` and
  ``dst`` are ids in the claim catalogue (or ``SYM:`` ids from the symbol
  records). Everything else lands in the dangling report instead of becoming
  an invented node.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from . import claims as claims_mod
from . import ledger as ledger_mod
from . import literature as literature_mod
from .claims import ADR_REF, LEDGER_ID
from .invariants import SUITES

ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / "index" / "graph.jsonl"

CURATED_TYPES = frozenset(
    {
        "blocks",  # contradictions.yaml: the gap whose completion resolves this
        "resolves",  # gaps.yaml
        "unblocks",  # gaps.yaml
        "depends_on",  # gaps.yaml
        "contradictions",  # governing_register.yaml
        "gaps",  # governing_register.yaml
        "supported_by",  # gaps.yaml unifying_candidates (id-shaped entries only)
        "claims",  # symbols.yaml
        "code_names",  # symbols.yaml
        "bears_on",  # literature/index.yaml
        "formalizes",  # theorems.yaml
        "promotes",  # theorems.yaml: the T1/T2 check a theorem lifts to T0
    }
)
DERIVED_TYPES = frozenset({"cites", "mentions", "amends", "retracts"})
TYPES = CURATED_TYPES | DERIVED_TYPES


@dataclass(frozen=True, order=True)
class Edge:
    src: str
    dst: str
    type: str
    #: "curated" (read from a field someone wrote) or "derived" (parsed out of
    #: free text this repository also wrote). Extraction mechanics, not truth.
    how: str
    #: The file (and where useful the line) the edge was read from.
    source: str


@dataclass
class Graph:
    edges: list[Edge]
    #: (unresolved id, "src -> dst", source) for every reference that resolved
    #: to no catalogue record. Empty in a sound tree; a test pins that.
    dangling: list[tuple[str, str, str]]


def _adr_id(text: str) -> str | None:
    m = ADR_REF.search(str(text))
    return f"ADR:{m.group(1)}" if m else None


def build(
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
) -> Graph:
    catalogue = catalogue if catalogue is not None else claims_mod.collect()
    symbols = symbols if symbols is not None else claims_mod.load_symbols()
    nodes = {c.id for c in catalogue} | {f"SYM:{s['id']}" for s in symbols}

    edges: set[Edge] = set()
    dangling: list[tuple[str, str, str]] = []

    def add(src: str, dst: str, type_: str, how: str, source: str) -> None:
        if src in nodes and dst in nodes:
            edges.add(Edge(src, dst, type_, how, source))
        else:
            for ref in (src, dst):
                if ref not in nodes:
                    dangling.append((ref, f"{src} -> {dst}", source))

    led = ledger_mod.load()
    for entry in led.contradictions:
        for gap in entry.get("blocks", []):
            add(entry["id"], gap, "blocks", "curated", "ledger/contradictions.yaml")
    for entry in led.gaps:
        for target in entry.get("resolves", []):
            add(entry["id"], target, "resolves", "curated", "ledger/gaps.yaml")
        for target in entry.get("unblocks", []):
            add(entry["id"], target, "unblocks", "curated", "ledger/gaps.yaml")
        for target in entry.get("depends_on", []):
            add(entry["id"], target, "depends_on", "curated", "ledger/gaps.yaml")
    for entry in led.register:
        for target in entry["contradictions"]:
            add(entry["id"], target, "contradictions", "curated", "ledger/governing_register.yaml")
        for target in entry["gaps"]:
            add(entry["id"], target, "gaps", "curated", "ledger/governing_register.yaml")
    for entry in led.unifying_candidates:
        # supported_by mixes id spaces: bare ledger ids, "ADR NNNN", and corpus
        # section strings. Only the first two are nodes; sections stay visible
        # in the claim record's `related` list.
        for ref in entry.get("supported_by", []):
            ref = str(ref)
            if LEDGER_ID.fullmatch(ref):
                add(entry["id"], ref, "supported_by", "curated", "ledger/gaps.yaml")
            elif adr := _adr_id(ref):
                add(entry["id"], adr, "supported_by", "curated", "ledger/gaps.yaml")

    for symbol in symbols:
        sid = f"SYM:{symbol['id']}"
        for target in symbol.get("claims", []):
            add(sid, target, "claims", "curated", "ledger/symbols.yaml")
        for name in symbol.get("code_names", []):
            # Lowercase code names are functions, not registry constants; they
            # have no catalogue record to point at.
            if name.isupper():
                add(sid, f"CONST:{name}", "code_names", "curated", "ledger/symbols.yaml")

    for paper in literature_mod.load().papers:
        for edge in paper.get("bears_on", []):
            target = edge["target"]
            dst = target if LEDGER_ID.fullmatch(target) else f"CONST:{target}"
            add(f"LIT:{paper['id']}:{target}", dst, "bears_on", "curated", "literature/index.yaml")

    # Checks cite claims only inside free text: the section string, the check
    # name, or the suite name ("tier collapse (G14)"). Parse all three. Static
    # registration data only — nothing here runs a check.
    for suite in SUITES:
        for name, section, _tier, fn in suite.checks:
            chk = claims_mod.check_id(suite.name, name)
            where = f"src/workhouse/invariants.py:{fn.__code__.co_firstlineno}"
            text = f"{name} | {section} | {suite.name}"
            for target in set(LEDGER_ID.findall(text)):
                add(chk, target, "cites", "derived", where)
            for number in set(ADR_REF.findall(text)):
                add(chk, f"ADR:{number}", "cites", "derived", where)

    for adr in claims_mod.decisions():
        for target in adr["mentions"]:
            add(adr["id"], target, "mentions", "derived", adr["where"])
        for target in adr["amends"]:
            add(adr["id"], target, "amends", "derived", adr["where"])
        for target in adr["retracts"]:
            add(adr["id"], target, "retracts", "derived", adr["where"])

    chk_ids: dict[str, list[str]] = {}
    for suite in SUITES:
        for name, _section, _tier, _fn in suite.checks:
            chk_ids.setdefault(name, []).append(claims_mod.check_id(suite.name, name))
    for theorem in claims_mod.load_theorems():
        tid = f"LEAN:{theorem['name']}"
        for target in theorem.get("formalizes", []):
            add(tid, target, "formalizes", "curated", "ledger/theorems.yaml")
        for check_name in theorem.get("promotes", []):
            for chk in chk_ids.get(check_name, [f"CHK:?{check_name}"]):
                add(tid, chk, "promotes", "curated", "ledger/theorems.yaml")

    return Graph(edges=sorted(edges), dangling=sorted(dangling))


def validate(graph: Graph | None = None) -> list[str]:
    """Structural problems, in the ledger.validate() style. Empty means sound."""
    graph = graph or build()
    problems = []
    for edge in graph.edges:
        if edge.type not in TYPES:
            problems.append(f"unknown edge type {edge.type!r} on {edge.src} -> {edge.dst}")
        if edge.how not in ("curated", "derived"):
            problems.append(f"unknown provenance {edge.how!r} on {edge.src} -> {edge.dst}")
    for ref, context, source in graph.dangling:
        problems.append(f"unresolved id {ref!r} in edge {context} ({source})")
    return problems


def render(graph: Graph | None = None) -> str:
    graph = graph or build()
    return "".join(json.dumps(asdict(e), sort_keys=True) + "\n" for e in graph.edges)


def write(path: Path | None = None) -> Path:
    target = path or GRAPH
    target.write_text(render())
    return target
