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

#--------use desimone.mplstype-------

import os
import matplotlib.pyplot as plt
os.chdir('/set/root/directory')
df=pd.read_csv('input_file.csv')
sns.set_context("talk")
plt.style.use('desimone.mplstyle')
x=''
y=''

my_cols = {'grp1': 'cyan', 'grp2': 'steelblue', 'grp3': 'lightslategrey'}
g = sns.lmplot(x=x, y=y, hue='grp', data=df, fit_reg=False, legend=False,
               palette=my_cols, scatter_kws={"s": 100, 'linewidths':1,'edgecolor':'black'})
g=sns.regplot(x=x, y=y, data=df, scatter=False, ax=g.axes[0, 0], line_kws={"color": "black"})
plt.axvline(x=0.160, color='black', linestyle = 'dashed')       #plot vertical line
plt.xlabel('')
plt.ylabel('')
plt.tight_layout()
plt.savefig('out_file.jpg', dpi=300, bbox_inches='tight')
plt.show()