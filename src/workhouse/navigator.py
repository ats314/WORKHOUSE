"""``workhouse why``: one query, the whole recorded evidence neighborhood.

Search answers "where is this?"; this answers "what do we actually know about
it?" — the record itself, every edge in and out of it, the checks that cite
it with their live verdicts, the theorems and papers that bear on it, and,
for a gap, what its resolution would unblock. Everything printed is read from
the catalogue, the graph, or the ledgers at call time; nothing is authored
here, and nothing is ranked by anything except the sources' own fields.

For the disputed nodes this is deliberately symmetrical: `why C2` prints both
sides and the delta, never a preference.
"""

from __future__ import annotations

import dataclasses
import re

from . import claims as claims_mod
from . import frontier as frontier_mod
from . import graph as graph_mod
from . import ledger as ledger_mod
from . import render as render_mod

_TIER_MARK = {0: "T0", 1: "T1", 2: "T2", 3: "T3"}

#: How re-runnable the evidence behind a record actually is -- orthogonal to
#: both mathematical status and verification tier, and the third axis the agent
#: memo (notes/imported/UPLOADS_2026-08-28i, Observation 11) asked for. An agent
#: currently has to infer this across claims, checks, constants and notes, and
#: the inference is easy to get wrong in the direction that flatters the record.
REPLAY = {
    "cold": "re-derived from definitions by a check that runs here, now",
    "arithmetic-only": "a check re-runs the arithmetic; the generating computation does not",
    "saved-output": "verified against a pinned artifact, not recomputed",
    "payload-absent": "no artifact and no check: the record rests on its document",
}


def replay_status(claim: claims_mod.Claim | None, incident: list[graph_mod.Edge]) -> str | None:
    """Classify replayability from what is recorded, never from the prose.

    The pentagonal fifth-order coefficient is the case that motivates it: an
    imported proven-status claim, record-backed, whose current constant is T3
    and whose arithmetic check passes while the generating ledgers are absent.
    Printing "T3" alone loses that; printing "proved" alone is worse.
    """
    if claim is None:
        return None
    if claim.kind == "check":
        return "cold" if claim.tier in (1, 2) else "arithmetic-only"
    if claim.kind == "theorem":
        return "cold"
    # A record with a live check pointing at it is re-derivable through it.
    if any(e.src.startswith("CHK:") or e.dst.startswith("CHK:") for e in incident):
        return "arithmetic-only"
    if claim.kind == "run":
        return "saved-output"
    return "payload-absent"


def _clip(text: str, width: int = 76) -> str:
    text = " ".join(str(text).split())
    return text if len(text) <= width else text[: width - 1] + "…"


def _resolve(query: str, node_ids: set[str]) -> str | None:
    """A forgiving id lookup. Fuzzier retrieval stays `workhouse search`'s job."""
    q = query.strip()
    candidates = [q, q.upper()]
    m = re.fullmatch(r"(?i)adr[:\s]*(\d{1,4})", q)
    if m:
        candidates.append(f"ADR:{m.group(1).zfill(4)}")
    if ":" in q:
        prefix, rest = q.split(":", 1)
        candidates += [f"{prefix.upper()}:{rest}", f"{prefix.upper()}:{rest.lower()}"]
    candidates += [f"CONST:{q}", f"LEAN:{q}", f"SYM:{q.lower()}", f"LIT:{q}", f"LIT:{q.upper()}"]
    for candidate in candidates:
        if candidate in node_ids:
            return candidate
    return None


def traverse(
    graph: graph_mod.Graph,
    start: str,
    depth: int = 1,
    relations: set[str] | None = None,
) -> tuple[list[graph_mod.Edge], dict[str, int]]:
    """Breadth-first over recorded edges. Deterministic, and non-inferential.

    Returns the edges reached within ``depth`` hops and the hop count of every
    node reached (``start`` itself is 0). Direction is kept on each edge but is
    not followed: an evidence neighborhood is a neighborhood in both directions,
    which is what makes ``depth 2`` answer "what does the thing blocking this
    rest on?".

    At ``depth=1`` the edge set is exactly the node's own incident edges, so the
    default view is byte-identical to what it was before this existed. Reaching
    a node here is never a claim about it: an edge is shown only where a source
    file records one, and two nodes two hops apart are not thereby related.
    """
    adjacency: dict[str, list[graph_mod.Edge]] = {}
    for edge in graph.edges:
        if relations is not None and edge.type not in relations:
            continue
        adjacency.setdefault(edge.src, []).append(edge)
        adjacency.setdefault(edge.dst, []).append(edge)
    for edges in adjacency.values():
        edges.sort()

    depth_of = {start: 0}
    frontier = [start]
    collected: list[graph_mod.Edge] = []
    seen: set[graph_mod.Edge] = set()
    for hop in range(1, max(1, depth) + 1):
        following: set[str] = set()
        for node in frontier:
            for edge in adjacency.get(node, ()):
                if edge not in seen:
                    seen.add(edge)
                    collected.append(edge)
                other = edge.dst if edge.src == node else edge.src
                if other not in depth_of:
                    depth_of[other] = hop
                    following.add(other)
        frontier = sorted(following)
        if not frontier:
            break
    return collected, depth_of


