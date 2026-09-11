"""Pair dossier: a mathematically informative comparison of two sources.

``workhouse discover connections`` names candidates but leaves an agent to open
both sources and work out what, if anything, they share. This module puts two
endpoints side by side: the located excerpt of each (path, lines, raw-byte
SHA-256), the exact tokens and terms both texts use, the regime, rank,
coupling, hypothesis and normalization markers a reviewer must compare, the
registered graph relations between them, and one heuristic proposal for the
kind of relationship together with the concrete checks that would confirm or
refute it.

Everything here is read-only over the checkout, the saved graph and the
disposable discovery cache. Nothing is written under ``ledger/``, ``index/``
or any source root, no check is executed, and no proposal is a dependency,
a proof or evidence: ``meaning`` says so on every result, and the confidence
vocabulary stops at ``medium`` because pattern matching cannot establish a
mathematical relationship. Status, evidence and tier are copied from records
verbatim and never derived.

Kind suggestion rules, tried in order (the first that fires wins; each names
the failure it prevents):

1. ``unrelated`` when the texts share fewer than two exact tokens and fewer
   than three terms, neither cites the other and no edge is registered. A
   lone common word must not read as a connection.
2. ``documentary`` when one text cites the other's file or record id, or the
   only registered relations are citation, containment or provenance edges.
   A citation is not a mathematical dependency.
3. ``disagreement`` when a shared symbol or shared exact rational carries
   different numeric neighbours in the two texts, or a shared rational
   appears with the opposite sign in one text only. Both values must be
   reproduced under one convention before anything is recorded; a
   normalization difference is the usual explanation.
4. ``literature-bearing`` when exactly one endpoint comes from the
   ``literature`` or ``paper`` family and nothing is registered between
   them. The registrable relation is a literature ``bears_on`` with a
   relation and status, not a dependency.
5. ``scope-restriction`` when the texts share a symbol but their detected
   regime or rank markers are disjoint (finite lattice against the
   thermodynamic limit, SU(2) against SU(N)). Reusing a bound across that
   boundary is the failure this catches.
6. ``equivalent-construction`` when both texts carry construction cues and
   share at least three symbols with symbol-set Jaccard at least 0.5. A
   unifying candidate needs a falsifier before registration.
7. ``compatible-hypothesis`` when both texts have hypothesis cue lines that
   share a symbol. Compatible hypotheses register as ``bears_on``, never
   ``depends_on``.
8. ``shared-operator`` when the texts share at least one symbol-like token.
   Shared vocabulary is not a dependency (ADR 0007).
9. ``reusable-ingredient`` when the texts share at least three terms but no
   symbol. ``depends_on`` requires confirming the ingredient is used.
10. ``unrelated`` otherwise; a registered non-documentary edge with no text
    signal falls back to the kind its edge class implies and says so.
"""

from __future__ import annotations

import contextlib
import hashlib
import inspect
import json
import re
import sqlite3
import sys
import textwrap
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

from .discovery_index import tokenize
from .discovery_present import MIN_EXCERPT_CHARS, excerpt, provenance_summary

SCHEMA = "workhouse-discovery/pair/v1"
ERROR_SCHEMA = "workhouse-discovery/error/v1"
PAIR_EXCERPT_CHARS = 900
MAX_EXCERPT_CHARS = 20000
MAX_TEXT_CHARS = 200_000
MEANING = "heuristic comparison for review; not evidence, not a dependency"
LEXICON_PATH = "graph-tasks/discovery/lexicon.yaml"
KINDS = (
    "shared-operator",
    "compatible-hypothesis",
    "reusable-ingredient",
    "equivalent-construction",
    "scope-restriction",
    "disagreement",
    "literature-bearing",
    "documentary",
    "unrelated",
)
CONFIDENCE = ("low", "medium")
# Where each kind may land by hand after review (ledger surfaces only; no new
# graph edge types). Discovery never applies these itself.
REGISTRABLE_AS = {
    "shared-operator": "no scientific edge; ledger/symbols.yaml claims/code_names if the "
    "operator is a named symbol, otherwise the review register only",
    "compatible-hypothesis": "bears_on (results.yaml, documents.yaml, a route or a study link); "
    "never depends_on",
    "reusable-ingredient": "depends_on on a RESULT or DERIV once the reviewer confirms the "
    "input is used in the argument; lean_support {name, scope} for a covered piece; else bears_on",
    "equivalent-construction": "gaps.yaml unifying_candidates (U-id, status conjectured, "
    "falsifier mandatory); a naming identity goes to ledger/symbols.yaml",
    "scope-restriction": "route cannot_decide, results.yaml supported_by scope text, "
    "derivation_statements remaining, or documents.yaml superseded_by",
    "disagreement": "literature bears_on relation contradicts, route cannot_decide, or a refuted "
    "unifying candidate; never a new C-id (tests pin C1-C22)",
    "literature-bearing": "literature/index.yaml bears_on {target, relation, status, detail} or "
    "a STUDY link",
    "documentary": "documents.yaml cites/bears_on; carries no mathematical dependency",
    "unrelated": "nothing",
}
FAMILY_PREFIXES = (
    ("docs/derivations/", "derivations"),
    ("theory/", "historical theory"),
    ("corpus-import/", "corpus-import"),
    ("notes/", "notes"),
    ("literature/", "literature"),
    ("paper/", "paper"),
    ("research/", "research"),
    ("docs/research/", "research"),
)
FAMILY_BY_ID = {
    "NOTE": "notes",
    "LIT": "literature",
    "STUDY": "literature",
    "CORPUS": "corpus-import",
    "DOC": "corpus-import",
    "ARCHIVE": "corpus-import",
}
SOURCE_FAMILIES = frozenset(label for _prefix, label in FAMILY_PREFIXES)
LITERATURE_FAMILIES = frozenset({"literature", "paper"})
DOCUMENTARY_TYPES = frozenset(
    {
        "cites",
        "contains",
        "mentions",
        "provenance",
        "pinned_as",
        "originates",
        "navigation",
        "labels",
    }
)
DEPENDENCY_TYPES = frozenset(
    {"depends_on", "rests_on", "supported_by", "formalizes", "promotes", "uses", "yields"}
)
REGIME_PHRASES = {
    "finite lattice": (
        "finite volume",
        "finite-volume",
        "finite lattice",
        "finite periodic",
        "fixed square",
        "compact square",
        "fixed lattice",
        "finite box",
        "single plaquette",
    ),
    "infinite volume/thermodynamic limit": (
        "thermodynamic limit",
        "infinite volume",
        "infinite-volume",
        "volume-uniform",
        "uniform in the volume",
        "uniform in volume",
        "uniformly in the volume",
        "l to infinity",
        "l tends to infinity",
    ),
    "continuum": ("continuum limit", "continuum", "lattice spacing", "a tends to zero", "a to 0"),
    "physical observable": (
        "physical mass",
        "physical observable",
        "physical gap",
        "mass gap",
        "glueball mass",
        "string tension",
    ),
}
RANK_PATTERNS = (
    ("SU(2)", r"\bsu\(?2\)?(?![a-z0-9])"),
    ("SU(3)", r"\bsu\(?3\)?(?![a-z0-9])"),
    ("SU(N)", r"\bsu\(?n\)?(?![a-z0-9])"),
    ("N=3", r"\bn\s*=\s*3(?![0-9])"),
    (
        "symbolic N",
        r"\b(?:symbolic|general|arbitrary|every|all|large)\s+n\b|\bq\(n\)|\bn-dependent\b"
        r"|\brank\s+n\b",
    ),
)
COUPLING_BASES = frozenset({"g", "beta", "u"})
NORMALIZATION_PATTERNS = (
    ("normalized", r"\bnormali[sz](?:ed|ation|ations|e|es|ing)\b"),
    ("convention", r"\bconventions?\b"),
    ("factor", r"\bfactors?\b"),
    ("1/2", r"(?<![\d/.])1\s*/\s*2(?![\d/])"),
    ("2pi", r"(?<![a-z0-9])2\s*\\?pi\b"),
)
_CUE = re.compile(
    r"\b(assum(?:e|es|ed|ing|ption|ptions)|hypothes[ie]s|provided|under|requires?|required"
    r"|if and only if|for all|uniform(?:ly)? in)\b",
    re.I,
)
_CONSTRUCTION = re.compile(
    r"\b(?:construct(?:ion|ions|ed|s)?|define[sd]?|definition|realization|realized|realisation"
    r"|representation|isomorphi(?:c|sm)|identif(?:y|ied|ication))\b",
    re.I,
)
_EXTENSION = re.compile(r"\.(?:md|tex|txt|py|lean|ya?ml|jsonl?)(?= \(|#|:\d|$)", re.I)
_LOCATOR = re.compile(r"^(?P<path>.+?):(?P<first>\d+)(?:-(?P<last>\d+))?$")
_ABSOLUTE = re.compile(r"^(?:[A-Za-z]:[/\\]|[/\\])")
_RATIONAL = re.compile(r"^-?\d+/\d+$")
_DECIMAL = re.compile(r"^-?(?:\d+\.\d+|\.\d+)(?:e[+-]?\d+)?$|^-?\d+e[+-]?\d+$")
_INTEGER = re.compile(r"^-?\d+$")
_GREEK_NAMES = [
    "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta",
    "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi",
    "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega",
]  # fmt: skip
_GREEK = dict(zip("αβγδεζηθικλμνξοπρστυφχψω", _GREEK_NAMES, strict=True))
_GREEK_SET = frozenset(_GREEK_NAMES)
MAX_CUE_LINES = 8
MAX_CONFLICTS = 10


