"""``workhouse derive``: one claim's evidence chain as a readable export.

The 2026-08-28 agent experience notes measured the remaining mechanical cost
of a synthesis: the graph selects sources well, but ordering the neighborhood
into a derivation-shaped document was still done by hand. This module emits
that document — for one root or several (``derive C2 G3 --format md``).

The export is **non-inferential by construction**, which is the property the
notes asked to preserve:

* only registered edges appear; the traversal never invents a relationship,
  and where no edge exists the export stays silent about the pair;
* reachability is never presented as derivation — nodes are grouped by what
  they *are* (origin documents, constants, checks, theorems, papers), each
  annotated with the recorded edge that brought it in;
* a contradiction's sides are printed side by side, never merged or ranked;
* every check carries its live verdict and its reproduce command, so the
  document ends in runnable verification rather than in citations.
"""

from __future__ import annotations

from dataclasses import dataclass

from . import claims as claims_mod
from . import graph as graph_mod
from . import ledger as ledger_mod
from . import navigator as navigator_mod

#: Presentation order: evidence before the things that rest on it. This is a
#: reading order for humans, computed from each node's kind alone — it is NOT
#: a claim that earlier rows imply later ones.
_KIND_RANK = {
    "document": 0,
    "citation": 1,
    "constant": 2,
    "check": 3,
    "theorem": 4,
    "paper": 5,
    "decision": 6,
    "contradiction": 7,
    "gap": 7,
    "register": 7,
    "unifying": 7,
}
_KIND_TITLE = {
    0: "Originating documents",
    1: "Cited sources",
    2: "Registered constants",
    3: "Checks, with live verdicts",
    4: "Lean theorems (T0)",
    5: "Published work",
    6: "Decisions (ADRs)",
    7: "Related ledger claims",
    8: "Other records",
}
_MAX_DEPTH = 2


@dataclass
class Neighbor:
    id: str
    depth: int
    #: The registered edges (type, other endpoint, direction) that pulled this
    #: node into the chain — the export's provenance for including it.
    via: list[str]


def _walk(
    root: str,
    graph: graph_mod.Graph,
    depth: int = _MAX_DEPTH,
    relations: frozenset[str] | None = None,
) -> dict[str, Neighbor]:
    """Breadth-first over registered edges, both directions, depth-capped.

    Deterministic: neighbors are visited in sorted order and each node keeps
    the sorted list of edges that reached it. Nothing about the walk implies
    logical dependency; it only bounds which recorded facts the export shows.
    ``relations`` restricts the walk to those edge types — a filter over what
    is shown, never a new inference: an edge outside the set is elided, not
    contradicted.
    """
    by_src: dict[str, list[graph_mod.Edge]] = {}
    by_dst: dict[str, list[graph_mod.Edge]] = {}
    for edge in graph.edges:
        if relations is not None and edge.type not in relations:
            continue
        by_src.setdefault(edge.src, []).append(edge)
        by_dst.setdefault(edge.dst, []).append(edge)

    out: dict[str, Neighbor] = {}
    frontier = [root]
    for d in range(1, depth + 1):
        nxt: list[str] = []
        for node in frontier:
            for edge in by_src.get(node, []):
                label = f"{node} —{edge.type}→ {edge.dst}"
                if edge.dst not in out and edge.dst != root:
                    out[edge.dst] = Neighbor(edge.dst, d, [])
                    nxt.append(edge.dst)
                if edge.dst != root:
                    out[edge.dst].via.append(label)
            for edge in by_dst.get(node, []):
                label = f"{edge.src} —{edge.type}→ {node}"
                if edge.src not in out and edge.src != root:
                    out[edge.src] = Neighbor(edge.src, d, [])
                    nxt.append(edge.src)
                if edge.src != root:
                    out[edge.src].via.append(label)
        frontier = sorted(set(nxt))
    for neighbor in out.values():
        neighbor.via = sorted(set(neighbor.via))
    return out


def data(
    roots: list[str],
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
    depth: int = _MAX_DEPTH,
    relations: frozenset[str] | None = None,
) -> tuple[dict, bool]:
    """The same chains as ``render``, as one JSON-ready object.

    Exists so an agent can consume a multi-root neighborhood without parsing
    Markdown. Nothing is included that ``render`` would not print, and the
    same non-inferential rules hold: registered edges only, ``via`` is each
    node's provenance for being here, and reachability is not derivation.
    """
    from dataclasses import asdict

    catalogue = catalogue if catalogue is not None else claims_mod.collect()
    symbols = symbols if symbols is not None else claims_mod.load_symbols()
    graph = graph if graph is not None else graph_mod.build(catalogue, symbols)
    by_id = {c.id: c for c in catalogue}
    sym_by_id = {f"SYM:{s['id']}": s for s in symbols}
    node_ids = set(by_id) | set(sym_by_id)

    ok = True
    out: dict = {"roots": {}, "depth": depth}
    if relations is not None:
        out["relations"] = sorted(relations)
    for query in roots:
        root = navigator_mod._resolve(query, node_ids)
        if root is None:
            out["roots"][query] = {"error": f"no record with id {query!r}"}
            ok = False
            continue
        record = asdict(by_id[root]) if root in by_id else sym_by_id[root]
        neighbors = {}
        for neighbor in _walk(root, graph, depth, relations).values():
            claim = by_id.get(neighbor.id)
            neighbors[neighbor.id] = {
                "depth": neighbor.depth,
                "via": neighbor.via,
                **(
                    {
                        "kind": claim.kind,
                        "statement": claim.statement,
                        "tier": claim.tier,
                        "status": claim.status,
                        "value": claim.value,
                        "reproduce": claim.reproduce,
                    }
                    if claim is not None
                    else {"kind": "symbol"}
                ),
            }
        out["roots"][root] = {"record": record, "neighbors": neighbors}
    return out, ok


