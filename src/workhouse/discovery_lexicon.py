"""Versioned, source-cited concept lexicon and agent query plans for discovery.

The discovery engine retrieves a cross-family source only when the query uses
that family's vocabulary: September derivations say ``conditional score`` and
``outside quantum pressure`` where imported notes say ``Brascamp-Lieb`` and
``effective potential``. This module maps a concept to its terminology
variants across source families, each variant cited to the line where that
family actually uses it, and turns a research question into sub-queries in the
other families' words. It runs without any model.

Rules the validator enforces, and the failure each prevents:

* every variant carries a ``path:lines`` citation whose file exists in the
  checkout and whose cited lines contain the variant's words -- a variant
  without an observed source is an invented synonym, and a search that
  expands through invented synonyms reads its own guesses as corpus evidence;
* the cited path must lie under the declared family's roots -- a note cited
  as a derivation would let one family's phrasing masquerade as another's;
* an entry must bridge at least two families -- a single-family entry can
  never surface a cross-family source, which is the only reason it exists;
* entries carry terminology only: ``status``, ``evidence`` and ``tier`` keys
  are rejected, so the lexicon cannot become a fourth place where scientific
  standing is asserted.

Expansions are retrieval aids. They add no evidence, change no score
semantics, and never write to the scientific graph.
"""

from __future__ import annotations

import contextlib
import datetime as _dt
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

from .discovery_index import tokenize

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = "workhouse-discovery-lexicon/v1"
PLAN_SCHEMA = "workhouse-discovery-plan/v1"
DEFAULT_PATH = "graph-tasks/discovery/lexicon.yaml"
FAMILIES = ("derivations", "historical", "notes", "literature", "corpus-import", "paper")
FAMILY_ROOTS = {
    "derivations": ("docs/derivations/", "docs/research/", "research/"),
    "historical": ("theory/",),
    "notes": ("notes/imported/",),
    "literature": ("literature/",),
    "corpus-import": ("corpus-import/",),
    "paper": ("paper/",),
}
# Scientific standing lives in ledger records under these names. A lexicon
# entry that carried them would be a fourth, unreviewed place to assert it.
RESERVED_KEYS = frozenset({"status", "evidence", "tier", "verified", "proven", "certified"})
TOP_KEYS = frozenset({"schema", "version", "updated_on", "description", "families", "entries"})
ENTRY_KEYS = frozenset({"concept", "meaning", "variants", "related", "added_by", "added_on"})
VARIANT_KEYS = frozenset({"text", "family", "source", "note"})
MAX_SUB_QUERIES = 31  # the engine fuses at most 32 texts including the question
# Measured 2026-09-11 on six derivation-vocabulary questions: at 1.0 focused
# reformulations reached notes/corpus/literature rows in five questions but
# kept only 1.5 of the question's own top-five hits on average; at 0.5 they
# still added one or two cross-family rows while keeping 3.2 of five.
DEFAULT_LEXICON_WEIGHT = 0.5
PLAN_INSTRUCTIONS = (
    "Add 2-4 reformulations in other families' vocabulary (imported notes, corpus-import, "
    "literature, paper, historical theory); keep exact rationals, symbols and IDs verbatim; "
    "do not add IDs from expected answers; delete lexicon rows that miss the question's "
    "sense; weights lie in (0, 10] and scale that text's rank contribution only (1.0 = the "
    "question; higher lexicon weights find more cross-family rows and displace more of the "
    "question's own). Pass the edited file to "
    "'workhouse discover search QUESTION --queries-file plan.json'."
)
PLAN_MEANING = (
    "Query reformulations are retrieval aids. They add no evidence, do not change recorded "
    "status, evidence or tier, and never write to the scientific graph."
)

_SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_SOURCE = re.compile(r"^(?P<path>[^:\s]+):(?P<first>\d+)(?:-(?P<last>\d+))?$")
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_LETTERS = str.maketrans(
    {"ł": "l", "Ł": "L", "ø": "o", "Ø": "O", "ß": "ss", "æ": "ae", "œ": "oe", "đ": "d", "Đ": "D"}
)
_TEX_ACCENT = re.compile(r"\\[\"'`^~=.]\{?([A-Za-z])\}?")
# Tokens a sub-query must carry verbatim: colon-joined graph IDs, short label
# IDs (G19, SC17, R12a), and signed rationals or decimals.
_PROTECTED = re.compile(
    r"\b[A-Z][A-Z0-9]*(?::[A-Za-z0-9_.-]+)+|\b[A-Z]{1,6}\d+[A-Za-z0-9_]*\b|"
    r"[+-]?\d+\s*/\s*[+-]?\d+|[+-]?\d+(?:\.\d+)?"
)


def fold(text: str) -> str:
    """ASCII-fold accents and TeX accent commands; keep everything else."""
    text = _TEX_ACCENT.sub(r"\1", text).translate(_LETTERS)
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(c for c in decomposed if not unicodedata.combining(c))


def _cited_tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", fold(text).lower()))


def _variant_tokens(text: str) -> list[str]:
    """Index tokens of a folded variant, unique and in order."""
    return list(dict.fromkeys(tokenize(fold(text))))