# ---------------------------------------------------------------------------
# Read-only access to the discovery cache


def _connection(index) -> sqlite3.Connection | None:
    connection = getattr(index, "_connection", None)
    return connection if isinstance(connection, sqlite3.Connection) else None


def chunk_by_id(index, chunk_id: str) -> dict | None:
    """One indexed chunk (record row or source passage) by its id, or ``None``.

    Reads the cache's ``chunks`` table only; it opens nothing and rebuilds
    nothing, so a pair query cannot trigger an index rebuild as a side effect.
    """
    connection = _connection(index)
    if connection is None:
        return None
    try:
        row = connection.execute("SELECT data FROM chunks WHERE id = ?", (chunk_id,)).fetchone()
    except sqlite3.Error:
        return None
    return json.loads(row[0]) if row else None


def _chunks_containing(index, needle: str) -> list[dict]:
    connection = _connection(index)
    if connection is None:
        return []
    try:
        rows = connection.execute(
            "SELECT data FROM chunks WHERE instr(data, ?) > 0 ORDER BY rowid", (needle,)
        ).fetchall()
    except sqlite3.Error:
        return []
    return [json.loads(raw) for (raw,) in rows]


def chunks_for_path(index, path: str, first: int | None = None, last: int | None = None) -> list:
    """Indexed passages of one source path, optionally overlapping a line range.

    The serialized chunk carries ``"path":"..."`` verbatim, so a substring
    prefilter narrows 27k rows in tens of milliseconds before the exact path
    and range test; a similarly named file cannot slip through the prefilter
    because the exact comparison follows.
    """
    needle = '"path":' + json.dumps(path, ensure_ascii=True)
    rows = []
    for row in _chunks_containing(index, needle):
        if row.get("path") != path or row.get("kind") != "passage":
            continue
        start, end = int(row.get("start_line", 1)), int(row.get("end_line", 1))
        if first is not None and last is not None and (end < first or start > last):
            continue
        rows.append(row)
    return rows


def chunks_for_claim(index, claim_id: str) -> list[dict]:
    """Source passages whose registered claim links include ``claim_id``."""
    needle = json.dumps(claim_id, ensure_ascii=True)
    return [
        row
        for row in _chunks_containing(index, needle)
        if row.get("kind") == "passage" and claim_id in (row.get("claim_ids") or [])
    ]


def _corpus_document_frequency(index, terms: list[str]) -> dict[str, int] | None:
    """Chunk counts per term from the FTS table, or ``None`` when unavailable."""
    connection = _connection(index)
    if connection is None:
        return None
    counts = {}
    try:
        for term in terms:
            key = "x" + term.encode("utf-8").hex()
            counts[term] = connection.execute(
                "SELECT count(*) FROM search WHERE search MATCH ?", (key,)
            ).fetchone()[0]
    except sqlite3.Error:
        return None
    return counts


# ---------------------------------------------------------------------------
# Endpoint resolution


def parse_locator(spec: str) -> dict:
    """Parse ``path:first[-last]`` or ``ext:<label>/path:first[-last]``.

    Only the trailing ``:digits[-digits]`` is a locator, so ``#`` and ``(2)``
    stay filename characters. Absolute paths and ``..`` segments are refused
    because an endpoint must lie inside the checkout or a declared external
    root; otherwise a dossier could hash and quote an arbitrary file.
    """
    body = spec.strip().replace("\\", "/")
    external = None
    if body.lower().startswith("ext:"):
        label, separator, rest = body[4:].partition("/")
        if not label or not separator or not rest:
            raise ValueError("external locator must read ext:<label>/<path>:<first>[-<last>]")
        if not re.fullmatch(r"[A-Za-z0-9._-]+", label):
            raise ValueError(f"external root label must be [A-Za-z0-9._-]+: {label!r}")
        external, body = label, rest
    match = _LOCATOR.match(body)
    if not match:
        raise ValueError(
            f"not a record id, PASSAGE id or locator 'path:first[-last]': {spec.strip()!r}"
        )
    path, first = match["path"], int(match["first"])
    last = int(match["last"] or first)
    if first < 1 or last < first:
        raise ValueError(f"locator lines must satisfy 1 <= first <= last: {spec.strip()!r}")
    if _ABSOLUTE.match(path) or any(part in ("", "..") for part in path.split("/")):
        raise ValueError(f"locator path must be checkout-relative without '..': {path!r}")
    return {"path": path, "first": first, "last": last, "external": external}


def parse_where(where: str) -> tuple[str, tuple[int, int] | None]:
    """Split a record's ``where`` into its file path and an optional line range.

    Text after the first complete filename extension is a locator: a section
    heading, ``lines a-b``, ``:line`` or ``#anchor``. A literal ``#`` or
    ``(2)`` in the filename precedes the extension and is preserved.
    """
    where = where.replace("\\", "/").strip()
    match = _EXTENSION.search(where)
    if not match:
        return where, None
    path, suffix = where[: match.end()], where[match.end() :]
    bounds = re.search(r"\blines?\s+(\d+)(?:\s*[-–]\s*(\d+))?", suffix) or re.fullmatch(
        r":(\d+)(?:[-–:](\d+))?", suffix
    )
    if not bounds:
        return path, None
    first = int(bounds[1])
    last = int(bounds[2] or bounds[1])
    return path, (first, max(first, last))


