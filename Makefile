# User interface
clean_all: clean_mpl-template clean_venv

mpl-template: external venv
	cd external && git clone https://github.com/austinorr/mpl-template.git
	@echo "------> Success ! now run : source venv/bin/activate && make build_mpt-env"

build_mpt-env:
	cd external/mpl-template && pip install -e .

clean_mpl-template:
	rm -rf external/mpl-template

venv:
	python3.11 -m venv venv
clean_venv:
	rm -rf venv

external:
	mkdir external
