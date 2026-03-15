PYTHON ?= python

.PHONY: install test lint format api

install:
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m ruff check .

format:
	$(PYTHON) -m black .

api:
	$(PYTHON) -m uvicorn api.app.main:app --host 127.0.0.1 --port 8000 --reload