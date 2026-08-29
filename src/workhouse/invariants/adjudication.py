from __future__ import annotations

import hashlib
import re
import sys

from .. import constants as K
from .. import settlement as S
from ._core import ROOT, _suite

# ==========================================================================
adjudication = _suite("settlement package and adjudication harness (G3)")


@adjudication.check("cold reruns re-certify both in-corpus audits", "SETTLEMENT.md §2")
def _():
    runs = S.read_cold_runs()
    ok = len(runs) == 2 and all(r.passed == r.total == 8 for r in runs)
    detail = "; ".join(f"{r.name.replace('cold_rerun_', '')} {r.passed}/{r.total}" for r in runs)
    return ok, detail


@adjudication.check("stranded-flux zero backend stays falsified (C7)", "MASTER_THEORY C7")
def _():
    run = next(r for r in S.read_cold_runs() if "stranded_flux" in r.name)
    # Cold rerun, so C7's evidence class rises from in-corpus to cold-reproduced.
    return run.verdict == "ZERO_BACKEND_FALSIFIED", (
        f"{run.passed}/{run.total}, verdict {run.verdict}; generating script "
        f"sha256 {run.source_sha256[:16]}... (the script is absent from this repo; "
        "settlement/SHA256SUMS pins the transcript, not the script)"
    )


@adjudication.check(
    "FINDING: the target-blindness scan cannot see two scalar-determining targets",
    "settlement/mce_adjudication_harness.py",
)
def _():
    audit = S.audit_contamination_scan()
    missed = audit.uncovered_scalar_determining
    # Asserting the gap, per the repository's convention for findings. When the
    # harness's CONTAMINATION_STRINGS is extended upstream this check will fail,
    # and the correct response is to retire it, not to widen it.
    return missed == {"delta_gamma", "hamer_8a4"}, (
        f"quarantined targets {len(audit.targets)}, scan strings {len(audit.strings)}; "
        f"uncovered {sorted(audit.uncovered)}. Two of those determine the disputed "
        "scalar: m_Gamma = q_band + Delta_Gamma exactly, and Hamer's 8*a_4 IS the "
        "scalar to 13 digits. The scan covers the 16-digit oracle form "
        "7751458630189173, but that string does NOT contain 7751458630184 — they "
        "diverge at index 12 — so an engine carrying either constant passes the scan. "
        "Closing it means adding 0827701250956414, 7751458630184 (and the ...417 "
        "rounding), 160506019419340168451, 7250590288602460800, 4405310420659200."
    )


@adjudication.check(
    "FINDING: the contamination scan reads only the engine file",
    "settlement/mce_adjudication_harness.py",
)
def _():
    return S.scans_a_single_file(), (
        "src = open(engine).read() — an engine that imports a helper module, loads a "
        "JSON/npz, or restores from the sqlite checkpoint carries that content past "
        "the scan entirely"
    )


@adjudication.check(
    "FINDING: the harness can never report COMPLETE",
    "settlement/mce_adjudication_harness.py",
)
def _():
    # item10_W22_toggle is assigned "OPEN (...)" unconditionally and the
    # completeness predicate rejects any OPEN value.
    return not S.verdict_can_be_complete(), (
        "protocol item 10 (W22 order-schedule toggle) is hardcoded OPEN, and the "
        "completeness predicate rejects any OPEN value, so even a certificate that "
        "discharges items 8 and 9 with a full shape block yields PARTIAL. Honest as a "
        "default, but the protocol has no path to closure until the engine exposes "
        "the toggle."
    )


@adjudication.check(
    "the harness carries the printed Delta_Gamma, not the rounded one",
    "settlement/mce_adjudication_harness.py",
    tier=2,
)
def _():
    # Byte-for-byte float equality, no tolerance — but both sides ARE floats,
    # so by this repository's own rule the check is T2 however exact it looks.
    v = S.harness_delta_gamma()
    return v == K.DELTA_GAMMA_AS_PRINTED_NUM, (
        f"harness has {v!r}, matching the corpus's printed value exactly (float identity, "
        f"not a tolerance); the correctly rounded value is {K.DELTA_GAMMA_NUM!r}. Harmless "
        "after unblinding, but if the digit string is added to the scan, add both forms."
    )


