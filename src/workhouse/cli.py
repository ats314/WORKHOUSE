"""``workhouse`` command line: verify the arithmetic, print the status."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

from . import atlas as atlas_mod
from . import certified as certified_mod
from . import claims as claims_mod
from . import frontier as frontier_mod
from . import graph as graph_mod
from . import ledger as ledger_mod
from . import literature as literature_mod
from . import navigator as navigator_mod
from . import search as search_mod
from . import triage as triage_mod
from .invariants import SUITES

ANSI = re.compile(r"\033\[[0-9;]*m")


def _plain_stdout_wanted(no_color: bool) -> bool:
    """ANSI is for terminals. Piped output — an agent, a file, CI — gets plain
    text unless the caller says otherwise, and NO_COLOR is honored as spec'd."""
    if no_color or os.environ.get("NO_COLOR"):
        return True
    return not sys.stdout.isatty()


class _AnsiStrippingStdout:
    """A stdout proxy that drops escape codes so every subcommand inherits the
    policy without threading a flag through each format function."""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def write(self, text: str) -> int:
        return self._wrapped.write(ANSI.sub("", text))

    def __getattr__(self, name):
        return getattr(self._wrapped, name)


def _verify(
    verbose: bool, only: str | None = None, tier: int | None = None, as_json: bool = False
) -> int:
    """Run the checks, or one of them.

    ``--only`` exists so a single claim can be re-established on its own, in
    about a second, by someone who does not trust it. A certification nobody can
    cheaply reproduce is only a claim of authority. Matching is a
    case-insensitive substring, so the name from CERTIFIED.md can be pasted
    whole or abbreviated.
    """
    failures = 0
    total = 0
    records: list[dict] = []
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
        if as_json:
            for r in results:
                total += 1
                if not r.passed:
                    failures += 1
                records.append(
                    {
                        "suite": suite.name,
                        "name": r.name,
                        "tier": r.tier,
                        "passed": r.passed,
                        "detail": r.detail,
                        "where": f"src/workhouse/invariants.py:{r.line}",
                        "reproduce": f"workhouse verify --only {r.name!r}",
                    }
                )
            continue
        print(f"\n\033[1m{suite.name}\033[0m")
        for r in results:
            total += 1
            mark = "\033[32mPASS\033[0m" if r.passed else "\033[31mFAIL\033[0m"
            print(f"  {mark}  \033[2mT{r.tier}\033[0m  {r.name}")
            # A filtered run is someone checking one thing: always show the
            # numbers, since the verdict alone is what they came not to trust.
            if r.detail and (verbose or needle or not r.passed):
                print(f"        {r.detail}")
            if r.detail and needle:
                print(f"        \033[2m{r.source}\033[0m")
            if not r.passed:
                failures += 1
    if as_json:
        print(
            json.dumps(
                {"checks": records, "total": total, "passed": total - failures},
                sort_keys=True,
            )
        )
        return 1 if (failures or total == 0) else 0
    if total == 0:
        print(f"no check matches {only!r}" if only else f"no check at tier {tier}")
        return 1
    print(f"\n{total - failures}/{total} checks passed")
    return 1 if failures else 0


def _cached_context() -> dict:
    """The navigation sources read from ``index/*.jsonl`` instead of live.

    The index files are staleness-tested, so at any commit this is the same
    graph in milliseconds instead of a full 224-check run per call — the cost
    that made iterating with ``why``/``derive`` slow. The one honest
    difference is that check verdicts are as-generated, not re-run, so the
    mode announces itself on stderr rather than passing as live.
    """
    print(
        "cached index: statuses as checked in under index/ "
        "(regenerate: workhouse index -w; live verdicts: drop --cached)",
        file=sys.stderr,
    )
    return {
        "catalogue": claims_mod.load_catalogue(),
        "symbols": claims_mod.load_symbols(),
        "graph": graph_mod.load(),
    }


