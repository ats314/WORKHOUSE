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
    sides = {
        c["id"]: [{"label": s["label"], "value": str(s["value"])} for s in c["sides"]]
        for c in led.contradictions
        if c.get("sides")
    }
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
        "edges": [{"s": e.src, "d": e.dst, "t": e.type, "h": e.how} for e in graph.edges],
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
    target.write_text(render(data), encoding="utf-8")
    return target
