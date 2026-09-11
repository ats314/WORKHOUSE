"""Hybrid corpus discovery with explicit retrieval provenance.

Rank fusion and graph traversal select research candidates. They never add
scientific edges, execute checks, or rewrite a source record's evidence tier.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

from .discovery_graph import GraphDiscovery
from .discovery_index import DiscoveryIndex

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = "workhouse-discovery/v1"


def reciprocal_rank_fusion(channels: dict[str, list[str]], weights=None, k=60) -> dict:
    """Fuse deduplicated rankings; scores express retrieval relevance only."""
    if k <= 0:
        raise ValueError("rank-fusion k must be positive")
    weights = weights or {}
    scores: dict[str, dict] = {}
    for name, ranking in channels.items():
        for rank, node in enumerate(dict.fromkeys(ranking), 1):
            contribution = weights.get(name, 1.0) / (k + rank)
            row = scores.setdefault(node, {"score": 0.0, "channels": {}})
            row["score"] += contribution
            row["channels"][name] = {"rank": rank, "contribution": contribution}
    return dict(sorted(scores.items(), key=lambda item: (-item[1]["score"], item[0])))


def _source_path(source: str) -> str:
    # Strip locators after an extension, preserving literal '#file' and '(2)' filenames.
    suffix = re.search(r"\.(?:md|tex|txt|py|lean|ya?ml|jsonl?)(?= (?:\(|#)|#)", source, re.I)
    if suffix:
        source = source[: suffix.end()]
    return re.sub(r":\d+(?::\d+)?$", "", source)


def _family(row: dict) -> str:
    return _source_path(row.get("path") or row.get("where", "") or row["id"])


def _select_diverse(rows: list[dict], limit: int, per_source: int = 2) -> list[dict]:
    """Source quotas prevent overlapping passages from filling a context."""
    selected, deferred = [], []
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        family = (
            _family({"id": row["id"], "where": row.get("where", "")})
            if isinstance(row.get("path"), list)
            else _family(row)
        )
        if counts[family] >= per_source:
            deferred.append(row)
        else:
            selected.append(row)
            counts[family] += 1
        if len(selected) == limit:
            return selected
    return (selected + deferred)[:limit]


class DiscoveryEngine:
    """One indexed corpus and saved graph, reusable across an agent's queries."""

    def __init__(self, root: Path = ROOT, *, cache_dir: Path | None = None):
        self.root = Path(root).resolve()
        self.index = DiscoveryIndex(self.root, cache_dir=cache_dir)
        self.index.build()
        symbols = [
            {
                "id": "SYM:" + row["id"],
                "kind": "symbol",
                "statement": row.get("canonical", row["id"]),
                "where": "ledger/symbols.yaml",
                "detail": json.dumps(row, sort_keys=True),
            }
            for row in self.index.symbols
        ]
        self.records = {row["id"]: row for row in self.index.records + symbols}
        self.graph = GraphDiscovery(list(self.records.values()), self.index.edges)
        self._catalogue = None

    def close(self):
        self.index.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    def _exact(self, query: str) -> list[str]:
        # Keep the established rational/alias semantics and saved input scope.
        from .claims import Claim
        from .search import search

        if query.strip() in self.records:
            return [query.strip()]
        if self._catalogue is None:
            # The saved catalogue is immutable for this engine's lifetime.
            self._catalogue = [Claim(**row) for row in self.index.records]
        hits, _ = search(query, catalogue=self._catalogue, symbols=self.index.symbols)
        return [
            hit.claim.id
            for hit in hits
            if hit.how == "exact value" or hit.how == "claim id" or "alias" in hit.how
        ]

    def _record_hit(self, node: str) -> dict:
        record = self.records[node]
        return {
            "id": node,
            "claim_ids": [node],
            "kind": "record",
            "path": _source_path(record.get("where", "")),
            "where": record.get("where", ""),
            "text": record.get("statement", ""),
            "record": record,
        }

    def search(
        self,
        query: str,
        limit: int = 10,
        seeds: list[str] | None = None,
        *,
        pool: int = 100,
        graph_weight: float = 0.8,
        related_limit: int = 5,
        semantic_scores: dict[str, float] | None = None,
        semantic: Path | None = None,
    ) -> dict:
        if not 1 <= limit <= 100:
            raise ValueError("limit must be between 1 and 100")
        if not 1 <= pool <= 1000:
            raise ValueError("candidate pool must be between 1 and 1000")
        if not 0 <= graph_weight <= 3:
            raise ValueError("graph weight must be between 0 and 3")
        if not 0 <= related_limit <= 100:
            raise ValueError("related limit must be between 0 and 100")
        seeds = list(dict.fromkeys(seeds or []))
        unknown = sorted(set(seeds) - self.records.keys())
        if unknown:
            raise ValueError(f"unknown seed IDs: {', '.join(unknown)}")
        if not query.strip() and not seeds:
            raise ValueError("supply a query or at least one seed ID")
        semantic_provenance = None
        if semantic is not None:
            from .discovery_semantic import SemanticVectors

            vectors = SemanticVectors.load(semantic, self.index.records)
            semantic_scores = (
                vectors.search(query, pool) if query.strip() else vectors.neighbors(seeds, pool)
            )
            semantic_provenance = {
                "model_id": vectors.model_id,
                "revision": vectors.revision,
                "fingerprint": vectors.fingerprint,
                "downloaded": False,
            }
        lexical = self.index.search(query, limit=max(pool, limit)) if query.strip() else []
        exact = self._exact(query) if query.strip() else []
        candidates, lexical_ranking = {}, []
        seed_weights: dict[str, float] = defaultdict(float)
        best_passage: dict[str, dict] = {}
        # A source chunk can map to a document and several scoped statements.
        # Split its restart weight, so richly annotated sources get no free boost.
        for rank, hit in enumerate(lexical, 1):
            linked = [node for node in hit.get("claim_ids", []) if node in self.records]
            hit_key = hit["id"]
            if hit.get("kind") == "record" and len(linked) == 1:
                hit_key = linked[0]
                row = self._record_hit(hit_key)
                row["matching_passage"] = hit
            else:
                row = {**hit, "where": f"{hit['path']}:{hit.get('start_line', 1)}"}
            row["id"] = hit_key
            candidates[hit_key] = row
            lexical_ranking.append(hit_key)
            for node in linked:
                seed_weights[node] += 1 / ((60 + rank) * max(1, len(linked)))
                if hit.get("kind") == "passage":
                    best_passage.setdefault(node, hit)
        for node in exact:
            seed_weights[node] += 0.2
        for node in seeds:
            seed_weights[node] += 1.0
        if semantic_scores:
            for rank, node in enumerate(
                sorted(semantic_scores, key=lambda key: (-semantic_scores[key], key))[:20], 1
            ):
                if node in self.records:
                    seed_weights[node] += 1 / (60 + rank)
        propagation = (
            self.graph.rank(dict(seed_weights), limit=pool, method="push", push_epsilon=1e-6)
            if seed_weights
            else {"scores": {}, "iterations": 0, "converged": True, "method": "push"}
        )
        channels = {"lexical": lexical_ranking, "exact": exact}
        if graph_weight:
            channels["graph"] = list(propagation["scores"])
        if semantic_scores:
            channels["semantic"] = sorted(
                (node for node in semantic_scores if node in self.records),
                key=lambda node: (-semantic_scores[node], node),
            )[:pool]
        fused = reciprocal_rank_fusion(
            channels, {"lexical": 1.0, "exact": 2.5, "graph": graph_weight, "semantic": 1.0}
        )
        # Source passages without registered links must not be penalized for
        # lacking a graph channel. Keep direct matches and associative results
        # in separate bands, as entity/chunk GraphRAG retrieval does.
        primary_channels = {name: ranking for name, ranking in channels.items() if name != "graph"}
        if not query.strip() and seeds:
            primary_channels = channels
        primary_scores = reciprocal_rank_fusion(
            primary_channels, {"lexical": 1.0, "exact": 2.5, "graph": graph_weight, "semantic": 1.0}
        )
        rows = []
        for node, scored in fused.items():
            row = candidates.get(node)
            if row is None and node in self.records:
                row = self._record_hit(node)
            if row is None:
                continue
            row = {**row, "score": scored["score"], "score_channels": scored["channels"]}
            if node in best_passage:
                row["matching_passage"] = best_passage[node]
            rows.append(row)
        rows_by_id = {row["id"]: row for row in rows}
        primary_rows = [
            {**rows_by_id[node], "score": score["score"], "score_channels": score["channels"]}
            for node, score in primary_scores.items()
            if node in rows_by_id
        ]
        hits = _select_diverse(primary_rows, limit)
        selected = {row["id"] for row in hits}
        related = (
            _select_diverse(
                [
                    row
                    for row in rows
                    if "graph" in row["score_channels"] and row["id"] not in selected
                ],
                related_limit,
            )
            if related_limit
            else []
        )
        explain_seeds = (
            seeds
            or exact[:3]
            or list(sorted(seed_weights, key=lambda node: (-seed_weights[node], node))[:3])
        )
        for hit in hits + related:
            node = hit["id"]
            hit["discovery_only"] = True
            if node in self.records:
                hit["commands"] = {
                    "why": ["workhouse", "why", node],
                    "brief": ["workhouse", "brief", node, "--json"],
                }
                if "graph" in hit["score_channels"]:
                    for seed in explain_seeds:
                        if seed != node:
                            witness = self.graph.paths(seed, node, limit=1, max_depth=3)
                            if witness["paths"]:
                                hit["graph_witness"] = {"seed": seed, **witness}
                                break
        metadata = self.index.metadata()
        return {
            "schema": SCHEMA,
            "query": query,
            "seeds": seeds,
            "hits": hits,
            "related": related,
            "provenance": metadata,
            "retrieval": {
                "channels": list(channels),
                "fusion": "weighted reciprocal rank fusion; k=60",
                "selection": "direct source matches and related graph candidates ranked separately",
                "related_limit": related_limit,
                "graph_weight": graph_weight,
                "graph_method": propagation.get("method"),
                "graph_iterations": propagation.get("iterations"),
                "graph_converged": propagation.get("converged"),
                "graph_residual": propagation.get("residual"),
                "graph_residual_meaning": propagation.get("residual_meaning"),
                "graph_tolerance": propagation.get("tolerance", 1e-6),
                "semantic": semantic_provenance,
                "candidate_pool": pool,
                "source_diversity": "two per source before filling unused slots",
                "saved_graph_freshness": "not assessed; retain workhouse brief for scientific use",
            },
            "meaning": "Discovery candidates; relevance is not proof or independent support. "
            "Recorded status, evidence and tier are preserved. Read sources and retain a briefing.",
            "execution": {"python_checks": 0, "lean": False, "scientific_index_written": False},
        }

    def connections(self, node: str, *, query: str = "", limit: int = 10) -> dict:
        if node not in self.records:
            raise ValueError(f"unknown graph ID: {node}")
        query = query or self.records[node].get("statement", "")
        search = self.search(query, limit=100, seeds=[node], pool=250, related_limit=100)
        candidates = list(
            dict.fromkeys(
                candidate
                for hit in search["hits"] + search["related"]
                for candidate in hit.get("claim_ids", [])
                if candidate != node and candidate in self.records
            )
        )
        linked = self.graph.neighbors(node)
        new_candidates = [candidate for candidate in candidates if candidate not in linked]
        # Shared witnesses are cheap for every candidate; bounded path searches
        # are not, so they run only for the rows an agent will actually read.
        explained = self.graph.connections(
            node, new_candidates, limit=len(new_candidates), paths_limit=0
        )
        by_id = {row["id"]: row for row in explained}
        structural = [row["id"] for row in explained if row.get("score", 0) > 0]
        fused = reciprocal_rank_fusion(
            {"retrieval": new_candidates, "shared_witnesses": structural},
            {"retrieval": 1.0, "shared_witnesses": 0.5},
        )
        ordered = []
        for target, score in fused.items():
            candidate = by_id[target]
            candidate["connection_rank"] = score
            candidate["where"] = self.records[target].get("where", "")
            ordered.append(candidate)
        connections = _select_diverse(ordered, limit)
        for row in connections:
            row.update(self.graph.explain_path(node, row["id"]))
        # Keep a slot for a content-related node outside the explored topology:
        # inspect a bounded number of further candidates for one without a path.
        if limit > 1 and all(row.get("path") for row in connections):
            selected_ids = {row["id"] for row in connections}
            budget = 10
            for row in ordered:
                if row["id"] in selected_ids or budget == 0:
                    continue
                budget -= 1
                row.update(self.graph.explain_path(node, row["id"]))
                if not row["path"]:
                    connections[-1] = row
                    break
        rankings = {}
        for hit in search["hits"] + search["related"]:
            for target in [hit["id"], *hit.get("claim_ids", [])]:
                previous = rankings.get(target)
                if previous is None or (
                    hit.get("kind") == "passage" and previous.get("kind") != "passage"
                ):
                    rankings[target] = hit
        for candidate in connections:
            target = candidate["id"]
            candidate["record"] = self.records[target]
            hit = rankings.get(target, {})
            candidate["retrieval"] = hit.get("score_channels", {})
            passage = hit.get("matching_passage") or (hit if hit.get("kind") == "passage" else None)
            if passage:
                candidate["matching_passage"] = passage
            candidate["retrieval_witness"] = {
                "hit_id": hit.get("id"),
                "query": query,
                "channels": hit.get("score_channels", {}),
            }
            candidate["review_required"] = [
                "Compare the exact objects, hypotheses, regime and normalizations.",
                "Read each cited argument and distinguish copied sources from independent origins.",
                "Register a mathematical relationship only after reviewing its implication.",
            ]
        return {
            "schema": "workhouse-discovery/connections/v1",
            "seed": self.records[node],
            "query": query,
            "candidates": connections,
            "already_connected_excluded": len(linked),
            "provenance": search["provenance"],
            "meaning": search["meaning"],
            "execution": search["execution"],
        }


