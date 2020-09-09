doc-create:
	mkdir -p docs && cd docs && sphinx-quickstart

doc:
	cp README.md docs/source/README.md
	cd docs && $(MAKE) html

install:
	pip install -r requirements.txt

