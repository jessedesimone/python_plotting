#!/usr/bin/env python3

'''
Plot a 2x2 subplot using matplotlib rc parameters
Use specific parameters for seaborn 
'''

#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statannotations.Annotator import Annotator

ex={
    'axes.titlesize' : 24,
    'axes.titleweight':   'bold',
    'axes.labelsize' : 24,
    'axes.labelweight': 'bold',
    'xtick.labelsize' : 18,
    'ytick.labelsize' : 18,
    'boxplot.notch': False,
    'axes.spines.left':   True,
    'axes.spines.bottom': True,
    'axes.spines.top':    False,
    'axes.spines.right':  False,
    'lines.linewidth': 2.275,
    'xtick.major.width': 1.3,
    'ytick.major.width': 1.3,
    'xtick.minor.width': 0.65,
    'ytick.minor.width': 0.65,
    'grid.linewidth': 1.8,
    'lines.linewidth': 2.275,
    'patch.linewidth': 1,
    'lines.markersize': 9.1,
    'lines.markeredgewidth': 0,
    'xtick.major.pad': 9.1,
    'ytick.major.pad': 9.1,
    'ytick.left': True,
    'font.family': ['sans-serif'],
    'font.sans-serif': ['Arial'],
    'xtick.bottom': True
} 

sns.set_theme(context='talk', style='white', rc=ex)
df=pd.read_csv('/Users/jessedesimone/Desktop/data.csv')
#sns.set_context("talk")
#plt.style.use('/Users/jessedesimone/Documents/postdoc_uf/writing/ab4240_v2/scripts/desimone.mplstyle')
x='grp'
order = ['plasma-/PET-', 'plasma+/PET-', 'plasma+/PET+']
pairs=[('plasma-/PET-', 'plasma+/PET-'), ('plasma-/PET-', 'plasma+/PET+'),('plasma+/PET-', 'plasma+/PET+')]
my_cols = {'plasma-/PET-': 'cyan', 'plasma+/PET-': 'steelblue', 'plasma+/PET+': 'lightslategrey'}

#plot subplots
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15,15))
'''plot ax1'''
y1='composite_gm_fw'
sns.boxplot(data=df, x=x, y=y1, order=order, palette=my_cols,
            showfliers=False,
            medianprops={"color": "black"},
            boxprops = {'edgecolor': 'black'},
            whiskerprops = {"color": "black"},
            capprops = {"color": "black"}, 
            ax=ax1)

sns.stripplot(data=df, x=x, y=y1, order=order, palette=my_cols, 
                  size=5, jitter=True, edgecolor="black", linewidth=1,
                  ax=ax1)
'''set ax1 params'''
ax1.set_title(label='Grey Matter')
ax1.set_ylabel('Composite FW')
ax1.set_xlabel('')
ax1.tick_params(axis="x")
ax1.tick_params(axis="y")
annot1 = Annotator(ax1, pairs, data=df, x=x, y=y1, order=order)
annot1.configure(test=None, loc='inside')
annot1.set_pvalues([0.0325, 0.0001, 0.21])
annot1.annotate()

'''plot ax2'''
y2='composite_wm_fw'
sns.boxplot(data=df, x=x, y=y2, order=order, palette=my_cols,
            showfliers=False,
            medianprops={"color": "black"},
            boxprops = {'edgecolor': 'black'},
            whiskerprops = {"color": "black"},
            capprops = {"color": "black"}, 
            ax=ax2)

sns.stripplot(data=df, x=x, y=y2, order=order, palette=my_cols, 
                  size=5, jitter=True, edgecolor="black", linewidth=1,
                  ax=ax2)
'''set ax2 params'''
ax2.set_title(label='White Matter')
ax2.set_ylabel('')
ax2.set_xlabel('')
ax2.tick_params(axis="x")
ax2.tick_params(axis="y")
annot2 = Annotator(ax2, pairs, data=df, x=x, y=y2, order=order)
annot2.configure(test=None, loc='inside')
annot2.set_pvalues([0.1131, 0.0002, 0.1577])
annot2.annotate()

'''plot ax3'''
y3='composite_gm_fat'
sns.boxplot(data=df, x=x, y=y3, order=order, palette=my_cols,
            showfliers=False,
            medianprops={"color": "black"},
            boxprops = {'edgecolor': 'black'},
            whiskerprops = {"color": "black"},
            capprops = {"color": "black"}, 
            ax=ax3)

sns.stripplot(data=df, x=x, y=y3, order=order, palette=my_cols, 
                  size=5, jitter=True, edgecolor="black", linewidth=1,
                  ax=ax3)
'''set ax3 params'''
ax3.set_title(label='')
ax3.set_ylabel('Composite FAt')
ax3.set_xlabel('')
ax3.tick_params(axis="x")
ax3.tick_params(axis="y")
annot3 = Annotator(ax3, pairs, data=df, x=x, y=y3, order=order)
annot3.configure(test=None, loc='inside')
annot3.set_pvalues([0.0056, 0.84, 0.011])
annot3.annotate()

'''plot ax4'''
y4='composite_wm_fat'
sns.boxplot(data=df, x=x, y=y4, order=order, palette=my_cols,
            showfliers=False,
            medianprops={"color": "black"},
            boxprops = {'edgecolor': 'black'},
            whiskerprops = {"color": "black"},
            capprops = {"color": "black"}, 
            ax=ax4)
sns.stripplot(data=df, x=x, y=y4, order=order, palette=my_cols, 
                  size=5, jitter=True, edgecolor="black", linewidth=1,
                  ax=ax4)

'''set ax4 params'''
ax4.set_title(label='')
ax4.set_ylabel('')
ax4.set_xlabel('')
ax4.set_ylim([0.475,0.6])
ax4.tick_params(axis="x")
ax4.tick_params(axis="y")
annot4 = Annotator(ax4, pairs, data=df, x=x, y=y4, order=order)
annot4.configure(test=None, loc='inside')
annot4.set_pvalues([0.0027, 0.99, 0.0254])
annot4.annotate()

#plot and save figure            
plt.savefig('/Users/jessedesimone/Desktop/test.jpg', dpi=600)
plt.show()