@adjudication.check("quarantined targets never reach the engine process", "GLUEBALL §18.1 item 6")
def _():
    audit = S.audit_contamination_scan()
    src = S.HARNESS.read_text(encoding="utf-8")
    # The architecture itself is sound: Q is module-local and the engine is
    # launched with a plain env, so no target is exported. The weakness audited
    # above is detection of a target already inside the engine, not leakage.
    leaks = re.findall(r"env\s*=\s*dict\(os\.environ,([^)]*)\)", src)
    exported = [seg for seg in leaks if any(t in seg for t in audit.targets)]
    return not exported, (
        f"{len(audit.targets)} targets held module-local; engine env carries only "
        "HODGE_SU3_M4_SEALED_SOURCE_FD. Quarantine architecture is sound — the gap "
        "is in detecting a target already present in the engine."
    )


@adjudication.check(
    "the engine the harness drives IS in the repository, renamed by the import",
    "corpus-import/records/RENAME_MANIFEST_2026-08-20.tsv via settlement.py",
)
def _():
    rename = S.engine_rename_record()
    on_disk = S.ENGINE.stat().st_size if S.ENGINE.exists() else -1
    first_line = S.ENGINE.read_text(encoding="utf-8", errors="ignore").splitlines()[0]
    ok = (
        rename is not None
        and rename.source.endswith("Hodge_SU3_Exact_MarkedCluster_m4_Colab.py")
        and rename.destination.endswith("DATA_SU3_Exact_MarkedCluster_m4_Colab.py")
        and rename.size == on_disk
        and "marked-cluster fourth-order engine" in first_line
    )
    sha = hashlib.sha256(S.ENGINE.read_bytes()).hexdigest()
    return ok, (
        f"rename manifest: {rename.source.split('/')[-1]} -> "
        f"{rename.destination.split('/')[-1]}, {rename.size} bytes = on-disk size; "
        f"sha256 {sha[:16]}...; the settlement package's received README records "
        "this engine as absent — that record described the filename, not the corpus"
    )


@adjudication.check(
    "the engine is clean under the harness scan AND the extended scan",
    "settlement/mce_adjudication_harness.py + the scan-gap FINDING above",
)
def _():
    hits = S.engine_scan_hits(extended=True)
    # The FINDING above stands: the harness's own list misses two
    # scalar-determining targets. This check closes the question it left open —
    # whether the engine actually carries one of the missed constants. It does
    # not: blind under both lists.
    return hits == [], (
        f"harness strings ({len(S.audit_contamination_scan().strings)}) plus "
        f"extension strings ({len(S.EXTENDED_CONTAMINATION_STRINGS)}) all absent "
        f"from the engine source; hits = {hits!r}"
    )


@adjudication.check(
    "the engine imports stdlib only, so the single-file scan bounds it",
    "settlement/mce_adjudication_harness.py + corpus engine source",
)
def _():
    roots = S.engine_import_roots()
    extras = roots - S.ENGINE_ALLOWED_IMPORTS
    # The single-file-scan FINDING above stands as a property of the harness.
    # For THIS engine the exposure is bounded: no helper module, no third-party
    # import, so nothing rides in past the scan at import time.
    return not extras, (
        f"{len(roots)} import roots, all in the allowed stdlib+sympy set; "
        f"unexpected = {sorted(extras)!r}"
    )


@adjudication.check(
    "freeze passes here: the corpus engine is behaviorally the verified one",
    "runs/mce_freeze_and_first_run_2026-08-22/FREEZE.json",
)
def _():
    fz = S.read_freeze()
    coverage_pin, preflight_pin = S.harness_preflight_pins()
    engine_sha = hashlib.sha256(S.ENGINE.read_bytes()).hexdigest()
    ok = (
        fz["contamination_scan"] == "clean"
        and fz["self_test"].startswith("47/47")
        and fz["engine_sha256"] == engine_sha
        and fz["preflight"]["candidate_coverage_certificate_sha256"] == coverage_pin
        and fz["preflight"]["preflight_sha256"] == preflight_pin
        and fz["preflight"]["total_exact_cluster_evaluations"] == 609
    )
    return ok, (
        f"self-test {fz['self_test']}; preflight coverage and output SHA256 both "
        "match the harness pins, so the imported engine reproduces the sealed "
        "geometry layer of the upstream-verified engine exactly; engine sha256 "
        f"{engine_sha[:16]}... recorded in FREEZE.json. Reproduce: harness freeze, "
        "~5 s"
    )


