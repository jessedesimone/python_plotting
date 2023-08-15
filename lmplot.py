import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/path/to/csv')

'''this will plit multiple regression lines for each hue'''
plt.style.use('seaborn-colorblind') 
sns.lmplot(data=df, x='', y='', hue='', ci=95, height=7)
plt.axvline(x=0.9, color='black', linestyle = 'dashed')
plt.suptitle('', fontweight='bold')
plt.xlabel('')
plt.ylabel('')
#plt.tight_layout()
plt.show()

'''this will plot a single regression line for multiple hues'''
g = sns.lmplot(x='', y='', hue='', data=df, fit_reg=False, legend=False)
sns.regplot(xx='', y='', data=df, scatter=False, ax=g.axes[0, 0])
plt.xlabel('')
plt.ylabel('')
plt.tight_layout()
plt.show()

#--------use specific rcParams-------

import os
import matplotlib.pyplot as plt
import seaborn as sns
ex={
    'axes.titlesize' : 24,
    'axes.titleweight':   'bold',
    'axes.labelsize' : 24,
    'axes.labelweight': 'bold',
    'xtick.labelsize' : 18,
    'ytick.labelsize' : 18,
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
x='ab42_40'
y='composite_gm_fw'

my_cols = {'plasma-/PET-': 'cyan', 'plasma+/PET-': 'steelblue', 'plasma+/PET+': 'lightslategrey'}
g = sns.lmplot(x=x, y=y, hue='grp', data=df, fit_reg=False, legend=False,
               palette=my_cols, scatter_kws={"s": 100, 'linewidths':1,'edgecolor':'black'})
g=sns.regplot(x=x, y=y, data=df, scatter=False, ax=g.axes[0, 0], line_kws={"color": "black"})
plt.axvline(x=0.160, color='black', linestyle = 'dashed')       #plot vertical line
plt.xlabel('')
plt.ylabel('')
plt.tight_layout()
#plt.savefig('out_file.jpg', dpi=300, bbox_inches='tight')
plt.show()

