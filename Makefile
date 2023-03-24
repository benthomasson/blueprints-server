

.PHONY: run test


run:
	uvicorn blueprints_server.app:app --reload --port 8000 --host 127.0.0.1 --log-level debug


test:
	pytest -v 
