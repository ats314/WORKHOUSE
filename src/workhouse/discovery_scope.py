"""External workstation roots for discovery indexing.

The discovery index reads the checkout's own source roots. The maintainer's
workstation also holds preserved collections outside every checkout
(``ALL THEORY``, ``ARCHIVE``, the intake folder, research campaigns). This
module declares which of those directories may be read, from the versioned
scope file ``graph-tasks/discovery/scope.yaml``, and resolves them against a
workstation base directory. It writes nothing and never turns an external
path into a scientific record: passages from these roots are T3 reading
candidates carrying an ``ext:<label>/`` locator.

Rules and the failure each prevents:

* Roots are declared relative to a base, never absolute, so a scope file
  checked into the repository cannot pin one workstation's drive layout and
  silently index nothing, or something else, on another machine.
* An absent root is reported and skipped, never an error, because the same
  scope file is loaded on CI and on collaborators' machines where the
  workstation folders do not exist.
* Labels use a small character set and must be unique, because they become
  the ``ext:<label>/`` locator prefix and must never collide with each other
  or with a checkout-relative path.
* Exclusion globs are matched on POSIX-style relative paths, so Windows and
  Linux make the same decisions and produce the same cache fingerprint.
* Reparse points (symlinks and NTFS junctions) are never followed:
  ``Path.is_symlink()`` is False for a junction, and the workstation keeps
  22 root junctions into ``ARCHIVE`` that would otherwise be indexed twice.
* No external path may resolve inside the checkout or into the canonical
  checkout's ``ledger/`` or ``index/``; those trees are the scientific graph
  and already reach discovery through the saved catalogue.
"""

from __future__ import annotations

import contextlib
import json
import os
import re
import stat as stat_module
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any

import yaml

SCHEMA = "workhouse-discovery-scope/v1"
LOCAL_SCHEMA = "workhouse-discovery-scope-local/v1"
REPORT_SCHEMA = "workhouse-discovery-scope/report/v1"
SCOPE_PATH = "graph-tasks/discovery/scope.yaml"
LOCAL_PATH = ".graph-state/discovery/scope.local.yaml"
BASE_ENV = "WORKHOUSE_DISCOVERY_BASE"
WORKSPACE_MARKER = "WORKSPACE.json"
DEFAULT_CANONICAL = "REPO"
PROTECTED_SUBTREES = ("ledger", "index")
TIERS = (1, 2, 3)
LOCATOR_PREFIX = "ext:"
_LABEL = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")


def _sha(raw: bytes) -> str:
    import hashlib

    return hashlib.sha256(raw).hexdigest()


