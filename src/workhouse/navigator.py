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

import re

from . import claims as claims_mod
from . import frontier as frontier_mod
from . import graph as graph_mod
from . import ledger as ledger_mod

_TIER_MARK = {0: "T0", 1: "T1", 2: "T2", 3: "T3"}


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


def branchwise(
    target: str | None = None,
    catalogue: list[claims_mod.Claim] | None = None,
    graph: graph_mod.Graph | None = None,
) -> tuple[str, bool]:
    """The branchwise-result view: every conflicting value, both branches whole.

    For each contradiction with recorded sides (or one, by id), print per
    branch its value and kind, the pinned documents that originate the claim,
    the checks and claims that depend on it, and — from the ledger's own
    ``blocks`` edge — the adjudication gap whose completion would unify the
    branches. Everything is read from curated fields; no branch is ranked,
    preferred, or averaged, and the "missing comparison" is the gap's own
    statement, not a synthesis.
    """
    catalogue = catalogue if catalogue is not None else claims_mod.collect()
    graph = graph if graph is not None else graph_mod.build(catalogue)
    by_id = {c.id: c for c in catalogue}
    led = ledger_mod.load()

    entries = [c for c in led.contradictions if c.get("sides")]
    if target is not None:
        wanted = target.strip().upper()
        entries = [c for c in entries if c["id"] == wanted]
        if not entries:
            return (
                f"no contradiction with recorded sides has id {target!r}.\n"
                "Branchwise view covers ledger contradictions carrying a `sides`"
                " field; try `workhouse branches` for all of them.",
                False,
            )

    lines: list[str] = []
    w = lines.append
    for n, entry in enumerate(entries):
        if n:
            w("")
        w(f"\033[1m{entry['id']}\033[0m — {entry['title']}  \033[2m[{entry['status']}]\033[0m")
        for side in entry["sides"]:
            w(f"  \033[1m{side['label']}\033[0m: {side['value']}  \033[2m({side['kind']})\033[0m")
            if side.get("decimal") is not None:
                w(f"    decimal: {side['decimal']!r}")
        if entry.get("delta") is not None:
            w(f"  gap between branches: {entry['delta']}")

        origins = sorted(
            e.src for e in graph.edges if e.dst == entry["id"] and e.type == "originates"
        )
        if origins:
            w("  originating documents (pinned):")
            for doc in origins:
                claim = by_id.get(doc)
                w(f"    {doc}" + (f" — {_clip(claim.statement, 70)}" if claim else ""))

        dependents = sorted(
            {e.src for e in graph.edges if e.dst == entry["id"] and e.type != "originates"}
            | {e.dst for e in graph.edges if e.src == entry["id"]}
        )
        checks = [d for d in dependents if d in by_id and by_id[d].kind == "check"]
        others = [d for d in dependents if d not in checks]
        if checks:
            w(f"  checks in the neighborhood ({len(checks)}):")
            for chk in checks[:8]:
                claim = by_id[chk]
                verdict = "PASS" if claim.status == "passing" else "FAIL"
                w(f"    [{verdict}] {_clip(claim.statement, 70)}")
            if len(checks) > 8:
                w(f"    … {len(checks) - 8} more (workhouse why {entry['id']})")
        if others:
            w(f"  \033[2mother recorded neighbors: {', '.join(others[:12])}\033[0m")

        for gap_id in entry.get("blocks", []):
            gap = next((g for g in led.gaps if g["id"] == gap_id), None)
            if gap:
                w(f"  \033[1mmissing comparison\033[0m ({gap_id}): {gap['title']}")
                if gap.get("leads"):
                    for lead in gap["leads"][:3]:
                        w(f"    lead: {_clip(lead, 90)}")
    if not entries:
        w("no contradiction in the ledger carries a `sides` field.")
    return "\n".join(lines), bool(entries)


