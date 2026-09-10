"""Replay SC17 exact controls while preserving the analytic and continuum boundary."""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

from workhouse.check_cache import fingerprint
from workhouse.invariants.wilson_sc17 import sc17

ROOT = Path(__file__).resolve().parents[1]


def main():
    controls = [vars(result) for result in sc17.run()]
    assert len(controls) == 9 and all(result["passed"] for result in controls)
    names = [
        "docs/derivations/wilson-sc17-spatial-closure.md",
        "docs/derivations/wilson-sc17-thermodynamic-limit.md",
        "docs/derivations/wilson-sc17-physical-time-limit.md",
        "docs/validation/wilson-sc17-independent-review.md",
        "docs/validation/wilson-sc17-bc2-update-audit.md",
        "docs/validation/wilson-sc17-late-ledger-audit.md",
        "docs/validation/wilson-g19-corpus-reconciliation.md",
        "docs/validation/wilson-g19-corpus-inventory.json",
        "docs/validation/wilson-g19-corpus-review-manifest.json",
        "docs/validation/wilson-g19-gaussian-review.md",
        "docs/validation/wilson-g19-sources-review.md",
        "docs/validation/wilson-g19-fibers-review.md",
        "docs/validation/wilson-g19-cauchy-repair.md",
        "docs/validation/wilson-g19-martingale-repair.md",
        "docs/validation/wilson-g19-review-2026-09-09.json",
        "notes/imported/UPLOADS_2026-09-01/Continuum_Combined.lean",
        "docs/derivations/wilson-true-blocks-independent-check.md",
        "docs/derivations/yangmills-continuum-balaban-multiscale-proof.md",
        "docs/derivations/wilson-background-covariance-continuation.md",
        "src/workhouse/invariants/wilson_sc17.py",
        "src/workhouse/invariants/wilson_background.py",
        "src/workhouse/invariants/__init__.py",
        "scripts/validate_wilson_sc17.py",
        "scripts/validate_wilson_g19_review.py",
        "ledger/documents.yaml",
        "ledger/gaps.yaml",
        "ledger/theorems.yaml",
        "lean/Workhouse/Basic.lean",
        "docs/validation/wilson-sc17-lean-build.txt",
        "docs/validation/wilson-sc17-lean-axioms.txt",
        "index/claims.jsonl",
        "index/graph.jsonl",
        "FRONTIER.md",
        "CERTIFIED.md",
    ]
    test_runs = []
    for path in sorted((ROOT / "docs/validation").glob("wilson-sc17-*.xml")):
        suites = ET.parse(path).findall(".//testsuite")
        counts = {
            key: sum(int(suite.get(key, "0")) for suite in suites)
            for key in ("tests", "failures", "errors", "skipped")
        }
        assert counts["failures"] == 0 and counts["errors"] == 0, path
        test_runs.append(
            {
                "file": path.name,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                **counts,
            }
        )
    assert len(test_runs) == 3, "Expected ledger, invariant and graph/freshness test records"
    lean_build = (ROOT / "docs/validation/wilson-sc17-lean-build.txt").read_text(encoding="utf-8")
    lean_complete = re.search(r"Build completed successfully \((\d+) jobs\)", lean_build)
    assert lean_complete, "The compiled Lean build log must report success"
    lean_axioms = []
    for name, payload in re.findall(
        r"'Workhouse\.([^']+)' depends on axioms: \[([^\]]*)\]",
        (ROOT / "docs/validation/wilson-sc17-lean-axioms.txt").read_text(encoding="utf-8"),
    ):
        axioms = [item.strip() for item in payload.split(",") if item.strip()]
        assert set(axioms) <= {"propext", "Classical.choice", "Quot.sound"}
        lean_axioms.append({"theorem": name, "axioms": axioms})
    assert len(lean_axioms) == 8 and len({item["theorem"] for item in lean_axioms}) == 8
    catalogue = [
        json.loads(line) for line in (ROOT / "index/claims.jsonl").read_text("utf-8").splitlines()
    ]
    native_checks = [item for item in catalogue if item["kind"] == "check"]
    assert native_checks and all(item["status"] == "passing" for item in native_checks)
    report = {
        "recorded_at": datetime.now(UTC).isoformat(),
        "scope": (
            "Nine active exact finite controls: the original eight plus the later supplied "
            "3x3 periodic scalar massless-reference control, independently read and replayed. "
            "The analytic proof has a separate independent review. "
            "Eight supplied Lean arithmetic lemmas (six SC17, two Brownian-slab budgets) "
            "were separately compiled with lake build --wfail and registered without "
            "promoting the analytic theorems. "
            "The actual finite periodic cubic SU(2) vacuum Hessian has exponential spatial "
            "summability for 0<=lambda<lambda_c, the proved threshold in (1/73,1/72), L>=3. "
            "At lambda<=1/73 the weighted row is at most 2/7 at weight 1025/1024; true "
            "conditional scores give angle row<=10658/24923, C_AT<=24923/14265<7/4 "
            "and the direct physical gap is at least (49846/37303)epsilon>4epsilon/3. "
            "The narrower lambda<=1/640 corollary retains weighted row<=1/64 at weight "
            "17/16, C_AT<=1567/1542 and physical gap>57epsilon/20. "
            "The analytic cut-response continuation constructs canonical fixed-coupling "
            "thermodynamic vacuum laws through lambda_c by endpoint continuity. Uniform "
            "scores give a closable cylinder-gradient form, a conservative self-adjoint "
            "generator with full/physical gap>=4epsilon/3, and plaquette spectral weight "
            ">=exp(-24pi lambda)/8 in [4epsilon/3,32epsilon exp(24pi lambda)]. "
            "The matrix norm is operator norm. The controls do not formalize the "
            "Markov propagator, analytic domains, Bochner, disintegration or infinite-form "
            "proofs in Lean. A separately reviewed Hilbert SDE and coordinate-martingale "
            "argument identifies actual free/periodic multitime vacuum limits with "
            "exp(-t K_mu), through lambda_c, without an operator-core assumption. "
            "This fixed-spacing analytic result does not certify continuum source matching "
            "or an isolated complete shell."
        ),
        "controls": controls,
        "test_runs": test_runs,
        "written_native_catalogue": {
            "passing": len(native_checks),
            "total": len(native_checks),
            "claims": len(catalogue),
            "input_fingerprint": fingerprint(),
        },
        "lean_build_jobs": int(lean_complete.group(1)),
        "supplied_lean_lemma_audit": lean_axioms,
        "remaining_derivation": (
            "The absolute-norm Volterra barrier has threshold lambda_c in (1/73,1/72), "
            "with polynomial 6561lambda^4+1458lambda^3-81lambda^2-72lambda+1. "
            "At lambda=1/72 its discriminant is -47/2304. "
            "The signed background alternative is proved conditionally: on actual compatible "
            "fibers establish the strict reference angle margin and the complete nonlinear "
            "excess ||(V_B-V_0)''+(W_B-W_0)''||_(s,infty)<=delta with "
            "2 beta_s(A)^2 delta/epsilon<1. Moving-projector, actual metric, cutoff and "
            "retained Schur corrections must be included when present. Those actual "
            "Wilson inputs and continuum carrier/source transport are not discharged. "
            "The broader G19 review supplies beta_s(A)<=sqrt(33)L C_s^2/v for the "
            "flat conditioned Gaussian reference at fixed blocking ratio, and exact "
            "V_0''+W_0''=2epsilon A^2 including the coupled cross block. "
            "The specific Balaban construction stops at (7.6) to Theorem 7.1: O(1/k) "
            "increments do not imply a Cauchy limit. Summable changes of the actual "
            "matched RG and observable/source maps are a sufficient repair not yet proved."
        ),
        "artifacts_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in names
        },
    }
    target = ROOT / "docs/validation/wilson-sc17-2026-09-09.json"
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{len(controls)} exact controls passed; {target}")


if __name__ == "__main__":
    main()
