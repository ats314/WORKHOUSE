"""The frontier is generated, so the thing to test is that it cannot go stale."""

import json
import subprocess
import sys
from pathlib import Path

from workhouse import frontier as F

ROOT = Path(__file__).resolve().parents[1]


def test_frontier_md_is_current():
    """A checked-in generated file is a lie the moment the inputs move.

    Regenerating must be a no-op. If this fails, run `make frontier` — the
    failure is the point: something changed and the orientation file did not.
    """
    on_disk = (ROOT / "FRONTIER.md").read_text()
    assert F.render(F.compute()) == on_disk, "FRONTIER.md is stale; run `make frontier`"


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
    hook = ROOT / ".claude" / "hooks" / "session-start.sh"
    proc = subprocess.run(
        ["bash", str(hook)],
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
