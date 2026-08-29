"""``workhouse`` command line: verify the arithmetic, print the status."""

from __future__ import annotations

import argparse
import contextlib
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


def _force_utf8_streams() -> None:
    """Make stdout able to carry the corpus's own alphabet.

    The registry prints ``\u2192``, ``\u0393``, ``\u03b5``, ``\u03b2`` in nearly every
    subcommand. Windows still opens stdout as cp1252, which can encode none of
    them, so ``why C2`` died with ``UnicodeEncodeError`` before printing a
    single edge -- a crash that says nothing about the claim it was asked
    about. Ask for UTF-8 explicitly rather than relying on the platform
    default; if the stream refuses to be reconfigured, at least stop it from
    raising, so a wrong glyph beats no output.
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:  # pytest's capture object, a StringIO, a pipe proxy
            continue
        try:
            reconfigure(encoding="utf-8", errors="backslashreplace")
        except (ValueError, OSError):
            with contextlib.suppress(ValueError, OSError):
                reconfigure(errors="backslashreplace")


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


def _why(node_id: str, as_json: bool = False) -> int:
    if as_json:
        data, found = navigator_mod.neighborhood(node_id)
        print(json.dumps(data, sort_keys=True))
        return 0 if found else 1
    text, found = navigator_mod.explain(node_id)
    print(text)
    return 0 if found else 1


def _derive(ids: list[str], out: str | None) -> int:
    from pathlib import Path

    from . import derive as derive_mod

    text, ok = derive_mod.render(ids)
    if out:
        Path(out).write_text(text + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {out}")
    else:
        print(text)
    return 0 if ok else 1


def _branches(target: str | None) -> int:
    text, ok = navigator_mod.branchwise(target)
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


def _cross_check() -> int:
    """Every T1 quantity, computed twice, by two libraries that share no code.

    The table is the point: a reader who does not trust "T1" can see which
    quantity was recomputed, in which engine, and whether the two agreed --
    and can see the scope line saying what the agreement does not cover.
    """
    from . import cross_check as X

    held, failed = X.run()
    rows = X.witnesses()
    print("\033[1mdual-engine witness for the T1 layer\033[0m")
    print(
        "\033[2msympy against python-flint. Witnesses the arithmetic, not the "
        "derivation:\n  a wrong formula would be computed identically wrong by "
        "both engines.\033[0m\n"
    )
    for w in rows:
        mark = "\033[32mAGREE\033[0m" if w.holds() else "\033[31mDIFFER\033[0m"
        kind = "independent" if w.independent else "\033[2mre-normalised\033[0m"
        print(f"  {mark}  {w.name}")
        print(f"         \033[2m{w.section} · {kind}\033[0m")
        if not w.holds():
            print(f"         sympy: {w.sympy_side}")
            print(f"         flint: {w.flint_side}")
    independent = sum(1 for w in rows if w.independent)
    print(
        f"\n{len(held)}/{len(rows)} agree; {independent} of them are second "
        "constructions rather than re-normalisations of sympy's own answer"
    )
    return 1 if failed else 0


def _identify(
    value: str | None, claim: str | None, halfwidth: float | None, ulp: bool, qmax: int
) -> int:
    """Ask what exact form a recorded float could have -- and what it cannot.

    The output is in four parts because the question has four honest answers,
    and the last two are the ones that get skipped: what the number knows about
    itself, which rationals it admits, which relations clear their own digit
    budget, and what precision a recomputation would need to decide.
    """
    from . import identify as ident

    registered = ident.targets()
    if claim:
        if claim not in registered:
            print(f"unknown target {claim!r}; registered: {', '.join(sorted(registered))}")
            return 1
        window = registered[claim]
        label = claim
    else:
        v = float(value)
        if ulp and halfwidth is None:
            # The transcription window: every real that rounds to this double.
            # Correct only for a value whose exact form was rounded once on the
            # way in -- a table entry, a printed rational -- and wrong for
            # anything a computation produced.
            window = ident.Window.half_ulp(v, "half-ulp of the double, as given")
            label = repr(v)
            halfwidth = window.halfwidth
        elif halfwidth is None:
            print(
                "--halfwidth is required for a bare value, and that is deliberate.\n"
                "The half-ulp of a double is the accuracy of the TRANSCRIPTION, not of\n"
                "the computation behind it, and the identification ceiling goes as its\n"
                "square root -- so defaulting it is how a spurious identification gets\n"
                "published. Pass the uncertainty you can defend, or use --claim for a\n"
                "target whose window this repository has sourced:\n"
                f"  {', '.join(sorted(registered))}"
            )
            return 1
        if not ulp:
            window = ident.Window(v, halfwidth, "given on the command line")
            label = repr(v)

    print(f"\033[1m{label}\033[0m = {window.value!r}")
    print(f"  window   +-{window.halfwidth:.3e}  ({window.provenance})")
    print(f"  digits   {window.digits:.1f} reliable of {ident.DOUBLE_DIGITS:.1f} a double can hold")
    sat = ident.saturation_denominator(window)
    ceiling = ident.identification_ceiling(window)
    print(f"  ceiling  no denominator past {ceiling:.3e} can be singled out")
    print(
        f"  saturation  every denominator at or above {sat:,} admits an integer "
        "numerator, exactly (reduced-denominator claims need a coprime witness)"
    )

    print("\n\033[1mrationals the window admits\033[0m")
    for q in (10**3, 10**6, qmax):
        found, truncated = ident.admissible_rationals(window, q)
        est = ident.farey_count(window, q)
        shown = ", ".join(str(f) for f in found[:4]) or "none"
        more = f" (+{len(found) - 4} more)" if len(found) > 4 else ""
        cap = "+" if truncated else ""
        print(f"  q <= {q:>12,}: {len(found)}{cap} admissible, ~{est:.3g} expected  {shown}{more}")

    print("\n\033[1minteger relations, and whether they would have happened anyway\033[0m")
    scale = ident.scale_digits(window)
    for name, basis in ident.bases().items():
        print(f"  basis {name}: {', '.join(basis)}  (lattice at {scale} digits)")
        for r in ident.sweep(window, basis, limit=2):
            print(f"    {r}")
        # The second engine, reported either way: a completed PSLQ search that
        # returns nothing is an exclusion with a number on it, and one that
        # returns something says the two engines agree about the regime.
        second = ident.pslq_relation(
            [window.value, *(float(v) for v in basis.values())], scale, maxcoeff=10**6
        )
        if second["relation"] is not None:
            print(f"    PSLQ agrees a relation exists here: {second['relation']}")
        elif second["exhausted"]:
            print("    PSLQ ran out of steps -- no exclusion claimed")
        else:
            print(
                f"    PSLQ completes with nothing: no relation of norm below "
                f"{second['norm_bound']:.6g} exists at {scale} digits"
            )

    print("\n\033[1mwhat would decide it\033[0m")
    for q in (10**6, 4405310420659200):
        need = ident.digits_required(window.value, q)
        verdict = (
            "already carried"
            if need <= window.digits
            else f"{need - window.digits:.1f} more needed"
        )
        print(f"  q <= {q:>22,}: {need:.1f} significant digits -- {verdict}")
    return 0


def _oeis(scan: bool, fetch: bool, only: str | None) -> int:
    """The sequence register, and what the OEIS says about it."""
    from . import oeis as oeis_mod

    if fetch:
        print(f"fetching {oeis_mod.SNAPSHOT_URL} (32 MB, the maintainers' own dump)")
        path = oeis_mod.fetch()
        print(f"  {path}  sha256 {oeis_mod.snapshot_digest()}")

    sequences = oeis_mod.load()
    problems = oeis_mod.validate(sequences)
    if problems:
        for p in problems:
            print(f"\033[31m{p}\033[0m")
        return 1
    if only:
        sequences = [s for s in sequences if s.id == only]
        if not sequences:
            print(f"no registered sequence {only!r}")
            return 1

    if scan:
        if not oeis_mod.SNAPSHOT.exists():
            print(f"no snapshot at {oeis_mod.SNAPSHOT}; run `workhouse oeis --fetch` first")
            return 1
        snapshot = oeis_mod.load_snapshot()
        print(f"snapshot: {len(snapshot):,} sequences, sha256 {oeis_mod.snapshot_digest()[:16]}...")
        result = oeis_mod.scan(sequences, snapshot)
        drift = []
        for s in sequences:
            live, recorded = result[s.id], s.scan
            if recorded and live["verdict"] != recorded.get("verdict"):
                drift.append(f"{s.id}: recorded {recorded.get('verdict')} -> now {live['verdict']}")
        print("\n\033[1mcontrols (the correlation correction, re-measured)\033[0m")
        for name, c in oeis_mod.measure_controls(snapshot).items():
            ratio = f"{c['ratio']:.2e}" if c["ratio"] else "exact"
            print(
                f"  {name:>12}  observed {c['observed']:>5}  "
                f"predicted {c['predicted']:.2e}  under by {ratio}"
            )
    else:
        result = {s.id: s.scan for s in sequences}

    print("\n\033[1msequence register\033[0m")
    for s in sequences:
        r = result.get(s.id) or {}
        mark = {
            "hit": "\033[32mHIT\033[0m ",
            "no-hit": "none",
            "not-evidence": "\033[2mn/e\033[0m ",
        }
        print(f"  {mark.get(r.get('verdict'), '?   ')} {s.id:<16} {s.title}")
        print(
            f"        {len(s.terms)} terms, {s.generated_by}; {r.get('reason', 'not yet scanned')}"
        )
        if r.get("hits"):
            print(f"        {', '.join('https://oeis.org/' + a for a in r['hits'])}")
    if scan and drift:
        print("\n\033[31mthe snapshot has moved under the register:\033[0m")
        for d in drift:
            print(f"  {d}")
        return 1
    return 0


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
    v.add_argument(
        "--cross-check",
        action="store_true",
        dest="cross_check",
        help="recompute the T1 layer's exact values in python-flint and show "
        "where the two engines agree; T1 otherwise means 'sympy says'",
    )
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

    de = sub.add_parser(
        "derive",
        help="export one or more claims' evidence chains as Markdown (registered edges only)",
    )
    de.add_argument("ids", nargs="+", help="root claim ids, e.g. C2 G3 G10")
    de.add_argument("-o", "--out", metavar="PATH", help="write to a file instead of stdout")

    br = sub.add_parser(
        "branches",
        help="the branchwise view: every conflicting value, both branches side by side",
    )
    br.add_argument("id", nargs="?", help="one contradiction id (default: all with sides)")

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

    idf = sub.add_parser(
        "identify",
        help="what exact form a recorded float could have -- and what it cannot",
    )
    idf.add_argument("value", nargs="?", help="the float, e.g. -0.020213328886166577")
    idf.add_argument(
        "--claim",
        metavar="NAME",
        help="a registered target whose uncertainty this repository has sourced "
        "(C_shp, A_shp, alpha_pen, m_Gamma)",
    )
    # Mutually exclusive: the two options are rival answers to "what is the
    # window", and accepting both used to leave the window unassigned and die
    # with UnboundLocalError instead of an argument error.
    idf_window = idf.add_mutually_exclusive_group()
    idf_window.add_argument(
        "--halfwidth",
        type=float,
        metavar="H",
        help="the value's honest uncertainty; required for a bare value, because "
        "the half-ulp of a double is the accuracy of the transcription and not "
        "of the computation",
    )
    idf_window.add_argument(
        "--ulp",
        action="store_true",
        help="take the window as the double's half-ulp; correct ONLY for a value "
        "whose exact form was rounded once on the way in, such as a printed "
        "table entry, and wrong for anything a computation produced",
    )
    idf.add_argument(
        "--qmax", type=int, default=10**9, help="largest denominator to enumerate (default 1e9)"
    )

    oe = sub.add_parser(
        "oeis",
        help="the sequence register, and what the OEIS says about it",
    )
    oe.add_argument(
        "--scan",
        action="store_true",
        help="re-run the match against the local snapshot and report any drift "
        "from the recorded verdicts",
    )
    oe.add_argument(
        "--fetch",
        action="store_true",
        help="download oeis.org/stripped.gz, the maintainers' own dump; the "
        "search endpoint is never queried, robots.txt disallows it",
    )
    oe.add_argument("--only", metavar="ID", help="one registered sequence")

    args = parser.parse_args(argv)
    _force_utf8_streams()
    if _plain_stdout_wanted(args.no_color):
        sys.stdout = _AnsiStrippingStdout(sys.stdout)
    if args.command == "verify":
        if args.cross_check:
            return _cross_check()
        return _verify(args.verbose, args.only, args.tier, args.json)
    if args.command == "search":
        return _search(args.query, args.corpus, args.limit, args.json)
    if args.command == "index":
        return _index(args.write)
    if args.command == "why":
        return _why(args.id, args.json)
    if args.command == "derive":
        return _derive(args.ids, args.out)
    if args.command == "branches":
        return _branches(args.id)
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
    if args.command == "identify":
        if not args.value and not args.claim:
            print("give a value or --claim NAME")
            return 1
        return _identify(args.value, args.claim, args.halfwidth, args.ulp, args.qmax)
    if args.command == "oeis":
        return _oeis(args.scan, args.fetch, args.only)
    return _status()


if __name__ == "__main__":
    sys.exit(main())
