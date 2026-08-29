.PHONY: help bootstrap check quick lint test verify status frontier certified lit catalogue atlas fmt manifest corpus-manifest lean corpus-index lock clean paper

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
# One pass is not always enough, and the shortfall is silent. Some checks READ
# a generated index -- note coverage reads index/graph.jsonl -- so on the pass
# that first adds a node they still see the previous generation, and their
# detail line lands in claims.jsonl one generation stale. The files look
# written, `make check` then fails with "stale; run `make catalogue`", and the
# obvious reading of that message is that the command was never run. Loop to a
# fixpoint instead: the second pass is skipped entirely when nothing moved.
	@n=0; prev=""; \
	while [ $$n -lt 4 ]; do \
		.venv/bin/workhouse index --write; \
		now=`cat index/claims.jsonl index/symbols.jsonl index/graph.jsonl | sha256sum`; \
		[ "$$now" = "$$prev" ] && break; \
		prev=$$now; n=`expr $$n + 1`; \
	done; \
	if [ $$n -ge 4 ]; then echo "catalogue did not converge in 4 passes"; exit 1; fi

atlas:           ## Render the theory graph to atlas.html (a view; never checked in)
	@.venv/bin/workhouse atlas

paper:           ## Build the final-edition PDF and run both stdlib core verifiers
# Each edition carries its OWN SOURCE_DATE_EPOCH, because the digest in
# paper/SHA256SUMS is only reproducible if pdflatex stamps the same time it
# stamped when the pin was taken. 1787961600 is 2026-08-29 00:00 UTC, so the
# final edition's internal creation date matches the date on its title page;
# the 2026-08-28 editions were built with 1756339200, which is 2025-08-28 --
# one year early. Their bytes are pinned evidence and stay as they are, so
# rebuilding them needs their own epoch (see paper/README.md).
	@python3 verify_core.py
	@cd paper && python3 verify_core.py \
		&& SOURCE_DATE_EPOCH=1787961600 FORCE_SOURCE_DATE=1 \
		   pdflatex -interaction=nonstopmode master_paper_2026-08-29.tex >/dev/null \
		&& SOURCE_DATE_EPOCH=1787961600 FORCE_SOURCE_DATE=1 \
		   pdflatex -interaction=nonstopmode master_paper_2026-08-29.tex >/dev/null \
		&& SOURCE_DATE_EPOCH=1787961600 FORCE_SOURCE_DATE=1 \
		   pdflatex -interaction=nonstopmode master_paper_2026-08-29.tex >/dev/null \
		&& echo "paper/master_paper_2026-08-29.pdf"


lit:             ## Published work, and which claim each paper bears on
	@.venv/bin/workhouse lit

certified:       ## Regenerate CERTIFIED.md — every checked claim, ranked by tier
	@.venv/bin/workhouse certified --write

frontier:        ## Regenerate FRONTIER.md from the ledgers and the suites
	@.venv/bin/workhouse frontier --write

regen: frontier certified catalogue  ## Every generated file, in one order — the staleness tests stop tripping on partial regens
	@echo "regenerated: FRONTIER.md CERTIFIED.md index/"

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
