"""Review-to-registration workflow for discovery candidates.

A discovery hit is a reading candidate, not a relationship. This module keeps
the record of what an agent compared, what it concluded and what evidence it
read in a register under ``graph-tasks/discovery/`` - the one directory that
no catalogue collector, check cache, briefing fingerprint or discovery source
root reads - and turns an established review into a *proposal file*: the
verbatim ledger fragment a human pastes, with the checklist that must be
satisfied first. Nothing here writes under ``ledger/``, ``index/`` or any
other scientific tree, and nothing here imports a graph or claims writer.

Every review file carries a hash chain borrowed from append-only journals:
``previous`` names the creation hash of the review before it, ``genesis``
hashes the fields fixed at creation, and ``sha256`` hashes the whole record as
the tool last wrote it. ``review validate`` recomputes all three, so an edited
reasoning, a flipped state, a removed record or a backdated one is reported
instead of reading as reviewed work.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = "workhouse-discovery-review/v1"
PROPOSAL_SCHEMA = "workhouse-discovery-proposal/v1"
REPLAY_SCHEMA = "workhouse-discovery-review/replay/v1"
VALIDATION_SCHEMA = "workhouse-discovery-review/validation/v1"
ERROR_SCHEMA = "workhouse-discovery-review/error/v1"
REGISTER = "graph-tasks/discovery"
TIMESTAMP_ENV = "WORKHOUSE_REVIEW_TIMESTAMP"
REVIEWER_ENV = "WORKHOUSE_REVIEWER"

#: Closed relationship vocabulary. A free-text kind would let "related" stand
#: for a dependency; each name below maps to one registration surface or to
#: an explicit "nothing to register".
RELATIONSHIP_KINDS = frozenset(
    {
        "shared-operator",
        "compatible-hypothesis",
        "reusable-ingredient",
        "equivalent-construction",
        "scope-restriction",
        "disagreement",
        "literature-bearing",
        "documentary",
        "unrelated",
    }
)
#: Review lifecycle, on review records only - never on claims (ADR 0015 lineage).
STATES = frozenset({"pending", "reviewing", "established", "rejected", "registered"})
#: Allowed transitions. Skipping ``reviewing`` would let a discovery hit be
#: called established without anyone recording that the sources were read.
TRANSITIONS = {
    "pending": frozenset({"reviewing"}),
    "reviewing": frozenset({"established", "rejected"}),
    "established": frozenset({"registered"}),
    "rejected": frozenset(),
    "registered": frozenset(),
}
#: Registration surfaces a proposal may target, and the file each one edits.
SURFACES = {
    "results": "ledger/results.yaml",
    "gaps": "ledger/gaps.yaml",
    "derivation": "ledger/derivation_statements.yaml",
    "documents": "ledger/documents.yaml",
    "literature": "literature/index.yaml",
}
CONTRADICTIONS_REFUSAL = (
    "ledger/contradictions.yaml is a verbatim transcription of the corpus's own register: "
    "tests pin it to C1-C22 with zero open items, so a new contradiction record is a test "
    "failure by design. Record a disagreement as a literature relation 'contradicts' "
    "(--surface literature), as a route 'cannot_decide' on the relevant gap, or as a "
    "unifying candidate with status 'refuted' (--surface gaps)."
)
#: Trees the tool never writes into, whatever --out says. The failure this
#: prevents: a proposal file landing beside the ledgers and being read as one.
PROTECTED_TREES = (
    "ledger",
    "index",
    "theory",
    "corpus-import",
    "lean",
    "docs/derivations",
    "docs/decisions",
    "paper",
)
PROTECTED_FILES = ("FRONTIER.md", "CERTIFIED.md")
IMMUTABLE_FIELDS = (
    "schema",
    "id",
    "seed",
    "target",
    "relationship_kind",
    "reasoning",
    "reviewer",
    "created",
    "evidence",
    "previous",
)
ROW_FIELDS = (
    "rank",
    "group",
    "id",
    "kind",
    "candidate_kind",
    "score",
    "connection_rank",
    "channels",
    "retrieval_channels",
    "query_ranks",
    "claim_ids",
    "source",
    "excerpt",
    "excerpt_truncated",
    "matched_terms",
    "record",
    "statement",
    "path",
    "path_found",
    "shared_witness_count",
)
EXCERPT_CHARS = 700
FALLBACK_ROWS = 3
CHECKLIST = (
    (
        "hypotheses_compared",
        "The hypotheses of both arguments were compared, not their vocabulary.",
    ),
    ("regime_stated", "The regime (finite lattice, infinite volume, continuum, ...) is stated."),
    ("normalization_compared", "Normalizations and coordinates were compared explicitly."),
    (
        "independence_of_origin_checked",
        "Copied prose was distinguished from an independent origin (a shared source family is "
        "not independence).",
    ),
    ("falsifier_stated", "What would refute the relationship is written down."),
    (
        "source_hashes_matched",
        "Every recorded source hash matches the file bytes in this checkout.",
    ),
)
APPLY_STEPS = (
    "Paste the fragment by hand into the named ledger file; edit exactly one field per proposal "
    "and keep every other field.",
    "Run the read-only validators: uv run --no-sync workhouse status; "
    'uv run --no-sync python -c "from workhouse import results; results.load()"; '
    'uv run --no-sync python -c "from workhouse import derivation_statements as d; '
    'd._checked()"; uv run --no-sync workhouse lit (literature surface).',
    "Regenerate the views in the documented order (workhouse index -w, frontier --write, "
    "certified --write) in a reviewed pull request, never from this tool.",
    "After the PR merges, run: workhouse discover review mark <id> --state registered "
    "--registered-as '<PR or commit> <ledger id and field>' --reason '...'.",
)
_ID = re.compile(r"\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*-[0-9a-f]{6}\Z")
_LOCATOR = re.compile(
    r"(?P<path>(?:ext:[^/:\\]+/)?[^:\\]+\.[A-Za-z0-9]+):(?P<start>\d+)(?:-(?P<end>\d+))?\Z"
)
_ABSOLUTE = re.compile(r"^(?:[A-Za-z]:[/\\]|/)")
_LEDGER_ID = re.compile(
    r"\b(?:[CGRU]\d+|(?:RESULT|CHK|LEAN|RUN|CITE|CONST|DOC|CORPUS|ARCHIVE|NOTE|LIT|ADR|ROUTE|DERIV)"
    r":[^\s,;]+)"
)
_CHANGE_REF = re.compile(r"(?:#\d+|\bPR\s*\d+|/pull/\d+|\b[0-9a-f]{7,40}\b)", re.I)
_UNIFYING_ID = re.compile(r"^\s*-\s*id:\s*U(\d+)\s*$", re.M)


class ReviewError(ValueError):
    """A refused request; the message says which rule refused it."""


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _canonical(value) -> str:
    """One byte string per value, independent of YAML layout and key order."""
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"))


def _hash(value) -> str:
    return _sha(_canonical(value).encode("utf-8"))


def _slug(text: str, limit: int = 40) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:limit].strip("-") or "review"


def _timestamp(value: str | None) -> str:
    """An ISO-8601 UTC timestamp from the argument, the environment, or the clock.

    Ordering the register by creation needs comparable instants, so a naive
    value is read as UTC and every stored value carries its offset.
    """
    raw = value or os.environ.get(TIMESTAMP_ENV)
    if raw is None:
        moment = datetime.now(UTC)
    else:
        try:
            moment = datetime.fromisoformat(raw.strip())
        except ValueError as exc:
            raise ReviewError(f"timestamp must be ISO-8601, got {raw!r}") from exc
        if moment.tzinfo is None:
            moment = moment.replace(tzinfo=UTC)
    return moment.astimezone(UTC).isoformat(timespec="seconds")


def _instant(value: str) -> datetime:
    moment = datetime.fromisoformat(value)
    return moment if moment.tzinfo else moment.replace(tzinfo=UTC)


def parse_locator(value: str) -> tuple[str, int, int] | None:
    """``path:start-end`` for a passage; ``None`` when the string is a record id."""
    match = _LOCATOR.match(value.replace("\\", "/"))
    if not match:
        return None
    first = int(match["start"])
    last = int(match["end"] or first)
    return match["path"], first, last


class _Dumper(yaml.SafeDumper):
    """Multi-line strings as literal blocks, so fragments are paste-ready."""


def _represent_text(dumper, value):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_Dumper.add_representer(str, _represent_text)


def _dump(data: dict) -> str:
    return yaml.dump(
        data,
        Dumper=_Dumper,
        sort_keys=False,
        allow_unicode=True,
        width=100,
        default_flow_style=False,
    )


def _new_file(path: Path, text: str) -> None:
    """Create only; an existing path is an error, so a record is never clobbered."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def _replace_file(path: Path, text: str) -> None:
    handle, temporary = tempfile.mkstemp(prefix=path.stem + ".", suffix=".tmp", dir=path.parent)
    os.close(handle)
    Path(temporary).write_text(text, encoding="utf-8", newline="\n")
    Path(temporary).replace(path)


