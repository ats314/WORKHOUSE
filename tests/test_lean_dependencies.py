"""Dependency records must agree with elaborated constants and pinned sources."""

from copy import deepcopy
from hashlib import sha256

import pytest
import yaml

from workhouse import derivation_statements as S
from workhouse import lean_dependencies as D


@pytest.fixture
def kernel_export(tmp_path):
    lean = tmp_path / "lean"
    (lean / "Workhouse").mkdir(parents=True)
    (lean / "Workhouse.lean").write_text("import Workhouse.Example\n", encoding="utf-8")
    (lean / "Workhouse/Example.lean").write_text("-- fixture proof sources\n", encoding="utf-8")
    (tmp_path / "ledger").mkdir()
    (tmp_path / "ledger/theorems.yaml").write_text(
        yaml.safe_dump(
            {
                "theorems": [{"name": "base"}, {"name": "derived"}],
            }
        ),
        encoding="utf-8",
    )

    def declaration(kind, *, types=(), proof=(), axioms=()):
        return dict(
            kind=kind,
            type_dependencies=list(types),
            proof_dependencies=list(proof),
            axioms=list(axioms),
        )

    data = dict(
        schema="lean-kernel-dependencies/v1",
        source_hash_mode=D.SOURCE_HASH_MODE,
        source_sha256=D.source_hashes(tmp_path),
        theorems={
            "base": dict(qualified_name="Workhouse.base", project_dependencies=[]),
            "derived": dict(qualified_name="Workhouse.derived", project_dependencies=["base"]),
        },
        declarations={
            "Workhouse.base": declaration("theorem", proof=["Eq.refl"], axioms=["propext"]),
            "Workhouse.helper": declaration(
                "definition", proof=["Workhouse.base"], axioms=["propext"]
            ),
            "Workhouse.derived": declaration(
                "theorem", proof=["Workhouse.helper"], axioms=["propext"]
            ),
        },
    )
    return tmp_path, data


def test_kernel_dependencies_follow_helpers_and_stop_at_registered_theorems(kernel_export):
    root, data = kernel_export
    assert D.validate(data, root) == []
    (edge,) = D.edge_records(data)
    assert (edge["src"], edge["dst"], edge["type"], edge["how"]) == (
        "LEAN:derived",
        "LEAN:base",
        "depends_on",
        "derived",
    )
    assert edge["source"].endswith("#Workhouse.derived")


def test_changed_source_invalidates_an_otherwise_valid_export(kernel_export):
    root, data = kernel_export
    (root / "lean/Workhouse/Example.lean").write_text("-- changed proof\n", encoding="utf-8")
    assert any("export is stale" in e for e in D.validate(data, root))


@pytest.mark.parametrize("ending", ["\n", "\r\n", "\r"])
def test_lean_fingerprints_ignore_only_checkout_line_ending_normalization(kernel_export, ending):
    root, data = kernel_export
    sources = {
        "Workhouse.lean": "import Workhouse.Example\n-- entry point\n",
        "Workhouse/Example.lean": (
            "namespace Workhouse\ntheorem sample : 1 = 1 := rfl\nend Workhouse\n"
        ),
        "ProofDependencies.lean": "import Workhouse\n-- extractor\n",
        "lean-toolchain": "leanprover/lean4:v4.24.0\n",
        "lake-manifest.json": '{\n  "packages": []\n}\n',
        "lakefile.toml": 'name = "workhouse"\nversion = "0.1.0"\n',
    }
    for relative, text in sources.items():
        (root / "lean" / relative).write_bytes(text.encode("utf-8"))
    data["source_sha256"] = D.source_hashes(root)
    for relative, text in sources.items():
        (root / "lean" / relative).write_bytes(text.replace("\n", ending).encode("utf-8"))
    assert D.validate(data, root) == []
    changed = sources["Workhouse/Example.lean"].replace("1 = 1", "1 = 2")
    (root / "lean/Workhouse/Example.lean").write_bytes(
        changed.replace("\n", ending).encode("utf-8")
    )
    assert any("export is stale" in error for error in D.validate(data, root))


