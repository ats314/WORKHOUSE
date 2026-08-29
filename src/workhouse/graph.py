"""Every relationship this repository records, as one generated edge list.

The entities already have machine-readable records — ``index/claims.jsonl``
plus the symbols in ``index/symbols.jsonl`` — but the relationships between
them were siloed in seven formats: ledger edge fields, the symbol records'
``claims``/``code_names`` lists, free-text section strings on checks,
literature ``bears_on`` edges, ADR prose, the notes register's review
verdicts, and (until ``ledger/theorems.yaml``) nothing at all for the Lean
layer. ``ledger/provenance.yaml`` extends the
reach into the corpus itself: pinned originating documents, with
``originates`` edges to the claims their values come from, and
``ledger/notes.yaml`` plus ``notes/*.jsonl`` extend it into the maintainer's
own archives -- every inventoried document, the archive that contains it, what
its review says it bears on, and which registered coefficients its bytes
carry. This module reads each of those sources and emits
``index/graph.jsonl``: one JSON record per edge,
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

import inspect
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from . import claims as claims_mod
from . import ledger as ledger_mod
from . import literature as literature_mod
from . import notes as notes_mod
from . import oeis as oeis_mod
from . import triage as triage_mod
from .claims import ADR_REF, LEDGER_ID
from .invariants import SUITES, source_path

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
        "cites",  # literature/index.yaml: the curated citation web, LIT -> LIT
        "formalizes",  # theorems.yaml
        "promotes",  # theorems.yaml: the T1/T2 check a theorem lifts to T0
        "originates",  # provenance.yaml: the corpus document a value comes from
        "uses",  # a check body reads a registered constant (K.NAME)
        "contains",  # notes.yaml: the archive a note document was inventoried in
        "evidences",  # runs/index.yaml: a pinned run record bears on a ledger item
        "matches",  # sequences.yaml: an OEIS entry containing a registered sequence
        "duplicate_of",  # notes.yaml reviews
        "superseded_by",  # notes.yaml reviews
    }
)
#: "cites" appears on both sides deliberately: the DERIVED kind is an id
#: parsed out of a check's free text (CHK -> ledger id), the CURATED kind is
#: the verbatim ``cites`` field of literature/index.yaml (LIT -> LIT). The
#: ``how`` field on each edge keeps them distinguishable.
DERIVED_TYPES = frozenset({"cites", "mentions", "amends", "retracts", "uses", "carries"})
TYPES = CURATED_TYPES | DERIVED_TYPES


#: Where the sequence edges come from, named once so the edge's `source` field
#: and the register cannot drift apart.
SEQ_SOURCE = "ledger/sequences.yaml"


def resolve_target(target: str) -> str:
    """A curated cross-reference as a catalogue node id.

    An already-namespaced id (anything containing a colon) passes through, a
    ledger id stands for itself, and a bare name is a registered constant.

    One rule for every register. The inline version this replaces coerced any
    non-ledger target to ``CONST:``, which would have turned a namespaced
    ``LEAN:foo`` into ``CONST:LEAN:foo`` and dangled it -- harmless only for as
    long as no curated file names one, which is not a property anybody was
    maintaining on purpose.
    """
    if ":" in target:
        return target
    if LEDGER_ID.fullmatch(target):
        return target
    return f"CONST:{target}"


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


def _module_helpers() -> dict[str, str]:
    """Module-level helpers across the invariant package, comments stripped.

    Not every constant a check reads appears in the check's own body. Several
    checks delegate to a module-level helper -- ``_sealed_gaps``,
    ``_bridge_towers`` and friends -- and the constants those helpers read were
    invisible to the ``uses`` scan, which left registered constants orphaned in
    the graph while a check demonstrably rested on them.

    Every submodule is walked, not just the package root. When ``invariants``
    was one file this was a single ``vars()`` sweep; after the split a helper
    lives beside the suite that uses it, so scanning only the package would
    have found none of them -- reintroducing precisely the orphaned-constant
    bug this function exists to prevent.
    """
    import importlib
    import inspect as _inspect
    import pkgutil

    from . import invariants as package

    modules = [package]
    for info in pkgutil.iter_modules(package.__path__):
        modules.append(importlib.import_module(f"{package.__name__}.{info.name}"))

    out: dict[str, str] = {}
    for module in modules:
        for name, obj in vars(module).items():
            # The checks themselves are all named `_` and are reached through
            # the suites, never by name; only named helpers are call targets.
            if name == "_" or not callable(obj) or not hasattr(obj, "__code__"):
                continue
            if getattr(obj, "__module__", None) != module.__name__:
                continue
            try:
                out[name] = re.sub(r"#[^\n]*", "", _inspect.getsource(obj))
            except OSError:  # pragma: no cover - source always available in-tree
                continue
    return out


def _with_helper_bodies(body: str, helpers: dict[str, str]) -> str:
    """A check's body plus the bodies of every module helper it reaches.

    Transitive, because helpers call helpers. Still computed and still honest:
    this is the source that actually runs when the check runs, so a constant
    found here IS read by the check. Comments are stripped throughout, for the
    same reason the Lean counters strip them -- a name in a comment is not a
    use.
    """
    body = re.sub(r"#[^\n]*", "", body)
    seen: set[str] = set()
    frontier = [body]
    collected = [body]
    while frontier:
        current = frontier.pop()
        for call in set(re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(", current)):
            if call in helpers and call not in seen:
                seen.add(call)
                collected.append(helpers[call])
                frontier.append(helpers[call])
    return "\n".join(collected)


def _coefficient_targets(catalogue: list[claims_mod.Claim]) -> dict[str, tuple[str, ...]]:
    """Coefficient name -> the catalogue constants whose digits it matches.

    ``triage.SIGNATURES`` stores each coefficient as the digit strings of its
    exact numerator and denominator (or, for the float-only ones, of its
    decimal). A constant whose own value contains every one of those digit
    groups is carrying that coefficient. This is the same value-first join the
    rest of the repository uses -- the exact rationals are the keys, not the
    names -- so the edge survives a document spelling a quantity differently
    from the registry.
    """

    def digits(value: object) -> str:
        return "".join(ch for ch in str(value) if ch.isdigit())

    constants = [c for c in catalogue if c.id.startswith("CONST:")]
    haystacks = {
        c.id: digits(c.value or "") + "|" + (digits(c.decimal) if c.decimal is not None else "")
        for c in constants
    }
    out: dict[str, tuple[str, ...]] = {}
    for name, signature in triage_mod.SIGNATURES.items():
        wanted = [group for part in signature for group in part]
        out[name] = tuple(
            sorted(cid for cid, hay in haystacks.items() if all(w in hay for w in wanted))
        )
    return out


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

    # The run register: evidences edges from each pinned run record to the
    # ledger items its entry names. Curated in runs/index.yaml; an edge says
    # "this executed run is evidence someone weighing that item should read",
    # and promotes nothing.
    for run in claims_mod.load_runs():
        for target in run.get("bears_on", []):
            add(f"RUN:{run['id']}", target, "evidences", "curated", "runs/index.yaml")

    # The sequence register. `bears_on` reads the register's own field name, so
    # the edge type is that field verbatim (ADR 0007). Targets are resolved
    # explicitly rather than by the literature module's `CONST:` coercion:
    # that coercion assumes every non-ledger target is a bare constant name and
    # would turn an already-namespaced id into `CONST:LEAN:...`, which dangles.
    for seq in oeis_mod.load():
        for target in seq.bears_on:
            add(f"SEQ:{seq.id}", resolve_target(target), "bears_on", "curated", SEQ_SOURCE)
        for aid in sorted((seq.scan or {}).get("hits", ())):
            add(f"OEIS:{aid}", f"SEQ:{seq.id}", "matches", "curated", SEQ_SOURCE)

    lit = literature_mod.load()
    for paper in lit.papers:
        for edge in paper.get("bears_on", []):
            target = edge["target"]
            add(
                f"LIT:{paper['id']}:{target}",
                resolve_target(target),
                "bears_on",
                "curated",
                "literature/index.yaml",
            )
    # The citation web: curated per-paper cites lists, emitted between the
    # paper-level LIT nodes. Bibliography, not endorsement — these edges can
    # rank and connect papers and can promote nothing.
    for src, dst in lit.cites():
        add(f"LIT:{src}", f"LIT:{dst}", "cites", "curated", "literature/index.yaml")

    # The notes archives. `contains` is the archive a document was inventoried
    # in; `bears_on`, `duplicate_of` and `superseded_by` are the verbatim
    # review fields. `carries` is the one derived edge here, and it is derived
    # by VALUE: triage records which coefficient signatures a document's bytes
    # contain, and a signature is the digit string of a registry constant's own
    # exact numerator and denominator. Matching those digits against the
    # catalogue's values links a document to a constant it demonstrably
    # carries, rather than to one a name map here decided it was about. No
    # edge promotes anything -- every note node is T3 whatever its verdict.
    notes = notes_mod.load()
    reviews = {r["digest"]: r for r in notes.reviews}
    note_ids = {
        (archive["id"], row["digest"]): claims_mod.note_id(archive["id"], row)
        for archive in notes.archives
        for row in notes.manifests.get(archive["id"], [])
    }
    signature_targets = _coefficient_targets(catalogue)
    for archive in notes.archives:
        aid = archive["id"]
        for row in notes.manifests.get(aid, []):
            nid = note_ids[(aid, row["digest"])]
            add(f"ARCHIVE:{aid}", nid, "contains", "curated", f"notes/{aid}.jsonl")
            for name in row.get("coefficients") or []:
                for target in signature_targets.get(name, ()):
                    add(nid, target, "carries", "derived", f"notes/{aid}.jsonl")
            review = reviews.get(row["digest"])
            if not review:
                continue
            for target in review.get("bears_on", []):
                # Same id-space rule the literature edges use: a bears_on
                # target is either a ledger id (C2, G14) or a bare constant
                # name, which is a CONST record.
                add(nid, resolve_target(target), "bears_on", "curated", "ledger/notes.yaml")
            for field_, type_ in (
                ("duplicate_of", "duplicate_of"),
                ("superseded_by", "superseded_by"),
            ):
                other = review.get(field_)
                if other and (aid, other) in note_ids:
                    add(nid, note_ids[(aid, other)], type_, "curated", "ledger/notes.yaml")

    # Checks cite claims only inside free text: the section string, the check
    # name, or the suite name ("tier collapse (G14)"). Parse all three. Static
    # registration data only — nothing here runs a check.
    for suite in SUITES:
        for name, section, _tier, fn in suite.checks:
            chk = claims_mod.check_id(suite.name, name)
            where = source_path(fn)
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

    for doc in claims_mod.load_provenance():
        for origin in doc["originates"]:
            add(
                f"DOC:{doc['id']}",
                origin["target"],
                "originates",
                "curated",
                "ledger/provenance.yaml",
            )

    # A check that reads a registered constant depends on it. The graph had no
    # such edge, so 85 registered constants sat in the catalogue unreachable
    # from any claim that uses them -- and `why CONST:B_3` could not answer
    # "which checks rest on this?". The check body is the honest source: a
    # constant referenced as K.NAME is used, and one that only appears in a
    # comment is not (comments are stripped first, for the same reason the Lean
    # counters strip them).
    known_constants = {c.id for c in catalogue if c.kind == "constant"}
    helpers = _module_helpers()
    for suite in SUITES:
        for name, _section, _tier, fn in suite.checks:
            try:
                body = inspect.getsource(fn)
            except OSError:  # pragma: no cover - source always available in-tree
                continue
            body = _with_helper_bodies(body, helpers)
            for const in sorted(set(re.findall(r"\bK\.([A-Z][A-Z0-9_]*)\b", body))):
                if f"CONST:{const}" in known_constants:
                    add(
                        claims_mod.check_id(suite.name, name),
                        f"CONST:{const}",
                        "uses",
                        "derived",
                        source_path(fn),
                    )

    # Every check cites its source by alias; the alias is now a node, so the
    # citation becomes an edge. Matched on a word boundary so PAPER_FLATBAND
    # does not also fire the PAPER alias it contains -- the two are different
    # documents, and a substring match would point readers at the wrong one.
    aliases = [a for a in claims_mod.load_document_aliases() if not a.get("unresolved")]
    for suite in SUITES:
        for name, section, _tier, fn in suite.checks:
            if not section:
                continue
            for alias in aliases:
                token = re.escape(alias["alias"])
                if re.search(rf"(?<![A-Za-z0-9_.]){token}(?![A-Za-z0-9_.])", section):
                    add(
                        claims_mod.check_id(suite.name, name),
                        f"CITE:{alias['alias']}",
                        "cites",
                        "derived",
                        source_path(fn),
                    )

    # A check that compares against a published result cites the paper by its
    # literature id ("HAMER_1989", "SCHIERHOLZ_1988"), and those ids are
    # already LIT: nodes. Until this resolved them, the published-comparisons
    # suite -- the whole external-corroboration layer -- sat orphaned in the
    # graph, so "which checks rest on Hamer?" had no answer. Same word-boundary
    # rule as the aliases above, and the same derivation: an id parsed out of
    # the check's own registered section string.
    paper_ids = {c.id[len("LIT:") :] for c in catalogue if c.id.startswith("LIT:")}
    for suite in SUITES:
        for name, section, _tier, fn in suite.checks:
            if not section:
                continue
            for paper in sorted(paper_ids):
                if ":" in paper:  # the per-edge LIT:<paper>:<target> records
                    continue
                token = re.escape(paper)
                if re.search(rf"(?<![A-Za-z0-9_.]){token}(?![A-Za-z0-9_.])", section):
                    add(
                        claims_mod.check_id(suite.name, name),
                        f"LIT:{paper}",
                        "cites",
                        "derived",
                        source_path(fn),
                    )

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
    target.write_text(render(), encoding="utf-8", newline="\n")
    return target
