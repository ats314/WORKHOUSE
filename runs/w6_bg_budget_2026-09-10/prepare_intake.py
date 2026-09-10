"""Preserve the authored sources and prepare their portable successor documents."""
from hashlib import sha256
import json
from pathlib import Path
import shutil

RUN = Path(__file__).resolve().parent
REPO = RUN.parents[1]
CAMPAIGN = Path(r"C:\WORKHOUSE\research\w6_bg_uniform_20260910")
PRIOR = Path(r"C:\WORKHOUSE\worktrees\w6-energy-form-20260910")
PREFIX = "../../runs/w6_bg_budget_2026-09-10/"
PREVIOUS = "../../runs/recent_research_integration_2026-09-09/sources/"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


files = []
for name in ["residual_analysis.md", "residual_verify.py", "residual_checks.json",
             "bg_analysis.md", "bg_gaussian_cutoff_check.py", "bg_gaussian_cutoff_checks.json"]:
    files.append((CAMPAIGN / name, RUN / "sources" / "campaign" / name, "new standalone campaign"))
for relative in ["docs/research/w6-subdivided-compact-transport-2026-09-10.md",
                 "lean/Workhouse/W6Subdivision.lean"]:
    files.append((PRIOR / relative, RUN / "sources" / "prior_subdivision" / relative,
                  "prior project subdivision result; not newly derived in this campaign"))
manifest = []
for source, target, attribution in files:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        assert digest(target) == digest(source), f"Refusing to overwrite differing intake: {target}"
    else:
        shutil.copyfile(source, target)
    manifest.append({"original_path": str(source), "preserved_path": target.relative_to(RUN).as_posix(),
                     "sha256": digest(source), "size_bytes": source.stat().st_size,
                     "attribution": attribution})
(RUN / "source_manifest.json").write_text(json.dumps({
    "schema": "w6-bg-intake/v1", "date": "2026-09-10", "sources": manifest,
    "scope": "Byte identity and attribution only; mathematical proof and finite replay have separate scopes."
}, indent=2) + "\n", encoding="utf-8")

residual = (CAMPAIGN / "residual_analysis.md").read_text(encoding="utf-8")
residual = residual.replace("(../w6_compact_continuation_20260909/",
                            "(" + PREVIOUS + "w6_compact_continuation_20260909/")
residual = residual.replace("(../../worktrees/w6-energy-form-20260910/docs/research/",
                            "(" + PREFIX + "sources/prior_subdivision/docs/research/")
for name in ["residual_verify.py", "residual_checks.json"]:
    residual = residual.replace("(" + name + ")", "(" + PREFIX + "sources/campaign/" + name + ")")
residual = residual.replace("The output pins the exact bytes of this note and its checking script.",
                            "The output pins the exact bytes of the preserved standalone note and its checking script.")
residual = residual.replace("10 September 2026. Analytic continuation", "10 September 2026. Portable integrated successor of the "
                            "[standalone note](" + PREFIX + "sources/campaign/residual_analysis.md). "
                            "The [intake manifest](" + PREFIX + "source_manifest.json) preserves its original path and bytes.\n\n"
                            "Analytic continuation", 1)
residual += ("\nThe referenced prior subdivision proof is preserved separately as "
             "[W6Subdivision.lean](" + PREFIX + "sources/prior_subdivision/lean/Workhouse/W6Subdivision.lean). "
             "This run did not rebuild that prior Lean source.\n")
rp = REPO / "docs/derivations/w6-ground-jets-and-transport-budget.md"
assert not rp.exists(), f"New successor already exists: {rp}"
rp.write_text(residual, encoding="utf-8")

bg = (CAMPAIGN / "bg_analysis.md").read_text(encoding="utf-8")
bg = bg.replace("10 September 2026. Standalone continuation; source files are unchanged.",
                "10 September 2026. Portable integrated successor of the "
                "[standalone analysis](" + PREFIX + "sources/campaign/bg_analysis.md). "
                "The [intake manifest](" + PREFIX + "source_manifest.json) preserves its original path and bytes. "
                "The endpoint, Gaussian inference obstruction and local repair below are new campaign arguments; "
                "the source criterion, actual-ground estimates and subdivision theorem are prior project results.")
bg = bg.replace("`C:/WORKHOUSE/REPO/runs/recent_research_integration_2026-09-09/sources/w6_compact_continuation_20260909/quantile_source_weight.md`",
                "[the prior source-energy criterion](" + PREVIOUS + "w6_compact_continuation_20260909/quantile_source_weight.md)")
bg = bg.replace("`../w6_square_block_20260909/source.md`",
                "[the square Gaussian source derivation](" + PREVIOUS + "w6_square_block_20260909/source.md)")
for name in ["quantile_source_weight.md", "quantile_scale.md", "compact_residual.md"]:
    bg = bg.replace("- `" + name + "`:", "- [" + name + "](" + PREVIOUS + "w6_compact_continuation_20260909/" + name + "):")
bg = bg.replace("`bg_gaussian_cutoff_check.py`", "[bg_gaussian_cutoff_check.py](" + PREFIX + "sources/campaign/bg_gaussian_cutoff_check.py)")
bg = bg.replace("`bg_gaussian_cutoff_checks.json`", "[bg_gaussian_cutoff_checks.json](" + PREFIX + "sources/campaign/bg_gaussian_cutoff_checks.json)")
bg = bg.replace("`residual_analysis.md`", "[the ground-jet and transport-budget companion](w6-ground-jets-and-transport-budget.md)")
bg = bg.replace("`C:/WORKHOUSE/worktrees/w6-energy-form-20260910/docs/research/w6-subdivided-compact-transport-2026-09-10.md`",
                "[the preserved prior subdivision note](" + PREFIX + "sources/prior_subdivision/docs/research/w6-subdivided-compact-transport-2026-09-10.md)")
start = bg.index("A targeted primary-source literature search located Barry Simon's")
end = bg.index("\n\nThe supplied worktree note", start)
bg = bg[:start] + bg[end+2:]
normalization = ("\nHere T includes one half of the original-edge T_op used in the companion "
                 "note, so both notes use the same compact Hamiltonian normalization.\n")
needle = "the source energy and conditional score variance are"
bg = bg.replace(needle, normalization + "\nThe source energy and conditional score variance are", 1)
bg += ("\nThe uncited external-literature search paragraph in the received note was not a proof input "
       "and is omitted from this integrated successor; its exact text remains in the preserved source.\n")
bp = REPO / "docs/derivations/w6-conditional-score-tail-control.md"
assert not bp.exists(), f"New successor already exists: {bp}"
bp.write_text(bg, encoding="utf-8")
print(json.dumps({"preserved_sources": len(manifest), "successors": [str(rp), str(bp)]}))