class Register:
    """The review and proposal directories of one checkout."""

    def __init__(self, root: Path | str | None = None, register: Path | str | None = None):
        self.root = Path(root or ROOT).resolve()
        self.dir = Path(register).resolve() if register else self.root / REGISTER
        self.reviews = self.dir / "reviews"
        self.proposals = self.dir / "proposals"
        self._external: dict[str, Path | None] | None = None

    def _external_roots(self) -> dict[str, Path | None]:
        """Present external roots by label, from the declared discovery scope."""
        if self._external is None:
            from . import discovery_scope

            roots: dict[str, Path | None] = {}
            try:
                scope = discovery_scope.load_scope(self.root)
            except ValueError:
                scope = None
            if scope is not None:
                for row in discovery_scope.resolve_roots(scope, self.root):
                    present = row.get("present") and not row.get("skipped")
                    roots[row["label"]] = Path(row["absolute"]) if present else None
            self._external = roots
        return self._external

    def locate(self, relative: str) -> tuple[Path | None, str | None]:
        """The file a locator path names, or the reason it cannot be read.

        Checkout-relative paths resolve under the checkout; ``ext:<label>/``
        paths resolve through the declared external root, so a reading of an
        intake passage can be recorded on the workstation that holds it and
        is reported as unavailable, not silently accepted, elsewhere.
        """
        relative = relative.replace("\\", "/")
        if _ABSOLUTE.match(relative):
            return None, "absolute paths are not accepted; use a checkout-relative or ext: path"
        if relative.startswith("ext:"):
            label, _slash, rest = relative[4:].partition("/")
            root = self._external_roots().get(label)
            if root is None:
                return None, f"external root {label!r} is not present on this workstation"
            return root / rest, None
        return self.root / relative, None

    # -- resolution against the saved catalogue and the checkout -----------------

    def catalogue_ids(self) -> set[str]:
        """Record ids the discovery engine can name: claims plus ``SYM:`` symbols."""
        ids: set[str] = set()
        for relative, prefix in (("index/claims.jsonl", ""), ("index/symbols.jsonl", "SYM:")):
            path = self.root / relative
            if not path.is_file():
                continue
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    with contextlib.suppress(ValueError, TypeError, KeyError):
                        ids.add(prefix + str(json.loads(line)["id"]))
        return ids

    def resolve_endpoint(self, value: str, ids: set[str] | None = None) -> list[str]:
        """Problems with a seed or target; empty when it names something real."""
        if not isinstance(value, str) or not value.strip():
            return ["endpoint must be a nonempty record id or path:start-end locator"]
        if _ABSOLUTE.match(value.strip()):
            # Checked before parsing: a POSIX absolute path has no colon and
            # would otherwise parse as a locator and resolve to itself.
            return [
                f"locator {value!r}: use a checkout-relative path or an "
                "ext:<label>/path:start-end locator, not an absolute path"
            ]
        locator = parse_locator(value)
        if locator is None:
            known = self.catalogue_ids() if ids is None else ids
            if value not in known:
                return [f"unknown record id {value!r}: not in index/claims.jsonl or symbols"]
            return []
        relative, first, last = locator
        path, reason = self.locate(relative)
        if path is None:
            return [f"locator {value!r}: {reason}"]
        if not path.is_file():
            return [f"locator {value!r}: no such file in the checkout or its external root"]
        try:
            count = len(path.read_bytes().decode("utf-8").splitlines())
        except UnicodeError:
            return [f"locator {value!r}: file is not UTF-8 text"]
        if not 1 <= first <= last <= count:
            return [f"locator {value!r}: lines must satisfy 1 <= start <= end <= {count}"]
        return []

    def file_sha256(self, relative: str) -> str | None:
        path, _reason = self.locate(relative)
        if path is None or not path.is_file():
            return None
        return _sha(path.read_bytes())

    # -- loading -------------------------------------------------------------------

    def load(self, review_id: str) -> dict:
        path = self.reviews / f"{review_id}.yaml"
        if not _ID.fullmatch(review_id) or not path.is_file():
            raise ReviewError(f"unknown review id {review_id!r}")
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ReviewError(f"review {review_id} is not a mapping")
        return data

    def records(self) -> list[tuple[Path, dict]]:
        """Every review in register order: by creation time, then id."""
        rows = []
        if not self.reviews.is_dir():
            return rows
        for path in sorted(self.reviews.glob("*.yaml")):
            try:
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
            except yaml.YAMLError as exc:
                raise ReviewError(f"{path.name}: invalid YAML: {exc}") from exc
            rows.append((path, data if isinstance(data, dict) else {"_invalid": True}))

        def order(item):
            data = item[1]
            created = data.get("created")
            try:
                moment = _instant(created) if isinstance(created, str) else None
            except ValueError:
                moment = None
            return (moment is None, moment or datetime.min.replace(tzinfo=UTC), str(data.get("id")))

        return sorted(rows, key=order)

    # -- evidence -------------------------------------------------------------------

    def _rows(self, result: dict) -> tuple[str, list[dict]]:
        """Compact rows from any discovery output; full responses are compacted."""
        from . import discovery_present as present

        schema = str(result.get("schema", ""))
        if schema == "workhouse-discovery/v1":
            terms = present.query_terms(result.get("queries") or result.get("query", ""))
            rows = [
                present.compact_hit(hit, terms, rank=rank, group="direct")
                for rank, hit in enumerate(result.get("hits", []), 1)
            ] + [
                present.compact_hit(hit, terms, rank=rank, group="related")
                for rank, hit in enumerate(result.get("related", []), 1)
            ]
            return "search", rows
        if schema == "workhouse-discovery/connections/v1":
            return "connections", present.present_connections(result)["candidates"]
        if schema.startswith("workhouse-discovery/connections"):
            return "connections", list(result.get("candidates", []))
        if schema.startswith(("workhouse-discovery/compact", "workhouse-discovery/context")):
            return "search", list(result.get("hits", [])) + list(result.get("related", []))
        if schema.startswith("workhouse-discovery/pair"):
            rows = []
            for side in ("a", "b"):
                endpoint = result.get(side)
                if not isinstance(endpoint, dict):
                    continue
                excerpt = endpoint.get("excerpt")
                rows.append(
                    {
                        "id": endpoint.get("id") or endpoint.get("id_or_locator"),
                        "kind": endpoint.get("kind"),
                        "source": endpoint.get("source"),
                        "claim_ids": list(endpoint.get("claim_ids") or []),
                        "excerpt": (excerpt.get("text") if isinstance(excerpt, dict) else excerpt),
                    }
                )
            return "pair", rows
        command = result.get("command") or (schema.split("/")[1] if "/" in schema else "unknown")
        rows = []
        for key in ("hits", "related", "candidates", "pairs", "rows"):
            rows.extend(row for row in result.get(key, []) or [] if isinstance(row, dict))
        return str(command), rows

    @staticmethod
    def _argv(command: str, result: dict) -> list[str]:
        """The command line that produced ``result``, reconstructed for replay."""
        explicit = result.get("argv")
        if isinstance(explicit, list) and explicit and all(isinstance(x, str) for x in explicit):
            argv = list(explicit)
        elif command == "connections":
            seed = result.get("seed") or {}
            seed_id = seed.get("id") if isinstance(seed, dict) else str(seed)
            argv = ["workhouse", "discover", "connections", str(seed_id)]
            query = result.get("query", "")
            if query and isinstance(seed, dict) and query != seed.get("statement", ""):
                argv += ["--query", str(query)]
            if result.get("candidates"):
                argv += ["--limit", str(len(result["candidates"]))]
        else:
            argv = ["workhouse", "discover", "search", str(result.get("query", ""))]
            for seed in result.get("seeds") or []:
                argv += ["--seed", str(seed)]
            queries = result.get("queries") or []
            for text in queries[1:] if queries and queries[0] == result.get("query") else queries:
                argv += ["--query", str(text)]
            if result.get("hits"):
                argv += ["--limit", str(len(result["hits"]))]
            budget = (result.get("budget") or {}).get("max_chars")
            if budget:
                argv += ["--context-chars", str(budget)]
        if "--json" not in argv:
            argv.append("--json")
        return argv

    @staticmethod
    def _compact(row: dict) -> dict:
        compact = {key: row[key] for key in ROW_FIELDS if key in row}
        excerpt = compact.get("excerpt")
        if isinstance(excerpt, str) and len(excerpt) > EXCERPT_CHARS:
            compact["excerpt"] = excerpt[:EXCERPT_CHARS]
            compact["excerpt_truncated"] = True
        if isinstance(compact.get("path"), list):
            compact["path"] = [str(step) for step in compact["path"][:6]]
        return json.loads(_canonical(compact))

    @staticmethod
    def _matches(row: dict, endpoints: list[str]) -> bool:
        names = {row.get("id"), *(row.get("claim_ids") or [])}
        source = row.get("source") if isinstance(row.get("source"), dict) else {}
        for endpoint in endpoints:
            if endpoint in names:
                return True
            locator = parse_locator(endpoint)
            if locator and source.get("path") == locator[0]:
                lines = source.get("lines") or source.get("passage_lines") or []
                if len(lines) == 2 and lines[0] <= locator[2] and lines[1] >= locator[1]:
                    return True
        return False

    def select_rows(self, rows: list[dict], endpoints: list[str]) -> tuple[list[dict], str]:
        relevant = [self._compact(row) for row in rows if self._matches(row, endpoints)]
        if relevant:
            return relevant, "rows naming the seed or target (by id, claim id or passage overlap)"
        fallback = [self._compact(row) for row in rows[:FALLBACK_ROWS]]
        return fallback, (
            f"top {len(fallback)} rows; no row named the seed or target - "
            "the evidence may not concern this pair"
        )

    def _source_hashes(self, rows: list[dict], endpoints: list[str]) -> list[dict]:
        wanted: dict[tuple[str, int, int], dict] = {}
        for endpoint in endpoints:
            locator = parse_locator(endpoint)
            if locator:
                wanted.setdefault(locator, {"role": "endpoint"})
        for row in rows:
            source = row.get("source") if isinstance(row.get("source"), dict) else {}
            lines = source.get("lines") or []
            if source.get("path") and len(lines) == 2:
                entry = wanted.setdefault(
                    (str(source["path"]), int(lines[0]), int(lines[1])), {"role": "row"}
                )
                if source.get("sha256"):
                    entry["indexed_sha256"] = source["sha256"]
        hashes = []
        for (path, first, last), entry in sorted(wanted.items()):
            current = self.file_sha256(path)
            item = {"path": path, "lines": [first, last], "sha256": current, "role": entry["role"]}
            indexed = entry.get("indexed_sha256")
            if indexed and indexed != current:
                item["indexed_sha256"] = indexed
                item["stale_at_recording"] = True
            hashes.append(item)
        return hashes

    def evidence(self, path: Path, endpoints: list[str], fingerprint: str | None) -> dict:
        """One evidence entry: what was run, which rows mattered, what they hashed to."""
        try:
            result = json.loads(Path(path).read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise ReviewError(f"evidence {path}: unreadable JSON ({exc})") from exc
        if not isinstance(result, dict):
            raise ReviewError(f"evidence {path}: expected a discovery JSON object")
        command, rows = self._rows(result)
        selected, selection = self.select_rows(rows, endpoints)
        provenance = result.get("provenance") if isinstance(result.get("provenance"), dict) else {}
        entry = {
            "command": command,
            "argv": self._argv(command, result),
            "fingerprint": fingerprint,
            "evidence_fingerprint": provenance.get("fingerprint"),
            "evidence_freshness": provenance.get("freshness"),
            "evidence_file": Path(path).name,
            "evidence_sha256": _sha(Path(path).read_bytes()),
            "schema": result.get("schema"),
            "selection": selection,
            "rows": selected,
            "source_hashes": self._source_hashes(selected, endpoints),
            "excerpt_sha256": _hash([row.get("excerpt", "") for row in selected]),
        }
        if fingerprint and provenance.get("fingerprint") not in (None, fingerprint):
            entry["fingerprint_note"] = (
                "evidence was produced against a different discovery cache than the one "
                "observed when this review was recorded"
            )
        return entry

    # -- add / mark ------------------------------------------------------------------

    def add(
        self,
        *,
        seed: str,
        target: str,
        kind: str,
        note: str,
        reviewer: str | None,
        evidence: list[str] | None = None,
        timestamp: str | None = None,
        slug: str | None = None,
        engine_factory=None,
    ) -> dict:
        if kind not in RELATIONSHIP_KINDS:
            raise ReviewError(
                f"unknown relationship kind {kind!r}; choose one of "
                + ", ".join(sorted(RELATIONSHIP_KINDS))
            )
        if not isinstance(note, str) or not note.strip():
            raise ReviewError("--note must state the reasoning; an empty review records nothing")
        reviewer = reviewer or os.environ.get(REVIEWER_ENV)
        if not reviewer or not reviewer.strip():
            raise ReviewError(
                f"--reviewer (or {REVIEWER_ENV}) must name the agent or model; "
                "an unattributed review cannot be questioned later"
            )
        if seed == target:
            raise ReviewError("seed and target must differ")
        ids = self.catalogue_ids()
        problems = self.resolve_endpoint(seed, ids) + self.resolve_endpoint(target, ids)
        if problems:
            raise ReviewError("; ".join(problems))
        created = _timestamp(timestamp)
        existing = self.records()
        if existing:
            last = existing[-1][1]
            last_created = last.get("created")
            if isinstance(last_created, str) and _instant(created) < _instant(last_created):
                raise ReviewError(
                    f"timestamp {created} precedes the last review ({last.get('id')} at "
                    f"{last_created}); the register is ordered by creation and cannot be "
                    "backdated"
                )
        fingerprint = None
        if evidence:
            if engine_factory is None:
                raise ReviewError("recording evidence needs the discovery engine fingerprint")
            engine = engine_factory()
            try:
                fingerprint = engine.index.metadata(check_current=False).get("fingerprint")
            finally:
                close = getattr(engine, "close", None)
                if callable(close):
                    close()
        endpoints = [seed, target]
        entries = [self.evidence(Path(path), endpoints, fingerprint) for path in evidence or []]
        core = {
            "seed": seed,
            "target": target,
            "relationship_kind": kind,
            "reasoning": note.strip(),
            "reviewer": reviewer.strip(),
            "created": created,
            "evidence": entries,
        }
        digest = _hash(core)[:6]
        label = _slug(slug) if slug else _slug(f"{kind}-{seed}")
        review_id = f"{created[:10]}-{label}-{digest}"
        if (self.reviews / f"{review_id}.yaml").exists():
            raise ReviewError(f"review {review_id} already exists with this exact content")
        previous = existing[-1][1].get("genesis") if existing else None
        record = {
            "schema": SCHEMA,
            "id": review_id,
            **core,
            "state": "pending",
            "updated": created,
            "registered_as": None,
            "history": [
                {
                    "state": "pending",
                    "at": created,
                    "reviewer": reviewer.strip(),
                    "reason": "recorded from discovery output; nothing reviewed yet",
                }
            ],
            "previous": previous,
        }
        record["genesis"] = _hash({key: record[key] for key in IMMUTABLE_FIELDS})
        record["sha256"] = _hash({k: v for k, v in record.items() if k != "sha256"})
        _new_file(self.reviews / f"{review_id}.yaml", _dump(record))
        return record

    def mark(
        self,
        review_id: str,
        *,
        state: str,
        reason: str,
        registered_as: str | None = None,
        reviewer: str | None = None,
        timestamp: str | None = None,
    ) -> dict:
        record = self.load(review_id)
        if state not in STATES:
            raise ReviewError(
                f"unknown state {state!r}; choose one of " + ", ".join(sorted(STATES))
            )
        if not isinstance(reason, str) or not reason.strip():
            raise ReviewError("--reason is mandatory: a state change without a reason is a guess")
        current = record.get("state")
        if state not in TRANSITIONS.get(current, frozenset()):
            allowed = ", ".join(sorted(TRANSITIONS.get(current, frozenset()))) or "none"
            raise ReviewError(
                f"cannot move {review_id} from {current!r} to {state!r}; allowed: {allowed}"
            )
        if state == "registered":
            problems = registration_problems(registered_as)
            if problems:
                raise ReviewError("; ".join(problems))
        at = _timestamp(timestamp)
        history = record.get("history") or []
        if history and _instant(at) < _instant(str(history[-1].get("at"))):
            raise ReviewError("timestamp precedes the last history entry; history is append-only")
        entry = {
            "state": state,
            "at": at,
            "reviewer": (reviewer or record.get("reviewer") or "").strip(),
            "reason": reason.strip(),
        }
        if state == "registered":
            entry["registered_as"] = registered_as.strip()
            record["registered_as"] = registered_as.strip()
        record["state"] = state
        record["updated"] = at
        record["history"] = [*history, entry]
        record["sha256"] = _hash({k: v for k, v in record.items() if k != "sha256"})
        _replace_file(self.reviews / f"{review_id}.yaml", _dump(record))
        return record

    # -- validate ---------------------------------------------------------------------

    def validate(self) -> dict:
        """Structural, vocabulary, chain and endpoint checks; read-only."""
        problems: list[str] = []
        records = self.records()
        ids = self.catalogue_ids()
        previous_genesis = None
        for path, data in records:
            label = path.name
            if data.get("_invalid"):
                problems.append(f"{label}: not a mapping")
                continue
            problems.extend(f"{label}: {issue}" for issue in _structure_problems(data))
            if data.get("id") and path.name != f"{data['id']}.yaml":
                problems.append(f"{label}: filename does not match id {data.get('id')!r}")
            for field in ("seed", "target"):
                value = data.get(field)
                if isinstance(value, str):
                    problems.extend(
                        f"{label}: {field} {issue}" for issue in self.resolve_endpoint(value, ids)
                    )
            try:
                genesis = _hash({key: data.get(key) for key in IMMUTABLE_FIELDS})
                content = _hash({k: v for k, v in data.items() if k != "sha256"})
            except (TypeError, ValueError):
                problems.append(f"{label}: record is not canonicalizable")
                previous_genesis = data.get("genesis")
                continue
            if data.get("genesis") != genesis:
                problems.append(f"{label}: creation fields were edited (genesis mismatch)")
            if data.get("sha256") != content:
                problems.append(f"{label}: content edited outside the tool (sha256 mismatch)")
            if data.get("previous") != previous_genesis:
                problems.append(
                    f"{label}: chain broken - previous {str(data.get('previous'))[:12]} does not "
                    f"name the preceding review ({str(previous_genesis)[:12]}); a record was "
                    "reordered, removed or inserted"
                )
            previous_genesis = data.get("genesis")
        return {
            "schema": VALIDATION_SCHEMA,
            "register": self.dir.as_posix(),
            "records": len(records),
            "problems": problems,
            "chain": "intact" if not any("chain broken" in p for p in problems) else "broken",
            "meaning": "Structural validation of review records; it decides nothing mathematical.",
        }

    # -- replay -------------------------------------------------------------------------

    def replay(self, review_id: str, *, engine_factory=None) -> dict:
        """Re-run recorded commands and compare fingerprints, hashes and excerpts."""
        record = self.load(review_id)
        endpoints = [str(record.get("seed")), str(record.get("target"))]
        entries = []
        for number, evidence in enumerate(record.get("evidence") or [], 1):
            argv = list(evidence.get("argv") or [])
            entry: dict = {"evidence": number, "argv": argv, "sources": []}
            if "--json" not in argv:
                argv.append("--json")
            output = None
            if not argv or argv[0] != "workhouse":
                entry["error"] = "recorded argv does not start with 'workhouse'; not replayed"
            else:
                try:
                    output = json.loads(_run_argv(argv, self.root))
                except (OSError, ValueError, subprocess.SubprocessError) as exc:
                    entry["error"] = f"replay failed: {exc}"
            if isinstance(output, dict) and "error" not in output:
                provenance = (
                    output.get("provenance") if isinstance(output.get("provenance"), dict) else {}
                )
                now = provenance.get("fingerprint")
                if now is None and engine_factory is not None:
                    engine = engine_factory()
                    try:
                        now = engine.index.metadata(check_current=False).get("fingerprint")
                    finally:
                        close = getattr(engine, "close", None)
                        if callable(close):
                            close()
                entry["fingerprint_recorded"] = evidence.get("fingerprint")
                entry["fingerprint_now"] = now
                entry["freshness_now"] = provenance.get("freshness")
                entry["fingerprint"] = (
                    "matched" if now == evidence.get("fingerprint") else "changed"
                )
                _command, rows = self._rows(output)
                selected, _selection = self.select_rows(rows, endpoints)
                excerpt_now = _hash([row.get("excerpt", "") for row in selected])
                entry["excerpt_sha256"] = (
                    "matched" if excerpt_now == evidence.get("excerpt_sha256") else "changed"
                )
                entry["rows_now"] = len(selected)
            elif isinstance(output, dict):
                entry["error"] = str(output.get("error"))
            for item in evidence.get("source_hashes") or []:
                current = self.file_sha256(str(item.get("path")))
                if current is None:
                    verdict = "missing"
                else:
                    verdict = "matched" if current == item.get("sha256") else "changed"
                entry["sources"].append(
                    {"path": item.get("path"), "lines": item.get("lines"), "sha256": verdict}
                )
            verdicts = [entry.get("fingerprint"), entry.get("excerpt_sha256")]
            verdicts += [source["sha256"] for source in entry["sources"]]
            if entry.get("error"):
                entry["verdict"] = "error"
            elif any(verdict in ("changed", "missing") for verdict in verdicts):
                entry["verdict"] = "changed"
            else:
                entry["verdict"] = "matched"
            entries.append(entry)
        outcomes = {entry["verdict"] for entry in entries}
        if not entries:
            overall = "no-evidence"
        elif "error" in outcomes:
            overall = "error"
        elif "changed" in outcomes:
            overall = "changed"
        else:
            overall = "matched"
        return {
            "schema": REPLAY_SCHEMA,
            "review": review_id,
            "state": record.get("state"),
            "entries": entries,
            "verdict": overall,
            "meaning": "Replay compares retrieval inputs and excerpts with the recorded ones; "
            "a match means the evidence still reads the same, not that the review is right.",
        }

    # -- propose --------------------------------------------------------------------------

    def next_unifying_id(self) -> str:
        path = self.root / "ledger" / "gaps.yaml"
        if not path.is_file():
            return "U<next free integer in ledger/gaps.yaml>"
        numbers = [int(n) for n in _UNIFYING_ID.findall(path.read_text(encoding="utf-8"))]
        return f"U{max(numbers) + 1}" if numbers else "U1"

    def propose(self, review_id: str, surface: str, out: str | None = None) -> tuple[Path, dict]:
        if surface == "contradictions":
            raise ReviewError("refused --surface contradictions: " + CONTRADICTIONS_REFUSAL)
        if surface not in SURFACES:
            raise ReviewError(f"unknown surface {surface!r}; choose one of " + ", ".join(SURFACES))
        record = self.load(review_id)
        if record.get("state") != "established":
            raise ReviewError(
                f"review {review_id} is {record.get('state')!r}; a proposal needs state "
                "'established' (pending -> reviewing -> established, each with a reason)"
            )
        kind = record.get("relationship_kind")
        if kind == "unrelated":
            raise ReviewError(
                "an 'unrelated' review has nothing to register; it stays in the register as a "
                "recorded negative"
            )
        destination = self._proposal_path(review_id, surface, out)
        proposal = build_proposal(self, record, surface)
        _new_file(destination, _dump(proposal))
        return destination, proposal

    def _proposal_path(self, review_id: str, surface: str, out: str | None) -> Path:
        if out is None:
            return self.proposals / f"{review_id}-{surface}.yaml"
        path = Path(out)
        resolved = (self.root / path).resolve() if not path.is_absolute() else path.resolve()
        if resolved.is_relative_to(self.root):
            relative = resolved.relative_to(self.root).as_posix()
            if relative in PROTECTED_FILES or any(
                relative == tree or relative.startswith(tree + "/") for tree in PROTECTED_TREES
            ):
                raise ReviewError(
                    f"refused --out {out}: proposals never land under a scientific tree "
                    f"({', '.join(PROTECTED_TREES)}); they are pasted by hand in a reviewed PR"
                )
        return resolved


def registration_problems(registered_as: str | None) -> list[str]:
    """``registered_as`` must name the change and the ledger id a human landed."""
    if not isinstance(registered_as, str) or not registered_as.strip():
        return ["--registered-as is required: name the PR or commit and the ledger id"]
    problems = []
    if not _CHANGE_REF.search(registered_as):
        problems.append("registered_as must name a PR (#123, PR 123, .../pull/123) or a commit sha")
    if not _LEDGER_ID.search(registered_as):
        problems.append(
            "registered_as must name the ledger id the relationship landed on "
            "(RESULT:..., DERIV:..., CITE:..., LIT:..., U8, G19, ...)"
        )
    return problems


def _structure_problems(data: dict) -> list[str]:
    problems = []
    if data.get("schema") != SCHEMA:
        problems.append(f"schema must be {SCHEMA}")
    review_id = data.get("id")
    if not isinstance(review_id, str) or not _ID.fullmatch(review_id):
        problems.append("id must be <date>-<slug>-<6 hex>")
    for field in ("seed", "target", "reasoning", "reviewer"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            problems.append(f"{field} must be a nonempty string")
    if data.get("relationship_kind") not in RELATIONSHIP_KINDS:
        problems.append(f"unknown relationship_kind {data.get('relationship_kind')!r}")
    state = data.get("state")
    if state not in STATES:
        problems.append(f"unknown state {state!r}")
    for field in ("created", "updated"):
        value = data.get(field)
        if not isinstance(value, str):
            problems.append(f"{field} must be an ISO-8601 string (quote it in YAML)")
        else:
            try:
                _instant(value)
            except ValueError:
                problems.append(f"{field} is not ISO-8601: {value!r}")
    evidence = data.get("evidence")
    if not isinstance(evidence, list):
        problems.append("evidence must be a list")
    else:
        for number, entry in enumerate(evidence, 1):
            if not isinstance(entry, dict):
                problems.append(f"evidence[{number}] must be a mapping")
                continue
            for field in ("command", "argv", "source_hashes", "excerpt_sha256"):
                if field not in entry:
                    problems.append(f"evidence[{number}] lacks {field}")
            if not isinstance(entry.get("argv"), list):
                problems.append(f"evidence[{number}].argv must be a list")
    history = data.get("history")
    if not isinstance(history, list) or not history:
        problems.append("history must be a nonempty list")
    else:
        current = None
        last_at = None
        for number, entry in enumerate(history, 1):
            if not isinstance(entry, dict):
                problems.append(f"history[{number}] must be a mapping")
                continue
            new = entry.get("state")
            if number == 1 and new != "pending":
                problems.append("history must start at pending")
            elif number > 1 and new not in TRANSITIONS.get(current, frozenset()):
                problems.append(f"history[{number}]: illegal transition {current!r} -> {new!r}")
            if not isinstance(entry.get("reason"), str) or not entry["reason"].strip():
                problems.append(f"history[{number}] lacks a reason")
            at = entry.get("at")
            try:
                moment = _instant(at) if isinstance(at, str) else None
            except ValueError:
                moment = None
            if moment is None:
                problems.append(f"history[{number}].at is not ISO-8601")
            elif last_at is not None and moment < last_at:
                problems.append(f"history[{number}] is out of order")
            last_at = moment or last_at
            if new == "registered":
                problems.extend(
                    f"history[{number}]: {p}"
                    for p in registration_problems(entry.get("registered_as"))
                )
            current = new
        if current != state and state in STATES:
            problems.append(f"state {state!r} disagrees with the last history entry {current!r}")
    if state == "registered":
        problems.extend(registration_problems(data.get("registered_as")))
    elif data.get("registered_as") not in (None, ""):
        problems.append("registered_as is set but the state is not registered")
    if data.get("previous") is not None and not isinstance(data.get("previous"), str):
        problems.append("previous must be a sha256 string or null")
    for field in ("genesis", "sha256"):
        if not isinstance(data.get(field), str) or len(data[field]) != 64:
            problems.append(f"{field} must be a sha256 hex digest")
    return problems


# -- proposal fragments ------------------------------------------------------------------


def _endpoint_with_prefix(record: dict, prefixes: tuple[str, ...]) -> tuple[str | None, str]:
    """(host, other): the endpoint whose id carries one of ``prefixes``, and the other."""
    seed, target = str(record.get("seed")), str(record.get("target"))
    if seed.startswith(prefixes):
        return seed, target
    if target.startswith(prefixes):
        return target, seed
    return None, target


def _catalogue_value(value: str) -> str:
    if parse_locator(value):
        path = parse_locator(value)[0]
        return (
            f"<FILL: catalogue id carrying passage {value}; a passage locator is not a catalogue "
            f"id - try: uv run --no-sync workhouse why {path}>"
        )
    return value


def _fill_host(prefix: str, meaning: str) -> str:
    return f"{prefix}<FILL: {meaning}; neither seed nor target carries this prefix>"


def _results_fragment(record: dict) -> tuple[str, list[str]]:
    kind = record["relationship_kind"]
    host, other = _endpoint_with_prefix(record, ("RESULT:",))
    notes = []
    host = host or _fill_host("RESULT:", "the result whose argument this review bears on")
    value = _catalogue_value(other)
    if kind == "reusable-ingredient" and other.startswith(("CHK:", "LEAN:", "RUN:")):
        field = "supported_by"
    elif kind == "reusable-ingredient":
        field = "depends_on"
    else:
        field = "bears_on"
    if kind == "disagreement":
        notes.append(
            "results.yaml has no disagreement field; prefer --surface literature (contradicts) "
            "or a refuted unifying candidate."
        )
    if kind == "shared-operator":
        notes.append("Shared vocabulary is not a dependency (ADR 0007); bears_on is the ceiling.")
    lines = [
        f"# ledger/results.yaml -> results[] entry `- id: {host}`; append to the existing",
        "# list and keep every other field (source, source_section, status, evidence unchanged).",
        f"# Relationship kind `{kind}` -> field `{field}`: "
        + {
            "depends_on": "a mathematical input actually used in the argument.",
            "bears_on": "relevance or consequence only, never a derivation.",
            "supported_by": "a control that establishes one named substatement.",
        }[field],
    ]
    if field == "supported_by":
        lines += [
            "    supported_by:",
            f"      - target: {value}",
            "        scope: <FILL: exactly which finite, scalar or formal substatement this "
            "control establishes; it never promotes the full statement>",
        ]
    else:
        lines += [f"    {field}:", f"      - {value}"]
    return "\n".join(lines) + "\n", notes


def _gaps_fragment(record: dict, register: Register) -> tuple[str, list[str]]:
    kind = record["relationship_kind"]
    seed, target = str(record["seed"]), str(record["target"])
    supported = [_catalogue_value(seed), _catalogue_value(target)]
    status = "refuted" if kind == "disagreement" else "conjectured"
    date = str(record.get("created", ""))[:10].replace("-", "_")
    first_line = str(record.get("reasoning", "")).strip().splitlines()[0][:160]
    lines = [
        "# ledger/gaps.yaml -> top-level `unifying_candidates:`; append one entry.",
        "# Only [CGRU]<n> ids and 'ADR NNNN' in supported_by become graph edges; other",
        "# strings stay display-only. ledger.validate rejects an empty falsifier.",
        f"  - id: {register.next_unifying_id()}",
        "    statement: |",
        f"      <FILL: the identification claimed between {seed} and {target}, as a statement "
        "that can be false>",
        "    supported_by:",
        *[f"      - {value}" for value in supported],
        "    falsifier: |",
        "      <FILL BEFORE APPLYING: what would have to be exhibited for the identification to "
        "fail. A candidate without a falsifier is an analogy, and analogies accumulate without "
        "ever being wrong.>",
        f"    status: {status}",
    ]
    if kind == "disagreement":
        lines += [
            f"    refuted_{date}: |",
            "      <FILL: which side of the disagreement refutes the identification and where>",
        ]
    lines += [
        "    note: |",
        f"      Discovery review {record['id']} ({kind}): {first_line}",
    ]
    return "\n".join(lines) + "\n", []


def _derivation_fragment(record: dict) -> tuple[str, list[str]]:
    kind = record["relationship_kind"]
    host, other = _endpoint_with_prefix(record, ("DERIV:",))
    host = host or _fill_host("DERIV:", "the statement whose argument uses the input")
    notes = []
    lines = [
        "# ledger/derivation_statements.yaml -> documents[].statements[] entry",
        f"# `id: {host}`; append to the existing list. Duplicates, unresolved parents and",
        "# cycles are rejected; sha256, locator and anchor of the document stay untouched.",
    ]
    if other.startswith("LEAN:"):
        lines += [
            "    lean_support:",
            f"    - name: {other.removeprefix('LEAN:')}",
            "      scope: <FILL: the stated ingredient only; lean_support never promotes the "
            "whole statement>",
        ]
    else:
        value = _catalogue_value(other)
        if not value.startswith(("DERIV:", "<FILL")):
            notes.append(
                "derivation_statements depends_on accepts DERIV: ids only; if the other end is "
                "not a derivation statement, use --surface results or documents instead."
            )
        lines += [
            "    depends_on:",
            f"    - {value}   # actual prerequisite in the source argument, kind `{kind}`",
        ]
    return "\n".join(lines) + "\n", notes


def _documents_fragment(record: dict) -> tuple[str, list[str]]:
    kind = record["relationship_kind"]
    host, other = _endpoint_with_prefix(record, ("CITE:",))
    alias = host.removeprefix("CITE:") if host else "<FILL: alias of the citing document>"
    lines = [
        f"# ledger/documents.yaml -> aliases[] entry `alias: {alias}`; append to the existing",
        "# list. Targets must resolve (an alias for cites, a catalogue id for bears_on).",
    ]
    if other.startswith("CITE:"):
        lines += ["    cites:", f"      - {other.removeprefix('CITE:')}"]
    else:
        lines += ["    bears_on:", f"      - {_catalogue_value(other)}   # kind `{kind}`"]
    return "\n".join(lines) + "\n", []


_LITERATURE_RELATION = {
    "disagreement": "contradicts",
    "reusable-ingredient": "supplies-method",
    "compatible-hypothesis": "corroborates",
    "literature-bearing": "corroborates",
    "equivalent-construction": "supplies-comparison",
}


def _literature_fragment(record: dict) -> tuple[str, list[str]]:
    kind = record["relationship_kind"]
    host, other = _endpoint_with_prefix(record, ("LIT:",))
    paper = host.split(":")[1] if host and host.count(":") >= 1 else "<FILL: paper id>"
    relation = _LITERATURE_RELATION.get(kind)
    vocabulary = (
        "supplies-value | supplies-method | corroborates | contradicts | supplies-comparison "
        "| confusable"
    )
    if kind == "disagreement":
        relation_line = f"        relation: {relation}"
    elif relation:
        relation_line = f"        relation: {relation}   # suggested; choose one of {vocabulary}"
    else:
        relation_line = f"        relation: <CHOOSE: {vocabulary}>"
    lines = [
        f"# literature/index.yaml -> papers[] entry `id: {paper}`; append to bears_on.",
        "# A paper is T3 until something checks it; the relation records what it bears on.",
        "    bears_on:",
        f"      - target: {_catalogue_value(other)}",
        relation_line,
        "        status: transcription-unverified   # verified | transcription-unverified | "
        "not-yet-obtained | refuted",
        "        detail: |",
        "          <FILL: what the paper establishes for this target and what it does not>",
    ]
    return "\n".join(lines) + "\n", []


def build_proposal(register: Register, record: dict, surface: str) -> dict:
    """The proposal document: fragment, checklist, evidence and the hand-apply statement."""
    builders = {
        "results": lambda: _results_fragment(record),
        "gaps": lambda: _gaps_fragment(record, register),
        "derivation": lambda: _derivation_fragment(record),
        "documents": lambda: _documents_fragment(record),
        "literature": lambda: _literature_fragment(record),
    }
    fragment, notes = builders[surface]()
    hash_check = []
    all_matched = True
    for evidence in record.get("evidence") or []:
        for item in evidence.get("source_hashes") or []:
            current = register.file_sha256(str(item.get("path")))
            matched = current is not None and current == item.get("sha256")
            all_matched = all_matched and matched
            hash_check.append(
                {"path": item.get("path"), "lines": item.get("lines"), "matched": matched}
            )
    checklist = []
    for key, text in CHECKLIST:
        item = {"item": key, "requirement": text, "done": False}
        if key == "source_hashes_matched":
            item["done"] = bool(hash_check) and all_matched
            item["observation"] = (
                "no source hashes recorded"
                if not hash_check
                else "all recorded source hashes match this checkout"
                if all_matched
                else "a recorded source changed; replay the review before applying"
            )
        checklist.append(item)
    return {
        "schema": PROPOSAL_SCHEMA,
        "review": record["id"],
        "surface": surface,
        "ledger_file": SURFACES[surface],
        "meaning": (
            "PROPOSAL, not a registration. This file was generated from a review record; "
            "nothing in the scientific ledgers or the generated index changed. Applying it is a "
            "hand edit of the named ledger file, followed by the validators and a reviewed PR. "
            "A discovery score is not evidence and this review is not a proof."
        ),
        "relationship": {
            "seed": record.get("seed"),
            "target": record.get("target"),
            "kind": record.get("relationship_kind"),
            "reviewer": record.get("reviewer"),
            "reasoning": record.get("reasoning"),
            "history": record.get("history"),
        },
        "fragment": fragment,
        "notes": notes,
        "checklist": checklist,
        "apply": list(APPLY_STEPS),
        "refused": {
            "contradictions": CONTRADICTIONS_REFUSAL,
            "writes": "This tool never writes under ledger/, index/ or any other scientific tree.",
        },
        "evidence": record.get("evidence") or [],
        "source_hash_check": hash_check,
    }


# -- subprocess replay ---------------------------------------------------------------------


def _run_argv(argv: list[str], root: Path) -> str:
    """Run a recorded ``workhouse ...`` line from the checkout; return its stdout."""
    uv = shutil.which("uv")
    command = (
        [uv, "run", "--no-sync", *argv]
        if uv
        else [sys.executable, "-m", "workhouse.cli", *argv[1:]]
    )
    completed = subprocess.run(
        command, cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if completed.returncode != 0 and not completed.stdout.strip():
        raise subprocess.SubprocessError(
            f"exit {completed.returncode}: {completed.stderr.strip()[-400:]}"
        )
    return completed.stdout


# -- CLI --------------------------------------------------------------------------------------


def add_parser(ds_sub) -> None:
    """Register ``review`` (with its sub-subcommands) and ``propose`` under ``discover``."""
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", help="checkout root (default: this package's repository)")
    common.add_argument(
        "--register", help=f"register directory (default: <root>/{REGISTER}); never a ledger tree"
    )
    common.add_argument("--json", action="store_true", help="machine-readable output")

    review = ds_sub.add_parser(
        "review", help="record, advance, replay and validate discovery reviews; writes no ledger"
    )
    rv = review.add_subparsers(dest="review_command", required=True)
    add = rv.add_parser("add", parents=[common], help="record a review in state pending")
    add.add_argument("--seed", required=True, help="record id or path:start-end passage locator")
    add.add_argument("--target", required=True, help="record id or path:start-end locator")
    add.add_argument("--kind", required=True, choices=sorted(RELATIONSHIP_KINDS))
    add.add_argument("--note", required=True, help="the reasoning, in words")
    add.add_argument("--reviewer", help=f"agent or model string (or {REVIEWER_ENV})")
    add.add_argument(
        "--evidence",
        action="append",
        default=[],
        metavar="PATH",
        help="discovery JSON output (search, connections, pair); relevant rows are copied",
    )
    add.add_argument("--timestamp", help=f"ISO-8601 creation time (or {TIMESTAMP_ENV})")
    add.add_argument("--slug", help="short label for the id (default: kind and seed)")
    listing = rv.add_parser("list", parents=[common], help="reviews in register order")
    listing.add_argument("--state", choices=sorted(STATES))
    show = rv.add_parser("show", parents=[common], help="one review record")
    show.add_argument("id")
    mark = rv.add_parser("mark", parents=[common], help="advance a review's state")
    mark.add_argument("id")
    mark.add_argument("--state", required=True, choices=sorted(STATES))
    mark.add_argument("--reason", required=True)
    mark.add_argument("--registered-as", help="PR/commit and ledger id, supplied by a human")
    mark.add_argument("--reviewer")
    mark.add_argument("--timestamp")
    replay = rv.add_parser("replay", parents=[common], help="re-run recorded evidence commands")
    replay.add_argument("id")
    rv.add_parser("validate", parents=[common], help="schema, vocabularies, chain, endpoints")

    propose = ds_sub.add_parser(
        "propose", parents=[common], help="emit the ledger fragment a human would paste"
    )
    propose.add_argument("id")
    propose.add_argument(
        "--surface", required=True, help="results | gaps | derivation | documents | literature"
    )
    propose.add_argument("--out", help="proposal path (never under ledger/ or index/)")


def _render_list(rows: list[dict]) -> str:
    if not rows:
        return "no reviews recorded"
    lines = []
    for row in rows:
        lines.append(
            f"{row['id']}  {row['state']:<11} {row['relationship_kind']:<23} "
            f"{row['seed']} -> {row['target']}"
        )
    return "\n".join(lines)


def _render_replay(result: dict) -> str:
    lines = [f"replay {result['review']} ({result['state']}): {result['verdict']}"]
    for entry in result["entries"]:
        lines.append(f"  evidence {entry['evidence']}: {' '.join(entry['argv'])}")
        if entry.get("error"):
            lines.append(f"    error: {entry['error']}")
        else:
            fingerprint, excerpts = entry.get("fingerprint"), entry.get("excerpt_sha256")
            lines.append(f"    fingerprint {fingerprint}  excerpts {excerpts}")
        for source in entry["sources"]:
            first, last = (source.get("lines") or ["?", "?"])[:2]
            lines.append(f"    {source['path']}:{first}-{last}  {source['sha256']}")
    lines.append(result["meaning"])
    return "\n".join(lines)


def run(args, engine_factory) -> int:
    """Dispatch ``discover review ...`` and ``discover propose``; 0 ok, 1 refused, 2 changed."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            with contextlib.suppress(ValueError, OSError):
                stream.reconfigure(encoding="utf-8", errors="replace")
    as_json = bool(getattr(args, "json", False))
    register = Register(getattr(args, "root", None), getattr(args, "register", None))
    try:
        if args.discovery_command == "propose":
            path, proposal = register.propose(args.id, args.surface, getattr(args, "out", None))
            if as_json:
                print(json.dumps({**proposal, "path": path.as_posix()}, sort_keys=True))
            else:
                print(f"proposal written: {path.as_posix()}\n\n{proposal['fragment']}")
                print(proposal["meaning"])
            return 0
        command = args.review_command
        if command == "add":
            record = register.add(
                seed=args.seed,
                target=args.target,
                kind=args.kind,
                note=args.note,
                reviewer=getattr(args, "reviewer", None),
                evidence=list(getattr(args, "evidence", None) or []),
                timestamp=getattr(args, "timestamp", None),
                slug=getattr(args, "slug", None),
                engine_factory=engine_factory,
            )
            print(json.dumps(record, sort_keys=True) if as_json else f"recorded {record['id']}")
            return 0
        if command == "list":
            wanted = getattr(args, "state", None)
            rows = [
                {
                    key: data.get(key)
                    for key in ("id", "state", "relationship_kind", "seed", "target", "updated")
                }
                for _path, data in register.records()
                if not wanted or data.get("state") == wanted
            ]
            print(json.dumps(rows, sort_keys=True) if as_json else _render_list(rows))
            return 0
        if command == "show":
            record = register.load(args.id)
            print(json.dumps(record, sort_keys=True) if as_json else _dump(record).rstrip())
            return 0
        if command == "mark":
            record = register.mark(
                args.id,
                state=args.state,
                reason=args.reason,
                registered_as=getattr(args, "registered_as", None),
                reviewer=getattr(args, "reviewer", None),
                timestamp=getattr(args, "timestamp", None),
            )
            print(
                json.dumps(record, sort_keys=True)
                if as_json
                else f"{record['id']} -> {record['state']}"
            )
            return 0
        if command == "replay":
            result = register.replay(args.id, engine_factory=engine_factory)
            print(json.dumps(result, sort_keys=True) if as_json else _render_replay(result))
            return {"matched": 0, "no-evidence": 0, "changed": 2}.get(result["verdict"], 1)
        if command == "validate":
            result = register.validate()
            if as_json:
                print(json.dumps(result, sort_keys=True))
            else:
                print(f"{result['records']} review(s); chain {result['chain']}")
                print("\n".join(result["problems"]) or "register valid")
            return 0 if not result["problems"] else 1
        raise ReviewError(f"unknown review command {command!r}")
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        error = {"schema": ERROR_SCHEMA, "error": str(exc)}
        print(json.dumps(error) if as_json else f"Review refused: {exc}")
        return 1
