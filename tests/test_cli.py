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
