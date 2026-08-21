.PHONY: help bootstrap check lint test verify status fmt manifest lock clean

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

fmt:             ## Auto-format
	@.venv/bin/ruff check --fix . && .venv/bin/ruff format .

manifest:        ## Regenerate theory/SHA256SUMS after a deliberate corpus change
	@cd theory && sha256sum *.md > SHA256SUMS && echo "theory/SHA256SUMS regenerated:" && cat SHA256SUMS

lock:            ## Refresh uv.lock from pyproject.toml
	@uv lock && echo "uv.lock refreshed"

clean:           ## Remove build and cache artifacts
	@rm -rf .pytest_cache .ruff_cache **/__pycache__ dist build *.egg-info
