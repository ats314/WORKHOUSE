#!/usr/bin/env bash
# SessionStart hook. Two jobs:
#
#   1. On a remote container, make tests and linters runnable before the agent
#      types anything.
#   2. Everywhere, inject the shared graph protocol notice, so a session opens knowing where
#      authority lives instead of inferring it from whichever file it opens
#      first. That inference is the failure mode this repository exists to
#      prevent, and it is cheapest to prevent at second zero.
#
# stdout is reserved for the hook's JSON. Everything else goes to stderr.
set -euo pipefail

cd "${CLAUDE_PROJECT_DIR:-$(pwd)}"

# Local machines already have their own setup; only shape the remote container.
if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ]; then
  bash scripts/bootstrap.sh >&2 || true

  # Persist env for the rest of the session.
  if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    {
      echo 'export PYTHONDONTWRITEBYTECODE=1'
      echo 'export PIP_DISABLE_PIP_VERSION_CHECK=1'
      # Put the project venv first so `python`/`pytest` resolve without
      # activation. Resolve the path now: the env file is sourced from an
      # arbitrary cwd later, so a literal $PWD here would point elsewhere.
      # bin/ on POSIX, Scripts/ on Windows -- see the probe below for why
      # naming only one of them is a silent failure rather than a loud one.
      for d in .venv/bin .venv/Scripts; do
        [ -d "$d" ] && echo "export PATH=\"$(cd "$d" && pwd):\$PATH\"" && break
      done
    } >> "$CLAUDE_ENV_FILE"
  fi
fi

# Startup is a small shared protocol notice. It does not execute checks or
# silently replace a missing task briefing with a different command.
# Probe both POSIX and native Windows environments.
python=python3
for candidate in .venv/bin/python .venv/Scripts/python.exe; do
  [ -x "$candidate" ] && python=$candidate && break
done

if brief=$("$python" -m workhouse.cli brief --startup 2>/dev/null); then
  "$python" - "$brief" <<'PY'
import json, sys
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": sys.argv[1],
    }
}))
PY
else
  # A degraded session is the one that needs orientation most. Emit a static
  # minimal brief instead of silence: where authority lives, that the
  # environment is broken, and the traps that do not need a working venv.
  cat <<'JSON'
{"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "WORKHOUSE: the graph briefing is UNAVAILABLE (environment missing or package import failed). Read README.md, INDEX.md, AGENTS.md and CLAUDE.md in the selected checkout. On the maintainer workstation the active checkout is C:/WORKHOUSE/REPO; older archive checkouts remain preserved sources. Follow CONTRIBUTING.md to restore the environment, then run uv run --no-sync workhouse brief --startup. Read docs/theory_graph_protocol.md and retain a task-specific workhouse brief ID --json snapshot before mathematical integration. Inspect local changes and live GitHub history before declaring a result missing. Preserve original sources and prior navigation bytes; do not delete, reset or relocate work. Use current_research.md under docs and the derivation proof map for current scope. Keep mathematical status, evidence and machine tier separate; accept valid novel arguments under their hypotheses. Exact rationals stay exact, floats retain _NUM, no 4**r rescaling, and no tolerance weakening. Follow the current ledger resolutions instead of reopening a dated dispute."}}
JSON
fi
