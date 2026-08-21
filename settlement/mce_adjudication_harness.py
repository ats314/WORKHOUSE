#!/usr/bin/env python3
"""mce_adjudication_harness.py — frozen-protocol driver for the fourth-order adjudication.

Wraps Hodge_SU3_Exact_MarkedCluster_m4_Colab.py (the target-blind marked-cluster
engine, "MCE") and enforces the GLUE3 v3.1 Section 18.1 protocol mechanically
wherever a script can. Comparison targets live ONLY in this file, in the
QUARANTINE block below; they are never passed to the engine, and the harness
refuses to adjudicate a certificate produced from an engine source that
contains any of them.

Usage (three phases, in order):

  python3 mce_adjudication_harness.py --engine mce.py freeze
      Stage 0-4: environment record, engine SHA-256, engine self-test (47 gates),
      geometry preflight (609 evaluations, zero physics), target-contamination
      scan. Writes FREEZE.json. Fast (minutes).

  python3 mce_adjudication_harness.py --engine mce.py run
      Stage 5: the sealed physical sweep. Requires FREEZE.json whose engine hash
      matches the current file. Long (hours-days; run on your production box;
      resumable via the engine's sqlite checkpoint). Produces the certificate
      JSON and expects the engine to print PASS_TARGET_BLIND_M4_SEALED.

  python3 mce_adjudication_harness.py --engine mce.py adjudicate
      Stage 6: loads the certificate, verifies hashes against FREEZE.json,
      and ONLY THEN unquarantines the comparison targets and prints the verdict:
      which scalar anchor the sealed m4 matches, the vacuum-ledger test
      q_old - E0^(4) =? m4 when the certificate carries E0^(4), and the shape
      adjudication (A =? 5/48, B,D =? 0, C vs C_old vs C_new, blind R holdout
      lam_R = 2 lam_M - lam_X) when the certificate carries kernel/shape data.
      Writes ADJUDICATION_MANIFEST.json.

Protocol coverage (GLUE3 18.1 items -> enforcement):
   1 canonical u + erratum      -> engine-internal; recorded in FREEZE
   2 occurrence schedule        -> engine self-test gates (P->W1->R1->W2->R2)
   3 609 evaluations + Moebius  -> --authorized-cluster-evaluations 609 + engine ledger
   4 vacuum-subtracted subtraction -> engine design; self-test gated
   5 sealed hashes              -> FREEZE.json (engine, preflight, certificate)
   6 no targets in data flow    -> contamination scan + quarantine architecture
   7 cold Stage-3H 189-record kernel  -> checked in certificate; else reported OPEN
   8 X/M fit + blind R holdout  -> adjudicator, if kernel present; else OPEN
   9 scalar ledger q_old - E0^(4) =? m4 -> adjudicator, if E0^(4) present; else OPEN
  10 W22 order-schedule toggle  -> reported OPEN unless engine exposes the toggle
  11 m4 and C from one run      -> checked in certificate content

Items reported OPEN are not silently skipped: the verdict is labeled PARTIAL
until every item is discharged.
"""
from __future__ import annotations
import argparse, hashlib, json, os, platform, re, subprocess, sys, time
from fractions import Fraction

AUTH_EVALS = 609
AUTH_COVERAGE_SHA = "4e7f5acfd5610a2bd434e88f94c6ba2ba12a258e618a1249f49472f76c5dbd73"
EXPECT_PREFLIGHT_SHA = "576a4a3f00a41f1805fd015836107fb27ebc44190bd57629c13c17cc28e9f16f"
FREEZE = "FREEZE.json"
MANIFEST = "ADJUDICATION_MANIFEST.json"
CERT_DEFAULT = "HODGE_SU3_EXACT_MARKED_CLUSTER_M4_CERTIFICATE.json"
CKPT_DEFAULT = "HODGE_SU3_EXACT_MARKED_CLUSTER_M4_CHECKPOINT.sqlite"

