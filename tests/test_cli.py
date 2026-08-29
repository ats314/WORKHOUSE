"""The command line's agent-facing contract.

Each test here pins a failure an agent actually hit (recorded in the
2026-08-28 theory-graph experience notes): the negative-query rescue eating
trailing options, ANSI codes reaching piped output, and the absence of a
machine-readable form for search/why/verify.
"""

from __future__ import annotations

import json

import pytest

from workhouse import cli as cli_mod
from workhouse import navigator as navigator_mod


class TestNegativeQueryRescue:
    def test_bare_negative_value_still_rescued(self):
        assert cli_mod._rescue_negative_query(["search", "-5/48"]) == ["search", "--", "-5/48"]

    def test_trailing_options_survive_the_rescue(self):
        # The recorded bug: `search -X --corpus --limit 12` inserted `--`
        # before the value, turning the later flags into unrecognized
        # positionals. The value must move behind the options instead.
        argv = ["search", "-211835444920651/4405310420659200", "--corpus", "--limit", "12"]
        assert cli_mod._rescue_negative_query(argv) == [
            "search",
            "--corpus",
            "--limit",
            "12",
            "--",
            "-211835444920651/4405310420659200",
        ]

    def test_explicit_separator_is_left_alone(self):
        argv = ["search", "--corpus", "--", "-5/48"]
        assert cli_mod._rescue_negative_query(argv) == argv

    def test_option_valued_queries_untouched(self):
        argv = ["search", "q_old", "--limit", "3"]
        assert cli_mod._rescue_negative_query(argv) == argv

    def test_negative_with_options_parses_end_to_end(self, capsys):
        rc = cli_mod.main(["search", "-5/48", "--limit", "3"])
        out = capsys.readouterr().out
        assert rc == 0
        assert "-5/48" in out


class TestPlainStdout:
    def test_no_color_flag_forces_plain(self):
        assert cli_mod._plain_stdout_wanted(True)

    def test_no_color_env_forces_plain(self, monkeypatch):
        monkeypatch.setenv("NO_COLOR", "1")
        assert cli_mod._plain_stdout_wanted(False)

    def test_piped_output_carries_no_ansi(self, capsys):
        # pytest's capture is not a tty, which is exactly the agent's world.
        cli_mod.main(["search", "C2", "--limit", "2"])
        assert "\033[" not in capsys.readouterr().out


class TestJsonOutput:
    def test_search_json_is_one_object_with_hits(self, capsys):
        rc = cli_mod.main(["search", "--json", "--limit", "2", "C2"])
        data = json.loads(capsys.readouterr().out)
        assert rc == 0
        assert data["query"] == "C2"
        assert data["total_hits"] >= len(data["hits"]) > 0
        assert {"how", "id", "statement", "tier"} <= set(data["hits"][0])

    def test_why_json_carries_record_and_edges(self, capsys):
        rc = cli_mod.main(["why", "--json", "C2"])
        data = json.loads(capsys.readouterr().out)
        assert rc == 0
        assert data["id"] == "C2"
        assert data["incoming"] and isinstance(data["incoming"][0]["type"], str)
        # Neighbors carry enough to act without a second lookup.
        some_check = next(v for v in data["neighbors"].values() if v["kind"] == "check")
        assert some_check["reproduce"].startswith("workhouse verify --only")

    def test_why_json_unknown_id_fails_with_error_object(self, capsys):
        rc = cli_mod.main(["why", "--json", "NO_SUCH_ID"])
        data = json.loads(capsys.readouterr().out)
        assert rc == 1
        assert "error" in data

    def test_verify_json_reports_each_check(self, capsys):
        rc = cli_mod.main(["verify", "--json", "--only", "Delta_C"])
        data = json.loads(capsys.readouterr().out)
        assert rc == 0
        assert data["total"] == data["passed"] > 0
        row = data["checks"][0]
        assert {"suite", "name", "tier", "passed", "detail", "where", "reproduce"} <= set(row)

    def test_verify_json_no_match_is_failure(self, capsys):
        rc = cli_mod.main(["verify", "--json", "--only", "zzz-no-such-check"])
        data = json.loads(capsys.readouterr().out)
        assert rc == 1
        assert data["total"] == 0