@pytest.mark.parametrize("mode", [None, "raw-bytes", "unknown"])
def test_lean_hash_normalization_mode_is_explicit(kernel_export, mode):
    root, data = kernel_export
    data["source_hash_mode"] = mode
    assert any("hash mode must be utf8-lf" in error for error in D.validate(data, root))


def test_derivation_fingerprints_remain_exact_bytes_including_line_endings(tmp_path):
    source = tmp_path / "docs/derivations/example.md"
    source.parent.mkdir(parents=True)
    original = b"# Source\nA follows from H.\n"
    source.write_bytes(original)
    row = dict(
        id="DERIV:EXAMPLE:A",
        statement="A under H",
        locator="Source",
        anchor="# Source",
        status="proven",
        evidence="analytic",
        hypotheses=["H"],
        depends_on=[],
        lean=[],
        remaining="Construct the actual operator.",
    )
    data = dict(
        schema="derivation-statements/v1",
        documents=[
            dict(
                id="CITE:EXAMPLE",
                path="docs/derivations/example.md",
                sha256=sha256(original).hexdigest(),
                statements=[row],
            )
        ],
    )
    assert S.validate(data, root=tmp_path) == []
    source.write_bytes(original.replace(b"\n", b"\r\n"))
    assert any("SHA-256 mismatch" in error for error in S.validate(data, root=tmp_path))


def test_nonstandard_axiom_cannot_be_called_a_kernel_certificate(kernel_export):
    root, data = kernel_export
    data["declarations"]["Workhouse.derived"]["axioms"].append("sorryAx")
    assert any("nonstandard axioms" in e and "sorryAx" in e for e in D.validate(data, root))


def test_missing_or_non_theorem_kernel_entry_cannot_match_the_registry(kernel_export):
    root, data = kernel_export
    del data["declarations"]["Workhouse.derived"]
    assert any("missing from elaborated environment" in e for e in D.validate(data, root))
    data["declarations"]["Workhouse.derived"] = dict(
        kind="definition",
        type_dependencies=[],
        proof_dependencies=[],
        axioms=[],
    )
    assert any("missing from elaborated environment" in e for e in D.validate(data, root))


def test_registered_name_cannot_be_redirected_to_a_different_theorem(kernel_export):
    root, data = kernel_export
    data["theorems"]["derived"]["qualified_name"] = "Workhouse.base"
    assert any("does not match registered name" in e for e in D.validate(data, root))


@pytest.mark.parametrize("dependencies", [[], ["derived"], ["base", "base"], "base"])
def test_project_dependency_summary_cannot_disagree_with_proof_constants(
    kernel_export,
    dependencies,
):
    root, data = kernel_export
    data["theorems"]["derived"]["project_dependencies"] = dependencies
    assert D.validate(data, root)


def test_spurious_but_registered_dependency_is_rejected(kernel_export):
    root, data = kernel_export
    data["theorems"]["base"]["project_dependencies"] = ["derived"]
    assert any("disagree with elaborated constants" in e for e in D.validate(data, root))


def test_type_dependencies_are_included_in_the_extraction(kernel_export):
    root, data = kernel_export
    record = data["declarations"]["Workhouse.derived"]
    record["proof_dependencies"] = []
    record["type_dependencies"] = ["Workhouse.helper"]
    assert D.validate(data, root) == []
    data["theorems"]["derived"]["project_dependencies"] = []
    assert any("disagree with elaborated constants" in e for e in D.validate(data, root))


def test_missing_local_helper_and_omitted_transitive_axioms_are_rejected(kernel_export):
    root, data = kernel_export
    missing = deepcopy(data)
    del missing["declarations"]["Workhouse.helper"]
    assert any("local kernel dependency missing" in e for e in D.validate(missing, root))
    data["declarations"]["Workhouse.derived"]["axioms"] = []
    assert any("omits local dependency axioms" in e for e in D.validate(data, root))


