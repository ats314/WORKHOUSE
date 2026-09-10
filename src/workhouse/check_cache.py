"""Per-check result cache, keyed on everything a check can read.

A full ``verify`` runs 265 checks in about four minutes; a regeneration of
the views runs them three times over (frontier, certified, catalogue) and the
catalogue loops to a fixpoint on top. A session that edits one check pays the
whole bill on every regeneration, and the 2026-09-01 session hit the
stale-index cycle twice waiting for it. The corpus scan already solved the
same problem for itself (``corpus_index.scan_cached``): fingerprint the
inputs, memoise on disk outside the repository, rebuild on any change.

This is that, for checks. Two rules keep it honest:

* **The key covers every input.** Not the check's own source alone -- a
  check reaches helpers, the constants registry, the ledgers, the pinned
  paper, the runs and the notes register -- so the key is a fingerprint of
  the whole ``src/workhouse`` tree and every data tree a check can open,
  by path, size and mtime. Any edit anywhere invalidates everything, which
  costs one four-minute run and never a stale verdict. The pinned corpus
  enters through its manifest rather than its 928 files, because the
  manifest is what a change to it must touch. The generated ``index/`` is
  keyed separately and only for the checks whose source names it, so the
  catalogue's fixpoint loop does not invalidate the other 264 on each pass.
* **``workhouse verify`` never reads it.** That command is the promise
  "re-derive it now", and a cached verdict is not a re-derivation. The
  cache serves the collectors -- the catalogue, CERTIFIED.md, FRONTIER.md
  -- whose job is to render verdicts that the tests hold equal to live ones.

``WORKHOUSE_NO_CACHE=1`` disables reads and writes everywhere.
Briefing observations provide a separate content-hash namespace and report
reuse; their ``fresh`` mode disables reads and writes for that request only.
"""

from __future__ import annotations

import hashlib
import json
import os
import stat
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

#: Trees a check may read, fingerprinted file by file. corpus-import enters
#: through its manifest (below), not its files.
INPUT_TREES = (
    "src/workhouse",
    "ledger",
    "paper",
    "runs",
    "literature",
    "notes",
    "theory",
    "docs/decisions",
    "docs/derivations",
    "lean",
    "verify_core.py",
    "scripts/verify_source_current_bridges.py",
    "scripts/verify_theory_geometry_bridges.py",
    "corpus-import/SHA256SUMS",
    "corpus-import/records",
)
#: Only checks whose source mentions the generated index are keyed on it.
INDEX_TREE = "index"
INDEX_TOKENS = ("index/", "GRAPH", "CLAIMS", "INDEX_DIR", "load_catalogue", "graph.jsonl")
SKIP_PARTS = {"__pycache__", ".git", ".venv", ".lake", "build", "imported"}

# Request-local provenance keeps fresh collection from changing process-wide
# cache settings or interfering with another caller's reuse report.
_OBSERVATION: ContextVar[dict | None] = ContextVar("workhouse_check_observation", default=None)


@contextmanager
def observe(*, content_key: str, fresh: bool = False):
    """Use a byte-identified namespace and report reuse for one collection."""
    report = {"content_key": content_key, "fresh": fresh, "reused": []}
    token = _OBSERVATION.set(report)
    try:
        yield report
    finally:
        _OBSERVATION.reset(token)


def _index_content_fingerprint() -> str:
    """Hash index bytes; never reuse a result after an incomplete index scan."""
    hasher = hashlib.sha256()
    for path in _walk(INDEX_TREE, strict=True):
        hasher.update(path.relative_to(ROOT).as_posix().encode("utf-8") + b"\0")
        hasher.update(hashlib.sha256(path.read_bytes()).digest())
    return hasher.hexdigest()


def enabled() -> bool:
    return os.environ.get("WORKHOUSE_NO_CACHE", "") not in ("1", "true", "yes")


def _cache_dir() -> Path:
    return Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "workhouse" / "checks"


def _walk(rel: str, *, strict: bool = False):
    target = ROOT / rel
    if strict:
        try:
            mode = target.stat().st_mode
        except FileNotFoundError:
            return
        is_file, is_dir = stat.S_ISREG(mode), stat.S_ISDIR(mode)
    else:
        is_file, is_dir = target.is_file(), target.is_dir()
    if is_file:
        yield target
        return
    if not is_dir:
        return
    if any(part in SKIP_PARTS for part in target.parts):
        return

    def onerror(error: OSError) -> None:
        # Legacy metadata keys retain their permission skips. Content-observed
        # collections must fail rather than certify an incomplete byte scan.
        if strict or not isinstance(error, PermissionError):
            raise error

    paths = []
    for directory, directories, filenames in os.walk(target, onerror=onerror):
        # Prune before descent: filtering rglob results still scans dependency caches.
        directories[:] = [name for name in directories if name not in SKIP_PARTS]
        for name in filenames:
            path = Path(directory) / name
            if name in SKIP_PARTS:
                continue
            is_file = stat.S_ISREG(path.stat().st_mode) if strict else path.is_file()
            if is_file:
                paths.append(path)
    yield from sorted(paths)


def fingerprint(trees=INPUT_TREES) -> str:
    """One digest over path, size and mtime of every file in the input trees."""
    hasher = hashlib.sha256()
    for rel in trees:
        for path in _walk(rel):
            try:
                st = path.stat()
            except OSError:
                continue
            hasher.update(
                f"{path.relative_to(ROOT).as_posix()}|{st.st_size}|{st.st_mtime_ns}\n".encode()
            )
    return hasher.hexdigest()


class CheckCache:
    """Lookups for one run: the fingerprints are computed once."""

    def __init__(self) -> None:
        self.observation = _OBSERVATION.get()
        self.on = enabled() and not (self.observation and self.observation["fresh"])
        if self.on and self.observation is not None:
            self.core = "content-v1:" + self.observation["content_key"]
            self.index = _index_content_fingerprint()
        else:
            self.core = fingerprint() if self.on else ""
            self.index = fingerprint((INDEX_TREE,)) if self.on else ""
        self.hits = 0
        self.misses = 0
        self.identities: dict[str, tuple[str, str]] = {}

    def key(self, suite: str, name: str, source: str) -> str:
        reads_index = any(token in source for token in INDEX_TOKENS)
        material = f"{self.core}|{self.index if reads_index else ''}|{suite}|{name}"
        key = hashlib.sha256(material.encode("utf-8")).hexdigest()
        self.identities[key] = (suite, name)
        return key

    def get(self, key: str) -> dict | None:
        if not self.on:
            return None
        path = _cache_dir() / f"{key}.json"
        if not path.exists():
            self.misses += 1
            return None
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            self.misses += 1
            return None
        self.hits += 1
        identity = self.identities.get(key)
        if self.observation is not None and identity is not None:
            self.observation["reused"].append(identity)
        return data

    def put(self, key: str, result) -> None:
        if not self.on:
            return
        try:
            directory = _cache_dir()
            directory.mkdir(parents=True, exist_ok=True)
            tmp = directory / f"{key}.json.tmp"
            tmp.write_text(json.dumps(asdict(result), sort_keys=True), encoding="utf-8")
            tmp.replace(directory / f"{key}.json")
        except OSError:
            pass  # a cache is a convenience, never a requirement


def clear() -> int:
    """Delete every cached result; returns how many were removed."""
    directory = _cache_dir()
    if not directory.exists():
        return 0
    n = 0
    for path in directory.glob("*.json"):
        path.unlink()
        n += 1
    return n
