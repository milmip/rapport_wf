# User interface
EXTENTION = pdf
IMG_DIR = img
FIG_DIR = figures
PY_FILES = $(shell find $(FIG_DIR) -type f -name "Figure*")
IMG_FILES = $(PY_FILES:$(FIG_DIR)/%.py=$(IMG_DIR)/%.$(EXTENTION))
PYTHON = python3
IMG_VIEWER = zathura

#interface
figures_clean:
	rm -f $(IMG_FILES)

figures: $(IMG_FILES)

Figure%: $(FIG_DIR)/Figure%.py
	$(PYTHON) -m $(FIG_DIR).Figure$*
	$(IMG_VIEWER) $(IMG_DIR)/Figure$*.$(EXTENTION)

venv:
	$(PYTHON) -m venv venv
	@echo "------> Success ! now run :"
	@echo "source venv/bin/activate"

venv_installs:
	pip install numpy matplotlib pandas scipy black

venv_clean:
	rm -rf venv

#Under de hoods
$(IMG_DIR)/%.$(EXTENTION): $(FIG_DIR)/%.py
	@echo $@ $<
	$(PYTHON) -m $(FIG_DIR).$*
