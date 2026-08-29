#!/usr/bin/env bash
# Single source of truth for "what is this repo made of".
# Prints one stack tag per line: node python rust go ruby tex notebooks
# Used by scripts/bootstrap.sh, scripts/check.sh and CI so they never drift.
set -euo pipefail

root="${1:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"

has() { [ -e "$root/$1" ]; }
any_file() {
  # Bounded-depth search so a big data/ dir can't make this crawl.
  find "$root" -maxdepth 3 -name "$1" \
    -not -path '*/node_modules/*' -not -path '*/.git/*' \
    -not -path '*/.venv/*' -not -path '*/target/*' \
    -print -quit 2>/dev/null | grep -q .
}

has package.json                                   && echo node
{ has pyproject.toml || has requirements.txt || has setup.py; } && echo python
has Cargo.toml                                     && echo rust
has go.mod                                         && echo go
has Gemfile                                        && echo ruby
any_file '*.tex'                                   && echo tex
any_file 'lean-toolchain'                            && echo lean
any_file '*.ipynb'                                 && echo notebooks

exit 0
