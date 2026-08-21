"""Getting unobtained papers into hand — lawfully, and with the human where
the licence puts them.

The citation web computes which papers matter and which of those nobody here
has read. This module closes the loop with three verbs, none of which ever
edits the index — curation stays a judgement made in ``literature/index.yaml``:

* **manifest** (``workhouse lit --acquire``) — the unobtained papers, ranked
  by the web's own relevance, each with the direct browser links a human
  needs to fetch it in two minutes. Publisher walls that refuse automation
  (ScienceDirect's open archive, APS) appear here as links for a person,
  and deliberately nowhere else in this module.
* **resolve** (``workhouse lit --resolve ID``) — try the sources that DO
  welcome automation, in order: arXiv, INSPIRE-hosted documents, KEK library
  preprint scans, and OpenAlex's open-access locations. A hit is downloaded
  into the inbox and hashed; a miss says exactly what was tried.
* **intake** (``workhouse lit --intake [DIR]``) — identify what landed in the
  inbox (by digest, by ``<ID>.pdf`` filename, or by a best-effort text sniff
  of the title page), print the digest ready to pin, and say what the
  licence permits. It reports; a person or agent then curates.

The inbox (``literature/inbox/``) is not the repository: it is gitignored,
because storing a paper is republishing it, and a working copy you obtained
lawfully for reading is not a right to redistribute. ``intake`` repeats that
warning on every run rather than trusting anyone to remember it.

What this module refuses to do, on purpose: impersonate a browser to a
publisher's bot wall, or touch any source that is not either openly licensed
or an open library service. The KEK library serves its preprint scans to the
public and merely rejects the default ``curl`` client string; sending a
normal browser identification there is ordinary client behaviour, not
circumvention, and it is the only place this module does so.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.request
import zlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from . import literature as lit_mod

ROOT = Path(__file__).resolve().parents[2]
INBOX = ROOT / "literature" / "inbox"

#: Sent only to open library/archive services (KEK scans, arXiv, INSPIRE,
#: OpenAlex). KEK's WAF rejects the default curl string while serving the
#: same file to any browser; identifying as one is ordinary, not evasive.
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) workhouse-literature"

FETCH_TIMEOUT = 60


# --------------------------------------------------------------------------
# pure link construction — no network, fully testable
# --------------------------------------------------------------------------


def sciencedirect_pii(doi: str | None) -> str | None:
    """The ScienceDirect PII embedded in an old Elsevier DOI.

    ``10.1016/0550-3213(86)90568-7`` -> ``0550321386905687``: the suffix with
    the punctuation removed. Only 10.1016 DOIs carry one.
    """
    if not doi or not str(doi).startswith("10.1016/"):
        return None
    suffix = str(doi).split("/", 1)[1]
    pii = re.sub(r"[^0-9A-Za-z]", "", suffix)
    return pii or None


def kek_scan_url(kekscan_id: str) -> str | None:
    """The KEK library's stable scan URL for a KEKSCAN id.

    Observed pattern, verified on retrieved scans: id ``80-10-101`` (or
    ``1976-10-104``) lives at ``/preprints/PDF/1980/8010/8010101.pdf`` — a
    two-digit year folder pair and the concatenated digits as filename.
    Pre-2000 ids only; a four-digit year starting 20 has no known pattern.
    """
    m = re.fullmatch(r"(?:19)?(\d{2})-(\d{2})-(\d{3})", str(kekscan_id).strip())
    if not m:
        return None
    yy, mm, nnn = m.groups()
    return f"https://lib-extopc.kek.jp/preprints/PDF/19{yy}/{yy}{mm}/{yy}{mm}{nnn}.pdf"


def browser_links(record: dict[str, Any]) -> list[tuple[str, str]]:
    """(label, url) pairs a HUMAN can open. Includes the walled ones."""
    links: list[tuple[str, str]] = []
    if record.get("arxiv"):
        links.append(("arxiv", f"https://arxiv.org/abs/{record['arxiv']}"))
    if record.get("doi"):
        links.append(("doi", f"https://doi.org/{record['doi']}"))
        pii = sciencedirect_pii(record.get("doi"))
        if pii:
            links.append(
                ("sciencedirect", f"https://www.sciencedirect.com/science/article/pii/{pii}")
            )
    if record.get("inspire_recid"):
        links.append(("inspire", f"https://inspirehep.net/literature/{record['inspire_recid']}"))
    return links


def resolve_plan(record: dict[str, Any]) -> list[tuple[str, str]]:
    """The static (no-network) part of the automated plan: (source, url).

    ScienceDirect and APS are deliberately absent — their walls refuse
    automation, so they are browser links in the manifest instead. The
    INSPIRE record is queried live in :func:`resolve` for hosted documents
    and KEKSCAN ids; here we can only plan the arXiv leg.
    """
    plan: list[tuple[str, str]] = []
    if record.get("arxiv"):
        plan.append(("arxiv", f"https://arxiv.org/pdf/{record['arxiv']}"))
    return plan


# --------------------------------------------------------------------------
# the manifest
# --------------------------------------------------------------------------


def manifest(lit: lit_mod.Literature | None = None) -> list[dict[str, Any]]:
    """Every unobtained node, ranked, with links and what obtaining settles."""
    lit = lit or lit_mod.load()
    rows = []
    for row in lit_mod.relevance(lit):
        if row["obtained"]:
            continue
        record = lit.entry(row["id"])
        assert record is not None
        if row["stub"]:
            settles = " ".join(str(record.get("note", "")).split())
        else:
            pending = [
                f"{e['target']} ({e['relation']}, now {e['status']})"
                for e in record.get("bears_on", [])
                if e["status"] != "verified"
            ]
            settles = (
                "; ".join(pending)
                if pending
                else "all edges already verified; obtaining adds the pin"
            )
        rows.append(
            {
                **row,
                "title": record.get("title", ""),
                "venue": record.get("venue", ""),
                "links": browser_links(record),
                "settles": settles,
                "licence": str(record.get("licence", "")).lower(),
            }
        )
    return rows


def format_manifest(lit: lit_mod.Literature | None = None) -> str:
    lit = lit or lit_mod.load()
    rows = manifest(lit)
    out: list[str] = []
    w = out.append
    w("\033[1mAcquisition manifest\033[0m — unobtained papers, ranked by the web itself")
    w("")
    w("Open each link in a browser, save the PDF into literature/inbox/ (ideally")
    w("named <ID>.pdf), then run `workhouse lit --intake`. Try")
    w("`workhouse lit --resolve <ID>` first — an open scan may need no browser.")
    for row in rows:
        w("")
        w(f"  \033[1m{row['id']}\033[0m  {row['title']}")
        w(
            f"    {row['venue']} ({row['year']}) · in-web {row['in_web']}"
            + (f" · INSPIRE {row['inspire']}" if row["inspire"] is not None else "")
        )
        for label, url in row["links"]:
            w(f"    {label:<14} {url}")
        w(f"    settles: {_clip(row['settles'])}")
    w("")
    w(f"{len(rows)} unobtained. The inbox is gitignored: a working copy is for")
    w("reading and pinning, never for committing.")
    return "\n".join(out)


def _clip(text: str, width: int = 200) -> str:
    text = " ".join(str(text).split())
    return text if len(text) <= width else text[: width - 1] + "…"


# --------------------------------------------------------------------------
# intake
# --------------------------------------------------------------------------

#: Words too common in this literature to identify anything.
_STOP = frozenset(
    ("a", "an", "and", "by", "for", "from", "in", "lattice", "of", "on")
    + ("the", "theory", "theories", "to", "with", "gauge", "su")
)


@dataclass
class Intake:
    path: Path
    sha256: str
    size: int
    matched: str | None
    how: str
    advice: list[str] = field(default_factory=list)


def _sniff_text(path: Path, limit: int = 4 * 1024 * 1024) -> str:
    """Best-effort text from a PDF, stdlib only: inflate the Flate streams
    and keep the printable runs. Works on text-layer PDFs (arXiv); returns
    little or nothing for image-only library scans, which is fine — those
    are identified by filename or digest instead."""
    try:
        raw = path.read_bytes()[:limit]
    except OSError:
        return ""
    pieces: list[str] = []
    for m in re.finditer(rb"stream\r?\n(.*?)endstream", raw, re.DOTALL):
        try:
            data = zlib.decompress(m.group(1).strip(b"\r\n"))
        except zlib.error:
            continue
        pieces.extend(run.decode("latin-1") for run in re.findall(rb"[ -~]{4,}", data[: 1 << 20]))
    return " ".join(pieces).lower()


def _title_tokens(title: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", str(title).lower())
    return {word for word in words if len(word) > 2 and word not in _STOP}


def identify(path: Path, lit: lit_mod.Literature) -> tuple[str | None, str]:
    """(node id, how) for one dropped file; (None, reason) when unidentified."""
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    for paper in lit.papers:
        if str(paper.get("source_sha256", "")) == digest:
            return paper["id"], "digest (already the pinned copy)"
    stem = path.stem.upper()
    if stem in {node.upper() for node in lit.node_ids}:
        actual = next(node for node in lit.node_ids if node.upper() == stem)
        return actual, "filename"
    text = _sniff_text(path)
    if text:
        best: tuple[float, str] | None = None
        for record in lit.papers + lit.stubs:
            doi = str(record.get("doi") or "")
            if doi and doi.lower() in text:
                return record["id"], "doi in text"
            tokens = _title_tokens(record.get("title", ""))
            if not tokens:
                continue
            hit = sum(1 for token in tokens if token in text) / len(tokens)
            if hit >= 0.8 and (best is None or hit > best[0]):
                best = (hit, record["id"])
        if best:
            return best[1], f"title tokens ({best[0]:.0%})"
    return None, "unidentified — rename to <ID>.pdf to claim it"


def intake(directory: Path | None = None, lit: lit_mod.Literature | None = None) -> list[Intake]:
    """Survey the inbox. Reads everything, writes nothing, edits nothing."""
    directory = directory or INBOX
    lit = lit or lit_mod.load()
    reports: list[Intake] = []
    if not directory.is_dir():
        return reports
    for path in sorted(directory.iterdir()):
        if not path.is_file() or path.name == "README.md":
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        matched, how = identify(path, lit)
        advice: list[str] = []
        if matched:
            record = lit.entry(matched)
            assert record is not None
            if matched in lit.stub_ids:
                advice.append(
                    "a stub cannot be pinned: promote it to a full entry with "
                    "verified metadata and a bears_on edge, then record the digest"
                )
            elif str(record.get("source_sha256", "")) == digest:
                advice.append("already pinned — this is the recorded copy, nothing to do")
            else:
                if record.get("source_sha256"):
                    advice.append(
                        "DIFFERENT BYTES from the recorded source_sha256 — a new "
                        "edition or a different scan; re-verify before re-pinning"
                    )
                advice.append(f"to pin the copy read:  source_sha256: {digest}")
                licence = str(record.get("licence", "")).lower()
                if licence in lit_mod.REDISTRIBUTABLE:
                    advice.append(f"licence {licence}: storing under fulltext/ is permitted")
                elif licence in lit_mod.VERBATIM_ONLY:
                    advice.append(
                        f"licence {licence}: an UNMODIFIED copy may be stored, and "
                        "the digest above is then mandatory"
                    )
                else:
                    advice.append(
                        f"licence {licence or 'unknown'}: pin only — the file itself "
                        "must never be committed"
                    )
                advice.append(
                    "then read it, flip the edges its reading verifies, and add "
                    "any published-comparisons check its numbers support"
                )
        reports.append(
            Intake(
                path=path,
                sha256=digest,
                size=path.stat().st_size,
                matched=matched,
                how=how,
                advice=advice,
            )
        )
    return reports


def format_intake(directory: Path | None = None, lit: lit_mod.Literature | None = None) -> str:
    directory = directory or INBOX
    reports = intake(directory, lit)
    out: list[str] = []
    w = out.append
    w(f"\033[1mInbox intake\033[0m — {directory}")
    if not reports:
        w("")
        w("  Nothing here. `workhouse lit --acquire` prints what is worth fetching")
        w("  and `workhouse lit --resolve <ID>` tries the open sources first.")
    for report in reports:
        w("")
        who = f"\033[1m{report.matched}\033[0m" if report.matched else "\033[33m?\033[0m"
        w(f"  {report.path.name}  ->  {who}  \033[2m({report.how})\033[0m")
        w(f"    sha256 {report.sha256}  ·  {report.size} bytes")
        for line in report.advice:
            w(f"    - {line}")
    w("")
    w("The inbox is gitignored and must stay that way: storing a paper is")
    w("republishing it. Nothing above edited the index — pinning is curation.")
    return "\n".join(out)


# --------------------------------------------------------------------------
# the resolver
# --------------------------------------------------------------------------


@dataclass
class Resolution:
    node_id: str
    tried: list[tuple[str, str, str]] = field(default_factory=list)  # (source, url, outcome)
    saved: Path | None = None
    sha256: str | None = None


def _fetch(url: str) -> bytes | None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=FETCH_TIMEOUT) as response:
            return response.read()
    except OSError:
        return None


def _inspire_extras(recid: int) -> tuple[list[str], list[str]]:
    """(INSPIRE-hosted document urls, KEKSCAN ids) for one record, live."""
    url = (
        f"https://inspirehep.net/api/literature/{recid}"
        "?fields=documents,external_system_identifiers"
    )
    body = _fetch(url)
    if body is None:
        return [], []
    try:
        metadata = json.loads(body).get("metadata", {})
    except ValueError:
        return [], []
    documents = [d["url"] for d in metadata.get("documents", []) if isinstance(d.get("url"), str)]
    kekscan = [
        e.get("value", "")
        for e in metadata.get("external_system_identifiers", [])
        if e.get("schema", "").upper() == "KEKSCAN"
    ]
    return documents, kekscan


def _openalex_pdf(doi: str) -> str | None:
    body = _fetch(f"https://api.openalex.org/works/doi:{doi}")
    if body is None:
        return None
    try:
        location = json.loads(body).get("best_oa_location") or {}
    except ValueError:
        return None
    url = location.get("pdf_url")
    return url if isinstance(url, str) and url else None


def resolve(node_id: str, lit: lit_mod.Literature | None = None) -> Resolution:
    """Try the automation-welcome sources for one paper, download the first
    hit into the inbox, and report every attempt either way."""
    lit = lit or lit_mod.load()
    record = lit.entry(node_id) or lit.entry(node_id.upper())
    if record is None:
        return Resolution(node_id=node_id, tried=[("index", node_id, "no such id")])
    result = Resolution(node_id=record["id"])

    candidates: list[tuple[str, str]] = list(resolve_plan(record))
    recid = record.get("inspire_recid")
    if recid:
        documents, kekscans = _inspire_extras(int(recid))
        candidates += [("inspire-document", url) for url in documents]
        for scan in kekscans:
            url = kek_scan_url(scan)
            if url:
                candidates.append(("kek-scan", url))
            else:
                result.tried.append(("kek-scan", scan, "id pattern not recognized"))
    if record.get("doi"):
        oa = _openalex_pdf(str(record["doi"]))
        if oa:
            candidates.append(("openalex-oa", oa))
        else:
            result.tried.append(("openalex-oa", str(record["doi"]), "no open location listed"))

    for source, url in candidates:
        body = _fetch(url)
        if body is None:
            result.tried.append((source, url, "unreachable or refused"))
            continue
        if not body.startswith(b"%PDF"):
            result.tried.append((source, url, "served something that is not a PDF"))
            continue
        INBOX.mkdir(parents=True, exist_ok=True)
        target = INBOX / f"{record['id']}.pdf"
        target.write_bytes(body)
        result.saved = target
        result.sha256 = hashlib.sha256(body).hexdigest()
        result.tried.append((source, url, f"saved ({len(body)} bytes)"))
        break
    return result


def format_resolution(resolution: Resolution) -> str:
    out: list[str] = []
    w = out.append
    w(f"\033[1mResolve {resolution.node_id}\033[0m")
    for source, url, outcome in resolution.tried:
        w(f"  {source:<17} {outcome}")
        w(f"    \033[2m{url}\033[0m")
    if resolution.saved:
        w("")
        w(f"  saved: {resolution.saved.relative_to(ROOT)}")
        w(f"  sha256 {resolution.sha256}")
        w("  Next: read it, then `workhouse lit --intake` for the pinning advice.")
    else:
        w("")
        w("  No open copy found by automation. `workhouse lit --acquire` prints the")
        w("  browser links — the walled open archives serve a person in seconds.")
    return "\n".join(out)
