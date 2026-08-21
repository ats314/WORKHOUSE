#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

rm -f \
  CERT_SHELL6_o2_representatives_v2.json \
  CERT_SHELL6_o2_matrix_v2.json \
  shell6_o2_analysis_v2.json \
  shell6_o2_matrix_v2_v1_compatible.json \
  shell6_o2_topology_cache_v2.pkl \
  CERT_SHELL6_o2_exact_channel_certificate_v2.json \
  CERT_SHELL6_shell46_t1_coupling_certificate_v1.json \
  THM_SHELL6_shell46_theorem_v2.md \
  DATA_SHELL6_shell46_t1_o2_diagnostic_scan.csv

python -u ENGINE_SHELL6_o2_symmetry_reduced_v2.py \
  --mode all \
  --representatives CERT_SHELL6_o2_representatives_v2.json \
  --matrix CERT_SHELL6_o2_matrix_v2.json \
  --analysis shell6_o2_analysis_v2.json \
  --term-cache shell6_o2_topology_cache_v2.pkl \
  | tee reproduce_shell6.log

python -u ENGINE_SHELL6_exact_channels_shell46_coupling_v2.py \
  | tee reproduce_exact_channels.log

python -u ENGINE_SHELL6_verify_release.py
echo "ALL SHELL6 V2 REPRODUCTION GATES PASS"
