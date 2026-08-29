from __future__ import annotations

from .. import constants as K
from .. import payloads as P
from ._core import _suite

# ---------------------------------------------------------------------------
# Restored payloads (G1). The ledger said five payload families were "only
# record-backed". The 2026-08-21 sweep found three of them shipped in
# corpus-import/ carrying the exact reference SHAs the records quote; these
# checks bind file, digest, and content to the registry so the claim is
# machine-checked rather than asserted. Two families remain absent, and the
# FINDING checks pin exactly what is missing — including that no reference
# SHA for a tetrahedral certificate exists anywhere, so shipping cannot close
# C15 and only the G5 re-derivation can.

restored = _suite("restored payloads (G1)")


@restored.check(
    "the 189-record kernel is shipped and carries both reference SHAs", "UNIFIED §6 / G1"
)
def _():
    pins = P.corpus_pins()
    rel = str(P.KERNEL.relative_to(P.CORPUS))
    actual = P.sha256_of(P.KERNEL)
    semantic = P.semantic_sha()
    row = P.canonical_rows().get("A20K", {})
    count = len(P.kernel_records())
    ok = (
        count == 189
        and actual == P.KERNEL_FILE_SHA == pins.get(rel) == row.get("sha256")
        and semantic == P.KERNEL_SEMANTIC_SHA
        and P.kernel_is_hermitian()
    )
    return ok, (
        f"{count} records; file sha {actual[:16]}… equals manifest row A20K, the corpus pin, "
        f"and the stage-3J verdict's quote; semantic sha {semantic[:16]}… equals the SOS "
        "certificate's reference; record set exactly Hermitian under (ip,op,d) -> (op,ip,-d)"
    )


@restored.check(
    "the kernel re-derives q, alpha, beta, and the historical C_shp exactly", "UNIFIED §6 / G1"
)
def _():
    c = P.kernel_constants()
    ok = (
        c["gamma_is_scalar"] == 1
        and c["q"] == P.as_fraction(K.Q_BAND_4)
        and c["alpha"] == P.as_fraction(K.ALPHA_PEN_3)
        and c["beta"] == P.as_fraction(K.BETA_PEN_3)
        and c["C_shp"] == P.as_fraction(K.C_SHP_HISTORICAL)
        and c["c_R"] == 2 * c["c_M"] - c["c_X"]
        and c["bandwidth"] == P.as_fraction(K.ALPHA_PEN_3) + P.as_fraction(K.BETA_PEN_3)
    )
    return ok, (
        f"H(Gamma) = q I with q = {c['q']} = q_band^(4); c_X - q = {c['alpha']} = alpha_pen(3); "
        f"2(c_M - c_X) = {c['beta']} = beta_pen_3; (beta - 2 alpha)/16 = {c['C_shp']} = "
        "C_shp (historical); c_R = 2 c_M - c_X (the pencil relation, on the raw records); "
        f"bandwidth = {c['bandwidth']}"
    )


@restored.check(
    "three kernel copies agree record-for-record, from two independent builds", "UNIFIED §6 / G1"
)
def _():
    record_sets = [dict(P.kernel_records(p)) for p in P.KERNEL_COPIES]
    identical = all(rs == record_sets[0] for rs in record_sets[1:])
    upstream = P.stage3i_hashes()
    return identical and len(upstream) == 2, (
        f"{len(P.KERNEL_COPIES)} shipped copies, {len(record_sets[0])} records each, "
        f"record-identical; meta names {len(upstream)} distinct upstream Stage-3I hashes "
        "(one a from-scratch rebuild), so the copies are independent builds of one content"
    )


@restored.check("the Q_32 ledger is the Newton transcript of the compact q law", "UNIFIED §8 / G1")
def _():
    v = P.q32_verification()
    quoted = P.walled_brauer()["q"]
    ok = (
        v["matches"]
        and (v["count"], v["positive"], v["zero"], v["negative"]) == (40, 33, 7, 0)
        and v["ledger_sha"] == quoted["newton_ledger_sha256"]
        and v["note_sha"] == quoted["compact_formula_sha256"]
    )
    return ok, (
        f"all {v['count']} coefficients equal the forward differences of Q32 at z = {v['base']}: "
        f"{v['positive']} positive, {v['zero']} zero tail, {v['negative']} negative; ledger and "
        "formula files hash-match the walled-Brauer certificate's quotes"
    )


@restored.check("the P_402 ledger is the Newton transcript of B_N * D_409", "UNIFIED §8 / G1")
def _():
    v = P.p402_verification()
    quoted = P.walled_brauer()["B"]
    ok = (
        v["matches"]
        and (v["count"], v["positive"], v["zero"], v["negative"]) == (424, 403, 21, 0)
        and v["last_nonzero"] == 402
        and v["ledger_sha"] == quoted["newton_coefficients_sha256"]
        and v["note_sha"] == quoted["structured_expression_sha256"]
    )
    return ok, (
        f"all {v['count']} coefficients equal the forward differences of B_N * D_409(N) at "
        f"N = {v['base']}, with B_N evaluated exactly from the structured 80-term expression: "
        f"{v['positive']} positive, {v['zero']} zero tail, degree {v['last_nonzero']}; ledger "
        "and expression files hash-match the walled-Brauer certificate's quotes"
    )


