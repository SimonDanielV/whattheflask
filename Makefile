flake:
	flake8 wtflask
	flake8 tests

install:
	pip install -e ".[dev]"

develop: install
	python setup.py develop

test:
	pytest --cov=wtflask

check: flake test clean

clean:
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf scikit_lego.egg-info
	rm -rf .ipynb_checkpoints
	rm -rf notebooks/.ipynb_checkpoints

build:
	docker build -t pythoncontainer .

serve:
	hug -f wtflask/web.py

test-gitlab:
	gitlab-runner exec docker test