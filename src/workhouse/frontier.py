"""The research frontier, computed rather than narrated.

Eight questions should be answerable at any moment: what is established, what
is supported but unproved, what is disputed, what is refuted, what is open,
which open problem blocks the most downstream theory, what the cheapest
decisive test is, and what principle might unify the established results.

Seven of the eight are computable from the ledgers, the invariant suites, and
the Lean tree, so they are computed here. Writing them by hand would guarantee
they go stale, and a stale frontier is worse than none: it reads current.

The eighth -- the unifying principle -- is a research judgement. It lives in
``ledger/gaps.yaml`` under ``unifying_candidates`` so it is data with a falsifier
attached, not prose inside a generated file.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from . import ledger as ledger_mod
from . import literature as literature_mod
from .invariants import SUITES

ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / "lean" / "Workhouse"
DECISIONS = ROOT / "docs" / "decisions"

#: Gap tier as a cost proxy, from gaps.yaml's own header.
TIER_COST = {
    0: "days",
    1: "weeks",
    2: "months",
    3: "unbounded",
}


@dataclass
class Frontier:
    checks_passed: int
    checks_total: int
    suites: list[tuple[str, int, int]]
    lean_theorems: int
    lean_sorries: int
    disputed: list[dict[str, Any]]
    refuted: list[dict[str, Any]]
    retracted: list[tuple[str, str]]
    open_gaps: list[dict[str, Any]]
    discharged_gaps: list[dict[str, Any]]
    downstream: list[tuple[str, int, list[str]]]
    cheapest: list[dict[str, Any]]
    spine: list[str]
    headline: str
    unifying: list[dict[str, Any]]
    external: list[tuple[str, str, str, str]]
    web: list[dict[str, Any]]
    acquisition: list[dict[str, Any]]


def strip_lean_comments(body: str) -> str:
    """Blank `/- ... -/` blocks (nested), `--` tails, and string contents.

    Newlines survive, so line numbers are stable for callers that scan
    per-line. The counters must see only code, in both directions: a module
    header that *says* "no `sorry`" must not count as one, and a string
    literal containing "/-" must not open a phantom comment that hides a
    real `sorry` until some later `-/`. Double-quoted strings are tracked
    with backslash escapes and their contents blanked (a `sorry` inside a
    string is data, not a proof hole).
    """
    out: list[str] = []
    i, depth = 0, 0
    in_string = False
    ident = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'!?")

    def char_literal_end(pos: int) -> int:
        """End index past a character literal at ``pos``, or ``pos`` if none.

        A quote after an identifier character is a prime (h'), never a
        literal; a literal is exactly '<char>' or '<backslash-escape>'.
        Without this, Char := '"' would open phantom string mode and blank
        every later theorem and sorry in the file.
        """
        if body[pos] != "'" or (pos > 0 and body[pos - 1] in ident):
            return pos
        j = pos + 1
        if j < len(body) and body[j] == "\\":
            j += 2
        elif j < len(body) and body[j] not in ("'", "\n"):
            j += 1
        else:
            return pos
        return j + 1 if j < len(body) and body[j] == "'" else pos

    while i < len(body):
        ch = body[i]
        two = body[i : i + 2]
        if in_string:
            if ch == "\\":
                i += 2
                continue
            if ch == '"':
                in_string = False
            elif ch == "\n":
                out.append("\n")
            i += 1
        elif two == "/-":
            depth += 1
            i += 2
        elif two == "-/" and depth:
            depth -= 1
            i += 2
        elif depth:
            if ch == "\n":
                out.append("\n")
            i += 1
        elif two == "--":
            end = body.find("\n", i)
            if end == -1:
                break
            i = end
        elif ch == "'" and (end := char_literal_end(i)) != i:
            i = end
        elif ch == '"':
            in_string = True
            i += 1
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def _lean_counts() -> tuple[int, int]:
    theorems = sorries = 0
    if not LEAN.exists():
        return 0, 0
    for path in LEAN.rglob("*.lean"):
        body = strip_lean_comments(path.read_text(encoding="utf-8"))
        theorems += len(re.findall(r"^\s*(?:theorem|lemma)\s", body, re.MULTILINE))
        sorries += len(re.findall(r"\bsorry\b", body))
    return theorems, sorries


def _retracted() -> list[tuple[str, str]]:
    """ADRs that withdraw an earlier decision, newest first.

    A repository that only records what it believes is not recording its
    reasoning. These are the entries where this repository was wrong.
    """
    out = []
    if not DECISIONS.exists():
        return out
    for path in sorted(DECISIONS.glob("*.md"), reverse=True):
        title = path.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
        # The title only. Scanning the body matches any ADR that merely mentions
        # a superseded document, which is most of them.
        if re.search(r"\bretract\w*|\bsupersed\w*|\bwithdraw\w*", title, re.IGNORECASE):
            out.append((path.stem, title))
    return out


def _downstream(led: ledger_mod.Ledgers) -> list[tuple[str, int, list[str]]]:
    """Rank gaps by how much they gate, over the ledger's own edges.

    Edges are ``unblocks`` (forward), the reverse of ``depends_on``, and each
    contradiction's ``blocks``. Weight is the size of the transitive closure
    plus the contradictions the gap claims to resolve -- everything that cannot
    move until this one does. A contradiction whose status is already
    ``resolved`` gates nothing and counts for nothing: a settled dispute is
    not downstream work, however recently it settled.
    """
    settled = {c["id"] for c in led.contradictions if c["status"] == "resolved"}
    forward: dict[str, set[str]] = {g["id"]: set(g.get("unblocks", [])) for g in led.gaps}
    for g in led.gaps:
        for prerequisite in g.get("depends_on", []):
            forward.setdefault(prerequisite, set()).add(g["id"])
    for c in led.contradictions:
        if c["id"] in settled:
            continue
        for blocked in c.get("blocks", []):
            # C blocks G, and whatever resolves C therefore gates G too.
            for g in led.gaps:
                if c["id"] in g.get("resolves", []):
                    forward.setdefault(g["id"], set()).add(blocked)

    def closure(start: str) -> set[str]:
        seen: set[str] = set()
        stack = list(forward.get(start, ()))
        while stack:
            node = stack.pop()
            if node in seen or node == start:
                continue
            seen.add(node)
            stack.extend(forward.get(node, ()))
        return seen

    ranked = []
    for g in led.open_gaps:
        # A discharged gap gates nothing: its work is done, whatever still
        # cites it. Reached ids that are themselves discharged drop out too.
        reached = sorted(closure(g["id"]) & led.open_gap_ids)
        resolves = sorted(c for c in g.get("resolves", []) if c not in settled)
        ranked.append((g["id"], len(reached) + len(resolves), reached + resolves))
    ranked.sort(key=lambda row: (-row[1], row[0]))
    return ranked


def _cheapest(led: ledger_mod.Ledgers) -> list[dict[str, Any]]:
    """Ready work that would *settle* something, cheapest first.

    Two filters, and the second is the one that matters. A gap is ready if no
    prerequisite gap is still open. A gap is decisive if it resolves a
    contradiction *that is still unsettled*, unblocks another gap, or is
    marked load-bearing. Cheap bookkeeping that settles nothing is not a
    decisive test however cheap it is, and listing it as one is how a
    frontier starts recommending busywork -- the same goes for re-settling a
    contradiction whose status is already resolved.
    """
    settled = {c["id"] for c in led.contradictions if c["status"] == "resolved"}
    unresolved = led.open_gap_ids
    ready = [g for g in led.open_gaps if not (set(g.get("depends_on", [])) & unresolved)]
    decisive = []
    for g in ready:
        still_open = [c for c in g.get("resolves", []) if c not in settled]
        if still_open or g.get("unblocks") or g.get("load_bearing"):
            decisive.append({**g, "settles": still_open + list(g.get("unblocks", []))})
    return sorted(decisive, key=lambda g: (g["tier"], g["id"]))


def compute() -> Frontier:
    led = ledger_mod.load()
    suites, passed, total = [], 0, 0
    for suite in SUITES:
        results = suite.run()
        ok = sum(1 for r in results if r.passed)
        suites.append((suite.name, ok, len(results)))
        passed += ok
        total += len(results)
    theorems, sorries = _lean_counts()
    lit = literature_mod.load()
    return Frontier(
        checks_passed=passed,
        checks_total=total,
        suites=suites,
        lean_theorems=theorems,
        lean_sorries=sorries,
        disputed=led.open_contradictions,
        refuted=[c for c in led.contradictions if c["status"] == "falsified"],
        retracted=_retracted(),
        open_gaps=led.open_gaps,
        discharged_gaps=led.discharged_gaps,
        downstream=_downstream(led),
        cheapest=_cheapest(led),
        spine=led.dependency_spine,
        headline=led.headline,
        unifying=led.unifying_candidates,
        external=[
            (paper["id"], edge["target"], edge["relation"], edge["status"])
            for paper, edge in lit.edges()
        ],
        web=literature_mod.relevance(lit),
        acquisition=literature_mod.acquisition_targets(lit),
    )


def render(f: Frontier) -> str:
    """FRONTIER.md. Generated; every number here is recomputed on each run."""
    out: list[str] = []
    w = out.append

    w("# Frontier")
    w("")
    w("**Generated by `workhouse frontier`. Do not edit — regenerate.**")
    w("")
    w(f"> {f.headline.strip()}")
    w("")
    w("This is the orientation file. It answers the eight questions in")
    w("`AGENTS.md` from the ledgers, the invariant suites, and the Lean tree, so")
    w("it cannot drift from what the repository actually checks.")
    w("")

    w("## 1. What is established")
    w("")
    w(f"**T0 — proof-checked.** {f.lean_theorems} Lean theorems, {f.lean_sorries} `sorry`.")
    w("")
    w(f"**T1/T2 — re-derived here.** {f.checks_passed}/{f.checks_total} checks pass.")
    w("")
    w("| Suite | Passing |")
    w("|---|---|")
    for name, ok, n in f.suites:
        w(f"| {name} | {ok}/{n} |")
    w("")
    w("`CERTIFIED.md` lists every one of these claims individually, ranked by")
    w("tier, each with the command that re-establishes it in about a second:")
    w("")
    w("```bash")
    w("workhouse verify --only 'h_4^side = A_+'   # one claim, with its numbers")
    w("```")
    w("")
    w("Everything else in the corpus is **T3: asserted and unchecked**. That is")
    w("the default, not an accusation.")
    w("")

    w("## 2. What is supported but not proved")
    w("")
    w("Read the check detail lines: a T2 pass is float agreement within a stated")
    w("tolerance and nothing more. `workhouse verify -v` prints every tolerance.")
    w("The corpus's own status/evidence split is the finer instrument — a claim")
    w("can be `proven` in status and `record-backed` in evidence, meaning the")
    w("argument exists and the artifact does not.")
    w("")

    w("## 3. What remains disputed")
    w("")
    if not f.disputed:
        w("Nothing is open in the contradiction register.")
    for c in f.disputed:
        w(f"**{c['id']} — {c['title']}**")
        w("")
        for side in c.get("sides", []):
            value = side.get("value")
            decimal = side.get("decimal")
            shown = f"`{value}`" + (f" = {decimal}" if decimal is not None else "")
            w(f"- {side['label']}: {shown}")
        if c.get("delta") is not None:
            w(f"- gap between them: `{c['delta']}`")
        w(f"- routed to: {', '.join(c.get('blocks', [])) or '(nothing)'}")
        w("")

    w("## 4. What has been refuted")
    w("")
    for c in f.refuted:
        w(f"- **{c['id']}** {c['title']} — {c.get('resolution', '').strip()}")
    w("")
    if f.retracted:
        w("Claims this repository made and withdrew:")
        w("")
        for stem, title in f.retracted:
            w(f"- `docs/decisions/{stem}.md` — {title}")
        w("")

    w("## 5. Open problems, by cost")
    w("")
    for tier in sorted(TIER_COST):
        rows = [g for g in f.open_gaps if g["tier"] == tier]
        if not rows:
            continue
        w(f"**Tier {tier} — {TIER_COST[tier]}**")
        w("")
        for g in rows:
            bearing = " **[load-bearing]**" if g.get("load_bearing") else ""
            partial = (
                " *(partial — see its status in the ledger)*" if g.get("state") == "partial" else ""
            )
            w(f"- `{g['id']}` {g['title']}{bearing}{partial}")
        w("")
    if f.discharged_gaps:
        w("**Discharged** — finished work stays recorded, not re-queued:")
        w("")
        for g in f.discharged_gaps:
            first = " ".join(str(g.get("status", "")).split()).split(" — ")[0]
            w(f"- `{g['id']}` {g['title']} — {first}")
        w("")

    w("## 6. What blocks the most downstream theory")
    w("")
    w("Transitive closure over the ledger's own `unblocks`, `depends_on`, and")
    w("`blocks` edges. The number is how much cannot move until this one does.")
    w("")
    w("| Gap | Gates | What cannot move until it does |")
    w("|---|---|---|")
    gated = [row for row in f.downstream if row[1]]
    for gid, weight, reached in gated[:6]:
        title = next(g["title"] for g in f.open_gaps if g["id"] == gid)
        w(f"| `{gid}` {title} | {weight} | {', '.join(reached)} |")
    if not gated:
        w("| — | 0 | nothing currently gates anything |")
    w("")
    for line in f.spine:
        w(f"- {line}")
    w("")

    w("## 7. The cheapest decisive test available now")
    w("")
    w("Ready — no open prerequisite — and decisive: it resolves a contradiction,")
    w("unblocks another gap, or is load-bearing. Cheapest first. Bookkeeping that")
    w("settles nothing is excluded however cheap it looks.")
    w("")
    for g in f.cheapest[:5]:
        settles = ", ".join(g.get("settles", [])) or "load-bearing"
        w(f"- `{g['id']}` ({TIER_COST[g['tier']]}) {g['title']} — settles {settles}")
        detail = " ".join(str(g.get("detail", "")).split())
        if detail:
            w(f"  - {detail}")
    w("")

    w("## 7b. What published work bears on this")
    w("")
    w("`literature/index.yaml` maps papers to claims; `workhouse lit --for C2`")
    w("queries it. External results matter here because they are **independent**")
    w("-- produced without knowledge of this program -- not because they are")
    w("published. A paper is T3 until something checks it, same as any document.")
    w("")
    w("| Paper | Bears on | Relation | Status |")
    w("|---|---|---|---|")
    for pid, target, relation, status in f.external:
        w(f"| `{pid}` | `{target}` | {relation} | {status} |")
    unread = sum(
        1 for _p, _t, _r, s in f.external if s in ("not-yet-obtained", "transcription-unverified")
    )
    w("")
    if unread:
        w(f"**{unread} of {len(f.external)} edges rest on a source nobody here has read")
        w("or pinned.** Obtaining and digest-pinning a primary source upgrades its")
        w("edges from assertion to verification — the Hamer 1989 table did exactly")
        w("that for the program's strongest external agreement.")
    else:
        w(f"All {len(f.external)} edges rest on read, pinned sources.")
    w("")

    w("The citation web, ranked. Two weights, kept apart because they mean")
    w("different things: **in-web** is how many indexed papers cite this one")
    w("(local — load-bearing for THIS program, computed at generation time),")
    w("**INSPIRE** is the field's global count, recorded with its date.")
    w("`workhouse lit --holes` prints the missing-link report over the same data.")
    w("")
    w("| Paper | In-web | INSPIRE (as of) | Standing |")
    w("|---|---|---|---|")
    for row in f.web:
        if row["in_web"] == 0 and row["stub"]:
            continue
        inspire = f"{row['inspire']} ({row['as_of']})" if row["inspire"] is not None else "—"
        if row["stub"]:
            standing = "stub"
        elif row["obtained"]:
            standing = "pinned"
        else:
            standing = "**not yet obtained**"
        w(f"| `{row['id']}` | {row['in_web']} | {inspire} | {standing} |")
    w("")
    if f.acquisition:
        top = f.acquisition[0]
        w(f"**Next acquisition target, computed: `{top['id']}`** — {top['in_web']} in-web")
        w("citations and nobody here has read or pinned it. The ranking surfaces")
        w("this automatically; obtaining the paper re-ranks it.")
        w("")

    w("## 8. What might unify the established results")
    w("")
    w("Research judgement, so it is data with a falsifier attached rather than")
    w("prose: `ledger/gaps.yaml`, `unifying_candidates`. A candidate with no")
    w("falsifier is an analogy, and analogies do not belong on this list.")
    w("")
    for u in f.unifying:
        w(f"**{u['id']} — {u['statement'].strip()}**")
        w("")
        w(f"- supported by: {', '.join(u.get('supported_by', [])) or '—'}")
        w(f"- would be falsified by: {' '.join(str(u['falsifier']).split())}")
        w(f"- status: {u['status']}")
        w("")

    return "\n".join(out) + "\n"


def brief() -> str:
    """A few hundred tokens for SessionStart injection.

    Deliberately not the whole frontier. What a session needs at second zero is
    where authority lives, what is actually open, and what not to do -- the rest
    is a command away. An injection long enough to skim is long enough to ignore.
    """
    f = compute()
    lines = [
        "WORKHOUSE — verification layer over a research corpus. Read AGENTS.md "
        "(posture) and CLAUDE.md (rules) before changing anything.",
        "",
        f"State: {f.checks_passed}/{f.checks_total} checks pass, "
        f"{f.lean_theorems} Lean theorems with {f.lean_sorries} sorry. "
        f"{len(f.disputed)} open contradiction, {len(f.open_gaps)} open gaps "
        f"({len(f.discharged_gaps)} discharged).",
        "",
        "Strongest work first: CERTIFIED.md ranks every checked claim by tier "
        "(T0 Lean, T1 exact, T2 numerical) and gives each one a re-check "
        "command — `workhouse verify --only '<name>'` runs it alone, with its "
        "numbers, in about a second.",
        "",
        "No document is authority; only a machine check is. Everything in "
        "theory/ is T3 (asserted, unchecked) until an invariant says otherwise.",
        "",
    ]
    if f.disputed:
        c = f.disputed[0]
        lines.append(f"Open: {c['id']} {c['title']}. Never promote either side.")
    if f.cheapest:
        g = f.cheapest[0]
        lines.append(f"Cheapest decisive next step: {g['id']} — {g['title']}.")
    lines += [
        "",
        "Traps: q_band^(4) and m_Gamma^(4) are differently anchored coordinates, "
        "not rival estimates (never 'two m_4 values'); never apply a 4**r "
        "rescaling; exact rationals stay sympy.Rational and floats carry _NUM; "
        "never edit theory/; never widen a tolerance to clear a finding.",
        "",
        "Orientation: FRONTIER.md, then ledger/, then invariants/. "
        "corpus-import/ is 950 files and ~61 context windows — target it, never "
        "read it recursively. Exact rationals are the join keys, not concepts.",
        "",
        "Commands: workhouse search <value|symbol|id> | why <id> | verify | "
        "frontier | status; make check. Search first: the measured failure "
        "mode is re-deriving what exists under different notation.",
    ]
    return "\n".join(lines)


def write(path: Path | None = None) -> Path:
    target = path or (ROOT / "FRONTIER.md")
    target.write_text(render(compute()), encoding="utf-8", newline="\n")
    return target
