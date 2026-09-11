"""Optional, revision-pinned local semantic candidates for hybrid discovery.

The default engine has no model dependency. Only explicit vector generation or
query encoding imports sentence-transformers; retrieval never downloads models.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path

SCHEMA = "workhouse-discovery/embeddings/v1"


def record_fingerprint(records: list[dict]) -> str:
    texts = sorted((row["id"], row.get("statement", ""), row.get("detail", "")) for row in records)
    return hashlib.sha256(json.dumps(texts, ensure_ascii=True).encode()).hexdigest()


def _unit(vector) -> list[float]:
    if not isinstance(vector, (list, tuple)) or not vector:
        raise ValueError("embedding must be a nonempty vector")
    if any(isinstance(value, bool) or not isinstance(value, (int, float)) for value in vector):
        raise ValueError("embedding values must be real numbers")
    if not all(math.isfinite(value) for value in vector):
        raise ValueError("embedding values must be finite")
    norm = math.hypot(*vector)
    if not math.isfinite(norm) or norm == 0:
        raise ValueError("embedding norm must be finite and nonzero")
    return [value / norm for value in vector]


class SemanticVectors:
    def __init__(self, payload: dict, records: list[dict]):
        if not isinstance(payload, dict):
            raise ValueError("embedding payload must be a JSON object")
        if payload.get("schema") != SCHEMA:
            raise ValueError("unsupported embedding schema")
        if payload.get("record_fingerprint") != record_fingerprint(records):
            raise ValueError("semantic vectors are stale for the saved record texts")
        if not isinstance(payload.get("revision"), str) or not re.fullmatch(
            r"[0-9a-f]{40}", payload["revision"]
        ):
            raise ValueError("embedding model revision must be a full commit SHA")
        model = payload.get("model_id")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("embedding model_id is required")
        known = {row["id"] for row in records}
        raw = payload.get("vectors")
        if not isinstance(raw, dict) or not raw or set(raw) - known:
            raise ValueError("vectors must name existing saved records")
        self.vectors = {node: _unit(vector) for node, vector in raw.items()}
        dimensions = {len(vector) for vector in self.vectors.values()}
        if len(dimensions) != 1 or next(iter(dimensions)) != payload.get("dimensions"):
            raise ValueError("embedding dimensions disagree")
        self.dimensions = next(iter(dimensions))
        self.model_id = model
        self.revision = payload["revision"]
        self.query_prefix = payload.get("query_prefix", "")
        if not isinstance(self.query_prefix, str):
            raise ValueError("query_prefix must be a string")
        self.fingerprint = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

    @classmethod
    def load(cls, path: Path, records: list[dict]):
        return cls(json.loads(Path(path).read_text(encoding="utf-8")), records)

    def rank(self, vector: list[float], limit: int = 100) -> dict[str, float]:
        if not 1 <= limit <= 1000:
            raise ValueError("semantic limit must be between 1 and 1000")
        query = _unit(vector)
        if len(query) != self.dimensions:
            raise ValueError("query embedding dimensions disagree")
        scored = (
            (node, math.fsum(a * b for a, b in zip(query, values, strict=True)))
            for node, values in self.vectors.items()
        )
        return dict(sorted(scored, key=lambda row: (-row[1], row[0]))[:limit])

    def search(self, query: str, limit: int = 100) -> dict[str, float]:
        model = _model(self.model_id, self.revision, allow_download=False)
        vector = model.encode([self.query_prefix + query], normalize_embeddings=True)[0].tolist()
        return self.rank(vector, limit)

    def neighbors(self, seeds: list[str], limit: int = 100) -> dict[str, float]:
        if not seeds or any(seed not in self.vectors for seed in seeds):
            raise ValueError("every semantic seed must have a stored vector")
        vectors = [self.vectors[seed] for seed in dict.fromkeys(seeds)]
        mean = [
            math.fsum(vector[i] for vector in vectors) / len(vectors)
            for i in range(self.dimensions)
        ]
        return self.rank(mean, limit)


def _model(model_id: str, revision: str, *, allow_download: bool):
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("model revision must be a full 40-character commit SHA")
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise ValueError(
            "optional semantic mode requires sentence-transformers; see docs/graph_discovery.md"
        ) from exc
    return SentenceTransformer(
        model_id, revision=revision, trust_remote_code=False, local_files_only=not allow_download
    )


def generate(
    records: list[dict],
    model_id: str,
    revision: str,
    *,
    allow_download=False,
    query_prefix="",
    batch_size=32,
) -> dict:
    """Generate vectors explicitly; model-specific truncation remains visible."""
    model = _model(model_id, revision, allow_download=allow_download)
    records = sorted(records, key=lambda row: row["id"])
    texts = [row.get("statement", "") + "\n" + row.get("detail", "") for row in records]
    vectors = model.encode(
        texts, batch_size=batch_size, normalize_embeddings=True, show_progress_bar=True
    )
    return {
        "schema": SCHEMA,
        "model_id": model_id,
        "revision": revision,
        "record_fingerprint": record_fingerprint(records),
        "query_prefix": query_prefix,
        "dimensions": int(vectors.shape[1]),
        "max_sequence_length": model.max_seq_length,
        "scope": "saved record statement and detail; model tokenizer truncates overlong inputs",
        "vectors": {
            row["id"]: vector.tolist() for row, vector in zip(records, vectors, strict=True)
        },
    }
