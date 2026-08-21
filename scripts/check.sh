#!/usr/bin/env bash
# Run this repo's linters and tests. Same entry point locally and in CI.
# Skips a step when its tool or config is absent rather than failing the build.
set -uo pipefail

root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
# No `set -e` here (checks are collected, not fatal), so guard the cd explicitly:
# without this a failed cd would silently run every check in the wrong tree.
cd "$root" || exit 1
stacks="$(bash scripts/detect-stack.sh "$root")"
status=0

run() {
  echo "── $* ──"
  "$@" || status=1
}

for s in $stacks; do
  case "$s" in
    node)
      # Only invoke scripts the package actually declares.
      for target in lint typecheck test; do
        if jq -e --arg t "$target" '.scripts[$t]' package.json >/dev/null 2>&1; then
          run npm run "$target"
        fi
      done
      ;;
    python)
      # shellcheck disable=SC1091  # generated at bootstrap time, absent when linting
      [ -d .venv ] && . .venv/bin/activate
      command -v ruff   >/dev/null 2>&1 && { run ruff check .; run ruff format --check .; }
      # Gate on opt-in config, not on the binary merely being present: an
      # ambient mypy with no project config only produces missing-stub noise.
      if command -v mypy >/dev/null 2>&1 && grep -q '^\[tool.mypy\]' pyproject.toml 2>/dev/null; then
        run mypy .
      fi
      command -v pytest >/dev/null 2>&1 && run pytest -q
      ;;
    rust)
      run cargo fmt --check
      run cargo clippy --all-targets -- -D warnings
      run cargo test
      ;;
    go)
      run go vet ./...
      run go test ./...
      ;;
    ruby)
      command -v rubocop >/dev/null 2>&1 && run bundle exec rubocop
      run bundle exec rake test
      ;;
  esac
done

if [ -z "$stacks" ]; then
  echo "check: no stacks detected — nothing to run."
fi

exit "$status"
