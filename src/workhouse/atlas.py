"""The theory graph as one self-contained HTML page.

``workhouse atlas`` renders the live catalogue — the same records the
staleness tests pin in ``index/`` — into a single file with no external
dependencies: a force-directed map of every connected record, and a detail
panel that is ``workhouse why`` for the mouse. The output is a **view, not a
record**: it is regenerated on demand and never checked in, so it cannot
drift and silently read as current the way a stale committed page would.

The same honesty rules as the graph apply. Only records with at least one
recorded edge are drawn; the disputed C2 carries both sides and a marker,
never a preference; unifying candidates carry their falsifier. Nothing in the
page is authored at render time — every string is copied from a catalogue
record or a ledger field.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from . import claims as claims_mod
from . import graph as graph_mod
from . import ledger as ledger_mod

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = Path(__file__).with_name("atlas_template.html")
DEFAULT_OUT = ROOT / "atlas.html"
MARKER = "/*__DATA__*/"


def _clip(text: Any, width: int) -> str:
    text = " ".join(str(text or "").split())
    return text if len(text) <= width else text[: width - 1] + "…"


def _claim_ref(claim: claims_mod.Claim) -> dict[str, Any]:
    """The source-authored fields needed to inspect one branch candidate."""
    return {
        "id": claim.id,
        "kind": claim.kind,
        "statement": _clip(claim.statement, 200),
        "tier": claim.tier,
        "status": _clip(claim.status, 80),
        "evidence": claim.evidence or "",
        "where": claim.where or "",
        "reproduce": claim.reproduce or "",
    }


def collect_data(
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
) -> dict[str, Any]:
    catalogue = catalogue if catalogue is not None else claims_mod.collect()
    symbols = symbols if symbols is not None else claims_mod.load_symbols()
    graph = graph if graph is not None else graph_mod.build(catalogue, symbols)

    connected = {e.src for e in graph.edges} | {e.dst for e in graph.edges}
    led = ledger_mod.load()
    by_value: dict[str, list[claims_mod.Claim]] = defaultdict(list)
    for claim in catalogue:
        if claim.kind == "constant" and claim.value is not None:
            by_value[str(claim.value)].append(claim)
    originators: dict[str, set[str]] = defaultdict(set)
    for edge in graph.edges:
        if edge.type == "originates":
            originators[edge.dst].add(edge.src)

    sides: dict[str, list[dict[str, Any]]] = {}
    for contradiction in led.contradictions:
        if not contradiction.get("sides"):
            continue
        records = []
        for side in contradiction["sides"]:
            value = str(side["value"])
            matches = [_claim_ref(claim) for claim in by_value.get(value, [])]
            records.append(
                {
                    "label": side["label"],
                    "value": value,
                    "kind": side.get("kind", ""),
                    "matches": matches,
                    "originators": sorted(
                        {doc for match in matches for doc in originators.get(match["id"], set())}
                    ),
                }
            )
        sides[contradiction["id"]] = records
    delta = {c["id"]: str(c["delta"]) for c in led.contradictions if c.get("delta") is not None}
    falsifier = {u["id"]: _clip(u["falsifier"], 400) for u in led.unifying_candidates}

    nodes: list[dict[str, Any]] = []
    for c in catalogue:
        if c.id not in connected:
            continue
        node: dict[str, Any] = {
            "id": c.id,
            "kind": c.kind,
            "statement": _clip(c.statement, 200),
            "tier": c.tier,
            "status": _clip(c.status, 80),
            "evidence": c.evidence or "",
            "value": _clip(c.value, 80) if c.value is not None else None,
            "where": c.where or "",
            "cites": _clip(c.cites, 300),
            # A result's final support boundary must remain visible even
            # when its hypotheses are longer than the ordinary preview.
            "detail": c.detail if c.kind == "result" else _clip(c.detail, 1200),
            "reproduce": c.reproduce or "",
        }
        if c.id in sides:
            node["sides"] = sides[c.id]
        if c.id in delta:
            node["delta"] = delta[c.id]
        if c.id in falsifier:
            node["falsifier"] = falsifier[c.id]
        nodes.append(node)
    for s in symbols:
        sid = f"SYM:{s['id']}"
        if sid not in connected:
            continue
        node = {
            "id": sid,
            "kind": "symbol",
            "statement": _clip(s.get("meaning", ""), 200),
            "tier": None,
            "status": "",
            "evidence": "",
            "value": _clip(", ".join(s.get("values", [])), 80) or None,
            "where": "ledger/symbols.yaml",
            "reproduce": f"workhouse search {s.get('canonical', s['id'])}",
        }
        if s.get("coined_here"):
            node["coined"] = True
        nodes.append(node)

    return {
        "nodes": nodes,
        "edges": [
            {"s": e.src, "d": e.dst, "t": e.type, "h": e.how, "p": e.source} for e in graph.edges
        ],
    }


def render(data: dict[str, Any] | None = None) -> str:
    data = data if data is not None else collect_data()
    payload = json.dumps(data, sort_keys=True, separators=(",", ":"))
    template = TEMPLATE.read_text(encoding="utf-8")
    if MARKER not in template:
        raise ValueError(f"atlas template lacks the {MARKER} marker")
    return template.replace(MARKER, payload)


def write(path: Path | None = None, data: dict[str, Any] | None = None) -> Path:
    target = path or DEFAULT_OUT
    target.write_text(render(data), encoding="utf-8", newline="\n")
    return target
