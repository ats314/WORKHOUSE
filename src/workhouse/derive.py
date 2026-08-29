"""``workhouse derive``: a claim's recorded support, dependency-ordered.

The agent memo's Observation 13: the graph made source *selection* fast, but
producing a readable theorem chain still meant manually ordering nodes and
rewriting formulas from the controlling sources. This module does the ordering
and the transcription; it does not do the mathematics.

Two rules, inherited from ``graph.py`` and tightened for this use:

* **Reachability is not entailment.** Every line below is one registered edge
  between two records. Walking from a claim to a document does not make the
  document a premise, and this export never says it does -- it says which edge
  it walked and which file that edge was read from.
* **Missing links are printed, not skipped.** A derivation that silently omits
  the step it could not find reads exactly like one that has no gap. Where a
  node has no recorded support, this says so under *Not established*.

The support direction of each relation is declared in ``SUPPORTS`` rather than
guessed per call, because "A supports B" and "A points at B" are different
questions and the ledgers answer only the second.
"""

from __future__ import annotations

from . import claims as claims_mod
from . import graph as graph_mod
from . import ledger as ledger_mod
from . import navigator as navigator_mod
from . import render as render_mod

#: Relation -> which endpoint is the *supporting* record. "src" means the edge
#: ``A -type-> B`` records A as support for B; "dst" means the reverse. Curated
#: here, one line per relation, because inverting one of these silently turns a
#: derivation upside down and no test of the arithmetic would catch it.
SUPPORTS = {
    "originates": "src",  # provenance.yaml: this document states the value
    "bears_on": "src",  # a paper bears on the claim
    "cites": "src",  # a check's registered name cites the ledger id
    "formalizes": "src",  # theorems.yaml: the Lean theorem formalizes the check
    "promotes": "src",  # theorems.yaml: the T1/T2 check a theorem lifts to T0
    "evidences": "src",  # runs/index.yaml: a pinned run bears on the item
    "resolves": "src",  # gaps.yaml: completing this gap resolves that item
    "supported_by": "dst",  # unifying candidates name their support
    "uses": "dst",  # a check body reads this registered constant
    "depends_on": "dst",  # gaps.yaml: this gap sits behind that one
    "claims": "dst",  # symbols.yaml: the claims a symbol carries
    "code_names": "dst",
    "contains": "src",  # notes.yaml: the archive a document was inventoried in
}


def _support_edges(graph: graph_mod.Graph) -> dict[str, list[graph_mod.Edge]]:
    """node -> the edges recording something that supports it."""
    out: dict[str, list[graph_mod.Edge]] = {}
    for edge in graph.edges:
        side = SUPPORTS.get(edge.type)
        if side is None:
            continue
        supported = edge.dst if side == "src" else edge.src
        supporter = edge.src if side == "src" else edge.dst
        if supporter == supported:
            continue  # a self-edge supports nothing
        out.setdefault(supported, []).append(edge)
    for edges in out.values():
        edges.sort()
    return out


def collect(
    roots: list[str],
    depth: int = 2,
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
    mode: str = "live",
) -> dict:
    """Gather each root's support closure and order it by distance from the root.

    Ordering is by hop distance, then by id: deterministic, and honest about
    what it is. It is *not* a proof order -- nothing here knows which lemma
    comes first in an argument, and pretending otherwise is precisely the
    inference this repository forbids.
    """
    catalogue, symbols, graph = navigator_mod.load_context(mode, catalogue, symbols, graph)
    by_id = {c.id: c for c in catalogue}
    sym_by_id = {f"SYM:{s['id']}": s for s in symbols}
    node_ids = set(by_id) | set(sym_by_id)
    supports = _support_edges(graph)
    led = ledger_mod.load()
    provenance = navigator_mod.provenance_targets()

    resolved: list[str] = []
    unresolved: list[str] = []
    for root in roots:
        node = navigator_mod._resolve(root, node_ids)
        (resolved if node else unresolved).append(node or root)

    sections = []
    for root in resolved:
        layers: dict[int, list[graph_mod.Edge]] = {}
        seen = {root}
        frontier = [root]
        for hop in range(1, max(1, depth) + 1):
            following: list[str] = []
            for node in frontier:
                for edge in supports.get(node, ()):
                    side = SUPPORTS[edge.type]
                    supporter = edge.src if side == "src" else edge.dst
                    layers.setdefault(hop, []).append(edge)
                    if supporter not in seen:
                        seen.add(supporter)
                        following.append(supporter)
            frontier = sorted(set(following))
            if not frontier:
                break

        claim = by_id.get(root)
        incident = [e for e in graph.edges if root in (e.src, e.dst)]
        contradiction = next((c for c in led.contradictions if c["id"] == root), None)
        gap = next((g for g in led.gaps if g["id"] == root), None)
        open_behind = sorted(set(gap.get("depends_on", [])) & led.open_gap_ids) if gap else []
        sections.append(
            {
                "id": root,
                "record": (
                    {"kind": "symbol", **sym_by_id[root]}
                    if root in sym_by_id
                    else {
                        "kind": claim.kind,
                        "statement": claim.statement,
                        "tier": claim.tier,
                        "status": claim.status,
                        "evidence": claim.evidence,
                        "value": claim.value,
                        "decimal": claim.decimal,
                        "where": claim.where,
                        "detail": claim.detail,
                    }
                ),
                "replay": navigator_mod.replay_status(claim, incident),
                "layers": {
                    str(hop): [
                        {
                            "supporter": (e.src if SUPPORTS[e.type] == "src" else e.dst),
                            "supports": (e.dst if SUPPORTS[e.type] == "src" else e.src),
                            "relation": e.type,
                            "how": e.how,
                            "source": e.source,
                            "statement": _statement(by_id, sym_by_id, e, SUPPORTS[e.type]),
                        }
                        for e in sorted(set(edges))
                    ]
                    for hop, edges in sorted(layers.items())
                },
                "contradiction": contradiction,
                "gap": gap,
                "blocked_behind": open_behind,
                "evidence": provenance.get(root, []),
                "next_actions": navigator_mod.next_actions(root, by_id, incident),
                "unsupported": root not in supports,
            }
        )
    return {
        "schema": render_mod.SCHEMA,
        "command": "derive",
        "mode": mode,
        "roots": roots,
        "unresolved": unresolved,
        "depth": depth,
        "sections": sections,
    }


