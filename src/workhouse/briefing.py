"""One explicit, content-identified THEORY GRAPH snapshot for every agent.

Saved mode parses the three saved files directly. It never takes the legacy
loaders' missing-file fallback into a live calculation. Matching provenance
means observed input bytes match; it is not a new proof or a new Lean build.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
import re
import stat
import subprocess
import sys
from dataclasses import asdict
from pathlib import Path

from . import check_cache

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = "workhouse-theory-graph/brief/v1"
PROTOCOL_VERSION = "workhouse-theory-graph/v1"
PROTOCOL_PATH = "docs/theory_graph_protocol.md"
STATE_PATH = ".graph-state/index-inputs.json"
INDEX_PATHS = ("index/claims.jsonl", "index/symbols.jsonl", "index/graph.jsonl")
INPUT_TREES = tuple(
    sorted(
        set(check_cache.INPUT_TREES)
        | {
            "src",
            "scripts",
            "research",
            "settlement",
            "pyproject.toml",
            "uv.lock",
            PROTOCOL_PATH,
        }
    )
)
SKIP_PARTS = {
    ".git",
    ".venv",
    "venv",
    ".lake",
    ".cache",
    "__pycache__",
    ".pytest_cache",
    ".pytest_temp",
    ".ruff_cache",
    ".mypy_cache",
    "build",
    "dist",
    "node_modules",
    ".graph-state",
    ".ipynb_checkpoints",
}
SKIP_SUFFIXES = {".pyc", ".pyo", ".olean", ".ilean"}
PIN_LINE = re.compile(r"^[0-9a-fA-F]{64}\s+\*?(.+)$")


class BriefingError(RuntimeError):
    def __init__(self, status: str, message: str):
        self.status = status
        super().__init__(message)


def data_hash(value) -> str:
    """SHA-256 of canonical UTF-8 JSON, without timestamps or host formatting."""
    raw = json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _file_record(raw: bytes) -> dict:
    return {"sha256": hashlib.sha256(raw).hexdigest(), "size": len(raw)}


def _manifest(files: dict) -> dict:
    return {"algorithm": "sha256", "files": files, "sha256": data_hash(files)}


def _read_stable(path: Path) -> bytes:
    try:
        before = path.stat()
        raw = path.read_bytes()
        after = path.stat()
    except OSError as exc:
        raise BriefingError("unavailable", f"cannot read {path}: {exc}") from exc
    if (before.st_size, before.st_mtime_ns, before.st_ino) != (
        after.st_size,
        after.st_mtime_ns,
        after.st_ino,
    ):
        raise BriefingError("changed_during_read", f"changed during read: {path}")
    return raw


def _input_paths(root: Path) -> set[Path]:
    def onerror(error):
        raise BriefingError("unavailable", f"cannot enumerate input: {error}") from error

    paths = set()
    for rel in INPUT_TREES:
        target = root / rel
        try:
            mode = target.stat().st_mode
        except FileNotFoundError:
            continue
        except OSError as exc:
            raise BriefingError("unavailable", f"cannot inspect input {target}: {exc}") from exc
        if stat.S_ISREG(mode):
            paths.add(target)
        elif stat.S_ISDIR(mode):
            for directory, dirs, files in os.walk(target, onerror=onerror):
                dirs[:] = sorted(d for d in dirs if d not in SKIP_PARTS)
                for name in dirs:
                    child = Path(directory) / name
                    if child.is_symlink() or not child.resolve().is_relative_to(root):
                        raise BriefingError(
                            "unavailable", f"linked input tree not scanned: {child}"
                        )
                for name in files:
                    path = Path(directory) / name
                    if path.suffix not in SKIP_SUFFIXES:
                        paths.add(path)
    # Hash actual locally pinned source bytes too, not merely the assertions in
    # SHA256SUMS. External archive inventory paths are outside this contract.
    for path in sorted(paths):
        if path.name != "SHA256SUMS":
            continue
        for line in _read_stable(path).decode("utf-8").splitlines():
            match = PIN_LINE.match(line.strip())
            if match:
                pinned = path.parent / match.group(1)
                if not pinned.resolve().is_relative_to(root):
                    raise BriefingError("unavailable", f"source pin leaves checkout: {pinned}")
                paths.add(pinned)
    return paths


def content_manifest(root: Path = ROOT) -> dict:
    """Hash tracked and untracked files in the declared input scope by bytes.

    Generated graph files and task receipts are separate from the input scope.
    Lean dependency source/pin files are included; build/package caches are not.
    """
    root = Path(root).resolve()
    files = {}
    for path in sorted(_input_paths(root)):
        rel = path.relative_to(root).as_posix()
        if not path.resolve().is_relative_to(root):
            raise BriefingError("unavailable", f"input leaves checkout: {rel}")
        files[rel] = _file_record(_read_stable(path))
    return _manifest(files)


def _read_index(root: Path, *, required: bool) -> dict[str, bytes]:
    raw = {}
    for rel in INDEX_PATHS:
        path = root / rel
        if not path.is_file():
            if required:
                raise BriefingError(
                    "unavailable", f"saved {rel} is missing; run workhouse index --write explicitly"
                )
            continue
        raw[rel] = _read_stable(path)
    return raw


def _index_manifest(raw: dict[str, bytes]) -> dict:
    return _manifest({rel: _file_record(value) for rel, value in sorted(raw.items())})


def _git(root: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "--no-optional-locks", "-C", str(root), *args],
            capture_output=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    # A successful status with inaccessible excludes is not a complete Git
    # observation. Keep Git availability explicit in that case.
    if result.returncode or result.stderr.strip():
        return None
    return result.stdout.decode("utf-8", errors="replace")


def _checkout(root: Path, manifest: dict) -> dict:
    revision = _git(root, "rev-parse", "HEAD")
    status = _git(
        root,
        "status",
        "--porcelain=v1",
        "-z",
        "--untracked-files=all",
        "--",
        *INPUT_TREES,
        "corpus-import",
        "index",
    )
    dirty = []
    if status is not None:
        fields = iter(status.split("\0"))
        for field in fields:
            if not field:
                continue
            mark, path = field[:2], field[3:]
            row = {"path": path, "status": mark}
            if "R" in mark or "C" in mark:
                row["original_path"] = next(fields, "")
            if path in manifest["files"] or path.startswith("index/") or "D" in mark:
                dirty.append(row)
    return {
        "root": str(root),
        "revision": revision.strip() if revision else None,
        "git_available": revision is not None and status is not None,
        "dirty": sorted(dirty, key=lambda row: row["path"]),
    }


def _runtime() -> dict:
    packages = {}
    for name in ("sympy", "PyYAML", "python-flint"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = "unavailable"
    return {"python": sys.version, "platform": sys.platform, "packages": packages}


def cache_observation(manifest: dict, *, fresh: bool = False):
    """A request-scoped byte-hash cache namespace, shared by brief and index -w."""
    return check_cache.observe(
        content_key=data_hash({"inputs": manifest["sha256"], "runtime": _runtime()}), fresh=fresh
    )


def _saved_views(raw: dict[str, bytes]):
    from .claims import Claim
    from .graph import Edge, Graph

    def rows(rel):
        return [json.loads(line) for line in raw[rel].decode("utf-8").splitlines() if line]

    try:
        catalogue = [Claim(**row) for row in rows(INDEX_PATHS[0])]
        symbols = rows(INDEX_PATHS[1])
        graph = Graph(edges=sorted(Edge(**row) for row in rows(INDEX_PATHS[2])), dangling=[])
        ids = [c.id for c in catalogue] + [f"SYM:{s['id']}" for s in symbols]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate catalogue or symbol IDs")
        nodes = set(ids)
        for edge in graph.edges:
            for endpoint in (edge.src, edge.dst):
                if endpoint not in nodes:
                    raise ValueError(f"unresolved graph endpoint {endpoint!r}")
    except (ValueError, TypeError, KeyError) as exc:
        raise BriefingError("unavailable", f"saved index is invalid: {exc}") from exc
    return catalogue, symbols, graph


def _rebuild(root: Path, manifest: dict, fresh: bool, progress: dict):
    from . import claims as claims_mod
    from . import graph as graph_mod

    if root != claims_mod.ROOT.resolve():
        raise BriefingError("unavailable", "live collection requires this module's own checkout")
    progress.update(
        {
            "mode": "fresh" if fresh else "rebuilt",
            "execution_state": "incomplete",
            "executed": None,
            "cache_reused": None,
            "failed": None,
        }
    )
    with cache_observation(manifest, fresh=fresh) as observation:
        catalogue = claims_mod.collect()
    reused = {claims_mod.check_id(suite, name) for suite, name in observation["reused"]}
    checks = sorted(
        (
            {
                "id": c.id,
                "provenance": "cache_reused" if c.id in reused else "executed",
                "passed": c.status == "passing",
                "command": c.reproduce,
            }
            for c in catalogue
            if c.kind == "check"
        ),
        key=lambda row: row["id"],
    )
    verification = {
        "mode": "fresh" if fresh else "rebuilt",
        "execution_state": "complete",
        "scope": "registered Python catalogue checks",
        "recorded": 0,
        "cache_reused": sum(row["provenance"] == "cache_reused" for row in checks),
        "executed": sum(row["provenance"] == "executed" for row in checks),
        "failed": sum(not row["passed"] for row in checks),
        "checks": checks,
        "cache_key": "input content SHA-256 and Python runtime",
        "runtime": _runtime(),
        "lean": {"executed": False, "provenance": "recorded source and declaration coverage"},
    }
    # Preserve completed Python work even if later graph assembly fails. If
    # collection itself fails, incomplete/unknown counts remain explicit.
    progress.update(verification)
    symbols = claims_mod.symbol_records(catalogue)
    graph = graph_mod.build(catalogue, symbols)
    raw = {
        rel: ("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)).encode("utf-8")
        for rel, rows in zip(
            INDEX_PATHS,
            ([asdict(c) for c in catalogue], symbols, [asdict(edge) for edge in graph.edges]),
            strict=True,
        )
    }
    return (catalogue, symbols, graph), raw, verification


def _freshness(root: Path, inputs: dict, saved: dict) -> tuple[str, str]:
    path = root / STATE_PATH
    if not path.is_file():
        return "unknown", "no successful index-generation input record exists"
    try:
        state = json.loads(_read_stable(path))
    except (ValueError, BriefingError):
        return "unknown", "index-generation input record is unreadable"
    if (
        not isinstance(state, dict)
        or state.get("schema") != "workhouse-theory-graph/index-inputs/v1"
    ):
        return "unknown", "index-generation input record has an unsupported schema"
    if state.get("input_manifest") != inputs:
        return "stale", "current input bytes differ from the successful index-generation record"
    if state.get("snapshot") != saved:
        return "stale", "saved graph bytes differ from the successful index-generation record"
    return "matched", "input and saved graph bytes match a successful index-generation record"


def _neighborhoods(ids, views):
    from . import navigator

    catalogue, symbols, graph = views
    by_id = {c.id: asdict(c) for c in catalogue}
    by_id.update({f"SYM:{s['id']}": s for s in symbols})

    def one(query):
        # The ordinary navigator also adds current-ledger priority metadata.
        # A retained snapshot must use only this catalogue and graph, including
        # when inspecting another checkout's saved files.
        node = navigator._resolve(query, set(by_id), navigator._corpus_paths(catalogue))
        if node is None:
            return {"query": query, "error": f"no record with id {query!r}"}, False
        incoming = [asdict(edge) for edge in graph.edges if edge.dst == node]
        outgoing = [asdict(edge) for edge in graph.edges if edge.src == node]
        adjacent = {
            end for edge in incoming + outgoing for end in (edge["src"], edge["dst"]) if end != node
        }
        return {
            "id": node,
            "record": by_id[node],
            "incoming": incoming,
            "outgoing": outgoing,
            "neighbors": {key: by_id[key] for key in sorted(adjacent) if key in by_id},
        }, True

    targets, errors = [], []
    for query in sorted(set(ids)):
        data, found = one(query)
        if not found:
            errors.append(data["error"])
        else:
            routes = {
                key for key, record in data["neighbors"].items() if record.get("kind") == "route"
            }
            if data["record"].get("kind") == "route":
                routes.add(data["id"])
            data["routes"] = [one(key)[0] for key in sorted(routes)]
        targets.append(data)
    return targets, errors


def build_brief(ids, *, root: Path = ROOT, live: bool = False, fresh: bool = False) -> dict:
    """Return one deterministic snapshot, including explicit failure envelopes.

    ``fresh`` implies rebuilding and disables all per-check cache reads/writes.
    Default saved mode executes zero checks, even when an index file is absent.
    """
    root = Path(root).resolve()
    live = live or fresh
    ids = [ids] if isinstance(ids, str) else list(ids)
    result = {
        "schema": SCHEMA,
        "protocol_version": PROTOCOL_VERSION,
        "status": "ok",
        "errors": [],
        "checkout": {"root": str(root)},
        "targets": [],
        "input_scope": {
            "trees": list(INPUT_TREES),
            "skip_parts": sorted(SKIP_PARTS),
            "skip_suffixes": sorted(SKIP_SUFFIXES),
            "source_pins": "local SHA256SUMS",
            "external_archives": "identity recorded by local registries; not reread",
        },
        "snapshot": {"mode": "rebuilt" if live else "saved", "freshness": "unknown"},
        "verification": {
            "mode": "fresh" if fresh else "rebuilt" if live else "saved",
            "execution_state": "not_started",
            "recorded": 0,
            "cache_reused": 0,
            "executed": 0,
            "lean": {"executed": False, "provenance": "saved coverage"},
        },
    }
    try:
        if not ids or any(not isinstance(query, str) or not query.strip() for query in ids):
            raise BriefingError("invalid_target", "supply at least one nonempty target id")
        inputs = content_manifest(root)
        result["input_manifest"] = inputs
        result["protocol"] = {"path": PROTOCOL_PATH, **inputs["files"].get(PROTOCOL_PATH, {})}
        if "sha256" not in result["protocol"]:
            raise BriefingError("unavailable", f"shared protocol is missing: {PROTOCOL_PATH}")
        result["checkout"] = _checkout(root, inputs)
        before = _read_index(root, required=not live)
        saved = _index_manifest(before)
        if live:
            views, raw, verification = _rebuild(root, inputs, fresh, result["verification"])
            result["verification"] = verification
            freshness, reason = "matched", "rebuilt while the observed input bytes stayed equal"
        else:
            views, raw = _saved_views(before), before
            result["verification"]["recorded"] = sum(c.kind == "check" for c in views[0])
            freshness, reason = _freshness(root, inputs, saved)
        result["snapshot"].update(_index_manifest(raw))
        result["snapshot"].update(
            {"saved_files": saved["files"], "freshness": freshness, "freshness_reason": reason}
        )
        result["targets"], errors = _neighborhoods(ids, views)
        result["errors"].extend(errors)
        if errors:
            result["status"] = "invalid_target"
        if views[2].dangling:
            raise BriefingError(
                "unavailable", f"rebuilt graph has unresolved edges: {views[2].dangling}"
            )
        after_inputs = content_manifest(root)
        if inputs != after_inputs or before != _read_index(root, required=not live):
            raise BriefingError(
                "changed_during_read", "graph or input bytes changed during briefing"
            )
        if result["checkout"] != _checkout(root, after_inputs):
            raise BriefingError("changed_during_read", "checkout revision or dirty state changed")
    except BriefingError as exc:
        result["status"] = exc.status
        result["errors"].append(str(exc))
        if exc.status == "changed_during_read":
            result["snapshot"]["freshness"] = "changed_during_read"
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result["status"] = "unavailable"
        result["errors"].append(f"{type(exc).__name__}: {exc}")
    result["snapshot_fingerprint"] = data_hash(result)
    return result


def validate_brief(brief: dict, root: Path = ROOT, check_current: bool = True) -> list[str]:
    """Validate envelope integrity, then optionally compare current checkout bytes."""
    errors = []
    if not isinstance(brief, dict):
        return ["brief must be an object"]
    if brief.get("schema") != SCHEMA or brief.get("protocol_version") != PROTOCOL_VERSION:
        errors.append("unsupported brief schema or protocol version")
    if brief.get("status") != "ok":
        errors.append(f"brief status is {brief.get('status')!r}")
    if brief.get("snapshot_fingerprint") != data_hash(
        {key: value for key, value in brief.items() if key != "snapshot_fingerprint"}
    ):
        errors.append("brief snapshot fingerprint mismatch")
    for name in ("input_manifest", "snapshot"):
        manifest = brief.get(name, {})
        if not isinstance(manifest, dict) or not isinstance(manifest.get("files"), dict):
            errors.append(f"{name} must contain a files object")
        elif manifest.get("sha256") != data_hash(manifest.get("files", {})):
            errors.append(f"{name} content manifest digest mismatch")
    if not isinstance(brief.get("checkout"), dict):
        errors.append("checkout must be an object")
    if errors or not check_current:
        return errors
    try:
        root = Path(root).resolve()
        current = content_manifest(root)
        if brief.get("input_manifest") != current:
            errors.append("current input content differs from brief")
        if brief.get("checkout", {}).get("revision") != _checkout(root, current)["revision"]:
            errors.append("current checkout revision differs from brief")
        saved = _index_manifest(_read_index(root, required=False))["files"]
        if brief.get("snapshot", {}).get("saved_files") != saved:
            errors.append("current saved index content differs from brief")
        if brief.get("snapshot", {}).get("freshness") != "matched":
            errors.append(f"brief freshness is {brief.get('snapshot', {}).get('freshness')!r}")
        if current != content_manifest(root):
            errors.append("input content changed during brief validation")
    except (BriefingError, OSError, ValueError) as exc:
        errors.append(str(exc))
    return errors


def record_index_state(root: Path, inputs: dict) -> Path:
    """Called only after index -w converges and validates successfully."""
    root = Path(root).resolve()
    if inputs != content_manifest(root):
        raise BriefingError("changed_during_read", "index input bytes changed during generation")
    raw = _read_index(root, required=True)
    state = {
        "schema": "workhouse-theory-graph/index-inputs/v1",
        "input_manifest": inputs,
        "snapshot": _index_manifest(raw),
    }
    if inputs != content_manifest(root) or raw != _read_index(root, required=True):
        raise BriefingError("changed_during_read", "input or index bytes changed while recording")
    target = root / STATE_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(f".{os.getpid()}.tmp")
    with temporary.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(state, sort_keys=True) + "\n")
    temporary.replace(target)
    return target


def startup_text(root: Path = ROOT) -> str:
    """Small common adapter payload. Never imports a collector or runs checks."""
    root = Path(root).resolve()
    path = root / PROTOCOL_PATH
    if not path.is_file():
        raise BriefingError("unavailable", f"shared THEORY GRAPH protocol missing: {path}")
    digest = _file_record(_read_stable(path))["sha256"]
    missing = [rel for rel in INDEX_PATHS if not (root / rel).is_file()]
    state = "unavailable: " + ", ".join(missing) if missing else "present; freshness not assessed"
    return (
        f"WORKHOUSE THEORY GRAPH | {PROTOCOL_VERSION}\n"
        f"Read {PROTOCOL_PATH} (SHA-256 {digest}).\n"
        f"Checkout: {root}\nSaved graph: {state}.\n"
        "Before mathematical work run workhouse brief ID --json --out .graph-state/START.json.\n"
        "Saved verdicts, cache reuse and request executions are separate. Check freshness; "
        "read the named source hypotheses and formal scope. Preserve route closures.\n"
        "Use the protocol's manual task record for the research handoff."
    )


def render_text(brief: dict) -> str:
    """Readable orientation with complete records; JSON is the retained envelope."""
    snapshot = brief["snapshot"]
    verification = brief["verification"]
    lines = [
        f"WORKHOUSE THEORY GRAPH | {PROTOCOL_VERSION}",
        f"Status: {brief['status']} | {snapshot['mode']} | freshness: {snapshot['freshness']}",
        f"Checkout: {brief['checkout']['root']}",
        f"Fingerprint: {brief['snapshot_fingerprint']}",
        f"Python checks: {verification['recorded']} saved, "
        f"{verification['cache_reused']} cached, {verification['executed']} executed; "
        "Lean build: not executed",
    ]
    lines.extend(f"Error: {error}" for error in brief["errors"])
    for target in brief["targets"]:
        lines.extend(["", json.dumps(target, indent=2, ensure_ascii=True, sort_keys=True)])
    lines.append("\nUse --json --out PATH to retain the full input and graph provenance.")
    return "\n".join(lines)
