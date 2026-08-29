"""``workhouse`` command line: verify the arithmetic, print the status."""

from __future__ import annotations

import argparse
import dataclasses
import re
import sys

from . import atlas as atlas_mod
from . import branches as branches_mod
from . import certified as certified_mod
from . import claims as claims_mod
from . import derive as derive_mod
from . import frontier as frontier_mod
from . import graph as graph_mod
from . import ledger as ledger_mod
from . import literature as literature_mod
from . import navigator as navigator_mod
from . import render as render_mod
from . import search as search_mod
from . import snapshot as snapshot_mod
from . import triage as triage_mod
from .invariants import SUITES


def _verify(
    verbose: bool,
    only: str | None = None,
    tier: int | None = None,
    out: render_mod.Out | None = None,
    as_json: bool = False,
) -> int:
    """Run the checks, or one of them.

    ``--only`` exists so a single claim can be re-established on its own, in
    about a second, by someone who does not trust it. A certification nobody can
    cheaply reproduce is only a claim of authority. Matching is a
    case-insensitive substring, so the name from CERTIFIED.md can be pasted
    whole or abbreviated.
    """
    out = out if out is not None else render_mod.Out(True)
    failures = 0
    total = 0
    collected: list[dict] = []
    needle = only.lower() if only else None
    for suite in SUITES:
        # Filter BEFORE running: `--only` promises one claim in about a
        # second, which post-filtering a full 100+-check run cannot keep.
        wanted = [
            name
            for name, _section, check_tier, _fn in suite.checks
            if (needle is None or needle in name.lower()) and (tier is None or check_tier == tier)
        ]
        if not wanted:
            continue
        results = [r for r in suite.run(names=set(wanted))]
        if not results:
            continue
        if not as_json:
            out(f"\n\033[1m{suite.name}\033[0m")
        for r in results:
            total += 1
            collected.append(
                {
                    "suite": suite.name,
                    "name": r.name,
                    "tier": r.tier,
                    "passed": r.passed,
                    "detail": r.detail,
                    "section": r.section,
                    "source": r.source,
                    "reproduce": f"workhouse verify --only {r.name!r}",
                }
            )
            if not as_json:
                mark = "\033[32mPASS\033[0m" if r.passed else "\033[31mFAIL\033[0m"
                out(f"  {mark}  \033[2mT{r.tier}\033[0m  {r.name}")
                # A filtered run is someone checking one thing: always show the
                # numbers, since the verdict alone is what they came not to trust.
                if r.detail and (verbose or needle or not r.passed):
                    out(f"        {r.detail}")
                if r.detail and needle:
                    out(f"        \033[2m{r.source}\033[0m")
            if not r.passed:
                failures += 1
    if as_json:
        render_mod.dump(
            {
                "schema": render_mod.SCHEMA,
                "command": "verify",
                "filter": {"only": only, "tier": tier},
                "total": total,
                "passed": total - failures,
                "failed": failures,
                "checks": collected,
            }
        )
        return 1 if (failures or total == 0) else 0
    if total == 0:
        out(f"no check matches {only!r}" if only else f"no check at tier {tier}")
        return 1
    out(f"\n{total - failures}/{total} checks passed")
    return 1 if failures else 0


