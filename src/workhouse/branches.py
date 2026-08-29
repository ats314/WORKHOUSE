"""``workhouse branches``: every unresolved disagreement, side by side.

The agent memo's Observation 10 named the graph's best property -- it refused
two tempting merges, keeping ``C2``'s exact historical coefficient and its
numerical v10a.26 coefficient as separate branch results rather than selecting
one because it appeared in a newer document. But reconstructing that picture
meant reading a contradiction record, its provenance entries, and its incident
edges in three places.

So this is a *view*, not a judgement. It prints, for each side: the value and
whether it is exact or float, the pinned document it originates in, the claims
that depend on it, and the comparison that is still missing. It never ranks the
sides, never averages them, and never prefers the exact rational for looking
more authoritative -- CLAUDE.md forbids exactly that, and a view that quietly
ordered the sides would be the first step toward it.
"""

from __future__ import annotations

from . import claims as claims_mod
from . import graph as graph_mod
from . import ledger as ledger_mod
from . import navigator as navigator_mod
from . import render as render_mod


def collect(
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
    mode: str = "live",
    include_closed: bool = False,
) -> dict:
    catalogue, symbols, graph = navigator_mod.load_context(mode, catalogue, symbols, graph)
    by_id = {c.id: c for c in catalogue}
    led = ledger_mod.load()
    provenance = navigator_mod.provenance_targets()

    rows = []
    for entry in led.contradictions:
        if not entry.get("sides"):
            continue
        if entry.get("status") != "open" and not include_closed:
            continue
        node = entry["id"]
        incident = [e for e in graph.edges if node in (e.src, e.dst)]
        dependents = sorted(
            {e.src for e in incident if e.dst == node and e.src.startswith(("CHK:", "G", "C", "R"))}
        )
        # The gap that would settle it, in the ledger's own direction.
        settled_by = sorted({e.dst for e in incident if e.src == node and e.type == "blocks"})
        gaps = {g["id"]: g for g in led.gaps}
        rows.append(
            {
                "id": node,
                "title": entry.get("title", ""),
                "status": entry.get("status", ""),
                "section": entry.get("section", ""),
                "delta": entry.get("delta"),
                "sides": [
                    {
                        **side,
                        "originates_in": [
                            {"document": d["document"], "path": d["path"], "sha256": d["sha256"]}
                            for d in provenance.get(node, [])
                            # A side's originator is matched by the ledger's own
                            # label appearing in the pin's `what`; where no pin
                            # names it, the list is empty rather than guessed.
                            if side["label"].lower() in str(d.get("what", "")).lower()
                        ],
                    }
                    for side in entry["sides"]
                ],
                "all_pins": [
                    {"document": d["document"], "path": d["path"], "what": d.get("what", "")}
                    for d in provenance.get(node, [])
                ],
                "dependents": dependents,
                "settled_by": [
                    {
                        "id": gid,
                        "title": gaps.get(gid, {}).get("title", ""),
                        "state": gaps.get(gid, {}).get("state", "open"),
                        "tier": gaps.get(gid, {}).get("tier"),
                        # The exact missing comparison, quoted from the gap, not
                        # summarised: this is the whole point of the view.
                        "falsifier": gaps.get(gid, {}).get("falsifier", ""),
                        "leads": gaps.get(gid, {}).get("leads", []),
                    }
                    for gid in settled_by
                ],
                "notes": entry.get("notes", ""),
                "replay": navigator_mod.replay_status(by_id.get(node), incident),
            }
        )
    return {
        "schema": render_mod.SCHEMA,
        "command": "branches",
        "mode": mode,
        "open_disagreements": len(rows),
        "branches": rows,
    }


def render(data: dict) -> str:
    lines: list[str] = []
    w = lines.append
    w(f"\033[1mBranchwise results\033[0m  {data['open_disagreements']} unresolved disagreement(s)")
    w("  \033[2mboth sides recorded, neither promoted — never average, never pick\033[0m")
    for row in data["branches"]:
        w("")
        w(f"\033[1m{row['id']}\033[0m — {row['title']}")
        standing = " · ".join(x for x in (row["status"], row["section"], row["replay"]) if x)
        if standing:
            w(f"  {standing}")
        w("")
        for side in row["sides"]:
            w(f"  \033[1m{side['label']}\033[0m")
            w(f"    value: {side['value']}  \033[2m({side['kind']})\033[0m")
            if side.get("decimal") is not None:
                w(f"    decimal: {side['decimal']!r}")
            for pin in side["originates_in"]:
                w(f"    originates in: {pin['document']}")
                w(f"      \033[2m{pin['path']}\033[0m")
                w(f"      \033[2msha256 {pin['sha256']}\033[0m")
            if not side["originates_in"]:
                w("    \033[2mno pin names this side; see all pins below\033[0m")
        if row["delta"] is not None:
            w("")
            w(f"  gap between them: {row['delta']}")
        if row["all_pins"] and not any(s["originates_in"] for s in row["sides"]):
            w("")
            w("  pinned documents:")
            for pin in row["all_pins"]:
                w(f"    {pin['document']} — {pin['what']}")
        if row["settled_by"]:
            w("")
            w("  \033[1mThe missing comparison\033[0m")
            for gap in row["settled_by"]:
                tier = f"cost tier {gap['tier']}" if gap["tier"] is not None else ""
                w(f"    {gap['id']} ({gap['state']}{', ' + tier if tier else ''}) — {gap['title']}")
                if gap["falsifier"]:
                    w(f"      falsifier: {' '.join(str(gap['falsifier']).split())}")
                for lead in gap["leads"][:3]:
                    w(f"      lead: {' '.join(str(lead).split())}")
        else:
            w("")
            w("  \033[33mno gap is recorded as settling this.\033[0m")
        if row["dependents"]:
            shown = row["dependents"][:8]
            more = f" … {len(row['dependents']) - 8} more" if len(row["dependents"]) > 8 else ""
            w("")
            w(f"  depends on it: {', '.join(shown)}{more}")
    return "\n".join(lines)
