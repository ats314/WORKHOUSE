"""Local, content-addressed retrieval over saved records and source passages.

This disposable SQLite index never executes a registered check and never writes
scientific records. Scores select reading candidates; their scientific standing
remains in the original catalogue. Source excerpts retain line and byte hashes.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import stat as stat_module
import tempfile
import uuid
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "workhouse-discovery-index/v1"
INDEX_PATHS = ("index/claims.jsonl", "index/graph.jsonl", "index/symbols.jsonl")
SOURCE_ROOTS = (
    "theory",
    "corpus-import",
    "paper",
    "docs/derivations",
    "docs/research",
    "docs/decisions",
    "notes/imported",
    "literature",
    "research",
)
EXTENSIONS = {".md", ".tex", ".txt"}
SKIP_PARTS = {
    ".git",
    ".venv",
    ".lake",
    "__pycache__",
    "node_modules",
    ".cache",
    ".graph-state",
    "inbox",
    "runs",
    "build",
    "dist",
    ".ipynb_checkpoints",
}
MAX_SOURCE_BYTES = 8 * 1024 * 1024
CHUNK_TOKENS = 180
MAX_CHUNK_CHARS = 12000
_TOKEN = re.compile(
    r"[+-]?\d+\s*/\s*[+-]?\d+|[A-Za-z][A-Za-z0-9_^']*|"
    r"[+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?"
)
_STOP = frozenset(
    [
        "the",
        "a",
        "an",
        "of",
        "and",
        "or",
        "to",
        "in",
        "on",
        "at",
        "for",
        "by",
        "with",
        "from",
        "as",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "that",
        "this",
        "these",
        "those",
        "it",
        "its",
        "which",
        "what",
        "where",
        "when",
        "who",
        "how",
        "we",
        "our",
        "you",
        "your",
        "they",
        "their",
        "into",
        "than",
        "then",
        "there",
        "here",
        "also",
        "can",
        "may",
        "will",
        "would",
        "should",
        "could",
        "do",
        "does",
        "did",
        "have",
        "has",
        "had",
        "but",
        "if",
        "so",
        "such",
        "per",
        "via",
        "each",
        "any",
        "all",
        "some",
    ]
)
_GREEK = dict(
    zip(
        "αβγδεζηθικλμνξοπρστυφχψω",
        [
            "alpha",
            "beta",
            "gamma",
            "delta",
            "epsilon",
            "zeta",
            "eta",
            "theta",
            "iota",
            "kappa",
            "lambda",
            "mu",
            "nu",
            "xi",
            "omicron",
            "pi",
            "rho",
            "sigma",
            "tau",
            "upsilon",
            "phi",
            "chi",
            "psi",
            "omega",
        ],
        strict=True,
    )
)


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"))


def tokenize(text: str) -> list[str]:
    """Keep mathematical join keys atomic; canonicalize rational values exactly."""
    text = text.replace("−", "-")
    text = "".join(_GREEK.get(c.lower(), c) for c in text)
    result = []
    for token in _TOKEN.findall(text):
        token = token.lower().removeprefix("+")
        if "/" in token:
            try:
                numerator, denominator = re.sub(r"\s+", "", token).split("/")
                token = str(Fraction(int(numerator), int(denominator)))
            except (ValueError, ZeroDivisionError):
                token = re.sub(r"\s+", "", token)
        elif token in _STOP:
            continue
        elif (
            len(token) > 4 and token.isalpha() and token.endswith("s") and not token.endswith("ss")
        ):
            token = token[:-1]
        result.append(token)
    return result


def _encoded(tokens: list[str]) -> str:
    # FTS sees only ASCII alphanumeric keys. Its tokenizer cannot discard a
    # fraction's slash/sign or parse a user-supplied MATCH operator.
    return " ".join("x" + token.encode("utf-8").hex() for token in tokens)


def _locator(where: str, source_paths) -> tuple[str, tuple[int, int] | None]:
    """Resolve an observed source filename before interpreting its suffix.

    Hash signs and parenthesized suffixes are legal source-name characters.
    Only text following a complete indexed filename can act as a locator.
    """
    normalized = where.replace("\\", "/")
    if normalized in source_paths:
        return normalized, None
    candidates = [
        path
        for path in source_paths
        if normalized.startswith(path)
        and (
            normalized[len(path) :].startswith((" (", "#"))
            or re.fullmatch(r":\d+(?:[-–]\d+)?", normalized[len(path) :])
        )
    ]
    if not candidates:
        return normalized, None
    path = max(candidates, key=lambda candidate: (len(candidate), candidate))
    suffix = normalized[len(path) :]
    colon = re.fullmatch(r":(\d+)(?:[-–](\d+))?", suffix)
    lines = re.search(r"\blines?\s+(\d+)(?:\s*[-–]\s*(\d+))?", suffix)
    bounds = lines or colon
    if bounds:
        first = int(bounds[1])
        last = int(bounds[2] or bounds[1])
        return path, (first, max(first, last))
    return path, None


_FENCE = re.compile(r"^\s*(```|~~~)")
_MATH_ENV = r"(equation|align|alignat|gather|multline|eqnarray|flalign|displaymath)\*?"
_ENV_OPEN = re.compile(r"\\begin\{" + _MATH_ENV + r"\}")
_ENV_CLOSE = re.compile(r"\\end\{" + _MATH_ENV + r"\}")


def protected_blocks(lines: list[str]) -> list[tuple[int, int]]:
    """Inclusive line-index spans of fenced code, display math and equation environments.

    A passage boundary inside one of these blocks separates an equation from
    its own closing delimiter, so the chunker keeps them whole when the
    character budget allows. Detection is line-based and conservative: an
    unclosed block runs to the end of the document.
    """
    spans: list[tuple[int, int]] = []
    state: tuple[str, str] | None = None
    start = 0
    for number, line in enumerate(lines):
        if state is None:
            fence = _FENCE.match(line)
            if fence:
                state, start = ("fence", fence.group(1)), number
            elif line.count("$$") % 2 == 1:
                state, start = ("dollar", ""), number
            elif "\\[" in line and "\\]" not in line[line.index("\\[") + 2 :]:
                state, start = ("bracket", ""), number
            else:
                opened = _ENV_OPEN.search(line)
                if opened and not _ENV_CLOSE.search(line):
                    state, start = ("env", opened.group(1)), number
            continue
        kind, marker = state
        if kind == "fence":
            fence = _FENCE.match(line)
            closed = bool(fence and fence.group(1) == marker)
        elif kind == "dollar":
            closed = line.count("$$") % 2 == 1
        elif kind == "bracket":
            closed = "\\]" in line
        else:
            ended = _ENV_CLOSE.search(line)
            closed = bool(ended and ended.group(1) == marker)
        if closed:
            spans.append((start, number))
            state = None
    if state is not None and lines:
        spans.append((start, len(lines) - 1))
    return spans


def _block_map(lines: list[str]) -> dict[int, tuple[int, int]]:
    blocks = {}
    for span in protected_blocks(lines):
        for number in range(span[0], span[1] + 1):
            blocks[number] = span
    return blocks


def _passages(text: str):
    """Whole-line windows, with bounded slices only for oversized single lines.

    A window that reaches its token budget inside a protected block keeps
    growing to the block's end while the character budget allows, and the
    one-line overlap is skipped when it would open the next window inside a
    block. Equations therefore travel with their delimiters.
    """
    lines = text.splitlines(keepends=True)
    blocks = _block_map(lines)
    start = 0
    while start < len(lines):
        if len(lines[start]) > MAX_CHUNK_CHARS:
            for offset in range(0, len(lines[start]), MAX_CHUNK_CHARS):
                part = lines[start][offset : offset + MAX_CHUNK_CHARS]
                yield start + 1, start + 1, offset + 1, offset + len(part), part
            start += 1
            continue
        end, count, chars = start, 0, 0
        while end < len(lines):
            line = lines[end]
            if end > start and (chars + len(line) > MAX_CHUNK_CHARS or count >= CHUNK_TOKENS):
                block = blocks.get(end)
                continuing = block is not None and block[0] < end
                if not (continuing and chars + len(line) <= MAX_CHUNK_CHARS):
                    break
            if len(line) > MAX_CHUNK_CHARS:
                break
            chars += len(line)
            count += len(tokenize(line))
            end += 1
        excerpt = "".join(lines[start:end])
        if excerpt.strip():
            yield start + 1, end, 1, len(lines[end - 1]), excerpt
        if end == len(lines):
            break
        # One complete trailing line overlaps where that still makes progress
        # and does not open the next window inside a protected block.
        trailing = blocks.get(end - 1)
        inside_block = trailing is not None and trailing[0] < end - 1
        overlap = end - start > 2 and len(tokenize(lines[end - 1])) <= 40 and not inside_block
        start = end - 1 if overlap else end


class DiscoveryIndex:
    def __init__(self, root: Path, cache_dir: Path | None = None):
        self.root = Path(root).resolve()
        self.cache_dir = (
            Path(cache_dir) if cache_dir is not None else self.root / ".graph-state/discovery"
        )
        self.records: list[dict] = []
        self.edges: list[dict] = []
        self.symbols: list[dict] = []
        self._connection: sqlite3.Connection | None = None
        self._meta: dict = {}
        self._current_fingerprint: str | None = None

    def _safe_path(self, path: Path) -> bool:
        try:
            return path.resolve().is_relative_to(self.root) and not path.is_symlink()
        except (OSError, RuntimeError):
            return False

    @staticmethod
    def _plain_file(path: Path) -> bool:
        """A regular file that is not a symlink or Windows reparse point.

        Directories are containment-checked with ``_safe_path`` before the walk
        descends, and the walk never follows links, so a plain file beneath a
        safe directory cannot escape the checkout. Resolving every file's real
        path cost more than hashing it, so files use one ``lstat`` instead.
        """
        try:
            status = os.lstat(path)
        except OSError:
            return False
        if stat_module.S_ISLNK(status.st_mode) or not stat_module.S_ISREG(status.st_mode):
            return False
        attributes = getattr(status, "st_file_attributes", 0)
        reparse = getattr(stat_module, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        return not (attributes & reparse)

    def _saved(self):
        raw, parsed, manifest = {}, {}, {}
        for relative in INDEX_PATHS:
            path = self.root / relative
            if not self._safe_path(path):
                raise ValueError(f"Saved graph path escapes the checkout: {relative}")
            data = path.read_bytes()  # Missing indexes fail; never collect().
            rows = []
            for line_number, line in enumerate(data.decode("utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except ValueError as exc:
                    raise ValueError(f"Invalid saved JSON at {relative}:{line_number}") from exc
                if not isinstance(row, dict):
                    raise ValueError(f"Saved record must be an object: {relative}:{line_number}")
                required = (
                    ("src", "dst", "type", "how", "source") if "graph" in relative else ("id",)
                )
                if any(not isinstance(row.get(key), str) or not row[key] for key in required):
                    raise ValueError(f"Invalid saved record at {relative}:{line_number}")
                rows.append((line_number, line, row))
            if "graph" not in relative and len({r[2]["id"] for r in rows}) != len(rows):
                raise ValueError(f"Duplicate saved record IDs: {relative}")
            raw[relative], parsed[relative] = data, rows
            manifest[relative] = {"sha256": _sha(data), "bytes": len(data)}
        return raw, parsed, manifest

    def _sources(self):
        sources, exclusions, inaccessible = {}, [], []
        for relative_root in SOURCE_ROOTS:
            directory = self.root / relative_root
            if not directory.exists():
                continue
            if not self._safe_path(directory):
                exclusions.append({"path": relative_root, "reason": "unsafe_path"})
                continue

            def walk_error(exc):
                inaccessible.append({"path": str(exc.filename), "reason": type(exc).__name__})

            for current, folders, files in os.walk(
                directory, followlinks=False, onerror=walk_error
            ):
                current_path = Path(current)
                for folder in sorted(folders):
                    if folder.lower() in SKIP_PARTS:
                        exclusions.append(
                            {
                                "path": (current_path / folder).relative_to(self.root).as_posix(),
                                "reason": "excluded_directory",
                            }
                        )
                folders[:] = sorted(
                    folder for folder in folders if folder.lower() not in SKIP_PARTS
                )
                safe_folders = []
                for folder in folders:
                    candidate = current_path / folder
                    if self._safe_path(candidate):
                        safe_folders.append(folder)
                    else:
                        exclusions.append(
                            {
                                "path": candidate.relative_to(self.root).as_posix(),
                                "reason": "unsafe_path",
                            }
                        )
                folders[:] = safe_folders
                for filename in sorted(files):
                    path = current_path / filename
                    if path.suffix.lower() not in EXTENSIONS:
                        continue
                    relative = path.relative_to(self.root).as_posix()
                    if not self._plain_file(path):
                        exclusions.append({"path": relative, "reason": "unsafe_path"})
                        continue
                    try:
                        if path.stat().st_size > MAX_SOURCE_BYTES:
                            exclusions.append({"path": relative, "reason": "size_limit"})
                            continue
                        raw = path.read_bytes()
                        if len(raw) > MAX_SOURCE_BYTES:
                            exclusions.append({"path": relative, "reason": "size_limit"})
                            continue
                        content = raw.decode("utf-8")
                    except UnicodeError:
                        exclusions.append({"path": relative, "reason": "non_utf8"})
                        continue
                    except OSError as exc:
                        inaccessible.append({"path": relative, "reason": type(exc).__name__})
                        continue
                    sources[relative] = {"sha256": _sha(raw), "bytes": len(raw), "text": content}
        return sources, exclusions, inaccessible

    @staticmethod
    def _fingerprint(index_manifest, sources, exclusions, inaccessible):
        source_manifest = {
            path: {key: source[key] for key in ("sha256", "bytes")}
            for path, source in sorted(sources.items())
        }
        identity = {
            "schema": SCHEMA,
            "index_manifest": index_manifest,
            "source_manifest": source_manifest,
            "exclusions": exclusions,
            "inaccessible_files": inaccessible,
            "settings": {
                "roots": SOURCE_ROOTS,
                "extensions": sorted(EXTENSIONS),
                "skip_parts": sorted(SKIP_PARTS),
                "max_source_bytes": MAX_SOURCE_BYTES,
                "chunk_tokens": CHUNK_TOKENS,
                "max_chunk_chars": MAX_CHUNK_CHARS,
            },
            "implementation_sha256": _sha(Path(__file__).read_bytes()),
        }
        return _sha(_json(identity).encode()), identity

    def _open_cache(self, path: Path, fingerprint: str) -> dict | None:
        connection = None
        try:
            connection = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
            if connection.execute("PRAGMA quick_check").fetchone()[0] != "ok":
                raise ValueError("SQLite integrity check failed")
            meta = json.loads(
                connection.execute("SELECT value FROM metadata WHERE key='build'").fetchone()[0]
            )
            if meta.get("fingerprint") != fingerprint or meta.get("schema") != SCHEMA:
                raise ValueError("Discovery cache identity mismatch")
            if (
                connection.execute("SELECT count(*) FROM chunks").fetchone()[0]
                != meta["chunk_count"]
            ):
                raise ValueError("Discovery cache row count mismatch")
            connection.execute(
                "SELECT rowid FROM search WHERE search MATCH 'x74657374' LIMIT 1"
            ).fetchall()
            self._connection = connection
            return meta
        except (sqlite3.Error, ValueError, TypeError, KeyError, IndexError):
            if connection is not None:
                connection.close()
            return None

    def build(self) -> dict:
        self.close()
        _raw, parsed, index_manifest = self._saved()
        self.records = [row[2] for row in parsed["index/claims.jsonl"]]
        self.edges = [row[2] for row in parsed["index/graph.jsonl"]]
        self.symbols = [row[2] for row in parsed["index/symbols.jsonl"]]
        sources, exclusions, inaccessible = self._sources()
        fingerprint, identity = self._fingerprint(index_manifest, sources, exclusions, inaccessible)
        self._current_fingerprint = fingerprint
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        target = self.cache_dir.resolve() / f"discovery-{fingerprint}.sqlite3"
        cache_problem = None
        if target.exists():
            cached = self._open_cache(target, fingerprint)
            if cached is not None:
                self._meta = {
                    **cached,
                    "cache_reused": True,
                    "cache_path": str(target),
                    "freshness": "matched",
                }
                return dict(self._meta)
            preserved = target.with_name(
                target.stem + ".invalid-" + uuid.uuid4().hex + target.suffix
            )
            target.rename(preserved)
            cache_problem = (
                "Invalid cache preserved at " + str(preserved) + "; rebuilt from source bytes."
            )

        source_claims = defaultdict(list)
        for record in self.records:
            path, bounds = _locator(str(record.get("where", "")), sources)
            if path in sources:
                if record["id"].startswith("DERIV:") and bounds is None:
                    continue
                source_claims[path].append((record["id"], bounds))

        rows = []
        for number, raw_line, record in parsed["index/claims.jsonl"]:
            fields = "\n".join(
                str(record.get(key) or "") for key in ("statement", "detail", "value")
            )
            rows.append(
                {
                    "id": record["id"],
                    "claim_ids": [record["id"]],
                    "text": raw_line,
                    "path": "index/claims.jsonl",
                    "start_line": number,
                    "end_line": number,
                    "start_col": 1,
                    "end_col": len(raw_line),
                    "source_sha256": index_manifest["index/claims.jsonl"]["sha256"],
                    "kind": "record",
                    "statement": str(record.get("statement", "")),
                    "source_locator": str(record.get("where", "")),
                    "terms": _encoded(tokenize(fields)),
                    "title_terms": _encoded(tokenize(record["id"])),
                }
            )
        passage_count = 0
        for path, source in sorted(sources.items()):
            for first, last, first_col, last_col, excerpt in _passages(source["text"]):
                tokens = tokenize(excerpt)
                if not tokens:
                    continue
                claim_ids = sorted(
                    {
                        claim_id
                        for claim_id, bounds in source_claims[path]
                        if bounds is None or (first <= bounds[1] and last >= bounds[0])
                    }
                )
                chunk_identity = [path, source["sha256"], first, last, first_col, last_col]
                rows.append(
                    {
                        "id": "PASSAGE:" + _sha(_json(chunk_identity).encode()),
                        "claim_ids": claim_ids,
                        "claim_spans": {
                            claim_id: {
                                "start_line": max(first, bounds[0]) if bounds else first,
                                "end_line": min(last, bounds[1]) if bounds else last,
                                "scope": "registered_lines" if bounds else "source_document",
                            }
                            for claim_id, bounds in source_claims[path]
                            if claim_id in claim_ids
                        },
                        "text": excerpt,
                        "path": path,
                        "start_line": first,
                        "end_line": last,
                        "start_col": first_col,
                        "end_col": last_col,
                        "source_sha256": source["sha256"],
                        "kind": "passage",
                        "statement": "",
                        "source_locator": f"{path}:{first}",
                        "terms": _encoded(tokens),
                        "title_terms": _encoded(tokenize(path)),
                    }
                )
                passage_count += 1
        meta = {
            **identity,
            "fingerprint": fingerprint,
            "source_count": len(sources),
            "record_count": len(self.records),
            "edge_count": len(self.edges),
            "symbol_count": len(self.symbols),
            "chunk_count": len(rows),
            "passage_count": passage_count,
            "source_exclusions": exclusions,
            "exclusion_count": len(exclusions),
            "inaccessible_count": len(inaccessible),
            "execution": {"checks_executed": 0, "lean_compiled": False},
            "freshness": "matched",
        }
        handle, temporary_name = tempfile.mkstemp(
            prefix="discovery-", suffix=".sqlite3", dir=self.cache_dir
        )
        os.close(handle)
        temporary = Path(temporary_name)
        connection = sqlite3.connect(temporary)
        try:
            connection.executescript("""
                CREATE TABLE metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE chunks(rowid INTEGER PRIMARY KEY, id TEXT UNIQUE NOT NULL,
                                    data TEXT NOT NULL);
                CREATE VIRTUAL TABLE search USING fts5(terms, title_terms);
            """)
            for rowid, row in enumerate(rows, 1):
                terms, title_terms = row.pop("terms"), row.pop("title_terms")
                connection.execute(
                    "INSERT INTO chunks VALUES(?,?,?)", (rowid, row["id"], _json(row))
                )
                connection.execute(
                    "INSERT INTO search(rowid,terms,title_terms) VALUES(?,?,?)",
                    (rowid, terms, title_terms),
                )
            connection.execute("INSERT INTO metadata VALUES('build',?)", (_json(meta),))
            connection.commit()
        finally:
            connection.close()
        # Only the disposable cache target is replaced. A failed temporary is
        # retained for diagnosis; source and scientific index bytes are untouched.
        try:
            temporary.replace(target)
        except OSError:
            # A concurrent builder may already have published and opened this
            # exact content identity. Use its validated file; retain our temp.
            concurrent = self._open_cache(target, fingerprint) if target.exists() else None
            if concurrent is None:
                raise
            self._meta = {
                **concurrent,
                "cache_reused": True,
                "cache_path": str(target),
                "concurrent_build_reused": True,
            }
            return dict(self._meta)
        if self._open_cache(target, fingerprint) is None:
            raise ValueError("New discovery cache failed validation")
        self._meta = {**meta, "cache_reused": False, "cache_path": str(target)}
        if cache_problem:
            self._meta["cache_recovery"] = cache_problem
        return dict(self._meta)

    def search(self, query: str, limit: int = 100) -> list[dict]:
        if self._connection is None:
            self.build()
        if limit < 0:
            raise ValueError("Search limit must be nonnegative")
        terms = sorted(set(tokenize(query)))[:64]
        if not terms or limit == 0:
            return []
        match = " OR ".join(_encoded([term]) for term in terms)
        assert self._connection is not None
        rows = self._connection.execute(
            """
            SELECT chunks.data, bm25(search,1.0,0.2) AS rank
            FROM search JOIN chunks ON chunks.rowid=search.rowid
            WHERE search MATCH ? ORDER BY rank, chunks.id LIMIT ?
        """,
            (match, limit),
        ).fetchall()
        return [{**json.loads(raw), "score": -float(rank)} for raw, rank in rows]

    def _index_manifest(self) -> dict:
        """Hashes of the three saved index files, without re-parsing them."""
        manifest = {}
        for relative in INDEX_PATHS:
            path = self.root / relative
            if not self._safe_path(path):
                raise ValueError(f"Saved graph path escapes the checkout: {relative}")
            data = path.read_bytes()
            manifest[relative] = {"sha256": _sha(data), "bytes": len(data)}
        return manifest

    def metadata(self, check_current: bool = True, *, recheck: bool = True) -> dict:
        """Cache scope and freshness.

        By default every call rehashes the declared sources, so an edit made
        after the engine started is reported as ``stale`` even when its size
        and modification time are unchanged. A batch session that issues many
        queries against inputs it knows are untouched may pass
        ``recheck=False`` to reuse the observation ``build`` made; the result
        then says so in ``freshness_observation``.
        """
        if not self._meta:
            self.build()
        result = json.loads(_json(self._meta))
        if check_current and not recheck and self._current_fingerprint is not None:
            result["current_fingerprint"] = self._current_fingerprint
            result["freshness"] = (
                "matched" if self._current_fingerprint == result["fingerprint"] else "stale"
            )
            result["freshness_observation"] = "hashed at engine start in this process"
        elif check_current:
            try:
                index_manifest = self._index_manifest()
                sources, exclusions, inaccessible = self._sources()
                current, _identity = self._fingerprint(
                    index_manifest, sources, exclusions, inaccessible
                )
                result["current_fingerprint"] = current
                result["freshness"] = "matched" if current == result["fingerprint"] else "stale"
                result["freshness_observation"] = "sources rehashed for this call"
                self._current_fingerprint = current
            except (OSError, ValueError) as exc:
                result["freshness"] = "unavailable"
                result["freshness_error"] = str(exc)
        return result

    def close(self):
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def __enter__(self):
        return self

    def __exit__(self, *_exc):
        self.close()