def _status(out: render_mod.Out, as_json: bool = False) -> int:
    led = ledger_mod.load()
    problems = ledger_mod.validate(led)

    if as_json:
        render_mod.dump(
            {
                "schema": render_mod.SCHEMA,
                "command": "status",
                "headline": led.headline,
                "contradictions": led.contradictions,
                "gaps": led.gaps,
                "unifying_candidates": led.unifying_candidates,
                "dependency_spine": led.dependency_spine,
                "problems": problems,
                "sound": not problems,
            }
        )
        return 1 if problems else 0

    out("\033[1mContradiction register\033[0m")
    for c in led.contradictions:
        flag = "\033[31m*\033[0m" if c["status"] == "open" else " "
        out(f"  {flag} {c['id']:<4} {c['status']:<22} {c['title']}")

    out("\n\033[1mGap analysis\033[0m")
    labels = {
        0: "tier 0 — bookkeeping (days)",
        1: "tier 1 — decisive finite computations (weeks)",
        2: "tier 2 — hard but structured (months)",
        3: "tier 3 — genuine open theorems (unbounded)",
    }
    for tier in sorted(labels):
        out(f"  {labels[tier]}")
        for g in led.gaps_by_tier(tier):
            bearing = " \033[33m[load-bearing]\033[0m" if g.get("load_bearing") else ""
            out(f"    {g['id']:<4} {g['title']}{bearing}")

    out("\n\033[1mDependency spine\033[0m")
    for line in led.dependency_spine:
        out(f"  - {line}")

    out(f"\n\033[1mHeadline\033[0m\n  {led.headline}")

    if problems:
        out("\n\033[31mLedger problems\033[0m")
        for p in problems:
            out(f"  - {p}")
        return 1
    out("\n\033[32mLedgers structurally sound.\033[0m")
    return 0


def _frontier(write: bool, brief: bool, out: render_mod.Out) -> int:
    if brief:
        out(frontier_mod.brief())
        return 0
    if write:
        target = frontier_mod.write()
        out(f"wrote {target.relative_to(frontier_mod.ROOT)}")
        return 0
    out(frontier_mod.render(frontier_mod.compute()))
    return 0


def _certified(write: bool, out: render_mod.Out) -> int:
    if write:
        target = certified_mod.write()
        out(f"wrote {target.relative_to(certified_mod.ROOT)}")
        return 0
    out(certified_mod.render())
    return 0


def _lit(
    target: str | None,
    holes: bool = False,
    acquire: bool = False,
    intake_dir: str | None = None,
    resolve_id: str | None = None,
    out: render_mod.Out | None = None,
) -> int:
    from pathlib import Path

    from . import acquisition as acquisition_mod

    out = out if out is not None else render_mod.Out(True)
    lit = literature_mod.load()
    problems = literature_mod.validate(lit)
    if resolve_id:
        out(acquisition_mod.format_resolution(acquisition_mod.resolve(resolve_id, lit)))
    elif intake_dir is not None:
        directory = Path(intake_dir) if intake_dir else acquisition_mod.INBOX
        out(acquisition_mod.format_intake(directory, lit))
    elif acquire:
        out(acquisition_mod.format_manifest(lit))
    elif holes:
        out(literature_mod.format_holes(lit))
    else:
        out(literature_mod.format_index(lit, target=target))
    if problems:
        out("\n\033[31mLiterature index problems\033[0m")
        for p in problems:
            out(f"  - {p}")
        return 1
    return 0


def _search(
    query: str, corpus: bool, limit: int, out: render_mod.Out, as_json: bool = False
) -> int:
    catalogue = claims_mod.load_catalogue()
    hits, symbols = search_mod.search(query, catalogue=catalogue)
    occurrences = search_mod.corpus_occurrences(query, limit=limit) if corpus else None
    found_in_corpus = occurrences is not None and occurrences.total_occurrences > 0
    if as_json:
        render_mod.dump(
            {
                "schema": render_mod.SCHEMA,
                "command": "search",
                "query": query,
                "claims": [
                    {"how": hit.how, **dataclasses.asdict(hit.claim)} for hit in hits[:limit]
                ],
                "symbols": symbols,
                "corpus": (
                    None
                    if occurrences is None
                    else {
                        "total_occurrences": occurrences.total_occurrences,
                        # Files, not occurrences: AGENTS.md counts distinct
                        # originating computations, and repetition is not
                        # independence. A consumer that sums hits re-learns that
                        # the hard way.
                        "files": [
                            {"path": path, "occurrences": n, "first_line": line, "sample": text}
                            for path, n, line, text in occurrences.files
                        ],
                    }
                ),
            }
        )
        return 0 if (hits or symbols or found_in_corpus) else 1
    out(search_mod.format_results(query, hits, symbols, occurrences, limit=limit))
    return 0 if (hits or symbols or found_in_corpus) else 1


