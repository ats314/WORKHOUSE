"""The originating-document register must stay pinned, quoted, and resolvable.

`ledger/provenance.yaml` asserts judgement — THIS corpus document originates
that claim — and judgement is exactly what must not rot silently. Everything
mechanical about an entry is checked here: the file exists and still hashes to
the corpus pin, every quote is really in the file near the recorded line, and
every target resolves in the claim catalogue. The one thing not checked is the
one thing that cannot be: whether the document is right.
"""

from pathlib import Path

from workhouse import claims as C
from workhouse import graph as G
from workhouse.payloads import corpus_pins, sha256_of

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus-import"

DOCUMENTS = C.load_provenance()
ROLES = {"transcript", "research-note", "notebook", "certificate"}
LINE_WINDOW = 20


def test_schema_is_complete_and_ids_unique():
    ids = [d["id"] for d in DOCUMENTS]
    assert len(set(ids)) == len(ids), "duplicate document ids"
    for doc in DOCUMENTS:
        assert doc["role"] in ROLES, f"{doc['id']}: unknown role {doc['role']!r}"
        assert str(doc.get("meaning", "")).strip(), f"{doc['id']}: no meaning"
        assert doc.get("originates"), f"{doc['id']}: originates nothing — not a register entry"
        for origin in doc["originates"]:
            for key in ("target", "what", "quote", "near_line"):
                assert origin.get(key), f"{doc['id']}: originates entry missing {key}"


def test_every_document_hashes_to_its_corpus_pin():
    """A corpus change must break this file loudly, not strand it."""
    if not CORPUS.is_dir():
        return
    pins = corpus_pins()
    for doc in DOCUMENTS:
        pin = pins.get(doc["path"])
        assert pin, f"{doc['id']}: {doc['path']} is not pinned in corpus-import/SHA256SUMS"
        assert doc["sha256"] == pin, f"{doc['id']}: recorded sha != corpus pin"
        actual = sha256_of(CORPUS / doc["path"])
        assert actual == pin, f"{doc['id']}: file on disk does not hash to the pin"


def test_every_quote_is_observed_near_its_line():
    """Quotes are observed, not invented — same discipline as corpus_spellings."""
    if not CORPUS.is_dir():
        return
    for doc in DOCUMENTS:
        lines = (CORPUS / doc["path"]).read_text(errors="replace").splitlines()
        for origin in doc["originates"]:
            quote, near = origin["quote"], int(origin["near_line"])
            hits = [i + 1 for i, line in enumerate(lines) if quote in line]
            assert hits, f"{doc['id']}: quote {quote!r} not found in {doc['path']}"
            assert any(abs(hit - near) <= LINE_WINDOW for hit in hits), (
                f"{doc['id']}: quote {quote!r} found at {hits}, none within "
                f"{LINE_WINDOW} lines of {near}"
            )


def test_every_target_resolves_and_the_graph_carries_the_edges():
    catalogue = C.collect()
    nodes = {c.id for c in catalogue}
    wanted = {
        (f"DOC:{doc['id']}", origin["target"]) for doc in DOCUMENTS for origin in doc["originates"]
    }
    for _src, target in wanted:
        assert target in nodes, f"unresolved originates target {target!r}"
    doc_ids = {c.id for c in catalogue if c.kind == "document"}
    assert doc_ids == {f"DOC:{d['id']}" for d in DOCUMENTS}
    graph = G.build(catalogue)
    have = {(e.src, e.dst) for e in graph.edges if e.type == "originates"}
    assert have == wanted, f"graph originates edges {have} != register {wanted}"
