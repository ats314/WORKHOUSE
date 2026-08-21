#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
RESULTS="$ROOT/results"
rm -rf "$RESULTS"
mkdir -p "$RESULTS"

export PYTHONHASHSEED=0
python -u "$ROOT/src/ENGINE_STRING_su3_tension_support_scan.py" \
  "$RESULTS/support_scan_raw.json" | tee "$RESULTS/support_scan_raw.log"
python -u "$ROOT/src/ENGINE_STRING_canonicalize_raw_outputs.py" \
  "$RESULTS/support_scan_raw.json"
python -u "$ROOT/src/ENGINE_STRING_su3_tension_local.py" \
  "$RESULTS/local_coefficients_raw.json" | tee "$RESULTS/local_coefficients_raw.log"
python -u "$ROOT/src/ENGINE_STRING_su3_tension_sigma4.py" \
  "$RESULTS/sigma4_raw.json" | tee "$RESULTS/sigma4_raw.log"
python -u "$ROOT/src/ENGINE_STRING_su3_tension_physical_verify.py" "$RESULTS" \
  | tee "$RESULTS/physical_verify.log"

python -u "$ROOT/src/ENGINE_STRING_canonicalize_logs.py" "$RESULTS"
python -u "$ROOT/src/ENGINE_STRING_make_manifest.py" "$RESULTS"
echo "ALL CLEAN REPRODUCTION STAGES PASS"