def _index(write: bool, out: render_mod.Out) -> int:
    if write:
        claims_path, symbols_path = claims_mod.write()
        graph_path = graph_mod.write()
        for path in (claims_path, symbols_path, graph_path):
            rows = len(path.read_text(encoding="utf-8").splitlines())
            out(f"wrote {path.relative_to(claims_mod.ROOT)}: {rows} records")
        problems = graph_mod.validate()
        if problems:
            out("\n\033[31mGraph problems\033[0m")
            for p in problems:
                out(f"  - {p}")
            return 1
        return 0
    for claim in claims_mod.collect():
        out(f"{claim.id}\t{claim.kind}\t{claim.statement}")
    return 0


def _why(
    node_id: str,
    out: render_mod.Out,
    depth: int = 1,
    relations: str | None = None,
    evidence: bool = False,
    all_relations: bool = False,
    checked_index: bool = False,
    as_json: bool = False,
) -> int:
    """One id's evidence neighborhood, as text or as data.

    ``--all`` is not a synonym for a big ``--depth``: it lifts the per-relation
    display cap so a neighborhood cannot hide a row behind "… 14 more", while
    leaving the traversal exactly one hop. Widening and un-truncating are
    different questions and an agent needs to ask them separately.
    """
    mode = "checked-index" if checked_index else "live"
    wanted = {r.strip() for r in relations.split(",") if r.strip()} if relations else None
    if wanted:
        unknown = sorted(wanted - graph_mod.TYPES)
        if unknown:
            out(f"unknown relation(s): {', '.join(unknown)}")
            out(f"recorded relations: {', '.join(sorted(graph_mod.TYPES))}")
            return 1
    if as_json:
        data = navigator_mod.payload(
            node_id, depth=depth, relations=wanted, evidence=evidence, mode=mode
        )
        render_mod.dump(data)
        return 0 if data["found"] else 1
    text, found = navigator_mod.explain(
        node_id,
        depth=depth,
        relations=wanted,
        evidence=evidence,
        mode=mode,
        cap=None if all_relations else 12,
    )
    out(text)
    if found and mode == "checked-index":
        out("")
        out(
            "  \033[2mread from index/ (the commit's verdicts, not a live run)."
            " Drop --checked-index for live.\033[0m"
        )
    return 0 if found else 1


def _branches(
    out: render_mod.Out,
    checked_index: bool = False,
    include_closed: bool = False,
    as_json: bool = False,
) -> int:
    """Every unresolved disagreement, both sides, neither promoted."""
    data = branches_mod.collect(
        mode="checked-index" if checked_index else "live", include_closed=include_closed
    )
    if as_json:
        render_mod.dump(data)
    else:
        out(branches_mod.render(data))
    # Exit 0: an open disagreement is the recorded state, not a failure.
    return 0


def _drift(out: render_mod.Out, as_json: bool = False) -> int:
    """Whether index/ still says what a live run says."""
    data = snapshot_mod.compare()
    if as_json:
        render_mod.dump(data)
    else:
        out(snapshot_mod.render(data))
    return 1 if data["stale"] else 0


def _derive(
    roots: list[str],
    out: render_mod.Out,
    depth: int = 2,
    checked_index: bool = False,
    as_json: bool = False,
) -> int:
    """The recorded support for one or more claims, dependency-ordered."""
    mode = "checked-index" if checked_index else "live"
    data = derive_mod.collect(roots, depth=depth, mode=mode)
    if as_json:
        render_mod.dump(data)
    else:
        out(derive_mod.render_markdown(data))
    # An unresolved root is a failed request, not an empty answer.
    return 1 if data["unresolved"] else 0


