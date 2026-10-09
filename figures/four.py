from .config import *
from .utils import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.serif": ["Latin Modern Roman"]
        })


#############################################
#########   Figure config           #########
#############################################

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2,2, figsize=classic, constrained_layout=True) #classic or half
make_draft(__file__)            #uncomment when needed

#plt.subplots_adjust(
#    left=0.1,
#    right=0.95,
#    top=0.92,
#    bottom=0.1,
#    wspace=0.3,
#    hspace=0.4)
#############################################
#########   Edit the mpl fig here   #########
#############################################

x = np.linspace(-1, 1, 50)
y = x**2

## Limits ####
xlim0 = (0, 1)
ylim0 = (0, 1)
xlim1 = (0, 1)
ylim1 = (0, 1)
xlim2 = (0, 1)
ylim2 = (0, 1)
xlim3 = (0, 1)
ylim3 = (0, 1)

ax0.set(xlim=xlim0, ylim=ylim0)
ax1.set(xlim=xlim1, ylim=ylim1)
ax2.set(xlim=xlim2, ylim=ylim2)
ax3.set(xlim=xlim3, ylim=ylim3)
#
##
#### Ticks ####
##
#ax0.set_xticks(np.linspace(xlim[0], xlim[1], num_ticks_x), labels=[], minor=False)
#ax0.set_yticks(np.linspace(ylim[0], ylim[1], num_ticks_y), minor=False)
#
#ax1.set_xticks(np.linspace(xlim[0], xlim[1], num_ticks_x), labels=[], minor=False)
#ax1.set_yticks(np.linspace(ylim[0], ylim[1], num_ticks_y), labels=[], minor=False)
#
#ax2.set_xticks(np.linspace(xlim[0], xlim[1], num_ticks_x), minor=False)
#ax2.set_yticks(np.linspace(ylim[0], ylim[1], num_ticks_y), minor=False)
#
#ax3.set_xticks(np.linspace(xlim[0], xlim[1], num_ticks_x), minor=False)
#ax3.set_yticks(np.linspace(ylim[0], ylim[1], num_ticks_y), labels=[], minor=False)
#
## Scale ####
#ax0.set_xscale("linear")
#ax1.set_xscale("linear")
#ax2.set_xscale("linear")
#ax3.set_xscale("linear")
#
## Box ####
#ax0.spines["top"].set_visible(False)
#ax0.spines["right"].set_visible(False)
#ax1.spines["top"].set_visible(False)
#ax1.spines["top"].set_visible(False)
#ax2.spines["top"].set_visible(False)
#ax2.spines["top"].set_visible(False)
#ax3.spines["right"].set_visible(False)
#ax3.spines["right"].set_visible(False)
#
## Automatic minor ticks ####
#ax0.minorticks_on()
#ax1.minorticks_on()
#ax2.minorticks_on()
#ax3.minorticks_on()
#
## Ticks params ####
#ax0.tick_params(axis="both", which="minor", length=0, grid_alpha=0.3)
#ax1.tick_params(axis="both", which="minor", length=0, grid_alpha=0.3)
#ax2.tick_params(axis="both", which="minor", length=0, grid_alpha=0.3)
#ax3.tick_params(axis="both", which="minor", length=0, grid_alpha=0.3)
#
#ax0.tick_params(axis="x", which="major", length=0)
#ax0.tick_params(axis="y", which="major")
#
#ax1.tick_params(axis="x", which="major", length=0)
#ax1.tick_params(axis="y", which="major", length=0)
#
#ax2.tick_params(axis="x", which="major")
#ax2.tick_params(axis="y", which="major")
#
#ax3.tick_params(axis="x", which="major")
#ax3.tick_params(axis="y", which="major", length=0)
#
#
##ax.tick_params(axis='x', which='minor', direction='in',
##               labelrotation=0,
##               length=6, width=2, colors='b',
##               grid_color='b', grid_alpha=0.5, grid_linestyle=':')
#
#
#ax0.grid(True, which="both", axis="both")
#ax1.grid(True, which="both", axis="both")
#ax2.grid(True, which="both", axis="both")
#ax3.grid(True, which="both", axis="both")
#
##
#### Suplies ####
##
## Lines ####
# ax0.axhline(y=1.0, ls="--", color="black")
# ax0.axvline(x=0.0, ls="-", color="grey")
# ax0.axline(xy1=(0,0), slope=1, ls="--", color="black")
#
## Annotation ####
# ax0.annotate("extrema", (2,4))
# ax0.annotate("extrema", (0,0), xytext=(0.2, 0.5), arrowprops={'arrowstyle': '->'})
#
## Text ####
# ax0.text(
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
# )
#
##
#### Label ####
##
## Axis label ####
#ax0.set_xlabel("")
#ax0.set_ylabel("")
#
#ax1.set_xlabel("")
#ax1.set_ylabel("")
#
#ax2.set_xlabel("")
#ax2.set_ylabel("")
#
#ax3.set_xlabel("")
#ax3.set_ylabel("")
#
## Title ####
ax0.set_title("(a)")
ax1.set_title("(b)")
ax2.set_title("(c)")
ax3.set_title("(d)")
#
## Data legend ####
# ax0.legend() # add this past the .plot / .scatter /  ect.
# fig.legend() # regroup for all plots
#
ax0.plot(x,y)
ax1.plot(x,y)
ax2.plot(x,y)
ax3.plot(x,y)

#############################################
#############################################
#############################################

fig.savefig(figure_path(__file__), dpi=150, format=EXPORT_FORMAT, bbox_inches=None)
