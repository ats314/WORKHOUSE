"""The frontier is generated, so the thing to test is that it cannot go stale."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from workhouse import frontier as F

ROOT = Path(__file__).resolve().parents[1]


def test_frontier_md_is_current():
    """A checked-in generated file is a lie the moment the inputs move.

    Regenerating must be a no-op. If this fails, run `make frontier` — the
    failure is the point: something changed and the orientation file did not.
    """
    on_disk = (ROOT / "FRONTIER.md").read_text(encoding="utf-8")
    assert F.render(F.compute()) == on_disk, "FRONTIER.md is stale; run `make frontier`"


def test_the_two_t0_counters_agree():
    """One Lean tree, one count. They were allowed to disagree once.

    `FRONTIER.md` and `CERTIFIED.md` each report the size of the T0 layer, and
    each used to scrape the tree with its own copy of the declaration pattern.
    `certified` widened its copy to allow the `@[simp]` prefix; `frontier` was
    left behind. The generated files then said 37 and 40 over the same three
    declarations, both regenerated, both staleness-tested, and neither test
    could see the disagreement because each only compared a file with the
    scrape that wrote it.

    A number this repository prints in two places is a number two things must
    agree on, which is the same rule it applies to the corpus.
    """
    from workhouse import certified as C

    counted, _sorries = F._lean_counts()
    assert counted == len(C.lean_claims()), (
        f"FRONTIER counts {counted} Lean theorems, CERTIFIED lists {len(C.lean_claims())}"
    )


def test_no_lean_theorem_is_counted_twice():
    """The scrape returns declarations, so a duplicated name is a real one."""
    names = [name for _rel, _n, name in F.lean_declarations()]
    dupes = sorted({n for n in names if names.count(n) > 1})
    assert not dupes, f"two Lean declarations share a name: {dupes}"


def test_the_brief_is_short_enough_to_read():
    """An injection long enough to skim is long enough to ignore."""
    text = F.brief()
    assert 400 < len(text) < 2000, len(text)


def test_the_brief_carries_the_traps_that_actually_recur():
    text = F.brief()
    for trap in ("m_4", "4**r", "_NUM", "theory/", "tolerance"):
        assert trap in text, f"the brief drops the {trap!r} trap"


def test_the_brief_names_the_open_contradiction_by_id():
    led_open = F.compute().disputed
    text = F.brief()
    for c in led_open:
        assert c["id"] in text


def test_the_hook_emits_valid_session_start_json():
    """The hook's stdout is parsed by the harness; anything else breaks startup."""
    bash = shutil.which("bash")
    if bash is None:
        pytest.skip("the session-start hook requires bash")
    hook = ROOT / ".claude" / "hooks" / "session-start.sh"
    proc = subprocess.run(
        [bash, str(hook)],
        capture_output=True,
        text=True,
        env={"PATH": "/usr/bin:/bin:/usr/local/bin", "CLAUDE_PROJECT_DIR": str(ROOT)},
        check=True,
    )
    payload = json.loads(proc.stdout)
    output = payload["hookSpecificOutput"]
    assert output["hookEventName"] == "SessionStart"
    assert "WORKHOUSE" in output["additionalContext"]


def test_the_cheapest_step_actually_settles_something():
    """Bookkeeping is not a decisive test, however cheap it is."""
    for gap in F.compute().cheapest:
        assert gap.get("resolves") or gap.get("unblocks") or gap.get("load_bearing"), gap["id"]


def test_downstream_ranking_puts_the_adjudication_first():
    """G3 gates the fourth order, which gates the sixth. If that stops being
    true the dependency spine has changed and someone should notice."""
    ranked = F.compute().downstream
    assert ranked[0][0] == "G3", ranked[:3]
    assert "C2" in ranked[0][2]


def test_unifying_candidates_all_carry_a_falsifier():
    for u in F.compute().unifying:
        assert str(u["falsifier"]).strip(), f"{u['id']} is an analogy, not a candidate"


def test_cli_frontier_runs():
    proc = subprocess.run(
        [sys.executable, "-m", "workhouse.cli", "frontier", "--brief"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=True,
    )
    assert "WORKHOUSE" in proc.stdout


def test_lean_counters_ignore_comments():
    """A module header that SAYS "no `sorry`" must not count as a sorry.

    PR #30's six new modules each carry such a header; the raw \\bsorry\\b
    count would report six sorries that do not exist, and a doc comment
    quoting a `theorem` line would inflate the theorem count the same way.
    """
    body = (
        "/-\nStatus: builds clean, no `sorry`; see `theorem demo` below.\n-/\n"
        "-- sorry is only mentioned in this comment\n"
        "theorem real_one : 1 = 1 := rfl\n"
        "/- nested /- block -/ still a comment: sorry -/\n"
        "lemma real_two : 2 = 2 := rfl -- trailing note: sorry\n"
    )
    stripped = F.strip_lean_comments(body)
    assert "sorry" not in stripped
    assert len(stripped.splitlines()) == len(body.splitlines())
    import re as _re

    assert len(_re.findall(r"^\s*(?:theorem|lemma)\s", stripped, _re.MULTILINE)) == 2


def test_current_lean_tree_has_no_sorries():
    theorems, sorries = F._lean_counts()
    assert sorries == 0, "a sorry entered the Lean tree (or the counter regressed)"
    assert theorems >= 28