@adjudication.check(
    "FINDING: the run stage fail-closes on cluster 1 of 609 — the shipped "
    "closure cap is below the first cluster's own demand",
    "runs/mce_freeze_and_first_run_2026-08-22/README.md",
)
def _():
    cap = S.engine_closure_cap()
    error = S.first_run_error()
    probe = S.first_run_probe()
    ok = (
        cap == 100
        and error == "ExactEngineError: unexpectedly large H0 closure"
        and probe["cap_in_transcript"] == cap
        and probe["max_measured_closure"] > cap
        and probe["first_support_size"] == 1
    )
    return ok, (
        f"first production cluster (support size {probe['first_support_size']}) "
        f"demands an H0 orbit of {probe['max_measured_closure']} states against "
        f"the shipped cap of {cap}, inherited from the electric-resolvent "
        "lineage; the guard aborts rather than truncates, so the frozen protocol "
        "as received cannot start on any hardware. No pre-production path "
        "exercises it: the self-test contracts no real half-history, the "
        "preflight runs zero physics, and the upstream sandbox only *started* "
        "cluster 1. The orbit is finite and barely 2x the cap — an operational "
        "miscalibration, not an explosion — but even the 1-face cluster (the "
        "smallest of 609; 474 are 3-face) exceeded 13 CPU-minutes without "
        "completing, so run-stage feasibility is a cost question upstream too"
    )


@adjudication.check(
    "FINDING: the marked-cluster engine emits the Gamma scalar only — a "
    "completed 609-sweep cannot decide C_shp",
    "engine certificate assembly + harness adjudicate stage",
)
def _():
    # G3's narrowed scope (ledger/gaps.yaml) is C_shp, because the Gamma-point
    # scalar is externally validated and Phi_C(0) = 0 makes Gamma-point data
    # structurally incapable of constraining Delta_C — that incapacity is
    # already a registered T1 finding in the off-axis channel suite. This
    # check establishes the same incapacity for G3's own lead engine, by
    # static scan (text only; the pinned corpus file is never imported):
    # every coefficient the sealed sweep assembles flows through
    # _exact_gamma_scalar, and the source contains no shape, kernel,
    # band-point, or Stage-3H output of any kind. The harness knows: its
    # adjudicate stage reports items 7/8 OPEN and says the run "adjudicates
    # the SCALAR only" when the certificate carries no kernel block — which,
    # for this engine, is always.
    #
    # Consequence, recorded not asserted: completing the 609-evaluation
    # sealed sweep — at ANY cost, on any hardware — leaves C2 exactly as
    # open as it is now. What can decide C_shp is a kernel-bearing
    # (Stage-3H lineage) recomputation, or a structural comparison of the
    # two sides' recorded block decompositions. The sweep's remaining value
    # is a blind confirmation of the already-validated scalar, and its cost
    # must be weighed against that, not against C2.
    src = S.ENGINE.read_text(encoding="utf-8", errors="ignore")
    harness = (ROOT / "settlement" / "mce_adjudication_harness.py").read_text(
        encoding="utf-8", errors="ignore"
    )
    scalar_only = src.count("_exact_gamma_scalar") >= 2 and '"m4": coefficients[3]' in src
    # bare "kernel" appears once, in a docstring about translating an
    # anchored resolvent kernel — not an output; the output-shaped tokens are
    # what the harness's shape adjudicator would need to find.
    no_kernel_output = (
        not any(
            token in src
            for token in ("shape", "band_point", "kernel_shape", "Stage-3H", "stage_3h", "3895")
        )
        and src.count("kernel") == 1
    )
    harness_knows = "adjudicates the SCALAR only" in harness
    ok = scalar_only and no_kernel_output and harness_knows
    return ok, (
        "engine source: coefficients assembled via _exact_gamma_scalar "
        f"({src.count('_exact_gamma_scalar')} occurrences), certificate m4 is "
        "coefficients[3] of that Gamma ledger, and the tokens shape / "
        "band_point / kernel_shape / Stage-3H / 3895 appear nowhere in "
        f"{len(src.splitlines())} lines; the harness's own adjudicate stage "
        "reports items 7/8 OPEN without a kernel block. With the registered "
        "Phi_C(0) = 0 finding (Gamma data cannot identify C_shp), the sealed "
        "609-sweep is structurally incapable of deciding C2 — G3's decisive "
        "path is a kernel-bearing recomputation or a block-structure "
        "comparison, not this sweep"
    )


