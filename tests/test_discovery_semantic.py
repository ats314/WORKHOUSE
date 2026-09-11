import copy

import pytest

from workhouse import discovery_semantic as S

RECORDS = [{"id": "A", "statement": "energy"}, {"id": "B", "statement": "form"}]


def payload():
    return {
        "schema": S.SCHEMA,
        "model_id": "fixture/model",
        "revision": "a" * 40,
        "record_fingerprint": S.record_fingerprint(RECORDS),
        "dimensions": 2,
        "vectors": {"A": [1.0, 0.0], "B": [0.8, 0.6]},
    }


def test_local_seed_neighbors_need_no_model_library():
    vectors = S.SemanticVectors(payload(), RECORDS)
    assert list(vectors.neighbors(["A"])) == ["A", "B"]
    assert vectors.neighbors(["A"])["B"] == pytest.approx(0.8)


def test_stale_vectors_and_moving_model_revisions_are_rejected():
    changed = copy.deepcopy(RECORDS)
    changed[0]["statement"] = "changed energy hypothesis"
    with pytest.raises(ValueError, match="stale"):
        S.SemanticVectors(payload(), changed)
    bad = payload()
    bad["revision"] = "main"
    with pytest.raises(ValueError, match="commit SHA"):
        S.SemanticVectors(bad, RECORDS)


@pytest.mark.parametrize(
    "vector", [[], [0, 0], [float("nan"), 1], [float("inf"), 1], [True, 1], [1, 2, 3]]
)
def test_invalid_embeddings_fail_closed(vector):
    bad = payload()
    bad["vectors"]["A"] = vector
    with pytest.raises(ValueError):
        S.SemanticVectors(bad, RECORDS)


def test_query_dimensions_and_missing_seeds_are_checked():
    vectors = S.SemanticVectors(payload(), RECORDS)
    with pytest.raises(ValueError):
        vectors.rank([1, 2, 3])
    with pytest.raises(ValueError):
        vectors.neighbors(["missing"])


@pytest.mark.parametrize("bad", [None, [], 1, "text", {**payload(), "revision": None}])
def test_malformed_payload_has_actionable_value_error(bad):
    with pytest.raises(ValueError):
        S.SemanticVectors(bad, RECORDS)
