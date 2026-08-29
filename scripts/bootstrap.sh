#!/usr/bin/env bash
# Install whatever this repo needs to lint and test. Idempotent, non-interactive.
# Safe to run on an empty repo: it simply finds nothing and exits clean.
set -euo pipefail

root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$root"
stacks="$(bash scripts/detect-stack.sh "$root")"

if [ -z "$stacks" ]; then
  echo "bootstrap: no dependency manifests found — nothing to install."
  exit 0
fi

for s in $stacks; do
  case "$s" in
    node)
      echo "bootstrap: node"
      # install (not ci) so the warm container cache is reused between sessions.
      if   [ -f pnpm-lock.yaml ]; then corepack enable >/dev/null 2>&1 || true; pnpm install
      elif [ -f yarn.lock ];      then corepack enable >/dev/null 2>&1 || true; yarn install
      else                             npm install
      fi
      ;;
    python)
      echo "bootstrap: python"
      if command -v uv >/dev/null 2>&1; then
        [ -d .venv ] || uv venv
        # shellcheck disable=SC1091
        . .venv/bin/activate
        # --all-extras: a bare `uv sync` installs only the main dependencies, so
        # ruff and pytest would be missing and check.sh would silently fall back
        # to a system pytest that cannot import the package.
        if   [ -f uv.lock ];           then uv sync --all-extras
        elif [ -f pyproject.toml ];    then uv pip install -e ".[dev]" || uv pip install -e .
        elif [ -f requirements.txt ];  then uv pip install -r requirements.txt
        fi
        if [ -f requirements-dev.txt ]; then uv pip install -r requirements-dev.txt; fi
      else
        python3 -m venv .venv
        # shellcheck disable=SC1091
        . .venv/bin/activate
        python3 -m pip install --upgrade pip
        if [ -f pyproject.toml ];   then pip install -e ".[dev]" || pip install -e .; fi
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi
      fi
      ;;
    rust)  echo "bootstrap: rust";  cargo fetch ;;
    go)    echo "bootstrap: go";    go mod download ;;
    ruby)  echo "bootstrap: ruby";  bundle install ;;
    tex)
      echo "bootstrap: tex"
      if ! command -v pdflatex >/dev/null 2>&1; then
        DEBIAN_FRONTEND=noninteractive apt-get update -qq
        DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
          texlive-latex-base texlive-latex-recommended texlive-latex-extra \
          texlive-fonts-recommended texlive-science texlive-bibtex-extra \
          texlive-extra-utils texlive-pictures latexmk biber \
          poppler-utils latexdiff chktex >/dev/null
      fi
      ;;
    lean)
      echo "bootstrap: lean"
      if ! command -v elan >/dev/null 2>&1; then
        curl -fsSL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \
          | sh -s -- -y --default-toolchain none >/dev/null 2>&1
        export PATH="$HOME/.elan/bin:$PATH"
      fi
      # Build in the lean/ subdir if it has a lakefile.
      lean_dir=$(find "$root" -maxdepth 2 -name 'lean-toolchain' -print -quit 2>/dev/null)
      if [ -n "$lean_dir" ]; then
        lean_dir=$(dirname "$lean_dir")
        (cd "$lean_dir" && lake exe cache get && lake build) >&2
      fi
      ;;
    notebooks) : ;;   # no install step
  esac
done

echo "bootstrap: done (${stacks//$'\n'/ })"
