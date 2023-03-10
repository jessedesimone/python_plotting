#!/usr/bin/env python3

'''code for grouped boxplot'''

#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('</path/to/infile.csv>')

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