def render(
    roots: list[str],
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
    depth: int = _MAX_DEPTH,
    relations: frozenset[str] | None = None,
) -> tuple[str, bool]:
    catalogue = catalogue if catalogue is not None else claims_mod.collect()
    symbols = symbols if symbols is not None else claims_mod.load_symbols()
    graph = graph if graph is not None else graph_mod.build(catalogue, symbols)
    by_id = {c.id: c for c in catalogue}
    sym_by_id = {f"SYM:{s['id']}": s for s in symbols}
    node_ids = set(by_id) | set(sym_by_id)
    led = ledger_mod.load()

    lines: list[str] = []
    w = lines.append
    ok = True

    w("# Evidence chains")
    w("")
    w("> Generated by `workhouse derive`. Only registered edges appear here;")
    w("> the absence of an edge means no relationship is recorded, and the")
    w("> ordering below is a reading order, not a proof. Statuses are computed")
    w("> at generation time. Nothing in this file is authored.")
    if relations is not None:
        w(f"> Restricted to edge types: {', '.join(sorted(relations))} — other")
        w("> recorded edges exist and are elided, not absent.")

    for query in roots:
        root = navigator_mod._resolve(query, node_ids)
        w("")
        if root is None:
            w(f"## {query} — no record with this id")
            ok = False
            continue

        if root in sym_by_id:
            symbol = sym_by_id[root]
            w(f"## {root} — {symbol['canonical']}")
            w("")
            w(" ".join(str(symbol.get("meaning", "")).split()))
        else:
            claim = by_id[root]
            w(f"## {root} — {claim.statement}")
            w("")
            standing = " · ".join(
                x
                for x in (
                    claim.kind,
                    f"T{claim.tier}" if claim.tier is not None else "",
                    claim.status,
                    claim.evidence,
                )
                if x
            )
            w(f"*{standing}*")
            if claim.value is not None:
                decimal = f"  (`{claim.decimal!r}`)" if claim.decimal is not None else ""
                w("")
                w(f"**Value:** `{claim.value}`{decimal}")

        entry = next((c for c in led.contradictions if c["id"] == root), None)
        if entry and entry.get("sides"):
            w("")
            w("### Both sides, neither promoted")
            w("")
            w("| branch | value | kind |")
            w("|---|---|---|")
            for side in entry["sides"]:
                w(f"| {side['label']} | `{side['value']}` | {side['kind']} |")
            if entry.get("delta") is not None:
                w("")
                w(f"Gap between them: `{entry['delta']}`.")
            for gap_id in entry.get("blocks", []):
                gap = next((g for g in led.gaps if g["id"] == gap_id), None)
                if gap:
                    w(f"Adjudication lives in {gap_id}: {gap['title']}.")

        neighbors = _walk(root, graph, depth, relations)
        by_rank: dict[int, list[Neighbor]] = {}
        for neighbor in neighbors.values():
            kind = by_id[neighbor.id].kind if neighbor.id in by_id else None
            rank = _KIND_RANK.get(kind, 8) if kind else 8
            by_rank.setdefault(rank, []).append(neighbor)

        for rank in sorted(by_rank):
            w("")
            w(f"### {_KIND_TITLE[rank]}")
            w("")
            for neighbor in sorted(by_rank[rank], key=lambda n: (n.depth, n.id)):
                claim = by_id.get(neighbor.id)
                if claim is None:
                    meaning = sym_by_id.get(neighbor.id, {}).get("meaning", "")
                    w(f"- **{neighbor.id}** — {' '.join(str(meaning).split())}")
                else:
                    verdict = ""
                    if claim.kind == "check":
                        verdict = " — **PASS**" if claim.status == "passing" else " — **FAIL**"
                    tier = f" (T{claim.tier})" if claim.tier is not None else ""
                    statement = " ".join(claim.statement.split())
                    # A citation alias's statement IS the alias ("GCSG"), which
                    # tells a reader nothing; its curated note does. Same for
                    # any node whose statement is only its own id tail.
                    if claim.detail and statement == neighbor.id.split(":", 1)[-1]:
                        statement = f"{statement} — {' '.join(claim.detail.split())}"
                    w(f"- **{neighbor.id}**{tier}{verdict} — {statement}")
                    if claim.value is not None:
                        w(f"  - value: `{claim.value}`")
                    if claim.kind == "check" and claim.reproduce:
                        w(f"  - reproduce: `{claim.reproduce}`")
                for label in neighbor.via[:4]:
                    w(f"  - edge: `{label}`")
                if len(neighbor.via) > 4:
                    w(f"  - … {len(neighbor.via) - 4} more recorded edges")

        if not neighbors:
            w("")
            w("No recorded edges. If a relationship exists, its home is a curated")
            w("field: `ledger/*.yaml`, `ledger/theorems.yaml`, `literature/index.yaml`.")

    w("")
    return "\n".join(lines), ok
