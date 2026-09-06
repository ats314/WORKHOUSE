"""One-shot UTF-8/LF copies of accepted next-package proof notes.

Preserves original source bytes and records every text substitution and
additive continuation for independent canonical-body reconstruction.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT = Path("paper/research_notes")
RUN = "literal_quantum_sources_2026-09-05"
SOURCES = [
    ("next_literal/LITERAL_VACUUM_COARSE_PROJECTION.md", "G19_WILSON_LITERAL_VACUUM_COARSE_SOURCES_20260905.md"),
    ("next_literal_common/COMMON_GAUSS_LITERAL_FAST_FLOOR.md", "G19_WILSON_COMMON_GAUSS_LITERAL_FAST_FLOOR_20260905.md"),
    ("next_literal/GROUND_MARGINAL_SCHUR_SCORE.md", "G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md"),
    ("next_gaussian_full/ENTIRE_GAUSSIAN_LITERAL_COMPLEMENT.md", "G19_GAUSSIAN_QUANTUM_FAST_SOURCES_20260905.md"),
    ("next_quantum_score_center/TRUE_GROUND_CENTER_SCORE_OBSTRUCTION.md", "G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md"),
]
INVERSE = BASE / "next_literal_inverse/LITERAL_INVERSE_ENERGY_FULL_FORM.md"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert len(SOURCES) == 5
    for relative, target in SOURCES:
        assert (BASE / relative).is_file()
        assert not (OUT / target).exists(), target
    assert digest(INVERSE) == "dbcd96ad5570f6fe8e625c002257b053a6ffc796058f4f3ca7cadd031edc676f"
    inverse_raw = INVERSE.read_text(encoding="utf-8")
    inverse_body = inverse_raw.split("\n", 1)[1].lstrip()
    inverse_body = re.sub(r"(?m)^## (\d+)\. ", r"### 9.\1. ", inverse_body)
    inverse_body = inverse_body.replace("`../next_literal/LITERAL_VACUUM_COARSE_PROJECTION.md`", "Sections 1–8 of this note")
    inverse_body = inverse_body.replace("`../next_literal_common/COMMON_GAUSS_LITERAL_FAST_FLOOR.md`", "[the common-Gauss proof](G19_WILSON_COMMON_GAUSS_LITERAL_FAST_FLOOR_20260905.md)")
    inverse_body = inverse_body.replace("`check_literal_inverse_energy.py`", f"[check_literal_inverse_energy.py](../../runs/{RUN}/check_literal_inverse_energy.py)")
    inverse_append = (
        "\n## 9. Full form from the compressed inverse\n\n"
        "This separately derived continuation is appended with its original proof\n"
        "scope. The original addendum and its independent exact controls are\n"
        f"preserved in the [literal-source run](../../runs/{RUN}/README.md).\n\n"
        + inverse_body
    )
    record = {"source_root": BASE.as_posix(), "run": RUN, "files": [], "inverse_original_sha256": digest(INVERSE)}
    prepared = []
    for relative, target in SOURCES:
        source = BASE / relative
        raw = source.read_text(encoding="utf-8")
        changes = []
        def replace(old, new):
            nonlocal raw
            if old in raw:
                changes.append({"old": old, "new": new, "count": raw.count(old)})
                raw = raw.replace(old, new)
        if relative.startswith("next_literal/") and "LITERAL_VACUUM" in relative:
            replace("5 September 2026. Independent outputs-only derivation. No current canonical\nsource, native check or sealed run is changed. This note concerns the actual", "5 September 2026. Analytic true-vacuum source theorem. This note concerns the actual")
            replace("These outputs do not alter the current canonical\npackage.", "The original derivation and exact controls are preserved in the cited run.")
        replace("5 September 2026. Independent outputs-only derivation.", "5 September 2026. Analytic additive common-Gauss theorem.")
        replace("5 September 2026. Outputs-only analytic successor.", "5 September 2026. Analytic full-quantum harmonic theorem.")
        replace("5 September 2026. Outputs-only analytic successor. This note disproves", "5 September 2026. Analytic exact-score successor. This note disproves")
        # The previous generic replacement may have matched the center text;
        # specialize its label without changing any mathematical sentence.
        if "TRUE_GROUND_CENTER" in target:
            replace("5 September 2026. Analytic full-quantum harmonic theorem. This note disproves", "5 September 2026. Analytic exact-score successor. This note disproves")
        replacement_paths = {
            "[LITERAL_VACUUM_COARSE_PROJECTION.md](../next_literal/LITERAL_VACUUM_COARSE_PROJECTION.md)": "[the literal-source theorem](G19_WILSON_LITERAL_VACUUM_COARSE_SOURCES_20260905.md)",
            "`next_literal/GROUND_MARGINAL_SCHUR_SCORE.md`": "[the generic score theorem](G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md)",
            "[check_common_gauss_literal_projection.py](check_common_gauss_literal_projection.py)": f"[check_common_gauss_literal_projection.py](../../runs/{RUN}/check_common_gauss_literal_projection.py)",
        }
        for old, new in replacement_paths.items():
            replace(old, new)
        for filename in re.findall(r"`(paper/research_notes/G19_[^`]+\.md)`", raw):
            basename = Path(filename).name
            replace(f"`{filename}`", f"[{basename}]({basename})")
        for script in ("check_literal_vacuum_projection.py", "check_entire_gaussian_literal_complement.py", "check_central_score_identity_independent.py"):
            replace(f"`{script}`", f"[{script}](../../runs/{RUN}/{script})")
        replace("are the immediate preceding\noutputs.", "are the immediate preceding\nproof notes.")
        additions = []
        if "LITERAL_VACUUM_COARSE" in target:
            additions.append(inverse_append)
        elif "COMMON_GAUSS" in target:
            additions.append("""