def evidence_for(node: str, targets: dict[str, list[dict]] | None = None) -> list[dict]:
    """The pinned corpus documents that originate a node's value.

    Each row carries the document's repository path, its SHA-256 as pinned in
    ``corpus-import/SHA256SUMS``, the observed quote, and the line it sits near
    -- everything a reader needs to open the file and see the claim for
    themselves. `tests/test_provenance.py` already verifies each quote is a
    fixed string present in the pinned bytes, so this surfaces a checked fact
    rather than a curated assurance.
    """
    targets = targets if targets is not None else provenance_targets()
    return targets.get(node, [])


def provenance_targets() -> dict[str, list[dict]]:
    """Invert ledger/provenance.yaml: claim id -> the documents originating it."""
    out: dict[str, list[dict]] = {}
    for doc in claims_mod.load_provenance():
        for entry in doc.get("originates", []):
            out.setdefault(entry["target"], []).append(
                {
                    "document": doc["id"],
                    "path": doc["path"],
                    "sha256": doc["sha256"],
                    "role": doc.get("role", ""),
                    "what": entry.get("what", ""),
                    "quote": entry.get("quote", ""),
                    "near_line": entry.get("near_line"),
                }
            )
    return out


def next_actions(
    node: str,
    by_id: dict[str, claims_mod.Claim],
    edges: list[graph_mod.Edge],
) -> list[dict[str, str]]:
    """Runnable commands, harvested from records -- never composed here.

    The memo's Observation 6 is the whole argument: the graph's strongest
    moment was selecting narrow executable checks instead of leaving the agent
    with a bibliography. A neighborhood that names its own re-check turns
    reading into verifying. Every command below is a record's own ``reproduce``
    field; where no record carries one, nothing is offered, because inventing a
    plausible command is exactly how an agent ends up verifying nothing.
    """
    actions: list[dict[str, str]] = []
    seen: set[str] = set()

    def offer(command: str, what: str) -> None:
        if command and command not in seen:
            seen.add(command)
            actions.append({"command": command, "what": what})

    own = by_id.get(node)
    if own is not None and own.reproduce:
        offer(own.reproduce, f"re-check {node} itself")
    # Incident checks, nearest first, in the graph's own order.
    for edge in edges:
        for end in (edge.src, edge.dst):
            if end == node:
                continue
            claim = by_id.get(end)
            if claim is not None and claim.kind == "check" and claim.reproduce:
                offer(claim.reproduce, f"{end} — {_clip(claim.statement, 60)}")
    return actions


def load_context(
    mode: str = "live",
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
) -> tuple[list[claims_mod.Claim], list[dict], graph_mod.Graph]:
    """Assemble the catalogue, symbols and graph in one of two honest modes.

    ``live`` runs every check and rebuilds every edge: verdicts are true as of
    now. ``checked-index`` rehydrates the staleness-tested files in ``index/``:
    milliseconds instead of seconds, no scientific stack needed, and the
    verdicts are those of the commit that generated them.

    Neither is the "right" one, which is exactly why the mode is printed rather
    than assumed. An agent that reads a stale PASS as a live one has been
    misled by a tool that knew better and stayed quiet.
    """
    if mode == "checked-index":
        catalogue = catalogue if catalogue is not None else claims_mod.load_catalogue()
        symbols = symbols if symbols is not None else claims_mod.load_symbols()
        graph = graph if graph is not None else graph_mod.load()
        return catalogue, symbols, graph
    catalogue = catalogue if catalogue is not None else claims_mod.collect()
    symbols = symbols if symbols is not None else claims_mod.load_symbols()
    graph = graph if graph is not None else graph_mod.build(catalogue, symbols)
    return catalogue, symbols, graph