@adjudication.check(
    "the v10a.26 cold kernel shares every protected shape parameter and "
    "differs only in C — and records no per-record kernel",
    "notes/imported/HODGE_RUNS_2026-08-28/15_hour_RUN.txt §[17]",
    tier=2,
)
def _():
    # The rewritten G3's first question — does the v10a.26 side have a
    # recorded block structure? — answered from the primary source: the
    # 15-hour dual-cold-oracle transcript, imported byte-verified from the
    # maintainer's HODGE RUNS archive. Its final unblind block prints the
    # cold kernel's full shape fit next to the historical values. Parsed
    # here, not quoted: A agrees with 5/48 at 6e-14 (the registered
    # A_SHP_3_NUM is this transcript's own printed value), B and D sit at
    # fit noise, alpha is 4A, C is exactly the registered float
    # C_SHP_NEW_NUM, and the kernel carries the canonical 189 anchored
    # records. So the two rival kernels agree on every symmetry-protected
    # parameter and differ ONLY in C — which, with the registered
    # A-pins-the-normal-block result, forces any structural divergence
    # into the A-carrying sector.
    #
    # The second half is an absence, asserted as one: nothing in the
    # transcript prints a displacement-resolved record (the scan pattern
    # below), so the 189 per-record values existed only in the dead A100
    # process's memory. K4_mass_cols was computed, counted, fitted — and
    # never dumped. That is why G3 step 2 is a rerun of the kernel leg
    # instrumented to dump records, and why this check is T2: every
    # quantity here is a printed float, not an exact rational.
    import re

    path = ROOT / "notes" / "imported" / "HODGE_RUNS_2026-08-28" / "15_hour_RUN.txt"
    text = path.read_text(encoding="utf-8", errors="ignore")
    # rfind, not index: the transcript interleaves the script with its
    # output, and the first occurrence is the print statement's own source.
    block = text[text.rfind("final mass-kernel shape:") :][:800]

    def printed(name):
        m = re.search(rf"{name}\s*=\s*([+-][\d.e-]+)", block)
        return float(m.group(1)) if m else None

    a, b, c, d = printed("A"), printed("B"), printed("C_direct"), printed("D")
    alpha = printed("alpha")
    a_gap = abs(a - float(K.A_SHP_3))
    records = "final mass-kernel anchored records= 189" in text
    per_record_dump = re.findall(
        r"\(\s*-?\d\s*,\s*-?\d\s*,\s*-?\d\s*\)[^\n]{0,120}?-?\d+\s*/\s*\d+", text
    )
    ok = (
        a == K.A_SHP_3_NUM
        and a_gap < 1e-12
        and abs(b) < 1e-12
        and abs(d) < 1e-11
        and abs(alpha - 4 * a) < 1e-12
        and abs(c - K.C_SHP_NEW_NUM) < 1e-14
        and records
        and not per_record_dump
        and "MIXED/THIRD RESULT" in text
    )
    return ok, (
        f"printed cold shape: A = {a!r} (|A - 5/48| = {a_gap:.1e}, and equal to "
        f"the registered A_SHP_3_NUM), B = {b:.1e}, D = {d:.1e}, alpha - 4A = "
        f"{alpha - 4 * a:.1e}, C_direct = {c!r} (|C - C_SHP_NEW_NUM| = "
        f"{abs(c - K.C_SHP_NEW_NUM):.1e}); 189 anchored records confirmed; "
        f"displacement-resolved record lines in 682KB of transcript: "
        f"{len(per_record_dump)}; verdict line MIXED/THIRD RESULT present. "
        "Both sides recorded, neither promoted: this check establishes where "
        "the kernels AGREE, and that the cold per-record values are absent "
        "from every recorded artifact"
    )


