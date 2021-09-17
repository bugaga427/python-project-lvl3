build:
	rm -rf dist
	poetry build

package-install:
	pip install --user dist/*.whl

test:
	poetry run pytest --cov=page_loader --cov-report xml tests/

.PHONY: build install test