# ---------------------------------------------------------------------------
# QUARANTINE — comparison targets. Never exported to the engine process.
# Sources: RUN15 unblind block; T1PM Section 10; GLUE3 Sections 8-10.
# ---------------------------------------------------------------------------
Q = {
    "m_gamma_run15": Fraction(-7751458630189173, 10**16),          # -0.7751458630189173
    "q_old": Fraction(-20721577909065127111, 7250590288602460800), # historical kernel
    "quarantined_shortcut": Fraction(-160506019419340168451, 14501180577204921600),
    "C_old": Fraction(-211835444920651, 4405310420659200),
    "C_new_float": -0.020213328886166577,
    "A_target": Fraction(5, 48),
    "alpha_target": Fraction(5, 12),
    "hamer_8a4": -0.7751458630184,   # transcription-caveat applies (GLUE3 2.3)
    "delta_gamma": 2.0827701250956414,
}
# strings that must NOT appear in the engine source (target blindness scan)
CONTAMINATION_STRINGS = [
    "7751458630189173", "20721577909065127111", "211835444920651",
    "020213328886166577", "0968932328773", "17607806155349",
    "132329431693349", "2857915988",
]

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for ch in iter(lambda: f.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()

def run(cmd, timeout=None, log=None):
    print("  $", " ".join(cmd))
    t0 = time.time()
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    out = p.stdout + p.stderr
    if log:
        with open(log, "w") as f:
            f.write(out)
    print(f"    exit={p.returncode}  ({time.time()-t0:.1f}s)  log={log}")
    return p.returncode, out

def stage_freeze(engine):
    rec = {"stage": "freeze", "time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "python": sys.version, "platform": platform.platform(),
           "engine_path": os.path.abspath(engine), "engine_sha256": sha256_file(engine)}
    # Stage 4 first (cheap): contamination scan — engine must be target-blind
    src = open(engine, errors="ignore").read()
    hits = [s for s in CONTAMINATION_STRINGS if s in src]
    if hits:
        print("[FAIL] target-contamination scan: engine source contains target constants:", hits)
        sys.exit(1)
    print("[PASS] target-contamination scan: engine source is free of all quarantined constants")
    rec["contamination_scan"] = "clean"
    # Stage 1: self-test
    rc, out = run([sys.executable, engine, "--self-test"], timeout=3600, log="harness_selftest.log")
    ok = rc == 0 and "PHASE3" in out and "FAIL" not in out
    m = re.search(r"(\d+)/(\d+)\s+exact Phase-2/Phase-3 gates passed", out)
    if not ok or not m or m.group(1) != m.group(2):
        print("[FAIL] engine self-test"); sys.exit(1)
    print(f"[PASS] engine self-test {m.group(0)}")
    rec["self_test"] = m.group(0)
    # Stage 2: manifest
    rc, out = run([sys.executable, engine, "--show-manifest"], timeout=600, log="harness_manifest.log")
    rec["engine_manifest_head"] = out[:2000]
    # Stage 3: geometry preflight (zero physics)
    rc, out = run([sys.executable, engine, "--geometry-preflight"], timeout=3600,
                  log="harness_preflight.log")
    ok = rc == 0 and "TRIALITY_CANDIDATE_PREFLIGHT_PASS_609_NO_PHYSICS" in out
    jm = re.search(r"\{.*\}", out, re.S)
    pj = json.loads(jm.group(0)) if jm else {}
    checks = [ok,
              pj.get("total_exact_cluster_evaluations") == AUTH_EVALS,
              pj.get("candidate_coverage_certificate_sha256") == AUTH_COVERAGE_SHA,
              pj.get("preflight_sha256") == EXPECT_PREFLIGHT_SHA,
              pj.get("physics_contractions_run") == 0]
    if not all(checks):
        print("[FAIL] geometry preflight", checks); sys.exit(1)
    print("[PASS] geometry preflight: 609 evaluations sealed, coverage SHA matches, zero physics")
    rec["preflight"] = {k: pj.get(k) for k in
                        ("total_exact_cluster_evaluations", "candidate_coverage_certificate_sha256",
                         "preflight_sha256", "candidate_manifest_sha256", "patch_face_count")}
    json.dump(rec, open(FREEZE, "w"), indent=2, sort_keys=True)
    print(f"FROZEN -> {FREEZE}  (engine sha256 {rec['engine_sha256'][:16]}...)")

RESUME_SECRET_FILE = "RESUME_SECRET.json"   # chmod 600; required to resume a run

def _launch_sealed(engine, output, checkpoint, extra_minutes=None):
    """Recreate the engine's authenticated-execution environment:
    sealed auth memfd + empty certificate memfd + sealed source fd, then exec.
    Returns (returncode, tail_of_log)."""
    import fcntl, secrets, importlib.util, ctypes
    spec = importlib.util.spec_from_file_location("mce_engine", engine)
    eng = importlib.util.module_from_spec(spec)
    sys.modules["mce_engine"] = eng       # required for dataclass introspection
    spec.loader.exec_module(eng)          # import stops before physics (engine docstring)
    runtime_sha = sha256_file(engine)
    context = eng.resume_authentication_context_sha256(runtime_sha)
    # persist/reuse resume credentials so the sqlite checkpoint remains resumable
    if os.path.exists(RESUME_SECRET_FILE):
        cred = json.load(open(RESUME_SECRET_FILE))
        if cred.get("context") != context:
            print("[FAIL] RESUME_SECRET.json belongs to a different engine/context; "
                  "delete it (fresh run) or restore the matching engine."); sys.exit(1)
    else:
        cred = {"recovery_secret": "HODGE-M4-v1-" + secrets.token_hex(32),
                "resume_salt_hex": secrets.token_hex(32),
                "resume_run_id": secrets.token_hex(32),
                "context": context}
        json.dump(cred, open(RESUME_SECRET_FILE, "w"), indent=2)
        os.chmod(RESUME_SECRET_FILE, 0o600)
        print(f"  new resume credentials -> {RESUME_SECRET_FILE} (chmod 600; keep to resume)")
    key = eng.derive_resume_authentication_key(
        cred["recovery_secret"], cred["resume_salt_hex"], cred["resume_run_id"], context)
    # certificate output memfd: empty, UNSEALED, allow sealing later by the engine
    out_fd = os.memfd_create("hodge_su3_certificate_output_v1", os.MFD_ALLOW_SEALING)
    bundle = {"schema": eng.RESUME_AUTH_SCHEMA, "key_hex": key.hex(),
              "resume_salt_hex": cred["resume_salt_hex"],
              "resume_run_id": cred["resume_run_id"],
              "authentication_context_sha256": context,
              "invocation_nonce": secrets.token_hex(32),
              "certificate_output_fd": out_fd}
    auth_fd = os.memfd_create("hodge_su3_resume_auth_v1", os.MFD_ALLOW_SEALING)
    os.write(auth_fd, json.dumps(bundle, sort_keys=True,
                                 separators=(",", ":")).encode())
    fcntl.fcntl(auth_fd, fcntl.F_ADD_SEALS,
                fcntl.F_SEAL_WRITE | fcntl.F_SEAL_SHRINK | fcntl.F_SEAL_GROW | fcntl.F_SEAL_SEAL)
    src_fd = os.open(engine, os.O_RDONLY)
    env = dict(os.environ, **{ "HODGE_SU3_M4_SEALED_SOURCE_FD": str(src_fd) })
    cmd = [sys.executable, f"/proc/self/fd/{src_fd}", "--run-phase3-physical",
           "--output", output, "--checkpoint", checkpoint,
           "--authorized-cluster-evaluations", str(AUTH_EVALS),
           "--authorized-candidate-certificate-sha256", AUTH_COVERAGE_SHA]
    print("  $", " ".join(cmd))
    with open("harness_production.log", "ab") as lg:
        p = subprocess.Popen(cmd, stdout=lg, stderr=lg, env=env,
                             pass_fds=(auth_fd, out_fd, src_fd))
        try:
            rc = p.wait()
        except KeyboardInterrupt:
            p.terminate(); p.wait()
            print("\n  interrupted — checkpoint retained; re-run `run` to resume.")
            sys.exit(130)
    # keep the authenticated memfd copy of the certificate alongside the file copy
    try:
        size = os.fstat(out_fd).st_size
        if size:
            data = os.pread(out_fd, size, 0)
            with open(output + ".memfd_copy.json", "wb") as f:
                f.write(data)
    finally:
        for fd in (auth_fd, out_fd, src_fd):
            try: os.close(fd)
            except OSError: pass
    tail = ""
    try:
        with open("harness_production.log", "rb") as f:
            f.seek(max(0, os.fstat(f.fileno()).st_size - 4000)); tail = f.read().decode(errors="ignore")
    except OSError:
        pass
    return rc, tail

def stage_run(engine, output, checkpoint):
    if not os.path.exists(FREEZE):
        print("[FAIL] no FREEZE.json — run `freeze` first"); sys.exit(1)
    fz = json.load(open(FREEZE))
    if fz["engine_sha256"] != sha256_file(engine):
        print("[FAIL] engine changed since freeze — re-freeze"); sys.exit(1)
    if os.name != "posix" or not hasattr(os, "memfd_create"):
        print("[FAIL] the engine's authenticated launch needs Linux (memfd + /proc). "
              "Run this stage on the production box."); sys.exit(1)
    print("Launching sealed physical sweep (resumable; interrupt freely, re-run to resume).")
    rc, tail = _launch_sealed(engine, output, checkpoint)
    if rc != 0 or "PASS_TARGET_BLIND_M4_SEALED" not in tail:
        print("[FAIL] production did not seal (see harness_production.log tail below). "
              "If it was interrupted, re-run this stage; the sqlite checkpoint resumes.")
        print(tail[-1500:])
        sys.exit(1)
    fz["certificate_path"] = os.path.abspath(output)
    fz["certificate_sha256"] = sha256_file(output)
    fz["sealed"] = True
    json.dump(fz, open(FREEZE, "w"), indent=2, sort_keys=True)
    print(f"[PASS] SEALED. certificate sha256 {fz['certificate_sha256'][:16]}...  Now run `adjudicate`.")

def _to_fraction(x):
    if isinstance(x, str) and "/" in x:
        n, d = x.split("/"); return Fraction(int(n), int(d))
    if isinstance(x, (int,)):
        return Fraction(x)
    if isinstance(x, str):
        try: return Fraction(x)
        except Exception: return None
    return None

def stage_adjudicate(engine, output):
    if not os.path.exists(FREEZE):
        print("[FAIL] no FREEZE.json"); sys.exit(1)
    fz = json.load(open(FREEZE))
    if not fz.get("sealed"):
        print("[FAIL] certificate not sealed by this harness — run `run` first"); sys.exit(1)
    if fz["engine_sha256"] != sha256_file(engine):
        print("[FAIL] engine changed since freeze"); sys.exit(1)
    if fz["certificate_sha256"] != sha256_file(output):
        print("[FAIL] certificate file changed since sealing"); sys.exit(1)
    cert = json.load(open(output))
    print("Certificate verified against freeze. UNQUARANTINING comparison targets now.\n")
    verdict = {"protocol": {}, "scalar": {}, "shape": {}}
    # --- scalar ---
    m4 = None
    for key in ("m4", "coefficient", "m4_rest", "seal_coefficient"):
        if key in cert: m4 = _to_fraction(cert[key]) or cert[key]; break
    if m4 is None:
        # search nested
        def find(d):
            if isinstance(d, dict):
                for k, v in d.items():
                    if k in ("m4", "m4_rest", "coefficient"):
                        return v
                    r = find(v)
                    if r is not None: return r
            elif isinstance(d, list):
                for v in d:
                    r = find(v)
                    if r is not None: return r
            return None
        m4 = find(cert)
    if m4 is None:
        print("[FAIL] certificate contains no m4 coefficient"); sys.exit(1)
    m4f = float(m4 if not isinstance(m4, Fraction) else m4)
    anchors = {"RUN15 linked oracle": float(Q["m_gamma_run15"]),
               "historical q_old": float(Q["q_old"]),
               "quarantined shortcut": float(Q["quarantined_shortcut"])}
    dists = {k: abs(m4f - v) for k, v in anchors.items()}
    best = min(dists, key=dists.get)
    print(f"SEALED m4 = {m4}  (float {m4f:.15f})")
    for k, v in sorted(dists.items(), key=lambda kv: kv[1]):
        print(f"  |m4 - {k}| = {v:.3e}")
    verdict["scalar"] = {"m4": str(m4), "nearest_anchor": best, "distances": dists}
    # vacuum-ledger hypothesis (protocol item 9)
    e0 = None
    for key in ("E0_4", "vacuum_e4", "E0_fourth_order", "e0_4"):
        if key in cert: e0 = _to_fraction(cert[key]); break
    if e0 is not None:
        lhs = float(Q["q_old"]) - float(e0)
        print(f"  vacuum-ledger test: q_old - E0^(4) = {lhs:.15f} vs m4 -> |diff| = {abs(lhs-m4f):.3e}")
        verdict["protocol"]["item9_vacuum_ledger"] = abs(lhs - m4f)
    else:
        print("  [OPEN] item 9: certificate carries no E0^(4); vacuum-ledger test not discharged")
        verdict["protocol"]["item9_vacuum_ledger"] = "OPEN"
    # --- shape ---
    shp = cert.get("shape") or cert.get("kernel_shape") or {}
    if shp:
        A = float(_to_fraction(shp.get("A")) or shp.get("A"))
        C = float(_to_fraction(shp.get("C")) or shp.get("C"))
        B = float(shp.get("B", 0.0)); D = float(shp.get("D", 0.0))
        print(f"shape: A={A} B={B} C={C} D={D}")
        print(f"  |A - 5/48| = {abs(A - float(Q['A_target'])):.3e};  |B|,|D| = {abs(B):.1e},{abs(D):.1e}")
        dC_old = abs(C - float(Q["C_old"])); dC_new = abs(C - Q["C_new_float"])
        print(f"  |C - C_old| = {dC_old:.3e}   |C - C_new| = {dC_new:.3e}")
        verdict["shape"] = {"A": A, "B": B, "C": C, "D": D,
                            "dC_old": dC_old, "dC_new": dC_new,
                            "verdict": ("HISTORICAL" if dC_old < 1e-9 else
                                        "RUN15-FOLDED" if dC_new < 1e-9 else "THIRD VALUE")}
        # blind R holdout, if band points present
        pts = cert.get("band_points") or {}
        if all(k in pts for k in ("X", "M", "R")):
            lX, lM, lR = (float(_to_fraction(pts[k]) or pts[k]) for k in ("X", "M", "R"))
            print(f"  blind R holdout: |lam_R - (2 lam_M - lam_X)| = {abs(lR - (2*lM - lX)):.3e}")
            verdict["protocol"]["item8_R_holdout"] = abs(lR - (2*lM - lX))
        else:
            verdict["protocol"]["item8_R_holdout"] = "OPEN (no band points in certificate)"
    else:
        print("[OPEN] items 7/8/11: certificate carries no kernel/shape block — this run "
              "adjudicates the SCALAR only; the C^shp adjudication still requires the "
              "engine's kernel output (Stage-3H) from the same sealed run.")
        verdict["shape"] = "OPEN"
    verdict["protocol"]["item10_W22_toggle"] = "OPEN (engine exposes no toggle flag)"
    complete = all(v not in ("OPEN",) and not (isinstance(v, str) and v.startswith("OPEN"))
                   for v in verdict["protocol"].values()) and verdict["shape"] != "OPEN"
    verdict["status"] = "COMPLETE" if complete else "PARTIAL (open items listed above)"
    out = {"freeze": fz, "verdict": verdict,
           "targets_used_after_unsealing_only": {k: str(v) for k, v in Q.items()}}
    json.dump(out, open(MANIFEST, "w"), indent=2, sort_keys=True, default=str)
    print(f"\nVERDICT STATUS: {verdict['status']}")
    print(f"manifest -> {MANIFEST}")

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--engine", required=True, help="path to Hodge_SU3_Exact_MarkedCluster_m4_Colab.py")
    ap.add_argument("--output", default=CERT_DEFAULT)
    ap.add_argument("--checkpoint", default=CKPT_DEFAULT)
    ap.add_argument("phase", choices=["freeze", "run", "adjudicate"])
    a = ap.parse_args()
    {"freeze": lambda: stage_freeze(a.engine),
     "run": lambda: stage_run(a.engine, a.output, a.checkpoint),
     "adjudicate": lambda: stage_adjudicate(a.engine, a.output)}[a.phase]()

if __name__ == "__main__":
    main()
