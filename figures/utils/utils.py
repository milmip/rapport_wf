import os.path
from config import *

def script_name(file):
    return os.path.basename(file)

def figure_name(file):
    return script_name(file).split(".")[0] + "." + EXPORT_FORMAT

def figure_path(file):
    return EXPORT_PATH/figure_name(file)