def context_pack(result: dict, max_chars: int = 16000) -> dict:
    """A hard-bounded agent handoff; record every omitted/truncated item."""
    if max_chars < 2000:
        raise ValueError("context budget must be at least 2000 characters")
    provenance = result.get("provenance", {})
    pack = {
        "schema": "workhouse-discovery/context/v1",
        "query": result.get("query", ""),
        "seeds": result.get("seeds", []),
        "meaning": result["meaning"],
        "source_fingerprint": provenance.get("fingerprint"),
        "source_freshness": provenance.get("freshness", "unknown"),
        "current_source_fingerprint": provenance.get("current_fingerprint"),
        "freshness_error": provenance.get("freshness_error"),
        "scientific_graph_freshness": "not assessed; use a retained workhouse brief",
        "execution": result.get("execution", {}),
        "hits": [],
        "omitted": 0,
        "budget": {"max_chars": max_chars, "unit": "serialized JSON characters, not tokens"},
    }

    def encoded():
        return json.dumps(pack, ensure_ascii=True, sort_keys=True)

    combined = [dict(hit, retrieval_group="direct") for hit in result.get("hits", [])]
    combined += [dict(hit, retrieval_group="related") for hit in result.get("related", [])]
    for hit in combined:
        pack["hits"].append(hit)
        if len(encoded()) + 100 > max_chars:
            pack["hits"].pop()
            pack["omitted"] += 1
    if len(encoded()) + 100 > max_chars:
        raise ValueError("query metadata exceeds context budget")
    pack["fingerprint"] = hashlib.sha256(encoded().encode()).hexdigest()
    return pack


def render_text(result: dict) -> str:
    lines = [result["meaning"], ""]
    if "candidates" in result:
        for row in result["candidates"]:
            lines.extend(
                [
                    row["id"],
                    f"  {row['record'].get('statement', '')}",
                    f"  {row['record'].get('where', '')}",
                    f"  shared witnesses: {len(row.get('shared_witnesses', []))}; "
                    f"registered path: {'yes' if row.get('path') else 'not found within bounds'}",
                ]
            )
    else:
        for row in result.get("hits", []) + result.get("related", []):
            if result.get("related") and row is result["related"][0]:
                lines.extend(["", "Related graph candidates (separate from direct matches)"])
            lines.extend(
                [
                    f"{row['score']:.5f}  {row['id']}",
                    f"  {row.get('where', '')}",
                    f"  {row.get('text', '')[:500]}",
                    f"  channels: {', '.join(row.get('score_channels', {}))}",
                ]
            )
    return "\n".join(lines)
