"""Replay the three preserved finite algebra controls and verify source identity."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

run = Path(__file__).resolve().parent
source = run / "sources/campaign"
records = run / "replay"
records.mkdir(exist_ok=True)
manifest = json.loads((run / "source_manifest.json").read_text(encoding="utf-8"))
results = []
for script, output, count_key in [
    ("residual_verify.py", "residual_checks.json", "passed"),
    ("bg_gaussian_cutoff_check.py", "bg_gaussian_cutoff_checks.json", "checks_passed"),
    ("bg_actual_potential_check.py", "bg_actual_potential_checks.json", "checks_passed"),
]:
    completed = subprocess.run([sys.executable, str(source / script)], cwd=source,
                               text=True, encoding="utf-8", capture_output=True, check=False)
    (records / (script + ".stdout.txt")).write_text(completed.stdout, encoding="utf-8")
    (records / (script + ".stderr.txt")).write_text(completed.stderr, encoding="utf-8")
    result = {"script": "sources/campaign/" + script, "exit_code": completed.returncode,
              "output": "sources/campaign/" + output}
    if completed.returncode == 0:
        result["checks_passed"] = json.loads((source / output).read_text(encoding="utf-8"))[count_key]
    results.append(result)
identity = []
for entry in manifest["sources"]:
    actual = sha256((run / entry["preserved_path"]).read_bytes()).hexdigest()
    identity.append({"path": entry["preserved_path"], "matches_intake_sha256": actual == entry["sha256"]})
record = {"date_utc": datetime.now(timezone.utc).isoformat(), "python": sys.executable,
          "results": results, "total_checks_passed": sum(item.get("checks_passed", 0) for item in results),
          "source_identity": identity,
          "scope": "24 exact finite algebra controls only; operator proofs and actual Wilson bounds have separate scopes."}
(records / "replay_record.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
assert all(item["exit_code"] == 0 for item in results), results
assert record["total_checks_passed"] == 24, record
assert all(item["matches_intake_sha256"] for item in identity), identity
print(json.dumps({"checks_passed": 24, "source_hashes_matched": len(identity)}))
