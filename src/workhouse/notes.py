"""The notes register: a structured intake path for the maintainer's archive.

The literature layer answers "what may a *published* paper contribute, and
under what discipline?" This module is its twin for the maintainer's own
research notes — years of working documents that are evidence about what was
tried, but T3 like everything else until a check says otherwise.

The path has three stations, and each leaves a record:

1. **Inventory** — ``workhouse notes --scan`` walks a mounted archive with
   :mod:`workhouse.triage` and writes ``notes/<archive-id>.jsonl``: one line
   per unique content digest, carrying every path that digest appears under
   and what the file's content signals. The manifest is checked in, so the
   review queue survives the archive being unmounted and "unreviewed" is
   computable in CI.
2. **Review** — a human (or an agent, reviewed) records a verdict per digest
   in ``ledger/notes.yaml``. Every verdict carries a mandatory ``reason``;
   a verdict without one is the same failure mode as a unifying candidate
   without a falsifier, and :func:`validate` rejects it.
3. **Incorporation** — an ``import`` verdict names where the bytes landed and
   the bytes are hashed against the digest, because "imported" is a claim and
   claims are checked. An ``extract`` verdict names the claims the note's
   content entered through, because content that arrives as checks needs no
   copy of the prose.

Nothing here deletes, moves, or edits archive files. ``set-aside`` is a
recorded judgement, not a trash can: the note stays in the archive, the
reason stays in the register, and both outlive the decision.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from . import triage as triage_mod

ROOT = Path(__file__).resolve().parents[2]
NOTES_DIR = ROOT / "notes"
REGISTER = ROOT / "ledger" / "notes.yaml"

#: The closed verdict vocabulary. ``import``: the bytes entered the repository
#: verbatim. ``extract``: the content entered as registered claims or checks,
#: no copy needed. ``duplicate``: same content as something already pinned or
#: reviewed. ``superseded``: an earlier draft of a later note. ``set-aside``:
#: reviewed and judged not load-bearing now — with the reason on record.
VERDICTS = frozenset({"import", "extract", "duplicate", "superseded", "set-aside"})

_HEX64 = frozenset("0123456789abcdef")


def _is_digest(value: str) -> bool:
    return len(value) == 64 and set(value) <= _HEX64


@dataclass
class Notes:
    archives: list[dict[str, Any]]
    reviews: list[dict[str, Any]]
    #: archive id -> manifest rows, one per unique digest.
    manifests: dict[str, list[dict[str, Any]]] = field(default_factory=dict)

    @property
    def archive_ids(self) -> set[str]:
        return {a["id"] for a in self.archives}

    def reviewed_digests(self, archive_id: str | None = None) -> set[str]:
        return {
            r["digest"]
            for r in self.reviews
            if archive_id is None or r.get("archive") == archive_id
        }

    def manifest_digests(self) -> set[str]:
        return {row["digest"] for rows in self.manifests.values() for row in rows}

    def unreviewed(self, archive_id: str) -> list[dict[str, Any]]:
        seen = self.reviewed_digests(archive_id)
        return [r for r in self.manifests.get(archive_id, []) if r["digest"] not in seen]


def _signal(row: dict[str, Any]) -> int:
    """Same ranking triage uses: coefficient-bearing files matter most."""
    return len(row.get("coefficients", [])) * 10 + (5 if row.get("has_erratum") else 0)


def load(register: Path | None = None, notes_dir: Path | None = None) -> Notes:
    register = register or REGISTER
    notes_dir = notes_dir or NOTES_DIR
    data = yaml.safe_load(register.read_text()) or {}
    notes = Notes(archives=data.get("archives", []), reviews=data.get("reviews", []))
    for archive in notes.archives:
        manifest = notes_dir / f"{archive['id']}.jsonl"
        if manifest.is_file():
            notes.manifests[archive["id"]] = [
                json.loads(line) for line in manifest.read_text().splitlines() if line.strip()
            ]
    return notes


def write_manifest(
    archive_root: Path, archive_id: str, notes: Notes, notes_dir: Path | None = None
) -> Path:
    """Inventory one archive into ``notes/<archive-id>.jsonl``.

    The archive must already be declared in the register: declaring the
    collection and inventorying it are separate deliberate events, and an
    inventory for an undeclared id would be a manifest nothing can review.
    """
    if archive_id not in notes.archive_ids:
        raise KeyError(f"archive {archive_id!r} is not declared in ledger/notes.yaml")
    report = triage_mod.scan(archive_root)

    by_digest: dict[str, dict[str, Any]] = {}
    for f in report.files:
        row = by_digest.setdefault(
            f.sha256,
            {
                "digest": f.sha256,
                "paths": [],
                "size": f.size,
                "scanned": f.scanned,
                "coefficients": f.coefficients,
                "has_erratum": f.has_erratum,
                "superseded_hint": f.superseded_hint,
                "date_hint": f.date_hint,
                "pinned_as": f.duplicate_of,
            },
        )
        row["paths"].append(str(f.path))

    rows = sorted(by_digest.values(), key=lambda r: r["paths"][0])
    for row in rows:
        row["paths"].sort()

    notes_dir = notes_dir or NOTES_DIR
    notes_dir.mkdir(parents=True, exist_ok=True)
    target = notes_dir / f"{archive_id}.jsonl"
    target.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
    return target


def _known_targets() -> set[str]:
    from . import literature as lit_mod

    return lit_mod._known_targets()


def validate(notes: Notes | None = None, root: Path | None = None) -> list[str]:
    """Structural problems in the register. Empty means it is sound."""
    notes = notes if notes is not None else load()
    root = root or ROOT
    problems: list[str] = []
    known: set[str] | None = None  # resolved lazily; most registers start empty

    seen_archives: set[str] = set()
    for archive in notes.archives:
        aid = archive["id"]
        if aid in seen_archives:
            problems.append(f"archive {aid}: duplicate id")
        seen_archives.add(aid)
        if not str(archive.get("description", "")).strip():
            problems.append(f"archive {aid}: no description — say what the collection is")
        if not str(archive.get("source", "")).strip():
            problems.append(f"archive {aid}: no source — say where the bytes live")

    manifest_digests = notes.manifest_digests()
    seen_reviews: set[tuple[str, str]] = set()
    for review in notes.reviews:
        digest = str(review.get("digest", ""))
        aid = str(review.get("archive", ""))
        label = f"review of {digest[:12] or '<no digest>'}"

        if not _is_digest(digest):
            problems.append(f"{label}: digest is not a SHA-256 digest")
        if aid not in notes.archive_ids:
            problems.append(f"{label}: unknown archive {aid!r}")
        elif aid not in notes.manifests:
            problems.append(
                f"{label}: archive {aid} has no manifest — inventory it first "
                f"(workhouse notes --scan)"
            )
        elif digest not in {r["digest"] for r in notes.manifests[aid]}:
            problems.append(f"{label}: digest is not in {aid}'s manifest")

        if (aid, digest) in seen_reviews:
            problems.append(f"{label}: reviewed twice — one digest, one verdict")
        seen_reviews.add((aid, digest))

        verdict = review.get("verdict")
        if verdict not in VERDICTS:
            problems.append(f"{label}: unknown verdict {verdict!r}")
        # A verdict with no reason is an assertion wearing a review's clothes.
        if not str(review.get("reason", "")).strip():
            problems.append(f"{label}: no reason — record why, or the review is decoration")

        if verdict == "import":
            dest = str(review.get("imported_to", ""))
            if not dest:
                problems.append(f"{label}: import names no imported_to path")
            elif not (root / dest).is_file():
                problems.append(f"{label}: imported_to {dest!r} does not exist")
            elif hashlib.sha256((root / dest).read_bytes()).hexdigest() != digest:
                problems.append(
                    f"{label}: imported_to {dest!r} does not hash to the digest — "
                    "an import is verbatim or it is an extract"
                )

        if verdict == "extract" and not review.get("bears_on"):
            problems.append(
                f"{label}: extract names no bears_on — say which claims the content entered"
            )

        if verdict == "duplicate":
            dup = str(review.get("duplicate_of", ""))
            if not dup:
                problems.append(f"{label}: duplicate names no duplicate_of")
            elif not _is_digest(dup) and not (root / dup).is_file():
                problems.append(
                    f"{label}: duplicate_of {dup!r} is neither a digest nor a repository file"
                )
            elif _is_digest(dup) and dup not in manifest_digests:
                problems.append(f"{label}: duplicate_of digest is in no manifest")

        if verdict == "superseded":
            sup = str(review.get("superseded_by", ""))
            if not _is_digest(sup):
                problems.append(f"{label}: superseded_by must be the successor's digest")
            elif sup not in manifest_digests:
                problems.append(f"{label}: superseded_by digest is in no manifest")

        for target in review.get("bears_on", []):
            if known is None:
                known = _known_targets()
            if target not in known:
                problems.append(f"{label}: bears on unknown target {target!r}")

    return problems


def queue(notes: Notes, limit: int = 20) -> list[tuple[str, dict[str, Any]]]:
    """The next files to review: unreviewed, highest signal first.

    Name-suggests-superseded rows sink below silent ones at equal signal —
    the hint is a prior, not a verdict.
    """
    pending: list[tuple[str, dict[str, Any]]] = []
    for aid in sorted(notes.manifests):
        pending.extend((aid, row) for row in notes.unreviewed(aid))
    pending.sort(
        key=lambda item: (
            -_signal(item[1]),
            item[1].get("superseded_hint", False),
            item[1]["paths"][0],
        )
    )
    return pending[:limit]


def format_status(notes: Notes) -> str:
    lines: list[str] = []
    add = lines.append
    add("Notes register — the maintainer's archive, under review")
    add("")
    if not notes.archives:
        add("no archives declared; declare one in ledger/notes.yaml")
    for archive in notes.archives:
        aid = archive["id"]
        add(f"{aid}: {archive.get('description', '').strip()}")
        rows = notes.manifests.get(aid)
        if rows is None:
            add("  declared, not yet inventoried — mount the archive and run")
            add(f"  workhouse notes --scan <root> --archive {aid}")
            add("")
            continue
        reviewed = notes.reviewed_digests(aid)
        counts: dict[str, int] = {}
        for review in notes.reviews:
            if review.get("archive") == aid:
                counts[review["verdict"]] = counts.get(review["verdict"], 0) + 1
        pending = notes.unreviewed(aid)
        bearing = sum(1 for r in pending if r.get("coefficients"))
        add(f"  {len(rows)} unique documents, {len(reviewed)} reviewed, {len(pending)} pending")
        for verdict in sorted(VERDICTS):
            if counts.get(verdict):
                add(f"    {counts[verdict]:>5}  {verdict}")
        if bearing:
            add(f"  {bearing} pending documents carry registered coefficients — review those first")
        add("")
    return "\n".join(lines).rstrip()


def format_queue(notes: Notes, limit: int = 20) -> str:
    items = queue(notes, limit)
    if not items:
        return "review queue is empty — every inventoried document has a verdict"
    lines = [f"Review queue — {len(items)} of the highest-signal unreviewed documents", ""]
    for aid, row in items:
        flags = ""
        if row.get("has_erratum"):
            flags += " [ERRATUM]"
        if row.get("superseded_hint"):
            flags += " [name suggests superseded]"
        if row.get("pinned_as"):
            flags += f" [== {row['pinned_as']}]"
        extra = len(row["paths"]) - 1
        copies = f"  (+{extra} copies)" if extra else ""
        lines.append(f"  {aid}: {row['paths'][0]}{copies}{flags}")
        if row.get("coefficients"):
            lines.append(f"      {', '.join(row['coefficients'])}")
    return "\n".join(lines)