def payload(
    query: str,
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
    depth: int = 1,
    relations: set[str] | None = None,
    evidence: bool = False,
    mode: str = "live",
) -> dict:
    """``why`` as data: the same neighborhood the text view renders.

    Built from the same traversal so the two cannot disagree. Consumers should
    key on ``schema``; fields are added over time, never repurposed.
    """
    catalogue, symbols, graph = load_context(mode, catalogue, symbols, graph)
    by_id = {c.id: c for c in catalogue}
    sym_by_id = {f"SYM:{s['id']}": s for s in symbols}
    node = _resolve(query, set(by_id) | set(sym_by_id))

    out: dict = {
        "schema": render_mod.SCHEMA,
        "command": "why",
        "mode": mode,
        "query": query,
        "found": node is not None,
        "id": node,
    }
    if node is None:
        out["hint"] = f"workhouse search {query!r}"
        return out

    if node in sym_by_id:
        out["kind"] = "symbol"
        out["record"] = dict(sym_by_id[node])
    else:
        claim = by_id[node]
        out["kind"] = claim.kind
        out["record"] = dataclasses.asdict(claim)

    edges, depth_of = traverse(graph, node, depth=depth, relations=relations)
    out["edges"] = [
        {
            **dataclasses.asdict(edge),
            "direction": "out" if edge.src == node else ("in" if edge.dst == node else "onward"),
            "depth": min(depth_of.get(edge.src, depth), depth_of.get(edge.dst, depth)) + 1,
        }
        for edge in edges
    ]
    out["reached"] = {k: v for k, v in sorted(depth_of.items()) if k != node}
    out["depth"] = depth
    if relations is not None:
        out["relations"] = sorted(relations)

    incident = [e for e in edges if node in (e.src, e.dst)]
    status = replay_status(by_id.get(node), incident)
    if status is not None:
        out["replay"] = {"status": status, "means": REPLAY[status]}

    led = ledger_mod.load()
    entry = next((c for c in led.contradictions if c["id"] == node), None)
    if entry:
        out["contradiction"] = entry
    gap = next((g for g in led.gaps if g["id"] == node), None)
    if gap:
        out["gap"] = gap
    candidate = next((u for u in led.unifying_candidates if u["id"] == node), None)
    if candidate:
        out["unifying_candidate"] = candidate

    if evidence:
        out["evidence"] = evidence_for(node)
    out["next_actions"] = next_actions(node, by_id, incident)
    return out


