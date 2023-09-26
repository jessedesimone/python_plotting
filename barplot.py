#!/usr/bin/env python3

'''
Module for plotting barplot for multiple variables
Designed for lots of variables to plot
'''
#import packages
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MaxNLocator

#read data
path_to_file = '/Users/jessedesimone/Desktop/'
file = 'test.csv'
infile = os.path.join(path_to_file,file)
df = pd.read_csv(infile)

#--------------Option 1 - Matplotlib-------------
#sort values
dff = df.sort_values(by='difference', ascending=True)
dff

plt.style.use('/Users/jessedesimone/env/lib/python3.9/site-packages/matplotlib/mpl-data/stylelib/seaborn-talk.mplstyle')
plt.style.use('/Users/jessedesimone/DeSimone_Github/python_plotting/desimone.mplstyle')
fig, ax = plt.subplots(figsize=(6,12), dpi=300)       #create the figure and axes objects, specify the size and the dots per inches 
bar1 = ax.barh(dff['variable'], dff['difference'], color='red')      #plot bars
# Reformat x-axis label and tick labels
ax.set_xlabel('', fontsize=12, labelpad=10) # No need for an axis label
ax.yaxis.set_label_position("left")
ax.yaxis.set_tick_params(pad=2, labelbottom=True, bottom=True, labelsize=8, labelrotation=0)
# Remove the spines
ax.spines[['right', 'left']].set_visible(False)
# Make the left spine thicker
ax.spines['left'].set_linewidth(1.1)
# Add in red line and rectangle on top
#ax.plot([0.05, 0.9], [0.98, 0.98], transform=fig.transFigure, clip_on=False, color='#E3120B', linewidth=.8)
#ax.add_patch(plt.Rectangle((0.12,.95), 0.1, -0.02, facecolor='#E3120B', transform=fig.transFigure, clip_on=False, linewidth = 0))
plt.ylim(-1,96)
ax.yaxis.set_tick_params(pad=2, labelbottom=True, labelsize=8, labelrotation=0)
# Add in title and subtitle
ax.text(x=0.05, y=.94, s="Grey Matter Free-Water", transform=fig.transFigure, ha='left', fontsize=12, weight='bold', alpha=1)
ax.text(x=0.05, y=.925, s="Aβ plasma+/PET+ versus Aβ plasma+/PET- difference", transform=fig.transFigure, ha='left', fontsize=10, alpha=1)
plt.tight_layout()
#plt.savefig('/Users/jessedesimone/Desktop/fig1.jpg', dpi=300)
plt.show()

#--------------Option 1 - Seaborn-------------
import seaborn as sns
sns.barplot(data=df, x='', y='', palette='dark', 
            capsize=.4, errcolor=".5",
            linewidth=3, edgecolor=".5")
sns.despine()
plt.ylabel('', fontweight='bold')       #set ylabel name
plt.xlabel('')      #set xlabel name
plt.tight_layout()
plt.savefig('')
plt.show()






