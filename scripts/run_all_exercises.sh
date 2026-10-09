#!/usr/bin/env bash
set -euo pipefail

exercises=(
  "src/01_bell_state.py"
  "src/02_logical_resource_estimate.py"
  "src/03_toffoli_resource_estimate.py"
  "src/04_multicontrol_resource_compare.py"
  "src/05_native_p0_compare.py"
  "src/06_linear_ownership_error.py"
)

for exercise in "${exercises[@]}"; do
  printf '\n==> %s\n' "$exercise"
  python "$exercise"
done
