"""Bounded retrieval over registered edges; no inferred scientific edges.

Personalized PageRank and shared-neighbor scores are discovery heuristics, not
proof probabilities. Exploratory walks can follow edges in either direction;
dependency walks only follow ``depends_on`` and ``rests_on`` as recorded. The
original edge dictionaries accompany every path step. This module imports no
collector, executes no checks, and never changes catalogue records.
"""

from __future__ import annotations

import json
import math
import re
from collections import defaultdict, deque
from copy import deepcopy
from typing import Any

DEPENDENCY_TYPES = frozenset({"depends_on", "rests_on"})

# These are retrieval weights, deliberately unrelated to scientific tiers.
# Navigation must not outweigh an actual registered dependency or proof link.
RELATION_WEIGHTS = {
    "depends_on": 1.0,
    "rests_on": 1.0,
    "formalizes": 0.95,
    "promotes": 0.85,
    "supported_by": 0.75,
    "evidences": 0.65,
    "yields": 0.7,
    "uses": 0.6,
    "bears_on": 0.5,
    "closed_by": 0.7,
    "targets": 0.5,
    "blocked_by": 0.5,
    "cannot_decide": 0.4,
    "resolves": 0.5,
    "unblocks": 0.5,
    "blocks": 0.4,
    "plans": 0.4,
    "claims": 0.4,
    "code_names": 0.4,
    "carries": 0.3,
    "originates": 0.3,
    "pinned_as": 0.2,
    "duplicate_of": 0.15,
    "superseded_by": 0.15,
    "amends": 0.15,
    "retracts": 0.15,
    "contradictions": 0.1,
    "gaps": 0.1,
    "technical_appendix": 0.1,
    "provenance": 0.08,
    "cites": 0.06,
    "labels": 0.05,
    "contains": 0.03,
    "navigation": 0.02,
    "mentions": 0.01,
}


def relationship_class(type_: str) -> str:
    """Retrieval role, never a replacement for the edge's recorded type."""
    if type_ in DEPENDENCY_TYPES:
        return "dependency"
    if type_ in {"formalizes", "promotes"}:
        return "formal_coverage"
    if type_ == "supported_by":
        return "scoped_support"
    if type_ in {"evidences", "yields", "uses", "carries"}:
        return "evidence"
    if type_ in {"cites", "contains", "pinned_as", "originates", "provenance"}:
        return "source"
    if type_ in {"plans", "targets", "blocked_by", "closed_by", "cannot_decide"}:
        return "route"
    return "navigation" if type_ in RELATION_WEIGHTS else "unknown"