def _status() -> int:
    led = ledger_mod.load()
    problems = ledger_mod.validate(led)

    print("\033[1mContradiction register\033[0m")
    for c in led.contradictions:
        flag = "\033[31m*\033[0m" if c["status"] == "open" else " "
        print(f"  {flag} {c['id']:<4} {c['status']:<22} {c['title']}")

    print("\n\033[1mGap analysis\033[0m")
    labels = {
        0: "tier 0 — bookkeeping (days)",
        1: "tier 1 — decisive finite computations (weeks)",
        2: "tier 2 — hard but structured (months)",
        3: "tier 3 — genuine open theorems (unbounded)",
    }
    for tier in sorted(labels):
        print(f"  {labels[tier]}")
        for g in led.gaps_by_tier(tier):
            bearing = " \033[33m[load-bearing]\033[0m" if g.get("load_bearing") else ""
            print(f"    {g['id']:<4} {g['title']}{bearing}")

    print("\n\033[1mDependency spine\033[0m")
    for line in led.dependency_spine:
        print(f"  - {line}")

    print(f"\n\033[1mHeadline\033[0m\n  {led.headline}")

    # Nodes no edge touches are invisible to `why`, `derive`, and the atlas —
    # an unlinked theorem or paper is evidence the graph cannot surface, and
    # a list nobody prints only ever grows. Read from the checked-in index:
    # orphanhood depends on edges alone, and the index is staleness-tested.
    orphans = graph_mod.unreferenced(
        graph_mod.load(), claims_mod.load_catalogue(), claims_mod.load_symbols()
    )
    print(f"\n\033[1mGraph coverage\033[0m — {len(orphans)} records with no recorded edge")
    for node in orphans:
        print(f"  {node}")
    if orphans:
        print("  (each is unreachable from every claim; curate an edge in ledger/*.yaml)")

    if problems:
        print("\n\033[31mLedger problems\033[0m")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\n\033[32mLedgers structurally sound.\033[0m")
    return 0


def _frontier(write: bool, brief: bool) -> int:
    if brief:
        print(frontier_mod.brief())
        return 0
    if write:
        target = frontier_mod.write()
        print(f"wrote {target.relative_to(frontier_mod.ROOT)}")
        return 0
    print(frontier_mod.render(frontier_mod.compute()))
    return 0


def _certified(write: bool) -> int:
    if write:
        target = certified_mod.write()
        print(f"wrote {target.relative_to(certified_mod.ROOT)}")
        return 0
    print(certified_mod.render())
    return 0


def _lit(
    target: str | None,
    holes: bool = False,
    acquire: bool = False,
    intake_dir: str | None = None,
    resolve_id: str | None = None,
) -> int:
    from pathlib import Path

    from . import acquisition as acquisition_mod

    lit = literature_mod.load()
    problems = literature_mod.validate(lit)
    if resolve_id:
        print(acquisition_mod.format_resolution(acquisition_mod.resolve(resolve_id, lit)))
    elif intake_dir is not None:
        directory = Path(intake_dir) if intake_dir else acquisition_mod.INBOX
        print(acquisition_mod.format_intake(directory, lit))
    elif acquire:
        print(acquisition_mod.format_manifest(lit))
    elif holes:
        print(literature_mod.format_holes(lit))
    else:
        print(literature_mod.format_index(lit, target=target))
    if problems:
        print("\n\033[31mLiterature index problems\033[0m")
        for p in problems:
            print(f"  - {p}")
        return 1
    return 0


def _search(query: str, corpus: bool, limit: int, as_json: bool = False) -> int:
    from dataclasses import asdict

    catalogue = claims_mod.load_catalogue()
    hits, symbols = search_mod.search(query, catalogue=catalogue)
    occurrences = search_mod.corpus_occurrences(query, limit=limit) if corpus else None
    nearest = None if hits else search_mod.nearest_value(query, catalogue)
    if as_json:
        payload = {
            "query": query,
            "hits": [{"how": h.how, **asdict(h.claim)} for h in hits[:limit]],
            "total_hits": len(hits),
            "symbols": symbols,
            "nearest": None
            if nearest is None
            else {
                "id": nearest[0].id,
                "value": nearest[0].value,
                "relative_distance": nearest[1],
                "note": "proximity, not identity",
            },
            "corpus": None
            if occurrences is None
            else {
                "total_occurrences": occurrences.total_occurrences,
                "files": [
                    {"path": p, "count": n, "first_line": line, "sample": text}
                    for p, n, line, text in occurrences.files
                ],
            },
        }
        print(json.dumps(payload, sort_keys=True))
    else:
        print(
            search_mod.format_results(
                query, hits, symbols, occurrences, limit=limit, nearest=nearest
            )
        )
    found_in_corpus = occurrences is not None and occurrences.total_occurrences > 0
    return 0 if (hits or symbols or found_in_corpus) else 1


def _index(write: bool) -> int:
    if write:
        claims_path, symbols_path = claims_mod.write()
        graph_path = graph_mod.write()
        for path in (claims_path, symbols_path, graph_path):
            rows = len(path.read_text(encoding="utf-8").splitlines())
            print(f"wrote {path.relative_to(claims_mod.ROOT)}: {rows} records")
        problems = graph_mod.validate()
        if problems:
            print("\n\033[31mGraph problems\033[0m")
            for p in problems:
                print(f"  - {p}")
            return 1
        return 0
    for claim in claims_mod.collect():
        print(f"{claim.id}\t{claim.kind}\t{claim.statement}")
    return 0


def _why(node_id: str, as_json: bool = False, cached: bool = False) -> int:
    kwargs = _cached_context() if cached else {}
    if as_json:
        data, found = navigator_mod.neighborhood(node_id, **kwargs)
        print(json.dumps(data, sort_keys=True))
        return 0 if found else 1
    text, found = navigator_mod.explain(node_id, **kwargs)
    print(text)
    return 0 if found else 1


def _derive(
    ids: list[str],
    out: str | None,
    depth: int = 2,
    relations: str | None = None,
    as_json: bool = False,
    cached: bool = False,
) -> int:
    from pathlib import Path

    from . import derive as derive_mod

    wanted = None
    if relations is not None:
        wanted = frozenset(r.strip() for r in relations.split(",") if r.strip())
        unknown = sorted(wanted - graph_mod.TYPES)
        if unknown:
            print(f"unknown edge type(s): {', '.join(unknown)}")
            print(f"registered types: {', '.join(sorted(graph_mod.TYPES))}")
            return 2
    kwargs = _cached_context() if cached else {}
    if as_json:
        data, ok = derive_mod.data(ids, depth=depth, relations=wanted, **kwargs)
        text = json.dumps(data, sort_keys=True)
    else:
        text, ok = derive_mod.render(ids, depth=depth, relations=wanted, **kwargs)
    if out:
        Path(out).write_text(text + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {out}")
    else:
        print(text)
    return 0 if ok else 1


def _branches(target: str | None, cached: bool = False) -> int:
    kwargs = {}
    if cached:
        context = _cached_context()
        kwargs = {"catalogue": context["catalogue"], "graph": context["graph"]}
    text, ok = navigator_mod.branchwise(target, **kwargs)
    print(text)
    return 0 if ok else 1


def _export(out: str | None) -> int:
    from pathlib import Path

    from . import export as export_mod

    text = export_mod.render()
    if out:
        Path(out).write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {out}")
    else:
        print(text, end="")
    return 0


def _atlas(out: str | None) -> int:
    from pathlib import Path

    data = atlas_mod.collect_data()
    target = atlas_mod.write(Path(out) if out else None, data)
    try:
        shown = target.relative_to(atlas_mod.ROOT)
    except ValueError:
        shown = target
    print(f"wrote {shown}: {len(data['nodes'])} nodes, {len(data['edges'])} edges")
    return 0


def _triage(directory: str, limit: int) -> int:
    from pathlib import Path

    try:
        report = triage_mod.scan(Path(directory))
    except NotADirectoryError as exc:
        print(f"not a directory: {exc}")
        return 1
    print(triage_mod.format_report(report, limit=limit))
    return 0


def _notes(scan: str | None, archive: str | None, queue_n: int | None) -> int:
    from pathlib import Path

    from . import notes as notes_mod

    registry = notes_mod.load()
    if scan is not None:
        if not archive:
            print("--scan needs --archive <id>; declare the id in ledger/notes.yaml first")
            return 1
        try:
            target = notes_mod.write_manifest(Path(scan), archive, registry)
        except (KeyError, NotADirectoryError) as exc:
            print(str(exc))
            return 1
        registry = notes_mod.load()
        rows = registry.manifests.get(archive, [])
        print(f"wrote {target.relative_to(notes_mod.ROOT)}: {len(rows)} unique documents")
        print(notes_mod.format_status(registry))
        return 0
    if queue_n is not None:
        print(notes_mod.format_queue(registry, queue_n))
        return 0
    print(notes_mod.format_status(registry))
    problems = notes_mod.validate(registry)
    for problem in problems:
        print(f"PROBLEM: {problem}")
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
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="never emit ANSI codes (also implied by a non-terminal stdout or NO_COLOR)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    v = sub.add_parser("verify", help="re-derive the corpus's exact claims")
    v.add_argument("-v", "--verbose", action="store_true", help="show detail for passes too")
    v.add_argument("--only", metavar="TEXT", help="run just the checks whose name contains TEXT")
    v.add_argument("--tier", type=int, choices=(1, 2), help="run only T1 or only T2 checks")
    v.add_argument("--json", action="store_true", help="machine-readable results, one JSON object")

    sub.add_parser("status", help="print the contradiction and gap registers")

    fr = sub.add_parser("frontier", help="what is established, disputed, refuted, and next")
    fr.add_argument("-w", "--write", action="store_true", help="regenerate FRONTIER.md")
    fr.add_argument(
        "-b", "--brief", action="store_true", help="the short form injected at session start"
    )

    se = sub.add_parser(
        "search",
        help="find a claim by exact rational, decimal, symbol, alias, or claim id",
    )
    se.add_argument("query", help="109151/249696 | -0.88009871 | q_old | C_shape | C2")
    se.add_argument(
        "--corpus",
        action="store_true",
        help="also scan the 928-file corpus for that exact value (slow)",
    )
    se.add_argument("--limit", type=int, default=20, help="claims to show (default 20)")
    se.add_argument("--json", action="store_true", help="machine-readable results, one JSON object")

    ix = sub.add_parser("index", help="the claim, symbol, and graph catalogues")
    ix.add_argument("-w", "--write", action="store_true", help="regenerate index/*.jsonl")

    wy = sub.add_parser("why", help="everything the repository records about one claim")
    wy.add_argument(
        "id",
        help="C2 | G14 | R5 | U3 | CONST:t_N | LEAN:newton_three | ADR:0005 | SYM:c_shp",
    )
    wy.add_argument(
        "--json", action="store_true", help="the record and every edge, one JSON object"
    )
    wy.add_argument(
        "--cached",
        action="store_true",
        help="read index/*.jsonl instead of re-running every check (fast; "
        "verdicts as checked in, not live)",
    )

    de = sub.add_parser(
        "derive",
        help="export one or more claims' evidence chains as Markdown (registered edges only)",
    )
    de.add_argument("ids", nargs="+", help="root claim ids, e.g. C2 G3 G10")
    de.add_argument("-o", "--out", metavar="PATH", help="write to a file instead of stdout")
    de.add_argument("--depth", type=int, default=2, help="how many edges out to walk (default 2)")
    de.add_argument(
        "--relations",
        metavar="TYPE,TYPE",
        help="walk only these edge types (e.g. blocks,resolves,uses); "
        "elides the rest, infers nothing",
    )
    de.add_argument(
        "--json", action="store_true", help="the chains as one JSON object instead of Markdown"
    )
    de.add_argument(
        "--cached",
        action="store_true",
        help="read index/*.jsonl instead of re-running every check (fast; "
        "verdicts as checked in, not live)",
    )

    br = sub.add_parser(
        "branches",
        help="the branchwise view: every conflicting value, both branches side by side",
    )
    br.add_argument("id", nargs="?", help="one contradiction id (default: all with sides)")
    br.add_argument(
        "--cached",
        action="store_true",
        help="read index/*.jsonl instead of re-running every check (fast; "
        "verdicts as checked in, not live)",
    )

    ex = sub.add_parser(
        "export",
        help="the whole graph as one versioned JSON envelope, for external ingestion",
    )
    ex.add_argument("-o", "--out", metavar="PATH", help="write to a file instead of stdout")

    at = sub.add_parser("atlas", help="render the theory graph to one self-contained HTML page")
    at.add_argument(
        "-o", "--out", metavar="PATH", help="output file (default: atlas.html, not checked in)"
    )

    li = sub.add_parser("lit", help="published work, and which claim each paper bears on")
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
        "certified", help="what is certified, ranked by tier, with how to re-check each claim"
    )
    ce.add_argument("-w", "--write", action="store_true", help="regenerate CERTIFIED.md")

    t = sub.add_parser(
        "triage",
        help="survey an unpinned archive against what this repository already knows",
    )
    t.add_argument("directory", help="path to the archive (read-only; nothing is copied)")
    t.add_argument("--limit", type=int, default=25, help="rows per section (default 25)")

    no = sub.add_parser(
        "notes",
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
    # A Windows console without UTF-8 mode encodes stdout as cp1252, which
    # cannot carry the edge arrows — so `why C2` crashed mid-print on the
    # exact machine the 2026-08-28 notes reported. Escaping the unencodable
    # character beats dying on it; on a UTF-8 stream every character encodes
    # and this never fires. Output only: reads stay strict utf-8 everywhere.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="backslashreplace")
    if _plain_stdout_wanted(args.no_color):
        sys.stdout = _AnsiStrippingStdout(sys.stdout)
    if args.command == "verify":
        return _verify(args.verbose, args.only, args.tier, args.json)
    if args.command == "search":
        return _search(args.query, args.corpus, args.limit, args.json)
    if args.command == "index":
        return _index(args.write)
    if args.command == "why":
        return _why(args.id, args.json, args.cached)
    if args.command == "derive":
        return _derive(args.ids, args.out, args.depth, args.relations, args.json, args.cached)
    if args.command == "branches":
        return _branches(args.id, args.cached)
    if args.command == "export":
        return _export(args.out)
    if args.command == "atlas":
        return _atlas(args.out)
    if args.command == "lit":
        return _lit(args.target, args.holes, args.acquire, args.intake, args.resolve)
    if args.command == "certified":
        return _certified(args.write)
    if args.command == "frontier":
        return _frontier(args.write, args.brief)
    if args.command == "triage":
        return _triage(args.directory, args.limit)
    if args.command == "notes":
        return _notes(args.scan, args.archive, args.queue)
    return _status()


if __name__ == "__main__":
    sys.exit(main())