def explain(
    query: str,
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
    depth: int = 1,
    relations: set[str] | None = None,
    evidence: bool = False,
    mode: str = "live",
    cap: int | None = 12,
) -> tuple[str, bool]:
    """The neighborhood as text.

    Every argument after ``graph`` is opt-in: at ``depth=1`` with no relation
    filter, no ``--evidence`` and live mode, the neighborhood renders as the
    same text as before they existed. That is deliberate -- this is a research
    tool someone may be reading mid-investigation, and a view that silently
    changes shape under them is worse than one that lacks a feature.

    One section *is* appended by default: the runnable re-check commands, which
    the memo asked for as a first-class field rather than a flag. It is
    strictly additional text at the end, and it is the difference between a
    neighborhood an agent reads and one it can act on.
    """
    catalogue, symbols, graph = load_context(mode, catalogue, symbols, graph)

    by_id = {c.id: c for c in catalogue}
    sym_by_id = {f"SYM:{s['id']}": s for s in symbols}
    node_ids = set(by_id) | set(sym_by_id)

    node = _resolve(query, node_ids)
    if node is None:
        return (
            f"no record with id {query!r}.\n"
            "`workhouse why` takes an id: C2, G14, R5, U3, CONST:t_N, "
            "LEAN:newton_three, ADR:0005, SYM:c_shp.\n"
            f"For fuzzier retrieval: workhouse search {query!r}",
            False,
        )

    lines: list[str] = []
    w = lines.append

    def describe(other: str) -> str:
        if other in by_id:
            claim = by_id[other]
            mark = _TIER_MARK.get(claim.tier, "  ") if claim.tier is not None else "  "
            verdict = ""
            if claim.kind == "check":
                passing = claim.status == "passing"
                verdict = " \033[32mPASS\033[0m" if passing else " \033[31mFAIL\033[0m"
            return f"{other}  \033[2m{mark}\033[0m{verdict}  {_clip(claim.statement, 60)}"
        if other in sym_by_id:
            return f"{other}  {_clip(sym_by_id[other].get('meaning', ''), 60)}"
        return other

    # -- the node itself ----------------------------------------------------
    if node in sym_by_id:
        symbol = sym_by_id[node]
        w(f"\033[1m{node}\033[0m — {symbol['canonical']}")
        w(f"  {' '.join(str(symbol.get('meaning', '')).split())}")
        spellings = symbol.get("corpus_spellings", [])
        if symbol.get("coined_here"):
            w(
                "  \033[33mCoined in this repository. The corpus writes "
                f"{', '.join(spellings)}. Not finding it is not absence.\033[0m"
            )
        elif spellings:
            w(f"  corpus spellings: {', '.join(spellings)}")
        for banned in symbol.get("forbidden", []):
            w(
                f"  \033[31mnever call it {banned['text']}:\033[0m "
                f"{' '.join(str(banned['why']).split())}"
            )
        if symbol.get("values"):
            w(f"  values: {', '.join(symbol['values'])}")
    else:
        claim = by_id[node]
        tier = _TIER_MARK.get(claim.tier, "") if claim.tier is not None else ""
        w(f"\033[1m{node}\033[0m — {claim.statement}")
        standing = " · ".join(x for x in (claim.kind, tier, claim.status, claim.evidence) if x)
        w(f"  {standing}")
        if claim.value is not None:
            decimal = f"  ({claim.decimal!r})" if claim.decimal is not None else ""
            w(f"  value: {claim.value}{decimal}")
        if claim.where:
            w(f"  \033[2m{claim.where}" + (f" · {claim.cites}" if claim.cites else "") + "\033[0m")
        if claim.detail:
            w(f"  {_clip(claim.detail, 200)}")
        if claim.reproduce:
            w(f"  \033[2m{claim.reproduce}\033[0m")

    # -- ledger detail the flat record cannot carry -------------------------
    led = ledger_mod.load()
    entry = next((c for c in led.contradictions if c["id"] == node), None)
    if entry and entry.get("sides"):
        w("")
        w("\033[1mBoth sides, neither promoted\033[0m")
        for side in entry["sides"]:
            w(f"  {side['label']}: {side['value']}  \033[2m({side['kind']})\033[0m")
        if entry.get("delta") is not None:
            w(f"  gap between them: {entry['delta']}")
    gap = next((g for g in led.gaps if g["id"] == node), None)
    if gap:
        cost = frontier_mod.TIER_COST.get(gap["tier"], "")
        state = gap.get("state", "open")
        w("")
        w(f"\033[1mGap standing\033[0m  {state} · cost tier {gap['tier']} — {cost}")
        if state != "open" and gap.get("status"):
            w(f"  {' '.join(str(gap['status']).split())}")
        open_prerequisites = sorted(set(gap.get("depends_on", [])) & led.open_gap_ids)
        if open_prerequisites:
            w(f"  blocked behind: {', '.join(open_prerequisites)}")
        if gap.get("protocol"):
            w(f"  frozen protocol: {len(gap['protocol'])} items in ledger/gaps.yaml")
        for key in ("inventory_trap", "note", "external_sharpening"):
            if gap.get(key):
                w(f"  {key}: {' '.join(str(gap[key]).split())}")
        if gap.get("leads"):
            w("  leads:")
            for lead in gap["leads"]:
                w(f"    {lead}")
        # Structured sub-blocks are too big to print; say they exist and where.
        elided = [
            key
            for key, value in gap.items()
            if isinstance(value, dict | list)
            and key not in ("resolves", "unblocks", "depends_on", "protocol", "leads")
        ]
        if elided:
            w(f"  \033[2malso in ledger/gaps.yaml: {', '.join(sorted(elided))}\033[0m")
        row = next((r for r in frontier_mod._downstream(led) if r[0] == node), None)
        if row and row[1]:
            w(f"  gates {row[1]} downstream: {', '.join(row[2])}")
    candidate = next((u for u in led.unifying_candidates if u["id"] == node), None)
    if candidate:
        w("")
        w(f"\033[1mFalsifier\033[0m  {' '.join(str(candidate['falsifier']).split())}")

    # -- every edge in and out, grouped by the source's own field name ------
    reached_edges, depth_of = traverse(graph, node, depth=depth, relations=relations)
    outgoing: dict[str, list[graph_mod.Edge]] = {}
    incoming: dict[str, list[graph_mod.Edge]] = {}
    onward: list[graph_mod.Edge] = []
    for edge in reached_edges:
        # Two independent tests, not if/elif: fourteen `duplicate_of` edges in
        # ledger/notes.yaml have src == dst, and those must keep appearing under
        # both headings exactly as they did before --depth existed.
        incident = False
        if edge.src == node:
            outgoing.setdefault(edge.type, []).append(edge)
            incident = True
        if edge.dst == node:
            incoming.setdefault(edge.type, []).append(edge)
            incident = True
        if not incident:
            # Reached only because --depth walked past a direct neighbour.
            onward.append(edge)

    def block(title: str, groups: dict[str, list[graph_mod.Edge]], other_end) -> None:
        if not groups:
            return
        w("")
        w(f"\033[1m{title}\033[0m")
        arrow = "→" if other_end == "dst" else "←"

        def rank(edge):
            # RETRACTED and FINDING checks must survive the display cap: losing
            # a retraction to alphabetical truncation is how a withdrawn claim
            # quietly starts reading as merely absent.
            #
            # RETRACTED outranks FINDING, and that ordering is load-bearing
            # rather than cosmetic. Findings accumulate -- the C2 geography
            # suite alone added four in one pass -- and when they shared a
            # priority band with retractions they pushed G14's retraction past
            # the cap by nothing more than alphabetical order. A neighbourhood
            # that grows must not be able to hide a withdrawal.
            claim = by_id.get(getattr(edge, other_end))
            statement = claim.statement if claim is not None and claim.kind == "check" else ""
            if statement.startswith("RETRACTED"):
                priority = 0
            elif statement.startswith("FINDING"):
                priority = 1
            else:
                priority = 2
            return (priority, edge.src, edge.dst)

        for type_ in sorted(groups):
            edges = sorted(groups[type_], key=rank)
            # `cap=None` (--all) prints every row. The cap exists so a busy node
            # stays readable, not to decide what matters; an agent asking for
            # the whole neighborhood must be able to get it.
            shown = edges if cap is None else edges[:cap]
            for edge in shown:
                w(f"  {type_} {arrow} {describe(getattr(edge, other_end))}")
            if len(edges) > len(shown):
                w(f"  {type_}: … {len(edges) - len(shown)} more")

    block("This record points at", outgoing, "dst")
    block("Points at this record", incoming, "src")

    if onward:
        w("")
        w(f"\033[1mFarther out\033[0m  {len(onward)} more edges within {depth} hops")
        by_hop: dict[int, list[str]] = {}
        for other, hop in depth_of.items():
            if hop >= 2:
                by_hop.setdefault(hop, []).append(other)
        for hop in sorted(by_hop):
            ids = sorted(by_hop[hop])
            head = ", ".join(ids[:8])
            more = f" … {len(ids) - 8} more" if len(ids) > 8 else ""
            w(f"  {hop} hops: {head}{more}")
        w(
            "  \033[2mreached, not related: an edge is shown only where a source records"
            " one,\n  and two nodes two hops apart are not thereby connected.\033[0m"
        )

    if not outgoing and not incoming:
        w("")
        w("  no recorded edges. If a relationship exists, its home is a curated")
        w("  field: ledger/*.yaml, ledger/theorems.yaml, or literature/index.yaml.")

    if evidence:
        rows = evidence_for(node)
        w("")
        w("\033[1mOriginating documents\033[0m")
        if not rows:
            w("  none pinned. ledger/provenance.yaml records an originating document")
            w("  only where someone judged it a distinct statement, not a carrier.")
        for row in rows:
            w(f"  {row['document']}  \033[2m{row['role']}\033[0m")
            w(f"    {row['path']}")
            w(f"    \033[2msha256 {row['sha256']}\033[0m")
            if row.get("what"):
                w(f"    {row['what']}")
            if row.get("quote"):
                near = f" (near line {row['near_line']})" if row.get("near_line") else ""
                w(f"    quote{near}: {row['quote']!r}")

    actions = next_actions(node, by_id, [e for e in reached_edges if node in (e.src, e.dst)])
    if actions:
        w("")
        w("\033[1mRe-check it yourself\033[0m")
        for action in actions[:6]:
            w(f"  {action['command']}")
            w(f"    \033[2m{action['what']}\033[0m")
        if len(actions) > 6:
            w(f"  \033[2m… {len(actions) - 6} more incident checks\033[0m")

    return "\n".join(lines), True