@restored.check(
    "q_N < 0 and beta_pen_N > 0 for every integer N >= 7 follow from the ledgers", "UNIFIED §8 / G1"
)
def _():
    signs = P.denominator_sign_certificate()
    q = P.q32_verification()
    b = P.p402_verification()
    ok = (
        signs["d34"]
        and signs["d409"]
        and q["negative"] == 0
        and q["positive"] > 0
        and b["negative"] == 0
        and b["positive"] > 0
    )
    return ok, (
        "no D34 factor has a real root at z >= 49 and no D409 factor at N >= 7, all leading "
        "coefficients positive, so both denominators are positive on the stable range; Newton "
        "nonnegativity with a positive lead then gives Q32(N^2) > 0 and P_402(N) > 0, hence "
        f"q_N = -(2/3N) Q32/D34 < 0 and beta_pen_N = P_402/D_409 > 0 for every integer N >= 7 "
        f"({signs['d409_factors']} denominator factors checked exactly)"
    )


@restored.check(
    "the stored fixed-rank q samples N = 7..18 match the compact law exactly", "UNIFIED §8 / C17"
)
def _():
    v = P.fixed_rank_verification()
    ok = v["all_match"] and v["count"] == 12 and v["ranks"] == list(range(7, 19))
    return ok, (
        f"{v['count']} stored samples at N = {v['ranks'][0]}..{v['ranks'][-1]}, each equal to "
        "-(2/3N) Q32(N^2)/D34(N^2) as an exact rational — the machine half of C17's resolution"
    )


@restored.check(
    "the SU(6) determinant correction is exactly 6/343 and momentum-independent",
    "GCSG (Aug 8) / C16",
)
def _():
    from fractions import Fraction

    cert = P.su6()
    balanced, full = cert["balanced_N6"], cert["full_SU6"]
    shifts = {key: Fraction(full[key]) - Fraction(balanced[key]) for key in ("q", "X", "M", "R")}
    unchanged = all(balanced[key] == full[key] for key in ("A", "B", "bandwidth"))
    ok = (
        all(shift == P.as_fraction(K.DELTA_Q_6) for shift in shifts.values())
        and unchanged
        and cert["gates"]["passed"]
        and cert["exceptional_geometry"]["determinant_permutation_terms"] == 720
    )
    return ok, (
        "full_SU6 minus balanced_N6 equals 6/343 at q, X, M, and R while A, B, and the "
        "bandwidth are unchanged — the determinant correction is a scalar shift, re-derived "
        "from the shipped certificate; 720 determinant permutation terms, 11/11 gates"
    )


@restored.check(
    "the SU(5) stage-1 scan is shipped: 895,524 pairs, zero determinant sectors",
    "GCSG (Aug 8) / C16",
)
def _():
    cert = P.stage1()
    geometry = cert["geometry"]
    ok = (
        geometry["candidate_support_output_pairs"] == 895524
        and cert["local_haar"]["epsilon_or_determinant_sectors"] == 0
        and geometry["exact_balance_sign_assignments"] == 33500
        and cert["passed"] is True
    )
    return ok, (
        "895,524 candidate support/output pairs with 0 epsilon-or-determinant sectors — the "
        "recorded SU(5) mod-5 emptiness, from the pinned stage-1 summary; 33,500 exact-balance "
        "sign assignments, passed: true"
    )


@restored.check(
    "FINDING: manifest row A60 names the pentagonal dual-cold bundle, and the tree lacks it",
    "UNIFIED §9.3 / G1",
)
def _():
    bundle = P.canonical_rows().get("A60", {})
    frontier = P.canonical_rows().get("A60F2", {})
    frontier_path = (
        "numerics/certificates/RUN_PENT_pentagonal_o4_minimal_representation_frontier_results.json"
    )
    frontier_shipped = P.corpus_pins().get(frontier_path) == frontier.get("sha256")
    absent = not P.pinned_paths_matching(r"pentagonal_o4_dual_cold")
    ok = (
        bundle.get("sha256") == "f2a8b30de1ba5f23f34c10a3102c42f000ca23f8f7eb1bbfdd9b068bb14da54a"
        and bundle.get("size") == "111743"
        and absent
        and frontier_shipped
    )
    return ok, (
        "the frontier certificate (row A60F2) IS shipped and hash-matched, but the dual-cold "
        "bundle (row A60, 111743 bytes) is not: any restoration must hash to "
        f"{bundle.get('sha256', '?')}; until then h_4^side, A_+, and A_- stay record-backed "
        "and their registry identities are the only machine evidence"
    )


@restored.check(
    "FINDING: no tetrahedral certificate exists, and no reference SHA is recorded for one",
    "corpus THM_FLUX_hodge_cellular_circuit_mobility_theorem.md / C15",
)
def _():
    in_corpus = P.pinned_paths_matching(r"tetrahedr")
    in_manifest = [
        row_id
        for row_id, row in P.canonical_rows().items()
        if "tetrahedr" in (row.get("path", "") + row.get("description", "")).lower()
    ]
    return not in_corpus and not in_manifest, (
        "no pinned path and no canonical-manifest row mentions a tetrahedral artifact, and no "
        "digest for one is recorded anywhere — so C15 cannot be closed by shipping; only the "
        "G5 re-derivation of the claimed -8/(N(N^2-1)) can close it"
    )
