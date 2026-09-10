from config import *

from mpl_template import Template
import matplotlib.pyplot as plt

TB_LST = [
[
    {
        "span": [0, 4, 0, 16],
        "name": "title",
        "text": {
                    "ha": "center",
                    "s": "S-PH, TP_1",
                    "va": "center",
                    "x": 0.5,
                    "y": 0.5,
                },
    },
    {
        "span": [0, 4, 16, 32],
        "name": "group",
        "text": {
                    "ha": "center",
                    "s": "Gr. 3",
                    "va": "center",
                    "weight": "bold",
                    "x": 0.5,
                    "y": 0.5,
                },
    },
],
[
    {
        "span": [0, 4, 0, 16],
        "name": "title",
        "text": {
                    "ha": "center",
                    "s": "S-PH, TP_1",
                    "va": "center",
                    "x": 0.5,
                    "y": 0.5,
                },
    },
    {
        "span": [4, 8, 0, 8],
        "name": "group",
        "text": {
                    "ha": "center",
                    "s": "Gr. 3",
                    "va": "center",
                    "weight": "bold",
                    "x": 0.5,
                    "y": 0.5,
                },
    },
    {
        "span": [4, 8, 8, 16],
        "name": "logo",
        "image": {
            "path": str(EPFL_LOGO),
            "scale": 0.8,
            "axes": {
                "zorder": 101,
            },
        },
    },
]
]
FIG_SIZE_LST = [(8.5, 5.5), (8.5, 11)] # inches
TB_COLS_LST = [(24,0), (16,0)]
TB_ROWS_LST = [(4,0), (4,4,0)]
MARGIN_lST = [(4, 6, 8, 8), (4, 8, 8, 8)]

def get_material(script, template_id=0, drft=True): 

    report_fig = Template(figsize=FIG_SIZE_LST[template_id],
                                   scriptname=script,
                                   titleblock_content=TB_LST[template_id],
                                   draft=drft, 
                                   titleblock_cols=TB_COLS_LST[template_id],
                                   titleblock_rows=TB_ROWS_LST[template_id])
    report_fig.path_text = script
    fig = report_fig.setup_figure()
    
    left, right, top, bottom = report_fig.margins
    top_sft, bottom_sft, left_sft, right_sft = MARGIN_lST[template_id]
    main = report_fig.gsfig[
        top_sft + top : -(report_fig.t_h + bottom + bottom_sft),
        left_sft + left : -(right + right_sft),]
    return fig, main