def _atlas(target_path: str | None, out: render_mod.Out) -> int:
    from pathlib import Path

    data = atlas_mod.collect_data()
    target = atlas_mod.write(Path(target_path) if target_path else None, data)
    try:
        shown = target.relative_to(atlas_mod.ROOT)
    except ValueError:
        shown = target
    out(f"wrote {shown}: {len(data['nodes'])} nodes, {len(data['edges'])} edges")
    return 0


def _triage(directory: str, limit: int, out: render_mod.Out) -> int:
    from pathlib import Path

    try:
        report = triage_mod.scan(Path(directory))
    except NotADirectoryError as exc:
        out(f"not a directory: {exc}")
        return 1
    out(triage_mod.format_report(report, limit=limit))
    return 0


def _notes(scan: str | None, archive: str | None, queue_n: int | None, out: render_mod.Out) -> int:
    from pathlib import Path

    from . import notes as notes_mod

    registry = notes_mod.load()
    if scan is not None:
        if not archive:
            out("--scan needs --archive <id>; declare the id in ledger/notes.yaml first")
            return 1
        try:
            target = notes_mod.write_manifest(Path(scan), archive, registry)
        except (KeyError, NotADirectoryError) as exc:
            out(str(exc))
            return 1
        registry = notes_mod.load()
        rows = registry.manifests.get(archive, [])
        out(f"wrote {target.relative_to(notes_mod.ROOT)}: {len(rows)} unique documents")
        out(notes_mod.format_status(registry))
        return 0
    if queue_n is not None:
        out(notes_mod.format_queue(registry, queue_n))
        return 0
    out(notes_mod.format_status(registry))
    problems = notes_mod.validate(registry)
    for problem in problems:
        out(f"PROBLEM: {problem}")
    return 1 if problems else 0


def _rescue_negative_query(argv: list[str]) -> list[str]:
    """Let `workhouse search -5/48 --corpus` work without the `--` incantation.

    argparse reads a leading-minus token as an option, and the flagship search
    examples are negative values. When the token after the subcommand looks
    like a value rather than a flag, move it behind a `--` separator at the end
    of the line instead of dying with "query is required".

    Moving it to the end rather than inserting `--` in place is the whole point:
    `--` makes argparse treat *everything* after it as positional, so the
    in-place form turned the perfectly natural

        workhouse search -211835444920651/4405310420659200 --corpus --limit 12

    into "unrecognized arguments: --corpus --limit 12". The trailing form keeps
    the options as options and still shields the negative value.
    """
    valueish = re.compile(r"^-\d+(/\d+)?$|^-\d*\.\d+([eE][-+]?\d+)?$")
    out = list(argv)
    for i, token in enumerate(out[:-1]):
        if token in ("search", "why") and valueish.match(out[i + 1]) and "--" not in out:
            value = out[i + 1]
            return out[: i + 1] + out[i + 2 :] + ["--", value]
    return out


