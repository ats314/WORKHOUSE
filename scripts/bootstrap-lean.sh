#!/usr/bin/env bash
# Install the T0 toolchain: elan, the pinned Lean, and mathlib's build cache.
#
# Kept out of scripts/bootstrap.sh deliberately. `make check` does not compile
# Lean, so folding this into the default bootstrap would make every session and
# every CI run pay a multi-GB mathlib download for a tier they are not going to
# check. This is the opt-in half: `make lean-setup`, and the two network steps
# of the Lean CI job, so the recipe has one definition instead of two that
# drift.
#
# Idempotent: a second run reinstalls nothing and re-verifies the cache.
set -uo pipefail

root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$root" || exit 1

elan_bin="${ELAN_HOME:-$HOME/.elan}/bin"

# Retry the network steps -- both have failed transiently in CI -- but still
# fail closed. A half-installed toolchain that reports success is worse than a
# clean failure, because the next thing to run is a proof check.
retry() {
  local what="$1"; shift
  local i
  for i in 1 2 3; do
    if "$@"; then return 0; fi
    echo "bootstrap-lean: $what attempt $i failed; retrying in $((i * 10))s" >&2
    sleep $((i * 10))
  done
  echo "bootstrap-lean: $what failed after 3 attempts" >&2
  return 1
}

install_elan() {
  curl -fsSL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \
    | sh -s -- -y --default-toolchain none
}

if [ -x "$elan_bin/elan" ]; then
  echo "bootstrap-lean: elan already installed ($("$elan_bin/elan" --version))"
else
  echo "bootstrap-lean: installing elan"
  retry "elan install" install_elan || exit 1
  [ -x "$elan_bin/elan" ] || { echo "bootstrap-lean: elan missing after install" >&2; exit 1; }
fi

export PATH="$elan_bin:$PATH"

# elan reads lean/lean-toolchain and fetches the pinned release on first use;
# lake-manifest.json then pins every dependency revision.
cd lean || exit 1
retry "lake exe cache get" lake exe cache get || exit 1

echo "bootstrap-lean: done — \`make lean\` will now proof-check the T0 core."