def _statement(by_id, sym_by_id, edge: graph_mod.Edge, side: str) -> str:
    node = edge.src if side == "src" else edge.dst
    if node in by_id:
        return by_id[node].statement
    if node in sym_by_id:
        return str(sym_by_id[node].get("meaning", ""))
    return ""


def render_markdown(data: dict) -> str:
    """The export a reader can paste into a manuscript, with its pins intact."""
    lines: list[str] = []
    w = lines.append
    w(f"# Recorded support for {', '.join(data['roots'])}")
    w("")
    w(
        f"Generated by `workhouse derive` in **{data['mode']}** mode, "
        f"depth {data['depth']}. Every row below is one edge recorded in a file "
        "named beside it. Reachability is not entailment: this is what the "
        "repository records, not a proof."
    )
    if data["unresolved"]:
        w("")
        w(f"**Unresolved ids:** {', '.join(data['unresolved'])} — nothing is recorded under these.")

    for section in data["sections"]:
        record = section["record"]
        w("")
        w(f"## {section['id']} — {record.get('statement') or record.get('canonical', '')}")
        w("")
        standing = [
            x
            for x in (
                record.get("kind"),
                None if record.get("tier") is None else f"T{record['tier']}",
                record.get("status"),
                record.get("evidence"),
            )
            if x
        ]
        w(f"*{' · '.join(standing)}*" if standing else "")
        if section.get("replay"):
            w("")
            w(f"Replay status: **{section['replay']}** — {navigator_mod.REPLAY[section['replay']]}")
        if record.get("value"):
            w("")
            w(f"Value: `{record['value']}`")

        if section["contradiction"] and section["contradiction"].get("sides"):
            w("")
            w("### Both sides, neither promoted")
            w("")
            w("| side | value | kind |")
            w("|---|---|---|")
            for side in section["contradiction"]["sides"]:
                w(f"| {side['label']} | `{side['value']}` | {side['kind']} |")
            if section["contradiction"].get("delta") is not None:
                w("")
                w(f"Gap between them: `{section['contradiction']['delta']}`")

        if section["layers"]:
            w("")
            w("### What it rests on, by distance")
            for hop in sorted(section["layers"], key=int):
                w("")
                w(f"**{hop} hop{'s' if hop != '1' else ''} out**")
                w("")
                w("| supporting record | relation | statement | recorded in |")
                w("|---|---|---|---|")
                for row in section["layers"][hop]:
                    statement = navigator_mod._clip(row["statement"], 70).replace("|", "\\|")
                    w(
                        f"| `{row['supporter']}` | {row['relation']} | {statement} "
                        f"| `{row['source']}` |"
                    )
        else:
            w("")
            w("### Not established here")
            w("")
            w(
                "No record supports this one. That is a statement about the "
                "repository, not about the mathematics: if a relationship "
                "exists, its home is a curated field in `ledger/`, "
                "`ledger/theorems.yaml`, or `literature/index.yaml`."
            )

        if section["blocked_behind"]:
            w("")
            w(f"### Blocked behind\n\n{', '.join(section['blocked_behind'])}")

        if section["evidence"]:
            w("")
            w("### Originating documents")
            w("")
            for row in section["evidence"]:
                w(f"- **{row['document']}** ({row['role']}) — `{row['path']}`")
                w(f"  - `sha256 {row['sha256']}`")
                if row.get("what"):
                    w(f"  - {row['what']}")
                if row.get("quote"):
                    near = f", near line {row['near_line']}" if row.get("near_line") else ""
                    w(f"  - observed quote{near}: `{row['quote']}`")

        if section["next_actions"]:
            w("")
            w("### Re-check it yourself")
            w("")
            for action in section["next_actions"][:10]:
                w(f"- `{action['command']}`")
    w("")
    return "\n".join(lines)
