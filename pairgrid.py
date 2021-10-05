#!/usr/local/bin/python3.9
"""
Copyright (C) 2021 Jesse DeSimone, Ph.D.

Change Log
=============
0.0.1 (2021-10-04)
-------------
Initial commit

WARNING: Pairgrid is computationally demanding, not reccommended for large number of predictors
"""

import pandas as pd
import seaborn as sns
import matplotlib as mpl
from scipy import stats

df = pd.read_csv("<path/to/file>")

# define correlation function (spearman or pearson)
def corrfunc(x, y, **kws):
    r, p = stats.pearsonr(x, y)  # use stats.pearsonr for pearson
    ax = plt.gca()
    ax.annotate("r = {:.2f}".format(r),
                xy=(.1, .9), xycoords=ax.transAxes)
    ax.annotate("p = {:.2f}".format(p),
                xy=(.6, .9), xycoords=ax.transAxes)

# Pairgrid
mpl.rcParams['axes.labelsize']=5
g = sns.PairGrid(df, palette=["red"], height=1, aspect=1.5)
g.map_upper(plt.scatter, s=1)
g.map_diag(sns.distplot, kde=False)
g.map_lower(sns.kdeplot, cmap="gist_heat")
g.map_lower(corrfunc)
g.map_upper(corrfunc)

# Pairplot
sns.set_palette(sns.color_palette("Set1", 8))
sns.pairplot(data=df,hue="Outcome",corner=True)
plt.show()
plt.tight_layout()