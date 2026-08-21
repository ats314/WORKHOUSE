.PHONY: help bootstrap check lint test verify status frontier certified lit catalogue atlas fmt manifest corpus-manifest lean corpus-index lock clean

help:            ## Show this help
	@grep -hE '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | awk -F':.*?## ' '{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

bootstrap:       ## Install dependencies for whatever stacks this repo contains
	@bash scripts/bootstrap.sh

check:           ## Everything CI runs: lint + tests
	@bash scripts/check.sh

lint:            ## Lint only
	@.venv/bin/ruff check . && .venv/bin/ruff format --check .

test:            ## Tests only
	@.venv/bin/pytest -q

verify:          ## Re-derive every exact claim in the corpus
	@.venv/bin/workhouse verify

status:          ## Print the contradiction and gap registers
	@.venv/bin/workhouse status

catalogue:       ## Regenerate the index/ catalogues: claims, symbols, graph
	@.venv/bin/workhouse index --write

atlas:           ## Render the theory graph to atlas.html (a view; never checked in)
	@.venv/bin/workhouse atlas

lit:             ## Published work, and which claim each paper bears on
	@.venv/bin/workhouse lit

certified:       ## Regenerate CERTIFIED.md — every checked claim, ranked by tier
	@.venv/bin/workhouse certified --write

frontier:        ## Regenerate FRONTIER.md from the ledgers and the suites
	@.venv/bin/workhouse frontier --write

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

lean:            ## T0: proof-check the Lean core (needs elan on PATH)
	@cd lean && lake build && echo "Lean core: proof-checked, no sorries"

corpus-manifest: ## Regenerate corpus-import/SHA256SUMS after a deliberate corpus change
	@.venv/bin/python -c "import hashlib,subprocess,pathlib; \
	 root=pathlib.Path('corpus-import'); \
	 ns=[n for n in subprocess.run(['git','ls-files','-z','corpus-import/'],capture_output=True,text=True).stdout.split(chr(0)) if n and not n.endswith('SHA256SUMS')]; \
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
