.PHONY: help bootstrap check quick lint test verify status frontier certified lit catalogue atlas fmt manifest corpus-manifest lean lean-setup corpus-index lock clean paper

help:            ## Show this help
	@grep -hE '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | awk -F':.*?## ' '{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

bootstrap:       ## Install dependencies for whatever stacks this repo contains
	@bash scripts/bootstrap.sh

check:           ## Everything CI runs: lint + tests (~2.5 min)
	@bash scripts/check.sh

quick:           ## The fast inner loop while iterating (~10 s): lint + the invariant tests
	@.venv/bin/ruff check . && .venv/bin/ruff format --check . \
		&& .venv/bin/pytest -q tests/test_invariants.py tests/test_constants.py

lint:            ## Lint only
	@.venv/bin/ruff check . && .venv/bin/ruff format --check .

test:            ## Tests only
	@.venv/bin/pytest -q

verify:          ## Re-derive every exact claim in the corpus
	@.venv/bin/workhouse verify

status:          ## Print the contradiction and gap registers
	@.venv/bin/workhouse status

catalogue:       ## Regenerate the index/ catalogues: claims, symbols, graph
# `workhouse index -w` iterates to a fixpoint itself (some checks read the
# generated graph and print its counts into their own detail lines, so one
# pass can leave claims.jsonl a generation behind); the loop that used to
# live here moved into the command so every caller gets it.
	@.venv/bin/workhouse index -w

atlas:           ## Render the theory graph to atlas.html (a view; never checked in)
	@.venv/bin/workhouse atlas

# Builds the 2026-08-28 edition, not the current master edition, and on
# purpose: that edition's digest in paper/SHA256SUMS is byte-reproducible
# under pdflatex + SOURCE_DATE_EPOCH, which is what makes the pin meaningful.
# The 2026-08-30 master edition is built with Tectonic, which is not a
# dependency of this repository -- see paper/README.md "Rebuilding". Both
# stdlib verifiers run here either way.
paper:           ## Build the 2026-08-28 paper PDF and run both stdlib core verifiers
	@python3 verify_core.py
	@cd paper && python3 verify_core.py \
		&& SOURCE_DATE_EPOCH=1756339200 FORCE_SOURCE_DATE=1 \
		   pdflatex -interaction=nonstopmode master_paper_2026-08-28.tex >/dev/null \
		&& SOURCE_DATE_EPOCH=1756339200 FORCE_SOURCE_DATE=1 \
		   pdflatex -interaction=nonstopmode master_paper_2026-08-28.tex >/dev/null \
		&& SOURCE_DATE_EPOCH=1756339200 FORCE_SOURCE_DATE=1 \
		   pdflatex -interaction=nonstopmode master_paper_2026-08-28.tex >/dev/null \
		&& echo "paper/master_paper_2026-08-28.pdf"


lit:             ## Published work, and which claim each paper bears on
	@.venv/bin/workhouse lit

certified:       ## Regenerate CERTIFIED.md — every checked claim, ranked by tier
	@.venv/bin/workhouse certified --write

frontier:        ## Regenerate FRONTIER.md from the ledgers and the suites
	@.venv/bin/workhouse frontier --write

# Catalogue FIRST. One check reads the generated graph (note coverage), so a
# view rendered before the catalogue pass records that check against the
# previous graph -- on 2026-09-01 that put "1 checks are failing" into a
# committed CERTIFIED.md the moment a new archive was declared. With the
# per-check cache a pass is seconds, so the views are rendered after the
# catalogue has reached its fixpoint, never before.
regen: catalogue frontier certified  ## Every generated file, in one order — the staleness tests stop tripping on partial regens
	@echo "regenerated: index/ FRONTIER.md CERTIFIED.md"

fmt:             ## Auto-format
	@.venv/bin/ruff check --fix . && .venv/bin/ruff format .

manifest:        ## Regenerate theory/SHA256SUMS after a deliberate corpus change
	@.venv/bin/python -c "import hashlib,pathlib; \
	 root=pathlib.Path('theory'); \
	 ns=sorted(str(p.relative_to(root)) for p in root.rglob('*') \
	           if p.is_file() and p.name != 'SHA256SUMS'); \
	 (root/'SHA256SUMS').write_text(''.join( \
	     f'{hashlib.sha256((root/n).read_bytes()).hexdigest()}  {n}' + chr(10) for n in ns)); \
	 print(f'theory/SHA256SUMS: {len(ns)} files')"

lean-setup:      ## Install the T0 toolchain: elan, pinned Lean, mathlib cache (~3 GB)
	@bash scripts/bootstrap-lean.sh

# --wfail because a bare `lake build` EXITS 0 ON A SORRY -- Lean logs
# "declaration uses `sorry`" as a warning, so the line this target prints would
# have gone on asserting "no sorries" while the sorry sat there. That is the
# repository's own failure mode: a claim asserted by a document (here, a
# Makefile echo) rather than computed. Verified by temporarily importing a
# `theorem p : (2:Q) = 2 := by sorry` module: plain build 0, --wfail 1.
# The flag fails on any warning, not just sorry, so it can only over-fail,
# never under-pass -- the safe direction for a tier that means "nothing here
# was left unproved". Python's regex sorry-counter in frontier.py reads the
# source; this reads the elaborator.
#
# A fresh container has no elan, and there `lake build` dies with a bare
# "lake: command not found" -- which reads as a broken Makefile rather than a
# missing toolchain, and has already been reported back as "T0 could not be
# re-run locally". Name the remedy instead. The PATH prefix picks up an
# elan-managed lake without an explicit export, because installing the
# toolchain and then still being told it is absent is the same wrong signal one
# step later.
lean:            ## T0: proof-check the Lean core (needs elan; `make lean-setup` installs it)
	@command -v lake >/dev/null 2>&1 || [ -x "$$HOME/.elan/bin/lake" ] || { \
		echo "make lean: elan is not installed -- run \`make lean-setup\` first" >&2; exit 1; }
	@cd lean && PATH="$$HOME/.elan/bin:$$PATH" lake build --wfail && echo "Lean core: proof-checked, no sorries"

corpus-manifest: ## Regenerate corpus-import/SHA256SUMS after a deliberate corpus change
	@.venv/bin/python -c "import hashlib,subprocess,pathlib; \
	 root=pathlib.Path('corpus-import'); \
	 repo_authored={'SHA256SUMS','CLAUDE.md'}; \
	 ns=[n for n in subprocess.run(['git','ls-files','-z','corpus-import/'],capture_output=True,text=True).stdout.split(chr(0)) if n and pathlib.Path(n).name not in repo_authored]; \
	 ls=[f'{hashlib.sha256(pathlib.Path(n).read_bytes()).hexdigest()}  {pathlib.Path(n).relative_to(root)}' for n in sorted(ns) if pathlib.Path(n).is_file()]; \
	 (root/'SHA256SUMS').write_text(chr(10).join(ls)+chr(10)); \
	 print(f'corpus-import/SHA256SUMS: {len(ls)} files')"

corpus-index:    ## Scan exact rationals across corpus code, certificates and notebooks
	@.venv/bin/python -c "from workhouse import corpus_index as X; \
	 c=X.scan(); p=X.scan(exts=X.PROSE_EXTS); \
	 print('coverage', X.coverage()); \
	 [print(' ', f) for f in X.rational_multiples(c,p)]"

lock:            ## Refresh uv.lock from pyproject.toml
	@uv lock && echo "uv.lock refreshed"

clean:           ## Remove build and cache artifacts
	@rm -rf .pytest_cache .ruff_cache **/__pycache__ dist build *.egg-info
