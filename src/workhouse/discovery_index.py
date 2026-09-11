"""Local, content-addressed retrieval over saved records and source passages.

This disposable SQLite index never executes a registered check and never writes
scientific records. Scores select reading candidates; their scientific standing
remains in the original catalogue. Source excerpts retain line and byte hashes.

External workstation roots declared in ``graph-tasks/discovery/scope.yaml``
(see :mod:`workhouse.discovery_scope`) are walked after the checkout's own
roots. Their files carry ``ext:<label>/`` locators, are deduplicated by
content hash against everything indexed before them, and are freshness-checked
by size and modification time between builds; the checkout's roots keep the
full content rehash on every call.
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

from . import discovery_scope as scope_module

SCHEMA = "workhouse-discovery-index/v1"
FRESHNESS_POLICY = {
    "internal": "content-hash every call",
    "external": "stat then content-hash on change",
}
INTERNAL_LABEL = "checkout"
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
    def __init__(self, root: Path, cache_dir: Path | None = None, *, verify_cache: bool = False):
        """``verify_cache`` runs SQLite's page-level quick_check when a cache is
        reused. It costs about half a second per 100 MB, so ordinary queries
        rely on the identity, row-count and probe checks and let a corrupt
        page surface as a query error; ``discover build`` and ``info`` verify."""
        self.root = Path(root).resolve()
        self.verify_cache = verify_cache
        self.cache_dir = (
            Path(cache_dir) if cache_dir is not None else self.root / ".graph-state/discovery"
        )
        self.records: list[dict] = []
        self.edges: list[dict] = []
        self.symbols: list[dict] = []
        self._connection: sqlite3.Connection | None = None
        self._meta: dict = {}
        self._current_fingerprint: str | None = None
        # External files seen by the last content pass: locator -> size,
        # mtime_ns and sha256. A later stat-policy pass reuses the hash of a
        # file whose size and mtime are unchanged and rereads any other.
        self._external_stat: dict[str, dict] = {}
        self.scope: scope_module.Scope | None = None

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

    def _sources(self, *, policy: str = "content"):
        """Checkout sources (always content-hashed), then external roots.

        ``policy`` reaches only the external walk; see ``_external_sources``.
        """
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
        external = self._external_sources(sources, exclusions, inaccessible, policy=policy)
        return sources, exclusions, inaccessible, external

    def _external_sources(self, sources, exclusions, inaccessible, *, policy: str) -> dict:
        """Walk the declared external roots after the checkout's own sources.

        ``policy`` is ``"content"`` (read and hash every file; used by
        ``build``) or ``"stat"`` (reuse the recorded hash of a file whose size
        and mtime_ns are unchanged; used by ``metadata`` rechecks). Content is
        deduplicated: a file whose sha256 was already indexed becomes an alias
        of that source and is not chunked again, so the flat ``GITHUB`` mirror
        and the three copies of every snapshot cost one passage set.
        """
        report: dict[str, Any] = {
            "declared": False,
            "base": None,
            "scope": None,
            "roots": [],
            "aliases": {},
            "stat": {},
            "labels": [],
        }
        self.scope = scope_module.load_scope(self.root)
        if self.scope is None:
            return report
        scope = self.scope
        report["declared"] = True
        report["base"] = str(scope.base) if scope.base is not None else None
        report["scope"] = scope.report(self.root)
        report["exclude_names"] = list(scope.exclude_names)
        report["exclude"] = list(scope.exclude)
        protected = scope_module.protected_paths(scope)
        name_matcher = scope_module.Matcher(scope.exclude_names)
        global_matcher = scope_module.Matcher(scope.exclude)
        by_sha: dict[str, str] = {}
        for path in sorted(sources):
            by_sha.setdefault(sources[path]["sha256"], path)
        aliases: dict[str, list[str]] = {}
        stat_map: dict[str, dict] = {}
        rows = scope_module.resolve_roots(scope, self.root)
        for root, row in zip(scope.roots, rows, strict=True):
            row.update({"files": 0, "sources": 0, "aliases": 0, "bytes": 0, "passages": 0})
            report["roots"].append(row)
            if row["skipped"]:
                continue
            report["labels"].append(root.label)
            self._walk_external(
                root,
                Path(row["absolute"]),
                row,
                sources=sources,
                exclusions=exclusions,
                inaccessible=inaccessible,
                by_sha=by_sha,
                aliases=aliases,
                stat_map=stat_map,
                matchers=(name_matcher, global_matcher, scope_module.Matcher(root.exclude)),
                protected=protected,
                policy=policy,
            )
        report["aliases"] = {sha: paths for sha, paths in sorted(aliases.items())}
        report["stat"] = stat_map
        return report

    def _walk_external(
        self,
        root,
        directory: Path,
        row: dict,
        *,
        sources,
        exclusions,
        inaccessible,
        by_sha,
        aliases,
        stat_map,
        matchers,
        protected,
        policy: str,
    ) -> None:
        """One ``scandir`` per directory; no path is resolved or followed below the root.

        The root was resolved and containment-checked by ``resolve_roots``.
        Reparse points are refused from the directory listing, so a real
        subdirectory's canonical path is its parent's canonical path plus its
        name; the containment check against the checkout and the protected
        subtrees is then path arithmetic, and the per-directory ``resolve``
        that dominated the freshness recheck is gone. A subdirectory whose
        listing holds ``.git`` is a nested checkout and is skipped whole.
        """
        name_matcher, global_matcher, root_matcher = matchers
        base_prefix = "" if root.path == "." else root.path + "/"
        try:
            resolved_root = directory.resolve(strict=True)
        except OSError as exc:
            inaccessible.append({"path": str(directory), "reason": type(exc).__name__})
            return
        forbidden = [self.root, *(Path(item) for item in protected)]
        stack: list[tuple[Path, str]] = [(directory, "")]
        while stack:
            current_path, relative_dir = stack.pop()
            depth = relative_dir.count("/") + 1 if relative_dir else 0
            try:
                with os.scandir(current_path) as listing:
                    entries = sorted(listing, key=lambda entry: entry.name)
            except OSError as exc:
                inaccessible.append({"path": str(current_path), "reason": type(exc).__name__})
                continue
            if relative_dir and any(entry.name == ".git" for entry in entries):
                exclusions.append(
                    {
                        "path": scope_module.locator(root.label, relative_dir),
                        "reason": "git_checkout",
                    }
                )
                continue
            subdirectories: list[tuple[Path, str]] = []
            for entry in entries:
                name = entry.name
                child_relative = f"{relative_dir}/{name}" if relative_dir else name
                locator = scope_module.locator(root.label, child_relative)
                try:
                    status = entry.stat(follow_symlinks=False)
                except OSError as exc:
                    inaccessible.append({"path": locator, "reason": type(exc).__name__})
                    continue
                reparse = stat_module.S_ISLNK(status.st_mode) or bool(
                    getattr(status, "st_file_attributes", 0)
                    & getattr(stat_module, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
                )
                if stat_module.S_ISDIR(status.st_mode) or (
                    reparse and not stat_module.S_ISREG(status.st_mode)
                ):
                    reason = None
                    if root.max_depth is not None and depth >= root.max_depth:
                        reason = "depth_limit"
                    elif name.lower() in SKIP_PARTS or name_matcher.match(name):
                        reason = "excluded_directory"
                    elif root_matcher.match(child_relative) or global_matcher.match(
                        base_prefix + child_relative
                    ):
                        reason = "scope_exclusion"
                    elif reparse:
                        reason = "reparse_point"
                    else:
                        canonical = resolved_root.joinpath(*child_relative.split("/"))
                        if any(
                            canonical == item or canonical.is_relative_to(item)
                            for item in forbidden
                        ):
                            reason = "unsafe_path"
                    if reason is None:
                        subdirectories.append((Path(entry.path), child_relative))
                    else:
                        exclusions.append({"path": locator, "reason": reason})
                    continue
                if Path(name).suffix.lower() not in EXTENSIONS:
                    continue
                file_relative = child_relative
                path = Path(entry.path)
                if root_matcher.match(file_relative) or global_matcher.match(
                    base_prefix + file_relative
                ):
                    exclusions.append({"path": locator, "reason": "scope_exclusion"})
                    continue
                if reparse or not stat_module.S_ISREG(status.st_mode):
                    exclusions.append({"path": locator, "reason": "unsafe_path"})
                    continue
                if status.st_size > MAX_SOURCE_BYTES:
                    exclusions.append({"path": locator, "reason": "size_limit"})
                    continue
                cached = self._external_stat.get(locator) if policy == "stat" else None
                if (
                    cached is not None
                    and cached["bytes"] == status.st_size
                    and cached["mtime_ns"] == status.st_mtime_ns
                ):
                    sha, size, text = cached["sha256"], cached["bytes"], None
                else:
                    try:
                        raw = path.read_bytes()
                        if len(raw) > MAX_SOURCE_BYTES:
                            exclusions.append({"path": locator, "reason": "size_limit"})
                            continue
                        text = raw.decode("utf-8")
                    except UnicodeError:
                        exclusions.append({"path": locator, "reason": "non_utf8"})
                        continue
                    except OSError as exc:
                        inaccessible.append({"path": locator, "reason": type(exc).__name__})
                        continue
                    sha, size = _sha(raw), len(raw)
                stat_map[locator] = {
                    "sha256": sha,
                    "bytes": size,
                    "mtime_ns": status.st_mtime_ns,
                }
                row["files"] += 1
                if sha in by_sha:
                    aliases.setdefault(sha, []).append(locator)
                    row["aliases"] += 1
                    continue
                by_sha[sha] = locator
                sources[locator] = {
                    "sha256": sha,
                    "bytes": size,
                    "text": text,
                    "external": True,
                    "source_label": root.label,
                    "tier": root.tier,
                }
                row["sources"] += 1
                row["bytes"] += size
            # Depth-first in sorted order, so exclusions and errors are listed
            # deterministically and the identity is stable across runs.
            stack.extend(reversed(subdirectories))

    @staticmethod
    def _fingerprint(index_manifest, sources, exclusions, inaccessible, external=None):
        source_manifest = {
            path: {key: source[key] for key in ("sha256", "bytes")}
            for path, source in sorted(sources.items())
        }
        external = external or {}
        scope = external.get("scope") or {}
        identity = {
            "schema": SCHEMA,
            "index_manifest": index_manifest,
            "source_manifest": source_manifest,
            "exclusions": exclusions,
            "inaccessible_files": inaccessible,
            # Alias groups are part of the identity because passage rows list
            # them; a new byte-identical copy changes what a reader is shown.
            "aliases": external.get("aliases", {}),
            "settings": {
                "roots": SOURCE_ROOTS,
                "extensions": sorted(EXTENSIONS),
                "skip_parts": sorted(SKIP_PARTS),
                "max_source_bytes": MAX_SOURCE_BYTES,
                "chunk_tokens": CHUNK_TOKENS,
                "max_chunk_chars": MAX_CHUNK_CHARS,
                # Labels of the external roots actually walked, and the full
                # declaration (paths, tiers, exclusions, presence) behind them.
                "external_roots": list(external.get("labels", [])),
                "external_scope": {
                    "schema": scope.get("schema"),
                    "version": scope.get("version"),
                    "roots": [
                        {
                            key: row[key]
                            for key in (
                                "label",
                                "path",
                                "tier",
                                "max_depth",
                                "exclude",
                                "present",
                                "skipped",
                            )
                        }
                        for row in external.get("roots", [])
                        if row["enabled"]
                    ],
                    "exclude_names": external.get("exclude_names", []),
                    "exclude": external.get("exclude", []),
                    "protected": scope.get("protected", []),
                },
            },
            "implementation_sha256": _sha(Path(__file__).read_bytes()),
        }
        return _sha(_json(identity).encode()), identity

    def _open_cache(self, path: Path, fingerprint: str) -> dict | None:
        connection = None
        try:
            connection = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
            if self.verify_cache and connection.execute("PRAGMA quick_check").fetchone()[0] != "ok":
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
        sources, exclusions, inaccessible, external = self._sources()
        self._external_stat = external["stat"]
        fingerprint, identity = self._fingerprint(
            index_manifest, sources, exclusions, inaccessible, external
        )
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
        aliases = external["aliases"]
        passages_by_label: dict[str, int] = defaultdict(int)
        for path, source in sorted(sources.items()):
            label = source.get("source_label", INTERNAL_LABEL)
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
                        # Byte-identical copies elsewhere; they were not chunked.
                        "aliases": list(aliases.get(source["sha256"], [])),
                        "external": bool(source.get("external", False)),
                        "source_label": label,
                        "terms": _encoded(tokens),
                        "title_terms": _encoded(tokenize(path)),
                    }
                )
                passage_count += 1
                passages_by_label[label] += 1
        for row in external["roots"]:
            row["passages"] = passages_by_label.get(row["label"], 0)
        meta = {
            **identity,
            "fingerprint": fingerprint,
            "source_count": len(sources),
            "internal_source_count": sum(1 for s in sources.values() if not s.get("external")),
            "external_source_count": sum(1 for s in sources.values() if s.get("external")),
            "record_count": len(self.records),
            "edge_count": len(self.edges),
            "symbol_count": len(self.symbols),
            "chunk_count": len(rows),
            "passage_count": passage_count,
            "source_exclusions": exclusions,
            "exclusion_count": len(exclusions),
            "inaccessible_count": len(inaccessible),
            "external_base": external["base"],
            "external_scope": external["scope"],
            "external_roots": [
                {key: value for key, value in row.items() if key != "exclude"}
                for row in external["roots"]
            ],
            "alias_count": sum(len(paths) for paths in aliases.values()),
            "freshness_policy": dict(FRESHNESS_POLICY),
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

        By default every call rehashes the checkout's declared sources, so an
        edit made after the engine started is reported as ``stale`` even when
        its size and modification time are unchanged. External workstation
        roots are rechecked by size and ``mtime_ns`` against the last content
        pass (``freshness_policy``): a changed stat rehashes that file, an
        edit that preserves both is not detected until the next ``build``.
        A batch session that issues many queries against inputs it knows are
        untouched may pass ``recheck=False`` to reuse the observation
        ``build`` made; the result then says so in ``freshness_observation``.
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
                sources, exclusions, inaccessible, external = self._sources(policy="stat")
                current, _identity = self._fingerprint(
                    index_manifest, sources, exclusions, inaccessible, external
                )
                result["current_fingerprint"] = current
                result["freshness"] = "matched" if current == result["fingerprint"] else "stale"
                result["freshness_observation"] = "sources rehashed for this call" + (
                    "; external files stat-checked and rehashed on change"
                    if external["labels"]
                    else ""
                )
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
