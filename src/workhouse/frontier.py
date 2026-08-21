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
    downstream: list[tuple[str, int, list[str]]]
    cheapest: list[dict[str, Any]]
    spine: list[str]
    headline: str
    unifying: list[dict[str, Any]]


def _lean_counts() -> tuple[int, int]:
    theorems = sorries = 0
    if not LEAN.exists():
        return 0, 0
    for path in LEAN.rglob("*.lean"):
        body = path.read_text()
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
        head = path.read_text()[:2000]
        if re.search(r"\bretract|\bsupersed|\bwithdraw", head, re.IGNORECASE):
            title = head.splitlines()[0].lstrip("# ").strip()
            out.append((path.stem, title))
    return out


def _downstream(led: ledger_mod.Ledgers) -> list[tuple[str, int, list[str]]]:
    """Rank gaps by how much they gate, over the ledger's own edges.

    Edges are ``unblocks`` (forward), the reverse of ``depends_on``, and each
    contradiction's ``blocks``. Weight is the size of the transitive closure
    plus the contradictions the gap claims to resolve -- everything that cannot
    move until this one does.
    """
    forward: dict[str, set[str]] = {g["id"]: set(g.get("unblocks", [])) for g in led.gaps}
    for g in led.gaps:
        for prerequisite in g.get("depends_on", []):
            forward.setdefault(prerequisite, set()).add(g["id"])
    for c in led.contradictions:
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
    for g in led.gaps:
        reached = sorted(closure(g["id"]))
        resolves = sorted(g.get("resolves", []))
        ranked.append((g["id"], len(reached) + len(resolves), reached + resolves))
    ranked.sort(key=lambda row: (-row[1], row[0]))
    return ranked


def _cheapest(led: ledger_mod.Ledgers) -> list[dict[str, Any]]:
    """Ready work that would *settle* something, cheapest first.

    Two filters, and the second is the one that matters. A gap is ready if no
    prerequisite gap is still open. A gap is decisive if it resolves a
    contradiction, unblocks another gap, or is marked load-bearing. Cheap
    bookkeeping that settles nothing is not a decisive test however cheap it
    is, and listing it as one is how a frontier starts recommending busywork.
    """
    unresolved = led.gap_ids
    ready = [g for g in led.gaps if not (set(g.get("depends_on", [])) & unresolved)]
    decisive = [g for g in ready if g.get("resolves") or g.get("unblocks") or g.get("load_bearing")]
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
    return Frontier(
        checks_passed=passed,
        checks_total=total,
        suites=suites,
        lean_theorems=theorems,
        lean_sorries=sorries,
        disputed=led.open_contradictions,
        refuted=[c for c in led.contradictions if c["status"] == "falsified"],
        retracted=_retracted(),
        open_gaps=led.gaps,
        downstream=_downstream(led),
        cheapest=_cheapest(led),
        spine=led.dependency_spine,
        headline=led.headline,
        unifying=led.unifying_candidates,
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
            w(f"- `{g['id']}` {g['title']}{bearing}")
        w("")

    w("## 6. What blocks the most downstream theory")
    w("")
    w("Transitive closure over the ledger's own `unblocks`, `depends_on`, and")
    w("`blocks` edges. The number is how much cannot move until this one does.")
    w("")
    w("| Gap | Gates | What cannot move until it does |")
    w("|---|---|---|")
    for gid, weight, reached in f.downstream[:6]:
        title = next(g["title"] for g in f.open_gaps if g["id"] == gid)
        w(f"| `{gid}` {title} | {weight} | {', '.join(reached) or '—'} |")
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
        settles = ", ".join(g.get("resolves", []) + g.get("unblocks", [])) or "load-bearing"
        w(f"- `{g['id']}` ({TIER_COST[g['tier']]}) {g['title']} — settles {settles}")
        detail = " ".join(str(g.get("detail", "")).split())
        if detail:
            w(f"  - {detail}")
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
        f"{len(f.disputed)} open contradiction, {len(f.open_gaps)} gaps.",
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
        "Orientation: FRONTIER.md, then ledger/, then invariants.py. "
        "corpus-import/ is 950 files and ~61 context windows — target it, never "
        "read it recursively. Exact rationals are the join keys, not concepts.",
        "",
        "Commands: workhouse frontier | verify | status; make check.",
    ]
    return "\n".join(lines)


def write(path: Path | None = None) -> Path:
    target = path or (ROOT / "FRONTIER.md")
    target.write_text(render(compute()))
    return target
