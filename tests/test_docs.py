"""Documentation checks are bounded, read-only and portable across checkouts."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_docs.py"
SPEC = importlib.util.spec_from_file_location("workhouse_check_docs", SCRIPT)
DOCS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DOCS)


def fixture(root, text, *, targets=None, maintained=None):
    (root / "README.md").write_text(text, encoding="utf-8")
    for name, content in (targets or {}).items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    manifest = root / "manifest.json"
    manifest.write_text(
        json.dumps(
            dict(schema="documentation-manifest/v1", maintained=maintained or ["README.md"])
        ),
        encoding="utf-8",
    )
    return DOCS.check(root, manifest)


def test_inline_reference_images_titles_and_balanced_destinations(tmp_path):
    result = fixture(
        tmp_path,
        '[file](docs/a(b).md#section "title")\n'
        "[full][TARGET] [collapsed][] [shortcut]\n"
        '[target]: <docs/a(b).md#section> "reference title"\n'
        "[collapsed]: docs/a(b).md\n[shortcut]: docs/a(b).md\n"
        "![figure](image.svg)\n[space](<a b.md>)\n",
        targets={"docs/a(b).md": "# Section\n", "image.svg": "<svg/>", "a b.md": "# Space"},
    )
    assert result["errors"] == []
    assert result["checked_links"] == 6


def test_duplicate_unicode_and_explicit_anchors(tmp_path):
    result = fixture(
        tmp_path,
        "[one](target.md#über-中文) [two](target.md#über-中文-1)\n"
        "[three](target.md#a-1-1) [explicit](target.md#Exact-ID)\n"
        "[name](target.md#named) [setext](target.md#setext-code)\n",
        targets={
            "target.md": "# Über 中文!\n# Über 中文!\n# A\n# A\n# A-1\n"
            '<span id="Exact-ID"></span><a name="named"></a>\n'
            "Setext `code`\n---\n"
        },
    )
    assert result["errors"] == []


def test_code_and_comments_do_not_create_links_or_headings(tmp_path):
    result = fixture(
        tmp_path,
        "# Real\n`[bad](missing.md)`\n``literal ` [bad](missing.md)``\n"
        "~~~markdown\n[bad](missing.md)\n# Phantom\n~~~\n"
        "```\n[bad](missing.md)\n```\n    [bad](missing.md)\n"
        "<!-- [bad](missing.md) -->\n[ok](#real)\n",
    )
    assert result["errors"] == []
    assert result["checked_links"] == 1
    assert "phantom" not in DOCS.markdown_anchors((tmp_path / "README.md").read_text())


@pytest.mark.parametrize("fence", ["```", "~~~"])
def test_fence_marker_in_comment_does_not_hide_live_markdown(tmp_path, fence):
    text = f"<!-- hidden example\n{fence}\n-->\n[bad](missing.md)\n# Real\n"
    result = fixture(tmp_path, text)
    assert len(result["errors"]) == 1
    assert "Missing local target" in result["errors"][0]["message"]
    assert result["errors"][0]["line"] == 4
    assert DOCS.markdown_anchors(text) == {"real"}
    assert len(DOCS.visible_blocks(text)) == len(text)


@pytest.mark.parametrize("fence", ["```", "~~~"])
def test_comment_marker_in_real_fence_does_not_hide_live_markdown(tmp_path, fence):
    text = f"{fence}\n<!-- unclosed example\n# Hidden\n{fence}\n[bad](missing.md)\n# Real\n"
    result = fixture(tmp_path, text)
    assert len(result["errors"]) == 1
    assert "Missing local target" in result["errors"][0]["message"]
    assert result["errors"][0]["line"] == 5
    assert DOCS.markdown_anchors(text) == {"real"}
    assert len(DOCS.visible_blocks(text)) == len(text)


@pytest.mark.parametrize(
    ("destination", "message"),
    [
        ("missing.md", "Missing local target"),
        ("Target.md", "Filename case mismatch"),
        ("target.md#absent", "Missing Markdown anchor"),
        ("../outside.md", "escapes the checkout"),
        ("%2e%2e/outside.md", "escapes the checkout"),
        ("/etc/passwd", "Absolute/local-machine"),
        ("C:/WORKHOUSE/README.md", "Absolute/local-machine"),
        (r"C:\WORKHOUSE\README.md", "Absolute/local-machine"),
        ("file:///C:/WORKHOUSE/README.md", "Absolute/local-machine"),
    ],
)
def test_bad_links_fail_with_actionable_source_locations(tmp_path, destination, message):
    result = fixture(tmp_path, f"# Title\n[bad]({destination})\n", targets={"target.md": "# Here"})
    assert len(result["errors"]) == 1
    assert result["errors"][0]["source"] == "README.md"
    assert result["errors"][0]["line"] == 2
    assert message in result["errors"][0]["message"]


def test_missing_reference_is_not_silently_ignored(tmp_path):
    result = fixture(tmp_path, "[full][undefined]\n[collapsed][]\n")
    assert len(result["errors"]) == 2
    assert all("Undefined link reference" in error["message"] for error in result["errors"])


def test_fragment_only_links_and_non_markdown_fragments(tmp_path):
    result = fixture(
        tmp_path, "# Home\n[here](#home) [pdf](paper.pdf#page=2)\n", targets={"paper.pdf": "x"}
    )
    assert result["errors"] == []
    assert result["unchecked_non_markdown_fragments"] == 1


def test_external_links_are_skipped_and_historical_targets_not_crawled(tmp_path):
    result = fixture(
        tmp_path,
        "[web](https://example.invalid/x) [mail](mailto:x@example.invalid)\n"
        "[past](runs/source.md#history)\n",
        targets={"runs/source.md": "# History\n[old broken link](missing.md)"},
    )
    assert result["errors"] == []
    assert result["skipped_external_links"] == 2
    assert result["checked_documents"] == 1


def test_nested_path_case_is_checked_even_on_case_insensitive_filesystems(tmp_path):
    result = fixture(tmp_path, "[bad](Docs/target.md)", targets={"docs/target.md": "# Target"})
    assert "Filename case mismatch" in result["errors"][0]["message"]


def test_percent_encoding_and_parent_links_inside_the_checkout(tmp_path):
    result = fixture(
        tmp_path,
        "# Home\n",
        maintained=["docs/guide.md"],
        targets={
            "docs/guide.md": "[root](../README.md#home)\n"
            "[unicode](<../a%20b.md#%C3%BCber> (a title))\n",
            "a b.md": "# Über\n",
        },
    )
    assert result["errors"] == []


def test_symlink_targets_cannot_escape_the_checkout(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    outside = tmp_path / "outside.md"
    outside.write_text("# Outside", encoding="utf-8")
    try:
        (root / "link.md").symlink_to(outside)
    except OSError:
        pytest.skip("Host does not permit symlink creation")
    result = fixture(root, "[outside](link.md#outside)")
    assert "outside the checkout" in result["errors"][0]["message"]


def test_multiline_reference_syntax_is_reported_as_unsupported(tmp_path):
    result = fixture(tmp_path, "[reference]:\n  target.md\n")
    assert result["warnings"]
    assert "multiline" in result["warnings"][0]["message"]


def test_manifest_paths_cannot_escape_and_are_required(tmp_path):
    result = fixture(tmp_path, "# Root", maintained=["../outside.md", "absent.md"])
    assert len(result["errors"]) == 2
    assert result["checked_documents"] == 0


def test_duplicate_manifest_documents_fail_before_scanning(tmp_path):
    result = fixture(tmp_path, "# Home", maintained=["README.md", "README.md"])
    assert len(result["errors"]) == 1
    assert "unique maintained" in result["errors"][0]["message"]
    assert result["checked_documents"] == 0


def test_cli_json_exit_status_and_read_only_behavior(tmp_path):
    fixture(tmp_path, "[bad](missing.md)")
    before = {p.relative_to(tmp_path): p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    run = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--root",
            str(tmp_path),
            "--manifest",
            "manifest.json",
            "--json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert run.returncode == 1
    assert json.loads(run.stdout)["errors"]
    assert before == {
        p.relative_to(tmp_path): p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()
    }