def _fingerprint(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


# --------------------------------------------------------------------------- validation


def _check_variant(
    label: str, variant, root: Path | None, check_citations: bool, problems: list[str]
) -> None:
    if not isinstance(variant, dict):
        problems.append(f"{label}: variant must be a mapping")
        return
    reserved = sorted(set(variant) & RESERVED_KEYS)
    if reserved:
        problems.append(
            f"{label}: reserved keys {reserved}; the lexicon carries terminology only, "
            "scientific standing stays in ledger records"
        )
    unknown = sorted(set(variant) - VARIANT_KEYS - RESERVED_KEYS)
    if unknown:
        problems.append(f"{label}: unknown variant keys {unknown}")
    text = variant.get("text")
    if not isinstance(text, str) or not text.strip():
        problems.append(f"{label}: text must be a nonempty string")
        return
    if not re.search(r"[A-Za-z]", fold(text)):
        problems.append(f"{label}: variant text {text!r} has no word; values are not vocabulary")
    if _PROTECTED.search(text) and re.search(r"[A-Z][A-Z0-9]*:", text):
        problems.append(f"{label}: variant text {text!r} looks like a graph ID, not a term")
    family = variant.get("family")
    if family not in FAMILIES:
        problems.append(f"{label}: family {family!r} is not one of {list(FAMILIES)}")
    source = variant.get("source")
    if not isinstance(source, str) or not (match := _SOURCE.match(source.strip())):
        problems.append(f"{label}: source must be 'path:line' or 'path:first-last', got {source!r}")
        return
    path = match["path"].replace("\\", "/")
    first, last = int(match["first"]), int(match["last"] or match["first"])
    if first < 1 or last < first:
        problems.append(f"{label}: cited lines {first}-{last} are not an ascending range")
    if path.startswith("/") or ".." in path.split("/"):
        problems.append(f"{label}: source path must be checkout-relative, got {path!r}")
        return
    if family in FAMILY_ROOTS and not path.startswith(FAMILY_ROOTS[family]):
        problems.append(
            f"{label}: family {family!r} sources live under {list(FAMILY_ROOTS[family])}, "
            f"not {path!r}"
        )
    if not check_citations or root is None:
        return
    target = root / path
    try:
        inside = target.resolve().is_relative_to(root.resolve()) and not target.is_symlink()
    except (OSError, RuntimeError):
        inside = False
    if not inside or not target.is_file():
        problems.append(f"{label}: cited source {path!r} does not exist in the checkout")
        return
    try:
        lines = target.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        problems.append(f"{label}: cited source {path!r} unreadable: {exc}")
        return
    if last > len(lines):
        problems.append(f"{label}: cited lines {first}-{last} exceed {path!r} ({len(lines)} lines)")
        return
    cited = _cited_tokens("\n".join(lines[first - 1 : last]))
    missing = [token for token in sorted(_cited_tokens(text)) if token not in cited]
    if missing:
        problems.append(
            f"{label}: words {missing} of variant {text!r} are not at {path}:{first}-{last}; "
            "a variant must quote the family's own spelling"
        )


def _check_entry(
    index: int, entry, root: Path | None, check_citations: bool, problems: list[str]
) -> str | None:
    label = f"entries[{index}]"
    if not isinstance(entry, dict):
        problems.append(f"{label}: entry must be a mapping")
        return None
    slug = entry.get("concept")
    if isinstance(slug, str) and slug:
        label = f"entries[{index}] ({slug})"
    reserved = sorted(set(entry) & RESERVED_KEYS)
    if reserved:
        problems.append(
            f"{label}: reserved keys {reserved}; the lexicon carries terminology only, "
            "scientific standing stays in ledger records"
        )
    unknown = sorted(set(entry) - ENTRY_KEYS - RESERVED_KEYS)
    if unknown:
        problems.append(f"{label}: unknown entry keys {unknown}")
    missing = sorted(ENTRY_KEYS - set(entry))
    if missing:
        problems.append(f"{label}: missing keys {missing}")
    if not isinstance(slug, str) or not _SLUG.match(slug):
        problems.append(f"{label}: concept must be a lowercase hyphenated slug, got {slug!r}")
        slug = None
    meaning = entry.get("meaning")
    if not isinstance(meaning, str) or not meaning.strip():
        problems.append(f"{label}: meaning must be a nonempty sentence")
    for key in ("added_by",):
        if not isinstance(entry.get(key), str) or not entry[key].strip():
            problems.append(f"{label}: {key} must be a nonempty string")
    added_on = entry.get("added_on")
    if isinstance(added_on, _dt.date):
        added_on = added_on.isoformat()
    if not isinstance(added_on, str) or not _DATE.match(added_on):
        problems.append(f"{label}: added_on must be an ISO date, got {entry.get('added_on')!r}")
    related = entry.get("related")
    if not isinstance(related, list) or any(not isinstance(item, str) for item in related):
        problems.append(f"{label}: related must be a list of concept slugs")
    variants = entry.get("variants")
    if not isinstance(variants, list) or not variants:
        problems.append(f"{label}: variants must be a nonempty list")
        return slug
    families = set()
    seen = set()
    for number, variant in enumerate(variants):
        _check_variant(f"{label}.variants[{number}]", variant, root, check_citations, problems)
        if isinstance(variant, dict):
            families.add(variant.get("family"))
            key = (fold(str(variant.get("text", ""))).lower(), variant.get("family"))
            if key in seen:
                problems.append(f"{label}.variants[{number}]: duplicate variant {key}")
            seen.add(key)
    if len(families & set(FAMILIES)) < 2:
        problems.append(
            f"{label}: variants span {sorted(families)}; an entry must bridge at least two "
            "source families or it can never surface a cross-family source"
        )
    return slug


def validate(document, root: Path | None = None, *, check_citations: bool = True) -> list[str]:
    """Structural and citation problems of a parsed lexicon; empty when valid."""
    problems: list[str] = []
    if not isinstance(document, dict):
        return ["lexicon must be a mapping"]
    if document.get("schema") != SCHEMA:
        problems.append(f"schema must be {SCHEMA!r}, got {document.get('schema')!r}")
    unknown = sorted(set(document) - TOP_KEYS)
    if unknown:
        problems.append(f"unknown top-level keys {unknown}")
    version = document.get("version")
    if not isinstance(version, int) or isinstance(version, bool) or version < 1:
        problems.append(f"version must be a positive integer, got {version!r}")
    entries = document.get("entries")
    if not isinstance(entries, list):
        return problems + ["entries must be a list"]
    slugs: dict[str, int] = {}
    for index, entry in enumerate(entries):
        slug = _check_entry(index, entry, root, check_citations, problems)
        if slug is not None:
            if slug in slugs:
                problems.append(f"entries[{index}]: duplicate concept {slug!r}")
            slugs.setdefault(slug, index)
    for entry in entries:
        if isinstance(entry, dict) and isinstance(entry.get("related"), list):
            for target in entry["related"]:
                if isinstance(target, str) and target not in slugs:
                    problems.append(f"{entry.get('concept')}: related concept {target!r} unknown")
                if target == entry.get("concept"):
                    problems.append(f"{entry.get('concept')}: an entry cannot relate to itself")
    return problems


def _resolve(path: str | Path | None, root: Path | None) -> tuple[Path, Path]:
    """The lexicon file and the checkout its citations are relative to.

    An explicit ``root`` wins. Otherwise a lexicon that lives under some
    ``<checkout>/graph-tasks/discovery/`` cites that checkout, so validating a
    copy in another tree never reads this package's sources by mistake.
    """
    target = Path(path) if path is not None else None
    if root is not None:
        root = Path(root).resolve()
    else:
        root = ROOT
        if target is not None and target.is_absolute():
            for parent in target.resolve().parents:
                if parent.name == "discovery" and parent.parent.name == "graph-tasks":
                    root = parent.parent.parent
                    break
    if target is None:
        target = root / DEFAULT_PATH
    elif not target.is_absolute():
        target = root / target
    return target, root


def load(
    path: str | Path | None = None, root: Path | None = None, *, check_citations: bool = True
) -> dict:
    """Parse and validate a lexicon file; raise ``ValueError`` listing every problem.

    Citations are checked against ``root`` (the checkout) unless
    ``check_citations`` is false, which only a caller that has just validated
    the same bytes should pass.
    """
    target, root = _resolve(path, root)
    raw = target.read_bytes()
    try:
        document = yaml.safe_load(raw.decode("utf-8"))
    except (UnicodeDecodeError, yaml.YAMLError) as exc:
        raise ValueError(f"lexicon {target.name} is not valid UTF-8 YAML: {exc}") from exc
    problems = validate(document, root, check_citations=check_citations)
    if problems:
        raise ValueError(f"lexicon {target.name} invalid:\n  " + "\n  ".join(problems))
    for entry in document["entries"]:
        if isinstance(entry.get("added_on"), _dt.date):
            entry["added_on"] = entry["added_on"].isoformat()
    document["path"] = target.as_posix()
    document["fingerprint"] = _fingerprint(raw)
    return document


def lexicon_list(lexicon: dict) -> list[dict]:
    """One compact row per concept: families bridged and variant count."""
    rows = []
    for entry in lexicon["entries"]:
        families = sorted({variant["family"] for variant in entry["variants"]})
        rows.append(
            {
                "concept": entry["concept"],
                "meaning": entry["meaning"],
                "families": families,
                "variants": len(entry["variants"]),
                "related": list(entry.get("related", [])),
            }
        )
    return sorted(rows, key=lambda row: row["concept"])


def lexicon_show(lexicon: dict, concept: str) -> dict:
    for entry in lexicon["entries"]:
        if entry["concept"] == concept:
            return entry
    raise ValueError(f"unknown concept {concept!r}; see 'workhouse discover lexicon list'")


# --------------------------------------------------------------------------- expansion


def _phrase_pattern(text: str) -> re.Pattern:
    """The variant's own words, in order, tolerant of plurals and separators.

    Built from the raw words (stop words included) rather than the index
    tokens, so ``uniform in volume`` is found in a query that says exactly
    that, while ``rare coarse fibers`` is not mistaken for ``rare fibers``
    and falls back to augmentation.
    """
    parts = []
    for word in re.findall(r"[A-Za-z0-9']+", fold(text)):
        stem = word[:-1] if len(word) > 3 and word.lower().endswith("s") else word
        parts.append(re.escape(stem) + r"(?:s|es)?")
    return re.compile(r"(?<![A-Za-z0-9])" + r"[\s\-–—_/*^]+".join(parts) + r"(?![A-Za-z0-9])", re.I)


def _protected(query: str) -> list[str]:
    return [re.sub(r"\s+", "", token) for token in _PROTECTED.findall(query)]


def _keeps_protected(sub_query: str, protected: list[str]) -> bool:
    compact = re.sub(r"\s+", "", sub_query)
    return all(token in compact for token in protected)


def matches(query: str, lexicon: dict) -> list[dict]:
    """Variants whose every index token occurs in the query.

    Deterministic order: more tokens first (a multi-word variant is a more
    specific match than a single word), then concept slug, then the
    variant's position in its entry.
    """
    present = set(tokenize(fold(query)))
    found = []
    for entry in lexicon["entries"]:
        for position, variant in enumerate(entry["variants"]):
            tokens = _variant_tokens(variant["text"])
            if tokens and all(token in present for token in tokens):
                found.append(
                    {
                        "concept": entry["concept"],
                        "text": variant["text"],
                        "family": variant["family"],
                        "source": variant["source"],
                        "tokens": tokens,
                        "position": position,
                    }
                )
    found.sort(key=lambda row: (-len(row["tokens"]), row["concept"], row["position"]))
    return found


def _alternatives(matched: dict, entry: dict) -> list[dict]:
    """Other-family variants of a matched concept, without near-duplicate phrasings.

    Two alternatives whose token sets nest (``Schur complement`` and ``Schur
    complement identity``) rank the same passages, and reciprocal-rank fusion
    then counts that passage once per sub-query: on the real corpus such
    stacked votes evicted the question's own top hits. Keep the first of any
    nesting pair, in lexicon order.
    """
    seen_keys = {fold(matched["text"]).lower()}
    chosen: list[set[str]] = [set(matched["tokens"])]
    alternatives = []
    for variant in entry["variants"]:
        key = fold(variant["text"]).lower()
        if variant["family"] == matched["family"] or key in seen_keys:
            continue
        tokens = set(_variant_tokens(variant["text"]))
        if not tokens or any(tokens <= other or tokens >= other for other in chosen):
            continue
        seen_keys.add(key)
        chosen.append(tokens)
        alternatives.append(variant)
    return alternatives


def expand(
    query: str,
    lexicon: dict,
    max_sub_queries: int = 6,
    *,
    mode: str = "focused",
    weight: float = DEFAULT_LEXICON_WEIGHT,
) -> dict:
    """Sub-queries that restate ``query`` in the other families' vocabulary.

    For each matched concept (best variant first) the other families'
    variants are taken in turn, so no single concept fills the budget.

    ``mode="focused"`` (default) emits each alternative phrase on its own,
    followed by the question's exact rationals, decimals and IDs. Measured on
    the checkout on 2026-09-11, this was the only shape that lifted imported
    notes, corpus-import and literature passages into the top ten for
    derivation-vocabulary questions; ``mode="in-place"``, which substitutes
    the alternative into the full question (or appends it when the matched
    phrase is not contiguous), left those top tens unchanged because the
    question's other words still favour its own family. Focused sub-queries
    cost precision, so ``weight`` (returned per sub-query for
    ``query_weights``) defaults below the question's 1.0; at 1.0 they evicted
    the question's own top hits on two of six questions.

    Every sub-query keeps the original text's protected tokens verbatim; an
    in-place substitution that would drop one falls back to appending.
    """
    if not 0 <= max_sub_queries <= MAX_SUB_QUERIES:
        raise ValueError(f"max_sub_queries must lie in [0, {MAX_SUB_QUERIES}]")
    if mode not in ("focused", "in-place"):
        raise ValueError("mode must be 'focused' or 'in-place'")
    if not 0 < weight <= 10:
        raise ValueError("lexicon weight must lie in (0, 10]")
    folded = " ".join(fold(query).split())
    protected = _protected(query)
    by_concept: dict[str, dict] = {}
    for row in matches(query, lexicon):
        by_concept.setdefault(row["concept"], row)
    entries = {entry["concept"]: entry for entry in lexicon["entries"]}
    queues = [
        (matched, alternatives)
        for concept, matched in by_concept.items()
        if (alternatives := _alternatives(matched, entries[concept]))
    ]
    sub_queries: list[str] = []
    explanations: list[str] = []
    detail: list[dict] = []
    taken = {folded.lower()}
    while len(sub_queries) < max_sub_queries and any(queue for _, queue in queues):
        for matched, queue in queues:
            if not queue or len(sub_queries) >= max_sub_queries:
                continue
            alternative = queue.pop(0)
            if mode == "focused":
                text, how = " ".join([alternative["text"], *protected]), "focused"
            else:
                found = _phrase_pattern(matched["text"]).search(folded)
                how = "replaced" if found else "augmented"
                text = (
                    folded[: found.start()] + alternative["text"] + folded[found.end() :]
                    if found
                    else folded + " " + alternative["text"]
                )
                if found and not _keeps_protected(text, protected):
                    text, how = folded + " " + alternative["text"], "augmented"
            text = " ".join(text.split())
            if text.lower() in taken:
                continue
            taken.add(text.lower())
            sub_queries.append(text)
            explanations.append(
                f"q{len(sub_queries) + 1}: {matched['concept']}: '{matched['text']}' "
                f"({matched['family']}) {how} -> '{alternative['text']}' "
                f"({alternative['family']}; {alternative['source']})"
            )
            detail.append(
                {
                    "sub_query": text,
                    "concept": matched["concept"],
                    "matched": {
                        "text": matched["text"],
                        "family": matched["family"],
                        "source": matched["source"],
                    },
                    "alternative": {
                        "text": alternative["text"],
                        "family": alternative["family"],
                        "source": alternative["source"],
                    },
                    "mode": how,
                }
            )
    return {
        "query": query,
        "mode": mode,
        "sub_queries": sub_queries,
        "weights": [weight] * len(sub_queries),
        "concepts": [concept for concept, _ in by_concept.items() if concept in entries],
        "explanations": explanations,
        "matches": [
            {key: row[key] for key in ("concept", "text", "family", "source")}
            for row in by_concept.values()
        ],
        "detail": detail,
        "protected": protected,
    }


def plan(
    query: str,
    lexicon: dict,
    max_sub_queries: int = 6,
    *,
    lexicon_weight: float = DEFAULT_LEXICON_WEIGHT,
    mode: str = "focused",
) -> dict:
    """A JSON query plan an agent edits and passes to ``search --queries-file``."""
    if not query.strip():
        raise ValueError("a plan needs a research question")
    expansion = expand(query, lexicon, max_sub_queries, mode=mode, weight=lexicon_weight)
    queries = [{"text": query.strip(), "weight": 1.0, "origin": "user"}]
    # Two concepts can produce the same reformulation, and a variant that is
    # already the question's own wording produces the question again; a plan
    # that repeats a text would double-count it at fusion time.
    seen = {" ".join(query.split()).casefold()}
    for row in expansion["detail"]:
        key = " ".join(str(row["sub_query"]).split()).casefold()
        if key in seen:
            continue
        seen.add(key)
        queries.append(
            {
                "text": row["sub_query"],
                "weight": lexicon_weight,
                "origin": f"lexicon:{row['concept']}",
                "cites": row["alternative"]["source"],
            }
        )
    return {
        "schema": PLAN_SCHEMA,
        "question": query.strip(),
        "queries": queries,
        "seeds": [],
        "instructions": PLAN_INSTRUCTIONS,
        "mode": mode,
        "concepts": expansion["concepts"],
        "explanations": expansion["explanations"],
        "lexicon": {
            "schema": lexicon.get("schema"),
            "version": lexicon.get("version"),
            "path": lexicon.get("path"),
            "fingerprint": lexicon.get("fingerprint"),
        },
        "meaning": PLAN_MEANING,
    }


# --------------------------------------------------------------------------- maintenance


def _entry_block(entry: dict, indent: str) -> str:
    """One list item, indented to match the file's existing ``entries`` items."""
    dumped = yaml.safe_dump(
        [entry], sort_keys=False, allow_unicode=True, width=100, default_flow_style=False
    )
    return "".join(indent + line + "\n" for line in dumped.rstrip("\n").splitlines())


def lexicon_add(path: str | Path | None, entry: dict, root: Path | None = None) -> dict:
    """Append one validated entry, bump the version, and re-validate the file.

    The file is rewritten only after the merged document passes the same
    validation as ``load``; a rejected entry leaves the bytes untouched. The
    ``entries:`` list must be the last top-level key so the append is textual
    and hand-written comments survive.
    """
    target, root = _resolve(path, root)
    original = target.read_bytes()
    lexicon = load(target, root)
    if not isinstance(entry, dict):
        raise ValueError("entry must be a mapping")
    entry = dict(entry)
    entry.setdefault("related", [])
    entry.setdefault("added_on", _dt.date.today().isoformat())
    if isinstance(entry.get("added_on"), _dt.date):
        entry["added_on"] = entry["added_on"].isoformat()
    ordered = {
        key: entry[key] for key in ("concept", "meaning", "variants", "related") if key in entry
    }
    ordered.update({key: entry[key] for key in entry if key not in ordered})
    merged = {key: value for key, value in lexicon.items() if key not in ("path", "fingerprint")}
    merged["entries"] = [*lexicon["entries"], ordered]
    problems = validate(merged, root)
    if problems:
        raise ValueError("entry rejected:\n  " + "\n  ".join(problems))
    text = original.decode("utf-8")
    keys = list(re.finditer(r"^([A-Za-z_]+):(.*)$", text, re.M))
    if not keys or keys[-1].group(1) != "entries":
        raise ValueError("lexicon_add needs 'entries:' as the last top-level key")
    entries_line = keys[-1]
    if entries_line.group(2).strip() == "[]":
        # An empty inline list cannot take a textual append; open it as a block.
        text = text[: entries_line.start()] + "entries:" + text[entries_line.end() :]
        indent = "  "
    else:
        first_item = re.search(r"^([ \t]*)-\s", text[entries_line.end() :], re.M)
        if first_item is None:
            raise ValueError("lexicon_add cannot find the entries list items to align with")
        indent = first_item.group(1)
    text = re.sub(
        r"^version:\s*\d+\s*$", f"version: {lexicon['version'] + 1}", text, count=1, flags=re.M
    )
    today = _dt.date.today().isoformat()
    if re.search(r"^updated_on:.*$", text, re.M):
        text = re.sub(r"^updated_on:.*$", f"updated_on: {today}", text, count=1, flags=re.M)
    if not text.endswith("\n"):
        text += "\n"
    text += _entry_block(ordered, indent)
    target.write_text(text, encoding="utf-8", newline="\n")
    try:
        return load(target, root)
    except ValueError:
        target.write_bytes(original)
        raise


# --------------------------------------------------------------------------- CLI


def add_parser(subparsers) -> None:
    """Register ``plan`` and ``lexicon`` under ``workhouse discover``."""
    plan_parser = subparsers.add_parser(
        "plan", help="query plan: the question plus lexicon reformulations in other vocabularies"
    )
    plan_parser.add_argument("question", help="research question in your own words")
    plan_parser.add_argument(
        "--lexicon", metavar="PATH", help=f"lexicon file (default {DEFAULT_PATH})"
    )
    plan_parser.add_argument(
        "--max-sub-queries", type=int, default=6, help="lexicon reformulations to add (default 6)"
    )
    plan_parser.add_argument(
        "--weight",
        type=float,
        default=DEFAULT_LEXICON_WEIGHT,
        help="rank weight of each lexicon reformulation (default 0.7; the question keeps 1.0)",
    )
    plan_parser.add_argument(
        "--mode",
        choices=("focused", "in-place"),
        default="focused",
        help="focused: each alternative phrase alone (reaches other families); "
        "in-place: substituted into the full question (keeps the question's own hits)",
    )
    plan_parser.add_argument("--out", help="retain the plan JSON in a new file; refuse overwrite")
    plan_parser.add_argument(
        "--root",
        metavar="DIR",
        help="checkout the lexicon's citations refer to (default: this one)",
    )
    plan_parser.add_argument("--json", action="store_true")
    lexicon_parser = subparsers.add_parser(
        "lexicon", help="the source-cited concept lexicon behind query plans"
    )
    lexicon_sub = lexicon_parser.add_subparsers(dest="lexicon_command", required=True)
    for name, help_text in (
        ("list", "every concept with the families it bridges"),
        ("show", "one concept with every cited variant"),
        ("add", "append a validated entry from a JSON or YAML file"),
        ("validate", "check schema, citations and family roots"),
    ):
        command = lexicon_sub.add_parser(name, help=help_text)
        if name == "show":
            command.add_argument("concept")
        if name == "add":
            command.add_argument(
                "--entry", required=True, metavar="PATH", help="JSON or YAML file with one entry"
            )
        command.add_argument(
            "--lexicon", metavar="PATH", help=f"lexicon file (default {DEFAULT_PATH})"
        )
        command.add_argument(
            "--root",
            metavar="DIR",
            help="checkout the lexicon's citations refer to (default: this one)",
        )
        command.add_argument("--json", action="store_true")


def render_plan(result: dict) -> str:
    lines = [result["meaning"], "", f"question: {result['question']}"]
    for number, row in enumerate(result["queries"], 1):
        lines.append(f"q{number}  w={row['weight']:<4} {row['origin']:<28} {row['text']}")
    if result.get("explanations"):
        lines.append("")
        lines.extend(result["explanations"])
    lines.extend(["", result["instructions"]])
    return "\n".join(lines)


def render_list(rows: list[dict]) -> str:
    lines = []
    for row in rows:
        lines.append(
            f"{row['concept']:<30} {row['variants']:>2} variants  {', '.join(row['families'])}"
        )
        lines.append(f"    {row['meaning']}")
    return "\n".join(lines)


def render_entry(entry: dict) -> str:
    lines = [entry["concept"], f"  {entry['meaning']}"]
    for variant in entry["variants"]:
        lines.append(f"  [{variant['family']}] {variant['text']}  ({variant['source']})")
    if entry.get("related"):
        lines.append(f"  related: {', '.join(entry['related'])}")
    lines.append(f"  added by {entry['added_by']} on {entry['added_on']}")
    return "\n".join(lines)


def _read_entry_file(path: str) -> dict:
    raw = Path(path).read_text(encoding="utf-8")
    entry = json.loads(raw) if raw.lstrip().startswith("{") else yaml.safe_load(raw)
    if not isinstance(entry, dict):
        raise ValueError("entry file must hold one mapping")
    return entry


def run(args, engine_factory=None) -> int:
    """Execute ``plan`` or ``lexicon``; returns the process exit code.

    ``engine_factory`` is accepted for uniformity with the other discovery
    commands and never called: plans and lexicon maintenance read sources and
    the lexicon file only, so no index is built and no scientific record is
    touched.
    """
    del engine_factory
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            with contextlib.suppress(ValueError, OSError):
                stream.reconfigure(encoding="utf-8", errors="replace")
    as_json = bool(getattr(args, "json", False))
    try:
        lexicon_path = getattr(args, "lexicon", None)
        root = Path(args.root) if getattr(args, "root", None) else None
        if args.discovery_command == "plan":
            lexicon = load(lexicon_path, root)
            result = plan(
                args.question,
                lexicon,
                args.max_sub_queries,
                lexicon_weight=args.weight,
                mode=args.mode,
            )
            report = render_plan(result)
            if getattr(args, "out", None):
                out = Path(args.out)
                out.parent.mkdir(parents=True, exist_ok=True)
                with out.open("x", encoding="utf-8", newline="\n") as handle:
                    handle.write(json.dumps(result, sort_keys=True, ensure_ascii=True) + "\n")
        elif args.lexicon_command == "validate":
            lexicon = load(lexicon_path, root)
            result = {
                "schema": lexicon["schema"],
                "version": lexicon["version"],
                "path": lexicon["path"],
                "fingerprint": lexicon["fingerprint"],
                "concepts": len(lexicon["entries"]),
                "variants": sum(len(entry["variants"]) for entry in lexicon["entries"]),
                "valid": True,
            }
            report = (
                f"lexicon valid: {result['concepts']} concepts, {result['variants']} cited "
                f"variants, version {result['version']}, fingerprint {result['fingerprint'][:12]}"
            )
        elif args.lexicon_command == "list":
            lexicon = load(lexicon_path, root)
            result = lexicon_list(lexicon)
            report = render_list(result)
        elif args.lexicon_command == "show":
            result = lexicon_show(load(lexicon_path, root), args.concept)
            report = render_entry(result)
        elif args.lexicon_command == "add":
            entry = _read_entry_file(args.entry)
            lexicon = lexicon_add(lexicon_path, entry, root)
            result = lexicon_show(lexicon, entry["concept"])
            report = f"added; lexicon version {lexicon['version']}\n" + render_entry(result)
        else:
            raise ValueError(f"unknown lexicon command {args.lexicon_command!r}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        error = {"schema": "workhouse-discovery/error/v1", "error": str(exc)}
        print(json.dumps(error) if as_json else f"Discovery lexicon unavailable: {exc}")
        return 1
    print(json.dumps(result, sort_keys=True, ensure_ascii=True) if as_json else report)
    return 0
