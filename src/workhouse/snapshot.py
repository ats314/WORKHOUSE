"""Whether the checked-in indexes still say what a live run says.

``index/*.jsonl``, ``FRONTIER.md`` and ``CERTIFIED.md`` are generated and
committed, which is what makes ``--checked-index`` fast and dependency-light.
It is also what makes them dangerous: a generated file that has drifted still
reads as current, and the agent memo (Observation 12) hit exactly that -- the
checked summaries reported a perfect verifier while a live run disagreed, and
nothing in the output said which was being read.

The staleness *tests* already fail when a generated file is out of date. This
is the other half: a command that says so on demand, before an agent builds an
argument on a snapshot, and that classifies what moved rather than rolling it
into one red total. A verdict that changed because a check now fails is a
different event from one that changed because a record was added, and calling
both "stale" loses the distinction that matters.
"""

from __future__ import annotations

from . import claims as claims_mod
from . import graph as graph_mod
from . import render as render_mod


def compare() -> dict:
    """Live versus checked, classified by what kind of thing moved."""
    live_claims = claims_mod.collect()
    checked_claims = claims_mod.load_catalogue()
    live_graph = graph_mod.build(live_claims, claims_mod.load_symbols())
    checked_graph = graph_mod.load()

    live_by_id = {c.id: c for c in live_claims}
    checked_by_id = {c.id: c for c in checked_claims}

    added = sorted(set(live_by_id) - set(checked_by_id))
    removed = sorted(set(checked_by_id) - set(live_by_id))
    # A verdict flip is the one an argument can be built on unknowingly.
    verdict_changed = sorted(
        {
            cid
            for cid in set(live_by_id) & set(checked_by_id)
            if live_by_id[cid].status != checked_by_id[cid].status
        }
    )
    detail_changed = sorted(
        {
            cid
            for cid in set(live_by_id) & set(checked_by_id)
            if live_by_id[cid].detail != checked_by_id[cid].detail
            and live_by_id[cid].status == checked_by_id[cid].status
        }
    )

    live_edges = {(e.src, e.dst, e.type, e.how, e.source) for e in live_graph.edges}
    checked_edges = {(e.src, e.dst, e.type, e.how, e.source) for e in checked_graph.edges}
    edges_added = sorted(live_edges - checked_edges)
    edges_removed = sorted(checked_edges - live_edges)

    # Path separators: the same tree generated on Windows must produce the same
    # bytes. Reported here rather than only in a test so a drifted snapshot
    # names the platform as the cause instead of looking like a content change.
    backslashed = sorted(
        {e.source for e in checked_graph.edges if "\\" in e.source}
        | {c.where for c in checked_claims if c.where and "\\" in c.where}
    )

    classes = {
        "verdict": verdict_changed,
        "record-added": added,
        "record-removed": removed,
        "detail": detail_changed,
        "edge-added": [f"{s} -{t}-> {d}" for s, d, t, _how, _src in edges_added],
        "edge-removed": [f"{s} -{t}-> {d}" for s, d, t, _how, _src in edges_removed],
        "platform": backslashed,
    }
    return {
        "schema": render_mod.SCHEMA,
        "command": "drift",
        "stale": any(classes.values()),
        "counts": {
            "live_claims": len(live_claims),
            "checked_claims": len(checked_claims),
            "live_edges": len(live_edges),
            "checked_edges": len(checked_edges),
        },
        "changed": {k: v for k, v in classes.items() if v},
    }


def render(data: dict) -> str:
    lines: list[str] = []
    w = lines.append
    counts = data["counts"]
    w("\033[1mSnapshot drift\033[0m  live run versus the checked-in index/")
    w(f"  claims: {counts['live_claims']} live · {counts['checked_claims']} checked")
    w(f"  edges:  {counts['live_edges']} live · {counts['checked_edges']} checked")
    if not data["stale"]:
        w("")
        w("\033[32m  index/ is current: --checked-index says what a live run says.\033[0m")
        return "\n".join(lines)
    w("")
    w("\033[33m  index/ has drifted. Regenerate with `make catalogue`.\033[0m")
    labels = {
        "verdict": "a check's verdict changed — an argument built on the snapshot may be wrong",
        "record-added": "records exist live that the snapshot has not got",
        "record-removed": "the snapshot carries records a live run no longer produces",
        "detail": "same verdict, different numbers",
        "edge-added": "relationships recorded live but absent from the snapshot",
        "edge-removed": "relationships in the snapshot that no source now records",
        "platform": "path separators are not POSIX — generated on Windows",
    }
    for kind, items in data["changed"].items():
        w("")
        w(f"  \033[1m{kind}\033[0m ({len(items)}) — {labels[kind]}")
        for item in items[:10]:
            w(f"    {item}")
        if len(items) > 10:
            w(f"    … {len(items) - 10} more")
    return "\n".join(lines)