def family_label(path: str | None, record_id: str | None = None, external: str | None = None):
    """Closed family vocabulary: where a text comes from, never what it proves."""
    if external:
        return f"external:{external}"
    lowered = (path or "").lower()
    for prefix, label in FAMILY_PREFIXES:
        if lowered.startswith(prefix):
            return label
    if record_id:
        return FAMILY_BY_ID.get(record_id.split(":", 1)[0], "catalogue")
    return "catalogue"


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _read_within(root: Path, relative: str) -> tuple[bytes, str] | None:
    """Bytes and normalized text of ``relative`` under ``root``, or ``None``.

    Containment is checked on the resolved path so a link or ``..`` cannot
    reach outside the root; the raw bytes are hashed before line endings are
    normalized, so the reported digest matches the index's passage hashes.
    """
    candidate = root / relative
    try:
        if candidate.is_symlink() or not candidate.resolve().is_relative_to(root.resolve()):
            return None
        if not candidate.is_file():
            return None
        raw = candidate.read_bytes()
    except (OSError, RuntimeError):
        return None
    text = raw.decode("utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
    return raw, text


def _slice(text: str, first: int, last: int) -> tuple[str, int]:
    lines = text.splitlines(keepends=True)
    return "".join(lines[first - 1 : last]), len(lines)


def _external_root(engine, label: str) -> Path | None:
    """Directory an ``ext:<label>/`` locator resolves to, or ``None``.

    The index's declared scope (``graph-tasks/discovery/scope.yaml`` resolved
    against the workstation base) is authoritative; a plain
    ``external_roots`` mapping on the engine or index is accepted for
    tests and batch sessions. An unknown label yields ``None`` so the dossier
    reports the source as unavailable instead of reading a guessed path.
    """
    index = getattr(engine, "index", None)
    scope = getattr(index, "scope", None)
    base = getattr(scope, "base", None)
    if base is not None:
        for root in getattr(scope, "enabled_roots", ()):
            if getattr(root, "label", None) == label:
                relative = getattr(root, "path", ".")
                return Path(base) if relative == "." else Path(base) / relative
    for holder in (index, engine):
        roots = getattr(holder, "external_roots", None)
        if isinstance(roots, dict) and label in roots:
            return Path(roots[label])
    return None


def _cap(text: str) -> tuple[str, bool]:
    if len(text) <= MAX_TEXT_CHARS:
        return text, False
    return text[:MAX_TEXT_CHARS], True


def _record_summary(record: dict) -> dict:
    detail = str(record.get("detail") or "")
    hypotheses = re.search(r"Hypotheses?:\s*(.+)", detail)
    scope = re.search(r"Scope:\s*(.+)", detail)
    summary = {
        "id": record.get("id"),
        "kind": record.get("kind"),
        "status": record.get("status"),
        "evidence": record.get("evidence"),
        "tier": record.get("tier"),
        "where": record.get("where"),
        "statement": str(record.get("statement") or "")[:600],
        "detail_chars": len(detail),
    }
    if hypotheses:
        summary["hypotheses"] = hypotheses[1].strip()[:600]
    if scope:
        summary["scope"] = scope[1].strip()[:400]
    return {key: value for key, value in summary.items() if value not in (None, "")}


RECORD_TEXT_FIELDS = ("statement", "hypotheses", "scope")


def _record_text(endpoint: dict) -> str:
    """Catalogue wording that joins the located text for markers and tokens."""
    record = endpoint.get("record") or {}
    return "\n".join(str(record.get(key) or "") for key in RECORD_TEXT_FIELDS)


def _record_endpoint(engine, record_id: str) -> dict:
    record = engine.records[record_id]
    where = str(record.get("where") or "")
    path, bounds = parse_where(where) if where else ("", None)
    fields = "\n".join(str(record.get(key) or "") for key in ("statement", "detail"))
    endpoint = {
        "id_or_locator": record_id,
        "kind": "record",
        "id": record_id,
        "family": family_label(path, record_id),
        "record": _record_summary(record),
        "claim_ids": [record_id],
        "source": {"path": path or None, "lines": None, "sha256": None, "available": False},
        "_text": fields,
        "_base_line": None,
        "text_scope": "record statement and detail",
    }
    passages = chunks_for_claim(engine.index, record_id) if path else []
    if bounds is None and passages:
        spans = [
            span
            for row in passages
            for claim, span in (row.get("claim_spans") or {}).items()
            if claim == record_id and span.get("scope") == "registered_lines"
        ]
        if spans:
            bounds = (
                min(int(span["start_line"]) for span in spans),
                max(int(span["end_line"]) for span in spans),
            )
    if not path:
        endpoint["source"]["reason"] = "record has no source location"
        return endpoint
    located = _read_within(engine.root, path)
    if located is None and family_label(path, record_id) == "notes":
        # NOTE records cite archive-relative paths; the byte-verified import
        # lives under notes/imported/.
        alternative = "notes/imported/" + path
        located = _read_within(engine.root, alternative)
        if located is not None:
            path = alternative
    endpoint["source"]["path"] = path
    if located is None:
        endpoint["source"]["reason"] = "source path is not a readable file in the checkout"
        return endpoint
    raw, text = located
    endpoint["source"].update(sha256=_sha(raw), available=True, bytes=len(raw))
    if passages:
        index_hashes = {row.get("source_sha256") for row in passages}
        endpoint["source"]["index_sha256_match"] = index_hashes == {_sha(raw)}
    line_count = len(text.splitlines())
    if bounds is not None:
        first, last = bounds
        if last > line_count:
            endpoint["source"]["reason"] = (
                f"registered lines {first}-{last} exceed the file's {line_count} lines"
            )
            return endpoint
        window, _ = _slice(text, first, last)
        endpoint["source"]["lines"] = [first, last]
        endpoint["_text"] = window
        endpoint["_base_line"] = first
        endpoint["text_scope"] = "registered source lines"
    elif endpoint["family"] in SOURCE_FAMILIES:
        capped, truncated = _cap(text)
        endpoint["source"]["lines"] = [1, line_count]
        endpoint["_text"] = capped
        endpoint["_base_line"] = 1
        endpoint["text_scope"] = "whole source document" + (" (capped)" if truncated else "")
    else:
        endpoint["text_scope"] = (
            "record statement and detail; the located file is a catalogue, not a passage"
        )
    return endpoint


def _passage_endpoint(engine, passage_id: str) -> dict:
    row = chunk_by_id(engine.index, passage_id)
    if row is None or row.get("kind") != "passage":
        raise ValueError(f"unknown PASSAGE id (not a passage in the discovery cache): {passage_id}")
    path = str(row.get("path") or "")
    first, last = int(row.get("start_line", 1)), int(row.get("end_line", 1))
    text = str(row.get("text") or "").replace("\r\n", "\n").replace("\r", "\n")
    external = path.split("/", 1)[0][4:] if path.lower().startswith("ext:") else None
    endpoint = {
        "id_or_locator": passage_id,
        "kind": "passage",
        "id": passage_id,
        "locator": f"{path}:{first}-{last}",
        "family": family_label(path, external=external),
        "claim_ids": list(row.get("claim_ids") or []),
        "source": {
            "path": path,
            "lines": [first, last],
            "sha256": row.get("source_sha256"),
            "available": True,
            "external": external,
            "scope": "indexed passage text",
        },
        "_text": text,
        "_base_line": first,
        "text_scope": "indexed passage",
    }
    located = None if external else _read_within(engine.root, path)
    if located is not None:
        endpoint["source"]["on_disk_sha256_match"] = _sha(located[0]) == row.get("source_sha256")
    return endpoint


def _locator_endpoint(engine, spec: str, locator: dict) -> dict:
    path, first, last = locator["path"], locator["first"], locator["last"]
    external = locator["external"]
    indexed_path = f"ext:{external}/{path}" if external else path
    endpoint = {
        "id_or_locator": spec.strip(),
        "kind": "passage",
        "id": None,
        "locator": f"{indexed_path}:{first}-{last}",
        "family": family_label(path, external=external),
        "claim_ids": [],
        "source": {
            "path": indexed_path,
            "lines": [first, last],
            "sha256": None,
            "available": False,
            "external": external,
        },
        "_text": "",
        "_base_line": first,
        "text_scope": "located source lines",
    }
    root = _external_root(engine, external) if external else engine.root
    located = _read_within(root, path) if root is not None else None
    overlapping = chunks_for_path(engine.index, indexed_path, first, last)
    if located is not None:
        raw, text = located
        window, line_count = _slice(text, first, last)
        if last > line_count:
            raise ValueError(f"locator {spec.strip()!r} exceeds the file's {line_count} line(s)")
        endpoint["source"].update(sha256=_sha(raw), available=True, bytes=len(raw))
        endpoint["_text"] = window
        if overlapping:
            hashes = {row.get("source_sha256") for row in overlapping}
            endpoint["source"]["index_sha256_match"] = hashes == {_sha(raw)}
    elif overlapping:
        # The bytes are not readable here (an external root that this engine
        # does not mount); the indexed passages still carry the text.
        pieces = []
        for row in overlapping:
            start = int(row.get("start_line", 1))
            lines = str(row.get("text") or "").splitlines(keepends=True)
            for number, line in enumerate(lines, start):
                if first <= number <= last:
                    pieces.append((number, line))
        text = "".join(line for _number, line in sorted(dict(pieces).items()))
        endpoint["_text"] = text.replace("\r\n", "\n").replace("\r", "\n")
        endpoint["source"].update(
            sha256=sorted({row.get("source_sha256") for row in overlapping})[0],
            available=True,
            scope="reconstructed from indexed passages; file bytes not readable here",
        )
    else:
        endpoint["source"]["reason"] = (
            f"external root {external!r} is not mounted by this engine and the path is not indexed"
            if external
            else "path is not a readable file in the checkout and is not indexed"
        )
    claim_ids = set()
    for row in overlapping:
        spans = row.get("claim_spans") or {}
        for claim in row.get("claim_ids") or []:
            span = spans.get(claim) or {}
            start = int(span.get("start_line", row.get("start_line", 1)))
            end = int(span.get("end_line", row.get("end_line", start)))
            if end >= first and start <= last:
                claim_ids.add(claim)
    endpoint["claim_ids"] = sorted(claim_ids)
    return endpoint


def resolve_endpoint(engine, spec: str) -> dict:
    """A record id, a ``PASSAGE:`` id, or a line locator; nothing is invented."""
    spec = spec.strip()
    if not spec:
        raise ValueError("an endpoint must be a record id, PASSAGE id or path:first-last")
    if spec in engine.records:
        return _record_endpoint(engine, spec)
    if spec.startswith("PASSAGE:"):
        return _passage_endpoint(engine, spec)
    return _locator_endpoint(engine, spec, parse_locator(spec))


# ---------------------------------------------------------------------------
# Shared tokens, markers and conflicts


def token_class(token: str) -> str | None:
    """rational | integer | symbol | term | None.

    Bare integers are line numbers and dates as often as values, so they
    count only as numeric neighbours in conflict detection, never as shared
    exact tokens.
    """
    if _RATIONAL.match(token) or _DECIMAL.match(token):
        return "rational"
    if _INTEGER.match(token):
        return "integer"
    if token in _GREEK_SET or len(token) == 1:
        return "symbol"
    if any(ch in token for ch in "_^'") or any(ch.isdigit() for ch in token):
        return "symbol"
    if len(token) >= 3 and token.isalpha():
        return "term"
    return None


def clean_tokens(tokens: list[str]) -> list[str]:
    """Drop the trailing ``_``/``^`` the tokenizer leaves on ``g^{-2}`` or ``C_{0}``.

    The index tokenizer stops at a brace, so LaTeX subscripts and
    superscripts yield stubs such as ``g^`` and ``c_``; two texts sharing a
    stub share a spelling accident, not a symbol.
    """
    return [cleaned for token in tokens if (cleaned := token.rstrip("_^'")) or token]


def _structured(token: str) -> bool:
    """A symbol with subscript, superscript, digit or a Greek name.

    Single letters are mostly LaTeX noise (``d\\mu``, ``e^{-x}``,
    ``\\mathrm``), so they are reported separately as weak evidence and never
    carry a value conflict.
    """
    if len(token) < 2:
        return False
    return (
        token in _GREEK_SET or any(ch in token for ch in "_^") or any(ch.isdigit() for ch in token)
    )


def shared_tokens(tokens_a: list[str], tokens_b: list[str], index=None) -> dict:
    """Exact tokens and terms present in both texts.

    Terms rank by corpus rarity when the FTS table is reachable (a word in
    few chunks is a better join key than a frequent one) and by two-text
    frequency otherwise; the output names which ranking was used.
    """
    counts_a, counts_b = Counter(tokens_a), Counter(tokens_b)
    common = sorted(counts_a.keys() & counts_b.keys())
    symbols = [token for token in common if token_class(token) == "symbol" and _structured(token)]
    single = [token for token in common if token_class(token) == "symbol" and len(token) == 1]
    rationals = [token for token in common if token_class(token) == "rational"]
    terms = [token for token in common if token_class(token) == "term"]
    symbols_a = {t for t in counts_a if token_class(t) == "symbol" and _structured(t)}
    symbols_b = {t for t in counts_b if token_class(t) == "symbol" and _structured(t)}
    union = symbols_a | symbols_b
    frequency = _corpus_document_frequency(index, terms[:300]) if len(terms) > 1 else None
    if frequency:
        ranked = sorted(terms, key=lambda t: (frequency.get(t, 0), counts_a[t] + counts_b[t], t))
        ranking = "corpus chunk frequency, ascending"
    else:
        ranked = sorted(terms, key=lambda t: (counts_a[t] + counts_b[t], t))
        ranking = "two-text frequency, ascending"
    top = ranked[:20]
    return {
        "exact_tokens": (rationals + symbols)[:60],
        "exact_token_count": len(rationals) + len(symbols),
        "symbols": symbols[:60],
        "single_letters": single[:26],
        "rationals": rationals[:40],
        "terms": top,
        "term_count": len(terms),
        "term_ranking": ranking,
        "term_counts": {
            term: {
                "a": counts_a[term],
                "b": counts_b[term],
                **({"corpus": frequency[term]} if frequency else {}),
            }
            for term in top
        },
        "symbol_jaccard": round(len(symbols_a & symbols_b) / len(union), 3) if union else 0.0,
    }


def _normalized(text: str) -> str:
    return "".join(_GREEK.get(ch.lower(), ch) for ch in text.replace("−", "-")).lower()


def _coupling_tokens(tokens: list[str]) -> list[str]:
    found = []
    for token in dict.fromkeys(clean_tokens(tokens)):
        base = re.split(r"[_^']", token, maxsplit=1)[0]
        if base in COUPLING_BASES and token not in found:
            found.append(token)
    return sorted(found)[:8]


def _line_symbols(line: str) -> list[str]:
    """Structured symbols on one line; the preview text is cut at 200 characters,
    and a hypothesis line in a ledger record is often longer than that."""
    tokens = clean_tokens(tokenize(line))
    return sorted({t for t in tokens if token_class(t) == "symbol" and _structured(t)})[:12]


def detect_markers(endpoint: dict) -> dict:
    """Rule-based regime, rank, coupling, hypothesis and normalization cues.

    Detection is literal phrase matching on the endpoint's text, so it can
    miss a regime stated in other words and it cannot read a hypothesis; the
    cue lines are quoted with line numbers so the reviewer reads the source.
    """
    text = endpoint.get("_text") or ""
    extra = _record_text(endpoint) if endpoint.get("kind") == "record" else ""
    lowered = _normalized(text + "\n" + extra)
    tokens = clean_tokens(tokenize(text + "\n" + extra))
    regime = [
        label
        for label, phrases in REGIME_PHRASES.items()
        if any(phrase in lowered for phrase in phrases)
    ]
    rank = [label for label, pattern in RANK_PATTERNS if re.search(pattern, lowered)]
    coupling = _coupling_tokens(tokens)
    if re.search(r"(?<![a-z])l\s*=", lowered):
        coupling.append("L=")
    cues = []
    base = endpoint.get("_base_line")
    for number, line in enumerate(text.splitlines(), 1):
        match = _CUE.search(line)
        if match and line.strip():
            cues.append(
                {
                    "line": base + number - 1 if base else None,
                    "cue": match[1].lower(),
                    "text": line.strip()[:200],
                    "symbols": _line_symbols(line),
                }
            )
    for line in extra.splitlines():
        match = _CUE.search(line)
        if match and line.strip():
            cues.append(
                {
                    "line": None,
                    "in": "record",
                    "cue": match[1].lower(),
                    "text": line.strip()[:200],
                    "symbols": _line_symbols(line),
                }
            )
    normalization = {}
    for label, pattern in NORMALIZATION_PATTERNS:
        hits = re.findall(pattern, lowered)
        if hits:
            normalization[label] = len(hits)
    return {
        "regime": regime,
        "rank": rank,
        "coupling": coupling,
        "hypothesis_cues": cues[:MAX_CUE_LINES],
        "hypothesis_cue_count": len(cues),
        "normalization": normalization,
        "construction_cues": bool(_CONSTRUCTION.search(lowered)),
        "semantics": "literal phrase detection; absence of a marker is not absence of a hypothesis",
    }


def _neighbours(tokens: list[str], target: str, radius: int) -> set[str]:
    found = set()
    for position, token in enumerate(tokens):
        if token != target:
            continue
        for other in tokens[max(0, position - radius) : position + radius + 1]:
            if other != target and token_class(other) in ("rational", "integer"):
                found.add(other)
    return found


_VALUE = r"(-?\d+(?:\s*/\s*\d+|\.\d+)?)(?![\d/]|\.\d)"
_EQUALS = r"\s*&?\s*(?:=|:=|\\equiv|\\approx|\\simeq|≈)\s*(?:\\left)?\(?\s*"


def _symbol_pattern(token: str) -> str:
    """Regex for a token as it appears in (normalized) source text.

    ``c_0`` must also match ``C_{0}`` and ``beta_n`` must match ``\\beta_{n}``,
    otherwise the stated value of a braced subscript is invisible.
    """
    parts = re.split(r"([_^])", token)
    pattern = r"\\?" + re.escape(parts[0])
    for position in range(1, len(parts), 2):
        operator = parts[position]
        operand = parts[position + 1] if position + 1 < len(parts) else ""
        pattern += re.escape(operator) + r"\{?" + re.escape(operand) + r"\}?"
    return r"(?<![a-z0-9_^\\])" + pattern + r"(?![a-z0-9_^])"


def stated_values(text: str, token: str) -> set[str]:
    """Numeric values the text assigns to ``token`` with ``=`` or an equivalent.

    Only explicit assignments count: ``0<g<g_*`` states a bound, not a
    value, and treating every nearby number as a value flagged the coupling
    ``g`` as disputed in the first real dossier.
    """
    values = set()
    for match in re.finditer(_symbol_pattern(token) + _EQUALS + _VALUE, text):
        raw = re.sub(r"\s+", "", match[1])
        if "/" in raw:
            numerator, denominator = raw.split("/")
            with contextlib.suppress(ValueError, ZeroDivisionError):
                raw = str(Fraction(int(numerator), int(denominator)))
        values.add(raw)
    return values


def value_conflicts(
    text_a: str, text_b: str, tokens_a: list[str], tokens_b: list[str], shared: dict
) -> list[dict]:
    """Shared carriers assigned different values, and sign flips.

    A carrier is a shared structured symbol or coupling name with a stated
    value in both texts, or a shared exact rational whose numeric
    neighbours (within three tokens) are disjoint. Disjoint values are a
    candidate disagreement, not a contradiction: the two texts may use
    different normalizations, which is exactly what the reviewer must settle.
    """
    conflicts = []
    norm_a, norm_b = _normalized(text_a), _normalized(text_b)
    for symbol in shared["symbols"] + [s for s in shared["single_letters"] if s in COUPLING_BASES]:
        values_a, values_b = stated_values(norm_a, symbol), stated_values(norm_b, symbol)
        if values_a and values_b and values_a.isdisjoint(values_b):
            conflicts.append(
                {
                    "carrier": symbol,
                    "basis": "stated values differ",
                    "a": sorted(values_a),
                    "b": sorted(values_b),
                }
            )
    set_a, set_b = set(tokens_a), set(tokens_b)
    for rational in shared["rationals"]:
        values_a, values_b = _neighbours(tokens_a, rational, 3), _neighbours(tokens_b, rational, 3)
        if values_a and values_b and values_a.isdisjoint(values_b):
            conflicts.append(
                {
                    "carrier": rational,
                    "basis": "shared rational with disjoint numeric neighbours",
                    "a": sorted(values_a),
                    "b": sorted(values_b),
                }
            )
        negated = rational[1:] if rational.startswith("-") else "-" + rational
        if (negated in set_a) != (negated in set_b):
            conflicts.append(
                {
                    "carrier": rational,
                    "basis": "opposite sign present in one text only",
                    "a": sorted({rational, negated} & set_a),
                    "b": sorted({rational, negated} & set_b),
                }
            )
    return conflicts[:MAX_CONFLICTS]


def documentary_citations(a: dict, b: dict) -> list[dict]:
    """Does either text name the other's file or record id?"""
    citations = []
    for side, this, other in (("a", a, b), ("b", b, a)):
        haystack = (this.get("_text") or "").lower()
        if this.get("kind") == "record":
            record = this.get("record") or {}
            haystack += "\n" + str(record.get("statement") or "").lower()
        names = []
        if other.get("id"):
            names.append(other["id"])
        path = (other.get("source") or {}).get("path") or ""
        if path:
            names.append(Path(path).name)
            stem = Path(path).stem
            if len(stem) >= 8:
                names.append(stem)
        for name in names:
            if name and name.lower() in haystack:
                citations.append({"in": side, "cites": name})
                break
    return citations


# ---------------------------------------------------------------------------
# Graph relations


def _path_summary(result: dict) -> dict:
    steps = []
    for step in (result.get("paths") or [[]])[0]:
        edge = step.get("edge", {})
        arrow = "->" if step.get("direction") == "forward" else "<-"
        steps.append(
            f"{step.get('from')} {arrow}[{edge.get('type')} {edge.get('how')}] {step.get('to')}"
        )
    return {
        "found": bool(result.get("paths")),
        "steps": steps,
        "truncated": bool(result.get("truncated")),
        "truncation_reasons": list(result.get("truncation_reasons") or []),
        "mode": result.get("mode"),
    }


def graph_relations(engine, a: dict, b: dict) -> dict:
    """Registered edges, witnesses and bounded paths between the endpoints.

    Records compare directly; a passage is represented by the claim ids the
    index maps it to. Every edge is one the graph already records, so this
    section can only confirm what is registered, never add to it.
    """
    graph = engine.graph
    out: dict[str, Any] = {
        "existing_relations": [],
        "shared_witnesses": [],
        "shared_witness_count": 0,
        "exploratory_path": None,
        "dependency_path": None,
        "claim_links": [],
        "shared_claim_ids": [],
        "semantics": "registered edges only; a retrieval path is not a dependency claim",
    }
    record_a = a["id"] if a["kind"] == "record" else None
    record_b = b["id"] if b["kind"] == "record" else None
    if record_a and record_b:
        out["mode"] = "record-record"
        rows = graph.connections(record_a, [record_b], limit=1, paths_limit=0)
        row = rows[0] if rows else {}
        out["existing_relations"] = [
            {key: edge.get(key) for key in ("src", "dst", "type", "how", "source")}
            for edge in row.get("existing_relations", [])
        ]
        out["shared_witnesses"] = [
            {
                "id": witness["id"],
                "degree": witness.get("degree"),
                "via": [
                    (witness.get("source_step") or {}).get("edge", {}).get("type"),
                    (witness.get("target_step") or {}).get("edge", {}).get("type"),
                ],
            }
            for witness in row.get("shared_witnesses", [])[:8]
        ]
        out["shared_witness_count"] = row.get("shared_witness_count", 0)
        out["source_family_comparison"] = (row.get("source_family") or {}).get("comparison")
        out["exploratory_path"] = _path_summary(
            graph.paths(record_a, record_b, limit=1, max_depth=4, max_visits=2000)
        )
        out["dependency_path"] = {
            "a_to_b": _path_summary(
                graph.paths(
                    record_a, record_b, limit=1, max_depth=6, max_visits=2000, dependency_only=True
                )
            ),
            "b_to_a": _path_summary(
                graph.paths(
                    record_b, record_a, limit=1, max_depth=6, max_visits=2000, dependency_only=True
                )
            ),
        }
        return out
    out["mode"] = "record-passage" if record_a or record_b else "passage-passage"
    claims_a = [record_a] if record_a else list(a.get("claim_ids") or [])
    claims_b = [record_b] if record_b else list(b.get("claim_ids") or [])
    out["shared_claim_ids"] = sorted(set(claims_a) & set(claims_b))
    if record_a and record_a in (b.get("claim_ids") or []):
        out["passage_maps_to_record"] = "b maps to a"
    if record_b and record_b in (a.get("claim_ids") or []):
        out["passage_maps_to_record"] = "a maps to b"
    links = []
    for src in claims_a[:5]:
        if src not in graph.records:
            continue
        targets = [t for t in claims_b[:8] if t in graph.records and t != src]
        for row in graph.connections(src, targets, limit=8, paths_limit=0):
            if row.get("existing_relations") or row.get("shared_witness_count"):
                links.append(
                    {
                        "a_claim": src,
                        "b_claim": row["id"],
                        "existing_relations": [
                            {key: edge.get(key) for key in ("src", "dst", "type", "how")}
                            for edge in row.get("existing_relations", [])
                        ],
                        "shared_witness_count": row.get("shared_witness_count", 0),
                    }
                )
    out["claim_links"] = links[:12]
    out["existing_relations"] = [edge for link in links for edge in link["existing_relations"]][:12]
    return out


# ---------------------------------------------------------------------------
# Lexicon concepts (optional; another module owns the lexicon)


def _lexicon_entries(loaded: Any) -> list[tuple[str, list[str]]]:
    if isinstance(loaded, dict) and "entries" in loaded:
        loaded = loaded["entries"]
    elif isinstance(loaded, dict) and "concepts" in loaded:
        loaded = loaded["concepts"]
    if hasattr(loaded, "concepts") and not isinstance(loaded, list | dict):
        loaded = loaded.concepts
    entries = []
    items = loaded.items() if isinstance(loaded, dict) else enumerate(loaded or [])
    for key, item in items:
        if isinstance(item, dict):
            name = item.get("id") or item.get("name") or item.get("concept") or key
            variants = item.get("variants") or item.get("spellings") or item.get("aliases") or []
        else:
            name = getattr(item, "id", None) or getattr(item, "name", None) or key
            variants = (
                getattr(item, "variants", None)
                or getattr(item, "spellings", None)
                or getattr(item, "aliases", None)
                or []
            )
        if isinstance(variants, str):
            variants = [variants]
        variants = [v.get("text") if isinstance(v, dict) else v for v in variants]
        variants = [str(v) for v in variants if isinstance(v, str | int | float)]
        if isinstance(name, str) and name:
            entries.append((name, list(dict.fromkeys([name, *variants]))))
    return entries


def _contains_sequence(tokens: list[str], sub: list[str]) -> bool:
    if not sub or len(sub) > len(tokens):
        return False
    first = sub[0]
    return any(
        tokens[i : i + len(sub)] == sub
        for i in range(len(tokens) - len(sub) + 1)
        if tokens[i] == first
    )


def _call_loader(loader, path: Path, root: Path):
    """Pass ``root`` only to a loader that declares it (the real one checks citations there)."""
    try:
        parameters = inspect.signature(loader).parameters
    except (TypeError, ValueError):
        parameters = {}
    return loader(path, root=root) if "root" in parameters else loader(path)


def lexicon_concepts(
    engine, text_a: str, text_b: str, tokens_a: list[str], tokens_b: list[str]
) -> dict:
    """Concepts whose variants occur in both texts, when the lexicon exists.

    The lexicon module is written by another agent; a missing module, an
    unfamiliar loader or a validation failure is reported as unavailable
    rather than guessed, so an empty concept list never masquerades as
    "no shared concepts". Its own ``matches`` (every variant token present)
    is used when it exists; otherwise variants are matched as token
    sequences.
    """
    path = Path(engine.root) / LEXICON_PATH
    if not path.is_file():
        return {"available": False, "reason": f"{LEXICON_PATH} not present", "concepts": []}
    try:
        from . import discovery_lexicon  # type: ignore[attr-defined]
    except ImportError:
        return {"available": False, "reason": "discovery_lexicon not importable", "concepts": []}
    loader = None
    for name in ("load_lexicon", "load", "read_lexicon"):
        candidate = getattr(discovery_lexicon, name, None)
        if callable(candidate):
            loader = candidate
            break
    if loader is None:
        holder = getattr(discovery_lexicon, "Lexicon", None)
        loader = getattr(holder, "load", None)
    if not callable(loader):
        return {"available": False, "reason": "discovery_lexicon exposes no loader", "concepts": []}
    try:
        loaded = _call_loader(loader, path, Path(engine.root))
    except Exception as exc:  # noqa: BLE001 - foreign loader; report, never crash the dossier
        return {"available": False, "reason": f"lexicon load failed: {exc}", "concepts": []}
    matcher = getattr(discovery_lexicon, "matches", None)
    concepts = []
    if callable(matcher):
        try:
            hits_a, hits_b = matcher(text_a, loaded), matcher(text_b, loaded)
        except Exception as exc:  # noqa: BLE001 - foreign matcher; report, never crash
            return {"available": False, "reason": f"lexicon matching failed: {exc}", "concepts": []}
        variants_a: dict[str, list[str]] = {}
        variants_b: dict[str, list[str]] = {}
        for hits, variants in ((hits_a, variants_a), (hits_b, variants_b)):
            for hit in hits:
                concept, text = str(hit.get("concept") or ""), str(hit.get("text") or "")
                if concept and text and text not in variants.setdefault(concept, []):
                    variants[concept].append(text)
        for concept in sorted(variants_a.keys() & variants_b.keys()):
            concepts.append(
                {"concept": concept, "a": variants_a[concept][:4], "b": variants_b[concept][:4]}
            )
        method = "discovery_lexicon.matches: every token of a variant present in the text"
    else:
        for name, variants in _lexicon_entries(loaded):
            matched_a = [
                v for v in variants if _contains_sequence(tokens_a, clean_tokens(tokenize(v)))
            ]
            matched_b = [
                v for v in variants if _contains_sequence(tokens_b, clean_tokens(tokenize(v)))
            ]
            if matched_a and matched_b:
                concepts.append({"concept": name, "a": matched_a[:4], "b": matched_b[:4]})
        method = "variant token sequence present in both texts"
    result = {"available": True, "method": method, "concepts": concepts[:20]}
    if isinstance(loaded, dict) and loaded.get("fingerprint"):
        result["fingerprint"] = loaded["fingerprint"]
    return result


# ---------------------------------------------------------------------------
# Proposal


def _location(endpoint: dict) -> str:
    source = endpoint.get("source") or {}
    path = (
        source.get("path")
        or (endpoint.get("record") or {}).get("where")
        or endpoint["id_or_locator"]
    )
    lines = source.get("lines")
    return f"{path}:{lines[0]}-{lines[1]}" if lines else str(path)


def _cue_symbols(markers: dict, symbols: list[str]) -> set[str]:
    wanted = set(symbols)
    found = set()
    for cue in markers.get("hypothesis_cues", []):
        found |= wanted & set(cue.get("symbols") or clean_tokens(tokenize(cue["text"])))
    return found


def _cue_with_symbol(markers: dict, symbols: list[str]) -> dict | None:
    """The first quoted cue line naming a shared symbol, else the first located cue.

    Pointing the reviewer at a cue line that does not mention the shared
    object sends them to the wrong hypothesis.
    """
    wanted = set(symbols)
    located = [c for c in markers.get("hypothesis_cues", []) if c.get("line")]
    for cue in located:
        if wanted & set(cue.get("symbols") or clean_tokens(tokenize(cue["text"]))):
            return cue
    return located[0] if located else None


def _check_next(kind: str, a: dict, b: dict, shared: dict, markers: dict, conflicts: list) -> list:
    loc_a, loc_b = _location(a), _location(b)
    symbols = shared["symbols"]
    named = ", ".join(symbols[:3]) or "the shared vocabulary"
    rank_a = ", ".join(markers["a"]["rank"]) or "no rank marker"
    rank_b = ", ".join(markers["b"]["rank"]) or "no rank marker"
    regime_a = ", ".join(markers["a"]["regime"]) or "no regime marker"
    regime_b = ", ".join(markers["b"]["regime"]) or "no regime marker"
    cue_a = _cue_with_symbol(markers["a"], symbols)
    cue_b = _cue_with_symbol(markers["b"], symbols)
    cue_ref = (
        f"A line {cue_a['line']} and B line {cue_b['line']}"
        if cue_a and cue_b
        else "the hypothesis lines quoted under markers"
    )
    if kind == "shared-operator":
        return [
            f"Compare the normalization of {named} in both sources (A {loc_a}; B {loc_b}).",
            f"Confirm the rank marker ({rank_a} vs {rank_b}) and the regime ({regime_a} vs "
            f"{regime_b}) before reusing any bound.",
            "Record the outcome as shared vocabulary only: a shared symbol registers no edge "
            "(ADR 0007); a named operator may enter ledger/symbols.yaml.",
        ]
    if kind == "compatible-hypothesis":
        return [
            f"Read {cue_ref} and decide whether each hypothesis set implies, restricts or "
            "contradicts the other.",
            f"Check that {named} denotes the same object under both hypothesis sets "
            "(same measure, domain and coupling convention).",
            "If compatible, register bears_on on the result or document; depends_on needs "
            "an actual use of one argument inside the other.",
        ]
    if kind == "reusable-ingredient":
        terms = ", ".join(shared["terms"][:4]) or "the shared terms"
        return [
            f"Identify the exact lemma or inequality in B ({loc_b}) that A ({loc_a}) would use; "
            f"the shared terms are {terms}.",
            f"Check its hypotheses cover A's regime ({regime_a}) and rank ({rank_a}).",
            "Register depends_on only after confirming the ingredient is used in the argument; "
            "otherwise record bears_on.",
        ]
    if kind == "equivalent-construction":
        return [
            f"Write both constructions of {named} in one notation and exhibit the map that "
            "identifies them.",
            "State the falsifier: what object, if exhibited, would break the identification.",
            "A unifying candidate enters ledger/gaps.yaml only with that falsifier; a naming "
            "identity belongs in ledger/symbols.yaml.",
        ]
    if kind == "scope-restriction":
        return [
            f"A is marked {regime_a} / {rank_a}; B is marked {regime_b} / {rank_b}. Find the "
            "hypothesis in each that fixes the regime.",
            f"State which statement about {named} is the special case and what extra input "
            "the general one needs.",
            "Record the restriction as a route cannot_decide, a supported_by scope or "
            "derivation remaining work; not as a dependency.",
        ]
    if kind == "disagreement":
        conflict = conflicts[0] if conflicts else {"carrier": named, "a": [], "b": []}
        return [
            f"The two excerpts state different values or signs for {conflict['carrier']} "
            f"(A: {', '.join(conflict.get('a') or []) or 'see excerpt'}; "
            f"B: {', '.join(conflict.get('b') or []) or 'see excerpt'}); reproduce both under "
            "one convention before recording a contradiction.",
            f"Check the normalization cues (A: {markers['a']['normalization'] or 'none'}; "
            f"B: {markers['b']['normalization'] or 'none'}) for a factor that explains the gap.",
            "Record a confirmed disagreement through literature contradicts, a route "
            "cannot_decide or a refuted unifying candidate; no new C-ids.",
        ]
    if kind == "literature-bearing":
        lit, other = (a, b) if a["family"] in LITERATURE_FAMILIES else (b, a)
        return [
            f"Identify which claim in {other['id_or_locator']} the literature passage "
            f"({_location(lit)}) supplies a value, method, comparison or contradiction for.",
            f"Compare the rank and regime markers ({rank_a} / {regime_a} vs {rank_b} / "
            f"{regime_b}) before treating the literature statement as applicable.",
            "Register through literature/index.yaml bears_on with a relation and status; a "
            "citation is not a dependency.",
        ]
    if kind == "documentary":
        return [
            "Confirm the citation refers to the same section and revision: compare the sha256 "
            f"and lines of both sources (A {loc_a}; B {loc_b}).",
            "Decide whether the citing text uses a result of the cited one or only names it.",
            "A documentary link is documents.yaml cites or bears_on; it carries no "
            "mathematical dependency.",
        ]
    return [
        f"Shared vocabulary is limited to {shared['exact_token_count']} exact token(s) and "
        f"{shared['term_count']} term(s); if a relation is still expected, search with a "
        "reformulated query or --seed.",
        "Do not register anything from this pair.",
    ]


def propose(
    a: dict,
    b: dict,
    shared: dict,
    lexicon: dict,
    markers: dict,
    conflicts: list,
    citations: list,
    graph: dict,
) -> dict:
    """One kind from the closed vocabulary, with the rule and reasons that chose it.

    See the module docstring for the ordered rules. Confidence is ``medium``
    only with at least two independent signals (a registered edge counts
    double); it is never ``high`` because these are pattern matches.
    """
    symbols, rationals = shared["symbols"], shared["rationals"]
    exact_count = shared["exact_token_count"]
    registered = graph.get("existing_relations") or []
    scientific = [edge for edge in registered if edge.get("type") not in DOCUMENTARY_TYPES]
    regimes_a, regimes_b = set(markers["a"]["regime"]), set(markers["b"]["regime"])
    ranks_a, ranks_b = set(markers["a"]["rank"]), set(markers["b"]["rank"])
    cues_a, cues_b = markers["a"]["hypothesis_cues"], markers["b"]["hypothesis_cues"]
    cue_symbols = _cue_symbols(markers["a"], symbols) & _cue_symbols(markers["b"], symbols)
    one_literature = (a["family"] in LITERATURE_FAMILIES) != (b["family"] in LITERATURE_FAMILIES)
    reasons: list[str] = []
    if registered:
        reasons.append(
            "registered relation(s): "
            + ", ".join(sorted({e.get("type") or "?" for e in registered}))
        )
    if shared["term_count"] or exact_count:
        reasons.append(
            f"{exact_count} shared exact token(s) ({', '.join((rationals + symbols)[:6])}); "
            f"{shared['term_count']} shared term(s)"
        )
    if lexicon.get("concepts"):
        reasons.append(
            "lexicon concepts in both: " + ", ".join(c["concept"] for c in lexicon["concepts"][:5])
        )
    if exact_count < 2 and shared["term_count"] < 3 and not citations and not registered:
        kind, rule = "unrelated", 1
        reasons.append("fewer than two shared exact tokens and fewer than three shared terms")
    elif citations or (registered and not scientific):
        kind, rule = "documentary", 2
        reasons.extend(f"{c['in'].upper()} cites {c['cites']}" for c in citations)
        if registered and not scientific:
            reasons.append("only documentary edge types are registered")
    elif conflicts:
        kind, rule = "disagreement", 3
        reasons.extend(
            f"{c['carrier']}: A {', '.join(c['a'])} vs B {', '.join(c['b'])} ({c['basis']})"
            for c in conflicts[:3]
        )
    elif one_literature and not registered:
        kind, rule = "literature-bearing", 4
        reasons.append(f"families {a['family']} vs {b['family']}")
    elif symbols and (
        (regimes_a and regimes_b and regimes_a.isdisjoint(regimes_b))
        or (ranks_a and ranks_b and ranks_a.isdisjoint(ranks_b))
    ):
        kind, rule = "scope-restriction", 5
        reasons.append(
            f"disjoint markers: regime {sorted(regimes_a)} vs {sorted(regimes_b)}; "
            f"rank {sorted(ranks_a)} vs {sorted(ranks_b)}"
        )
    elif (
        markers["a"]["construction_cues"]
        and markers["b"]["construction_cues"]
        and len(symbols) >= 3
        and shared["symbol_jaccard"] >= 0.5
    ):
        kind, rule = "equivalent-construction", 6
        reasons.append(
            f"construction cues in both; symbol Jaccard {shared['symbol_jaccard']} over "
            f"{len(symbols)} shared symbols"
        )
    elif cues_a and cues_b and cue_symbols:
        kind, rule = "compatible-hypothesis", 7
        reasons.append("hypothesis cue lines in both share " + ", ".join(sorted(cue_symbols)[:5]))
    elif symbols:
        kind, rule = "shared-operator", 8
        reasons.append("shared symbol-like tokens without a hypothesis-level match")
    elif shared["term_count"] >= 3:
        kind, rule = "reusable-ingredient", 9
        reasons.append("shared terms only; no shared symbol")
    elif scientific:
        dependency = any(edge.get("type") in DEPENDENCY_TYPES for edge in scientific)
        kind, rule = ("reusable-ingredient" if dependency else "compatible-hypothesis"), 10
        reasons.append("no text signal; kind implied by the registered edge class")
    else:
        kind, rule = "unrelated", 10
    signals = 0
    if scientific:
        signals += 2
    if exact_count >= 4:
        signals += 1
    if lexicon.get("concepts"):
        signals += 1
    exploratory = graph.get("exploratory_path") or {}
    if exploratory.get("found") and len(exploratory.get("steps") or []) <= 2:
        signals += 1
    if kind == "disagreement":
        # A stated value for a structured symbol in both texts is the one
        # conflict signal worth a second look; sign flips and neighbour
        # disagreements stay low until a reviewer reads the lines.
        signals = 1 + int(
            any(c["carrier"] in symbols and c["basis"] == "stated values differ" for c in conflicts)
        )
    if kind == "unrelated":
        signals = 0
    confidence = "medium" if signals >= 2 else "low"
    return {
        "kind": kind,
        "confidence": confidence,
        "rule": rule,
        "reasons": reasons,
        "check_next": _check_next(kind, a, b, shared, markers, conflicts),
        "registrable_as": REGISTRABLE_AS[kind],
        "semantics": "heuristic kind from the closed vocabulary; review decides, never this field",
    }


# ---------------------------------------------------------------------------
# Dossier


def _excerpt_for(endpoint: dict, terms: list[str], max_chars: int) -> dict:
    text = endpoint.get("_text") or ""
    if not text and endpoint.get("kind") == "record":
        record = endpoint.get("record") or {}
        text = str(record.get("statement") or "")
    window = excerpt(text, terms, max_chars)
    base = endpoint.get("_base_line")
    first, last = window["line_offset"]
    lines = [base + first, base + last] if base and text else None
    return {
        "text": window["text"],
        "lines": lines,
        "truncated": window["truncated"],
        "cuts_block": window["cuts_block"],
        "terms_from": "the other endpoint's tokens",
    }


def _commands(a: dict, b: dict, kind: str | None) -> dict:
    prefix = "uv run --no-sync workhouse"
    commands = {
        "pair": f"{prefix} discover pair {a['id_or_locator']!r} {b['id_or_locator']!r} --json "
        "--out .graph-state/TASK/pair.json",
    }
    if kind:
        commands["review_add"] = (
            f"{prefix} discover review add --seed {a['id_or_locator']!r} "
            f"--target {b['id_or_locator']!r} --kind {kind} "
            "--note '<what you read in both sources that decides it>'"
        )
    for side, endpoint in (("a", a), ("b", b)):
        if endpoint["kind"] == "record":
            commands[f"why_{side}"] = f"{prefix} why {endpoint['id']}"
            commands[f"brief_{side}"] = (
                f"{prefix} brief {endpoint['id']} --json --out .graph-state/TASK/brief-{side}.json"
            )
    if a["kind"] == "record" and b["kind"] == "record":
        commands["path"] = f"{prefix} discover path {a['id']} {b['id']} --json"
    return commands


def pair(engine, a_spec: str, b_spec: str, *, excerpt_chars: int = PAIR_EXCERPT_CHARS) -> dict:
    """Build the dossier for two endpoints; read-only over every input."""
    if not MIN_EXCERPT_CHARS <= excerpt_chars <= MAX_EXCERPT_CHARS:
        raise ValueError(
            f"excerpt budget must lie in [{MIN_EXCERPT_CHARS}, {MAX_EXCERPT_CHARS}] characters"
        )
    a, b = resolve_endpoint(engine, a_spec), resolve_endpoint(engine, b_spec)
    compare_a = a["_text"] + ("\n" + _record_text(a) if a["kind"] == "record" else "")
    compare_b = b["_text"] + ("\n" + _record_text(b) if b["kind"] == "record" else "")
    tokens_a = clean_tokens(tokenize(compare_a))
    tokens_b = clean_tokens(tokenize(compare_b))
    shared = shared_tokens(tokens_a, tokens_b, engine.index)
    lexicon = lexicon_concepts(engine, compare_a, compare_b, tokens_a, tokens_b)
    # Excerpt selection uses the raw tokenizer so it agrees with the
    # index's own term counting inside ``excerpt``.
    a["excerpt"] = _excerpt_for(a, sorted(set(tokenize(compare_b))), excerpt_chars)
    b["excerpt"] = _excerpt_for(b, sorted(set(tokenize(compare_a))), excerpt_chars)
    markers = {"a": detect_markers(a), "b": detect_markers(b)}
    conflicts = value_conflicts(compare_a, compare_b, tokens_a, tokens_b, shared)
    citations = documentary_citations(a, b)
    graph = graph_relations(engine, a, b)
    endpoints = {"a": a, "b": b}
    unavailable = [
        side
        for side, endpoint in endpoints.items()
        if endpoint["kind"] == "passage" and not endpoint["source"].get("available")
    ]
    if unavailable:
        # An endpoint whose bytes cannot be read compares as empty text; the
        # rules would call that 'unrelated' and print a review command for
        # a reading nobody could have done.
        proposal = {
            "kind": None,
            "rule": 0,
            "confidence": None,
            "reasons": [
                f"endpoint {side} unavailable: {endpoints[side]['source'].get('reason')}"
                for side in unavailable
            ],
            "registrable_as": "nothing until the endpoint's bytes are readable here",
            "check_next": [
                "Mount or index the external root named by the locator, or point the "
                "locator at a checkout-relative copy, then rerun the pair.",
            ],
        }
    else:
        proposal = propose(a, b, shared, lexicon, markers, conflicts, citations, graph)
    for endpoint in (a, b):
        endpoint["text_chars"] = len(endpoint.pop("_text"))
        endpoint.pop("_base_line", None)
    metadata = engine.index.metadata()
    return {
        "schema": SCHEMA,
        "pair": [a_spec.strip(), b_spec.strip()],
        "argv": ["workhouse", "discover", "pair", a_spec.strip(), b_spec.strip(), "--json"],
        "a": a,
        "b": b,
        "shared": {**shared, "lexicon": lexicon},
        "markers": markers,
        "value_conflicts": conflicts,
        "citations": citations,
        "graph": graph,
        "proposal": proposal,
        "commands": _commands(a, b, proposal["kind"]),
        "excerpt_chars": excerpt_chars,
        "provenance": provenance_summary(metadata, engine.root),
        "meaning": MEANING,
        "execution": {"python_checks": 0, "lean": False, "scientific_index_written": False},
    }


# ---------------------------------------------------------------------------
# Text rendering and CLI


def _columns(left: list[str], right: list[str], width: int) -> list[str]:
    column = max(20, (width - 3) // 2)

    def wrap(lines: list[str]) -> list[str]:
        out: list[str] = []
        for line in lines:
            out.extend(textwrap.wrap(line.rstrip(), column, break_long_words=True) or [""])
        return out

    left_lines, right_lines = wrap(left), wrap(right)
    height = max(len(left_lines), len(right_lines))
    left_lines += [""] * (height - len(left_lines))
    right_lines += [""] * (height - len(right_lines))
    return [
        f"{l_line:<{column}} | {r_line}".rstrip()
        for l_line, r_line in zip(left_lines, right_lines, strict=True)
    ]


def _endpoint_header(label: str, endpoint: dict) -> list[str]:
    source = endpoint.get("source") or {}
    lines = [f"{label}  {endpoint['id_or_locator']}  [{endpoint['kind']}, {endpoint['family']}]"]
    record = endpoint.get("record") or {}
    if record:
        status = ", ".join(
            f"{key} {record[key]}" for key in ("status", "evidence", "tier") if key in record
        )
        lines.append(f"    {status}" if status else "    (no status fields)")
        lines.append(f"    statement: {record.get('statement', '')[:300]}")
        if record.get("hypotheses"):
            lines.append(f"    hypotheses: {record['hypotheses'][:300]}")
    where = _location(endpoint)
    digest = (source.get("sha256") or "")[:12]
    availability = "" if source.get("available") else f"  (unavailable: {source.get('reason')})"
    lines.append(f"    {where}  sha256 {digest or '-'}{availability}")
    if endpoint.get("claim_ids") and endpoint["kind"] == "passage":
        lines.append("    claims: " + ", ".join(endpoint["claim_ids"][:6]))
    return lines


def render_pair(result: dict, width: int = 100) -> str:
    """Readable dossier: excerpts side by side, markers, shared tokens, proposal."""
    a, b = result["a"], result["b"]
    lines = [
        f"pair dossier  {a['id_or_locator']}  <->  {b['id_or_locator']}",
        result["meaning"],
        "",
    ]
    lines.extend(_endpoint_header("A", a))
    lines.extend(_endpoint_header("B", b))
    lines.append("")
    excerpt_a = (a.get("excerpt") or {}).get("text", "").strip().splitlines()
    excerpt_b = (b.get("excerpt") or {}).get("text", "").strip().splitlines()
    loc_a = (a.get("excerpt") or {}).get("lines")
    loc_b = (b.get("excerpt") or {}).get("lines")
    head_a = f"A excerpt lines {loc_a[0]}-{loc_a[1]}" if loc_a else "A excerpt"
    head_b = f"B excerpt lines {loc_b[0]}-{loc_b[1]}" if loc_b else "B excerpt"
    lines.extend(
        _columns(
            [head_a, "-" * len(head_a), *excerpt_a], [head_b, "-" * len(head_b), *excerpt_b], width
        )
    )
    lines.append("")
    shared = result["shared"]
    lines.append("shared exact tokens: " + (", ".join(shared["exact_tokens"][:30]) or "none"))
    if shared.get("single_letters"):
        lines.append(
            "shared single letters (weak, LaTeX-prone): " + ", ".join(shared["single_letters"])
        )
    lines.append(
        "shared terms ("
        + shared["term_ranking"]
        + "): "
        + (
            ", ".join(
                f"{term}({shared['term_counts'][term]['a']}/{shared['term_counts'][term]['b']})"
                for term in shared["terms"]
            )
            or "none"
        )
    )
    lexicon = shared.get("lexicon") or {}
    if lexicon.get("available"):
        lines.append(
            "lexicon concepts: " + (", ".join(c["concept"] for c in lexicon["concepts"]) or "none")
        )
    else:
        lines.append(f"lexicon concepts: unavailable ({lexicon.get('reason')})")
    lines.append("")
    markers = result["markers"]
    rows = [("regime", "regime"), ("rank", "rank"), ("coupling", "coupling")]
    lines.append(f"{'markers':<16}{'A':<41} B")
    for label, key in rows:
        left = ", ".join(markers["a"][key]) or "-"
        right = ", ".join(markers["b"][key]) or "-"
        lines.append(f"{label:<16}{left[:40]:<41} {right[:40]}")
    norm_a = ", ".join(f"{k}({v})" for k, v in markers["a"]["normalization"].items()) or "-"
    norm_b = ", ".join(f"{k}({v})" for k, v in markers["b"]["normalization"].items()) or "-"
    lines.append(f"{'normalization':<16}{norm_a[:40]:<41} {norm_b[:40]}")
    for side in ("a", "b"):
        cues = markers[side]["hypothesis_cues"]
        lines.append(f"hypothesis cues {side.upper()} ({markers[side]['hypothesis_cue_count']}):")
        for cue in cues[:5]:
            where = f"L{cue['line']}" if cue.get("line") else cue.get("in", "record")
            lines.append(f"    {where} [{cue['cue']}] {cue['text'][:110]}")
        if not cues:
            lines.append("    none")
    lines.append("")
    graph = result["graph"]
    relations = graph.get("existing_relations") or []
    lines.append(
        f"graph ({graph.get('mode')}): registered relations "
        + (
            ", ".join(f"{e.get('src')} -{e.get('type')}-> {e.get('dst')}" for e in relations[:4])
            or "none"
        )
    )
    if graph.get("shared_witness_count"):
        lines.append(
            f"    shared witnesses {graph['shared_witness_count']}: "
            + ", ".join(w["id"] for w in graph["shared_witnesses"][:4])
        )
    if graph.get("exploratory_path") is not None:
        path = graph["exploratory_path"]
        lines.append(
            "    exploratory path: "
            + (" | ".join(path["steps"]) if path["found"] else "not found within bounds")
        )
        dependency = graph.get("dependency_path") or {}
        for direction in ("a_to_b", "b_to_a"):
            step = dependency.get(direction) or {}
            lines.append(
                f"    dependency path {direction}: "
                + (" | ".join(step.get("steps", [])) if step.get("found") else "none")
            )
    if graph.get("shared_claim_ids"):
        lines.append("    shared claim ids: " + ", ".join(graph["shared_claim_ids"][:6]))
    if graph.get("passage_maps_to_record"):
        lines.append(f"    {graph['passage_maps_to_record']}")
    for link in (graph.get("claim_links") or [])[:4]:
        lines.append(
            f"    {link['a_claim']} ~ {link['b_claim']}: "
            + (", ".join(e.get("type") for e in link["existing_relations"]) or "witnesses only")
        )
    if result.get("value_conflicts"):
        lines.append("value conflicts:")
        for conflict in result["value_conflicts"][:5]:
            lines.append(
                f"    {conflict['carrier']}: A {', '.join(conflict['a'])} vs B "
                f"{', '.join(conflict['b'])}  ({conflict['basis']})"
            )
    if result.get("citations"):
        lines.append(
            "citations: "
            + "; ".join(f"{c['in'].upper()} cites {c['cites']}" for c in result["citations"])
        )
    lines.append("")
    proposal = result["proposal"]
    lines.append(
        f"proposal: {proposal['kind']}  "
        f"(confidence {proposal['confidence']}, rule {proposal['rule']})"
    )
    for reason in proposal["reasons"]:
        lines.append(f"    reason: {reason}")
    lines.append(f"    registrable as: {proposal['registrable_as']}")
    lines.append("check next:")
    for number, step in enumerate(proposal["check_next"], 1):
        lines.append(f"    {number}. {step}")
    lines.append("commands:")
    for name, command in result["commands"].items():
        lines.append(f"    {name}: {command}")
    provenance = result.get("provenance") or {}
    lines.append("")
    lines.append(
        f"discovery cache {str(provenance.get('fingerprint') or '')[:12]}  freshness "
        f"{provenance.get('freshness')}"
    )
    return "\n".join(lines)


def add_parser(subparsers) -> None:
    """Register ``workhouse discover pair A B``."""
    parser = subparsers.add_parser(
        "pair", help="compare two sources side by side: excerpts, markers, shared tokens, proposal"
    )
    parser.add_argument("a", metavar="A", help="record id, PASSAGE id, or path:first-last")
    parser.add_argument(
        "b", metavar="B", help="record id, PASSAGE id, path:first-last or ext:label/path:first-last"
    )
    parser.add_argument(
        "--excerpt-chars",
        type=int,
        default=PAIR_EXCERPT_CHARS,
        help=f"excerpt budget per endpoint (default {PAIR_EXCERPT_CHARS})",
    )
    parser.add_argument("--json", action="store_true", help="machine-readable dossier")
    parser.add_argument("--out", help="retain JSON in a new file; refuse overwrite")


def _utf8_streams() -> None:
    # Windows pipes default to a legacy code page; excerpts carry Greek and arrows.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            with contextlib.suppress(ValueError, OSError):
                stream.reconfigure(encoding="utf-8", errors="replace")


def run(args, engine_factory) -> int:
    """CLI entry: build the dossier, retain it if asked, print text or JSON."""
    _utf8_streams()
    try:
        with engine_factory() as engine:
            result = pair(
                engine,
                args.a,
                args.b,
                excerpt_chars=getattr(args, "excerpt_chars", None) or PAIR_EXCERPT_CHARS,
            )
        if getattr(args, "out", None):
            path = Path(args.out)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(json.dumps(result, sort_keys=True, ensure_ascii=True) + "\n")
        print(json.dumps(result, sort_keys=True) if args.json else render_pair(result))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        error = {"schema": ERROR_SCHEMA, "error": str(exc)}
        print(json.dumps(error) if args.json else f"Discovery unavailable: {exc}")
        return 1