class TestWhyNextActions:
    def test_explain_ends_with_runnable_verifier_commands(self):
        text, found = navigator_mod.explain("C2")
        assert found
        assert "Re-check it yourself" in text
        assert "workhouse verify --only" in text

    def test_neighborhood_matches_explain_resolution(self):
        data, found = navigator_mod.neighborhood("adr 5")
        assert found and data["id"] == "ADR:0005"


@pytest.mark.parametrize(
    "module_name",
    ["claims", "certified", "graph", "ledger", "literature", "navigator", "search", "cli"],
)
def test_no_locale_dependent_text_reads(module_name):
    """The Windows failure mode: a read_text() without an encoding decodes with
    the locale codepage (cp1252) and dies on UTF-8 bytes the repo legitimately
    contains. Every text read in these modules must pin utf-8."""
    import inspect
    import re
    from importlib import import_module

    src = inspect.getsource(import_module(f"workhouse.{module_name}"))
    bare = [
        line.strip()
        for line in src.splitlines()
        if re.search(r"\.read_text\(\)|\.write_text\([^)]*\)$", line)
        and "encoding" not in line
        and not line.strip().startswith(("#", '"', "'"))
    ]
    assert not bare, f"locale-dependent reads/writes in {module_name}: {bare}"


class TestDerive:
    def test_multi_root_markdown_export(self, capsys):
        rc = cli_mod.main(["derive", "C2", "G3"])
        out = capsys.readouterr().out
        assert rc == 0
        assert "## C2" in out and "## G3" in out
        # The disagreement is preserved whole: both branches, never a winner.
        assert "-211835444920651/4405310420659200" in out
        assert "-0.020213328886166577" in out
        assert "Both sides, neither promoted" in out
        # Every included node carries the registered edge that brought it in,
        # and the export says out loud that it never infers.
        assert "edge: `" in out
        assert "not a proof" in out

    def test_checks_carry_verdict_and_reproduce(self, capsys):
        cli_mod.main(["derive", "C2"])
        out = capsys.readouterr().out
        assert "**PASS**" in out
        assert "reproduce: `workhouse verify --only" in out

    def test_unknown_root_fails_but_renders_the_rest(self, capsys):
        rc = cli_mod.main(["derive", "NOPE", "G3"])
        out = capsys.readouterr().out
        assert rc == 1
        assert "no record with this id" in out
        assert "## G3" in out


class TestBranches:
    def test_c2_shows_both_sides_and_the_missing_comparison(self, capsys):
        rc = cli_mod.main(["branches", "C2"])
        out = capsys.readouterr().out
        assert rc == 0
        assert "historical" in out and "v10a.26" in out
        assert "missing comparison (G3)" in out
        assert "originating documents" in out

    def test_no_sides_id_is_a_clean_failure(self, capsys):
        rc = cli_mod.main(["branches", "C999"])
        assert rc == 1
        assert "no contradiction" in capsys.readouterr().out


class TestExport:
    def test_envelope_shape_and_vocabularies(self, capsys):
        rc = cli_mod.main(["export"])
        data = json.loads(capsys.readouterr().out)
        assert rc == 0
        assert data["schema_version"]
        assert set(data["tier_vocabulary"]) == {"0", "1", "2", "3"}
        assert set(data["edge_how_vocabulary"]) == {"curated", "derived"}
        assert len(data["claims"]) > 2000
        assert len(data["edges"]) > 2500
        edge = data["edges"][0]
        assert {"src", "dst", "type", "how", "source"} == set(edge)
        # T3 stays T3 in export: nothing is promoted on the way out.
        c2 = next(c for c in data["claims"] if c["id"] == "C2")
        assert c2["tier"] == 3


