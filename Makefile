build:
	rm -rf dist
	poetry build

lint:
	poetry run flake8 page_loader

package-install:
	pip install --user dist/*.whl

test:
	poetry run pytest --cov=page_loader --cov-report xml tests/

.PHONY: build lint package-install test