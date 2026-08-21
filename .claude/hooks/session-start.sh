#!/usr/bin/env bash
# SessionStart hook. Two jobs:
#
#   1. On a remote container, make tests and linters runnable before the agent
#      types anything.
#   2. Everywhere, inject the frontier brief, so a session opens knowing where
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
      [ -d .venv ] && echo "export PATH=\"$(cd .venv/bin && pwd):\$PATH\""
    } >> "$CLAUDE_ENV_FILE"
  fi
fi

# The brief is computed from the ledgers and the suites, so it cannot go stale.
# If the package will not import -- no venv yet, a syntax error mid-edit -- say
# nothing rather than injecting a stale or broken block.
python=python3
[ -x .venv/bin/python ] && python=.venv/bin/python

if brief=$("$python" -m workhouse.cli frontier --brief 2>/dev/null); then
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
{"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "WORKHOUSE — verification layer over a research corpus. The computed frontier brief is UNAVAILABLE (no venv or the package failed to import): run `make bootstrap`, then `workhouse frontier --brief`. Until then: read FRONTIER.md, AGENTS.md, CLAUDE.md before changing anything. Standing traps: never edit theory/ or corpus-import/; never promote either side of C2; exact rationals stay sympy.Rational and floats carry _NUM; never apply a 4**r rescaling; never widen a tolerance."}}
JSON
fi
