"""``workhouse ask``: a natural-language candidate finder, outside the tiers.

The exact-rational search is the right front door for a value, and useless
for a question. "which document argues the upper band edge from regularity"
has no rational in it. The 2026-08-28 agent experience note asked for a
semantic surface over the corpus, with one condition this module keeps: it
finds *candidates* and promotes nothing. Every hit is T3, every catalogue
hit carries its ``why`` command, and no check reads anything here.

The ranking is BM25 over chunks of the corpus prose (``corpus-import``
``.md`` and ``.tex``), the pinned paper sources, the ADRs, and every
catalogue record's statement and detail. Lexical rather than embedded, on
purpose: it needs no model, no download, no new dependency, it is
deterministic on every machine, and the join keys of this corpus are tokens
(``5/48``, ``C_shp``, ``t_N``) that an embedding would blur. An embedding
backend can be added behind the same interface if it ever earns its weight;
ADR 0017 records the trade.

The index is memoised on disk outside the repository, keyed on a fingerprint
of its inputs, the way the corpus scan and the check cache are.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import pickle
import re
from dataclasses import dataclass
from pathlib import Path

from . import claims as claims_mod

ROOT = Path(__file__).resolve().parents[2]
CORPUS_DIR = ROOT / "corpus-import"
PAPER_DIR = ROOT / "paper"
DECISIONS_DIR = ROOT / "docs" / "decisions"

PROSE_EXTS = {".md", ".tex"}
SKIP_PARTS = {"archive", "__pycache__", ".git", "GITHUB", ".venv"}
#: Chunk size in tokens, with the overlap that keeps a sentence from being
#: split between two chunks and lost to both.
CHUNK = 160
OVERLAP = 40
MAX_BYTES = 4 * 1024 * 1024

#: Tokens: words, identifiers with underscores, and exact rationals kept whole
#: so `5/48` is one term and never `5` and `48`.
_TOKEN = re.compile(r"-?\d+/\d+|[A-Za-z][A-Za-z0-9_^']*|\d+(?:\.\d+)?")
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
        "not",
        "no",
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
        "one",
        "two",
    ]  # noqa: SIM905 -- a word list reads as words, not as 70 quoted literals
)


def tokenize(text: str) -> list[str]:
    out = []
    for tok in _TOKEN.findall(text):
        low = tok.lower()
        if low in _STOP or len(low) < 2:
            continue
        # light stemming: plural nouns and a few verb endings
        if len(low) > 4 and low.endswith("s") and not low.endswith("ss"):
            low = low[:-1]
        out.append(low)
    return out


@dataclass
class Chunk:
    #: `corpus-import/<path>:<line>` for prose, a catalogue id for records.
    where: str
    #: The catalogue id when the chunk IS a record, else "".
    claim: str
    text: str
    tokens: list[str]


def _prose_files():
    for root in (CORPUS_DIR, PAPER_DIR, DECISIONS_DIR):
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in PROSE_EXTS:
                continue
            if any(part in SKIP_PARTS for part in path.parts):
                continue
            if path.stat().st_size > MAX_BYTES:
                continue
            yield path


def _chunk_file(path: Path) -> list[Chunk]:
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return []
    rel = path.relative_to(ROOT).as_posix()
    # token stream with the line each token came from
    stream: list[tuple[str, int]] = []
    for lineno, line in enumerate(lines, 1):
        for tok in tokenize(line):
            stream.append((tok, lineno))
    chunks: list[Chunk] = []
    start = 0
    while start < len(stream):
        window = stream[start : start + CHUNK]
        first_line, last_line = window[0][1], window[-1][1]
        text = " ".join(lines[first_line - 1 : last_line]).strip()
        chunks.append(
            Chunk(
                where=f"{rel}:{first_line}",
                claim="",
                text=" ".join(text.split())[:600],
                tokens=[t for t, _ in window],
            )
        )
        if start + CHUNK >= len(stream):
            break
        start += CHUNK - OVERLAP
    return chunks


def _record_chunks(catalogue: list[claims_mod.Claim]) -> list[Chunk]:
    out = []
    for claim in catalogue:
        text = " ".join(x for x in (claim.statement, claim.detail, claim.value or "") if x)
        tokens = tokenize(text)
        if not tokens:
            continue
        out.append(
            Chunk(where=claim.where or claim.id, claim=claim.id, text=text[:600], tokens=tokens)
        )
    return out


@dataclass
class Index:
    chunks: list[Chunk]
    df: dict[str, int]
    avg_len: float

    def score(self, query: str, k1: float = 1.5, b: float = 0.75) -> list[tuple[float, Chunk]]:
        terms = tokenize(query)
        if not terms:
            return []
        n = len(self.chunks)
        idf = {
            t: math.log(1 + (n - self.df.get(t, 0) + 0.5) / (self.df.get(t, 0) + 0.5))
            for t in terms
        }
        scored = []
        for chunk in self.chunks:
            if not any(t in chunk.tokens for t in terms):
                continue
            counts: dict[str, int] = {}
            for t in chunk.tokens:
                counts[t] = counts.get(t, 0) + 1
            length = len(chunk.tokens)
            s = 0.0
            for t in terms:
                f = counts.get(t, 0)
                if f:
                    s += idf[t] * f * (k1 + 1) / (f + k1 * (1 - b + b * length / self.avg_len))
            if s > 0:
                scored.append((s, chunk))
        scored.sort(key=lambda x: (-x[0], x[1].where))
        return scored


def _fingerprint(catalogue_path: Path) -> str:
    h = hashlib.sha256()
    for path in _prose_files():
        st = path.stat()
        h.update(f"{path.relative_to(ROOT).as_posix()}|{st.st_size}|{st.st_mtime_ns}\n".encode())
    if catalogue_path.exists():
        st = catalogue_path.stat()
        h.update(f"catalogue|{st.st_size}|{st.st_mtime_ns}\n".encode())
    return h.hexdigest()


def build(catalogue: list[claims_mod.Claim] | None = None) -> Index:
    catalogue = catalogue if catalogue is not None else claims_mod.load_catalogue()
    chunks: list[Chunk] = []
    for path in _prose_files():
        chunks.extend(_chunk_file(path))
    chunks.extend(_record_chunks(catalogue))
    df: dict[str, int] = {}
    for chunk in chunks:
        for t in set(chunk.tokens):
            df[t] = df.get(t, 0) + 1
    avg = sum(len(c.tokens) for c in chunks) / max(1, len(chunks))
    return Index(chunks, df, avg)


def load_cached() -> Index:
    """The index, memoised on disk outside the repository."""
    key = _fingerprint(claims_mod.CLAIMS)
    cache_dir = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "workhouse"
    cache = cache_dir / f"finder-{key[:24]}.pkl"
    if cache.exists() and os.environ.get("WORKHOUSE_NO_CACHE", "") not in ("1", "true", "yes"):
        try:
            return pickle.loads(cache.read_bytes())
        except Exception:
            pass
    index = build()
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        tmp = cache_dir / f"finder-{key[:24]}.tmp"
        tmp.write_bytes(pickle.dumps(index))
        tmp.replace(cache)
    except OSError:
        pass
    return index


def ask(query: str, limit: int = 10, index: Index | None = None) -> tuple[list[dict], str]:
    """Top candidates for a natural-language query, and the rendered report."""
    index = index if index is not None else load_cached()
    hits = index.score(query)[:limit]
    rows = [
        {
            "score": round(s, 3),
            "where": c.where,
            "claim": c.claim,
            "text": c.text[:300],
            "why": f"workhouse why {c.claim!r}" if c.claim else "",
        }
        for s, c in hits
    ]
    lines = [
        f"\033[1mcandidates for:\033[0m {query}",
        "  \033[2mA candidate finder, not evidence: every hit is T3. Route a catalogue hit "
        "through `workhouse why`; open a corpus hit at the line shown.\033[0m",
    ]
    if not rows:
        lines.append(
            "  no chunk shares a term with the query; try the value or symbol with "
            "`workhouse search`"
        )
    for row in rows:
        lines.append("")
        head = f"  {row['score']:6.2f}  {row['where']}"
        if row["claim"]:
            head += f"  \033[2m{row['claim']}\033[0m"
        lines.append(head)
        lines.append(f"         {row['text'][:220]}")
        if row["why"]:
            lines.append(f"         \033[2m{row['why']}\033[0m")
    return rows, "\n".join(lines)


def render_json(rows: list[dict], query: str) -> str:
    return json.dumps({"query": query, "candidates": rows, "tier": "T3"}, sort_keys=True)
