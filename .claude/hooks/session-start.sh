#!/usr/bin/env bash
# SessionStart hook — prepares a Claude Code on the web container so that
# tests and linters are runnable the moment the session opens.
#
# Runs synchronously: the session waits for it, which costs a few seconds of
# startup but guarantees no race where the agent runs `pytest` before the
# venv exists. Switch to async by emitting {"async": true} as the first line.
set -euo pipefail

# Local machines already have their own setup; only shape the remote container.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(pwd)}"

bash scripts/bootstrap.sh

# Persist env for the rest of the session.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  {
    echo 'export PYTHONDONTWRITEBYTECODE=1'
    echo 'export PIP_DISABLE_PIP_VERSION_CHECK=1'
    # Put the project venv first so `python`/`pytest` resolve without activation.
    # Resolve the path now: the env file is sourced from an arbitrary cwd later,
    # so a literal $PWD here would point at the wrong directory.
    [ -d .venv ] && echo "export PATH=\"$(cd .venv/bin && pwd):\$PATH\""
  } >> "$CLAUDE_ENV_FILE"
fi
