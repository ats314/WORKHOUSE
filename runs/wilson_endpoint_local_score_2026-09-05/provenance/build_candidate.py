"""Build an additive documentation candidate without editing the repository."""

# Markdown templates preserve readable links and table rows as literal lines.
# ruff: noqa: E501

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "pyproject.toml").is_file())
BASE = HERE.parent.parent
TREE = HERE / "tree"
RUN = "wilson_endpoint_local_score_2026-09-05"
SPECS = [
    (
        "next_full_window_comparison/LITERAL_ENDPOINT_COMPLETE_WINDOW.md",
        "G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md",
        "4dcb8da8880414960035de61780dedd5ac7f31f3e1159846b37235000e01b930",
        [
            "check_literal_endpoint_window.py",
            "literal_endpoint_window_controls_frozen.json",
            "INDEPENDENT_ENDPOINT_WINDOW_AUDIT.md",
        ],
    ),
    (
        "next_energy_local_score/TRUE_GROUND_LOCALIZED_WILSON_SCORE.md",
        "G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md",
        "92c90d38b44975a75fe5f69f483ef1fea2190385e345dc33d575d6ac05848f55",
        [
            "check_localized_true_ground_score.py",
            "localized_true_ground_score_controls.json",
            "INDEPENDENT_LOCAL_SCORE_AUDIT.md",
        ],
    ),
    (
        "next_local_gradient_tensorization/LOCAL_GRADIENT_EXCITATION_SUPPORT.md",
        "G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md",
        "e955622980220d74e1a70144fcc6a9921c6b9831bf81204555e72c589b65a140",
        [
            "check_local_gradient_tensorization.py",
            "local_gradient_tensorization_controls_final.json",
        ],
    ),
    (
        "next_covariant_block_sources/LOCAL_COVARIANT_AVERAGED_PATH_SOURCES.md",
        "G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md",
        "7f2703641051ff90f9ab9e5b9d2155fc4ef69b7f9ac717f3f683a01bcf0a5653",
        [
            "check_covariant_path_sources.py",
            "covariant_path_source_controls.json",
            "check_fourier_alias_independent.py",
            "fourier_alias_independent_controls_frozen.json",
            "INDEPENDENT_FOURIER_ALIAS_AUDIT.md",
        ],
    ),
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read(relative: str) -> str:
    return (ROOT / relative).read_bytes().decode("utf-8")


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected one unmodified insertion anchor: {old[:70]!r}")
    return text.replace(old, new, 1)


def yaml_list(rows: list, spaces: int = 2) -> str:
    text = yaml.safe_dump(rows, allow_unicode=True, sort_keys=False, width=98)
    return "".join(" " * spaces + line if line.strip() else line for line in text.splitlines(True))


def main() -> None:
    TREE.mkdir(exist_ok=True)
    targets = {}
    copies = []
    for original_rel, basename, expected, evidence in SPECS:
        original = BASE / original_rel
        raw = original.read_bytes()
        if digest(raw) != expected:
            raise ValueError(f"Unfrozen or changed original: {original_rel}")
        body = raw.decode("utf-8").replace("\r\n", "\n")
        changes = []
        for old, new in (
            ("Outputs-only research continuation.", "Analytic research continuation."),
            ("Outputs-only analytic continuation.", "Analytic research continuation."),
            ("Outputs-only continuation.", "Analytic research continuation."),
            (
                "No frozen source or run is changed.",
                "The originating derivation is preserved unchanged.",
            ),
            (
                "`../next_local_gradient_tensorization/LOCAL_GRADIENT_EXCITATION_SUPPORT.md`",
                "[local gradient source theorem](G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md)",
            ),
        ):
            count = body.count(old)
            if count:
                body = body.replace(old, new)
                changes.append({"old": old, "new": new, "count": count})
        # Only observed repository proof basenames are converted into local links.
        pattern = re.compile(r"`(?:paper/research_notes/)?(G(?:18|19)_[A-Z0-9_]+\.md)`")
        for match in list(pattern.finditer(body))[::-1]:
            old = match.group(0)
            new = f"[{match.group(1)}]({match.group(1)})"
            body = body[: match.start()] + new + body[match.end() :]
            changes.append({"old": old, "new": new, "count": 1})
        appendix = "\n\n## Canonical source provenance and reproduction\n\n"
        appendix += (
            f"This is the canonical copy of the independently reviewed 5 September\n"
            f"derivation [{original.name}](../../runs/{RUN}/{original.name}),\n"
            f"whose original SHA256 is `{expected}`. The original proof bytes are\n"
            "preserved; this copy adjusts only stage metadata and relative links,\n"
            "then appends this explicitly separate provenance and follow-up record.\n\n"
            f"The [reproduction run](../../runs/{RUN}/README.md) preserves the analytic\n"
            "sources and the precisely scoped finite controls:\n\n"
        )
        appendix += "".join(f"- [{name}](../../runs/{RUN}/{name})\n" for name in evidence)
        if "LOCAL_GRADIENT_EXCITATION" in basename:
            appendix += (
                "\nThe [actual localized true-ground score theorem](G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md)\n"
                "subsequently proves the local additive score premise left as a target\n"
                "in Section 7. Its selected-source scope remains distinct from the\n"
                "[complete endpoint comparison](G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md),\n"
                "which controls the full high retained spectrum. Ambient interacting\n"
                "ground/source and scale comparisons remain open.\n"
            )
        elif "TRUE_GROUND_LOCALIZED" in basename:
            appendix += (
                "\nThe [complete endpoint theorem](G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md)\n"
                "provides a separate complete additive spectral comparison including\n"
                "all high retained directions. It does not promote the selected\n"
                "static Schur estimate here to a bound on every retained source.\n"
            )
        body = body.rstrip() + appendix
        rel = "paper/research_notes/" + basename
        targets[rel] = body
        copies.append(
            {
                "source": str(original.relative_to(ROOT).as_posix()),
                "source_sha256": expected,
                "canonical": rel,
                "replacements": changes,
                "appendix": appendix,
                "canonical_sha256": digest(body.encode("utf-8")),
            }
        )

    new_results = yaml.safe_load((HERE / "results.fragment.yaml").read_text(encoding="utf-8"))[
        "results"
    ]
    new_aliases = yaml.safe_load((HERE / "documents.fragment.yaml").read_text(encoding="utf-8"))[
        "aliases"
    ]
    for rel, key, rows in (
        ("ledger/results.yaml", "results", new_results),
        ("ledger/documents.yaml", "aliases", new_aliases),
    ):
        old = read(rel)
        before = yaml.safe_load(old)[key]
        name = "id" if key == "results" else "alias"
        if set(x[name] for x in before) & set(x[name] for x in rows):
            raise ValueError("A proposed new ledger record already exists")
        targets[rel] = replace_once(old, f"{key}:\n", f"{key}:\n" + yaml_list(rows))
        if yaml.safe_load(targets[rel])[key][len(rows) :] != before:
            raise ValueError("An existing ledger record changed")

    gap_additions = yaml.safe_load((HERE / "gaps.fragment.yaml").read_text(encoding="utf-8"))
    old_gaps = read("ledger/gaps.yaml")
    updated_gaps = old_gaps
    for gap_id, additions in gap_additions.items():
        marker = f"  - id: {gap_id}\n"
        start = updated_gaps.index(marker)
        end = updated_gaps.find("\n  - id: ", start + len(marker))
        if end < 0:
            end = len(updated_gaps)
        block = updated_gaps[start:end]
        match = re.search(r"    plan:\n( +)- step:", block)
        if match is None:
            raise ValueError("Expected existing plan step indentation")
        block = replace_once(
            block, "    plan:\n", "    plan:\n" + yaml_list(additions, len(match.group(1)))
        )
        updated_gaps = updated_gaps[:start] + block + updated_gaps[end:]
    before_gaps = yaml.safe_load(old_gaps)["gaps"]
    after_gaps = yaml.safe_load(updated_gaps)["gaps"]
    for old, new in zip(before_gaps, after_gaps, strict=True):
        restored = dict(new)
        if old["id"] in gap_additions:
            restored["plan"] = new["plan"][len(gap_additions[old["id"]]) :]
        if restored != old:
            raise ValueError("An old gap field or route was changed")
    targets["ledger/gaps.yaml"] = updated_gaps

    readme_latest = """The [complete endpoint comparison](paper/research_notes/G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md)
now transports the entire additive physical Wilson low cluster at its natural
time, with every high retained source direction included. Its two-lag matrix
certificate keeps the complete spectral-tail premise explicit. The
[actual localized quantum-ground score](paper/research_notes/G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md)
gives relative `O(u^-1)` Schur loss for local class sources and `O(u^-1/2)` for
the complete selected common-Gauss chart. The
[local gradient theorem](paper/research_notes/G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md)
transfers that estimate without a copy-count factor. These static selected-source
and complete endpoint conclusions have different scopes.

A [local gauge-covariant matrix block](paper/research_notes/G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md)
now realizes a physical tangent source with a uniform full three-dimensional
harmonic bound and an entire regulated Gaussian fast/source consequence.
The next target is its actual interacting quantum ground, fast form and
generated endpoint/history law, with a consistent physical clock and scale
trajectory. The [new run](runs/wilson_endpoint_local_score_2026-09-05/README.md)
keeps analytic theorems separate from finite exact controls.

"""
    targets["README.md"] = replace_once(
        read("README.md"), "## Current research\n\n", "## Current research\n\n" + readme_latest
    )

    research_latest = readme_latest.replace(
        "paper/research_notes/", "../paper/research_notes/"
    ).replace("(runs/", "(../runs/")
    research_latest = "## Latest scale comparison\n\n" + research_latest
    targets["docs/current_research.md"] = replace_once(
        read("docs/current_research.md"),
        "## Established starting point\n",
        research_latest + "## Established starting point\n",
    )
    old_target = "Prove energy-localized true-ground score/form control for the actual\ninteracting Wilson family."
    new_target = (
        "The actual local additive score premise is now proved, and the exact\n"
        "endpoint theorem separately controls its complete additive physical\n"
        "cluster including all high retained sources. The new local covariant\n"
        "matrix observation realizes the uniform physical harmonic source.\n"
        "Extend those inputs to actual interacting Wilson ground/source and\n"
        "endpoint laws, with quantitative errors uniform over the block family."
    )
    targets["docs/current_research.md"] = replace_once(
        targets["docs/current_research.md"], old_target, new_target
    )

    goal_latest = """The latest step joins three established mechanisms. The
[complete endpoint theorem](../paper/research_notes/G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md)
transports the entire additive physical low spectrum with high retained
sources controlled. The [actual local score theorem](../paper/research_notes/G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md)
and [excitation-support localization](../paper/research_notes/G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md)
give a uniform selected-source Schur estimate. The
[local covariant path block](../paper/research_notes/G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md)
gives an actual spatially local observation with the required uniform
transverse tangent and full regulated Gaussian source mechanism.

The remaining step is the actual interacting nonlinear fast/source and
generated-law comparison for that geometry. Endpoint positivity alone
does not erase memory, create a local Markov logarithm or assemble a
compatible scale hierarchy. A selected static source estimate alone does
not control its entire retained Schur complement. The conditional endpoint
clock budget states sufficient summable losses for a full gap, with those
interacting and hierarchy hypotheses still open.

"""
    targets["docs/research_goal.md"] = replace_once(
        read("docs/research_goal.md"),
        "## The next central target\n\n",
        "## The next central target\n\n" + goal_latest,
    )
    targets["docs/research_goal.md"] = targets["docs/research_goal.md"].replace(
        "Wilson energy-localized forms and coarse matching required",
        "interacting forms and coarse matching required",
    )
    targets["docs/research_goal.md"] = replace_once(
        targets["docs/research_goal.md"],
        "Realize the actual Wilson block and generated history dynamics,",
        "Realize the interacting fast/source and generated-history comparison for the local Wilson block,",
    )
    paper_latest = """## Current endpoint and local-source continuation

- [Complete literal endpoint spectrum](research_notes/G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md): full retained-space comparison, two-lag complete-count criterion and actual additive Wilson clusters.
- [Actual localized true-ground score](research_notes/G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md): fixed-SU(N) derivative control and relative class/common-Gauss selected-source loss.
- [Local gradient excitation supports](research_notes/G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md): arbitrary profile superpositions without copy-count loss and a cutoff onto frame.
- [Local covariant path sources](research_notes/G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md): globally defined matrix observation, exact cochain tangent, full harmonic bound and regulated Gaussian source consequence.

The [reproduction run](../runs/wilson_endpoint_local_score_2026-09-05/README.md)
preserves the original proofs and exact finite controls. These inputs advance
the interacting scale comparison; they do not construct the nonlinear
interacting hierarchy, identify every OS history range or remove the regulator.

"""
    targets["paper/README.md"] = replace_once(
        read("paper/README.md"),
        "## The manuscript of record\n",
        paper_latest + "## The manuscript of record\n",
    )
    targets[
        "docs/decisions/0042-compare-complete-endpoints-with-local-covariant-sources.md"
    ] = """# 42. Compare complete endpoints with local covariant sources

Date: 2026-09-05. Status: accepted.

This advances G19 physical scale comparison and G23 generated-history and
complementary-energy control through actual source and energy mechanisms.

Use the exact literal endpoint C_tau=J*exp(-tau h)J when making the complete
spectral comparison. Its polar/min-max proof includes the entire retained
space, and a finite two-lag certificate is valid only with an independently
complete spectral-tail/frame premise. The actual additive Wilson theorem
then transports every low radial and common-Gauss pair state in its natural
physical time. Keep its generated temporal memory and the distinction
between a positive quantum logarithm and a continuous-time Markov generator.

Record the actual localized true-ground score separately. Its class-source
loss is O(u^-1), and its complete chosen common-Gauss chart has O(u^-1/2)
loss uniformly in additive copy count. Exact excitation supports and centered
local scores supply that uniformity. A global any-bad event fails, and this
chosen static chart is not the whole marginal or Schur spectral subspace.

Use local anchored path averages to give the coarse observation an actual
gauge-covariant spatial meaning. Keep its output as a matrix average, which
need not be unitary. Its two commuting zero-cochain squares are distinct;
anchors cancel on physical transverse cotangents. The full harmonic bound
and regulated Gaussian source theorem follow on that tangent space. They
do not supply an actual nonlinear interacting fast form or an OS map.

Register five analytic results from four proof notes. Dependencies record
mathematical inputs; finite checks and runs receive only their exact scoped
support edges. Keep all previous proofs and dead routes unchanged. The next
target is the interacting true-ground/source and endpoint-law comparison,
including interfaces, flat variables, a compatible quantum hierarchy and
summable errors in one physical clock. Rooted infrared construction and
the Clay continuum obligations retain their established separate scopes.
"""

    # Validate dependency endpoints and acyclicity without relying on stale views.
    all_results = yaml.safe_load(targets["ledger/results.yaml"])["results"]
    all_aliases = yaml.safe_load(targets["ledger/documents.yaml"])["aliases"]
    known = {row["id"] for row in all_results} | {"CITE:" + row["alias"] for row in all_aliases}
    known |= {row["id"] for row in after_gaps}
    dependencies = {row["id"]: row["depends_on"] for row in all_results}
    for row in new_results:
        for endpoint in [row["source"], *row["depends_on"], *row["bears_on"]]:
            if endpoint not in known:
                raise ValueError(f"Unresolved new result endpoint {endpoint}")
    alias_names = {row["alias"] for row in all_aliases}
    for row in new_aliases:
        if any(ref not in alias_names for ref in row.get("cites", [])):
            raise ValueError("Unresolved document citation")
    complete, active = set(), set()

    def visit(node):
        if node in active:
            raise ValueError("Cyclic result proof dependency")
        if node in complete:
            return
        active.add(node)
        for child in dependencies.get(node, []):
            visit(child)
        active.remove(node)
        complete.add(node)

    for node in dependencies:
        visit(node)

    manifest = {
        "schema": "workhouse-endpoint-docs-candidate/v1",
        "run": RUN,
        "proof_copies": copies,
        "targets": {},
        "new_result_ids": [x["id"] for x in new_results],
        "new_aliases": [x["alias"] for x in new_aliases],
        "old_result_alias_gap_fields_and_route_history_preserved": True,
        "all_result_dependencies_acyclic": True,
    }
    for rel, text in targets.items():
        path = TREE / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        data = text.replace("\r\n", "\n").encode("utf-8")
        path.write_bytes(data)
        old_path = ROOT / rel
        manifest["targets"][rel] = {
            "before_sha256": digest(old_path.read_bytes()) if old_path.exists() else None,
            "after_sha256": digest(data),
        }
    (HERE / "CANDIDATE_COPY_AUDIT.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(
        json.dumps(
            {
                "staged_files": len(targets),
                "proofs": len(copies),
                "results": len(new_results),
                "canonical_repository_unchanged": True,
            }
        )
    )


if __name__ == "__main__":
    main()
