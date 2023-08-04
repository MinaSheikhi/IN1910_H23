.PHONY: clean clean-ipynb clean-pyc clean-build docs help upgrade
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

docs: ## Build book
	jupyter-book build -W book
	touch book/_build/html/.nojekyll


show:  ## Open index page
	open book/_build/html/index.html

clean: clean-build clean-pyc clean-ipynb clean-pytest-cache clean-ipynb clean-mypy-cache ## remove all build, test, coverage and Python artifacts

checkout-pages:
	git checkout gh-pages
	git merge master -m "Merge master"

gh-pages-deploy: checkout-pages docs   ## Deploy to github pages
	git checkout gh-pages
	git add -f book/_build/html && git commit -m "Add html docs"
	git subtree push --prefix book/_build/html origin gh-pages
	git checkout master

update-prod:  ## check existing files in H21 repo if there is a diff update IN1910_H21
	python scripts/synch_dev_prod.py prod

update-dev:  ## check existing files in H21 repo if there is a diff update IN1910_dev
	python scripts/synch_dev_prod.py dev

move-to-prod: ## move file or folder to prod-repo, given path
	cp -R $(path) ../IN1910_H22/$(path)

move-slides-to-prod: ## move file or folder in book/docs/slides/
	cp -R book/docs/slides/$(path) ../IN1910_H22/book/docs/slides/$(path)

check-prod-dev-diff:  ## Check diff between H21 repo and dev repo
	python scripts/synch_dev_prod.py dev --dry-run

clean-build: ## remove build artifacts
	rm -fr book/_build/

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-pytest-cache: ## Remove pytest cache
	find . -name '.pytest_cache' -exec rm -fr {} +

clean-ipynb:  ## remove notebook artifacts
	find . -name '.ipynb_checkpoints' -exec rm -fr {} +

clean-mypy-cache:  ## remove pytest cache
	find . -name '.mypy_cache' -exec rm -fr {} +