class TestNearestValue:
    def test_miss_reports_nearest_registered_value(self, capsys):
        # One digit off the C20 gate value: close enough that silence would be
        # the confident-false-negative failure mode, far enough to be a miss.
        rc = cli_mod.main(["search", "-1474623/1675521"])
        out = capsys.readouterr().out
        assert rc == 1
        assert "nearest registered value" in out
        # Both C20 branches sit ~6e-7 away (they differ from each other by only
        # 3e-15); either is a correct nearest answer, and the test must not
        # promote one of them.
        assert "-1474623/1675520" in out or "-521965902/593076541" in out
        assert "Proximity is not identity" in out

    def test_hit_path_stays_silent_about_proximity(self, capsys):
        cli_mod.main(["search", "-5/48", "--limit", "2"])
        assert "nearest registered value" not in capsys.readouterr().out

    def test_json_carries_the_nearest_object(self, capsys):
        cli_mod.main(["search", "--json", "--", "-1474623/1675521"])
        data = json.loads(capsys.readouterr().out)
        assert data["nearest"]["value"] in ("-1474623/1675520", "-521965902/593076541")
        assert 0 < data["nearest"]["relative_distance"] < 1e-5


def test_generated_files_pin_lf_newlines():
    """Path.write_text translates \\n to the platform newline unless told not
    to, so an unpinned writer makes every generated file CRLF on Windows and
    the byte-determinism the manifest depends on is gone."""
    import inspect
    from importlib import import_module

    for module_name in ["claims", "graph", "certified", "frontier", "notes", "atlas"]:
        src = inspect.getsource(import_module(f"workhouse.{module_name}"))
        for i, line in enumerate(src.splitlines()):
            if ".write_text(" in line and not line.strip().startswith("#"):
                window = "\n".join(src.splitlines()[i : i + 4])
                assert 'newline="\\n"' in window, f"{module_name}: unpinned newline: {line.strip()}"


class TestLegacyEncodingStdout:
    """A cp1252 stdout must not be able to kill a subcommand.

    The recorded failure: the `Windows smoke` job ran `workhouse why C2` and
    got `UnicodeEncodeError: 'charmap' codec can't encode character '→'`
    before a single edge was printed. Windows opens stdout as cp1252, and the
    registry's own alphabet -- the arrow between claim ids, `Γ`, `ε`, `β` --
    lies outside it. These run on every platform, so the Linux `check` job
    catches a regression without waiting for the Windows runner.
    """

    @pytest.mark.parametrize(
        "argv",
        [
            ["why", "C2"],
            ["frontier", "--brief"],
            ["search", "--", "-5/48"],
        ],
    )
    def test_subcommand_survives_a_cp1252_stdout(self, argv, capsysbinary, monkeypatch):
        import io
        import sys

        # A real cp1252 text stream over a byte sink: the same object Windows
        # hands the process, not a mock of one.
        raw = io.BytesIO()
        stream = io.TextIOWrapper(raw, encoding="cp1252", newline="\n")
        monkeypatch.setattr(sys, "stdout", stream)
        assert cli_mod.main(argv) == 0
        sys.stdout.flush()
        assert raw.getvalue(), "the subcommand printed nothing"

    def test_the_arrow_survives_as_itself(self, monkeypatch):
        import io
        import sys

        raw = io.BytesIO()
        stream = io.TextIOWrapper(raw, encoding="cp1252", newline="\n")
        monkeypatch.setattr(sys, "stdout", stream)
        assert cli_mod.main(["why", "C2"]) == 0
        sys.stdout.flush()
        # Not merely "did not crash": the arrow is reconfigured to UTF-8, so it
        # arrives as its own bytes rather than a backslash escape.
        assert "→".encode() in raw.getvalue()