def neighborhood(
    query: str,
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
) -> tuple[dict, bool]:
    """The `why` neighborhood as data: the record, every edge, no prose.

    Same sources and same non-inferential traversal as ``explain``; this exists
    so an agent can consume the neighborhood without parsing ANSI-decorated
    text. Nothing is included that ``explain`` would not print.
    """
    from dataclasses import asdict

    catalogue = catalogue if catalogue is not None else claims_mod.collect()
    symbols = symbols if symbols is not None else claims_mod.load_symbols()
    graph = graph if graph is not None else graph_mod.build(catalogue, symbols)

    by_id = {c.id: c for c in catalogue}
    sym_by_id = {f"SYM:{s['id']}": s for s in symbols}
    node = _resolve(query, set(by_id) | set(sym_by_id))
    if node is None:
        return {"query": query, "error": f"no record with id {query!r}"}, False

    record = asdict(by_id[node]) if node in by_id else sym_by_id[node]
    outgoing = [asdict(e) for e in graph.edges if e.src == node]
    incoming = [asdict(e) for e in graph.edges if e.dst == node]
    neighbors = {}
    for edge in outgoing + incoming:
        for end in (edge["src"], edge["dst"]):
            if end != node and end in by_id and end not in neighbors:
                claim = by_id[end]
                neighbors[end] = {
                    "kind": claim.kind,
                    "statement": claim.statement,
                    "tier": claim.tier,
                    "status": claim.status,
                    "reproduce": claim.reproduce,
                }
    return {
        "id": node,
        "record": record,
        "outgoing": outgoing,
        "incoming": incoming,
        "neighbors": neighbors,
    }, True


def explain(
    query: str,
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict] | None = None,
    graph: graph_mod.Graph | None = None,
) -> tuple[str, bool]:
    catalogue = catalogue if catalogue is not None else claims_mod.collect()
    symbols = symbols if symbols is not None else claims_mod.load_symbols()
    graph = graph if graph is not None else graph_mod.build(catalogue, symbols)

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
        # Routes, by state. This is the block that answers "what has been
        # tried" without a trip through the run READMEs: a dead route names
        # what killed it, a live one is where effort goes, an untried one is a
        # recorded proposal nobody has spent anything on.
        routes = gap.get("plan", []) or []
        if routes:
            w("")
            w("\033[1mRoutes\033[0m")
            order = {"live": 0, "untried": 1, "done": 2, "dead": 3}
            for step in sorted(routes, key=lambda st: order.get(st.get("state"), 9)):
                rid = claims_mod.route_id(node, step["step"])
                w(f"  [{step.get('state', '?')}] {step['step']}  \033[2m{rid}\033[0m")
                for ref in step.get("closed_by", []) or []:
                    w(f"      closed by {ref}")
                for ref in step.get("cannot_decide", []) or []:
                    w(f"      cannot decide {ref}")
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
    outgoing: dict[str, list[graph_mod.Edge]] = {}
    incoming: dict[str, list[graph_mod.Edge]] = {}
    for edge in graph.edges:
        if edge.src == node:
            outgoing.setdefault(edge.type, []).append(edge)
        if edge.dst == node:
            incoming.setdefault(edge.type, []).append(edge)

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
            shown = edges[:12]
            for edge in shown:
                w(f"  {type_} {arrow} {describe(getattr(edge, other_end))}")
            if len(edges) > len(shown):
                w(f"  {type_}: … {len(edges) - len(shown)} more")

    block("This record points at", outgoing, "dst")
    block("Points at this record", incoming, "src")

    if not outgoing and not incoming:
        w("")
        w("  no recorded edges. If a relationship exists, its home is a curated")
        w("  field: ledger/*.yaml, ledger/theorems.yaml, or literature/index.yaml.")

    # -- next actions: the neighboring checks, as runnable commands ---------
    # A neighborhood that ends in a bibliography leaves the reader to invent
    # their next step; one that ends in verifier commands does not. Only
    # registered checks appear here — nothing is suggested that is not
    # already an edge.
    neighbor_ids = {e.src for e in graph.edges if e.dst == node} | {
        e.dst for e in graph.edges if e.src == node
    }
    commands = sorted(
        {
            by_id[n].reproduce
            for n in neighbor_ids
            if n in by_id and by_id[n].kind == "check" and by_id[n].reproduce
        }
    )
    if node in by_id and by_id[node].kind == "check" and by_id[node].reproduce:
        commands = [by_id[node].reproduce] + [c for c in commands if c != by_id[node].reproduce]
    if commands:
        w("")
        w("\033[1mRe-check it yourself\033[0m")
        for command in commands[:6]:
            w(f"  {command}")
        if len(commands) > 6:
            w(f"  … {len(commands) - 6} more neighboring checks")

    return "\n".join(lines), True
