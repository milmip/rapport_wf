import os.path
from config import *
import matplotlib.pyplot as plt

from scipy import constants
from scipy import constants

#format
classic = 17 / (constants.inch * 100), 17 / 1.62  / (constants.inch * 100)
half = 17 / 2 / (constants.inch * 100), 17 / 1.62  / (constants.inch * 100)

def script_name(file):
    return os.path.basename(file)

def figure_name(file):
    return script_name(file).split(".")[0] + "." + EXPORT_FORMAT

def figure_path(file):
    return EXPORT_PATH/figure_name(file)

def make_draft(file):
    plt.figtext(0.0,0.0, "DRAFT", fontdict={
            'family': 'sans-serif',   # ou 'serif', 'monospace'
            'color': 'red',
            'weight': 'bold',         # 'normal', 'bold', 'light', 'heavy', ou un entier 0-1000
            'size': 28,               # taille en points
            'alpha': 0.5,             # transparence (0 = invisible, 1 = opaque)
        })
    plt.figtext(0.0,0.0, script_name(file), fontdict={
            'family': 'sans-serif',   # ou 'serif', 'monospace'
            'size': 14,               # taille en points
            'alpha': 1,             # transparence (0 = invisible, 1 = opaque)
        })