def main(argv: list[str] | None = None) -> int:
    argv = _rescue_negative_query(sys.argv[1:] if argv is None else argv)
    parser = argparse.ArgumentParser(prog="workhouse", description=__doc__)
    # Two parents rather than global flags before the subcommand: an agent
    # writes `workhouse why C2 --json`, which is where the flag reads naturally,
    # and argparse only accepts a top-level option BEFORE the subcommand.
    tint = argparse.ArgumentParser(add_help=False)
    tint.add_argument(
        "--color",
        dest="color",
        action="store_true",
        default=None,
        help="force ANSI colour even when stdout is not a terminal",
    )
    tint.add_argument(
        "--no-color",
        dest="color",
        action="store_false",
        help="never emit ANSI colour (also: set NO_COLOR in the environment)",
    )
    structured = argparse.ArgumentParser(add_help=False)
    structured.add_argument(
        "--json",
        dest="as_json",
        action="store_true",
        help="emit one JSON document instead of text, for a machine consumer",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    v = sub.add_parser(
        "verify", parents=[tint, structured], help="re-derive the corpus's exact claims"
    )
    v.add_argument("-v", "--verbose", action="store_true", help="show detail for passes too")
    v.add_argument("--only", metavar="TEXT", help="run just the checks whose name contains TEXT")
    v.add_argument("--tier", type=int, choices=(1, 2), help="run only T1 or only T2 checks")

    sub.add_parser(
        "status",
        parents=[tint, structured],
        help="print the contradiction and gap registers",
    )

    fr = sub.add_parser(
        "frontier", parents=[tint], help="what is established, disputed, refuted, and next"
    )
    fr.add_argument("-w", "--write", action="store_true", help="regenerate FRONTIER.md")
    fr.add_argument(
        "-b", "--brief", action="store_true", help="the short form injected at session start"
    )

    se = sub.add_parser(
        "search",
        parents=[tint, structured],
        help="find a claim by exact rational, decimal, symbol, alias, or claim id",
    )
    se.add_argument("query", help="109151/249696 | -0.88009871 | q_old | C_shape | C2")
    se.add_argument(
        "--corpus",
        action="store_true",
        help="also scan the 928-file corpus for that exact value (slow)",
    )
    se.add_argument("--limit", type=int, default=20, help="claims to show (default 20)")

    ix = sub.add_parser("index", parents=[tint], help="the claim, symbol, and graph catalogues")
    ix.add_argument("-w", "--write", action="store_true", help="regenerate index/*.jsonl")

    wy = sub.add_parser(
        "why",
        parents=[tint, structured],
        help="everything the repository records about one claim",
    )
    wy.add_argument(
        "id",
        help="C2 | G14 | R5 | U3 | CONST:t_N | LEAN:newton_three | ADR:0005 | SYM:c_shp",
    )
    wy.add_argument(
        "--depth",
        type=int,
        default=1,
        metavar="N",
        help="walk N hops out (default 1). Reaching a node is not a claim about it",
    )
    wy.add_argument(
        "--relations",
        metavar="A,B",
        help="only these edge types, comma-separated (e.g. blocks,resolves)",
    )
    wy.add_argument(
        "--evidence",
        action="store_true",
        help="add the pinned originating documents: path, SHA-256, observed quote, line",
    )
    wy.add_argument(
        "--all",
        dest="all_relations",
        action="store_true",
        help="lift the per-relation display cap; nothing is summarised as '… N more'",
    )
    wy.add_argument(
        "--checked-index",
        action="store_true",
        help="read index/*.jsonl instead of running the suites: fast, and the "
        "verdicts are the generating commit's rather than live",
    )

    at = sub.add_parser(
        "atlas", parents=[tint], help="render the theory graph to one self-contained HTML page"
    )
    at.add_argument(
        "-o", "--out", metavar="PATH", help="output file (default: atlas.html, not checked in)"
    )

    br = sub.add_parser(
        "branches",
        parents=[tint, structured],
        help="every unresolved disagreement, both sides side by side",
    )
    br.add_argument(
        "--checked-index",
        action="store_true",
        help="read index/*.jsonl instead of running the suites",
    )
    br.add_argument(
        "--closed", dest="include_closed", action="store_true", help="include settled disagreements"
    )

    sub.add_parser(
        "drift",
        parents=[tint, structured],
        help="whether the checked-in index/ still says what a live run says",
    )

    de = sub.add_parser(
        "derive",
        parents=[tint, structured],
        help="one or more claims' recorded support, dependency-ordered, as Markdown",
    )
    de.add_argument("ids", nargs="+", metavar="ID", help="C2 | G24 | G10 | CONST:t_N")
    de.add_argument(
        "--depth", type=int, default=2, metavar="N", help="hops of support to follow (default 2)"
    )
    de.add_argument(
        "--checked-index",
        action="store_true",
        help="read index/*.jsonl instead of running the suites",
    )

    li = sub.add_parser(
        "lit", parents=[tint], help="published work, and which claim each paper bears on"
    )
    li.add_argument(
        "--for",
        dest="target",
        metavar="ID",
        help="show only work bearing on this claim (C2, G18, R14, U3, or a constant)",
    )
    li.add_argument(
        "--holes",
        action="store_true",
        help="the missing-link report: papers on one claim with no citation path, "
        "and papers skipping their claim's most-cited source",
    )
    li.add_argument(
        "--acquire",
        action="store_true",
        help="the acquisition manifest: every unobtained paper, ranked, with the "
        "browser links a human needs to fetch it",
    )
    li.add_argument(
        "--intake",
        nargs="?",
        const="",
        metavar="DIR",
        help="survey literature/inbox (or DIR): identify dropped PDFs, print the "
        "digest to pin and what the licence permits; edits nothing",
    )
    li.add_argument(
        "--resolve",
        metavar="ID",
        help="try the automation-welcome open sources (arXiv, INSPIRE documents, "
        "KEK scans, OpenAlex) for one paper and download a hit into the inbox",
    )

    ce = sub.add_parser(
        "certified",
        parents=[tint],
        help="what is certified, ranked by tier, with how to re-check each claim",
    )
    ce.add_argument("-w", "--write", action="store_true", help="regenerate CERTIFIED.md")

    t = sub.add_parser(
        "triage",
        parents=[tint],
        help="survey an unpinned archive against what this repository already knows",
    )
    t.add_argument("directory", help="path to the archive (read-only; nothing is copied)")
    t.add_argument("--limit", type=int, default=25, help="rows per section (default 25)")

    no = sub.add_parser(
        "notes",
        parents=[tint],
        help="the notes register: archive inventories, review queue, verdict status",
    )
    no.add_argument(
        "--scan",
        metavar="DIR",
        help="inventory a mounted archive into notes/<archive-id>.jsonl (read-only)",
    )
    no.add_argument(
        "--archive",
        metavar="ID",
        help="which declared archive --scan is inventorying",
    )
    no.add_argument(
        "--queue",
        type=int,
        nargs="?",
        const=20,
        metavar="N",
        help="the next documents to review, highest signal first (default 20)",
    )

    args = parser.parse_args(argv)
    as_json = getattr(args, "as_json", False)
    # JSON is the machine surface; painting it would only make it harder to
    # parse, and no consumer of a pipe wants SGR codes inside a string value.
    out = render_mod.Out(False if as_json else render_mod.should_color(override=args.color))

    if args.command == "verify":
        return _verify(args.verbose, args.only, args.tier, out, as_json)
    if args.command == "search":
        return _search(args.query, args.corpus, args.limit, out, as_json)
    if args.command == "index":
        return _index(args.write, out)
    if args.command == "why":
        return _why(
            args.id,
            out,
            depth=args.depth,
            relations=args.relations,
            evidence=args.evidence,
            all_relations=args.all_relations,
            checked_index=args.checked_index,
            as_json=as_json,
        )
    if args.command == "branches":
        return _branches(out, args.checked_index, args.include_closed, as_json)
    if args.command == "drift":
        return _drift(out, as_json)
    if args.command == "derive":
        return _derive(
            args.ids, out, depth=args.depth, checked_index=args.checked_index, as_json=as_json
        )
    if args.command == "atlas":
        return _atlas(args.out, out)
    if args.command == "lit":
        return _lit(args.target, args.holes, args.acquire, args.intake, args.resolve, out)
    if args.command == "certified":
        return _certified(args.write, out)
    if args.command == "frontier":
        return _frontier(args.write, args.brief, out)
    if args.command == "triage":
        return _triage(args.directory, args.limit, out)
    if args.command == "notes":
        return _notes(args.scan, args.archive, args.queue, out)
    return _status(out, as_json)


if __name__ == "__main__":
    sys.exit(main())