@adjudication.check(
    "the two 189-record kernels agree everywhere except three amplitudes, "
    "and the on-site anchor swap moves C by exactly zero",
    "runs/g3_kernel_record_dump_2026-08-28 + the historical certificate",
    tier=2,
)
def _():
    # G3 step 2, executed: the cold kernel's 189 records (never previously
    # written down; reproduced on CPU in 12.3 minutes from the pinned
    # v10a.26 script, kernel leg only) against the pinned historical
    # certificate, both through ONE stdlib reimplementation of the
    # transcript's 4-point Bloch shape fit (kernel_comparison.py).
    #
    # The extractor is validated on both sides before anything structural
    # is claimed: it must return each kernel's own registered fingerprints
    # — historical C_shp and q_old (exact rationals, compared as floats),
    # the cold C_SHP_NEW_NUM, and A = 5/48 for BOTH kernels.
    #
    # The structural findings, neither side promoted:
    #   * identical 189-record support;
    #   * one scale factor s explains 144 of 189 records to ~2e-12 — the
    #     entire rotation-type bulk has identical relative structure;
    #   * the divergence is confined to the A-carrying sector the
    #     registered block result predicted: the cross-plane amplitude
    #     (24 records, ONE value per kernel, opposite sign), the nn
    #     same-plane NORMAL/IN-PLANE amplitudes (18 records), and the
    #     on-site scalar (the q_band-vs-m_Gamma anchor, ADR 0002);
    #   * the anchor difference is shape-inert: swapping the on-site
    #     diagonal alone moves C by exactly zero;
    #   * the class-swap Delta_C contributions are linear and sum to the
    #     measured C difference.
    from .. import kernel_comparison as KCMP

    r = KCMP.compare()
    sh, sc = r["shape_hist"], r["shape_cold"]
    validated = (
        r["support_hist"] == r["support_cold"]
        and len(r["support_hist"]) == 189
        and abs(sh["C"] - float(K.C_SHP_HISTORICAL)) < 1e-12
        and abs(sh["rest"] - float(K.Q_BAND_4)) < 1e-11
        and abs(sc["C"] - K.C_SHP_NEW_NUM) < 1e-12
        and abs(sh["A"] - float(K.A_SHP_3)) < 1e-11
        and abs(sc["A"] - float(K.A_SHP_3)) < 1e-11
    )
    divergent_classes = {cls: len(keys) for cls, keys in r["divergent"].items()}
    structure = (
        r["bulk_count"] == 144
        and r["bulk_spread"] < 1e-9
        and divergent_classes
        == {
            ("nn", "same"): 18,
            ("onsite", "same"): 3,
            ("nn", "cross"): 12,
            ("onsite", "cross"): 6,
            ("diag2", "cross"): 6,
        }
    )
    # the divergent cross sector is ONE number: a single cold/hist
    # multiplier across all 24 records, and the 96 remaining cross records
    # ride the bulk scale exactly.
    cross_one_number = r["cross_ratios"] == {-10.688697232} and r["small_cross_ratios"] == {1.0}
    anchor_inert = abs(r["swaps"][("onsite", "same")]) < 1e-10
    total = sum(r["swaps"].values())
    actual = sc["C"] - r["c_base"]
    linear = abs(total - actual) < 1e-9
    ok = validated and structure and cross_one_number and anchor_inert and linear
    return ok, (
        f"extractor validated on both sides: hist C = {sh['C']:.12f} "
        f"(= C_shp historical), hist rest = {sh['rest']:.12f} (= q_old), "
        f"cold C = {sc['C']:.15g} (= C_SHP_NEW_NUM), A = 5/48 both "
        f"(|dA| < 1e-11); support identical, 189 records; scale s = "
        f"{r['scale']:.12f} explains {r['bulk_count']}/189 records with "
        f"spread {r['bulk_spread']:.1e}; divergent classes "
        f"{divergent_classes}; on-site anchor swap dC = "
        f"{r['swaps'][('onsite', 'same')]:.1e} (shape-inert, ADR 0002); "
        f"divergent cross sector is one number — cold/hist = "
        f"{sorted(r['cross_ratios'])} uniform across all 24 records, and the "
        f"96 remaining cross records ride the bulk scale exactly; "
        f"class swaps sum {total:+.12f} vs measured {actual:+.12f}. The "
        "dispute is three amplitudes in the A-carrying sector; the "
        "rotation bulk is structurally shared. Neither kernel preferred"
    )