## 7. Full Hamiltonian form and entire-window continuation

The separately proved [compressed-inverse continuation](G19_WILSON_LITERAL_VACUUM_COARSE_SOURCES_20260905.md#9-full-form-from-the-compressed-inverse)
upgrades the additive common-Gauss result to the entire form

```text
h_M >= c_u Q_M,
c_u^-1=1/t_u+max{(1/a_u-1/t_u)d_r^2,
                  (1/(2alpha_u)-1/t_u)(2d_A^2-d_A^4)}.
```

It uses the exact vacuum and the complete inverse spectral bound, with the
same orthogonal support decomposition. The coefficient tends to
`(sqrt(3)+sqrt(5))sqrt(u)` uniformly over finite and countable copies.
It differs from the sharper restricted-compression constant in (21), which
cannot automatically be assigned to a full noncommuting form. The entire
spectral window `[0,E]`, `E<c_u`, has an onto literal frame with lower bound
`1-E/c_u`. The original exact low-window Gram weights remain available.

This is an additive continuation, not an interacting or OS-range claim.
Its independent original proof is preserved with the literal-source run.
""")
        elif "GROUND_MARGINAL_SCHUR_SCORE" in target:
            anchor = "## 5. The precise Wilson target exposed by this identity\n"
            assert raw.count(anchor) == 1
            annotation = """
**Later resolution, 5 September 2026.** The displayed global sublinear
Fisher candidate in this section is retained as the proposal at this stage.
The [exact central SU(2) true-ground identity](G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md)
disproves it for the actual two-square bouquet, on open coarse neighborhoods
at sufficiently large u. Sections 1–4 of this note remain valid. The
successor gives an energy-localized integral/resolvent criterion, retaining
the high-retained-space obligation before any full-gap conclusion.

"""
            replace(anchor, anchor + annotation)
        elif "TRUE_GROUND_CENTER" in target:
            replace("the immediate preceding\noutputs", "the immediate preceding\nproof notes")
        evidence = (
            "\nThe accepted original derivation, independent audits and finite controls\n"
            f"are preserved in the [sealed evidence run](../../runs/{RUN}/README.md).\n"
            "The run's native checks retain their finite scope; the operator, domain\n"
            "and limiting statements above are analytic proofs.\n"
        )
        additions.append(evidence)
        result = raw.rstrip() + "\n" + "".join(additions)
        assert "\r" not in result
        prepared.append((OUT / target, result))
        record["files"].append({"source": source.as_posix(), "source_sha256": digest(source), "canonical": (OUT / target).as_posix(), "replacements": changes, "appendices": additions, "canonical_sha256": hashlib.sha256(result.encode("utf-8")).hexdigest()})
    # Verify reconstruction before writing, preserving every original byte.
    for item in record["files"]:
        text = Path(item["source"]).read_text(encoding="utf-8")
        for change in item["replacements"]:
            assert text.count(change["old"]) == change["count"]
            text = text.replace(change["old"], change["new"])
        rebuilt = text.rstrip() + "\n" + "".join(item["appendices"])
        assert hashlib.sha256(rebuilt.encode("utf-8")).hexdigest() == item["canonical_sha256"]
    for target, text in prepared:
        target.write_text(text, encoding="utf-8", newline="\n")
    record_path = Path(__file__).with_name("CANONICAL_LITERAL_COPY_AUDIT.json")
    record_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(f"{x['canonical']} {x['canonical_sha256']}" for x in record["files"]))


if __name__ == "__main__":
    main()
