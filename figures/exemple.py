from config import *
from utils.utils import script_name, figure_path
from frame import get_material

import matplotlib.pyplot as plt
import numpy as np

#############################################
#########   Figure config           #########
#############################################
temp_id = 0 # 0 half, 1 full
draft=True
#############################################

fig, main = get_material(script_name(__file__), temp_id, draft)
ax0 = fig.add_subplot(main)

#############################################
#########   Edit the mpl fig here   #########
#############################################

x = np.linspace(-1, 1, 50)
y = x**2

## Limits ####
#xlim = (-1,1)
#ylim = (-1,1)
#ax0.set(xlim=xlim, ylim=ylim)
#
##
#### Ticks ####
##
#ax0.set_xticks([0, 1], labels=[], minor=False)
#
## Scale ####
#ax0.set_xscale("linear")
#
## Automatic minor ticks ####
#ax0.minorticks_on()
#
## Ticks params ####
#ax0.tick_params(axis='x', which='major', direction='in', 
#                labelrotation=0, 
#                length=6, width=2, colors='r', 
#                grid_color='r', grid_alpha=0.5, grid_linestyle=':')
#ax0.tick_params(axis='x', which='minor', direction='in', 
#                labelrotation=0, 
#                length=6, width=2, colors='b', 
#                grid_color='b', grid_alpha=0.5, grid_linestyle=':')
#
#
#ax0.grid(True, which='major', axis='both')
#
##
#### Suplies ####
##
## Lines ####
#ax0.axhline(y=1.0, ls="--", color="black")
#ax0.axvline(x=0.0, ls="-", color="grey")
#ax0.axline(xy1=(0,0), slope=1, ls="--", color="black")
#
## Annotation ####
#ax0.annotate("extrema", (2,4))
#ax0.annotate("extrema", (0,0), xytext=(0.2, 0.5), arrowprops={'arrowstyle': '->'})
#
## Text ####
#ax0.text(
#    -0.5, 0,
#    "Titre",
#    fontsize=16,
#    fontweight='bold',
#    fontstyle='italic',
#    color='darkblue',
#    ha='center',
#    va='top',
#    rotation=0,
#    alpha=0.9,
#    family='serif',
#    bbox=dict(
#        boxstyle="round,pad=0.4",
#        facecolor="lightyellow",
#        alpha=0.5,
#        edgecolor="black",
#        linewidth=1
#    )
#)
#
##
#### Label ####
##
## Axis label ####
#ax0.set_xlabel("Time (s)")
#ax0.set_ylabel("s1 and s2")
#
## Title ####
#fig.suptitle("Titre")
#
## Data legend ####
#ax0.legend() # add this past the .plot / .scatter /  ect.
#fig.legend() # regroup for all plots
#
ax0.plot(x,y, label="parabola")
#############################################
#############################################
#############################################

fig.savefig(figure_path(__file__), dpi=150, format=EXPORT_FORMAT, bbox_inches=None)
