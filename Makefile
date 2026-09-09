# User interface
EXTENTION = png
IMG_DIR = img
FIG_DIR = figures
PY_FILES = $(shell find $(FIG_DIR) -type f -name "Figure*") 
IMG_FILES = $(PY_FILES:$(FIG_DIR)/%.py=$(IMG_DIR)/%.$(EXTENTION))

clean_figures:
	rm -f $(IMG_FILES)
	
figures: $(IMG_FILES)

new-fig:
	@next=$$(ls figures/Figure[0-9][0-9].py 2>/dev/null | grep -oE '[0-9]+' | sort -n | tail -1); \
	next=$$(echo $${next:-0} | sed 's/^0*//'); \
	next=$$(printf "%02d" $$((next + 1))); \
	cp figures/exemple.py "figures/Figure$${next}.py"; \
	echo "Créé : figures/Figure$${next}.py"

$(IMG_DIR)/%.$(EXTENTION): $(FIG_DIR)/%.py
	@echo $@ $<
	python3.11 $< -d 1

clean_all: clean_mpl-template clean_venv

mpl-template: external venv
	cd external && git clone https://github.com/austinorr/mpl-template.git
	@echo "------> Success ! now run :"
	@echo "source venv/bin/activate && make build_mpt-env"

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