def is_reparse_point(path: Path | str) -> bool:
    """True for a symlink, an NTFS junction or any other reparse point.

    ``Path.is_symlink()`` reports False for junctions, so a walker relying on
    it alone would descend the workstation's root junctions into ``ARCHIVE``.
    One ``lstat`` answers both questions without following the link.
    """
    try:
        status = os.lstat(path)
    except OSError:
        return False
    if stat_module.S_ISLNK(status.st_mode):
        return True
    attributes = getattr(status, "st_file_attributes", 0)
    reparse = getattr(stat_module, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    return bool(attributes & reparse)


def glob_to_regex(pattern: str) -> str:
    """Translate a path glob to a regular expression over POSIX relative paths.

    ``**`` spans directory levels, ``*`` and ``?`` stay inside one segment,
    and a trailing ``/**`` also matches the directory itself so that a
    pattern like ``GITHUB/**`` prunes ``GITHUB`` before it is entered.
    """
    out: list[str] = []
    i, n = 0, len(pattern)
    while i < n:
        char = pattern[i]
        if pattern.startswith("/**", i) and i + 3 == n:
            out.append("(?:/.*)?")
            i += 3
        elif pattern.startswith("**/", i):
            out.append("(?:.*/)?")
            i += 3
        elif pattern.startswith("**", i):
            out.append(".*")
            i += 2
        elif char == "*":
            out.append("[^/]*")
            i += 1
        elif char == "?":
            out.append("[^/]")
            i += 1
        else:
            out.append(re.escape(char))
            i += 1
    return "".join(out)


def normalize_pattern(pattern: str) -> str:
    text = pattern.replace("\\", "/").strip()
    while text.startswith("./"):
        text = text[2:]
    return text.strip("/")


class Matcher:
    """Ordered glob patterns; ``match`` names the first pattern that applies.

    Matching ignores case because the workstation's NTFS volumes do, so a
    pattern written as ``FINAL PAPERS/**`` must exclude ``Final Papers``.
    """

    def __init__(self, patterns) -> None:
        self.patterns = tuple(normalize_pattern(p) for p in patterns)
        self._compiled = [
            (pattern, re.compile(glob_to_regex(pattern), re.IGNORECASE))
            for pattern in self.patterns
            if pattern
        ]

    def match(self, relative: str) -> str | None:
        for pattern, regex in self._compiled:
            if regex.fullmatch(relative):
                return pattern
        return None

    def __bool__(self) -> bool:
        return bool(self._compiled)


@dataclass(frozen=True)
class ExternalRoot:
    label: str
    path: str
    tier: int
    enabled: bool = True
    exclude: tuple[str, ...] = ()
    max_depth: int | None = None
    note: str = ""

    def declaration(self) -> dict:
        """The identity-relevant part of the declaration (no free-text note)."""
        return {
            "label": self.label,
            "path": self.path,
            "tier": self.tier,
            "enabled": self.enabled,
            "exclude": list(self.exclude),
            "max_depth": self.max_depth,
        }


@dataclass
class Scope:
    schema: str
    version: int
    roots: tuple[ExternalRoot, ...]
    exclude_names: tuple[str, ...] = ()
    exclude: tuple[str, ...] = ()
    protected: tuple[str, ...] = ()
    path: Path | None = None
    sha256: str | None = None
    local_path: Path | None = None
    local_base: str | None = None
    local_disabled: tuple[str, ...] = ()
    local_enabled: tuple[str, ...] = ()
    base: Path | None = None
    base_source: str | None = None
    canonical: str = DEFAULT_CANONICAL
    errors: list[str] = field(default_factory=list)

    @property
    def enabled_roots(self) -> tuple[ExternalRoot, ...]:
        return tuple(root for root in self.roots if root.enabled)

    def declarations(self) -> dict:
        """What the cache fingerprint sees: enabled roots and exclusion policy."""
        return {
            "schema": self.schema,
            "version": self.version,
            "exclude_names": list(self.exclude_names),
            "exclude": list(self.exclude),
            "protected": list(self.protected),
            "roots": [root.declaration() for root in self.enabled_roots],
        }

    def report(self, root: Path | None = None) -> dict:
        return {
            "path": _relative_or_absolute(self.path, root),
            "schema": self.schema,
            "version": self.version,
            "sha256": self.sha256,
            "base": str(self.base) if self.base is not None else None,
            "base_source": self.base_source,
            "local_override": _relative_or_absolute(self.local_path, root),
            "local_disabled": list(self.local_disabled),
            "local_enabled": list(self.local_enabled),
            "protected": list(self.protected),
            "root_count": len(self.roots),
            "enabled_count": len(self.enabled_roots),
        }


def _relative_or_absolute(path: Path | None, root: Path | None) -> str | None:
    if path is None:
        return None
    if root is not None:
        try:
            return path.resolve().relative_to(Path(root).resolve()).as_posix()
        except (ValueError, OSError):
            pass
    return path.as_posix()


def _check_relative(text: str, what: str) -> str:
    if not isinstance(text, str) or not text.strip():
        raise ValueError(f"{what} must be a non-empty string")
    posix = text.replace("\\", "/").strip()
    if PureWindowsPath(posix).is_absolute() or PurePosixPath(posix).is_absolute():
        raise ValueError(f"{what} must be relative to the workstation base: {text!r}")
    if PureWindowsPath(posix).drive:
        raise ValueError(f"{what} must not carry a drive: {text!r}")
    parts = [part for part in posix.split("/") if part not in ("", ".")]
    if ".." in parts:
        raise ValueError(f"{what} must not climb above the base: {text!r}")
    return "/".join(parts) or "."


def _string_list(value: Any, what: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        raise ValueError(f"{what} must be a list of non-empty strings")
    return tuple(value)


def parse_root(entry: Any, position: int) -> ExternalRoot:
    if not isinstance(entry, dict):
        raise ValueError(f"roots[{position}] must be a mapping")
    unknown = set(entry) - {"label", "path", "tier", "enabled", "exclude", "max_depth", "note"}
    if unknown:
        raise ValueError(f"roots[{position}] has unknown keys: {sorted(unknown)}")
    label = entry.get("label")
    if not isinstance(label, str) or not _LABEL.match(label):
        raise ValueError(
            f"roots[{position}].label must match {_LABEL.pattern} (it becomes the ext: prefix)"
        )
    path = _check_relative(entry.get("path"), f"roots[{position}].path")
    tier = entry.get("tier")
    if tier not in TIERS or isinstance(tier, bool):
        raise ValueError(f"roots[{position}].tier must be one of {TIERS}")
    enabled = entry.get("enabled", True)
    if not isinstance(enabled, bool):
        raise ValueError(f"roots[{position}].enabled must be true or false")
    max_depth = entry.get("max_depth")
    if max_depth is not None and (
        isinstance(max_depth, bool) or not isinstance(max_depth, int) or max_depth < 0
    ):
        raise ValueError(f"roots[{position}].max_depth must be a nonnegative integer or null")
    exclude = tuple(
        _check_relative(item, f"roots[{position}].exclude")
        for item in _string_list(entry.get("exclude"), f"roots[{position}].exclude")
    )
    note = entry.get("note", "")
    if not isinstance(note, str):
        raise ValueError(f"roots[{position}].note must be a string")
    return ExternalRoot(label, path, tier, enabled, exclude, max_depth, note)


def parse_scope(data: Any, *, path: Path | None = None, sha256: str | None = None) -> Scope:
    """Validate a parsed scope document; every failure names the offending key."""
    if not isinstance(data, dict):
        raise ValueError("discovery scope must be a mapping")
    if data.get("schema") != SCHEMA:
        raise ValueError(f"discovery scope schema must be {SCHEMA!r}, got {data.get('schema')!r}")
    unknown = set(data) - {"schema", "version", "roots", "exclude_names", "exclude", "protected"}
    if unknown:
        raise ValueError(f"discovery scope has unknown keys: {sorted(unknown)}")
    version = data.get("version")
    if isinstance(version, bool) or not isinstance(version, int) or version < 1:
        raise ValueError("discovery scope version must be a positive integer")
    roots_data = data.get("roots")
    if not isinstance(roots_data, list):
        raise ValueError("discovery scope roots must be a list")
    roots = tuple(parse_root(entry, number) for number, entry in enumerate(roots_data))
    labels = [root.label for root in roots]
    duplicates = sorted({label for label in labels if labels.count(label) > 1})
    if duplicates:
        raise ValueError(f"duplicate root labels: {duplicates}")
    exclude_names = _string_list(data.get("exclude_names"), "exclude_names")
    if any("/" in name or "\\" in name for name in exclude_names):
        raise ValueError("exclude_names entries are directory names, not paths")
    exclude = tuple(
        _check_relative(item, "exclude") for item in _string_list(data.get("exclude"), "exclude")
    )
    protected = tuple(
        _check_relative(item, "protected")
        for item in _string_list(data.get("protected"), "protected")
    )
    return Scope(
        schema=SCHEMA,
        version=version,
        roots=roots,
        exclude_names=exclude_names,
        exclude=exclude,
        protected=protected,
        path=path,
        sha256=sha256,
    )


def apply_local(scope: Scope, data: Any, *, path: Path | None = None) -> Scope:
    """Apply ``scope.local.yaml``: a base override and per-label enable/disable.

    Unknown labels are errors rather than ignored, so a typo cannot leave a
    tier-3 root enabled while the operator believes it was switched off.
    """
    if not isinstance(data, dict):
        raise ValueError("local discovery scope must be a mapping")
    if data.get("schema") != LOCAL_SCHEMA:
        raise ValueError(f"local discovery scope schema must be {LOCAL_SCHEMA!r}")
    unknown = set(data) - {"schema", "base", "disable", "enable"}
    if unknown:
        raise ValueError(f"local discovery scope has unknown keys: {sorted(unknown)}")
    base = data.get("base")
    if base is not None and (not isinstance(base, str) or not base.strip()):
        raise ValueError("local discovery scope base must be a non-empty string")
    disable = _string_list(data.get("disable"), "disable")
    enable = _string_list(data.get("enable"), "enable")
    known = {root.label for root in scope.roots}
    missing = sorted(set(disable + enable) - known)
    if missing:
        raise ValueError(f"local discovery scope names unknown root labels: {missing}")
    both = sorted(set(disable) & set(enable))
    if both:
        raise ValueError(f"local discovery scope both enables and disables: {both}")
    roots = tuple(
        ExternalRoot(
            root.label,
            root.path,
            root.tier,
            (root.enabled or root.label in enable) and root.label not in disable,
            root.exclude,
            root.max_depth,
            root.note,
        )
        for root in scope.roots
    )
    scope.roots = roots
    scope.local_path = path
    scope.local_base = base
    scope.local_disabled = disable
    scope.local_enabled = enable
    return scope


def workstation_base(checkout: Path) -> tuple[Path | None, str]:
    """The nearest ancestor holding ``WORKSPACE.json`` and its canonical checkout name.

    The checkout itself is not considered: a workspace marker inside the
    repository would make the checkout its own base and every root a
    self-reference.
    """
    checkout = Path(checkout).resolve()
    for ancestor in checkout.parents:
        marker = ancestor / WORKSPACE_MARKER
        if marker.is_file():
            canonical = DEFAULT_CANONICAL
            try:
                loaded = json.loads(marker.read_text(encoding="utf-8"))
                value = loaded.get("canonical_repository") if isinstance(loaded, dict) else None
                if isinstance(value, str) and value.strip():
                    canonical = _check_relative(value, "canonical_repository")
            except (OSError, ValueError):
                pass
            return ancestor, canonical
    return None, DEFAULT_CANONICAL


def load_scope(checkout: Path, *, environ: dict | None = None) -> Scope | None:
    """Load, validate and resolve the checkout's scope; ``None`` when undeclared.

    Base precedence: ``WORKHOUSE_DISCOVERY_BASE``, then the local override
    file, then the ``WORKSPACE.json`` ancestor. A malformed scope file raises
    rather than indexing a guessed subset.
    """
    checkout = Path(checkout).resolve()
    environ = os.environ if environ is None else environ
    scope_path = checkout / SCOPE_PATH
    if not scope_path.is_file():
        return None
    raw = scope_path.read_bytes()
    try:
        data = yaml.safe_load(raw.decode("utf-8"))
    except (UnicodeError, yaml.YAMLError) as exc:
        raise ValueError(f"discovery scope {SCOPE_PATH} is not valid YAML: {exc}") from exc
    scope = parse_scope(data, path=scope_path, sha256=_sha(raw))
    local_path = checkout / LOCAL_PATH
    if local_path.is_file():
        try:
            local_data = yaml.safe_load(local_path.read_text(encoding="utf-8"))
        except (UnicodeError, yaml.YAMLError) as exc:
            raise ValueError(
                f"local discovery scope {LOCAL_PATH} is not valid YAML: {exc}"
            ) from exc
        apply_local(scope, local_data, path=local_path)
    workspace, canonical = workstation_base(checkout)
    scope.canonical = canonical
    env_base = environ.get(BASE_ENV)
    if env_base:
        scope.base, scope.base_source = Path(env_base), "environment"
    elif scope.local_base:
        scope.base, scope.base_source = Path(scope.local_base), "local_override"
    elif workspace is not None:
        scope.base, scope.base_source = workspace, "workspace_marker"
    else:
        scope.base, scope.base_source = None, None
    if scope.base is not None:
        with contextlib.suppress(OSError):
            scope.base = scope.base.resolve()
    protected = [f"{canonical}/{name}" for name in PROTECTED_SUBTREES]
    scope.protected = tuple(dict.fromkeys(protected + list(scope.protected)))
    return scope


def protected_paths(scope: Scope) -> tuple[Path, ...]:
    if scope.base is None:
        return ()
    return tuple(scope.base / relative for relative in scope.protected)


def safe_external(path: Path, checkout: Path, protected) -> bool:
    """A real directory or file whose resolved location stays outside the checkout
    and outside every protected scientific subtree."""
    try:
        resolved = Path(path).resolve(strict=True)
    except (OSError, RuntimeError):
        return False
    checkout = Path(checkout)
    if resolved == checkout or resolved.is_relative_to(checkout):
        return False
    return all(
        not (resolved == Path(item) or resolved.is_relative_to(Path(item))) for item in protected
    )


def resolve_roots(scope: Scope, checkout: Path) -> list[dict]:
    """Presence and admissibility of every declared root, without walking it.

    ``skipped`` names why a root contributes nothing: ``disabled``,
    ``base_unavailable``, ``absent``, ``not_a_directory``, ``reparse_point``
    or ``unsafe_path``. Absence is a report, never an error.
    """
    checkout = Path(checkout).resolve()
    protected = protected_paths(scope)
    rows = []
    for root in scope.roots:
        row = {
            "label": root.label,
            "path": root.path,
            "tier": root.tier,
            "enabled": root.enabled,
            "max_depth": root.max_depth,
            "exclude": list(root.exclude),
            "note": root.note,
            "absolute": None,
            "present": False,
            "skipped": None,
        }
        directory = None
        if scope.base is not None:
            directory = scope.base if root.path == "." else scope.base / root.path
            row["absolute"] = str(directory)
            try:
                row["present"] = stat_module.S_ISDIR(os.lstat(directory).st_mode)
            except OSError:
                row["present"] = False
        if not root.enabled:
            row["skipped"] = "disabled"
        elif directory is None:
            row["skipped"] = "base_unavailable"
        elif not row["present"]:
            try:
                os.lstat(directory)
                row["skipped"] = "not_a_directory"
            except OSError:
                row["skipped"] = "absent"
        elif is_reparse_point(directory):
            row["skipped"] = "reparse_point"
        elif not safe_external(directory, checkout, protected):
            row["skipped"] = "unsafe_path"
        rows.append(row)
    return rows


def locator(label: str, relative: str) -> str:
    """``ext:<label>/<posix path>``: distinct from every checkout-relative locator."""
    return f"{LOCATOR_PREFIX}{label}/{relative}"


def split_locator(text: str) -> tuple[str, str] | None:
    """Inverse of :func:`locator`; ``None`` for a checkout-relative path."""
    if not text.startswith(LOCATOR_PREFIX):
        return None
    label, _slash, relative = text[len(LOCATOR_PREFIX) :].partition("/")
    return label, relative


def checkout_root() -> Path:
    return Path(__file__).resolve().parents[2]


def render_report(report: dict) -> str:
    scope = report.get("scope") or {}
    lines = [
        f"discovery scope {scope.get('path')} ({scope.get('schema')}, version "
        f"{scope.get('version')})",
        f"base {scope.get('base')} (from {scope.get('base_source') or 'nowhere: unavailable'})",
        f"local override: {scope.get('local_override') or 'none'}",
        "workstation paths; an absent root is skipped and reported, never an error",
        "",
        f"{'tier':>4}  {'label':28s} {'state':16s} path",
    ]
    for row in report.get("roots", []):
        state = row.get("skipped") or "indexed"
        if row.get("files") is not None and not row.get("skipped"):
            state = (
                f"{row['sources']} src {row['aliases']} alias {row.get('passages', '?')} passages"
            )
        lines.append(f"{row['tier']:>4}  {row['label']:28s} {state:16s} {row['path']}")
        if row.get("note"):
            lines.append(f"{'':34s} {row['note']}")
    lines.append("")
    lines.append(
        f"exclude_names {len(report.get('exclude_names', []))}  "
        f"base-relative excludes {len(report.get('exclude', []))}  "
        f"protected {', '.join(scope.get('protected') or [])}"
    )
    if report.get("error"):
        lines.append(f"error: {report['error']}")
    return "\n".join(lines)


def scope_report(checkout: Path, *, environ: dict | None = None) -> dict:
    checkout = Path(checkout).resolve()
    try:
        scope = load_scope(checkout, environ=environ)
    except ValueError as exc:
        return {
            "schema": REPORT_SCHEMA,
            "scope": {"path": SCOPE_PATH},
            "roots": [],
            "error": str(exc),
        }
    if scope is None:
        return {
            "schema": REPORT_SCHEMA,
            "scope": {"path": SCOPE_PATH, "declared": False},
            "roots": [],
            "exclude_names": [],
            "exclude": [],
        }
    return {
        "schema": REPORT_SCHEMA,
        "scope": {"declared": True, **scope.report(checkout)},
        "roots": resolve_roots(scope, checkout),
        "exclude_names": list(scope.exclude_names),
        "exclude": list(scope.exclude),
        "meaning": "Declared external reading scope; presence is a filesystem observation, "
        "not a statement about the standing of any document.",
    }


def add_parser(subparsers) -> None:
    """Register ``workhouse discover scope`` on the discover sub-parser group."""
    command = subparsers.add_parser(
        "scope",
        help="report the declared external workstation roots and whether each is present",
    )
    command.add_argument(
        "--build",
        action="store_true",
        help="also build or reuse the discovery cache and report per-root file counts",
    )
    command.add_argument("--json", action="store_true")
    command.add_argument("--out", help="retain JSON in a new file; refuse overwrite")


def run(args, engine_factory) -> int:
    """Print the scope report; with ``--build`` merge the engine's measured counts.

    ``engine_factory`` is called only when counts were requested, so a scope
    typo is diagnosable without building a cache.
    """
    report = scope_report(checkout_root())
    if getattr(args, "build", False) and not report.get("error"):
        try:
            with engine_factory() as engine:
                meta = engine.index.metadata(recheck=False)
        except (OSError, ValueError, KeyError) as exc:
            report["error"] = f"discovery build failed: {exc}"
        else:
            measured = {row["label"]: row for row in meta.get("external_roots", [])}
            for row in report["roots"]:
                row.update(
                    {
                        key: measured.get(row["label"], {}).get(key)
                        for key in ("files", "sources", "aliases", "bytes", "passages")
                    }
                )
            report["fingerprint"] = meta.get("fingerprint")
            report["alias_count"] = meta.get("alias_count")
            report["freshness_policy"] = meta.get("freshness_policy")
    if getattr(args, "out", None):
        target = Path(args.out)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(report, sort_keys=True, ensure_ascii=True) + "\n")
    print(json.dumps(report, sort_keys=True) if args.json else render_report(report))
    return 1 if report.get("error") else 0
