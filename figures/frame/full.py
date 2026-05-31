from config import *

from mpl_template import Template
import matplotlib.pyplot as plt

FIG_SIZE = (8.5, 11) # inches
TBK = [
        #{
        #    "name": "title",
        #    "text": [
        #        {
        #            "s": "Ventes Mensuelles 2024",
        #            "weight": "bold",
        #            "x": 0.5, "y": 0.54,
        #            "va": "baseline", "ha": "center",
        #        },
        #        {
        #            "s": "Rapport Exemple — mpl-template",
        #            "weight": "light",
        #            "x": 0.5, "y": 0.46,
        #            "va": "top", "ha": "center",
        #            "color": (0.4, 0.4, 0.4),
        #        },
        #    ],
        #}, 
    {
        "name": "logo",
        "image": {
            "path": str(EPFL_LOGO),
            "scale": 0.75,
        },
    },
    {
        "name": "project",
        "text": {"s": TP_TITLE, "x": 0.5, "y": 0.5, "va": "center", "ha": "center"},
    },
    {
        "name": "date",
        "text": {"s": DATE, "x": 0.5, "y": 0.5, "va": "center", "ha": "center"},
    },
    {
        "name": "group",
        "text": {"s": GROUP, "weight": "bold", "x": 0.5, "y": 0.5, "va": "center", "ha": "center"},
    },
]

def get_material(script, drft=False):
    report_fig = Template(figsize=FIG_SIZE, scriptname=script, titleblock_content=TBK, draft=drft)
    report_fig.path_text = script
    fig = report_fig.setup_figure()
    
    left, right, top, bottom = report_fig.margins
    main = report_fig.gsfig[
        4 + top : -(report_fig.t_h + bottom + 8),
        8 + left : -(right + 8),]
    return fig, main

