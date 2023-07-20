#!/usr/bin/env python3

'''code for grouped boxplot'''

#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('</path/to/infile.csv>')

#-------option 1 using melt for multiple variables----------
# melt dataframe for boxplots
df_melt=pd.melt(df,id_vars=['grp'],var_name='<variable name>', value_name='<value name>')

# grouped boxplot
fig, ax = plt.subplots(1, figsize=(10,5))
sns.boxplot(data=df_melt, x='<variable name>', y='<value name>', hue='grp', palette='dark')
plt.suptitle('<title>', fontweight='bold')
plt.ylabel('<ylabel>', fontweight='bold')
plt.xlabel('<xlabel>')
#plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#-------option 2 single variable----------
'''add annotations for level of significance'''
sns.set_context("notebook")
x=''
y=''
order = ['<x var 1>','x var 2','x var 3']     #define order of x variables
pairs=[('<x var 1>','<x var 2>'), ('<x var 1>','<x var 3>'),('<x var 2>','<x var 3>')]      #define pairs of comparisons
my_cols = {'<x var 1>': 'blue', '<x var 2>': 'orange', '<x var 3>': 'red'}      #define colors for x groups
ax = sns.boxplot(data=df, x=x, y=y, order=order, notch=False, 
                 palette=my_cols, fliersize = 5,
                 flierprops={"marker": "o", 'markerfacecolor':'black', 'markeredgecolor':'black'}, 
                 medianprops={"color": "black"}, 
                 boxprops = {'edgecolor': 'black', 'linewidth': 1},
                 whiskerprops = {"color": "black"},
                 capprops = {"color": "blue"})
#ax2=sns.stripplot(data=df, x=x, y=y, order=order, color='black')   #add stripplot
ax.set_xticklabels(['<x var 1>', '<x var 1>', '<x var 1>'])     #define x tick names
sns.despine()
annot = Annotator(ax, pairs, data=df, x=x, y=y, order=order)
annot.configure(test=None, loc='inside')
annot.set_pvalues([0.04, 0.001, 0.5])       #specify p values for each pair
annot.annotate()
plt.ylabel('', fontweight='bold')       #set ylabel name
plt.xlabel('')      #set xlabel name
plt.tight_layout()
plt.savefig('')
plt.show()