def test_recursive_definitions_are_allowed_but_cyclic_theorems_are_not(kernel_export):
    root, data = kernel_export
    data["declarations"]["Workhouse.helper"]["proof_dependencies"].append("Workhouse.helper")
    assert D.validate(data, root) == []
    data["declarations"]["Workhouse.base"]["proof_dependencies"] = ["Workhouse.derived"]
    data["theorems"]["base"]["project_dependencies"] = ["derived"]
    assert any("circular registered" in e for e in D.validate(data, root))


@pytest.mark.parametrize(
    "field,value",
    [
        ("theorems", []),
        ("declarations", []),
        ("theorems", {"base": None}),
        ("declarations", {"Workhouse.base": None}),
    ],
)
def test_malformed_kernel_containers_report_errors_instead_of_crashing(kernel_export, field, value):
    root, data = kernel_export
    data[field] = value
    assert D.validate(data, root)


@pytest.mark.parametrize(
    "field,value",
    [
        ("kind", []),
        ("axioms", None),
        ("proof_dependencies", "Workhouse.base"),
        ("type_dependencies", [None]),
    ],
)
def test_malformed_kernel_declaration_fields_report_errors(kernel_export, field, value):
    root, data = kernel_export
    data["declarations"]["Workhouse.base"][field] = value
    assert D.validate(data, root)


def test_non_mapping_exports_are_rejected(kernel_export):
    root, _ = kernel_export
    assert D.validate(None, root)
    assert S.validate(None, root=root)


@pytest.mark.parametrize("document", [None, [], {"id": [], "path": []}])
def test_malformed_derivation_document_does_not_crash(tmp_path, document):
    assert S.validate(dict(schema="derivation-statements/v1", documents=[document]), root=tmp_path)


@pytest.mark.parametrize(
    "field,value",
    [
        ("id", []),
        ("status", []),
        ("evidence", {}),
        ("anchor", []),
        ("depends_on", None),
        ("lean", "bad"),
        ("lean_support", "bad"),
        ("lean_support", [{"name": [], "scope": 1}]),
    ],
)
def test_malformed_derivation_fields_do_not_crash(tmp_path, field, value):
    source = tmp_path / "docs/derivations/example.md"
    source.parent.mkdir(parents=True)
    source.write_text("# Source\n", encoding="utf-8")
    row = dict(
        id="DERIV:EXAMPLE:A",
        statement="A",
        locator="Source",
        anchor="# Source",
        status="proven",
        evidence="analytic",
        hypotheses=[],
        depends_on=[],
        lean=[],
        remaining="The actual construction remains.",
    )
    row[field] = value
    data = dict(
        schema="derivation-statements/v1",
        documents=[
            dict(
                id="CITE:EXAMPLE",
                path="docs/derivations/example.md",
                sha256="not-current",
                statements=[row],
            )
        ],
    )
    assert S.validate(data, root=tmp_path, theorem_names=set())


def test_existing_citation_cannot_point_at_the_wrong_derivation(tmp_path):
    source = tmp_path / "docs/derivations/example.md"
    source.parent.mkdir(parents=True)
    source.write_text("# Source\n", encoding="utf-8")
    (tmp_path / "ledger").mkdir()
    (tmp_path / "ledger/documents.yaml").write_text(
        yaml.safe_dump(
            {
                "aliases": [{"alias": "EXAMPLE", "path": "docs/derivations/different.md"}],
            }
        ),
        encoding="utf-8",
    )
    data = dict(
        schema="derivation-statements/v1",
        documents=[
            dict(
                id="CITE:EXAMPLE",
                path="docs/derivations/example.md",
                sha256="not-current",
                statements=[],
            )
        ],
    )
    assert any("native citation does not identify" in e for e in S.validate(data, root=tmp_path))