def _nonnegative_int(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


class GraphDiscovery:
    """Index a saved catalogue once for deterministic, bounded discovery.

    Invalid endpoints are reported in ``diagnostics`` and excluded rather than
    invented. Duplicate edge records and parallel provenance copies do not
    multiply PageRank weight. Archive membership edges are retained for direct
    relationship reporting but excluded from exploratory traversal.
    """

    def __init__(self, records: list[dict], edges: list[dict]) -> None:
        self.records: dict[str, dict] = {}
        for record in records:
            id_ = record.get("id")
            if not isinstance(id_, str) or not id_:
                raise ValueError("every catalogue record needs a nonempty string id")
            if id_ in self.records:
                raise ValueError(f"duplicate catalogue id: {id_}")
            self.records[id_] = deepcopy(record)
        self.records = dict(sorted(self.records.items()))
        self._adj: dict[str, list[tuple[str, int, str, float]]] = defaultdict(list)
        self._dependencies: dict[str, list[tuple[str, int, str, float]]] = defaultdict(list)
        self._dependents: dict[str, list[tuple[str, int, str, float]]] = defaultdict(list)
        self._direct: dict[tuple[str, str], list[int]] = defaultdict(list)
        self._weights: dict[str, dict[str, float]] = defaultdict(dict)
        self.edges: list[dict] = []
        dangling: list[dict] = []
        malformed: list[dict] = []
        archive_edges = 0
        serialized = sorted({json.dumps(e, sort_keys=True) for e in edges})
        for encoded in serialized:
            edge = json.loads(encoded)
            if any(
                not isinstance(edge.get(key), str) or not edge[key]
                for key in ("src", "dst", "type", "how", "source")
            ) or edge["how"] not in {"curated", "derived"}:
                malformed.append(edge)
                continue
            src, dst = edge["src"], edge["dst"]
            if src not in self.records or dst not in self.records:
                dangling.append(edge)
                continue
            index = len(self.edges)
            self.edges.append(edge)
            self._direct[(src, dst)].append(index)
            if src != dst:
                self._direct[(dst, src)].append(index)
            weight = RELATION_WEIGHTS.get(edge["type"], 0.01)
            if edge["how"] == "derived" and edge["type"] not in DEPENDENCY_TYPES:
                weight *= 0.5
            if edge["type"] in DEPENDENCY_TYPES:
                self._dependencies[src].append((dst, index, "forward", weight))
                self._dependents[dst].append((src, index, "reverse", weight))
            if edge["type"] == "contains" and (
                src.startswith("ARCHIVE:") or self.records[src].get("kind") == "archive"
            ):
                archive_edges += 1
                continue
            for start, end, direction in ((src, dst, "forward"), (dst, src, "reverse")):
                if direction == "reverse" and src == dst:
                    continue
                self._adj[start].append((end, index, direction, weight))
                # Copied provenance records are not independent evidence.
                self._weights[start][end] = max(self._weights[start].get(end, 0.0), weight)
        for adjacency in (self._adj, self._dependencies, self._dependents):
            for node, entries in adjacency.items():
                entries.sort(key=lambda item: (-item[3], item[0], item[1], item[2]))
                # A different copy of the same provenance is not another route.
                # Keep its original edge available through existing_relations.
                seen_steps: set[tuple[str, str, str]] = set()
                distinct = []
                for item in entries:
                    key = (item[0], self.edges[item[1]]["type"], item[2])
                    if key not in seen_steps:
                        seen_steps.add(key)
                        distinct.append(item)
                adjacency[node] = distinct
        self._transitions: dict[str, tuple[tuple[str, float], ...]] = {}
        for src, neighbors in self._weights.items():
            corrected = {
                dst: weight / math.sqrt(max(1, len(self._weights.get(dst, {}))))
                for dst, weight in sorted(neighbors.items())
            }
            total = math.fsum(corrected.values())
            self._transitions[src] = tuple(
                (dst, weight / total) for dst, weight in corrected.items()
            )
        self.diagnostics = {
            "nodes": len(self.records),
            "registered_edges": len(self.edges),
            "duplicate_edges_ignored": len(edges) - len(serialized),
            "archive_membership_edges_excluded": archive_edges,
            "dangling_edges": dangling,
            "malformed_edges": malformed,
        }

    def rank(
        self,
        seeds: dict[str, float],
        *,
        limit: int = 100,
        alpha: float = 0.85,
        max_iterations: int = 60,
        tolerance: float = 1e-8,
    ) -> dict[str, Any]:
        """Weighted personalized PageRank with seed-directed dangling mass.

        Destination degree correction reduces hub attraction. ``scores`` contains
        the top positive scores, without renormalizing after ``limit``; omitted
        score mass is reported. Convergence uses the absolute L1 residual.
        """
        _nonnegative_int(limit, "limit")
        _nonnegative_int(max_iterations, "max_iterations")
        if max_iterations == 0:
            raise ValueError("max_iterations must be positive")
        if not math.isfinite(alpha) or not 0 <= alpha < 1:
            raise ValueError("alpha must be finite and in [0, 1)")
        if not math.isfinite(tolerance) or tolerance <= 0:
            raise ValueError("tolerance must be finite and positive")
        if any(not math.isfinite(v) or v < 0 for v in seeds.values()):
            raise ValueError("seed weights must be finite and nonnegative")
        known = {
            key: float(value)
            for key, value in sorted(seeds.items())
            if key in self.records and value > 0
        }
        unknown = sorted(key for key in seeds if key not in self.records)
        # Scale before summation so large but finite inputs do not overflow.
        scale = max(known.values(), default=1.0)
        total = math.fsum(value / scale for value in known.values())
        personalization = {key: (value / scale) / total for key, value in known.items()}
        scores = dict(personalization)
        iterations, residual, converged = 0, 0.0, not bool(scores)
        for iteration in range(1, max_iterations + 1) if scores else ():
            dangling = math.fsum(
                value for node, value in scores.items() if node not in self._transitions
            )
            restart = 1 - alpha + alpha * dangling
            updated = {node: restart * weight for node, weight in personalization.items()}
            for node in sorted(scores):
                mass = alpha * scores[node]
                for neighbor, probability in self._transitions.get(node, ()):
                    updated[neighbor] = updated.get(neighbor, 0.0) + mass * probability
            residual = math.fsum(
                abs(updated.get(node, 0.0) - scores.get(node, 0.0))
                for node in sorted(updated.keys() | scores.keys())
            )
            scores, iterations = updated, iteration
            if residual <= tolerance:
                converged = True
                break
        ordered = sorted(
            ((node, value) for node, value in scores.items() if value > 0),
            key=lambda item: (-item[1], item[0]),
        )
        selected = dict(ordered[:limit])
        return {
            "scores": selected,
            "iterations": iterations,
            "converged": converged,
            "residual": residual,
            "alpha": alpha,
            "tolerance": tolerance,
            "seed_weights": personalization,
            "unknown_seeds": unknown,
            "total_score_mass": math.fsum(scores.values()),
            "returned_score_mass": math.fsum(selected.values()),
            "scored_nodes": len(ordered),
            "candidate_only": True,
            "semantics": "bidirectional retrieval relevance, not mathematical implication",
        }

    def _step(self, src: str, item: tuple[str, int, str, float]) -> dict:
        dst, index, direction, _weight = item
        edge = self.edges[index]
        return {
            "edge": deepcopy(edge),
            "direction": direction,
            "from": src,
            "to": dst,
            "relationship_class": relationship_class(edge["type"]),
        }

    def paths(
        self,
        src: str,
        dst: str,
        *,
        max_depth: int = 4,
        limit: int = 3,
        max_visits: int = 5000,
        dependency_only: bool = False,
    ) -> dict[str, Any]:
        """Return deterministic shortest-first simple paths under explicit caps.

        A visit is an examined adjacency entry, including rejected cycles.
        ``truncated`` says a depth, output or visit cap stopped exploration; it
        does not assert that another valid path exists. Dependency paths follow
        recorded direction only; exploratory paths label reverse traversals.
        """
        for name, value in (("max_depth", max_depth), ("limit", limit), ("max_visits", max_visits)):
            _nonnegative_int(value, name)
        unknown = sorted({node for node in (src, dst) if node not in self.records})
        result: dict[str, Any] = {
            "source": src,
            "target": dst,
            "paths": [],
            "visits": 0,
            "truncated": False,
            "truncation_reasons": [],
            "unknown_nodes": unknown,
            "mode": "recorded_dependencies" if dependency_only else "exploratory",
            "candidate_only": not dependency_only,
            "semantics": (
                "registered dependency chain; hypotheses and scopes still require review"
                if dependency_only
                else "retrieval path, not a mathematical dependency"
            ),
        }
        if unknown:
            return result
        adjacency = self._dependencies if dependency_only else self._adj
        reasons: set[str] = set()
        if limit == 0:
            result.update(truncated=True, truncation_reasons=["limit"])
            return result
        if src == dst:
            result["paths"] = [[]]
            return result
        queue = deque([(src, [], frozenset({src}))])
        stop = False
        while queue and not stop:
            node, trail, seen = queue.popleft()
            entries = adjacency.get(node, ())
            if len(trail) >= max_depth:
                if entries:
                    reasons.add("max_depth")
                continue
            for item in entries:
                if result["visits"] >= max_visits:
                    reasons.add("max_visits")
                    stop = True
                    break
                result["visits"] += 1
                nxt = item[0]
                if nxt in seen:
                    continue
                next_trail = [*trail, self._step(node, item)]
                if nxt == dst:
                    result["paths"].append(next_trail)
                    if len(result["paths"]) >= limit:
                        reasons.add("limit")
                        stop = True
                        break
                else:
                    queue.append((nxt, next_trail, seen | {nxt}))
        result["truncated"] = bool(reasons)
        result["truncation_reasons"] = sorted(reasons)
        return result

    def dependency_impact(
        self,
        node_id: str,
        *,
        direction: str = "downstream",
        max_depth: int = 8,
        limit: int = 100,
        max_visits: int = 5000,
    ) -> dict[str, Any]:
        """Find recorded dependents or prerequisites, retaining edge direction.

        Downstream impact traverses dependency edges in reverse to find records
        that use this input. It does not infer that every dependent is invalid
        when an input changes, or that alternative route inputs are cumulative.
        """
        if direction not in {"downstream", "upstream"}:
            raise ValueError("direction must be downstream or upstream")
        for name, value in (("max_depth", max_depth), ("limit", limit), ("max_visits", max_visits)):
            _nonnegative_int(value, name)
        result: dict[str, Any] = {
            "source": node_id,
            "direction": direction,
            "nodes": [],
            "visits": 0,
            "truncated": False,
            "truncation_reasons": [],
            "unknown_nodes": [] if node_id in self.records else [node_id],
            "semantics": (
                "recorded dependency impact requiring scope review, not inferred invalidity"
            ),
        }
        if result["unknown_nodes"]:
            return result
        adjacency = self._dependents if direction == "downstream" else self._dependencies
        queue = deque([(node_id, [])])
        seen = {node_id}
        reasons: set[str] = set()
        stop = False
        if limit == 0:
            result.update(truncated=True, truncation_reasons=["limit"])
            return result
        while queue and not stop:
            node, trail = queue.popleft()
            entries = adjacency.get(node, ())
            if len(trail) >= max_depth:
                if entries:
                    reasons.add("max_depth")
                continue
            for item in entries:
                if result["visits"] >= max_visits:
                    reasons.add("max_visits")
                    stop = True
                    break
                result["visits"] += 1
                nxt = item[0]
                if nxt in seen:
                    continue
                seen.add(nxt)
                path = [*trail, self._step(node, item)]
                result["nodes"].append({"id": nxt, "depth": len(path), "path": path})
                if len(result["nodes"]) >= limit:
                    reasons.add("limit")
                    stop = True
                    break
                queue.append((nxt, path))
        result["truncated"] = bool(reasons)
        result["truncation_reasons"] = sorted(reasons)
        return result

    def _source_families(self, node_id: str) -> list[str]:
        record = self.records[node_id]
        declared = record.get("source_family")
        families = {f"declared:{declared}"} if isinstance(declared, str) and declared else set()

        def add_location(item: dict) -> None:
            where = item.get("where")
            if isinstance(where, str) and where:
                # Strip recognized locator suffixes after a file extension.
                # A literal '# transcript.txt' or 'report (2).md' is a filename.
                extensions = r"(?:md|tex|txt|py|lean|yaml|yml|jsonl?)"
                marker = r"(?:#+\s|lines?\s+\d|(?:lemma|theorem|proposition|corollary|section)\b)"
                location = re.sub(
                    rf"^(.+\.{extensions})\s+\({marker}[\s\S]*$",
                    r"\1",
                    where,
                    flags=re.IGNORECASE,
                )
                location = re.sub(rf"^(.+\.{extensions})#[^\r\n]*$", r"\1", location)
                location = re.sub(r":\d+(?::\d+)?$", "", location)
                families.add("path:" + location.replace("\\", "/"))

        add_location(record)
        for neighbor, index, direction, _weight in self._adj.get(node_id, ()):
            type_ = self.edges[index]["type"]
            if (
                (type_ == "cites" and direction == "forward")
                or type_ == "pinned_as"
                or (type_ == "originates" and direction == "reverse")
            ):
                families.add("source:" + neighbor)
                add_location(self.records[neighbor])
        return sorted(families)

    def connections(
        self,
        node_id: str,
        candidates: list[str],
        *,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Explain candidate pairs using shared witnesses and bounded paths.

        Shared-neighbor resource allocation favors specific witnesses over hubs.
        Source-family overlap is a provenance-navigation hint, never a count of
        independent computations. Unknown candidate IDs are omitted; no candidate
        is inserted into the registered graph or promoted to a scientific edge.
        """
        _nonnegative_int(limit, "limit")
        if node_id not in self.records or limit == 0:
            return []
        neighbors = self._weights.get(node_id, {})
        source_families = self._source_families(node_id)
        output: list[dict[str, Any]] = []
        for target in sorted(set(candidates) - {node_id}):
            if target not in self.records:
                continue
            other = self._weights.get(target, {})
            witnesses = []
            for witness in sorted((neighbors.keys() & other.keys()) - {node_id, target}):
                contribution = min(neighbors[witness], other[witness]) / max(
                    1, len(self._weights.get(witness, {}))
                )
                left = next(item for item in self._adj[node_id] if item[0] == witness)
                right = next(item for item in self._adj[target] if item[0] == witness)
                witnesses.append(
                    {
                        "id": witness,
                        "score": contribution,
                        "degree": len(self._weights.get(witness, {})),
                        "source_step": self._step(node_id, left),
                        "target_step": self._step(target, right),
                    }
                )
            witnesses.sort(key=lambda item: (-item["score"], item["id"]))
            existing = [
                deepcopy(self.edges[index]) for index in self._direct.get((node_id, target), ())
            ]
            target_families = self._source_families(target)
            shared_families = sorted(set(source_families) & set(target_families))
            output.append(
                {
                    "id": target,
                    "candidate_only": True,
                    "score": math.fsum(item["score"] for item in witnesses),
                    "shared_witnesses": witnesses[:8],
                    "shared_witness_count": len(witnesses),
                    "existing_relations": existing,
                    "has_registered_relation": bool(existing),
                    "source_family": {
                        "source": source_families,
                        "target": target_families,
                        "shared": shared_families,
                        "comparison": "overlap"
                        if shared_families
                        else (
                            "no_recorded_overlap"
                            if source_families and target_families
                            else "unknown"
                        ),
                        "semantics": "source locator comparison; not independent evidence",
                    },
                    "semantics": "connection candidate for source review; no new registered edge",
                }
            )
        output.sort(key=lambda item: (-item["score"], item["id"]))
        for item in output[:limit]:
            paths = self.paths(node_id, item["id"], limit=1, max_visits=1000)
            item["path"] = paths["paths"][0] if paths["paths"] else []
            item["path_found"] = bool(paths["paths"])
            item["path_truncated"] = paths["truncated"]
            item["path_truncation_reasons"] = paths["truncation_reasons"]
        return output[:limit]