@adjudication.check(
    "FINDING: the closure cap is a third-order scaffold and fourth order needs 160",
    "engine closure(), max_states=100",
)
def _():
    # G3's run stage fail-closes on cluster 1 of 609 with
    # ExactEngineError("unexpectedly large H0 closure"). The registered finding
    # said the shipped cap is below the first cluster's own demand. It did not
    # say by how much, and "raise it" and "this needs a cheaper contraction"
    # are opposite conclusions, so the number matters.
    #
    # Measured here: the H0 closure grows geometrically with insertion depth,
    # 1, 2, 8, 32, 160. Fourth order IS depth four, so the demand is 160
    # against a cap of 100 -- short by a factor of 1.6, not by orders of
    # magnitude. The cap has every appearance of having been calibrated at
    # depth three, where 32 leaves threefold headroom, and then being hit the
    # moment the engine went to fourth order.
    #
    # The whole walk costs well under a second, which rules the closure out as
    # the reason the sweep is slow: whatever makes a full cluster expensive is
    # downstream of here, in the Haar contractions and resolvent inversions.
    #
    # The engine is NOT modified. This reimplements the same breadth-first walk
    # over the engine's own h0_action, without the cap, and produces no
    # certificate. Nothing here adjudicates C2 or licenses raising the cap in a
    # sealed run; it says what the cap would have to be.
    from collections import deque
    from importlib.util import module_from_spec, spec_from_file_location

    path = (
        ROOT
        / "corpus-import"
        / "programs"
        / "hodge_o4_adjudication"
        / "src"
        / "DATA_SU3_Exact_MarkedCluster_m4_Colab.py"
    )
    spec = spec_from_file_location("mce_engine_probe", path)
    engine = module_from_spec(spec)
    sys.modules["mce_engine_probe"] = engine
    # Importing writes __pycache__ NEXT TO the source, which here is inside
    # pinned corpus -- and an unpinned .pyc appearing in corpus-import/ fails
    # test_corpus_integrity. Running a check must not modify the corpus it
    # reads, so suppress bytecode for the duration of the import.
    previously = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(engine)
    finally:
        sys.dont_write_bytecode = previously

    def closure_size(state):
        factor, seed = engine.simplify_unitarity(state)
        if factor != 1:
            return None
        seen = {seed}
        queue = deque((seed,))
        while queue:
            for candidate in engine.h0_action(queue.popleft()):
                if candidate not in seen:
                    seen.add(candidate)
                    queue.append(candidate)
        return len(seen)

    patch, roots, _coverages, _candidate = engine.build_o4_triality_candidate_full_t1_coverage()
    builder = engine.ExactFaceInsertionBuilder(patch)
    root = roots[sorted(roots)[0]]
    vector = builder.source_axial(root)
    chain = sorted(patch.adjacency[root])[:4]

    curve = []
    for depth in range(5):
        if depth:
            vector = builder.insert_face(vector, chain[depth - 1], +1)
        sizes = [s for s in (closure_size(st) for st in vector) if s is not None]
        curve.append(max(sizes))

    cap = 100
    return curve == [1, 2, 8, 32, 160] and curve[4] > cap, (
        f"H0 closure by insertion depth: {curve}, a clean geometric growth. Fourth order is "
        f"depth 4, so the demand is {curve[4]} against the engine's shipped cap of {cap} -- "
        f"short by a factor of {curve[4] / cap:.1f}, not by orders of magnitude, and consistent "
        "with a cap calibrated at depth 3 where 32 leaves threefold headroom. The walk costs "
        "under a second, so the closure is not why the 609-cluster sweep is slow"
    )
