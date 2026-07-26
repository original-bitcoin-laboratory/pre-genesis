.PHONY: fetch verify status

fetch:
	./scripts/fetch-artifacts.sh

verify:
	python3 ./scripts/verify-artifacts.py

status:
	@cat docs/STATUS.md
