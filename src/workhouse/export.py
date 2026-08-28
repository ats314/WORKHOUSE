"""``workhouse export``: the whole graph as one versioned JSON envelope.

The agent experience notes recommend feeding this repository's deterministic
graph into external semantic projections (the registered ``research-map``
service among them) rather than letting those systems re-derive relationships
from prose. That ingestion needs a stable contract, not a scrape of
``index/*.jsonl`` — so this emits one self-describing object carrying the
claims, symbols, and edges together with the fields the notes name as
non-negotiable to preserve: ``how`` (curated vs derived), evidence tier,
lifecycle status, and the reproduce command that routes final inspection back
through executable verification.

The envelope promotes nothing: every record keeps the tier and status the
repository computed, and consumers are expected to route claim adjudication
back through ``workhouse why`` and ``workhouse verify``, exactly as the notes
prescribe.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import asdict
from pathlib import Path

from . import claims as claims_mod
from . import graph as graph_mod

#: Bump on any change to the envelope's shape. Consumers pin against this,
#: not against the repository layout.
SCHEMA_VERSION = "1.0.0"

ROOT = Path(__file__).resolve().parents[2]


def _commit() -> str | None:
    """The checkout this envelope was generated from, when git is available.

    Advisory metadata only — the envelope's content is fully determined by the
    working tree, and a consumer must not treat the hash as a content pin.
    """
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except OSError:
        return None
    sha = out.stdout.strip()
    return sha if out.returncode == 0 and len(sha) == 40 else None


def build() -> dict:
    catalogue = claims_mod.collect()
    symbols = claims_mod.load_symbols()
    graph = graph_mod.build(catalogue, symbols)
    return {
        "schema_version": SCHEMA_VERSION,
        "generator": "workhouse export",
        "generated_from_commit": _commit(),
        "tier_vocabulary": {
            "0": "proved: Lean 4 compiles it, no sorry, standard axioms only",
            "1": "derived: re-derived symbolically from stated definitions, exactly",
            "2": "numerical: float agreement within a stated tolerance",
            "3": "asserted: a document says so and nothing checks it",
        },
        "edge_how_vocabulary": {
            "curated": "read from a field someone wrote",
            "derived": "parsed out of free text this repository also wrote",
        },
        "claims": [asdict(c) for c in catalogue],
        "symbols": symbols,
        "edges": [asdict(e) for e in graph.edges],
    }


def render() -> str:
    return json.dumps(build(), sort_keys=True, ensure_ascii=False, indent=1) + "\n"
