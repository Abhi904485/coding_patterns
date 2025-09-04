.PHONY: test coverage clean lint typecheck security format all

# Run all tests
test_with_coverage:
	pytest -v

# Remove caches and coverage files
clean:
	rm -rf .pytest_cache .coverage htmlcov coverage.xml

# Clean pyc 
clean_pycache:
	find . -type d -name "__pycache__" -exec rm -rf {} +

# Lint only (no changes)
lint:
	black --check src tests
	ruff check src tests

# Auto-fix lint issues
lint-fix:
	black src tests
	ruff check --fix src tests

# Type checking
typecheck:
	mypy src tests

# Security scanning
security:
	bandit -r src

# Auto-format using Ruff
format:
	ruff format src tests

# Run everything
all: clean lint-fix typecheck security test_with_coverage clean_pycache
