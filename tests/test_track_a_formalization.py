"""Keep corrected Track A proofs scoped and their rejected drafts recoverable."""

import json
from hashlib import sha256

from workhouse import derivation_statements as D


def test_received_track_a_sources_keep_their_exact_bytes():
    run = D.ROOT / "runs/track_a_formalization_2026-09-09"
    manifest = json.loads((run / "source_manifest.json").read_text(encoding="utf-8"))
    assert manifest["files"]
    for row in manifest["files"]:
        path = (run / row["snapshot_path"]).resolve()
        assert path.is_relative_to(run.resolve())
        assert sha256(path.read_bytes()).hexdigest() == row["sha256"]


def test_abstract_track_a_proofs_do_not_close_the_wilson_realization():
    statements = {s["id"]: s for d in D.load()["documents"] for s in d["statements"]}
    w6 = statements["DERIV:WILSON_SELECTED_INVERSE_WALL:W6"]
    sc17 = statements["DERIV:WILSON_SC17_SPATIAL_CLOSURE:R4_R9"]
    assert w6["status"] == "open" and not w6["lean"]
    assert sc17["status"] == "conditional" and not sc17["lean"]
    assert "factored_w6_bound" in {x["name"] for x in w6["lean_support"]}
    assert "continuous_riccati_barrier" in {x["name"] for x in sc17["lean_support"]}
    # A later full realization should deliberately update this scope guard,
    # not silently turn the same abstract proof into the physical theorem.
    new = {k: v for k, v in statements.items() if k.startswith("DERIV:TRACK_A_SUPPORTED:")}
    assert new and all(row["lean"] for row in new.values())
    assert all(not set(row["depends_on"]) & {w6["id"], sc17["id"]} for row in new.values())
